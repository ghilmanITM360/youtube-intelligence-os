# Native consecutive-frame windows around localised hidden changes (X069: 10347-10356, X088: 13352-13361). External output frames/montages7/N_*.jpg
import cv2,numpy as np,sys
W={'X069':range(10347,10357),'X088':range(13352,13362)}
need={f for r in W.values() for f in r};fr={};cap=cv2.VideoCapture(sys.argv[1]);i=0
while i<=max(need):
    ok,im=cap.read()
    if not ok:break
    if i in need: fr[i]=cv2.resize(im,(384,216),interpolation=cv2.INTER_AREA)
    i+=1
for k,r in W.items():
    ims=[]
    for f in r:
        a=fr[f].copy();cv2.rectangle(a,(0,0),(110,16),(0,0,0),-1);cv2.putText(a,f"f{f}",(3,12),cv2.FONT_HERSHEY_SIMPLEX,.45,(255,255,255),1);ims.append(a)
    cv2.imwrite(f'frames/montages7/N_{k}.jpg',np.vstack([np.hstack(ims[:5]),np.hstack(ims[5:])]),[cv2.IMWRITE_JPEG_QUALITY,82])
