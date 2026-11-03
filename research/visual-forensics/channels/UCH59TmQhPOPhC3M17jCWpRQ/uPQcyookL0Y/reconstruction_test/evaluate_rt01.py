# Independent evaluation of RT-01 output against spec v2 criteria (measured from the rendered pixels, not from the worker's claims).
import cv2,json,numpy as np,subprocess,sys
from pathlib import Path
d=Path(sys.argv[1]);tl=json.loads((d/'timeline.json').read_text())
pr=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,codec_name,nb_frames','-of','json',str(d/'rt01.mp4')]))['streams'][0]
cap=cv2.VideoCapture(str(d/'rt01.mp4'));F=[]
while True:
    ok,im=cap.read()
    if not ok:break
    F.append(im)
H,W=F[0].shape[:2];C=[]
def box(k):
    b=tl['boxes'][k] if 'boxes' in tl else tl[k];x0,y0,x1,y1=(b if len(b)==4 else b)
    if x1<=1.0 and y1<=1.0 and (x1>x0):return int(x0*W),int(y0*H),int(x1*W),int(y1*H)
    return int(x0*W),int(y0*H),int((x0+x1)*W),int((y0+y1)*H)
def ink(im,bx):
    x0,y0,x1,y1=bx;g=cv2.cvtColor(im[y0:y1,x0:x1],cv2.COLOR_BGR2GRAY)<100;return g
crit={}
crit['format']=dict(ok=(pr['width'],pr['height'],pr['r_frame_rate'],pr['codec_name'])==(1920,1080,'30000/1001','h264'),got=pr)
bg=np.mean([F[len(F)//2][y,x] for y,x in [(5,5),(5,W-6),(H-6,5),(H-6,W-6)]],axis=0)[::-1];crit['bg_colour']=dict(ok=bool(np.all(np.abs(bg-252)<=4)),got=bg.round(1).tolist(),want='#fcfcfc')
# M1: measure reveal from pixels in line1 box: frames where ink extent grows; leftmost ink fixed
b1=box(tl.get('line1_key','line1'));ext=[];left=[]
for im in F:
    g=ink(im,b1);cols=np.nonzero(g.any(0))[0];ext.append(int(cols.max()) if len(cols) else -1);left.append(int(cols.min()) if len(cols) else -1)
grow=[i for i in range(1,len(F)) if ext[i]>ext[i-1]+2];m1=(grow[0]-0,grow[-1]) if grow else None
dur=(grow[-1]-grow[0]+1) if grow else 0
lefts={left[i] for i in grow}
crit['M1_clip_reveal']=dict(ok=bool(grow) and 3<=dur<=6 and (max(lefts)-min(lefts)<=3),measured_growth_frames=grow,duration=dur,left_edge_values=sorted(lefts),want='3-6 frames, left-to-right (left ink edge fixed)')
# M3: line2 ink bbox height per frame -> peak then smaller settle
b2=box(tl.get('line2_key','line2'));hh=[]
for im in F:
    g=ink(im,b2);rows=np.nonzero(g.any(1))[0];hh.append(int(rows.max()-rows.min()) if len(rows) else 0)
on=next((i for i,h in enumerate(hh) if h>0),None)
if on is not None:
    win=hh[on:on+10];pk=int(np.argmax(win));final=hh[min(len(hh)-1,on+15)]
    crit['M3_pop_overshoot']=dict(ok=pk<=2 and win[pk]>final*1.03,onset=on,heights=win,peak_offset=pk,final=final,want='peak within 2 frames of onset, then settle smaller')
else:crit['M3_pop_overshoot']=dict(ok=False,note='line2 never appears')
# M5: mouth box changes; each change must be a single-frame replacement (no intermediate states)
bm=box(tl.get('mouth_key','mouth'));sig=[ink(im,bm).astype(np.uint8) for im in F];chg=[i for i in range(1,len(F)) if (sig[i]!=sig[i-1]).mean()>0.01]
runs=[];[runs.append([i,i]) if not runs or i>runs[-1][1]+1 else runs[-1].__setitem__(1,i) for i in chg]
crit['M5_pose_swap']=dict(ok=len(runs)>=2 and all(a==b for a,b in runs),change_frames=chg,want='>=2 swaps, each completes in exactly 1 frame')
crit['claims_vs_measured']=dict(M1_claimed=[tl.get('M1_start'),tl.get('M1_end')],M5_claimed=tl.get('M5_swaps'))
res={'frames':len(F),'criteria':crit,'overall':'PASS' if all(v.get('ok',True) for k,v in crit.items() if k!='claims_vs_measured') else 'FAIL'}
(d/'EVALUATION.json').write_text(json.dumps(res,indent=1,default=int));print(json.dumps(res,indent=1,default=int)[:3000])
