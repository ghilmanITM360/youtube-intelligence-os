import cv2,sys,numpy as np,csv
cap=cv2.VideoCapture(sys.argv[1]);i=0;rows=[]
while True:
    ok,f=cap.read()
    if not ok:break
    b=f[708:720]            # bottom 12 rows
    hsv=cv2.cvtColor(b,cv2.COLOR_BGR2HSV)
    y=((hsv[...,0]>=20)&(hsv[...,0]<=35)&(hsv[...,1]>=150)&(hsv[...,2]>=180))
    col=y.any(axis=0)
    xs=np.nonzero(col)[0]
    rows.append((i,int(y.sum()),int(xs.max()+1) if len(xs) else 0,int(xs.min()) if len(xs) else 0))
    i+=1
with open('tables/progress_bar.csv','w',newline='') as fh:
    w=csv.writer(fh);w.writerow(['frame','yellow_px_bottom12','bar_right_x','bar_left_x']);w.writerows(rows)
print(i)
