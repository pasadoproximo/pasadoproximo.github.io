# Portfolio de Jorge Delgado Aguilera · pasadoproximo.github.io

Web estática publicada con GitHub Pages desde la rama `main` (hay `.nojekyll`: todo se sirve tal cual).
Cada push a `main` se publica solo en 1-2 minutos. El Consejo de Clío vive en otro repositorio
(`pasadoproximo/consejo-de-clio`) y se sirve en `/consejo-de-clio/`.

## Rediseño de octubre de 2026: el porfolio como curso (rama `rediseno-2026-10`, sin publicar)

**Manda sobre lo que diga el resto de este archivo.** El brief y las maquetas (`1-home` … `6-didakora`, PNG + HTML) están en
`rediseno-porfolio-v3.zip`, en la carpeta de arriba. Las páginas deben ser **exactas a los PNG** (mismas medidas, textos y orden):
se comparan con capturas a 1280 px (maqueta servida al lado) y se revisan a 390 px.
Lo anterior queda en `_antes/`, en `main` y en las ramas `rediseno-2026-10-intento1` (maquetas v1) e `-intento2` (maquetas v2).

- Plantillas nuevas en `build.py`, sección «CURSO»: `head_c`, `cab` (barra roja de progreso a todo el ancho arriba, verde al 100 %; debajo, la cabecera de 56 px con «Lección X de 5 · Y %» sin segmentos y el menú Índice ·
  Proyectos · Sobre mí · Contacto; las dos bajan fijas con la página), `pie_c`, `home_c` (/), `lista_c` (/proyectos/), `ficha_c` (fichas con textos en `PAGINA` de
  `data.py`), `sobre_c` (/sobre-mi/), `contacto_pag_c` (/contacto/). Estilos en `assets/curso.css`, scripts en `assets/curso.js`
  (subir `CURSOV` si cambian). El marcado copia los estilos en línea de las maquetas; el bloque móvil de la maqueta va al
  **final** del CSS (en la maqueta iba delante y las reglas de escritorio lo anulaban).
- Fichas de proyecto: la del Consejo, con sus textos en `PAGINA` (`ficha_c`); las otras 14, automáticas (`ficha_auto`): su
  contenido de siempre de `data.py`, sin cambiar textos, con el formato y el orden del Consejo, que manda para
  todas (Jorge, 23-10-2026): cabecera y cuatro cajas → «La necesidad» (el párrafo a la izquierda y «Qué hice / Cómo lo hice /
  Para qué lo hice» en filas a la derecha) → bloque visual con los botones → «Lo que hice yo» → el resto → «Lo que puedo
  afirmar», siempre al final. Sus piezas antiguas (visor de PDF,
  actividades incrustadas, monjes, chat…) llevan el CSS de `site.css` limitado a `.p-ficha` (`assets/curso-fichas-base.css`,
  generado con `_build/extraer_piezas.py`: no editar a mano) y la estética nueva encima (`assets/curso-fichas.css`), más
  `site.js`. «Lo que hice yo» en las de IA (`CON_IA`) con «[texto de Jorge]» hasta que Jorge dé los textos; al tenerlos, pasar
  el proyecto a `PAGINA`. Sin bloque visual propio (llevan `<!-- TODO visual -->`): Monasterio (su vídeo está en «Cómo
  funciona»), Asistente, Repositorio digital y e-Portfolio: ya tienen vídeo con la plantilla (`VIDEO_FICHA`, `ficha.webm`); el
  vídeo antiguo del Monasterio (con música) sale de «Cómo funciona». `project()` queda como plantilla anterior.
- Pie: solo la línea «© 2026 Jorge Delgado Aguilera · Campanillas, Málaga» con el estilo de la maqueta (sin «¿Hablamos?»). En la
  portada y en Contacto, el guiño «Curso completado al 100 % · Ya sabes qué hago».
- Formulario «Contacta»: Formspree, ID `mljjerlq` (cuenta de Jorge).
- Actividad de la portada: B en navy con feedback verde; A y C en rojo explicando por qué están mal (textos aprobados).
- /proyectos/: 6 destacados y 9 en la tabla. «Mi parte»: Consejo «Diseño de los roles e instrucciones», Asistente
  «Configuración, materiales y pruebas», Mantenimiento con agentes «Diseño del equipo y aprobación de cada cambio».
  Años y herramientas de la tabla: los del repo, no los de la maqueta. «Verifica lo que dice la IA»: «Demo sin login», sin enlace
  hasta que exista el curso.
- Consejo de Clío: textos de Jorge de la v2, vídeo y PDF de la sesión real de Ucrania, capturas Arendt/Ibn Jaldún en «Comprobado»,
  aviso «Contrasta siempre la información» antes de «Todas las fichas». Sin fragmento de instrucciones (Jorge: «de momento no»).
- Sobre mí: hostelería «Ibis Málaga Centro, recepcionista» (desde 2015 en varias empresas); PROA+ 30 alumnos, de 4 a 7.
- El correo no va en el hero (la maqueta no lo lleva).
- Repositorio digital: de Didákora solo queda el párrafo de «Mantenerlo al día» con «Abrir Didákora» y «Ver el Monasterio»
  (Jorge: Didákora ya tiene su sitio). Sin tabla de antes y ahora, sin «Así es Didákora» ni su vídeo (`didakora.webm` ya no
  se usa en el rediseño; se conserva para `_antes/`). Se cambia al final de `data.py`.
- **Vídeos de proyecto: todos con la estética del del Consejo de Clío** (aprobada por Jorge el 23-10-2026). Plantilla en
  `_build/plantilla-video/` (añadir el proyecto a `P` en su script; en modo `grabar=1` la ficha central carga la grabación) y
  ejemplo de grabación en `_build/grabar_consejo_plantilla.js`; los demás, con `_build/grabar_ficha.js` (un guion por proyecto;
  el Monasterio necesita su `servidor.py` en el 8020 y va a ×1,5; Repositorio y e-Portfolio, capturas de Google Sites con
  `_build/capturar_sites.js`, fuera de git). Textos del cierre: `proyectos.js`, generado por `build.py`. Reglas:
  - Fondo navy `#061033` en todo el vídeo; barra roja fina arriba que avanza con el vídeo y se pone verde en el cierre.
  - Intro de 2 s: etiqueta «Ficha de trabajo · [proyecto]» en sky, título Bricolage 800 en blanco, subtítulo (el de su página)
    en `#E6EBF8`, firma «Jorge Delgado Aguilera · pasadoproximo.github.io».
  - La grabación ocupa **toda la pantalla** (nada de una pantalla dentro de otra), en modo claro, con el fondo de la web grabada
    en navy y sus tarjetas en crema suave (`--surface:#FBF6E8`) para que destaquen los carteles.
  - Carteles: ficha blanca, borde navy, sombra dura sky, **centrados abajo**; etiqueta roja pequeña (el paso) y el texto en
    Alegreya Sans con la parte clave en negrita. El cartel cambia a la vez que empieza el desplazamiento.
  - Cierre de 2 s: «Lo que puedo afirmar» con Comprobado / En uso / Pendiente (en verde, rojo y gris claros) y la firma.
  - Unos 30 s. 16:9 (1280×720, WebM VP9) para la web y 9:16 (1080×1920, MP4 H.264, la web grabada a 540 px y ampliada ×2)
    para Instagram, este fuera del repo en `../videos-instagram/` (lo sube Jorge).
  - En la página: póster = miniatura navy de la plantilla (`?s=miniatura`), botón blanco «Ver el vídeo · 30 s» encima; los
    controles aparecen al pulsar; marco fino navy, sin sombra.

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
- `sitemap.xml` (índice: el del porfolio y el de Didákora), `sitemap-porfolio.xml` y `robots.txt` → generados por `build.py`
  (`sitemap()`). El Consejo de Clío no entra: es otro repo y no se enlaza.
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

- Publicado el rediseño el 23-10-2026 (`main` = `rediseno-2026-10`). Jorge lo revisa en local y pide cambios: corregir en la
  rama y volver a publicar.
- Repositorio digital, «Mantenerlo al día»: ¿punto en vez de dos puntos, como en Didákora? Sin decidir.
- Las 10 fichas sin «Lo que puedo afirmar»: Jorge las revisa una a una.

- «Probar el consejo» sigue en claude.ai (usa la IA de Claude): pide iniciar sesión, es inevitable.
