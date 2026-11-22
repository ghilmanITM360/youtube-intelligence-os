import subprocess, numpy as np, sys, glob, os, json
from concurrent.futures import ThreadPoolExecutor
D="/Users/ghilmankhan/workprojects/videos in mp3/CasuallyFinance"
W,H=192,108
def probe(f):
    o=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height:format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.split()
    w,h=o[0].split(",")[:2]; return int(w),int(h),float(o[1])
def frames(f,w,h,maxdur,step):
    # scale to fit 192 wide (landscape) or 108 wide (portrait) 
    if w>=h: sw,sh=192,108
    else: sw,sh=108,192
    cmd=["ffmpeg","-v","error","-t",str(maxdur),"-i",f,"-vf",f"fps=1/{step},scale={sw}:{sh}","-f","rawvideo","-pix_fmt","rgb24","-"]
    b=subprocess.run(cmd,capture_output=True).stdout
    n=len(b)//(sw*sh*3)
    return np.frombuffer(b[:n*sw*sh*3],np.uint8).reshape(n,sh,sw,3).astype(int)
def classify(fr):
    # light canvas: >=55% of pixels near-white/cream (all channels >=235) 
    mx=fr.min(axis=2)
    light=(mx>=235).mean()
    # flat-colour canvas: dominant quantised colour >=55%
    q=(fr//16).reshape(-1,3); k=q[:,0]*256+q[:,1]*16+q[:,2]
    dom=np.bincount(k).max()/len(k)
    return light,dom
def run(f):
    w,h,d=probe(f); 
    fr=frames(f,w,h,300,4)
    res=[]
    for x in fr:
        l,dm=classify(x)
        if l>=0.55: c="light"
        elif dm>=0.55: c="flat"
        else: c="full"
        res.append(c)
    return os.path.basename(f),(w,h),round(d),res
files=sorted(glob.glob(D+"/*.mp4"))
sel=[]
for f in files:
    try:
        w,h,d=probe(f)
    except Exception: continue
    sel.append((f,w,h,d))
LF=[f for f,w,h,d in sel if w>h and w>=1280]
SH=[f for f,w,h,d in sel if h>w and w>=720]
import random; random.seed(1); SHs=random.sample(SH,min(30,len(SH)))
out={}
with ThreadPoolExecutor(6) as ex:
    for name,res_,d,res in ex.map(run,LF+SHs):
        out[name]=dict(res=res_,dur=d,cls=res)
json.dump(out,open("bgstat.json","w"))
def summ(names,label):
    t=sum(len(out[n]["cls"]) for n in names)
    c={k:sum(out[n]["cls"].count(k) for n in names) for k in("light","flat","full")}
    print(label,len(names),"videos",t,"frames",{k:round(v/t,3) for k,v in c.items()})
    return c
summ([os.path.basename(f) for f in LF],"LONGFORM")
summ([os.path.basename(f) for f in SHs],"SHORTS")
for f in LF:
    n=os.path.basename(f); cl=out[n]["cls"]; print(round(cl.count("light")/len(cl),2),round(cl.count("flat")/len(cl),2),round(cl.count("full")/len(cl),2),len(cl),n[:60])
