import cv2, numpy as np, os, math, csv, subprocess, shutil
D = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(D, "frames_tmp"); os.makedirs(FR, exist_ok=True)
W, H = 1920, 1080
AA = cv2.LINE_AA
TEAL = (0x8A, 0x8A, 0x1F)       # BGR of #1F8A8A
INK = (40, 40, 40); PAPER = (247, 247, 247); GREY = (225, 225, 225)
DARK = (18, 14, 14); WHITE = (245, 245, 245)
F = cv2.FONT_HERSHEY_DUPLEX

def text(img, s, org, scale=1.2, col=INK, th=3, frac=1.0, center=False):
    n = max(0, math.ceil(len(s) * frac))
    if n == 0: return
    if center:
        w = cv2.getTextSize(s, F, scale, th)[0][0]; org = (org[0] - w // 2, org[1])
    cv2.putText(img, s[:n], org, F, scale, col, th, AA)

def pebble(img, cx, cy, s=1.0, col=INK, hold_mug=False, dark=False):
    c = WHITE if dark else INK
    cv2.ellipse(img, (cx, cy), (int(80*s), int(105*s)), 0, 0, 360, c, 4, AA)
    for dx in (-28, 28): cv2.circle(img, (cx+int(dx*s), cy-int(25*s)), int(7*s), c, -1, AA)
    cv2.ellipse(img, (cx, cy+int(5*s)), (int(18*s), int(10*s)), 0, 10, 170, c, 3, AA)
    if hold_mug:
        mug(img, cx+int(130*s), cy+int(40*s), 0.55, c)
        cv2.line(img, (cx+int(70*s), cy+int(30*s)), (cx+int(100*s), cy+int(55*s)), c, 4, AA)

def mug(img, cx, cy, s=1.0, col=INK):
    w, h = int(90*s), int(110*s)
    cv2.rectangle(img, (cx-w, cy-h//2), (cx+w, cy+h//2+int(20*s)), col, 4, AA)
    cv2.ellipse(img, (cx+w, cy), (int(50*s), int(40*s)), 0, -90, 90, col, 4, AA)

def steam(img, cx, cy, s=1.0, frac=1.0, col=TEAL):
    for i, dx in enumerate((-50, 0, 50)):
        pts = [(cx+int((dx+14*math.sin(t/8*6.28+i))*s), cy-int(t*9*s)) for t in range(9)]
        k = max(2, int(len(pts)*frac)) if frac > 0 else 0
        if k >= 2: cv2.polylines(img, [np.array(pts[:k], np.int32)], False, col, 4, AA)

def glow(img, cx, cy, r=330):
    ov = np.zeros((H, W), np.float32); yy, xx = np.ogrid[:H, :W]
    ov = np.clip(1 - np.hypot(xx-cx, yy-cy)/r, 0, 1)**2
    img[:] = np.clip(img*(1-ov[..., None]*0.9) + np.array(TEAL)*ov[..., None]*0.9*1.0, 0, 255).astype(np.uint8)

def canvas(dark=False): return np.full((H, W, 3), DARK if dark else PAPER, np.uint8)

def anchor(img, s, dark=False):
    cv2.rectangle(img, (560, 30), (1360, 110), TEAL, -1, cv2.LINE_AA)
    text(img, s, (960, 85), 1.4, WHITE, 3, center=True)

def board(img, dark=False):
    cv2.rectangle(img, (620, 260), (1780, 960), WHITE if dark else INK, 4, AA)

ev = []
def E(a, b, dev, d): ev.append((a, b, dev, d))

def scene1(f):
    im = canvas(); cv2.rectangle(im, (140, 40), (1780, 190), GREY, -1, AA)
    cv2.rectangle(im, (140, 40), (1780, 190), INK, 3, AA)
    text(im, "Q. WHAT IF YOUR COFFEE NEVER COOLED DOWN?", (180, 135), 1.5, INK, 3, frac=min(1, (f+1)/10))
    pebble(im, 330, 700, 1.6); board(im); return im
def scene2(f):
    im = scene1(10)
    if f >= 84: mug(im, 1200, 640, 1.8)
    if f >= 108: steam(im, 1200, 540, 1.8, min(1, (f-107)/8))
    if f >= 116: text(im, "85°C", (1420, 500), 1.8, TEAL, 4)
    return im
def scene3(f):
    im = canvas(); a = "T = 0 MIN" if f < 176 else "T = 10 MIN" if f < 200 else "T = 1 HOUR"
    anchor(im, a); mug(im, 960, 560, 2.2)
    if f >= 204:
        text(im, "COOLS TO 40°C", (960, 900), 1.8, INK, 4, center=True)
        if f >= 216:
            p = min(1, (f-215)/8); cv2.line(im, (560, 880), (560+int(800*p), 880), TEAL, 8, AA)
    return im
def scene4(f):
    im = canvas(True); glow(im, 960, 560); mug(im, 960, 560, 2.2, WHITE); anchor(im, "T = 1 HOUR", True)
    if f >= 264: text(im, "STILL 85°C", (960, 900), 2.0, WHITE, 4, center=True)
    pebble(im, 330, 760, 1.4, dark=True)
    if f >= 300: text(im, "NICE.", (330, 560), 1.5, WHITE, 3, center=True)
    return im
def desk(f):
    im = canvas(); cv2.rectangle(im, (0, 760), (W, H), GREY, -1); cv2.line(im, (0, 760), (W, 760), INK, 4, AA)
    groups = [[(300, 0.8), (620, 0.8)], [(940, 0.8), (1260, 0.8)], [(1580, 0.8), (1800, 0.6)]]
    for g, t in zip(groups, (368, 392, 416)):
        if f >= t:
            for x, s in g: mug(im, x, 700, s); steam(im, x, 630, s*0.9)
    return im
def scene5(f):
    if f < 344:
        p = (f-335)/8; p = min(max(p, 0), 1)
        wide = np.hstack([scene4(335), desk(f)])
        x = int(p*W); im = wide[:, x:x+W].copy()
        if 0 < p < 1:
            k = 41; ker = np.zeros((k, k), np.float32); ker[k//2] = 1.0/k
            im = cv2.filter2D(im, -1, ker)
    else: im = desk(f)
    if f >= 344: anchor(im, "T = 1 YEAR")
    return im
def earth(f):
    im = canvas(); cv2.circle(im, (960, 520), 330, INK, 5, AA)
    cv2.ellipse(im, (850, 440), (110, 60), 20, 0, 360, INK, 3, AA); cv2.ellipse(im, (1080, 600), (90, 120), -10, 0, 360, INK, 3, AA)
    mug(im, 960, 180, 0.3, TEAL); cv2.circle(im, (960, 180), 70, TEAL, 2, AA)
    if f >= 456: text(im, "THE WARMEST MUG IN THE SOLAR SYSTEM", (960, 980), 1.5, INK, 3, center=True)
    return im
def scene7(f):
    im = canvas(); pebble(im, 960, 600, 2.4, hold_mug=True)
    if f >= 528: text(im, "I'LL JUST WAIT.", (960, 260), 2.0, INK, 4, center=True)
    return im

def frame(f):
    if f < 72: return scene1(f)
    if f < 144: return scene2(f)
    if f < 240: return scene3(f)
    if f < 336: return scene4(f)
    if f < 432: return scene5(f)
    if f < 504:
        if f < 438:
            a = (f-431)/6; return cv2.addWeighted(desk_end, 1-a, earth(f), a, 0)
        return earth(f)
    return scene7(f)

desk_end = None
desk_end = scene5(431)
for f in range(576): cv2.imwrite(f"{FR}/f{f:04d}.png", frame(f))

E(0,9,"write-on type","Question card text writes on letter-group by letter-group; pebble + empty board static")
E(84,84,"pop-on","Mug pops onto board")
E(108,115,"write-on stroke","Steam lines write on")
E(116,116,"pop-on","Label 85C pops")
E(144,144,"hard cut","New canvas; anchor T = 0 MIN; mug centred")
E(176,176,"state swap","Anchor T = 10 MIN")
E(200,200,"state swap","Anchor T = 1 HOUR")
E(204,204,"pop-on","Label COOLS TO 40C pops")
E(216,223,"write-on stroke","Teal strike-through over COOLS TO 40C")
E(240,240,"hard cut","Dark canvas; glowing mug; anchor T = 1 HOUR")
E(264,264,"pop-on","Label STILL 85C")
E(300,300,"pop-on","Narrator aside NICE.")
E(336,343,"slide/pan with motion blur","Pan right from dark mug scene to desk")
E(344,344,"state swap","Anchor becomes T = 1 YEAR")
E(368,368,"pop-on","Mug group 1 on desk")
E(392,392,"pop-on","Mug group 2 on desk")
E(416,416,"pop-on","Mug group 3 on desk")
E(432,437,"cross-dissolve","Desk to Earth zoom-out with tiny mug")
E(456,456,"pop-on","Label THE WARMEST MUG IN THE SOLAR SYSTEM")
E(504,504,"hard cut","Pebble narrator holding mug")
E(528,528,"pop-on","Aside I'LL JUST WAIT.; hold to frame 575")
with open(f"{D}/RT1_intended_timeline.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["start_frame","end_frame","device","description"]); w.writerows(ev)
subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","24","-i",f"{FR}/f%04d.png","-c:v","libx264","-pix_fmt","yuv420p","-r","24",f"{D}/RT1_animatic.mp4"],check=True)
shutil.rmtree(FR)
