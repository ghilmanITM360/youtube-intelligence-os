import numpy as np, cv2, json, subprocess, math
from PIL import Image, ImageDraw, ImageFont
W,H,N=1920,1080,208
rng=np.random.default_rng(7)
INK=(24,24,24)  # BGR-agnostic gray
def bgr(h): return (int(h[5:7],16),int(h[3:5],16),int(h[1:3],16))
WATER,GRASS,SKY=bgr('#68c8d8'),bgr('#789838'),bgr('#d0f8f8')
HOR=150
def cxf(y):
    t=(y-HOR)/(H-HOR); return 1000+430*t**.6*(1-.7*t)*math.sin(2*math.pi*1.2*t+.4)
def wf(y):
    t=(y-HOR)/(H-HOR); return 40+1750*t**.6
def jl(img,pts,col,w0=4,w1=7):
    for a,b in zip(pts[:-1],pts[1:]):
        cv2.line(img,(int(a[0]),int(a[1])),(int(b[0]),int(b[1])),col,int(rng.integers(w0,w1+1)),cv2.LINE_AA)
def wob(pts,j=2.0): return [(x+rng.normal(0,j),y+rng.normal(0,j)) for x,y in pts]
# ---- background (drawn once)
bg=np.zeros((H,W,3),np.uint8); bg[:]=GRASS; bg[:HOR]=SKY
ys=np.arange(HOR,H+1,4)
L=[(cxf(y)-wf(y)/2,y) for y in ys]; R=[(cxf(y)+wf(y)/2,y) for y in ys]
poly=np.array(L+R[::-1],np.int32)
rmask=np.zeros((H,W),np.uint8); cv2.fillPoly(rmask,[poly],255)
hills=[(250,100,520),(1560,92,560)]
hm=np.zeros((H,W),np.uint8); hm[HOR:]=255
for hx,hy,hw in hills:
    pts=[(x,HOR-(HOR-hy)*(0.5+0.5*math.cos(math.pi*(x-hx)/hw))) for x in range(hx-hw,hx+hw+1,8)]
    cv2.fillPoly(hm,[np.array(pts+[(hx+hw,HOR),(hx-hw,HOR)],np.int32)],255)
    cv2.fillPoly(bg,[np.array(pts+[(hx+hw,HOR+2),(hx-hw,HOR+2)],np.int32)],GRASS)
    jl(bg,wob(pts,1.2),INK,4,6)
bg[rmask>0]=WATER
hmask=(hm>0)&(rmask==0)
hm_in=cv2.erode(hmask.astype(np.uint8),np.ones((15,15)))>0
# distant pale hills + clouds in sky
for x0,r in [(780,90),(1320,70),(600,60)]:
    pts=[(x,HOR-8-r*0.12*math.cos(math.pi*(x-x0)/r/2)) for x in range(x0-r,x0+r,10)]
    jl(bg,wob(pts,1),bgr('#8fb8a8'),2,3)
for cx0,cy0 in [(900,50),(1250,80),(500,30),(1650,35)]:
    for k in range(3):
        pts=[(cx0+i*14-60+k*20,cy0+k*10+6*math.sin(i*.8)) for i in range(9)]
        jl(bg,wob(pts,1),(255,255,255),2,3)
# grass strokes (sparse) and ripples
lay=bg.copy()
for _ in range(1700):
    x,y=rng.integers(0,W),rng.integers(HOR,H)
    if not hm_in[y,x]: continue
    s=0.5+(y-HOR)/(H-HOR)
    for k in range(int(rng.integers(1,4))):
        a=-math.pi/2+rng.normal(0,.5); l=(8+10*s)*rng.uniform(.6,1.2)
        cv2.line(lay,(int(x+k*5*s),y),(int(x+k*5*s+l*math.cos(a)),int(y+l*math.sin(a))),bgr('#4c7424'),2,cv2.LINE_AA)
bg[hm_in]=lay[hm_in]
rm_in=cv2.erode(rmask,np.ones((25,25)))>0
lay=bg.copy()
for _ in range(900):
    x,y=rng.integers(0,W),rng.integers(HOR+10,H)
    if not rm_in[y,x]: continue
    s=0.3+(y-HOR)/(H-HOR)*1.2; a=int(26*s)
    cv2.ellipse(lay,(int(x),int(y)),(a,int(a*.28)+1),0,200,340,bgr('#48a0c0'),2,cv2.LINE_AA)
bg[rm_in]=lay[rm_in]
# banks
jl(bg,wob([(x,y) for x,y in L if x>-20],1.5),INK,4,7); jl(bg,wob([(x,y) for x,y in R if x<W+20],1.5),INK,4,7)
# village
for i,x in enumerate(range(1070,1190,22)):
    h=10+(i%2)*4; y=HOR-1
    cv2.rectangle(bg,(x,y-h),(x+14,y),bgr('#e8e0c8'),-1); cv2.rectangle(bg,(x,y-h),(x+14,y),INK,2)
    cv2.fillPoly(bg,[np.array([(x-3,y-h),(x+7,y-h-9),(x+17,y-h)],np.int32)],bgr('#a04830'))
    cv2.polylines(bg,[np.array([(x-3,y-h),(x+7,y-h-9),(x+17,y-h)],np.int32)],True,INK,2,cv2.LINE_AA)
# trees
def tree(x,y,h):
    tw=h*.07; jl(bg,wob([(x-tw,y),(x-tw,y-h*.5)],1),INK,5,6); jl(bg,wob([(x+tw,y),(x+tw,y-h*.5)],1),INK,5,6)
    cv2.rectangle(bg,(int(x-tw+4),int(y-h*.5)),(int(x+tw-4),int(y)),bgr('#7a5230'),-1)
    for dx,dy,r in [(-.18,.55,.2),(.18,.58,.2),(0,.78,.24),(-.05,.6,.22)]:
        c=(int(x+dx*h),int(y-dy*h)); cv2.circle(bg,c,int(r*h),bgr('#3f6a24'),-1)
        pts=[(c[0]+r*h*math.cos(a),c[1]+r*h*math.sin(a)) for a in np.linspace(0,2*math.pi,16)]
        jl(bg,wob(pts+[pts[0]],1.5),INK,4,6)
tree(120,430,170); tree(250,640,260); tree(1720,520,220)
bg=bg.copy()
# ---- groups
FONT=ImageFont.truetype('/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf',20).path
def mkgroup(word,fs,item):
    f=ImageFont.truetype(FONT,fs); tw=int(f.getlength(word))+20; th=int(fs*1.2)
    alen=int(fs*1.3); GW=tw+60; GH=th+alen+int(fs*1.1)+30
    im=Image.new('RGBA',(GW,GH),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.text((10,6),word,font=f,fill=(255,255,255,255),stroke_width=3,stroke_fill=(24,24,24,255))
    ax=GW//2; ay=th+alen+int(fs*.5)  # item anchor
    sx=tw*.45; sy=th
    n=7
    for i in range(n):
        t=i/(n-1); x=sx+(ax-sx)*t+12*math.sin(t*3); y=sy+(ay-fs*.35-sy)*t
        r=max(3,fs//16)
        d.ellipse((x-r,y-r,x+r,y+r),fill=(255,255,255,255),outline=(24,24,24,255),width=2)
    ex,ey=ax,ay-fs*.35
    for ddx in (-fs*.22,fs*.22):
        d.line((ex,ey,ex+ddx,ey-fs*.2),fill=(24,24,24,255),width=7); d.line((ex,ey,ex+ddx,ey-fs*.2),fill=(255,255,255,255),width=3)
    item(d,ax,ay,fs)
    return np.array(im),ax,ay
def bugs(d,x,y,fs):
    for dx,dy in [(-8,-3),(0,4),(9,-2),(2,-9)]:
        d.ellipse((x+dx-3,y+dy-3,x+dx+3,y+dy+3),fill=(20,20,20,255))
def mud(d,x,y,fs):
    r=fs*.28; pts=[(x+r*(1+.25*math.sin(a*3))*math.cos(a)*1.3,y+r*(1+.25*math.sin(a*3))*math.sin(a)*.8) for a in np.linspace(0,2*math.pi,20)]
    d.polygon(pts,fill=(0x7a,0x52,0x30,255),outline=(24,24,24,255))
def fish(d,x,y,fs):
    r=fs*.5
    d.polygon([(x-r,y),(x-r*.1,y-r*.4),(x+r*.5,y),(x-r*.1,y+r*.4)],fill=(150,150,150,255),outline=(24,24,24,255))
    d.polygon([(x+r*.45,y),(x+r*.9,y-r*.35),(x+r*.9,y+r*.35)],fill=(150,150,150,255),outline=(24,24,24,255))
    d.ellipse((x-r*.7,y-r*.12,x-r*.55,y+r*.03),fill=(20,20,20,255))
    d.line((x-r*.45,y-r*.15,x-r*.35,y+r*.15),fill=(24,24,24,255),width=2)
GR=[dict(word='bugs',fs=58,item=bugs,on=55,y0=470,dx0=-110,y1=255,dx1=-20,s1=.42),
    dict(word='mud',fs=72,item=mud,on=85,y0=700,dx0=-210,y1=370,dx1=-230,s1=.45),
    dict(word='rotten fish',fs=88,item=fish,on=115,y0=930,dx0=-330,y1=520,dx1=-250,s1=.5)]
for g in GR:
    g['im'],g['ax'],g['ay']=mkgroup(g['word'],g['fs'],g['item'])
    ys_,xs_=np.nonzero(g['im'][...,3]>40); g['bb']=(xs_.min(),ys_.min(),xs_.max(),ys_.max())
    g['im']=g['im'][...,[2,1,0,3]].copy()
D0,D1=70,195
def gstate(g,f):
    p=min(1,max(0,(f-max(D0,g['on']))/(D1-max(D0,g['on']))))
    y=g['y0']+(g['y1']-g['y0'])*p; dx=g['dx0']+(g['dx1']-g['dx0'])*p
    return cxf(y)+dx*(1-.5*p),y,1+(g['s1']-1)*p
def blit(fr,im,ax,ay,px,py,s,reveal=1.0):
    h,w=im.shape[:2]
    pm=im.astype(np.float32); pm[...,:3]*=pm[...,3:]/255
    nw,nh=max(1,int(w*s)),max(1,int(h*s))
    sm=cv2.resize(pm,(nw,nh),interpolation=cv2.INTER_AREA)
    x0,y0=int(px-ax*s),int(py-ay*s)
    cut=int(nw*reveal)
    xa,ya=max(0,x0),max(0,y0); xb,yb=min(W,x0+cut),min(H,y0+nh)
    if xb<=xa or yb<=ya: return (x0,y0,x0+nw,y0+nh)
    sub=sm[ya-y0:yb-y0,xa-x0:xb-x0]; a=sub[...,3:]/255
    reg=fr[ya:yb,xa:xb].astype(np.float32)
    fr[ya:yb,xa:xb]=np.clip(sub[...,:3]*1+reg*(1-a),0,255).astype(np.uint8)
    return (x0,y0,x0+nw,y0+nh)
# figure (RGBA, local origin = waterline center)
FW,FH=360,480
def mkfig():
    S=Image.new('RGBA',(FW,FH),(0,0,0,0)); d=ImageDraw.Draw(S); k=(24,24,24,255)
    ox,oy=FW//2,FH-60
    d.polygon([(ox-130,oy),(ox-110,oy-80),(ox-50,oy-110),(ox+50,oy-110),(ox+110,oy-80),(ox+130,oy)],fill=(0xb0,0x58,0x4c,255),outline=k)
    d.rectangle((ox-22,oy-135,ox+22,oy-95),fill=(0xe6,0xc2,0x98,255),outline=k)
    d.ellipse((ox-70,oy-310,ox+70,oy-130),fill=(0xe6,0xc2,0x98,255),outline=k,width=5)
    d.pieslice((ox-76,oy-318,ox+76,oy-190),180,360,fill=(0x3a,0x2a,0x22,255),outline=k)
    for ex in (-30,30):
        d.arc((ox+ex-14,oy-230,ox+ex+14,oy-210),0,180,fill=k,width=5)
    d.arc((ox-20,oy-175,ox+20,oy-150),190,350,fill=k,width=5)
    d.line((ox-48,oy-250,ox-16,oy-246),fill=k,width=4); d.line((ox+16,oy-246,ox+48,oy-250),fill=k,width=4)
    d.ellipse((ox-150,oy-14,ox+150,oy+26),fill=(0xd8,0xf4,0xf8,255),outline=k,width=4)  # ripple ring over chest base
    return np.array(S),ox,oy
fig,fax,fay=mkfig(); fig=fig[...,[2,1,0,3]].copy()
F0=140
def fstate(f):
    p=(f-F0)/(N-1-F0)
    wl=1500+(450-1500)*p; s=1+(.28-1)*p
    return cxf(min(max(wl,HOR),H))+70*(1-p)+8*math.sin(f*.2),wl+4*math.sin(f*.3)*s,s
# ---- render
out='rt.mp4'
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30000/1001','-i','-',
  '-an','-c:v','libx264','-pix_fmt','yuv420p','-crf','14','-r','30000/1001','-frames:v',str(N),out],stdin=subprocess.PIPE)
bbo=[]
for f in range(N):
    fr=bg.copy(); boxes=[]
    for g in GR:
        if f<g['on']: continue
        px,py,s=gstate(g,f); rev=min(1,(f-g['on']+1)/5)
        blit(fr,g['im'],g['ax'],g['ay'],px,py,s,rev); b=g['bb']
        boxes.append((px+(b[0]-g['ax'])*s,py+(b[1]-g['ay'])*s,px+(b[2]-g['ax'])*s,py+(b[3]-g['ay'])*s))
    if f>=F0:
        px,py,s=fstate(f); blit(fr,fig,fax,fay,px,py,s)
    bbo.append(boxes)
    if f==104: cv2.imwrite('/private/tmp/claude-501/f104.png',fr); d=np.abs(fr.astype(int)-np.array(GRASS)).sum(2); print('f104 green frac',(d<=60).mean(),'water',(np.abs(fr.astype(int)-np.array(WATER)).sum(2)<=30).mean())
    if f in(0,60,120,150,207): cv2.imwrite(f'/private/tmp/claude-501/f{f}.png',fr)
    ff.stdin.write(fr.tobytes())
ff.stdin.close(); ff.wait()
for f,bs in enumerate(bbo):
    for i in range(len(bs)):
        for j in range(i+1,len(bs)):
            a,b=bs[i],bs[j]
            if a[0]<b[2] and b[0]<a[2] and a[1]<b[3] and b[1]<a[3]: print('OVERLAP',f,i,j); break
json.dump(dict(frames=N,fps='30000/1001',camera_motion=False,label_onsets={g['word']:g['on'] for g in GR},
  write_on_frames=5,drift_start=D0,drift_end=D1,drift_start_per_group={g['word']:max(D0,g['on']) for g in GR},
  figure_enter=F0,figure_end=N-1,static_until=40),open('timeline.json','w'),indent=1)
