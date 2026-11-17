// Original assets only. No private creator reference pixels in distributable sheets.
const fs=require('fs'),path=require('path'),sharp=require('sharp');const R=path.resolve(__dirname,'..');
const rows=JSON.parse(fs.readFileSync(path.join(R,'manifests/ASSET_DATA.json')));
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;');
const type=(text,w,h=38,size=16)=>Buffer.from(`<svg width="${w}" height="${h}"><rect width="100%" height="100%" fill="white"/><text x="10" y="27" font-family="sans-serif" font-size="${size}" fill="#211b18">${esc(text)}</text></svg>`);
const tile=async(r,w,h)=>sharp(path.join(R,'assets/exports',r.asset_id+'.png')).resize(w,h,{fit:'contain',background:'#fff'}).flatten({background:'#fff'}).png().toBuffer();
(async()=>{
 const art=rows.filter(r=>!['CANVAS','ORIGINAL_LETTERING'].includes(r.classification)).sort((a,b)=>a.category.localeCompare(b.category)||a.asset_id.localeCompare(b.asset_id));
 const letters=rows.filter(r=>r.classification==='ORIGINAL_LETTERING');let layers=[];const W=1500,base=80,artH=Math.ceil(art.length/6)*245;
 layers.push({input:type('Original illustration / variants / documentary crops — counts separated in ASSET_COUNTS.json',W,60,21),left:0,top:0});
 for(let i=0;i<art.length;i++){const r=art[i],x=i%6*250,y=base+Math.floor(i/6)*245;layers.push({input:await tile(r,230,185),left:x+10,top:y});layers.push({input:type(r.asset_id,250,35,14),left:x,top:y+190});}
 layers.push({input:type('Editable original lettering — 57 semantic labels; not 57 unique illustrations',W,50,21),left:0,top:base+artH});
 for(let i=0;i<letters.length;i++){const r=letters[i],x=i%3*500,y=base+artH+60+Math.floor(i/3)*95;layers.push({input:await tile(r,470,53),left:x+15,top:y});layers.push({input:type(r.asset_id,500,30,13),left:x,top:y+54});}
 await sharp({create:{width:W,height:base+artH+70+Math.ceil(letters.length/3)*95,channels:4,background:'white'}}).composite(layers).png().toFile(path.join(R,'FULL_ASSET_CONTACT_SHEET.png'));
 const overview=[];for(let n=1;n<=7;n++){const x=(n-1)%4*270,y=Math.floor((n-1)/4)*525;overview.push({input:await sharp(path.join(R,`SCENE_${String(n).padStart(2,'0')}.png`)).resize(270,480).png().toBuffer(),left:x,top:y+40});overview.push({input:type('SCENE '+String(n).padStart(2,'0'),270,40,17),left:x,top:y});}
 await sharp({create:{width:1080,height:1050,channels:4,background:'white'}}).composite(overview).png().toFile(path.join(R,'SCENE_OVERVIEW.png'));
 const poses=rows.filter(r=>r.classification==='POSE_EXPRESSION_VARIANT');const faces=rows.filter(r=>r.classification==='EXPRESSION_OVERLAY');let chars=[];
 chars.push({input:type('Same original host — production poses and separable expression overlays',1400,60,23),left:0,top:0});
 for(let i=0;i<poses.length;i++){const x=i%4*350,y=70+Math.floor(i/4)*475;chars.push({input:await tile(poses[i],300,405),left:x+25,top:y});chars.push({input:type(poses[i].asset_id,350,40,18),left:x,top:y+412});}
 for(let i=0;i<faces.length;i++){const x=i%6*230,y=1040;chars.push({input:await tile(faces[i],180,180),left:x+25,top:y});chars.push({input:type(faces[i].asset_id,230,40,16),left:x,top:y+180});}
 await sharp({create:{width:1400,height:1280,channels:4,background:'white'}}).composite(chars).png().toFile(path.join(R,'PRODUCTION_CHARACTER_SHEET.png'));
 console.log('Created original-only full asset sheet, seven-scene overview and production character sheet.');
})().catch(e=>{console.error(e);process.exit(1)});
