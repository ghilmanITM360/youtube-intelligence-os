# inset_bbox.py SRC x0 y0 x1 y1 thr f_start f_end : bbox of bright (gray>thr) pixels inside a fixed native-res ROI per frame. MEASURED.
import cv2,sys,numpy as np
src=sys.argv[1];x0,y0,x1,y1,thr,a,b=map(int,sys.argv[2:9])
cap=cv2.VideoCapture(src);cap.set(cv2.CAP_PROP_POS_FRAMES,max(0,a-60));i=int(cap.get(cv2.CAP_PROP_POS_FRAMES))
while i<=b:
    ok,im=cap.read()
    if not ok:break
    if i>=a:
        g=cv2.cvtColor(im[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY)>thr;r=np.nonzero(g.sum(1)>20)[0];c=np.nonzero(g.sum(0)>20)[0]
        print(i, (int(r.max()-r.min()+1),int(c.max()-c.min()+1)) if len(r) and len(c) else (0,0))
    i+=1
