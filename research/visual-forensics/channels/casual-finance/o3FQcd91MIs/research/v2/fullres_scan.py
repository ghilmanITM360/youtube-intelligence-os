import cv2,csv,sys,numpy as np
F=sys.argv[1]
pict=[r['pict'] for r in csv.DictReader(open('tables/frame_metrics.csv'))]
cap=cv2.VideoCapture(F);prev=None;rows=[];i=0
k=np.ones((3,3),np.uint8)
while True:
    ok,f=cap.read()
    if not ok:break
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    if prev is None: rows.append((i,pict[i],0,0,0,0,0,0));prev=g;i+=1;continue
    d=cv2.absdiff(g,prev)
    m6=d>=6;n6=int(m6.sum());n12=int((d>=12).sum());mx=int(d.max())
    # edge proximity: gradient magnitude of current frame
    if n6:
        ed=cv2.dilate(cv2.Canny(g,30,90),k,iterations=2)>0
        edge_frac=float((m6&ed).sum()/n6)
        ys,xs=np.nonzero(m6);bw=int(xs.max()-xs.min()+1);bh=int(ys.max()-ys.min()+1)
        nc=cv2.connectedComponents(m6.astype(np.uint8),connectivity=8)[0]-1
    else: edge_frac=0;bw=bh=0;nc=0
    rows.append((i,pict[i],n6,n12,mx,round(edge_frac,3),bw*bh,nc))
    prev=g;i+=1
with open('v2/frame_metrics_fullres.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['frame','pict','px_diff_ge6','px_diff_ge12','max_abs_diff','edge_fraction','bbox_area','components']);w.writerows(rows)
print(i)
