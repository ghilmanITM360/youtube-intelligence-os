# D3 calibration probe: high-contrast pixel-change clusters (px_diff_ge150>=T) outside D1/D2 neighbourhoods; montage of a sample for visual calibration.
import csv,numpy as np,cv2,json,sys
T=int(sys.argv[1]);n=int(sys.argv[2]);FPS=30000/1001
m=list(csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv')));N=len(m)
cf=np.array([float(x['changed_frac_thr10_320']) for x in m]);hi=np.array([int(x['px_diff_ge150']) for x in m])
near=np.zeros(N,bool)
for i in np.nonzero(cf>=0.3)[0]:near[max(0,i-4):i+5]=True
for r in list(csv.DictReader(open('tables/scenedetect_candidates.csv')))[1:]:i=int(r['start_frame']);near[max(0,i-4):i+5]=True
idx=[i for i in np.nonzero(hi>=T)[0] if not near[i]];cl=[]
for i in idx:
    if cl and i-cl[-1][1]<=4:cl[-1][1]=int(i)
    else:cl.append([int(i),int(i)])
json.dump(cl,open(f'tables/d3_clusters_T{T}.json','w'))
samp=cl[::max(1,len(cl)//n)][:n];need={f for a,b in samp for f in (a-1,a,b+1)}
cap=cv2.VideoCapture(json.load(open('source_manifest.json'))['source_path']);got={}
for i in range(max(need)+1):
    ok,im=cap.read()
    if i in need:got[i]=cv2.resize(im,(320,180))
rows=[]
for a,b in samp:
    ts=[]
    for f in (a-1,a,b+1):t=got[f].copy();cv2.putText(t,f'f{f}',(3,15),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,0,255),2);ts.append(t)
    rows.append(np.hstack(ts))
cv2.imwrite(f'frames/d3_probe_T{T}.png',np.vstack(rows));print(len(cl),'clusters; sampled',len(samp))
