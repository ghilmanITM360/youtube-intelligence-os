import cv2,numpy as np,csv,sys
SRC="/Users/ghilmankhan/Downloads/videos in mp3/BarelyEvolved-MP4/The Worst Time in History to Be Born as a Human [uPQcyookL0Y].mp4"
W={"W047":(8420,8452),"W081":(13158,13180),"W085b":(13990,14008)}
cap=cv2.VideoCapture(SRC);rows=[]
for k,(a,b) in W.items():
    cap.set(cv2.CAP_PROP_POS_FRAMES,a-1);ok,p=cap.read();p=p.astype(np.float32)
    for n in range(a,b+1):
        ok,f=cap.read();ff=f.astype(np.float32)
        rows.append([k,n,round(float(ff.mean()),3),round(float(np.abs(ff-p).mean()),3),round(float((np.abs(ff-p).max(2)>24).mean()),5)])
        cv2.imwrite(f"frames/native/{k}_{n}.png",f);p=ff
cap.release()
with open("tables/k_boundary_native_metrics.csv","w",newline="") as o:
    w=csv.writer(o);w.writerow("window,frame,mean_luma,mad_vs_prev,frac_px_changed_gt24".split(","));w.writerows(rows)
for r in rows:print(*r)
