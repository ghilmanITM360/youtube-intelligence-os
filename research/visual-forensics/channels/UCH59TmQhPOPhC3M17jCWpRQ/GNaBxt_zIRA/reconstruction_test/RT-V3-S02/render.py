import json, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
SPEC=json.load(open('SPEC_GIVEN_TO_WORKER.json'))
tab={int(k):v for k,v in SPEC['camera_scale_table'].items()}
def scale(i):
    if i in tab: return tab[i]
    return (tab[i-1]+tab[i+1])/2 if i+1 in tab else tab[i-1]
N=179; K=2; W,H=1920*K,1080*K
rng=np.random.RandomState(7)
def hx(h): h=h.lstrip('#'); return (int(h[4:6],16),int(h[2:4],16),int(h[0:2],16))  # BGR
INK=hx('#101010')
def P(pts): return (np.array(pts,float)*K)
def wob(pts,a=1.5):
    p=P(pts); return (p+rng.uniform(-a,a,p.shape)*K).astype(np.int32)
def poly(img,pts,fill=None,w=5,closed=True):
    p=wob(pts)
    if fill is not None: cv2.fillPoly(img,[p],fill)
    cv2.polylines(img,[p],closed,INK,int(w*K+rng.randint(-1,2)),cv2.LINE_AA)
def rect(img,x0,y0,x1,y1,fill,w=5): poly(img,[(x0,y0),(x1,y0),(x1,y1),(x0,y1)],fill,w)
def ell(img,c,r,fill,w=5):
    cv2.ellipse(img,(int(c[0]*K),int(c[1]*K)),(int(r[0]*K),int(r[1]*K)),0,0,360,fill,-1,cv2.LINE_AA)
    cv2.ellipse(img,(int(c[0]*K),int(c[1]*K)),(int(r[0]*K),int(r[1]*K)),0,0,360,INK,int(w*K),cv2.LINE_AA)
def line(img,a,b,w=5,col=INK):
    cv2.line(img,tuple((np.array(a)*K).astype(int)),tuple((np.array(b)*K).astype(int)),col,int(w*K),cv2.LINE_AA)
def grain(img,x0,y0,x1,y1,col,n,L=60):
    for _ in range(n):
        x=rng.uniform(x0,x1);y=rng.uniform(y0,y1)
        cv2.line(img,(int(x*K),int(y*K)),(int((x+rng.uniform(10,L))*K),int((y+rng.uniform(-2,2))*K)),col,K,cv2.LINE_AA)

WALL=hx('#c89858'); WOOD=hx('#683818'); BOARD=hx('#485028'); FLOOR=hx('#a87c48')
def static():
    im=np.zeros((H,W,3),np.uint8); im[:]=WALL
    im[int(470*K):]=FLOOR
    # wall speckle texture
    for _ in range(9000):
        x=rng.randint(0,W);y=rng.randint(0,int(470*K)); d=rng.randint(-14,6)
        cv2.circle(im,(x,y),rng.randint(1,3),tuple(int(max(0,min(255,c+d))) for c in WALL),-1)
    for y in range(480,1080,40): line(im,(0,y),(1920,y+rng.randint(-3,3)),2,hx('#8c6438'))
    line(im,(0,470),(1920,470),5)
    # board (olive, faint dust) with wood frame
    bx0,by0,bx1,by1=520,110,1400,410
    rect(im,bx0-20,by0-20,bx1+20,by1+20,WOOD,6)
    rect(im,bx0,by0,bx1,by1,BOARD,5)
    layer=np.zeros_like(im)
    for _ in range(40):
        c=(int(rng.uniform(bx0+20,bx1-20)*K),int(rng.uniform(by0+20,by1-20)*K))
        cv2.ellipse(layer,c,(int(rng.uniform(20,60)*K),int(rng.uniform(6,14)*K)),rng.uniform(0,180),0,360,(30,30,28),-1)
    layer=cv2.GaussianBlur(layer,(0,0),9*K)
    m=np.zeros((H,W),np.uint8); cv2.rectangle(m,(bx0*K+6,by0*K+6),(bx1*K-6,by1*K-6),255,-1)
    im[m>0]=np.clip(im[m>0].astype(int)+layer[m>0]//4,0,255).astype(np.uint8)
    grain(im,bx0-18,by0-18,bx1+18,by0-4,hx('#4c2810'),30); grain(im,bx0-18,by1+4,bx1+18,by1+18,hx('#4c2810'),30)
    # chalk ledge
    rect(im,bx0-20,by1+20,bx1+20,by1+36,WOOD,5)
    # posters
    rect(im,250,150,430,320,hx('#e0d0a0'),5)
    ell(im,(340,215),(40,30),hx('#c07040'),4); poly(im,[(310,250),(370,250),(340,295)],hx('#587848'),4)  # fish-ish blob
    rect(im,1450,140,1610,300,hx('#d8c898'),5)
    poly(im,[(1480,270),(1530,170),(1580,270)],hx('#907858'),4); ell(im,(1565,185),(18,18),hx('#e8b838'),4)
    # desks and stools
    for r,(y,s) in enumerate([(640,1.0),(790,1.25),(960,1.5)]):
        for cx in np.linspace(260,1300,4)+r*60:
            w=100*s;h=22*s
            poly(im,[(cx-w,y),(cx+w,y),(cx+w*0.9,y+h),(cx-w*0.9,y+h)],WOOD,5)
            for dx in(-0.7,0.7): line(im,(cx+dx*w,y+h),(cx+dx*w,y+h+60*s),6)
            ell(im,(cx,y+h+70*s),(34*s,10*s),hx('#8a5a30'),4)
            line(im,(cx,y+h+75*s),(cx,y+h+110*s),6)
    grain(im,0,500,1920,1080,hx('#6c4c28'),600,120)
    # lectern (stone)
    poly(im,[(1500,500),(1780,500),(1800,720),(1480,720)],hx('#9a9890'),6)
    for _ in range(200):
        x=rng.uniform(1490,1790);y=rng.uniform(505,715); cv2.circle(im,(int(x*K),int(y*K)),rng.randint(1,3),hx('#7c7a72'),-1)
    line(im,(1500,540),(1780,540),4); line(im,(1530,520),(1760,520),3)
    # text (cursive chalk)
    pil=Image.fromarray(im[...,::-1]); d=ImageDraw.Draw(pil)
    txt="topic: sabre cat"; target=0.60*(bx1-bx0)*K
    size=100
    for _ in range(12):
        f=ImageFont.truetype('/System/Library/Fonts/Supplemental/SnellRoundhand.ttc',size,index=1)
        bb=d.textbbox((0,0),txt,font=f); wd=bb[2]-bb[0]
        size=int(size*target/wd)
    f=ImageFont.truetype('/System/Library/Fonts/Supplemental/SnellRoundhand.ttc',size,index=1)
    bb=d.textbbox((0,0),txt,font=f); cx=(bx0+bx1)/2*K; cy=(by0+by1)/2*K
    pos=(cx-(bb[0]+bb[2])/2,cy-(bb[1]+bb[3])/2)
    d.text(pos,txt,font=f,fill=(236,234,222),stroke_width=1,stroke_fill=(236,234,222))
    tb=(pos[0]+bb[0],pos[1]+bb[1],pos[0]+bb[2],pos[1]+bb[3])
    return np.array(pil)[...,::-1].copy(),tb
BASE,TB=static()
tbc=[v/K for v in TB]
print('text bbox canvas',tbc)

# teacher + pointer drawn per state
HAND=(1500,452)
def teacher(mouth,tip):
    im=BASE.copy()
    # body behind lectern
    poly(im,[(1560,520),(1580,450),(1700,450),(1730,520)],hx('#a05830'),6)
    ell(im,(1640,385),(46,52),hx('#e0b080'),6)   # head (bald)
    ell(im,(1640,345),(10,5),hx('#f0cfa0'),1)
    # moustache
    poly(im,[(1600,405),(1640,396),(1680,405),(1690,470),(1660,425),(1640,420),(1620,425),(1590,470)],hx('#f0f0ea'),5)
    for ex in(1624,1656): ell(im,(ex,372),(5,5),INK,2)
    line(im,(1612,358),(1634,352),4); line(im,(1646,352),(1668,358),4)
    if mouth: ell(im,(1640,432),(10,8),hx('#401818'),3)
    else: line(im,(1628,432),(1652,432),4)
    # arm + hand
    line(im,(1590,480),(1540,470),14,hx('#a05830')); line(im,(1590,480),(1540,470),5)
    line(im,(1540,470),HAND,10,INK); ell(im,HAND,(11,11),hx('#e0b080'),4)
    # stick (thin, extends slightly past hand)
    v=np.array(tip,float)-HAND; u=v/np.linalg.norm(v)
    line(im,tuple(np.array(HAND)-u*40),tip,6,hx('#503010'))
    return im
rest_tip=(1380,700)
# pose swaps: (start frame, tip, mouth)  -- hover/tap steps
ty=(tbc[1]+tbc[3])/2/1.0
tx=lambda f: tbc[0]+f*(tbc[2]-tbc[0])
poses=[(0,rest_tip),(59,(tx(.97)+40,ty+20)),(66,(tx(.92),ty-5)),(68,(tx(.97)+40,ty+20)),
 (84,(tx(.70),ty-10)),(86,(tx(.74),ty+30)),(100,(tx(.45),ty)),(101,(tx(.45),ty+25)),(103,(tx(.45),ty+30)),
 (122,(tx(.22),ty-5)),(124,(tx(.25),ty+25)),(144,(tx(.60),ty-10)),(146,(tx(.60),ty+20)),(148,(tx(.97)+40,ty+20))]
mouth_open=set(list(range(0,12))+list(range(20,28))+list(range(40,46))+list(range(60,68))+list(range(80,90))+list(range(100,112))+list(range(122,134))+list(range(144,156))+list(range(166,172)))
def tip_at(i):
    t=poses[0][1]
    for s,p in poses:
        if i>=s: t=p
    return tuple(float(v) for v in t)
cache={}
cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s','1920x1080','-r','30000/1001','-i','-',
 '-an','-c:v','libx264','-pix_fmt','yuv420p','-preset','slow','-crf','14','rt.mp4']
pr=subprocess.Popen(cmd,stdin=subprocess.PIPE)
scales=[]
for i in range(N):
    key=(i in mouth_open,tip_at(i))
    if key not in cache: cache={key:teacher(*key)}
    s=scale(i); scales.append(s)
    M=np.array([[s/K,0,960*(1-s)],[0,s/K,50*(1-s)]],np.float64)
    out=cv2.warpAffine(cache[key],M,(1920,1080),flags=cv2.INTER_AREA if False else cv2.INTER_LINEAR,borderMode=cv2.BORDER_REPLICATE)
    pr.stdin.write(out.tobytes())
pr.stdin.close(); pr.wait()
s=scales[-1]
sx=lambda c:(c-960)*s+960; sy=lambda c:(c-50)*s+50
print('final text screen bbox',sx(tbc[0]),sy(tbc[1]),sx(tbc[2]),sy(tbc[3]))
poseidx=[p[0] for p in poses]
json.dump({'frames':N,'camera_fixed_point':[960,50],'scales_used':scales,
 'f0':'hard cut wide classroom','push_in':[8,58],'creep':[59,178],
 'pointer_pose_swap_frames':poseidx,'pointer_tap_frames(1-2f each)':[66,67,84,85,100,101,102,122,123,144,145],
 'mouth_open_frames':sorted(mouth_open),
 'text_screen_bbox_final':[sx(tbc[0]),sy(tbc[1]),sx(tbc[2]),sy(tbc[3])]},open('timeline.json','w'))
