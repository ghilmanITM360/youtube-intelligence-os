# states_v2: split original draft states at reviewer-HARD_CUT candidates not already used as a split (tier B and second-detector C). Originals immutable. DRAFT, not semantically validated.
import csv,json,numpy as np
S=list(csv.DictReader(open('tables/states_machine.csv')))
A=list(csv.DictReader(open('tables/review_verdicts_sparse_montage.csv')))
C4=json.load(open('agents/reviewer_4/OUT_reviewer_4.json'))['verdicts'];Cc={r['id']:r for r in csv.DictReader(open('tables/candidates_second_detector.csv'))}
cuts=[(int(a['start']),a['id']) for a in A if a['tier']=='B' and a['reviewer_verdict']=='HARD_CUT']+[(int(Cc[v['id']]['start']),v['id']) for v in C4 if v['verdict']=='HARD_CUT']
cuts.sort();out=[];used=[]
for s in S:
    a,b=int(s['start']),int(s['end']);pts=[(f,i) for f,i in cuts if a<f<=b and s['kind']=='STABLE_OR_MOTION_STATE']
    cur=a;entry=s['entry']
    for f,i in pts:
        out.append((cur,f-1,s['kind'],entry,s['state_id']));cur=f;entry=i;used.append(i)
    out.append((cur,b,s['kind'],entry,s['state_id']))
n=14647;cov=np.zeros(n,int)
with open('tables/states_v2_draft.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['state_v2','start','end','frames','start_pts_s','end_pts_s','kind','entry','parent_state_v1','status'])
    for k,(a,b,kd,en,p) in enumerate(out,1):
        cov[a:b+1]+=1;w.writerow([f'V{k:03d}',a,b,b-a+1,round(a*1001/30000,3),round(b*1001/30000,3),kd,en,p,'DRAFT_UNVALIDATED'])
print('v1',len(S),'v2',len(out),'splits applied',len(used),used,'uncovered',int((cov==0).sum()),'overlap',int((cov>1).sum()),'frames',int(cov.sum()))
print('unapplied cut frames (in transition/at boundary):',[(i,f) for f,i in cuts if i not in used])
