from PIL import Image, ImageDraw
import numpy as np
R="/Users/ghilmankhan/workprojects/visual-audit-worktrees/casually-finance/productions/new-original-video-v1-rent-01/"
ref=R+"style_audit/ref/"
def mask(im,thr=200):
    a=np.array(im.convert("RGB")).astype(int); return a.min(axis=2)<thr
specs=[("brc_a","Ref A: stick man (Brace 0:07)",(390,90,590,500)),("brc_b","Ref A': neutral (Brace 0:46)",(390,90,590,500)),("inv_a","Ref B: two men (Investor 0:55)",(110,150,270,500)),("inv_b","Ref C: mug man (Investor 0:37)",(200,130,440,470))]
tiles=[];rows=[]
for n,lab,box in specs:
    im=Image.open(ref+n+".jpg").crop(box); m=mask(im)
    ys,xs=np.where(m); t=im.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1)); mm=m[ys.min():ys.max()+1,xs.min():xs.max()+1]
    H=mm.shape[0]
    # head = skin region: R>200,G in 150-215,B in 110-190 (peach)
    a=np.array(t.convert("RGB")).astype(int); skin=(a[...,0]>215)&(a[...,1]>160)&(a[...,1]<225)&(a[...,2]>120)&(a[...,2]<200)&(a[...,0]-a[...,2]>25)
    sy,sx=np.where(skin)
    hh=(sy.max()-sy.min()+1) if len(sy)>50 else float('nan'); hw=(sx.max()-sx.min()+1) if len(sx)>50 else float('nan')
    # body-line width: median horizontal run length of ink in the torso rows (below head, 55-75% of figure height)
    rows_=[]
    for y in range(int(H*0.55),int(H*0.7)):
        r=mm[y]; runs=[];c=0
        for v in r:
            if v:c+=1
            elif c: runs.append(c);c=0
        if c:runs.append(c)
        rows_+= [x for x in runs]
    lw=np.median(rows_) if rows_ else float('nan')
    rows.append((lab,H,hh,hw,lw)); tiles.append((lab,t))
sp=Image.open(R+"v1_assets/approved/v1_ch_p1_neutral_closed@12852084.png").convert("RGBA"); sp=sp.crop(sp.getbbox())
A=np.array(sp); al=A[...,3]>128; H=al.shape[0]
a=A[...,:3].astype(int); skin=al&(a[...,0]>150)&(a[...,0]-a[...,2]>40)&(a[...,1]>90)&(np.arange(H)[:,None]<H*0.2)
sy,sx=np.where(skin); hh=sy.max()-sy.min()+1; hw=sx.max()-sx.min()+1
# torso width at 40% height: alpha run
y=int(H*0.38); xs=np.where(al[y])[0]; tw=xs.max()-xs.min()
# leg width at 85%
y2=int(H*0.85); r=al[y2]; runs=[];c=0
for v in r:
    if v:c+=1
    elif c: runs.append(c);c=0
if c:runs.append(c)
rows.append(("V1 renter sprite",H,hh,hw,np.median(runs)))
print("V1 torso width@38%H",tw,"/H",round(tw/H,3),"leg runs@85%",runs,"leg/H",round(np.median(runs)/H,3))
bg=Image.new("RGBA",sp.size,(253,253,253,255)); bg.alpha_composite(sp); tiles.append(("V1 renter",bg.convert("RGB")))
for lab,H,hh,hw,lw in rows: print(f"{lab:36s} H={H} head_h={hh} head_h/H={hh/H:.2f} head_w/H={hw/H:.2f} torso-ish line px={lw} line/H={lw/H:.3f}")
Hh=520; W=sum(int(t.width*Hh/t.height) for _,t in tiles)+20*(len(tiles)+1)
out=Image.new("RGB",(W,Hh+50),(253,253,253)); x=20; dr=ImageDraw.Draw(out)
for lab,t in tiles:
    w=int(t.width*Hh/t.height); out.paste(t.resize((w,Hh)),(x,45)); dr.text((x,15),lab,fill=(0,0,0)); x+=w+20
out.save(R+"style_audit/chars_normalized.jpg",quality=92)
