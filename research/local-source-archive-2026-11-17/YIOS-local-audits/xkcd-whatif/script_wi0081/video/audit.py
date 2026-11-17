"""Text audit from two renders: art.mp4 (text hidden) and txt.mp4 (only text, 50% so stacked text goes darker). 8 fps, 540x960."""
import subprocess, numpy as np, sys
W,H,FPS=540,960,12
def frames(p):
    c=subprocess.Popen(['ffmpeg','-v','error','-i',p,'-vf',f'fps={FPS},scale={W}:{H}:flags=area,format=gray','-f','rawvideo','-'],stdout=subprocess.PIPE)
    n=W*H
    while True:
        b=c.stdout.read(n)
        if len(b)<n: break
        yield np.frombuffer(b,dtype=np.uint8).reshape(H,W)
def dil(m,it=2):
    for _ in range(it):
        o=m.copy(); o[1:]|=m[:-1]; o[:-1]|=m[1:]; o[:,1:]|=m[:,:-1]; o[:,:-1]|=m[:,1:]; m=o
    return m
C=30  # cell size at half res
ev=[]
for i,(a,t) in enumerate(zip(frames('audit/art.mp4'),frames('audit/txt.mp4'))):
    T=i/FPS
    tm=t<215
    if tm.sum()<30: continue
    ink=a<150
    hit=dil(tm,2)&ink
    dbl=t<95
    edge=np.zeros_like(tm); edge[:4]=edge[-4:]=True; edge[:,:4]=edge[:,-4:]=True
    clip=tm&edge
    for k,m,th in (('ART',hit,14),('TEXT',dbl,18),('CLIP',clip,4)):
        if m.sum()<th: continue
        for cy in range(0,H,C):
            for cx in range(0,W,C):
                c=int(m[cy:cy+C,cx:cx+C].sum())
                if c>=th: ev.append((T,k,(cx*2,cy*2,(cx+C)*2,(cy+C)*2),c))
runs=[]
for T,k,bb,m in sorted(ev,key=lambda e:(e[1],e[0])):
    for r in runs:
        if r['k']==k and T-r['t1']<=0.3 and abs(r['bb'][0]-bb[0])<=70 and abs(r['bb'][1]-bb[1])<=70:
            r['t1']=T; r['m']=max(r['m'],m); r['n']+=1; r['bb']=(min(r['bb'][0],bb[0]),min(r['bb'][1],bb[1]),max(r['bb'][2],bb[2]),max(r['bb'][3],bb[3])); break
    else: runs.append(dict(k=k,t0=T,t1=T,bb=bb,m=m,n=1))
runs.sort(key=lambda r:r['t0'])
for r in runs: print(f"{r['k']:5s} {r['t0']:6.2f}-{r['t1']:6.2f} n={r['n']:2d} px={r['m']:4d} bbox={r['bb']}")
print(len(runs),'runs')
