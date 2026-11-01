import json,csv,collections,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
O='integrated_v2/';os.makedirs(O,exist_ok=True);N=21410
rd=lambda p:list(csv.DictReader(open(p)))
def w(name,rows):
    keys=[];[keys.append(k) for r in rows for k in r if k not in keys]
    with open(O+name,'w',newline='') as f:
        x=csv.DictWriter(f,keys);x.writeheader();x.writerows(rows)
plan={p['id']:p for p in rd('v2_scripts/second_pass_plan.csv')}
sp={}
for n in range(1,12):
    r=f'R{n:02d}'
    for x in json.load(open(f'agents/second_pass/{r}/OUT_{r}.json'))['items']:
        x['shard']=r;x['kind']=plan[x['id']]['kind'];x['plan_note']=plan[x['id']]['note'];sp[x['id']]=x
fl=lambda v:';'.join(map(str,v)) if isinstance(v,list) else str(v)
# 1 ledger of all second-pass claims (reviewer claims, never edited)
w('second_pass_ledger.csv',[dict(shard=x['shard'],kind=x['kind'],id=x['id'],plan_note=x['plan_note'],original_verdict=x['original_verdict'],original_type=x['original_type'],independent_verdict=x['independent_verdict'],corrected_type=x['corrected_type'],state_boundary=x['state_boundary'],confidence=x['confidence'],viewing=x['viewing'],frame_range=x['frame_range'],frames_viewed=fl(x['frames_viewed']),evidence_file=fl(x['evidence_file']),correction=x['correction'],remaining_uncertainty=x['remaining_uncertainty'],desc=x['desc']) for x in sp.values()])
# 2 candidates
C=rd('integrated_v1/candidates_integrated.csv');cn=0;out=[]
for c in C:
    s=sp.get(c['id']);r=dict(c);r['first_verdict']=c['verdict'];r['first_type']=c['type']
    if not s:r.update(second_pass='NONE',final_status='FIRST_PASS_ONLY',final_verdict=c['verdict'],final_type=c['type'],second_viewing='',second_shard='',second_note='')
    else:
        v=s['independent_verdict'];t=s['corrected_type'] if v=='RECLASSIFIED' and s['corrected_type'] else c['type']
        fv={'CONFIRMED':c['verdict'],'RECLASSIFIED':c['verdict'],'NOT_A_CHANGE':'NOT_A_CHANGE','CODEC_ARTIFACT':'CODEC_ARTIFACT','UNVERIFIED':'UNVERIFIED','SPLIT':'SPLIT_PROPOSED_UNVERIFIED','NO_SPLIT':c['verdict']}[v]
        r.update(second_pass=v,final_status='SECOND_PASSED',final_verdict=fv,final_type=t,second_viewing=s['viewing'],second_shard=s['shard'],second_note=s['correction'])
    out.append(r)
w('candidates_v2.csv',out)
# 3 disputes
D=rd('integrated_v1/disputes_integrated.csv')
w('disputes_v2.csv',[dict(d,second_pass=sp[d['id']]['independent_verdict'] if d['id'] in sp else 'NONE',second_viewing=sp[d['id']]['viewing'] if d['id'] in sp else '',second_note=sp[d['id']]['correction'] if d['id'] in sp else '') for d in D])
# 4 gaps (kept as separate segments, never absorbed)
G=rd('integrated_v1/unowned_intervals.csv');gaps=[]
for g in G:
    k='U%s-%s'%(g['start'],g['end']);s=sp.get(k)
    st=('CONTINUATION_OF_NEIGHBOUR_CLAIM' if s['independent_verdict']=='CONFIRMED' else 'NEW_COMPOSITION_OR_TRANSITION_CLAIM' if s['independent_verdict']=='RECLASSIFIED' else 'UNVERIFIED') if s else 'NOT_SECOND_PASSED'
    gaps.append(dict(gap_id='G'+k[1:],start=g['start'],end=g['end'],n_frames=g['n_frames'],prev_state=g['prev_state'],next_state=g['next_state'],status=st,internal_boundary_frame_claim=s['frame_range'] if s and st.startswith('NEW') else '',viewing=s['viewing'] if s else '',confidence=s['confidence'] if s else '',note=s['correction'] if s else ''))
w('gaps_v2.csv',gaps)
# 5 merge rulings
S={s['id']:s for s in rd('integrated_v1/states_integrated.csv')};M=rd('integrated_v1/merge_measured_signal.csv')
gp=collections.defaultdict(list)
for g in gaps:gp[(g['prev_state'],g['next_state'])].append(g)
mr=[]
for m in M:
    s=sp.get(m['state']);cross=int(m['gap_frames_between'])>0
    base=s['independent_verdict'] if s else 'NOT_REVIEWED'
    gl=gp.get((m['prev'],m['state']),[]);gs=[g['status'] for g in gl]
    if base=='CONFIRMED': rule='MERGE_ACCEPTED'
    elif base=='RECLASSIFIED': rule='KEEP_SEPARATE'
    else: rule='UNRULED'
    why=''
    if cross:
        if rule=='MERGE_ACCEPTED' and any(x.startswith('NEW') for x in gs): rule='KEEP_SEPARATE_GAP_HAS_NEW_COMPOSITION';why='intervening gap reviewed: new composition/transition claim'
        elif rule=='MERGE_ACCEPTED' and not gl: why='gap_frames_between>0 but no unowned interval found between states'; rule='MERGE_ACCEPTED_GAP_UNMATCHED'
        elif rule=='MERGE_ACCEPTED': why='intervening gap(s) reviewed as continuation (SAMPLED claims)'
    mr.append(dict(m,gap_crossing=int(cross),second_pass=base,viewing=s['viewing'] if s else '',confidence=s['confidence'] if s else '',gaps_between=';'.join(g['gap_id'] for g in gl),gap_status=';'.join(gs),final_ruling_v2=rule,ruling_basis=why or (s['correction'] if s else '')))
w('merge_rulings_v2.csv',mr)
KS={m['state'] for m in mr if m['final_ruling_v2'].startswith('KEEP')}
# 6 compositions
sts=sorted(S.values(),key=lambda s:int(s['start']));comps=[];cur=None
for s in sts:
    mg=s['id'] in {m['state'] for m in mr if m['final_ruling_v2'].startswith('MERGE')}
    if mg and cur and int(s['start'])>=cur['end']: cur['members'].append(s['id']);cur['end']=int(s['end'])
    else: cur=dict(members=[s['id']],start=int(s['start']),end=int(s['end']));comps.append(cur)
for i,c in enumerate(comps):c.update(comp_id='C%04d'%i,n_states=len(c['members']),members=';'.join(c['members']),n_frames=c['end']-c['start']+1)
w('composition_groups_v2.csv',comps)
# 7 frame partition
own=[None]*N;ov=0
for s in sts:
    for f in range(int(s['start']),int(s['end'])+1):
        ov+=own[f] is not None;own[f]=s['id']
for g in gaps:
    for f in range(int(g['start']),int(g['end'])+1):
        ov+=own[f] is not None;own[f]=g['gap_id']
seg=[];i=0
while i<N:
    j=i
    while j+1<N and own[j+1]==own[i]:j+=1
    seg.append(dict(owner=own[i],kind='GAP' if (own[i] or '').startswith('G') else 'STATE' if own[i] else 'UNACCOUNTED',start=i,end=j,n_frames=j-i+1));i=j+1
w('frame_partition_v2.csv',seg)
# stats
samp=[x for x in sp.values() if x['plan_note'].startswith('CONFIRMED_SAMPLE')]
err=lambda L:collections.Counter(x['independent_verdict'] for x in L)
st=dict(frames_total=N,frames_owned_by_state=sum(1 for o in own if o and o[0]=='S'),frames_in_gap_segments=sum(1 for o in own if o and o[0]=='G'),frames_unaccounted=sum(o is None for o in own),overlaps=ov,
 states=len(sts),gaps=len(gaps),gap_status=dict(collections.Counter(g['status'] for g in gaps)),compositions=len(comps),
 merge_flags=len(mr),merge_rulings=dict(collections.Counter(m['final_ruling_v2'] for m in mr)),gap_crossing_merges=sum(m['gap_crossing'] for m in mr),
 second_pass_total=len(sp),second_pass_verdicts=dict(err(sp.values())),second_pass_by_kind={k:dict(err([x for x in sp.values() if x['kind']==k])) for k in ('candidate','dispute','unowned','merge','state')},
 confirmed_sample_n=len(samp),confirmed_sample_verdicts=dict(err(samp)),
 viewing=dict(collections.Counter(x['viewing'] for x in sp.values())),
 candidates_final=dict(collections.Counter(c['final_verdict'] for c in out)),candidates_first_pass_only=sum(c['final_status']=='FIRST_PASS_ONLY' for c in out),
 status='SECOND_PASS_INTEGRATED_STRUCTURE_ONLY_NOT_SEMANTICALLY_CERTIFIED',note='reviewer claims; unowned gaps kept as separate segments, not absorbed; most gap/merge items SAMPLED')
json.dump(st,open(O+'integration_stats.json','w'),indent=1);print(json.dumps(st,indent=1))
