# Review of frame clusters below the episode thresholds (px>=150 count 8..39 with px>=12 >=100), outside any episode window.
import pandas as pd, numpy as np, cv2, sys
from collections import deque
F=sys.argv[1]; d=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv'); E=pd.read_csv('tables/episodes_classified.csv')
inep=np.zeros(len(d),bool)
for r in E.itertuples(): inep[max(r.start-1,0):r.end+2]=True
low=(~inep)&(d.pict!='I')&(d.px_diff_ge150>=8)&(d.px_diff_ge12>=100)
idx=np.nonzero(low.values)[0];cl=[];s=None
for i in idx:
    if s is not None and i-p<=3:p=i
    else:
        if s is not None:cl.append((s,p))
        s=i;p=i
if s is not None:cl.append((s,p))
need={}
for k,(a,b) in enumerate(cl):
    for j in {max(a-1,0),a,b,min(b+1,len(d)-1),min(b+6,len(d)-1)}: need.setdefault(j,[]).append(k)
cap=cv2.VideoCapture(F);i=0;fr={}
while i<=max(need):
    ok,f=cap.read()
    if not ok:break
    if i in need: fr[i]=f
    i+=1
rows=[];info=[]
for k,(a,b) in enumerate(cl):
    pre=fr[max(a-1,0)];post=fr[min(b+6,len(d)-1)];mid=fr[a]
    gp=cv2.cvtColor(pre,cv2.COLOR_BGR2GRAY).astype(int);gq=cv2.cvtColor(post,cv2.COLOR_BGR2GRAY).astype(int);g1=cv2.cvtColor(fr[b],cv2.COLOR_BGR2GRAY).astype(int)
    m=np.abs(gp-g1)>=24;m2=np.abs(gp-gq)>=24
    mm=m|m2
    if mm.any():
        ys,xs=np.nonzero(mm);x0,x1,y0,y1=xs.min(),xs.max()+1,ys.min(),ys.max()+1
    else:x0=x1=y0=y1=0
    cx=max(0,min(1280-400,(x0+x1)//2-200));cy=max(0,min(720-225,(y0+y1)//2-112))
    def crop(im):return cv2.resize(im[cy:cy+225,cx:cx+400],(320,180))
    ov=cv2.cvtColor(cv2.convertScaleAbs(gq.astype(np.uint8),alpha=0.4,beta=130),cv2.COLOR_GRAY2BGR);ov[m2|m]=(0,0,255)
    tiles=[cv2.resize(pre,(256,144)),cv2.resize(mid,(256,144)),cv2.resize(fr[b],(256,144)),cv2.resize(post,(256,144)),cv2.resize(ov,(256,144)),crop(pre),crop(fr[b])]
    labs=[f"pre f{max(a-1,0)}",f"first f{a}",f"last f{b}",f"post f{min(b+6,len(d)-1)}","net diff",f"crop pre",f"crop f{b}"]
    row=[]
    for t,l in zip(tiles,labs):
        t=cv2.resize(t,(256,144)) if t.shape[1]!=256 else t
        cv2.putText(t,l,(2,10),cv2.FONT_HERSHEY_SIMPLEX,0.36,(0,0,200),1);row.append(t)
    hdr=np.full((15,256*7,3),235,np.uint8);cv2.putText(hdr,f"SUB{k+1:03d} f{a}-{b} {float(d.pts_time[a]):.3f}s n150max={int(d.px_diff_ge150[a:b+1].max())} bbox=({x0},{y0})-({x1},{y1})",(3,11),cv2.FONT_HERSHEY_SIMPLEX,0.42,(150,0,0),1)
    rows.append(np.vstack([hdr,np.hstack(row)]))
    info.append(dict(sub_id=f'SUB{k+1:03d}',start=a,end=b,n=b-a+1,pts=float(d.pts_time[a]),n150_max=int(d.px_diff_ge150[a:b+1].max()),n12_max=int(d.px_diff_ge12[a:b+1].max()),diff_bbox=f'{x0};{y0};{x1};{y1}',sheet=f'subthreshold/sub_sheet_{k//6+1:02d}.jpg',row=k%6))
for j in range(0,len(rows),6):cv2.imwrite(f'subthreshold/sub_sheet_{j//6+1:02d}.jpg',np.vstack(rows[j:j+6]),[cv2.IMWRITE_JPEG_QUALITY,80])
pd.DataFrame(info).to_csv('subthreshold/subthreshold_clusters.csv',index=False);print(len(cl),'clusters',(len(rows)+5)//6,'sheets')
