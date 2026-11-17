import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const runtime = JSON.parse(fs.readFileSync(path.join(here, 'runtime.json')));
const require = createRequire(path.join(runtime.packages, '_thumbnail_loader.cjs'));
const sharp = require('sharp');
const out = path.dirname(here);
const C = {ink:'#142A38',teal:'#147D83',paper:'#FFF5DF',coral:'#F16850',gold:'#E8BC62',skin:'#BB7557',hair:'#342A39'};

// Original illustration geometry. No imported visual assets or competitor references.
function shopper(x,y,s=1) {
  return `<g id="remy-shopper" transform="translate(${x} ${y}) scale(${s})" stroke="${C.ink}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round">
    <g id="torso"><path d="M74 287 Q155 250 230 285 L271 500 Q175 537 45 502Z" fill="${C.teal}"/><path d="M107 275 L132 310 L166 292 L192 273" fill="${C.paper}"/><path d="M103 468 Q170 488 229 470" fill="none" stroke="#0F5D67"/><path d="M52 501 L245 501 L263 565 L54 565Z" fill="${C.ink}"/></g>
    <g id="head"><path d="M122 223 L115 285 Q154 320 188 278 L184 221" fill="${C.skin}"/>
    <path d="M76 114 Q72 72 143 65 Q225 58 239 131 L232 196 Q225 234 192 250 L122 249 Q89 234 85 191 L64 172 L63 139Z" fill="${C.skin}"/>
    <path d="M78 168 Q42 153 53 104 Q20 59 70 40 Q62 2 111 15 Q140 -14 169 15 Q217 -9 231 38 Q282 46 250 101 L215 126 L200 82 Q155 118 108 102 L101 161Z" fill="${C.hair}"/>
    <path d="M66 153 Q43 150 48 176 Q53 198 86 194" fill="${C.skin}"/><path d="M63 172 L72 177" fill="none" stroke-width="5"/>
    <path d="M127 146 L153 140 M185 139 L213 149" fill="none" stroke-width="8"/>
    <ellipse cx="144" cy="165" rx="7" ry="12" fill="${C.ink}" stroke="none"/><ellipse cx="202" cy="164" rx="7" ry="12" fill="${C.ink}" stroke="none"/>
    <path d="M177 170 L187 194 L170 199" fill="none" stroke-width="5"/><path d="M149 221 Q172 207 197 216" fill="none" stroke-width="7"/>
    <path d="M130 115 Q151 107 172 102" fill="none" stroke="#56424C" stroke-width="6"/>
    </g>
    <g id="arm-point"><path d="M223 290 Q247 288 264 319 L299 356 L346 304 L373 332 L314 403 Q295 419 276 400 L222 352" fill="${C.teal}"/><path d="M335 314 L353 291 L383 312 L367 340Z" fill="${C.paper}"/>
    <path d="M350 295 L359 271 Q364 259 376 266 L385 279 L422 250 Q434 243 440 253 Q445 261 436 269 L408 294 L426 289 Q441 289 440 303 L428 321 Q415 334 397 328 L379 320Z" fill="${C.skin}"/><path d="M405 297 L416 311" fill="none" stroke-width="5"/></g>
    <g id="arm-rest"><path d="M74 296 Q47 287 31 321 L10 405 Q6 432 28 443 L89 467 L105 429 L59 406 L81 356" fill="${C.teal}"/><path d="M91 425 L112 434 L100 475 L81 467Z" fill="${C.paper}"/><path d="M110 434 Q139 431 152 446 L158 470 Q153 482 140 475 L134 465 L113 480 L101 474Z" fill="${C.skin}"/></g>
  </g>`;
}
function start(label) {
 return `<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" role="img" aria-labelledby="title"><title id="title">${label}</title><defs><pattern id="dots" width="36" height="36" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.4" fill="#FFF5DF" opacity=".09"/></pattern></defs><rect width="1080" height="1920" fill="${C.ink}"/><rect width="1080" height="1920" fill="url(#dots)"/><circle cx="940" cy="1660" r="480" fill="#1B3744"/><circle cx="75" cy="180" r="285" fill="#1B3744"/><g font-family="Avenir Next, Arial, sans-serif" font-weight="800">`;
}
function clock(cx,cy,r) {
 let ticks='';
 for(let i=0;i<12;i++){const a=i*Math.PI/6; ticks+=`<path d="M${cx+Math.sin(a)*r*.8} ${cy-Math.cos(a)*r*.8} L${cx+Math.sin(a)*r*.69} ${cy-Math.cos(a)*r*.69}"/>`;}
 return `<g id="clock"><circle cx="${cx+8}" cy="${cy+17}" r="${r+12}" fill="#091D29"/><circle cx="${cx}" cy="${cy}" r="${r}" fill="${C.gold}" stroke="${C.ink}" stroke-width="12"/><circle cx="${cx}" cy="${cy}" r="${r*.88}" fill="${C.paper}"/><g stroke="${C.ink}" stroke-width="${r*.035}" stroke-linecap="round">${ticks}<path d="M${cx} ${cy-r*.49}V${cy}L${cx-r*.43} ${cy}" fill="none"/></g><circle cx="${cx}" cy="${cy}" r="${r*.06}" fill="${C.ink}"/></g>`;
}
const A=start('Original finance thumbnail A: the condition in a no-interest offer')+`
 <g id="headline" fill="${C.paper}" text-anchor="middle"><text x="540" y="444" font-size="144" letter-spacing="-4">NO</text><text x="540" y="585" font-size="137" letter-spacing="-6">INTEREST?</text></g>
 <g id="hero-offer" transform="rotate(5 636 1040)">
 <path d="M459 723 L957 723 L957 1320 Q904 1364 866 1331 L834 1360 L799 1331 L764 1360 L729 1331 L694 1360 L659 1331 L624 1360 L589 1331 L554 1360 L519 1331 L459 1360Z" fill="#091D29"/>
 <path d="M428 695 L926 695 L926 1286 L893 1314 L858 1286 L823 1314 L788 1286 L753 1314 L718 1286 L683 1314 L648 1286 L613 1314 L578 1286 L543 1314 L508 1286 L473 1314 L428 1286Z" fill="${C.paper}" stroke="${C.ink}" stroke-width="12"/>
 <path d="M434 704H920V815H434Z" fill="${C.teal}"/>
 <path d="M477 758H675 M477 1182H847 M477 1230H727" stroke="#76B5AE" stroke-width="15" stroke-linecap="round"/>
 <text x="679" y="1056" fill="${C.coral}" font-size="253" text-anchor="middle" letter-spacing="-12">IF</text>
 <text x="679" y="1134" fill="${C.ink}" font-size="47" text-anchor="middle" letter-spacing="-1">PAID IN FULL</text>
 </g>
 <ellipse cx="308" cy="1480" rx="225" ry="34" fill="#091D29"/>
 ${shopper(73,889,1.01)}
 <g id="emphasis" stroke="${C.gold}" stroke-width="13" stroke-linecap="round"><path d="M902 612L926 583 M949 658L988 649"/></g>
 </g></svg>`;
const B=start('Original finance thumbnail B: deferred interest reaches back to purchase day')+`
 <g id="headline" fill="${C.paper}" text-anchor="middle"><text x="540" y="434" font-size="117" letter-spacing="-4">BACK TO</text><text x="540" y="569" font-size="139" letter-spacing="-5">DAY ONE</text></g>
 ${clock(554,948,286)}
 <g id="rewind-arrow" fill="none" stroke="${C.coral}" stroke-width="42" stroke-linecap="round"><path d="M797 726 C1006 920 891 1233 630 1253"/></g>
 <path d="M799 672 L722 753 L840 772Z" fill="${C.coral}" stroke="${C.ink}" stroke-width="7" stroke-linejoin="round"/>
 <g id="interest-receipt" transform="rotate(-8 740 1357)"><path d="M519 1194H942V1513L913 1490L878 1513L843 1490L808 1513L773 1490L738 1513L703 1490L668 1513L633 1490L598 1513L563 1490L519 1513Z" fill="${C.paper}" stroke="${C.ink}" stroke-width="11"/><rect x="525" y="1200" width="411" height="113" fill="${C.coral}"/><text x="730" y="1274" font-size="57" text-anchor="middle" fill="${C.ink}" letter-spacing="-2">INTEREST</text><path d="M578 1375H875M578 1437H784" stroke="#C7BEAE" stroke-width="17" stroke-linecap="round"/></g>
 <ellipse cx="299" cy="1538" rx="192" ry="28" fill="#091D29"/>
 ${shopper(80,1018,.87)}
 </g></svg>`;

for (const [name,svg] of [['A',A],['B',B]]) {
 const clean=svg;
 fs.writeFileSync(path.join(here,`thumbnail_${name}.svg`),clean);
 await sharp(Buffer.from(clean),{density:144}).png().toFile(path.join(out,`thumbnail_${name}.png`));
 for(const w of [160,320])await sharp(Buffer.from(clean)).resize({width:w}).png().toFile(path.join(here,`thumbnail_${name}_${w}.png`));
 await sharp(Buffer.from(clean)).extract({left:0,top:285,width:1080,height:1350}).resize({width:320}).png().toFile(path.join(here,`thumbnail_${name}_crop_4x5.png`));
}
const panels=[];
for (let i=0;i<2;i++){
 const name=i?'B':'A';
 panels.push({input:path.join(here,`thumbnail_${name}_320.png`),left:i*344,top:0});
 panels.push({input:path.join(here,`thumbnail_${name}_160.png`),left:i*344,top:590});
}
await sharp({create:{width:664,height:875,channels:3,background:'#DDD7CD'}}).composite(panels).png().toFile(path.join(here,'mobile_review.png'));
console.log('Rendered A and B, editable SVGs, 160/320px previews and 4:5 crop checks.');
