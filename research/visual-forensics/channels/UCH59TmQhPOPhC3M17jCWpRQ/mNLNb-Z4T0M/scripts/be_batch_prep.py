# Generic per-batch evidence prep for a video workspace (cwd): native representative PNGs (+kmeans palette), measured-peak motion strips,
# ASR excerpt. One sequential decode (no random seeks) so extracted pixels are decode-order exact.
import cv2,csv,json,sys,numpy as np
from pathlib import Path
cv2.setNumThreads(2);FPS=30000/1001
batch,i0,i1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
S=list(csv.DictReader(open('tables/states_v1.csv')))[i0:i1]
M={int(r['frame']):float(r['mean_abs_diff_320']) for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))}
rep={};peaks=[]
for s in S:
    a,b=int(s['start']),int(s['end']);n=b-a+1
    # ponytail: 1 rep for <0.5s, 2 for <4s, 3 otherwise; 1 strip (top measured peak) per state >=1s, 2 if >=6s
    fr=[min(b,a+2)] if n<15 else ([min(b,a+4),b-2] if n<120 else [min(b,a+4),(a+b)//2,b-3])
    for f in fr:rep[f]=s['state']
    k=2 if n>=180 else (1 if n>=30 else 0);cand=sorted(((M[f],f) for f in range(a+6,b-5) if M[f]>=1.0),reverse=True);got=[]
    for v,f in cand:
        if len(got)==k:break
        if all(abs(f-g)>=15 for g in got):got.append(f)
    for f in sorted(got):peaks.append({'state':s['state'],'peak_frame':f,'mean_abs_diff_320':M[f],'strip_frames':';'.join(str(x) for x in range(f-3,f+5) if a<=x<=b)})
need=set(rep)|{int(x) for p in peaks for x in p['strip_frames'].split(';')}
cap=cv2.VideoCapture(json.load(open('source_manifest.json'))['source_path']);full={};small={}
for i in range(max(need)+1):
    ok,im=cap.read();assert ok,i
    if i in rep:full[i]=im
    if i in need:small[i]=cv2.resize(im,(480,270),interpolation=cv2.INTER_AREA)
nd=Path(f'frames/native_rep/{batch}');nd.mkdir(parents=True,exist_ok=True);rows=[]
for f,st in sorted(rep.items()):
    p=f'{nd}/{st}_f{f}.png';cv2.imwrite(p,full[f]);px=full[f][::4,::4].reshape(-1,3).astype(np.float32)
    _,lab,c=cv2.kmeans(px,5,None,(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0),1,cv2.KMEANS_PP_CENTERS);cnt=np.bincount(lab.ravel(),minlength=5);o=np.argsort(-cnt)
    rows.append({'state':st,'frame':f,'pts_s':round(f/FPS,6),'native_png':p,'kmeans5_palette_hex_share':';'.join('#%02x%02x%02x:%.1f%%'%(int(c[k][2]),int(c[k][1]),int(c[k][0]),100*cnt[k]/cnt.sum()) for k in o)})
w=csv.DictWriter(open(f'tables/rep_frames_{batch}.csv','w',newline=''),list(rows[0]));w.writeheader();w.writerows(rows)
od=Path(f'frames/motion_strips/{batch}');od.mkdir(parents=True,exist_ok=True)
for pk in peaks:
    fs=[int(x) for x in pk['strip_frames'].split(';')];t=[]
    for f in fs:
        im=small[f].copy();cv2.rectangle(im,(0,0),(200,26),(0,0,0),-1);cv2.putText(im,f'f{f} {f/FPS:.3f}s',(4,19),cv2.FONT_HERSHEY_SIMPLEX,.55,(255,255,255),1);t.append(im)
    while len(t)%4:t.append(np.zeros_like(t[0]))
    pk['strip_png']=f'{od}/{pk["state"]}_peak{pk["peak_frame"]}.png';cv2.imwrite(pk['strip_png'],np.vstack([np.hstack(t[i:i+4]) for i in range(0,len(t),4)]))
w=csv.DictWriter(open(f'tables/motion_peaks_{batch}.csv','w',newline=''),['state','peak_frame','mean_abs_diff_320','strip_frames','strip_png']);w.writeheader();w.writerows(peaks)
t0=int(S[0]['start'])/FPS;t1=(int(S[-1]['end'])+1)/FPS
asr=[r|{'seg_index':i} for i,r in enumerate(csv.DictReader(open('asr/asr_small_en_segments.csv'))) if float(r['end'])>t0 and float(r['start'])<t1]
w=csv.DictWriter(open(f'tables/asr_excerpt_{batch}.csv','w',newline=''),['seg_index','start','end','text','avg_logprob','no_speech_prob']);w.writeheader();w.writerows(asr)
print(batch,S[0]['state'],S[-1]['state'],'reps',len(rows),'strips',len(peaks),'asr',len(asr),round(t0,2),round(t1,2))
