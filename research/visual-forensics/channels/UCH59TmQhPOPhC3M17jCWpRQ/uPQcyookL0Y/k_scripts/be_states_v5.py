import csv
S=list(csv.DictReader(open('tables/states_v4_draft.csv')))
F=1001/30000
mv={'W047':(8438,'W046','end'),'W086':(14059,'W085b','end')}
note={'W047':'v5: onset f8438 = first changed frame (static f8434-8437 MAD 0); classroom panel slides in from right over white card f8438-8441, settled f8442 (MEASURED + native f8438 viewed)',
 'W086':'v5: onset f14059 = first changed frame (fade-in from black begins; changed bbox x576-1289,y440-1063), luma 2->18->49 by f14063',
 'W085b':'v5: end f14058; fade-in from black f13993-13999 (static from f14000, MEASURED native); fade-out ~f14030-14058',
 'W046':'v5: end f8437','W081':'v5: hard cut at f13168 confirmed (MAD 161, 99.9% px changed; f13169-13174 static) - boundary unchanged'}
by={r['state_v4']:r for r in S}
for k,(s,prev,_) in mv.items():
    by[k]['start']=str(s);by[prev]['end']=str(s-1)
for r in S:
    a,b=int(r['start']),int(r['end']);r['frames']=str(b-a+1)
    r['start_pts_s']=str(round(a*F,3));r['end_pts_s']=str(round(b*F,3));r['dur_s']=str(round((b-a+1)*F,3))
    r['v5_note']=note.get(r['state_v4'],'')
    r['status']='DRAFT_UNVALIDATED'
for i,r in enumerate(S):
    assert (int(r['start'])==0) if i==0 else int(r['start'])==int(S[i-1]['end'])+1
assert int(S[-1]['end'])==14646 and sum(int(r['frames']) for r in S)==14647
with open('tables/states_v5_draft.csv','w',newline='') as o:
    w=csv.DictWriter(o,fieldnames=list(S[0].keys()));w.writeheader();w.writerows(S)
print(len(S),'ok')
