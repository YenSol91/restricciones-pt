"""
create_asana_tasks.py
Crea las 168 restricciones como tareas individuales en el proyecto de Asana.
Ejecutar localmente con ASANA_TOKEN en la variable de entorno.
Si ya existe asana_task_gids.json, salta las tareas ya creadas (reanudable).

Uso:
  $env:ASANA_TOKEN = "tu_token"
  py create_asana_tasks.py
"""
import os, sys, json, time
from pathlib import Path
import requests

HERE        = Path(__file__).parent
DATA_FILE   = HERE / "restricciones_data.json"
GID_FILE    = HERE / "asana_task_gids.json"

PROJECT_GID = "1217441236213348"
BASE        = "https://app.asana.com/api/1.0"

SECTION_TO_STAGE = {
    "Sin Iniciar":            "SIN_INICIAR",
    "ELE — Elegir":           "ELE",
    "COT — Cotización":       "COT",
    "OC — Orden de Compra":   "OC",
    "PRO — Proceso":          "PRO",
    "PRELI — Preliquidación": "PRELI",
    "SIT — En Sitio":         "SIT",
}
STAGE_NORM = {
    "ABIERTA": "SIN_INICIAR", "PENDIENTE": "SIN_INICIAR",
    "EN GESTIÓN": "ELE", "EN PROCESO": "ELE",
    "RESUELTA": "SIT", "TERMINADA": "SIT",
    "TRA": "PRELI",
}
VALID_STAGES = set(SECTION_TO_STAGE.values())

TOKEN = os.environ.get("ASANA_TOKEN", "").strip()
if not TOKEN:
    print("ERROR: define ASANA_TOKEN antes de correr el script.")
    print('  PowerShell: $env:ASANA_TOKEN = "tu_token"')
    sys.exit(1)

HDRS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get(url, params=None):
    r = requests.get(f"{BASE}{url}", headers=HDRS, params=params)
    r.raise_for_status()
    return r.json()["data"]


def post(url, body):
    r = requests.post(f"{BASE}{url}", headers=HDRS, json={"data": body})
    r.raise_for_status()
    return r.json()["data"]


def normalize_stage(estado):
    s = STAGE_NORM.get(estado, estado)
    return s if s in VALID_STAGES else "SIN_INICIAR"


def build_notes(r):
    lines = []
    if r.get("tipo"):          lines.append(f"Tipo: {r['tipo']}")
    if r.get("frente"):        lines.append(f"Frente: {r['frente']}")
    if r.get("zona"):          lines.append(f"Zona: {r['zona']}")
    if r.get("material"):      lines.append(f"Material: {r['material']}")
    if r.get("prioridad"):     lines.append(f"Prioridad: {r['prioridad']}")
    if r.get("riesgo"):        lines.append(f"Riesgo: {r['riesgo']}")
    if r.get("impactoDias"):   lines.append(f"Impacto: {r['impactoDias']} días")
    if r.get("actividadBloqueada"):
        lines.append(f"Actividad bloqueada: {r['actividadBloqueada']}")
    if r.get("descripcion"):   lines.append(f"\n{r['descripcion']}")
    if r.get("accion"):        lines.append(f"\nAcción requerida: {r['accion']}")
    return "\n".join(lines)


def main():
    # Cargar GIDs existentes (para poder reanudar si se interrumpe)
    existing = {}
    if GID_FILE.exists():
        with open(GID_FILE, encoding="utf-8") as f:
            existing = {int(k): v for k, v in json.load(f).get("tasks", {}).items()}
        print(f"GIDs existentes: {len(existing)}")

    with open(DATA_FILE, encoding="utf-8") as f:
        restricciones = json.load(f)

    # Obtener secciones del proyecto
    sections = get(f"/projects/{PROJECT_GID}/sections", {"opt_fields": "gid,name"})
    stage_to_sec = {}
    for s in sections:
        stage = SECTION_TO_STAGE.get(s["name"])
        if stage:
            stage_to_sec[stage] = s["gid"]
    print(f"Secciones encontradas: {list(stage_to_sec.keys())}\n")

    new_gids = dict(existing)
    created = 0
    skipped = 0
    errors = 0

    for r in restricciones:
        rid = r["id"]
        if rid in existing:
            skipped += 1
            continue

        stage = normalize_stage(r.get("estado"))
        sec_gid = stage_to_sec.get(stage, stage_to_sec.get("SIN_INICIAR"))

        try:
            # Crear tarea
            task = post("/tasks", {
                "name": r.get("titulo", f"Restricción R-{rid:03d}"),
                "notes": build_notes(r),
                "projects": [PROJECT_GID],
                **({"due_on": r["fechaCompromiso"]} if r.get("fechaCompromiso") else {}),
            })
            task_gid = task["gid"]

            # Mover a la sección correcta
            if sec_gid:
                post(f"/sections/{sec_gid}/addTask", {"task": task_gid})

            new_gids[rid] = task_gid
            created += 1
            print(f"  [{created:3d}] R-{rid:03d} → {task_gid}  [{stage}]  {r.get('frente','')}")
            time.sleep(0.18)

        except Exception as e:
            errors += 1
            print(f"  ERROR R-{rid:03d}: {e}")
            time.sleep(0.5)

        # Guardar parcialmente cada 20 tareas (por si se interrumpe)
        if created % 20 == 0 and created > 0:
            _save_gids(new_gids)

    _save_gids(new_gids)
    print(f"\n{'='*50}")
    print(f"Creadas:  {created}")
    print(f"Omitidas: {skipped}  (ya existían)")
    print(f"Errores:  {errors}")
    print(f"GIDs guardados en {GID_FILE.name}")


def _save_gids(gids):
    with open(GID_FILE, "w", encoding="utf-8") as f:
        json.dump({"tasks": {str(k): v for k, v in sorted(gids.items())}},
                  f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
