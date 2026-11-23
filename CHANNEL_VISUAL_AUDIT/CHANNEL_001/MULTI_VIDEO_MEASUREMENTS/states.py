import an, subprocess, numpy as np, csv, sys
ids=[('33NVvWsGt9k','33NVvWsGt9k'),('xdF8HOwCgTU','xdF8HOwCgTU'),('zLvSl1irqtU','zLvSl1irqtU'),('3132dfa8',"Your Dollar's Emergency"),('1eTwFcXq1iw','1eTwFcXq1iw'),('02f598d4','Nobody-Is-Talking')]
R=6
for vid,key in ids:
    p=an.find(key); s=an.probe(p); w,h=int(s['width']),int(s['height']); TW=135; TH=int(round(TW*h/w))
    pr=subprocess.Popen(['/opt/homebrew/bin/ffmpeg','-v','error','-i',p,'-vf',f'fps={R},scale={TW}:{TH}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    n=TW*TH*3; fs=[]
    while True:
        b=pr.stdout.read(n)
        if len(b)<n: break
        fs.append(np.frombuffer(b,np.uint8).reshape(TH,TW,3).astype(np.int16))
    # state split: ink-mask change vs state anchor
    ink=[(np.abs(f-253).sum(-1)>60) for f in fs]
    st=[0]; anc=0
    for i in range(1,len(fs)):
        a,b=ink[anc],ink[i]; u=(a|b).sum(); iou=(a&b).sum()/u if u else 1
        if iou<0.80: st.append(i); anc=i
    st.append(len(fs)); rows=[]
    for k in range(len(st)-1):
        a,b=st[k],st[k+1]; m=ink[(a+b)//2]; ys,xs=np.where(m)
        f=fs[(a+b)//2]; sat=(f.max(-1)-f.min(-1))>50
        cols=f[sat]; top=''
        if len(cols):
            q=cols//40; kk,cn=np.unique(q[:,0]*100+q[:,1]*10+q[:,2],return_counts=True); j=cn.argmax(); c=kk[j]; top='#%02x%02x%02x'%(c//100*40+20,c//10%10*40+20,c%10*40+20)
        rows.append(dict(state=f'S{k+1:03d}',t0=round(a/R,2),t1=round(b/R,2),dur=round((b-a)/R,2),ink_frac=round(float(m.mean()),3),
          bbox_y=[int(ys.min()*h/TH),int(ys.max()*h/TH)] if len(ys) else '',bbox_x=[int(xs.min()*w/TW),int(xs.max()*w/TW)] if len(xs) else '',sat_frac=round(float(sat.mean()),3),accent=top))
    with open(f'states_{vid}.csv','w') as o:
        wr=csv.DictWriter(o,rows[0].keys()); wr.writeheader(); wr.writerows(rows)
    d=[r['dur'] for r in rows]
    print(vid,'states',len(rows),'mean dur',round(np.mean(d),2),'med',np.median(d),'accents',sorted(set(r['accent'] for r in rows if r['accent']))[:8],flush=True)
