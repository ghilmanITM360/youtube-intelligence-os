import cv2,csv,sys,json,numpy as np
F=sys.argv[1]
ev=list(csv.DictReader(open('visual_event_ledger.csv')))
rows=[]
for e in ev:
    a,b=int(e['start_frame']),int(e['end_frame'])
    chg=list(range(a,b+1))
    if len(chg)>8: chg=chg[:8]
    spec=[('pre-8',a-8),('pre-1',a-1)]+[('chg',k) for k in chg]+[('post+1',b+1),('stable',b+10)]
    spec=[(l,max(0,min(8337,k))) for l,k in spec]
    rows.append((e,spec))
need={k for _,s in rows for _,k in s}
cap=cv2.VideoCapture(F);full={};i=0
while i<=max(need):
    ok,f=cap.read()
    if not ok:break
    if i in need: full[i]=f
    i+=1
def gray(f): return cv2.cvtColor(cv2.resize(f,(320,180),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY).astype(int)
out=[];img=[]
for e,spec in rows:
    d={k:v for l,k in spec for v in [0]}
    ks=[k for _,k in spec]
    pre=gray(full[spec[0][1]]),gray(full[spec[1][1]])
    post=gray(full[spec[-2][1]]),gray(full[spec[-1][1]])
    pre_stab=float((np.abs(pre[0]-pre[1])>10).mean());post_stab=float((np.abs(post[0]-post[1])>10).mean())
    chg_frames=[k for l,k in spec if l=='chg']
    step=[float((np.abs(gray(full[k])-gray(full[k-1] if k-1 in full else full[spec[1][1]]))>10).mean()) for k in chg_frames]
    out.append(dict(event_id=e['event_id'],before_state=e['before_state'],after_state=e['after_state'],frames_viewed=';'.join(f"{l}:f{k}(pts {(k+1)/30:.4f})" for l,k in spec),
      change_frames=len(chg_frames),pre_window_stable_frac=round(pre_stab,5),post_window_stable_frac=round(post_stab,5),
      pre_window_stable=pre_stab<0.0006,post_window_stable=post_stab<0.0006))
    tiles=[]
    for l,k in spec:
        t=cv2.resize(full[k],(300,169),interpolation=cv2.INTER_AREA)
        cv2.putText(t,f"{l} f{k} {(k+1)/30:.3f}s",(3,13),cv2.FONT_HERSHEY_SIMPLEX,0.42,(0,0,255),1)
        tiles.append(t)
    cv2.putText(tiles[0],f"{e['event_id']} {e['before_state']}>{e['after_state']}",(3,163),cv2.FONT_HERSHEY_SIMPLEX,0.42,(255,0,0),1)
    while len(tiles)<5: tiles.append(np.full((169,300,3),150,np.uint8))
    if len(tiles)>5:  # wrap long rows into 2 rows
        r1=np.hstack(tiles[:5]);r2=np.hstack((tiles[5:]+[np.full((169,300,3),150,np.uint8)]*5)[:5]);img.append(np.vstack([r1,r2]))
    else: img.append(np.hstack(tiles))
sheets=[];cur=[];h=0
for im in img:
    if h+im.shape[0]>1250: sheets.append(cur);cur=[];h=0
    cur.append(im);h+=im.shape[0]
sheets.append(cur)
for n,s in enumerate(sheets,1): cv2.imwrite(f'v2/boundary_sheet_{n:02d}.jpg',np.vstack(s),[cv2.IMWRITE_JPEG_QUALITY,78])
with open('v2/boundary_windows.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print(len(sheets),'sheets;',sum(1 for o in out if not(o['pre_window_stable'] and o['post_window_stable'])),'windows with instability')
for o in out:
    if not(o['pre_window_stable'] and o['post_window_stable']): print(o['event_id'],o['pre_window_stable_frac'],o['post_window_stable_frac'])
