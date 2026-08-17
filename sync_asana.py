"""
sync_asana.py — Pull Asana → restricciones_data.json → reconstruye index.html
Diseñado para correr en GitHub Actions y en local.
Requiere: ASANA_TOKEN en variable de entorno.
"""
import os, sys, json, time, subprocess, argparse
from pathlib import Path
import requests

HERE        = Path(__file__).parent
DATA_FILE   = HERE / "restricciones_data.json"
GID_FILE    = HERE / "asana_task_gids.json"
BUILD_GUIDE = HERE / "build_guide.py"
PYTHON      = sys.executable

PROJECT_GID = "1217441236213348"
BASE        = "https://app.asana.com/api/1.0"

SECTION_TO_STAGE = {
    "Sin Iniciar":           "SIN_INICIAR",
    "ELE — Elegir":          "ELE",
    "COT — Cotización":      "COT",
    "OC — Orden de Compra":  "OC",
    "PRO — Proceso":         "PRO",
    "PRELI — Preliquidación":"PRELI",
    "SIT — En Sitio":        "SIT",
}
STAGE_TO_SECTION = {v: k for k, v in SECTION_TO_STAGE.items()}

TOKEN = os.environ.get("ASANA_TOKEN", "").strip()

def hdrs():
    if not TOKEN:
        print("ERROR: falta ASANA_TOKEN"); sys.exit(1)
    return {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json",
            "Content-Type": "application/json"}

def get_paged(url, params=None):
    results, offset = [], None
    while True:
        p = dict(params or {}, limit=100)
        if offset: p["offset"] = offset
        r = requests.get(f"{BASE}{url}", headers=hdrs(), params=p)
        r.raise_for_status()
        data = r.json()
        results.extend(data["data"])
        npt = data.get("next_page")
        if not npt: break
        offset = npt["offset"]
    return results

def post_api(url, body):
    r = requests.post(f"{BASE}{url}", headers=hdrs(), json={"data": body})
    r.raise_for_status()
    return r.json()["data"]


def pull():
    print("── PULL: Asana → JSON → HTML")

    sections = get_paged(f"/projects/{PROJECT_GID}/sections",
                         {"opt_fields": "gid,name"})
    sec_map = {s["gid"]: SECTION_TO_STAGE.get(s["name"]) for s in sections}
    sec_map = {k: v for k, v in sec_map.items() if v}
    print(f"   Secciones: {len(sec_map)}")

    print("   Leyendo tareas...")
    tasks = get_paged("/tasks",
        {"project": PROJECT_GID,
         "opt_fields": "gid,name,due_on,memberships.section.gid,completed,custom_fields,custom_fields.name,custom_fields.multi_enum_values,custom_fields.multi_enum_values.name"})
    print(f"   Tareas: {len(tasks)}")

    with open(DATA_FILE, encoding="utf-8") as f:
        restricciones = json.load(f)

    # Índice (material, frente) → restricción para buscar por tareas Principal
    by_mat_frente = {}
    for r in restricciones:
        key = (r.get("material", "").strip(), r.get("frente", "").strip())
        by_mat_frente[key] = r

    # Pares (material, frente) cubiertos por alguna tarea Principal activa
    covered_pairs = set()

    changes = 0
    for task in tasks:
        if task.get("completed"):
            continue
        name = task.get("name", "")

        # Los frentes vienen del custom field "Ubicación" (multi-select)
        ubicacion = next(
            (cf for cf in (task.get("custom_fields") or []) if cf.get("name") == "Ubicación"),
            None
        )
        frente_names = {opt["name"] for opt in (ubicacion.get("multi_enum_values") or [])} if ubicacion else set()
        if not frente_names:
            continue

        material = name.replace("(Principal)", "").strip()

        for frente in frente_names:
            covered_pairs.add((material, frente))

        new_stage = None
        for m in (task.get("memberships") or []):
            sec_gid = (m.get("section") or {}).get("gid")
            s = sec_map.get(sec_gid)
            if s:
                new_stage = s
                break
        if not new_stage:
            continue

        due = task.get("due_on")
        for frente in frente_names:
            r = by_mat_frente.get((material, frente))
            if not r:
                continue
            rid = r["id"]
            if r.get("estado") != new_stage:
                print(f"   R-{rid:03d} [{material} / {frente}]: {r.get('estado')} → {new_stage}")
                r["estado"] = new_stage
                changes += 1
            if due and r.get("fechaCompromiso") != due:
                print(f"   R-{rid:03d}: fecha → {due}")
                r["fechaCompromiso"] = due
                changes += 1

    # Eliminar restricciones no cubiertas por ninguna tarea Principal activa
    # (solo si Asana devolvió al menos alguna tarea Principal para evitar borrado accidental)
    if covered_pairs:
        before = len(restricciones)
        restricciones = [
            r for r in restricciones
            if (r.get("material", "").strip(), r.get("frente", "").strip()) in covered_pairs
        ]
        removed = before - len(restricciones)
        if removed > 0:
            print(f"   Eliminadas {removed} restricciones sin tarea Principal en Asana")
            changes += removed

    print(f"   Cambios: {changes}")
    if changes == 0:
        print("   Sin cambios.")
        return False

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(restricciones, f, ensure_ascii=False, indent=2)

    result = subprocess.run([PYTHON, str(BUILD_GUIDE)], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"   ERROR build: {result.stderr[:500]}"); return False
    print(f"   {result.stdout.strip()}")
    return True


def push(state_file: Path):
    print(f"── PUSH: {state_file.name} → Asana")
    with open(state_file, encoding="utf-8-sig") as f:
        exported = json.load(f)

    status_overrides = exported.get("status", {})
    if not status_overrides:
        print("   Sin cambios de etapa."); return

    with open(GID_FILE, encoding="utf-8") as f:
        gid_data = json.load(f)
    gid_map = {int(k): v for k, v in gid_data["tasks"].items()}

    sections = get_paged(f"/projects/{PROJECT_GID}/sections", {"opt_fields": "gid,name"})
    sec_name_to_gid = {s["name"]: s["gid"] for s in sections}

    updates = 0
    for rid_str, new_stage in status_overrides.items():
        rid = int(rid_str)
        task_gid = gid_map.get(rid)
        if not task_gid: continue
        section_name = STAGE_TO_SECTION.get(new_stage)
        section_gid  = sec_name_to_gid.get(section_name) if section_name else None
        if not section_gid:
            print(f"   R-{rid:03d}: sección no encontrada, omitida"); continue
        try:
            post_api(f"/sections/{section_gid}/addTask", {"task": task_gid})
            print(f"   R-{rid:03d} → {new_stage}")
            updates += 1
            time.sleep(0.12)
        except Exception as e:
            print(f"   ERROR R-{rid:03d}: {e}")

    dates = exported.get("dates", {})
    for rid_str, new_date in dates.items():
        if not new_date: continue
        rid = int(rid_str)
        task_gid = gid_map.get(rid)
        if not task_gid: continue
        try:
            r = requests.put(f"{BASE}/tasks/{task_gid}", headers=hdrs(),
                             json={"data": {"due_on": new_date}})
            r.raise_for_status()
            time.sleep(0.12)
        except Exception as e:
            print(f"   ERROR fecha R-{rid:03d}: {e}")

    print(f"   Push completo: {updates} tareas actualizadas")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pull", action="store_true")
    ap.add_argument("--push", metavar="FILE")
    args = ap.parse_args()
    if not args.pull and not args.push:
        ap.print_help(); sys.exit(0)
    if args.pull:
        pull()
    if args.push:
        push(Path(args.push))
    print("Sync completado:", time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
