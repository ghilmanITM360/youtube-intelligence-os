import json,csv,re,collections,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
O='integrated_v1/'; N=21410
def rd(p): return list(csv.DictReader(open(p)))
mach={r['id']:r for r in rd('tables/candidates_classified.csv')}
cand,stat,disp,prov=[],[],[],[]
for n in range(1,11):
    d=json.load(open(f'agents/shard_{n}/OUT_shard_{n}.json'))
    ms={r['state_id']:r for r in rd(f'agents/shard_{n}/states.csv')}
    for c in d['candidates']:
        m=mach[c['id']]; cand.append(dict(c,shard=n,start=m['start'],end=m['end'],machine_cls=m['cls'],machine_kind=m['kind'],evidence=m['evidence'])); 
    for s in d['states']:
        m=ms[s['id']]; stat.append(dict(s,shard=n,start=int(m['start']),end=int(m['end']),n_frames=int(m['n_frames']),rep_image=m['rep_image']))
    for x in d['disputes']: disp.append(dict(x,shard=n))
    prov.append(dict(shard=n,file=f'agents/shard_{n}/OUT_shard_{n}.json',cands=len(d['candidates']),states=len(d['states']),disputes=len(d['disputes']),reviewer='first-pass sonnet subagent',pass_='FIRST_PASS_UNVERIFIED_BY_SECOND_REVIEWER'))
stat.sort(key=lambda s:s['start'])
def w(name,rows):
    keys=[];[keys.append(k) for r in rows for k in r if k not in keys]
    with open(O+name,'w',newline='') as f:
        x=csv.DictWriter(f,keys);x.writeheader();x.writerows(rows)
# frame ownership
owner=[None]*N;overlap=0
for s in stat:
    for f in range(s['start'],s['end']+1):
        if owner[f] is not None: overlap+=1
        owner[f]=s['id']
un=[];i=0
while i<N:
    if owner[i] is None:
        j=i
        while j+1<N and owner[j+1] is None: j+=1
        un.append(dict(start=i,end=j,n_frames=j-i+1,prev_state=owner[i-1] if i else '',next_state=owner[j+1] if j+1<N else '',status='UNOWNED_UNREVIEWED'));i=j+1
    else:i+=1
# composition groups from MERGE_WITH_PREV (draft; ruling pending)
flag=lambda s:'MERGE_WITH_PREV' in json.dumps(s)
comps=[];cur=None;nonadj=0
for k,s in enumerate(stat):
    if flag(s) and cur and cur['members'][-1]!=None:
        if s['start']!=stat[k-1]['end']+1: nonadj+=1
        cur['members'].append(s['id']);cur['end']=s['end']
    else:
        cur=dict(members=[s['id']],start=s['start'],end=s['end']);comps.append(cur)
for k,c in enumerate(comps): c['comp_id']=f'C{k:04d}';c['n_states']=len(c['members']);c['members']=';'.join(c['members']);c['n_frames']=c['end']-c['start']+1;c['merge_ruling']='DRAFT_FIRST_PASS_FLAG_UNRULED' if c['n_states']>1 else 'SINGLE'
w('candidates_integrated.csv',cand);w('states_integrated.csv',stat);w('disputes_integrated.csv',disp)
w('composition_groups_DRAFT.csv',comps);w('unowned_intervals.csv',un);w('reviewer_provenance.csv',prov)
w('corrections.csv',[c for c in cand if c['verdict'] not in('CONFIRMED',)])
w('unverified.csv',[c for c in cand if c['verdict']=='UNVERIFIED'])
st=dict(candidates=len(cand),states=len(stat),disputes=len(disp),dup_candidate_ids=len(cand)-len({c['id'] for c in cand}),dup_state_ids=len(stat)-len({s['id'] for s in stat}),
 frames_total=N,frames_owned=sum(o is not None for o in owner),frame_overlaps=overlap,unowned_intervals=len(un),unowned_frames=sum(u['n_frames'] for u in un),
 compositions=len(comps),states_flagged_merge=sum(flag(s) for s in stat),flagged_nonadjacent=nonadj,verdicts=dict(collections.Counter(c['verdict'] for c in cand)),
 missing_machine_cands=len(set(mach)-{c['id'] for c in cand}),status='FIRST_PASS_INTEGRATED_UNRULED')
json.dump(st,open(O+'integration_stats.json','w'),indent=1);print(json.dumps(st,indent=1))
