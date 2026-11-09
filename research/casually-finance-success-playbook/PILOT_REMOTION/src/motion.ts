export type Point = {x:number;y:number};
export type FrameKey = readonly [number,number];
export const clamp=(v:number)=>Math.max(0,Math.min(1,v));
export const smooth=(v:number)=>{const t=clamp(v);return t*t*(3-2*t);};
export function key(frame:number,keys:readonly FrameKey[]):number{
 if(frame<=keys[0][0])return keys[0][1];
 for(let i=1;i<keys.length;i++)if(frame<=keys[i][0]){
  const [a,v]=keys[i-1],[b,w]=keys[i];return v+(w-v)*smooth((frame-a)/(b-a));
 }
 return keys.at(-1)![1];
}
export const reveal=(f:number,start:number,length=18)=>smooth((f-start)/length);
export const pop=(f:number,start:number)=>key(f,[[start,0],[start+9,1.05],[start+17,1]]);
export const camera=(f:number,length:number,amount=.035)=>1+amount*smooth(f/length);
export type PoseName='shrug'|'point'|'hold';
export const POSES={
 shrug:{hipY:226,leftUpper:100,leftElbow:-18,rightUpper:-100,rightElbow:18,head:-5},
 point:{hipY:224,leftUpper:12,leftElbow:-34,rightUpper:-108,rightElbow:10,head:3},
 hold:{hipY:225,leftUpper:-12,leftElbow:-65,rightUpper:12,rightElbow:65,head:-2},
} as const;
export function poseAt(f:number,name:PoseName,from:PoseName='hold'){
 const t=smooth(f/24),p=POSES[name],q=POSES[from];
 return Object.fromEntries(Object.keys(p).map(k=>[k,q[k as keyof typeof q]+(p[k as keyof typeof p]-q[k as keyof typeof q])*t])) as Record<keyof typeof p,number>;
}
export function solveLeg(hip:Point,foot:Point,a:number,b:number,side:number):Point{
 const dx=foot.x-hip.x,dy=foot.y-hip.y,d=Math.hypot(dx,dy);
 if(d>a+b || d<Math.abs(a-b))throw new Error('Unreachable foot anchor');
 const along=(a*a-b*b+d*d)/(2*d),off=Math.sqrt(Math.max(0,a*a-along*along));
 return {x:hip.x+dx*along/d+side*dy*off/d,y:hip.y+dy*along/d-side*dx*off/d};
}
