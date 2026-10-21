// Graba el vídeo del monasterio de Didákora para su página de proyecto (1264 × 712, 30 fps, en bucle).
// Es una RECREACIÓN avisada: el monasterio se abre con ?demo=<ciclo> y repite ese ciclo con sus datos reales (hallazgos,
// propuestas, decisiones, cambios y capturas) sin lanzar Claude Code ni escribir nada. El rótulo final y la barra lo dicen.
// Recorrido: la campana → los monjes trabajando (un vistazo a cada sala) → Fray Gaspar cuenta lo que encontró → apruebo en el tablón
// → Fray Bartolomé y Fray Custodio trabajando → Fray Custodio enseña su revisión → Libro del Abad: el antes y el después.
// 1. Arrancar el monasterio (/monasterio en Claude Code, desde didakora): sirve «El pasado próximo» en el 8020.
// 2. PW=<ruta al paquete playwright> node _build/grabar_monasterio.js <carpeta de salida> [ciclo]   (por defecto 2026-10-21-3)
//    deja en la carpeta todo.mjpeg (los fotogramas) y poster.jpg.
// 3. ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i todo.mjpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -row-mt 1 -pix_fmt yuv420p -an monasterio.webm
//    (sirve el ffmpeg que trae Playwright: ms-playwright/ffmpeg-*/ffmpeg-win64.exe)
// 4. Copiar monasterio.webm y poster.jpg (como monasterio-video.jpg) a assets/proyectos/monasterio-didakora/ y subir el ?v= en data.py.
const { chromium } = require(process.env.PW);
const fs = require("fs"), path = require("path");
const OUT = process.argv[2], CICLO = process.argv[3] || "2026-10-21-3";
const W = 1264, H = 712, URL = `http://127.0.0.1:8020/didakora/agentes/monasterio/?demo=${CICLO}`;

// rótulo arriba y fundido para los cambios de escena
const INIT = `document.addEventListener("DOMContentLoaded", () => {
  const css = document.createElement("style");
  css.textContent = "#rc{position:fixed;left:50%;top:84px;z-index:9997;transform:translate(-50%,0);background:#061033;color:#fff;" +
    "font:800 25px/1 'Bricolage Grotesque',sans-serif;letter-spacing:-.02em;padding:18px 28px;border-radius:999px;white-space:nowrap;" +
    "box-shadow:0 14px 34px rgba(6,16,51,.35);transition:opacity .35s ease,transform .35s ease;pointer-events:none}" +
    "#rc b{color:#FF8A6B}#rc.off{opacity:0;transform:translate(-50%,-14px)}" +
    "#fd{position:fixed;inset:0;background:#05081a;z-index:9996;opacity:0;transition:opacity .25s ease;pointer-events:none}#fd.on{opacity:1}";
  document.head.appendChild(css);
  const c = document.createElement("div"); c.id = "rc"; c.className = "off";
  const f = document.createElement("div"); f.id = "fd"; document.body.append(f, c);
  window.__cap = html => new Promise(r => {
    const show = () => { if (html) { c.innerHTML = html; c.classList.remove("off"); } r(); };
    if (!c.classList.contains("off")) { c.classList.add("off"); setTimeout(show, 380); } else show();
  });
});`;

(async () => {
  const browser = await chromium.launch({ channel: "chrome" });
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, reducedMotion: "no-preference" });
  await ctx.addInitScript(INIT);
  const page = await ctx.newPage();
  const wait = ms => page.waitForTimeout(ms);
  const cap = html => page.evaluate(h => window.__cap(h), html);
  const tecla = async (k, ms = 60) => { await page.keyboard.down(k); await wait(ms); await page.keyboard.up(k); await wait(120); };
  // pasa una página del diálogo o elige una opción por su texto (con teclas, una pulsación de más se salta pasos)
  const opcion = texto => page.evaluate(t => { dlg.mostrado = dlg.texto.length; pintarDialogo(); const i = dlg.ops.findIndex(o => o.t.startsWith(t)); if (i < 0) throw new Error("no hay opción " + t); elegir(i); }, texto);
  const vista = general => page.evaluate(g => window.__vista(g), general);
  const corte = async (fn) => { await page.evaluate(() => document.getElementById("fd").classList.add("on")); await wait(280); await fn(); await wait(80); await page.evaluate(() => document.getElementById("fd").classList.remove("on")); await wait(250); };
  const ir = (x, y, d) => page.evaluate(([x, y, d]) => window.__ir(x, y, d), [x, y, d]);
  // cámara fija en el centro de una sala (null: vuelve a seguir al abad)
  const camara = (x, y) => page.evaluate(([x, y]) => { window.__cam = x == null ? null : { x, y }; sucio = true; }, [x, y]);
  await page.goto(URL, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => document.getElementById("carga").classList.contains("oculto"));
  await tecla("Enter"); await tecla("Enter"); // cierra la bienvenida antes de grabar
  await ir(12, 14, 0); await wait(600);
  // grabación: fotogramas del navegador con su hora
  const frames = [];
  const cdp = await ctx.newCDPSession(page);
  cdp.on("Page.screencastFrame", f => { frames.push({ t: f.metadata.timestamp, d: Buffer.from(f.data, "base64") }); cdp.send("Page.screencastFrameAck", { sessionId: f.sessionId }).catch(() => {}); });
  await cdp.send("Page.startScreencast", { format: "jpeg", quality: 90, maxWidth: W, maxHeight: H, everyNthFrame: 1 });
  const T0 = Date.now() / 1000;
  // 1 · la campana
  await cap("Toco la campana para <b>empezar un ciclo</b>");
  await wait(1200);
  await tecla("Space"); await wait(1600);
  await opcion("Tocar la campana"); await wait(900);
  await tecla("Escape");
  // 2 · los monjes trabajando: un vistazo a cada sala (el abad mira desde un rincón que no les corta el paso)
  await corte(() => camara(5, 5));
  await cap("Fray Gaspar <b>busca novedades</b> en las fuentes");
  await wait(3600);
  await corte(() => camara(15.5, 5));
  await cap("Fray Anselmo las cruza con el catálogo y <b>prepara propuestas</b>");
  await wait(5200);
  // 3 · lo que trae Fray Gaspar
  await corte(async () => { await camara(null); await ir(3, 8, 0); });
  await cap("Cada monje <b>me cuenta lo que ha hecho</b>");
  await tecla("Space"); await wait(2800);
  await opcion("Siguiente"); await wait(2600);
  await tecla("Escape");
  // 4 · apruebo en el tablón
  await corte(() => ir(18, 20, 2));
  await cap("Apruebo cada propuesta <b>desde el tablón</b>");
  await tecla("Space"); await wait(3000);
  await opcion("Aprobar A"); await wait(1500);
  await opcion("Siguiente pergamino"); await wait(2600);
  await opcion("Aprobar A"); await wait(1200);
  await tecla("Escape");
  // 5 · Fray Bartolomé cambia la web y Fray Custodio la revisa
  await corte(() => camara(3.5, 17));
  await cap("Fray Bartolomé <b>cambia la web</b>");
  await wait(4600);
  await corte(() => camara(27.5, 17.5));
  await cap("Y Fray Custodio <b>lo revisa todo</b>");
  await wait(5800);
  // 6 · la revisión de Fray Custodio
  await corte(async () => { await camara(null); await ir(27, 17, 0); });
  await cap("Fray Custodio comprueba todo, <b>también en el móvil</b>");
  await tecla("Space"); await wait(2600);
  await opcion("Siguiente"); await wait(2000);
  await opcion("Siguiente"); await wait(2800);
  await tecla("Escape"); await wait(200);
  // 7 · el Libro del Abad: el antes y el después
  await tecla("KeyL"); await wait(700);
  await page.click('.pestanas [data-p="ciclo"]'); await wait(1200);
  await cap("Y en el Libro, <b>el antes y el después</b> de cada cambio");
  await page.evaluate(() => new Promise(r => { const c = document.querySelector("#libro-c"), h = [...c.querySelectorAll("h3")].find(x => /cambiado/.test(x.textContent));
    const y1 = h ? h.offsetTop - 10 : 0, y0 = c.scrollTop, t0 = performance.now();
    const f = t => { const p = Math.min(1, (t - t0) / 1400), q = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2; c.scrollTop = y0 + (y1 - y0) * q; p < 1 ? requestAnimationFrame(f) : r(); };
    requestAnimationFrame(f); }));
  await wait(3800);
  await tecla("Escape"); await wait(200);
  await cap("Recreación con datos reales · <b>nada se publica sin mí</b>");
  await wait(2800);
  await cap(""); await wait(600);
  await cdp.send("Page.stopScreencast");
  const T1 = Date.now() / 1000;
  await browser.close();
  // a 30 fotogramas por segundo: en cada instante, el último fotograma que había llegado
  frames.sort((a, b) => a.t - b.t);
  const t0 = Math.max(frames[0].t, T0), t1 = Math.min(T1, frames[frames.length - 1].t + 1);
  const fd = fs.openSync(path.join(OUT, "todo.mjpeg"), "w");
  let j = 0, n = 0;
  for (let t = t0; t < t1; t += 1 / 30) {
    while (j + 1 < frames.length && frames[j + 1].t <= t) j++;
    fs.writeSync(fd, frames[j].d); n++;
    if (Math.abs(t - (t0 + 6.5)) < 1 / 60) fs.writeFileSync(path.join(OUT, "poster.jpg"), frames[j].d);
  }
  fs.closeSync(fd);
  console.log("fotogramas:", frames.length, "→", n, "a 30 fps =", (n / 30).toFixed(1), "s");
})();
