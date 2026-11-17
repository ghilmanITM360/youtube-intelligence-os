// Static raster export and contact sheets only. No video/frame/timeline dependency.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),sharp=require('sharp');
const root=path.resolve(__dirname,'..'),scene=Number(process.argv[2]);
const read=p=>JSON.parse(fs.readFileSync(p));
const h=b=>crypto.createHash('sha256').update(b).digest('hex');
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;');
const label=(s,w=320,height=40)=>Buffer.from(`<svg width="${w}" height="${height}"><rect width="100%" height="100%" fill="white"/><text x="8" y="25" font-family="sans-serif" font-size="15" fill="#211b18">${esc(s)}</text></svg>`);
(async()=>{
 const records=read(path.join(root,'manifests/ASSET_DATA.json'));
 for(const r of records){const src=fs.readFileSync(path.join(root,r.source)),out=path.join(root,'assets/exports',r.asset_id+'.png');
  // Skip unchanged validated source exports by byte hash recorded in render index.
  const indexFile=path.join(root,'manifests/EXPORT_HASHES.json');const old=fs.existsSync(indexFile)?read(indexFile):{};
  if(old[r.asset_id]?.source_sha256===h(src)&&fs.existsSync(out)&&old[r.asset_id]?.png_sha256===h(fs.readFileSync(out)))continue;
  await sharp(src).png().toFile(out);
 }
 const s=read(path.join(root,'manifests',`SCENE_${String(scene).padStart(2,'0')}.json`));
 let comps=[];const cellw=320,cellh=620,cols=Math.min(s.states.length,4),rows=Math.ceil(s.states.length/cols);
 for(let i=0;i<s.states.length;i++){
  const state=s.states[i],src=path.join(root,'assets/scene_compositions',state.state_id+'.svg');
  const native=await sharp(src).png().toBuffer();const mobile=await sharp(native).resize(320,569).png().toBuffer();
  const stress=await sharp(native).resize(160,284).png().toBuffer();
  await fs.promises.writeFile(path.join(root,'assets/exports',state.state_id+'_320.png'),mobile);
  comps.push({input:mobile,left:(i%cols)*cellw,top:Math.floor(i/cols)*cellh+40});comps.push({input:label(state.state_id+' / '+state.start+'-'+state.end+'s'),left:(i%cols)*cellw,top:Math.floor(i/cols)*cellh});
  if(i===s.states.length-1){
   await fs.promises.writeFile(path.join(root,`SCENE_${String(scene).padStart(2,'0')}.png`),native);
   await fs.promises.writeFile(path.join(root,'assets/exports',`SCENE_${String(scene).padStart(2,'0')}_160.png`),stress);
   // Conservative simulated obstruction mask; exact mobile UI is platform/device dependent.
   const mask=Buffer.from('<svg width="320" height="569"><rect x="0" y="0" width="320" height="35" fill="#999" fill-opacity=".22"/><rect x="276" y="90" width="44" height="390" fill="#999" fill-opacity=".22"/><rect x="0" y="487" width="320" height="82" fill="#999" fill-opacity=".22"/></svg>');
   const masked=await sharp(mobile).composite([{input:mask}]).png().toBuffer();
   await sharp({create:{width:510,height:610,channels:4,background:'white'}}).composite([{input:label('320 / simulated UI',320),left:0,top:0},{input:masked,left:0,top:40},{input:label('160 stress',180),left:330,top:0},{input:stress,left:330,top:40}]).png().toFile(path.join(root,'assets/exports',`SCENE_${String(scene).padStart(2,'0')}_MOBILE_QA.png`));
  }
 }
 await sharp({create:{width:cols*cellw,height:rows*cellh,channels:4,background:'white'}}).composite(comps).png().toFile(path.join(root,'assets/exports',`SCENE_${String(scene).padStart(2,'0')}_CONTACT.png`));
 const index={};for(const r of records)index[r.asset_id]={source_sha256:h(fs.readFileSync(path.join(root,r.source))),png_sha256:h(fs.readFileSync(path.join(root,'assets/exports',r.asset_id+'.png')))};
 fs.writeFileSync(path.join(root,'manifests/EXPORT_HASHES.json'),JSON.stringify(index,null,2));
 console.log(`Scene ${scene}: ${s.states.length} static state previews, native final, 320/160 review; ${records.length} reusable assets available.`);
})().catch(e=>{console.error(e);process.exit(1)});
