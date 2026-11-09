import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
U={u['gap_id']:u for u in csv.DictReader(open('integrated_v3/unowned_intervals_v3.csv'))}
G=open('phaseA/boundary_rule_gaps.txt').read().split()
need=set()
for g in G:
    b=int(U[g]['end']);need|=set(range(b-6,b+1))
fr={};cap=cv2.VideoCapture(src);i=0
while i<=max(need):
    ok,im=cap.read()
    if not ok:break
    if i in need:fr[i]=cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY),(320,180)).astype(np.int16)
    i+=1
d=lambda a,b:round(float((np.abs(fr[a]-fr[b])>24).mean()),4)
rows=[]
for g in G:
    b=int(U[g]['end']);jump=d(b-1,b);prior=[d(f-1,f) for f in range(b-4,b)];mx=max(prior)
    iso=jump>=0.10 and jump>=3*max(mx,0.005)
    rows.append(dict(gap_id=g,end=b,jump_at_end=jump,prior_4_consec=' '.join(map(str,prior)),isolated_spike='YES' if iso else 'NO'))
    print(rows[-1])
w=csv.DictWriter(open('phaseA/boundary_spike.csv','w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
