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
        "name": "Para el profesorado",
        "desc": "Recursos, guías y formación pensados para el trabajo del docente, no para el del alumnado.",
    },
}

ICON_EXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
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
    h1="PasadoPróximo-2ºESO: un asistente de IA para la clase de Historia",
    lede="Trabajo Fin del Máster en Tecnología Educativa y Competencias Digitales (Universidad Europea, curso 2023-2024). Propone un asistente creado con los GPT personalizados de ChatGPT para acompañar a un grupo de 2.º de ESO en Geografía e Historia, dentro y fuera del aula.",
    meta=[("Para quién", "Un grupo de 2.º ESO y su docente de Geografía e Historia"),
          ("Tipo", "Trabajo Fin de Máster · propuesta didáctica"),
          ("Herramientas", "GPT personalizado (GPT-4o) y Google Classroom"),
          ("Estado", "Diseñado y probado en simulación. Pendiente de pilotaje con alumnado")],
    links=[("Leer el TFM completo", "/assets/pdf/tfm-asistente-gpt-2eso.pdf", "dl")],
    sections=[
        ("El problema", """
<p>El punto de partida es un instituto público de una barriada de Málaga y un grupo de 2.º de ESO heterogéneo: alumnado que va bien, alumnado desenganchado de la materia y varios casos que necesitan apoyos distintos (dificultades con el idioma, discapacidad visual, altas capacidades). En ese contexto el TFM identifica siete necesidades concretas:</p>
<ul class="pl">
<li><b>Aulas llenas.</b> Con 25 a 30 estudiantes es muy difícil atender los ritmos de cada uno.</li>
<li><b>Retroalimentación tardía.</b> El alumnado se entera de lo que no ha entendido cuando ya ha pasado.</li>
<li><b>Recursos poco adaptados.</b> Preparar un material distinto para cada caso no es realista.</li>
<li><b>Desconexión fuera del aula.</b> Muchos problemas aparecen en casa, al hacer la tarea sin nadie a quien preguntar.</li>
<li><b>Desinformación.</b> Hace falta aprender a contrastar lo que se lee.</li>
<li><b>Mal uso de ChatGPT.</b> Se usa para que haga la tarea, sin esfuerzo cognitivo.</li>
<li><b>Recelo docente.</b> Parte del departamento rechaza la IA sin haberla probado.</li>
</ul>"""),
        ("Qué se propone", """
<p>Un asistente de clase que se nutre de los materiales del curso y no sustituye al docente. Las decisiones de diseño más importantes fueron estas:</p>
<ol class="steps">
<li><b>Primero, los materiales del aula.</b> Se le cargaron nueve unidades del curso, guías para hacer comentarios de texto, resúmenes o líneas del tiempo, un banco de preguntas de repaso, los enunciados y rúbricas de las actividades y un tablón de anuncios. Solo recurre a internet cuando el alumno quiere ampliar.</li>
<li><b>Guía, no resuelve.</b> Si se le pide hacer una actividad, se niega y ofrece ayuda para que el alumno la haga.</li>
<li><b>Dice de dónde sale cada respuesta.</b> Al final de cada respuesta indica si viene de los materiales de clase, de una fuente externa académica o institucional, o si la ha generado la IA. En ese último caso avisa de que puede tener errores y hay que comprobarla.</li>
<li><b>Pensado para incluir.</b> Puede traducir, simplificar un texto, atender por voz desde el móvil o proponer retos a quien va más rápido.</li>
<li><b>Acceso controlado.</b> Se comparte por enlace en Google Classroom, con la cuenta educativa, y sin introducir datos personales del alumnado.</li>
</ol>"""),
        ("Cómo se hizo", """
<p>Primero, definir las necesidades y los objetivos. Después, preparar los materiales y configurar el GPT: contexto del centro y del grupo, funciones, niveles de acceso a la información y cuidado con las fuentes. Luego vinieron las pruebas simuladas. En ellas apareció el fallo más importante: cuando se le pedía una actividad, la resolvía. Se reconfiguró para que se negara a hacerlo, y también se reforzó que diera prioridad a los materiales de clase.</p>
<p>La propuesta se completa con lo que hace falta para llevarla al aula: un cuestionario inicial sobre lo que el alumnado sabe de la IA, una sesión sobre su uso ético, una reunión informativa con las familias, cinco actividades de ejemplo (de un mapa mental colaborativo sobre la Edad Media a un debate sobre el término «Reconquista») y un plan de evaluación con rúbricas, autoevaluación, portfolio y revisión de las conversaciones.</p>"""),
    ],
    gallery=[
        ("/assets/proyectos/tfm/guia-sin-resolver.png", "Se le pide que haga una actividad y responde que no puede hacerla, pero ofrece ayuda para completarla."),
        ("/assets/proyectos/tfm/fuente-archivos.png", "La respuesta indica que la información sale de los materiales de clase, en este caso de la Unidad 5."),
        ("/assets/proyectos/tfm/fuente-ia.png", "Cuando la información no está en los materiales, avisa de que la ha generado la IA y que hay que verificarla."),
        ("/assets/proyectos/tfm/correccion.png", "Repaso: el alumno responde y el asistente corrige los conceptos mal entendidos."),
    ],
    gallery_title="Cómo responde",
    value=["Detectar necesidades reales de un aula y convertirlas en objetivos.",
           "Diseñar una herramienta de IA con criterios pedagógicos (DUA, LOMLOE) y de protección de datos.",
           "Probar, encontrar fallos y corregirlos antes de llevarla al aula.",
           "Plantear cómo se evaluaría, también sus riesgos: dependencia tecnológica, sobrecarga de información y falta de formación docente."],
    note="Es una propuesta: no se ha probado con alumnado real, así que no hay resultados de aprendizaje que mostrar. Las capturas son de las pruebas que hice al configurar el asistente.",
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
    lede="Una inteligencia artificial ha escrito un texto sobre la caída de Málaga en 1937. Está bien redactado, suena convincente y tiene nueve errores. Ocho se cazan con el tema estudiado; el noveno, razonando.",
    meta=[("Nivel", "4.º ESO y 2.º Bachillerato"),
          ("Cuándo", "Al final de la unidad de la Guerra Civil, como repaso"),
          ("Duración", "Una sesión de 55 minutos, ampliable a dos"),
          ("Agrupamiento", "Parejas o grupos de 3")],
    links=[("Descargar la actividad (PDF)", "/assets/pdf/cazadores-de-bulos.pdf", "dl")],
    sections=[
        ("Por qué funciona", """
<p>Los errores no están escondidos en detalles de especialista: caen justo sobre lo que el alumnado acaba de estudiar. El mapa de julio de 1936, quién apoyó a cada bando, qué fueron las Brigadas Internacionales y dónde combatieron, la cronología de Madrid y Guernica. Quien ha seguido el tema los caza sin buscar nada. Quien no, descubre en veinte minutos qué no se sabía.</p>
<p>Por eso sirve a la vez para dos cosas: aprender a no fiarse de un texto solo porque suena bien, y repasar. Al corregir la hoja se ve de un vistazo qué contenidos han quedado flojos.</p>"""),
        ("Cómo se hace", """
<ol class="steps">
<li><b>Se reparte sin avisar (5 min).</b> Que lo lean como un texto cualquiera. Lo normal es que nadie sospeche.</li>
<li><b>Se destapa la trampa (5 min).</b> Lo ha escrito una IA y tiene nueve errores. No se dice cuáles.</li>
<li><b>A cazar en grupos (25 min).</b> Primero de memoria y después con el libro y el atlas. Un error solo cuenta si dicen dónde lo han comprobado.</li>
<li><b>Puesta en común (20 min).</b> Y la pregunta que importa: ¿cuál te habrías creído si nadie te avisa?</li>
</ol>
<p>Se puede ajustar: más fácil, diciendo cuántos errores hay en cada párrafo; más difícil, sin decir cuántos hay. Y en una sesión extra, cada grupo fabrica su propio texto falso para el grupo de al lado.</p>"""),
    ],
    value=["Diseñar una actividad que trabaja a la vez el contenido y la lectura crítica.",
           "Usar la IA como objeto de análisis, no como atajo."],
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
    lede="En las prácticas del Máster en Tecnología Educativa, como coordinador TIC en prácticas del Colegio Cerrado de Calderón (Málaga), creé un repositorio de herramientas digitales para todo el claustro. El centro lo presentó en el IX Congreso Internacional de Creatividad Educativa (Braining, Valencia, abril de 2025). En 2026 lo he revisado y rehecho para Secundaria.",
    meta=[("Para quién", "El claustro del centro (2024) y docentes de Secundaria (2026)"),
          ("Tipo", "Web de recursos y autoformación"),
          ("Herramientas", "Google Sites (2024) · web propia (2026)"),
          ("Reconocimiento", "Presentado por el centro en Braining 2025")],
    links=[("Abrir la caja de herramientas", "/herramientas/", "int"),
           ("Ver el repositorio original", "https://sites.google.com/view/repositorio-digital-docente-cc/inicio", "ext"),
           ("Noticia de Braining", "https://colegiocerradodecalderon.es/braining/", "ext")],
    sections=[
        ("La necesidad", """
<p>Hay cientos de herramientas digitales y muy poco tiempo para elegir. Un docente necesita saber rápido qué hace cada una, para qué edad sirve y cómo usarla en su materia, sin tener que probarlas todas.</p>"""),
        ("2024 · El repositorio del centro", """
<p>Una web organizada por etapas (Infantil, los tres ciclos de Primaria, Secundaria y Bachillerato por departamentos) y un área de apoyo al profesorado. Cada herramienta tiene su ficha con la función, la edad recomendada, ideas de uso en el aula y un tutorial en vídeo. El centro la usa como herramienta de autoformación.</p>"""),
        ("2026 · La caja de herramientas", """
<p>Dos años después muchas cosas habían cambiado, así que la he rehecho para Secundaria:</p>
<ul class="pl">
<li><b>Separada por quién la usa:</b> 64 herramientas para el aula, 34 para el trabajo del docente y 20 bancos de recursos.</li>
<li><b>Revisada una a una</b> en octubre de 2026, con un apartado para las que han cerrado o cambiado y su alternativa.</li>
<li><b>La IA que ya llega con la cuenta del centro</b> (Gemini, NotebookLM, Copilot) y cómo usarla con alumnado.</li>
<li><b>Criterios claros:</b> gratuita o con plan gratuito, edad mínima y autorización del centro.</li>
</ul>"""),
    ],
    value=["Seleccionar y organizar información para que otros docentes la usen.",
           "Mantener un recurso vivo: revisarlo, retirar lo que ya no sirve y explicar por qué."],
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
    lede="Una rúbrica en formulario para valorar un recurso digital con criterios comunes antes de llevarlo al aula: la calidad del contenido, la accesibilidad y el uso que se le puede dar en clase.",
    meta=[("Para quién", "Docentes que eligen recursos digitales"),
          ("Tipo", "Rúbrica en formulario"),
          ("Herramientas", "Jotform")],
    links=[("Abrir la rúbrica", "https://form.jotform.com/241185578598070", "ext")],
    sections=[],
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
    sections=[],
    value=["Documentar el propio aprendizaje y las evidencias de cada módulo."],
    related=["asistente-gpt-2eso", "repositorio-digital", "rubrica-materiales-digitales"],
))

FEATURED = ["consejo-de-clio", "repositorio-digital", "asistente-gpt-2eso", "cazadores-de-bulos"]

BY = {p["slug"]: p for p in P}
