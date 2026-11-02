# v4 review packs: consecutive/dense native-source frames (resized for montage) for merge boundaries, discrepancies, UNCLEAR bursts, and 52 onset candidates. Output external frames/montages9 + tables/v4_pack_index.json
import csv,cv2,numpy as np,sys,os,json
SRC=sys.argv[1];os.makedirs('frames/montages9',exist_ok=True)
need={}
def want(f):
    f=max(0,min(14646,int(f)));need.setdefault(f,{});return f
packs=[] # (name,cols,tilew,tileh,[(label,[frames])...]) -> tiles
def tiles(fr): return [want(f) for f in fr]
# merges
B={r['id']:r for r in csv.DictReader(open('tables/v2_boundaries.csv'))}
for i in "X002 X041 X042 X043 X044 X052 X069 X088 X092 X095".split():
    b=int(B[i]['frames'].split('|')[2])
    packs.append((f'M_{i}_consec',3,480,270,tiles(range(b-4,b+5))))
    packs.append((f'M_{i}_context',3,480,270,tiles(range(b-60,b+61,15))))
# discrepancies
packs.append(('D_X001_f718-726',3,480,270,tiles(range(718,727))))
packs.append(('D_X001_f833-841',3,480,270,tiles(range(833,842))))
packs.append(('D_X001_f600-720_step15',3,480,270,tiles(range(600,721,15))))
packs.append(('D_X059_f9353-9361',3,480,270,tiles(range(9353,9362))))
packs.append(('D_X059_f9320-9360_step5',3,480,270,tiles(range(9320,9361,5))))
# unclear bursts
for s,f in (('22',697),('125',12989),('129',13100),('140',13362)):
    packs.append((f'U_seq{s}_consec',3,480,270,tiles(range(f-4,f+5))))
    packs.append((f'U_seq{s}_spaced',3,480,270,tiles(range(f-8,f+25,4))))
# onsets
O=[r for r in csv.DictReader(open('tables/intra_state_events_detector.csv')) if r['kind']!='BURST']
rows=[]
for r in O:
    f,e=int(r['frame']),int(r['end_frame'])
    fr=[f-2,f,(f+e)//2,e,e+1,e+3] if r['kind']=='STILL_ONSET' else [f-3,f-1,f,f+1,f+3,f+6]
    rows.append((f"seq{r['seq']} {r['kind'][:5]} {r['state_id']}",tiles(fr)))
for j in range(0,len(rows),4): packs.append((f'O_{j//4+1:02d}',6,320,180,rows[j:j+4]))
cap=cv2.VideoCapture(SRC);k=0;mx=max(need)
while k<=mx:
    ok,fr=cap.read()
    if not ok:break
    if k in need:
        need[k]={'a':cv2.resize(fr,(480,270),interpolation=cv2.INTER_AREA),'b':cv2.resize(fr,(320,180),interpolation=cv2.INTER_AREA)}
    k+=1
def tile(f,w):
    im=need[f]['a' if w==480 else 'b'].copy();cv2.rectangle(im,(0,0),(84 if w==480 else 70,16),(0,0,0),-1);cv2.putText(im,f"f{f}",(3,12),cv2.FONT_HERSHEY_SIMPLEX,.45,(255,255,255),1);return im
idx={}
for name,cols,w,h,body in packs:
    if name.startswith('O_'):
        lines=[]
        for lab,fr in body:
            r=np.hstack([tile(f,w) for f in fr]);cv2.putText(r,lab,(4,h-6),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,255,255),1);lines.append(r)
        img=np.vstack(lines);idx[name]={l:fr for l,fr in body}
    else:
        ts=[tile(f,w) for f in body]
        while len(ts)%cols:ts.append(np.zeros((h,w,3),np.uint8))
        img=np.vstack([np.hstack(ts[i:i+cols]) for i in range(0,len(ts),cols)]);idx[name]=body
    cv2.imwrite(f'frames/montages9/{name}.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,85])
json.dump(idx,open('tables/v4_pack_index.json','w'))
print(len(packs),'images')
