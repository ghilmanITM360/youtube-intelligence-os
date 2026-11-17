# Second detector candidates: ink_iou_change>=0.7 (threshold chosen so all 5 reviewer-confirmed missed cuts are retained), frames not within +-4 of tier A/B candidates, clustered with gap<=4 frames.
import csv,cv2,numpy as np,sys,os
M=list(csv.DictReader(open('tables/second_detector_measurements.csv')));n=len(M);iou=np.array([float(x['ink_iou_change']) for x in M])
Cd=list(csv.DictReader(open('tables/candidates.csv')));known=np.zeros(n,bool)
for c in Cd: known[max(0,int(c['start'])-4):int(c['end'])+5]=True
S=list(csv.DictReader(open('tables/states_machine.csv')))
idx=[i for i in np.nonzero(iou>=0.7)[0] if not known[i]];runs=[]
for i in idx:
    if runs and i-runs[-1][1]<=4: runs[-1][1]=int(i)
    else: runs.append([int(i),int(i)])
def st(f): return next(s['state_id'] for s in S if int(s['start'])<=f<=int(s['end']))
rows=[]
for k,(a,b) in enumerate(runs,1): rows.append(dict(id=f'C{k:03d}',start=a,end=b,start_pts_s=round(a*1001/30000,3),max_ink_iou=round(float(iou[a:b+1].max()),3),state_id=st(a),status='DETECTOR_CANDIDATE_UNVERIFIED'))
w=csv.DictWriter(open('tables/candidates_second_detector.csv','w',newline=''),list(rows[0]));w.writeheader();w.writerows(rows)
need={}
for r in rows:
    r['fr']=sorted({max(0,r['start']-1),r['start'],r['end'],min(n-1,r['end']+1)}); [need.setdefault(f,None) for f in r['fr']]
cap=cv2.VideoCapture(sys.argv[1]);i=0
while i<=max(need):
    ok,fr=cap.read()
    if not ok:break
    if i in need: need[i]=cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA)
    i+=1
os.makedirs('frames/montages5',exist_ok=True);out=[]
for r in rows:
    ims=[]
    for f in r['fr']:
        im=need[f].copy();cv2.rectangle(im,(0,0),(210,22),(0,0,0),-1);cv2.putText(im,f"f{f} t={f*1001/30000:.3f}",(4,16),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),1);ims.append(im)
    while len(ims)<4: ims.append(np.zeros((270,480,3),np.uint8))
    row=np.hstack(ims);cv2.putText(row,f"{r['id']} {r['state_id']} start={r['start']} end={r['end']} ink={r['max_ink_iou']}",(4,262),cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,255),2);out.append(row)
for k in range(0,len(out),5): cv2.imwrite(f'frames/montages5/Q{k//5+1:02d}.jpg',np.vstack(out[k:k+5]),[cv2.IMWRITE_JPEG_QUALITY,78])
print(len(rows),'clusters',(len(out)+4)//5,'montages')
