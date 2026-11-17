# Second detector for white-card/low-pixel-change cuts. Per consecutive frame pair at 320x180 gray:
# ink = gray<200 mask; ink_iou_change = 1-IoU(ink_prev,ink_cur); ink_area = fraction ink; hist_l1 = 0.5*L1 of 32-bin gray histograms; colour_hist_l1 = same on 8x8x8 BGR (as 512 bins).
import cv2,csv,sys,numpy as np
cap=cv2.VideoCapture(sys.argv[1]);out=csv.writer(open(sys.argv[2],'w',newline=''));out.writerow(['frame','ink_area','ink_iou_change','hist_l1','colour_hist_l1'])
pi=None;ph=None;pc=None;i=0
while True:
    ok,fr=cap.read()
    if not ok:break
    sm=cv2.resize(fr,(320,180),interpolation=cv2.INTER_AREA);g=cv2.cvtColor(sm,cv2.COLOR_BGR2GRAY)
    ink=g<200;h=np.bincount((g>>3).ravel(),minlength=32)/g.size
    c=cv2.calcHist([sm],[0,1,2],None,[8,8,8],[0,256]*3).ravel();c/=c.sum()
    if pi is None: row=[0,0,0]
    else:
        u=(ink|pi).sum();iou=(ink&pi).sum()/u if u else 1.0
        row=[round(1-float(iou),4),round(float(0.5*np.abs(h-ph).sum()),4),round(float(0.5*np.abs(c-pc).sum()),4)]
    out.writerow([i,round(float(ink.mean()),4)]+row);pi=ink;ph=h;pc=c;i+=1
print(i,'frames')
