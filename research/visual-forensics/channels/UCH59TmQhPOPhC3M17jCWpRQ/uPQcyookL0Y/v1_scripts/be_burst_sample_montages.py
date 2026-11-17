# Stratified sample of BURST candidates: per state with bursts, the strongest burst and the median-strength burst (max 2/state). Frames: prev, burst, +3, +8.
import csv,cv2,numpy as np,sys,os,collections
B=[r for r in csv.DictReader(open('tables/intra_state_events_detector.csv')) if r['kind']=='BURST']
M=[float(r['px_diff_ge12']) for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))]
by=collections.defaultdict(list)
for b in B: b['g']=M[int(b['frame'])]; by[b['state_id']].append(b)
sel=[]
for sid,L in sorted(by.items()):
    L=sorted(L,key=lambda b:-b['g']); pick=[L[0]]
    if len(L)>2: pick.append(L[len(L)//2])
    elif len(L)==2: pick.append(L[1])
    sel+=pick
need={}
for b in sel:
    f=int(b['frame']); b['fr']=[f-1,f,min(14646,f+3),min(14646,f+8)]; [need.setdefault(x,None) for x in b['fr']]
cap=cv2.VideoCapture(sys.argv[1]);i=0
while i<=max(need):
    ok,fr=cap.read()
    if not ok:break
    if i in need: need[i]=cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA)
    i+=1
rows=[]
for b in sel:
    ims=[]
    for x in b['fr']:
        im=need[x].copy();cv2.rectangle(im,(0,0),(210,22),(0,0,0),-1);cv2.putText(im,f"f{x} t={x*1001/30000:.3f}",(4,16),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255),1);ims.append(im)
    row=np.hstack(ims);cv2.putText(row,f"seq{b['seq']} {b['state_id']} burst f{b['frame']} ge12={int(b['g'])}",(4,262),cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,255),2);rows.append(row)
os.makedirs('frames/montages4',exist_ok=True)
for k in range(0,len(rows),4): cv2.imwrite(f'frames/montages4/P{k//4+1:02d}.jpg',np.vstack(rows[k:k+4]),[cv2.IMWRITE_JPEG_QUALITY,78])
csv.writer(open('tables/burst_sample_ids.csv','w',newline='')).writerows([['seq','state_id','frame']]+[[b['seq'],b['state_id'],b['frame']] for b in sel])
print(len(sel),'bursts',(len(rows)+3)//4,'montages')
