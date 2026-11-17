# v4b targeted dense packs for onset-review YES rows that fall strictly inside a v3 state (seq132 W081 f13204, seq148 W085 f13846, seq150 W085 f13993). Output frames/montages10.
import cv2,numpy as np,sys,os,json
SRC=sys.argv[1];os.makedirs('frames/montages10',exist_ok=True)
T={'seq132':13204,'seq148':13846,'seq150':13993}
packs=[]
for k,b in T.items():
    packs.append((f'T_{k}_consec',list(range(b-4,b+5))));packs.append((f'T_{k}_spaced',list(range(b-40,b+41,10))))
need={f for _,fr in packs for f in fr};cap=cv2.VideoCapture(SRC);k=0;D={}
while k<=max(need):
    ok,fr=cap.read()
    if not ok:break
    if k in need:D[k]=cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA)
    k+=1
idx={}
for n,fr in packs:
    ts=[]
    for f in fr:
        im=D[f].copy();cv2.rectangle(im,(0,0),(84,16),(0,0,0),-1);cv2.putText(im,f"f{f}",(3,12),cv2.FONT_HERSHEY_SIMPLEX,.45,(255,255,255),1);ts.append(im)
    cv2.imwrite(f'frames/montages10/{n}.jpg',np.vstack([np.hstack(ts[i:i+3]) for i in range(0,9,3)]),[cv2.IMWRITE_JPEG_QUALITY,85]);idx[n]=fr
json.dump(idx,open('tables/v4b_pack_index.json','w'));print(len(packs))
