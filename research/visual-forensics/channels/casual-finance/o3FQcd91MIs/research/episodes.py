import csv, json
r=list(csv.DictReader(open('tables/frame_metrics.csv')))
fr=[(int(x['frame']),float(x['pts_time']),float(x['changed_frac_thr10']),float(x['mean_abs_diff']),float(x['mean_luma'])) for x in r]
THR=0.0006  # >=~35px of 57600 at 320x180
act=[f[0] for f in fr if f[2]>=THR]
eps=[];cur=None
for i in act:
    if cur and i-cur[1]<=3: cur[1]=i
    else:
        if cur: eps.append(cur)
        cur=[i,i]
if cur: eps.append(cur)
out=[]
for k,(a,b) in enumerate(eps):
    seg=[f for f in fr if a<=f[0]<=b]
    out.append(dict(ep=k+1,start_frame=a,end_frame=b,start_pts=round(fr[a][1],4),end_pts=round(fr[b][1],4),n=b-a+1,peak_frac=round(max(s[2] for s in seg),4),sum_frac=round(sum(s[2] for s in seg),3),peak_mad=round(max(s[3] for s in seg),2)))
json.dump(out,open('tables/episodes.json','w'))
with open('tables/episodes.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print(len(out),'episodes; frames active',len(act))
# prior states
st=[(x['state_id'],float(x['start_sec']),float(x['end_sec'])) for x in csv.DictReader(open('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/02_VIDEO_FORENSICS/o3FQcd91MIs/STATES.csv'))]
bounds=[s[1] for s in st[1:]]
miss=0;tab=[]
for bt in bounds:
    near=[e for e in out if e['start_pts']-0.34<=bt<=e['end_pts']+0.34]
    if not near: miss+=1; tab.append(bt)
print('prior boundaries',len(bounds),'with no episode within 0.34s:',miss,tab)
used=set()
for bt in bounds:
    for e in out:
        if e['start_pts']-0.34<=bt<=e['end_pts']+0.34: used.add(e['ep'])
extra=[e for e in out if e['ep'] not in used]
print('episodes not explained by prior boundary:',len(extra))
for e in extra: print(e)
