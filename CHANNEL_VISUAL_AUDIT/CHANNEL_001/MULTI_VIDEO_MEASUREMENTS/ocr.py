import an, subprocess, glob, os, csv, io
ids=[('10nEByVLya0','10nEByVLya0'),('1eTwFcXq1iw','1eTwFcXq1iw'),('33NVvWsGt9k','33NVvWsGt9k'),('xdF8HOwCgTU','xdF8HOwCgTU'),('zLvSl1irqtU','zLvSl1irqtU')]
for vid,key in ids:
    p=an.find(key); d=f'ocr/{vid}'; os.makedirs(d,exist_ok=True)
    subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-y','-i',p,'-vf','fps=1/3','-q:v','2',f'{d}/f_%03d.png'])
    ys=[]; words=0; frames=0; wc=0
    for f in sorted(glob.glob(d+'/f_*.png')):
        o=subprocess.run(['tesseract',f,'-','--psm','11','tsv'],capture_output=True,text=True).stdout.splitlines()[1:]
        got=False
        for l in o:
            c=l.split('\t')
            if len(c)==12 and c[11].strip() and float(c[10])>60 and len(c[11].strip())>1 and c[11].strip().isalpha():
                ys.append(int(c[7])+int(c[9])//2); got=True; wc+=1
        frames+=1; words+=got
    import numpy as np
    h,_=np.histogram(ys,bins=10,range=(0,1920)) if ys else ([0]*10,0)
    print(vid,'frames',frames,'frames_with_text',words,'words',wc,'ybins(192px)',list(map(int,h)),flush=True)
