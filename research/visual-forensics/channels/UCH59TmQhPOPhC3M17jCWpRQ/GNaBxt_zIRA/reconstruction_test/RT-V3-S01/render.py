import numpy as np, cv2, json, subprocess, random
from PIL import Image, ImageDraw, ImageFont
D='/Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-03-GNaBxt_zIRA-deep-ct-scan/reconstruction_test/RT-V3-S01/'
K=2; CW,CH=1920*K,1080*K; N=179
rng=random.Random(7); nr=np.random.RandomState(7)
INK=(8,8,8)
def hx(h): return tuple(int(h[i:i+2],16) for i in (1,3,5))
WALL,BOARD,WOOD,WOOD2,STONE,SKIN=hx('#c89858'),hx('#485428'),hx('#683818'),hx('#7c4a20'),hx('#9a9484'),hx('#e0a878')
im=Image.new('RGB',(CW,CH),WALL); d=ImageDraw.Draw(im)
def P(p): return [(x*K,y*K) for x,y in p]
def wob(pts,j=2): return [(x+rng.uniform(-j,j),y+rng.uniform(-j,j)) for x,y in pts]
def line(pts,w=None,c=INK):
    pts=P(pts)
    for a,b in zip(pts,pts[1:]):
        d.line([a,b],fill=c,width=int((w or rng.uniform(4,7))*K))
        r=(w or 5)*K/2; d.ellipse([b[0]-r,b[1]-r,b[0]+r,b[1]+r],fill=c)
def poly(pts,fill,out=True):
    d.polygon(P(pts),fill=fill)
    if out: line(pts+[pts[0]])
def rect(x0,y0,x1,y1,fill,out=True):
    pts=wob([(x0,y0),(x1,y0),(x1,y1),(x0,y1)],2); poly(pts,fill,out)
def grain(x0,y0,x1,y1,dark,light,n,horiz=True):
    for _ in range(n):
        y=rng.uniform(y0,y1); x=rng.uniform(x0,x1); L=rng.uniform(30,160)
        c=dark if rng.random()<.6 else light
        if horiz: d.line([(x*K,y*K),(min(x+L,x1)*K,(y+rng.uniform(-2,2))*K)],fill=c,width=K*rng.randint(1,2))
        else: d.line([(x*K,y*K),((x+rng.uniform(-2,2))*K,min(y+L,y1)*K)],fill=c,width=K*rng.randint(1,2))
# floor + wall
rect(-10,700,1930,1090,hx('#b08040'),False)
line([(0,700),(1920,702)],6)
grain(0,704,1920,1080,hx('#8a5c28'),hx('#c89858'),700)
for y in (780,870,970): line([(0,y),(1920,y+rng.uniform(-3,3))],3,hx('#6a4820'))
# wall marks
for _ in range(120):
    x,y=rng.uniform(0,1920),rng.uniform(0,690); pts=[(x,y)]
    for _ in range(rng.randint(2,4)): pts.append((pts[-1][0]+rng.uniform(-25,25),pts[-1][1]+rng.uniform(-18,30)))
    d.line(P(pts),fill=hx('#a97c40') if rng.random()<.7 else hx('#d8ac70'),width=K*rng.randint(1,3))
for _ in range(2200):
    x,y=rng.uniform(0,1920)*K,rng.uniform(0,690)*K; r=rng.uniform(1,3)*K
    d.ellipse([x-r,y-r,x+r,y+r],fill=hx('#b88848') if rng.random()<.5 else hx('#d8a868'))
# board
rect(560,185,1560,625,WOOD)
grain(562,187,1558,623,hx('#3e2008'),hx('#8a5a2c'),500)
rect(590,215,1530,595,BOARD)
for _ in range(900): # board streaks/dust
    x,y=rng.uniform(592,1528),rng.uniform(217,593); L=rng.uniform(10,70)
    d.line([(x*K,y*K),((x+L)*K,(y+rng.uniform(-6,6))*K)],fill=hx('#58623a') if rng.random()<.5 else hx('#3c4420'),width=K*rng.randint(1,3))
for _ in range(60):
    x,y=rng.uniform(610,1510),rng.uniform(230,580); r=rng.uniform(12,40)
    d.ellipse([(x-r)*K,(y-r*.5)*K,(x+r)*K,(y+r*.5)*K],fill=hx('#5c6a42'))
line([(610,590),(1510,590)],3,hx('#8a8e72')) # chalk ledge
rect(620,596,930,614,WOOD2)
# chalk text
def font(sz):
    for f in ('/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf','/System/Library/Fonts/Supplemental/Chalkboard.ttc'):
        try: return ImageFont.truetype(f,sz)
        except Exception: pass
TXT='topic: sabre cat'; fnt=font(104*K)
tl=Image.new('L',(CW,CH),0); td=ImageDraw.Draw(tl)
bb=td.textbbox((0,0),TXT,font=fnt); tw=bb[2]-bb[0]
TX=1130*K-tw//2; TY=int(395*K)
td.text((TX-bb[0],TY),TXT,font=fnt,fill=255)
ta=np.array(tl).astype(np.float32)/255; ta*=(nr.rand(CH,CW)>0.12)  # chalky breakup
base=np.array(im).astype(np.float32)
base=base*(1-ta[...,None]*.92)+np.array([238,238,226],np.float32)*ta[...,None]*.92
im=Image.fromarray(base.astype(np.uint8)); d=ImageDraw.Draw(im)
# posters
def poster(x0,y0,x1,y1,kind):
    rect(x0,y0,x1,y1,hx('#e8d4a0'))
    cx,cy=(x0+x1)/2,(y0+y1)/2
    if kind==0:
        d.ellipse(P([(cx-70,y0+22),(cx-20,y0+72)])[0]+P([(cx-70,y0+22),(cx-20,y0+72)])[1],fill=hx('#d89030'),outline=INK,width=5*K)
        poly([(x0+14,y1-60),(cx-10,y0+110),(cx+30,y1-60)],hx('#8a8070'))
        poly([(cx+10,y1-60),(cx+70,y0+130),(x1-12,y1-60)],hx('#a09484'))
        txt='fire is hot'
    else:
        for i,(dx,dy) in enumerate([(-45,10),(0,-25),(45,10),(0,35)]):
            d.ellipse(P([(cx+dx-18,cy+dy-14),(cx+dx+18,cy+dy+14)])[0]+P([(cx+dx-18,cy+dy-14),(cx+dx+18,cy+dy+14)])[1],fill=hx('#7a5030'),outline=INK,width=4*K)
        txt='big paw!'
    d.text((cx*K,(y1-28)*K),txt,font=font(34*K),fill=INK,anchor='mm')
poster(100,230,370,500,0); poster(1585,250,1745,430,1)
# second small left poster
rect(400,300,520,420,hx('#dcc088')); d.text((460*K,360*K),'no\nbones\ninside',font=font(26*K),fill=INK,anchor='mm',align='center')
for row,(yy,sc) in enumerate([(790,.8),(880,.95),(990,1.1)]):
    for dx in range(120+row*60,1640,330):
        w=190*sc; h=60*sc; x0=dx; y0=yy
        rect(x0+w*.45,y0+h+55*sc,x0+w*.45+70*sc,y0+h+75*sc,WOOD2)   # stool seat
        line([(x0+w*.5,y0+h+75*sc),(x0+w*.48,y0+h+120*sc)],6); line([(x0+w*.65,y0+h+75*sc),(x0+w*.67,y0+h+120*sc)],6)
        line([(x0+10*sc,y0+h),(x0+6*sc,y0+h+110*sc)],7); line([(x0+w-10*sc,y0+h),(x0+w-6*sc,y0+h+110*sc)],7)
        poly([(x0+25*sc,y0),(x0+w,y0),(x0+w+20*sc,y0+h),(x0,y0+h)],WOOD)
        grain(x0+25*sc,y0+4,x0+w,y0+h-4,hx('#3e2008'),hx('#8a5a2c'),14)
# lectern (stone) + teacher body
poly([(1660,650),(1920,650),(1920,1090),(1680,1090)],STONE)
for _ in range(300):
    x,y=rng.uniform(1670,1915),rng.uniform(655,1080); r=rng.uniform(1,4)
    d.ellipse([(x-r)*K,(y-r)*K,(x+r)*K,(y+r)*K],fill=hx('#7e786a') if rng.random()<.5 else hx('#b0aa9a'))
line([(1670,700),(1920,700)],4); line([(1690,900),(1920,900)],3,hx('#6a665a'))
poly([(1715,655),(1735,600),(1845,600),(1865,655)],hx('#8a5a2c'))   # fur tunic
line([(1745,612),(1790,640),(1835,612)],4)
poly([(1650,640),(1920,640),(1920,665),(1650,665)],hx('#aaa496'))
# head
d.ellipse(P([(1730,480),(1850,600)])[0]+P([(1730,480),(1850,600)])[1],fill=SKIN,outline=INK,width=6*K)
d.ellipse(P([(1722,535),(1738,565)])[0]+P([(1722,535),(1738,565)])[1],fill=SKIN,outline=INK,width=5*K)
d.ellipse(P([(1842,535),(1858,565)])[0]+P([(1842,535),(1858,565)])[1],fill=SKIN,outline=INK,width=5*K)
for ex in (1765,1815): d.ellipse([(ex-5)*K,535*K,(ex+5)*K,547*K],fill=INK)
line([(1752,522),(1778,528)],6,hx('#f0f0f0')); line([(1802,528),(1828,522)],6,hx('#f0f0f0'))
line([(1790,540),(1784,562),(1796,562)],4)
poly([(1790,568),(1750,572),(1722,600),(1718,640),(1735,622),(1760,596),(1790,588),(1820,596),(1845,622),(1862,640),(1858,600),(1830,572)],hx('#f4f4f4'))
canvas=np.array(im)
# fine static grain over all
canvas=np.clip(canvas.astype(np.int16)+nr.randint(-9,10,(CH,CW,1)),0,255).astype(np.uint8)
canvas=cv2.cvtColor(canvas,cv2.COLOR_RGB2BGR)
# timeline
def ease(t): t=min(max(t,0),1); return t*t*t*(t*(6*t-15)+10)
HAND=(1722,618); REST=(1706,430)
poses=[(0,REST),(66,(1340,540)),(84,(1215,445)),(86,(1215,456)),(87,(1215,445)),(106,(1040,440)),(108,(1040,452)),(109,(1040,440)),
       (128,(1360,445)),(130,(1360,456)),(131,(1360,445)),(150,(1130,455)),(152,(1130,466)),(153,(1130,455)),(168,(1290,520))]
mouth_open=[(70,75),(80,86),(96,103),(112,120),(126,131),(140,147),(156,162),(168,175)]
def pose(f):
    p=REST
    for s,t in poses:
        if f>=s: p=t
    return p
def view(f):
    e=ease((f-8)/50); s=1+.70*e
    if f>=59: s=1.70+.035*(f-58)/120
    return s,-670*e
def frame(f):
    c=canvas.copy(); tip=pose(f)
    h=(int(HAND[0]*K),int(HAND[1]*K))
    if tip!=REST or True:
        hand=(1722,618)
        cv2.line(c,(int(1752*K),int(655*K)),(int(hand[0]*K),int(hand[1]*K)),hx('#8a5a2c')[::-1],int(26*K))
        cv2.line(c,(int(1752*K),int(655*K)),(int(hand[0]*K),int(hand[1]*K)),INK,int(5*K)) if False else None
        cv2.line(c,(int(hand[0]*K),int(hand[1]*K)),(int(tip[0]*K),int(tip[1]*K)),(40,70,110),int(9*K),cv2.LINE_AA)
        cv2.line(c,(int(hand[0]*K),int(hand[1]*K)),(int(tip[0]*K),int(tip[1]*K)),(20,30,50),int(3*K),cv2.LINE_AA)
        cv2.circle(c,(int(hand[0]*K),int(hand[1]*K)),int(15*K),SKIN[::-1],-1,cv2.LINE_AA)
        cv2.circle(c,(int(hand[0]*K),int(hand[1]*K)),int(15*K),INK,int(4*K),cv2.LINE_AA)
    op=any(a<=f<=b for a,b in mouth_open)
    if op: cv2.ellipse(c,(1790*K,593*K),(11*K,8*K),0,0,360,(20,20,60),-1,cv2.LINE_AA)
    else: cv2.line(c,(1778*K,593*K),(1802*K,593*K),INK,int(4*K),cv2.LINE_AA)
    s,tx=view(f)
    M=np.float32([[s/K,0,960-960*s+tx],[0,s/K,540-540*s]])
    return cv2.warpAffine(c,M,(1920,1080),flags=cv2.INTER_AREA if False else cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s','1920x1080','-r','30000/1001','-i','-',
  '-c:v','libx264','-pix_fmt','yuv420p','-crf','14','-preset','medium','-r','30000/1001','-frames:v',str(N),D+'rt.mp4'],stdin=subprocess.PIPE)
tl=[]
for f in range(N):
    ff.stdin.write(frame(f).tobytes()); s,tx=view(f)
    tl.append(dict(f=f,scale=round(s,4),pan_px=round(tx,1),pointer_tip=pose(f),mouth_open=any(a<=f<=b for a,b in mouth_open)))
ff.stdin.close(); ff.wait()
json.dump(dict(cut_f=0,push_start=8,push_end=58,creep=[59,178],scale_end_push=1.70,scale_end=1.735,pan_total_px=-670,
  pointer_swaps=[dict(f=s,tip=t) for s,t in poses],mouth_open_ranges=mouth_open,frames=tl),open(D+'timeline.json','w'),indent=0)
