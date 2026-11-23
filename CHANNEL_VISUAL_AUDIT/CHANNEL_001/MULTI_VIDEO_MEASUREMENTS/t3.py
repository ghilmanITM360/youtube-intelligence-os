import an, csv, subprocess, sys, os, numpy as np
from PIL import Image
vid,key=sys.argv[1],sys.argv[2]
p=an.find(key); rows=list(csv.DictReader(open(f'states_{vid}.csv'))); os.makedirs(f't3_{vid}',exist_ok=True)
out=[]
for r in rows:
    t=(float(r['t0'])+float(r['t1']))/2; f=f't3_{vid}/{r["state"]}.png'
    subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-y','-ss',str(t),'-i',p,'-frames:v','1',f])
    a=np.array(Image.open(f).convert('RGB')).astype(int); H,W,_=a.shape
    ink=np.abs(a-253).sum(-1)>60; ys,xs=np.where(ink)
    q=a[ink]//32*32+16
    if len(q):
        k,c=np.unique(q[:,0]*65536+q[:,1]*256+q[:,2],return_counts=True); o=np.argsort(-c)[:3]
        pal=' '.join('#%02x%02x%02x:%.2f'%(k[i]>>16,(k[i]>>8)&255,k[i]&255,c[i]/len(q)) for i in o)
    else: pal=''
    sat=((a.max(-1)-a.min(-1))>60).mean()
    txt=subprocess.run(['tesseract',f,'-','--psm','11'],capture_output=True,text=True).stdout.split()
    txt=' '.join(w for w in txt if len(w)>1 and any(ch.isalnum() for ch in w))
    out.append(dict(state=r['state'],t0=r['t0'],t1=r['t1'],dur=r['dur'],ink_frac=round(float(ink.mean()),3),sat_frac=round(float(sat),3),
      bbox_y=f'{ys.min()}-{ys.max()}' if len(ys) else '',bbox_x=f'{xs.min()}-{xs.max()}' if len(xs) else '',palette_top3=pal,ocr_text=txt[:120]))
    print(out[-1]['state'],out[-1]['dur'],out[-1]['bbox_y'],out[-1]['palette_top3'][:40],'|',out[-1]['ocr_text'][:60],flush=True)
with open(f't3_{vid}.csv','w') as o:
    w=csv.DictWriter(o,out[0].keys()); w.writeheader(); w.writerows(out)
