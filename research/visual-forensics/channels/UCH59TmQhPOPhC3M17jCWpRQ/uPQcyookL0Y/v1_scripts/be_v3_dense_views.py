# Dense (8-per-state) strips of left and right v2 states for the 20 flagged boundaries (9 SPURIOUS + 14 hidden_change, union). Also lists top change peaks per state to localise hidden cuts. Output external: frames/montages7/.
import csv,cv2,numpy as np,sys,os,json
S={r['state_v2']:r for r in csv.DictReader(open('tables/states_v2_draft.csv'))}
B={r['id']:r for r in csv.DictReader(open('tables/v2_boundaries.csv'))}
M=list(csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv')));cf=[float(r['changed_frac_thr10_320']) for r in M]
ids=sorted("X002 X041 X042 X044 X052 X069 X088 X092 X095 X001 X004 X017 X046 X059 X068 X074 X080 X087 X090 X097".split())
def pick(s,e,n=8):
    if e-s+1<=n: return list(range(s,e+1))
    return sorted(set(int(round(s+(e-s)*k/(n-1))) for k in range(n)))
plan=[];need={}
for i in ids:
    L,R=S[B[i]['left']],S[B[i]['right']];rows=[]
    for st in (L,R):
        s,e=int(st['start']),int(st['end']);fr=pick(s,e);rows.append((st['state_v2'],fr))
        [need.setdefault(f,None) for f in fr]
    pk=[]
    for st in (L,R):
        s,e=int(st['start']),int(st['end']);c=sorted(range(s+1,e+1),key=lambda f:-cf[f])[:3]
        pk.append({st['state_v2']:[(f,round(cf[f],3)) for f in c]})
    plan.append((i,rows,pk))
cap=cv2.VideoCapture(sys.argv[1]);k=0
while k<=max(need):
    ok,fr=cap.read()
    if not ok:break
    if k in need: need[k]=cv2.resize(fr,(240,135),interpolation=cv2.INTER_AREA)
    k+=1
os.makedirs('frames/montages7',exist_ok=True);blocks=[];peaks={}
for i,rows,pk in plan:
    peaks[i]=pk;rimgs=[]
    for sid,fr in rows:
        ims=[]
        for f in fr:
            im=need[f].copy();cv2.rectangle(im,(0,0),(150,16),(0,0,0),-1);cv2.putText(im,f"{sid} f{f}",(3,12),cv2.FONT_HERSHEY_SIMPLEX,.4,(255,255,255),1);ims.append(im)
        while len(ims)<8: ims.append(np.zeros((135,240,3),np.uint8))
        rimgs.append(np.hstack(ims))
    blk=np.vstack(rimgs);cv2.putText(blk,i,(4,130),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,255,255),2);blocks.append(blk)
for j in range(0,len(blocks),4): cv2.imwrite(f'frames/montages7/D{j//4+1:02d}.jpg',np.vstack(blocks[j:j+4]),[cv2.IMWRITE_JPEG_QUALITY,80])
json.dump(peaks,open('tables/v3_dense_peaks_measured.json','w'))
json.dump({i:[{sid:fr} for sid,fr in rows] for i,rows,_ in plan},open('tables/v3_dense_frames_index.json','w'))
print(len(blocks),'blocks',(len(blocks)+3)//4,'images')
