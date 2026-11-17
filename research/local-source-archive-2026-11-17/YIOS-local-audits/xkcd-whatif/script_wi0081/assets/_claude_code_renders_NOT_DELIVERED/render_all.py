"""Deterministic code renderer for all 62 GEN assets (no image model, so no drift).
Head = pixels of ALIEN_HEAD_CLEAN (the owner master); body/props = vector line art.
Run: python3 assets/qa/render_all.py   -> assets/final/<ID>.png + PLACEMENT.json"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import numpy as np, math, json, random
ROOT = Path(__file__).resolve().parents[2]; OUT = ROOT/'assets/final'; OUT.mkdir(exist_ok=True)
INK, MINT, G1, G2, RED, BG = (12,12,12,255), (227,252,222,255), (228,228,228,255), (196,196,196,255), (215,38,61,255), (248,248,248,255)
WHITE = (255,255,255,255); SS = 2; PLACE = {}

class Cv:
    def __init__(s, w, h, ox=0, oy=0, k=1, bg=None):
        s.w, s.h, s.ox, s.oy, s.k = w, h, ox, oy, k
        s.im = Image.new('RGBA', (w*SS, h*SS), bg or (0,0,0,0)); s.d = ImageDraw.Draw(s.im)
    def P(s, p): return ((p[0]-s.ox)*s.k*SS, (p[1]-s.oy)*s.k*SS)
    def line(s, pts, w=9, col=INK, wb=1.4, seed=0, closed=False):
        pts = list(pts) + ([pts[0]] if closed else [])
        q = [s.P(p) for p in (wob(pts, wb*0.5/s.k, seed) if wb else pts)]
        ww = max(1, round(w*s.k*SS))
        s.d.line(q, fill=col, width=ww, joint='curve'); r = ww/2
        for x, y in (q[0], q[-1]) if not closed else q[::6]: s.d.ellipse((x-r, y-r, x+r, y+r), fill=col)
    def shape(s, pts, fill=WHITE, w=9, seed=0, wb=1.4, outline=True):
        if fill: s.d.polygon([s.P(p) for p in pts], fill=fill)
        if outline: s.line(pts, w, closed=True, seed=seed, wb=wb)
    def ell(s, cx, cy, rx, ry, fill=WHITE, w=9, rot=0, outline=True, a0=0, a1=360, n=72):
        pts = ellp(cx, cy, rx, ry, rot, a0, a1, n)
        if a1-a0 < 360: s.line(pts, w)
        else: s.shape(pts, fill, w, outline=outline)
    def dot(s, x, y, r, col=INK):
        a, b = s.P((x, y)); rr = r*s.k*SS; s.d.ellipse((a-rr, b-rr, a+rr, b+rr), fill=col)
    def poly_mask(s, pts):
        m = Image.new('L', s.im.size, 0); ImageDraw.Draw(m).polygon([s.P(p) for p in pts], fill=255); return m
    def clip(s, mask): s.im.putalpha(ImageChops.multiply(s.im.getchannel('A'), mask))
    def out(s): return s.im.resize((s.w, s.h), Image.LANCZOS)

def ellp(cx, cy, rx, ry, rot=0, a0=0, a1=360, n=72):
    c, s_ = math.cos(math.radians(rot)), math.sin(math.radians(rot)); r = []
    for i in range(n+1):
        t = math.radians(a0+(a1-a0)*i/n); x, y = rx*math.cos(t), ry*math.sin(t)
        r.append((cx+x*c-y*s_, cy+x*s_+y*c))
    return r[:-1] if a1-a0 >= 360 else r
def wob(pts, a, seed, step=14):
    P = [np.array(p, float) for p in pts]; o = []
    for i in range(len(P)-1):
        n = max(1, int(np.linalg.norm(P[i+1]-P[i])//step)); o += [P[i]+(P[i+1]-P[i])*j/n for j in range(n)]
    o.append(P[-1]); r, c = [o[0]], 0
    for i in range(1, len(o)-1):
        c += np.linalg.norm(o[i]-o[i-1]); t = o[i+1]-o[i-1]; nr = np.array([-t[1], t[0]])/(np.linalg.norm(t)+1e-9)
        r.append(o[i]+nr*a*math.sin(c*0.035+seed))
    r.append(o[-1]); return [tuple(p) for p in r]
def cr(pts, n=12):  # Catmull-Rom smoothing
    P = [pts[0]]+list(pts)+[pts[-1]]; o = []
    for i in range(1, len(P)-2):
        for j in range(n):
            t = j/n; t2, t3 = t*t, t*t*t
            o.append(tuple(0.5*((2*P[i][d])+(-P[i-1][d]+P[i+1][d])*t+(2*P[i-1][d]-5*P[i][d]+4*P[i+1][d]-P[i+2][d])*t2+(-P[i-1][d]+3*P[i][d]-3*P[i+1][d]+P[i+2][d])*t3) for d in (0, 1)))
    return o+[tuple(pts[-1])]
def rotp(p, c, deg):  # visual clockwise on screen
    t = math.radians(deg); x, y = p[0]-c[0], p[1]-c[1]
    return (c[0]+x*math.cos(t)-y*math.sin(t), c[1]+x*math.sin(t)+y*math.cos(t))
def drop(cx, base, h, w):  # teardrop, tip up
    return [(cx, base-h)]+[(cx+w/2*math.sin(math.radians(a)), base-w/2+w/2*math.cos(math.radians(a))) for a in range(20, 341, 10)][:0] + \
        cr([(cx, base-h), (cx+w*0.28, base-h*0.55), (cx+w/2, base-w*0.5), (cx, base), (cx-w/2, base-w*0.5), (cx-w*0.28, base-h*0.55), (cx, base-h)], 8)
def save(aid, im, mode='RGBA', note='', **pl):
    im = im.convert(mode); assert im.size == SIZES[aid], (aid, im.size, SIZES[aid])
    im.save(OUT/f'{aid}.png'); PLACE[aid] = dict(note=note, **pl)

# ---------------------------------------------------------------- character
HA = np.array(Image.open(ROOT/'assets/chr/ALIEN_HEAD_CLEAN.png').convert('RGBA')); HA[..., 3] = np.where(HA[..., 3] >= 240, 255, HA[..., 3])  # owner policy: clamp near-opaque alpha to 255 (master file untouched)
HEAD = Image.fromarray(HA)
def label(mask):
    lab = np.zeros(mask.shape, int); n = 0
    for y, x in zip(*np.nonzero(mask)):
        if lab[y, x]: continue
        n += 1; st = [(y, x)]; lab[y, x] = n
        while st:
            cy, cx = st.pop()
            for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                yy, xx = cy+dy, cx+dx
                if 0 <= yy < mask.shape[0] and 0 <= xx < mask.shape[1] and mask[yy, xx] and not lab[yy, xx]: lab[yy, xx] = n; st.append((yy, xx))
    return lab, n
def prep_head():
    lum = HA[..., :3].mean(-1); dark = (lum < 110) & (HA[..., 3] > 200); dark[:150] = 0; dark[472:] = 0
    lab, n = label(dark); comps = []
    for i in range(1, n+1):
        ys, xs = np.nonzero(lab == i)
        if len(ys) > 150 and not (xs.min() < 345 or xs.max() > 636): comps.append((xs.mean(), ys.mean(), len(ys), i))
    comps.sort(); eyes = [c for c in comps if c[2] > 1500]; mouth = [c for c in comps if c[2] < 1500][0]
    assert len(eyes) == 2, comps
    m = np.zeros(dark.shape, bool)
    for c in comps: m |= (lab == c[3])
    m = np.array(Image.fromarray((m*255).astype('uint8')).filter(ImageFilter.MaxFilter(7))) > 0
    blank = HA.copy(); blank[m] = (227, 251, 222, 255)
    def ink(sel):
        sm = np.array(Image.fromarray((np.isin(lab, sel)*255).astype('uint8')).filter(ImageFilter.MaxFilter(7))) > 0
        a = (np.clip((235-lum)/215, 0, 1)*255*sm).astype('uint8'); z = np.full(m.shape, 12, 'uint8')
        return Image.fromarray(np.dstack([z, z, z, a]), 'RGBA')
    return Image.fromarray(blank), ink([eyes[0][3]]), ink([eyes[1][3]]), ink([mouth[3]]), eyes, mouth
BLANK, EL, ER, MO, EYES, MOUTH = prep_head()
CL, CR_, CM = (EYES[0][0], EYES[0][1]), (EYES[1][0], EYES[1][1]), (MOUTH[0], MOUTH[1])
ca = np.array(HEAD)[..., 3] > 200; ys = np.nonzero(ca[:505].any(1))[0]; CHIN_Y = ys.max(); CHIN_X = np.nonzero(ca[CHIN_Y-3])[0].mean()
MINT_C = 490.0
def xf(im, cx, cy, sx=1, sy=1, rot=0, dx=0, dy=0):  # scale/rotate about (cx,cy) then translate (rot visual CCW)
    t = math.radians(rot); c, s_ = math.cos(t), math.sin(t)
    # forward: p' = C + R(S(p-C)) + d ; PIL needs inverse
    a, b, d_, e = sx*c, -sy*s_, sx*s_, sy*c   # forward matrix [[a,b],[d_,e]] with y-down rotation CCW -> [[c,s],[-s,c]]
    M = np.array([[c*sx, s_*sy], [-s_*sx, c*sy]]); Mi = np.linalg.inv(M); C = np.array([cx, cy]); D = np.array([dx, dy])
    off = C-D-Mi@C if False else C - Mi@(C+D)
    return im.transform(im.size, Image.AFFINE, (Mi[0,0], Mi[0,1], off[0], Mi[1,0], Mi[1,1], off[1]), Image.BICUBIC)
def lid(layer, cut, ey):  # cut the top `cut` fraction of an eye
    a = np.array(layer); ys = np.nonzero(a[..., 3] > 30)[0]; y0, y1 = ys.min(), ys.max(); a[:int(y0+(y1-y0)*cut), 3] = 0
    return Image.fromarray(a, 'RGBA')
def mouth_layer(kind, shift=(0, 0), sx=1):
    cv = Cv(300, 140, int(CM[0]-150), int(CM[1]-70)); x, y = CM[0]+shift[0], CM[1]+shift[1]
    if kind == 'o': cv.ell(x, y+4, 13, 15, fill=None, w=9)
    elif kind == 'smirk': cv.line(cr([(x-24, y+2), (x-4, y+5), (x+16, y+1), (x+30, y-12)], 8), 9, wb=0)
    elif kind == 'frown': cv.line(cr([(x-24, y+8), (x-6, y-3), (x+10, y-3), (x+26, y+9)], 8), 9, wb=0)
    elif kind == 'wavy': cv.line(cr([(x-26, y+2), (x-13, y-5), (x, y+3), (x+13, y-5), (x+26, y+2)], 8), 9, wb=0)
    l = Image.new('RGBA', (1024, 1536), (0,0,0,0)); l.paste(cv.out(), (int(CM[0]-150), int(CM[1]-70))); return l
def head(view='front', expr='neutral', tilt=0, neck=False):
    """returns 1024x1536 RGBA head (master coordinates). view: front/tq/prof/back"""
    if view == 'front' and expr == 'neutral': h = HEAD.copy()
    else:
        el, er, mo = EL, ER, MO
        if view == 'front':
            if expr == 'curious': el = xf(EL, *CL, rot=6); er = xf(ER, *CR_, sx=1.12, sy=1.12, dy=-7); mo = xf(MO, *CM, rot=-8, dx=14)
            elif expr == 'surprised': el = xf(EL, *CL, sx=1.08, sy=1.08); er = xf(ER, *CR_, sx=1.08, sy=1.08); mo = mouth_layer('o')
            elif expr == 'deadpan': el = lid(EL, .35, 0); er = lid(ER, .35, 0); mo = xf(MO, *CM, sx=1.15)
            elif expr == 'smug': el = lid(xf(EL, *CL, rot=-4), .3, 0); er = lid(xf(ER, *CR_, rot=4), .3, 0); mo = mouth_layer('smirk')
            elif expr == 'worried': el = xf(EL, *CL, rot=-16); er = xf(ER, *CR_, rot=16, dy=2); mo = mouth_layer('frown')
        elif view == 'tq': el = xf(EL, *CL, dx=24, sx=1.0); er = xf(ER, *CR_, sx=.62, dx=14); mo = xf(MO, *CM, sx=.8, dx=30)
        elif view == 'prof': el = xf(EL, *CL, sx=.85, dx=70+30); er = Image.new('RGBA', EL.size); mo = xf(MO, *CM, sx=.75, dx=112)
        if view == 'back': el = er = mo = Image.new('RGBA', EL.size)
        interior = Image.fromarray(((np.array(BLANK)[..., 0] > 215) & (np.array(BLANK)[..., 1] > 245) & (np.array(BLANK)[..., 3] > 250)).astype('uint8')*255)
        h = BLANK.copy()
        for f in (el, er, mo):
            f = f.copy(); f.putalpha(ImageChops.multiply(f.getchannel('A'), interior)); h = Image.alpha_composite(h, f)
        if view == 'tq': h = xf(h, MINT_C, 320, sx=.90)
        if view == 'prof': h = xf(h, MINT_C, 320, sx=.66)
    a = np.array(h); a[CHIN_Y+10:] = 0 if not neck else a[CHIN_Y+10:]; h = Image.fromarray(a, 'RGBA')
    if tilt: h = h.rotate(tilt, center=(CHIN_X, CHIN_Y), resample=Image.BICUBIC)
    return h

def ik(S, W, bend=1, L=187.5):
    dx, dy = W[0]-S[0], W[1]-S[1]; d = min(math.hypot(dx, dy), 2*L-0.5); h = math.sqrt(max(L*L-(d/2)**2, 0))
    ux, uy = dx/(math.hypot(dx, dy) or 1), dy/(math.hypot(dx, dy) or 1); mx, my = S[0]+ux*d/2, S[1]+uy*d/2
    c = [(mx-uy*h, my+ux*h), (mx+uy*h, my-ux*h)]; e = max(c, key=lambda p: p[0]*{'L': -1, 'R': 1}[bend]) if bend in ('L', 'R') else max(c, key=lambda p: p[1]*bend)
    return e, (S[0]+ux*d, S[1]+uy*d)
def curl(cv, E, W, kind):
    u = np.array(W)-np.array(E); u = u/np.linalg.norm(u); n = np.array([-u[1], u[0]])
    if kind == 'spoon': c = np.array(W)+u*11+n*0; cv.line(ellp(c[0], c[1], 13, 13, 0, math.degrees(math.atan2(*(-u[::-1]))) + 40 + 90 - 90, math.degrees(math.atan2(*(-u[::-1]))) + 40 + 270, 24), 9, wb=0)
    elif kind == 'pinch':
        for sgn in (1, -1): cv.line([tuple(W), tuple(np.array(W)+u*16+n*7*sgn), tuple(np.array(W)+u*26+n*3*sgn)], 9, wb=0)
    elif kind == 'point': cv.line([tuple(W), tuple(np.array(W)+u*28)], 9, wb=0)
POSES = {  # id: view, tilt(+up), lean, armR wrist, armL wrist, curl kind, expr, ticks
 'P01': ('front', 0, 0, (846,880), (690,880), None, 'neutral', 0), 'P02': ('tq', 10, 0, (1090,335), (690,880), None, 'neutral', 0),
 'P03': ('tq', -25, 0, (846,880), (690,880), None, 'neutral', 0), 'P04': ('tq', 0, 0, (1130,560), (690,880), None, 'neutral', 0),
 'P05': ('tq', 0, 0, (1050,420), (690,880), 'spoon', 'neutral', 0), 'P06': ('tq', -10, 0, (990,453), (690,880), 'spoon', 'neutral', 0),
 'P07': ('tq', -10, 0, (1110,453), (690,880), 'spoon', 'neutral', 0), 'P08': ('tq', -10, 8, (970,453), (690,880), 'spoon', 'worried', 1),
 'P09': ('tq', -10, 8, (1130,453), (690,880), 'spoon', 'worried', -1), 'P10': ('tq', 8, 0, (1050,333), (690,880), 'pinch', 'neutral', 0),
 'P11': ('tq', 0, 0, (1130,470), (690,880), 'point', 'neutral', 0), 'P12': ('front', 6, 0, (996,400), (540,400), None, 'deadpan', 0),
 'P13': ('tq', -15, 0, (1050,285), (690,880), 'pinch', 'neutral', 0), 'P14': ('prof', 30, 0, (846,880), (690,880), None, 'neutral', 0)}
HANG = ((722, 880), (814, 880))
LEGS = {'front': (708, 828), 'tq': (718, 832), 'prof': (726, 822), 'back': (708, 828)}
def figure(view='front', tilt=0, lean=0, wr=(846,880), wl=(690,880), cu=None, expr='neutral', ticks=0, hang=False):
    cv = Cv(1536, 1536); HIP, SH = (768, 760), (768, 520); sh = rotp(SH, HIP, lean); chin = rotp((768, 496), HIP, lean)
    cv.line([chin, sh, HIP], 9, seed=1)
    for i, x in enumerate(LEGS[view]): cv.line([HIP, (x, 1098)], 9, seed=2+i)
    for i, (w, bend) in enumerate(((wl, 'L' if wl[1] >= 800 else 1), (wr, 'R' if wr[1] >= 800 else 1))):
        e, wv = ik(sh, w, bend); cv.line([sh, e, wv], 9, seed=5+i)
        if w == wr and cu: curl(cv, e, wv, cu)
    if view == 'prof': pass
    im = cv.out(); h = head(view, expr, tilt)
    h = h.transform(h.size, Image.AFFINE, (1, 0, -(768-MINT_C), 0, 1, -1), Image.BICUBIC)  # shift head into figure frame
    big = Image.new('RGBA', (1536, 1536), (0,0,0,0)); big.paste(h, (0, 0))
    if lean: big = big.rotate(-lean, center=HIP, resample=Image.BICUBIC)
    im = Image.alpha_composite(im, big)
    if ticks:
        t = Cv(1536, 1536)
        for k in range(2): t.line([(1006+k*22, 300+k*30), (1032+k*22, 292+k*30)] if ticks > 0 else [(1006+k*22, 292+k*30), (1032+k*22, 300+k*30)], 9, wb=0)
        im = Image.alpha_composite(im, t.out())
    return im
def grip_sheet(kind):
    cv = Cv(1536, 768)
    for i, rot in enumerate((0, 14, -14)):
        cx = 256+i*512; W = (cx+(i-1)*14, 420); E = (cx-170+i*30, 640); cv.line([(cx-330+i*40, 740), E, W], 9, seed=i)
        u = np.array(W)-np.array(E); u = u/np.linalg.norm(u)
        if kind in ('G01', 'G02'):
            L = 330 if kind == 'G01' else 300; ang = rot+(0 if kind == 'G01' else 90)
            a = rotp((W[0], W[1]-60), W, ang); b = rotp((W[0], W[1]-60+L), W, ang)
            cv.shape([(a[0]-9, a[1]), (a[0]+9, a[1]), (b[0]+9, b[1]), (b[0]-9, b[1])], WHITE, 9, wb=0); cv.shape(ellp(b[0], b[1]+30, 24, 34, -ang), WHITE, 9, wb=0)
        if kind == 'G04': cv.shape([(W[0]+14, W[1]-18), (W[0]+54, W[1]-18), (W[0]+54, W[1]+22), (W[0]+14, W[1]+22)], WHITE, 9, wb=0)
        curl(cv, E, W, {'G01': 'spoon', 'G02': 'pinch', 'G03': 'point', 'G04': 'pinch'}[kind])
    return cv.out()

# ---------------------------------------------------------------- props
def mug_pts():  # stage coords; outer left/right x at y
    xl = lambda y: 548+8*(y-1110)/260; xr = lambda y: 772-8*(y-1110)/260
    return xl, xr
def mug_cv(fill, line=True):
    cv = Cv(1000, 640, 410, 1060, 2); xl, xr = mug_pts(); r = 16
    body = [(xl(1110), 1110), (xr(1110), 1110)]+[(xr(1370)-r+r*math.cos(math.radians(a)), 1370-r+r*math.sin(math.radians(a))) for a in range(0, 91, 15)]+[(xl(1370)+r-r*math.sin(math.radians(a)), 1370-r+r*math.cos(math.radians(a))) for a in range(0, 91, 15)]
    hand = cr([(xr(1150), 1150), (822, 1148), (852, 1235), (815, 1318), (xr(1320), 1318)], 10)
    if fill: cv.shape(body, WHITE, 7, wb=0); cv.line(hand, 7, wb=0); cv.line([(xl(1120)+4, 1121), (xr(1120)-4, 1121)], 4, wb=0)
    else: cv.shape(body, None, 7, wb=0); cv.line(hand, 7, wb=0); cv.line([(xl(1120)+4, 1121), (xr(1120)-4, 1121)], 4, wb=0)
    return cv
def inner_poly(top=1100):
    xl, xr = mug_pts(); return [(xl(top)+12, top), (xr(top)-12, top), (xr(1362)-12, 1362), (xl(1362)+12, 1362)]
def water(kind):
    cv = Cv(1000, 640, 410, 1060, 2); yw, yc = {'1': (1150, 1150), '2': (1144, 1160), '3': (1126, 1210)}[kind]
    xs = np.linspace(560, 760, 60); surf = []
    for x in xs:
        u = abs(x-660)/100
        surf.append((x, yc-(yc-yw)*(u**2 if kind == '2' else u**1.4) if kind != '1' else yw))
    cv.d.polygon([cv.P(p) for p in surf+[(760, 1362), (560, 1362)]], fill=G1); cv.line(surf, 7, wb=0)
    n = {'1': 0, '2': 3, '3': 5}[kind]
    for i in range(n):
        rx = 22+i*(60/ max(n, 1)) if kind == '3' else 30+i*22; cy = yc+40+i*18
        cv.line(ellp(660, cy, rx, rx*0.35, 0, 190-i*12, 350+i*8, 30), 7, wb=0)
    cv.clip(cv.poly_mask(inner_poly())); return cv
def spoon_draw(cv, gx, gy, ang=0, col=INK, alpha=255):
    top = gy-0.6*680/2*0  # grip fixed; stage coords not used (pixel k=1)
    T = (gx, gy-0.6*680+0); Bn = (gx, gy+0.4*680-120)
    pts_h = [(gx-10, T[1]), (gx+10, T[1]), (gx+10, Bn[1]), (gx-10, Bn[1])]; bowl = ellp(gx, Bn[1]+60, 44, 60)
    R = lambda p: rotp(p, (gx, gy), -ang) if ang else p  # ang>0 = CCW visual
    cv.shape([R(p) for p in bowl], WHITE, 14, wb=0); cv.shape([R(p) for p in pts_h], WHITE, 14, wb=0)
    cv.shape([R(p) for p in bowl[8:28]][:0] or [R(p) for p in bowl], WHITE, 0, wb=0, outline=False)
def spoon(w, h, gx, gy, ang=0, extra=None):
    cv = Cv(w, h); spoon_draw(cv, gx, gy, ang)
    if extra: extra(cv)
    return cv
def dial_ticks(cv, cx, cy, r0, r1, n=24, w=14):
    for i in range(n):
        a = math.radians(-135+270*i/(n-1)); cv.line([(cx+r0*math.sin(a), cy-r0*math.cos(a)), (cx+r1*math.sin(a), cy-r1*math.cos(a))], w, wb=0)
def horse(cv, bx, by, s=1.0):
    P = lambda x, y: (bx+(x-350)*s, by+(y-620)*s)
    for i, x in enumerate((250, 290, 410, 450)): cv.line([P(x, 410), P(x+(4 if i % 2 else -4), 620)], 14, seed=i)
    cv.shape([P(*p) for p in ellp(350, 360, 170, 80)], WHITE, 14)
    cv.shape([P(*p) for p in cr([(450, 330), (480, 250), (505, 190), (545, 170), (590, 215), (560, 235), (530, 240), (505, 330)], 8)], WHITE, 14)
    cv.shape([P(*p) for p in cr([(505, 190), (512, 160), (524, 182)], 4)], WHITE, 14, wb=0)
    for i in range(3): cv.line([P(490-i*6, 200+i*28), P(462-i*12, 215+i*30)], 14, seed=9+i)
    for i in range(3): cv.line(cr([P(190, 330+i*8), P(150-i*10, 390+i*20), P(160-i*12, 470+i*18)], 8), 14, seed=20+i)
    cv.dot(*P(540, 200), 6)

def run_props():
    # --- mug family
    mug_cv(True).out(); save('MUG-01', mug_cv(True).out(), note='stage origin (410,1060), k=2', origin=(410, 1060), k=2)
    save('MUG-02', mug_cv(False).out(), note='identical coordinates to MUG-01', origin=(410, 1060), k=2)
    for i, n in enumerate(('1', '2', '3'), 1): save(f'WTR-0{i}', water(n).out(), note='clipped to inner mug polygon', origin=(410, 1060), k=2)
    cv = Cv(1000, 640, 410, 1060, 2); rnd = random.Random(4)
    for sgn, x0 in ((-1, 580), (1, 740)):
        for j in range(5):
            x = x0+sgn*(10+j*17); y = 1100-14*j+ (j % 2)*10; r = 7 if j % 2 else 9
            if j % 2: cv.shape(drop(x+sgn*6, y+6, 26, 14), G1, 7, wb=0)
            else: cv.ell(x, y, r, r, G1, 7)
        cv.line([(x0+sgn*8, 1084), (x0+sgn*26, 1074)], 7, wb=0)
    save('WTR-04', cv.out(), note='droplets leave the rim y=1110', origin=(410, 1060), k=2)
    # --- spoons (k=1 px canvas; grip pivot)
    spoon_draw_ = lambda cv, x, y, a=0: spoon_draw(cv, x, y, a)
    c = Cv(200, 800); spoon_draw(c, 100, 468); save('SPN-01', c.out(), note='grip at (100,468) = 60% from top', grip=(100, 468))
    for aid, a, gx in (('SPN-02', 20, 200), ('SPN-03', -20, 200)):
        c = Cv(400, 800); spoon_draw(c, gx, 468, a); save(aid, c.out(), note=f'rotated {a} about grip (200,468)', grip=(200, 468))
    c = Cv(600, 800); a2 = Cv(600, 800); spoon_draw(a2, 340, 468); l2 = a2.out(); l2.putalpha(l2.getchannel('A').point(lambda v: v//2))
    spoon_draw(c, 260, 468); base = Image.alpha_composite(l2, c.out()); sp = Cv(600, 800)
    for i in range(4): sp.line([(200+30*0-i*0+40, 560+i*34), (120-i*6, 560+i*34)], 9, wb=0)
    save('SPN-04', Image.alpha_composite(base, sp.out()), note='leading copy grip (260,468), ghost copy 80px right', grip=(260, 468))
    cv = Cv(800, 300, 480, 1040, 2); T = np.array([math.cos(math.radians(15)), -math.sin(math.radians(15))]); Bc = np.array([574., 1156.])
    pts = lambda l0, l1, hw: [tuple(Bc+T*l0+np.array([-T[1], T[0]])*hw), tuple(Bc+T*l1+np.array([-T[1], T[0]])*hw), tuple(Bc+T*l1-np.array([-T[1], T[0]])*hw), tuple(Bc+T*l0-np.array([-T[1], T[0]])*hw)]
    cv.shape(pts(20, 300, 5), WHITE, 7, wb=0); cv.shape([tuple(Bc+(T*math.cos(math.radians(a))*30+np.array([-T[1], T[0]])*math.sin(math.radians(a))*22)) for a in range(0, 360, 12)], WHITE, 7, wb=0)
    save('SPN-05', cv.out(), note='origin (480,1040) k=2; rim contacts (560,1110),(760,1110)', origin=(480, 1040), k=2)
    def drips(cv): [cv.shape(drop(100+d, 800+j*0, 0, 0) if 0 else drop(100+d, y, 30, 16), G1, 14, wb=0) for d, y in ((-18, 790), (6, 835), (24, 872))]; cv.line([(86, 700), (112, 692)], 14, wb=0)
    c = Cv(200, 900); spoon_draw(c, 100, 468); drips(c); save('SPN-06', c.out(), note='grip (100,468)', grip=(100, 468))
    # --- thermometer
    cv = Cv(400, 560); cv.ell(150, 150, 142, 142, WHITE, 14); dial_ticks(cv, 150, 150, 112, 132, w=9); cv.ell(150, 150, 12, 12, INK, 14); cv.line([(150, 292), (150, 440)], 14, wb=0); cv.line([(80, 440), (220, 440)], 14, wb=0)
    save('THM-01', cv.out(), note='dial centre (150,150) px; 24 ticks over 270 deg', pivot=(150, 150))
    cv = Cv(200, 200); cv.line([(100, 100), (100, 6)], 10, wb=0); cv.ell(100, 112, 9, 9, INK, 6); save('THM-02', cv.out(), note='needle 94 px (canvas limit), hub (100,100); 20C=-108deg', pivot=(100, 100))
    cv = Cv(600, 700, 620, 1000, 2); path = cr([(885, 1300), (882, 1190), (856, 1120), (808, 1088), (772, 1100), (756, 1150), (750, 1210), (748, 1250)], 12)
    cv.line(path, 7, wb=0); cv.dot(748, 1255, 6); save('THM-03', cv.out(), note='origin (620,1000) k=2', origin=(620, 1000), k=2)
    # --- table plate, rulers
    cv = Cv(2160, 3840, 0, 0, 2, bg=BG); cv.line([(0, 1700), (1080, 1700)], 7, wb=0); cv.line([(420, 1370), (1080, 1370)], 7, wb=0)
    for x in (450, 1050): cv.line([(x, 1370), (x, 1700)], 7, wb=0)
    save('TBL-01', cv.out(), 'RGB', note='stage plate 1080x1920 at 2x; floor y=1700, table y=1370, left edge x=420')
    cv = Cv(300, 2300); cv.line([(60, 2280), (60, 280)], 14, wb=0)
    for i in range(0, 17):
        y = 2280-i*125; cv.line([(60, y), (60+(70 if i % 2 == 0 else 40), y)], 14, wb=0)
    save('RUL-01', cv.out(), note='spine x=60 px; zero y=2280 px; 250 px per 100 W (50 W minor ticks); top 800 W at y=280', zero=(60, 2280))
    cv = Cv(300, 1300); cv.shape(ellp(100, 1240, 50, 50), WHITE, 14, wb=0); cv.shape([(64, 90), (136, 90), (136, 1215), (64, 1215)], WHITE, 14, wb=0); cv.ell(100, 1240, 40, 40, WHITE, 0, outline=False); cv.line([(78, 1216), (122, 1216)], 0)
    for i in range(17): y = 1210-70*i; cv.line([(144, y), (144+(60 if i % 2 == 0 else 36), y)], 14, wb=0)
    save('THR-01', cv.out(), note='20C tick y=1210 px, 14 px per C, 100C tick y=90')
    # --- jug
    cv = Cv(700, 900); body = [(90, 240), (570, 240), (558, 840), (102, 840)]
    cv.shape(body, WHITE, 14, wb=0); cv.d.polygon([cv.P(p) for p in [(97, 540), (564, 540), (558, 833), (103, 833)]], fill=G1); cv.line([(97, 540), (564, 540)], 14, wb=0)
    cv.shape(body, None, 14, wb=0); cv.line([(90, 240), (40, 214), (70, 262)], 14, wb=0); cv.line(cr([(566, 300), (660, 330), (662, 520), (562, 590)], 8), 14, wb=0)
    for i in range(1, 10): y = 840-60*i; cv.line([(102, y), (102+(70 if i % 5 == 0 else 44), y)], 14, wb=0)
    save('JUG-01', cv.out(), note='250 ml tick at y=540 px (60 px per 50 ml), base y=840')
    # --- clock, bulb, microwave, horse
    cv = Cv(400, 460); cx, cy = 150, 170; cv.d.pieslice([cv.P((cx-100, cy-100)), cv.P((cx+100, cy+100))], -90*1, -90+120, fill=G2) if False else None
    cv.d.pieslice((cx*SS-100*SS, cy*SS-100*SS, cx*SS+100*SS, cy*SS+100*SS), -90, 30, fill=G2); cv.ell(cx, cy, 142, 142, None, 14); cv.shape([(130, 4), (170, 4), (170, 28), (130, 28)], WHITE, 14, wb=0)
    for i in range(12): a = math.radians(30*i); cv.line([(cx+112*math.sin(a), cy-112*math.cos(a)), (cx+130*math.sin(a), cy-130*math.cos(a))], 14, wb=0)
    cv.line([(cx, cy), (cx, cy-100)], 14, wb=0); cv.dot(cx, cy, 10); save('CLK-01', cv.out(), note='centre (150,170); sector 12 to 4 o\'clock', center=(150, 170))
    cv = Cv(300, 420); cv.shape(ellp(150, 262, 70, 70), WHITE, 14, wb=0); cv.shape([(122, 320), (178, 320), (178, 420), (122, 420)], WHITE, 14, wb=0)
    for y in (345, 372, 398): cv.line([(122, y), (178, y)], 12, wb=0)
    cv.line([(130, 320), (130, 280), (140, 262), (150, 290), (160, 262), (170, 280), (170, 320)], 10, wb=0); save('BLB-01', cv.out(), note='base bottom (150,420)')
    cv = Cv(600, 440); cv.shape([(100, 170), (500, 170), (500, 430), (100, 430)], WHITE, 14, wb=0); cv.shape([(130, 200), (350, 200), (350, 400), (130, 400)], G1, 14, wb=0)
    cv.shape([(200, 330), (280, 330), (276, 385), (204, 385)], WHITE, 12, wb=0); cv.line(cr([(280, 345), (306, 348), (306, 372), (278, 372)], 6), 12, wb=0)
    cv.line([(372, 200), (372, 400)], 10, wb=0)
    for y in (240, 300, 360): cv.ell(430, y, 16, 16, WHITE, 12)
    cv.line(cr([(500, 400), (530, 420), (550, 405), (574, 424)], 6), 12, wb=0); save('MWV-01', cv.out(), note='base (300,430)')
    cv = Cv(700, 640); horse(cv, 350, 620, 1.0); save('HRS-01', cv.out(), note='hoof baseline y=620, centre x=350')
    # --- Niagara
    rnd = random.Random(7); cv = Cv(2160, 1620, 0, 0, 2, bg=BG)
    cv.d.rectangle(cv.P((0, 700))+cv.P((1080, 810)), fill=G1)
    L = [(0, 110), (330, 122), (338, 300), (324, 480), (346, 700), (0, 700)]; R = [(1080, 110), (750, 122), (742, 300), (756, 480), (734, 700), (1080, 700)]
    for poly in (L, R): cv.shape(poly, G2, 7, wb=0.8)
    for poly, sg in ((L, 1), (R, -1)):
        for _ in range(26):
            x = (rnd.uniform(30, 300) if sg == 1 else rnd.uniform(780, 1050)); y = rnd.uniform(150, 660); cv.line([(x, y), (x+sg*24, y+14)], 4, wb=0)
    cv.line(cr([(330, 122), (430, 140), (540, 148), (650, 140), (750, 122)], 10), 7, wb=0); cv.line([(0, 700), (1080, 700)], 7, wb=0)
    save('NIA-01', cv.out(), 'RGB', note='stage 1080x810 @2x; crest y=120, pool y=700; centre x 360..720 empty')
    cv = Cv(720, 1160, 0, 0, 2); cv.d.rectangle(cv.P((0, 0))+cv.P((360, 580)), fill=G1)
    for i, x in enumerate(np.linspace(24, 336, 9)): cv.line([(x, 10+rnd.uniform(0, 40)), (x, 440+rnd.uniform(0, 120))], 4, wb=0)
    a = np.array(cv.out()); fade = np.clip((1160-np.arange(1160))/380, 0, 1)[:, None]; a[..., 3] = (a[..., 3]*fade).astype('uint8'); a[:30, :, 3] = (a[:30, :, 3]*(np.arange(30)[:, None]/30)).astype('uint8')
    save('NIA-02', Image.fromarray(a, 'RGBA'), note='top (540,120) bottom (540,700) stage; fading bottom')
    cv = Cv(2160, 1620, 0, 0, 2, bg=BG); cv.d.rectangle(cv.P((0, 700))+cv.P((480, 810)), fill=G1); cv.d.rectangle(cv.P((300, 0))+cv.P((540, 700)), fill=G1)
    for x in (330, 380, 430, 480, 520): cv.line([(x, 20+rnd.uniform(0, 100)), (x, 520+rnd.uniform(0, 140))], 4, wb=0)
    cv.line([(0, 700), (480, 700)], 7, wb=0); cv.shape([(480, 700), (1080, 700), (1080, 810), (480, 810)], G2, 7, wb=0)
    cv.shape([(490, 540), (590, 540), (580, 700), (500, 700)], WHITE, 7, wb=0); cv.d.polygon([cv.P(p) for p in [(493, 590), (587, 590), (580, 697), (500, 697)]], fill=G1); cv.line([(493, 590), (587, 590)], 7, wb=0)
    save('NIA-03', cv.out(), 'RGB', note='cup base (540,700), cup 160 tall? (stage) ~160; curtain x 300..540')
    cv = Cv(900, 400, 0, 0, 2); ix, iy = 225, 185
    for i in range(14):
        t = math.radians(-80+160*i/13); r = 70+ (i % 3)*34; x, y = ix+r*math.sin(t), iy-r*math.cos(t)*1.0
        cv.line([(ix+34*math.sin(t), iy-34*math.cos(t)), (ix+(r-18)*math.sin(t), iy-(r-18)*math.cos(t))], 7, wb=0); cv.ell(x, y, 8+(i % 2)*3, 8+(i % 2)*3, G1, 7)
    cv.line([(ix-30, iy), (ix+30, iy)], 7, wb=0); save('NIA-04', cv.out(), note='impact point canvas px (450,370); crown above', impact=(450, 370))
    cv = Cv(400, 1200); cv.shape(ellp(200, 120, 170, 120), WHITE, 14, wb=0); cv.shape([(30, 120), (370, 120), (370, 1080), (30, 1080)], WHITE, 14, wb=0); cv.shape(ellp(200, 1080, 170, 90), WHITE, 14, wb=0)
    cv.d.rectangle(cv.P((34, 122)) + cv.P((366, 1078)), fill=WHITE); cv.line([(30, 120), (30, 1080)], 14, wb=0); cv.line([(370, 120), (370, 1080)], 14, wb=0)
    for i in range(12): y = 1010-i*80; cv.line([(250, y), (250+(70 if i % 5 == 0 else 40), y)], 14, wb=0)
    save('NIA-06', cv.out(), note='12 ticks each 0.01 C, 80 px apart, tick0 y=1010; capsule frame = magnifier-style')
    # --- cavitation
    cv = Cv(1400, 900); cv.shape([(80, 130), (1320, 130), (1320, 870), (80, 870)], G1, 14, wb=0); cv.line([(80, 130), (1320, 130)], 14, wb=0)
    cv.line([(715, 500), (860, 40)], 20, wb=0, col=INK); cv.line([(715, 500), (860, 40)], 6, wb=0, col=WHITE)
    cv.shape(ellp(620, 520, 120, 60), WHITE, 14, wb=0)
    for y in (490, 520, 550): cv.line([(330, y), (440, y)], 14, wb=0)
    save('CAV-01', cv.out(), note='bowl trailing edge canvas px (500,520); moves right', trailing=(500, 520))
    cv = Cv(700, 450, 0, 0, 1)
    for i, (x, y, r) in enumerate([(236, 252, 8), (218, 262, 13), (196, 250, 10), (176, 266, 17), (160, 244, 7), (140, 262, 12), (118, 252, 9), (100, 268, 6), (205, 284, 6), (150, 226, 5), (250, 240, 6)]): cv.ell(x, y, r, r, WHITE, 7)
    save('CAV-02', cv.out(), note='canvas = stage scale; cluster origin (250,260) spreads to x=90', origin_px=(250, 260))
    cv = Cv(900, 800); cv.shape([(150, 120), (750, 120), (750, 560), (700, 600), (200, 600), (150, 560)], WHITE, 14, wb=0); cv.d.polygon([cv.P(p) for p in [(157, 170), (743, 170), (743, 556), (696, 594), (204, 594), (157, 556)]], fill=G1); cv.line([(157, 170), (743, 170)], 14, wb=0)
    cv.line([(750, 200), (810, 200)], 14, wb=0); cv.line([(150, 200), (90, 200)], 14, wb=0)
    for i, (x, y, r) in enumerate([(250, 560, 10), (330, 540, 13), (420, 565, 9), (500, 550, 14), (580, 565, 10), (660, 540, 12), (300, 420, 11), (470, 360, 14), (610, 300, 10)]): cv.ell(x, y, r, r, WHITE, 7)
    for x in (300, 420, 540, 640): cv.line(cr([(x, 100), (x-14, 70), (x+14, 40), (x, 14)], 6), 10, wb=0)
    for i, (x, h) in enumerate(((380, 110), (450, 160), (520, 110))): cv.shape(drop(x, 760, h, 60), RED, 10, wb=0)
    save('CAV-03', cv.out(), note='flame centre canvas (450,660); bubble row y=580')
    cv = Cv(300, 300)
    for x, h, w in ((150, 160, 96), (100, 110, 60), (200, 110, 60)): cv.shape(drop(x, 300, h, w), RED, 10, wb=0)
    save('FLM-01', cv.out(), note='base (150,300)')
    # --- reference sheets
    cv = Cv(2400, 900)
    for i in range(3):
        x0 = 120+i*780
        cv.shape([(x0, 220), (x0+460, 220), (x0+440, 740), (x0+20, 740)] if i != 1 else ellp(x0+230, 480, 230, 230), WHITE, 14, wb=0)
        if i == 0: cv.line(cr([(x0+460, 290), (x0+600, 300), (x0+620, 470), (x0+450, 680)], 8), 14, wb=0)
        if i == 1: cv.ell(x0+230, 480, 210, 210, G1, 14); cv.line(cr([(x0+440, 380), (x0+590, 400), (x0+590, 560), (x0+440, 580)], 8), 14, wb=0)
        if i == 2: cv.ell(x0+230, 220, 230, 60, WHITE, 14); cv.line(cr([(x0+460, 290), (x0+600, 300), (x0+620, 470), (x0+450, 680)], 8), 14, wb=0)
        y = 740-0.9*520
        for xx in range(x0+10, x0+450, 40): cv.line([(xx, y), (xx+20, y)], 8, wb=0)
    save('MUG-R01', cv.out(), note='side / top-down / three-quarter; dashed line at 90% fill')
    cv = Cv(2000, 800); cv.ell(400, 400, 300, 300, WHITE, 14); dial_ticks(cv, 400, 400, 230, 270); cv.line([(400, 400), (480, 220)], 12, wb=0); cv.ell(400, 400, 20, 20, INK, 14)
    cv.shape([(900, 120), (990, 120), (990, 640), (900, 640)], WHITE, 14, wb=0); cv.line([(900, 700), (1000, 700)], 14, wb=0)
    cv.line(cr([(1300, 700), (1360, 400), (1520, 250), (1700, 360), (1760, 560)], 12), 14, wb=0); cv.dot(1760, 575, 14)
    save('THM-R01', cv.out(), note='front dial / side body / probe cable')
SIZES = {}
def render_chars():
    for i in range(1, 5):
        v = ('front', 'tq', 'prof', 'back')[i-1]; save(f'CHR-V0{i}', figure(v), note=f'view {v}')
    for i, e in enumerate(('neutral', 'curious', 'surprised', 'deadpan', 'smug', 'worried'), 1):
        save(f'CHR-X0{i}', head('front', e, neck=True), note=f'expression {e}; master coordinates (identity for neutral)')
    for g in ('G01', 'G02', 'G03', 'G04'): save(f'CHR-{g}', grip_sheet(g), note='arm end curl, 26px, no hand')
    for p, (v, t, l, wr, wl, c, e, tk) in POSES.items():
        save(f'CHR-{p}', figure(v, t, l, wr, wl, c, e, tk), note=f'pose {p}; wrists R{wr} L{wl}')

if __name__ == '__main__':
    import re
    spec = json.loads((ROOT/'assets/qa/spec_inventory.json').read_text())
    for k, v in spec.items():
        if '/ GEN /' in v['spec']:
            m = re.search(r'\*\*Output:\*\* (\d+)x(\d+)', v['spec']); SIZES[k] = (int(m.group(1)), int(m.group(2)))
    render_chars(); run_props()
    miss = [k for k in SIZES if k not in PLACE]; print('rendered', len(PLACE), 'missing', miss)
    (ROOT/'assets/PLACEMENT.json').write_text(json.dumps(PLACE, indent=1))
