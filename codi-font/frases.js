const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2]);
  const list = await p.evaluate(() => phrasesCa());
  fs.writeFileSync(process.argv[3], JSON.stringify(list, null, 1));
  console.log(list.length, 'phrases');
  await b.close();
})();
