import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
U=list(csv.DictReader(open('integrated_v3/unowned_intervals_v3.csv')))
S=sorted(csv.DictReader(open('integrated_v3/reviewed_states_v3.csv')),key=lambda s:int(s['start']))
need=set()
for u in U:
    b=int(u['end']);need|={b-1,b,b+1}
for s in S:
    a=int(s['start']);need|={a-1,a,a+1}
need={f for f in need if f>=0};fr={};cap=cv2.VideoCapture(src);i=0;last=max(need)
while i<=last:
    ok,im=cap.read()
    if not ok:break
    if i in need:fr[i]=cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY),(320,180)).astype(np.int16)
    i+=1
d=lambda a,b:float((np.abs(fr[a]-fr[b])>24).mean())
rows=[]
for u in U:
    b=int(u['end']);rows.append(dict(kind='gap_end',id=u['gap_id'],frame=b,d_prev=round(d(b-1,b),4),d_to_next_state_start=round(d(b,b+1),4)))
for s in S:
    a=int(s['start'])
    if a>=2:rows.append(dict(kind='state_start',id=s['id'],frame=a,d_prev=round(d(a-1,a),4),d_to_next=round(d(a,a+1),4)))
w=csv.DictWriter(open('phaseA/boundary_all.csv','w'),fieldnames=['kind','id','frame','d_prev','d_to_next_state_start','d_to_next']);w.writeheader();w.writerows(rows)
g=[r for r in rows if r['kind']=='gap_end'];s=[r for r in rows if r['kind']=='state_start']
print('gap_end: frame b ~= b+1 (<2%):',sum(r['d_to_next_state_start']<=0.02 for r in g),'/',len(g),'; b differs from b-1 (>10%):',sum(r['d_prev']>0.10 for r in g))
print('state_start: frame a-1 vs a >10%:',sum(r['d_prev']>0.10 for r in s),'/',len(s),'; a ~= a+1 (<2%):',sum(r['d_to_next']<=0.02 for r in s))
