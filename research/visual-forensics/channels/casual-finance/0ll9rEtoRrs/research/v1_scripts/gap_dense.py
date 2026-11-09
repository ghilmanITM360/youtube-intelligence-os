import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
U=list(csv.DictReader(open('integrated_v2/unowned_intervals_v2.csv')))
P=[u for u in U if u['gap_id'] in('U037','U072','U075','U128') or u['desc_mentions_cut']=='YES' or u['sp_class'] in('EMBEDDED_VIDEO','UNCERTAIN','DISTINCT_COMPOSITION','FADE_OR_TRANSITION') or int(u['n_frames'])>=90]
rng=[(int(u['start']),int(u['end']),u['gap_id']) for u in P]
lo=min(r[0] for r in rng)
cap=cv2.VideoCapture(src);cap.set(cv2.CAP_PROP_POS_FRAMES,0)
cur={r[2]:{'f':[],'d':[]} for r in rng}
by={}
for a,b,g in rng:
    for f in range(a,b+1):by.setdefault(f,[]).append(g)
last=max(r[1] for r in rng);i=0;prev=None
while i<=last:
    ok,im=cap.read()
    if not ok:break
    if i in by:
        g=cv2.resize(im,(320,180))
        gr=cv2.cvtColor(g,cv2.COLOR_BGR2GRAY).astype(np.int16)
        for gid in by[i]:
            d=float((np.abs(gr-prev)>24).mean()) if prev is not None else 0.0
            cur[gid]['f'].append((i,g,d if i>0 else 0))
    prev=cv2.cvtColor(cv2.resize(im,(320,180)),cv2.COLOR_BGR2GRAY).astype(np.int16) if (i+1) in by else None
    i+=1
rows=[]
for a,b,g in rng:
    F=cur[g]['f'];n=len(F)
    idx=sorted(set(np.linspace(0,n-1,min(n,12)).astype(int)))
    tiles=[]
    for j in idx:
        t=F[j][1].copy();cv2.putText(t,f'f{F[j][0]}',(4,16),0,0.5,(0,0,255),1);tiles.append(t)
    while len(tiles)%4:tiles.append(np.zeros_like(tiles[0]))
    sheet=np.vstack([np.hstack(tiles[k:k+4]) for k in range(0,len(tiles),4)])
    cv2.imwrite(f'phaseA/gap_sheets/{g}.jpg',sheet,[cv2.IMWRITE_JPEG_QUALITY,80])
    ds=[x[2] for x in F[1:]]
    cuts=[F[k+1][0] for k,x in enumerate(ds) if x>0.5]
    rows.append(dict(gap_id=g,start=a,end=b,n=n,max_consec_diff=round(max(ds),3) if ds else 0,mean_consec_diff=round(float(np.mean(ds)),4) if ds else 0,frames_gt50pct=' '.join(map(str,cuts)),frames_gt15pct=' '.join(str(F[k+1][0]) for k,x in enumerate(ds) if 0.15<x<=0.5)[:80]))
w=csv.DictWriter(open('phaseA/gap_dense_metrics.csv','w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows);print(len(rows))
