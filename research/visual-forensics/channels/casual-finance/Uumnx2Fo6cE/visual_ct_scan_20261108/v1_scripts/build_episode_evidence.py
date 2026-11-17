# One sequential decode: for every episode, build native-frame review row (tiles from decoded frames, downscaled), net-change metrics, stable frame JPG.
import cv2, sys, csv, numpy as np, pandas as pd
from collections import deque
F=sys.argv[1]
E=pd.read_csv('tables/episodes_v2.csv'); n_total=int(pd.read_csv('FULL_FRAME_MEASUREMENTS.csv',usecols=['frame']).frame.max())+1
eps=E.to_dict('records')
TW,TH=256,144; ROWS=8; NT=7
need_at={}  # frame index at which episode is processed
for k,e in enumerate(eps): need_at.setdefault(min(e['end']+9,n_total-1),[]).append(k)
ring=deque(maxlen=100); out=[]; rows_img=[]
def get(i):
    for j,f in ring:
        if j==i: return f
    return None
def tile(fr,label):
    t=cv2.resize(fr,(TW,TH),interpolation=cv2.INTER_AREA)
    cv2.rectangle(t,(0,0),(TW,13),(255,255,255),-1); cv2.putText(t,label,(2,10),cv2.FONT_HERSHEY_SIMPLEX,0.36,(0,0,200),1); return t
def process(k):
    e=eps[k]; a,b,L=e['start'],e['end'],e['n']
    nxt=eps[k+1]['start'] if k+1<len(eps) else n_total
    pre1=max(a-1,0); post1=min(b+1,n_total-1)
    stable=max(post1,min(b+8,nxt-1,n_total-1))
    gp=cv2.cvtColor(get(pre1),cv2.COLOR_BGR2GRAY).astype(np.int16); gs=cv2.cvtColor(get(stable),cv2.COLOR_BGR2GRAY).astype(np.int16)
    d=np.abs(gp-gs); m=d>=24; netf=float(m.mean())
    if m.any():
        ys,xs=np.nonzero(m); bx=(xs.min()/640,ys.min()/360,(xs.max()+1)/640,(ys.max()+1)/360)
    else: bx=(0,0,0,0)
    cp=gp<240; cs=gs<240; u=(cp|cs).sum(); iou=float((cp&cs).sum()/u) if u else 1.0
    if L<=2: ids=[('pre-4',max(a-4,0)),('pre-1',pre1),('chg',a),('chg+1' if L==2 else 'post+1',min(a+1,n_total-1) if L==2 else post1),('post+1',post1),('stable',stable)]
    else:
        q=[a,a+(b-a)//3,a+2*(b-a)//3,b]; ids=[('pre-1',pre1)]+[(f'm{j}',x) for j,x in enumerate(q)]+[('stable',stable)]
    ts=[tile(get(i),f"{l} f{i} {float(PTS[i]):.3f}s") for l,i in ids]
    ov=cv2.cvtColor(cv2.convertScaleAbs(gs.astype(np.uint8),alpha=0.4,beta=130),cv2.COLOR_GRAY2BGR); ov[m]=(0,0,255)
    ov=cv2.resize(ov,(TW,TH),interpolation=cv2.INTER_AREA)
    if m.any(): cv2.rectangle(ov,(int(bx[0]*TW),int(bx[1]*TH)),(int(bx[2]*TW),int(bx[3]*TH)),(0,160,0),1)
    ts.append(tile(ov,f"net diff {netf*100:.1f}%"))
    while len(ts)<NT: ts.append(np.full((TH,TW,3),200,np.uint8))
    row=np.hstack(ts[:NT]); hdr=np.full((15,row.shape[1],3),235,np.uint8)
    cv2.putText(hdr,f"EP{e['ep']:04d} {e['cls']} f{a}-{b} ({L}f) {float(PTS[a]):.3f}-{float(PTS[b]):.3f}s",(3,11),cv2.FONT_HERSHEY_SIMPLEX,0.42,(150,0,0),1)
    rows_img.append(np.vstack([hdr,row]))
    cv2.imwrite(f"frames/ep_stable/e{e['ep']:04d}.jpg",get(stable),[cv2.IMWRITE_JPEG_QUALITY,80])
    e2=dict(ep=e['ep'],pre_frame=pre1,stable_frame=stable,net_changed_frac=round(netf,5),net_bbox=';'.join(f'{v:.3f}' for v in bx),content_iou=round(iou,4),frames_viewed=';'.join(f"{l}:f{i}" for l,i in ids),
            sheet=f"boundary_sheets/bsheet_{(k//ROWS)+1:03d}.jpg",sheet_row=k%ROWS)
    out.append(e2)
PTS=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv',usecols=['pts_time']).pts_time.values
cap=cv2.VideoCapture(F); i=0; first_saved=False
sheet_no=0
while True:
    ok,f=cap.read()
    if not ok: break
    f=cv2.resize(f,(640,360),interpolation=cv2.INTER_AREA); ring.append((i,f))
    if i==min(8,eps[0]['start']-1) and not first_saved:
        cv2.imwrite('frames/ep_stable/e0000.jpg',f,[cv2.IMWRITE_JPEG_QUALITY,80]); first_saved=True
    for k in need_at.get(i,[]):
        process(k)
        if len(rows_img)==ROWS or (k==len(eps)-1):
            sheet_no+=1; cv2.imwrite(f'boundary_sheets/bsheet_{sheet_no:03d}.jpg',np.vstack(rows_img),[cv2.IMWRITE_JPEG_QUALITY,80]); rows_img=[]
    i+=1
if rows_img: sheet_no+=1; cv2.imwrite(f'boundary_sheets/bsheet_{sheet_no:03d}.jpg',np.vstack(rows_img),[cv2.IMWRITE_JPEG_QUALITY,80])
pd.DataFrame(out).to_csv('tables/episode_evidence.csv',index=False); print(i,'frames',len(out),'episodes',sheet_no,'sheets')
