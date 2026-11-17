# One row per boundary between consecutive v2 states: [mid of state k][last frame of k][first frame of k+1][mid of state k+1]. Boundary id = B-k (V{k}|V{k+1}).
import csv,cv2,numpy as np,sys,os
S=list(csv.DictReader(open('tables/states_v2_draft.csv')));rows=[]
for k in range(len(S)-1):
    a,b=S[k],S[k+1];m1=(int(a['start'])+int(a['end']))//2;m2=(int(b['start'])+int(b['end']))//2
    rows.append(dict(id=f"X{k+1:03d}",left=a['state_v2'],right=b['state_v2'],fr=[m1,int(a['end']),int(b['start']),m2],entry=b['entry'],kinds=a['kind'][:6]+'|'+b['kind'][:6]))
need={}
for r in rows: [need.setdefault(f,None) for f in r['fr']]
cap=cv2.VideoCapture(sys.argv[1]);i=0
while i<=max(need):
    ok,fr=cap.read()
    if not ok:break
    if i in need: need[i]=cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA)
    i+=1
os.makedirs('frames/montages6',exist_ok=True);out=[]
for r in rows:
    ims=[]
    for lab,f in zip(['midL','endL','startR','midR'],r['fr']):
        im=need[f].copy();cv2.rectangle(im,(0,0),(260,22),(0,0,0),-1);cv2.putText(im,f"{lab} f{f} t={f*1001/30000:.2f}",(4,16),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),1);ims.append(im)
    row=np.hstack(ims);cv2.putText(row,f"{r['id']} {r['left']}|{r['right']} entry={r['entry']} {r['kinds']}",(4,262),cv2.FONT_HERSHEY_SIMPLEX,.55,(0,255,255),2);out.append(row)
for k in range(0,len(out),5): cv2.imwrite(f'frames/montages6/X{k//5+1:02d}.jpg',np.vstack(out[k:k+5]),[cv2.IMWRITE_JPEG_QUALITY,78])
csv.writer(open('tables/v2_boundaries.csv','w',newline='')).writerows([['id','left','right','entry','frames']]+[[r['id'],r['left'],r['right'],r['entry'],'|'.join(map(str,r['fr']))] for r in rows])
print(len(rows),'boundaries',(len(out)+4)//5,'montages')
