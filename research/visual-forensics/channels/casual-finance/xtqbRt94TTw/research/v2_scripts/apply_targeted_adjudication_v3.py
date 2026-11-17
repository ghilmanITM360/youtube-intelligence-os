import pathlib,json,csv,collections,copy
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');O=R/'integrated_v3'
raw=json.loads((R/'agents/merge_split_review/OUT_targeted_adjudication.json').read_text());expected={x['state_id']:x for x in json.loads((R/'agents/merge_split_review/items_with_gap_context.json').read_text())};ids=[x['state_id'] for x in raw['items']];assert len(ids)==len(set(ids)) and set(ids)<=set(expected)
assert set(ids).isdisjoint(raw['pending_state_ids']) and set(ids)|set(raw['pending_state_ids'])==set(expected)
for x in raw['items']:
 assert x['previous']==expected[x['state_id']]['previous'];assert x['merge_ruling'] in ('MERGE_CONTIGUOUS','SAME_LAYOUT_NONCONTIGUOUS','KEEP_DISTINCT','UNRESOLVED');assert x['split_ruling'] in ('SPLIT','NO_SPLIT','UNRESOLVED','NOT_REQUESTED');assert x['description'].strip() and x['evidence_paths']
P=list(csv.DictReader((R/'integrated_v2/frame_partition_v2.csv').open()))
for p in P:p['start']=int(p['start']);p['end']=int(p['end'])
# Preserve all raw output. Apply only matching explicit UNRESOLVED brackets to a new version.
corrections=raw.get('gap_corrections',[]);original_gaps={x['id']:x for x in csv.DictReader((R/'session_20261103/gaps.csv').open())};parts=[]
for x in corrections:
 g=original_gaps[x['gap_id']];assert int(g['start'])<=int(x['start'])<=int(x['end'])<=int(g['end'])
for p in P:
 matching=[(i,x) for i,x in enumerate(corrections) if int(x['start'])<=p['end'] and int(x['end'])>=p['start']]
 if not matching:parts.append(p);continue
 bounds=sorted({p['start'],p['end']+1,*[max(p['start'],int(x['start'])) for _,x in matching],*[min(p['end']+1,int(x['end'])+1) for _,x in matching]})
 for lo,hi in zip(bounds,bounds[1:]):
  active=[(i,x) for i,x in matching if int(x['start'])<=lo and hi-1<=int(x['end'])];assert len(active)<=1
  q=dict(p);q.update(start=lo,end=hi-1,interval_id=p['interval_id']+f'.R{lo}')
  if active:
   i,x=active[0];g=original_gaps[x['gap_id']];assert x['owner'] in ('PREVIOUS','FOLLOWING','NEW','UNRESOLVED')
   q.update(description=x['description'],source_ref='agents/merge_split_review/OUT_targeted_adjudication.json#'+x['gap_id'],boundary_precision=x['precision'],semantic_status='UNRESOLVED' if x['owner']=='UNRESOLVED' else 'INDEPENDENT_TARGETED_NATIVE_REVIEW',state_id=g['previous'] if x['owner']=='PREVIOUS' else g['following'] if x['owner']=='FOLLOWING' else x['gap_id']+f'RN{i}' if x['owner']=='NEW' else p['state_id'])
  parts.append(q)
parts.sort(key=lambda x:x['start']);split_pending=[]
for x in raw['items']:
 if x['split_ruling']!='SPLIT':continue
 f=x.get('split_frame')
 if not isinstance(f,int):split_pending.append(x['state_id']);continue
 hit=[p for p in parts if p['state_id']==x['state_id'] and p['start']<f<=p['end']]
 assert len(hit)==1,(x['state_id'],f,'split not inside state')
 p=hit[0];b=dict(p);b.update(start=f,state_id=p['state_id']+'b',interval_id=p['interval_id']+'.b',source_ref='agents/merge_split_review/OUT_targeted_adjudication.json#'+x['state_id']);p['end']=f-1;p['interval_id']+='.a';parts.append(b)
 for q in parts:
  if q['state_id']==x['state_id'] and q['start']>=f:q['state_id']+='b'
parts.sort(key=lambda x:x['start']);parent={p['state_id']:p['state_id'] for p in parts}
def find(x):
 while parent[x]!=x:x=parent[x]
 return x
for x in raw['items']:
 if x['split_ruling']=='SPLIT' and isinstance(x.get('split_frame'),int):parent[x['state_id']+'b']=x['state_id']
rulings=[]
for x in raw['items']:
 r=dict(x);r['applied_merge']=False
 if x['merge_ruling']=='MERGE_CONTIGUOUS':
  sid,prev=x['state_id'],x['previous'];lo=max(p['end'] for p in parts if p['state_id']==prev);hi=min(p['start'] for p in parts if p['state_id']==sid);between=[p for p in parts if p['start']>lo and p['end']<hi]
  if all(p['state_id'] in (prev,sid) for p in between):parent[find(sid)]=find(prev);r['applied_merge']=True
  else:r['application_note']='BLOCKED: intervening independently observed state; recurrence is not continuity'
 rulings.append(r)
assert not O.exists();O.mkdir()
def write(name,rows):
 with (O/name).open('w') as f:
  fieldnames=list(dict.fromkeys(k for r in rows for k in r));w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader()
  for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
counts=[0]*19862
for p in parts:
 for f in range(p['start'],p['end']+1):counts[f]+=1
 p.update(composition_group=find(p['state_id']),n_frames=p['end']-p['start']+1,start_pts=(p['start']+1)/24,end_exclusive_pts=(p['end']+2)/24)
assert set(counts)=={1};write('frame_partition_v3.csv',parts);write('merge_split_rulings_v3.csv',rulings)
groups=[]
for p in parts:
 if groups and groups[-1]['composition_group']==p['composition_group'] and groups[-1]['end']+1==p['start']:
  groups[-1]['end']=p['end'];groups[-1]['state_ids']+=';'+p['state_id'];groups[-1]['interval_ids']+=';'+p['interval_id']
 else:groups.append(dict(composition_group=p['composition_group'],start=p['start'],end=p['end'],state_ids=p['state_id'],interval_ids=p['interval_id']))
for g in groups:g.update(n_frames=g['end']-g['start']+1,start_pts=(g['start']+1)/24,end_exclusive_pts=(g['end']+2)/24)
write('composition_intervals_v3.csv',groups)
# Retain base event timing/provenance; corrections append independent observations.
events=list(csv.DictReader((R/'integrated_v2/visual_event_ledger_v2.csv').open()))
for x in corrections:events.append(dict(event_id=x['gap_id']+'_TARGETED',source_start_frame=x['start'],source_end_frame=x['end'],source_start_pts=(int(x['start'])+1)/24,source_end_exclusive_pts=(int(x['end'])+2)/24,event_class=x['event_type'],description=x['description'],verdict=x['owner'],timing_precision=x['precision'],review_scope='TARGETED_NATIVE_ADJUDICATION',source_ref='agents/merge_split_review/OUT_targeted_adjudication.json'))
write('visual_event_ledger_v3.csv',events)
stats={'frames':19862,'numerical_missing':0,'numerical_overlaps':0,'gap_items_reviewed':123,'gap_frames_reviewed':3116,'unresolved_gap_frames':sum(p['n_frames'] for p in parts if p['semantic_status']=='UNRESOLVED'),'unresolved_brackets':[dict(start=p['start'],end=p['end'],id=p['interval_id']) for p in parts if p['semantic_status']=='UNRESOLVED'],'targeted_items_completed':len(ids),'targeted_items_pending':len(raw['pending_state_ids']),'merge_ruling_counts':dict(collections.Counter(x['merge_ruling'] for x in raw['items'])),'merges_applied':sum(x['applied_merge'] for x in rulings),'split_ruling_counts':dict(collections.Counter(x['split_ruling'] for x in raw['items'])),'splits_pending_exact_timing':split_pending,'composition_intervals':len(groups),'partition_intervals':len(parts),'semantic_full_video_certification':False,'actual_listening_seconds':0,'status':'VISUAL_ANALYSIS_PARTIAL_NOT_CT_COMPLETE'}
(O/'integration_stats_v3.json').write_text(json.dumps(stats,indent=2));print(stats)
