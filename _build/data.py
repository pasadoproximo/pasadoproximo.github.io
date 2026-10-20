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
        "desc": "Recursos y guías para el trabajo del docente y el portfolio de mi propia formación.",
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
    lede="Una herramienta con IA para docentes: pegas una noticia, eliges el curso y seis personajes de la historia preparan una sesión para el aula. Cada uno tiene su papel y uno existe solo para buscar errores.",
    meta=[("Para quién", "Docentes de Geografía e Historia, de 1.º ESO a Bachillerato"),
          ("Tipo", "Aplicación con IA · material de libre uso"),
          ("Herramientas", "Claude (artefacto con agentes de IA)"),
          ("Estado", "Publicada. Funciona con una cuenta de Claude, también la gratuita")],
    links=[("Probar el consejo", "https://claude.ai/artifact/7fyLPT3yg45X1Wr4Mu9rjx", "ext")],
    cta_note="«Probar el consejo» se abre en Claude y pide iniciar sesión (sirve la cuenta gratuita).",
    sections=[
        ("El problema", """
<p class="cq-par">Traer la actualidad a clase de Historia engancha al alumnado y le hace cuestionársela. Pero, a veces, prepararlo bien lleva tiempo. Pedírselo sin más a una IA es rápido, pero puede inventar un dato o presentar una opinión como un hecho.</p>"""),
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
<p class="psub">Con una sesión real para 4.º ESO.</p>
<div class="cq-how">
<div class="cq-how-t">
<div class="cq-news"><span class="tag">La noticia</span><div><b>La NASA y el Departamento de Energía acuerdan el primer reactor nuclear para misiones espaciales en 2028</b><small>whatsnew.com · 14 de octubre de 2026</small></div></div>
<ol class="cq-pasos">
<li><b>Pegas la noticia y eliges el curso</b><span>Tucídides solo la relaciona con las unidades de ese curso.</span></li>
<li><b>Cada pensador hace su parte</b><span>Aquí, la Guerra Fría y el Sputnik de 1957, un relato y tres preguntas para debatir.</span></li>
<li class="cq-p-rev"><b>Ibn Jaldún revisa y corrige</b><span>Clío daba por hecho lo que era una opinión de la autora. Se corrige antes de llegar a clase.</span></li>
</ol>
</div>
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
    slug="asistente-gpt-2eso", cat="herramientas", year="2024",
    title="Asistente de IA", tags=["TFM", "2.º ESO"], kind="caso",
    card="Un GPT que guía al alumnado sin darle la respuesta y dice siempre de dónde sale cada dato.",
    viz="v-chat",
    h1="PasadoPróximo-2ºESO: un asistente de IA que guía sin resolver",
    lede="Mi TFM del Máster en Tecnología Educativa (Universidad Europea, 2023-2024): un GPT personalizado que acompaña a un grupo de 2.º ESO en Geografía e Historia. No hace la tarea: ayuda a hacerla y dice de dónde sale cada respuesta.",
    meta=[("Para quién", "Un grupo de 2.º ESO y su docente de Geografía e Historia"),
          ("Tipo", "Trabajo Fin de Máster · propuesta didáctica"),
          ("Herramientas", "GPT personalizado (GPT-4o) y Google Classroom"),
          ("Estado", "Configurado y probado en simulación. Sin pilotar con alumnado")],
    links=[("Leer el TFM completo (PDF)", "/assets/pdf/tfm-asistente-gpt-2eso.pdf", "dl")],
    sections=[
        ("La necesidad", """
<p class="psub">Un grupo heterogéneo de 2.º ESO en un instituto público de una barriada de Málaga: aulas de 25 a 30 estudiantes, retroalimentación que llega tarde, dudas sin resolver en casa y alumnado que usa ChatGPT para que le haga la tarea.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Configuré un GPT personalizado que acompaña al grupo en Geografía e Historia: resuelve dudas, propone repasos y dice de dónde sale cada dato.</span></li>
<li><b>Cómo lo hice</b><span>Le di los materiales de las nueve unidades y un banco de preguntas, con instrucciones para priorizar esos materiales, guiar sin resolver y no pedir datos personales.</span></li>
<li><b>Para qué lo hice</b><span>Para que el alumnado tenga apoyo también en casa, reciba retroalimentación a tiempo y aprenda a contrastar, en vez de usar la IA para copiar.</span></li>
</ul>"""),
        dict(title="Qué hace en la práctica",
             intro='<p class="psub">Cuatro comportamientos configurados y probados.</p>',
             cols=2, frame=True,
             figs=[("/assets/proyectos/tfm/guia-sin-resolver.png", "El alumno pide «¿Puedes hacerme la actividad 2 del tema 1?» y el asistente responde que no puede realizarla por él, pero que puede guiarle para completarla", "<b>Guía, no resuelve.</b> Si le piden la actividad, ayuda a hacerla."),
                   ("/assets/proyectos/tfm/fuente-archivos.png", "Respuesta del asistente sobre la sociedad de la Península Ibérica medieval que termina indicando que la información sale del documento de la Unidad 5", "<b>Cita la unidad.</b> Si la respuesta sale de los materiales de clase, dice de cuál."),
                   ("/assets/proyectos/tfm/fuente-ia.png", "Respuesta del asistente sobre Abderramán III que avisa de que la información ha sido generada por inteligencia artificial y debe verificarse", "<b>Avisa si es IA.</b> Si no está en los materiales, lo dice y pide verificarlo."),
                   ("/assets/proyectos/tfm/correccion.png", "El alumno escribe que taifa significa impuesto sobre la tierra y el asistente le corrige: era un pequeño reino musulmán surgido tras la desintegración del Califato de Córdoba", "<b>Corrige el repaso.</b> Explica lo que no se ha entendido.")]),
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
    lede="Una herramienta de estudio para el tema de relieve de Geografía de España. En lugar de memorizar una lista de unidades, el alumnado pulsa sobre lo que quiere repasar y el mapa le señala dónde está, con una ficha explicativa, imágenes y preguntas.",
    meta=[("Nivel", "2.º Bachillerato · Geografía de España"),
          ("Para quién", "Alumnado que estudia el relieve peninsular"),
          ("Tipo", "Aplicación web interactiva"),
          ("Herramientas", "Claude (artefacto web)")],
    links=[("Abrir el mapa", "/apps/mapa-de-relieves/", "int")],
    sections=[
        ("Para qué sirve", """
<p>El relieve de la Península se suele estudiar como una lista de nombres. El problema es que esa lista no dice dónde está cada cosa ni por qué está ahí. El mapa organiza el tema en cuatro bloques y une cada concepto con su lugar:</p>
<ul class="pl">
<li><b>Evolución geológica:</b> qué se formó en cada era.</li>
<li><b>Estructuras:</b> zócalo, cordilleras de plegamiento y cuencas sedimentarias.</li>
<li><b>Roquedo:</b> silíceo, calizo y arcilloso.</li>
<li><b>Erosión:</b> los agentes que han modelado el paisaje.</li>
</ul>
<p>Cada elemento tiene su ficha, imágenes y preguntas de repaso. Así se puede usar para estudiar en casa o en clase, proyectado, para explicar.</p>"""),
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
    lede="Una IA ha escrito un texto sobre la caída de Málaga en 1937. Suena convincente y tiene nueve errores: ocho se cazan con el tema estudiado y el noveno, razonando. Sirve a la vez para repasar y para aprender a no fiarse de un texto solo porque está bien escrito.",
    meta=[("Nivel", "4.º ESO y 2.º Bachillerato"),
          ("Cuándo", "Al final de la unidad de la Guerra Civil, como repaso"),
          ("Duración", "Una sesión de 55 minutos, ampliable a dos"),
          ("Agrupamiento", "Parejas o grupos de 3")],
    links=[("Descargar la actividad (PDF)", "/assets/pdf/cazadores-de-bulos.pdf", "dl")],
    sections=[
        ("Así empieza el texto", """
<p>Un fragmento real del documento que recibe el alumnado. Te enseño dos de los nueve errores; los demás están en el PDF, con el solucionario para el docente.</p>
<blockquote class="excerpt">
<p><mark class="err" id="e1">Málaga fue una de las ciudades que quedaron en manos del bando sublevado desde el mismo comienzo de la guerra</mark><sup aria-hidden="true">1</sup>, en julio de 1936. Aun así, durante el invierno de 1937 se convirtió en uno de los frentes más activos del sur peninsular […]</p>
<p>La defensa de la ciudad estuvo dirigida por <mark class="err" id="e2">el general José Miaja</mark><sup aria-hidden="true">2</sup>, el mismo que unos meses antes había organizado la resistencia de Madrid. […]</p>
</blockquote>
<dl class="errs">
<div><dt><span>1</span> Málaga, sublevada desde julio de 1936</dt><dd>Falso. Málaga fue republicana hasta febrero de 1937. <b>Se comprueba</b> con el mapa de España en julio de 1936.</dd></div>
<div><dt><span>2</span> El general Miaja dirigía la defensa</dt><dd>Falso. Miaja dirigió la defensa de Madrid; en Málaga el responsable era el coronel José Villalba. <b>Se comprueba</b> con el epígrafe de la batalla de Madrid.</dd></div>
</dl>"""),
        ("Cómo se hace", """
<ol class="steps">
<li><b>Se reparte sin avisar (5 min).</b> Lo normal es que nadie sospeche.</li>
<li><b>Se destapa la trampa (5 min):</b> lo ha escrito una IA y tiene nueve errores.</li>
<li><b>A cazar en grupos (25 min),</b> primero de memoria y luego con el libro y el atlas. Un error solo cuenta si dicen dónde lo han comprobado.</li>
<li><b>Puesta en común (20 min):</b> ¿cuál te habrías creído si nadie te avisa?</li>
</ol>"""),
        dict(title="El material", cols=2, intro="<p>El PDF trae la guía docente, el texto, la hoja de registro y el solucionario con su rúbrica.</p>",
             figs=[("/assets/proyectos/cazadores-de-bulos/pagina-2.jpg", "Página 2 del PDF: el Documento A, «La caída de Málaga y la huida por la carretera», con el aviso de que es un texto falso de uso didáctico y pistas para repasar", "Página 2: el texto con los nueve errores y las pistas."),
                   ("/assets/proyectos/cazadores-de-bulos/pagina-3.jpg", "Página 3 del PDF: hoja de registro con columnas para lo que dice el texto, lo que pasó en realidad y dónde se ha comprobado", "Página 3: la hoja de registro del alumnado.")]),
    ],
    related=["la-ia-tambien-miente", "constitucion-1812", "la-nube-pesa"],
))

P.append(dict(
    slug="la-ia-tambien-miente", cat="aula", year="2026",
    title="La IA también miente", tags=["Serie de imágenes", "Cualquier nivel"], kind="ficha",
    card="Escenas históricas generadas con IA con anacronismos escondidos y una trampa en cada una.",
    viz="img:/assets/ia-miente/mercado.jpg",
    lede="Una serie quincenal que publico en LinkedIn. Cada entrega es una escena histórica generada con IA que esconde anacronismos. Y siempre hay una trampa: algo que parece imposible y sí es de la época.",
    meta=[("Para quién", "Docentes que quieran llevarla a clase y cualquiera con curiosidad"),
          ("Tipo", "Serie de imágenes para el aula"),
          ("Herramientas", "Claude y Canva")],
    links=[],
    sections=[
        ("La idea", """
<p>Las imágenes generadas con IA tienen un aspecto muy convincente, pero mezclan épocas sin ningún problema. Buscar los errores obliga a mirar con atención y a preguntarse de dónde viene cada objeto. La trampa final evita que se marque como error todo lo que «parece moderno».</p>"""),
    ],
    gallery=[("/assets/ia-miente/mercado.jpg", "Entrega 1 · Mercado medieval. Hay cinco errores y una trampa.")],
    spoiler=("/assets/ia-miente/mercado-solucion.jpg", "Ver la solución", "Solución: el cartel impreso, el maíz, los tomates, las patatas y los girasoles son anacronismos. Las gafas de lectura sí son de la época."),
    value=["Llevar la alfabetización visual y sobre IA a algo que se resuelve en cinco minutos."],
    related=["cazadores-de-bulos", "consejo-de-clio", "asistente-gpt-2eso"],
))

P.append(dict(
    slug="la-nube-pesa", cat="aula", year="2026",
    title="La nube pesa", tags=["Actividad (PDF)", "2.º ESO"], kind="ficha",
    card="Cada equipo reconstruye un eslabón de lo que hay detrás de un gesto digital y propone una medida.",
    viz="v-nube",
    lede="¿De dónde sale y qué consume un gesto digital? Cinco equipos reconstruyen la cadena que hay detrás de mandar una foto o hacer una pregunta a un asistente: del mineral al residuo.",
    meta=[("Nivel", "2.º ESO, adaptable a 3.º ESO"),
          ("Cuándo", "Al cerrar el tema de recursos naturales y desigualdad"),
          ("Duración", "Una sesión de 55 minutos"),
          ("Agrupamiento", "Cinco equipos de 4 o 5")],
    links=[("Descargar la actividad (PDF)", "/assets/pdf/la-nube-pesa.pdf", "dl")],
    sections=[
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
        dict(title="El material", cols=2, intro="<p>El PDF trae la guía docente cronometrada, las fichas, la hoja de la cadena y el solucionario con las fuentes de los datos.</p>", figs=[("/assets/proyectos/la-nube-pesa/pagina-2.jpg", "Página 2 del PDF: cinco fichas de eslabón (extracción, fabricación y transporte, uso y vida útil, centro de datos y residuo) con datos y preguntas", "Página 2: las cinco fichas de eslabón, para recortar y repartir."), ("/assets/proyectos/la-nube-pesa/pagina-3.jpg", "Página 3 del PDF: hoja de la cadena con columnas de dato y fuente, lugar en el mapa, quién gana y quién pierde y el espacio para la medida", "Página 3: la hoja de la cadena que completa cada equipo.")]),
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
    lede="Un comentario de texto colaborativo con Hypothes.is. Por parejas, el alumnado anota artículos de la Constitución de 1812 y marca cada fragmento como #APOYA, #LIMITA o #PREGUNTA. Después debate con una condición: nada de lo que se diga vale si no está anclado a un fragmento.",
    meta=[("Nivel", "4.º ESO, adaptable a 2.º Bachillerato"),
          ("Cuándo", "Tras la Guerra de la Independencia y las Cortes de Cádiz"),
          ("Duración", "Una sesión de 55 minutos"),
          ("Herramientas", "Hypothes.is (o Google Docs con comentarios)")],
    links=[("Descargar la actividad (PDF)", "/assets/pdf/constitucion-1812-hypothesis.pdf", "dl")],
    sections=[
        ("Cómo se hace", """
<ol class="steps">
<li><b>La pregunta (5 min).</b> Dos equipos con postura asignada: ruptura revolucionaria o liberalización con límites.</li>
<li><b>Anotación por parejas (20 min).</b> Al menos tres anotaciones y una respondiendo a otra pareja. El docente ve el margen en directo.</li>
<li><b>Debate (15 min).</b> Cada intervención empieza citando el artículo anotado.</li>
<li><b>Cierre (10 min).</b> Votación razonada y una pregunta: ¿por qué un mismo texto puede sostener las dos posturas?</li>
</ol>
<p>Incluye un plan B sin cuentas, con Google Docs y variantes para subir o bajar el nivel.</p>"""),
        dict(title="El material", cols=2, intro="<p>El PDF trae la guía docente, el dosier de artículos, la hoja de registro y el solucionario con rúbrica.</p>", figs=[("/assets/proyectos/constitucion-1812/pagina-2.jpg", "Página 2 del PDF: dosier de trabajo con artículos de la Constitución de 1812 y el protocolo de anotación #APOYA, #LIMITA y #PREGUNTA", "Página 2: el dosier de artículos y el protocolo de marcas."), ("/assets/proyectos/constitucion-1812/pagina-3.jpg", "Página 3 del PDF: hoja de registro con tabla de anotaciones, respuesta a otra pareja y votación razonada", "Página 3: la hoja de registro de la pareja.")]),
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
    lede="Un escape room digital para repasar el siglo XIX español. Ambientado en <i>El Ministerio del Tiempo</i>, el alumnado actúa como agentes que deben impedir que se altere el 2 de mayo de 1808.",
    meta=[("Nivel", "4.º ESO"),
          ("Tipo", "Escape room digital de repaso"),
          ("Herramientas", "Genially")],
    links=[("Jugar al escape room", "https://view.genially.com/65f972b6e99bde00148864ea", "ext")],
    sections=[
        ("Qué hay dentro", """
<p>Las pruebas recorren el siglo: las Pinturas Negras de Goya, textos para completar sobre la Guerra de la Independencia, el Trienio Liberal, el Bienio Progresista y La Gloriosa. Al final hay una caja fuerte con un código que solo se abre con lo aprendido.</p>
<p>Un tema largo y con muchas fechas se convierte en una misión con un orden y una meta.</p>"""),
        dict(title="Así se ve", cols=1, figs=[("/assets/proyectos/escape-room-siglo-xix/portada.jpg", "Pantalla de inicio del escape room en Genially, con el logotipo de El Ministerio del Tiempo sobre una mesa de despacho y el botón Empezar", "La pantalla de inicio en Genially.")]),
    ],
    value=["Diseñar un repaso gamificado con una narrativa que el alumnado reconoce."],
    related=["excursion-roma-3d", "la-ia-tambien-miente", "constitucion-1812"],
))

P.append(dict(
    slug="excursion-roma-3d", cat="aula", year="2024",
    title="Excursión a Roma en 3D", tags=["Mundo 3D", "1.º ESO"], kind="ficha",
    card="Un mundo 3D con edificios de la Antigua Roma para recorrer su arquitectura.",
    viz="v-cos",
    lede="Un mundo virtual con algunos de los edificios más representativos de la Antigua Roma, creado para recorrerlo en clase. Es una actividad de introducción: primero una visita guiada y después se comparan la arquitectura romana y la griega.",
    meta=[("Nivel", "1.º ESO"),
          ("Tipo", "Mundo 3D para una visita guiada"),
          ("Herramientas", "CoSpaces Edu (hoy Delightex)")],
    links=[("Visitar el mundo 3D", "https://edu.delightex.com/EXA-NNH", "ext")],
    sections=[
        ("La idea", """
<p>La idea es motivar al alumnado a través de la inmersión: que se sitúe en el espacio antes de entrar en los conceptos. En una de las habitaciones de la domus me encontraréis descansando: un guiño para que la visita tenga algo de juego.</p>"""),
        dict(title="Así se ve", cols=1, figs=[("/assets/proyectos/excursion-roma-3d/delightex.jpg", "Página pública del mundo «Excursión a Roma» en Delightex: una habitación de la domus con un avatar y la descripción de la actividad", "La página del mundo en Delightex, con una habitación de la domus.")]),
    ],
    value=["Usar la realidad virtual al servicio de un objetivo concreto: comparar dos arquitecturas."],
    related=["escape-room-siglo-xix", "mapa-de-relieves", "la-ia-tambien-miente"],
))

# ---------------------------------------------------------------- PROFESORADO
P.append(dict(
    slug="repositorio-digital", cat="profesorado", year="2024 · 2026",
    title="Repositorio digital docente", tags=["Web de recursos", "Profesorado"], kind="caso",
    lab="Web de recursos",
    card="La web de herramientas que creé para un centro en 2024 y que en 2026 se ha convertido en Didakora.",
    viz="v-caja",
    h1="Del repositorio de centro a Didakora",
    lede="Una web para que el profesorado encuentre rápido qué herramienta digital usar. La creé en 2024 para el Colegio Cerrado de Calderón (Málaga), en las prácticas del Máster en Tecnología Educativa. En 2026 la he convertido en Didakora, una web propia de herramientas revisadas para docentes.",
    meta=[("Para quién", "El claustro del centro (2024) y docentes de todas las etapas (2026)"),
          ("Tipo", "Web de recursos y autoformación"),
          ("Herramientas", "Google Sites (2024) · Didakora, web propia (2026)"),
          ("Reconocimiento", "Presentada por el centro en Braining 2025")],
    links=[("Ver el repositorio original", "https://sites.google.com/view/repositorio-digital-docente-cc/inicio", "ext"),
           ("Abrir Didakora", "https://pasadoproximo.github.io/didakora/", "ext")],
    sections=[
        ("La necesidad", """
<p class="psub">La dirección estaba intentando fomentar la digitalización del centro y el claustro tenía dificultades para encontrar las herramientas digitales adecuadas. Faltaba un sitio común claro y adaptado a todas las etapas (Infantil, Primaria y Secundaria) que permitiera la autoformación del profesorado.</p>
<ul class="needs three">
<li><b>Qué hice</b><span>Elaboré una web mediante Google Sites donde se recogían todas las herramientas digitales que los docentes podían usar en sus clases. Se organizaba por etapas y materias.</span></li>
<li><b>Cómo lo hice</b><span>Realicé una curación de herramientas digitales específica tras detectar mediante entrevistas las necesidades del centro y de los propios docentes.</span></li>
<li><b>Para qué lo hice</b><span>Para fomentar la autoformación del profesorado y estandarizar los criterios de selección de herramientas digitales de acuerdo a lo que demandaba el centro.</span></li>
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
             intro='<p class="psub">La tecnología educativa evoluciona muy rápido: dos años después, muchas herramientas habían cerrado o cambiado. Por eso en 2026 la he rehecho como Didakora.</p>',
             cols=1, figs=[],
             after="""<div class="upd">
<div class="upd-h" aria-hidden="true"><span>Antes</span><span></span><span>Ahora</span></div>
<div class="upd-r"><div class="upd-a"><b>Herramientas cerradas</b><span class="upd-logos"><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/flip.png" alt="" width="24" height="24" loading="lazy"><s>Flip</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/tome.png" alt="" width="24" height="24" loading="lazy"><s>Tome</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/classcraft.png" alt="" width="24" height="24" loading="lazy"><s>Classcraft</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/earteach.svg" alt="" width="24" height="24" loading="lazy"><s>EarTeach</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/hablaconlahistoria.svg" alt="" width="24" height="24" loading="lazy"><s>Hablaconlahistoria</s></span></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Cada una tiene su alternativa</b><span class="upd-logos"><span class="upd-lg"><img src="/herramientas/logos/padlet.png" alt="" width="24" height="24" loading="lazy"><span>Padlet</span></span><span class="upd-lg"><img src="/herramientas/logos/gamma.png" alt="" width="24" height="24" loading="lazy"><span>Gamma</span></span><span class="upd-lg"><img src="/herramientas/logos/classdojo.png" alt="" width="24" height="24" loading="lazy"><span>ClassDojo</span></span><span class="upd-lg"><img src="/herramientas/logos/musictheory.png" alt="" width="24" height="24" loading="lazy"><span>musictheory.net</span></span><span class="upd-lg"><img src="/herramientas/logos/gemini.png" alt="" width="24" height="24" loading="lazy"><span>Gemini</span></span></span></div></div>
<div class="upd-r"><div class="upd-a"><b>Nombres que cambiaron</b><span class="upd-logos"><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/quizizz.png" alt="" width="24" height="24" loading="lazy"><s>Quizizz</s></span><span class="upd-old"><img src="/assets/proyectos/repositorio-digital/antes/freepik.png" alt="" width="24" height="24" loading="lazy"><s>Freepik</s></span></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Con su nombre actual</b><span class="upd-logos"><span class="upd-lg"><img src="/herramientas/logos/wayground.png" alt="" width="24" height="24" loading="lazy"><span>Wayground</span></span><span class="upd-lg"><img src="/herramientas/logos/magnific.png" alt="" width="24" height="24" loading="lazy"><span>Magnific</span></span></span></div></div>
<div class="upd-r"><div class="upd-a"><b>Faltaba la IA de los centros</b><span class="upd-gone"><em>Ninguna IA con cuenta del centro</em></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Para usarla con la cuenta del centro</b><span class="upd-logos"><span class="upd-lg"><img src="/herramientas/logos/gemini.png" alt="" width="24" height="24" loading="lazy"><span>Gemini</span></span><span class="upd-lg"><img src="/herramientas/logos/notebooklm.png" alt="" width="24" height="24" loading="lazy"><span>NotebookLM</span></span><span class="upd-lg"><img src="/herramientas/logos/copilot.png" alt="" width="24" height="24" loading="lazy"><span>Copilot</span></span></span></div></div>
<div class="upd-r"><div class="upd-a"><b>Difícil de encontrar</b><span class="upd-path"><span>Etapa</span><i>›</i><span>Materia</span><i>›</i><span>Herramienta</span></span></div><span class="upd-ar" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span><div class="upd-b"><span class="vh">Ahora: </span><b>Se busca por nombre o por lo que necesitas</b></div></div>
</div>
<div class="caja-demo">
<h3>Así es Didakora</h3>
<div class="dk-t"><p>Se busca por el nombre de la herramienta o por lo que quieres hacer y se filtra por etapa. También se puede entrar por diez categorías según para qué sirve cada herramienta.</p><p class="cdf-t">Cada ficha te da</p><ul class="cdf"><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 11v5M12 8h.01"/></svg></span>Qué es la herramienta</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 7h10M7 11h10M7 15h6"/><path d="M5 3h14v18l-3.5-2.5L12 21l-3.5-2.5L5 21z"/></svg></span>Para qué la puedes usar</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M2 9 12 4l10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg></span>La etapa</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M14 9l2 2"/></svg></span>Dispositivos y cuenta que necesita</li><li><span class="cdf-i" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 7h11M4 12h16M4 17h9"/></svg></span>Herramientas alternativas</li></ul>
</div>
<div class="dk-video">
<video src="/assets/proyectos/repositorio-digital/didakora.webm" poster="/assets/proyectos/repositorio-digital/didakora-video.jpg" width="1264" height="712" muted loop playsinline preload="metadata" aria-label="Vídeo de Didakora: se busca «repasar», se filtra por Primaria y se abre la ficha de Kahoot!, con qué es, para qué usarla, qué necesita y sus alternativas"></video>
<button type="button" class="dk-play" aria-label="Pausar el vídeo"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-pause" d="M9 6v12M15 6v12"/><path class="i-play" d="M8 5.5v13l11-6.5z"/></svg></button>
<script>(()=>{const w=document.currentScript.parentElement,v=w.querySelector("video"),b=w.querySelector(".dk-play");
const set=on=>{w.classList.toggle("paused",!on);b.setAttribute("aria-label",on?"Pausar el vídeo":"Reproducir el vídeo");};
b.addEventListener("click",()=>{if(v.paused){v.play();set(true);}else{v.pause();set(false);}});
// arranca al verse en pantalla, salvo si el sistema pide reducir el movimiento
if(matchMedia("(prefers-reduced-motion: reduce)").matches){set(false);return;}
new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting&&!w.classList.contains("paused"))v.play().catch(()=>set(false));else if(!e.isIntersecting)v.pause();}),{threshold:.3}).observe(v);})();</script>
</div>
</div>"""),
    ],
    related=["audita-tu-programacion", "rubrica-materiales-digitales", "e-portfolio-master"],
))

P.append(dict(
    slug="audita-tu-programacion", cat="profesorado", year="2026",
    title="Audita tu programación", tags=["Guía (PDF)", "Profesorado"], kind="ficha",
    card="Un método con NotebookLM para encontrar criterios de evaluación que no se evalúan en ninguna actividad.",
    viz="v-aud",
    lede="Una programación didáctica tiene decenas de páginas y nadie la sostiene entera en la cabeza. El fallo típico es un criterio de evaluación que está en la tabla y luego no se evalúa en ninguna actividad. Esta guía usa NotebookLM para localizar esos huecos, con cita y página.",
    meta=[("Para quién", "Docentes y opositores que revisan su programación"),
          ("Tipo", "Guía paso a paso con ocho prompts"),
          ("Herramientas", "NotebookLM (plan gratuito)"),
          ("Tiempo", "Unos 40 minutos la primera vez")],
    links=[("Descargar la guía (PDF)", "/assets/pdf/audita-tu-programacion.pdf", "dl")],
    sections=[
        ("Cómo está pensada", """
<p>NotebookLM responde citando el fragmento exacto del documento que se le sube y eso permite comprobar cada respuesta. No es un corrector: es un buscador que señala dónde mirar. La decisión sobre si un criterio está evaluado sigue siendo del docente, con el documento delante.</p>
<ul class="pl">
<li><b>Antes de nada, privacidad:</b> quitar la portada con el nombre y el DNI antes de subir el documento.</li>
<li><b>Ocho prompts en orden:</b> del inventario de criterios a la cobertura, cada uno apoyado en el anterior.</li>
<li><b>Una hoja de registro</b> para anotar el veredicto, porque la herramienta no lo guarda.</li>
</ul>"""),
        dict(title="El material", cols=2, intro="<p>La guía tiene cuatro páginas: montaje del cuaderno, los ocho prompts, la hoja de auditoría y qué hacer cuando la herramienta se equivoca.</p>", figs=[("/assets/proyectos/audita-tu-programacion/pagina-2.jpg", "Página 2 del PDF: los ocho prompts numerados (inventario, cobertura, los huecos, nombrar no es evaluar, sobrecarga, instrumentos, contraste con el decreto y la defensa)", "Página 2: los ocho prompts, para copiar tal cual."), ("/assets/proyectos/audita-tu-programacion/pagina-3.jpg", "Página 3 del PDF: hoja de auditoría con columnas para criterio, qué dice la herramienta, fragmento citado y comprobación", "Página 3: la hoja de auditoría donde se anota el veredicto.")]),
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
    lede="Una calculadora para opositores: calcula la probabilidad de que en el sorteo salga al menos uno de los temas que llevas preparados. Sirve para cualquier especialidad.",
    meta=[("Para quién", "Opositores de cualquier especialidad"),
          ("Tipo", "Aplicación web"),
          ("Herramientas", "Claude (artefacto web)"),
          ("Privacidad", "Los datos no salen del navegador")],
    links=[("Abrir El bombo", "/apps/el-bombo/", "int")],
    sections=[
        ("Para qué sirve", """
<p>Decidir cuántos temas preparar es una de las dudas más habituales al opositar. Ver la probabilidad real ayuda a planificar el estudio con datos en lugar de intuiciones.</p>"""),
    ],
    value=["Resolver una necesidad concreta con una herramienta sencilla y sin pedir datos."],
    related=["audita-tu-programacion", "rubrica-materiales-digitales", "repositorio-digital"],
))

P.append(dict(
    slug="rubrica-materiales-digitales", cat="profesorado", year="2024",
    title="Rúbrica de materiales digitales", tags=["Formulario", "Profesorado"], kind="ficha",
    card="Una rúbrica en formulario para valorar un recurso digital antes de llevarlo al aula.",
    viz="v-rub",
    lede="Un formulario de 17 preguntas para valorar un material educativo digital antes de llevarlo al aula, basado en la norma UNE 71362:2020 de calidad de los materiales educativos digitales.",
    meta=[("Para quién", "Docentes que eligen recursos digitales"),
          ("Tipo", "Rúbrica en formulario"),
          ("Herramientas", "Jotform")],
    links=[("Abrir la rúbrica", "https://form.jotform.com/241185578598070", "ext")],
    sections=[dict(title="Así se ve", cols=1, figs=[("/assets/proyectos/rubrica-materiales-digitales/formulario.jpg", "Pantalla de inicio del formulario en Jotform: Instrumento de evaluación digital, basado en la normativa 71362:2020, 17 preguntas", "La pantalla de inicio del formulario.")])],
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
<li><b>Reflexión sobre la práctica</b><span>Cada trabajo termina con qué aprendió y cómo lo llevaría a clase.</span><em>Todos los módulos</em></li>
</ul>"""),
        dict(title="Así se ve", cols=1, figs=[("/assets/proyectos/e-portfolio-master/inicio.jpg", "Portada del e-Portfolio en Google Sites con el menú de los cinco módulos, galería de imágenes y sobre mí", "La portada, con un apartado por módulo.")]),
    ],
    value=["Documentar el propio aprendizaje y las evidencias de cada módulo."],
    related=["asistente-gpt-2eso", "repositorio-digital", "rubrica-materiales-digitales"],
))

FEATURED = ["repositorio-digital", "asistente-gpt-2eso", "consejo-de-clio", "cazadores-de-bulos"]

BY = {p["slug"]: p for p in P}
