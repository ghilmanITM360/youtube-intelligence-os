import csv,cv2,numpy as np,sys
V=sys.argv[1]
C=[c for c in csv.DictReader(open('tables/candidates.csv'))]
sel=[c for c in C if (c['tier']=='A' and int(c['id'][1:])<=36) or c['tier']=='B']
need={}
for c in sel:
    a,b=int(c['start']),int(c['end']); fr=[max(0,a-1),a] + ([ (a+b)//2 ] if b>a else []) + [min(14646,b+1)]
    c['frames']=sorted(set(fr)); [need.setdefault(f,None) for f in c['frames']]
cap=cv2.VideoCapture(V); i=0; mx=max(need)
while i<=mx:
    ok,fr=cap.read()
    if not ok: break
    if i in need: need[i]=cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA)
    i+=1
rows=[]
for c in sel:
    ims=[]
    for f in c['frames']:
        im=need[f].copy(); cv2.rectangle(im,(0,0),(210,22),(0,0,0),-1); cv2.putText(im,f"f{f} t={f*1001/30000:.3f}",(4,16),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),1); ims.append(im)
    while len(ims)<4: ims.append(np.zeros((270,480,3),np.uint8))
    row=np.hstack(ims); cv2.putText(row,f"{c['id']} {c['kind']} start={c['start']} end={c['end']}",(4,262),cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,255),2); rows.append(row)
import os; os.makedirs('frames/montages',exist_ok=True)
for k in range(0,len(rows),5):
    cv2.imwrite(f'frames/montages/M{k//5+1:02d}.jpg',np.vstack(rows[k:k+5]),[cv2.IMWRITE_JPEG_QUALITY,80])
print(len(sel),'candidates',(len(rows)+4)//5,'montages')
