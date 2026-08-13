import json
from pathlib import Path
HERE = Path(__file__).parent

with open(HERE / 'restricciones_data.json', encoding='utf-8') as f:
    restricciones = json.load(f)

ACTIVIDADES = {
    "Tempisque 500":  ["2da mano","Armadura vigas","Block","Caña","Columnas de madera","Cubierta","Enchape","Hojalateria","Louvers/Fachada","Mobiliario","Obra exterior","Plaqueria/loza sanitaria","Policarbonato","Puertas","Repello Fino","Repello Grueso","Rodapié","Sello y 1era mano","Sisas","Tapicheles","Techo","Teja","Ventanería"],
    "Tempisque 600":  ["2da mano","Armadura vigas","Block","Caña","Columnas de madera","Cubierta","Enchape","Hojalateria","Louvers/Fachada","Mobiliario","Obra exterior","Plaqueria/loza sanitaria","Policarbonato","Puertas","Repello Fino","Repello Grueso","Rodapié","Sello y 1era mano","Sisas","Tapicheles","Techo","Teja","Ventanería"],
    "Solana C":       ["Armadura vigas","Cubierta","Enchape","Formaleta vigas","Gypsum","Hojalateria","Repello Fino","Repello Grueso","Sello y 1era mano","Sisas","Techo","Teja"],
    "Solana U":       ["Armadura vigas","Cubierta","Enchape","Formaleta vigas","Gypsum","Hojalateria","Repello Fino","Repello Grueso","Sello y 1era mano","Sisas","Techo","Teja"],
    "Serena 500":     ["Armadura vigas","Armadura vigas techo","Block N1","Block N2","Cubierta","Entrepiso","Estructura metalica cochera","Estructura metalica gradas","Formaleta vigas techo","Gypsum","Hojalateria","Obra falsa","Repello Fino","Repello Grueso","Sello y 1era mano","Sisas","Techo","Teja","Viguetas"],
    "Aurora 500":     ["Armadura vigas","Armadura vigas techo","Block N1","Block N2","Cubierta","Entrepiso","Estructura metalica cochera","Estructura metalica gradas","Formaleta vigas techo","Gypsum","Hojalateria","Obra falsa","Repello Fino","Repello Grueso","Sello y 1era mano","Sisas","Techo","Teja","Viguetas"],
    "Casitas P2":     ["Enchape","Gypsum","Puertas","Sello y 1era mano","Teja","Ventanería"],
    "Casitas P3":     ["Enchape","Gypsum","Puertas","Sello y 1era mano","Teja","Ventanería"],
    "Casitas P4":     ["Enchape","Gypsum","Puertas","Sello y 1era mano","Teja","Ventanería"],
    "Tempisque P2":   ["Cubierta","Gypsum","Hojalateria","Pedestales externos","Repello Fino","Repello Grueso","Sisas","Techo","Teja"],
    "Tempisque P4":   ["Cubierta","Gypsum","Hojalateria","Pedestales externos","Repello Fino","Repello Grueso","Sisas","Techo","Teja"],
    "THS P1":         ["Armadura vigas","Armadura vigas techo","Block N1","Block N2","Cubierta","Entrepiso","Estructura metalica gradas","Formaleta vigas techo","Obra falsa","Techo","Viguetas"],
    "THS P2":         ["Armadura vigas","Armadura vigas techo","Block N1","Block N2","Cubierta","Entrepiso","Estructura metalica gradas","Formaleta vigas techo","Obra falsa","Techo","Viguetas"],
    "THS P3":         ["Armadura vigas","Armadura vigas techo","Block N1","Block N2","Cubierta","Entrepiso","Estructura metalica gradas","Formaleta vigas techo","Obra falsa","Techo","Viguetas"],
    "THS P4":         ["Armadura vigas","Armadura vigas techo","Block N1","Block N2","Cubierta","Entrepiso","Estructura metalica gradas","Formaleta vigas techo","Obra falsa","Techo","Viguetas"],
}

r_js = json.dumps(restricciones, ensure_ascii=False)
a_js = json.dumps(ACTIVIDADES, ensure_ascii=False)

html = f'''<title>Restricciones Constructivas — Parque Tempisque</title>
<style>
/* ── Tokens ─────────────────────────────────────── */
:root {{
  --accent:     #1B5E35;
  --accent-mid: #2D8653;
  --accent-faint:#E6F2EB;

  /* Stage colors */
  --ele:     #4472C4; --ele-bg:  #D6E4F7;
  --cot:     #5B9BD5; --cot-bg:  #D9EDF9;
  --oc:      #C9A800; --oc-bg:   #FFF5CC;
  --pro:     #ED7D31; --pro-bg:  #FCE8D5;
  --preli:     #C55A11; --preli-bg:  #FAD9C0;
  --sit:     #70AD47; --sit-bg:  #DFF0D0;
  --sin:     #7A7A7A; --sin-bg:  #EBEBEB;

  --bg:      #F4F3EE;
  --surface: #FFFFFF;
  --zone-bg: #EAEAE3;
  --border:  #D4D2CB;
  --ink:     #1C2018;
  --ink-2:   #4A5244;
  --ink-3:   #7A8172;
  --r:  5px; --r2: 8px;
  --sh:  0 1px 3px rgba(0,0,0,.07),0 1px 2px rgba(0,0,0,.04);
  --sh2: 0 4px 12px rgba(0,0,0,.10);
}}
@media(prefers-color-scheme:dark){{
  :root{{
    --ele:#6B96E0;--ele-bg:#1A2A4A;
    --cot:#7AB5E8;--cot-bg:#122038;
    --oc: #D4B020;--oc-bg: #2A2000;
    --pro:#F09050;--pro-bg:#2D1A08;
    --preli:#D87040;--preli-bg:#2A1005;
    --sit:#88C860;--sit-bg:#122008;
    --sin:#909090;--sin-bg:#252525;
    --bg:#12160E;--surface:#1A1F15;--zone-bg:#1F261A;
    --border:#2E3829;--ink:#E4EAD8;--ink-2:#A8B49C;--ink-3:#6A7A60;
    --accent-faint:#1E3326;
  }}
}}
:root[data-theme="dark"]{{
  --ele:#6B96E0;--ele-bg:#1A2A4A;
  --cot:#7AB5E8;--cot-bg:#122038;
  --oc: #D4B020;--oc-bg: #2A2000;
  --pro:#F09050;--pro-bg:#2D1A08;
  --preli:#D87040;--preli-bg:#2A1005;
  --sit:#88C860;--sit-bg:#122008;
  --sin:#909090;--sin-bg:#252525;
  --bg:#12160E;--surface:#1A1F15;--zone-bg:#1F261A;
  --border:#2E3829;--ink:#E4EAD8;--ink-2:#A8B49C;--ink-3:#6A7A60;
  --accent-faint:#1E3326;
}}
:root[data-theme="light"]{{
  --ele:#4472C4;--ele-bg:#D6E4F7;
  --cot:#5B9BD5;--cot-bg:#D9EDF9;
  --oc: #C9A800;--oc-bg: #FFF5CC;
  --pro:#ED7D31;--pro-bg:#FCE8D5;
  --preli:#C55A11;--preli-bg:#FAD9C0;
  --sit:#70AD47;--sit-bg:#DFF0D0;
  --sin:#7A7A7A;--sin-bg:#EBEBEB;
  --bg:#F4F3EE;--surface:#FFFFFF;--zone-bg:#EAEAE3;
  --border:#D4D2CB;--ink:#1C2018;--ink-2:#4A5244;--ink-3:#7A8172;
  --accent-faint:#E6F2EB;
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{font-size:15px}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--ink);line-height:1.5;min-height:100vh}}
button{{cursor:pointer;font:inherit;border:none;background:none}}
input,select,textarea{{font:inherit}}
@media(prefers-reduced-motion:reduce){{*{{transition:none!important;animation:none!important}}}}

/* ── Topbar ───────────────────────────────────── */
#topbar{{position:sticky;top:0;z-index:100;background:var(--accent);padding:0 20px;display:flex;align-items:center;gap:14px;height:52px;box-shadow:0 2px 8px rgba(0,0,0,.25)}}
.brand{{display:flex;flex-direction:column;line-height:1.1;white-space:nowrap}}
.brand-name{{font-size:13px;font-weight:700;color:#fff;letter-spacing:.04em;text-transform:uppercase}}
.brand-sub{{font-size:10px;color:rgba(255,255,255,.65);letter-spacing:.06em;text-transform:uppercase}}
.tb-div{{width:1px;height:26px;background:rgba(255,255,255,.25);flex-shrink:0}}
#search-wrap{{flex:1;max-width:420px;display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);border-radius:6px;padding:0 12px;height:34px}}
#search-wrap svg{{opacity:.7;flex-shrink:0}}
#search{{flex:1;background:none;border:none;outline:none;color:#fff;font-size:13px}}
#search::placeholder{{color:rgba(255,255,255,.55)}}
/* Legend strip in topbar */
.legend-strip{{display:flex;gap:4px;align-items:center;margin-left:auto}}
.leg-item{{display:flex;align-items:center;gap:4px;font-size:10px;color:rgba(255,255,255,.8)}}
.leg-pill{{font-size:9px;font-weight:800;letter-spacing:.04em;padding:2px 6px;border-radius:3px;color:#fff}}
.leg-pill.l-ele{{background:var(--ele)}} .leg-pill.l-cot{{background:var(--cot)}}
.leg-pill.l-oc{{background:var(--oc);color:#1a1a00}} .leg-pill.l-pro{{background:var(--pro)}}
.leg-pill.l-preli{{background:var(--preli)}} .leg-pill.l-sit{{background:var(--sit)}}
.leg-pill.l-sin{{background:var(--sin)}}
#theme-btn{{width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.8);font-size:14px;flex-shrink:0}}
#theme-btn:hover{{background:rgba(255,255,255,.22)}}

/* ── KPI bar ──────────────────────────────────── */
#kpibar{{background:var(--surface);border-bottom:1px solid var(--border);padding:6px 20px;display:flex;align-items:center;gap:8px;overflow-x:auto}}
.kpi-block{{display:flex;align-items:center;gap:6px;padding:4px 10px;border-radius:4px;border:1px solid var(--border);white-space:nowrap;font-size:12px;color:var(--ink-2)}}
.kpi-block .k-num{{font-size:16px;font-weight:800;font-variant-numeric:tabular-nums;line-height:1}}
.kpi-block .k-label{{font-size:10px;color:var(--ink-3)}}
.kpi-block .k-dot{{width:10px;height:10px;border-radius:2px;flex-shrink:0}}
.kpi-div{{width:1px;height:28px;background:var(--border);flex-shrink:0}}
#results-count{{margin-left:auto;font-size:11px;color:var(--ink-3);white-space:nowrap;font-variant-numeric:tabular-nums}}

/* ── Filterbar ────────────────────────────────── */
#filterbar{{position:sticky;top:52px;z-index:90;background:var(--surface);border-bottom:1px solid var(--border);padding:7px 20px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}}
.filter-label{{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);white-space:nowrap}}
.chip-row{{display:flex;gap:4px;flex-wrap:wrap}}
.chip{{font-size:11px;padding:3px 10px;border-radius:20px;border:1px solid var(--border);color:var(--ink-2);background:var(--surface);transition:all .12s;letter-spacing:.02em}}
.chip:hover{{border-color:var(--accent-mid);color:var(--accent)}}
.chip.active{{font-weight:700;color:#fff;border-color:transparent}}
.chip.s-ele.active{{background:var(--ele)}} .chip.s-cot.active{{background:var(--cot)}}
.chip.s-oc.active{{background:var(--oc);color:#2a2000}} .chip.s-pro.active{{background:var(--pro)}}
.chip.s-preli.active{{background:var(--preli)}} .chip.s-sit.active{{background:var(--sit)}}
.chip.s-sin.active{{background:var(--sin)}}
.chip.s-all.active{{background:var(--accent)}}
.sep{{width:1px;height:20px;background:var(--border);flex-shrink:0}}

/* ── Main ─────────────────────────────────────── */
#main{{max-width:980px;margin:0 auto;padding:24px 20px 60px}}

/* ── Zone ─────────────────────────────────────── */
.zone{{margin-bottom:32px}}
.zone-header{{display:flex;align-items:center;gap:10px;margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--accent)}}
.zone-name{{font-size:18px;font-weight:800;color:var(--accent);letter-spacing:-.01em}}
.zone-badge{{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-3);background:var(--zone-bg);padding:2px 8px;border-radius:3px}}
.zone-stats{{margin-left:auto;font-size:11px;color:var(--ink-3);font-variant-numeric:tabular-nums}}

/* ── Frente ───────────────────────────────────── */
.frente-list{{display:flex;flex-direction:column;gap:6px}}
.frente{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;box-shadow:var(--sh)}}
.frente-btn{{width:100%;text-align:left;display:flex;align-items:center;gap:10px;padding:11px 16px;min-height:46px;transition:background .12s}}
.frente-btn:hover{{background:var(--accent-faint)}}
.frente-icon{{width:8px;height:8px;border-radius:50%;background:var(--border);flex-shrink:0}}
.frente.fi-ele .frente-icon{{background:var(--ele);box-shadow:0 0 0 3px var(--ele-bg)}}
.frente.fi-cot .frente-icon{{background:var(--cot);box-shadow:0 0 0 3px var(--cot-bg)}}
.frente.fi-oc  .frente-icon{{background:var(--oc); box-shadow:0 0 0 3px var(--oc-bg)}}
.frente.fi-pro .frente-icon{{background:var(--pro);box-shadow:0 0 0 3px var(--pro-bg)}}
.frente.fi-preli .frente-icon{{background:var(--preli);box-shadow:0 0 0 3px var(--preli-bg)}}
.frente.fi-sit .frente-icon{{background:var(--sit);box-shadow:0 0 0 3px var(--sit-bg)}}
.frente.fi-sin .frente-icon{{background:var(--sin);box-shadow:0 0 0 3px var(--sin-bg)}}
.frente-name{{font-size:14px;font-weight:700;color:var(--ink);letter-spacing:-.01em}}
.frente-fase{{font-size:11px;color:var(--ink-3);letter-spacing:.04em;text-transform:uppercase}}
.frente-counts{{margin-left:auto;display:flex;gap:4px;align-items:center;flex-wrap:wrap}}
/* Compra progress en frente header */
.frente-compra-prog{{font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;white-space:nowrap;flex-shrink:0;font-variant-numeric:tabular-nums}}
.frente-compra-prog.cp-none{{background:var(--sin-bg);color:var(--sin)}}
.frente-compra-prog.cp-partial{{background:var(--preli-bg);color:var(--preli)}}
.frente-compra-prog.cp-all{{background:var(--sit-bg);color:var(--sit)}}
/* Print button */
#print-btn{{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:5px 11px;border-radius:6px;background:rgba(255,255,255,.12);color:rgba(255,255,255,.85);border:1px solid rgba(255,255,255,.2);white-space:nowrap;flex-shrink:0;cursor:pointer;transition:background .12s}}
#print-btn:hover{{background:rgba(255,255,255,.22)}}
/* Gantt overlay */
#gantt-btn,#export-state-btn{{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:5px 11px;border-radius:6px;background:rgba(255,255,255,.12);color:rgba(255,255,255,.85);border:1px solid rgba(255,255,255,.2);white-space:nowrap;flex-shrink:0;cursor:pointer;transition:background .12s}}
#gantt-btn:hover,#export-state-btn:hover{{background:rgba(255,255,255,.22)}}
#gantt-overlay{{position:fixed;inset:0;background:var(--bg);z-index:300;display:none;flex-direction:column;overflow:hidden}}
#gantt-overlay.open{{display:flex}}
#gantt-top{{background:var(--accent);padding:0 20px;display:flex;align-items:center;gap:12px;height:52px;flex-shrink:0}}
#gantt-top h2{{font-size:13px;font-weight:700;color:#fff;letter-spacing:.02em;white-space:nowrap;margin:0;flex:1;min-width:0}}
#gantt-body{{flex:1;overflow:auto}}
.g-close-btn{{background:rgba(255,255,255,.15);border:none;color:#fff;padding:5px 14px;border-radius:5px;cursor:pointer;font-size:12px;font-weight:700;white-space:nowrap;flex-shrink:0}}
.g-close-btn:hover{{background:rgba(255,255,255,.25)}}
.g-legend{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;flex-shrink:0}}
.g-leg-item{{display:flex;align-items:center;gap:4px;font-size:10px;color:rgba(255,255,255,.8)}}
.g-leg-dot{{width:10px;height:10px;border-radius:2px;flex-shrink:0}}
/* Print mode */
@media print{{
  .topbar,.filter-bar,#filterbar,#kpibar,.add-btn,.expand-btn,#consol-overlay,#modal-overlay,#gantt-overlay,
  #print-btn,#theme-btn,.notes-wrap,.compra-row,.qty-casa-row,.qty-row,.detail-sep,
  .frente-btn .chevron{{display:none!important}}
  body,html{{background:#fff!important;color:#000!important}}
  .frente-body{{max-height:none!important;overflow:visible!important;display:block!important}}
  .frente-body-inner{{border-top:1px solid #ddd;padding:8px 0;display:flex!important;flex-direction:column!important}}
  .rcard{{border:1px solid #ccc;border-radius:4px;margin-bottom:6px;page-break-inside:avoid}}
  .rcard-detail{{display:grid!important}}
  .rcard-top{{padding:8px}}
  .frente-name{{font-size:13px;font-weight:700}}
  .zone-header{{border-bottom:2px solid #000;margin-bottom:8px}}
}}
.badge{{font-size:9px;font-weight:800;padding:2px 6px;border-radius:3px;font-variant-numeric:tabular-nums;letter-spacing:.04em;text-transform:uppercase;color:#fff}}
.b-ele{{background:var(--ele)}} .b-cot{{background:var(--cot)}}
.b-oc{{background:var(--oc);color:#2a2000}} .b-pro{{background:var(--pro)}}
.b-preli{{background:var(--preli)}} .b-sit{{background:var(--sit)}}
.b-sin{{background:var(--sin)}} .b-empty{{background:var(--zone-bg);color:var(--ink-3)}}
.chevron{{width:20px;height:20px;display:flex;align-items:center;justify-content:center;color:var(--ink-3);flex-shrink:0;transition:transform .2s}}
.frente.open .chevron{{transform:rotate(180deg)}}

/* ── Frente body ──────────────────────────────── */
.frente-body{{max-height:0;overflow:hidden;transition:max-height .28s ease}}
.frente.open .frente-body{{max-height:5000px}}
.frente-body-inner{{border-top:1px solid var(--border);padding:10px 16px 12px;display:flex;flex-direction:column;gap:8px}}
.acts-strip{{display:flex;align-items:center;gap:5px;flex-wrap:wrap;padding:6px 10px;background:var(--accent-faint);border-radius:var(--r)}}
.acts-label{{font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);white-space:nowrap}}
.act-chip{{font-size:10px;padding:2px 7px;border-radius:3px;background:var(--surface);border:1px solid rgba(27,94,53,.2);color:var(--accent);font-weight:500}}
.add-btn{{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--accent-mid);padding:5px 10px;border:1px dashed var(--accent-mid);border-radius:var(--r);transition:all .12s;width:fit-content}}
.add-btn:hover{{background:var(--accent-faint)}}
.empty-frente{{font-size:12px;color:var(--ink-3);padding:6px 0;display:flex;align-items:center;gap:8px}}

/* ── Restriction card ─────────────────────────── */
.rcard{{border:1px solid var(--border);border-radius:var(--r);background:var(--bg);overflow:hidden;transition:box-shadow .12s}}
.rcard:hover{{box-shadow:0 2px 8px rgba(0,0,0,.08)}}
.rcard-head{{display:flex;align-items:flex-start;cursor:pointer;padding:10px 14px 10px 0}}
.rcard-stripe{{width:4px;flex-shrink:0;align-self:stretch;min-height:40px}}
.st-ele{{background:var(--ele)}} .st-cot{{background:var(--cot)}}
.st-oc {{background:var(--oc)}} .st-pro{{background:var(--pro)}}
.st-preli{{background:var(--preli)}} .st-sit{{background:var(--sit)}}
.st-sin{{background:var(--sin)}}
.rcard-main{{flex:1;padding-left:12px}}
.rcard-top{{display:flex;align-items:center;gap:7px;flex-wrap:wrap}}
.rcard-id{{font-size:10px;color:var(--ink-3);font-weight:700;letter-spacing:.06em;font-variant-numeric:tabular-nums}}
.rcard-tipo{{font-size:10px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;padding:2px 7px;border-radius:3px}}
.t-compra{{background:#FEF4E7;color:#8B5A00}} .t-diseno{{background:#E8F0FC;color:#1A48A0}}
.t-permiso{{background:#F3E8F8;color:#6B1FA0}} .t-subc{{background:#E8F5FA;color:#0A6080}}
.t-otro{{background:var(--sin-bg);color:var(--sin)}}
:root[data-theme="dark"] .t-compra{{background:#2D1F0E;color:#E8A84A}}
:root[data-theme="dark"] .t-diseno{{background:#1A2A4A;color:#80AAEE}}
:root[data-theme="dark"] .t-permiso{{background:#2A1240;color:#C090E8}}
:root[data-theme="dark"] .t-subc{{background:#0A2030;color:#60C0E0}}
@media(prefers-color-scheme:dark){{
  .t-compra{{background:#2D1F0E;color:#E8A84A}} .t-diseno{{background:#1A2A4A;color:#80AAEE}}
  .t-permiso{{background:#2A1240;color:#C090E8}} .t-subc{{background:#0A2030;color:#60C0E0}}
}}
.overdue-badge{{font-size:10px;font-weight:700;padding:2px 7px;border-radius:3px;background:var(--preli-bg);color:var(--preli);font-variant-numeric:tabular-nums}}
.rcard-titulo{{font-size:13px;font-weight:600;color:var(--ink);margin-top:3px;line-height:1.3}}
.rcard-meta{{margin-top:5px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}}
.meta-item{{font-size:11px;color:var(--ink-3);display:flex;align-items:center;gap:4px}}
.meta-resp{{font-weight:600;color:var(--ink-2)}}
.prio-dot{{width:7px;height:7px;border-radius:50%;flex-shrink:0}}
.prio-alta{{background:var(--preli)}} .prio-media{{background:var(--oc)}} .prio-baja{{background:var(--sit)}}
.rcard-right{{display:flex;flex-direction:column;align-items:flex-end;gap:6px;padding-left:10px;flex-shrink:0}}

/* ── Stage pill ───────────────────────────────── */
.stage-pill{{
  display:inline-flex;flex-direction:column;align-items:center;
  padding:3px 10px;border-radius:4px;
  cursor:pointer;user-select:none;
  transition:transform .1s,opacity .1s;
  border:none;min-width:48px;
}}
.stage-pill:hover{{transform:scale(1.06);opacity:.9}}
.stage-pill .sp-code{{font-size:12px;font-weight:800;letter-spacing:.06em;line-height:1.1}}
.stage-pill .sp-name{{font-size:8px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;opacity:.8;line-height:1;margin-top:1px}}
.sp-ele{{background:var(--ele);color:#fff}}
.sp-cot{{background:var(--cot);color:#fff}}
.sp-oc {{background:var(--oc);color:#2a2000}}
.sp-pro{{background:var(--pro);color:#fff}}
.sp-preli{{background:var(--preli);color:#fff}}
.sp-sit{{background:var(--sit);color:#fff}}
.sp-sin{{background:var(--sin);color:#fff}}

.expand-btn{{font-size:10px;color:var(--ink-3);display:flex;align-items:center;gap:3px;padding:3px 7px;border-radius:3px;background:var(--border);transition:all .12s}}
.expand-btn:hover,.rcard.expanded .expand-btn{{background:var(--accent-faint);color:var(--accent)}}

/* ── Card detail ──────────────────────────────── */
.rcard-detail{{display:none;border-top:1px solid var(--border);padding:14px 16px;background:var(--surface)}}
.rcard.expanded .rcard-detail{{display:block}}
.detail-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px 20px;margin-bottom:12px}}
@media(max-width:600px){{.detail-grid{{grid-template-columns:1fr}}}}
.detail-field label{{font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);display:block;margin-bottom:2px}}
.detail-field span{{font-size:12px;color:var(--ink);line-height:1.4}}
.detail-sep{{height:1px;background:var(--border);margin:12px 0}}
.detail-sect{{font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px}}
.impact-row{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px}}
.impact-pill{{display:flex;align-items:center;gap:6px;padding:5px 10px;border:1px solid var(--border);border-radius:5px;font-size:11px;color:var(--ink-2)}}
.impact-pill.r-alto {{border-color:var(--preli);background:var(--preli-bg);color:var(--preli)}}
.impact-pill.r-medio{{border-color:var(--oc); background:var(--oc-bg); color:var(--oc)}}
.impact-pill.r-bajo {{border-color:var(--sit);background:var(--sit-bg);color:var(--sit)}}
/* Stage progress bar */
.stage-progress{{display:flex;gap:3px;margin:12px 0}}
.sp-step{{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px}}
.sp-step-bar{{height:6px;border-radius:3px;width:100%;background:var(--border)}}
.sp-step.active .sp-step-bar{{background:var(--step-col)}}
.sp-step.done   .sp-step-bar{{background:var(--step-col);opacity:.45}}
.sp-step-lbl{{font-size:8px;font-weight:700;letter-spacing:.04em;color:var(--ink-3);text-align:center}}
.sp-step.active .sp-step-lbl{{color:var(--ink-2);font-weight:800}}
/* Editable date */
.date-edit-wrap{{display:flex;align-items:center;gap:6px}}
.date-val{{font-size:12px;color:var(--ink);cursor:pointer;border-bottom:1px dashed var(--border);padding-bottom:1px;transition:color .12s,border-color .12s}}
.date-val:hover{{border-color:var(--accent-mid);color:var(--accent)}}
.date-input{{font-size:12px;border:1px solid var(--accent-mid);border-radius:4px;padding:3px 6px;background:var(--bg);color:var(--ink);display:none}}
.date-save{{font-size:10px;font-weight:700;padding:3px 8px;border-radius:3px;background:var(--accent);color:#fff;display:none;cursor:pointer;border:none}}
/* Notes */
.notes-wrap{{margin-top:12px}}
.notes-wrap label{{font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);display:block;margin-bottom:4px}}
.notes-input{{width:100%;min-height:54px;border:1px solid var(--border);border-radius:var(--r);background:var(--bg);color:var(--ink);font-size:12px;padding:7px 10px;resize:vertical;line-height:1.4}}
.notes-input:focus{{outline:none;border-color:var(--accent-mid)}}
.notes-save{{margin-top:5px;font-size:11px;font-weight:600;color:var(--accent);padding:3px 10px;border:1px solid var(--accent-mid);border-radius:4px;background:var(--accent-faint);transition:all .12s}}
.notes-save:hover{{background:var(--accent);color:#fff}}
.asana-link-btn{{display:inline-flex;align-items:center;gap:5px;padding:3px 10px;border-radius:4px;font-size:11px;font-weight:600;background:#f06a35;color:#fff;border:none;cursor:pointer;text-decoration:none;margin-left:7px;vertical-align:middle;transition:opacity .15s;line-height:1.4}}
.asana-link-btn:hover{{opacity:.82}}

/* ── Modal ────────────────────────────────────── */
#modal-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:200;display:none;align-items:center;justify-content:center;padding:16px}}
#modal-overlay.open{{display:flex}}
#modal{{background:var(--surface);border-radius:var(--r2);width:100%;max-width:480px;padding:20px;box-shadow:0 8px 32px rgba(0,0,0,.2);max-height:90vh;overflow-y:auto}}
.modal-title{{font-size:15px;font-weight:700;color:var(--ink);margin-bottom:16px}}
.form-row{{margin-bottom:12px}}
.form-row label{{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);display:block;margin-bottom:4px}}
.form-row input,.form-row select,.form-row textarea{{width:100%;border:1px solid var(--border);border-radius:var(--r);background:var(--bg);color:var(--ink);font-size:13px;padding:7px 10px}}
.form-row textarea{{min-height:60px;resize:vertical}}
.modal-btns{{display:flex;gap:8px;justify-content:flex-end;margin-top:16px}}
.btn-cancel{{font-size:12px;padding:6px 14px;border-radius:4px;border:1px solid var(--border);color:var(--ink-2)}}
.btn-save{{font-size:12px;padding:6px 14px;border-radius:4px;background:var(--accent);color:#fff;font-weight:600}}

/* ── Empty state ──────────────────────────────── */
#empty-state{{display:none;text-align:center;padding:60px 20px;color:var(--ink-3)}}
mark{{background:#FFF176;color:inherit;border-radius:2px;padding:0 1px}}
@media(prefers-color-scheme:dark){{mark{{background:#4A420A}}}}
:root[data-theme="dark"] mark{{background:#4A420A}}
::-webkit-scrollbar{{width:6px}}
::-webkit-scrollbar-thumb{{background:var(--border);border-radius:3px}}

/* ── Compra Global button ──────────────────────────── */
.tb-btn-global{{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:700;letter-spacing:.04em;padding:5px 12px;border-radius:5px;background:rgba(255,255,255,.18);color:#fff;border:1px solid rgba(255,255,255,.3);transition:background .12s;white-space:nowrap;flex-shrink:0}}
.tb-btn-global:hover{{background:rgba(255,255,255,.28)}}
/* Qty field */
.qty-row{{display:flex;align-items:center;gap:5px}}
.qty-input{{width:72px;border:1px solid var(--border);border-radius:4px;padding:3px 6px;background:var(--bg);color:var(--ink);font-size:12px;font-variant-numeric:tabular-nums}}
.qty-unit{{width:90px;border:1px solid var(--border);border-radius:4px;padding:3px 4px;background:var(--bg);color:var(--ink);font-size:12px}}
.qty-input:focus,.qty-unit:focus{{outline:none;border-color:var(--accent-mid)}}
.qty-casa-row{{display:flex;align-items:center;gap:5px;margin-top:5px;flex-wrap:wrap}}
.qty-casa-inp{{width:60px;border:1px solid var(--border);border-radius:4px;padding:3px 5px;background:var(--bg);color:var(--ink);font-size:12px;font-variant-numeric:tabular-nums}}
.qty-casas-list{{min-width:110px;flex:1;border:1px solid var(--border);border-radius:4px;padding:3px 5px;background:var(--bg);color:var(--ink);font-size:12px}}
.qty-casa-inp:focus,.qty-casas-list:focus{{outline:none;border-color:var(--accent-mid)}}
.qcl{{font-size:10px;color:var(--ink-3);white-space:nowrap;font-weight:600}}
.qty-calc-total{{font-size:11px;color:var(--accent);font-weight:700;margin-left:2px;white-space:nowrap;font-variant-numeric:tabular-nums}}
.compra-row{{margin-top:7px;display:flex;flex-direction:column;gap:5px}}
.compra-header{{display:flex;align-items:center;justify-content:space-between;font-size:10px;color:var(--ink-3);font-weight:600;text-transform:uppercase;letter-spacing:.4px}}
.compra-chips-wrap{{display:flex;flex-wrap:wrap;gap:4px;min-height:22px}}
.compra-chip{{display:inline-flex;align-items:center;gap:2px;padding:2px 9px;border-radius:3px;font-size:11px;font-weight:700;cursor:pointer;border:1px solid var(--border);background:var(--bg-2);color:var(--ink-2);transition:background .15s,color .15s,border-color .15s;font-variant-numeric:tabular-nums;line-height:1.6}}
.compra-chip:hover{{background:var(--border);border-color:var(--ink-3)}}
.compra-chip.compra-done{{background:var(--sit);border-color:var(--sit);color:#fff}}
.compra-count-lbl{{font-size:10px;font-weight:600;padding:1px 6px;border-radius:10px;background:var(--bg-2);color:var(--ink-3)}}
.compra-count-lbl.all-done{{background:var(--sit);color:#fff}}
/* Consolidation overlay */
#consol-overlay{{position:fixed;inset:0;background:var(--bg);z-index:300;display:none;flex-direction:column;overflow:hidden}}
#consol-overlay.open{{display:flex}}
#consol-top{{background:var(--accent);padding:0 20px;display:flex;align-items:center;gap:12px;height:52px;flex-shrink:0;overflow-x:auto}}
#consol-top h2{{font-size:13px;font-weight:700;color:#fff;letter-spacing:.02em;white-space:nowrap}}
#consol-search-wrap{{flex:1;max-width:340px;display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);border-radius:5px;padding:0 10px;height:32px;flex-shrink:0}}
#consol-search{{flex:1;background:none;border:none;outline:none;color:#fff;font-size:13px}}
#consol-search::placeholder{{color:rgba(255,255,255,.55)}}
.consol-close{{width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;flex-shrink:0;margin-left:4px}}
.consol-close:hover{{background:rgba(255,255,255,.25)}}
.consol-export{{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:5px 12px;border-radius:5px;background:rgba(255,255,255,.18);color:#fff;border:1px solid rgba(255,255,255,.3);white-space:nowrap;flex-shrink:0;transition:background .12s}}
.consol-export:hover{{background:rgba(255,255,255,.28)}}
#consol-body{{flex:1;overflow-y:auto;padding:20px}}
#consol-inner{{max-width:980px;margin:0 auto}}
#consol-summary{{display:flex;gap:24px;flex-wrap:wrap;margin-bottom:16px;padding:12px 16px;background:var(--surface);border:1px solid var(--border);border-radius:var(--r2);align-items:flex-start}}
#consol-summary div{{font-size:12px;color:var(--ink-3)}}
.consol-mat-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r2);margin-bottom:10px;overflow:hidden;box-shadow:var(--sh)}}
.consol-mat-head{{padding:11px 16px;display:flex;align-items:center;gap:10px;cursor:pointer;transition:background .12s}}
.consol-mat-head:hover{{background:var(--accent-faint)}}
.consol-mat-name{{font-size:14px;font-weight:700;color:var(--ink);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.consol-mat-count{{font-size:10px;font-weight:700;padding:2px 8px;border-radius:3px;background:var(--zone-bg);color:var(--ink-3);white-space:nowrap;flex-shrink:0}}
.consol-mat-qty{{font-size:13px;font-weight:800;color:var(--accent);font-variant-numeric:tabular-nums;white-space:nowrap;flex-shrink:0}}
.consol-mat-qty.partial{{color:var(--oc)}}
.consol-mat-body{{display:none;border-top:1px solid var(--border)}}
.consol-mat-card.expanded .consol-mat-body{{display:block}}
.consol-mat-card.expanded .consol-mat-head svg{{transform:rotate(180deg)}}
.consol-frente-row{{display:grid;grid-template-columns:1.5fr auto 110px 140px 100px;gap:8px;align-items:center;padding:7px 16px;border-bottom:1px solid var(--border);font-size:12px}}
.consol-frente-row:last-child{{border-bottom:none}}
.consol-frente-name{{font-weight:600;color:var(--ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.consol-qty-cell{{font-variant-numeric:tabular-nums;color:var(--ink);font-weight:600;white-space:nowrap;text-align:right}}
.consol-qty-cell.empty{{color:var(--ink-3);font-style:italic;font-weight:400}}
.consol-stage-mini{{font-size:9px;font-weight:800;padding:2px 6px;border-radius:3px;color:#fff;white-space:nowrap}}
.consol-resp-cell{{color:var(--ink-3);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.consol-date-cell{{color:var(--ink-3);white-space:nowrap;font-size:11px}}
@media(max-width:700px){{
  .consol-resp-cell,.consol-date-cell{{display:none}}
  .consol-frente-row{{grid-template-columns:1.5fr auto 1fr}}
}}
</style>

<!-- Topbar -->
<div id="topbar">
  <div class="brand">
    <span class="brand-name">Parque Tempisque</span>
    <span class="brand-sub">Control de Restricciones</span>
  </div>
  <div class="tb-div"></div>
  <div id="search-wrap">
    <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input id="search" type="search" placeholder="Buscar material, frente, responsable…" autocomplete="off">
  </div>
  <div class="legend-strip" id="legend-strip">
    <span class="leg-item"><span class="leg-pill l-ele">ELE</span> Elección</span>
    <span class="leg-item"><span class="leg-pill l-cot">COT</span> Cotización</span>
    <span class="leg-item"><span class="leg-pill l-oc">OC</span> Orden de compra</span>
    <span class="leg-item"><span class="leg-pill l-pro">PRO</span> Producción</span>
    <span class="leg-item"><span class="leg-pill l-preli">TRA</span> Etapa Preliminar</span>
    <span class="leg-item"><span class="leg-pill l-sit">SIT</span> En sitio</span>
  </div>
  <button class="tb-btn-global" onclick="showConsolidacion()">
    <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 01-8 0"/></svg>
    Compra Global
  </button>
  <button id="gantt-btn" onclick="openGantt()" title="Ver diagrama Gantt">
    <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="2" rx="1"/><rect x="3" y="9" width="12" height="2" rx="1"/><rect x="3" y="14" width="15" height="2" rx="1"/><rect x="3" y="19" width="9" height="2" rx="1"/></svg>
    Gantt
  </button>
  <button id="export-state-btn" onclick="exportState()" title="Exportar cambios para sincronizar con Asana">
    <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
    Exportar
  </button>
  <button id="print-btn" onclick="window.print()" title="Imprimir vista">
    <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
    Imprimir
  </button>
  <button id="theme-btn" title="Cambiar tema">☀</button>
</div>

<!-- KPI bar -->
<div id="kpibar"></div>

<!-- Filterbar -->
<div id="filterbar">
  <span class="filter-label">Etapa</span>
  <div class="chip-row" id="status-chips"></div>
  <div class="sep"></div>
  <span class="filter-label">Tipo</span>
  <div class="chip-row" id="type-chips"></div>
  <span id="results-count"></span>
</div>

<!-- Main -->
<div id="main">
  <div id="zone-container"></div>
  <div id="empty-state">
    <svg width="48" height="48" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <p style="margin-top:10px">No se encontraron restricciones con estos filtros.</p>
  </div>
</div>

<!-- Modal -->
<div id="modal-overlay">
  <div id="modal">
    <div class="modal-title" id="modal-title">Nueva Restricción</div>
    <div class="form-row"><label>Título</label><input id="f-titulo" type="text" placeholder="Descripción breve del problema"></div>
    <div class="form-row"><label>Tipo</label>
      <select id="f-tipo">
        <option value="Material / Compra">Material / Compra</option>
        <option value="Diseño Pendiente">Diseño Pendiente</option>
        <option value="Permiso / Trámite">Permiso / Trámite</option>
        <option value="Subcontratista / MO">Subcontratista / MO</option>
        <option value="Otro">Otro</option>
      </select>
    </div>
    <div class="form-row"><label>Etapa actual</label>
      <select id="f-estado">
        <option value="SIN_INICIAR">— Sin iniciar</option>
        <option value="ELE">ELE — Elección</option>
        <option value="COT">COT — Cotización</option>
        <option value="OC">OC — Orden de compra</option>
        <option value="PRO">PRO — Producción</option>
        <option value="PRELI">TRA — Etapa Preliminar</option>
        <option value="SIT">SIT — En sitio</option>
      </select>
    </div>
    <div class="form-row"><label>Prioridad</label>
      <select id="f-prio"><option value="Alta">Alta</option><option value="Media">Media</option><option value="Baja">Baja</option></select>
    </div>
    <div class="form-row"><label>Responsable</label><input id="f-resp" type="text" value="Y. Solano"></div>
    <div class="form-row"><label>Fecha Compromiso</label><input id="f-fecha" type="date"></div>
    <div class="form-row"><label>Descripción</label><textarea id="f-desc" placeholder="Detalle del problema…"></textarea></div>
    <div class="form-row"><label>Actividad Bloqueada</label><input id="f-bloquea" type="text"></div>
    <div class="modal-btns">
      <button class="btn-cancel" id="modal-cancel">Cancelar</button>
      <button class="btn-save" id="modal-save">Guardar</button>
    </div>
  </div>
</div>

<!-- Consolidation overlay -->
<div id="consol-overlay">
  <div id="consol-top">
    <h2>📦 Compra Global por Material</h2>
    <div id="consol-search-wrap">
      <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <input id="consol-search" type="search" placeholder="Buscar material…" autocomplete="off">
    </div>
    <button class="consol-export" onclick="exportConsolidacion()">
      <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      Copiar tabla
    </button>
    <button class="consol-close" onclick="closeConsolidacion()" title="Cerrar (Esc)">✕</button>
  </div>
  <div id="consol-body">
    <div id="consol-inner">
      <div id="consol-summary"></div>
      <div id="consol-list"></div>
    </div>
  </div>
</div>

<!-- Gantt overlay -->
<div id="gantt-overlay">
  <div id="gantt-top">
    <h2>&#x1F4CA; Diagrama Gantt — Restricciones Constructivas</h2>
    <div class="g-legend" id="gantt-legend"></div>
    <button class="g-close-btn" onclick="closeGantt()" title="Cerrar (Esc)">&#x2715; Cerrar</button>
  </div>
  <div id="gantt-body"></div>
</div>

<script>
/* ═══════════ DATA ═══════════ */
const BASE_DATA = {r_js};
const ACTIVIDADES = {a_js};
const FRENTES_BY_ZONE = {{
  "Los Parques":[
    {{nombre:"THA P1",fase:"Fase 1"}},{{nombre:"THA P4",fase:"Fase 4"}},
    {{nombre:"THC P2",fase:"Fase 2"}},{{nombre:"THC P3P4",fase:"Fase 3-4"}},
    {{nombre:"THS P1",fase:"Fase 1"}},{{nombre:"THS P2",fase:"Fase 2"}},
    {{nombre:"THS P3",fase:"Fase 3"}},{{nombre:"THS P4",fase:"Fase 4"}},
    {{nombre:"AP1 P1",fase:"Fase 1"}},{{nombre:"AP2 P1",fase:"Fase 1"}},
    {{nombre:"APP3 P3",fase:"Fase 3"}},{{nombre:"APP4 P3",fase:"Fase 3"}},
    {{nombre:"APP4 P5",fase:"Fase 5"}},
    {{nombre:"Casitas P2",fase:"Fase 2"}},{{nombre:"Casitas P3",fase:"Fase 3"}},
    {{nombre:"Casitas P4",fase:"Fase 4"}},
    {{nombre:"Tempisque P2",fase:"Fase 2"}},{{nombre:"Tempisque P4",fase:"Fase 4"}},
    {{nombre:"Vereda P2",fase:"Fase 2"}},{{nombre:"Vereda P5",fase:"Fase 5"}},
  ],
  "La Pampa":[
    {{nombre:"Aurora 500",fase:"Fase 1"}},{{nombre:"Serena 500",fase:"Fase 1"}},
    {{nombre:"Solana C",fase:"Fase 1"}},{{nombre:"Solana U",fase:"Fase 1"}},
    {{nombre:"Tempisque 500",fase:"Fase 1"}},{{nombre:"Tempisque 600",fase:"Fase 2"}},
  ]
}};

/* ═══════════ CASAS REF (plano de sitio) ═══ */
const CASAS_REF = {{
  /* ── La Pampa ─────────────────────────── */
  "Aurora 500":    ["502","503","508","509","601","604","609","701","705","709"],
  "Serena 500":    ["501","707","1003","1103"],
  "Tempisque 500": ["504","505","506","507"],
  "Tempisque 600": ["602","603","605","606","607","608","702","703","704","706","708"],
  "Solana C":      ["801","901","1002","1101"],
  "Solana U":      ["802","902","1001","1102"],
  /* ── Los Parques — fuente: Procore "Áreas de planos" ─────── */
  /* TH Arista → frente THA */
  "THA P1":      ["101","102","103","104"],
  "THA P4":      ["301","401","503"],
  /* TH Clásica → frente THC */
  "THC P2":      ["204","207"],
  "THC P3P4":    ["302","303","304","402","403","413","414","504"],
  /* THS individual (zonas 1A–3A) + clusters 8A/9A (THS 105–109) */
  "THS P1":      ["105","106","107","108","109"],
  "THS P2":      ["201","202","203","205","206"],
  "THS P3":      ["305","901","902","903","904","905","906","907","908","909","910","916","917"],
  "THS P4":      ["801","802","803","804","805","806","807","808","809","810","811","812","813","814","815","816"],
  /* Casitas */
  "Casitas P2":  ["208","209","210"],
  "Casitas P3":  ["306","307"],
  "Casitas P4":  ["404","405","406"],
  /* Tempisque */
  "Tempisque P2":["213","214","215"],
  "Tempisque P4":["411","412"],
  /* AP pisos, edificios APP, Vereda */
  "AP1 P1":      ["121","122","131","132"],
  "AP2 P1":      ["123","124","133","134"],
  "APP3 P3":     [],
  "APP4 P3":     [],
  "APP4 P5":     [],
  "Vereda P2":   [],
  "Vereda P5":   [],
}};

/* Asana integration */
const ASANA_PROJECT = "1217441236213348";
const ASANA_TASKS = {{1:"1217436475477452",2:"1217436204020511",3:"1217436444358373",4:"1217444547960839",5:"1217444547865679",6:"1217441236308157",7:"1217444547998182",8:"1217444547945224",9:"1217436444381472",10:"1217436475793254",11:"1217441235456118",12:"1217441236416023",13:"1217436475741154",14:"1217453126912708",15:"1217449224860356",16:"1217449224533022",17:"1217444546723098",18:"1217436475140503",19:"1217449224013873",20:"1217441235859578",21:"1217449225028696",22:"1217441236519386",23:"1217441236193433",24:"1217436475947212",25:"1217436475951008",26:"1217441236518262",27:"1217449224113305",28:"1217441236537003",29:"1217436475920953",30:"1217436444652181",31:"1217449224763582",32:"1217436444636556",33:"1217444548204188",34:"1217453159971881",35:"1217436475456358",36:"1217444548225446",37:"1217436444857727",38:"1217441236519411",39:"1217436475784371",40:"1217436445005379",41:"1217449224705870",42:"1217436445014117",43:"1217444547356070",44:"1217436445015472",45:"1217444546388819",46:"1217436475887556",47:"1217441236647131",48:"1217441236792642",49:"1217449224113333",50:"1217436476144840",51:"1217444547498200",52:"1217436475971936",53:"1217449225162758",54:"1217444548370427",55:"1217444548372003",56:"1217444548381544",57:"1217436444225450",58:"1217453126959327",59:"1217441236801425",60:"1217449225093951",61:"1217436475726577",62:"1217449225293674",63:"1217436445136370",64:"1217436476093120",65:"1217441236751571",66:"1217436475805053",67:"1217444548468993",68:"1217441236561235",69:"1217436475688975",70:"1217449224403402",71:"1217441236975756",72:"1217436476264944",73:"1217436445211210",74:"1217444548537329",75:"1217453126912742",76:"1217444548142457",77:"1217441236864154",78:"1217436445179421",79:"1217449225294854",80:"1217444548553011",81:"1217449225185938",82:"1217441236908399",83:"1217441236891831",84:"1217436445015858",85:"1217436476437387",86:"1217444548554668",87:"1217436444510874",88:"1217436476084618",89:"1217441237084952",90:"1217444548543327",91:"1217449224443857",92:"1217436444928395",93:"1217444547828876",94:"1217444548225474",95:"1217436476383964",96:"1217436445284332",97:"1217436476248583",98:"1217449225565019",99:"1217449225576058",100:"1217436475763748",101:"1217436476573150",102:"1217449225575996",103:"1217436476589438",104:"1217436476534350",105:"1217436476546421",106:"1217436476616451",107:"1217449225624074",108:"1217436476573373",109:"1217441237312645",110:"1217436476407635",111:"1217436445106908",112:"1217436476317525",113:"1217436445283977",114:"1217449225586771",115:"1217436476507333",116:"1217436476319859",117:"1217436476690194",118:"1217441236659068",119:"1217444548868764",120:"1217436476419451",121:"1217436445203339",122:"1217436476244241",123:"1217436445074936",124:"1217444548927584",125:"1217441237099110",126:"1217436445434799",127:"1217436445284365",128:"1217436476729850",129:"1217436476634689",130:"1217444548868673",131:"1217449225813973",132:"1217441237133009",133:"1217441237460347",134:"1217441237153972",135:"1217436476529897",136:"1217449225576088",137:"1217436476204560",138:"1217449225687116",139:"1217436476845182",140:"1217441237489972",141:"1217449225654339",142:"1217436445632520",143:"1217441236213388",144:"1217449225743301",145:"1217441237033745",146:"1217436476763260",147:"1217441237133231",148:"1217436445075574",149:"1217441237652103",150:"1217436476483360",151:"1217444548984152",152:"1217449225665267",153:"1217441237479269",154:"1217441237471043",155:"1217441237401771",156:"1217436476953208",157:"1217441237626111",158:"1217449226015546",159:"1217449225704508",160:"1217441237728571",161:"1217444548515682",162:"1217436476407666",163:"1217444548927499",164:"1217449225875083",165:"1217441237635527",166:"1217444549112476",167:"1217436476982723",168:"1217436445455148"}};

/* Stage config */
const STAGES = ['SIN_INICIAR','ELE','COT','OC','PRO','PRELI','SIT'];
const STAGE_LABEL = {{SIN_INICIAR:'—',ELE:'ELE',COT:'COT',OC:'OC',PRO:'PRO',PRELI:'PRELI',SIT:'SIT'}};
const STAGE_NAME  = {{SIN_INICIAR:'Sin iniciar',ELE:'Elección',COT:'Cotización',OC:'Orden de compra',PRO:'Producción',PRELI:'Etapa Preliminar',SIT:'En sitio'}};
const STAGE_CLS   = {{SIN_INICIAR:'sin',ELE:'ele',COT:'cot',OC:'oc',PRO:'pro',PRELI:'preli',SIT:'sit'}};

/* ═══════════ STORE ══════════ */
const STORE_KEY = 'pt-r-v3';
function loadState() {{
  try{{ const d=JSON.parse(localStorage.getItem(STORE_KEY))||{{}};return {{custom:d.custom||[],status:d.status||{{}},notes:d.notes||{{}},cantidades:d.cantidades||{{}},compras:d.compras||{{}},openFrentes:d.openFrentes||[],inicios:d.inicios||{{}}}}; }}
  catch{{ return {{custom:[],status:{{}},notes:{{}},cantidades:{{}},compras:{{}},openFrentes:[],inicios:{{}}}}; }}
}}
function saveState(s) {{ try{{localStorage.setItem(STORE_KEY,JSON.stringify(s));}}catch{{}} }}
let state = loadState();
let nextId = Math.max(0,...BASE_DATA.map(r=>r.id)) + 1 + (state.custom||[]).length;

function allR() {{ return [...BASE_DATA,...(state.custom||[])]; }}
function getStage(r) {{
  const raw = state.status[r.id] || r.estado || 'SIN_INICIAR';
  // normalise old values from previous version
  if(raw==='ABIERTA'||raw==='PENDIENTE') return 'SIN_INICIAR';
  if(raw==='EN GESTIÓN'||raw==='EN PROCESO') return 'ELE';
  if(raw==='RESUELTA'||raw==='TERMINADA') return 'SIT';
  if(raw==='TRA') return 'PRELI';
  if(STAGES.includes(raw)) return raw;
  return 'SIN_INICIAR';
}}
function cycleStage(cur) {{ return STAGES[(STAGES.indexOf(cur)+1)%STAGES.length]; }}

/* ═══════════ FILTERS ════════ */
const TODAY = new Date('2026-08-04');
let filterStatus='TODAS', filterType='TODOS', searchQ='';
function daysOverdue(r) {{
  const s = getStage(r);
  const fc = (state.dates && state.dates[r.id]) || r.fechaCompromiso;
  if(!fc||s==='SIT') return 0;
  const d = new Date(fc+'T00:00:00');
  return Math.max(0,Math.floor((TODAY-d)/86400000));
}}
function fmtDate(s) {{
  if(!s) return '—';
  const d=new Date(s+'T00:00:00');
  return d.toLocaleDateString('es-CR',{{day:'2-digit',month:'short',year:'numeric'}});
}}
function matchesF(r) {{
  const s=getStage(r);
  if(filterStatus!=='TODAS'&&s!==filterStatus) return false;
  if(filterType!=='TODOS'&&r.tipo!==filterType) return false;
  if(searchQ){{
    const q=searchQ.toLowerCase();
    const h=[r.titulo,r.frente,r.material,r.tipo,r.responsable,r.descripcion].join(' ').toLowerCase();
    if(!h.includes(q)) return false;
  }}
  return true;
}}
function hl(t,q){{
  if(!q||!t) return t||'';
  return t.replace(new RegExp('('+q.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&')+')','gi'),'<mark>$1</mark>');
}}

/* ═══════════ RENDER ═════════ */
function renderKPIs() {{
  const all=allR();
  const counts={{}};
  STAGES.forEach(s=>counts[s]=0);
  all.forEach(r=>counts[getStage(r)]++);
  const venc=all.filter(r=>daysOverdue(r)>0).length;
  document.getElementById('kpibar').innerHTML = STAGES.map(s=>`
    <div class="kpi-block">
      <div class="k-dot" style="background:var(--${{STAGE_CLS[s]}})"></div>
      <div><div class="k-num">${{counts[s]}}</div><div class="k-label">${{STAGE_NAME[s]}}</div></div>
    </div>`).join('<div class="kpi-div"></div>') +
    `<div class="kpi-div"></div>
     <div class="kpi-block" style="border-color:var(--preli)">
       <div class="k-dot" style="background:var(--preli)"></div>
       <div><div class="k-num">${{venc}}</div><div class="k-label">Vencidas</div></div>
     </div>
     <span id="results-count" style="margin-left:auto"></span>`;
}}
function renderChips() {{
  const stages=[['TODAS','Todas','all'],...STAGES.map(s=>[s,STAGE_LABEL[s]+' '+STAGE_NAME[s],STAGE_CLS[s]])];
  document.getElementById('status-chips').innerHTML=stages.map(([v,l,c])=>{{
    const a=v===filterStatus;
    return `<button class="chip s-${{c}}${{a?' active':''}}" data-status="${{v}}">${{l}}</button>`;
  }}).join('');
  const types=['TODOS','Material / Compra','Diseño Pendiente','Permiso / Trámite','Subcontratista / MO','Otro'];
  document.getElementById('type-chips').innerHTML=types.map(t=>{{
    const a=t===filterType;
    return `<button class="chip${{a?' active s-all':''}}" data-type="${{t}}">${{t==='TODOS'?'Todos':t}}</button>`;
  }}).join('');
}}

function stageProgressHtml(cur) {{
  const ci=STAGES.indexOf(cur);
  const colors=['var(--sin)','var(--ele)','var(--cot)','var(--oc)','var(--pro)','var(--preli)','var(--sit)'];
  return `<div class="stage-progress">${{STAGES.map((s,i)=>{{
    const cls=i<ci?'done':i===ci?'active':'';
    const col=colors[i];
    return `<div class="sp-step ${{cls}}" style="--step-col:${{col}}">
      <div class="sp-step-bar"></div>
      <div class="sp-step-lbl">${{STAGE_LABEL[s]}}</div>
    </div>`;
  }}).join('')}}</div>`;
}}

function renderCard(r,q) {{
  const stg=getStage(r);
  const od=daysOverdue(r);
  const cls=STAGE_CLS[stg];
  const notes=(state.notes&&state.notes[r.id])||'';
  const riskCls=r.riesgo?'r-'+r.riesgo.toLowerCase():'';
  return `<div class="rcard" data-id="${{r.id}}">
    <div class="rcard-head" onclick="toggleCard(${{r.id}})">
      <div class="rcard-stripe st-${{cls}}"></div>
      <div class="rcard-main">
        <div class="rcard-top">
          <span class="rcard-id">R-${{String(r.id).padStart(3,'0')}}</span>
          <span class="rcard-tipo ${{tipoClass(r.tipo)}}">${{r.tipo}}</span>
          ${{od>0?`<span class="overdue-badge">⚠ ${{od}}d vencida</span>`:''}}
        </div>
        <div class="rcard-titulo">${{hl(r.titulo,q)}}</div>
        <div class="rcard-meta">
          <span class="meta-item"><div class="prio-dot prio-${{r.prioridad.toLowerCase()}}"></div>${{r.prioridad}}</span>
          <span class="meta-item meta-resp">${{hl(getCustomResp(r),q)}}</span>
          ${{r.material?`<span class="meta-item">${{hl(r.material,q)}}</span>`:''}}
          ${{getCustomDate(r)?`<span class="meta-item">Hito: ${{fmtDate(getCustomDate(r))}}</span>`:''}}
        </div>
      </div>
      <div class="rcard-right">
        <button class="stage-pill sp-${{cls}}" onclick="event.stopPropagation();cycleStatus(${{r.id}})" title="Clic para cambiar etapa — ${{STAGE_NAME[stg]}}">
          <span class="sp-code">${{STAGE_LABEL[stg]}}</span>
          <span class="sp-name">${{STAGE_NAME[stg]}}</span>
        </button>
        <button class="expand-btn" onclick="event.stopPropagation();toggleCard(${{r.id}})">
          <span class="expand-lbl">Detalle</span>
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M6 9l6 6 6-6"/></svg>
        </button>
      </div>
    </div>
    <div class="rcard-detail">
      ${{stageProgressHtml(stg)}}
      <div class="detail-grid">
        <div class="detail-field"><label>Descripción</label><span>${{r.descripcion||'—'}}</span></div>
        <div class="detail-field"><label>Etapa</label><span>${{r.etapa||'—'}}</span></div>
        <div class="detail-field"><label>Actividad bloqueada</label><span>${{r.actividadBloqueada||'—'}}</span></div>
        <div class="detail-field"><label>Responsable</label>
          <div class="date-edit-wrap">
            <span class="date-val" data-resp="${{r.id}}" onclick="editResp(${{r.id}})" title="Clic para editar responsable">${{getCustomResp(r)}}</span>
            <input class="date-input" data-resp="${{r.id}}" type="text" value="${{getCustomResp(r)}}" placeholder="Nombre del responsable">
            <button class="date-save" data-resp="${{r.id}}" onclick="saveResp(${{r.id}})">✓</button>
          </div>
        </div>
        <div class="detail-field"><label>Fecha hito</label>
          <div class="date-edit-wrap">
            <span class="date-val" data-id="${{r.id}}" onclick="editDate(${{r.id}})" title="Clic para editar fecha">${{fmtDate(getCustomDate(r))}}</span>
            <input class="date-input" data-id="${{r.id}}" type="date" value="${{getCustomDate(r)||''}}">
            <button class="date-save" data-id="${{r.id}}" onclick="saveDate(${{r.id}})">✓</button>
          </div>
        </div>
        <div class="detail-field"><label>Cantidad</label>
          <div class="qty-casa-row">
            <span class="qcl">${{r.frente.startsWith('AP')?'c/apto.':'c/casa:'}}</span>
            <input class="qty-casa-inp" data-qid="${{r.id}}" type="number" min="0" step="0.01" placeholder="0" value="${{getQtyCasa(r.id)}}" onchange="calcQtyCasa(${{r.id}})" onblur="calcQtyCasa(${{r.id}})">
            <span class="qcl">${{r.frente.startsWith('AP')?'Aptos:':'Casas:'}}</span>
            <input class="qty-casas-list" data-qid="${{r.id}}" data-frente="${{r.frente}}" type="text" placeholder="ej: 101, 102…" value="${{getCasasList(r.id, r.frente)}}" onchange="calcQtyCasa(${{r.id}})" onblur="calcQtyCasa(${{r.id}})">
            <span class="qty-calc-total" data-qtot="${{r.id}}">${{getQtyTotalStr(r.id)}}</span>
          </div>
          <div class="compra-row">
            <div class="compra-header">
              <span>Compra por ${{r.frente.startsWith('AP')?'apartamento':'casa'}}</span>
              <span class="compra-count-lbl" id="compra-count-${{r.id}}"></span>
            </div>
            <div class="compra-chips-wrap" id="compra-chips-${{r.id}}" data-rid="${{r.id}}" data-frente="${{r.frente}}"></div>
          </div>
          <div class="qty-row" style="margin-top:4px">
            <input class="qty-input" data-qid="${{r.id}}" type="number" min="0" step="0.01" placeholder="Total" value="${{getQtyVal(r.id)}}" onchange="saveQty(${{r.id}})" onblur="saveQty(${{r.id}})">
            <select class="qty-unit" data-qid="${{r.id}}" onchange="saveQty(${{r.id}})">${{qtyUnitOptions(r.id)}}</select>
          </div>
        </div>
      </div>
      ${{r.impactoDias||r.riesgo?`
        <div class="detail-sect">Impacto</div>
        <div class="impact-row">
          ${{r.impactoDias?`<div class="impact-pill"><strong>${{r.impactoDias}}</strong>&nbsp;días de atraso</div>`:''}}
          ${{r.riesgo?`<div class="impact-pill ${{riskCls}}">Riesgo <strong>${{r.riesgo}}</strong></div>`:''}}
        </div>`:''}}
      <div class="detail-sep"></div>
      <div class="notes-wrap">
        <label>Notas / Seguimiento</label>
        <textarea class="notes-input" data-id="${{r.id}}" placeholder="Acciones tomadas, contactos, fechas clave…">${{notes}}</textarea>
        <button class="notes-save" data-id="${{r.id}}">Guardar nota</button>
        ${{ASANA_TASKS[r.id]?`<a class="asana-link-btn" href="https://app.asana.com/0/1217441236213348/${{ASANA_TASKS[r.id]}}" target="_blank" rel="noopener" onclick="event.stopPropagation()"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11.5" cy="6.5" r="4.5"/><circle cx="17.5" cy="17.5" r="4.5"/><circle cx="5.5" cy="17.5" r="4.5"/></svg> Ver en Asana</a>`:''}}
      </div>
    </div>
  </div>`;
}}

function getCustomDate(r) {{
  return (state.dates && state.dates[r.id]) || r.fechaCompromiso || '';
}}
function getCustomResp(r) {{
  return (state.resps && state.resps[r.id]) || r.responsable || '';
}}
function editResp(id) {{
  const inp = document.querySelector(`.date-input[data-resp="${{id}}"]`);
  const val = document.querySelector(`.date-val[data-resp="${{id}}"]`);
  const sav = document.querySelector(`.date-save[data-resp="${{id}}"]`);
  if (!inp) return;
  inp.style.display = 'inline-block'; sav.style.display = 'inline-block'; val.style.display = 'none';
  inp.focus(); inp.select();
}}
function saveResp(id) {{
  const inp = document.querySelector(`.date-input[data-resp="${{id}}"]`);
  const val = document.querySelector(`.date-val[data-resp="${{id}}"]`);
  const sav = document.querySelector(`.date-save[data-resp="${{id}}"]`);
  if (!inp) return;
  if (!state.resps) state.resps = {{}};
  state.resps[id] = inp.value.trim() || val.textContent;
  saveState(state);
  val.textContent = state.resps[id];
  inp.style.display = 'none'; sav.style.display = 'none'; val.style.display = 'inline';
  // update header meta too
  const card = document.querySelector(`.rcard[data-id="${{id}}"]`);
  if (card) {{
    const rm = card.querySelector('.meta-resp');
    if (rm) rm.textContent = state.resps[id];
  }}
}}
function editDate(id) {{
  const inp = document.querySelector(`.date-input[data-id="${{id}}"]`);
  const val = document.querySelector(`.date-val[data-id="${{id}}"]`);
  const sav = document.querySelector(`.date-save[data-id="${{id}}"]`);
  if (!inp) return;
  inp.style.display = 'inline-block';
  sav.style.display = 'inline-block';
  val.style.display = 'none';
  inp.focus();
}}
function saveDate(id) {{
  const inp = document.querySelector(`.date-input[data-id="${{id}}"]`);
  const val = document.querySelector(`.date-val[data-id="${{id}}"]`);
  const sav = document.querySelector(`.date-save[data-id="${{id}}"]`);
  if (!inp) return;
  if (!state.dates) state.dates = {{}};
  state.dates[id] = inp.value;
  saveState(state);
  val.textContent = fmtDate(inp.value);
  inp.style.display = 'none';
  sav.style.display = 'none';
  val.style.display = 'inline';
}}
function tipoClass(t) {{
  if(t==='Material / Compra') return 't-compra';
  if(t==='Diseño Pendiente')  return 't-diseno';
  if(t==='Permiso / Trámite') return 't-permiso';
  if(t==='Subcontratista / MO') return 't-subc';
  return 't-otro';
}}

function frenteIconClass(rs) {{
  if(!rs.length) return '';
  const priority=['SIN_INICIAR','ELE','COT','OC','PRO','PRELI','SIT'];
  for(const s of priority) {{
    if(rs.some(r=>getStage(r)===s)) return 'fi-'+STAGE_CLS[s];
  }}
  return '';
}}

function renderAll() {{
  const q=searchQ.toLowerCase().trim();
  const container=document.getElementById('zone-container');
  let totalVisible=0;

  container.innerHTML=Object.entries(FRENTES_BY_ZONE).map(([zona,frentes])=>{{
    const allZone=allR().filter(r=>r.zona===zona);
    const zoneSin=allZone.filter(r=>getStage(r)==='SIN_INICIAR').length;

    const frentesHtml=frentes.map(f=>{{
      const rs=allR().filter(r=>r.zona===zona&&r.frente===f.nombre&&matchesF(r));
      totalVisible+=rs.length;
      const shouldOpen=rs.length>0&&(q||filterStatus!=='TODAS'||filterType!=='TODOS'||(state.openFrentes&&state.openFrentes.includes(f.nombre)));
      const iconCls=frenteIconClass(allR().filter(r=>r.zona===zona&&r.frente===f.nombre));

      // Count by stage for badges
      const stageCounts={{}};
      STAGES.forEach(s=>stageCounts[s]=rs.filter(r=>getStage(r)===s).length);
      const badges=STAGES.filter(s=>stageCounts[s]>0)
        .map(s=>`<span class="badge b-${{STAGE_CLS[s]}}">${{stageCounts[s]}} ${{STAGE_LABEL[s]}}</span>`)
        .join('');

      const acts=(ACTIVIDADES[f.nombre]||[]);
      const actsHtml=acts.length?`<div class="acts-strip">
        <span class="acts-label">Actividades ago-sep</span>
        ${{acts.map(a=>`<span class="act-chip">${{a}}</span>`).join('')}}
      </div>`:'';

      const bodyContent=`
        ${{actsHtml}}
        ${{rs.map(r=>renderCard(r,q)).join('')}}
        ${{!rs.length?`<div class="empty-frente"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>Sin restricciones con estos filtros</div>`:''}}
        <button class="add-btn" onclick="openModal('${{zona}}','${{f.nombre}}')">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12h14"/></svg>
          Agregar restricción
        </button>`;

      return `<div class="frente ${{iconCls}} ${{shouldOpen?'open':''}}" data-frente="${{f.nombre}}">
        <button class="frente-btn" onclick="toggleFrente(this)">
          <div class="frente-icon"></div>
          <span class="frente-name">${{hl(f.nombre,q)}}</span>
          <div class="frente-counts">
            ${{badges||'<span class="badge b-empty">Sin restricciones</span>'}}
          </div>
          ${{frenteCompraProgHtml(rs)}}
          <div class="chevron"><svg width="10" height="10" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></div>
        </button>
        <div class="frente-body"><div class="frente-body-inner">${{bodyContent}}</div></div>
      </div>`;
    }}).join('');

    return `<section class="zone">
      <div class="zone-header">
        <h2 class="zone-name">${{zona}}</h2>
        <span class="zone-badge">${{frentes.length}} frentes</span>
        <span class="zone-stats">${{zoneSin}} sin iniciar · ${{allZone.length}} total</span>
      </div>
      <div class="frente-list">${{frentesHtml}}</div>
    </section>`;
  }}).join('');

  // Update results count in kpibar
  const rc=document.getElementById('results-count');
  if(rc) rc.textContent=`${{totalVisible}} restricci${{totalVisible===1?'ón':'ones'}}`;
  document.getElementById('empty-state').style.display=
    totalVisible===0&&(q||filterStatus!=='TODAS'||filterType!=='TODOS')?'block':'none';

  renderKPIs(); renderChips(); bindChips();
  document.querySelectorAll('.notes-save').forEach(btn=>{{
    btn.addEventListener('click',e=>{{
      const id=+e.target.dataset.id;
      const ta=document.querySelector(`.notes-input[data-id="${{id}}"]`);
      if(!state.notes) state.notes={{}};
      state.notes[id]=ta.value; saveState(state);
      btn.textContent='✓ Guardado';
      setTimeout(()=>btn.textContent='Guardar nota',1500);
    }});
  }});
}}

/* ═══════════ ACTIONS ════════ */
function toggleFrente(btn) {{
  const el=btn.closest('.frente');
  el.classList.toggle('open');
  const name=el.dataset.frente;
  if(!state.openFrentes) state.openFrentes=[];
  if(el.classList.contains('open')) {{
    if(!state.openFrentes.includes(name)) state.openFrentes.push(name);
  }} else {{
    state.openFrentes=state.openFrentes.filter(n=>n!==name);
  }}
  saveState(state);
}}
function toggleCard(id) {{
  const card=document.querySelector(`.rcard[data-id="${{id}}"]`);
  if(!card) return;
  card.classList.toggle('expanded');
  card.querySelector('.expand-lbl').textContent=card.classList.contains('expanded')?'Ocultar':'Detalle';
  if(card.classList.contains('expanded')) renderCompraChips(id);
}}
function cycleStatus(id) {{
  const r=allR().find(x=>x.id===id);
  if(!r) return;
  // Save open UI state before re-render
  const expandedCards=new Set([...document.querySelectorAll('.rcard.expanded')].map(el=>+el.dataset.id));
  const openFrentes=new Set([...document.querySelectorAll('.frente.open')].map(el=>el.dataset.frente));
  state.status[id]=cycleStage(getStage(r));
  saveState(state); renderAll();
  // Restore open UI state
  expandedCards.forEach(eid=>{{
    const card=document.querySelector(`.rcard[data-id="${{eid}}"]`);
    if(card){{card.classList.add('expanded');const lbl=card.querySelector('.expand-lbl');if(lbl)lbl.textContent='Ocultar';renderCompraChips(eid);}}
  }});
  openFrentes.forEach(fname=>{{
    const el=document.querySelector(`.frente[data-frente="${{fname}}"]`);
    if(el) el.classList.add('open');
  }});
}}
function bindChips() {{
  document.querySelectorAll('[data-status]').forEach(b=>b.addEventListener('click',()=>{{filterStatus=b.dataset.status;renderAll();}}));
  document.querySelectorAll('[data-type]').forEach(b=>b.addEventListener('click',()=>{{filterType=b.dataset.type;renderAll();}}));
}}
let modalZona='',modalFrente='';
function openModal(zona,frente) {{
  modalZona=zona; modalFrente=frente;
  document.getElementById('modal-title').textContent=`Nueva Restricción — ${{frente}}`;
  ['f-titulo','f-desc','f-bloquea','f-fecha'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('modal-overlay').classList.add('open');
}}
document.getElementById('modal-cancel').addEventListener('click',()=>document.getElementById('modal-overlay').classList.remove('open'));
document.getElementById('modal-overlay').addEventListener('click',e=>{{
  if(e.target===document.getElementById('modal-overlay')) document.getElementById('modal-overlay').classList.remove('open');
}});
document.getElementById('modal-save').addEventListener('click',()=>{{
  const titulo=document.getElementById('f-titulo').value.trim();
  if(!titulo){{alert('Por favor ingresa un título.');return;}}
  const nr={{
    id:nextId++,titulo,
    tipo:document.getElementById('f-tipo').value,
    zona:modalZona,frente:modalFrente,material:'',etapa:'',
    estado:document.getElementById('f-estado').value,
    prioridad:document.getElementById('f-prio').value,
    responsable:document.getElementById('f-resp').value||'Y. Solano',
    fechaId:new Date().toISOString().split('T')[0],
    fechaCompromiso:document.getElementById('f-fecha').value||null,
    actividadBloqueada:document.getElementById('f-bloquea').value,
    impactoDias:null,riesgo:null,
    descripcion:document.getElementById('f-desc').value,
    accion:'',actualizaciones:[],pasos:[],_custom:true,
  }};
  if(!state.custom) state.custom=[];
  state.custom.push(nr); saveState(state);
  document.getElementById('modal-overlay').classList.remove('open');
  renderAll();
  setTimeout(()=>{{
    const el=document.querySelector(`.frente[data-frente="${{modalFrente}}"]`);
    if(el&&!el.classList.contains('open')) el.classList.add('open');
  }},100);
}});
/* ═══════════ QUANTITIES ════════ */
function getQtyVal(id) {{ return state.cantidades&&state.cantidades[id]?state.cantidades[id].qty:''; }}
function getQtyUnit(id) {{ return state.cantidades&&state.cantidades[id]?state.cantidades[id].unit:'und'; }}
function getQtyCasa(id) {{ return state.cantidades&&state.cantidades[id]?state.cantidades[id].qtyCasa||'':''; }}
function getFrenteCompraProgress(rs){{
  let total=0,done=0;
  rs.forEach(r=>{{
    const casas=getCasasArray(r.id,r.frente);
    total+=casas.length;
    if(casas.length&&state.compras&&state.compras[r.id])
      done+=casas.filter(c=>state.compras[r.id][c]).length;
  }});
  return {{total,done}};
}}
function frenteCompraProgHtml(rs){{
  const p=getFrenteCompraProgress(rs);
  if(!p.total) return '';
  const cls=p.done===p.total?'cp-all':p.done>0?'cp-partial':'cp-none';
  const lbl=p.done===p.total?'\u2713 '+p.done+'/'+p.total:p.done+'/'+p.total;
  return `<span class="frente-compra-prog ${{cls}}" title="Compras: ${{p.done}} de ${{p.total}} unidades">${{lbl}}</span>`;
}}
function getCasasArray(id,frente){{
  const listStr=getCasasList(id,frente);
  return listStr?listStr.split(',').map(s=>s.trim()).filter(Boolean):[];
}}
function renderCompraChips(id){{
  const wrap=document.getElementById('compra-chips-'+id);
  if(!wrap) return;
  const frente=wrap.dataset.frente;
  const casas=getCasasArray(id,frente);
  const cp=state.compras&&state.compras[id]?state.compras[id]:{{}};
  const counter=document.getElementById('compra-count-'+id);
  if(!casas.length){{
    wrap.innerHTML='<span style="font-size:11px;color:var(--ink-3)">Sin casas</span>';
    if(counter){{counter.textContent='';counter.className='compra-count-lbl';}}
    return;
  }}
  const bought=casas.filter(c=>cp[c]).length;
  wrap.innerHTML=casas.map(casa=>{{
    const done=!!cp[casa];
    return `<button class="compra-chip ${{done?'compra-done':''}}" onclick="toggleCompra(${{id}},'${{casa}}')" title="${{done?'Comprado — clic para desmarcar':'Pendiente — clic para marcar comprado'}}">${{done?'✓ ':''}}${{casa}}</button>`;
  }}).join('');
  if(counter){{
    counter.textContent=`${{bought}}/${{casas.length}}`;
    counter.className='compra-count-lbl'+(bought===casas.length&&casas.length?' all-done':'');
  }}
}}
function toggleCompra(id,casa){{
  if(!state.compras) state.compras={{}};
  if(!state.compras[id]) state.compras[id]={{}};
  if(state.compras[id][casa]) delete state.compras[id][casa];
  else state.compras[id][casa]=true;
  if(Object.keys(state.compras[id]).length===0) delete state.compras[id];
  saveState(state);
  renderCompraChips(id);
}}
function getCasasList(id, frente) {{
  const c=state.cantidades&&state.cantidades[id];
  if(c&&c.casasList!==undefined) return c.casasList;
  return CASAS_REF[frente]?CASAS_REF[frente].join(', '):'';
}}
function countCasas(id) {{
  const c=state.cantidades&&state.cantidades[id];
  const list=c&&c.casasList!==undefined?c.casasList:(
    (()=>{{ const el=document.querySelector(`.qty-casas-list[data-qid="${{id}}"]`); return el?el.value:''; }})()
  );
  if(!list||!list.trim()) return 0;
  return list.split(',').filter(s=>s.trim()).length;
}}
function getQtyTotalStr(id) {{
  const c=state.cantidades&&state.cantidades[id];
  if(!c||!c.qtyCasa) return '';
  const nc=c.casasList!==undefined?c.casasList.split(',').filter(s=>s.trim()).length:0;
  if(!nc) return '';
  const t=parseFloat(c.qtyCasa)*nc;
  return isNaN(t)?'':'= '+(t%1===0?t:t.toFixed(2))+' '+(c.unit||'und');
}}
function qtyUnitOptions(id) {{
  const cur=getQtyUnit(id);
  const units=['und','m²','m lineal','kg','sacos','pza','rollo','caja','litros','m³'];
  return units.map(u=>`<option value="${{u}}"${{cur===u?' selected':''}}>${{u}}</option>`).join('');
}}
function saveQty(id) {{
  const qinp=document.querySelector(`.qty-input[data-qid="${{id}}"]`);
  const usel=document.querySelector(`.qty-unit[data-qid="${{id}}"]`);
  const casaInp=document.querySelector(`.qty-casa-inp[data-qid="${{id}}"]`);
  const listInp=document.querySelector(`.qty-casas-list[data-qid="${{id}}"]`);
  if(!qinp) return;
  const qty=qinp.value.trim();
  const unit=usel?usel.value:'und';
  const qtyCasa=casaInp?casaInp.value:'';
  const casasList=listInp?listInp.value.trim():'';
  if(!state.cantidades) state.cantidades={{}};
  if(qty||qtyCasa||casasList) state.cantidades[id]={{qty,unit,qtyCasa,casasList}};
  else delete state.cantidades[id];
  saveState(state);
  renderCompraChips(id);
}}
function calcQtyCasa(id) {{
  const casaInp=document.querySelector(`.qty-casa-inp[data-qid="${{id}}"]`);
  const listInp=document.querySelector(`.qty-casas-list[data-qid="${{id}}"]`);
  const qinp=document.querySelector(`.qty-input[data-qid="${{id}}"]`);
  const usel=document.querySelector(`.qty-unit[data-qid="${{id}}"]`);
  const totSpan=document.querySelector(`.qty-calc-total[data-qtot="${{id}}"]`);
  if(!casaInp||!listInp) return;
  const qc=parseFloat(casaInp.value)||0;
  const listStr=listInp.value.trim();
  const nc=listStr?listStr.split(',').filter(s=>s.trim()).length:0;
  if(qc>0&&nc>0){{
    const total=qc*nc;
    const tStr=total%1===0?String(total):total.toFixed(2);
    if(qinp) qinp.value=tStr;
    if(totSpan){{const u=usel?usel.value:'und';totSpan.textContent='= '+tStr+' '+u;}}
  }} else {{
    if(totSpan) totSpan.textContent='';
  }}
  if(!state.cantidades) state.cantidades={{}};
  const qty=qinp?qinp.value.trim():'';
  const unit=usel?usel.value:'und';
  if(qty||casaInp.value||listStr) state.cantidades[id]={{qty,unit,qtyCasa:casaInp.value,casasList:listStr}};
  else delete state.cantidades[id];
  saveState(state);
}}

/* ═══════════ CONSOLIDACION ════════ */
function showConsolidacion() {{
  renderConsolidacion('');
  document.getElementById('consol-overlay').classList.add('open');
  const cs=document.getElementById('consol-search');
  cs.value=''; setTimeout(()=>cs.focus(),50);
}}
function closeConsolidacion() {{
  document.getElementById('consol-overlay').classList.remove('open');
}}
function renderConsolidacion(q) {{
  const all=allR();
  const pending=all.filter(r=>getStage(r)!=='SIT');
  const groups={{}};
  pending.forEach(r=>{{
    const mat=(r.material||r.titulo||'').trim()||'Sin clasificar';
    if(!groups[mat]) groups[mat]=[];
    groups[mat].push(r);
  }});
  const sq=q.toLowerCase().trim();
  const filtered=Object.entries(groups)
    .filter(([mat])=>!sq||mat.toLowerCase().includes(sq))
    .sort((a,b)=>b[1].length-a[1].length);
  const totalMats=filtered.length;
  const totalItems=filtered.reduce((s,[,rs])=>s+rs.length,0);
  const withQty=filtered.reduce((s,[,rs])=>s+rs.filter(r=>state.cantidades&&state.cantidades[r.id]&&state.cantidades[r.id].qty).length,0);
  document.getElementById('consol-summary').innerHTML=`
    <div><strong style="font-size:20px;display:block;line-height:1.1">${{totalMats}}</strong>materiales</div>
    <div><strong style="font-size:20px;display:block;line-height:1.1">${{totalItems}}</strong>restricciones pendientes</div>
    <div><strong style="font-size:20px;display:block;line-height:1.1">${{withQty}}</strong>con cantidad definida</div>
    <div style="flex:1"></div>
    <div style="font-size:11px;color:var(--ink-3);align-self:center;text-align:right">Clic en un material para expandir los frentes<br>Ingrese cantidades en cada tarjeta de restricción</div>
  `;
  document.getElementById('consol-list').innerHTML=filtered.length?filtered.map(([mat,rs])=>{{
    const qtys={{}};
    rs.forEach(r=>{{
      const c=state.cantidades&&state.cantidades[r.id];
      if(c&&c.qty){{const u=c.unit||'und';qtys[u]=(qtys[u]||0)+(parseFloat(c.qty)||0);}}
    }});
    const hasQty=rs.some(r=>state.cantidades&&state.cantidades[r.id]&&state.cantidades[r.id].qty);
    const allHaveQty=hasQty&&rs.every(r=>state.cantidades&&state.cantidades[r.id]&&state.cantidades[r.id].qty);
    const qtyStr=Object.entries(qtys).map(([u,v])=>`${{v%1===0?v:v.toFixed(2)}} ${{u}}`).join(' + ');
    return `<div class="consol-mat-card">
      <div class="consol-mat-head" onclick="this.closest('.consol-mat-card').classList.toggle('expanded')">
        <span class="consol-mat-name">${{mat}}</span>
        <span class="consol-mat-count">${{rs.length}} frente${{rs.length>1?'s':''}}</span>
        ${{hasQty?`<span class="consol-mat-qty ${{allHaveQty?'':'partial'}}" title="${{allHaveQty?'Total completo':'Total parcial — faltan cantidades'}}">${{allHaveQty?'':'~'}}${{qtyStr}}</span>`:'<span style="font-size:11px;color:var(--ink-3)">sin cantidades</span>'}}
        <svg width="9" height="9" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" style="color:var(--ink-3);flex-shrink:0;transition:transform .2s"><path d="M6 9l6 6 6-6"/></svg>
      </div>
      <div class="consol-mat-body">
        <div class="consol-frente-row" style="background:var(--zone-bg);font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)">
          <span>Frente</span><span>Etapa</span><span>Cantidad</span><span>Responsable</span><span>Fecha hito</span>
        </div>
        ${{rs.slice().sort((a,b)=>a.frente.localeCompare(b.frente)).map(r=>{{
          const stg=getStage(r);const c=state.cantidades&&state.cantidades[r.id];
          const qv=c&&c.qty?`${{c.qty}} ${{c.unit}}`:'';
          const nc=c&&c.casasList?c.casasList.split(',').filter(s=>s.trim()).length:0;
          const casaDetail=c&&c.qtyCasa&&nc>0?`<br><span style="font-size:10px;color:var(--ink-3);font-weight:400">(${{c.qtyCasa}}/c × ${{nc}} casas)</span>`:'';
          return `<div class="consol-frente-row">
            <span class="consol-frente-name">${{r.frente}}</span>
            <span><span class="consol-stage-mini sp-${{STAGE_CLS[stg]}}">${{STAGE_LABEL[stg]}}</span></span>
            <span class="consol-qty-cell ${{qv?'':'empty'}}">${{qv||'—'}}${{casaDetail}}</span>
            <span class="consol-resp-cell" title="${{getCustomResp(r)}}">${{getCustomResp(r)||'—'}}</span>
            <span class="consol-date-cell">${{fmtDate(getCustomDate(r))}}</span>
          </div>`;
        }}).join('')}}
      </div>
    </div>`;
  }}).join(''):'<p style="text-align:center;padding:48px;color:var(--ink-3)">No se encontraron materiales.</p>';
}}
function exportConsolidacion() {{
  const all=allR().filter(r=>getStage(r)!=='SIT');
  const rows=[['Material','Frente','Zona','Etapa','Cantidad','Unidad','Responsable','Fecha hito','Unidades','Compradas','Pendientes','% Comprado']];
  all.slice().sort((a,b)=>(a.material||a.titulo||'').localeCompare(b.material||b.titulo||'')).forEach(r=>{{
    const c=state.cantidades&&state.cantidades[r.id];
    const casas=getCasasArray(r.id,r.frente);
    const cp=state.compras&&state.compras[r.id]?state.compras[r.id]:{{}};
    const done=casas.filter(x=>cp[x]).length;
    const pct=casas.length?Math.round(done/casas.length*100)+'%':'';
    rows.push([r.material||r.titulo||'',r.frente,r.zona,STAGE_NAME[getStage(r)],
      c?c.qty:'',c?c.unit:'',getCustomResp(r),getCustomDate(r)||'',
      casas.length||'',done||'',casas.length-done||'',pct]);
  }});
  const tsv=rows.map(row=>row.map(v=>String(v).replace(/\\t/g,' ')).join('\\t')).join('\\n');
  navigator.clipboard.writeText(tsv).then(()=>{{
    const btn=document.querySelector('.consol-export');const orig=btn.innerHTML;
    btn.textContent='\\u2713 Copiado!';
    setTimeout(()=>{{btn.innerHTML=orig;}},2000);
  }}).catch(()=>{{
    const csv=rows.map(row=>row.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',')).join('\\n');
    const blob=new Blob(['\\uFEFF'+csv],{{type:'text/csv;charset=utf-8'}});
    const a=document.createElement('a');a.href=URL.createObjectURL(blob);
    a.download='restricciones_'+new Date().toISOString().slice(0,10)+'.csv';
    a.click();URL.revokeObjectURL(a.href);
  }});
}}
document.getElementById('consol-search').addEventListener('input',e=>renderConsolidacion(e.target.value));
document.addEventListener('keydown',e=>{{
  if(e.key==='Escape') {{
    if(document.getElementById('gantt-overlay').classList.contains('open')) closeGantt();
    else if(document.getElementById('consol-overlay').classList.contains('open')) closeConsolidacion();
  }}
}});

/* ═══════════ EXPORTAR ESTADO (sync Asana) ══════════ */
function exportState() {{
  const out = {{
    exportedAt: new Date().toISOString(),
    status: state.status||{{}},
    dates: state.dates||{{}},
    notes: state.notes||{{}},
    inicios: state.inicios||{{}},
    cantidades: state.cantidades||{{}},
  }};
  const json = JSON.stringify(out, null, 2);
  const blob = new Blob(['\\uFEFF'+json], {{type:'application/json;charset=utf-8'}});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'pt_estado_' + new Date().toISOString().slice(0,10) + '.json';
  a.click();
  URL.revokeObjectURL(a.href);
}}

/* ═══════════ GANTT ══════════ */
let _gs=null;
function saveInicio(id,val){{
  if(!state.inicios) state.inicios={{}};
  if(val) state.inicios[id]=val; else delete state.inicios[id];
  saveState(state);
  refreshGanttBar(+id);
}}
function refreshGanttBar(id){{
  if(!_gs) return;
  const r=allR().find(x=>x.id===id);
  if(!r) return;
  const el=document.querySelector(`[data-gbar="${{id}}"]`);
  if(el) el.innerHTML=_ganttBar(r);
}}
function _ganttBar(r){{
  if(!_gs) return '';
  const {{PX,TW,xpx,gridLines,weekGL,todayLine,today,todayX}}=_gs;
  const stg=getStage(r); const cls=STAGE_CLS[stg];
  const dueStr=getCustomDate(r);
  const iniStr=(state.inicios&&state.inicios[r.id])||'';
  const hasDue=!!dueStr, hasIni=!!iniStr;
  let x1,x2;
  if(hasIni) x1=xpx(new Date(iniStr+'T00:00:00')); else x1=todayX;
  if(hasDue) x2=xpx(new Date(dueStr+'T00:00:00')); else x2=Math.min(TW,x1+PX*60);
  const w=Math.max(6,x2-x1);
  const due=hasDue?new Date(dueStr+'T00:00:00'):null;
  const overdue=due&&due<today;
  const striped=overdue?';background-image:repeating-linear-gradient(45deg,transparent,transparent 4px,rgba(0,0,0,.22) 4px,rgba(0,0,0,.22) 8px)':'';
  const lbl=r.material||r.titulo||'';
  let h=gridLines+weekGL+todayLine;
  if(!hasDue&&!hasIni){{
    h+=`<span style="position:absolute;left:${{todayX+6}}px;top:50%;transform:translateY(-50%);font-size:9px;color:var(--ink-3);font-style:italic">sin fecha</span>`;
    return h;
  }}
  const tip=`${{lbl}} | ${{STAGE_NAME[stg]}}${{hasIni?' inicio:'+iniStr:''}}${{hasDue?' → '+fmtDate(dueStr):''}}${{overdue?' ⚠ VENCIDA':''}}`;
  h+=`<div title="${{tip}}" style="position:absolute;left:${{x1}}px;width:${{w}}px;top:7px;bottom:7px;border-radius:3px;background:var(--${{cls}})${{striped}};z-index:2;box-shadow:0 1px 3px rgba(0,0,0,.18)">`;
  if(w>60&&hasDue){{
    const dlbl=fmtDate(dueStr).replace(' ',' ');
    h+=`<span style="position:absolute;right:4px;top:50%;transform:translateY(-50%);font-size:8px;font-weight:700;color:rgba(255,255,255,.93);white-space:nowrap;pointer-events:none">${{dlbl}}</span>`;
  }}
  if(hasIni){{
    const ilbl=new Date(iniStr+'T00:00:00').toLocaleDateString('es-CR',{{day:'2-digit',month:'short'}}).replace(' ',' ');
    h+=`<span style="position:absolute;left:3px;top:50%;transform:translateY(-50%);font-size:8px;font-weight:700;color:rgba(255,255,255,.93);white-space:nowrap;pointer-events:none">${{ilbl}}</span>`;
  }}
  h+='</div>';
  if(hasDue){{
    const mx=xpx(due);
    h+=`<div title="Vence: ${{fmtDate(dueStr)}}" style="position:absolute;left:${{mx-4}}px;top:50%;transform:translateY(-50%) rotate(45deg);width:9px;height:9px;background:var(--${{cls}});border:2px solid var(--surface);z-index:4;pointer-events:none"></div>`;
  }}
  if(!hasDue){{
    h+=`<div style="position:absolute;left:${{x1+w-1}}px;top:50%;transform:translateY(-50%);font-size:12px;color:var(--${{cls}});z-index:4;pointer-events:none;font-weight:700">&#x2192;</div>`;
  }}
  return h;
}}
function openGantt(){{
  document.getElementById('gantt-overlay').classList.add('open');
  renderGantt();
}}
function closeGantt(){{
  document.getElementById('gantt-overlay').classList.remove('open');
}}
function renderGantt(){{
  const PX=6;
  const today=TODAY;
  const active=allR().filter(r=>getStage(r)!=='SIT');

  // Date range — include both due dates and start dates
  const allDts=[
    ...active.map(r=>getCustomDate(r)).filter(Boolean),
    ...active.map(r=>state.inicios&&state.inicios[r.id]).filter(Boolean)
  ].map(s=>new Date(s+'T00:00:00'));
  const rangeStart=new Date(today.getFullYear(),today.getMonth()-1,1);
  let rangeEnd;
  if(allDts.length){{
    const maxD=new Date(Math.max(...allDts));
    rangeEnd=new Date(Math.max(
      new Date(today.getFullYear(),today.getMonth()+5,1).getTime(),
      new Date(maxD.getFullYear(),maxD.getMonth()+2,1).getTime()
    ));
  }} else {{
    rangeEnd=new Date(today.getFullYear(),today.getMonth()+5,1);
  }}

  const totalDays=Math.round((rangeEnd-rangeStart)/86400000);
  const TW=totalDays*PX;
  const LW=218;
  function xpx(d){{ return Math.max(0,Math.min(TW,Math.round((d-rangeStart)/86400000)*PX)); }}
  const todayX=xpx(today);

  // Month grid lines + headers
  const months=[];
  let mc=new Date(rangeStart.getFullYear(),rangeStart.getMonth(),1);
  while(mc<rangeEnd){{ months.push(new Date(mc)); mc=new Date(mc.getFullYear(),mc.getMonth()+1,1); }}

  const gridLines=months.map(m=>`<div style="position:absolute;left:${{xpx(m)}}px;top:0;bottom:0;width:1px;background:var(--border);opacity:.5;pointer-events:none"></div>`).join('');

  // Week grid lines + labels (every Monday)
  const weekGridLines=[];
  const weekLabels=[];
  let wd=new Date(rangeStart);
  while(wd.getDay()!==1) wd=new Date(wd.getTime()+86400000);
  while(wd<rangeEnd){{
    const wx=xpx(wd);
    weekGridLines.push(`<div style="position:absolute;left:${{wx}}px;top:0;bottom:0;width:1px;border-left:1px dashed rgba(128,128,128,.3);pointer-events:none"></div>`);
    const wlbl=wd.getDate()+'\\u00a0'+wd.toLocaleDateString('es-CR',{{month:'short'}}).slice(0,3);
    weekLabels.push(`<div style="position:absolute;left:${{wx}}px;width:${{PX*7}}px;top:0;bottom:0;border-left:1px dashed rgba(128,128,128,.25);display:flex;align-items:center;padding-left:2px;font-size:8px;color:var(--ink-3);white-space:nowrap;overflow:hidden">${{wlbl}}</div>`);
    wd=new Date(wd.getTime()+86400000*7);
  }}
  const weekGL=weekGridLines.join('');
  const weekHd=weekLabels.join('');

  const todayLine=`<div style="position:absolute;left:${{todayX}}px;top:0;bottom:0;width:2px;background:var(--accent);opacity:.75;z-index:3;pointer-events:none"></div>`;

  // Cache state for refreshGanttBar
  _gs={{PX,TW,LW,xpx,gridLines,weekGL,todayLine,today,todayX,rangeStart}};

  // Month header
  const monthHd=months.map((m,i)=>{{
    const nx=i+1<months.length?xpx(months[i+1]):TW;
    const w=nx-xpx(m);
    return `<div style="position:absolute;left:${{xpx(m)}}px;width:${{w}}px;top:0;height:22px;border-right:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:800;color:var(--ink-2);overflow:hidden;white-space:nowrap;background:var(--surface)">${{m.toLocaleDateString('es-CR',{{month:'long',year:'2-digit'}})}}</div>`;
  }}).join('');

  // Legend
  document.getElementById('gantt-legend').innerHTML=STAGES.filter(s=>s!=='SIN_INICIAR').map(s=>
    `<div class="g-leg-item"><div class="g-leg-dot" style="background:var(--${{STAGE_CLS[s]}})"></div>${{STAGE_NAME[s]}}</div>`
  ).join('')+`<div class="g-leg-item"><div class="g-leg-dot" style="background:var(--accent)"></div>Hoy</div>`;

  // Build header (2 rows: months + weeks)
  let html=`<div style="display:flex;position:sticky;top:0;z-index:12;background:var(--surface);border-bottom:2px solid var(--border)">
    <div style="width:${{LW}}px;flex-shrink:0;border-right:1px solid var(--border);position:sticky;left:0;background:var(--surface);z-index:15">
      <div style="padding:4px 8px;font-size:10px;font-weight:700;color:var(--ink-2);height:22px;display:flex;align-items:center;border-bottom:1px solid var(--border)">Restricción</div>
      <div style="padding:2px 8px;font-size:8px;color:var(--ink-3);height:20px;display:flex;align-items:center">Inicio → Hito &#x25C6;</div>
    </div>
    <div style="width:${{TW}}px;flex-shrink:0;position:relative;overflow:hidden">
      <div style="height:22px;position:relative">${{monthHd}}<div style="position:absolute;left:${{todayX}}px;top:0;bottom:0;width:2px;background:var(--accent);opacity:.75"></div></div>
      <div style="height:20px;position:relative;border-top:1px solid var(--border)">${{weekHd}}<div style="position:absolute;left:${{todayX}}px;top:0;bottom:0;width:2px;background:var(--accent);opacity:.75"></div></div>
    </div>
  </div>`;

  // Content rows
  Object.entries(FRENTES_BY_ZONE).forEach(([zona,frentes])=>{{
    let zr='';
    frentes.forEach(f=>{{
      const rs=active.filter(r=>r.zona===zona&&r.frente===f.nombre);
      if(!rs.length) return;
      zr+=`<div style="display:flex;background:var(--zone-bg)">
        <div style="width:${{LW}}px;flex-shrink:0;padding:3px 8px;font-size:10px;font-weight:700;color:var(--ink-2);border-right:1px solid var(--border);border-bottom:1px solid var(--border);position:sticky;left:0;background:var(--zone-bg);z-index:5">${{f.nombre}}</div>
        <div style="width:${{TW}}px;flex-shrink:0;height:22px;border-bottom:1px solid var(--border);position:relative;overflow:hidden">${{gridLines}}${{weekGL}}${{todayLine}}</div>
      </div>`;
      rs.forEach(r=>{{
        const stg=getStage(r); const cls=STAGE_CLS[stg];
        const iniStr=(state.inicios&&state.inicios[r.id])||'';
        const od=daysOverdue(r);
        const lbl=(r.material||r.titulo||'').substring(0,36);
        zr+=`<div style="display:flex;min-height:42px">
          <div style="width:${{LW}}px;flex-shrink:0;padding:3px 6px;border-right:1px solid var(--border);border-bottom:1px solid var(--border);display:flex;flex-direction:column;justify-content:center;gap:3px;overflow:hidden;position:sticky;left:0;background:var(--surface);z-index:5">
            <div style="display:flex;align-items:center;gap:4px;overflow:hidden">
              <span style="flex-shrink:0;padding:1px 4px;border-radius:3px;font-size:8px;font-weight:700;background:var(--${{cls}}-bg);color:var(--${{cls}});line-height:1.4">${{STAGE_LABEL[stg]}}</span>
              <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:10px;color:var(--ink);min-width:0" title="${{r.material||r.titulo||''}}">${{lbl}}</span>
              ${{od>0?`<span style="flex-shrink:0;font-size:8px;color:var(--pro);font-weight:700">⚠</span>`:''}}
            </div>
            <div style="display:flex;align-items:center;gap:3px">
              <span style="font-size:8px;color:var(--ink-3);flex-shrink:0">Inicio:</span>
              <input type="date" value="${{iniStr}}" style="font-size:8px;border:1px solid var(--border);border-radius:3px;padding:1px 2px;background:var(--surface);color:var(--ink);width:100px;flex-shrink:0" onchange="saveInicio(${{r.id}},this.value)" title="Fecha de inicio de la actividad">
            </div>
          </div>
          <div data-gbar="${{r.id}}" style="width:${{TW}}px;flex-shrink:0;min-height:42px;border-bottom:1px solid var(--border);position:relative;overflow:hidden">
            ${{_ganttBar(r)}}
          </div>
        </div>`;
      }});
    }});
    if(zr){{
      html+=`<div style="display:flex;background:var(--accent)">
        <div style="width:${{LW}}px;flex-shrink:0;padding:4px 8px;font-size:10px;font-weight:800;color:#fff;letter-spacing:.05em;text-transform:uppercase;position:sticky;left:0;background:var(--accent);z-index:5">${{zona}}</div>
        <div style="width:${{TW}}px;flex-shrink:0;height:24px;position:relative;overflow:hidden">${{gridLines}}</div>
      </div>`+zr;
    }}
  }});
  document.getElementById('gantt-body').innerHTML=html;
}}

let theme=window.matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';
document.getElementById('theme-btn').addEventListener('click',()=>{{
  theme=theme==='dark'?'light':'dark';
  document.documentElement.setAttribute('data-theme',theme);
  document.getElementById('theme-btn').textContent=theme==='dark'?'☀':'☾';
}});
renderAll();
</script>'''

out_path = HERE / 'index.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"HTML generado: {len(html):,} bytes")
