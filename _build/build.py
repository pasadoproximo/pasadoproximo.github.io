#!/usr/bin/env python3
"""Genera la portada, el índice de proyectos y una página por proyecto.

Uso:  python3 _build/build.py   (desde la raíz del repositorio)
El contenido está en _build/data.py. Las animaciones de cada tarjeta se toman
de _build/source_old.html (la portada anterior), para no duplicar el código.
"""
import os, re, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import P, BY, CATS, FEATURED, ICON_EXT, ICON_DL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = open(os.path.join(ROOT, "_build/source_old.html"), encoding="utf-8").read()
SITE = "https://pasadoproximo.github.io"


def balanced(t, start, tag="div"):
    depth = 0
    for m in re.finditer(r"<(/?)%s\b[^>]*>" % tag, t[start:]):
        depth += 1 if m.group(1) == "" else -1
        if depth == 0:
            return t[start:start + m.end()]
    raise ValueError("sin cierre")


def grab(cls):
    i = SRC.index('<div class="%s' % cls)
    return balanced(SRC, i)


def absolutize(h):
    return (h.replace('src="assets/', 'src="/assets/')
             .replace('href="assets/', 'href="/assets/')
             .replace('src="herramientas/', 'src="/herramientas/'))


# ---------- visuales de las tarjetas (reutilizados de la portada anterior)
VIZ = {}
for k in ["v-chat", "v-bulos", "v-nube", "v-1812", "v-aud", "v-bombo", "v-esc", "v-rub", "v-cos", "v-epo", "v-caja"]:
    VIZ[k] = absolutize(grab("viz " + k))
mapsvg = SRC[SRC.index('<svg class="mini-map"'):]
mapsvg = mapsvg[:mapsvg.index("</svg>") + 6]
claude_chip = '<div class="made"><span><img src="/assets/tools/claude.png" alt="" width="20" height="20" loading="lazy">Claude</span></div>'
VIZ["map"] = '<div class="viz v-map" aria-hidden="true">%s%s</div>' % (claude_chip, mapsvg)
council = SRC[SRC.index('<div class="council"'):]
council = balanced(council, 0)
VIZ["council"] = '<div class="viz v-council" aria-hidden="true">%s</div>' % council.replace(' role="img" aria-label="Heródoto, Tucídides, Hannah Arendt, Clío, Sócrates e Ibn Jaldún"', "")


def viz(p):
    v = p["viz"]
    if v.startswith("img:"):
        return '<div class="viz v-img" aria-hidden="true"><img src="%s" alt="" loading="lazy"></div>' % v[4:]
    return VIZ[v]


def url(p):
    return p.get("ext") or "/proyectos/%s/" % p["slug"]


# ---------- piezas comunes
LOGO = '<svg width="22" height="22" viewBox="0 0 26 26"><path d="M13 2 2 7h22L13 2Z" fill="#fff"/><rect x="3" y="8" width="20" height="2" fill="#fff"/><rect x="5" y="11" width="2.4" height="9" fill="#fff"/><rect x="9.6" y="11" width="2.4" height="9" fill="#fff"/><rect x="14" y="11" width="2.4" height="9" fill="#fff"/><rect x="18.6" y="11" width="2.4" height="9" fill="#fff"/><rect x="2" y="21" width="22" height="2.4" fill="#fff"/></svg>'
FAVICON = re.search(r'<link rel="icon"[^>]*>', SRC).group(0)
FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+SC:wght@700&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&display=swap">'''
CSSV = "24"


def head(title, desc, path, og="/assets/og.jpg"):
    t = html.escape(title)
    d = html.escape(desc)
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
{FAVICON}
{FONTS}
<link rel="stylesheet" href="/assets/site.css?v={CSSV}">
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="wrap">'''


def topbar(active=""):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f'''
<header class="top">
 <div class="bar">
  <a class="brand" href="/" aria-label="Inicio · Jorge Delgado Aguilera"><span class="logo" aria-hidden="true">{LOGO}</span></a>
  <nav aria-label="Principal">
   {a("/proyectos/", "Proyectos", "proyectos").replace("<a ", "<a class=\"nav-key\" ",1)}
   {a("/#sobre-mi", "Sobre mí", "sobre")}
   {a("/herramientas/", "Caja de herramientas", "herr")}
   <a class="cv" href="/assets/pdf/CV-Jorge-Delgado-Aguilera.pdf" download aria-label="Descargar CV (PDF)">CV <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg></a>
   <a class="hire" href="/#contacto">Contacto</a>
  </nav>
 </div>
</header>
'''


def foot():
    return '''
<footer><span>© 2026 Jorge Delgado Aguilera</span><span>Campanillas, Málaga</span></footer>
</div>
<script src="/assets/site.js?v=''' + CSSV + '''" defer></script>
</body>
</html>
'''


def card(p, lvl="h3"):
    tags = " · ".join(html.escape(t) for t in p["tags"][:2])
    return f'''<a class="t pc lift rv" href="{url(p)}">
 <span class="arrow" aria-hidden="true">{ICON_EXT}</span>
 {viz(p)}
 <div class="pc-tags">{tags}</div>
 <{lvl}>{p["title"]}</{lvl}>
 <p>{p["card"]}</p>
</a>'''


def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)
    print("·", path)


# ================================================================= PORTADA
def section(id_):
    i = SRC.index(f'<section class="sec" id="{id_}">') if f'<section class="sec" id="{id_}">' in SRC else SRC.index(f'<section class="sec bento" id="{id_}">')
    return absolutize(balanced(SRC, i, "section"))


def home():
    exp = section("experiencia")
    form = section("formacion")
    contact = section("contacto")
    # dentro de «Sobre mí» los bloques usan h3 en vez de h2
    exp = exp.replace('<span class="lab">Experiencia docente</span><h2>En el aula</h2>', '<span class="lab">Experiencia docente</span><h3 class="h3big">En el aula</h3>')
    form = form.replace('<span class="lab">Formación</span><h2>De la Historia al aula digital</h2>', '<span class="lab">Formación</span><h3 class="h3big">De la Historia al aula digital</h3>')
    form = form.replace('<br><em>Matrícula de Honor en el TFM</em>', '')
    form = form.replace('<em>TFM: asistente GPT para 2.º ESO</em>', '<em><a href="/proyectos/asistente-gpt-2eso/">TFM: asistente de IA para 2.º ESO</a></em>')
    exp = exp.replace('<li>Repositorio digital para todo el claustro.</li>', '<li><a href="/proyectos/repositorio-digital/">Repositorio digital</a> para todo el claustro.</li>')
    # «Con qué trabajo»: en vez de las cintas de texto, una rejilla fija de logos agrupada por uso
    def grupo(titulo, items, nota=""):
        lis = "".join(f'<li><img src="/herramientas/logos/{f}.png" alt="" width="40" height="40" loading="lazy"><span>{n}</span></li>' for n, f in items)
        extra = f'<p class="tg-note">{nota}</p>' if nota else ""
        return f'<div class="tg"><span class="lab">{titulo}</span><ul>{lis}</ul>{extra}</div>'
    tools = '<div class="tgrid">' + "".join([
        grupo("Inteligencia artificial", [("Claude", "claude"), ("ChatGPT", "chatgpt"), ("Gemini", "gemini"), ("Copilot", "copilot"), ("NotebookLM", "notebooklm")]),
        grupo("Aula virtual", [("Moodle", "moodle"), ("Classroom", "classroom"), ("Teams", "teams")]),
        grupo("Crear y evaluar", [("Genially", "genially"), ("Canva", "canva"), ("Book Creator", "bookcreator"), ("CapCut", "capcut"),
                                  ("Kahoot", "kahoot"), ("Mentimeter", "mentimeter"), ("Wooclap", "wooclap"), ("Edpuzzle", "edpuzzle"), ("Jotform", "jotform")]),
        grupo("E-learning", [("Articulate Rise 360", "articulate"), ("Articulate Storyline 360", "articulate"), ("H5P", "h5p")]),
    ]) + '</div>'
    form = re.sub(r'(<div class="marq( rev)?" aria-label="[^"]*"><div class="track">.*?</div></div>\s*)+', tools, form, count=1, flags=re.S)
    form = form.replace('<h3 class="big" style="margin-top:8px">Con qué trabajo</h3>', '<h3 class="big h3big" style="margin-top:8px">Con qué trabajo</h3>')
    feat = "\n".join(card(BY[s]) for s in FEATURED)
    body = f'''
<main id="contenido">
 <section class="bento hero2" aria-label="Presentación">
  <div class="t dark h2-main rv">
   <span class="live"><span class="dot" aria-hidden="true"></span>Abierto a proyectos</span>
   <h1>Jorge Delgado Aguilera</h1>
   <p class="value">Diseño materiales educativos digitales y soy profesor de Geografía e Historia. Creo actividades, herramientas y formación para que la tecnología, y en especial la IA, ayude al alumnado a <b>leer fuentes, contrastar y argumentar.</b></p>
   <div class="cta">
    <a class="btn solid" href="/proyectos/">Ver proyectos <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    <a class="btn line" href="#contacto">Contactar</a>
   </div>
  </div>
  <div class="t h-photo rv">
   <img src="/assets/jorge.jpg?v=2" alt="Jorge Delgado Aguilera en un aula, con una estantería de libros y un mapamundi al fondo" width="1024" height="1044" fetchpriority="high">
  </div>
 </section>

 <section class="sec" id="proyectos" aria-labelledby="dest-h">
  <div class="sec-head rv">
   <div><span class="lab">Proyectos destacados</span><h2 id="dest-h">Lo que he construido</h2></div>
   <p>Cuatro trabajos que muestran lo que hago: un recurso para todo un claustro, un trabajo académico, una herramienta con IA y una actividad de aula.</p>
  </div>
  <div class="pgrid">
{feat}
  </div>
  <div class="all-link rv"><a class="dl" href="/proyectos/">Ver los {len(P)} proyectos <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
 </section>

 <section class="sec" id="sobre-mi" aria-labelledby="sobre-h">
  <div class="sec-head rv">
   <div><span class="lab">Sobre mí</span><h2 id="sobre-h">Historia con criterio</h2></div>
  </div>
  <div class="about rv">
   <p>Soy profesor de Geografía e Historia, con el Máster de Profesorado (UMA) y el Máster en Tecnología Educativa y Competencias Digitales. He dado clase de refuerzo a alumnado de ESO y Bachillerato en el programa PROA+ y creé el repositorio digital de un centro. Me interesa una idea sencilla: la tecnología, también la IA, tiene sentido en clase cuando ayuda a pensar, no cuando piensa por el alumnado.</p>
   <p class="qline"><q>Los textos no hablan sino cuando se sabe interrogarlos.</q> <span class="author">Marc Bloch</span></p>
  </div>
 </section>
{exp}
{form}
{contact}
</main>'''
    out = head("Jorge Delgado Aguilera · Diseño de materiales educativos digitales",
               "Diseñador de materiales educativos digitales y profesor de Geografía e Historia en Málaga. Diseño actividades, herramientas y formación para que la tecnología y la IA ayuden a leer fuentes, contrastar y argumentar.",
               "/") + topbar("") + body + foot()
    write("/", out)


# ================================================================= ÍNDICE
def index():
    # las categorías son botones que despliegan sus proyectos debajo, como en la Caja de herramientas;
    # la del repositorio va primera y abierta al entrar, y solo hay una abierta a la vez
    order = ["profesorado", "herramientas", "aula"]
    chev = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
    goals = ""
    for i, k in enumerate(order):
        c = CATS[k]; n = sum(1 for p in P if p["cat"] == k); op = i == 0
        cards = "\n".join(card(p) for p in P if p["cat"] == k)
        goals += f'''
  <h2 class="cg-h" id="{k}" style="--i:{i}"><button type="button" class="cg" id="cg-{k}" aria-expanded="{str(op).lower()}" aria-controls="cp-{k}"><b>{c["name"]}</b><span class="gi">{chev}</span><span class="gd">{c["desc"]}</span><span class="num">{n}<span class="vh"> proyectos</span></span></button></h2>
  <div class="cgp" id="cp-{k}" role="region" aria-labelledby="cg-{k}" style="--i:{i}"{"" if op else " hidden"}><div class="pgrid g3">
{cards}
  </div></div>'''
    secs = f'''
 <section class="pcats" aria-label="Proyectos por categoría">
  <div class="cgrid">{goals}
  </div>
  <noscript><style>.cgp[hidden]{{display:block}}</style></noscript>
 </section>'''
    body = f'''
<main id="contenido">
 <section class="sec first">
  <div class="sec-head rv">
   <div><span class="lab">Proyectos</span><h1 class="h1page">Todo lo que he construido</h1></div>
   <p>{len(P)} trabajos agrupados por para qué sirven. Los proyectos más grandes se explican a fondo; las actividades y recursos tienen una ficha breve con su descarga o su enlace.</p>
  </div>
 </section>
{secs}
</main>'''
    write("/proyectos/", head("Proyectos · Jorge Delgado Aguilera",
                              "Herramientas con IA, actividades de aula y recursos para el profesorado diseñados por Jorge Delgado Aguilera, profesor de Geografía e Historia.",
                              "/proyectos/") + topbar("proyectos") + body + foot())


# ================================================================= PÁGINA DE PROYECTO
def btn(label, href, kind, first):
    cls = "btn solid" if first else "btn line"
    if kind == "dl":
        return f'<a class="{cls}" href="{href}" download>{label} {ICON_DL}</a>'
    if kind == "ext":
        return f'<a class="{cls}" href="{href}" rel="noopener" target="_blank">{label} {ICON_EXT}<span class="vh"> (se abre en otra pestaña)</span></a>'
    return f'<a class="{cls}" href="{href}">{label} {ICON_EXT}</a>'


from PIL import Image as _Img


def fig(src, alt, cap=""):
    """Figura con tamaño real (evita saltos al cargar) y enlace a la imagen completa."""
    w = h = None
    fp = os.path.join(ROOT, src.lstrip("/").split("?")[0])
    if os.path.exists(fp):
        w, h = _Img.open(fp).size
    dims = f' width="{w}" height="{h}"' if w else ""
    capt = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure><a href="{src}" target="_blank" rel="noopener" aria-label="Ver la imagen a tamaño completo: {html.escape(re.sub("<[^>]+>","",alt))}"><img src="{src}" alt="{html.escape(alt)}" loading="lazy" decoding="async"{dims}></a>{capt}</figure>'


def render_section(x):
    if isinstance(x, tuple):
        h, b = x
        return f'\n <section class="psec rv"><h2>{h}</h2>{b}</section>'
    # bloque de evidencias: {"title", "intro", "figs":[(src, alt, cap)], "cols", "after"}
    figs = "".join(fig(*f) for f in x["figs"])
    cols = {1: " one", 2: "", 3: " three"}.get(x.get("cols", 2), "")
    wide = " wide" if x.get("cols", 2) != 1 else ""
    intro = x.get("intro", "")
    after = re.sub(r"FIG:([^|\n]+)\|([^|\n]+)\|(.+?)(?=\n|</div>)", lambda m: fig(m.group(1), m.group(2), m.group(3)), x.get("after", ""))
    head = f'<h2>{x["title"]}</h2>' if x.get("title") else ""
    cont = " cont" if not x.get("title") else ""
    frame = " frame" if x.get("frame") else ""
    gal = f'<div class="gal{cols}{frame}">{figs}</div>' if figs else ""
    return f'\n <section class="psec{wide}{cont} rv">{head}{intro}{gal}{after}</section>'


def project(p):
    c = CATS[p["cat"]]
    meta = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in p.get("meta", []))
    links = "".join(btn(l, h, k, i == 0) for i, (l, h, k) in enumerate(p.get("links", [])))
    secs = "".join(render_section(x) for x in p.get("sections", []))
    gal = ""
    if p.get("gallery"):
        figs = "".join(fig(s, cap, cap) for s, cap in p["gallery"])
        one = " one" if len(p["gallery"]) == 1 else ""
        gal = f'\n <section class="psec wide rv"><h2>{p.get("gallery_title","El resultado")}</h2><div class="gal{one}">{figs}</div>'
        if p.get("spoiler"):
            s, lab, txt = p["spoiler"]
            gal += f'<details class="spoiler"><summary>{lab}</summary><figure><img src="{s}" alt="{html.escape(txt)}" loading="lazy"><figcaption>{txt}</figcaption></figure></details>'
        gal += "</section>"
    val = ""
    if p.get("value") and p.get("kind") == "caso":
        val = '\n <section class="psec rv"><h2>Qué demuestra</h2><ul class="pl">' + "".join(f"<li>{v}</li>" for v in p["value"]) + "</ul>"
        if p.get("note"):
            val += f'<p class="pnote">{p["note"]}</p>'
        val += "</section>"
    rel = "\n".join(card(BY[s]) for s in p.get("related", []))
    h1 = p.get("h1", p["title"])
    body = f'''
<main id="contenido">
 <nav class="crumbs" aria-label="Ruta"><a href="/proyectos/">Proyectos</a><span aria-hidden="true">/</span><a href="/proyectos/#{p["cat"]}">{c["name"]}</a></nav>
 <section class="bento phead" aria-labelledby="ph1">
  <div class="t dark ph-main rv">
   <span class="lab">{p.get("lab") or (("Caso de estudio" if p.get("kind")=="caso" else "Ficha") + " · " + " · ".join(html.escape(t) for t in p["tags"][:2]) + " · " + p["year"])}</span>
   <h1 id="ph1">{h1}</h1>
   <p class="lede">{p["lede"]}</p>
   {f'<div class="cta">{links}</div>' if links else ''}
   {f'<p class="cta-note">{p["cta_note"]}</p>' if p.get("cta_note") else ''}
  </div>
  <div class="t ph-vis rv">{viz(p)}</div>
 </section>
 {f'<dl class="pmeta rv">{meta}</dl>' if meta else ''}
 <div class="pbody{' caso' if p.get('kind')=='caso' else ''}">{secs}{gal}{val}
 </div>
 <section class="sec related" aria-labelledby="rel-h">
  <div class="sec-head rv"><div><span class="lab">Sigue explorando</span><h2 id="rel-h">Proyectos relacionados</h2></div>
  <a class="dl" href="/proyectos/">Todos los proyectos <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
  <div class="pgrid g3">
{rel}
  </div>
 </section>
</main>'''
    desc = re.sub("<[^>]+>", "", p["card"])
    write(f"/proyectos/{p['slug']}/", head(f"{re.sub('<[^>]+>','',h1)} · Jorge Delgado Aguilera", desc, f"/proyectos/{p['slug']}/") + topbar("proyectos") + body + foot())


if __name__ == "__main__":
    home()
    index()
    for p in P:
        if not p.get("ext"):
            project(p)
