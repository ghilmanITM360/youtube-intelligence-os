import React from 'react';
import {poseAt,solveLeg,PoseName} from './motion';
export const C={ink:'#19353F',cream:'#FAF3E6',paper:'#FFFDFA',coral:'#DE7357',teal:'#267C78',mint:'#D2E8D8',yellow:'#E8B957',skin:'#C88D61',hair:'#233547',muted:'#526A70',red:'#B84239'};
export const Text=({x,y,size=48,fill=C.ink,weight=700,children,anchor='start'}:{x:number;y:number;size?:number;fill?:string;weight?:number;children:React.ReactNode;anchor?:'start'|'middle'|'end'})=><text x={x} y={y} fontSize={size} fill={fill} fontWeight={weight} textAnchor={anchor} fontFamily="Arial, sans-serif">{children}</text>;
export const Card=({x,y,w,h,children,fill=C.paper}:{x:number;y:number;w:number;h:number;children?:React.ReactNode;fill?:string})=><g transform={`translate(${x} ${y})`}><rect x={6} y={9} width={w} height={h} rx={30} fill={C.ink} opacity={.08}/><rect width={w} height={h} rx={30} fill={fill} stroke={C.ink} strokeWidth={5}/>{children}</g>;
export const Environment=()=> <g>
 <rect width={1920} height={1080} fill={C.cream}/><path d="M0 832 Q900 814 1920 832 V1080 H0Z" fill="#EADCC5"/>
 <rect x={78} y={147} width={265} height={302} rx={100} fill="#E8EEE1" stroke={C.ink} strokeWidth={5}/>
 <path d="M208 150V448 M80 297H340" stroke={C.ink} strokeWidth={5}/><circle cx={272} cy={225} r={32} fill={C.yellow}/>
 <path d="M85 389 Q143 334 207 386 Q270 337 342 392" fill="none" stroke="#AECABD" strokeWidth={22}/>
 <g transform="translate(1660 495)"><path d="M50 262V42 M50 191Q-42 144 5 87Q62 102 50 191 M52 156Q130 119 118 41Q61 39 52 156" fill={C.teal} stroke={C.ink} strokeWidth={5}/><path d="M0 228H102L88 332H14Z" fill={C.coral} stroke={C.ink} strokeWidth={5}/></g>

</g>;
function Hand({point=false}:{point?:boolean}){return <g stroke={C.ink} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round" fill={C.skin}>
 {point?<path d="M-11 0 Q-14 14-10 23 L-7 52 Q-4 58 0 53 L1 28 Q8 29 11 24 Q17 22 15 16 Q21 12 15 6 L9-3 L-1-8 Q-7-11-11 0Z"/>:<path d="M-11 0 Q-17 10-15 16 L-9 32 Q-5 37-2 31 L-2 17 L1 38 Q6 44 9 37 L8 17 L12 32 Q18 38 20 30 L15 10 Q14-1 6-4 L-1-8 Q-10-11-11 0Z"/>}
 <path d="M-11 8 Q-30 10-26 20 Q-21 25-12 20"/>
 </g>}
function Arm({x,upper,elbow,point=false}:{x:number;upper:number;elbow:number;point?:boolean}){return <g transform={`translate(${x} 119) rotate(${upper})`}>
 <path d="M0 0L0 77" stroke={C.ink} strokeWidth={34} strokeLinecap="round"/><path d="M0 0L0 77" stroke={C.coral} strokeWidth={26} strokeLinecap="round"/>
 <g transform={`translate(0 77) rotate(${elbow})`}><path d="M0 0L0 68" stroke={C.ink} strokeWidth={25} strokeLinecap="round"/><path d="M0 0L0 68" stroke={C.skin} strokeWidth={17} strokeLinecap="round"/><path d="M-14-2H14V17H-14Z" fill={C.coral} stroke={C.ink} strokeWidth={4}/><g transform="translate(0 69)"><Hand point={point}/></g></g>
 </g>}
export type Expression='curious'|'concerned'|'explain'|'pleased'|'neutral';
export function Character({x=340,y=280,scale=1.4,f=0,pose='hold',from='hold',expression='neutral'}:{x?:number;y?:number;scale?:number;f?:number;pose?:PoseName;from?:PoseName;expression?:Expression}){
 const p=poseAt(f,pose,from), blink=(f%151>144)? .18:1;
 return <g transform={`translate(${x} ${y}) scale(${scale})`}>
 <ellipse cx={0} cy={421} rx={95} ry={15} fill={C.ink} opacity={.12}/>
 {[-1,1].map(side=>{const hip={x:side*30,y:p.hipY},foot={x:side*56,y:410},k=solveLeg(hip,foot,95,95,side);return <g key={side}>
 <path d={`M${hip.x} ${hip.y}L${k.x} ${k.y}L${foot.x} ${foot.y}`} stroke={C.ink} strokeWidth={38} fill="none" strokeLinecap="round"/><path d={`M${hip.x} ${hip.y}L${k.x} ${k.y}L${foot.x} ${foot.y-15}`} stroke="#344D59" strokeWidth={27} fill="none" strokeLinecap="round"/>
 <path d={`M${foot.x-23} 390Q${foot.x-4} 384 ${foot.x+20} 398L${foot.x+34} 412Q${foot.x+37} 423 ${foot.x+19} 423H${foot.x-24}Z`} fill={C.yellow} stroke={C.ink} strokeWidth={5}/><path d={`M${foot.x-14} 398h20 M${foot.x-11} 404h24`} stroke={C.ink} strokeWidth={3}/>
 </g>})}
 <Arm x={-58} upper={p.leftUpper} elbow={p.leftElbow}/>
 <path d={`M-53 106Q-32 87 0 98Q35 86 57 109L63 ${p.hipY+8}Q0 ${p.hipY+25}-64 ${p.hipY+8}Z`} fill={C.coral} stroke={C.ink} strokeWidth={6}/><path d="M-25 111Q0 132 25 111" fill="none" stroke={C.ink} strokeWidth={5}/><path d={`M-50 ${p.hipY-4}Q0 ${p.hipY+10} 52 ${p.hipY-4}`} fill="none" stroke="#B9523E" strokeWidth={5}/><path d="M-28 178h55v37h-55Z" fill="#E58869" stroke={C.ink} strokeWidth={3}/>
 <path d="M-18 78v22q18 17 36 0V78" fill={C.skin} stroke={C.ink} strokeWidth={5}/>
 <g transform={`rotate(${p.head} 0 59)`}>
 <path d="M-54 16Q-65-40-16-41Q21-64 58-28Q75-8 59 43L48 76H-48Z" fill={C.hair} stroke={C.ink} strokeWidth={6}/>
 <ellipse cx={-57} cy={38} rx={12} ry={18} fill={C.skin} stroke={C.ink} strokeWidth={5}/><ellipse cx={57} cy={38} rx={12} ry={18} fill={C.skin} stroke={C.ink} strokeWidth={5}/>
 <path d="M-51 0Q-41-21-8-12Q24 8 48-7L54 40Q56 79 21 91Q-7 103-38 79Q-60 61-51 0Z" fill={C.skin} stroke={C.ink} strokeWidth={5}/>
 <path d="M-51 1Q-68-26-25-39Q-5-56 30-38Q48-30 48-7Q22 7-8-12Q-30-12-51 1Z" fill={C.hair}/><path d="M-37-21Q-4-41 18-25" stroke="#425D71" strokeWidth={6} strokeLinecap="round" fill="none"/>
 <g fill="none" stroke={C.ink} strokeWidth={4}><circle cx={-24} cy={31} r={22}/><circle cx={26} cy={31} r={22}/><path d="M-2 28h6 M-47 28l-10-2 M48 28l9-2"/></g>
 <ellipse cx={-24} cy={33} rx={4} ry={7*blink} fill={C.ink}/><ellipse cx={26} cy={33} rx={4} ry={7*blink} fill={C.ink}/><path d="M1 34l-5 17h10" fill="none" stroke={C.ink} strokeWidth={3} strokeLinecap="round"/>
 <path d={expression==='concerned'?'M-39 9l23-8 M16 1l23 8':expression==='curious'?'M-38 0l23 6 M16-1l23-3':'M-38 3h21 M16 3h21'} fill="none" stroke={C.ink} strokeWidth={4} strokeLinecap="round"/>
 <path d={expression==='pleased'?'M-17 65Q0 82 19 63':expression==='concerned'?'M-15 73Q0 61 17 72':expression==='explain'?'M-10 64Q5 56 17 67Q9 82-5 77Z':'M-13 70Q2 74 15 68'} stroke={C.ink} fill={expression==='explain'?C.ink:'none'} strokeWidth={4} strokeLinecap="round"/>
 <circle cx={-41} cy={58} r={9} fill={C.coral} opacity={.3}/><circle cx={41} cy={58} r={9} fill={C.coral} opacity={.3}/>
 </g>
 {pose==='hold'&&<g opacity={Math.max(0,Math.min(1,(f-20)/6))}><Contract x={0} y={190} scale={.38}/></g>}
 <Arm x={57} upper={p.rightUpper} elbow={p.rightElbow} point={pose==='point'}/>
 </g>;
}
export function House({x=0,y=0,scale=1}:{x?:number;y?:number;scale?:number}){return <g transform={`translate(${x} ${y}) scale(${scale})`} fill={C.mint} stroke={C.ink} strokeWidth={6} strokeLinejoin="round"><path d="M-84-5V94H86V-5Z"/><path d="M-110-3L0-96L112-3Z" fill={C.coral}/><path d="M-20 36h44v58" fill={C.yellow}/><rect x={-63} y={13} width={31} height={32} fill={C.paper}/><rect x={42} y={13} width={29} height={32} fill={C.paper}/><path d="M-103 99H105" fill="none"/></g>}
export function Lock({x=0,y=0,scale=1}:{x?:number;y?:number;scale?:number}){return <g transform={`translate(${x} ${y}) scale(${scale})`} stroke={C.ink} strokeWidth={6} strokeLinecap="round"><path d="M-30-2V-27Q-30-62 0-62Q30-62 30-27V-2" fill="none"/><rect x={-43} y={-3} width={86} height={72} rx={13} fill={C.yellow}/><circle cy={25} r={7} fill={C.ink}/><path d="M0 30v15"/></g>}
export function Contract({x=0,y=0,scale=1,label='FIXED',rate='6%'}:{x?:number;y?:number;scale?:number;label?:string;rate?:string}){return <g transform={`translate(${x} ${y}) scale(${scale})`}><path d="M-100-142H62L100-104V146H-100Z" fill={C.paper} stroke={C.ink} strokeWidth={5}/><path d="M62-142v38h38" fill={C.mint} stroke={C.ink} strokeWidth={5}/><Text x={0} y={-81} size={28} anchor="middle">{label}</Text><Text x={0} y={-24} size={53} anchor="middle">{rate}</Text><path d="M-62 11H62 M-62 31H62 M-62 51H28" stroke="#8AA5A7" strokeWidth={5}/><path d="M-53 107Q-37 65-26 98Q-10 76-6 109Q9 83 22 96Q43 104 61 91" stroke={C.teal} strokeWidth={5} fill="none"/><circle cx={64} cy={120} r={14} fill={C.coral}/></g>}
export function Coin({x=0,y=0,scale=1}:{x?:number;y?:number;scale?:number}){return <g transform={`translate(${x} ${y}) scale(${scale})`}><circle r={40} fill={C.yellow} stroke={C.ink} strokeWidth={5}/><circle r={29} fill="none" stroke="#B68829" strokeWidth={3}/><Text x={0} y={15} size={43} anchor="middle">$</Text></g>}
export function Bank({x=0,y=0,scale=1}:{x?:number;y?:number;scale?:number}){return <g transform={`translate(${x} ${y}) scale(${scale})`} stroke={C.ink} strokeWidth={5} fill={C.mint}><path d="M-118-57L0-130L118-57Z"/><rect x={-116} y={-55} width={232} height={25}/>{[-79,-27,27,79].map(x=><rect key={x} x={x-12} y={-29} width={24} height={102} fill={C.paper}/>)}<path d="M-122 77H123v26H-122Z"/><Text x={0} y={-64} size={24} anchor="middle">FED</Text></g>}
