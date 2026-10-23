// Graba el vídeo de una ficha de proyecto con la plantilla de vídeo del porfolio (norma en CLAUDE.md: la del Consejo de Clío):
// intro de 2 s, la fuente a pantalla completa con carteles en fichas centrados abajo y cierre de 2 s, unos 30 s.
// (El del Consejo tiene su propio script: _build/grabar_consejo_plantilla.js.)
// 1. Servir el repo en el 8000 (python -m http.server 8000) y, para el monasterio, la carpeta «El pasado próximo» en el 8020
//    (python -m http.server 8020 --bind 127.0.0.1: desde ahí se llega a didakora/agentes/monasterio/). Para el Repositorio y el e-Portfolio,
//    antes: node _build/capturar_sites.js _build/plantilla-video/capturas
// 2. PW=<ruta al paquete playwright> node _build/grabar_ficha.js <proyecto> <169|916> <carpeta de salida>
//    deja en la carpeta todo.mjpeg (los fotogramas).
// 3. 16:9 (web): ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i todo.mjpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -row-mt 1
//      -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -color_range tv -colorspace bt709 -an video.webm
//    9:16 (Instagram): ... -c:v libx264 -crf 20 -preset slow -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -movflags +faststart -an video.mp4
// 4. Póster: la miniatura de la plantilla (?p=<proyecto>&s=miniatura). Copiar a assets/proyectos/<proyecto>/ y subir el ?v= en data.py.
const { chromium } = require(process.env.PW);
const fs = require("fs"), path = require("path");
const [PROY, FMT, OUT] = [process.argv[2], process.argv[3] === "916" ? "916" : "169", process.argv[4]];
const [W, H] = FMT === "916" ? [1080, 1920] : [1280, 720];
// el monasterio necesita la carpeta «El pasado próximo» (8020); el resto, el repo servido en el 8000 (sus rutas /assets/…)
const BASE = PROY === "monasterio-didakora" ? "http://127.0.0.1:8020/pasadoproximo.github.io" : "http://localhost:8000";
const URL = `${BASE}/_build/plantilla-video/?f=${FMT}&p=${PROY}&grabar=1`;

// Guiones: qué se ve y qué dice cada cartel. Los textos salen de la ficha del proyecto (data.py), sin inventar nada.
let T_INI = Date.now();
// el monasterio marca su propio ritmo (cada monje trabaja 6 s en la recreación): esa parte se monta a ×1,5 para quedar en unos 30 s
const VELOCIDAD = { "monasterio-didakora": 1.5 };
const GUIONES = {
  // Recreación avisada con datos reales: el monasterio repite el ciclo 2026-10-21-3 sin lanzar ni escribir nada
  "monasterio-didakora": async ({ cap, wait, frame, tecla, page }) => {
    // elige una opción del diálogo por su texto; espera a que exista (las propuestas llegan según avanza el ciclo)
    const opcion = async t => {
      await frame.waitForFunction(t => { if (typeof dlg === "undefined" || !dlg.ops) return false;  // dlg es una variable del juego, no de window
        dlg.mostrado = dlg.texto.length; pintarDialogo(); return dlg.ops.some(o => o.t.startsWith(t)); }, t, { timeout: 15000 }).catch(async () => {
        const hay = await frame.evaluate(() => typeof dlg === "undefined" ? "sin diálogo" : JSON.stringify({ texto: String(dlg.texto || "").slice(0, 80), ops: (dlg.ops || []).map(o => o.t) }));
        throw new Error(`no llega la opción «${t}»; en pantalla: ${hay}`); });
      await frame.evaluate(t => elegir(dlg.ops.findIndex(o => o.t.startsWith(t))), t);
    };
    const ir = (x, y, d) => frame.evaluate(([x, y, d]) => window.__ir(x, y, d), [x, y, d]);
    const camara = (x, y) => frame.evaluate(([x, y]) => { window.__cam = x == null ? null : { x, y }; sucio = true; }, [x, y]);
    const corte = async fn => { await page.evaluate(() => window.__fundido(true)); await wait(280); await fn(); await wait(80); await page.evaluate(() => window.__fundido(false)); await wait(250); };
    await cap("1 · Toco la campana", "Empiezo un ciclo <b>desde el monasterio</b>"); await wait(900);
    await tecla("Space"); await wait(1300); await opcion("Tocar la campana"); await wait(700); await tecla("Escape");
    await corte(() => camara(5, 5)); await cap("Fray Gaspar · rastreador", "<b>Busca novedades</b> en las fuentes"); await wait(2600);
    await corte(() => camara(15.5, 5)); await cap("Fray Anselmo · coordinador", "Las cruza con el catálogo y <b>prepara propuestas</b>"); await wait(2800);
    await frame.waitForFunction(() => typeof D !== "undefined" && D.pendientes && D.pendientes.length > 0, null, { timeout: 20000 });  // las propuestas llegan solas
    await corte(async () => { await camara(null); await ir(18, 20, 2); }); await cap("2 · Sello los pergaminos", "<b>Apruebo, edito o rechazo</b> cada propuesta");
    await tecla("Space"); await wait(2200); await opcion("Aprobar A"); await wait(1200); await opcion("Siguiente pergamino"); await wait(1800); await opcion("Aprobar A"); await wait(800); await tecla("Escape");
    await corte(() => camara(3.5, 17)); await cap("3 · Ellos lo hacen", "Fray Bartolomé <b>cambia la web</b>"); await wait(2600);
    await corte(() => camara(27.5, 17.5)); await cap("3 · Y lo revisan", "Fray Custodio <b>lo revisa todo</b>, también en el móvil"); await wait(2800);
    await corte(async () => { await camara(null); await ir(27, 17, 0); });
    await tecla("KeyL"); await wait(600); await frame.click('.pestanas [data-p="ciclo"]'); await wait(800);
    await cap("4 · Yo publico", "En el Libro del Abad, <b>el antes y el después</b> de cada cambio");
    await frame.evaluate(() => new Promise(r => { const c = document.querySelector("#libro-c"), h = [...c.querySelectorAll("h3")].find(x => /cambiado/.test(x.textContent));
      const y1 = h ? h.offsetTop - 10 : 0, y0 = c.scrollTop, t0 = performance.now();
      const f = t => { const p = Math.min(1, (t - t0) / 1400), q = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2; c.scrollTop = y0 + (y1 - y0) * q; p < 1 ? requestAnimationFrame(f) : r(); };
      requestAnimationFrame(f); }));
    await wait(2600);
    await tecla("Escape"); await wait(200);
    await cap("Recreación con datos reales", "<b>Nada se publica sin mí</b>"); await wait(2000);
  },
  // Los cuatro comportamientos configurados y probados (los chats de su ficha)
  "asistente-gpt-2eso": async ({ cap, wait, sc }) => {
    const T = ["Guía, no resuelve", "Cita la unidad", "Avisa si es IA", "Corrige el repaso"];
    for (let i = 0; i < 4; i++) {
      await Promise.all([sc(`.beh-i:nth-of-type(${i + 1})`, 1200, 40), cap(`Comportamiento ${i + 1} de 4`, `<b>${T[i]}</b>`)]);
      await wait(4700);
    }
  },
  // El repositorio de 2024 en Google Sites: capturas reales de sus páginas
  "repositorio-digital": async ({ cap, wait, img, desl, page }) => {
    // la portada y las etapas se desplazan; las fichas van en planos fijos con su videotutorial cargado (Jorge, 23-10-2026)
    const plano = async (n, lab, txt) => { await page.evaluate(() => window.__fundido(true)); await wait(260); await img("plano" + n);
      await page.evaluate(() => window.__fundido(false)); await cap(lab, txt); await wait(4300); };
    await img(1); await cap("El repositorio de 2024", "Una web de recursos en Google Sites <b>para todo el claustro</b>"); await desl(800, 5000); await wait(400);
    await img(2); await cap("Por etapas y materias", "Infantil, Primaria y <b>Secundaria y Bachillerato</b>"); await desl(900, 4200); await wait(300);
    await plano(1, "Infantil · 5 años · Cokitos", "Cada herramienta con su ficha: <b>videotutorial, qué es y las áreas que trabaja</b>");
    await plano(2, "Primaria · 1.º ciclo · StopMotion", "El videotutorial de Rosa Liarte, <b>qué es y sus usos en el aula</b>");
    await plano(3, "Primaria · 2.º ciclo · Edpuzzle", "Con su videotutorial y <b>el botón a la herramienta</b>");
    await plano(4, "Apoyo docente · Magic School", "También herramientas <b>para el trabajo del docente</b>");
  },
  // Los cinco módulos del máster (textos de «Qué puedes ver en él»)
  "e-portfolio-master": async ({ cap, wait, img, desl }) => {
    await img(1); await cap("e-Portfolio del máster", "Los trabajos de los cinco módulos <b>y lo que aprendí</b>"); await desl(1100, 3000); await wait(600);
    const M = [["Módulos 1 y 4", "Diseño de materiales digitales"], ["Módulos 2 y 3", "Búsqueda y curación de información"],
               ["Módulo 3", "Trabajo colaborativo"], ["Módulos 1 y 4", "Diseño de materiales digitales"], ["Módulo 5", "Evaluación digital, <b>con Jotform, CoRubrics y SELFIE</b>"]];
    for (let i = 0; i < 5; i++) { await img(i + 2); await cap(M[i][0], M[i][1].includes("<b>") ? M[i][1] : `<b>${M[i][1]}</b>`); await desl(1600, 3400); await wait(500); }
  },
};

(async () => {
  if (!GUIONES[PROY]) throw new Error("no hay guion para " + PROY);
  const browser = await chromium.launch({ channel: "chrome" });
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, colorScheme: "light", reducedMotion: "no-preference" });
  const page = await ctx.newPage();
  const wait = ms => page.waitForTimeout(ms);
  await page.goto(URL, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  let frame = null;
  if (await page.$("iframe")) {
    const el = await page.$("iframe"); frame = await el.contentFrame(); await frame.waitForLoadState("load");
    if (PROY === "monasterio-didakora") {
      await frame.waitForFunction(() => document.getElementById("carga").classList.contains("oculto"));
      await page.focus("iframe"); await frame.focus("body").catch(() => {});
    }
  }
  const T = {
    page, frame, wait,
    cap: (l, t) => { if (l) console.log(((Date.now() - T_INI) / 1000).toFixed(1) + " s · " + l); return page.evaluate(([l, t]) => window.__cap(l, t), [l, t]); },
    sc: (sel, ms, arriba) => page.evaluate(([s, m, a]) => window.__scroll(s, m, a), [sel, ms, arriba]),
    img: n => page.evaluate(n => window.__img(n), n),
    desl: (y, ms) => page.evaluate(([y, m]) => window.__desliza(y, m), [y, ms]),
    tecla: async (k, ms = 60) => { await page.keyboard.down(k); await wait(ms); await page.keyboard.up(k); await wait(120); },
  };
  if (PROY === "monasterio-didakora") { await T.tecla("Enter"); await T.tecla("Enter"); await frame.evaluate(() => window.__ir(12, 14, 0)); }
  if (PROY === "repositorio-digital" || PROY === "e-portfolio-master") await T.img(1);
  await wait(800);

  T_INI = Date.now();
  const frames = [];
  const cdp = await ctx.newCDPSession(page);
  cdp.on("Page.screencastFrame", f => { frames.push({ t: f.metadata.timestamp, d: Buffer.from(f.data, "base64") }); cdp.send("Page.screencastFrameAck", { sessionId: f.sessionId }).catch(() => {}); });
  await cdp.send("Page.startScreencast", { format: "jpeg", quality: 90, maxWidth: W, maxHeight: H, everyNthFrame: 1 });
  const bar = (p, ms) => page.evaluate(([a, b]) => window.__bar(a, b), [p, ms]);
  // intro (2 s)
  await bar(6, 2000); await wait(2000);
  // la fuente con sus carteles; la barra avanza mientras
  const V = VELOCIDAD[PROY] || 1;
  await page.evaluate(() => window.__ir("cuerpo")); const T_CUERPO = Date.now() / 1000; await bar(94, 26000 * V); await wait(400);
  await GUIONES[PROY](T);
  await T.cap(null, null); await page.evaluate(() => document.querySelector(".rotulo").classList.add("off")); await wait(300);
  // cierre (2 s), con la barra en verde
  const T_CIERRE = Date.now() / 1000;
  await page.evaluate(() => window.__ir("cierre")); await bar(100, 400); await wait(2300);
  const TSTOP = Date.now() / 1000;  // Chrome solo manda fotogramas cuando algo cambia: el cierre quieto se alarga hasta aquí
  await cdp.send("Page.stopScreencast");
  await browser.close();
  fs.mkdirSync(OUT, { recursive: true });
  const fd = fs.openSync(path.join(OUT, "todo.mjpeg"), "w");
  frames.sort((a, b) => a.t - b.t);
  const t0 = frames[0].t, t1 = Math.max(frames[frames.length - 1].t, TSTOP);
  let j = 0, n = 0;
  for (let t = t0; t <= t1; t += (t >= T_CUERPO && t < T_CIERRE ? V : 1) / 30) { while (j + 1 < frames.length && frames[j + 1].t <= t) j++; fs.writeSync(fd, frames[j].d); n++; }
  fs.closeSync(fd);
  console.log(`${PROY} ${FMT}: ${n} fotogramas (${(n / 30).toFixed(1)} s) en ${OUT}`);
})();
