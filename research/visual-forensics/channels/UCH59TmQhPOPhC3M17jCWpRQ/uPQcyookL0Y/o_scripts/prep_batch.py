# Checkpoint O+ batch prep: decode-verify rep frames, intra-state motion strips from measured peaks, ASR excerpt.
import cv2,csv,json,sys,numpy as np
from pathlib import Path
cv2.setNumThreads(1)
p=Path('.');batch,i0,i1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
FPS=30000/1001
S=list(csv.DictReader(open('tables/states_v6_draft.csv')))[i0:i1]
rep=list(csv.DictReader(open(f'tables/k_rep_frames_{batch}.csv')));repf={int(r['frame']):r for r in rep}
M={int(r['frame']):float(r['mean_abs_diff_320']) for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))}
# ponytail: top-2 measured diff peaks per state (>=1.0, >=6f from bounds, >=15f apart); detector candidates, not events
peaks=[]
for s in S:
    a,b=int(s['start']),int(s['end']);cand=sorted(((M[f],f) for f in range(a+6,b-5) if M[f]>=1.0),reverse=True);got=[]
    for v,f in cand:
        if all(abs(f-g)>=15 for g in got):got.append(f)
        if len(got)==2:break
    for f in sorted(got):peaks.append({'state':s['state_v4'],'peak_frame':f,'mean_abs_diff_320':M[f],'strip_frames':';'.join(str(x) for x in range(f-3,f+5,1) if a<=x<=b)})
need=set(repf)|{int(x) for pk in peaks for x in pk['strip_frames'].split(';')}
src=json.loads(Path('source_manifest.json').read_text())['source_path'];cap=cv2.VideoCapture(src);mm=[];got={}
for f in range(max(need)+1):
    ok,im=cap.read();assert ok,f
    if f in repf and not (im==cv2.imread(repf[f]['native_png'])).all():mm.append(f)
    if f in need:got[f]=cv2.resize(im,(480,270),interpolation=cv2.INTER_AREA)
cap.release()
od=Path(f'frames/motion_strips/{batch}');od.mkdir(parents=True,exist_ok=True)
for pk in peaks:
    fs=[int(x) for x in pk['strip_frames'].split(';')];tiles=[]
    for f in fs:
        t=got[f].copy();cv2.rectangle(t,(0,0),(200,26),(0,0,0),-1);cv2.putText(t,f'f{f} {f/FPS:.3f}s',(4,19),cv2.FONT_HERSHEY_SIMPLEX,0.55,(255,255,255),1);tiles.append(t)
    while len(tiles)%4:tiles.append(np.zeros_like(tiles[0]))
    img=np.vstack([np.hstack(tiles[i:i+4]) for i in range(0,len(tiles),4)])
    pk['strip_png']=f'{od}/{pk["state"]}_peak{pk["peak_frame"]}.png';cv2.imwrite(pk['strip_png'],img)
with open(f'tables/o_motion_peaks_{batch}.csv','w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=list(peaks[0]));w.writeheader();w.writerows(peaks)
Path(f'tables/o_decode_verification_{batch}.json').write_text(json.dumps({'method':'sequential OpenCV decode from frame0 vs random-access PNGs','frames_checked':len(repf),'mismatches':mm},indent=1))
t0=int(S[0]['start'])/FPS;t1=(int(S[-1]['end'])+1)/FPS
asr=[r|{'seg_index':i} for i,r in enumerate(csv.DictReader(open('asr/asr_small_en_segments.csv'))) if float(r['end'])>t0 and float(r['start'])<t1]
with open(f'tables/o_asr_excerpt_{batch}.csv','w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=['seg_index','start','end','text','avg_logprob','no_speech_prob']);w.writeheader();w.writerows(asr)
print('rep',len(repf),'mismatch',mm,'peaks',len(peaks),'asr segs',[a['seg_index'] for a in asr],round(t0,3),round(t1,3))
