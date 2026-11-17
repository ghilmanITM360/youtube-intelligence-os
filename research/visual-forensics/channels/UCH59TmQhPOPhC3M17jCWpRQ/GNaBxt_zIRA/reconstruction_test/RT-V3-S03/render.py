import json, subprocess, numpy as np, cv2, sys
from PIL import Image, ImageDraw, ImageFont
W, H, N = 1920, 1080, 179
FONT = "/System/Library/Fonts/Supplemental/SnellRoundhand.ttc"
SPEC = json.load(open("SPEC_GIVEN_TO_WORKER.json"))
tab = {int(k): v for k, v in SPEC["camera_scale_table"].items()}
ks = sorted(tab)
scale = lambda i: float(np.interp(i, ks, [tab[k] for k in ks]))
def c(h):  # hex rgb -> bgra
    h = h.lstrip('#'); return (int(h[4:6],16), int(h[2:4],16), int(h[0:2],16), 255)
INK, WALL, WOOD, BOARD = c('#101010'), c('#c89858'), c('#683818'), c('#485428')
SKIN, PAPER, STONE, STONE2, WHITE, FUR = c('#e0b080'), c('#e8d8a8'), c('#9a9484'), c('#7c7668'), c('#f0ece0'), c('#a06830')
FLOOR, WOOD2 = c('#b48444'), c('#82502a')

class Cv:
    def __init__(s, img, S, ox=0, oy=0, w=4, seed=0):
        s.img, s.S, s.ox, s.oy, s.w, s.r = img, S, ox, oy, w, np.random.RandomState(seed)
    def P(s, pts, j=0.8):
        a = np.array(pts, float) + s.r.normal(0, j, (len(pts), 2))
        return np.round(a * s.S + [s.ox, s.oy]).astype(np.int32)
    def sub(s, pts, closed):
        out = []; n = len(pts)
        for i in range(n if closed else n - 1):
            a, b = np.array(pts[i], float), np.array(pts[(i+1) % n], float)
            m = max(1, int(np.hypot(*(b-a)) // 25))
            out += [a + (b-a)*t/m for t in range(m)]
        if not closed: out.append(np.array(pts[-1], float))
        return out
    def line(s, pts, w=None, col=INK, closed=False):
        p = s.P(s.sub(pts, closed)); w = w or s.w
        for i in range(len(p) - (0 if closed else 1)):
            t = max(1, int(round(w * s.S * s.r.uniform(.85, 1.2))))
            a, b = p[i], p[(i+1) % len(p)]
            cv2.line(s.img, tuple(map(int,a)), tuple(map(int,b)), col, t, cv2.LINE_AA)
            cv2.circle(s.img, tuple(map(int,a)), t//2, col, -1, cv2.LINE_AA)
    def shape(s, pts, fill, w=None):
        cv2.fillPoly(s.img, [s.P(s.sub(pts, True), 0.6)], fill, cv2.LINE_AA)
        s.line(pts, w, closed=True)
    def rect(s, x, y, w_, h_, fill, w=None): s.shape([(x,y),(x+w_,y),(x+w_,y+h_),(x,y+h_)], fill, w)
    def ell(s, cx, cy, rx, ry, fill, w=None):
        t = np.linspace(0, 2*np.pi, 40, endpoint=False)
        s.shape([(cx+rx*np.cos(a), cy+ry*np.sin(a)) for a in t], fill, w)
    def thick(s, a, b, wd, fill):  # outlined limb
        s.line([a, b], wd + 2*s.w, INK); s.line([a, b], wd, fill)

def noise(h, w, seed, amp, sig=1.3):
    n = np.random.RandomState(seed).normal(0, 1, (h, w)).astype(np.float32)
    n = cv2.GaussianBlur(n, (0, 0), sig); return n / n.std() * amp

# ---------------- background (canvas coords 1920x1080, drawn at 2x) ----------------
def make_bg():
    S = 2; img = np.zeros((H*S, W*S, 4), np.uint8); img[:] = WALL
    d = Cv(img, S, seed=1, w=4)
    img[700*S:] = FLOOR
    d.line([(0,700),(1920,700)], 4)
    for x in range(-40, 1920, 170):  # plaster block lines on wall
        d.line([(x,40),(x+8,300)], 1.5, c('#b88848'))
    # posters
    d.rect(190, 95, 210, 215, PAPER); d.ell(295, 190, 42, 42, c('#e8b838'))
    for a in np.linspace(0, 2*np.pi, 10, endpoint=False):
        d.line([(295+52*np.cos(a),190+52*np.sin(a)),(295+72*np.cos(a),190+72*np.sin(a))], 3)
    d.rect(1425, 95, 150, 215, PAPER)
    d.line([(1450,190),(1500,170),(1545,200),(1500,225),(1450,190)], 4)  # fish
    d.line([(1450,190),(1435,170)], 4); d.line([(1450,190),(1435,212)], 4); d.ell(1515,190,4,4,INK,2)
    for x in (1458,1475,1492): d.line([(x,255),(x+14,270),(x+28,255)], 3)
    # chalkboard
    d.rect(540, 38, 840, 345, WOOD, 5)
    bm = np.zeros((H*S, W*S), np.uint8)
    d.rect(562, 62, 796, 298, BOARD, 5)
    cv2.rectangle(bm, (566*S,66*S), (1354*S,356*S), 255, -1)
    d.rect(530, 380, 860, 22, WOOD, 5); d.rect(600, 372, 40, 8, WHITE, 3)
    sm = np.zeros((H*S, W*S), np.float32); r = np.random.RandomState(5)
    for _ in range(16):
        cv2.ellipse(sm, (int(r.uniform(580,1340)*S), int(r.uniform(80,350)*S)), (int(r.uniform(30,110)*S), int(r.uniform(10,30)*S)),
                    r.uniform(0,180), 0, 360, float(r.choice([-1, 1]))*r.uniform(.4,1), -1)
    sm = cv2.GaussianBlur(sm, (0,0), 28) * 14 * (bm > 0)
    # desks
    def desk(x, y, w):
        h = int(w*.12)
        for lx in (x+w*.08, x+w*.84): d.rect(lx, y+h, w*.08, w*.55, WOOD2)
        d.rect(x, y, w, h, WOOD); d.rect(x+w*.1, y+h, w*.8, h*.8, WOOD2)
        sx = x + w*.5; sy = y + w*.62
        for off in (-.22, .22): d.line([(sx+off*w*.8, sy), (sx+off*w, sy+w*.35)], 5)
        d.ell(sx, sy, w*.2, w*.06, WOOD)
        d.line([(x+w*.1,y+h*.5),(x+w*.9,y+h*.5)], 1.6, c('#401c08'))
    for row, (y, w, xs) in enumerate([(640, 130, range(330, 1500, 260)), (770, 190, range(180, 1700, 360)), (930, 270, range(60, 1700, 520))]):
        for x in xs: desk(x + (row%2)*60, y, w)
    img[..., :3] = np.clip(img[..., :3].astype(np.float32) + noise(H*S, W*S, 11, 4.5)[..., None] + sm[..., None], 0, 255)
    # text via PIL
    pil = Image.fromarray(img[..., :3][..., ::-1].copy()); dr = ImageDraw.Draw(pil)
    for (cx, cy, t, sz) in [(295, 285, "sun", 40), (1500, 292, "fish", 40)]:
        f = ImageFont.truetype(FONT, sz*S, index=1); dr.text((cx*S, cy*S), t, font=f, fill=(30,20,10), anchor="mm")
    txt, tw = "topic: sabre cat", 480*S
    sz = 100
    while ImageDraw.Draw(Image.new('L',(1,1))).textlength(txt, font=ImageFont.truetype(FONT, sz, index=1)) < tw: sz += 4
    f = ImageFont.truetype(FONT, sz, index=1)
    m = Image.new('L', (W*S, H*S), 0); ImageDraw.Draw(m).text((960*S, 215*S), txt, font=f, fill=255, anchor="mm")
    m = np.array(m, np.float32) / 255
    m = cv2.dilate(m, np.ones((3,3))) * np.clip(0.88 + noise(H*S, W*S, 3, .12, .8), .55, 1)
    out = np.array(pil)[..., ::-1].astype(np.float32)
    out = out * (1 - m[..., None]) + np.array([232, 238, 240], np.float32) * m[..., None]
    out = cv2.GaussianBlur(out, (0,0), 0.8)
    bb = np.argwhere(m > .3); print("text bbox canvas x", bb[:,1].min()/S, bb[:,1].max()/S, "y", bb[:,0].min()/S, bb[:,0].max()/S)
    return np.clip(out, 0, 255).astype(np.uint8)

# ---------------- teacher sprite (units: head height 220 at k=1; rendered R=2) ----------------
R, OX, OY, SW, SH = 2, 460, 200, 720, 1000
POSES = {0: ((-120,175),(-150,40)), 1: ((-150,110),(-260,-10)), 2: ((-150,80),(-245,-105)),
         3: ((-155,75),(-285,-112)), 4: ((-145,85),(-215,-118)), 5: ((-160,78),(-320,-108))}
_cache = {}
def sprite(pose, mouth):
    if (pose, mouth) in _cache: return _cache[(pose, mouth)]
    img = np.zeros((SH*R, SW*R, 4), np.uint8)
    d = Cv(img, R, OX*R/R, OY*R/R, w=4.5, seed=7)  # offsets in px below
    d.ox, d.oy = OX*R, OY*R
    d.shape([(-75,90),(75,90),(160,215),(-160,215)], FUR)
    d.line([(-30,100),(0,150),(30,100)], 3)
    d.shape([(-200,190),(190,190),(190,232),(-200,232)], STONE)  # lectern top
    d.shape([(-170,232),(165,232),(165,780),(-170,780)], STONE2)
    for y in range(300, 780, 90):
        d.line([(-170,y),(165,y)], 3, c('#585244')); d.line([(-60+(y%180),y),(-60+(y%180),y+90)], 3, c('#585244'))
    d.ell(-86, 5, 14, 24, SKIN); d.ell(86, 5, 14, 24, SKIN)
    d.ell(0, 0, 85, 110, SKIN)
    for sx in (-1, 1):  # side wisps, brows, eyes
        d.shape([(sx*80,-30),(sx*112,-10),(sx*100,40),(sx*82,30)], WHITE, 3.5)
        d.shape([(sx*15,-32),(sx*60,-48),(sx*66,-30),(sx*20,-20)], WHITE, 3.5)
        d.ell(sx*38, -8, 6, 8, INK, 2)
    d.ell(-4, 22, 24, 18, c('#d09870'))
    d.shape([(-4,40),(-90,36),(-118,95),(-112,175),(-90,172),(-56,105),(-4,70)], WHITE)
    d.shape([(4,40),(90,36),(118,95),(112,175),(90,172),(56,105),(4,70)], WHITE)
    if mouth: d.ell(0, 82, 20, 14, c('#702020'), 3)
    else: d.line([(-16,80),(16,80)], 4)
    (hx, hy), (tx, ty) = POSES[pose]
    d.thick((-100,160), (hx,hy), 26, FUR)
    d.line([(hx,hy),(tx,ty)], 4+4, INK); d.line([(hx,hy),(tx,ty)], 3, c('#c8a060'))
    d.ell(hx, hy, 15, 15, SKIN, 3.5)
    img[..., :3] = np.clip(img[..., :3].astype(np.float32) + noise(SH*R, SW*R, 21, 4)[..., None], 0, 255)  # static layer texture
    a = img[..., 3:4].astype(np.float32) / 255
    img[..., :3] = (img[..., :3] * a).astype(np.uint8)  # premultiply
    _cache[(pose, mouth)] = img; return img

def pose_at(i):
    if i < 64: return 0
    for a, b, p in [(72,73,2),(96,97,3),(120,121,4),(146,147,5)]:
        if a <= i <= b: return p
    return 1
def mouth_at(i): return int(i >= 12 and (i // 6) % 2 == 1)

def main():
    bg = make_bg(); cv2.imwrite("bg_debug.png", bg[:, :, :]) if False else None
    s58 = scale(58); tl = {"camera_push": [8, 58], "pointer_pose_changes": [], "mouth_open_runs": [], "frames": []}
    ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r","30000/1001","-i","-",
        "-frames:v",str(N),"-c:v","libx264","-preset","slow","-crf","14","-pix_fmt","yuv420p","-r","30000/1001","-movflags","+faststart","rt.mp4"], stdin=subprocess.PIPE)
    prev = None
    for i in range(N):
        s = scale(i)
        M = np.float32([[s/2,0,960-960*s],[0,s/2,50-50*s]])
        fr = cv2.warpAffine(bg, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)[..., :3]
        p = float(np.clip((s-1)/(s58-1), 0, 1)); k = 1 + .45*p; px, py = 1700 - 60*p, 380 + 90*p
        sp = sprite(pose_at(i), mouth_at(i))
        T = np.float32([[k/R,0,px-OX*k],[0,k/R,py-OY*k]])
        t = cv2.warpAffine(sp, T, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        a = t[..., 3:4].astype(np.float32) / 255
        out = np.clip(t[..., :3] + fr.astype(np.float32) * (1 - a), 0, 255).astype(np.uint8)
        ff.stdin.write(out.tobytes())
        if i in (0, 30, 58, 100, 178): cv2.imwrite(f"check_f{i}.png", out)
        pm = (pose_at(i), mouth_at(i))
        if prev and prev[0] != pm[0]: tl["pointer_pose_changes"].append({"frame": i, "pose": pm[0]})
        if prev and prev[1] != pm[1]: tl["mouth_open_runs"].append({"frame": i, "open": bool(pm[1])})
        prev = pm
        tl["frames"].append({"i": i, "scale": round(s, 5), "teacher_k": round(k, 4), "teacher_head": [round(px,1), round(py,1)]})
    ff.stdin.close(); ff.wait()
    tl["note"] = "pose0 held-down f0-63; lift (pose1) f64; taps: f72-73 p2, f96-97 p3, f120-121 p4, f146-147 p5; else pose1. Cut at f0, push f8-58 per table."
    json.dump(tl, open("timeline.json", "w"), indent=1)
main()
