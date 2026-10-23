// Capturas de página completa de las webs de Google Sites (no dejan incrustarse) para la plantilla de vídeo.
// PW=<ruta al paquete playwright> node _build/capturar_sites.js _build/plantilla-video/capturas   (fuera de git: se regeneran)
const { chromium } = require(process.env.PW);
const R = "https://sites.google.com/view/repositorio-digital-docente-cc/", E = "https://sites.google.com/view/e-portfolio-jorge/";
const OUT = process.argv[2];
// Repositorio: la 3 es Primaria · 1.º ciclo, con la ficha de StopMotion y el tutorial de Rosa Liarte (Jorge, 23-10-2026)
const PAG = { "repositorio-digital": [R + "inicio", R + "secundaria-y-bachillerato", R + "primaria/1-ciclo", R + "secundaria-y-bachillerato/sociales/generales"],
  "e-portfolio-master": [E + "inicio", E + "m%C3%B3dulo-1", E + "m%C3%B3dulo-2", E + "m%C3%B3dulo-3", E + "m%C3%B3dulo-4", E + "m%C3%B3dulo-5"] };
const fs = require("fs"), marcas = {};  // dónde empieza la ficha en la que se para el vídeo (px de la captura)
const MARCA = { "repositorio-digital-3": /^stop ?motion$/i };
(async () => { const b = await chromium.launch({ channel: "chrome" });
  for (const [f, w, k] of [["169", 1280, 1], ["916", 540, 2]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: k }); const p = await ctx.newPage();
    for (const [proy, urls] of Object.entries(PAG)) for (let i = 0; i < urls.length; i++) {
      await p.goto(urls[i], { waitUntil: "load", timeout: 60000 }).catch(() => {}); await p.waitForTimeout(3000);
      const ok = p.getByText("Entendido", { exact: false }); if (await ok.count()) await ok.first().click().catch(() => {});
      await p.evaluate(async () => { for (let y = 0; y < Math.min(document.documentElement.scrollHeight, 9000); y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); } window.scrollTo(0, 0); });
      await p.waitForTimeout(1200);
      const re0 = MARCA[`${proy}-${i + 1}`];
      if (re0) {  // YouTube solo carga el vídeo incrustado cuando está a la vista: ir a la ficha y esperar a que aparezca
        await p.evaluate(src => { const r = new RegExp(src, "i"); const h = [...document.querySelectorAll("h1")].find(e => r.test(e.textContent.trim())); if (h) h.scrollIntoView({ block: "start" }); }, re0.source);
        // el plano de la ficha: una captura de pantalla (no de página completa, donde el vídeo sale en blanco) del tamaño del vídeo
        await p.setViewportSize({ width: w, height: f === "169" ? 714 : 957 }); await p.waitForTimeout(6000);
        await p.screenshot({ path: `${OUT}/${proy}/${i + 1}b-${f}.jpg`, type: "jpeg", quality: 85 });
        await p.setViewportSize({ width: w, height: 900 }); await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(800);
      }
      const alto = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 8000));
      const re = MARCA[`${proy}-${i + 1}`];
      if (re) marcas[`${proy}/${i + 1}-${f}`] = k * await p.evaluate(src => { const r = new RegExp(src, "i"); const h = [...document.querySelectorAll("h1")].find(e => r.test(e.textContent.trim())); return h ? Math.round(h.getBoundingClientRect().top + scrollY) : 0; }, re.source);
      await p.screenshot({ path: `${OUT}/${proy}/${i + 1}-${f}.jpg`, type: "jpeg", quality: 82, clip: { x: 0, y: 0, width: w, height: alto }, fullPage: true });
      console.log(f, proy, i + 1, alto);
    }
    await ctx.close();
  }
  fs.writeFileSync(`${OUT}/marcas.json`, JSON.stringify(marcas, null, 1)); console.log("marcas", marcas);
  // Planos fijos de fichas del repositorio con su videotutorial cargado (YouTube solo se ve en una captura de pantalla
  // y con la ficha a la vista): sin desplazarse por ellas en el vídeo (Jorge, 23-10-2026)
  const PLANOS = [[R + "infantil/5-a%C3%B1os", /^cokitos$/i], [R + "primaria/1-ciclo", /^stop ?motion$/i],
                  [R + "primaria/2-ciclo", /^edpuzzle$/i], [R + "apoyo-docente", /^magic ?school/i]];
  for (const [f, w, k] of [["169", 1280, 1], ["916", 540, 2]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: f === "169" ? 714 : 957 }, deviceScaleFactor: k }); const p = await ctx.newPage();
    for (let i = 0; i < PLANOS.length; i++) {
      const [u, re] = PLANOS[i];
      await p.goto(u, { waitUntil: "load", timeout: 60000 }).catch(() => {}); await p.waitForTimeout(2500);
      const ok = p.getByText("Entendido", { exact: false }); if (await ok.count()) await ok.first().click().catch(() => {});
      const hay = await p.evaluate(src => { const r = new RegExp(src, "i"); const h = [...document.querySelectorAll("h2")].find(e => r.test(e.textContent.trim()));
        if (!h) return false; h.scrollIntoView({ block: "start" }); window.scrollBy(0, -64); return true; }, re.source);
      if (!hay) { console.log("no encuentro", re, "en", u); continue; }
      await p.waitForTimeout(7000);
      await p.screenshot({ path: `${OUT}/repositorio-digital/plano${i + 1}-${f}.jpg`, type: "jpeg", quality: 85 });
      console.log(f, "plano", i + 1, re);
    }
    await ctx.close();
  }
  await b.close(); })();
