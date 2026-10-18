# Portfolio de Jorge Delgado Aguilera · pasadoproximo.github.io

Web estática publicada con GitHub Pages desde la rama `main` (hay `.nojekyll`: todo se sirve tal cual).
Cada push a `main` se publica solo en 1-2 minutos. El Consejo de Clío vive en otro repositorio
(`pasadoproximo/consejo-de-clio`) y se sirve en `/consejo-de-clio/`.

## Estructura

- `index.html`, `proyectos/index.html`, `proyectos/<slug>/index.html` → **generados**. No editarlos a mano.
- `_build/data.py` → el contenido: categorías (`CATS`), los 14 proyectos (`P`) y los destacados (`FEATURED`).
- `_build/build.py` → genera las páginas a partir de `data.py`. Plantillas de portada, índice y ficha.
- `_build/source_old.html` → de aquí se copian las animaciones de las tarjetas y las secciones de la portada
  **Experiencia, Formación (con «Con qué trabajo») y Contacto**. Para cambiar esas secciones, editar este archivo.
- `assets/site.css`, `assets/site.js` → estilos y scripts comunes. Si cambian, subir `CSSV` en `build.py`
  (rompe la caché del navegador).
- `herramientas/` → la «Caja de herramientas digitales». Página propia, se edita directamente
  (`index.html` + `tools.js` con los datos; logos en `herramientas/logos/`).
- `apps/` → el Mapa de relieves y El bombo, recuperados de claude.ai y alojados aquí (no dependen de Claude).
- `anterior/` → copia de la portada antigua (sin indexar). No tocar.
- `_build/cv.html` → fuente del CV. Para regenerar el PDF: Chrome headless con `--print-to-pdf` (comando al inicio del archivo).
- `assets/pdf/` → materiales descargables y el CV. `assets/proyectos/<slug>/` → capturas reales de cada proyecto.

## Flujo de trabajo

1. Editar `_build/data.py` (o `build.py` / `source_old.html` / `assets/`).
2. `python3 _build/build.py` (necesita Python 3 y Pillow; en este equipo: `%LOCALAPPDATA%/Programs/Python/Python312/python.exe`).
3. Probar en local: `python3 -m http.server 8000` y abrir http://localhost:8000. Revisar escritorio y móvil (390 px):
   que nada se salga por los lados y que los enlaces internos funcionen.
4. Commit con autor `Jorge Delgado Aguilera <jorgedelagui@gmail.com>` y mensaje en español que diga qué cambia.
5. `git pull --rebase` antes de `git push` por si hay cambios de otra sesión.

## Identidad visual (no cambiarla)

- Azul marino `#061033`, `--navy3 #1B2C6B`, azul claro `--sky #9FB3FF`, `--ice #DDE4F6`, fondo `--bg #F2F4F9`.
- Tipografías: Bricolage Grotesque (títulos), Alegreya SC (citas), Alegreya Sans (texto).
- Bloques redondeados tipo «bento», barra superior en píldora que se pega arriba al bajar, foco azulado que sigue al ratón.
- Criterio acordado: **pocos cajones**. Cajón solo para lo que se pulsa o lo que debe destacar (bloques azul marino);
  el texto informativo va sobre el fondo, separado con líneas finas `#D3DAEA`.

## Contenido: normas

- Tono humilde y concreto. Nada de títulos grandilocuentes («experto», «consultor»).
- Titular actual: «Diseño de materiales educativos digitales · Profesor de Geografía e Historia».
  Objetivo: empleo en educación digital fuera del aula.
- Solo experiencia educativa en la web.
- **No inventar** métricas, resultados, capturas ni testimonios. El TFM (asistente GPT 2.º ESO) **no se ha pilotado
  con alumnado**: distinguir siempre comprobado / esperado / pendiente. Del repositorio no hay datos de uso.
- Capturas solo reales. Si falta una, pedirla a Jorge en vez de simularla.
- Cursos con formato «4.º ESO», «2.º Bachillerato». Etiquetas de tarjeta: formato · nivel o destinatario.
- No mostrar el teléfono. Contacto: correo, LinkedIn, Instagram @pasadoproximo.
- Nunca publicar ni programar nada en redes en nombre de Jorge: dejarlo preparado y que él pulse.

## Proyectos

- Casos de estudio (`kind="caso"`): repositorio digital, asistente TFM y Consejo de Clío. Usan todo el ancho y bloques
  horizontales (`needs`, `hsteps`, `gal frame`, `status`). El Consejo tiene además su web completa en `/consejo-de-clio/`,
  con la misma barra que el portfolio.
- Todas las páginas (portfolio, Caja de herramientas y Consejo) comparten la misma barra: solo logo + menú.
- El resto son fichas breves (`kind="ficha"`): descripción, material real, nivel y enlace.
- Destacados en portada, en este orden: repositorio, asistente, Consejo de Clío, Cazadores de bulos.
- En Cazadores de bulos solo se muestran 2 de los 9 errores (no revelar el resto).

## Pendiente

- «Probar el consejo» sigue en claude.ai (usa la IA de Claude): pide iniciar sesión, es inevitable.
