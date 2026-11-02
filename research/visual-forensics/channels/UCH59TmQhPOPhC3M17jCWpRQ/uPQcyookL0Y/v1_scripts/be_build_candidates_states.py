# Barely Evolved uPQcyookL0Y: thresholds derived from THIS source (30000/1001 fps, 1920x1080, CFR). Not copied from Casually Finance (24 fps, whiteboard).
# Tier A: runs of changed_frac_thr10_320>=0.5 (hard-cut / transition candidates). Tier B: local peaks 0.15<=cf<0.5 and >=3x neighbour max (+-4f).
import csv,numpy as np
r=list(csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))); N=len(r)
cf=np.array([float(x['changed_frac_thr10_320']) for x in r]); pts=lambda i:i*1001/30000
idx=np.nonzero(cf>=0.5)[0]; runs=[];s=None
for i in idx:
    if s is None: s=p=int(i)
    elif i==p+1: p=int(i)
    else: runs.append((s,p)); s=p=int(i)
runs.append((s,p))
cands=[]
for k,(a,b) in enumerate(runs,1):
    cands.append(dict(id=f'A{k:03d}',tier='A',start=a,end=b,kind='CUT_CANDIDATE' if a==b else 'TRANSITION_CANDIDATE',peak_cf=round(float(cf[a:b+1].max()),4)))
inA=np.zeros(N,bool)
for a,b in runs: inA[max(0,a-4):b+5]=True
nb=0
for i in range(1,N):
    if 0.15<=cf[i]<0.5 and not inA[i]:
        nbh=np.r_[cf[max(0,i-4):i],cf[i+1:i+5]]
        if cf[i]>=3*nbh.max()+0.02: nb+=1; cands.append(dict(id=f'B{nb:03d}',tier='B',start=i,end=i,kind='SOFT_PEAK_CANDIDATE',peak_cf=round(float(cf[i]),4)))
with open('tables/candidates.csv','w',newline='') as f:
    w=csv.DictWriter(f,['id','tier','start','end','kind','peak_cf','start_pts_s','end_pts_s']); w.writeheader()
    for c in cands: c['start_pts_s']=round(pts(c['start']),6); c['end_pts_s']=round(pts(c['end']),6); w.writerow(c)
# draft states: contiguous partition; multi-frame A runs become their own TRANSITION state
bounds=[];cur=0;sid=0;states=[]
def add(a,b,kind,entry):
    global sid; sid+=1; states.append(dict(state_id=f'S{sid:03d}',start=a,end=b,kind=kind,entry=entry,frames=b-a+1,start_pts_s=round(pts(a),6),end_pts_s=round(pts(b),6),duration_s=round((b-a+1)*1001/30000,6)))
prev_entry='START'
for k,(a,b) in enumerate(runs,1):
    if a==0: continue
    if a-1>=cur: add(cur,a-1,'STABLE_OR_MOTION_STATE',prev_entry)
    if b>a: add(a,b,'TRANSITION_STATE',f'A{k:03d}'); cur=b+1; prev_entry=f'A{k:03d}_exit'
    else: cur=a; prev_entry=f'A{k:03d}'
if cur<=N-1: add(cur,N-1,'STABLE_OR_MOTION_STATE',prev_entry)
with open('tables/states_machine.csv','w',newline='') as f:
    w=csv.DictWriter(f,list(states[0])); w.writeheader(); w.writerows(states)
cov=np.zeros(N,int)
for s_ in states: cov[s_['start']:s_['end']+1]+=1
print('candidates A',sum(c['tier']=='A' for c in cands),'B',nb,'states',len(states),'frames',N,'uncovered',int((cov==0).sum()),'overlap',int((cov>1).sum()),'sum_frames',sum(s_['frames'] for s_ in states))
d=sorted(s_['duration_s'] for s_ in states); print('state dur min',d[0],'median',d[len(d)//2],'max',d[-1])
