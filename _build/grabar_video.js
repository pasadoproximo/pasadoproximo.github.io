// Graba el vídeo de Didákora para el Repositorio digital del portfolio (1264 × 712, 30 fps, en bucle).
// Recorrido: portada → busca «repasar» → filtra por Primaria → ficha de Kahoot! → alternativas → logo → portada.
// 1. Servir la carpeta «El pasado próximo» en el 8020 (python -m http.server 8020).
// 2. PW=<ruta al paquete playwright> node _build/grabar_video.js <carpeta de salida> <didakora/marca/didakora-apilado-cielo.svg>
//    deja en la carpeta todo.mjpeg (los fotogramas) y poster.jpg.
// 3. ffmpeg -f image2pipe -framerate 30 -c:v mjpeg -i todo.mjpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -row-mt 1 -pix_fmt yuv420p -an didakora.webm
// 4. Copiar didakora.webm y poster.jpg (como didakora-video.jpg) a assets/proyectos/repositorio-digital/ y subir el ?v= en data.py.
const { chromium } = require(process.env.PW);
const fs = require("fs"), path = require("path");
const OUT = process.argv[2];
const W = 1264, H = 712, BASE = "http://127.0.0.1:8020/didakora";
let LOGO = fs.readFileSync(process.argv[3], "utf8").replace(/<title>.*?<\/title>/, "");
{ const i = LOGO.indexOf(">", LOGO.indexOf("<g ")) + 1, j = LOGO.indexOf("</g>", i);
  LOGO = LOGO.slice(0, i) + '<g class="caja">' + LOGO.slice(i, j) + "</g>" + LOGO.slice(j); }

// se inyecta en cada página: rótulo, cursor y pantalla final; el estado pasa de una página a otra por sessionStorage
const INIT = `(() => {
  const LOGO = ${JSON.stringify(LOGO)};
  const st = () => { try { return JSON.parse(sessionStorage.rec || "{}"); } catch (e) { return {}; } };
  const save = o => { sessionStorage.rec = JSON.stringify(Object.assign(st(), o)); };
  document.addEventListener("DOMContentLoaded", () => {
    const s = st();
    const css = document.createElement("style");
    css.textContent = \`
      html{scrollbar-width:none}::-webkit-scrollbar{display:none}
      #rc{position:fixed;left:50%;bottom:26px;z-index:9997;transform:translate(-50%,0);background:#061033;color:#fff;
        font:800 25px/1 var(--f-disp),sans-serif;letter-spacing:-.02em;padding:18px 28px;border-radius:999px;white-space:nowrap;
        box-shadow:0 14px 34px rgba(6,16,51,.28);transition:opacity .35s ease,transform .35s ease;pointer-events:none}
      #rc b{color:#FF8A6B;font-weight:800}
      #rc.off{opacity:0;transform:translate(-50%,14px)}
      #rcur{position:fixed;left:0;top:0;z-index:9999;width:22px;height:22px;pointer-events:none;will-change:transform}
      #rend{position:fixed;inset:0;z-index:9998;background:#9FB3FF;overflow:hidden;display:flex;flex-direction:column;
        align-items:center;justify-content:center;transition:opacity .6s ease;color:#061033;pointer-events:none}
      #rend.off{opacity:0}
      #rend::before{content:"";position:absolute;width:420px;height:420px;border-radius:50%;background:#FF8A6B;right:-120px;top:-160px}
      #rend::after{content:"";position:absolute;width:240px;height:240px;border-radius:50%;border:30px solid rgba(255,255,255,.55);left:-60px;bottom:-150px}
      #rend svg{width:414px;height:auto;display:block}
      #rend p{font:500 24px/1.3 var(--f-body),sans-serif;margin:30px 0 0}
      #rend.tap .caja{animation:dk-salto .55s cubic-bezier(.3,.7,.4,1)}
      #rend.tap .caja>path:nth-child(1){animation:dk-sol-i .55s ease-in-out}
      #rend.tap .caja>path:nth-child(2){animation:dk-sol-d .55s ease-in-out}\`;
    document.head.appendChild(css);
    const c = document.createElement("div"); c.id = "rc"; c.innerHTML = s.cap || ""; if (!s.cap) c.className = "off";
    const e = document.createElement("div"); e.id = "rend"; e.innerHTML = LOGO + "<p>Herramientas digitales para docentes, revisadas una a una</p>";
    if (!s.end) e.className = "off";
    const k = document.createElement("div"); k.id = "rcur";
    k.innerHTML = '<svg viewBox="0 0 22 22"><path d="M3 2v16l4.2-4 2.9 6.6 2.7-1.2-2.9-6.4H16z" fill="#111" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg>';
    const put = (x, y) => { k.style.transform = "translate(" + (x - 3) + "px," + (y - 2) + "px)"; };
    put(s.x ?? 905, s.y ?? 205);
    document.body.append(c, e, k);
    addEventListener("mousemove", ev => { put(ev.clientX, ev.clientY); save({ x: ev.clientX, y: ev.clientY }); }, true);
    window.__cap = html => new Promise(r => {
      save({ cap: html });
      if (!c.classList.contains("off")) { c.classList.add("off"); setTimeout(() => { if (html) { c.innerHTML = html; c.classList.remove("off"); } r(); }, 380); }
      else { if (html) { c.innerHTML = html; c.classList.remove("off"); } r(); }
    });
    window.__end = on => { save({ end: on }); e.classList.toggle("off", !on); e.classList.remove("tap"); };
    window.__tap = () => { e.classList.remove("tap"); void e.offsetWidth; e.classList.add("tap"); };
    window.__scroll = (to, ms) => new Promise(r => {
      const y0 = scrollY, t0 = performance.now();
      const f = t => { const p = Math.min(1, (t - t0) / ms), q = p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
        scrollTo(0, y0 + (to - y0) * q); p < 1 ? requestAnimationFrame(f) : r(); };
      requestAnimationFrame(f);
    });
  });
})();`;

(async () => {
  const browser = await chromium.launch({ channel: "chrome" });
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, reducedMotion: "no-preference" });
  await ctx.addInitScript(INIT);
  const page = await ctx.newPage();
  const wait = ms => page.waitForTimeout(ms);
  let mx = 905, my = 205;
  const move = async (x, y, ms = 800) => {
    const x0 = mx, y0 = my, t0 = Date.now();
    for (;;) {
      const p = Math.min(1, (Date.now() - t0) / ms), q = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      await page.mouse.move(x0 + (x - x0) * q, y0 + (y - y0) * q);
      if (p >= 1) break; await wait(8);
    }
    mx = x; my = y;
  };
  const center = async sel => { const b = await page.locator(sel).first().boundingBox(); return [b.x + b.width / 2, b.y + b.height / 2]; };
  const cap = html => page.evaluate(h => window.__cap(h), html);

  await page.goto(BASE + "/", { waitUntil: "networkidle" });
  await page.evaluate(() => { sessionStorage.rec = JSON.stringify({ x: 905, y: 205 }); });
  await page.reload({ waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.mouse.move(mx, my); await wait(800);

  // grabación: fotogramas del navegador con su hora
  const frames = [];
  const cdp = await ctx.newCDPSession(page);
  cdp.on("Page.screencastFrame", f => { frames.push({ t: f.metadata.timestamp, d: Buffer.from(f.data, "base64") }); cdp.send("Page.screencastFrameAck", { sessionId: f.sessionId }).catch(() => {}); });
  await cdp.send("Page.startScreencast", { format: "jpeg", quality: 92, maxWidth: W, maxHeight: H, everyNthFrame: 1 });
  const T0 = Date.now() / 1000;

  // 1 · portada
  await wait(700);
  await cap("<b>117</b> herramientas digitales, revisadas para tu clase");
  await wait(1900);
  // 2 · busca
  let [x, y] = await center("#hq");
  await move(x - 160, y, 900); await page.mouse.click(mx, my);
  await cap("Busca por <b>lo que quieres hacer</b>");
  await wait(300);
  await page.keyboard.type("repasar", { delay: 130 });
  await wait(700);
  [x, y] = await center(".hs button[type=submit]");
  await move(x, y, 650); await wait(200);
  await page.evaluate(() => { const s = JSON.parse(sessionStorage.rec); s.cap = "Busca por <b>lo que quieres hacer</b>"; sessionStorage.rec = JSON.stringify(s); });
  await Promise.all([page.waitForURL(/todas/), page.mouse.click(mx, my)]);
  await page.waitForLoadState("load"); await page.evaluate(() => document.fonts.ready);
  // 3 · resultados
  await wait(400);
  await cap("Resultados <b>al momento</b>, ordenados por relevancia");
  await wait(1800);
  // 4 · etapa
  [x, y] = await center("#lnv .dd-b");
  await move(x, y, 800); await wait(150);
  await page.mouse.click(mx, my);
  await cap("Filtra por <b>etapa</b>");
  await wait(600);
  [x, y] = await center('#lnv [data-v="P"]');
  await move(x, y, 500); await wait(250);
  await page.mouse.click(mx, my);
  await wait(1200);
  await page.evaluate(() => window.__scroll(330, 900)); await wait(400);
  // 5 · ficha
  [x, y] = await center("#lgrid .tc-a");
  await move(x, y, 800); await wait(500);
  await page.evaluate(() => { const s = JSON.parse(sessionStorage.rec); s.cap = "Filtra por <b>etapa</b>"; sessionStorage.rec = JSON.stringify(s); });
  await Promise.all([page.waitForURL(/kahoot/), page.mouse.click(mx, my)]);
  await page.waitForLoadState("load"); await page.evaluate(() => document.fonts.ready);
  await wait(300);
  await cap("Cada herramienta, <b>explicada en su ficha</b>");
  await wait(1800);
  [x, y] = await center(".fq p");
  await move(x + 120, y, 900);
  await cap("<b>Qué es</b>, para qué usarla y qué necesita");
  await wait(900);
  [x, y] = await center(".fa dl");
  await move(x, y, 900); await wait(900);
  // 6 · alternativas
  const ya = await page.evaluate(() => document.getElementById("h-alt").getBoundingClientRect().top + scrollY - 110);
  await page.evaluate(([to]) => window.__scroll(to, 1300), [ya]);
  await cap("Y <b>alternativas</b> para comparar");
  [x, y] = await center(".alt .tcg .tc-a");
  await move(x, y, 900);
  await wait(1800);
  // 7 · cierre con el logo y vuelta a la portada (para que el bucle empiece donde acaba)
  await cap("");
  await page.evaluate(() => window.__end(true));
  await move(905, 205, 700);
  await page.evaluate(() => window.__tap());
  await wait(2900);
  await page.goto(BASE + "/", { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await wait(500);
  await page.evaluate(() => window.__end(false));
  await wait(1300);

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
    if (Math.abs(t - (t0 + 2.6)) < 1 / 60) fs.writeFileSync(path.join(OUT, "poster.jpg"), frames[j].d);
  }
  fs.closeSync(fd);
  console.log("fotogramas:", frames.length, "→", n, "a 30 fps =", (n / 30).toFixed(1), "s");
})();
