import cv2, csv, sys, numpy as np, os
F=sys.argv[1]
st=list(csv.DictReader(open('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/02_VIDEO_FORENSICS/o3FQcd91MIs/STATES.csv')))
cap=cv2.VideoCapture(F)
def get(i):
    cap.set(cv2.CAP_PROP_POS_FRAMES,i); ok,f=cap.read(); return f
# representative frame: midpoint of each state (frame idx = round(t*30)-1 clamps)
items=[]
for s in st:
    a,b=float(s['start_sec']),float(s['end_sec'])
    # pick frame 0.5s after start if state long, else mid
    t=min(a+0.6,(a+b)/2) if b-a>1.2 else (a+b)/2
    items.append((s['state_id'],int(round(t*30))))
os.makedirs('frames',exist_ok=True)
W,H=640,360; per=6
for k in range(0,len(items),per):
    chunk=items[k:k+per]; tiles=[]
    for sid,i in chunk:
        f=get(i); f=cv2.resize(f,(W,H),interpolation=cv2.INTER_AREA)
        cv2.putText(f,f"{sid} f{i} t{(i+1)/30:.2f}",(8,24),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        tiles.append(f)
    while len(tiles)<per: tiles.append(np.zeros((H,W,3),np.uint8))
    sheet=np.vstack([np.hstack(tiles[:3]),np.hstack(tiles[3:])])
    cv2.imwrite(f'frames/state_sheet_{k//per+1:02d}.jpg',sheet,[cv2.IMWRITE_JPEG_QUALITY,80])
print(len(items),'states ->',(len(items)+per-1)//per,'sheets')
