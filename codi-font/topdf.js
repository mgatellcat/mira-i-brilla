const { chromium } = require('playwright');
(async () => {
  const [src, pdf, png] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + src, { waitUntil: 'networkidle' }).catch(() => p.goto('file://' + src));
  await p.waitForTimeout(800);
  await p.pdf({ path: pdf, format: 'A4', landscape: true, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close();
  console.log('pdf ok');
})();
