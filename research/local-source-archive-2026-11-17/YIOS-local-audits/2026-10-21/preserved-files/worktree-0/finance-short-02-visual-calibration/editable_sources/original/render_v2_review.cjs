// Static comparison and source-review images only. No keyframes or video generation.
const sharp=require('sharp'),fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..'),refs=path.join(root,'editable_sources/references/owner_examples');
const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;');
const label=(w,h,lines,size=22)=>Buffer.from(`<svg width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="white"/>${lines.map((t,i)=>`<text x="10" y="${30+i*(size+13)}" font-family="sans-serif" font-size="${size}" fill="#171512">${escape(t)}</text>`).join('')}</svg>`);
(async()=>{
 const cases=[
  ['HERO_01','REF_09.png',{left:800,top:714,width:400,height:714},'2EZzwupIa80 S007.2 / 51.80s',10,['Paper grip / sparse white field','Original host; no map character','Folded bill and irregular props','Remaining: cleaner letterforms']],
  ['HERO_02','REF_03.png',{left:1061,top:362,width:177,height:337},'rSa2aziEsAI M0027 / 39.4248s',16,['Independent buildings / notes','Original reverse expense flow','Reserve link is conceptual','Remaining: diagram is sparser']],
  ['HERO_03','REF_09.png',{left:2400,top:0,width:400,height:714},'2EZzwupIa80 S006.1 / 44.75s',13,['Real evidence / original character','Separate red figure highlight','No imitation official panel','Remaining: calmer expression']]
 ];
 const layers=[];const locators=[];
 for(let i=0;i<cases.length;i++){
  const [name,file,box,locator,count,notes]=cases[i],y=70+i*700;
  const ref=await sharp(path.join(refs,file)).extract(box).png().toBuffer();fs.writeFileSync(path.join(refs,name+'_reference_tile.png'),ref);
  const refPreview=await sharp(ref).resize(320,570,{fit:'contain',background:'white'}).png().toBuffer();
  const ours=await sharp(path.join(root,name+'.png')).resize(320,569).png().toBuffer();
  const stress=await sharp(path.join(root,name+'.png')).resize(160,284).png().toBuffer();
  layers.push({input:label(1460,50,[name+' / reference '+locator+' / original authored sample'],23),left:20,top:y});
  layers.push({input:refPreview,left:30,top:y+55},{input:ours,left:390,top:y+55},{input:stress,left:770,top:y+55});
  layers.push({input:label(500,400,['320px original + 160px stress',count+' editable top-level layers','Art verdict: reviewable, approval pending','REFERENCE_SUPPORTED: technique','ART_DIRECTION_INFERENCE: staging',...notes],20),left:970,top:y+75});
  locators.push({hero:name,source_file:'editable_sources/references/owner_examples/'+file,source_video_locator:locator,crop_pixels:box,review_only:true});
 }
 layers.push({input:label(1460,55,['Private reference comparisons. Creator frames are not commercial assets. No equivalence or human sign-off claimed.'],20),left:20,top:10});
 await sharp({create:{width:1500,height:2180,channels:4,background:'white'}}).composite(layers).png().toFile(path.join(root,'VISUAL_COMPARISON.png'));
 fs.writeFileSync(path.join(refs,'V2_COMPARISON_LOCATORS.json'),JSON.stringify(locators,null,2));
 const triptych=[];
 for(let i=1;i<=3;i++)triptych.push({input:await sharp(path.join(root,'HERO_0'+i+'.png')).resize(360,640).png().toBuffer(),left:(i-1)*360,top:0});
 await sharp({create:{width:1080,height:640,channels:4,background:'white'}}).composite(triptych).png().toFile(path.join(__dirname,'HERO_REVIEW.png'));
 const mobile=[];
 for(let i=1;i<=3;i++){
  const m=await sharp(path.join(root,'HERO_0'+i+'.png')).resize(320,569).png().toBuffer();
  const zones=Buffer.from('<svg xmlns="http://www.w3.org/2000/svg" width="320" height="569"><rect width="320" height="36" fill="#555" opacity="0.6"/><rect x="275" y="36" width="45" height="429" fill="#555" opacity="0.6"/><rect y="465" width="320" height="104" fill="#555" opacity="0.6"/></svg>');
  mobile.push({input:await sharp(m).composite([{input:zones,left:0,top:0}]).png().toBuffer(),left:20+(i-1)*340,top:60});
  mobile.push({input:await sharp(path.join(root,'HERO_0'+i+'.png')).resize(160,284).png().toBuffer(),left:100+(i-1)*340,top:715});
 }
 mobile.push({input:label(1020,45,['320px / simulated top, right and bottom obstruction; platform layout varies'],20),left:10,top:10},{input:label(1020,45,['160px stress / fine evidence labels remain secondary'],22),left:10,top:650});
 await sharp({create:{width:1040,height:1030,channels:4,background:'white'}}).composite(mobile).png().toFile(path.join(root,'editable_sources/references/QA_MOBILE_V2.png'));
 console.log('Saved new owner-reference comparison, current triptych and V2 mobile QA.');
})();
