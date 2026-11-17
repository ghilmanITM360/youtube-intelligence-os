# Single decode pass: low-res (320x180) global metrics + full-res localized diff metrics + colour. Outputs FULL_FRAME_MEASUREMENTS.csv
import cv2, csv, subprocess, sys, numpy as np
F, OUT = sys.argv[1], sys.argv[2]
p = subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','frame=pts_time,pict_type','-of','csv=p=0',F],capture_output=True,text=True).stdout.strip().split('\n')
meta=[[x for x in l.split(',') if x] for l in p]
cap=cv2.VideoCapture(F); pg=None; pl=None; rows=[]; i=0
k=np.ones((3,3),np.uint8)
while True:
    ok,fr=cap.read()
    if not ok: break
    g=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
    sm=cv2.resize(g,(320,180),interpolation=cv2.INTER_AREA).astype(np.int16)
    mb,mg,mr=[float(x) for x in fr.reshape(-1,3).mean(0)]
    sat=float(cv2.cvtColor(cv2.resize(fr,(160,90),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2HSV)[...,1].mean())
    ed=float((cv2.Canny(sm.astype(np.uint8),50,150)>0).mean())
    m=meta[i] if i<len(meta) else ['','']
    m=m+['']*(2-len(m))
    if m[0] in ('I','P','B'): m=[m[1],m[0]]
    if pg is None:
        row=[0,0,0,0,0,0,0,0,0,0]
    else:
        df=np.abs(sm-pl); frac=float((df>10).mean()); mad=float(df.mean())
        d=cv2.absdiff(g,pg); m6=d>=6; n6=int(m6.sum()); n12=int((d>=12).sum()); mx=int(d.max()); n150=int((d>=150).sum())
        if n6:
            edg=cv2.dilate(cv2.Canny(g,30,90),k,iterations=2)>0
            ef=float((m6&edg).sum()/n6)
            ys,xs=np.nonzero(m6); bb=int((xs.max()-xs.min()+1)*(ys.max()-ys.min()+1))
            nc=int(cv2.connectedComponents(m6.astype(np.uint8),connectivity=8)[0]-1)
        else: ef=0; bb=0; nc=0
        row=[round(frac,5),round(mad,4),n6,n12,n150,mx,round(ef,3),bb,nc,0]
    rows.append([i,m[0],m[1] if len(m)>1 else '',round(float(sm.mean()),2),round(mr,2),round(mg,2),round(mb,2),round(sat,2),round(ed,4)]+row[:9])
    pg=g; pl=sm; i+=1
with open(OUT,'w',newline='') as f:
    w=csv.writer(f); w.writerow(['frame','pts_time','pict','mean_luma','mean_r','mean_g','mean_b','mean_sat','edge_density','changed_frac_thr10_320','mean_abs_diff_320','px_diff_ge6','px_diff_ge12','px_diff_ge150','max_abs_diff','edge_fraction','bbox_area','components'])
    w.writerows(rows)
print(i,'frames')
