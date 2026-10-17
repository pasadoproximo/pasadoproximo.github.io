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
        "desc": "Recursos y guías para el trabajo del docente, y el portfolio de mi propia formación.",
    },
}

ICON_EXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
FIG_GUIA = "FIG:/assets/proyectos/tfm/guia-sin-resolver.png|El alumno pide «¿Puedes hacerme la actividad 2 del tema 1?» y el asistente responde que no puede realizarla por él, pero que puede guiarle para completarla|El asistente se niega y ofrece ayuda para hacerla."
ICON_DL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'

P = []

# ---------------------------------------------------------------- HERRAMIENTAS
P.append(dict(
    slug="consejo-de-clio", ext="/consejo-de-clio/", cat="herramientas", year="2026",
    title="El Consejo de Clío", tags=["Aplicación con IA", "Secundaria"], kind="caso",
    card="Seis agentes de IA convierten una noticia de hoy en una sesión de clase, y uno revisa a todos.",
    viz="council",
))

P.append(dict(
    slug="asistente-gpt-2eso", cat="herramientas", year="2024",
    title="Asistente de IA para 2.º ESO", tags=["Trabajo Fin de Máster", "2.º ESO"], kind="caso",
    card="Un GPT que guía al alumnado sin darle la respuesta y dice siempre de dónde sale cada dato.",
    viz="v-chat",
    h1="PasadoPróximo-2ºESO: un asistente de IA que guía sin resolver",
    lede="Mi Trabajo Fin del Máster en Tecnología Educativa (Universidad Europea, 2023-2024): un asistente creado con los GPT personalizados de ChatGPT para acompañar a un grupo de 2.º ESO en Geografía e Historia. No hace la tarea por el alumno: le ayuda a hacerla y le dice de dónde sale cada respuesta.",
    meta=[("Para quién", "Un grupo de 2.º ESO y su docente de Geografía e Historia"),
          ("Tipo", "Trabajo Fin de Máster · propuesta didáctica"),
          ("Herramientas", "GPT personalizado (GPT-4o) y Google Classroom"),
          ("Estado", "Configurado y probado en simulación. Sin pilotar con alumnado")],
    links=[("Leer el TFM completo (PDF)", "/assets/pdf/tfm-asistente-gpt-2eso.pdf", "dl")],
    sections=[
        ("El problema", """
<p>Un instituto público de una barriada de Málaga y un grupo de 2.º ESO heterogéneo, con alumnado desenganchado y varios casos que necesitan apoyos distintos. El TFM parte de siete necesidades:</p>
<ul class="pl two">
<li><b>Aulas llenas:</b> 25 a 30 estudiantes por grupo.</li>
<li><b>Retroalimentación tardía:</b> el error se descubre cuando ya ha pasado.</li>
<li><b>Recursos poco adaptados</b> a cada alumno.</li>
<li><b>Dudas en casa</b> sin nadie a quien preguntar.</li>
<li><b>Desinformación:</b> hace falta aprender a contrastar.</li>
<li><b>Mal uso de ChatGPT</b> para que haga la tarea.</li>
<li><b>Recelo docente</b> ante la IA sin haberla probado.</li>
</ul>"""),
        dict(title="La decisión clave: guiar, no resolver",
             intro="<p>En las pruebas apareció el fallo más importante: cuando se le pedía una actividad, el asistente la resolvía. Así perdía todo su valor didáctico. Lo reconfiguré para que se negara a hacerla y ofreciera ayuda para llegar a la respuesta.</p>",
             cols=2,
             figs=[],
             after="""<div class="vs">
<div class="vs-a"><span class="vs-l">Antes del ajuste</span><p class="vs-q">«¿Puedes hacerme la actividad 2 del tema 1?»</p><p>El asistente <b>resolvía la actividad</b>. Lo documenté en las pruebas del TFM; no conservo captura de esa versión.</p></div>
<div class="vs-b"><span class="vs-l">Después del ajuste</span>""" + FIG_GUIA + """</div>
</div>"""),
        dict(title="Dice de dónde sale cada respuesta",
             intro="<p>Prioriza los materiales de clase. Cuando la información no está en ellos, lo dice y avisa de que hay que comprobarla.</p>",
             cols=2,
             figs=[("/assets/proyectos/tfm/fuente-archivos.png", "Respuesta del asistente sobre la sociedad de la Península Ibérica medieval que termina indicando que la información sale del documento de la Unidad 5", "Si sale de los materiales, cita la unidad."),
                   ("/assets/proyectos/tfm/fuente-ia.png", "Respuesta del asistente sobre Abderramán III que avisa de que la información ha sido generada por inteligencia artificial y debe verificarse", "Si no, avisa de que la ha generado la IA y hay que verificarla.")]),
        dict(title="También sirve para repasar",
             intro="<p>Tiene un banco de preguntas de cada unidad. El alumno responde y el asistente corrige lo que no ha entendido.</p>",
             cols=1,
             figs=[("/assets/proyectos/tfm/correccion.png", "El alumno escribe que taifa significa impuesto sobre la tierra y el asistente le corrige: era un pequeño reino musulmán surgido tras la desintegración del Califato de Córdoba", "Corrección de dos definiciones del tema de la Península Ibérica en la Edad Media.")]),
        ("Cómo se hizo", """
<ol class="steps">
<li><b>Necesidades y objetivos</b> del grupo, con el marco de la LOMLOE, el currículo andaluz, el DUA y la protección de datos.</li>
<li><b>Materiales:</b> nueve unidades del curso, guías (comentario de texto, resumen, línea del tiempo…), banco de preguntas, rúbricas y un tablón de anuncios.</li>
<li><b>Configuración:</b> contexto del grupo sin datos personales, prioridad a los materiales, fuentes académicas y aviso de origen en cada respuesta.</li>
<li><b>Pruebas simuladas y ajustes</b>, recogidas en el anexo del TFM.</li>
<li><b>Plan para el aula:</b> cuestionario inicial, sesión de uso ético, reunión con familias, cinco actividades de ejemplo y evaluación con rúbricas y revisión de conversaciones.</li>
</ol>"""),
        ("Lo comprobado y lo pendiente", """
<div class="status">
<div><span class="st-l ok">Comprobado</span><p>Que el asistente se puede configurar para guiar sin resolver, priorizar los materiales y avisar del origen de cada dato. Lo muestran las capturas, que son de las pruebas de configuración.</p></div>
<div><span class="st-l exp">Esperado, sin evaluar</span><p>Más comprensión de los contenidos, autonomía y pensamiento crítico. El TFM lo plantea como objetivos y propone cómo medirlos, pero no hay datos.</p></div>
<div><span class="st-l pend">Pendiente</span><p>Pilotarlo con un grupo real y pasar el cuestionario de efectividad. Riesgos a vigilar: dependencia tecnológica, sobrecarga de información y formación docente.</p></div>
</div>"""),
    ],
    related=["consejo-de-clio", "la-ia-tambien-miente", "audita-tu-programacion"],
))

P.append(dict(
    slug="mapa-de-relieves", cat="herramientas", year="2026",
    title="Mapa de relieves de la Península Ibérica", tags=["Aplicación web", "Bachillerato"], kind="ficha",
    card="Un mapa interactivo que localiza cada relieve, era geológica o agente erosivo y lo explica.",
    viz="map",
    lede="Una herramienta de estudio para el tema de relieve de Geografía de España. En lugar de memorizar una lista de unidades, el alumnado pulsa sobre lo que quiere repasar y el mapa le señala dónde está, con una ficha explicativa, imágenes y preguntas.",
    meta=[("Para quién", "Alumnado que estudia el relieve peninsular"),
          ("Tipo", "Aplicación web interactiva"),
          ("Herramientas", "Claude (artefacto web)")],
    links=[("Abrir el mapa", "https://claude.ai/artifact/YNDYutXDuViE2pPjahzvFm", "ext")],
cta_note="Se abre en Claude. Puede pedir que inicies sesión.",
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
    title="Cazadores de bulos históricos", tags=["Actividad (PDF)", "4.º ESO y 2.º Bachillerato"], kind="ficha",
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
    meta=[("Para quién", "Docentes que quieran llevarla a clase, y cualquiera con curiosidad"),
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
        dict(title="El material", cols=2, intro="<p>El PDF trae la guía docente cronometrada, las fichas, la hoja de la cadena y el solucionario con las fuentes de los datos.</p>", figs=[("/assets/proyectos/la-nube-pesa/pagina-2.jpg", "Página 2 del PDF: cinco fichas de eslabón (extracción, fabricación y transporte, uso y vida útil, centro de datos y residuo) con datos y preguntas", "Página 2: las cinco fichas de eslabón, para recortar y repartir."), ("/assets/proyectos/la-nube-pesa/pagina-3.jpg", "Página 3 del PDF: hoja de la cadena con columnas de dato y fuente, lugar en el mapa, quién gana y quién pierde, y el espacio para la medida", "Página 3: la hoja de la cadena que completa cada equipo.")]),
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
<li><b>Anotación por parejas (20 min).</b> Al menos tres anotaciones, y una respondiendo a otra pareja. El docente ve el margen en directo.</li>
<li><b>Debate (15 min).</b> Cada intervención empieza citando el artículo anotado.</li>
<li><b>Cierre (10 min).</b> Votación razonada y una pregunta: ¿por qué un mismo texto puede sostener las dos posturas?</li>
</ol>
<p>Incluye un plan B sin cuentas, con Google Docs, y variantes para subir o bajar el nivel.</p>"""),
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
    title="Excursión a Roma en 3D", tags=["Mundo 3D", "ESO"], kind="ficha",
    card="Un mundo 3D con edificios de la Antigua Roma para recorrer su arquitectura.",
    viz="v-cos",
    lede="Un mundo virtual con algunos de los edificios más representativos de la Antigua Roma, creado para recorrerlo en clase. Es una actividad de introducción: primero una visita guiada y después se comparan la arquitectura romana y la griega.",
    meta=[("Tipo", "Mundo 3D para una visita guiada"),
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
    card="La web de herramientas que creé para un centro en 2024 y su revisión de 2026 para Secundaria.",
    viz="v-caja",
    h1="Del repositorio de centro a la caja de herramientas",
    lede="Una web para que el profesorado encuentre rápido qué herramienta digital usar, para qué edad y cómo. La creé en 2024 para el Colegio Cerrado de Calderón (Málaga), en las prácticas del Máster en Tecnología Educativa, y en 2026 la he rehecho para Secundaria.",
    meta=[("Para quién", "El claustro del centro (2024) y docentes de Secundaria (2026)"),
          ("Tipo", "Web de recursos y autoformación"),
          ("Herramientas", "Google Sites (2024) · web propia (2026)"),
          ("Reconocimiento", "Presentada por el centro en Braining 2025")],
    links=[("Abrir la caja de herramientas", "/herramientas/", "int"),
           ("Ver el repositorio original", "https://sites.google.com/view/repositorio-digital-docente-cc/inicio", "ext"),
           ("Noticia de Braining", "https://colegiocerradodecalderon.es/braining/", "ext")],
    sections=[
        ("La necesidad", "<p>Hay cientos de herramientas y poco tiempo para probarlas. Un docente necesita saber de un vistazo qué hace cada una, para qué edad sirve y cómo usarla en su materia.</p>"),
        dict(title="2024 · La web del centro",
             intro="<p>Organizada por etapas y, en Secundaria y Bachillerato, por departamentos, con un apartado de apoyo al profesorado. Cada herramienta tiene una ficha con su función, la edad recomendada, ideas de uso y un tutorial en vídeo. El centro la presentó en el IX Congreso Internacional de Creatividad Educativa (Braining, Valencia, abril de 2025) como herramienta de autoformación.</p>",
             cols=1,
             figs=[("/assets/proyectos/repositorio-digital/inicio-2024.jpg", "Portada del repositorio en Google Sites: menú por etapas (Infantil, Primaria, Secundaria y Bachillerato, Apoyo docente, Recursos) y los objetivos del repositorio", "La portada, con el menú por etapas y los objetivos.")],
             after=""),
        dict(title="", cols=2, intro="",
             figs=[("/assets/proyectos/repositorio-digital/sociales-2024.jpg", "Página de Sociales del repositorio: lista de herramientas específicas (StopMotion, realidad virtual, mapas, cronogramas, debates…) y la ficha de StopMotion", "Sociales: herramientas específicas de la materia y su ficha."),
                   ("/assets/proyectos/repositorio-digital/apoyo-docente-2024.jpg", "Página de Apoyo docente del repositorio con su índice: edición de PDF, inteligencia artificial, curación de contenido y evaluación", "Apoyo docente: herramientas para el trabajo del profesor.")]),
        dict(title="2026 · La caja de herramientas",
             intro="<p>Dos años después muchas herramientas habían cerrado o cambiado. La he rehecho para Secundaria: separada por quién la usa (aula, docente y recursos), revisada una a una en octubre de 2026, con lo que ha cerrado y su alternativa, y con la IA que ya llega con la cuenta del centro.</p>",
             cols=2,
             figs=[("/assets/proyectos/repositorio-digital/caja-2026.jpg", "Portada de la Caja de herramientas digitales: 64 herramientas para el aula, 34 para el docente, 20 recursos y 7 que han cerrado o cambiado", "La portada: qué hay y qué ha cambiado desde 2024."),
                   ("/assets/proyectos/repositorio-digital/caja-fichas-2026.jpg", "Fichas de la caja con qué hace el alumnado, ideas para clase, nivel, dispositivos y cuenta necesaria, y botones de abrir y tutoriales", "Cada ficha dice qué hace el alumnado, ideas para clase y qué necesita.")]),
        ("Lo que puedo afirmar", "<p>El centro la usa y la presentó en Braining. No tengo datos de visitas ni de uso por parte del profesorado, así que no los incluyo.</p>"),
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
<p>NotebookLM responde citando el fragmento exacto del documento que se le sube, y eso permite comprobar cada respuesta. No es un corrector: es un buscador que señala dónde mirar. La decisión sobre si un criterio está evaluado sigue siendo del docente, con el documento delante.</p>
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
    links=[("Abrir El bombo", "https://claude.ai/artifact/QpKwMAWgRSBhUjUpAgk8LM", "ext")],
cta_note="Se abre en Claude. Puede pedir que inicies sesión.",
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
    lede="El portfolio digital del Máster en Tecnología Educativa y Competencias Digitales (Universidad Europea, 2023-2024). Recoge el trabajo de los cinco módulos: curación de información, visualización, Aula del Futuro y más.",
    meta=[("Tipo", "Portfolio académico"),
          ("Herramientas", "Google Sites")],
    links=[("Ver el e-Portfolio", "https://sites.google.com/view/e-portfolio-jorge/inicio", "ext")],
    sections=[dict(title="Así se ve", cols=1, figs=[("/assets/proyectos/e-portfolio-master/inicio.jpg", "Portada del e-Portfolio en Google Sites con el menú de los cinco módulos, galería de imágenes y sobre mí", "La portada, con un apartado por módulo.")])],
    value=["Documentar el propio aprendizaje y las evidencias de cada módulo."],
    related=["asistente-gpt-2eso", "repositorio-digital", "rubrica-materiales-digitales"],
))

FEATURED = ["consejo-de-clio", "repositorio-digital", "asistente-gpt-2eso", "cazadores-de-bulos"]

BY = {p["slug"]: p for p in P}
