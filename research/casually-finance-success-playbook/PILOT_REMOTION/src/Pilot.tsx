import React,{useLayoutEffect} from 'react';
import {AbsoluteFill,Audio,staticFile,useCurrentFrame} from 'remotion';
import timeline from './timeline.json';
import {C,Text,Card,Character,Environment,House,Lock,Contract,Coin,Bank,Expression} from './art';
import {key,pop,reveal,PoseName} from './motion';
import {pushIn} from './camera-presets';
import {DURATION} from './story';
const poses:PoseName[]=['shrug','hold','point','point','hold','point','shrug','hold'];
const expressions:Expression[]=['concerned','explain','explain','neutral','curious','explain','concerned','pleased'];
const Heading=({label,small}:{label:string;small:string})=><g><Text x={603} y={228} size={66}>{label}</Text><Text x={607} y={286} size={32} weight={500} fill={C.muted}>{small}</Text></g>;
const Arrow=({x,y,length=120,down=false,color=C.teal}:{x:number;y:number;length?:number;down?:boolean;color?:string})=><g transform={`translate(${x} ${y}) ${down?'rotate(90)':''}`}><path d={`M0 0H${length-25}`} stroke={color} strokeWidth={14} strokeLinecap="round"/><path d={`M${length-35}-23L${length} 0L${length-35} 23`} fill="none" stroke={color} strokeWidth={14} strokeLinecap="round" strokeLinejoin="round"/></g>;
const Show=({f,at=0,x=0,y=0,children}:{f:number;at?:number;x?:number;y?:number;children:React.ReactNode})=>{const s=pop(f,at);return <g transform={`translate(${x} ${y}) scale(${s})`} opacity={s===0?0:1}>{children}</g>};
function Scene({i,f}:{i:number;f:number}){
 if(i===0)return <>
 <Text x={605} y={229} size={82}>RATE CUT.</Text><Text x={605} y={320} size={68}>SAME PAYMENT?</Text>
 <Card x={613} y={370} w={380} h={375} fill={C.mint}><Text x={190} y={76} size={40} anchor="middle">POLICY RATE</Text><g transform={`translate(190 ${key(f,[[0,125],[10,125],[38,260]])})`}><Text x={0} y={20} size={95} anchor="middle">%</Text></g><Arrow x={300} y={121} length={154} down/></Card>
 <Card x={1094} y={370} w={450} h={375}><Text x={225} y={76} size={40} anchor="middle">YOUR PAYMENT</Text><Text x={225} y={180} size={58} anchor="middle">UNCHANGED</Text><Show f={f} at={40} x={225} y={254}><Lock scale={.75}/></Show></Card>
 </>;
 if(i===1)return <>
 <Heading label="A contract, not a live ticker." small="Standard U.S. fixed-rate mortgage"/>
 <Show f={f} at={6} x={899} y={552}><Contract scale={1.25}/></Show><Show f={f} at={33} x={903} y={655}><Lock scale={.7}/></Show>
 <Show f={f} at={63} x={1230} y={500}><Text x={0} y={0} size={61}>SET AT SIGNING</Text><Text x={0} y={72} size={49}>Rate stays fixed.</Text><Text x={0} y={133} size={31} weight={500} fill={C.muted}>6% is an illustration.</Text></Show>
 </>;
 if(i===2)return <>
 <Heading label="Two different rates." small="A policy change does not reset your loan."/>
 <Show f={f} at={4} x={817} y={526}><Bank scale={1.12}/></Show><Text x={816} y={719} size={41} anchor="middle">OVERNIGHT TARGET</Text>
 <Show f={f} at={25} x={1280} y={529}><Contract scale={1.05}/></Show><Text x={1280} y={740} size={41} anchor="middle">CONTRACT RATE</Text>
 <g opacity={reveal(f,32)}><path d={`M998 530H${998+145*reveal(f,32,32)}`} stroke={C.teal} strokeWidth={9} strokeDasharray="14 14"/><g transform={`translate(${key(f,[[32,998],[63,1146],[78,1115]])} 531)`}><circle r={18} fill={C.teal}/></g></g>
 <Show f={f} at={58} x={1144} y={522}><Lock scale={.6}/></Show>
 </>;
 if(i===3)return <>
 <Heading label="The scheduled payment holds." small="Even if market rates fall • illustrative relationship"/>
 <Card x={608} y={333} w={955} h={447}>
 <Text x={45} y={63} size={35}>MARKET RATES</Text><Text x={45} y={244} size={35}>SCHEDULED PRINCIPAL + INTEREST</Text>
 <path d="M45 174H854 M45 351H854" stroke="#B7C6C2" strokeWidth={3}/>
 <path d="M54 103C280 103 353 142 556 151S766 172 851 172" fill="none" stroke={C.coral} strokeWidth={12} strokeLinecap="round" pathLength={1} strokeDasharray="1" strokeDashoffset={1-reveal(f,13,66)}/>
 <path d="M54 294H851" stroke={C.teal} strokeWidth={12} strokeLinecap="round" pathLength={1} strokeDasharray="1" strokeDashoffset={1-reveal(f,52,65)}/>
 <g opacity={reveal(f,108)}><Lock x={880} y={268} scale={.38}/></g><Text x={46} y={410} size={33}>BEFORE</Text><Text x={854} y={410} size={33} anchor="end">AFTER</Text>
 </Card>
 </>;
 if(i===4)return <>
 <Heading label="Refinancing is a new loan." small="The existing loan is replaced, not automatically repriced."/>
 <g transform={`translate(${key(f,[[0,835],[115,835],[150,753]])} 535)`} opacity={key(f,[[0,1],[110,1],[158,.42]])}><Contract label="OLD LOAN"/><Text x={0} y={220} size={39} anchor="middle">EXISTING</Text></g>
 <g opacity={reveal(f,24)}><Arrow x={991} y={544} length={138}/></g>
 <Show f={f} at={49} x={1308} y={535}><Contract label="NEW LOAN" rate="?%"/><Text x={0} y={220} size={39} anchor="middle">NEW TERMS</Text></Show>
 <Show f={f} at={91} x={1030} y={753}><Text x={0} y={0} size={32} fill={C.muted} anchor="middle" weight={500}>A separate application and decision</Text></Show>
 </>;
 if(i===5)return <>
 <Heading label="Check the whole trade-off." small="A lower headline rate is only one part."/>
 {[['APPROVAL','Can you qualify?'],['CLOSING COSTS','What does it cost?'],['NEW TERM','How long will you pay?']].map(([title,sub],j)=><Show key={title} f={f} at={7+j*31} x={630+j*325} y={410}><Card x={0} y={0} w={294} h={330} fill={j===1?C.mint:C.paper}><Text x={147} y={73} size={31} anchor="middle">{title}</Text>{j===1?<Coin x={147} y={151}/>:j===0?<g><circle cx={147} cy={151} r={47} fill={C.yellow} stroke={C.ink} strokeWidth={5}/><path d="M123 150l17 19 36-38" fill="none" stroke={C.ink} strokeWidth={7} strokeLinecap="round"/></g>:<g><rect x={105} y={105} width={86} height={91} rx={10} fill={C.yellow} stroke={C.ink} strokeWidth={5}/><path d="M105 129h86 M123 94v22 M172 94v22" stroke={C.ink} strokeWidth={5}/><Text x={148} y={177} size={39} anchor="middle">?</Text></g>}<Text x={147} y={267} size={23} anchor="middle" weight={500}>{sub}</Text></Card></Show>)}
 </>;
 if(i===6)return <>
 <Heading label="Fixed rate ≠ fixed total bill." small="Taxes and insurance may change your escrow payment."/>
 <Show f={f} at={5} x={827} y={545}><House scale={1.25}/></Show>
 <Card x={1101} y={337} w={433} h={465}><Text x={216} y={62} size={38} anchor="middle">TOTAL MONTHLY BILL</Text>
 <rect x={45} y={101} width={343} height={106} rx={16} fill={C.mint}/><Text x={216} y={147} size={35} anchor="middle">PRINCIPAL + INTEREST</Text><Text x={216} y={184} size={28} anchor="middle" weight={500}>scheduled amount</Text>
 <g transform={`translate(0 ${key(f,[[36,100],[62,0],[102,-12],[142,0]])})`} opacity={reveal(f,36)}><rect x={45} y={221} width={343} height={112} rx={16} fill="#F2C9AA"/><Text x={216} y={266} size={35} anchor="middle">TAXES + INSURANCE</Text><Text x={216} y={309} size={31} anchor="middle">CAN CHANGE</Text></g><Text x={216} y={405} size={28} anchor="middle" weight={500}>Other fees may also apply.</Text>
 </Card>
 </>;
 return <>
 <Text x={606} y={234} size={68}>THE BACKDROP CHANGES.</Text><Text x={606} y={322} size={71}>YOUR CONTRACT DOESN’T.</Text>
 <g opacity={1-reveal(f,12,65)}><Arrow x={818} y={440} length={170} down color={C.coral}/><Text x={754} y={430} size={65}>%</Text></g>
 <g transform={`translate(${key(f,[[0,1275],[72,1118]])} 574) scale(${key(f,[[0,1],[72,1.25]])})`}><Contract/><Lock x={0} y={68} scale={.55}/></g>
 <Show f={f} at={75} x={895} y={783}><Text x={0} y={0} size={40} anchor="middle" fill={C.teal}>Understand the loan you signed.</Text></Show>
 </>;
}
export const Pilot:React.FC=()=>{
 const frame=useCurrentFrame();const i=Math.max(0,timeline.findIndex(t=>frame>=t.from&&frame<t.endFrame));const item=timeline[i],f=frame-item.from;
 useLayoutEffect(()=>{
  const clipped:Array<string>=[];
  document.querySelectorAll('svg text').forEach(el=>{
   const text=el as SVGGraphicsElement,box=text.getBBox(),matrix=text.getCTM();
   if(!matrix)return;
   const a=new DOMPoint(box.x,box.y).matrixTransform(matrix),b=new DOMPoint(box.x+box.width,box.y+box.height).matrixTransform(matrix);
   if(a.x<0||b.x>1920||a.y<0||b.y>1080)clipped.push(el.textContent??'');
  });
  console.log('TEXT_QA '+JSON.stringify({frame,clipped}));
 },[frame]);
 const zoom=pushIn(f,item.endFrame-item.from,.025).scale; const line=timeline.find(t=>frame/30>=t.voiceStart&&frame/30<t.voiceEnd);
 // Sentence-aligned summary captions; exact narration is in the bundled SRT.
 return <AbsoluteFill style={{backgroundColor:C.cream}}><Audio src={staticFile('audio/mix.wav')}/>
 <svg viewBox="0 0 1920 1080" width="1920" height="1080">
 <g transform={`translate(960 540) scale(${zoom}) translate(-960 -540)`}><Environment/>
 <Scene i={i} f={f}/><Character x={339} y={300} scale={1.23} f={f} pose={poses[i]} from={poses[Math.max(0,i-1)]} expression={expressions[i]}/>
 </g>
 <rect x={65} y={54} width={380} height={58} rx={29} fill={C.ink}/><Text x={255} y={94} size={28} fill={C.cream} anchor="middle">NORI • MONEY EXPLAINED</Text>
 <Text x={1835} y={94} size={28} fill={C.muted} anchor="end" weight={500}>ORIGINAL PILOT / U.S. FIXED-RATE</Text>
 <Text x={83} y={892} size={26} fill={C.muted} weight={500}>Sources: Federal Reserve Consumer Help • CFPB  |  No current rate forecast</Text>
 <rect x={65} y={932} width={1790} height={106} rx={25} fill={C.ink}/><Text x={960} y={1000} size={58} fill={C.paper} anchor="middle">{line?.caption??item.caption}</Text>
 <rect x={65} y={1056} width={1790*frame/(DURATION-1)} height={5} rx={2} fill={C.teal}/>
 </svg></AbsoluteFill>;
};
export const CharacterBoard:React.FC=()=> <AbsoluteFill style={{backgroundColor:C.cream}}><svg width="1920" height="1080" viewBox="0 0 1920 1080"><rect width={1920} height={1080} fill={C.cream}/><Text x={65} y={79} size={47}>Nori — one authored rig, three poses × five expressions</Text>
 {(['shrug','point','hold'] as PoseName[]).flatMap((pose,row)=>(['curious','concerned','explain','pleased','neutral'] as Expression[]).map((e,col)=><g key={`${pose}-${e}`}><Character x={190+col*375} y={157+row*304} scale={.57} f={40} pose={pose} expression={e}/><Text x={190+col*375} y={430+row*303} size={24} anchor="middle">{pose} / {e}</Text></g>))}
 </svg></AbsoluteFill>;
export const AssetBoard:React.FC=()=> <AbsoluteFill><svg width="1920" height="1080" viewBox="0 0 1920 1080"><Environment/><Text x={500} y={90} size={54}>Original editable finance kit</Text><House x={600} y={500} scale={1.7}/><Bank x={975} y={500} scale={1.4}/><Contract x={1370} y={495} scale={1.3}/><Lock x={840} y={740}/><Coin x={1125} y={745} scale={1.4}/></svg></AbsoluteFill>;
