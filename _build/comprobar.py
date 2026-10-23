#!/usr/bin/env python3
"""Comprobación final del porfolio (brief 2.8): enlaces internos rotos (archivos y #anclas), imágenes sin alt, títulos
duplicados, meta description ausentes y contraste de los colores del rediseño.
Uso:  python _build/comprobar.py   (desde la raíz del repositorio, después de build.py)"""
import os, re, glob, html
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGINAS = ["index.html", "proyectos/index.html", "sobre-mi/index.html", "contacto/index.html"] + sorted(
    glob.glob("proyectos/*/index.html", root_dir=ROOT))
ids = {}
textos = {}
for f in PAGINAS:
    t = open(os.path.join(ROOT, f), encoding="utf-8").read()
    textos[f] = t
    ids["/" + f.replace("index.html", "")] = set(re.findall(r'\sid="([^"]+)"', t))


def destino(url, desde):
    """Ruta de archivo de un enlace interno, o None si no es interno."""
    if re.match(r"^(https?:|mailto:|tel:|data:|javascript:)", url) or url.startswith("//") or url.startswith("/didakora/"):  # Didákora: su propio repo, mismo dominio
        return None
    ruta = url.split("#")[0].split("?")[0]
    if not ruta:
        return desde
    if not ruta.startswith("/"):
        ruta = "/" + os.path.normpath(os.path.join(os.path.dirname(desde), ruta)).replace("\\", "/")
    return ruta


problemas = defaultdict(list)
titulos = defaultdict(list)
for f, t in textos.items():
    pag = "/" + f.replace("index.html", "")
    sin = re.sub(r"<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->", "", t, flags=re.S)
    for attr, url in re.findall(r'\s(href|src|poster)="([^"]+)"', sin):
        url = html.unescape(url)
        r = destino(url, f)
        if r is None:
            continue
        fs = os.path.join(ROOT, r.lstrip("/"))
        if r.endswith("/"):
            fs = os.path.join(fs, "index.html")
        if not os.path.exists(fs) and not os.path.exists(fs + "index.html"):
            problemas["Enlaces internos rotos"].append(f"{pag}: {url}")
            continue
        if "#" in url and attr == "href":
            ancla = url.split("#", 1)[1]
            dest = r if r.endswith("/") else r
            if ancla and dest in ids and ancla not in ids[dest] and not ancla.startswith(("aula", "herramientas", "profesorado")):
                problemas["Anclas que no existen"].append(f"{pag}: {url}")
    for img in re.findall(r"<img\b[^>]*>", sin):
        if not re.search(r'\salt="', img):
            problemas["Imágenes sin alt"].append(f"{pag}: {img[:90]}")
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    titulos[m.group(1).strip() if m else "(sin título)"].append(pag)
    d = re.search(r'<meta name="description" content="([^"]*)"', t)
    if not d or len(d.group(1).strip()) < 30:
        problemas["Meta description ausente o muy corta"].append(pag)
for tt, ps in titulos.items():
    if len(ps) > 1 or tt == "(sin título)":
        problemas["Títulos duplicados o ausentes"].append(f"{tt}: {', '.join(ps)}")


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + .05) / (lb + .05)


# pares de color de las fichas y bloques nuevos: (texto, fondo, para qué, ¿texto grande?)
PARES = [("#5A6480", "#FFFFFF", "texto gris de las fichas", False), ("#5A6480", "#F2F4F9", "texto gris sobre el fondo", False),
         ("#A3322A", "#FFFFFF", "etiqueta roja (tipo) en ficha", False), ("#A3322A", "#F2F4F9", "etiqueta roja sobre el fondo", False),
         ("#5E7D3A", "#FFFFFF", "estado verde en ficha", False), ("#5E7D3A", "#F2F4F9", "estado verde sobre el fondo", False),
         ("#061033", "#9FB3FF", "texto navy sobre el subrayador sky", False), ("#9FB3FF", "#061033", "acento sky en bloque navy", False),
         ("#E6EBF8", "#061033", "texto claro en bloque navy", False), ("#FFFFFF", "#A3322A", "texto blanco en la opción roja", False),
         ("#061033", "#F6E0DD", "feedback rojo claro", False), ("#061033", "#DCE7D0", "feedback verde claro", False)]
contraste = [(round(ratio(a, b), 2), a, b, q, g) for a, b, q, g in PARES]

print(f"Páginas revisadas: {len(PAGINAS)}\n")
for k in ["Enlaces internos rotos", "Anclas que no existen", "Imágenes sin alt", "Títulos duplicados o ausentes", "Meta description ausente o muy corta"]:
    v = problemas.get(k, [])
    print(f"{k}: {len(v)}")
    for x in v:
        print("   ·", x)
print("\nContraste (WCAG AA: 4,5 en texto normal, 3 en texto grande):")
for r, a, b, q, g in contraste:
    print(f"   {'OK ' if r >= (3 if g else 4.5) else 'BAJO'} {r:>5}  {a} sobre {b}  ({q})")
