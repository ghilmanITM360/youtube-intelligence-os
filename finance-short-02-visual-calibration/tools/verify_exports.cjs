// Re-render to memory and compare decoded pixels; does not rewrite approved exports.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),sharp=require('sharp');const R=path.resolve(__dirname,'..');
const read=p=>JSON.parse(fs.readFileSync(p));const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
(async()=>{
 let assets=0,states=0,natives=0;const mismatches=[];
 async function equal(src,out,resize){let render=sharp(src);if(resize)render=render.resize(...resize);const a=await render.ensureAlpha().raw().toBuffer({resolveWithObject:true}),b=await sharp(out).ensureAlpha().raw().toBuffer({resolveWithObject:true});if(a.info.width!==b.info.width||a.info.height!==b.info.height||digest(a.data)!==digest(b.data))mismatches.push(path.relative(R,out));}
 for(const r of read(path.join(R,'manifests/ASSET_DATA.json'))){await equal(path.join(R,r.source),path.join(R,'assets/exports',r.asset_id+'.png'));assets++;}
 for(let n=1;n<=7;n++){const s=read(path.join(R,'manifests',`SCENE_${String(n).padStart(2,'0')}.json`));
  for(const state of s.states){
   // Export pipeline rasterizes native before resizing; keep that documented order.
   const native=await sharp(path.join(R,'assets/scene_compositions',state.state_id+'.svg')).png().toBuffer();await equal(native,path.join(R,'assets/exports',state.state_id+'_320.png'),[320,569]);states++;
  }
  await equal(path.join(R,'assets/scene_compositions',`SCENE_${String(n).padStart(2,'0')}.svg`),path.join(R,`SCENE_${String(n).padStart(2,'0')}.png`));natives++;
 }
 const report={result:mismatches.length?'FAIL':'PASS',independent_asset_pixel_matches:assets,state_preview_pixel_matches:states,native_scene_pixel_matches:natives,mismatches,runtime:{node:process.version,sharp:sharp.versions.sharp,libvips:sharp.versions.vips},scope:'Same-runtime decoded pixel equality; not a claim of all-platform renderer pixel identity'};
 fs.writeFileSync(path.join(R,'manifests/EXPORT_VALIDATION.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));if(mismatches.length)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
