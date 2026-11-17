import numpy as np, cv2, json, subprocess, math
from PIL import Image, ImageDraw, ImageFont
W,H,N=1920,1080,208
rng=np.random.default_rng(7)
INK=(16,16,16)
def rgb(h): return tuple(int(h[i:i+2],16) for i in (1,3,5))
GRASS,WATER,SKY,SAND=rgb('#789838'),rgb('#68c8d8'),rgb('#d0f8f8'),rgb('#e0cfa0')
HZ=165
def wob(pts,a=2.0,sub=6):
    out=[]
    for (x0,y0),(x1,y1) in zip(pts[:-1],pts[1:]):
        for k in range(sub):
            t=k/sub; out.append((x0+(x1-x0)*t+rng.normal(0,a),y0+(y1-y0)*t+rng.normal(0,a)))
    out.append(pts[-1]); return np.array(out,np.int32)
def line(im,pts,col=INK,w=5,a=1.5,closed=False):
    p=wob(pts+([pts[0]] if closed else []),a)
    cv2.polylines(im,[p],False,col,w+int(rng.integers(-1,2)),cv2.LINE_AA)
def river_c(t): return 960+330*t**0.8*math.sin(2*math.pi*1.15*t+0.6)-60*t
def river_w(t): return 14+1000*t**1.05
def build_bg():
    im=np.zeros((H,W,3),np.uint8); im[:]=SAND; im[:HZ]=SKY
    # distant hills
    for cx,rx,ry in [(300,260,45),(700,200,30),(1250,230,38),(1650,280,50)]:
        pts=[(cx+rx*math.cos(a),HZ-ry*math.sin(a)) for a in np.linspace(math.pi,0,14)]
        cv2.fillPoly(im,[np.array(pts,np.int32)],(190,225,215)); line(im,[(int(x),int(y)) for x,y in pts],w=3)
    # village
    for i,x in enumerate(range(900,1060,26)):
        h=14+int(rng.integers(0,8)); y=HZ-2
        pts=[(x,y),(x,y-h),(x+11,y-h-12),(x+22,y-h),(x+22,y)]
        cv2.fillPoly(im,[np.array(pts,np.int32)],(190,110,90)); line(im,pts,w=3,a=0.6,closed=True)
    cv2.line(im,(0,HZ),(W,HZ),INK,4)
    # hills
    hills=[(220,420,580,240),(1700,410,540,230)]
    mask=np.zeros((H,W),np.uint8)
    for cx,cy,rx,ry in hills:
        a=np.linspace(math.pi,2*math.pi,40)
        pts=[(cx+rx*math.cos(t),cy+ry*math.sin(t)+rng.normal(0,3)) for t in a]+[(cx+rx*math.cos(t),cy+(ry+170)*math.sin(t)*-1) for t in np.linspace(2*math.pi,math.pi,30)]
        poly=np.array(pts,np.int32); cv2.fillPoly(im,[poly],GRASS); cv2.fillPoly(mask,[poly],255)
        line(im,[(int(x),int(y)) for x,y in pts[:40]],w=6,a=1.5)
    # river
    ys=np.arange(HZ,H+1,6); L=[];R=[]
    for y in ys:
        t=(y-HZ)/(H-HZ); c=river_c(t); w=river_w(t)
        L.append((c-w+rng.normal(0,3),y)); R.append((c+w+rng.normal(0,3),y))
    poly=np.array(L+R[::-1],np.int32)
    wmask=np.zeros((H,W),np.uint8); cv2.fillPoly(wmask,[poly],255)
    im[wmask>0]=WATER
    line(im,[(int(x),int(y)) for x,y in L],w=6,a=1.2); line(im,[(int(x),int(y)) for x,y in R],w=6,a=1.2)
    # trees on hills
    for tx,ty,s in [(210,330,1.0),(420,380,0.8),(1640,310,0.9)]:
        tr=[(tx-8*s,ty+90*s),(tx-6*s,ty+10*s),(tx+6*s,ty+10*s),(tx+9*s,ty+90*s)]
        cv2.fillPoly(im,[np.array(tr,np.int32)],(70,92,120)); line(im,[(int(x),int(y)) for x,y in tr],w=5,a=1,closed=True)
        cp=[(tx+70*s*math.cos(a)+rng.normal(0,4),ty-10*s+62*s*math.sin(a)+rng.normal(0,4)) for a in np.linspace(0,2*math.pi,16)]
        cv2.fillPoly(im,[np.array(cp,np.int32)],(60,120,50)); line(im,[(int(x),int(y)) for x,y in cp],w=5,a=1,closed=True)
    # texture
    gm=(mask>0)&(wmask==0); n=0
    while n<1500:
        x,y=int(rng.integers(0,W)),int(rng.integers(HZ,H))
        if gm[y,x]:
            cv2.line(im,(x,y),(x+int(rng.integers(-5,6)),y-int(rng.integers(8,16))),(70,110,40),2,cv2.LINE_AA); n+=1
    n=0
    while n<260:
        x,y=int(rng.integers(0,W)),int(rng.integers(HZ+10,H))
        if wmask[y,x] and wmask[y,min(x+60,W-1)]:
            t=(y-HZ)/(H-HZ); l=int(10+50*t)
            cv2.ellipse(im,(x,y),(l,max(3,int(l/5))),0,200,340,(70,150,175),2,cv2.LINE_AA); n+=1
    for _ in range(7):
        x,y=int(rng.integers(50,W-250)),int(rng.integers(15,110)); l=int(rng.integers(90,220))
        cv2.ellipse(im,(x,y),(l//2,10),0,190,350,(250,255,255),3,cv2.LINE_AA)
        cv2.ellipse(im,(x+l//3,y-8),(l//3,8),0,190,350,(250,255,255),3,cv2.LINE_AA)
    return im
BG=build_bg()  # drawn once, reused identically
FONT="/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf"
def label_group(word,cap,item):
    """returns RGBA float canvas (rigid group) at scale 1; text size from cap height"""
    f=ImageFont.truetype(FONT,100); b=f.getbbox("H"); fs=int(100*cap/(b[3]-b[1])); f=ImageFont.truetype(FONT,fs)
    tw=int(f.getlength(word))+20; Wc=tw+int(cap*3.2); Hc=int(cap*3.6)
    im=Image.new("RGBA",(Wc,Hc),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.text((10,2),word,font=f,fill=(255,255,255,255),stroke_width=3,stroke_fill=(20,20,20,255))
    # dotted arrow from label down-right to item
    sx,sy=10+tw*0.5,int(cap*1.7); ex,ey=tw+cap*1.2,Hc-cap*0.8
    for k in range(9):
        t=k/9; x=sx+(ex-sx)*t; y=sy+(ey-sy)*t
        d.ellipse((x-3,y-3,x+3,y+3),fill=(255,255,255,255),outline=(20,20,20,255))
    ang=math.atan2(ey-sy,ex-sx)
    for da in (2.6,-2.6):
        d.line((ex,ey,ex+cap*0.3*math.cos(ang+da),ey+cap*0.3*math.sin(ang+da)),fill=(255,255,255,255),width=4)
    ix,iy=ex+cap*0.35,ey+cap*0.2; r=cap*0.28
    if item=="dot": d.ellipse((ix-6,iy-6,ix+6,iy+6),fill=(30,30,30,255))
    elif item=="blob":
        pts=[(ix+r*1.2*math.cos(a)*(1+.15*math.sin(3*a)),iy+r*.8*math.sin(a)) for a in np.linspace(0,6.28,20)]
        d.polygon(pts,fill=(122,82,48,255),outline=(20,20,20,255))
    else:
        d.ellipse((ix-r*1.3,iy-r*.6,ix+r*1.0,iy+r*.6),fill=(140,140,140,255),outline=(20,20,20,255),width=3)
        d.polygon([(ix+r*.9,iy),(ix+r*1.7,iy-r*.6),(ix+r*1.7,iy+r*.6)],fill=(140,140,140,255),outline=(20,20,20,255))
        d.line((ix-r*.8,iy-r*.15,ix-r*.6,iy+r*.15),fill=(20,20,20,255),width=3)
    return np.array(im).astype(np.float32)
def ease(p): p=min(max(p,0),1); return p*p*(3-2*p)
# id, word, cap, item, onset, drift start, start pos, end pos, end scale
G=[("g1","bugs",40,"dot",55,70,(770,500),(880,300),0.5),
   ("g2","mud",52,"blob",85,85,(580,690),(760,410),0.5),
   ("g3","rotten fish",66,"fish",115,115,(420,880),(660,560),0.5)]
CANV=[label_group(w,c,i) for _,w,c,i,*_ in G]
def person():
    S=4; im=Image.new("RGBA",(420*S//2,520*S//2),(0,0,0,0)); d=ImageDraw.Draw(im)
    k=S/2; ink=(20,20,20,255)
    def P(l): return [(x*k,y*k) for x,y in l]
    d.polygon(P([(30,520),(50,330),(130,290),(290,290),(370,330),(390,520)]),fill=(70,100,170,255),outline=ink); 
    d.line(P([(30,520),(50,330),(130,290),(290,290),(370,330),(390,520)]),fill=ink,width=int(6*k),joint="curve")
    d.rectangle((185*k,240*k,235*k,300*k),fill=(235,195,160,255),outline=ink,width=int(5*k))
    d.ellipse((115*k,60*k,305*k,270*k),fill=(235,195,160,255),outline=ink,width=int(6*k))
    d.pieslice((105*k,40*k,315*k,230*k),180,360,fill=(90,55,30,255),outline=ink,width=int(6*k))
    for ex in (170,250):
        d.arc((ex*k-22*k,160*k-8*k,ex*k+22*k,160*k+16*k),10,170,fill=ink,width=int(5*k))
    d.arc((180*k,215*k,240*k,245*k),200,340,fill=ink,width=int(5*k))
    wv=[(x*k,(478+6*math.sin(x/18))*k) for x in range(0,421,6)]
    d.polygon(wv+[(420*k,520*k),(0,520*k)],fill=(104,200,216,255)); d.line(wv,fill=ink,width=int(5*k))
    return np.array(im).astype(np.float32)
PER=person()
def paste(fr,rgba,cx,cy,s,reveal=1.0):
    h,w=rgba.shape[:2]; nw,nh=max(1,int(w*s)),max(1,int(h*s))
    r=cv2.resize(rgba,(nw,nh),interpolation=cv2.INTER_AREA)
    if reveal<1: r[:,int(nw*reveal):,3]=0
    x0,y0=int(cx-nw/2),int(cy-nh/2)
    xa,ya,xb,yb=max(0,x0),max(0,y0),min(W,x0+nw),min(H,y0+nh)
    if xa>=xb or ya>=yb: return
    sub=r[ya-y0:yb-y0,xa-x0:xb-x0]; a=sub[...,3:4]/255.0
    fr[ya:yb,xa:xb]=(fr[ya:yb,xa:xb]*(1-a)+sub[...,2::-1]*a).astype(np.uint8)
tl={"static_camera":True,"first_motion_frame":55,"groups":{},"person":{"enter":140,"end":207}}
for g in G: tl["groups"][g[1]]={"onset":g[4],"writeon_frames":5,"drift_start":g[5],"drift_end":195}
ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","bgr24","-s","1920x1080","-r","30000/1001","-i","-","-vf","format=yuv420p","-c:v","libx264","-crf","14","-r","30000/1001","-frames:v",str(N),"rt.mp4"],stdin=subprocess.PIPE)
for f in range(N):
    fr=BG.copy()[...,::-1].copy()  # to BGR
    fr=BG[...,::-1].copy()
    # NOTE: paste() expects BGR frame and RGBA (RGB order) source -> sub[...,2::-1] converts
    for (gid,w,c,i,on,ds,sp,ep,es),cv in zip(G,CANV):
        if f<on: continue
        p=ease((f-ds)/(195-ds)) if f>=ds else 0
        s=1-(1-es)*p; cx=sp[0]+(ep[0]-sp[0])*p; cy=sp[1]+(ep[1]-sp[1])*p
        paste(fr,cv,cx,cy,s,reveal=min(1,(f-on+1)/5))
    if f>=140:
        p=(f-140)/67; q=1-(1-p)**1.6
        cy=1130+(500-1130)*q+8*math.sin(f/5); t=(cy-HZ)/(H-HZ); s=0.78-0.5*q
        paste(fr,PER,river_c(max(t,0))+20,cy,s)
    ff.stdin.write(fr.tobytes())
ff.stdin.close(); ff.wait()
json.dump(tl,open("timeline.json","w"),indent=1)
