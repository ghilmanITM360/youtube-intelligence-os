import csv,json,shutil,os,copy,sys
sys.path.insert(0,'v1_scripts')
import integrate_v3 as v3
rd=v3.rd;wr=v3.wr
os.makedirs('integrated_v4',exist_ok=True)
for f in os.listdir('integrated_v3'):
    if f.endswith(('.csv','.json')) and 'v3' in f:
        shutil.copy('integrated_v3/'+f,'integrated_v4/'+f.replace('_v3','_v4'))
    elif f.endswith('.csv'):shutil.copy('integrated_v3/'+f,'integrated_v4/'+f)
spike={r['gap_id']:r for r in rd('phaseA/boundary_spike.csv')}
RULE=[g for g,r in spike.items() if r['isolated_spike']=='YES']
def apply(states,unowned,rule=RULE):
    S={s['id']:s for s in states}
    for u in unowned:
        u.setdefault('orig_end',u['end']);u.setdefault('boundary_rule','');u.setdefault('orig_n_frames',u['n_frames'])
    for s in states:s.setdefault('orig_start',s['start']);s.setdefault('boundary_rule','')
    for u in unowned:
        if u['gap_id'] in rule:
            b=int(u['end']);ns=S[u['next_state']];assert int(ns['start'])==b+1
            u['end']=str(b-1);u['n_frames']=str(int(u['n_frames'])-1);u['pts_end']=f"{b/24:.4f}";u['boundary_rule']='SPIKE_LAST_FRAME_REASSIGNED_TO_NEXT_STATE'
            ns['start']=str(b);ns['n_frames']=str(int(ns['n_frames'])+1);ns['pts_start']=f"{(b+1)/24:.4f}";ns['duration_s']=f"{int(ns['n_frames'])/24:.4f}";ns['boundary_rule']='STARTS_ONE_FRAME_EARLIER_BY_SPIKE_RULE'
    return states,unowned
if __name__=='__main__':
    states=rd('integrated_v3/reviewed_states_v3.csv');comps=rd('integrated_v3/compositions_v3.csv');unowned=rd('integrated_v3/unowned_intervals_v3.csv');M=rd('integrated_v3/merge_decisions_v3.csv')
    G=[u for u in unowned if u['rr_reviewed']=='YES']
    states,unowned=apply(states,unowned)
    S0=sorted(states,key=lambda s:int(s['start']))
    byc={}
    for s in S0:byc.setdefault(s['composition_id'],[]).append(s)
    for c in comps:
        m=byc[c['composition_id']];c['start']=m[0]['start'];c['end']=m[-1]['end'];c['span_frames']=int(m[-1]['end'])-int(m[0]['start'])+1;c['state_frames']=sum(int(x['end'])-int(x['start'])+1 for x in m)
    e=v3.check(states,comps,unowned,M,G);print('POSITIVE',e or 'PASS','rule applied to',len(RULE),'gaps:',' '.join(RULE))
    ch=[s['id'] for s in states if s['boundary_rule']];print(len(ch),'states changed')
    wr('integrated_v4/reviewed_states_v4.csv',states);wr('integrated_v4/compositions_v4.csv',comps);wr('integrated_v4/unowned_intervals_v4.csv',unowned)
    wr('integrated_v4/boundary_rule_application_v4.csv',[dict(gap_id=g,next_state=spike[g]['gap_id'] and [u['next_state'] for u in unowned if u['gap_id']==g][0],frame_reassigned=spike[g]['end'],jump_at_end=spike[g]['jump_at_end'],prior_4_consec=spike[g]['prior_4_consec']) for g in RULE])
    neg={}
    # revert a patch on one side only -> must fail tiling
    s2=copy.deepcopy(states);[s.__setitem__('start',s['orig_start']) for s in s2 if s['boundary_rule']][:1]
    neg['state boundary reverted without gap']=v3.check(s2,comps,unowned,M,G)
    u2=copy.deepcopy(unowned);x=[u for u in u2 if u['boundary_rule']][0];x['end']=x['orig_end'];neg['gap boundary reverted without state']=v3.check(states,comps,u2,M,G)
    s3=copy.deepcopy(states);y=[s for s in s3 if s['boundary_rule']][0];y['start']=str(int(y['start'])-1);neg['over-extended state']=v3.check(s3,comps,unowned,M,G)
    for k,v in neg.items():print('NEG',k,'DETECTED' if v else 'MISSED',v[:2])
    sm=json.load(open('integrated_v3/integration_summary_v3.json'));sm.update(status='BOUNDARY_RULE_APPLIED_STRUCTURE_STILL_NOT_SEMANTICALLY_CERTIFIED',boundary_rule_gaps=RULE,boundary_rule_not_applied=[g for g in spike if g not in RULE],validator_positive='PASS' if not e else 'FAIL',boundary_negative_tests={k:('DETECTED' if v else 'MISSED') for k,v in neg.items()},unowned_frames=sum(int(u['n_frames']) for u in unowned),state_frames=sum(int(s['n_frames']) for s in states))
    json.dump(sm,open('integrated_v4/integration_summary_v4.json','w'),indent=1);print(sm['state_frames'],sm['unowned_frames'])
