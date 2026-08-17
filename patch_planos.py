"""
Parche: agrega vista de planos de sitio al artifact.
Modifica build_guide.py con hotspots de La Pampa y zonas de Los Parques.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
bg   = (HERE / 'build_guide.py').read_text(encoding='utf-8')

# ── 1. Python data-loading (after the with open restricciones block) ─────────
PYTHON_LOAD = '''
# ── Planos data ─────────────────────────────────────────────────
_planos_path = HERE / 'planos_data.json'
if _planos_path.exists():
    with open(_planos_path, encoding='utf-8') as _pf:
        _planos = json.load(_pf)
    _pampa_b64   = _planos['la_pampa']['b64']
    _parques_b64 = _planos['los_parques']['b64']
    _pampa_hs    = _planos['la_pampa']['hotspots']
else:
    _pampa_b64 = _parques_b64 = ''
    _pampa_hs  = []

_PARQUES_ZONES = [
    {"frente":"THS P1",      "label":"THS P1", "xPct":42.5,"yPct":9.5, "wPct":20, "hPct":15},
    {"frente":"AP1 P1",      "label":"AP1 P1", "xPct":67,  "yPct":9.5, "wPct":22, "hPct":7 },
    {"frente":"AP2 P1",      "label":"AP2 P1", "xPct":60,  "yPct":18.5,"wPct":27, "hPct":6 },
    {"frente":"THS P2",      "label":"THS P2", "xPct":22,  "yPct":19,  "wPct":17, "hPct":12},
    {"frente":"THC P2",      "label":"THC P2", "xPct":38,  "yPct":18.5,"wPct":9,  "hPct":11},
    {"frente":"Tempisque P2","label":"TMP P2", "xPct":27,  "yPct":30,  "wPct":13, "hPct":7 },
    {"frente":"Casitas P2",  "label":"CAS P2", "xPct":12,  "yPct":27,  "wPct":9,  "hPct":11},
    {"frente":"APP3 P3",     "label":"APP3",   "xPct":72,  "yPct":30,  "wPct":17, "hPct":33},
    {"frente":"THC P3P4",    "label":"THC P3", "xPct":46.5,"yPct":31,  "wPct":9,  "hPct":5 },
    {"frente":"THS P4",      "label":"THS P4", "xPct":22,  "yPct":41,  "wPct":24, "hPct":18},
    {"frente":"Tempisque P4","label":"TMP P4", "xPct":41,  "yPct":44,  "wPct":18, "hPct":12},
    {"frente":"Casitas P3",  "label":"CAS P3", "xPct":15,  "yPct":46,  "wPct":9,  "hPct":6 },
    {"frente":"Vereda P2",   "label":"VER P2", "xPct":2.5, "yPct":46,  "wPct":12, "hPct":28},
]
_parques_hs   = _PARQUES_ZONES
_pampa_hs_js  = json.dumps(_pampa_hs,   ensure_ascii=False)
_parques_hs_js= json.dumps(_parques_hs, ensure_ascii=False)
'''

OLD_LOAD = "r_js = json.dumps(restricciones, ensure_ascii=False)"
NEW_LOAD = PYTHON_LOAD.strip() + "\n\n" + OLD_LOAD
bg = bg.replace(OLD_LOAD, NEW_LOAD, 1)

# ── 2. CSS (before </style>) ─────────────────────────────────────────────────
CSS = '''
/* ── Planos overlay ────────────────────────────────── */
#planos-overlay{{position:fixed;inset:0;background:var(--bg);z-index:300;display:none;flex-direction:column;overflow:hidden}}
#planos-overlay.open{{display:flex}}
#planos-top{{background:var(--accent);padding:0 16px;display:flex;align-items:center;gap:10px;height:52px;flex-shrink:0;overflow-x:auto}}
#planos-top h2{{font-size:13px;font-weight:700;color:#fff;white-space:nowrap;margin-right:4px}}
.pln-tab{{font-size:12px;font-weight:700;padding:5px 14px;border-radius:5px;color:rgba(255,255,255,.65);transition:all .12s;white-space:nowrap;flex-shrink:0}}
.pln-tab.active{{background:rgba(255,255,255,.22);color:#fff}}
#plano-hint{{font-size:10px;color:rgba(255,255,255,.5);white-space:nowrap;flex:1;text-align:center}}
.pln-close{{width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;flex-shrink:0}}
.pln-close:hover{{background:rgba(255,255,255,.25)}}
#planos-body{{flex:1;display:flex;overflow:hidden}}
#plano-map{{flex:1;overflow:auto;position:relative;background:var(--zone-bg);display:flex;align-items:flex-start;justify-content:center;padding:12px}}
#plano-img{{max-width:900px;width:100%;display:block;height:auto;border-radius:4px;box-shadow:var(--sh2)}}
.plano-svg-layer{{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none}}
#frente-panel{{width:0;overflow:hidden;background:var(--surface);border-left:1px solid var(--border);transition:width .22s ease;display:flex;flex-direction:column;flex-shrink:0}}
#frente-panel.open{{width:320px}}
#fp-top{{padding:12px 14px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:8px;flex-shrink:0;min-width:320px}}
#fp-name{{font-size:14px;font-weight:800;color:var(--ink);flex:1}}
#fp-count{{font-size:10px;color:var(--ink-3);background:var(--zone-bg);padding:2px 8px;border-radius:10px;white-space:nowrap}}
#fp-close{{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--ink-2);font-size:12px;flex-shrink:0}}
#fp-close:hover{{background:var(--zone-bg)}}
#fp-body{{flex:1;overflow-y:auto;padding:10px 14px;display:flex;flex-direction:column;gap:7px;min-width:320px}}
.fp-card{{background:var(--bg);border:1px solid var(--border);border-radius:var(--r);padding:9px 11px;cursor:pointer;transition:border-color .12s}}
.fp-card:hover{{border-color:var(--accent-mid);background:var(--accent-faint)}}
.fp-mat{{font-size:12px;font-weight:700;color:var(--ink);line-height:1.3;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.fp-sub{{font-size:10px;color:var(--ink-3);margin-top:1px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.fp-row{{display:flex;align-items:center;gap:5px;margin-top:5px}}
.fp-stage{{font-size:9px;font-weight:800;padding:2px 6px;border-radius:3px;color:#fff;flex-shrink:0}}
.fp-resp{{font-size:10px;color:var(--ink-3);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.fp-date{{font-size:10px;color:var(--ink-3);white-space:nowrap}}
.fp-empty{{text-align:center;color:var(--ink-3);font-size:12px;padding:24px 8px}}
'''

bg = bg.replace('</style>', CSS + '</style>', 1)

# ── 3. Topbar button (before the Gantt button) ───────────────────────────────
OLD_GANTT_BTN = '''  <button id="gantt-btn" onclick="openGantt()" title="Ver diagrama Gantt">'''
NEW_GANTT_BTN = '''  <button id="planos-btn" onclick="openPlanos()" title="Ver planos de sitio">
    <svg width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 6l9-3 9 3v12l-9 3-9-3z"/><path d="M12 3v18"/><path d="M3 6l9 3 9-3"/></svg>
    Planos
  </button>
  <button id="gantt-btn" onclick="openGantt()" title="Ver diagrama Gantt">'''
bg = bg.replace(OLD_GANTT_BTN, NEW_GANTT_BTN, 1)

# ── 4. Planos overlay HTML (after Gantt overlay closing div) ─────────────────
OLD_AFTER_GANTT = '''<script>'''
NEW_AFTER_GANTT = '''<!-- Planos overlay -->
<div id="planos-overlay">
  <div id="planos-top">
    <h2>Planos de Sitio</h2>
    <button class="pln-tab active" onclick="switchPlan('pampa')">La Pampa</button>
    <button class="pln-tab" onclick="switchPlan('parques')">Los Parques</button>
    <span id="plano-hint">Haga clic sobre una vivienda para ver sus restricciones</span>
    <button class="pln-close" onclick="closePlanos()" title="Cerrar (Esc)">&#x2715;</button>
  </div>
  <div id="planos-body">
    <div id="plano-map">
      <img id="plano-img" src="" alt="Plano de sitio" style="max-width:900px;width:100%;display:block;height:auto;border-radius:4px">
    </div>
    <div id="frente-panel">
      <div id="fp-top">
        <span id="fp-name">Frente</span>
        <span id="fp-count"></span>
        <button id="fp-close" onclick="closeFrentePanel()">&#x2715;</button>
      </div>
      <div id="fp-body"></div>
    </div>
  </div>
</div>

<script>'''
bg = bg.replace(OLD_AFTER_GANTT, NEW_AFTER_GANTT, 1)

# ── 5. JS constants + functions (before renderAll()) ─────────────────────────
JS_PLANOS = '''/* ════════ PLANOS ════════ */
const PLANO_PAMPA_B64    = "data:image/jpeg;base64,{_pampa_b64}";
const PLANO_PARQUES_B64  = "data:image/jpeg;base64,{_parques_b64}";
const PLANO_PAMPA_HS     = {_pampa_hs_js};
const PLANO_PARQUES_HS   = {_parques_hs_js};
const FRENTE_COLOR = {{
  "Aurora 500":"#4472C4","Serena 500":"#70AD47","Tempisque 500":"#ED7D31",
  "Tempisque 600":"#C9A800","Solana C":"#5B9BD5","Solana U":"#C55A11",
  "THS P1":"#4472C4","THS P2":"#5B9BD5","THS P4":"#7BA5CE",
  "AP1 P1":"#70AD47","AP2 P1":"#4E9B30","APP3 P3":"#2D8653",
  "THC P2":"#ED7D31","THC P3P4":"#C55A11",
  "Tempisque P2":"#C9A800","Tempisque P4":"#8A7000",
  "Casitas P2":"#9B59B6","Casitas P3":"#7B3F9B",
  "Vereda P2":"#E05050",
}};
let _curPlan = 'pampa';
let _hsSvg   = null;

function openPlanos() {{
  document.getElementById('planos-overlay').classList.add('open');
  _renderPlan('pampa');
  document.addEventListener('keydown', _planoKey);
}}
function closePlanos() {{
  document.getElementById('planos-overlay').classList.remove('open');
  document.removeEventListener('keydown', _planoKey);
}}
function _planoKey(e) {{ if(e.key==='Escape') closePlanos(); }}

function switchPlan(plan) {{
  _curPlan = plan;
  document.querySelectorAll('.pln-tab').forEach((btn,i)=>{{
    btn.classList.toggle('active',(plan==='pampa')?i===0:i===1);
  }});
  closeFrentePanel();
  _renderPlan(plan);
}}

function _renderPlan(plan) {{
  const img = document.getElementById('plano-img');
  img.onload = _drawHotspots;
  img.src = plan==='pampa' ? PLANO_PAMPA_B64 : PLANO_PARQUES_B64;
  if(img.complete && img.naturalWidth) _drawHotspots();
}}

function _drawHotspots() {{
  const img  = document.getElementById('plano-img');
  const map  = document.getElementById('plano-map');
  const W    = img.offsetWidth;
  const H    = img.offsetHeight;
  const offX = img.offsetLeft;
  const offY = img.offsetTop;

  if(_hsSvg) _hsSvg.remove();
  const svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
  svg.setAttribute('class','plano-svg-layer');
  svg.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none';
  map.appendChild(svg);
  _hsSvg = svg;

  const hs = _curPlan==='pampa' ? PLANO_PAMPA_HS : PLANO_PARQUES_HS;
  hs.forEach(h=>{{
    const col  = FRENTE_COLOR[h.frente]||'#888';
    const x    = offX + (h.xPct/100)*W;
    const y    = offY + (h.yPct/100)*H;
    const rw   = (h.wPct/100)*W;
    const rh   = (h.hPct/100)*H;
    const lbl  = h.unit||h.label||h.frente;

    const rect = document.createElementNS('http://www.w3.org/2000/svg','rect');
    rect.setAttribute('x',x.toFixed(1));
    rect.setAttribute('y',y.toFixed(1));
    rect.setAttribute('width',rw.toFixed(1));
    rect.setAttribute('height',rh.toFixed(1));
    rect.setAttribute('fill',col);
    rect.setAttribute('fill-opacity','0.22');
    rect.setAttribute('stroke',col);
    rect.setAttribute('stroke-width','1.5');
    rect.setAttribute('rx','3');
    rect.style.cssText='cursor:pointer;pointer-events:all;transition:fill-opacity .12s';
    rect.addEventListener('mouseenter',()=>rect.setAttribute('fill-opacity','0.45'));
    rect.addEventListener('mouseleave',()=>rect.setAttribute('fill-opacity','0.22'));
    rect.addEventListener('click',()=>selectFrente(h.frente));
    const t = document.createElementNS('http://www.w3.org/2000/svg','title');
    t.textContent=h.frente+(h.unit?' (#'+h.unit+')':'');
    rect.appendChild(t);
    svg.appendChild(rect);

    if(rw>24){{
      const txt = document.createElementNS('http://www.w3.org/2000/svg','text');
      txt.setAttribute('x',(x+rw/2).toFixed(1));
      txt.setAttribute('y',(y+rh/2).toFixed(1));
      txt.setAttribute('text-anchor','middle');
      txt.setAttribute('dominant-baseline','middle');
      txt.setAttribute('font-size',Math.min(10,rh/1.8,rw/lbl.length*1.6).toFixed(1));
      txt.setAttribute('font-weight','700');
      txt.setAttribute('fill',col);
      txt.setAttribute('font-family','Segoe UI,sans-serif');
      txt.style.pointerEvents='none';
      txt.style.userSelect='none';
      txt.textContent=lbl;
      svg.appendChild(txt);
    }}
  }});
}}

function selectFrente(frente) {{
  const rs = allR().filter(r=>r.frente===frente);
  document.getElementById('fp-name').textContent = frente;
  document.getElementById('fp-count').textContent = rs.length+' restricciones';
  const body = document.getElementById('fp-body');
  if(rs.length===0){{
    body.innerHTML='<p class="fp-empty">Sin restricciones registradas.</p>';
  }} else {{
    body.innerHTML = rs.map(r=>{{
      const stg  = getStage(r);
      const cls  = STAGE_CLS[stg]||'sin';
      const mat  = r.material||r.titulo||'(Sin título)';
      const sub  = r.frente+(r.actividad?' — '+r.actividad:'');
      const resp = getCustomResp(r);
      const fecha= getCustomDate(r)||'';
      return `<div class="fp-card" onclick="goToCard(${{r.id}})">
        <div class="fp-mat">${{mat}}</div>
        <div class="fp-sub">${{sub}}</div>
        <div class="fp-row">
          <span class="fp-stage" style="background:var(--${{cls}})">${{STAGE_LABEL[stg]}}</span>
          <span class="fp-resp">${{resp}}</span>
          ${{fecha?`<span class="fp-date">${{fecha.slice(0,7)}}</span>`:''}}
        </div>
      </div>`;
    }}).join('');
  }}
  document.getElementById('frente-panel').classList.add('open');
}}

function closeFrentePanel(){{
  document.getElementById('frente-panel').classList.remove('open');
}}

function goToCard(id){{
  closePlanos();
  setTimeout(()=>{{
    const el=document.querySelector('[data-id="'+id+'"]');
    if(!el)return;
    const frenteContent=el.closest('.frente')?.querySelector('.frente-content');
    if(frenteContent&&frenteContent.style.display==='none'){{
      el.closest('.frente')?.querySelector('.frente-btn')?.click();
    }}
    el.scrollIntoView({{behavior:'smooth',block:'center'}});
    el.style.outline='2px solid var(--accent)';
    el.style.transition='outline .5s';
    setTimeout(()=>el.style.outline='',2000);
  }},200);
}}

window.addEventListener('resize',()=>{{
  if(document.getElementById('planos-overlay').classList.contains('open')){{
    _drawHotspots();
  }}
}});

'''

# Replace the LAST standalone renderAll(); (before </script>)
# Use the theme-button block as the anchor to find the right insertion point
OLD_RENDER_ALL = "renderAll();\n</script>'''"
NEW_RENDER_ALL  = JS_PLANOS + "renderAll();\n</script>'''"
if OLD_RENDER_ALL in bg:
    bg = bg.replace(OLD_RENDER_ALL, NEW_RENDER_ALL, 1)
else:
    raise ValueError("Could not find insertion anchor 'renderAll();\\n</script>\\''''")

# ── 6. Write result ──────────────────────────────────────────────────────────
(HERE / 'build_guide.py').write_text(bg, encoding='utf-8')
print("Patch OK — build_guide.py actualizado")
print(f"  Tamaño: {len(bg)//1024} KB")
