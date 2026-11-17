// Static PNG export only. Uses the preinstalled runtime's Sharp; no video/timing code.
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '../..');
(async () => {
  for (const name of ['CHARACTER_SHEET','HERO_01','HERO_02','HERO_03']) {
    await sharp(path.join(__dirname,name+'.svg')).png().toFile(path.join(root,name+'.png'));
  }
  for (const file of fs.readdirSync(__dirname).filter(f=>/^(HOST_|PROP_|ANN_|DGM_).*\.svg$/.test(f))) {
    await sharp(path.join(__dirname,file)).png().toFile(path.join(__dirname,file.replace('.svg','.png')));
  }
  console.log('Exported static PNGs and independent transparent layers.');
})();
