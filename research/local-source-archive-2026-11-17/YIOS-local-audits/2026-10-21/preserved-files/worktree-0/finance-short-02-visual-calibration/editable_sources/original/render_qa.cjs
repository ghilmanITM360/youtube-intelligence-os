// Static review comparisons only; source tiles are separately identified.
const sharp=require('sharp'),fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..'), refs=path.join(root,'editable_sources/references');
const label=(w,h,t)=>Buffer.from(`<svg width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="white"/><text x="12" y="29" font-family="sans-serif" font-size="20" fill="#171512">${t}</text></svg>`);
(async()=>{
 const cases=[
  ['HERO_01','rSa2aziEsAI_sheet_001.jpg',0,0,'rSa2aziEsAI S001.0 @1.237s'],
  ['HERO_02','rSa2aziEsAI_sheet_002.jpg',400,355,'rSa2aziEsAI S010.3 @38.640s'],
  ['HERO_03','2EZzwupIa80_sheet_003.jpg',1000,0,'2EZzwupIa80 S006.0 @37.350s']
 ];
 for(const [name,file,left,top,caption] of cases){
  const reference=await sharp(path.join(refs,file)).extract({left,top,width:200,height:355}).resize(360,640,{fit:'contain',background:'white'}).png().toBuffer();
  const sample=await sharp(path.join(root,name+'.png')).resize(360,640).png().toBuffer();
  await sharp({create:{width:920,height:820,channels:4,background:'white'}}).composite([
   {input:label(435,45,'Reference / '+caption),left:20,top:20},
   {input:label(400,45,'Original / '+name+' (static sample)'),left:490,top:20},
   {input:reference,left:40,top:90},{input:sample,left:520,top:90},
   {input:label(880,45,'Private comparison. Reference state stamp retained; aspect ratio preserved.'),left:20,top:760}
  ]).png().toFile(path.join(refs,'QA_'+name+'_side_by_side.png'));
 }
 const overlays=[];
 for(let i=1;i<=3;i++){
  const name='HERO_0'+i;
  const mobile=await sharp(path.join(root,name+'.png')).resize(320,569).png().toBuffer();
  const stress=await sharp(path.join(root,name+'.png')).resize(160,284).png().toBuffer();
  const zones=Buffer.from('<svg xmlns="http://www.w3.org/2000/svg" width="320" height="569"><rect x="0" y="0" width="320" height="36" fill="#555" opacity="0.65"/><rect x="275" y="36" width="45" height="429" fill="#555" opacity="0.65"/><rect x="0" y="465" width="320" height="104" fill="#555" opacity="0.65"/></svg>');
  const tested=await sharp(mobile).composite([{input:zones,left:0,top:0}]).png().toBuffer();
  overlays.push({input:tested,left:20+(i-1)*340,top:70},{input:stress,left:100+(i-1)*340,top:745});
 }
 overlays.push({input:label(1020,45,'320px / simulated UI obstruction; no universal platform-safe guarantee'),left:10,top:10},
 {input:label(1020,45,'160px stress / source body text is secondary to large redraws'),left:10,top:690});
 await sharp({create:{width:1040,height:1060,channels:4,background:'white'}}).composite(overlays).png().toFile(path.join(refs,'QA_MOBILE.png'));
 console.log('Three actual-reference comparisons + mobile review image saved.');
})();
