# Remaining BURST candidates (113 minus 31 sampled). Frames: prev, burst, +3, +8 (same as sample). Adds v3 state id. External output frames/montages8/R*.jpg
import csv,cv2,numpy as np,sys,os
B=[r for r in csv.DictReader(open('tables/intra_state_events_detector.csv')) if r['kind']=='BURST']
done={r['seq'] for r in csv.DictReader(open('tables/burst_sample_ids.csv'))}
V3=list(csv.DictReader(open('tables/states_v3_draft.csv')))
def v3(f):
    for s in V3:
        if int(s['start'])<=f<=int(s['end']):return s['state_v3']
M=[float(r['px_diff_ge12']) for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))]
sel=[b for b in B if b['seq'] not in done];need={}
for b in sel:
    f=int(b['frame']);b['fr']=[f-1,f,min(14646,f+3),min(14646,f+8)];b['v3']=v3(f);[need.setdefault(x,None) for x in b['fr']]
cap=cv2.VideoCapture(sys.argv[1]);i=0
while i<=max(need):
    ok,fr=cap.read()
    if not ok:break
    if i in need:need[i]=cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA)
    i+=1
rows=[]
for b in sel:
    ims=[]
    for x in b['fr']:
        im=need[x].copy();cv2.rectangle(im,(0,0),(210,22),(0,0,0),-1);cv2.putText(im,f"f{x} t={x*1001/30000:.3f}",(4,16),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),1);ims.append(im)
    row=np.hstack(ims);cv2.putText(row,f"seq{b['seq']} {b['v3']} burst f{b['frame']} ge12={int(M[int(b['frame'])])}",(4,262),cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,255),2);rows.append(row)
os.makedirs('frames/montages8',exist_ok=True)
for k in range(0,len(rows),4):cv2.imwrite(f'frames/montages8/R{k//4+1:02d}.jpg',np.vstack(rows[k:k+4]),[cv2.IMWRITE_JPEG_QUALITY,78])
csv.writer(open('tables/burst_rest_ids.csv','w',newline='')).writerows([['row','seq','state_v1','state_v3','frame','montage']]+[[k+1,b['seq'],b['state_id'],b['v3'],b['frame'],f"R{k//4+1:02d}"] for k,b in enumerate(sel)])
print(len(sel),'bursts',(len(rows)+3)//4,'montages')
