import csv,json,cv2,numpy as np
W='.'
src=json.load(open('source_manifest.json'))['source_path']
S=sorted(csv.DictReader(open('integrated_v2/reviewed_states_v2.csv')),key=lambda s:int(s['start']))
need={}
pairs=[]
for i,s in enumerate(S):
    if s['flag_merge']=='True' and i>0:
        p=S[i-1]; pairs.append((p['id'],s['id'],int(p['end']),int(s['start']),int(p['start']),int(s['end'])))
for a,b,pe,ss,ps,se in pairs:
    for f in (pe,ss,ps,se): need[f]=None
fr=sorted(need); cap=cv2.VideoCapture(src); i=0; k=0
while k<len(fr):
    ok,im=cap.read()
    if not ok: break
    if i==fr[k]:
        need[i]=cv2.resize(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY),(320,180)).astype(np.int16); k+=1
        while k<len(fr) and fr[k]==i: k+=1
    i+=1
def frac(a,b): return float((np.abs(a-b)>24).mean())
out=[]
for a,b,pe,ss,ps,se in pairs:
    out.append(dict(prev=a,id=b,gap_frames=ss-pe-1,boundary_diff=round(frac(need[pe],need[ss]),4),prev_start_to_this_end=round(frac(need[ps],need[se]),4)))
w=csv.DictWriter(open('phaseA/merge_metrics.csv','w'),fieldnames=out[0].keys());w.writeheader();w.writerows(out)
print(len(out),i)
