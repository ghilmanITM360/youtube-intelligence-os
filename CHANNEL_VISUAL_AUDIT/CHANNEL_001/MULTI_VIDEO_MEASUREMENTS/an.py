import sys, subprocess, json, glob, os, numpy as np
D=os.path.expanduser('~/workprojects/videos in mp3/CasuallyFinance/')
def find(vid):
    for p in glob.glob(D+'*.mp4'):
        if vid in p: return p
def probe(p):
    o=subprocess.check_output(['/opt/homebrew/bin/ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_frames,duration','-of','json',p]);return json.loads(o)['streams'][0]
def run(vid,key):
    p=find(key); s=probe(p); w,h=int(s['width']),int(s['height']); fr=s['r_frame_rate']; fps=eval(fr)
    TW=216; TH=int(round(TW*h/w)); R=6
    pr=subprocess.Popen(['/opt/homebrew/bin/ffmpeg','-v','error','-i',p,'-vf',f'fps={R},scale={TW}:{TH}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    n=TW*TH*3; fs=[]
    while True:
        b=pr.stdout.read(n)
        if len(b)<n: break
        fs.append(np.frombuffer(b,np.uint8).reshape(TH,TW,3))
    F=np.array(fs).astype(np.int16); N=len(F)
    d=np.abs(F[1:]-F[:-1]).mean(axis=(1,2,3))
    cuts=int((d>18).sum()); 
    bgs=[tuple(F[i][2:6,2:6].reshape(-1,3).mean(0).round().astype(int)) for i in range(0,N,max(1,N//20))]
    bgm=max(set(bgs),key=bgs.count)
    bg=np.array(bgm)
    ink=(np.abs(F-bg).sum(-1)>60)  # N,TH,TW
    rows=ink.mean(axis=(0,2))   # row ink profile
    act=np.where(rows>0.01)[0]
    # content band: rows with ink, excluding bottom caption zone 
    dark=(F.sum(-1)<150)
    drow=dark.mean(axis=(0,2))
    # caption rows: dark in lower half
    lo=int(TH*0.62); cap=np.where(drow[lo:]>0.01)[0]+lo
    # palette
    q=(F[::6].reshape(-1,3)//32)
    keys,cnt=np.unique(q[:,0]*64+q[:,1]*8+q[:,2],return_counts=True)
    top=np.argsort(-cnt)[:8]
    pal=[('#%02x%02x%02x'%(((k//64)*32+16),(((k//8)%8)*32+16),((k%8)*32+16)),round(cnt[i]/cnt.sum(),3)) for i,k in zip(top,keys[top])]
    stat=(d<1.0).mean()
    # full-frame photo/clip proxy: frames where ink fraction >0.85
    full=(ink.mean(axis=(1,2))>0.85).mean()
    dur=N/R
    r=dict(id=vid,key=key,w=w,h=h,fps=round(fps,2),dur=round(dur,1),bg=list(map(int,bgm)),
      cuts=cuts,cuts_per_10s=round(cuts/dur*10,1),static_frac=round(float(stat),2),fullframe_frac=round(float(full),2),
      content_rows_px=[int(act.min()*h/TH),int(act.max()*h/TH)] if len(act) else None,
      caption_rows_px=[int(cap.min()*h/TH),int(cap.max()*h/TH)] if len(cap) else None,palette=pal,
      dmax=round(float(d.max()),1),dmean=round(float(d.mean()),2))
    print(json.dumps(r)); return r
if __name__=='__main__':
    ids=[('02f598d4','Nobody-Is-Talking'),('33NVvWsGt9k','33NVvWsGt9k'),('1eTwFcXq1iw','1eTwFcXq1iw'),('3132dfa8',"Your Dollar's Emergency"),('xdF8HOwCgTU','xdF8HOwCgTU'),('zLvSl1irqtU','zLvSl1irqtU'),('10nEByVLya0','10nEByVLya0')]
    out=[]
    for a,b in ids:
        try: out.append(run(a,b))
        except Exception as e: print(a,'ERR',e)
    json.dump(out,open('multi.json','w'),indent=1)
