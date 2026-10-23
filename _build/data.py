import re
# Contenido de los proyectos del portfolio.
# Todo sale de los materiales reales (PDF, TFM, webs publicadas). No se inventan resultados.

CATS = {
    "herramientas": {
        "name": "Herramientas y asistentes",
        "desc": "Aplicaciones y asistentes que he diseñado para que el alumnado o el docente trabajen de otra manera.",
    },
    "aula": {
        "name": "Actividades de aula",
        "desc": "Situaciones de aprendizaje listas para llevar a clase, con su guía docente y sus materiales.",
    },
    "profesorado": {
        "name": "Profesorado y formación",
        "desc": "Recursos y guías para el trabajo docente. Portfolio del Máster de Competencias Digitales.",
    },
}

ICON_EXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
ICON_DL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'

P = []

# ---------------------------------------------------------------- HERRAMIENTAS
P.append(dict(
    slug="consejo-de-clio", cat="herramientas", year="2026",
    title="El Consejo de Clío", tags=["Aplicación con IA", "Secundaria"], kind="caso",
    card="Seis agentes de IA convierten una noticia de hoy en una sesión de clase y uno revisa a todos.",
    viz="council",
    h1="El Consejo de Clío",
    lede="Pegas una noticia, eliges el curso y seis personajes de la historia preparan una sesión para el aula.",
    meta=[("Para quién", "Docentes de Geografía e Historia, de 1.º ESO a Bachillerato"),
          ("Tipo", "Aplicación con IA · material de libre uso"),
          ("Herramientas", "Claude (artefacto con agentes de IA)"),
          ("Estado", "Publicada. Funciona con una cuenta de Claude, también la gratuita")],
    links=[("Probar el consejo", "https://claude.ai/artifact/7fyLPT3yg45X1Wr4Mu9rjx", "ext")],
    cta_note="Se abre en Claude y pide iniciar sesión (sirve la cuenta gratuita).",
    sections=[
        ("La necesidad", """
<p class="psub">Traer la actualidad a clase de Historia es necesario y engancha al alumnado. Prepararlo bien lleva tiempo y pedírselo sin más a una IA puede traer problemas.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Una herramienta con IA para docentes.</span></li>
<li><b>Cómo lo hice</b><span>Creando un equipo de seis agentes de IA en Claude.</span></li>
<li><b>Para qué lo hice</b><span>Para agilizar el proceso y filtrar la información.</span></li>
</ul>"""),
        ("Seis pensadores, un equipo", """
<p class="psub">Un pequeño equipo de agentes de IA: cada miembro hace una sola tarea y le pasa su trabajo al siguiente. Pulsa en cada cara para ver qué hace.</p>
<div class="cq cq-board">
<ol class="cq-team" aria-label="Los seis miembros del consejo, en orden">
<li><button type="button" class="cq-m" data-n="Heródoto" data-r="Resume la noticia" data-t="Lee la noticia y cuenta qué ha pasado y cuáles son las claves, sin opinar." aria-pressed="true"><span class="cq-face">[[AV:0]]<span class="cq-n">1</span><span class="cq-ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span><b>Heródoto</b><small>Resume la noticia</small></button></li>
<li><button type="button" class="cq-m" data-n="Tucídides" data-r="La sitúa en el temario" data-t="Busca la unidad y los apartados del curso elegido con los que encaja la noticia y avisa si el encaje es solo parcial." aria-pressed="false"><span class="cq-face">[[AV:1]]<span class="cq-n">2</span><span class="cq-ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span><b>Tucídides</b><small>La sitúa en el temario</small></button></li>
<li><button type="button" class="cq-m" data-n="Hannah Arendt" data-r="La conecta con el presente" data-t="Compara las dos épocas: qué se repite, qué ha cambiado y por qué importa hoy." aria-pressed="false"><span class="cq-face">[[AV:2]]<span class="cq-n">3</span><span class="cq-ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span><b>Hannah Arendt</b><small>La conecta con el presente</small></button></li>
<li><button type="button" class="cq-m" data-n="Clío" data-r="Se la cuenta al alumnado" data-t="Escribe el relato para la clase, del hecho histórico a la noticia de hoy." aria-pressed="false"><span class="cq-face">[[AV:3]]<span class="cq-n">4</span><span class="cq-ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span><b>Clío</b><small>Se la cuenta al alumnado</small></button></li>
<li><button type="button" class="cq-m" data-n="Sócrates" data-r="Plantea el debate" data-t="Propone tres preguntas abiertas para debatir en clase, sin dar la respuesta." aria-pressed="false"><span class="cq-face">[[AV:4]]<span class="cq-n">5</span><span class="cq-ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span><b>Sócrates</b><small>Plantea el debate</small></button></li>
<li><button type="button" class="cq-m" data-n="Ibn Jaldún" data-r="Revisa a todos" data-t="Repasa el trabajo de los otros cinco, señala lo que falla y pide que se corrija antes de dar la sesión por buena." aria-pressed="false"><span class="cq-face">[[AV:5]]<span class="cq-n">6</span><span class="cq-ok" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span><b>Ibn Jaldún</b><small>Revisa a todos</small></button></li>
<li class="cq-line" aria-hidden="true"><i></i></li>
</ol>
<div class="cq-say" aria-live="polite"><span class="cq-k">1</span><div><b>Heródoto</b><span class="cq-r">Resume la noticia</span><p>Lee la noticia y cuenta qué ha pasado y cuáles son las claves, sin opinar.</p></div><button type="button" class="cq-play" aria-label="Pausar la animación">Pausar</button></div>
</div>"""),
        ("Cómo funciona", """
<p class="psub">Tres pasos, con una sesión real.</p>
<div class="cq-how">
<ol class="cq-pasos">
<li><b>Pegas una noticia y eliges el curso</b><span>En el vídeo, el acuerdo de la NASA para llevar un reactor nuclear al espacio, para 4.º ESO.</span></li>
<li><b>Cada pensador hace su parte</b><span>Resumen, encaje en el temario (la Guerra Fría y el Sputnik), relato y preguntas para debatir.</span></li>
<li><b>Ibn Jaldún revisa y corrige</b><span>Clío daba por hecho una opinión de la autora. Se corrige antes de llegar a clase.</span></li>
</ol>
<div class="dk-video cq-vid">
<video src="/assets/proyectos/consejo-de-clio/sesion.webm" poster="/assets/proyectos/consejo-de-clio/sesion-poster.jpg" width="720" height="866" muted loop playsinline preload="metadata" aria-label="Vídeo de una sesión real: los seis pensadores trabajan por turnos e Ibn Jaldún corrige un error de Clío"></video>
<button type="button" class="dk-play" aria-label="Pausar el vídeo"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-pause" d="M9 6v12M15 6v12"/><path class="i-play" d="M8 5.5v13l11-6.5z"/></svg></button>
<script>(()=>{const w=document.currentScript.parentElement,v=w.querySelector("video"),b=w.querySelector(".dk-play");
const set=on=>{w.classList.toggle("paused",!on);b.setAttribute("aria-label",on?"Pausar el vídeo":"Reproducir el vídeo");};
b.addEventListener("click",()=>{if(v.paused){v.play();set(true);}else{v.pause();set(false);}});
// arranca al verse en pantalla, salvo si el sistema pide reducir el movimiento
if(matchMedia("(prefers-reduced-motion: reduce)").matches){set(false);return;}
new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&!w.classList.contains("paused"))v.play().catch(()=>set(false));else if(!e.isIntersecting)v.pause();}),{threshold:.3}).observe(v);})();</script>
</div>
</div>"""),
        ("Antes de llevarlo a clase", """
<div class="cq-warn"><div class="cq-wh"><svg class="cq-wi" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5 2.5 20h19z"/><path d="M12 10v4.5M12 17.4v.1"/></svg><b>Contrasta siempre la información</b></div>
<p>Los seis miembros del consejo son una IA y pueden equivocarse. Ibn Jaldún reduce los errores, pero no los elimina, porque también es una IA. Antes de usar la sesión en el aula, comprueba los datos con la noticia original y con otras fuentes fiables. Esto simplemente es un filtro más.</p></div>"""),
    ],
    related=["asistente-gpt-2eso", "la-ia-tambien-miente", "cazadores-de-bulos"],
))

P.append(dict(
    slug="monasterio-didakora", cat="herramientas", year="2026",
    title="El monasterio de Didákora", tags=["Agentes de IA", "Mantenimiento web"], kind="caso",
    card="Cinco agentes de IA mantienen Didákora al día y yo decido desde un videojuego.",
    viz="img:/assets/proyectos/monasterio-didakora/tarjeta.png",
    h1="El monasterio de Didákora",
    lede="Cinco agentes de IA revisan Didákora y me proponen cambios. Yo decido desde un monasterio en pixel art.",
    meta=[("Para quién", "Didákora, mi web de herramientas digitales para docentes"),
          ("Tipo", "Equipo de agentes de IA con una interfaz de videojuego"),
          ("Herramientas", "Claude Code (cinco subagentes), Python y JavaScript"),
          ("Estado", "En uso desde octubre de 2026. Funciona en mi ordenador: no está publicado")],
    links=[],
    sections=[
        ("La necesidad", """
<p class="psub">Una web de herramientas educativas se queda vieja enseguida: unas cierran, otras cambian de nombre o de dirección y cada semana salen otras nuevas. Revisarla a mano lleva muchas horas.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Un equipo de cinco agentes de IA que mantiene Didákora al día.</span></li>
<li><b>Cómo lo hice</b><span>Con subagentes de Claude Code y un videojuego para supervisarlos.</span></li>
<li><b>Para qué lo hice</b><span>Para tener la web siempre actualizada sin perder el control de lo que se publica.</span></li>
</ul>"""),
        ("Cinco monjes, un equipo", """
<p class="psub">Cada agente es un monje con un solo oficio. Ninguno publica nada: eso lo decido yo.</p>
<ul class="monjes">
<li><img src="/assets/proyectos/monasterio-didakora/rastreador.png" alt="" width="96" height="96" loading="lazy"><b>Fray Gaspar</b><small>Rastreador</small><span>Busca novedades en fuentes como el INTEF o Educación 3.0 y anota cada hallazgo con su fuente.</span></li>
<li><img src="/assets/proyectos/monasterio-didakora/coordinador-editorial.png" alt="" width="96" height="96" loading="lazy"><b>Fray Anselmo</b><small>Coordinador</small><span>Lo cruza con el catálogo y me lo presenta en pergaminos, con opciones para decidir.</span></li>
<li><img src="/assets/proyectos/monasterio-didakora/administrador-web.png" alt="" width="96" height="96" loading="lazy"><b>Fray Bartolomé</b><small>Administrador</small><span>Hace solo lo que apruebo: cambia la web, la regenera y pasa las pruebas.</span></li>
<li><img src="/assets/proyectos/monasterio-didakora/auditor.png" alt="" width="96" height="96" loading="lazy"><b>Fray Custodio</b><small>Auditor</small><span>Revisa enlaces, textos, el buscador y cómo se ve en el móvil, antes y después.</span></li>
<li><img src="/assets/proyectos/monasterio-didakora/optimizador.png" alt="" width="96" height="96" loading="lazy"><b>Fray Ambrosio</b><small>Optimizador</small><span>Cuando lo convoco, estudia los ciclos y propone mejoras para el propio equipo.</span></li>
</ul>"""),
        ("Cómo funciona", """
<p class="psub">Un ciclo, de la campana a la web. El vídeo es una recreación con los datos reales de un ciclo: lo que encontraron, propusieron, hicieron y revisaron los monjes y lo que aprobé.</p>
<ol class="hsteps four">
<li><b>Toco la campana</b><span>Fray Gaspar recorre las fuentes aprobadas y Fray Anselmo prepara las propuestas.</span></li>
<li><b>Sello los pergaminos</b><span>Apruebo, edito o rechazo cada propuesta en el tablón o hablando con Fray Anselmo.</span></li>
<li><b>Ellos lo hacen y lo revisan</b><span>Fray Bartolomé cambia la web y Fray Custodio la revisa, también en el móvil.</span></li>
<li><b>Yo publico</b><span>Veo el antes y el después de cada cambio en el Libro del Abad y decido cuándo sale a la web.</span></li>
</ol>
<div class="dk-video mo-vid">
<video src="/assets/proyectos/monasterio-didakora/monasterio.webm?v=2" poster="/assets/proyectos/monasterio-didakora/monasterio-video.jpg?v=2" width="1264" height="712" muted loop playsinline preload="metadata" aria-label="Vídeo, recreación con los datos reales de un ciclo: suena la campana y los monjes trabajan en sus salas; Fray Gaspar cuenta lo que encontró; en el tablón se aprueban EduGems y Doc to Form Quiz Maker; Fray Bartolomé cambia la web; Fray Custodio enseña su revisión y las capturas del móvil; el Libro del Abad muestra el antes y el después"></video>
<audio src="/assets/proyectos/monasterio-didakora/musica.wav?v=1" loop preload="none"></audio>
<button type="button" class="dk-son" aria-pressed="false" aria-label="Activar la música"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-alt" d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path class="i-on" d="M15.5 9a4 4 0 0 1 0 6M18 6.5a7.5 7.5 0 0 1 0 11"/><path class="i-off" d="m16 9.5 5 5M21 9.5l-5 5"/></svg></button>
<button type="button" class="dk-play" aria-label="Pausar el vídeo"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-pause" d="M9 6v12M15 6v12"/><path class="i-play" d="M8 5.5v13l11-6.5z"/></svg></button>
<script>(()=>{const w=document.currentScript.parentElement,v=w.querySelector("video"),b=w.querySelector(".dk-play");
const set=on=>{w.classList.toggle("paused",!on);b.setAttribute("aria-label",on?"Pausar el vídeo":"Reproducir el vídeo");};
b.addEventListener("click",()=>{if(v.paused){v.play();set(true);}else{v.pause();set(false);}});
const a=w.querySelector("audio"),s=w.querySelector(".dk-son");let on=false,ult=0;
const pinta=()=>{s.setAttribute("aria-pressed",on);s.setAttribute("aria-label",on?"Silenciar la música":"Activar la música");};
const suena=()=>{if(!on||v.paused)return;a.play().catch(()=>{const go=e=>{if(e.target.closest&&e.target.closest(".dk-son"))return;quita();if(on&&!v.paused)a.play().catch(()=>{});};const quita=()=>{document.removeEventListener("pointerdown",go,true);document.removeEventListener("keydown",go,true);};document.addEventListener("pointerdown",go,true);document.addEventListener("keydown",go,true);});};
s.addEventListener("click",()=>{if(on&&a.paused&&!v.paused){a.play().catch(()=>{});return;}on=!on;pinta();on?suena():a.pause();});
v.addEventListener("play",suena);v.addEventListener("pause",()=>a.pause());
v.addEventListener("timeupdate",()=>{if(v.currentTime<ult-1){a.currentTime=0;}ult=v.currentTime;});
// arranca al verse en pantalla, salvo si el sistema pide reducir el movimiento
if(matchMedia("(prefers-reduced-motion: reduce)").matches){set(false);return;}
new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&!w.classList.contains("paused"))v.play().catch(()=>set(false));else if(!e.isIntersecting)v.pause();}),{threshold:.3}).observe(v);})();</script>
</div>"""),
        ("Lo que puedo afirmar", """
<div class="status four">
<div class="s-ok"><span class="st-l ok">Comprobado</span><p>Cuatro ciclos completos en octubre de 2026: diecisiete cambios en Didákora, entre ellos tres herramientas nuevas y el aviso de la guía de protección de datos del INTEF en doce fichas. Todos, revisados por el Auditor.</p></div>
<div class="s-ok"><span class="st-l ok">Bajo control</span><p>Los agentes no pueden publicar. Cada cambio espera mi aprobación y yo publico cuando lo he visto.</p></div>
<div class="s-exp"><span class="st-l exp">Se mejora</span><p>Fray Ambrosio estudió los primeros ciclos y propuso once mejoras para el equipo. Apliqué diez.</p></div>
<div class="s-pend"><span class="st-l pend">Pendiente</span><p>Medir cuánto tiempo ahorra frente a revisar la web a mano y si sus propuestas aciertan con más ciclos.</p></div>
</div>
<p class="creditos">Personajes y escenario: arte libre de <a href="https://lpc.opengameart.org/" rel="noopener" target="_blank">Liberated Pixel Cup</a> (CC-BY-SA 3.0 y GPL 3.0), montado y recoloreado para el monasterio. <a href="/assets/proyectos/monasterio-didakora/creditos.txt" target="_blank">Ver los créditos de cada pieza</a>.</p>"""),
    ],
    related=["consejo-de-clio", "repositorio-digital", "asistente-gpt-2eso"],
))

P.append(dict(
    slug="asistente-gpt-2eso", cat="herramientas", year="2024",
    title="Asistente de IA", tags=["TFM", "2.º ESO"], kind="caso",
    card="Un GPT que guía al alumnado sin darle la respuesta y dice siempre de dónde sale cada dato.",
    viz="v-chat",
    h1="Asistente de IA para 2.º ESO",
    lede="Un asistente de IA para 2.º ESO que guía al estudiante sin resolver.",
    meta=[("Para quién", "Un grupo de 2.º ESO y su docente de Geografía e Historia"),
          ("Tipo", "Trabajo Fin de Máster · propuesta didáctica"),
          ("Herramientas", "GPT personalizado (GPT-4o) y Google Classroom"),
          ("Estado", "Configurado y probado en simulación. Sin pilotar con alumnado")],
    links=[("Leer el TFM completo (PDF)", "/assets/pdf/tfm-asistente-gpt-2eso.pdf", "dl")],
    sections=[
        ("La necesidad", """
<p class="psub">En muchos institutos públicos se producen los mismos problemas: aulas de 25 a 30 estudiantes, retroalimentación que llega tarde o no llega, dudas sin resolver que van a casa y un alumnado que usa ChatGPT para que le haga la tarea.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Configuración de un GPT personalizado para la clase de Geografía e Historia en 2.º ESO.</span></li>
<li><b>Cómo lo hice</b><span>Introduje el material de clase y le di instrucciones para guiar sin resolver y no pedir datos personales.</span></li>
<li><b>Para qué lo hice</b><span>Para ayudar a la diversidad del aula y concienciar sobre el uso adecuado de la IA.</span></li>
</ul>"""),
        dict(title="Qué hace en la práctica",
             intro='<p class="psub">Cuatro comportamientos configurados y probados.</p>',
             cols=2, figs=[],
             after="""<div class="beh">
<div class="beh-i"><h3>Guía, no resuelve</h3>
<div class="bchat"><div class="bc-top"><span class="bc-av" aria-hidden="true"><svg viewBox="0 0 26 26"><path d="M13 2 2 7h22L13 2Z"/><rect x="3" y="8" width="20" height="2"/><rect x="5" y="11" width="2.4" height="9"/><rect x="9.6" y="11" width="2.4" height="9"/><rect x="14" y="11" width="2.4" height="9"/><rect x="18.6" y="11" width="2.4" height="9"/><rect x="2" y="21" width="22" height="2.4"/></svg></span>PasadoPróximo-2ºESO</div><p class="bc-u s" style="--d:0.3s">¿Puedes hacerme la actividad 2 del tema 1?</p><div class="bc-a s" style="--d:1.1s"><span class="bc-dots" aria-hidden="true"><i></i><i></i><i></i></span><p class="s" style="--d:2.4s">Puedo ayudarte con la actividad 2 del tema 1, <mark>pero no puedo realizar la actividad por ti.</mark> Mi objetivo es guiarte para que puedas completarla por ti mismo, fomentando tu aprendizaje activo.</p><p class="s" style="--d:3.0s">Dicho esto, dime cuál es la actividad 2 y en qué parte te gustaría que te ayudara.</p></div></div></div>
<div class="beh-i"><h3>Cita la unidad</h3>
<div class="bchat"><div class="bc-top"><span class="bc-av" aria-hidden="true"><svg viewBox="0 0 26 26"><path d="M13 2 2 7h22L13 2Z"/><rect x="3" y="8" width="20" height="2"/><rect x="5" y="11" width="2.4" height="9"/><rect x="9.6" y="11" width="2.4" height="9"/><rect x="14" y="11" width="2.4" height="9"/><rect x="18.6" y="11" width="2.4" height="9"/><rect x="2" y="21" width="22" height="2.4"/></svg></span>PasadoPróximo-2ºESO</div><div class="bc-a s" style="--d:0.3s"><span class="bc-dots" aria-hidden="true"><i></i><i></i><i></i></span><p class="s" style="--d:1.6s"><b>4. La Compleja Sociedad de la Península Ibérica</b></p><p class="s" style="--d:2.2s"><b>Sociedad en Al-Ándalus:</b> Compuesta por árabes, bereberes, muladíes (convertidos al Islam) y no musulmanes como los judíos y mozárabes (cristianos en territorio musulmán). […]</p><p class="s" style="--d:2.8s"><mark>La información ha sido extraída de los documentos que subiste, específicamente del documento de la <b>Unidad 5 - La Península Ibérica en la Edad Media</b>.</mark></p></div></div></div>
<div class="beh-i"><h3>Avisa si es IA</h3>
<div class="bchat"><div class="bc-top"><span class="bc-av" aria-hidden="true"><svg viewBox="0 0 26 26"><path d="M13 2 2 7h22L13 2Z"/><rect x="3" y="8" width="20" height="2"/><rect x="5" y="11" width="2.4" height="9"/><rect x="9.6" y="11" width="2.4" height="9"/><rect x="14" y="11" width="2.4" height="9"/><rect x="18.6" y="11" width="2.4" height="9"/><rect x="2" y="21" width="22" height="2.4"/></svg></span>PasadoPróximo-2ºESO</div><div class="bc-a s" style="--d:0.3s"><span class="bc-dots" aria-hidden="true"><i></i><i></i><i></i></span><p class="s" style="--d:1.6s">Este resumen está basado en información general sobre la figura de Abderramán III y no en los documentos que me has proporcionado. […]</p><p class="s" style="--d:2.2s"><mark>La información proporcionada ha sido generada por inteligencia artificial y debe verificarse.</mark></p></div></div></div>
<div class="beh-i"><h3>Corrige el repaso</h3>
<div class="bchat"><div class="bc-top"><span class="bc-av" aria-hidden="true"><svg viewBox="0 0 26 26"><path d="M13 2 2 7h22L13 2Z"/><rect x="3" y="8" width="20" height="2"/><rect x="5" y="11" width="2.4" height="9"/><rect x="9.6" y="11" width="2.4" height="9"/><rect x="14" y="11" width="2.4" height="9"/><rect x="18.6" y="11" width="2.4" height="9"/><rect x="2" y="21" width="22" height="2.4"/></svg></span>PasadoPróximo-2ºESO</div><p class="bc-u s" style="--d:0.3s">Taifa significa impuesto sobre la tierra<br>Los mozárabes eran los cristianos que vivían en Al-Ándalus</p><div class="bc-a s" style="--d:1.1s"><span class="bc-dots" aria-hidden="true"><i></i><i></i><i></i></span><p class="s" style="--d:2.4s">Parece que hay un pequeño malentendido en las definiciones. Vamos a corregirlas:</p><ol class="s" style="--d:3.0s"><li><b>Taifa</b>: En realidad, una <i>taifa</i> <mark>no es un impuesto, sino un pequeño reino musulmán</mark> que surgió tras la desintegración del Califato de Córdoba en el año 1031.</li><li><b>Mozárabes</b>: Correcto, los <i>mozárabes</i> eran cristianos que vivían en territorio musulmán. […]</li></ol></div></div></div>
</div>"""),
        ("Cómo lo hice", """
<ol class="hsteps">
<li><b>Necesidades</b><span>Objetivos del grupo con la LOMLOE, el currículo andaluz, el DUA y la protección de datos.</span></li>
<li><b>Materiales</b><span>Nueve unidades, guías de trabajo, banco de preguntas, rúbricas y tablón de anuncios.</span></li>
<li><b>Configuración</b><span>Sin datos personales, con prioridad a los materiales y aviso de origen.</span></li>
<li><b>Pruebas</b><span>Simulaciones y ajustes, recogidos en el anexo del TFM.</span></li>
<li><b>Plan de aula</b><span>Cuestionario inicial, sesión de uso ético, familias, cinco actividades y rúbricas.</span></li>
</ol>"""),
        ("Lo que puedo afirmar", """
<div class="status">
<div class="s-ok"><span class="st-l ok">Comprobado</span><p>Guía sin resolver, prioriza los materiales de clase y avisa del origen de cada dato, como muestran las capturas de las pruebas.</p></div>
<div class="s-exp"><span class="st-l exp">Esperado</span><p>Más comprensión, autonomía y pensamiento crítico. El TFM propone cómo medirlo, aunque aún no hay datos.</p></div>
<div class="s-pend"><span class="st-l pend">Pendiente</span><p>Pilotarlo con un grupo real y vigilar la dependencia del alumnado, la sobrecarga de información y la formación docente.</p></div>
</div>"""),
    ],
    related=["consejo-de-clio", "la-ia-tambien-miente", "audita-tu-programacion"],
))

P.append(dict(
    slug="mapa-de-relieves", cat="herramientas", year="2026",
    title="Mapa de relieves de la Península Ibérica", tags=["Aplicación web", "2.º Bachillerato"], kind="ficha",
    card="Un mapa interactivo que localiza cada relieve, era geológica o agente erosivo y lo explica.",
    viz="map",
    lede="Mapa interactivo para estudiar el relieve de la Península.",
    meta=[("Nivel", "2.º Bachillerato · Geografía de España"),
          ("Para quién", "Alumnado que estudia el relieve peninsular"),
          ("Tipo", "Aplicación web interactiva"),
          ("Herramientas", "Claude (artefacto web)")],
    links=[],  # se usa en «La herramienta»
    sections=[
        ("La necesidad", """
<p class="psub">El tema del relieve suele ser complicado. Muchas veces, mientras estás estudiando una cosa, necesitas mirar lo que ya has repasado para entenderlo mejor porque es fácil de olvidar.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Un mapa interactivo del relieve de la Península Ibérica.</span></li>
<li><b>Cómo lo hice</b><span>Con Claude, organizando el tema en cuatro bloques y revisando el contenido.</span></li>
<li><b>Para qué lo hice</b><span>Para volver a lo ya repasado en cualquier momento y entender mejor el tema.</span></li>
</ul>"""),
        dict(title="La herramienta", cols=1, intro="""<p>Se pulsa un relieve o un tema: el mapa lo localiza y una ficha lo explica. El tema va en cuatro bloques:</p>
<ul class='pl'>
<li><b>Evolución geológica:</b> la cronología y lo que se formó en cada era.</li>
<li><b>Estructuras:</b> relieves aclinales, monoclinales, plegados, fallados y sajónicos.</li>
<li><b>Roquedo:</b> silíceo, kárstico, arcilloso y volcánico.</li>
<li><b>Erosión:</b> laminar, fluvial, glaciar, eólica y marina.</li>
</ul>
<p>Cada ficha tiene qué es, sus partes y formas, imágenes, dónde está en España y preguntas de repaso.</p>
<p>Los colores del texto indican de qué documento de clase sale cada dato: los apuntes, el PDF o la presentación (PPS). Lo que va en azul se ha añadido.</p>""", figs=[], go_texto=True, zoom=True, embed=("iframe", "/apps/mapa-de-relieves/", "Mapa de relieves de la Península Ibérica", "Abrir el mapa", "/apps/mapa-de-relieves/")),
    ],
    value=["Convertir un tema memorístico en una herramienta de consulta visual.",
           "Diseñar y construir una aplicación sencilla con IA, revisando el contenido."],
    related=["el-bombo", "excursion-roma-3d", "consejo-de-clio"],
))

# ---------------------------------------------------------------- AULA
P.append(dict(
    slug="cazadores-de-bulos", cat="aula", year="2026",
    title="Cazadores de bulos históricos", tags=["Actividad", "4.º ESO y 2.º Bach."], kind="ficha",
    card="Un texto escrito por una IA sobre la caída de Málaga en 1937, convincente y con nueve errores.",
    viz="v-bulos",
    lede="Actividad para repasar y desarrollar pensamiento crítico.",
    meta=[("Nivel", "4.º ESO y 2.º Bachillerato"),
          ("Cuándo", "Repaso de la Guerra Civil"),
          ("Duración", "Una sesión de 55 minutos, ampliable a dos"),
          ("Agrupamiento", "Parejas o grupos de 3")],
    links=[],  # el PDF se descarga desde «El material»
    sections=[
        ("La necesidad", """
<p class="psub">Al acabar la unidad de la Guerra Civil hace falta repasar. Además, el alumnado tiene que aprender a no fiarse de un texto solo porque está bien escrito, sobre todo si lo ha escrito una IA.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Generar un texto de repaso con errores sobre la caída de Málaga.</span></li>
<li><b>Cómo lo hice</b><span>Pedirle a la IA que ocho errores salieran del temario y uno tuviera que ser razonado.</span></li>
<li><b>Para qué lo hice</b><span>Para repasar y aprender a desconfiar de un texto que parece correcto.</span></li>
</ul>"""),
        ("Así empieza el texto", """
<p>Un fragmento real del documento que recibe el alumnado. Te enseño dos de los nueve errores, los demás están en el PDF, con el solucionario para el docente.</p>
<blockquote class="excerpt">
<p><mark class="err" id="e1">Málaga fue una de las ciudades que quedaron en manos del bando sublevado desde el mismo comienzo de la guerra</mark><sup aria-hidden="true">1</sup>, en julio de 1936. Aun así, durante el invierno de 1937 se convirtió en uno de los frentes más activos del sur peninsular […]</p>
<p>La defensa de la ciudad estuvo dirigida por <mark class="err" id="e2">el general José Miaja</mark><sup aria-hidden="true">2</sup>, el mismo que unos meses antes había organizado la resistencia de Madrid. […]</p>
</blockquote>
<dl class="errs">
<div><dt><span>1</span> Málaga, sublevada desde julio de 1936</dt><dd>Falso. Málaga fue republicana hasta febrero de 1937. <b>Se comprueba</b> con el mapa de España en julio de 1936.</dd></div>
<div><dt><span>2</span> El general Miaja dirigía la defensa</dt><dd>Falso. Miaja dirigió la defensa de Madrid, en Málaga el responsable era el coronel José Villalba. <b>Se comprueba</b> con el epígrafe de la batalla de Madrid.</dd></div>
</dl>"""),
        ("Cómo se hace", """
<ol class="steps">
<li><b>Se reparte sin avisar (5 min).</b> Lo normal es que nadie sospeche.</li>
<li><b>Se destapa la trampa (5 min):</b> lo ha escrito una IA y tiene nueve errores.</li>
<li><b>A cazar en grupos (25 min),</b> primero de memoria y luego con el libro y el atlas. Un error solo cuenta si dicen dónde lo han comprobado.</li>
<li><b>Puesta en común (20 min):</b> ¿cuál te habrías creído si nadie te avisa?</li>
</ol>"""),
        dict(title="El material", cols=1, intro="<p>El PDF tiene cuatro páginas, listas para imprimir:</p><ul class='pl'><li><b>Guía docente (pág. 1):</b> la ficha de la actividad, por qué funciona como repaso, los cuatro pasos de la sesión y cómo subir o bajar el nivel.</li><li><b>Documento A (pág. 2):</b> el texto falso con los nueve errores, avisado como material didáctico, con los cuatro puntos del tema que conviene repasar y una pista para el error número nueve.</li><li><b>Hoja de registro (pág. 3):</b> para anotar lo que dice el texto, lo que pasó en realidad y dónde se ha comprobado, con una pregunta final individual.</li><li><b>Solucionario y rúbrica (pág. 4, solo para el docente):</b> la corrección de cada error con el contenido del tema que lo delata, lo que sí es verdad en el texto y una rúbrica de tres criterios.</li></ul>", figs=[], pdf=("/assets/pdf/cazadores-de-bulos.pdf", "/assets/proyectos/cazadores-de-bulos/pdf-")),
    ],
    related=["la-ia-tambien-miente", "constitucion-1812", "la-nube-pesa"],
))

P.append(dict(
    slug="la-ia-tambien-miente", cat="aula", year="2026",
    title="La IA también miente", tags=["Serie de imágenes", "Cualquier nivel"], kind="ficha",
    card="Escenas históricas generadas con IA con anacronismos escondidos y una trampa en cada una.",
    viz="img:/assets/ia-miente/mercado.jpg",
    lede="Serie de imágenes para mirar con ojo crítico lo que genera una IA.",
    meta=[("Para quién", "Docentes que quieran llevarla a clase y cualquiera con curiosidad"),
          ("Tipo", "Serie quincenal de imágenes en LinkedIn"),
          ("Herramientas", "Claude y Canva")],
    links=[],  # la imagen se ve en «La actividad»
    sections=[
        ("La necesidad", """
<p class="psub">Las imágenes generadas con IA tienen un aspecto muy convincente, pero mezclan épocas sin ningún problema.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Una serie de escenas históricas generadas con IA que esconden anacronismos.</span></li>
<li><b>Cómo lo hice</b><span>Esconder en cada escena una trampa: algo que parece imposible y sí es de la época.</span></li>
<li><b>Para qué lo hice</b><span>Para entrenar la mirada y aprender a desconfiar de una imagen que parece real.</span></li>
</ul>"""),
        dict(title="La actividad", cols=1, intro="""<p><b>Entrega 1 · Mercado medieval.</b> Hay cinco errores y una trampa.</p>
<ul class='pl'>
<li><b>Busca los anacronismos:</b> objetos que no podían estar en un mercado medieval.</li>
<li><b>Cuidado con la trampa:</b> hay algo que parece moderno y sí es de la época. Así no se marca como error todo lo que «parece moderno».</li>
<li><b>Pregúntate de dónde viene cada objeto:</b> buscar los errores obliga a mirar con atención.</li>
</ul>""",
             figs=[], embed=("flip", "/assets/ia-miente/mercado.jpg", "Entrega 1 de la serie: un mercado medieval generado con IA con cinco anacronismos y una trampa", "/assets/ia-miente/mercado-solucion-foto.jpg", "<h3>Las cinco que no pueden estar y la que sí</h3><ol><li><b>Cartel impreso:</b> todas las letras iguales. La imprenta es de 1450.</li><li><b>Maíz:</b> de América. Después de 1492.</li><li><b>Tomates:</b> de América. Después de 1492.</li><li><b>Patatas:</b> de los Andes. Llegan a España hacia 1570.</li><li><b>Girasoles:</b> de América. Llegan a Europa en el siglo XVI.</li><li class='ok'><b>Las gafas</b> están bien. Hay gafas de lectura en Italia desde finales del siglo XIII.</li></ol>")),
    ],
    value=["Llevar la alfabetización visual y sobre IA a algo que se resuelve en cinco minutos."],
    related=["cazadores-de-bulos", "consejo-de-clio", "asistente-gpt-2eso"],
))

P.append(dict(
    slug="la-nube-pesa", cat="aula", year="2026",
    title="La nube pesa", tags=["Actividad (PDF)", "2.º ESO"], kind="ficha",
    card="Cada equipo reconstruye un eslabón de lo que hay detrás de un gesto digital y propone una medida.",
    viz="v-nube",
    lede="Actividad para descubrir lo que consume un gesto digital y argumentar una medida.",
    meta=[("Nivel", "2.º ESO, adaptable a 3.º ESO"),
          ("Cuándo", "Cierre del tema de recursos naturales y desigualdad"),
          ("Duración", "Una sesión de 55 minutos"),
          ("Agrupamiento", "Cinco equipos de 4 o 5")],
    links=[],  # el PDF se descarga desde «El material»
    sections=[
        ("La necesidad", """
<p class="psub">Mandar una foto o hacer una pregunta a un asistente parece un gesto sin peso. Detrás hay una cadena que va del mineral al residuo.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Una actividad en la que cinco equipos reconstruyen la cadena de un gesto digital.</span></li>
<li><b>Cómo lo hice</b><span>Con fichas de datos verificados y una regla: toda medida tiene que decir quién la paga.</span></li>
<li><b>Para qué lo hice</b><span>Para unir la Geografía con algo que el alumnado hace cada día y argumentar con datos.</span></li>
</ul>"""),
        ("La regla que sostiene la actividad", """
<p>Al final, cada equipo propone una medida y siempre con el mismo formato: <b>«Proponemos ___. Esto lo paga ___».</b> Si falta la segunda mitad, la medida no se admite.</p>
<p>Se repasan recursos, tensiones internacionales y desigualdad, pero lo que se evalúa de verdad es si el alumnado distingue entre opinar sobre un problema y hacer una propuesta sabiendo a quién le cuesta.</p>"""),
        ("Cómo se hace", """
<ol class="steps">
<li><b>El gesto (5 min).</b> Todos mandan una foto a la vez. En la pizarra: ¿cuánto acaba de pesar eso?</li>
<li><b>Montaje (20 min).</b> Cada equipo trabaja un eslabón (extracción, fabricación, uso, centro de datos, residuo) y prepara un dato con su fuente, un lugar en el mapa y quién gana y quién pierde.</li>
<li><b>La cadena entera (10 min).</b> Se proyecta seguida. Una sola pregunta: ¿el que pierde es el mismo en los cinco eslabones?</li>
<li><b>La medida (10 min).</b> Cada equipo escribe su frase. Las que no tienen segunda mitad se devuelven.</li>
</ol>
<p>Funciona también sin dispositivos, con una cartulina por equipo. Los datos están verificados a septiembre de 2026 y la guía recuerda comprobarlos antes de usarla.</p>"""),
        dict(title="El material", cols=1, intro="<p>El PDF tiene cuatro páginas, listas para imprimir:</p><ul class='pl'><li><b>Guía docente (pág. 1):</b> la ficha didáctica, la regla de la medida, la sesión cronometrada minuto a minuto y variantes para bajar o subir el nivel o para trabajar sin dispositivos.</li><li><b>Fichas de eslabón (pág. 2):</b> cinco fichas para recortar (extracción, fabricación y transporte, uso y vida útil, centro de datos y residuo), cada una con sus datos y un dato que busca el propio equipo.</li><li><b>Hoja de la cadena (pág. 3):</b> una por equipo, con el dato y su fuente, el lugar en el mapa, quién gana, quién pierde y el espacio para la medida.</li><li><b>Solucionario (pág. 4):</b> lo que suele pasar en clase y qué contenido del tema delata, una rúbrica de tres criterios y las fuentes de todos los datos.</li></ul>", figs=[], pdf=("/assets/pdf/la-nube-pesa.pdf", "/assets/proyectos/la-nube-pesa/pdf-")),
    ],
    value=["Unir un tema de Geografía con algo que el alumnado hace cada día.",
           "Evaluar la argumentación con una regla sencilla y clara."],
    related=["cazadores-de-bulos", "constitucion-1812", "excursion-roma-3d"],
))

P.append(dict(
    slug="constitucion-1812", cat="aula", year="2026",
    title="¿Fue liberal la Constitución de 1812?", tags=["Actividad (PDF)", "4.º ESO"], kind="ficha",
    card="Comentario de texto colaborativo: las parejas anotan los artículos y debaten con el texto delante.",
    viz="v-1812",
    lede="Comentario de texto colaborativo para debatir con fuentes primarias.",
    meta=[("Nivel", "4.º ESO, adaptable a 2.º Bachillerato"),
          ("Cuándo", "Tras las Cortes de Cádiz"),
          ("Duración", "Una sesión de 55 minutos"),
          ("Herramientas", "Hypothes.is (o Google Docs con comentarios)")],
    links=[],  # el PDF se descarga desde «El material»
    sections=[
        ("La necesidad", """
<p class="psub">Ante un texto histórico es fácil opinar sin apoyarse en lo que dice. La Constitución de 1812 admite dos lecturas: ruptura revolucionaria o liberalización con límites.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Un comentario de texto colaborativo sobre la Constitución de 1812 con Hypothes.is.</span></li>
<li><b>Cómo lo hice</b><span>Marcando cada fragmento como #APOYA, #LIMITA o #PREGUNTA antes de debatir.</span></li>
<li><b>Para qué lo hice</b><span>Para trabajar fuentes primarias y debatir solo con lo que dice el texto.</span></li>
</ul>"""),
        ("Cómo se hace", """
<ol class="steps">
<li><b>La pregunta (5 min).</b> Dos equipos con postura asignada: ruptura revolucionaria o liberalización con límites.</li>
<li><b>Anotación por parejas (20 min).</b> Al menos tres anotaciones y una respondiendo a otra pareja. El docente ve el margen en directo.</li>
<li><b>Debate (15 min).</b> Cada intervención empieza citando el artículo anotado.</li>
<li><b>Cierre (10 min).</b> Votación razonada y una pregunta: ¿por qué un mismo texto puede sostener las dos posturas?</li>
</ol>
<p>Incluye un plan B sin cuentas, con Google Docs y variantes para subir o bajar el nivel.</p>"""),
        dict(title="El material", cols=1, intro="<p>El PDF tiene cuatro páginas, listas para imprimir:</p><ul class='pl'><li><b>Guía docente (pág. 1):</b> la ficha didáctica, cómo preparar Hypothes.is en diez minutos (con un plan B sin cuentas), la sesión cronometrada y variantes para subir o bajar el nivel.</li><li><b>Dosier de trabajo (pág. 2):</b> los artículos de la Constitución de 1812, el protocolo de marcas #APOYA, #LIMITA y #PREGUNTA y los dos roles de la pareja: anotador y verificador.</li><li><b>Hoja de registro (pág. 3):</b> las anotaciones de la pareja, la respuesta a otra pareja, una votación razonada antes y después del debate y una pregunta final individual.</li><li><b>Solucionario y rúbrica (pág. 4, solo para el docente):</b> la etiqueta esperada en cada artículo, qué debería aparecer en la anotación, qué contenido delata el fallo y una rúbrica de tres criterios.</li></ul>", figs=[], pdf=("/assets/pdf/constitucion-1812-hypothesis.pdf", "/assets/proyectos/constitucion-1812/pdf-")),
    ],
    value=["Trabajar fuentes primarias con una herramienta digital que hace visible el razonamiento.",
           "Diseñar un debate en el que se argumenta con evidencias, no con opiniones."],
    related=["cazadores-de-bulos", "escape-room-siglo-xix", "la-nube-pesa"],
))

P.append(dict(
    slug="escape-room-siglo-xix", cat="aula", year="2024",
    title="Escape room del siglo XIX", tags=["Escape room", "4.º ESO"], kind="ficha",
    card="Repaso del siglo XIX español ambientado en El Ministerio del Tiempo, con una caja fuerte al final.",
    viz="v-esc",
    lede="Escape room digital para repasar el siglo XIX español.",
    meta=[("Nivel", "4.º ESO"),
          ("Tipo", "Escape room digital de repaso"),
          ("Herramientas", "Genially")],
    links=[],  # se juega en «La actividad»
    sections=[
        ("La necesidad", """
<p class="psub">El siglo XIX español es un tema largo y con muchas fechas. Repasarlo de memoria se hace pesado.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Un escape room digital ambientado en <i>El Ministerio del Tiempo</i>.</span></li>
<li><b>Cómo lo hice</b><span>Con Genially, con pruebas que recorren el siglo y una caja fuerte al final.</span></li>
<li><b>Para qué lo hice</b><span>Para convertir el repaso en una misión con un orden y una meta.</span></li>
</ul>"""),
        dict(title="La actividad", cols=1, intro="""<p>El alumnado actúa como agentes del Ministerio que deben impedir que se altere el 2 de mayo de 1808. Las pruebas recorren el siglo:</p>
<ul class='pl'>
<li><b>Las Pinturas Negras de Goya.</b></li>
<li><b>La Guerra de la Independencia,</b> con textos para completar.</li>
<li><b>El Trienio Liberal.</b></li>
<li><b>El Bienio Progresista.</b></li>
<li><b>La Gloriosa.</b></li>
<li><b>Una caja fuerte final,</b> con un código que solo se abre con lo aprendido.</li>
</ul>""", figs=[], go_texto=True, embed=("iframe", "https://view.genially.com/65f972b6e99bde00148864ea", "Escape room del siglo XIX en Genially", "Jugar a pantalla completa", "https://view.genially.com/65f972b6e99bde00148864ea")),
    ],
    value=["Diseñar un repaso gamificado con una narrativa que el alumnado reconoce."],
    related=["excursion-roma-3d", "la-ia-tambien-miente", "constitucion-1812"],
))

P.append(dict(
    slug="excursion-roma-3d", cat="aula", year="2024",
    title="Excursión a Roma en 3D", tags=["Mundo 3D", "1.º ESO"], kind="ficha",
    card="Un mundo 3D con edificios de la Antigua Roma para recorrer su arquitectura.",
    viz="v-cos",
    lede="Mundo 3D para recorrer la Antigua Roma en clase.",
    meta=[("Nivel", "1.º ESO"),
          ("Tipo", "Mundo 3D para una visita guiada"),
          ("Herramientas", "CoSpaces Edu (hoy Delightex)")],
    links=[],  # se visita en «La actividad»
    sections=[
        ("La necesidad", """
<p class="psub">Para introducir la Antigua Roma en 1.º ESO, el alumnado necesita situarse en el espacio antes de entrar en los conceptos.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Un mundo virtual con edificios representativos de la Antigua Roma.</span></li>
<li><b>Cómo lo hice</b><span>Con CoSpaces Edu (hoy Delightex), con un guiño escondido en la domus.</span></li>
<li><b>Para qué lo hice</b><span>Para motivar con la inmersión y comparar la arquitectura romana con la griega.</span></li>
</ul>"""),
        dict(title="La actividad", cols=1, intro="""<p>Un recorrido por algunos de los edificios más representativos de la Antigua Roma, cada uno con su explicación:</p>
<ul class='chips-ed'><li>Templo</li><li>El Coliseo</li><li>Panteón de Agripa</li><li>Ara Pacis</li><li>Obras de ingeniería</li><li>Domus romana</li></ul>
<p>Es una actividad de introducción en dos momentos:</p>
<ul class='pl'>
<li><b>Visita guiada:</b> el alumnado recorre el mundo y se sitúa en el espacio antes de entrar en los conceptos.</li>
<li><b>Comparación:</b> después se comparan la arquitectura romana y la griega.</li>
<li><b>Un guiño:</b> en una de las habitaciones de la domus me encontraréis descansando, para que la visita tenga algo de juego.</li>
</ul>""", figs=[], go_texto=True, embed=("iframe", "https://edu.delightex.com/EXA-NNH", "Excursión a Roma en Delightex", "Visitar a pantalla completa", "https://edu.delightex.com/EXA-NNH")),
    ],
    value=["Usar la realidad virtual al servicio de un objetivo concreto: comparar dos arquitecturas."],
    related=["escape-room-siglo-xix", "mapa-de-relieves", "la-ia-tambien-miente"],
))

# ---------------------------------------------------------------- PROFESORADO
P.append(dict(
    slug="repositorio-digital", cat="profesorado", year="2024 · 2026",
    title="Repositorio digital docente", tags=["Web de recursos", "Profesorado"], kind="caso",
    lab="Web de recursos",
    card="La web de herramientas que creé para un centro en 2024 y que en 2026 se ha convertido en Didákora.",
    viz="didakora",
    h1="Del repositorio de centro a Didákora",
    lede="Una web con herramientas digitales para docentes.",
    meta=[("Para quién", "Colegio Cerrado de Calderón (2024) · Docentes (2026)"),
          ("Tipo", "Web de recursos y autoformación"),
          ("Herramientas", "Google Sites (2024) · Web propia (2026)"),
          ("Reconocimiento", "Presentada por el centro en Braining 2025")],
    links=[("Abrir Didákora", "https://pasadoproximo.github.io/didakora/", "ext"),
           ("Ver el repositorio original", "https://sites.google.com/view/repositorio-digital-docente-cc/inicio", "ext")],
    sections=[
        ("La necesidad", """
<p class="psub">La Dirección del Colegio Cerrado de Calderón quería fomentar la digitalización de su centro y ayudar a la autoformación del profesorado (Infantil, Primaria y Secundaria).</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Elaboración de un repositorio digital docente totalmente adaptado en Google Sites.</span></li>
<li><b>Cómo lo hice</b><span>Entrevistas con la Dirección y los docentes para realizar una curación de herramientas digitales.</span></li>
<li><b>Para qué lo hice</b><span>Para fomentar la autoformación del profesorado y estandarizar criterios de selección.</span></li>
</ul>"""),
        dict(title="Así era cada ficha",
             intro='<p class="psub">Dos ejemplos de etapas distintas: una herramienta de Infantil y otra de Secundaria.</p>',
             cols=1, figs=[],
             after="""<div class="ficha1 two">
FIG:/assets/proyectos/repositorio-digital/ficha-infantil-2024.jpg?v=2|Ficha de Cokitos en Infantil (5 años): videotutorial de YouTube, qué es la plataforma, las áreas que trabaja (Matemáticas, Lengua, Ciencias, Arte y música) y botón a la web|<b>Infantil · 5 años · Matemáticas</b>
FIG:/assets/proyectos/repositorio-digital/ficha-2024.jpg?v=2|Ficha de StopMotion en el repositorio de 2024: videotutorial de YouTube, explicación de la técnica, tres usos en el aula, «Todas las edades» y botón a la app|<b>Secundaria y Bachillerato · Sociales</b>
</div>"""),
        ("Lo que puedo afirmar", """
<div class="status four">
<div class="s-ok"><span class="st-l ok">En uso</span><p>El centro la usó con su claustro como herramienta de autoformación del profesorado.</p></div>
<div class="s-exp"><span class="st-l exp">Congreso</span><p>El centro la presentó en Braining, congreso de creatividad educativa (Valencia, 2025). <a href="https://colegiocerradodecalderon.es/braining/" rel="noopener" target="_blank">Ver la noticia</a>.</p></div>
<div class="s-exp"><span class="st-l exp">Todo el centro</span><p>Se unificó el criterio para elegir las herramientas digitales que se usan en el centro.</p></div>
<div class="s-pend"><span class="st-l pend">Más de 100</span><p>Más de 100 herramientas y recursos para el centro, cada uno con su ficha y su videotutorial.</p></div>
</div>"""),
        dict(title="Mantenerlo al día",
             intro='<p class="psub">La tecnología educativa evoluciona muy rápido: dos años después, muchas herramientas habían cerrado o cambiado. Por eso en 2026 la he rehecho como Didákora.</p>',
             cols=1, figs=[],
             after="""<div class="upd">
<div class="upd-h" aria-hidden="true"><span>Antes</span><span></span><span>Ahora</span></div>
<div class="upd-r"><div class="upd-a"><b>Herramientas cerradas</b><span class="upd-logos"><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/flip.png" alt="" width="24" height="24" loading="lazy"><s>Flip</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/tome.png" alt="" width="24" height="24" loading="lazy"><s>Tome</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/classcraft.png" alt="" width="24" height="24" loading="lazy"><s>Classcraft</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/earteach.svg" alt="" width="24" height="24" loading="lazy"><s>EarTeach</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/hablaconlahistoria.svg" alt="" width="24" height="24" loading="lazy"><s>Hablaconlahistoria</s></span></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Cada una tiene su alternativa</b><span class="upd-logos"><span class="upd-lg"><img src="/herramientas/logos/padlet.png" alt="" width="24" height="24" loading="lazy"><span>Padlet</span></span><span class="upd-lg"><img src="/herramientas/logos/gamma.png" alt="" width="24" height="24" loading="lazy"><span>Gamma</span></span><span class="upd-lg"><img src="/herramientas/logos/classdojo.png" alt="" width="24" height="24" loading="lazy"><span>ClassDojo</span></span><span class="upd-lg"><img src="/herramientas/logos/musictheory.png" alt="" width="24" height="24" loading="lazy"><span>musictheory.net</span></span><span class="upd-lg"><img src="/herramientas/logos/gemini.png" alt="" width="24" height="24" loading="lazy"><span>Gemini</span></span></span></div></div>
<div class="upd-r"><div class="upd-a"><b>Nombres que cambiaron</b><span class="upd-logos"><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/quizizz.png" alt="" width="24" height="24" loading="lazy"><s>Quizizz</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/freepik.png" alt="" width="24" height="24" loading="lazy"><s>Freepik</s></span></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Con su nombre actual</b><span class="upd-logos"><span class="upd-lg"><img src="/herramientas/logos/wayground.png" alt="" width="24" height="24" loading="lazy"><span>Wayground</span></span><span class="upd-lg"><img src="/herramientas/logos/magnific.png" alt="" width="24" height="24" loading="lazy"><span>Magnific</span></span></span></div></div>
<div class="upd-r"><div class="upd-a"><b>Faltaba la IA de los centros</b><span class="upd-gone"><em>Ninguna IA con cuenta del centro</em></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Para usarla con la cuenta del centro</b><span class="upd-logos"><span class="upd-lg"><img src="/herramientas/logos/gemini.png" alt="" width="24" height="24" loading="lazy"><span>Gemini</span></span><span class="upd-lg"><img src="/herramientas/logos/notebooklm.png" alt="" width="24" height="24" loading="lazy"><span>NotebookLM</span></span><span class="upd-lg"><img src="/herramientas/logos/copilot.png" alt="" width="24" height="24" loading="lazy"><span>Copilot</span></span></span></div></div>
<div class="upd-r"><div class="upd-a"><b>Difícil de encontrar</b><span class="upd-path"><span>Etapa</span><i>›</i><span>Materia</span><i>›</i><span>Herramienta</span></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Se busca por nombre o por lo que necesitas</b></div></div>
</div>
<div class="caja-demo">
<h3>Así es Didákora</h3>
<div class="dk-t"><p>Se busca por el nombre de la herramienta o por lo que quieres hacer y se filtra por etapa. También se puede entrar por diez categorías según para qué sirve cada herramienta.</p><p class="cdf-t">Cada ficha te da</p><ul class="cdf"><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 11v5M12 8h.01"/></svg></span>Qué es la herramienta</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 7h10M7 11h10M7 15h6"/><path d="M5 3h14v18l-3.5-2.5L12 21l-3.5-2.5L5 21z"/></svg></span>Para qué la puedes usar</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M2 9 12 4l10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg></span>La etapa</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M14 9l2 2"/></svg></span>Dispositivos y cuenta que necesita</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 7h11M4 12h16M4 17h9"/></svg></span>Herramientas alternativas</li></ul>
</div>
<div class="dk-video">
<video src="/assets/proyectos/repositorio-digital/didakora.webm?v=4" poster="/assets/proyectos/repositorio-digital/didakora-video.jpg?v=4" width="1264" height="712" muted loop playsinline preload="metadata" aria-label="Vídeo de Didákora: se busca «repasar», se filtra por Primaria y se abre la ficha de Kahoot!, con qué es, para qué usarla, qué necesita y sus alternativas"></video>
<button type="button" class="dk-play" aria-label="Pausar el vídeo"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-pause" d="M9 6v12M15 6v12"/><path class="i-play" d="M8 5.5v13l11-6.5z"/></svg></button>
<script>(()=>{const w=document.currentScript.parentElement,v=w.querySelector("video"),b=w.querySelector(".dk-play");
const set=on=>{w.classList.toggle("paused",!on);b.setAttribute("aria-label",on?"Pausar el vídeo":"Reproducir el vídeo");};
b.addEventListener("click",()=>{if(v.paused){v.play();set(true);}else{v.pause();set(false);}});
// arranca al verse en pantalla, salvo si el sistema pide reducir el movimiento
if(matchMedia("(prefers-reduced-motion: reduce)").matches){set(false);return;}
new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&!w.classList.contains("paused"))v.play().catch(()=>set(false));else if(!e.isIntersecting)v.pause();}),{threshold:.3}).observe(v);})();</script>
</div>
</div>
<div class="dk-mas">
<h3>Cómo se mantiene al día</h3>
<p>Cinco agentes de IA revisan Didákora y yo decido qué cambia desde un monasterio en pixel art.</p>
<a class="btn" href="/proyectos/monasterio-didakora/">Ver Monasterio <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
</div>"""),
    ],
    related=["monasterio-didakora", "audita-tu-programacion", "rubrica-materiales-digitales"],
))

P.append(dict(
    slug="audita-tu-programacion", cat="profesorado", year="2026",
    title="Audita tu programación", tags=["Guía (PDF)", "Profesorado"], kind="ficha",
    card="Un método con NotebookLM para encontrar criterios de evaluación que no se evalúan en ninguna actividad.",
    viz="v-aud",
    lede="Guía para encontrar con NotebookLM los criterios que no se evalúan.",
    meta=[("Para quién", "Docentes y opositores que revisan su programación"),
          ("Tipo", "Guía paso a paso con ocho prompts"),
          ("Herramientas", "NotebookLM (plan gratuito)"),
          ("Tiempo", "Unos 40 minutos la primera vez")],
    links=[],  # el PDF se descarga desde «El material»
    sections=[
        ("La necesidad", """
<p class="psub">En una programación de decenas de páginas es fácil que un criterio de evaluación aparezca en la tabla y luego no se evalúe en ninguna actividad. Encontrarlo a mano obliga a releerla entera.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Una guía paso a paso con ocho prompts para NotebookLM.</span></li>
<li><b>Cómo lo hice</b><span>Aprovechando que NotebookLM cita el fragmento exacto del documento.</span></li>
<li><b>Para qué lo hice</b><span>Para localizar esos huecos con cita y página, sin releer la programación entera.</span></li>
</ul>"""),
        ("Cómo está pensada", """
<p>NotebookLM responde citando el fragmento exacto del documento que se le sube y eso permite comprobar cada respuesta. No es un corrector: es un buscador que señala dónde mirar. La decisión sobre si un criterio está evaluado sigue siendo del docente, con el documento delante.</p>
<ul class="pl">
<li><b>Antes de nada, privacidad:</b> quitar la portada con el nombre y el DNI antes de subir el documento.</li>
<li><b>Ocho prompts en orden:</b> del inventario de criterios a la cobertura, cada uno apoyado en el anterior.</li>
<li><b>Una hoja de registro</b> para anotar el veredicto, porque la herramienta no lo guarda.</li>
</ul>"""),
        dict(title="El material", cols=1, intro="<p>La guía tiene cuatro páginas, lista para imprimir:</p><ul class='pl'><li><b>Para qué sirve y montaje (pág. 1):</b> qué busca la guía, cómo quitar los datos personales antes de subir nada, qué necesitas y cómo montar el cuaderno en cinco pasos.</li><li><b>Los ocho prompts (pág. 2):</b> para copiar tal cual y en orden, cada uno con una nota de para qué sirve.</li><li><b>Hoja de auditoría (pág. 3):</b> para anotar lo que dice la herramienta, el fragmento que cita y tu propia comprobación, con los cuatro veredictos posibles.</li><li><b>Qué no hace bien (pág. 4):</b> los límites de NotebookLM, cuándo no conviene usarla y las fuentes consultadas.</li></ul>", figs=[], pdf=("/assets/pdf/audita-tu-programacion.pdf", "/assets/proyectos/audita-tu-programacion/pdf-")),
    ],
    value=["Usar la IA para una tarea docente real y comprobable.",
           "Escribir instrucciones que otro docente puede seguir sin ayuda."],
    related=["repositorio-digital", "el-bombo", "asistente-gpt-2eso"],
))

P.append(dict(
    slug="el-bombo", cat="profesorado", year="2026",
    title="El bombo", tags=["Aplicación web", "Opositores"], kind="ficha",
    card="Calcula la probabilidad de que salga alguno de tus temas en el sorteo de las oposiciones.",
    viz="v-bombo",
    lede="Calculadora para saber qué probabilidad tienes de que salga uno de tus temas.",
    meta=[("Para quién", "Opositores de cualquier especialidad"),
          ("Tipo", "Aplicación web"),
          ("Herramientas", "Claude (artefacto web)"),
          ("Privacidad", "Los datos no salen del navegador")],
    links=[],  # se usa en «La herramienta»
    sections=[
        ("La necesidad", """
<p class="psub">Decidir cuántos temas preparar es una de las dudas más habituales al opositar.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Una calculadora para opositores de cualquier especialidad.</span></li>
<li><b>Cómo lo hice</b><span>Con Claude, como aplicación web que no pide datos.</span></li>
<li><b>Para qué lo hice</b><span>Para planificar el estudio con datos en lugar de intuiciones.</span></li>
</ul>"""),
        dict(title="La herramienta", cols=1, intro="""<p>Una calculadora para opositores de cualquier especialidad:</p>
<ul class='pl'>
<li><b>El bombo:</b> cada bola es un tema. Se pulsa para sumarle una vuelta de repaso.</li>
<li><b>La cobertura:</b> la probabilidad de que salga al menos uno de tus temas preparados. También la de que salgan dos o más.</li>
<li><b>La curva:</b> cuánto sube la probabilidad con cada tema que preparas.</li>
<li><b>Tu convocatoria:</b> se cambian los temas del temario, las bolas que salen y tus títulos. Todo se guarda en tu navegador.</li>
</ul>""", figs=[], go_texto=True, embed=("iframe", "/apps/el-bombo/", "El bombo, calculadora para opositores", "Abrir El bombo", "/apps/el-bombo/")),
    ],
    value=["Resolver una necesidad concreta con una herramienta sencilla y sin pedir datos."],
    related=["audita-tu-programacion", "rubrica-materiales-digitales", "repositorio-digital"],
))

P.append(dict(
    slug="rubrica-materiales-digitales", cat="profesorado", year="2024",
    title="Rúbrica de materiales digitales", tags=["Formulario", "Profesorado"], kind="ficha",
    card="Una rúbrica en formulario para valorar un recurso digital antes de llevarlo al aula.",
    viz="v-rub",
    lede="Formulario para valorar un material digital antes de llevarlo al aula.",
    meta=[("Para quién", "Docentes que eligen recursos digitales"),
          ("Tipo", "Rúbrica en formulario"),
          ("Herramientas", "Jotform")],
    links=[],  # se rellena en «La rúbrica»
    sections=[
        ("La necesidad", """
<p class="psub">Antes de llevar un recurso digital al aula hay que valorarlo. Sin criterios comunes, cada docente lo hace a su manera.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Un formulario de 17 preguntas para valorar un material educativo digital.</span></li>
<li><b>Cómo lo hice</b><span>Con Jotform, a partir de la norma UNE 71362:2020.</span></li>
<li><b>Para qué lo hice</b><span>Para que elegir un recurso sea una decisión con criterios compartidos.</span></li>
</ul>"""),
        dict(title="La rúbrica", cols=1, intro="""<p>Un instrumento de evaluación digital de 17 preguntas para decidir si un material educativo digital está listo para el aula:</p>
<ul class='pl'>
<li><b>Basado en una norma:</b> la UNE 71362:2020 de calidad de los materiales educativos digitales.</li>
<li><b>Se responde en línea,</b> desde el propio formulario, pregunta a pregunta.</li>
<li><b>Criterios compartidos:</b> cualquier docente valora el recurso con las mismas preguntas.</li>
</ul>""", figs=[], go_texto=True, embed=("iframe", "https://form.jotform.com/241185578598070", "Rúbrica de materiales digitales en Jotform", "Abrir el formulario en otra pestaña", "https://form.jotform.com/241185578598070")),
    ],
    value=["Convertir la selección de recursos en una decisión con criterios compartidos."],
    related=["repositorio-digital", "audita-tu-programacion", "e-portfolio-master"],
))

P.append(dict(
    slug="e-portfolio-master", cat="profesorado", year="2024",
    title="e-Portfolio del máster", tags=["Portfolio", "Máster"], kind="ficha",
    card="Los cinco módulos del Máster en Tecnología Educativa reunidos en una web.",
    viz="v-epo",
    lede="El portfolio que hice durante el Máster en Tecnología Educativa y Competencias Digitales (Universidad Europea, 2023-2024). Reúne los trabajos de los cinco módulos y, en cada uno, lo que aprendí.",
    meta=[("Tipo", "Portfolio académico"),
          ("Máster", "Tecnología Educativa y Competencias Digitales"),
          ("Herramientas", "Google Sites")],
    links=[("Ver el e-Portfolio", "https://sites.google.com/view/e-portfolio-jorge/inicio", "ext")],
    sections=[
        ("Qué puedes ver en él", """
<p class="psub">Si buscas a alguien para diseñar formación o materiales digitales, aquí están las pruebas de lo que sé hacer, con un ejemplo real de cada cosa.</p>
<ul class="epo-sk">
<li><b>Diseño de materiales digitales</b><span>Un vídeo con stop motion, un pódcast en grupo, un material interactivo y una situación de aprendizaje STEAM.</span><em>Módulos 1 y 4</em></li>
<li><b>Búsqueda y curación de información</b><span>Ecuaciones de búsqueda, organización de fuentes y curación de contenidos para el aula.</span><em>Módulos 2 y 3</em></li>
<li><b>Trabajo colaborativo</b><span>Una actividad colaborativa diseñada para el aula y la planificación de sus espacios.</span><em>Módulo 3</em></li>
<li><b>Evaluación digital</b><span>Instrumentos de evaluación según la norma UNE 71362:2020, con Jotform, CoRubrics y SELFIE.</span><em>Módulo 5</em></li>
<li><b>Reflexión sobre la práctica</b><span>Cada trabajo termina con qué aprendí y cómo lo llevaría a clase.</span><em>Todos los módulos</em></li>
</ul>"""),
    ],
    value=["Documentar el propio aprendizaje y las evidencias de cada módulo."],
    related=["asistente-gpt-2eso", "repositorio-digital", "rubrica-materiales-digitales"],
))

FEATURED = ["repositorio-digital", "asistente-gpt-2eso", "consejo-de-clio", "cazadores-de-bulos"]

BY = {p["slug"]: p for p in P}

# ---------------------------------------------------------------- FICHAS DE TRABAJO (rediseño, maqueta 3-proyecto)
# Orden: migas + H1 + subtítulo → ficha (4 cajas) → «Lo que hice yo» (proyectos con IA, palabras de Jorge) → bloque visual
# con los botones al lado → «Lo que puedo afirmar» (el error corregido primero, con sus capturas) → la necesidad y cómo
# funciona → «Todas las fichas» y la siguiente. Textos de la maqueta y, donde ella deja corchetes, los que Jorge dio
# en el chat (22-10-2026). Lo que falte, entre corchetes y visible.
PAGINA = {
    "consejo-de-clio": dict(
        migas="Herramientas", lnum="Herramienta · 2026",
        sub="Seis agentes de IA preparan una sesión a partir de una noticia. El docente la contrasta antes de llevarla al aula.",
        ficha=[("Para quién", "Docentes de Historia, 1.º ESO a Bachillerato"), ("Tipo", "Aplicación con IA · libre uso"),
               ("Herramientas", "Claude · 6 agentes"), ("Estado", "Publicada · necesita cuenta de Claude")],
        hice=[("Diseñé", "el equipo. Elegí a los seis personajes por su relación con el papel de cada agente y escribí sus instrucciones, el formato de la sesión y el diseño."),
              ("Amplié", "el equipo de cuatro historiadores a seis. Añadí a Hannah Arendt y a Sócrates para conectar con el presente y abrir el debate."),
              ("Probé", "con noticias de actualidad de temas distintos, varias por curso, para ver cómo filtraba. Antes de llevar una sesión a clase, contrasto el material final."),
              ("Descarté", "que leyera la noticia desde un enlace. Pegar el texto es más fiable.")],
        # sesión real del 22-10-2026 (EFE, Ucrania, 1.º Bachillerato), grabada con la plantilla de vídeo: _build/grabar_consejo_plantilla.js
        video=("/assets/proyectos/consejo-de-clio/sesion-ucrania.webm?v=8", "/assets/proyectos/consejo-de-clio/sesion-ucrania-poster.jpg?v=8",
               "Vídeo de 30 segundos de una sesión real para 1.º Bachillerato con una noticia de EFE sobre Ucrania. Los seis pensadores trabajan por turnos, Hannah Arendt iguala 1991 con hoy e Ibn Jaldún lo corrige"),
        botones=[("Probar el Consejo (cuenta gratuita de Claude)", "https://claude.ai/artifact/7fyLPT3yg45X1Wr4Mu9rjx"),
                 ("Ver una sesión de ejemplo en PDF", "/assets/pdf/consejo-de-clio-sesion-ucrania.pdf")],
        nota="El vídeo y el PDF se abren sin cuenta. La app pide iniciar sesión en Claude.",
        afirmar=[("Comprobado", "Ibn Jaldún ha detectado varios fallos en las numerosas pruebas que he realizado."),
                 ("En uso", "Recurso abierto a disposición de los docentes."),
                 ("Pendiente", "Medir si las sesiones ahorran tiempo real y cuántos errores deja pasar el revisor.")],
        # el error corregido, de la sesión real: va dentro de «Comprobado»
        capturas=[("/assets/proyectos/consejo-de-clio/ucrania-arendt.jpg", "Turno de Hannah Arendt en la sesión real: «En 1991, la disolución de la URSS dejó a Ucrania como Estado independiente sin que el nuevo marco de seguridad quedara del todo resuelto. Hoy, como entonces, las grandes potencias discuten qué fronteras y qué garantías valen para la región»", "Antes: el turno de Arendt"),
                  ("/assets/proyectos/consejo-de-clio/ucrania-ibn-jaldun.jpg", "Revisión de Ibn Jaldún en la sesión real, aprobada con correcciones: «‹reparto› y ‹las grandes potencias discuten› en 1991 es una equivalencia simplista. Entonces decidieron las repúblicas soviéticas, no un reparto entre potencias»", "Después: la revisión de Ibn Jaldún")],
        necesidad="Traer la actualidad a clase de Historia engancha, pero prepararlo bien lleva tiempo y pedírselo sin más a una IA trae problemas de rigor.",
        pasos_titulo="Cómo funciona",
        pasos=[("1 · Pegas la noticia", "Y eliges el curso. Heródoto la resume sin opinar."),
               ("2 · Cada pensador hace su parte", "Tucídides la sitúa en el temario, Arendt la conecta con el presente, Clío la cuenta, Sócrates plantea el debate."),
               ("3 · Ibn Jaldún revisa", "Corrige lo que no se sostiene antes de que llegue al aula.")],
        aviso=("Contrasta siempre la información.", "Los seis miembros son una IA y pueden equivocarse. Comprueba los datos con la noticia original y otras fuentes antes de usar la sesión."),
        siguiente=("Cazadores de bulos", "cazadores-de-bulos"),
    ),
}

# Repositorio digital: de Didákora, solo el párrafo de «Mantenerlo al día» y dos botones (Jorge, 23-10-2026: Didákora ya
# tiene su sitio). La tabla de antes y ahora, «Así es Didákora» con su vídeo y «Cómo se mantiene al día» siguen arriba en
# este archivo, en _antes/ y en git, por si se quieren recuperar.
for _x in BY["repositorio-digital"]["sections"]:
    if isinstance(_x, dict) and _x.get("title") == "Mantenerlo al día":
        _DIDAKORA_ANTES = _x["after"]  # lo de Didákora pasa a su propia ficha (abajo)
        _x["after"] = ('<p class="dk-botones" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:18px">'
                       '<a class="btn" href="/didakora/">Abrir Didákora</a>'
                       '<a class="btn o" href="/proyectos/monasterio-didakora/">Ver el Monasterio</a></p>')


# ---------------------------------------------------------------- Didákora, con su propia ficha (Jorge, 23-10-2026)
# Con los bloques que estaban en el Repositorio digital (la tabla de antes y ahora, «Así es Didákora» y el Monasterio) y los
# textos de la web de Didákora («Sobre mí» y la autoría). «Lo que hice yo» y «Lo que puedo afirmar», con las palabras de Jorge.
_i = _DIDAKORA_ANTES.index('<div class="caja-demo">'); _v = _DIDAKORA_ANTES.index('<div class="dk-video">'); _m = _DIDAKORA_ANTES.index('<div class="dk-mas">')
_TABLA = _DIDAKORA_ANTES[:_i]
_ASI = re.sub(r"<h3>Así es Didákora</h3>", "", _DIDAKORA_ANTES[_i:_v]) + "</div>"
# La tabla, al día con la lista de cambios de Didákora (CHANGES de tools.js, octubre de 2026): Body Maps y Popplet,
# retiradas, con su alternativa, y CoSpaces Edu, que ahora se llama Delightex Edu
_old = lambda img, n: f'<span class="upd-old"><img src="{img}" alt="" width="24" height="24" loading="lazy"><s>{n}</s></span>'
_new = lambda img, n: f'<span class="upd-lg"><img src="{img}" alt="" width="24" height="24" loading="lazy"><span>{n}</span></span>'
def _añade(t, ancla, html):
    assert ancla in t, ancla
    i = t.index(ancla); j = t.index("</span></div>", i)
    return t[:j] + html + t[j:]
_TABLA = _añade(_TABLA, "<s>Hablaconlahistoria</s>", _old("/herramientas/logos/bodymaps.png", "Body Maps") + _old("/herramientas/logos/popplet.png", "Popplet"))
_TABLA = _añade(_TABLA, "Cada una tiene su alternativa", _new("/herramientas/logos/anatomy3d.png", "Anatomy 3D Atlas") + _new("/herramientas/logos/mindomo.png", "Mindomo"))
_TABLA = _añade(_TABLA, "<s>Freepik</s>", _old("/herramientas/logos/cospaces.png", "CoSpaces Edu"))
_TABLA = _añade(_TABLA, "Con su nombre actual", _new("/assets/tools/delightex.png", "Delightex Edu"))
P.append(dict(
    slug="didakora", cat="profesorado", year="2026", title="Didákora", tags=["Web de recursos", "Docentes"], kind="caso",
    card="120 herramientas digitales para docentes, revisadas a mano.",
    lede="120 herramientas digitales para docentes, revisadas a mano, con su ficha y su fecha.",
    meta=[("Para quién", "Docentes de Infantil, Primaria y Secundaria y Bachillerato"), ("Tipo", "Web de recursos"),
          ("Herramientas", "Web propia"), ("Estado", "Publicada · actualizada en octubre de 2026")],
    links=[("Abrir Didákora", "https://pasadoproximo.github.io/didakora/", "ext"), ("Ver el Monasterio", "/proyectos/monasterio-didakora/", "int")],
    sections=[
        ("La necesidad", '<p class="psub">La tecnología educativa evoluciona muy rápido. Dos años después, muchas herramientas habían cerrado o cambiado. '
                         'Didákora es la actualización del <a href="/proyectos/repositorio-digital/">repositorio digital</a> que creé en 2024 para el Colegio Cerrado de Calderón, que el centro presentó '
                         'en el <a href="https://colegiocerradodecalderon.es/braining/" rel="noopener" target="_blank">IX Congreso Internacional de Creatividad Educativa</a> (Braining, Valencia, 2025).</p>'
                         '<ul class="needs three"><li><b>Qué hice</b><span>La actualización del repositorio de 2024 como web propia, con buscador y diez categorías.</span></li>'
                         '<li><b>Cómo lo hice</b><span>Sustituyendo lo que había cerrado y revisando cada ficha con sus fuentes oficiales.</span></li>'
                         '<li><b>Para qué lo hice</b><span>Para ofrecer un recurso que agilice la búsqueda de herramientas digitales y aportar mi conocimiento sobre ellas.</span></li></ul>'),
        ("Cómo funciona", _ASI),
        ("Qué cambió desde 2024", _TABLA),
        ("Lo que puedo afirmar", '<div class="status"><div class="s-ok"><span class="st-l ok">Comprobado</span><p>Las 120 fichas están revisadas a mano y fechadas: octubre de 2026.</p></div>'
                                 '<div class="s-exp"><span class="st-l exp">En uso</span><p>Publicada y abierta a cualquier docente, sin registro.</p></div>'
                                 '<div class="s-pend"><span class="st-l pend">Pendiente</span><p>Medir cuánto se usa: todavía no tengo datos de visitas.</p></div></div>'),
    ],
    related=["repositorio-digital", "monasterio-didakora", "audita-tu-programacion"],
))
BY["didakora"] = P[-1]
