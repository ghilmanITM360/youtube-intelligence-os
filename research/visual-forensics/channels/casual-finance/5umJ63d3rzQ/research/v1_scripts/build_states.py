# Machine-derived PRELIMINARY states from candidate_evidence.csv (unreviewed; visual review pass must confirm/correct). 30 fps.
import pandas as pd,numpy as np
E=pd.read_csv('tables/candidate_evidence.csv');M=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv',usecols=['pts_time']);PTS=M.pts_time.values;N=len(M);FPS=30
SINGLE={'HARD_REPLACE_FULL','LARGE_PARTIAL_REPLACE','PARTIAL_OR_ADDITIVE'}
def kind(r):
    if r.source=='SUB':return 'MICRO_EVENT_CANDIDATE'
    if r.n<=2:return 'STATE_BOUNDARY' if r.cls in SINGLE else 'MICRO_EVENT'
    return 'STATE_TRANSITION_MOTION' if r.net_changed_frac>=0.02 else 'INTRA_STATE_MOTION'
E['kind']=E.apply(kind,axis=1);E.to_csv('tables/candidates_classified.csv',index=False)
bnd=E[E.kind.isin(['STATE_BOUNDARY','STATE_TRANSITION_MOTION'])].sort_values('start')
st=[];cur=0;ent=None
for r in bnd.itertuples():
    if r.start-1>=cur:st.append(dict(start=cur,end=r.start-1,entry=ent,exit=r.id))
    cur=r.start if r.kind=='STATE_BOUNDARY' else r.end+1;ent=r.id
st.append(dict(start=cur,end=N-1,entry=ent,exit=None))
S=pd.DataFrame(st);S.insert(0,'state_id',[f'S{k:04d}' for k in range(len(S))])
S['n_frames']=S.end-S.start+1;S['pts_start']=PTS[S.start].round(4);S['pts_end']=PTS[S.end].round(4);S['duration_s']=(S.n_frames/FPS).round(4)
def ch(r,ks):
    c=E[E.kind.isin(ks)&(E.start>=r.start)&(E.end<=r.end)];return ';'.join(c.id)
S['micro_events']=[ch(r,['MICRO_EVENT','MICRO_EVENT_CANDIDATE']) for r in S.itertuples()]
S['motion_intervals']=[ch(r,['INTRA_STATE_MOTION']) for r in S.itertuples()]
S['entry']=S.entry.fillna('');S['exit']=S.exit.fillna('')
S['rep_image']=[f'frames/stable/{e}.jpg' if e else 'frames/stable/'+E.sort_values('start').id.iloc[0]+'.jpg' for e in S.entry]
S['review_status']='UNREVIEWED_MACHINE_DRAFT'
S.to_csv('tables/states_machine.csv',index=False)
cov=np.zeros(N,int)
for r in S.itertuples():cov[r.start:r.end+1]+=1
for r in E[E.kind=='STATE_TRANSITION_MOTION'].itertuples():cov[r.start:r.end+1]+=1
print(E.kind.value_counts().to_dict());print(len(S),'draft states; uncovered',int((cov==0).sum()),'overlap',int((cov>1).sum()),'median dur',S.duration_s.median(),'min',S.duration_s.min())
# scenedetect cross-check
sc=pd.read_csv('tables/scenedetect_candidates.csv');cuts=sc.start_frame.values[1:]
bs=set(E[E.kind=='STATE_BOUNDARY'].start.tolist()+E[E.kind=='STATE_TRANSITION_MOTION'].start.tolist())
hit=sum(1 for c in cuts if any(abs(c-b)<=2 for b in bs));print('scenedetect cuts',len(cuts),'within 2f of a draft boundary',hit)
bsorted=np.array(sorted(bs));near=sum(1 for b in bsorted if np.abs(cuts-b).min()<=2);print('draft boundaries',len(bsorted),'with a scenedetect cut within 2f',near)
