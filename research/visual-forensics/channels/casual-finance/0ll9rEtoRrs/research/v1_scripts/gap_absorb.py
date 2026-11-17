import csv,json,cv2,numpy as np,collections
src=json.load(open('source_manifest.json'))['source_path']
S=sorted(csv.DictReader(open('integrated_v4/reviewed_states_v4.csv')),key=lambda s:int(s['start']));SI={s['id']:s for s in S};BYEND={int(s['end']):s for s in S};BYSTART={int(s['start']):s for s in S}
U=list(csv.DictReader(open('integrated_v4/unowned_intervals_v4.csv')))
need=set()
for u in U:
    a,b=int(u['start']),int(u['end']);need|=set(range(a-1,b+2))
fr={};cap=cv2.VideoCapture(src);i=0;mx=max(need)
while i<=mx:
    ok,im=cap.read()
    if not ok:break
    if i in need:fr[i]=cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY),(320,180)).astype(np.int16)
    i+=1
d=lambda x,y:float((np.abs(fr[x]-fr[y])>24).mean())
out=[]
for u in U:
    a,b=int(u['start']),int(u['end']);p,n=BYEND[a-1],BYSTART[b+1]
    cons=[(f,d(f-1,f)) for f in range(a,b+2)]   # f-1 -> f, includes boundary at gap start (prev end -> a) and into next start
    cons_in=[(f,x) for f,x in cons if f<=b]      # cuts landing on a gap frame (start frame included)
    cut=max(cons_in,key=lambda t:t[1]) if cons_in else (a,0)
    cutf=cut[0] if cut[1]>=0.5 else None
    same=p['composition_id']==n['composition_id']
    rel=u['sp_relation_proposed']
    if same:dec,basis='ABSORB_WHOLE','prev and next state are the same composition'
    elif cutf is not None:dec,basis='SPLIT_AT_CUT',f'measured cut f{cutf} ({cut[1]:.2f}); before->prev composition, from cut->next composition'
    elif rel=='PREV':dec,basis='ABSORB_PREV','second-pass relation PREV; no measured cut >=50%'
    elif rel=='NEXT':dec,basis='ABSORB_NEXT','second-pass relation NEXT; no measured cut >=50%'
    elif rel=='UNCLEAR':
        d1=d(a-1,a);d2=d(b,b+1);m=max((x for f,x in cons_in),default=0)
        if d1<=0.05 and d2>0.10:dec,basis='ABSORB_PREV',f'measured: continuous from prev end (d={d1:.3f}); jump at next start d={d2:.3f}'
        elif d2<=0.05 and d1>0.10:dec,basis='ABSORB_NEXT',f'measured: jump at gap start d={d1:.3f}; continuous into next start (d={d2:.3f})'
        else:dec,basis='UNRESOLVED',f'UNCLEAR relation and no decisive measurement (d_start={d1:.3f}, d_end={d2:.3f})'
    else:dec,basis='KEEP_STANDALONE',f'second-pass relation {rel} ({u["rr_class"]}); not absorbed'
    out.append(dict(gap_id=u['gap_id'],start=a,end=b,n_frames=b-a+1,prev_state=p['id'],next_state=n['id'],prev_comp=p['composition_id'],next_comp=n['composition_id'],second_pass_relation=rel,rr_class=u['rr_class'],max_consec_in_gap=round(cut[1],3),cut_frame=cutf or '',decision=dec,basis=basis))
w=csv.DictWriter(open('integrated_v4/gap_absorption_decisions.csv','w'),fieldnames=out[0].keys());w.writeheader();w.writerows(out)
c=collections.Counter(o['decision'] for o in out);fc=collections.Counter()
for o in out:fc[o['decision']]+=o['n_frames']
print(c);print(fc)
