import an, subprocess, numpy as np, json
ids=[('02f598d4','Nobody-Is-Talking'),('33NVvWsGt9k','33NVvWsGt9k'),('1eTwFcXq1iw','1eTwFcXq1iw'),('3132dfa8',"Your Dollar's Emergency"),('xdF8HOwCgTU','xdF8HOwCgTU'),('zLvSl1irqtU','zLvSl1irqtU'),('10nEByVLya0','10nEByVLya0')]
res={}
for vid,key in ids:
    p=an.find(key); s=an.probe(p); w,h=int(s['width']),int(s['height']); TW=108; TH=int(round(TW*h/w))
    pr=subprocess.Popen(['/opt/homebrew/bin/ffmpeg','-v','error','-i',p,'-vf',f'fps=4,scale={TW}:{TH}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    n=TW*TH*3; ink=np.zeros(TH); dk=np.zeros(TH); c=0
    while True:
        b=pr.stdout.read(n)
        if len(b)<n: break
        f=np.frombuffer(b,np.uint8).reshape(TH,TW,3).astype(int)
        ink+=(np.abs(f-253).sum(-1)>60).mean(1); dk+=(f.sum(-1)<150).mean(1); c+=1
    ink/=c; dk/=c
    bins=[(round(i/20,2),round(float(ink[int(i*TH/20):int((i+1)*TH/20)].mean()),3),round(float(dk[int(i*TH/20):int((i+1)*TH/20)].mean()),3)) for i in range(20)]
    print(vid,w,h,' '.join(f'{b[0]:.2f}:{b[1]:.2f}/{b[2]:.2f}' for b in bins),flush=True)
