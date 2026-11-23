import subprocess, numpy as np, sys, os, glob
def meas(p,tag):
    W,H=1080,1920; TW,TH=135,240; R=6
    pr=subprocess.Popen(['/opt/homebrew/bin/ffmpeg','-v','error','-i',p,'-vf',f'fps={R},scale={TW}:{TH}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    n=TW*TH*3; fs=[]
    while True:
        b=pr.stdout.read(n)
        if len(b)<n: break
        fs.append(np.frombuffer(b,np.uint8).reshape(TH,TW,3).astype(np.int16))
    F=np.array(fs); N=len(F); dur=N/R
    d=np.abs(F[1:]-F[:-1]).mean(axis=(1,2,3)); cuts=int((d>18).sum())
    ink=[(np.abs(f-253).sum(-1)>60) for f in fs]; st=1; anc=0
    for i in range(1,N):
        a,b=ink[anc],ink[i]; u=(a|b).sum()
        if (( a&b).sum()/u if u else 1)<0.80: st+=1; anc=i
    prof=np.mean([m.mean(1) for m in ink],axis=0); act=np.where(prof>0.01)[0]
    # ocr
    d_=f'ocr_{tag}'; os.makedirs(d_,exist_ok=True)
    subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-y','-i',p,'-vf','fps=1/3','-q:v','2',f'{d_}/f_%03d.png'])
    ys=[]
    for f in sorted(glob.glob(d_+'/f_*.png')):
        for l in subprocess.run(['tesseract',f,'-','--psm','11','tsv'],capture_output=True,text=True).stdout.splitlines()[1:]:
            c=l.split('\t')
            if len(c)==12 and c[11].strip().isalpha() and len(c[11].strip())>1 and float(c[10])>60: ys.append(int(c[7])+int(c[9])//2)
    h,_=np.histogram(ys,bins=10,range=(0,1920)) if ys else ([0]*10,0)
    print(tag,'dur',round(dur,1),'cuts/10s',round(cuts/dur*10,1),'states',st,'mean_state_s',round(dur/st,2),'content_rows',(int(act.min()*H/TH),int(act.max()*H/TH)),'ocr_bins',list(map(int,h)),flush=True)
for p in sys.argv[1:]: meas(p,os.path.basename(p)[:3])
