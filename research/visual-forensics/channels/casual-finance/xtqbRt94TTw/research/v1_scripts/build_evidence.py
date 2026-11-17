# One sequential decode. Builds multi-tier candidate list (EP = episodes_v2 tier T1; SUB = tiers T2/T3/T4 sub-threshold clusters outside episodes)
# and a >=960x540 evidence image per candidate with native-resolution bbox crops. Nothing is inferred from unreadable text.
import cv2,sys,numpy as np,pandas as pd
from collections import deque
F=sys.argv[1]
d=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv');E=pd.read_csv('tables/episodes_v2.csv');N=len(d);PTS=d.pts_time.values
inep=np.zeros(N,bool)
for r in E.itertuples(): inep[max(r.start-1,0):r.end+2]=True
base=(~inep)&(d.pict!='I').values
T2=base&(d.px_diff_ge150>=1).values&(d.px_diff_ge12>=45).values
T3=base&~T2&(d.px_diff_ge12>=450).values&(d.px_diff_ge150==0).values
T4=base&~T2&~T3&(d.px_diff_ge6>=3375).values
tier=np.where(T2,2,np.where(T3,3,np.where(T4,4,0)))
cands=[]
for r in E.itertuples(): cands.append(dict(id=f'EP{r.ep:04d}',source='EP',tier='T1',start=r.start,end=r.end,cls=r.cls))
idx=np.nonzero(tier>0)[0];cl=[];s=None
for i in idx:
    if s is not None and i-p<=3:p=i
    else:
        if s is not None:cl.append((s,p))
        s=i;p=i
if s is not None:cl.append((s,p))
for k,(a,b) in enumerate(cl,1):
    t=int(tier[a:b+1][tier[a:b+1]>0].min());cands.append(dict(id=f'SUB{k:03d}',source='SUB',tier=f'T{t}',start=a,end=b,cls='SUB_THRESHOLD'))
cands.sort(key=lambda c:(c['start'],c['id']))
for k,c in enumerate(cands):
    c['nxt']=cands[k+1]['start'] if k+1<len(cands) else N
need={}
for k,c in enumerate(cands): need.setdefault(min(c['end']+9,N-1),[]).append(k)
ring=deque(maxlen=300);out=[]
def get(i):
    for j,f in ring:
        if j==i:return f
def lab(img,t,sc=0.6):
    cv2.rectangle(img,(0,0),(img.shape[1],22),(255,255,255),-1);cv2.putText(img,t,(4,16),cv2.FONT_HERSHEY_SIMPLEX,sc,(0,0,200),1,cv2.LINE_AA);return img
def process(k):
    c=cands[k];a,b=c['start'],c['end'];L=b-a+1
    pre=max(a-1,0);st=max(min(b+1,N-1),min(b+8,c['nxt']-1,N-1))
    P=get(pre);S=get(st);gp=cv2.cvtColor(P,cv2.COLOR_BGR2GRAY).astype(np.int16);gs=cv2.cvtColor(S,cv2.COLOR_BGR2GRAY).astype(np.int16)
    m=np.abs(gp-gs)>=24;netf=float(m.mean());mm=m.copy()
    samp=sorted(set([a,b]+[a+(b-a)*j//4 for j in range(5)]))
    for j in samp:
        if get(j) is not None: mm|=np.abs(gp-cv2.cvtColor(get(j),cv2.COLOR_BGR2GRAY).astype(np.int16))>=24
    if mm.any():
        ys,xs=np.nonzero(mm);x0,x1,y0,y1=int(xs.min()),int(xs.max())+1,int(ys.min()),int(ys.max())+1
    else:x0=x1=y0=y1=0
    cp=gp<240;cs=gs<240;u=(cp|cs).sum();iou=float((cp&cs).sum()/u) if u else 1.0
    big=lambda im:cv2.resize(im,(960,540),interpolation=cv2.INTER_AREA)
    A=big(P).copy();B=big(S).copy()
    if mm.any():
        for im in (A,B):cv2.rectangle(im,(int(x0*.5),int(y0*.5)),(int(x1*.5),int(y1*.5)),(0,160,0),2)
    lab(A,f"{c['id']} {c['tier']} {c['cls']} PRE f{pre} {PTS[pre]:.3f}s");lab(B,f"STABLE f{st} {PTS[st]:.3f}s  frames f{a}-{b} ({L}f)")
    row1=np.hstack([A,B])
    cx0=max(0,min(1920-640,(x0+x1)//2-320));cy0=max(0,min(1080-360,(y0+y1)//2-180))
    cw=min(640,max(x1-x0+48,200)) if mm.any() else 640;ch=min(360,max(y1-y0+48,120)) if mm.any() else 360
    cx0=max(0,min(1920-cw,(x0+x1)//2-cw//2));cy0=max(0,min(1080-ch,(y0+y1)//2-ch//2))
    if not mm.any():cx0,cy0,cw,ch=640,360,640,360
    last=get(b);crops=[]
    for im,l in ((P,'native crop PRE'),(last,f'native crop f{b}'),(S,'native crop STABLE')):
        cr=im[cy0:cy0+ch,cx0:cx0+cw].copy();cr=np.pad(cr,((0,360-cr.shape[0]),(0,640-cr.shape[1]),(0,0)),constant_values=200);crops.append(lab(cr,f"{l} @({cx0},{cy0}) {cw}x{ch}",0.5))
    ov=cv2.cvtColor(cv2.convertScaleAbs(gs.astype(np.uint8),alpha=0.4,beta=130),cv2.COLOR_GRAY2BGR);ov[mm]=(0,0,255);ov=lab(cv2.resize(ov,(640,360),interpolation=cv2.INTER_AREA),f"net diff {netf*100:.2f}%",0.5)
    row2=np.hstack(crops+[ov])[:, :1920]
    rows=[row1,row2]
    if L>2:
        mids=[a+(b-a)*j//3 for j in range(4)];ts=[lab(cv2.resize(get(j),(480,270),interpolation=cv2.INTER_AREA),f"f{j} {PTS[j]:.3f}s",0.5) for j in mids]
        rows.append(np.hstack(ts))
    W=1920;rows=[np.pad(r,((0,0),(0,W-r.shape[1]),(0,0)),constant_values=235) for r in rows]
    cv2.imwrite(f"evidence/{c['id']}.jpg",np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,82])
    cv2.imwrite(f"frames/stable/{c['id']}.jpg",big(S),[cv2.IMWRITE_JPEG_QUALITY,82])
    out.append(dict(id=c['id'],source=c['source'],tier=c['tier'],cls=c['cls'],start=a,end=b,n=L,pts_start=round(float(PTS[a]),4),pts_end=round(float(PTS[b]),4),pre_frame=pre,stable_frame=st,net_changed_frac=round(netf,5),
        diff_bbox=f'{x0};{y0};{x1};{y1}',content_iou=round(iou,4),peak_n150=int(d.px_diff_ge150[a:b+1].max()),peak_frac=round(float(d.changed_frac_thr10_320[a:b+1].max()),4),has_I=bool((d.pict[a:b+1]=='I').any()),evidence=f"evidence/{c['id']}.jpg"))
cap=cv2.VideoCapture(F);i=0
while True:
    ok,f=cap.read()
    if not ok:break
    ring.append((i,f))
    for k in need.get(i,[]):process(k)
    i+=1
pd.DataFrame(out).to_csv('tables/candidate_evidence.csv',index=False);print(i,'frames',len(out),'candidates',sum(1 for c in cands if c['source']=='SUB'),'sub')
