import pandas as pd, numpy as np, json
E=pd.read_csv('tables/episodes_v2.csv').merge(pd.read_csv('tables/episode_evidence.csv'),on='ep')
M=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv',usecols=['frame','pts_time'])
PTS=M.pts_time.values; N=len(M)
SINGLE={'HARD_REPLACE_FULL','LARGE_PARTIAL_REPLACE','PARTIAL_OR_ADDITIVE'}
def kind(r):
    if r.n<=2:
        return 'STATE_BOUNDARY' if r.cls in SINGLE else 'MICRO_EVENT'
    return 'STATE_TRANSITION_MOTION' if r.net_changed_frac>=0.02 else 'INTRA_STATE_MOTION'
E['kind']=E.apply(kind,axis=1)
print(E.kind.value_counts().to_dict())
# states
bnd=E[E.kind.isin(['STATE_BOUNDARY','STATE_TRANSITION_MOTION'])].sort_values('start')
states=[];cur=0;ent=None
for r in bnd.itertuples():
    end=r.start-1
    if end>=cur: states.append(dict(start=cur,end=end,entry_ep=ent,exit_ep=r.ep))
    cur=r.start if r.kind=='STATE_BOUNDARY' else r.end+1; ent=r.ep
states.append(dict(start=cur,end=N-1,entry_ep=ent,exit_ep=None))
S=pd.DataFrame(states);S.insert(0,'state_id',[f'S{k:04d}' for k in range(len(S))])
S['n_frames']=S.end-S.start+1;S['pts_start']=PTS[S.start].round(4);S['pts_end']=PTS[S.end].round(4);S['duration_s']=(S.n_frames/24).round(4)
# shot inference (INFERRED): new shot at full replace or content IoU<0.5 on a boundary
eb=E.set_index('ep')
shot=0;shots=[]
for r in S.itertuples():
    if r.entry_ep is None or pd.isna(r.entry_ep): shot+=1
    else:
        x=eb.loc[int(r.entry_ep)]
        if x.cls=='HARD_REPLACE_FULL' or x.content_iou<0.5: shot+=1
    shots.append(f'SH{shot:03d}')
S['shot_id_inferred']=shots
S['rep_ep']=S.entry_ep.apply(lambda v:0 if pd.isna(v) else int(v))
S['rep_image']=S.rep_ep.apply(lambda v:f'frames/ep_stable/e{v:04d}.jpg')
# children
def children(r,kinds):
    c=E[(E.kind.isin(kinds))&(E.start>=r.start)&(E.end<=r.end)]
    return ';'.join(f'EP{int(x):04d}' for x in c.ep)
S['micro_events']=[children(r,['MICRO_EVENT']) for r in S.itertuples()]
S['motion_intervals']=[children(r,['INTRA_STATE_MOTION']) for r in S.itertuples()]
S['entry_ep']=S.entry_ep.apply(lambda v:'' if pd.isna(v) else f'EP{int(v):04d}');S['exit_ep']=S.exit_ep.apply(lambda v:'' if pd.isna(v) else f'EP{int(v):04d}')
S.to_csv('tables/states_machine.csv',index=False);E.to_csv('tables/episodes_classified.csv',index=False)
print(len(S),'states',S.shot_id_inferred.nunique(),'inferred shots; min dur',S.duration_s.min(),'median',S.duration_s.median())
print('micro children',sum(1 for v in S.micro_events if v),'intra motion',sum(1 for v in S.motion_intervals if v))
# verify coverage: states + transition motions cover all frames
cov=np.zeros(N,int)
for r in S.itertuples(): cov[r.start:r.end+1]+=1
for r in E[E.kind=='STATE_TRANSITION_MOTION'].itertuples(): cov[r.start:r.end+1]+=1
print('uncovered',int((cov==0).sum()),'overlap',int((cov>1).sum()))
