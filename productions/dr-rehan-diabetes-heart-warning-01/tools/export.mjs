import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const sharp=require(process.env.SHARP_MODULE || 'sharp');
const root=path.resolve(new URL('..',import.meta.url).pathname);
async function walk(dir){let out=[];for(const e of await fs.readdir(dir,{withFileTypes:true})){const p=path.join(dir,e.name);out.push(...e.isDirectory()?await walk(p):[p]);}return out;}
for(const folder of ['assets','scenes']){
 for(const file of await walk(path.join(root,folder))){
  if(!file.endsWith('.svg'))continue;
  const dest=path.join(root,'exports',path.relative(root,file).replace(/\.svg$/,'.png'));
  await fs.mkdir(path.dirname(dest),{recursive:true});
  let fresh=false;try{fresh=(await fs.stat(dest)).mtimeMs >= (await fs.stat(file)).mtimeMs;}catch{}
  if(!fresh)await sharp(file).png().toFile(dest);
 }
}
console.log('SVG → PNG exports complete');
