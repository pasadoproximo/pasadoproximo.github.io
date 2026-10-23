// Capturas de página completa de las webs de Google Sites (no dejan incrustarse) para la plantilla de vídeo.
// PW=<ruta al paquete playwright> node _build/capturar_sites.js _build/plantilla-video/capturas   (fuera de git: se regeneran)
const { chromium } = require(process.env.PW);
const R = "https://sites.google.com/view/repositorio-digital-docente-cc/", E = "https://sites.google.com/view/e-portfolio-jorge/";
const OUT = process.argv[2];
const PAG = { "repositorio-digital": [R + "inicio", R + "secundaria-y-bachillerato", R + "infantil/5-a%C3%B1os", R + "secundaria-y-bachillerato/sociales/generales"],
  "e-portfolio-master": [E + "inicio", E + "m%C3%B3dulo-1", E + "m%C3%B3dulo-2", E + "m%C3%B3dulo-3", E + "m%C3%B3dulo-4", E + "m%C3%B3dulo-5"] };
(async () => { const b = await chromium.launch({ channel: "chrome" });
  for (const [f, w, k] of [["169", 1280, 1], ["916", 540, 2]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: k }); const p = await ctx.newPage();
    for (const [proy, urls] of Object.entries(PAG)) for (let i = 0; i < urls.length; i++) {
      await p.goto(urls[i], { waitUntil: "load", timeout: 60000 }).catch(() => {}); await p.waitForTimeout(3000);
      const ok = p.getByText("Entendido", { exact: false }); if (await ok.count()) await ok.first().click().catch(() => {});
      await p.evaluate(async () => { for (let y = 0; y < Math.min(document.documentElement.scrollHeight, 9000); y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); } window.scrollTo(0, 0); });
      await p.waitForTimeout(1200);
      const alto = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 8000));
      await p.screenshot({ path: `${OUT}/${proy}/${i + 1}-${f}.jpg`, type: "jpeg", quality: 82, clip: { x: 0, y: 0, width: w, height: alto }, fullPage: true });
      console.log(f, proy, i + 1, alto);
    }
    await ctx.close();
  }
  await b.close(); })();
