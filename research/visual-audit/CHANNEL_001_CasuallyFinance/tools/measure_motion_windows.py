import csv,os,subprocess,numpy as np,json,sys
from PIL import Image
H=os.path.expanduser('~/YIOS-local-audits/');V=os.path.expanduser('~/workprojects/videos in mp3/CasuallyFinance/')
import glob,re
ids=['CFrVTZBYa3Q','10nEByVLya0','turJ6VMfUjI','SYSUh-oow6M','eePIUX0Sd6c','yViMyIVOHkQ','Xkk9GnnJHBg','DKyJABtbF2o','RXFBHYxyqdk','hbsYaLaN_F8','dPoDyl9Ys38','7K991LgY3tc','WCS1bK3KB3U','KTnp2OlQJHA','Im-N3K9Pnf0']
vids={}
for i in ids:
    g=[V+f for f in os.listdir(V) if f.endswith('['+i+'].mp4')]
    if not g: continue
    pr=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate,width,height','-of','csv=p=0',g[0]],capture_output=True,text=True).stdout.strip().split(',')
    n,d=pr[2].split('/');vids[i]=(os.path.basename(g[0]),round(int(n)/int(d)),int(pr[1])>int(pr[0]))
W,Hh=480,270
def frames(path,fps,a,n,vertical):
    w,h=(270,480) if vertical else (W,Hh)
    c=['ffmpeg','-v','error','-ss',f'{a/fps:.5f}','-i',path,'-frames:v',str(n),'-vf',f'scale={w}:{h},format=gray','-f','rawvideo','-']
    b=subprocess.run(c,capture_output=True).stdout
    return np.frombuffer(b,np.uint8).reshape(-1,h,w).astype(np.int16)
def scale_est(a,b):
    h,w=a.shape;best=(1.0,1e9)
    for s in np.arange(1.0,1.8,0.01):
        nh,nw=int(h/s),int(w/s);y,x=(h-nh)//2,(w-nw)//2
        c=np.array(Image.fromarray(a[y:y+nh,x:x+nw].astype(np.uint8)).resize((w,h)),np.int16)
        e=np.abs(c-b).mean()
        if e<best[1]:best=(s,e)
    return round(best[0],2)
KEYS=['POP_IN','POSE','TEXT_SWAP','TEXT_TYPE','SLIDE_IN','RISE_IN','ZOOM_IN','PAN','DRAWON','HOP_IN','POP_OUT']
out=[]
for vid,(fn,fps,vert) in vids.items():
    ev=list(csv.DictReader(open(H+f'2026-11-08-{vid}-deep-ct-scan/visual_event_ledger.csv')))
    cnt={}
    for e in ev:
        t=e['transition_type']
        k=next((k for k in KEYS if k in t),None)
        if not k or cnt.get(k,0)>=8: continue
        s=int(e['start_frame'])
        if s<5: continue
        cnt[k]=cnt.get(k,0)+1
        a=s-3;n=34
        F=frames(V+fn,fps,a,n,vert)
        if len(F)<10: continue
        cf=[float((np.abs(F[i]-F[i-1])>16).mean()) for i in range(1,len(F))]
        thr=max(0.0005,0.1*max(cf))
        act=[i+1 for i,v in enumerate(cf) if v>thr]
        span=(act[-1]-act[0]+1) if act else 0
        sc=None
        if k=='ZOOM_IN':
            ref=F[4]
            sc=[scale_est(ref,F[i]) for i in range(4,min(len(F),34),2)]
        out.append(dict(video_id=vid,event_id=e['event_id'],klass=k,transition=t,start_frame=s,fps=fps,
          active_frames=len(act),first_active_rel=(act[0]-3 if act else None),span_frames=span,peak_changed_frac=round(max(cf),4),
          peak_frame_rel=cf.index(max(cf))+1-3,cf_series=[round(x,4) for x in cf],scale_series_every3=sc))
json.dump(out,open('mw2.json','w'))
print(len(out),list(vids))
