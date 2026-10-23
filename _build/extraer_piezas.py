#!/usr/bin/env python3
"""Copia de assets/site.css las reglas de las piezas de las fichas de proyecto (necesidad, pasos, «Lo que puedo afirmar»,
visor de PDF, actividades incrustadas, «Ver la solución», monjes, chat del asistente, antes → ahora…) y las limita a las
fichas del rediseño (.p-ficha). Resultado: assets/curso-fichas-base.css. Encima, assets/curso-fichas.css les da la estética
nueva. Volver a ejecutarlo si cambian esas piezas en site.css:  python _build/extraer_piezas.py
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css = open(os.path.join(ROOT, "assets/site.css"), encoding="utf-8").read()
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)

PIEZAS = ["psec", "psub", "pbody", "needs", "nec", "st-l", "s-ok", "s-exp", "s-pend", "status", "upd", "mat", "emb", "cdf",
          "beh", "bchat", "bc-", "steps", "hsteps", "err", "errs", "excerpt", "dk-", "zoom", "txt", "pl", "monjes", "mo-vid",
          "i-play", "i-pause", "i-on", "i-off", "i-alt", "flip", "f-a", "f-b", "ficha1", "epo", "creditos", "caja-demo",
          "gal", "fig", "pnote", "spoiler", "vh", "cq-", "council"]
pat = re.compile(r"\.(" + "|".join(re.escape(p) for p in PIEZAS) + r")[\w-]*")


def reglas(t):
    """Divide un bloque CSS en (cabecera, cuerpo); los @media llevan su contenido como cuerpo."""
    out, i = [], 0
    while i < len(t):
        j = t.find("{", i)
        if j < 0:
            break
        cab = t[i:j].strip()
        prof, k = 1, j + 1
        while prof and k < len(t):
            prof += {"{": 1, "}": -1}.get(t[k], 0)
            k += 1
        out.append((cab, t[j + 1:k - 1]))
        i = k
    return out


def ambito(sel):
    return ",".join(".p-ficha " + s.strip() for s in sel.split(","))


def filtra(t):
    res = []
    for cab, cuerpo in reglas(t):
        if cab.startswith("@keyframes"):
            if any(p in cab for p in ("bc", "dk", "flip", "upd", "mo", "cq", "beh", "err")):
                res.append(f"{cab}{{{cuerpo}}}")
        elif cab.startswith("@media") or cab.startswith("@supports"):
            dentro = filtra(cuerpo)
            if dentro:
                res.append(f"{cab}{{{dentro}}}")
        elif cab.startswith(":root"):
            res.append(f".p-ficha{{{cuerpo}}}")  # variables de color y tipografía de site.css
        else:
            sels = [s for s in cab.split(",") if pat.search(s)]
            if sels:
                res.append(f"{ambito(','.join(sels))}{{{cuerpo}}}")
    return "\n".join(res)


salida = ("/* GENERADO por _build/extraer_piezas.py a partir de assets/site.css: no editar a mano.\n"
          "   Las piezas de las fichas de proyecto, limitadas a .p-ficha. La estética nueva va en curso-fichas.css. */\n" + filtra(css) + "\n")
open(os.path.join(ROOT, "assets/curso-fichas-base.css"), "w", encoding="utf-8").write(salida)
print("assets/curso-fichas-base.css:", len(salida), "bytes,", salida.count("{"), "reglas")
