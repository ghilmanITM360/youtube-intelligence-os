import cv2, csv, json, subprocess, sys, numpy as np
F=sys.argv[1]
p=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','frame=pts_time,pict_type','-of','csv=p=0',F],capture_output=True,text=True).stdout.strip().split('\n')
pts=[]
for l in p:
    a=l.split(','); pts.append((a[0],a[1] if len(a)>1 else ''))
cap=cv2.VideoCapture(F); prev=None; rows=[]; i=0
while True:
    ok,fr=cap.read()
    if not ok: break
    g=cv2.cvtColor(cv2.resize(fr,(320,180),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY).astype(np.int16)
    if prev is None: d=0; frac=0.0; mad=0.0
    else:
        df=np.abs(g-prev); d=int(df.sum()); frac=float((df>10).mean()); mad=float(df.mean())
    rows.append((i,*(pts[i] if i<len(pts) else ('','')),round(float(g.mean()),2),round(frac,5),round(mad,4)))
    prev=g; i+=1
with open('tables/frame_metrics.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['frame','pts_time','pict','mean_luma','changed_frac_thr10','mean_abs_diff']); w.writerows(rows)
print(i,'frames')
