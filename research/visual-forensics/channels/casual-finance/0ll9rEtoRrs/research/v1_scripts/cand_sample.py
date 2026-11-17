import csv,json,cv2,numpy as np,random,collections
random.seed(20261101)
src=json.load(open('source_manifest.json'))['source_path']
C=list(csv.DictReader(open('integrated_v3/reviewed_candidates_v3.csv')))
X=[c for c in C if c['sp_decision']=='NOT_SECOND_PASSED']
by=collections.defaultdict(list)
for c in X:by[c['final_type']].append(c)
sel=[]
for t,l in by.items():
    k=len(l) if len(l)<=14 else max(8,round(len(l)*0.15))
    # spread over shards, prefer long gaps/high-impact via sort key then random
    random.shuffle(l);l.sort(key=lambda c:(collections.Counter(x['shard'] for x in sel).get(c['shard'],0)))
    sel+=l[:k]
print(len(sel),collections.Counter(c['final_type'] for c in sel))
# controls
S=list(csv.DictReader(open('integrated_v3/reviewed_states_v3.csv')))
cand_frames=[int(c['start']) for c in C]
ctl=[]
random.shuffle(S)
for s in S:
    a,b=int(s['start']),int(s['end'])
    if b-a<30:continue
    f=random.randint(a+8,b-14)
    if any(abs(f-x)<=14 for x in cand_frames):continue
    ctl.append(dict(id=f'CTL{len(ctl)+1:02d}',pre_frame=f,stable_frame=f+6,final_type=random.choice(['ADDITIVE_ENTRY','HIGHLIGHT_ADD','TEXT_CHANGE','DRAW_ON_OR_REVEAL']),shard='CTL',start=f,desc='(control)'));
    if len(ctl)==20:break
rows=[dict(id=c['id'],pre=int(c['pre_frame']),stable=int(c['stable_frame']),typ=c['final_type'],conf=c['confidence'],shard=c['shard'],ctl=False) for c in sel]+[dict(id=c['id'],pre=c['pre_frame'],stable=c['stable_frame'],typ=c['final_type'],conf='',shard='CTL',ctl=True) for c in ctl]
random.shuffle(rows)
want={}
for r in rows:
    want[r['pre']]=None;want[r['stable']]=None
ks=sorted(want);cap=cv2.VideoCapture(src);n=0;k=0
while k<len(ks):
    ok,im=cap.read()
    if not ok:break
    if n==ks[k]:want[n]=cv2.resize(im,(560,315));k+=1
    n+=1
tiles=[]
for r in rows:
    a=want[r['pre']].copy();b=want[r['stable']].copy()
    cv2.putText(a,f"{r['id']} BEFORE f{r['pre']}",(6,22),0,0.6,(0,0,255),2);cv2.putText(b,f"AFTER f{r['stable']}  claimed={r['typ']}",(6,22),0,0.6,(0,0,255),2)
    tiles.append(np.hstack([a,b]))
idx=[]
for j in range(0,len(tiles),6):
    cv2.imwrite(f'phaseA/cand_sheets/c{j//6+1:02d}.jpg',np.vstack(tiles[j:j+6]),[cv2.IMWRITE_JPEG_QUALITY,80]);idx.append((f'c{j//6+1:02d}',' '.join(r['id'] for r in rows[j:j+6])))
csv.writer(open('phaseA/cand_sheet_index.csv','w')).writerows([('sheet','ids')]+idx)
w=csv.DictWriter(open('phaseA/cand_sample_key_PRIVATE.csv','w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print(len(rows),len(idx))
