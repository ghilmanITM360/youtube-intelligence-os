import csv,json,copy,statistics as st,collections
N=24298
rd=lambda p:list(csv.DictReader(open(p)))
def wr(p,rows,fields=None):
    f=fields or list(rows[0].keys());w=csv.DictWriter(open(p,'w',newline=''),fieldnames=f);w.writeheader();w.writerows(rows)
def load():
    S=sorted(rd('integrated_v2/reviewed_states_v2.csv'),key=lambda s:int(s['start']))
    M=[];[M.extend(rd(f'phaseA/merge_review_{i}.csv')) for i in(1,2,3)]
    G=[];[G.extend(rd(f'phaseA/gap_review_{i}.csv')) for i in(1,2)]
    return S,M,G
SIBLING_SAME={'S0089.2':'S0089.1','S0116.2':'S0116.1'}  # own frame review, phaseA/split_children
CORR={
 'S0089.1':'Brown-haired glasses man with green tie, left of frame, arm raised in thumbs-up; no text (f2962-3003).',
 'S0089.2':'Same man, arm lowered, neutral face; red handwritten "20 years" at upper right and a tiny caption beside him (f3004-3021).',
 'S0097.1':'Blank canvas with only a small tilted cheque icon at lower left (f3223-3226).',
 'S0097.2':'Timeline starts: "Dwight retires" label, man holding a cheque; red timeline bar grows with Year 1/15/30/35+ and money bags and cheques added (f3227-3348).',
 'S0116.1':'Row of four bond certificates at top; man holding cheque with "Dwight retires" label; red timeline bar begins to grow (f4097-4111).',
 'S0116.2':'Same layout; timeline labelled Year 1/15/30/35+ completes while money bags and cheques are added beneath the bonds (f4112-4208).',
 'S0475.1':'Smiling black-haired stick figure, centred, arms out, static (f22094-22116).',
 'S0475.2':'Globe with sleepy eyes and two to three hopping money-bag characters; one bag falls over at end (f22117-22157).',
 'S0475.3':'Frowning black-haired stick figure, centred, one arm bent across body, small arm movement (f22158-22227).',
 'S0466P':'Presenter (brown hair, shrug) at left of a line chart of active pension participants (defined contribution vs defined benefit) with a red arrow moving left to right along the lines (f21569-21627).',
 'S0466':'Hard replacement at f21628 (observed in sequential decode): green country cartoons across the lower half, web chart strip appears at top from about f21650 (f21628-21718).',
 'S0033':'Smiling spiky-haired stick figure centred, static through f1294. The earlier note of a portrait infographic cut-in before f1290 is NOT visible in sampled frames; infographic location unresolved (see U011/f1295).'}
def build():
    S,M,G=load()
    md={m['id']:m for m in M}
    grp=[];cur=None;comp_of={}
    for s in S:
        d=md.get(s['id']); join=False
        if d and d['decision']=='MERGE_CONFIRMED' and grp: join=True
        if s['id'] in SIBLING_SAME and grp: join=True
        if join: grp[-1].append(s)
        else: grp.append([s])
    states=[];comps=[]
    for k,g in enumerate(grp,1):
        cid=f'CMP{k:04d}'
        for s in g:
            t=dict(s);t['composition_id']=cid;d=md.get(s['id'])
            t['merge_decision']=d['decision'] if d else ('SIBLING_SAME_COMPOSITION' if s['id'] in SIBLING_SAME else 'NOT_FLAGGED');t['merge_confidence']=d['confidence'] if d else '';t['merge_reason']=d['reason'] if d else ''
            t['family']=t['family'] or 'F5 screenshot+character'
            t['corr_desc']=CORR.get(s['id'],'');t['corr_basis']='phaseA/split_children sheet, sequential decode, own review' if s['id'] in CORR else ''
            states.append(t)
        comps.append(dict(composition_id=cid,n_states=len(g),state_ids=' '.join(s['id'] for s in g),start=g[0]['start'],end=g[-1]['end'],span_frames=int(g[-1]['end'])-int(g[0]['start'])+1,state_frames=sum(int(s['end'])-int(s['start'])+1 for s in g),first_family=g[0]['family']))
    U=rd('integrated_v2/unowned_intervals_v2.csv');gm={r['gap_id']:r for r in rd('phaseA/gap_dense_metrics.csv')};gr={g['gap_id']:g for g in G}
    unowned=[]
    for u in U:
        t=dict(u);g=gr.get(u['gap_id']);m=gm.get(u['gap_id'])
        t['rr_reviewed']='YES' if g else 'NO'
        t['rr_class']=g['class'] if g else '';t['rr_secondary']=g['secondary'] if g else '';t['rr_hard_cut_frame_reviewer']=g['hard_cut_frame'] if g else ''
        t['rr_reason']=g['reason'] if g else '';t['rr_confidence']=(g.get('confidence') or g.get('confidence(HIGH/MEDIUM/LOW)')) if g else ''
        t['rr_limited_by_sampling']=(g.get('limited_by_sampling') or g.get('limited_by_sampling(YES/NO)')) if g else ''
        t['measured_max_consec_diff']=m['max_consec_diff'] if m else '';t['measured_frames_gt50pct']=m['frames_gt50pct'] if m else ''
        fp=u['sp_class'];t['rr_vs_second_pass']=('' if not g else 'SAME' if g['class']==fp else 'DIFFERS')
        unowned.append(t)
    return S,states,comps,unowned,M,G
def check(states,comps,unowned,M,G,orig_states=None,verbose=True):
    e=[]
    ids=[s['id'] for s in states]
    if len(ids)!=len(set(ids)):e.append('dup state id')
    if len(set(ids))!=530:e.append(f'state count {len(set(ids))}')
    cm=collections.Counter()
    for c in comps:
        for i in c['state_ids'].split():cm[i]+=1
    if set(cm)!=set(ids) or any(v!=1 for v in cm.values()):e.append('composition membership mismatch')
    if len({c['composition_id'] for c in comps})!=len(comps):e.append('dup composition id')
    cov=[0]*N
    for s in states:
        for f in range(int(s['start']),int(s['end'])+1):cov[f]+=1
    for u in unowned:
        for f in range(int(u['start']),int(u['end'])+1):cov[f]+=1
    if any(v>1 for v in cov):e.append('overlap')
    if any(v==0 for v in cov):e.append(f'uncovered {sum(v==0 for v in cov)}')
    if len(unowned)!=143:e.append('unowned count')
    mids={m['id'] for m in M}
    flagged={s['id'] for s in states if s['flag_merge']=='True'}
    if mids!=flagged:e.append('merge decisions do not cover flagged set')
    cid={s['id']:s['composition_id'] for s in states}
    order=[s['id'] for s in states]
    for m in M:
        i=order.index(m['id'])
        if m['decision']=='UNCERTAIN' and cid[order[i]]==cid[order[i-1]]:e.append('UNCERTAIN grouped '+m['id'])
        if m['decision']=='MERGE_CONFIRMED' and cid[order[i]]!=cid[order[i-1]]:e.append('CONFIRMED not grouped '+m['id'])
        if not m['reason'].strip():e.append('lost reviewer reason '+m['id'])
    for s in states:
        if '.' in s['id'] and s['id']!='S0466P' and not s.get('parent_id'):e.append('split child w/o parent '+s['id'])
    for c in comps:
        ms=c['state_ids'].split()
        if any(i not in order for i in ms):e.append('unknown member in '+c['composition_id']);continue
        idx=[order.index(i) for i in ms]
        if idx!=list(range(idx[0],idx[0]+len(idx))):e.append('noncontiguous '+c['composition_id'])
    if sum(1 for u in unowned if u['rr_reviewed']=='YES')!=len(G) or len(G)!=48:e.append('gap review coverage')
    for u in unowned:
        if u['rr_reviewed']=='YES' and not u['rr_reason'].strip():e.append('gap reason lost '+u['gap_id'])
    return e
if __name__=='__main__':
    S,states,comps,unowned,M,G=build()
    e=check(states,comps,unowned,M,G);print('POSITIVE',e or 'PASS')
    wr('integrated_v3/reviewed_states_v3.csv',states);wr('integrated_v3/compositions_v3.csv',comps);wr('integrated_v3/unowned_intervals_v3.csv',unowned)
    wr('integrated_v3/merge_decisions_v3.csv',M);wr('integrated_v3/split_child_corrections_v3.csv',[dict(state_id=k,corrected_description=v) for k,v in CORR.items()])
    import shutil
    for f in('reviewed_candidates_v2.csv','reviewed_disputes_v2.csv','cross_shard_references.csv','anomaly_ledger_v2.csv'):shutil.copy('integrated_v2/'+f,'integrated_v3/'+f.replace('_v2','_v3') if '_v2' in f else 'integrated_v3/'+f)
    # negative tests
    neg={}
    s2=copy.deepcopy(states);c2=copy.deepcopy(comps);c2[0]['state_ids']=c2[0]['state_ids'].split()[0]+' S9999';neg['bad composition member']=check(s2,c2,unowned,M,G)
    c3=copy.deepcopy(comps);c3.pop();neg['dropped composition']=check(states,c3,unowned,M,G)
    s4=copy.deepcopy(states);s4[10]['end']=str(int(s4[10]['end'])+5);neg['overlap']=check(s4,comps,unowned,M,G)
    u5=copy.deepcopy(unowned);u5.pop(5);neg['dropped gap']=check(states,comps,u5,M,G)
    m6=copy.deepcopy(M);m6[0]['reason']='';neg['lost reviewer provenance']=check(states,comps,unowned,m6,G)
    m7=copy.deepcopy(M);m7.pop();neg['missing merge decision']=check(states,comps,unowned,m7,G)
    m8=copy.deepcopy(M);[m.__setitem__('decision','MERGE_CONFIRMED') for m in m8 if m['decision']=='UNCERTAIN'];neg['uncertain flipped w/o regroup']=check(states,comps,unowned,m8,G)
    s9=copy.deepcopy(states);s9[3]['id']=s9[2]['id'];neg['duplicate state id']=check(s9,comps,unowned,M,G)
    for k,v in neg.items():print('NEG',k,'DETECTED' if v else 'MISSED',v[:2])
    dur=[c['span_frames']/24 for c in comps]
    summ=dict(status='MERGE_SPLIT_GAP_RECONCILED_STRUCTURE_STILL_NOT_SEMANTICALLY_CERTIFIED',states=len(states),compositions=len(comps),state_frames=sum(int(s['end'])-int(s['start'])+1 for s in states),unowned_intervals=len(unowned),unowned_frames=sum(int(u['n_frames']) for u in unowned),total_frames=N,
      merge_decisions=dict(collections.Counter(m['decision'] for m in M)),comp_median_span_s=round(st.median(dur),2),comp_mean_span_s=round(st.mean(dur),2),comp_p90_span_s=round(sorted(dur)[int(.9*len(dur))],2),
      gaps_rereviewed=48,gap_class_rr=dict(collections.Counter(u['rr_class'] for u in unowned if u['rr_reviewed']=='YES')),candidates_second_pass_not_reviewed=807,validator_positive='PASS' if not e else 'FAIL',negative_tests={k:('DETECTED' if v else 'MISSED') for k,v in neg.items()},audio='AUDIO_NOT_VERIFIED')
    json.dump(summ,open('integrated_v3/integration_summary_v3.json','w'),indent=1);print(json.dumps(summ,indent=1))
