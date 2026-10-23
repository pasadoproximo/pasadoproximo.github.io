// Graba el vídeo del Consejo de Clío para su página de proyecto (1280 × 720, 30 fps, unos 30 s, en bucle).
// Es una SESIÓN REAL: la del 22-10-2026 con la noticia de EFE sobre las negociaciones de Ucrania, para 1.º Bachillerato.
// Se reproduce con el propio artefacto del Consejo, en el que la «sesión de ejemplo» se sustituye por los textos de esa
// sesión copiados tal cual (sin llamar a Claude). Recorrido: la noticia → los seis pensadores → Heródoto y Tucídides →
// Arendt iguala 1991 con hoy → Ibn Jaldún lo corrige → la versión final.
// 1. Servir _build/consejo-sesion/ (el artefacto con la sesión real; pdf.html es la versión para el PDF) en el 8030:
//    python -m http.server 8030 --directory _build/consejo-sesion   ·   PDF: chrome --headless --no-pdf-header-footer
//    --print-to-pdf=assets/pdf/consejo-de-clio-sesion-ucrania.pdf http://localhost:8030/pdf.html
// 2. PW=<ruta al paquete playwright> node _build/grabar_consejo.js <carpeta de salida> [url]
//    deja en la carpeta todo.mjpeg (los fotogramas) y poster.jpg.
// 3. ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i todo.mjpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -row-mt 1 -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -color_range tv -colorspace bt709 -an sesion.webm
//    (rango «tv»: con el rango completo del JPEG, Chrome no lo decodifica)
// 4. Copiar sesion.webm y poster.jpg (como sesion-poster.jpg) a assets/proyectos/consejo-de-clio/ y subir el ?v= en data.py.
const { chromium } = require(process.env.PW);
const fs = require("fs"), path = require("path");
const OUT = process.argv[2], URL = process.argv[3] || "http://localhost:8030/";
const W = 1280, H = 720;

// rótulo abajo, como en el vídeo del monasterio
const INIT = `document.addEventListener("DOMContentLoaded", () => {
  const css = document.createElement("style");
  css.textContent = "#rc{position:fixed;left:50%;bottom:34px;z-index:9997;transform:translate(-50%,0);background:#061033;color:#fff;" +
    "font:800 24px/1.15 'Bricolage Grotesque',sans-serif;letter-spacing:-.02em;padding:16px 26px;border-radius:999px;white-space:nowrap;" +
    "box-shadow:0 14px 34px rgba(0,0,0,.45);transition:opacity .35s ease,transform .35s ease;pointer-events:none}" +
    "#rc b{color:#9FB3FF}#rc.off{opacity:0;transform:translate(-50%,14px)}html{scroll-behavior:auto!important}";
  document.head.appendChild(css);
  const l = document.createElement("link"); l.rel = "stylesheet";
  l.href = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&display=swap"; document.head.appendChild(l);
  const c = document.createElement("div"); c.id = "rc"; c.className = "off"; document.body.append(c);
  window.__cap = html => new Promise(r => {
    const show = () => { if (html) { c.innerHTML = html; c.classList.remove("off"); } r(); };
    if (!c.classList.contains("off")) { c.classList.add("off"); setTimeout(show, 380); } else show();
  });
  // desplazamiento suave hasta un elemento (con su margen arriba), en ms
  window.__ir = (sel, ms, arriba = 90, n = 0) => new Promise(r => {
    const el = typeof sel === "number" ? null : document.querySelectorAll(sel)[n];
    const y0 = scrollY, y1 = Math.max(0, Math.min(document.documentElement.scrollHeight - innerHeight,
      el ? el.getBoundingClientRect().top + scrollY - arriba : sel));
    const t0 = performance.now(), ease = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    const paso = now => { const t = Math.min(1, (now - t0) / ms); scrollTo(0, y0 + (y1 - y0) * ease(t)); t < 1 ? requestAnimationFrame(paso) : r(); };
    requestAnimationFrame(paso);
  });
});`;

(async () => {
  const browser = await chromium.launch({ channel: "chrome" });
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, colorScheme: "dark", reducedMotion: "no-preference" });
  await ctx.addInitScript(INIT);
  const page = await ctx.newPage();
  const wait = ms => page.waitForTimeout(ms);
  const cap = html => page.evaluate(h => window.__cap(h), html);
  const ir = (sel, ms, arriba, n) => page.evaluate(([s, m, a, i]) => window.__ir(s, m, a, i), [sel, ms, arriba, n]);
  await page.goto(URL, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await wait(600);

  const frames = [];
  const cdp = await ctx.newCDPSession(page);
  cdp.on("Page.screencastFrame", f => { frames.push({ t: f.metadata.timestamp, d: Buffer.from(f.data, "base64") }); cdp.send("Page.screencastFrameAck", { sessionId: f.sessionId }).catch(() => {}); });
  await cdp.send("Page.startScreencast", { format: "jpeg", quality: 90, maxWidth: W, maxHeight: H, everyNthFrame: 1 });
  const T0 = Date.now() / 1000;
  let tPoster = 0;

  // 1 · la noticia
  await cap("Una sesión real: noticia de EFE, <b>1.º Bachillerato</b>");
  await wait(3200);
  // 2 · los seis pensadores
  await ir(".mesa", 1400, 40);
  await cap("Seis pensadores <b>trabajan por turnos</b>");
  await wait(2800);
  // 3 · Heródoto y Tucídides
  await ir('.turno[data-agent="herodoto"]', 1400, 60);
  await cap("Heródoto la resume y Tucídides <b>la sitúa en el temario</b>");
  await wait(2600);
  // 4 · Arendt iguala 1991 con hoy
  await ir('.turno[data-agent="arendt"]', 1400, 60);
  await cap("Arendt <b>iguala 1991 con hoy</b>");
  await wait(3400);
  // 5 · Ibn Jaldún lo corrige
  await ir('.turno[data-agent="jaldun"]', 1600, 40);
  await cap("Ibn Jaldún <b>lo corrige</b>. En 1991 decidieron las repúblicas");
  tPoster = Date.now() / 1000 - T0 + 1.2;
  await wait(4600);
  // 6 · la versión final
  await ir(".separador", 1600, 30);
  await cap("La versión final, <b>lista para contrastarla</b> y llevarla a clase");
  await wait(4200);
  await cap(null); await page.evaluate(() => document.getElementById("rc").classList.add("off"));
  await ir(0, 1400);
  await wait(500);

  await cdp.send("Page.stopScreencast");
  await browser.close();
  // fotogramas a 30 fps constantes (se repite el último cuando la pantalla no cambia)
  fs.mkdirSync(OUT, { recursive: true });
  const fd = fs.openSync(path.join(OUT, "todo.mjpeg"), "w");
  const t0 = frames[0].t, t1 = frames[frames.length - 1].t;
  let j = 0, n = 0;
  for (let t = t0; t <= t1; t += 1 / 30) {
    while (j + 1 < frames.length && frames[j + 1].t <= t) j++;
    fs.writeSync(fd, frames[j].d); n++;
    if (tPoster && Math.abs(t - (t0 + tPoster)) < 1 / 60) fs.writeFileSync(path.join(OUT, "poster.jpg"), frames[j].d);
  }
  fs.closeSync(fd);
  console.log(`${n} fotogramas (${(n / 30).toFixed(1)} s)`);
})();
