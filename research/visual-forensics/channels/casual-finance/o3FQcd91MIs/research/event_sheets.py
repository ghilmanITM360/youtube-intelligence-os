import cv2,csv,sys,numpy as np
F=sys.argv[1]
ev=list(csv.DictReader(open('visual_event_ledger.csv')))
need=set()
rowspec=[]
for e in ev:
    a,b=int(e['start_frame']),int(e['end_frame'])
    fr=[a-1]+list(range(a,min(b,a+2)+1))+[b+1]
    fr=sorted(set(fr)); rowspec.append((e['event_id'],e['before_state'],e['after_state'],fr)); need|=set(fr)
need|={0,8337}
cap=cv2.VideoCapture(F);cache={};i=0
while i<=max(need):
    ok,f=cap.read()
    if not ok:break
    if i in need: cache[i]=cv2.resize(f,(256,144),interpolation=cv2.INTER_AREA)
    i+=1
rows=[]
for eid,b,a,fr in rowspec:
    t=[]
    for k in fr:
        x=cache[k].copy();cv2.putText(x,f"f{k}",(4,14),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,0,255),1);t.append(x)
    cv2.putText(t[0],f"{eid} {b}>{a}",(4,138),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,0,0),1)
    while len(t)<5:t.append(np.full((144,256,3),150,np.uint8))
    rows.append(np.hstack(t[:5]))
per=8
for k in range(0,len(rows),per):
    cv2.imwrite(f'frames/event_sheet_{k//per+1:02d}.jpg',np.vstack(rows[k:k+per]),[cv2.IMWRITE_JPEG_QUALITY,75])
# first and last frame
cv2.imwrite('frames/first_last.jpg',np.hstack([cache[0],cache[8337]]))
print(len(rows),'rows',(len(rows)+per-1)//per,'sheets')
