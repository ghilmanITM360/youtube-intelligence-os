# states v4 draft: v3 + one supported split (W085 at f13993, reviewer_11 consecutive frames) + annotation corrections. v1-v3 files untouched.
import csv,json,statistics as st
T='tables/'
V3=list(csv.DictReader(open(T+'states_v3_draft.csv')))
pts=lambda f:round(f*1001/30000,3)
M={int(r['frame']):float(r['pts_time']) for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))}
V4=[]
for r in V3:
    if r['state_v3']=='W085':
        for sid,s,e,note in (('W085a',13810,13992,'scene (sky/sun/tree) ... fades to black ~f13963; f13989-13992 pure black'),('W085b',13993,14059,'"and yet" text fades in from black at f13993 (reviewer_11 consecutive frames); fade-in ends within f13997-14003; fade to black again ~f14030-14058 (seq154/155 sparse)')):
            V4.append(dict(state_v4=sid,parent_state_v3='W085',start=s,end=e,kind='STABLE_OR_MOTION_STATE',entry=r['entry']+('' if sid=='W085a' else '+v4split'),parent_states_v2=r['parent_states_v2'],basis=note,status='DRAFT_UNVALIDATED'))
    else:
        V4.append(dict(state_v4=r['state_v3'],parent_state_v3=r['state_v3'],start=int(r['start']),end=int(r['end']),kind=r['kind'],entry=r['entry'],parent_states_v2=r['parent_states_v2'],basis=r['merge_basis'],status='DRAFT_UNVALIDATED'))
prev=-1
for s in V4:
    assert s['start']==prev+1,(s['state_v4'],prev);prev=s['end']
    s['frames']=s['end']-s['start']+1;s['start_pts_s']=round(M[s['start']],3);s['end_pts_s']=round(M[s['end']],3);s['dur_s']=round(s['frames']*1001/30000,3)
assert prev==14646 and V4[0]['start']==0
flds=['state_v4','parent_state_v3','start','end','frames','start_pts_s','end_pts_s','dur_s','kind','entry','parent_states_v2','basis','status']
w=csv.DictWriter(open(T+'states_v4_draft.csv','w',newline=''),fieldnames=flds);w.writeheader();w.writerows(V4)
print(len(V4),'states; gaps/overlaps 0; frames',sum(s['frames'] for s in V4))
# narration link
A=json.load(open('asr/asr_small_en.json'));words=A['words'];segs=A['segments']
rows=[]
for s in V4:
    a,b=s['start_pts_s'],s['end_pts_s']+1001/30000
    ws=[x for x in words if a<=(x['start']+x['end'])/2<b]
    txt=''.join(x['w'] for x in ws).strip()
    rows.append(dict(state_v4=s['state_v4'],start_frame=s['start'],end_frame=s['end'],start_s=a,dur_s=s['dur_s'],words=len(ws),words_per_min=round(len(ws)/s['dur_s']*60,1) if s['dur_s'] else 0,asr_text_PROVISIONAL=txt,label='PROVISIONAL_ASR_word_midpoint_in_state_NOT_LISTENING'))
w=csv.DictWriter(open(T+'narration_state_link_provisional.csv','w',newline=''),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# pacing (units: seconds from PTS; frames at 29.97fps)
d=[s['dur_s'] for s in V4];tot=14647*1001/30000
q=lambda p:sorted(d)[min(len(d)-1,int(p*len(d)))]
P=dict(unit='seconds (frames*1001/30000); source 29.97fps CFR 1920x1080',draft='states_v4_draft (DRAFT_UNVALIDATED, shot-level; excludes sub-state card swaps/camera moves)',states=len(d),total_s=round(tot,2),mean_s=round(st.mean(d),2),median_s=round(st.median(d),2),p10_s=q(.1),p90_s=q(.9),min_s=min(d),max_s=max(d),states_per_min=round(len(d)/tot*60,2),
 words_total=len(words),words_per_min_overall=round(len(words)/tot*60,1),
 per_minute=[dict(minute=m,states_started=sum(1 for s in V4 if m*60<=s['start_pts_s']<(m+1)*60),words=sum(1 for x in words if m*60<=x['start']<(m+1)*60)) for m in range(9)],
 caveat='Counts shot-level states only; in-state events (card swaps, camera moves, fades) are in the intra-state tables, so true visual-change rate is higher. Words from provisional ASR.')
json.dump(P,open(T+'pacing_metrics_v4.json','w'),indent=1);print(json.dumps({k:P[k] for k in P if k!='per_minute'}));print(P['per_minute'])
