# Merge reviewer JSON (7 shards) + machine tables -> core CSV deliverables. Fails loudly on any mismatch.
import json, glob, re, sys, cv2, numpy as np, pandas as pd
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-24-Uumnx2Fo6cE-deep-ct-scan/'
import os; os.chdir(R)
S=pd.read_csv('tables/states_machine.csv').fillna('')
E=pd.read_csv('tables/episodes_classified.csv').fillna('')
SUBC=pd.read_csv('subthreshold/subthreshold_clusters.csv'); SUBR=json.load(open('subthreshold/sub_review.json'))
PTS=pd.read_csv('FULL_FRAME_MEASUREMENTS.csv',usecols=['pts_time']).pts_time.values
ep_rev={}; st_rev={}
for k in range(1,8):
    j=json.load(open(f'agents/shard_{k}/OUT_shard_{k}.json'))
    for e in j['episodes']: assert e['ep'] not in ep_rev,('dup ep',e['ep']); e['shard']=k; ep_rev[e['ep']]=e
    for s in j['states']: assert s['id'] not in st_rev,('dup state',s['id']); s['shard']=k; st_rev[s['id']]=s
assert set(ep_rev)==set(E.ep), ('episode mismatch',len(set(E.ep)-set(ep_rev)),len(set(ep_rev)-set(E.ep)))
assert set(st_rev)==set(S.state_id), ('state mismatch',len(set(S.state_id)-set(st_rev)),len(set(st_rev)-set(S.state_id)))
def palette(path):
    im=cv2.imread(path)
    if im is None: return ''
    px=im.reshape(-1,3)[::7].astype(np.float32)
    _,lab,cen=cv2.kmeans(px,5,None,(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0),2,cv2.KMEANS_PP_CENTERS)
    cnt=np.bincount(lab.ravel(),minlength=5)/len(lab); o=np.argsort(-cnt)
    return ' '.join('#%02x%02x%02x:%.3f'%(int(cen[i][2]),int(cen[i][1]),int(cen[i][0]),cnt[i]) for i in o)
def parent_state(frame):
    m=S[(S.start<=frame)&(S.end>=frame)]
    return m.state_id.iloc[0] if len(m) else ''
rows=[]
for r in S.itertuples():
    a=st_rev[r.state_id]
    rows.append(dict(state_id=r.state_id,shot_id_inferred_machine=r.shot_id_inferred,start_frame=r.start,end_frame=r.end,n_frames=r.n_frames,pts_start=r.pts_start,pts_end=r.pts_end,duration_s=r.duration_s,
        entry_episode=r.entry_ep,exit_episode=r.exit_ep,micro_events=r.micro_events,intra_motion=r.motion_intervals,evidence_image=r.rep_image,review_shard=a['shard'],
        palette_measured=palette(r.rep_image),asr_text_unverified=r.asr_text_unverified,asr_status='ASR_ONLY_NOT_AUDIO_VERIFIED',
        **{k:a.get(k,'') for k in ['objects','background','illustration','typography','readable_text','unreadable_text','hierarchy','camera_motion','entry_exit','story_function','evidence','confidence','continuity','recon','prompt','family']}))
VS=pd.DataFrame(rows)
# inferred shot grouping from reviewer YES flags at state-entry episodes
shot=0;sid=[]
for r in S.itertuples():
    ent=int(r.entry_ep[2:]) if r.entry_ep else None
    if ent is None or ep_rev[ent].get('shot_boundary')=='YES': shot+=1
    sid.append(f'SH{shot:03d}')
VS['shot_id_inferred']=sid
n_yes=sum(1 for e in ep_rev.values() if e.get('shot_boundary')=='YES'); n_amb=sum(1 for e in ep_rev.values() if e.get('shot_boundary')=='AMBIGUOUS')
VS.to_csv('VISUAL_STATES.csv',index=False)
# boundary verification
bv=[]
for r in E.itertuples():
    a=ep_rev[r.ep]
    bv.append(dict(event_id=f'EP{r.ep:04d}',kind=r.kind,measured_class=r.cls,start_frame=r.start,end_frame=r.end,n_frames=r.n,pts_start=r.pts_start,pts_end=r.pts_end,peak_changed_frac_320=r.peak_frac,net_changed_frac=r.net_changed_frac,net_bbox_norm=r.net_bbox,content_iou=r.content_iou,
        frames_viewed=r.frames_viewed,evidence_sheet=f'{r.sheet}#row{r.sheet_row}',verdict=a['verdict'],final_type=a['type'],reviewer_description=a['desc'],shot_boundary_inferred=a.get('shot_boundary',''),confidence=a.get('confidence',''),
        label_measured='MEASURED_FRAME_EVENT',label_visual='VISUALLY_CONFIRMED_CHANGE' if a['verdict'] in('CONFIRMED','RECLASSIFIED') else ('CODEC_ARTIFACT' if a['verdict']=='CODEC_ARTIFACT' else 'UNVERIFIED'),
        label_shot='INFERRED_SHOT_BOUNDARY' if a.get('shot_boundary')=='YES' else ''))
for r in SUBC.itertuples():
    d=SUBR[r.sub_id]
    bv.append(dict(event_id=r.sub_id,kind='MICRO_EVENT_SUBTHRESHOLD',measured_class='SUBTHRESHOLD_HIGH_CONTRAST_CLUSTER',start_frame=r.start,end_frame=r.end,n_frames=r.n,pts_start=round(PTS[r.start],4),pts_end=round(PTS[r.end],4),peak_changed_frac_320='',net_changed_frac='',net_bbox_norm=r.diff_bbox,content_iou='',
        frames_viewed=f'pre,first,last,post+6',evidence_sheet=f'{r.sheet}#row{r.row}',verdict='CONFIRMED',final_type=d['type'],reviewer_description=d['desc'],shot_boundary_inferred='NO',confidence=d['confidence'],label_measured='MEASURED_FRAME_EVENT',label_visual='VISUALLY_CONFIRMED_CHANGE',label_shot=''))
BV=pd.DataFrame(bv);BV.to_csv('BOUNDARY_VERIFICATION.csv',index=False)
# intra-state events
ev=[];n=0
for r in E[E.kind=='MICRO_EVENT'].itertuples():
    a=ep_rev[r.ep];n+=1
    ev.append(dict(event_id=f'EVI{n:04d}',source_episode=f'EP{r.ep:04d}',tier='MAIN_THRESHOLD',parent_state=parent_state(r.start),start_frame=r.start,end_frame=r.end,pts_start=r.pts_start,pts_end=r.pts_end,type=a['type'],verdict=a['verdict'],description=a['desc'],confidence=a.get('confidence',''),evidence_sheet=f'{r.sheet}#row{r.sheet_row}',label='VISUALLY_CONFIRMED_CHANGE' if a['verdict'] in('CONFIRMED','RECLASSIFIED') else a['verdict']))
for r in SUBC.itertuples():
    d=SUBR[r.sub_id];n+=1
    ev.append(dict(event_id=f'EVI{n:04d}',source_episode=r.sub_id,tier='SUBTHRESHOLD',parent_state=parent_state(r.start),start_frame=r.start,end_frame=r.end,pts_start=round(PTS[r.start],4),pts_end=round(PTS[r.end],4),type=d['type'],verdict='CONFIRMED',description=d['desc'],confidence=d['confidence'],evidence_sheet=f'{r.sheet}#row{r.row}',label='VISUALLY_CONFIRMED_CHANGE'))
IV=pd.DataFrame(ev).sort_values('start_frame').reset_index(drop=True);IV['event_id']=[f'EVI{k+1:04d}' for k in range(len(IV))];IV.to_csv('INTRA_STATE_EVENTS.csv',index=False)
# motion intervals (n>=3 episodes)
mo=[];n=0
for r in E[E.n>=3].itertuples():
    a=ep_rev[r.ep];n+=1;m=a.get('motion') or {}
    prev=S[S.end<r.start].state_id.iloc[-1] if (S.end<r.start).any() else ''
    nxt=S[S.start>r.end].state_id.iloc[0] if (S.start>r.end).any() else ''
    parent=parent_state(r.start) if r.kind=='INTRA_STATE_MOTION' else ''
    mo.append(dict(motion_id=f'MOT{n:04d}',source_episode=f'EP{r.ep:04d}',kind=r.kind,measured_class=r.cls,start_frame=r.start,end_frame=r.end,n_frames=r.n,pts_start=r.pts_start,pts_end=r.pts_end,duration_s=round(r.n/24,3),state_before=prev,state_after=nxt,parent_state_if_intra=parent,
        motion_type=a['type'],path=m.get('path',''),easing=m.get('easing',''),duration_note=m.get('duration_note',''),description=a['desc'],verdict=a['verdict'],confidence=a.get('confidence',''),evidence_sheet=f'{r.sheet}#row{r.sheet_row}',peak_changed_frac=r.peak_frac,mean_changed_frac=r.mean_frac))
pd.DataFrame(mo).to_csv('MOTION_INTERVALS.csv',index=False)
print('states',len(VS),'episodes',len(BV)-len(SUBC),'sub',len(SUBC),'intra events',len(IV),'motion',len(mo))
print('verdicts',pd.Series([e['verdict'] for e in ep_rev.values()]).value_counts().to_dict())
print('shot YES',n_yes,'AMBIGUOUS',n_amb,'-> inferred shots in state table',VS.shot_id_inferred.nunique())
