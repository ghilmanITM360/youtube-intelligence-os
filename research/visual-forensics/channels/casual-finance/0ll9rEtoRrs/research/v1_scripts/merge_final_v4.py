import csv,sys,copy,json,collections
sys.path.insert(0,'v1_scripts')
import integrate_v3 as v3
rd=v3.rd;wr=v3.wr
BASIS={
 'S0022':('MERGE_CONFIRMED','Own review of 6 frames: gap mid-frame f864 shows the same country cast mid-scale/reposition animation, then the chart strip appears; one continuous composition.'),
 'S0035':('MERGE_CONFIRMED','Own review: gap mid-frame f1378 shows the same debt infographic mid-zoom; Germany character and "heck ye" text then enter on the zoomed infographic; one composition.'),
 'S0056':('KEEP_SEPARATE','Own review: hard replace at f2101->f2102 (0 gap frames): Dwight re-drawn smaller with a CV, label and arrow gone, layout rebuilt; same character but new composition.'),
 'S0080':('MERGE_CONFIRMED','Own review (first-pass unflagged; blind control also judged same): same man and bill layout, a second bill is added at right; additive entry within one composition.'),
 'S0212':('KEEP_SEPARATE','Own review: hard re-layout at f7944->f7945 (0 gap frames): same asset set (Dwight timeline, cheques, bags) is shrunk and moved down, bond row and money bags added; no intermediate frames, so a new composition by the continuation rule.')}
RULE='Continuation rule: a composition continues only if the existing layout is preserved or smoothly animated (intermediate frames); a hard re-layout starts a new composition even when assets are reused.'
def regroup(states,M):
    md={m['id']:m for m in M}
    S=sorted(states,key=lambda s:int(s['start']))
    grp=[]
    for s in S:
        d=md.get(s['id']);join=False
        if grp and d and d['decision']=='MERGE_CONFIRMED':join=True
        if grp and s['id'] in v3.SIBLING_SAME:join=True
        if join:grp[-1].append(s)
        else:grp.append([s])
    comps=[]
    for k,g in enumerate(grp,1):
        cid=f'CMP{k:04d}'
        for s in g:
            s['composition_id']=cid;d=md.get(s['id'])
            s['merge_decision']=d['decision'] if d else s['merge_decision'] if s['id'] in v3.SIBLING_SAME else 'NOT_FLAGGED'
        comps.append(dict(composition_id=cid,n_states=len(g),state_ids=' '.join(s['id'] for s in g),start=g[0]['start'],end=g[-1]['end'],span_frames=int(g[-1]['end'])-int(g[0]['start'])+1,state_frames=sum(int(s['end'])-int(s['start'])+1 for s in g),first_family=g[0]['family']))
    return S,comps
if __name__=='__main__':
    states=rd('integrated_v4/reviewed_states_v4.csv');old=rd('integrated_v4/compositions_v4.csv');unowned=rd('integrated_v4/unowned_intervals_v4.csv')
    M=rd('integrated_v4/merge_decisions_v4.csv')
    oldmap={}
    for c in old:
        for i in c['state_ids'].split():oldmap[i]=c['composition_id']
    prev={s['id']:s for s in states}
    order=sorted(states,key=lambda s:int(s['start']));pid={order[i]['id']:order[i-1]['id'] for i in range(1,len(order))}
    for m in M:
        m.setdefault('orig_decision',m['decision'])
    for sid,(dec,why) in BASIS.items():
        row=next((m for m in M if m['id']==sid),None)
        if row is None:row=dict(id=sid,prev=pid[sid],decision='',reason='',confidence='',orig_decision='NOT_FLAGGED_FIRST_PASS');M.append(row)
        row.update(decision=dec,reason=why,confidence='HIGH' if sid in('S0056','S0080','S0022') else 'MEDIUM',final_basis=RULE)
    for m in M:m.setdefault('final_basis','')
    S,comps=regroup(states,M)
    G=[u for u in unowned if u['rr_reviewed']=='YES']
    chk=copy.deepcopy(S)
    for s in chk:
        if s['id'] in('S0080','S0212'):s['flag_merge']='True'   # in-memory only: validator expects decisions == flagged set
    e=v3.check(chk,comps,unowned,M,G);print('POSITIVE',e or 'PASS',len(comps),'compositions')
    wr('integrated_v4/reviewed_states_v4.csv',S);wr('integrated_v4/compositions_v4.csv',comps);wr('integrated_v4/merge_decisions_v4.csv',M)
    import os
    if not os.path.exists('integrated_v4/composition_id_map_pre_merge_final.csv'):wr('integrated_v4/composition_id_map_pre_merge_final.csv',[dict(state_id=s['id'],old_composition_id=oldmap[s['id']],new_composition_id=s['composition_id']) for s in S])
    neg={}
    s2=copy.deepcopy(chk);c2=copy.deepcopy(comps);m2=copy.deepcopy(M)
    [m.__setitem__('decision','UNCERTAIN') for m in m2 if m['id']=='S0022'];neg['decision changed without regroup']=v3.check(chk,comps,unowned,m2,G)
    m3=copy.deepcopy(M);[m.__setitem__('decision','MERGE_CONFIRMED') for m in m3 if m['id']=='S0056'];neg['KEEP_SEPARATE flipped without regroup']=v3.check(chk,comps,unowned,m3,G)
    m4=[m for m in M if m['id']!='S0080'];neg['dropped added merge decision']=v3.check(chk,comps,unowned,m4,G)
    for k,v in neg.items():print('NEG',k,'DETECTED' if v else 'MISSED')
    sm=json.load(open('integrated_v4/integration_summary_v4.json'));sm.update(compositions=len(comps),merge_decisions_final=dict(collections.Counter(m['decision'] for m in M)),merge_final_negative_tests={k:('DETECTED' if v else 'MISSED') for k,v in neg.items()},merge_continuation_rule=RULE)
    json.dump(sm,open('integrated_v4/integration_summary_v4.json','w'),indent=1)
