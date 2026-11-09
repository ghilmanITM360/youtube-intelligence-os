import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
U={u['gap_id']:u for u in csv.DictReader(open('integrated_v3/unowned_intervals_v3.csv'))}
S={s['id']:s for s in csv.DictReader(open('integrated_v3/reviewed_states_v3.csv'))}
G=['U031','U035','U044','U059','U069','U073','U074','U077','U083','U088','U096','U120','U123']
need={}
for g in G:
    a,b=int(U[g]['start']),int(U[g]['end']);ns=int(S[U[g]['next_state']]['start']);assert ns==b+1,(g,ns,b)
    for f in range(a,ns+1):need[f]=None
cap=cv2.VideoCapture(src);last=max(need);i=0
while i<=last:
    ok,im=cap.read()
    if not ok:break
    if i in need:need[i]=cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY),(320,180)).astype(np.int16)
    i+=1
out=[]
for g in G:
    u=U[g];a,b=int(u['start']),int(u['end']);ref=need[b+1]
    d=[(f,round(float((np.abs(need[f]-ref)>24).mean()),4)) for f in range(a,b+1)]
    # earliest f such that all frames f..b are within 2% of next-state first frame
    k=b+1
    for f in range(b,a-1,-1):
        if dict(d)[f]<=0.02:k=f
        else:break
    out.append(dict(gap_id=g,next_state=u['next_state'],start=a,end=b,n=b-a+1,stable_match_from=k if k<=b else '',stable_frames=b-k+1 if k<=b else 0,diff_trace=' '.join(f'{f}:{x}' for f,x in d[-8:])))
w=csv.DictWriter(open('phaseA/boundary_probe.csv','w'),fieldnames=out[0].keys());w.writeheader();w.writerows(out)
for o in out:print(o['gap_id'],o['next_state'],o['start'],o['end'],o['n'],'match_from',o['stable_match_from'],o['stable_frames'],'|',o['diff_trace'][-70:])
