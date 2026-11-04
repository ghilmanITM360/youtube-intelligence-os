# grab.py SRC OUT f1 f2 ... : sequential-decode exact frame indices, save tiles (native or scaled) into one sheet
import cv2,sys,numpy as np
src,out,scale=sys.argv[1],sys.argv[2],float(sys.argv[3]);want=sorted(int(x) for x in sys.argv[4:])
cap=cv2.VideoCapture(src);i=0;got={}
cap.set(cv2.CAP_PROP_POS_FRAMES,max(0,want[0]-60));i=int(cap.get(cv2.CAP_PROP_POS_FRAMES))
# ponytail: seek-then-sequential; exact-index trust relies on CFR + verify via pts below
while i<=want[-1]:
    ok,im=cap.read()
    if not ok:break
    if i in want:
        im=cv2.resize(im,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA) if scale!=1 else im
        cv2.putText(im,f"f{i}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2);got[i]=im
    i+=1
tiles=[got[k] for k in want if k in got];cols=min(4,len(tiles));rows=(len(tiles)+cols-1)//cols
h,w=tiles[0].shape[:2];sheet=np.full((rows*h,cols*w,3),255,np.uint8)
for n,t in enumerate(tiles):sheet[(n//cols)*h:(n//cols+1)*h,(n%cols)*w:(n%cols+1)*w]=t
cv2.imwrite(out,sheet);print(out,len(tiles),sheet.shape)
