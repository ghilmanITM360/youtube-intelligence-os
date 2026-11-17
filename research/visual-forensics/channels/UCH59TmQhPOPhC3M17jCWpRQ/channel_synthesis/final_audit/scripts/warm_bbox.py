# warm_bbox.py SRC x0 y0 x1 y1 f_start f_end : height of rows inside ROI where >=300 px are warm (R>G+8) -- picture panel on green board. MEASURED.
import cv2,sys,numpy as np
src=sys.argv[1];x0,y0,x1,y1,a,b=map(int,sys.argv[2:8])
cap=cv2.VideoCapture(src);cap.set(cv2.CAP_PROP_POS_FRAMES,max(0,a-60));i=int(cap.get(cv2.CAP_PROP_POS_FRAMES));out=[]
while i<=b:
    ok,im=cap.read()
    if not ok:break
    if i>=a:
        roi=im[y0:y1,x0:x1].astype(int);m=(roi[:,:,2]>roi[:,:,1]+8);r=np.nonzero(m.sum(1)>=300)[0]
        out.append(f"{i}:{int(r.max()-r.min()+1) if len(r) else 0}")
    i+=1
print(' '.join(out))
