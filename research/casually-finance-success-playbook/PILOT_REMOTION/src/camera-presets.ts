import {smooth} from './motion';
/** Pure world transforms. Captions/source strip remain outside this parent. */
export const pushIn=(frame:number,duration:number,amount=.025)=>({scale:1+amount*smooth(frame/duration),x:0,y:0});
export const pullOut=(frame:number,duration:number,amount=.025)=>({scale:1+amount*(1-smooth(frame/duration)),x:0,y:0});
export const panAcross=(frame:number,duration:number,pixels=24)=>({scale:1.03,x:-pixels*smooth(frame/duration),y:0});
