#!/usr/bin/env python3
"""Genera la portada, el índice de proyectos y una página por proyecto.

Uso:  python3 _build/build.py   (desde la raíz del repositorio)
El contenido está en _build/data.py. Las animaciones de cada tarjeta se toman
de _build/source_old.html (la portada anterior), para no duplicar el código.
"""
import os, re, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import P, BY, CATS, FEATURED, ICON_EXT, ICON_DL, PAGINA

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
# las seis caras sueltas, para la página del Consejo: [[AV:0]] … [[AV:5]] (el color va en --c)
AVS = re.findall(r'<span style="--c:(#[0-9A-Fa-f]+)" title="[^"]+">(<svg.*?</svg>)</span>', council, re.S)
def caras(h):
    def un(m):
        c, svg = AVS[int(m.group(1))]
        return svg.replace('<svg class="avatar"', f'<svg class="avatar" style="--c:{c}"')
    return re.sub(r"\[\[AV:(\d)\]\]", un, h)


# Didákora en la portada: el logo apilado (copia de didakora/marca/didakora-apilado-cielo.svg) con la caja en su grupo para animarla
_dk = open(os.path.join(ROOT, "assets", "proyectos", "repositorio-digital", "didakora-apilado.svg"), encoding="utf-8").read().strip()
_dk = re.sub(r"<title>.*?</title>", "", _dk).replace(' role="img" aria-label="Didákora"', "")
_i = _dk.index(">", _dk.index("<g ")) + 1; _j = _dk.index("</g>", _i)
_dk = _dk[:_i] + '<g class="caja">' + _dk[_i:_j] + "</g>" + _dk[_j:]
VIZ["didakora"] = '<div class="viz v-dk" aria-hidden="true">%s</div>' % _dk


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
CSSV = "117"


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
   {a("/didakora/", "Didákora", "herr")}
   <a class="cv" href="/assets/pdf/CV-Jorge-Delgado-Aguilera.pdf" download aria-label="Descargar CV (PDF)">CV <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg></a>
   <a class="hire" href="#contacto">Contacto</a>
  </nav>
 </div>
</header>
'''


CONTACTO = [
 ("Correo", "mailto:jorgedelagui@gmail.com", '<rect x="3" y="4" width="18" height="16" rx="3.5"/><path d="m4 7 8 6.5 8-6.5"/>', ""),
 ("LinkedIn", "https://www.linkedin.com/in/jorgedelgadoaguilera", '<rect x="3" y="3" width="18" height="18" rx="4.5"/><path d="M8 10.5V16.5M8 7.6v.1M11.8 16.5v-6M11.8 13.2c0-1.7 1.1-2.8 2.5-2.8s2.3 1 2.3 2.8v3.3"/>', ' rel="noopener" target="_blank"'),
 ("Instagram", "https://www.instagram.com/pasadoproximo/", '<rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><path d="M17.3 6.7v.1"/>', ' rel="noopener" target="_blank"'),
 ("Descargar el CV", "/assets/pdf/CV-Jorge-Delgado-Aguilera.pdf", '<path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>', " download"),
]
def foot():
    iconos = "".join(f'<a href="{u}"{x} aria-label="{n}" title="{n}"><svg viewBox="0 0 24 24" aria-hidden="true">{d}</svg></a>' for n, u, d, x in CONTACTO)
    return f'''
<aside class="fin" id="contacto" aria-labelledby="h-fin">
 <svg class="fin-logo" viewBox="0 0 26 26" aria-hidden="true"><path class="fl-r" d="M13 2 2 7h22L13 2Z"/><rect class="fl-e" x="3" y="8" width="20" height="2"/><rect class="fl-c c1" x="5" y="11" width="2.4" height="9"/><rect class="fl-c c2" x="9.6" y="11" width="2.4" height="9"/><rect class="fl-c c3" x="14" y="11" width="2.4" height="9"/><rect class="fl-c c4" x="18.6" y="11" width="2.4" height="9"/><rect class="fl-b" x="2" y="21" width="22" height="2.4"/></svg>
 <h2 id="h-fin">¿Hablamos<span>?</span></h2>
 <p>Abierto a proyectos de docencia, formación del profesorado y tecnología educativa.</p>
 <nav class="fin-c" aria-label="Contacto">{iconos}</nav>
</aside>
<footer><span>© 2026 Jorge Delgado Aguilera</span><span>Campanillas, Málaga</span></footer>
</div>
<script src="/assets/site.js?v={CSSV}" defer></script>
</body>
</html>
'''


def card(p, lvl="h3", desc=False, etiqueta=False):
    tags = " · ".join(html.escape(t) for t in p["tags"][:2])
    tags = f'\n <div class="pc-tags">{tags}</div>' if etiqueta else ""  # las tarjetas van sin la etiqueta gris (portada, índice y relacionados)
    texto = f'\n <p>{p["card"]}</p>' if desc else ""  # todas las tarjetas: solo etiqueta y título (desc=True añade el texto)
    flecha = f'\n <span class="arrow" aria-hidden="true">{ICON_EXT}</span>' if desc else ""  # y sin flecha
    return f'''<a class="t pc lift rv" href="{url(p)}">{flecha}
 {viz(p)}{tags}
 <{lvl}>{p["title"]}</{lvl}>{texto}
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
        grupo("E-learning", [("Rise 360", "rise"), ("Storyline 360", "storyline"), ("H5P", "h5p")]),
    ]) + '</div>'
    form = re.sub(r'(<div class="marq( rev)?" aria-label="[^"]*"><div class="track">.*?</div></div>\s*)+', tools, form, count=1, flags=re.S)
    form = form.replace('<h3 class="big" style="margin-top:8px">Con qué trabajo</h3>', '<h3 class="big h3big" style="margin-top:8px">Con qué trabajo</h3>')
    # en la portada, el repositorio se presenta como Didákora, con su logo animado
    home = {"repositorio-digital": dict(title="Didákora", viz="didakora")}
    feat = "\n".join(card(dict(BY[s], **home.get(s, {})), etiqueta=False) for s in FEATURED)
    body = f'''
<main id="contenido">
 <section class="bento hero2" aria-label="Presentación">
  <div class="t dark h2-main rv">
   <span class="live"><span class="dot" aria-hidden="true"></span>Abierto a proyectos</span>
   <h1>Jorge Delgado Aguilera</h1>
   <p class="value">Diseño materiales educativos digitales y soy profesor de Geografía e Historia. Creo actividades, herramientas y formación para que la tecnología, en especial la IA, ayude al alumnado a <b>leer fuentes, contrastar y argumentar.</b></p>
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
</main>'''
    out = head("Jorge Delgado Aguilera · Diseño de materiales educativos digitales",
               "Diseñador de materiales educativos digitales y profesor de Geografía e Historia en Málaga. Diseño actividades, herramientas y formación para que la tecnología y la IA ayuden a leer fuentes, contrastar y argumentar.",
               "/") + topbar("") + body + foot()
    write("/", out)


# ================================================================= ÍNDICE
def index():
    # botones (pestañas): «Todos» y las tres categorías; el elegido se queda en azul marino y debajo se ven sus proyectos; «Todos», al entrar
    order = ["profesorado", "herramientas", "aula"]
    todos = [p for k in order for p in P if p["cat"] == k]
    # en «Todos», el monasterio va justo después de Didákora (el Repositorio digital), aunque sea de otra categoría
    for antes, despues in [("repositorio-digital", "monasterio-didakora")]:
        m = next((p for p in todos if p["slug"] == despues), None)
        if m: todos.remove(m); todos.insert(next(i for i, p in enumerate(todos) if p["slug"] == antes) + 1, m)
    groups = [("todos", {"name": "Todos", "desc": "Todos mis proyectos, de las tres categorías."}, todos)]
    groups += [(k, CATS[k], [p for p in P if p["cat"] == k]) for k in order]
    tabs = panels = ""
    for i, (k, c, ps) in enumerate(groups):
        n = len(ps); op = i == 0
        cards = "\n".join(card(p) for p in ps)
        tabs += (f'<button type="button" class="ct" role="tab" id="cg-{k}" aria-selected="{str(op).lower()}" aria-controls="{k}"'
                 f'{"" if op else " tabindex=" + chr(34) + "-1" + chr(34)}>{c["name"]}<span class="num">{n}<span class="vh"> proyectos</span></span></button>')
        panels += f'''
  <div class="cgp" id="{k}" role="tabpanel" aria-labelledby="cg-{k}"{"" if op else " hidden"}>
   <p class="cgd">{c["desc"]}</p>
   <div class="pgrid g3">
{cards}
   </div>
  </div>'''
    secs = f'''
 <section class="pcats" aria-label="Proyectos por categoría">
  <div class="ctabs" role="tablist" aria-label="Categorías de proyectos">{tabs}</div>{panels}
  <noscript><style>.ctabs{{display:none}}</style></noscript>
 </section>'''
    body = f'''
<main id="contenido">
 <h1 class="vh">Proyectos</h1>
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
        # «La necesidad» (problema + qué, cómo y para qué) ocupa todo el ancho en todos los proyectos, como en los casos de estudio
        cls = " wide nec" if h == "La necesidad" else ""
        # el texto de muestra de Cazadores de bulos, a todo el ancho para que se lea mejor
        if h == "Así empieza el texto": cls = " wide txt"
        # e-Portfolio: la lista de lo que se puede ver, a todo el ancho para que las líneas sean largas
        if h == "Qué puedes ver en él": cls = " wide"
        return f'\n <section class="psec{cls} rv"><h2>{h}</h2>{caras(b)}</section>'
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
    # «El material» con PDF: el texto a la izquierda y, del texto al borde derecho, una ventana del mismo alto que el texto
    # con las páginas del PDF (se baja por dentro para leerlas) y el botón de descarga fijo abajo
    if x.get("pdf"):
        pdf, pre = x["pdf"]
        pages, n = "", 1
        while os.path.exists(os.path.join(ROOT, f"{pre}{n}.jpg".lstrip("/"))):
            w, h = _Img.open(os.path.join(ROOT, f"{pre}{n}.jpg".lstrip("/"))).size
            pages += f'<img src="{pre}{n}.jpg" alt="Página {n} del PDF" width="{w}" height="{h}" loading="lazy" decoding="async">'
            n += 1
        name = pdf.rsplit("/", 1)[1]
        view = (f'<div class="mat-pdf"><div class="mat-sc" tabindex="0" aria-label="Vista previa del PDF ({n - 1} páginas)">{pages}</div>'
                f'<a class="mat-dl" href="{pdf}" download="{name}">{ICON_DL}Descargar el PDF</a></div>')
        return f'\n <section class="psec wide rv">{head}<div class="mat"><div class="mat-t">{intro}</div>{view}</div></section>'
    # «La actividad» sin PDF: la actividad digital (Genially, Delightex, Jotform…) o la imagen, en el mismo sitio que el visor del PDF;
    # el botón para abrirla aparte va debajo del texto
    if x.get("embed"):
        kind, src, title, label, href = x["embed"]
        # La IA también miente: la imagen sin marco; «Ver la solución», encima, la funde en la solución y
        # despliega la leyenda de los errores debajo del texto (columna izquierda)
        if kind == "flip":
            sol, ley = label, href
            w, h = _Img.open(os.path.join(ROOT, src.lstrip("/"))).size
            inner = (f'<div class="flip-im" style="aspect-ratio:{w}/{h}">'
                     f'<img class="f-a" src="{src}" alt="{html.escape(title)}" width="{w}" height="{h}" loading="lazy" decoding="async">'
                     f'<img class="f-b" src="{sol}" alt="La misma escena con los cinco anacronismos y la trampa marcados" width="{w}" height="{h}" loading="lazy" decoding="async">'
                     f'<button type="button" class="flip-b" aria-pressed="false">Ver la solución</button></div>')
            leyenda = f'<div class="flip-ley" aria-hidden="true"><div>{ley}</div></div>'
            return f'\n <section class="psec wide rv">{head}<div class="mat emb flip"><div class="mat-t">{intro}{leyenda}</div><div class="mat-pdf">{inner}</div></div></section>'
        if kind == "img":
            w, h = _Img.open(os.path.join(ROOT, src.lstrip("/"))).size
            inner = f'<a class="mat-img" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{html.escape(title)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a>'
        else:
            inner = f'<iframe src="{src}" title="{html.escape(title)}" loading="lazy" allow="fullscreen; autoplay; xr-spatial-tracking" allowfullscreen></iframe>'
        go = f'<p class="mat-go">{btn(label, href, "ext", True)}</p>'
        return f'\n <section class="psec wide rv">{head}<div class="mat emb"><div class="mat-t">{intro}{go if x.get("go_texto") else ""}</div><div class="mat-pdf{' zoom' if x.get('zoom') else ''}">{inner}</div></div>{"" if x.get("go_texto") else go}</section>'
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
  <div class="sec-head rv"><div><span class="lab">Sigue explorando</span><h2 id="rel-h">Proyectos relacionados</h2></div></div>
  <div class="pgrid g3">
{rel}
  </div>
  <div class="all-link rv"><a class="dl" href="/proyectos/">Todos los proyectos <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
 </section>
</main>'''
    desc = re.sub("<[^>]+>", "", p["card"])
    write(f"/proyectos/{p['slug']}/", head(f"{re.sub('<[^>]+>','',h1)} · Jorge Delgado Aguilera", desc, f"/proyectos/{p['slug']}/") + topbar("proyectos") + body + foot())


# ================================================================= CURSO (rediseño de octubre de 2026)
# El porfolio como curso de cinco lecciones. Marcado y estilos copiados de las maquetas del brief
# (1-home.html … 5-contacto.html): las reglas comunes en assets/curso.css, el resto en línea como en ellas.
# Lo anterior (home(), index(), project()) se conserva para poder recuperar piezas.
CURSOV = "27"
FONTS_C = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&display=swap">'''
MAIL = "jorgedelagui@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/jorgedelgadoaguilera"
INSTAGRAM = "https://www.instagram.com/pasadoproximo/"
CV = "/assets/pdf/CV-Jorge-Delgado-Aguilera.pdf"
FORMSPREE = "mljjerlq"  # formulario «Contacta» (cuenta de Jorge en formspree.io)


def head_c(title, desc, path, og="/assets/og.jpg", pagina=""):
    t = html.escape(title)
    d = html.escape(desc)
    return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{t}</title><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{d}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
{FAVICON}
{FONTS_C}
<link rel="stylesheet" href="/assets/curso.css?v={CURSOV}">
</head><body{f' class="{pagina}"' if pagina else ""}>
<a class="skip" href="#contenido">Saltar al contenido</a>'''


NAV_C = [("/", "Índice", "indice"), ("/proyectos/", "Proyectos", "proyectos"), ("/sobre-mi/", "Sobre mí", "sobre"), ("/contacto/", "Contacto", "contacto")]


def cab(active="", leccion=1, completo=False, subrayar=True, etiqueta="", texto=""):
    """Barra roja de progreso a todo el ancho arriba (como en la maqueta) y la cabecera debajo; las dos bajan con la página
    (Jorge, 23-10-2026: sin los cinco segmentos, solo
    «Lección X de 5 · Y %»). En la portada el script cambia el rótulo según la lección; en las interiores, fijo."""
    if completo:
        lbl = '<span class="k" id="proglbl" style="color:#5E7D3A">Curso completado · 100 %</span>'
    elif texto:  # la ficha de trabajo pone su propio rótulo («Lección 2 · ficha de trabajo»)
        lbl = f'<span class="k" id="proglbl">{texto}</span>'
    else:
        lbl = f'<span class="k" id="proglbl">Lección {leccion} de 5 · {etiqueta or f"{leccion * 20} %"}</span>'
    def a(href, label, key):
        if key == active and not subrayar:  # la maqueta de la portada no subraya «Índice»
            return f'<a href="{href}" aria-current="page" style="text-decoration:none">{label}</a>'
        if key == active:
            return f'<a href="{href}" aria-current="page" style="text-decoration:none;border-bottom:2px solid #A3322A;padding-bottom:2px">{label}</a>'
        return f'<a href="{href}" style="text-decoration:none">{label}</a>'
    nav = "".join(a(*n) for n in NAV_C)
    return f'''
<div class="fija">
<div class="barra" aria-hidden="true"><div></div></div>
<header class="wrap cab" style="display:flex;justify-content:space-between;align-items:center;height:74px;border-bottom:1px solid #061033">
  <a href="/" style="font-family:'Bricolage Grotesque';font-weight:800;font-size:22px;letter-spacing:-.01em;text-decoration:none">Jorge Delgado Aguilera</a>
  <button type="button" class="menu-b" aria-expanded="false" aria-controls="menu">Menú</button>
  <div id="prog" style="display:flex;align-items:center;gap:14px" aria-label="Progreso del curso">
    {lbl}
  </div>
  <nav id="menu" aria-label="Principal" style="display:flex;gap:30px;font-weight:500">{nav}</nav>
</header>
</div>
'''


def pie_c(guino=False, margen=True, guino_izq=False):
    """La línea © de siempre; a la derecha, el guiño (portada) o los enlaces de las interiores."""
    # sin correo, LinkedIn ni Didákora a la derecha (Jorge, 23-10-2026): solo el guiño en la portada
    der = '<span>Curso completado al 100 % · Ya sabes qué hago</span>' if guino else ""
    mt = ";margin-top:72px" if margen else ""
    return f'''<footer class="wrap" style="padding:28px 40px;border-top:1px solid #061033;display:flex;justify-content:space-between;color:#5A6480;font-size:15px{mt}"><span>© 2026 Jorge Delgado Aguilera · Campanillas, Málaga{" · Curso completado al 100 % · Ya sabes qué hago" if guino_izq else ""}</span>{der}</footer>
<script src="/assets/curso.js?v={CURSOV}" defer></script>
</body></html>
'''


ICO_C = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#061033" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
CIRC = 'style="width:52px;height:52px;border:1.5px solid #061033;border-radius:50%;display:inline-flex;align-items:center;justify-content:center"'


def contacto_c(margen=True):
    """Iconos de correo, LinkedIn e Instagram + «Descargar el CV» (lección 5, en la portada y en Contacto)."""
    return (f'<div style="display:flex;gap:14px;{"margin-top:22px;" if margen else ""}align-items:center;flex-wrap:wrap">'
            f'<a href="mailto:{MAIL}" aria-label="Correo" {CIRC}>{ICO_C}<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></a>'
            f'<a href="{LINKEDIN}" rel="noopener" target="_blank" aria-label="LinkedIn" {CIRC}>{ICO_C}<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 10v7M8 7v.5M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/></svg></a>'
            f'<a href="{INSTAGRAM}" rel="noopener" target="_blank" aria-label="Instagram" {CIRC}>{ICO_C}<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="#061033"/></svg></a>'
            f'<a class="btn o" href="{CV}" download style="margin-left:6px">Descargar el CV</a></div>')


def form_c(filas=4, sin_altura=False):
    accion = f' action="https://formspree.io/f/{FORMSPREE}" method="POST"' if FORMSPREE else ""
    campo = 'style="border:1px solid #061033;padding:11px;font:inherit;background:#F2F4F9"'
    return f'''<form class="ficha"{accion} style="{"min-height:0;" if sin_altura else ""}gap:12px">{"" if FORMSPREE else "<!-- TODO: falta el ID de Formspree -->"}<span class="tipo">Contacta</span><input type="hidden" name="_subject" value="Mensaje desde el porfolio">
      <label class="k" style="display:flex;flex-direction:column;gap:6px">Nombre<input name="nombre" autocomplete="name" required {campo}></label>
      <label class="k" style="display:flex;flex-direction:column;gap:6px">Email<input type="email" name="email" autocomplete="email" required {campo}></label>
      <label class="k" style="display:flex;flex-direction:column;gap:6px">¿Qué necesitas?<textarea name="mensaje" rows="{filas}" required {campo}></textarea></label>
      <button class="btn" style="border:none;font:inherit;font-weight:700;align-self:flex-start">Enviar</button></form>'''


def leccion5_c():
    return f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start">
    <div><h2 class="serif" style="font-size:44px;margin-bottom:14px">Ahora pregunta tú</h2><p style="margin:0;color:#5A6480;max-width:40ch">Abierto a proyectos de diseño instruccional, formación del profesorado y tecnología educativa. En remoto o en Málaga.</p>{contacto_c()}</div>
    {form_c()}
  </div>'''


def home_c():
    li = 'style="display:flex;justify-content:space-between;padding:12px 0;border-top:1px solid #E1E6F0'
    paso = 'class="paso" style="border:1px solid #9FB3FF;padding:18px;display:flex;flex-direction:column;gap:8px"'
    paso_n = 'style="font-family:\'Bricolage Grotesque\';font-size:30px;color:#9FB3FF"'
    paso_p = 'style="margin:0;font-size:15px;color:#E6EBF8"'
    body = f'''<main id="contenido">
<section class="wrap" style="display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:center;padding:80px 40px 64px">
  <div style="display:flex;flex-direction:column;gap:26px">
    <p class="lab">Curso de 12 minutos · para quien contrata diseño instruccional</p>
    <h1 class="serif" style="font-size:78px">Cómo diseño materiales que hacen pensar</h1>
    <p style="margin:0;font-size:20px;max-width:38ch;color:#2A3352">Cinco lecciones cortas, una actividad ramificada y una evaluación final que haces tú. Al terminar sabrás qué hago, cómo lo hago y para qué lo hago.</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/sobre-mi/">Lección 1: sobre mí</a><a class="btn o" href="/proyectos/">Ir directo a los proyectos</a></div>
  </div>
  <nav class="ficha idx" aria-label="Índice del curso" style="gap:0;padding:28px 30px">
    <span class="tipo">Índice del curso</span>
    <ol style="margin:14px 0 0;padding:0;list-style:none;display:flex;flex-direction:column">
      <li {li}"><a href="/sobre-mi/"><b style="color:#5E7D3A">✓</b>&nbsp; 1 · Quién soy y para quién trabajo</a><span class="k">2 min</span></li>
      <li {li};font-weight:700"><a href="#leccion-2">▶&nbsp; 2 · Cuatro trabajos, uno por tipo</a><span class="k">3 min</span></li>
      <li {li}"><a href="#leccion-3">3 · Actividad: ¿y si lo hizo la IA?</a><span class="k">1 min</span></li>
      <li {li}"><a href="#leccion-4">4 · Cómo trabajo, en cuatro pasos</a><span class="k">3 min</span></li>
      <li {li};border-bottom:1px solid #E1E6F0"><a href="#leccion-5">5 · Evaluación final: ahora pregunta tú</a><span class="k">3 min</span></li>
    </ol>
  </nav>
</section>

<section class="wrap" id="leccion-2" data-lesson="2"><div class="lesson">
  <div class="num"><b>02</b><span class="k">Lección 2 · 3 min</span></div>
  <div>
    <h2 class="serif" style="font-size:44px;margin-bottom:18px">Cuatro trabajos, uno por tipo</h2>
    <p class="obj"><b>Objetivo:</b> al terminar esta lección podrás decir qué tipo de material sé hacer y en qué estado está cada uno.</p>
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:28px;padding-right:6px">
      <a class="ficha" href="/didakora/"><span class="tipo">Recurso</span><h3>Didákora</h3><p>121 herramientas digitales revisadas a mano, con ficha y fecha.</p><span class="estado"><i></i>En uso</span></a>
      <a class="ficha" href="/proyectos/consejo-de-clio/"><span class="tipo">Herramienta</span><h3>El Consejo de Clío</h3><p>Seis agentes preparan la sesión; el docente la contrasta.</p><span class="estado"><i></i>Comprobado</span></a>
      <a class="ficha" href="/proyectos/cazadores-de-bulos/"><span class="tipo">Actividad</span><h3>Cazadores de bulos históricos</h3><p>Nueve errores escondidos en un texto sobre Málaga en 1936.</p><span class="estado"><i></i>4.º ESO</span></a>
      <div class="ficha"><span class="tipo">Curso</span><h3>Verifica lo que dice la IA</h3><p>Tres lecciones y una rutina de cinco minutos para clase.</p><span class="estado"><i></i>Rise y Storyline</span></div>
    </div>
    <div class="next" style="justify-content:space-between;align-items:center"><a href="/proyectos/" style="font-weight:700;border-bottom:2px solid #A3322A;text-decoration:none;padding-bottom:2px">Ver el resto de proyectos</a><a class="btn" href="#leccion-3">Siguiente: la actividad</a></div>
  </div>
</div></section>

<section class="wrap" id="leccion-3" data-lesson="3"><div class="lesson">
  <div class="num"><b>03</b><span class="k">Actividad · 1 min</span></div>
  <div class="rama">
    <h2 class="serif" style="font-size:44px;margin-bottom:18px">¿Y si lo hizo la IA?</h2>
    <p style="margin:0 0 22px;font-size:18px;max-width:60ch">Un alumno de 4.º entrega un comentario de texto impecable sobre la Constitución de 1812. Sospechas que lo ha escrito una IA. ¿Qué haces?</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
      <button type="button" class="opt mal" data-op="a" aria-pressed="false"><span>A</span>Lo paso por un detector y actúo según el resultado.</button>
      <button type="button" class="opt" data-op="b" aria-pressed="false"><span>B</span>Le pido que defienda en voz alta tres afirmaciones de su texto con el libro delante.</button>
      <button type="button" class="opt mal" data-op="c" aria-pressed="false"><span>C</span>Prohíbo el uso de IA en la siguiente tarea.</button>
    </div>
    <p class="fb mal" data-op="a" style="margin:16px 0 0" hidden aria-live="polite"><b>Has elegido A.</b> Los detectores de IA se equivocan: marcan como artificiales textos escritos por personas y dejan pasar los que se han retocado. Un porcentaje no demuestra nada y acusar con él a un alumno es injusto. Prueba otra opción.</p>
    <p class="fb" data-op="b" style="margin:16px 0 0" hidden aria-live="polite"><b>Has elegido B.</b> Es lo que hago en "Cazadores de bulos": la IA no se detecta, se interroga. Un detector falla; una pregunta bien hecha, no. Esa idea está en todos mis materiales.</p>
    <p class="fb mal" data-op="c" style="margin:16px 0 0" hidden aria-live="polite"><b>Has elegido C.</b> Prohibirla no resuelve el caso: no sabes si este comentario es suyo y la IA seguirá a mano fuera del aula. Lo que importa es comprobar si entiende lo que ha entregado. Prueba otra opción.</p>
    <div class="next"><a class="btn" href="#leccion-4">Siguiente: cómo trabajo</a></div>
  </div>
</div></section>

<section id="leccion-4" style="background:#061033;color:#fff;margin-top:24px" data-lesson="4" data-oscuro>
  <div class="wrap" style="display:grid;grid-template-columns:200px 1fr;gap:40px;padding:64px 40px">
    <div class="num" style="display:flex;flex-direction:column;gap:8px"><b style="font-family:'Bricolage Grotesque';font-weight:800;font-size:54px;line-height:1;letter-spacing:-.03em">04</b><span class="k" style="color:#9FB3FF">Lección 4 · 3 min</span></div>
    <div style="display:flex;flex-direction:column;gap:18px">
      <h2 class="serif" style="font-size:44px;color:#fff">Cómo trabajo, en cuatro pasos</h2>
      <p style="margin:0;font-size:18px;color:#E6EBF8;max-width:60ch">El mismo proceso en todos los proyectos. Aquí, con el repositorio digital que creé para el Colegio Cerrado de Calderón (2024).</p>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">
        <div {paso}><b {paso_n}>1</b><b>Parto de una necesidad de aula</b><p {paso_p}>{CODE_C["1"]}</p></div>
        <div {paso}><b {paso_n}>2</b><b>Diseño el material y sus reglas</b><p {paso_p}>{CODE_C["2"]}</p></div>
        <div {paso}><b {paso_n}>3</b><b>Lo pruebo y busco el fallo</b><p {paso_p}>{CODE_C["3"]}</p></div>
        <div {paso}><b {paso_n}>4</b><b>Digo qué está comprobado y qué no</b><p {paso_p}>{CODE_C["4"]}</p></div>
      </div>
      <blockquote style="margin:14px 0 0;font-family:'Bricolage Grotesque';font-weight:700;font-size:26px;line-height:1.2;color:#fff">«{TESTIMONIO_C}»</blockquote>
      <p style="margin:0;font-size:15px;color:#9FB3FF">Jorge Lanzat · Subdirector General · Colegio Cerrado de Calderón</p>
    </div>
  </div>
</section>

<section class="wrap" id="leccion-5" data-lesson="5"><div class="lesson" style="border-top:none">
  <div class="num"><b>05</b><span class="k">Evaluación final · 3 min</span></div>
  {leccion5_c()}
</div></section>
</main>
'''
    write("/", head_c("Jorge Delgado Aguilera · Diseño de materiales educativos digitales",
                      "Cómo diseño materiales que hacen pensar: un curso de 12 minutos en cinco lecciones cortas, con una actividad ramificada y una evaluación final que haces tú.", "/")
          + cab("indice", subrayar=False) + body + pie_c(guino=True, margen=False))


# /proyectos/ (maqueta 2-proyectos): 6 destacados en fichas y los otros 9 en una tabla, con filtros por categoría.
# Textos de la maqueta; «Mi parte», elegido por Jorge. Años y herramientas de la tabla: los del repo (Jorge, 23-10-2026),
# y la tabla va de la más reciente a la más antigua, como dice su subtítulo.
FICHA_LISTA = [
    # (slug o URL, categoría, tipo, título, descripción, mi parte, estado)
    (None, "profesorado", "Curso", "Verifica lo que dice la IA", "Tres lecciones en Rise y una ramificación en Storyline. SCORM descargable.", "", "Demo sin login"),  # sin enlace hasta que el curso exista: entonces, su URL en vez de None
    ("/didakora/", "profesorado", "Recurso", "Didákora", "121 herramientas revisadas a mano, con ficha y fecha.", "", "En uso"),
    ("consejo-de-clio", "herramientas", "Herramienta", "El Consejo de Clío", "Seis agentes preparan la sesión; el docente la contrasta.", "Diseño de los roles e instrucciones", "Comprobado"),
    ("asistente-gpt-2eso", "herramientas", "Herramienta", "Asistente de IA para 2.º ESO", "Un GPT que guía sin resolver y cita la unidad.", "Configuración, materiales y pruebas", "Pendiente de pilotar"),
    ("monasterio-didakora", "herramientas", "Proceso", "Mantenimiento con agentes", "Cinco agentes proponen cambios en Didákora; yo apruebo cada uno.", "Diseño del equipo y aprobación de cada cambio", "17 cambios en 4 ciclos"),
    ("cazadores-de-bulos", "aula", "Actividad", "Cazadores de bulos históricos", "Nueve errores escondidos en un texto sobre Málaga en 1936.", "", "4.º ESO"),
]
TABLA_LISTA = [
    # (slug, categoría, título, tipo, herramienta, año), en el orden de la maqueta
    ("audita-tu-programacion", "profesorado", "Audita tu programación", "Formación", "NotebookLM", "2026"),
    ("repositorio-digital", "profesorado", "Repositorio digital de centro", "Recurso", "Google Sites", "2024"),
    ("constitucion-1812", "aula", "¿Fue liberal la Constitución de 1812?", "Actividad", "Hypothes.is", "2026"),
    ("la-ia-tambien-miente", "aula", "La IA también miente", "Actividad", "Claude y Canva", "2026"),
    ("la-nube-pesa", "aula", "La nube pesa", "Actividad", "", "2026"),
    ("mapa-de-relieves", "herramientas", "Mapa de relieves de la Península", "Herramienta", "Claude", "2026"),
    ("rubrica-materiales-digitales", "profesorado", "Rúbrica de materiales digitales", "Formación", "Jotform", "2024"),
    ("escape-room-siglo-xix", "aula", "Escape room del siglo XIX", "Actividad", "Genially", "2024"),
    ("excursion-roma-3d", "aula", "Excursión a Roma en 3D", "Actividad", "CoSpaces", "2024"),
]


def lista_c():
    def enlace(s):
        return s if s.startswith("/") else url(BY[s])
    fichas = []
    for s, cat, tipo, tit, desc, mi, est in FICHA_LISTA:
        dentro = (f'<span class="tipo">{tipo}</span><h3>{tit}</h3><p>{desc}</p>'
                  + (f'<span class="mi">Mi parte: {mi}</span>' if mi else "")
                  + f'<span class="estado"><i></i>{est}</span>')
        fichas.append(f'<a class="ficha" data-cat="{cat}" href="{enlace(s)}">{dentro}</a>' if s else f'<div class="ficha" data-cat="{cat}">{dentro}</div>')
    tabla = sorted(TABLA_LISTA, key=lambda f: -int(f[5]))  # orden cronológico, de lo más reciente a lo más antiguo
    filas = "".join(f'<tr data-cat="{cat}"><td><a href="{url(BY[s])}">{tit}</a></td><td>{tipo}</td><td>{herr}</td><td>{ano}</td></tr>'
                    for s, cat, tit, tipo, herr, ano in tabla)
    fichas_html = "\n      ".join(fichas)
    # subtítulos que cambian con el filtro (Jorge): cuántos destacados y cuántos «otros» hay en cada opción
    NUM = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
    NOMBRE = {"profesorado": "formación", "herramientas": "herramientas", "aula": "actividades"}
    def txt_dest(k):
        n = len(FICHA_LISTA) if k == "todos" else sum(c == k for _, c, *_ in FICHA_LISTA)
        de = "" if k == "todos" else f" de {NOMBRE[k]}"
        return f"El{de} que mejor muestra lo que hago" if n == 1 else f"Los {NUM[n]}{de} que mejor muestran lo que hago"
    def txt_otros(k):
        n = len(TABLA_LISTA) if k == "todos" else sum(c == k for _, c, *_ in TABLA_LISTA)
        return "Uno más" if n == 1 else f"{NUM[n].capitalize()} más, en orden cronológico"
    claves = ["todos", "profesorado", "herramientas", "aula"]
    attr_dest = " ".join(f'data-t-{k}="{txt_dest(k)}"' for k in claves)
    attr_otros = " ".join(f'data-t-{k}="{txt_otros(k)}"' for k in claves)
    cats = [c for _, c, *_ in FICHA_LISTA] + [c for _, c, *_ in TABLA_LISTA]
    fil = "".join(f'<button type="button" class="filter{" on" if k == "todos" else ""}" data-cat="{k}" aria-pressed="{str(k == "todos").lower()}">{n}</button>'
                  for k, n in [("todos", "Todos"), ("profesorado", "Formación"), ("herramientas", "Herramientas"), ("aula", "Actividades")])
    body = f'''<main id="contenido">
<section class="wrap"><div class="lesson">
  <div class="lnum"><b>02</b><span class="k">Lección 2 · ampliación</span><span class="k">{len(cats)} proyectos · {min(int(f[5]) for f in TABLA_LISTA)}-2026</span>
    <div class="filtros" role="group" aria-label="Filtrar por categoría">{fil}</div></div>
  <div>
    <h1 class="serif" style="font-size:64px;margin-bottom:18px">Todas las fichas de trabajo</h1>
    <p class="obj"><b>Objetivo:</b> al terminar podrás elegir el proyecto que más se parezca a lo que necesitas y ver qué hice yo en él.</p>
    <div class="rule"><h2 class="serif" style="font-size:32px;font-weight:700">Destacados</h2><span class="k sub-f" {attr_dest}>{txt_dest("todos")}</span></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px;padding:24px 6px 10px 0">
      {fichas_html}
    </div>
    <div class="rule" id="otros" style="margin-top:40px"><h2 class="serif" style="font-size:32px;font-weight:700">Otros proyectos</h2><span class="k sub-f" {attr_otros}>{txt_otros("todos")}</span></div>
    <table style="margin-top:10px"><thead><tr><th scope="col">Proyecto</th><th scope="col">Tipo</th><th scope="col">Herramienta</th><th scope="col">Año</th></tr></thead><tbody>{filas}</tbody></table>
    <div class="next"><a class="btn" href="/#leccion-3">Volver al curso: lección 3</a></div>
  </div>
</div></section>
</main>
'''
    write("/proyectos/", head_c("Proyectos · Jorge Delgado Aguilera",
                                "Herramientas con IA, actividades de aula y recursos para el profesorado diseñados por Jorge Delgado Aguilera, profesor de Geografía e Historia.",
                                "/proyectos/", pagina="p-lista")
          + cab("proyectos", leccion=2, etiqueta="ampliación") + body + pie_c())


# Fichas de trabajo (maqueta 3-proyecto), con los textos de PAGINA en data.py
COLOR_AFIRMAR = {"Comprobado": "#5E7D3A", "En uso": "#A3322A", "Pendiente": "#5A6480"}


def ficha_c(slug):
    p, d = BY[slug], PAGINA[slug]
    facts = "".join(f'<div class="fact"><span>{a}</span><b>{b}</b></div>' for a, b in d["ficha"])
    hice = ""
    if d.get("hice"):
        frases = "".join(f'<p style="color:#061033"><b>{v}</b> {t}</p>' for v, t in d["hice"])
        hice = f"""
<section class="wrap" style="padding:48px 40px 0;display:flex;flex-direction:column;gap:18px">
  <div class="rule"><h2 class="serif" style="font-size:36px;font-weight:700">Lo que hice yo</h2></div>
  <div class="ficha" style="min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:12px 32px">{frases}</div>
</section>"""
    if d.get("video"):
        src, poster, alt = d["video"]
        # sin controles nativos hasta que se pulsa (tapaban el cartel): un botón píldora del porfolio encima
        visual = (f'<div class="vid"><video src="{src}" poster="{poster}" muted playsinline preload="metadata" aria-label="{html.escape(alt)}" '
                  f'style="width:100%;height:auto;display:block;border:1px solid #061033"></video>'
                  f'<button type="button" class="btn vid-b">▶&nbsp; Ver el vídeo · 30 s</button></div>')
    else:
        visual = '<!-- TODO visual --><div class="ph" style="min-height:340px">[visual]</div>'
    ext = ' rel="noopener" target="_blank"'
    botones = "".join(f'<a class="btn{" o" if i else ""}" style="text-align:center" href="{h}"{"" if h.startswith("/") else ext}>{l}</a>' for i, (l, h) in enumerate(d["botones"]))
    caps = "".join(f'<a href="{c_src}" target="_blank" rel="noopener" style="display:flex;flex-direction:column;gap:4px;text-decoration:none">'
                   f'<img src="{c_src}" alt="{html.escape(c_alt)}" loading="lazy" style="width:100%;border:1px solid #E1E6F0;display:block">'
                   f'<span class="k" style="font-size:13px">{c_pie}</span></a>'
                   for c_src, c_alt, c_pie in d.get("capturas", []))
    tarjetas = []
    for i, (t, x) in enumerate(d["afirmar"]):
        # el error corregido, en una ventana emergente (Jorge: sin capturas a la vista)
        extra = '<button type="button" class="abre" data-abre="error-corregido">Ver el error corregido: antes y después</button>' if i == 0 and caps else ""
        color = COLOR_AFIRMAR.get(t, "#A3322A")
        st = "" if color == "#A3322A" else f' style="color:{color}"'  # el rojo es el de .tipo
        tarjetas.append(f'<div class="ficha" style="min-height:0"><span class="tipo"{st}>{t}</span><p style="color:#061033">{x}</p>{extra}</div>')
    pasos = "".join(f'<div class="step"><b>{a}</b><span>{b}</span></div>' for a, b in d["pasos"])
    dialogo = ""
    if caps:
        dialogo = f'''
<dialog class="pop" id="error-corregido" aria-labelledby="pop-t">
  <div class="pop-c"><span class="tipo" style="color:#5E7D3A">Comprobado</span><h2 id="pop-t" class="serif" style="font-size:30px;font-weight:700">El error corregido</h2>
  <div class="pop-g">{caps}</div>
  <button type="button" class="btn pop-x" data-cierra>Cerrar</button></div>
</dialog>'''
    sig_t, sig_s = d["siguiente"]
    aviso = ""
    if d.get("aviso"):  # antes de «Todas las fichas», con la caja de objetivo de la maqueta (8.º bloque del brief)
        aviso = f'<section class="wrap" style="padding:48px 40px 0"><p class="obj" role="note" style="margin:0"><b>{d["aviso"][0]}</b> {d["aviso"][1]}</p></section>\n'
    titulo = re.sub("<[^>]+>", "", p.get("h1", p["title"]))
    body = f"""<main id="contenido">
<section class="wrap" style="padding:56px 40px 0;display:grid;grid-template-columns:200px 1fr;gap:40px">
  <div class="lnum"><b>02</b><span class="k">Ficha de trabajo</span><span class="k">{d["lnum"]}</span></div>
  <div style="display:flex;flex-direction:column;gap:18px">
  <p class="k"><a href="/proyectos/" style="color:inherit;text-decoration:none">Proyectos</a> / <a href="/proyectos/" style="color:inherit;text-decoration:none">{d["migas"]}</a></p>
  <h1 class="serif" style="font-size:72px">{titulo}</h1>
  <p style="margin:0;font-size:22px;max-width:42ch;line-height:1.35">{d["sub"]}</p>
  <p class="obj" style="margin-top:8px"><b>Objetivo de esta ficha:</b> al terminar sabrás qué hace, qué hice yo y qué está comprobado.</p>
  </div>
</section>
<section class="wrap" style="padding:36px 40px 0;display:grid;grid-template-columns:repeat(4,1fr);gap:14px">
  {facts}
</section>{hice}
<section class="wrap" style="padding:48px 40px 0;display:grid;grid-template-columns:7fr 5fr;gap:28px;align-items:stretch">
  {visual}
  <div style="display:flex;flex-direction:column;gap:12px;justify-content:center">{botones}<p style="margin:0;color:#5A6480;font-size:15px;text-align:center">{d["nota"]}</p></div>
</section>
<section class="wrap" style="padding:56px 40px 0;display:flex;flex-direction:column;gap:18px">
  <div class="rule"><h2 class="serif" style="font-size:36px;font-weight:700">Lo que puedo afirmar</h2></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px;padding:10px 6px 10px 0;align-items:start">
    {"".join(tarjetas)}
  </div>
</section>
<section class="wrap" style="padding:56px 40px 0;display:grid;grid-template-columns:1fr 1fr;gap:60px">
  <div><p class="lab">La necesidad</p><p style="margin:10px 0 0">{d["necesidad"]}</p></div>
  <div><p class="lab" style="margin-bottom:10px">{d["pasos_titulo"]}</p>{pasos}</div>
</section>
{aviso}<section class="wrap" style="padding:40px 40px 0"><div class="next" style="justify-content:space-between"><a href="/proyectos/" style="font-weight:700;border-bottom:2px solid #A3322A;text-decoration:none;padding-bottom:2px">Todas las fichas</a><a class="btn" href="{url(BY[sig_s])}">Siguiente ficha: {sig_t}</a></div></section>{dialogo}
</main>
"""
    write(f"/proyectos/{slug}/", head_c(f"{titulo} · Jorge Delgado Aguilera", re.sub("<[^>]+>", "", d["sub"]), f"/proyectos/{slug}/", pagina="p-ficha")
          + cab("proyectos", leccion=2, texto="Lección 2 · ficha de trabajo") + body + pie_c())


# Sobre mí = lección 1 (maqueta 4-sobre-mi). Datos del CV; los corchetes de la maqueta, con lo que Jorge dio en el chat
# (PROA+: estimación suya; hostelería: desde 2015 en varias empresas, ahora en Ibis Málaga Centro).
EXPERIENCIA_C = [
    ("2023 – 2025", "Profesor de refuerzo · PROA+", "Sertudema · Residencia Escolar Andalucía", "30 alumnos · 3 h/día · nota media del grupo de 4 a 7"),
    ("2024", "Coordinación TIC", "Colegio Cerrado de Calderón · Repositorio digital para el claustro, presentado en Braining 2025", ""),
    ("2019", "Prácticas docentes", "IES Campanillas · 2.º ESO, Bachillerato y PMAR · Matrícula de Honor en el TFM", ""),
    ("2015 – hoy", "Hostelería · Ibis Málaga Centro, recepcionista", "Atención al público en inglés a diario, incidencias y coordinación de equipos.", ""),
]
FORMACION_C = [
    ("2024", "Máster en Tecnología Educativa y Competencias Digitales", "Universidad Europea"),
    ("2019", "Máster en Formación del Profesorado", "Universidad de Málaga"),
    ("2017", "Grado en Historia", "Universidad de Málaga"),
    ("2014", "Grado Superior en Administración y Finanzas", "IES Politécnico Jesús Marín"),
    ("Idiomas", "Inglés B1 acreditado (Cambridge)", "Uso profesional diario · B2 en curso"),
]


# «Con qué trabajo» (brief 2.6): solo las herramientas con proyecto detrás, cada una enlazada a él (lista aprobada por Jorge
# en la v2). Rise y Storyline, sin enlace hasta que exista el curso.
HERRAMIENTAS_C = [
    ("Rise 360", "/herramientas/logos/rise.png", [("Verifica lo que dice la IA", None)]),
    ("Storyline 360", "/herramientas/logos/storyline.png", [("Verifica lo que dice la IA", None)]),
    ("Claude", "/assets/tools/claude.png", [("Consejo de Clío", "/proyectos/consejo-de-clio/"), ("Monasterio", "/proyectos/monasterio-didakora/")]),
    ("ChatGPT", "/assets/tools/chatgpt.png", [("Asistente 2.º ESO", "/proyectos/asistente-gpt-2eso/")]),
    ("NotebookLM", "/assets/tools/notebooklm.png", [("Audita tu programación", "/proyectos/audita-tu-programacion/")]),
    ("Genially", "/assets/tools/genially.png", [("Escape room s. XIX", "/proyectos/escape-room-siglo-xix/")]),
    ("Hypothes.is", "/assets/tools/hypothesis.png", [("Constitución de 1812", "/proyectos/constitucion-1812/")]),
    ("Google Sites", "/assets/tools/google-sites.png", [("Repositorio de centro", "/proyectos/repositorio-digital/")]),
]


def herramientas_c():
    out = []
    for nombre, ico, projs in HERRAMIENTAS_C:
        destinos = " · ".join(f'<a href="{h}">{t}</a>' if h else f'<span>{t}</span>' for t, h in projs)
        out.append(f'<li class="herr"><img src="{ico}" alt="" width="22" height="22" loading="lazy"><b>{nombre}</b><span class="k" aria-hidden="true">→</span>{destinos}</li>')
    return "\n    ".join(out)


def sobre_c():
    def filas(items):
        out = []
        for i, it in enumerate(items):
            y, h, t = it[:3]
            extra = f'<p style="color:#061033;margin-top:6px">{it[3]}</p>' if len(it) > 3 and it[3] else ""
            ultimo = ' style="border-bottom:1px solid #E1E6F0"' if i == len(items) - 1 else ""
            out.append(f'<div class="exp"{ultimo}><span class="y">{y}</span><div><h3>{h}</h3><p>{t}</p>{extra}</div></div>')
        return "\n    ".join(out)
    body = f'''<main id="contenido">
<section class="wrap" style="display:grid;grid-template-columns:200px 1fr;gap:40px;padding:56px 40px 0"><div class="lnum"><b>01</b><span class="k">Lección 1 · 2 min</span></div><div><h1 class="serif" style="font-size:56px;margin-bottom:18px">Quién soy y para quién trabajo</h1><p class="obj"><b>Objetivo:</b> al terminar sabrás qué hago, qué formación tengo y dónde he dado clase.</p></div></section>
<section class="wrap" style="display:grid;grid-template-columns:1fr 420px;gap:72px;align-items:center;padding:16px 40px 56px">
  <div style="display:flex;flex-direction:column;gap:26px"><h2 class="serif" style="font-size:60px">Lo que sé hacer lo aprendí en el aula</h2><p style="margin:0;font-size:20px;max-width:40ch;color:#2A3352">Diseñador de materiales educativos digitales y profesor de Geografía e Historia. Málaga, o en remoto.</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="{CV}" download>Descargar el CV</a><a class="btn o" href="mailto:{MAIL}">{MAIL}</a></div></div>
  <div class="foto" style="position:relative;justify-self:end"><div style="position:absolute;inset:0;transform:translate(14px,14px);background:#9FB3FF"></div><img src="/assets/jorge.jpg" alt="Jorge Delgado Aguilera" width="420" height="460" style="width:420px;height:460px;object-fit:cover;display:block;position:relative"></div>
</section>
<section class="wrap" style="padding:24px 40px 0;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:start">
  <div style="display:flex;flex-direction:column;gap:14px"><div class="rule"><h2 class="serif" style="font-size:34px;font-weight:700">Experiencia</h2></div>
    {filas(EXPERIENCIA_C)}
  </div>
  <div style="display:flex;flex-direction:column;gap:14px"><div class="rule"><h2 class="serif" style="font-size:34px;font-weight:700">Formación</h2></div>
    {filas(FORMACION_C)}
    <figure class="ficha" style="min-height:0;margin:24px 0 0"><span class="tipo">Testimonio</span><blockquote style="margin:0"><p style="font-style:italic;color:#061033">«{TESTIMONIO_C}»</p></blockquote><figcaption class="k">Jorge Lanzat · Subdirector General</figcaption></figure>
  </div>
</section>
<section class="wrap" style="padding:56px 40px 0;display:flex;flex-direction:column;gap:18px">
  <div class="rule"><h2 class="serif" style="font-size:34px;font-weight:700">Con qué trabajo</h2><span class="k">Cada herramienta, con el proyecto en el que la uso</span></div>
  <ul class="herrs">
    {herramientas_c()}
  </ul>
</section>
<section class="wrap" style="padding:40px 40px 0"><div class="next"><a class="btn" href="/#leccion-2">Siguiente: lección 2, los trabajos</a></div></section>
</main>
'''
    write("/sobre-mi/", head_c("Sobre mí · Jorge Delgado Aguilera",
                               "Jorge Delgado Aguilera, diseñador de materiales educativos digitales y profesor de Geografía e Historia en Málaga: experiencia, formación e idiomas.",
                               "/sobre-mi/", pagina="p-sobre")
          + cab("sobre", leccion=1) + body + pie_c())


# Contacto = lección 5 (maqueta 5-contacto)
def contacto_pag_c():
    body = f'''<main id="contenido">
<section class="wrap"><div class="lesson">
  <div class="lnum"><b>05</b><span class="k">Evaluación final</span></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start">
    <div style="display:flex;flex-direction:column;gap:22px"><h1 class="serif" style="font-size:64px">Ahora pregunta tú</h1><p style="margin:0;font-size:19px;max-width:40ch;color:#2A3352">Abierto a proyectos de diseño instruccional, formación del profesorado y tecnología educativa. En remoto o en Málaga.</p>
      {contacto_c(margen=False)}</div>
    {form_c(filas=5, sin_altura=True)}
  </div>
</div></section>
</main>
'''
    write("/contacto/", head_c("Contacto · Jorge Delgado Aguilera",
                               "Contacta con Jorge Delgado Aguilera: proyectos de diseño instruccional, formación del profesorado y tecnología educativa, en remoto o en Málaga.",
                               "/contacto/", pagina="p-contacto")
          + cab("contacto", leccion=5) + body + pie_c(guino_izq=True))


# Lección 4 de la portada: los cuatro pasos, con las palabras de Jorge
CODE_C = {  # textos de Jorge (notas del 23-10-2026), ajustados a una longitud parecida para que las cajas cuadren
    "1": "El centro, en plena digitalización, necesitaba una herramienta para que el profesorado se autoformara.",
    "2": "Entrevisté al centro y a sus docentes, hice una curación de herramientas digitales y creé la web.",
    "3": "Tras una primera versión, la adapté a lo que los docentes necesitaban de cada herramienta.",
    "4": 'El centro la usó para la autoformación docente y la presentó al <a href="https://colegiocerradodecalderon.es/braining/" rel="noopener" target="_blank" style="color:#fff">IX Congreso de Creatividad Educativa</a>.',
}
TESTIMONIO_C = "Quiero expresarte mi agradecimiento por el excelente trabajo que has realizado al crear la nueva web de recursos TIC para nuestro colegio. Estoy seguro de que esta herramienta será de gran valor para nuestros estudiantes y docentes."


if __name__ == "__main__":
    home_c()
    lista_c()
    sobre_c()
    contacto_pag_c()
    for p in P:
        if not p.get("ext"):
            if p["slug"] in PAGINA:
                ficha_c(p["slug"])
            else:
                project(p)  # plantilla anterior, hasta que tenga sus textos en PAGINA
