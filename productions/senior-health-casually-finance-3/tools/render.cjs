const fs=require('fs'),path=require('path');
const sharp=require('/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'..');
async function walk(dir){let out=[];for(const f of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,f.name);if(f.isDirectory())out.push(...await walk(p));else if(p.endsWith('.svg'))out.push(p)}return out}
(async()=>{for(const pkg of fs.readdirSync(root).filter(x=>/^0\d_/.test(x))){for(const sub of ['assets/svg','scene_states'])for(const p of await walk(path.join(root,pkg,sub))){const out=p.replace('/assets/svg/','/assets/png/').replace(/\.svg$/,'.png');fs.mkdirSync(path.dirname(out),{recursive:true});await sharp(p).png().toFile(out)}console.log(pkg,'rendered')}})().catch(e=>{console.error(e);process.exit(1)});
