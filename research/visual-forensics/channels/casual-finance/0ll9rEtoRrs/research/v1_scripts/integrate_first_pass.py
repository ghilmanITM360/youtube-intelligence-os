# Deterministic structural integration of 10 preserved first-pass reviewer outputs. Reads only; writes integrated/.
# Does NOT certify semantics: every row keeps reviewer provenance and evidence-quality flag.
import json,glob,re,pandas as pd
sm=pd.read_csv('tables/states_machine.csv').set_index('state_id');ce=pd.read_csv('tables/candidate_evidence.csv').set_index('id')
pri=set(open('repair/priority_ids.txt').read().split())
C=[];S=[];D=[]
for p in sorted(glob.glob('agents/shard_*/OUT_shard_*.json')):
    n=int(re.search(r'shard_(\d+)',p).group(1));j=json.load(open(p))
    for k,L in(('candidates',C),('states',S),('disputes',D)):
        for r in j[k]:r['shard']=n;L.append(r)
C=pd.DataFrame(C);S=pd.DataFrame(S);D=pd.DataFrame(D)
assert len(C)==1032 and not C.id.duplicated().any() and set(C.id)==set(ce.index)
assert len(S)==524 and set(S.id)==set(sm.index) and len(D)==148
C['evidence_quality']=C.id.map(lambda i:'EXACT_FRAME_EVIDENCE_REBUILT_UNVIEWED_BY_REVIEWER' if i in pri else 'FIRST_PASS_REVIEWER_ONLY')
C['pass']='FIRST_PASS_UNVERIFIED'
C=C.join(ce[['start','end','pre_frame','stable_frame','net_changed_frac']],on='id');C.to_csv('integrated/reviewed_candidates.csv',index=False)
ev=S.apply(lambda r:json.dumps(r.to_dict()),axis=1)
S['flag_split']=ev.str.contains('SPLIT_NEEDED');S['flag_merge']=ev.str.contains('MERGE_WITH_PREV')
S=S.join(sm[['start','end','n_frames','pts_start','pts_end','duration_s']],on='id');S['pass']='FIRST_PASS_UNVERIFIED'
S.to_csv('integrated/reviewed_states.csv',index=False)
D['pass']='FIRST_PASS_UNVERIFIED';D.to_csv('integrated/reviewed_disputes.csv',index=False)
# cross-shard references
own=dict(zip(C.id,C.shard));x=[]
for r in S.itertuples():
    sd=sm.loc[r.id]
    for ref in {sd.entry,sd.exit,*str(sd.micro_events).split(';')}:
        if ref in own and own[ref]!=r.shard:x.append(dict(state=r.id,state_shard=r.shard,ref=ref,ref_owner_shard=own[ref],resolution='INTENTIONAL_STATE_REFERENCE_CROSS_SHARD_CANDIDATE_REVIEWED_IN_OWNER_SHARD'))
pd.DataFrame(x).to_csv('integrated/cross_shard_references.csv',index=False)
S[S.flag_split][['id','shard','start','end','evidence']].to_csv('integrated/split_needed_pending.csv',index=False)
sm2=sm.reset_index().sort_values('start');U=pd.read_csv('repair/unowned_intervals.csv')
summ=dict(candidates=len(C),verdicts=C.verdict.value_counts().to_dict(),states=len(S),disputes=D.verdict.value_counts().to_dict(),split=int(S.flag_split.sum()),merge=int(S.flag_merge.sum()),
 cross_shard_refs=len(x),unowned_intervals=len(U),unowned_frames=int(U.n_frames.sum()),state_frames=int(sm.n_frames.sum()),total_frames=24298,
 exact_evidence_rebuilt=len(pri),status='FIRST_PASS_INTEGRATED_STRUCTURE_ONLY_NOT_SEMANTICALLY_CERTIFIED')
assert summ['state_frames']+summ['unowned_frames']==24298
json.dump(summ,open('integrated/integration_summary.json','w'),indent=1);print(json.dumps(summ,indent=1))
