import csv,json,os,shutil,copy,collections,statistics as st
N=24298
rd=lambda p:list(csv.DictReader(open(p)))
def wr(p,rows):
    w=csv.DictWriter(open(p,'w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
def owners(states,gaps,dec):
    """per-frame ownership runs: list of dict(start,end,owner_type,state_id,composition_id,gap_id,basis)"""
    runs=[]
    for s in states:runs.append(dict(start=int(s['start']),end=int(s['end']),owner_type='STATE',state_id=s['id'],composition_id=s['composition_id'],gap_id='',basis='state'))
    for g in gaps:
        d=dec[g['gap_id']];a,b=int(g['start']),int(g['end'])
        base=dict(state_id='',gap_id=g['gap_id'])
        if d['decision'] in('ABSORB_WHOLE','ABSORB_PREV'):runs.append(dict(base,start=a,end=b,owner_type='GAP_ABSORBED',composition_id=d['prev_comp'],basis=d['decision']+': '+d['basis']))
        elif d['decision'] in('ABSORB_NEXT','SPLIT_AT_CUT'):
            cf=int(d['cut_frame']) if d['decision']=='SPLIT_AT_CUT' else a
            if cf>a:runs.append(dict(base,start=a,end=cf-1,owner_type='GAP_ABSORBED',composition_id=d['prev_comp'],basis='SPLIT_AT_CUT before cut: '+d['basis']))
            runs.append(dict(base,start=cf,end=b,owner_type='GAP_ABSORBED',composition_id=d['next_comp'],basis=d['decision']+': '+d['basis']))
        elif d['decision']=='KEEP_STANDALONE':runs.append(dict(base,start=a,end=b,owner_type='GAP_STANDALONE',composition_id='',basis=d['basis']))
        else:runs.append(dict(base,start=a,end=b,owner_type='GAP_UNRESOLVED',composition_id='',basis=d['basis']))
    return sorted(runs,key=lambda r:r['start'])
def check(runs,comps,dec,gaps):
    e=[];cov=[0]*N
    for r in runs:
        if r['start']>r['end']:e.append('bad run '+str(r['gap_id'] or r['state_id']));continue
        for f in range(r['start'],r['end']+1):cov[f]+=1
    if any(v>1 for v in cov):e.append('overlap')
    if any(v==0 for v in cov):e.append(f'uncovered {sum(v==0 for v in cov)}')
    if {g['gap_id'] for g in gaps}!=set(dec):e.append('gap decisions mismatch')
    cids={c['composition_id'] for c in comps}
    for r in runs:
        if r['owner_type'] in('STATE','GAP_ABSORBED') and r['composition_id'] not in cids:e.append('unknown composition '+r['composition_id']);break
    byc=collections.defaultdict(list)
    for r in runs:
        if r['composition_id']:byc[r['composition_id']].append(r)
    for cid,l in byc.items():
        l.sort(key=lambda r:r['start'])
        for x,y in zip(l,l[1:]):
            if y['start']!=x['end']+1:e.append('composition not contiguous '+cid);break
    for g in gaps:
        if dec[g['gap_id']]['decision'] not in('ABSORB_WHOLE','ABSORB_PREV','ABSORB_NEXT','SPLIT_AT_CUT','KEEP_STANDALONE','UNRESOLVED'):e.append('bad decision '+g['gap_id'])
        if not dec[g['gap_id']]['basis'].strip():e.append('lost basis '+g['gap_id'])
    return e
if __name__=='__main__':
    os.makedirs('integrated_v5',exist_ok=True)
    for f in os.listdir('integrated_v4'):
        if f.endswith(('.csv','.json')) and 'v4' in f:shutil.copy('integrated_v4/'+f,'integrated_v5/'+f.replace('_v4','_v5'))
        elif f.endswith('.csv') and f!='gap_absorption_decisions.csv':shutil.copy('integrated_v4/'+f,'integrated_v5/'+f)
    states=rd('integrated_v4/reviewed_states_v4.csv');comps=rd('integrated_v4/compositions_v4.csv');gaps=rd('integrated_v4/unowned_intervals_v4.csv')
    D=rd('integrated_v4/gap_absorption_decisions.csv')
    for d in D:
        d['conflict_with_second_pass']='YES' if d['decision']=='SPLIT_AT_CUT' and d['second_pass_relation'] in('PREV',) else ''
    dec={d['gap_id']:d for d in D}
    runs=owners(states,gaps,dec);e=check(runs,comps,dec,gaps);print('POSITIVE',e or 'PASS')
    wr('integrated_v5/gap_absorption_decisions_v5.csv',D)
    wr('integrated_v5/frame_ownership_v5.csv',runs)
    ab=collections.Counter();agaps=collections.defaultdict(list)
    for r in runs:
        if r['owner_type']=='GAP_ABSORBED':ab[r['composition_id']]+=r['end']-r['start']+1;agaps[r['composition_id']].append(r['gap_id'])
    allr=collections.defaultdict(list)
    for r in runs:
        if r['composition_id']:allr[r['composition_id']].append(r)
    for c in comps:
        l=allr[c['composition_id']];c['absorbed_gap_frames']=ab[c['composition_id']];c['absorbed_gap_ids']=' '.join(agaps[c['composition_id']]);c['full_start']=min(r['start'] for r in l);c['full_end']=max(r['end'] for r in l);c['full_span_frames']=c['full_end']-c['full_start']+1
    for u in gaps:
        d=dec[u['gap_id']];u['abs_decision']=d['decision'];u['abs_basis']=d['basis']
    wr('integrated_v5/compositions_v5.csv',comps);wr('integrated_v5/unowned_intervals_v5.csv',gaps)
    neg={}
    r2=[r for r in runs if r['gap_id']!=gaps[3]['gap_id']];neg['dropped gap ownership']=check(r2,comps,dec,gaps)
    r3=copy.deepcopy(runs);x=[r for r in r3 if r['owner_type']=='GAP_ABSORBED'][0];x['end']+=1;neg['gap run overlaps next']=check(r3,comps,dec,gaps)
    r4=copy.deepcopy(runs);x=[r for r in r4 if r['owner_type']=='GAP_ABSORBED'][0];x['composition_id']='CMP9999';neg['unknown composition']=check(r4,comps,dec,gaps)
    r5=copy.deepcopy(runs);x=[r for r in r5 if r['owner_type']=='GAP_ABSORBED' and dec[r['gap_id']]['decision']=='ABSORB_PREV'][0];x['composition_id']=[c['composition_id'] for c in comps][-1];neg['absorbed into non-adjacent composition']=check(r5,comps,dec,gaps)
    d6=copy.deepcopy(dec);d6[gaps[0]['gap_id']]['basis']='';neg['lost basis']=check(runs,comps,d6,gaps)
    for k,v in neg.items():print('NEG',k,'DETECTED' if v else 'MISSED',v[:1])
    own=collections.Counter();[own.__setitem__(r['owner_type'],own[r['owner_type']]+r['end']-r['start']+1) for r in runs]
    sp=[int(c['full_span_frames'])/24 for c in comps]
    sm=json.load(open('integrated_v5/integration_summary_v5.json'));sm.update(status='GAPS_ABSORBED_WHERE_EVIDENCE_SUPPORTS_STRUCTURE_STILL_NOT_SEMANTICALLY_CERTIFIED',frames_by_owner=dict(own),gap_decisions=dict(collections.Counter(d['decision'] for d in D)),composition_full_span_s=dict(median=round(st.median(sp),2),mean=round(st.mean(sp),2)),validator_positive='PASS' if not e else 'FAIL',absorption_negative_tests={k:('DETECTED' if v else 'MISSED') for k,v in neg.items()})
    json.dump(sm,open('integrated_v5/integration_summary_v5.json','w'),indent=1);print(sm['frames_by_owner'],sm['composition_full_span_s'])
