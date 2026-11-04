import numpy as np, cv2, json, subprocess, math
from PIL import Image, ImageDraw, ImageFont
OX, OY, CW, CH = 300, 1400, 4550, 2600
INK=(8,8,8); BROWN=(0x28,0x48,0x78); BROWN2=(0x28,0x58,0x88); DARK=(0x18,0x30,0x58)
GREY=(0x78,0x88,0x88); LEAF=(0x45,0x7a,0x6b); BG=248
N=158
def P(x,y): return (int(round(x+OX)),int(round(y+OY)))
def stroke(img,pts,w,col=INK,rng=None,j=2.5):
    out=[]
    for a,b in zip(pts[:-1],pts[1:]):
        n=max(1,int(math.hypot(b[0]-a[0],b[1]-a[1])//35))
        for k in range(n): 
            t=k/n; out.append((a[0]+(b[0]-a[0])*t+rng.normal(0,j),a[1]+(b[1]-a[1])*t+rng.normal(0,j)))
    out.append(pts[-1])
    for a,b in zip(out[:-1],out[1:]):
        cv2.line(img,P(*a),P(*b),col,max(1,int(w*rng.uniform(.8,1.25))),cv2.LINE_AA)
    for a in out[::2]: cv2.circle(img,P(*a),max(1,int(w*.45)),col,-1,cv2.LINE_AA)
def shape(img,pts,fill,w,rng):
    if fill is not None: cv2.fillPoly(img,[np.array([P(*p) for p in pts],np.int32)],fill,cv2.LINE_AA)
    stroke(img,list(pts)+[pts[0]],w,INK,rng,j=w*.35)
def blob(cx,cy,rx,ry,rng,n=72,wob=.04,spiky=0):
    ph=rng.uniform(0,6,3); pts=[]
    for i in range(n):
        a=2*math.pi*i/n
        r=1+wob*(math.sin(2*a+ph[0])+.6*math.sin(3*a+ph[1])+.4*math.sin(5*a+ph[2]))
        if spiky: r+=spiky*(((i%4)/3)-.5)
        pts.append((cx+rx*r*math.cos(a),cy+ry*r*math.sin(a)))
    return pts
def limb(p0,p1,w0,w1,bend,n=14):
    (x0,y0),(x1,y1)=p0,p1; mx,my=(x0+x1)/2,(y0+y1)/2
    dx,dy=x1-x0,y1-y0; L=math.hypot(dx,dy); nx,ny=-dy/L,dx/L
    c=(mx+nx*bend,my+ny*bend); L_,R_=[],[]
    for i in range(n+1):
        t=i/n; x=(1-t)**2*x0+2*t*(1-t)*c[0]+t*t*x1; y=(1-t)**2*y0+2*t*(1-t)*c[1]+t*t*y1
        tx=2*(1-t)*(c[0]-x0)+2*t*(x1-c[0]); ty=2*(1-t)*(c[1]-y0)+2*t*(y1-c[1]); l=math.hypot(tx,ty)
        w=(w0+(w1-w0)*t)/2; L_.append((x-ty/l*w,y+tx/l*w)); R_.append((x+ty/l*w,y-tx/l*w))
    return L_+R_[::-1]
def hatch(img,cx,cy,rx,ry,k,rng,w,side=1,dx=30,dy=50):
    for _ in range(k):
        a=rng.uniform(0,2*math.pi); r=math.sqrt(rng.uniform(.2,.9))
        x=cx+rx*r*math.cos(a); y=cy+ry*r*math.sin(a)
        if (x-cx)*side<0: continue
        stroke(img,[(x,y),(x+dx*rng.uniform(.6,1.2)*-side,y+dy*rng.uniform(.6,1.2))],w,DARK,rng,j=2)
def text(img,lines,xr,y,size,col=INK):
    f=ImageFont.truetype('/System/Library/Fonts/MarkerFelt.ttc',size)
    for i,s in enumerate(lines):
        m=Image.new('L',(size*14,int(size*1.6)),0); d=ImageDraw.Draw(m); d.text((4,0),s,font=f,fill=255)
        a=np.array(m,np.float32)[:,:,None]/255; bb=m.getbbox(); wd=bb[2]
        x0=int(xr-wd+OX); y0=int(y+i*size*1.25+OY); reg=img[y0:y0+a.shape[0],x0:x0+a.shape[1]]
        reg[:]=(reg*(1-a)+np.array(col,np.float32)*a).astype(np.uint8)
def bracket(img,x,y0,y1,w,tick,rng):
    stroke(img,[(x,y0),(x,y1)],w,INK,rng,1.5)
    stroke(img,[(x-tick,y0),(x+tick,y0)],w,INK,rng,1.5); stroke(img,[(x-tick,y1),(x+tick,y1)],w,INK,rng,1.5)
def world(b1,l1,b2,l2,blink,arm,cblink):
    rng=np.random.default_rng(7); img=np.full((CH,CW,3),BG,np.uint8)
    # --- creature
    cx=2860; W=13
    for lx in (2690,3030):
        shape(img,limb((lx,420),(lx+(20 if lx>2860 else -20),985),300,250,40*(1 if lx>2860 else -1)),BROWN,W,rng)
        for k in range(3): shape(img,limb((lx-70+k*70,975),(lx-50+k*70+(20 if lx>2860 else -20),1005),60,22,0),GREY,8,rng)
    shape(img,limb((cx,-760),(cx,200),420,700,0)if False else blob(cx,-100,560,790,rng,wob=.03,spiky=.05),BROWN,W,rng)
    hatch(img,cx,-100,540,760,70,rng,8,1)
    hatch(img,cx,-100,540,760,25,rng,8,-1,dx=-25)
    for sgn in (-1,1):
        sh=(cx+sgn*430,-450); hd=(cx+sgn*560,520)
        shape(img,limb(sh,hd,230,170,sgn*70),BROWN2,W,rng)
        hatch(img,(sh[0]+hd[0])/2,(sh[1]+hd[1])/2,90,450,14,rng,8,sgn)
        for k in range(3):
            s=hd[0]+(k-1)*55; shape(img,limb((s,hd[1]-20),(s+(k-1)*20+sgn*25,hd[1]+180),44,6,sgn*50),GREY,8,rng)
    hy=-940
    shape(img,[(cx+sgn*215,hy-170+d) for sgn,d in ((-1,0),(1,0))]+[(cx+sgn*230,hy-90) for sgn in (1,)],BROWN,W,rng) if False else None
    for sgn in (-1,1): shape(img,blob(cx+sgn*230,hy-150,60,70,rng),BROWN,W,rng)
    shape(img,blob(cx,hy,270,230,rng,wob=.03,spiky=.05),BROWN2,W,rng)
    shape(img,blob(cx,hy+90,120,90,rng,wob=.03),(0x60,0x80,0xa0),9,rng)
    cv2.ellipse(img,P(cx,hy+55),(34,22),0,0,360,INK,-1,cv2.LINE_AA)
    for sgn in (-1,1):
        e=(cx+sgn*100,hy-30)
        if cblink: stroke(img,[(e[0]-26,e[1]),(e[0]+26,e[1])],9,INK,rng)
        else: cv2.circle(img,P(*e),22,INK,-1,cv2.LINE_AA)
        stroke(img,[(e[0]-35,e[1]-50),(e[0]+35,e[1]-62+sgn*10)],9,INK,rng)
    stroke(img,[(cx-50,hy+120),(cx,hy+140),(cx+50,hy+120)],8,INK,rng)
    hatch(img,cx,hy,250,210,8,rng,7,1,dx=20,dy=30)
    # --- villager
    vx=760; w=6
    stroke(img,[(vx,410),(vx,720)],w,INK,rng)
    stroke(img,[(vx,500),(vx-100,640)] ,w,INK,rng)
    stroke(img,[(vx,500),(vx+110,640)] if not arm else [(vx,500),(vx+120,360)],w,INK,rng)
    stroke(img,[(vx-18,790),(vx-62,975),(vx-20,980)],w,INK,rng); stroke(img,[(vx+18,790),(vx+62,975),(vx+105,980)],w,INK,rng)
    shape(img,[(vx-85,690),(vx+85,690),(vx+95,790),(vx+55,760),(vx+25,810),(vx-10,765),(vx-45,815),(vx-75,765),(vx-95,790)],LEAF,w,rng)
    stroke(img,[(vx,700),(vx,780)],4,INK,rng,1)
    shape(img,blob(vx,290,100,120,rng,wob=.02),(0xf8,0xf8,0xf8),w,rng)
    shape(img,[(vx-45,185),(vx-30,130),(vx-8,172),(vx+10,115),(vx+25,175),(vx+50,140),(vx+52,190)],BROWN,5,rng)
    for sgn in (-1,1):
        e=(vx+sgn*38,290)
        if blink: stroke(img,[(e[0]-10,e[1]),(e[0]+10,e[1])],5,INK,rng,1)
        else: cv2.circle(img,P(*e),9,INK,-1,cv2.LINE_AA)
    cv2.ellipse(img,P(vx,335),(28,18),0,20,160,INK,5,cv2.LINE_AA)
    # --- brackets
    if b1: bracket(img,560,170,980,6,22,rng)
    if l1: text(img,["4 ft 11 in (150 cm)","110 lbs (50 kg)"],525,500,56)
    if b2: bracket(img,1930,-1155,980,12,50,rng)
    if l2: text(img,["13 ft 1 in (400 cm)","9,900 lbs (4,500 kg)"],1885,-1060,92)
    return img
def ease(t): t=min(max(t,0),1); return t*t*t*(t*(6*t-15)+10)  # smootherstep
cache={}; frames=[]; tl={"bracket1_in":13,"label1_in":14,"zoom":[24,37],"bracket2_in":38,"label2_in":39,"blink_villager":[80,81,121],"villager_arm_swap":[100,101],"creature_blink":[140],"hold":[52,157],"n_frames":N}
cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s','1920x1080','-r','30000/1001','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','14','-r','30000/1001','rt.mp4']
pr=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for f in range(N):
    key=(f>=13,f>=14,f>=38,f>=39,f in(80,81,121),f in(100,101),f==140)
    e=ease((f-24)/13); s=1+(0.43-1)*e; tx=120*e; ty=579*e
    ck=(key,round(s,5))
    if ck not in cache:
        c=world(*key)
        if s<1: c=cv2.GaussianBlur(c,(0,0),0.45/s)
        M=np.array([[s,0,tx-OX*s],[0,s,ty-OY*s]])
        cache[ck]=cv2.warpAffine(c,M,(1920,1080),flags=cv2.INTER_AREA if False else cv2.INTER_LINEAR,borderValue=(BG,)*3)
        if f in(0,20,30,60,100) : cv2.imwrite(f'/tmp/x/f{f}.png',cache[ck])
    pr.stdin.write(cache[ck].tobytes())
pr.stdin.close(); pr.wait()
json.dump(tl,open('timeline.json','w'),indent=1)
