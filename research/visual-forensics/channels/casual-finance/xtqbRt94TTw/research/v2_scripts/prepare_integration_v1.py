import csv,json,pathlib,collections,hashlib,cv2,numpy as np
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
O=R/'integrated_v1';O.mkdir(exist_ok=True)
def read(p):return list(csv.DictReader(p.open()))
def write(p,rows):
 with p.open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)));w.writeheader();w.writerows(rows)
source=json.loads((R/'source_manifest.json').read_text()); states=read(R/'tables/states_machine.csv'); gaps=read(R/'session_20261103/gaps.csv'); outputs={i:json.loads((R/f'agents/shard_{i}/OUT_shard_{i}.json').read_text()) for i in range(1,11)}
for kind,table in [('states','states_machine'),('candidates','candidates_classified'),('disputes','disputes_scenedetect')]:
 base=read(R/f'tables/{table}.csv'); mapping={}; reviewrows=[]
 for i,o in outputs.items():
  for r in o[kind]:
   assert r['id'] not in mapping,(kind,r['id']);mapping[r['id']]=r
   reviewrows.append(dict(r,reviewer_shard=i,reviewer_file=f'agents/shard_{i}/OUT_shard_{i}.json',review_status='FIRST_PASS_ONLY',image_read_audit='PENDING'))
 key='state_id' if kind=='states' else 'id'; assert {x[key] for x in base}==set(mapping)
 merged=[]
 for r in base:
  a=next(x for x in reviewrows if x['id']==r[key]);d=dict(r)
  for k,v in a.items():d['review_'+k]=json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v
  merged.append(d)
 write(O/f'{kind}_first_pass.csv',merged)
# Numerical accounting explicitly distinguishes unowned gaps from verified states.
partition=[]
for s in states:partition.append(dict(partition_id=s['state_id'],start=int(s['start']),end=int(s['end']),kind='DRAFT_STATE',semantic_status='FIRST_PASS_ONLY'))
for g in gaps:partition.append(dict(partition_id=g['id'],start=int(g['start']),end=int(g['end']),kind='UNOWNED_GAP',semantic_status='PENDING_INDEPENDENT_VISUAL_REVIEW'))
partition.sort(key=lambda x:x['start']);cursor=0
for x in partition:assert x['start']==cursor;x['n_frames']=x['end']-x['start']+1;cursor=x['end']+1
assert cursor==19862;write(O/'frame_partition_provisional.csv',partition)
# Duplicate prompts compared to evidence flags, without silently treating as merge.
dups=[]
for i,o in outputs.items():
 seen={}
 for s in o['states']:
  prior=seen.get(s['prompt'],''); merge=s['evidence'].startswith('MERGE_WITH_PREV')
  if prior or merge or s['evidence'].startswith('SPLIT_NEEDED'):
   dups.append(dict(shard=i,state_id=s['id'],duplicate_of=prior,merge_requested=merge,split_requested=s['evidence'].startswith('SPLIT_NEEDED'),evidence=s['evidence'],ruling='PENDING_VISUAL_ADJUDICATION'))
  seen.setdefault(s['prompt'],s['id'])
write(O/'merge_split_prompt_audit.csv',dups)
stats={'n_frames':cursor,'draft_states':len(states),'candidates':766,'disputes':339,'unowned_intervals':len(gaps),'unowned_frames':sum(int(g['n_frames']) for g in gaps),'partition_numerical':'PASS_WITH_EXPLICIT_UNOWNED_GAPS','semantic_integration':'PENDING','first_pass_shards':10,'native_image_read_audit':'PENDING','audio_listened_seconds':0,'status':'VISUAL_ANALYSIS_PARTIAL_NOT_CT_COMPLETE'}
(O/'integration_stats.json').write_text(json.dumps(stats,indent=2))
# Each gap: before/after plus every 4th frame and adjacent candidate cut frames. Scaled, never native claims.
cutframes={int(x['cut_frame']) for x in read(R/'tables/disputes_scenedetect.csv')};targets={};requests=[]
for g in gaps:
 lo,hi=int(g['start']),int(g['end']);fs={max(0,lo-1),lo,hi,min(19861,hi+1),*range(lo,hi+1,4)}
 for c in cutframes:
  if lo<=c<=hi:fs.update(f for f in (c-1,c,c+1) if lo<=f<=hi)
 g['frames']=sorted(fs)
 for f in fs:targets[f]=None
cap=cv2.VideoCapture(source['source_path']);assert cap.isOpened()
for f in range(max(targets)+1):
 ok,img=cap.read();assert ok,f
 if f in targets:targets[f]=cv2.resize(img,(480,270),interpolation=cv2.INTER_AREA)
cap.release();ev=R/'integration_evidence_v1';ev.mkdir(exist_ok=True);receipts=[]
for idx,g in enumerate(gaps):
 dest=R/f'agents/gap_review_{idx//41+1:02}';dest.mkdir(exist_ok=True);paths=[]
 for page,start in enumerate(range(0,len(g['frames']),12),1):
  fs=g['frames'][start:start+12];sheet=np.full((int(np.ceil(len(fs)/3))*294,1440,3),240,np.uint8)
  for j,f in enumerate(fs):
   y,x=(j//3)*294,(j%3)*480;sheet[y:y+270,x:x+480]=targets[f];cv2.putText(sheet,f'{g["id"]} f{f} PTS={(f+1)/24:.6f}',(x+6,y+288),cv2.FONT_HERSHEY_SIMPLEX,.51,(0,0,0),1,cv2.LINE_AA)
  q=ev/f'{g["id"]}_{page:02}.jpg';assert not q.exists();assert cv2.imwrite(str(q),sheet,[cv2.IMWRITE_JPEG_QUALITY,92]);paths.append(str(q));receipts.append(dict(path=str(q.relative_to(R)),sha256=hashlib.sha256(q.read_bytes()).hexdigest(),frames=';'.join(map(str,fs)),method='cv2 sequential decode from source frame0; 1920x1080 scaled to 480x270; frame labels measured PTS=(f+1)/24'))
 requests.append(dict(g,sheets=paths,review_batch=idx//41+1))
write(ev/'extraction_receipts.csv',receipts)
for batch in (1,2,3):
 items=[x for x in requests if x['review_batch']==batch];(R/f'agents/gap_review_{batch:02}/items.json').write_text(json.dumps(items,indent=2))
print(stats,'gap sheets',len(receipts),'sampled frames',len(targets))
