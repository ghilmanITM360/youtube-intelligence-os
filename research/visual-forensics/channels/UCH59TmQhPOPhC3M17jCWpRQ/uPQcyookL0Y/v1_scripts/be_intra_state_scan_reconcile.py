# Intra-state scan (states >180 frames ~6 s) + reconcile with reviewer verdicts. Thresholds derived from this source (1920x1080, 30000/1001):
# STILL frame: px_diff_ge12<500 (~0.024% of frame). STILL run >=15 frames (0.5 s) => onset/offset events. BURST: ge12>=100000 (~4.8% frame) and >=8x rolling median (+-15f).
# All outputs are DETECTOR CANDIDATES, not visually verified.
import csv,numpy as np
r=list(csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv')));S=list(csv.DictReader(open('tables/states_machine.csv')))
g12=np.array([float(x['px_diff_ge12']) for x in r]);t=lambda i:round(i*1001/30000,3)
ev=[];summ=[]
for s in S:
    a,b=int(s['start']),int(s['end'])
    if b-a+1<=180: continue
    still=g12[a:b+1]<500; runs=[];st=None
    for k,v in enumerate(list(still)+[False]):
        if v and st is None: st=k
        if not v and st is not None:
            if k-st>=15: runs.append((a+st,a+k-1))
            st=None
    n0=len(ev)
    for x,y in runs:
        if x>a: ev.append((s['state_id'],'STILL_ONSET',x,y,f'still {y-x+1}f'))
        if y<b: ev.append((s['state_id'],'MOTION_ONSET_AFTER_STILL',y+1,y+1,''))
    for i in range(a+1,b+1):
        w=g12[max(a,i-15):min(b,i+15)+1]
        if g12[i]>=100000 and g12[i]>=8*max(np.median(w),1) and not (ev and ev[-1][2]==i-1 and ev[-1][1]=='BURST'): ev.append((s['state_id'],'BURST',i,i,f'ge12={int(g12[i])}'))
    summ.append((s['state_id'],a,b,b-a+1,round(float(still.mean()),3),len(runs),sum(1 for e in ev[n0:] if e[1]=='BURST')))
ev.sort(key=lambda e:e[2])
with open('tables/intra_state_events_detector.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['seq','state_id','kind','frame','end_frame','pts_s','note','status']);[w.writerow([i+1,e[0],e[1],e[2],e[3],t(e[2]),e[4],'DETECTOR_CANDIDATE_UNVERIFIED']) for i,e in enumerate(ev)]
with open('tables/long_state_summary.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['state_id','start','end','frames','still_fraction','still_runs_ge15f','bursts']);w.writerows(summ)
# reconcile: states entered via a cut the reviewers judged SAME_SCENE_MOTION or UNCLEAR get a flag; originals untouched
V={x['id']:x for x in csv.DictReader(open('tables/review_verdicts_sparse_montage.csv'))}
with open('tables/states_reconciled_v1.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(list(S[0])+['entry_review_verdict','reconcile_flag']);flag=0
    for s in S:
        e=s['entry'].split('_')[0]; v=V.get(e,{}).get('reviewer_verdict','') if e.startswith('A') else ''
        fl='SPLIT_DOUBTFUL_SAME_SCENE_MOTION' if v=='SAME_SCENE_MOTION' else ('ENTRY_UNCLEAR' if v=='UNCLEAR' else ('TRANSITION_STATE_REVIEWER_'+v if s['kind']=='TRANSITION_STATE' and v else ''))
        flag+=bool(fl); w.writerow(list(s.values())+[v,fl])
# structural check on reconciled table
R=list(csv.DictReader(open('tables/states_reconciled_v1.csv')));cov=np.zeros(len(r),int)
for s in R: cov[int(s['start']):int(s['end'])+1]+=1
print('long states',len(summ),'events',len(ev),dict((k,sum(e[1]==k for e in ev)) for k in set(e[1] for e in ev)));print('flagged states',flag,'uncovered',int((cov==0).sum()),'overlap',int((cov>1).sum()),'states',len(R))
print('flags:',[(s['state_id'],s['reconcile_flag'],s['entry']) for s in R if s['reconcile_flag']])
