import numpy as np, cv2, json, subprocess, math, random, os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
W, H, N, HOR = 1920, 1080, 208, 250
rng = random.Random(7)
INK = (16, 16, 16)
def bgr(h): return (int(h[4:6],16), int(h[2:4],16), int(h[0:2],16))
def cxf(y):
    u = (y-HOR)/(H-HOR); return 960 + (60+260*u)*math.sin(2*math.pi*1.25*u + 0.3)
def wf(y):
    u = max((y-HOR)/(H-HOR), 0); return 100 + 1900*u**0.95

# ---------- static background (drawn once) ----------
bg = np.zeros((H, W, 3), np.uint8); bg[:] = bgr('d0f8f8')
def wob(pts, j=3):
    return [(x+rng.uniform(-j,j), y+rng.uniform(-j,j)) for x, y in pts]
def line(img, pts, col=INK, lo=4, hi=7, j=2):
    pts = wob(pts, j)
    for a, b in zip(pts, pts[1:]):
        cv2.line(img, (int(a[0]),int(a[1])), (int(b[0]),int(b[1])), col, rng.randint(lo,hi), cv2.LINE_AA)
def curve(f, t0, t1, n=40):
    return [f(t0+(t1-t0)*i/n) for i in range(n+1)]
# ground
bg[HOR:] = bgr('98b858')
# distant hills + clouds
for cx0, w0, h0 in [(200,380,70),(700,300,50),(1300,420,80),(1750,300,60)]:
    pts = curve(lambda t: (cx0+w0*t, HOR-h0*math.cos(t*math.pi/2*1.0)**1.2*1.0+8), -1, 1, 30)
    poly = np.array(pts+[(cx0+w0,HOR+4),(cx0-w0,HOR+4)], np.int32)
    cv2.fillPoly(bg, [poly], bgr('a8d8a0')); line(bg, pts, (60,80,60), 2, 3)
for _ in range(9):
    x, y = rng.randint(50,1850), rng.randint(25,150); L = rng.randint(80,220)
    line(bg, curve(lambda t:(x+L*t, y+10*math.sin(t*5)), 0, 1, 12), (190,215,215), 2, 4, 1)
# two hills
for hx, hw, ht, hb in [(330,560,430,760),(1620,600,470,820)]:
    pts = curve(lambda t: (hx+hw*t, hb-(hb-ht)*(1-t*t)**0.8), -1, 1, 50)
    poly = np.array(pts+[(hx+hw,H),(hx-hw,H)], np.int32)
    cv2.fillPoly(bg, [poly], bgr('789838')); line(bg, pts, INK, 5, 7)
# river
ys = list(range(HOR, H+1, 8))
L = [(cxf(y)-wf(y)/2, y) for y in ys]; R = [(cxf(y)+wf(y)/2, y) for y in ys]
cv2.fillPoly(bg, [np.array(L+R[::-1], np.int32)], bgr('68c8d8'))
# water band lighter alt tint in lower-right to use #68b8d8
m = np.zeros((H,W), np.uint8); cv2.fillPoly(m, [np.array(L+R[::-1], np.int32)], 255)
pass
line(bg, L, INK, 4, 7); line(bg, R, INK, 4, 7)
# grass strokes/tufts on land
land = np.ones((H,W), np.uint8)*255; cv2.fillPoly(land, [np.array(L+R[::-1], np.int32)], 0)
cnt = 0
while cnt < 2600:
    x, y = rng.randint(0,W-1), rng.randint(HOR+10,H-1)
    if not land[y,x]: continue
    s = 0.5+ (y-HOR)/400.0; hgt = rng.randint(8,16)*min(s,2.0)
    col = (30,90,50) if bg[y,x,0] < 100 else (50,120,80)
    for k in (-1,0,1):
        cv2.line(bg,(x+k*5,y),(x+k*8+rng.randint(-2,2),int(y-hgt)),col,rng.randint(2,3),cv2.LINE_AA)
    cnt += 1
# ripples on water
cnt = 0
while cnt < 650:
    x, y = rng.randint(0,W-1), rng.randint(HOR+8,H-4)
    if land[y,x]: continue
    s = 0.15+(y-HOR)/830*1.1; ln = int(40*s)+8
    col = (255,250,235) if rng.random()<.6 else (150,120,60)
    line(bg, curve(lambda t:(x+ln*t, y+4*s*math.sin(t*6)), 0, 1, 8), col, 2, 3, 0.5); cnt += 1
# village on horizon
for vx in range(1180, 1420, 34):
    w2 = rng.randint(14,20); y0 = HOR-2
    cv2.rectangle(bg,(vx,y0-10),(vx+w2,y0),bgr('e8e0d0'),-1)
    roof = np.array([(vx-3,y0-10),(vx+w2//2,y0-24),(vx+w2+3,y0-10)],np.int32)
    cv2.fillPoly(bg,[roof],bgr('5060c0')); cv2.polylines(bg,[roof],True,INK,2,cv2.LINE_AA)
    cv2.rectangle(bg,(vx,y0-10),(vx+w2,y0),INK,2,cv2.LINE_AA)
# trees
def tree(x, y, s):
    line(bg, [(x,y),(x-3*s,y-50*s),(x,y-90*s)], INK, 5, 7, 1)
    line(bg, [(x+14*s,y),(x+12*s,y-45*s),(x+10*s,y-90*s)], INK, 5, 7, 1)
    cv2.rectangle(bg,(x+2,int(y-88*s)),(x+10,int(y-2)),bgr('684820'),-1)
    for dx, dy, r in [(-40,-120,44),(35,-125,46),(0,-170,50),(-5,-110,42)]:
        cv2.circle(bg,(int(x+dx*s),int(y+dy*s)),int(r*s),bgr('507820'),-1,cv2.LINE_AA)
    for dx, dy, r in [(-40,-120,44),(35,-125,46),(0,-170,50)]:
        cv2.ellipse(bg,(int(x+dx*s),int(y+dy*s)),(int(r*s),int(r*s)),0,rng.randint(0,40),rng.randint(250,320),INK,5,cv2.LINE_AA)
tree(150, 520, 1.1); tree(300, 700, 1.4); tree(1700, 640, 1.2)
bg = np.ascontiguousarray(bg)

# ---------- sprites (3x supersampled, RGBA) ----------
SS = 3
def font(sz): return ImageFont.truetype('/Library/Fonts/Bradley Hand Bold.ttf', sz*SS) if os.path.exists('/Library/Fonts/Bradley Hand Bold.ttf') else ImageFont.truetype('/System/Library/Fonts/Noteworthy.ttc', sz*SS)
def hand_text(d, xy, txt, sz):
    f = font(sz); x, y = xy[0]*SS, xy[1]*SS
    for ch in txt:
        if ch == ' ': x += sz*SS*0.3; continue
        tmp = Image.new('RGBA', (sz*SS*2, sz*SS*2), (0,0,0,0)); td = ImageDraw.Draw(tmp)
        td.text((sz*SS*0.5, sz*SS*0.3), ch, font=f, fill=(255,255,255,255), stroke_width=3*SS//1, stroke_fill=(16,16,16,255))
        tmp = tmp.rotate(rng.uniform(-7,7), resample=Image.BICUBIC)
        d._image.alpha_composite(tmp, (int(x-sz*SS*0.5), int(y-sz*SS*0.3+rng.uniform(-4,4)*SS)))
        x += d.textlength(ch, font=f)*0.92
def group(txt, item):
    im = Image.new('RGBA', (520*SS, 260*SS), (0,0,0,0)); d = ImageDraw.Draw(im); d._image = im
    hand_text(d, (20, 10), txt, 92)
    # dotted arrow from under text to item
    x0, y0, x1, y1 = 260, 125, 400, 190
    for i in range(7):
        t = i/7; px, py = (x0+(x1-x0)*t)*SS, (y0+(y1-y0)*t)*SS
        d.ellipse([px-6*SS, py-6*SS, px+6*SS, py+6*SS], fill=(255,255,255,255), outline=(16,16,16,255), width=SS*2)
    ax, ay = x1*SS, y1*SS
    d.polygon([(ax-4*SS,ay-22*SS),(ax+24*SS,ay-4*SS),(ax-18*SS,ay+12*SS)], fill=(255,255,255,255), outline=(16,16,16,255), width=SS*2)
    ix, iy = 440*SS, 215*SS
    if item == 'dot':
        d.ellipse([ix-9*SS,iy-9*SS,ix+9*SS,iy+9*SS], fill=(24,24,24,255))
        for a in (-2,0,2): d.line([ix+a*5*SS,iy,ix+a*9*SS,iy+16*SS], fill=(16,16,16,255), width=2*SS)
    elif item == 'blob':
        d.polygon([(ix-26*SS,iy+6*SS),(ix-18*SS,iy-12*SS),(ix,iy-18*SS),(ix+20*SS,iy-10*SS),(ix+30*SS,iy+8*SS),(ix+8*SS,iy+16*SS),(ix-14*SS,iy+14*SS)], fill=(40,80,120,255), outline=(16,16,16,255), width=3*SS)
    else:
        d.polygon([(ix-30*SS,iy),(ix,iy-16*SS),(ix+24*SS,iy),(ix,iy+16*SS)], fill=(150,150,150,255), outline=(16,16,16,255), width=3*SS)
        d.polygon([(ix+22*SS,iy),(ix+42*SS,iy-14*SS),(ix+42*SS,iy+14*SS)], fill=(150,150,150,255), outline=(16,16,16,255), width=3*SS)
        d.ellipse([ix-20*SS,iy-6*SS,ix-14*SS,iy],fill=(16,16,16,255))
        d.line([ix-31*SS,iy+3*SS,ix-22*SS,iy+7*SS],fill=(16,16,16,255),width=2*SS)
    return np.array(im)
def person():
    w, h = 300, 340
    im = Image.new('RGBA', (w*SS, h*SS), (0,0,0,0)); d = ImageDraw.Draw(im)
    def S(l): return [(x*SS, y*SS) for x, y in l]
    O = (16,16,16,255)
    d.polygon(S([(20,340),(30,215),(90,190),(210,190),(270,215),(285,340)]), fill=(220,150,60,255), outline=O, width=6*SS)  # torso
    d.rectangle([128*SS,170*SS,172*SS,200*SS], fill=(240,200,160,255), outline=O, width=5*SS)  # neck
    d.ellipse([75*SS,30*SS,225*SS,190*SS], fill=(245,208,170,255), outline=O, width=6*SS)  # head
    d.pieslice([72*SS,22*SS,228*SS,150*SS], 180, 360, fill=(60,40,30,255), outline=O, width=6*SS)  # hair
    for ex in (125, 175):  # closed eyes arcs
        d.arc([(ex-17)*SS,112*SS,(ex+17)*SS,136*SS], 20, 160, fill=O, width=5*SS)
        d.line([(ex-6)*SS,134*SS,(ex-10)*SS,146*SS], fill=(90,140,200,255), width=3*SS)  # tear
    d.arc([128*SS,150*SS,172*SS,176*SS], 200, 340, fill=O, width=5*SS)  # frown
    d.line([(100)*SS,98*SS,(118)*SS,92*SS], fill=O, width=4*SS); d.line([(200)*SS,98*SS,(182)*SS,92*SS], fill=O, width=4*SS)
    return np.array(im)
SPR = {1: group('bugs','dot'), 2: group('mud','blob'), 3: group('rotten fish','fish')}
FIG = person()
def prem(a): 
    f = a.astype(np.float32); f[...,:3] *= f[...,3:]/255.0; return f
def place(frame, spr, cx, cy, s, ref, reveal=1.0):
    sh, sw = spr.shape[:2]
    if reveal < 1.0:
        spr = spr.copy(); spr[:, int(sw*reveal):] = 0
    tw, th = max(int(sw*s/SS*ref[0]),1), max(int(sh*s/SS*ref[1]),1)
    r = cv2.resize(prem(spr), (tw, th), interpolation=cv2.INTER_AREA)
    x0, y0 = int(cx-tw/2), int(cy-th/2)
    xa, ya, xb, yb = max(x0,0), max(y0,0), min(x0+tw,W), min(y0+th,H)
    if xa >= xb or ya >= yb: return (x0,y0,x0+tw,y0+th)
    r = r[ya-y0:yb-y0, xa-x0:xb-x0]; a = r[...,3:]/255.0
    reg = frame[ya:yb, xa:xb].astype(np.float32)
    frame[ya:yb, xa:xb] = np.clip(r[...,:3][..., ::-1]*0 + 0, 0, 0) if False else np.clip(r[...,[2,1,0]] + reg*(1-a), 0, 255).astype(np.uint8)
    return (x0, y0, x0+tw, y0+th)

# ---------- timeline ----------
G = {1:dict(ap=55,y0=600,o0=-250,s0=.6,y1=340,o1=-60,s1=.22),
     2:dict(ap=85,y0=780,o0=-330,s0=.8,y1=410,o1=-150,s1=.28),
     3:dict(ap=115,y0=940,o0=-420,s0=1.0,y1=502,o1=-240,s1=.36)}
DR0, DR1, FIG0, FIG1 = 70, 195, 140, 207
def smooth(t): t = min(max(t,0),1); return t*t*(3-2*t)
def lerp(a,b,t): return a+(b-a)*t
tl = {'static_camera': True, 'groups': {}, 'figure': {'enter': FIG0, 'end': FIG1}, 'drift': [DR0, DR1]}
for k, g in G.items(): tl['groups'][str(k)] = {'appear': g['ap'], 'writeon_frames': 6, 'drift_start': max(DR0, g['ap']), 'drift_end': DR1}
enc = subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30000/1001','-i','-',
    '-an','-c:v','libx264','-pix_fmt','yuv420p','-preset','medium','-crf','14','-r','30000/1001',os.path.join(HERE,'rt.mp4')], stdin=subprocess.PIPE)
fr_check = {}
for f in range(N):
    fr = bg.copy(); boxes = {}
    # figure first (under labels)
    if f >= FIG0:
        p = smooth((f-FIG0)/(FIG1-FIG0)); y = lerp(1130, 410, p)
        u = max((y-HOR)/(H-HOR), 0); s = 0.2+0.8*min(u,1)*0.95
        x = cxf(y)+280*s + 10*math.sin(f*0.15)*s
        boxes['fig'] = place(fr, FIG, x, y, s, (1,1))
    for k, g in G.items():
        if f < g['ap']: continue
        p = smooth((f-max(DR0,g['ap']))/(DR1-max(DR0,g['ap']))) if f >= DR0 else 0
        y = lerp(g['y0'], g['y1'], p); o = lerp(g['o0'], g['o1'], p); s = lerp(g['s0'], g['s1'], p)
        rv = min((f-g['ap']+1)/6.0, 1.0)
        boxes[k] = place(fr, SPR[k], cxf(y)+o, y, s, (1,1), rv)
    ks = list(boxes)
    for i in range(len(ks)):
        for j in range(i+1, len(ks)):
            a, b = boxes[ks[i]], boxes[ks[j]]
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                print('OVERLAP', f, ks[i], ks[j], a, b)
    if f in (0,60,120,150,207): cv2.imwrite(os.path.join(HERE, f'_chk_{f}.png'), fr)
    enc.stdin.write(fr.tobytes())
enc.stdin.close(); enc.wait()
json.dump(tl, open(os.path.join(HERE,'timeline.json'),'w'), indent=1)
