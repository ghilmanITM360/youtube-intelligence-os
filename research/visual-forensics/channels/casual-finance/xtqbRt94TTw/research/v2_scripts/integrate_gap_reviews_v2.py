import pathlib,json,csv,collections,sys,hashlib
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');sys.path.insert(0,str(R/'v2_scripts'))
from validate_gap_reviews_v1 import validate
O=R/'integrated_v2';assert not O.exists(),'Version already exists; never overwrite sealed integration';[validate(R/f'agents/gap_review_{batch:02}/OUT_gap_review_{batch:02}.json',batch) for batch in (1,2,3)];O.mkdir()
def read(name):return list(csv.DictReader((R/name).open()))
def write(name,rows):
 with (O/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)));w.writeheader();w.writerows(rows)
G={x['id']:x for x in read('session_20261103/gaps.csv')};parts=[];gapledger=[];reads=[]
for s in read('tables/states_machine.csv'):
 parts.append(dict(interval_id=s['state_id'],state_id=s['state_id'],start=int(s['start']),end=int(s['end']),origin='IMMUTABLE_DRAFT_STATE',semantic_status='FIRST_PASS_REVIEWED',boundary_precision='MACHINE_CANDIDATE_NOT_INDEPENDENT_NATIVE',source_ref=f'tables/states_machine.csv#{s["state_id"]}',description='See states_first_pass.csv; unchanged source draft interval'))
for batch in (1,2,3):
 path=R/f'agents/gap_review_{batch:02}/OUT_gap_review_{batch:02}.json';d=validate(path,batch);reads+=d['evidence_reads']
 for item in d['items']:
  gap=G[item['id']]
  for k,s in enumerate(item['segments'],1):
   sid=gap['previous'] if s['owner']=='PREVIOUS' else gap['following'] if s['owner']=='FOLLOWING' else f'{item["id"]}N{k:02}' if s['owner']=='NEW' else f'{item["id"]}UNRESOLVED{k:02}'
   seg=dict(interval_id=f'{item["id"]}.{k:02}',state_id=sid,start=int(s['start']),end=int(s['end']),origin='GAP_INDEPENDENT_REVIEW',semantic_status='UNRESOLVED' if s['owner']=='UNRESOLVED' else 'INDEPENDENT_GAP_REVIEW_SAMPLED' if s['boundary_precision']!='EXACT_NATIVE' else 'INDEPENDENT_GAP_NATIVE_BOUNDARY_VERIFIED',boundary_precision=s['boundary_precision'],source_ref=f'agents/gap_review_{batch:02}/OUT_gap_review_{batch:02}.json#{item["id"]}',description=s['description'])
   parts.append(seg);gapledger.append(dict(seg,gap_id=item['id'],assigned_owner=s['owner'],event_type=s['event_type'],evidence_frames=json.dumps(s['evidence_frames']),confidence=s['confidence'],notes=item.get('notes','')))
parts.sort(key=lambda x:x['start']);counts=[0]*19862
for p in parts:
 assert 0<=p['start']<=p['end']<19862
 for f in range(p['start'],p['end']+1):counts[f]+=1
 p.update(n_frames=p['end']-p['start']+1,start_pts=(p['start']+1)/24,end_exclusive_pts=(p['end']+2)/24)
assert set(counts)=={1},'Missing/overlapping frames'
write('frame_partition_v2.csv',parts);write('gap_rulings_v2.csv',gapledger)
# Coalesce only adjacent intervals assigned to the same state by direct gap review; first-pass merge claims remain pending.
states=[]
for p in parts:
 if states and states[-1]['state_id']==p['state_id'] and states[-1]['end']+1==p['start']:
  states[-1]['end']=p['end'];states[-1]['member_intervals']+=';'+p['interval_id'];states[-1]['review_scope']+=';'+p['semantic_status']
 else:states.append(dict(state_id=p['state_id'],start=p['start'],end=p['end'],member_intervals=p['interval_id'],review_scope=p['semantic_status']))
for p in states:p.update(n_frames=p['end']-p['start']+1,start_pts=(p['start']+1)/24,end_exclusive_pts=(p['end']+2)/24)
write('states_integrated_v2.csv',states)
# Each source candidate retains measured machine window separately from visual onset uncertainty.
events=[]
for c in read('integrated_v1/candidates_first_pass.csv'):
 events.append(dict(event_id=c['id'],source_start_frame=int(c['start']),source_end_frame=int(c['end']),source_start_pts=(int(c['start'])+1)/24,source_end_exclusive_pts=(int(c['end'])+2)/24,event_class=c.get('review_type','UNKNOWN'),candidate_kind=c['kind'],verdict=c['review_verdict'],description=c['review_desc'],shot_boundary_claim=c.get('review_shot_boundary','AMBIGUOUS'),visual_onset_verified_frame='',evidence=c['evidence'],review_scope='FIRST_PASS',timing_precision='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET',source_ref=c['review_reviewer_file']))
for g in gapledger:
 events.append(dict(event_id=g['interval_id'],source_start_frame=g['start'],source_end_frame=g['end'],source_start_pts=(g['start']+1)/24,source_end_exclusive_pts=(g['end']+2)/24,event_class=g['event_type'],candidate_kind='GAP_RECOVERY',verdict=g['semantic_status'],description=g['description'],shot_boundary_claim='SEE_GAP_RULING',visual_onset_verified_frame=g['start'] if g['boundary_precision']=='EXACT_NATIVE' else '',evidence=g['evidence_frames'],review_scope='INDEPENDENT_GAP_REVIEW',timing_precision=g['boundary_precision'],source_ref=g['source_ref']))
write('visual_event_ledger_v2.csv',events)
C={c['id']:c for c in read('tables/candidates_classified.csv')};disputes=[]
for d in read('integrated_v1/disputes_first_pass.csv'):
 f=int(d['cut_frame']);matched=d['review_matches_candidate'];contained=[c['id'] for c in C.values() if int(c['start'])<=f<=int(c['end'])]
 owners=[p for p in parts if p['start']<=f<=p['end']];assert len(owners)==1
 disputes.append(dict(dispute_id=d['id'],cut_frame=f,source_pts=(f+1)/24,first_pass_verdict=d['review_verdict'],description=d['review_desc'],reviewer_candidate_claim=matched,measured_containing_candidates=';'.join(contained),claim_contains_cut=matched in contained,state_at_cut=owners[0]['state_id'],partition_at_cut=owners[0]['interval_id'],adjudication='FIRST_PASS_ONLY_NOT_339_MISSING_CUTS',source_ref=d['review_reviewer_file']))
write('dispute_resolution_v2.csv',disputes)
# A provisional cut ledger, never shot count certification.
shots=[dict(shot_candidate_id=d['dispute_id'],first_frame_candidate=d['cut_frame'],source_pts=d['source_pts'],evidence_ref=f'disputes/{d["dispute_id"]}.jpg',verification='FIRST_PASS_CUT_CLAIM; exact edit boundary may require native review',description=d['description']) for d in disputes if d['first_pass_verdict']=='REAL_STATE_CHANGE'];write('shot_boundary_claims_v2.csv',shots)
counts_by=collections.Counter(g['assigned_owner'] for g in gapledger);stats={'frames':19862,'coverage_counts_min':min(counts),'coverage_counts_max':max(counts),'numerical_missing':counts.count(0),'numerical_overlap':sum(x>1 for x in counts),'gap_items_reviewed':len(G),'gap_frames_reviewed':3116,'gap_segments':len(gapledger),'gap_owner_segment_counts':dict(counts_by),'unresolved_gap_frames':sum(g['end']-g['start']+1 for g in gapledger if g['assigned_owner']=='UNRESOLVED'),'native_boundary_gap_segments':sum(g['boundary_precision']=='EXACT_NATIVE' for g in gapledger),'scaled_sampled_gap_segments':sum(g['boundary_precision']=='SAMPLED_BRACKET' for g in gapledger),'integrated_state_intervals':len(states),'new_gap_composition_segments':counts_by['NEW'],'first_pass_merges_pending':142,'first_pass_splits_pending':3,'disputes':339,'dispute_first_pass_counts':dict(collections.Counter(d['first_pass_verdict'] for d in disputes)),'claim_candidate_frame_mismatches':[d['dispute_id'] for d in disputes if not d['claim_contains_cut']],'semantic_full_video_certification':False,'audio_listened_seconds':0,'status':'VISUAL_ANALYSIS_PARTIAL_NOT_CT_COMPLETE'}
(O/'integration_stats_v2.json').write_text(json.dumps(stats,indent=2));print(stats)
