# Build contiguous state table from reviewed boundary candidates: HARD_CUT starts new state at new_state_first_frame;
# FADE/SLIDE: multi-frame candidate becomes TRANSITION_STATE [start,end] then new state; same-scene classes become intra-state events.
import csv,sys
rv=sys.argv[1];FPS=30000/1001
N=sum(1 for _ in open('FULL_FRAME_MEASUREMENTS.csv'))-1
C={x['cand']:x for x in csv.DictReader(open('tables/boundary_candidates.csv'))};R=list(csv.DictReader(open(f'agents/{rv}/boundary_review.csv')))
cuts=[];events=[]
for x in R:
    c=C[x['cand']];k=x['classification'];a,b=int(c['start']),int(c['end'])
    if k=='HARD_CUT':cuts.append((int(x['new_state_first_frame'].lstrip('f')),None,x['cand'],k))
    elif k in('FADE_OR_DISSOLVE','SLIDE_WIPE_OR_MASK_TRANSITION'):
        nf=int(x['new_state_first_frame'].lstrip('f'))
        if b-a>=2:cuts.append((a,'T',x['cand'],k));cuts.append((max(nf,b+1),None,x['cand'],k+'_EXIT'))
        else:cuts.append((nf,None,x['cand'],k))
    else:events.append(dict(cand=x['cand'],start=a,end=b,start_pts_s=round(a/FPS,3),classification=k,note=x['note'],before=x['before_description'],after=x['after_description']))
cuts=sorted({c[0]:c for c in cuts if 0<c[0]<N}.values())
S=[];cur=0;kind='STABLE_OR_MOTION_STATE';entry='START'
for f,t,cand,k in cuts:
    if f<=cur:continue
    S.append(dict(start=cur,end=f-1,kind=kind,entry=entry));cur=f;kind='TRANSITION_STATE' if t=='T' else 'STABLE_OR_MOTION_STATE';entry=f'{cand}:{k}'
S.append(dict(start=cur,end=N-1,kind=kind,entry=entry))
for i,s in enumerate(S,1):s.update(state=f'S{i:03d}',frames=s['end']-s['start']+1,start_pts_s=round(s['start']/FPS,6),end_pts_s=round((s['end']+1)/FPS,6))
assert S[0]['start']==0 and S[-1]['end']==N-1 and all(x['end']+1==y['start'] for x,y in zip(S,S[1:]))
for e in events:e['state']=next(s['state'] for s in S if s['start']<=e['start']<=s['end'])
keys=['state','start','end','frames','start_pts_s','end_pts_s','kind','entry']
w=csv.DictWriter(open('tables/states_v1.csv','w',newline=''),keys,extrasaction='ignore');w.writeheader();w.writerows(S)
w=csv.DictWriter(open('tables/intra_state_events_v1.csv','w',newline=''),list(events[0]));w.writeheader();w.writerows(events)
d=sorted(s['frames']/FPS for s in S);print('states',len(S),'transitions',sum(s['kind']=='TRANSITION_STATE' for s in S),'events',len(events),'frames',N,'dur min/med/max',round(d[0],2),round(d[len(d)//2],2),round(d[-1],2))
