# Portfolio de Jorge Delgado Aguilera · pasadoproximo.github.io

Web estática publicada con GitHub Pages desde la rama `main` (hay `.nojekyll`: todo se sirve tal cual).
Cada push a `main` se publica solo en 1-2 minutos. El Consejo de Clío vive en otro repositorio
(`pasadoproximo/consejo-de-clio`) y se sirve en `/consejo-de-clio/`.

## Estructura

- `index.html`, `proyectos/index.html`, `proyectos/<slug>/index.html` → **generados**. No editarlos a mano.
- `_build/data.py` → el contenido: categorías (`CATS`), los 15 proyectos (`P`) y los destacados (`FEATURED`).
- `_build/build.py` → genera las páginas a partir de `data.py`. Plantillas de portada, índice y ficha.
- `_build/source_old.html` → de aquí se copian las animaciones de las tarjetas y las secciones de la portada
  **Experiencia, Formación (con «Con qué trabajo») y Contacto**. Para cambiar esas secciones, editar este archivo.
- `assets/site.css`, `assets/site.js` → estilos y scripts comunes. Si cambian, subir `CSSV` en `build.py`
  (rompe la caché del navegador).
- `herramientas/` → la antigua «Caja de herramientas digitales», que en octubre de 2026 pasó a ser **Didákora**, una web propia
  (repo `pasadoproximo/didakora` → https://pasadoproximo.github.io/didakora/, con su propio CLAUDE.md). Aquí solo quedan:
  `herramientas/index.html`, que redirige a Didákora (con `#id` lleva a la ficha y con `?q=` a la búsqueda), y
  `herramientas/logos/`, que usa la página del Repositorio digital (y `tools.js`, ya sin uso, como copia de los datos de 2026). No editar la caja aquí.
- El menú enlaza a «Didákora» (`/didakora/`). La página del Repositorio digital explica el paso de 2024 a Didákora con un vídeo real
  de la web (`assets/proyectos/repositorio-digital/didakora.webm` + póster `didakora-video.jpg`, 34 s, sin sonido, en bucle,
  con botón de pausa; no arranca si el sistema pide reducir el movimiento). Si Didákora cambia mucho, regrabarlo con
  `_build/grabar_video.js` (Playwright + Chrome, con Didákora servida en el 8020; las instrucciones están al principio del script) y subir el `?v=` en `data.py`.
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
- Bloques redondeados tipo «bento», barra superior en píldora que se pega arriba al bajar (siempre redondeada, a 12 px del borde; también en el Consejo), foco azulado que sigue al ratón.
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
  horizontales (`needs`, `hsteps`, `gal frame`, `status`). El Consejo tiene su web en `/consejo-de-clio/`, pero **no se enlaza**
  desde el portfolio. Su página de proyecto (título del hero: solo el nombre): el problema en un párrafo →
  seis caras numeradas que hablan por turnos (`.cq-board`, se pueden pulsar y pausar; las caras salen de `[[AV:n]]`) →
  «Cómo funciona», mezclado con la sesión real: tres pasos en vertical unidos por una línea (todos en azul marino) y el vídeo grande (recortado a la conversación
  y la revisión, `assets/proyectos/consejo-de-clio/sesion.webm`) → aviso «Contrasta siempre la información». Poca chapa:
  que se entienda a simple vista.
- «Lo que puedo afirmar» (`.status`): tarjetas blancas con sombra suave y el título en azul (`--navy3`).
- Todas las páginas (portfolio y Consejo) comparten la misma barra: solo logo + menú. Didákora tiene su propia barra.
- Índice `/proyectos/`: botones en píldora (pestañas, `.ct`): «Todos» y las tres categorías; el elegido queda en azul marino
  y debajo salen su descripción y sus proyectos. Orden: Todos (elegida al entrar), Profesorado y formación, Herramientas y asistentes,
  Actividades de aula. Flechas izquierda/derecha para moverse; `/proyectos/#aula` elige esa. Sin JavaScript se ven todas.
- Tarjetas de proyecto (`card()`), en la portada y en todas partes: solo el visual y el título, centrado, sin etiqueta gris,
  sin texto ni flecha ni foco que sigue al ratón.
- Pie común (`foot()`): bloque azul marino «¿Hablamos?» con los contactos como iconos y el templo del logo que se construye
  por piezas (animación); debajo, nombre y lugar. En la portada sustituye a la antigua sección «Contacto» (`#contacto`).
- Repositorio digital, «Mantenerlo al día»: filas antes → ahora (`.upd`, sin cajas): en «Antes» los iconos originales (archivados en Wayback Machine, en `assets/proyectos/repositorio-digital/antes/`; EarTeach y Hablaconlahistoria no tenían, llevan un icono propio: oreja y Colón) en gris y tachados; en «Ahora» los logos reales, en dos columnas compactas;
  debajo «Así es Didákora» (texto + vídeo real de Didákora). Ya no hay bloques 2024/2026 ni la animación de la caja antigua.
- Títulos de sección: la descripción va siempre debajo del título, nunca a la derecha (`.sec-head` en columna).
- **El monasterio de Didákora** (`monasterio-didakora`, caso de Herramientas): el sistema de cinco agentes de IA que mantiene Didákora
  y su interfaz de videojuego (vive en el repo de Didákora, `agentes/monasterio/`, privado y solo en local). Página: la necesidad →
  los cinco monjes con su retrato (`.monjes`) → «Cómo funciona» (`hsteps four` + vídeo real) → «Lo que puedo afirmar» → créditos del
  arte LPC (CC-BY-SA/GPL: obligatorio citarlos; `assets/proyectos/monasterio-didakora/creditos.txt`). Las cifras salen de los
  registros de los ciclos: actualizarlas si se citan nuevas. Vídeo: **recreación avisada** (Jorge la eligió el 21-10-2026) del
  ciclo 2026-10-21-3 con el modo `?demo=<ciclo>` del monasterio, que repite un ciclo real con sus datos sin lanzar ni escribir
  nada; la página y el vídeo dicen que es una recreación. Se graba con `_build/grabar_monasterio.js` (instrucciones al principio).
  Música: chiptune medieval original (`_build/musica_monasterio.py` → `musica.wav`, bucle de 32 s), en un `<audio>` aparte
  porque el ffmpeg disponible no codifica audio. Está **apagada al entrar** (Jorge lo pidió): suena solo al pulsar el
  altavoz (`.dk-son`), sigue al vídeo y se reinicia con cada vuelta. El vídeo de Didákora
  (Repositorio digital) va sin música: Jorge la descartó. El Repositorio digital enlaza a él con una línea (`.dk-mas`).
- El resto son fichas breves (`kind="ficha"`): descripción, material real, nivel y enlace.
- Destacados en portada, en este orden: repositorio, asistente, Consejo de Clío, Cazadores de bulos.
- En Cazadores de bulos solo se muestran 2 de los 9 errores (no revelar el resto).

## Pendiente

- «Probar el consejo» sigue en claude.ai (usa la IA de Claude): pide iniciar sesión, es inevitable.
