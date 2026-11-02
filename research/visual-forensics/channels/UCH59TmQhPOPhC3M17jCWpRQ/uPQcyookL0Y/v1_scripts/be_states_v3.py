# v3 = v2 with 7 merge groups (all dense/native-frame viewed by orchestrator); v1/v2 untouched. Card-internal hidden changes are sub-events, not states.
import csv
S=list(csv.DictReader(open('tables/states_v2_draft.csv')))
G=[('V002','V003','X002 fade-to-black continuing same face; dense strip viewed'),
   ('V041','V045','X041-X044 one continuous wide->tight zoom->hold->zoom-out shot; dense strips viewed (X043 reviewer=TRANSITION, merged by orchestrator on dense view)'),
   ('V052','V053','X052 fade-in of same blackboard shot; dense strip viewed'),
   ('V069','V070','X069 white->wood dissolve then continuous pull-back/pan with man entering f10349-10353; NATIVE frames f10347-10356 viewed'),
   ('V088','V089','X088 same white card: 3000 label removed and crowd slides in f13354-13357; NATIVE frames f13352-13361 viewed'),
   ('V092','V093','X092 fade-out to black same pose; dense strip viewed'),
   ('V095','V096','X095 fade-in same cave scene; dense strip viewed')]
idx={r['state_v2']:i for i,r in enumerate(S)};out=[];i=0;gm={a:(b,n) for a,b,n in G}
while i<len(S):
    r=S[i]
    if r['state_v2'] in gm:
        b,n=gm[r['state_v2']];mem=S[i:idx[b]+1];kind=max(mem,key=lambda m:int(m['frames']))['kind']
        s,e=int(mem[0]['start']),int(mem[-1]['end']);ps=[m['state_v2'] for m in mem];basis=n;i=idx[b]+1
    else:
        s,e=int(r['start']),int(r['end']);kind=r['kind'];ps=[r['state_v2']];basis='';i+=1
        mem=[r]
    out.append(dict(start=s,end=e,frames=e-s+1,start_pts_s=round(s*1001/30000,3),end_pts_s=round(e*1001/30000,3),kind=kind,entry=mem[0]['entry'],parent_states_v2='+'.join(ps),merge_basis=basis,status='DRAFT_UNVALIDATED'))
for k,r in enumerate(out):r['state_v3']=f"W{k+1:03d}"
cols=['state_v3','start','end','frames','start_pts_s','end_pts_s','kind','entry','parent_states_v2','merge_basis','status']
w=csv.DictWriter(open('tables/states_v3_draft.csv','w',newline=''),cols);w.writeheader();w.writerows(out)
cov=[0]*14647
for r in out:
    for f in range(r['start'],r['end']+1):cov[f]+=1
assert all(c==1 for c in cov),'gap/overlap'
print(len(out),'states; gaps/overlaps 0; frames',sum(r['frames'] for r in out))
