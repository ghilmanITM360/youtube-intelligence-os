# Per-video boundary candidates: D1 = runs of changed_frac_thr10_320>=T (calibrated per source, arg), D2 = PySceneDetect ContentDetector(12) starts.
# Union clustered (gap<=4f). Writes tables/boundary_candidates.csv and review montages frames/boundary_review/Bnn.jpg (6 candidates x 6 tiles).
import csv,sys,cv2,numpy as np,json,os
T=float(sys.argv[1]);FPS=30000/1001
m=list(csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv')));N=len(m);cf=np.array([float(x['changed_frac_thr10_320']) for x in m])
pts=[]
for i in np.nonzero(cf>=T)[0]:pts.append((int(i),'D1'))
for r in list(csv.DictReader(open('tables/scenedetect_candidates.csv')))[1:]:pts.append((int(r['start_frame']),'D2'))
import glob
for g in glob.glob('tables/d3_clusters_T*.json'):  # D3 = high-contrast px change clusters outside D1/D2 (calibrated per source via be_d3_probe.py)
    for a,b in json.load(open(g)):pts+=[(a,'D3'),(b,'D3')]
pts.sort();cl=[]
for f,d in pts:
    if cl and f-cl[-1]['end']<=4:cl[-1]['end']=max(cl[-1]['end'],f);cl[-1]['det'].add(d)
    else:cl.append({'start':f,'end':f,'det':{d}})
rows=[]
for k,c in enumerate(cl,1):
    a,b=c['start'],c['end']
    fr=sorted({max(0,a-2),max(0,a-1),a,min(N-1,(a+b)//2 if b>a else a+1),min(N-1,b+1),min(N-1,b+3)})
    rows.append(dict(cand=f'K{k:03d}',start=a,end=b,frames=b-a+1,start_pts_s=round(a/FPS,3),detectors='+'.join(sorted(c['det'])),peak_cf=round(float(cf[a:b+1].max()),3),tiles=';'.join(map(str,fr))))
w=csv.DictWriter(open('tables/boundary_candidates.csv','w',newline=''),list(rows[0]));w.writeheader();w.writerows(rows)
need={int(f) for r in rows for f in r['tiles'].split(';')}
src=json.load(open('source_manifest.json'))['source_path'];cap=cv2.VideoCapture(src);got={}
for i in range(max(need)+1):
    ok,im=cap.read();assert ok
    if i in need:got[i]=cv2.resize(im,(320,180),interpolation=cv2.INTER_AREA)
os.makedirs('frames/boundary_review',exist_ok=True);lines=[]
for r in rows:
    ts=[]
    for f in map(int,r['tiles'].split(';')):
        t=got[f].copy();cv2.rectangle(t,(0,0),(150,18),(0,0,0),-1);cv2.putText(t,f'f{f} {f/FPS:.2f}s',(3,13),cv2.FONT_HERSHEY_SIMPLEX,.42,(255,255,255),1);ts.append(t)
    while len(ts)<6:ts.append(np.zeros_like(ts[0]))
    row=np.hstack(ts);cv2.rectangle(row,(0,160),(330,180),(0,0,0),-1);cv2.putText(row,f"{r['cand']} {r['start']}-{r['end']} {r['detectors']}",(3,175),cv2.FONT_HERSHEY_SIMPLEX,.45,(0,255,255),1);lines.append(row)
for k in range(0,len(lines),6):
    blk=lines[k:k+6]
    while len(blk)<6:blk.append(np.zeros_like(lines[0]))
    p=f'frames/boundary_review/B{k//6+1:02d}.png';cv2.imwrite(p,np.vstack(blk))
    for r in rows[k:k+6]:r['montage']=p
w=csv.DictWriter(open('tables/boundary_candidates.csv','w',newline=''),list(rows[0]));w.writeheader();w.writerows(rows)
print('candidates',len(rows),'montages',(len(lines)+5)//6,'D1only',sum(r['detectors']=='D1' for r in rows),'D2only',sum(r['detectors']=='D2' for r in rows),'both',sum(r['detectors']=='D1+D2' for r in rows),'D3',sum('D3' in r['detectors'] for r in rows))
