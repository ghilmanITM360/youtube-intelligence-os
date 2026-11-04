# overshoot_scan.py SRC OUT.csv name:start:end ...  — per-frame changed-region bbox vs pre-onset frame (native res, diff>40 gray)
# overshoot signature: some frame's bbox h or w exceeds the settled (end) value by >=3% before settling. MEASURED geometry only.
import cv2,sys,csv,numpy as np
src,out=sys.argv[1],sys.argv[2];ev=[(a,int(b),int(c)) for a,b,c in (x.split(':') for x in sys.argv[3:])]
cap=cv2.VideoCapture(src);rows=[];F={};need=set()
for _,s,e in ev: need|=set(range(s-1,e+1))
i=0;last=max(need)
while i<=last:
    ok,im=cap.read()
    if not ok:break
    if i in need:F[i]=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    i+=1
for name,s,e in ev:
    base=F[s-1];seq=[]
    for f in range(s,e+1):
        m=(cv2.absdiff(F[f],base)>40).astype(np.uint8);m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
        ys,xs=np.nonzero(m);seq.append((f,int(m.sum()),int(np.ptp(ys)) if len(ys) else 0,int(np.ptp(xs)) if len(xs) else 0))
    fh,fw=seq[-1][2],seq[-1][3]
    pk=max(seq[:-1],key=lambda t:t[2]+t[3]) if len(seq)>1 else seq[-1]
    ov=fh>20 and (pk[2]>=fh*1.03 or pk[3]>=fw*1.03) and pk[0]<seq[-1][0]
    rows.append(dict(event=name,start=s,end=e,settled_h=fh,settled_w=fw,peak_frame=pk[0],peak_h=pk[2],peak_w=pk[3],overshoot_signature=ov,seq=';'.join(f'{f}:{h}x{w}' for f,_,h,w in seq)))
w=csv.DictWriter(open(out,'w'),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for r in rows:print(r['event'],r['overshoot_signature'],r['seq'][:200])
