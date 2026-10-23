// Graba el vídeo del Consejo de Clío con la plantilla de vídeo del porfolio (brief 1.3): intro de 2 s, la sesión real
// dentro de una ficha con carteles en fichas (mismos textos que el vídeo anterior) y cierre de 2 s con «Lo que puedo afirmar».
// Es la SESIÓN REAL del 22-10-2026 (noticia de EFE sobre Ucrania, 1.º Bachillerato), en modo claro.
// 1. Servir el repo en el 8000: python -m http.server 8000
// 2. PW=<ruta al paquete playwright> node _build/grabar_consejo_plantilla.js <carpeta de salida> [169|916]
//    deja en la carpeta todo.mjpeg (los fotogramas) y poster.jpg.
// 3. 16:9 (web): ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i todo.mjpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -row-mt 1
//      -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -color_range tv -colorspace bt709 -an sesion-ucrania.webm
//    9:16 (Instagram): ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i todo.mjpeg -c:v libx264 -crf 20 -preset slow
//      -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -movflags +faststart -an consejo-de-clio-9x16.mp4
// 4. Copiar sesion-ucrania.webm y poster.jpg (como sesion-ucrania-poster.jpg) a assets/proyectos/consejo-de-clio/ y subir el ?v= en data.py.
const { chromium } = require(process.env.PW);
const fs = require("fs"), path = require("path");
const OUT = process.argv[2], F = process.argv[3] === "916" ? "916" : "169";
const [W, H] = F === "916" ? [1080, 1920] : [1280, 720];
const URL = `http://localhost:8000/_build/plantilla-video/?f=${F}&grabar=1`;

// carteles: [etiqueta, texto] (los textos, los del vídeo anterior; las etiquetas, los pasos de «Cómo funciona»)
const CARTELES = [
  ["1 · Pegas la noticia", "Una sesión real: noticia de EFE, <b>1.º Bachillerato</b>"],
  ["2 · Cada pensador hace su parte", "Seis pensadores <b>trabajan por turnos</b>"],
  ["2 · Cada pensador hace su parte", "Heródoto la resume y Tucídides <b>la sitúa en el temario</b>"],
  ["El error", "Arendt <b>iguala 1991 con hoy</b>"],
  ["3 · Ibn Jaldún revisa", "Ibn Jaldún <b>lo corrige</b>. En 1991 decidieron las repúblicas"],
  ["La versión final", "<b>Lista para contrastarla</b> y llevarla a clase"],
];

(async () => {
  const browser = await chromium.launch({ channel: "chrome" });
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, colorScheme: "light", reducedMotion: "no-preference" });
  const page = await ctx.newPage();
  const wait = ms => page.waitForTimeout(ms);
  const ir = s => page.evaluate(x => window.__ir(x), s);
  const bar = (p, ms) => page.evaluate(([a, b]) => window.__bar(a, b), [p, ms]);
  const cap = i => page.evaluate(([l, t]) => window.__cap(l, t), i === null ? [null, null] : CARTELES[i]);
  const sc = (sel, ms, arriba) => page.evaluate(([s, m, a]) => window.__scroll(s, m, a), [sel, ms, arriba]);
  await page.goto(URL, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.frameLocator("iframe").locator(".mesa").waitFor();
  await wait(800);

  const frames = [];
  const cdp = await ctx.newCDPSession(page);
  cdp.on("Page.screencastFrame", f => { frames.push({ t: f.metadata.timestamp, d: Buffer.from(f.data, "base64") }); cdp.send("Page.screencastFrameAck", { sessionId: f.sessionId }).catch(() => {}); });
  await cdp.send("Page.startScreencast", { format: "jpeg", quality: 90, maxWidth: W, maxHeight: H, everyNthFrame: 1 });
  const T0 = Date.now() / 1000;
  let tPoster = 0;
  const TOTAL = 31000;  // la barra avanza a lo largo de todo el vídeo

  // intro (2 s)
  await bar(100 * 2000 / TOTAL, 2000); await wait(2000);
  // la sesión
  await ir("cuerpo"); await bar(100 * 29000 / TOTAL, 27000); await wait(400);
  // el cartel cambia a la vez que empieza el desplazamiento
  const paso = (sel, ms, arriba, i) => Promise.all([sc(sel, ms, arriba), cap(i)]);
  await cap(0); await wait(2700);
  await paso(".mesa", 1300, 20, 1); await wait(2300);
  await paso('.turno[data-agent="herodoto"]', 1300, 30, 2); await wait(2300);
  await paso('.turno[data-agent="arendt"]', 1300, 30, 3); await wait(2900);
  await paso('.turno[data-agent="jaldun"]', 1500, 20, 4);
  tPoster = Date.now() / 1000 - T0 + 1.2;
  await wait(3900);
  await paso(".separador", 1500, 20, 5); await wait(2900);
  await cap(null); await page.evaluate(() => document.querySelector(".rotulo").classList.add("off")); await wait(300);
  // cierre (2 s), con la barra en verde
  await ir("cierre"); await bar(100, 400); await wait(2300);

  const TSTOP = Date.now() / 1000;  // Chrome solo manda fotogramas cuando algo cambia: el cierre quieto se alarga hasta aquí
  await cdp.send("Page.stopScreencast");
  await browser.close();
  // fotogramas a 30 fps constantes (se repite el último cuando la pantalla no cambia)
  fs.mkdirSync(OUT, { recursive: true });
  const fd = fs.openSync(path.join(OUT, "todo.mjpeg"), "w");
  const t0 = frames[0].t, t1 = Math.max(frames[frames.length - 1].t, TSTOP);
  let j = 0, n = 0;
  for (let t = t0; t <= t1; t += 1 / 30) {
    while (j + 1 < frames.length && frames[j + 1].t <= t) j++;
    fs.writeSync(fd, frames[j].d); n++;
    if (tPoster && Math.abs(t - (t0 + tPoster)) < 1 / 60) fs.writeFileSync(path.join(OUT, "poster.jpg"), frames[j].d);
  }
  fs.closeSync(fd);
  console.log(`${n} fotogramas (${(n / 30).toFixed(1)} s) en ${OUT}`);
})();
