import os, sys, csv, shutil, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(OUT, "frames_tmp")
W, H, FPS, N = 1920, 1080, 50, 1500
BG = (253, 253, 253); INK = (15, 15, 15); YEL = (242, 212, 42); RED = (232, 50, 30)
LW = 13
rng = np.random.default_rng(7)
FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"


S = 1.2


def tp(p):
    return (960 + (p[0] - 960) * S, 540 + (p[1] - 540) * S)


def new():
    return np.full((H, W, 3), BG, np.uint8)


def dense(pts, closed=False, step=22):
    pts = [np.array(p, float) for p in pts]
    if closed:
        pts = pts + [pts[0]]
    out = []
    for a, b in zip(pts[:-1], pts[1:]):
        n = max(1, int(np.linalg.norm(b - a) // step))
        for i in range(n):
            out.append(a + (b - a) * i / n)
    out.append(pts[-1])
    return np.array(out)


def line(img, pts, w=LW, col=INK, closed=False, wob=2.2):
    w = max(3, int(round(w * 0.77)))  # outline calibration: ~12 px measured
    p = dense([tp(q) for q in pts], closed)
    if wob:
        j = rng.normal(0, wob, p.shape)
        j[0] = j[-1] = 0 if not closed else j[0]
        p = p + j
    ip = np.round(p).astype(np.int32)
    cv2.polylines(img, [ip], False, col, w, cv2.LINE_AA)
    for q in (ip[0], ip[-1]):
        cv2.circle(img, tuple(int(v) for v in q), w // 2, col, -1, cv2.LINE_AA)


def poly(img, pts, fill=None, w=LW, col=INK):
    p = dense([tp(q) for q in pts], True)
    if fill is not None:
        cv2.fillPoly(img, [np.round(p).astype(np.int32)], fill, cv2.LINE_AA)
    line(img, pts, w, col, closed=True)


def ell(img, c, rx, ry=None, fill=BG, w=LW, a0=0, a1=360):
    ry = ry or rx
    n = max(14, int((rx + ry) / 9))
    t = np.radians(np.linspace(a0, a1, n, endpoint=(a1 - a0 < 360)))
    pts = [(c[0] + rx * np.cos(x), c[1] + ry * np.sin(x)) for x in t]
    if a1 - a0 >= 360:
        poly(img, pts, fill, w)
    else:
        line(img, pts, w)


def rect(img, x0, y0, x1, y1, fill=BG, w=LW):
    poly(img, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, w)


def dot(img, c, r, col=INK):
    c = tp(c); r = r * S
    cv2.circle(img, (int(c[0]), int(c[1])), int(r), col, -1, cv2.LINE_AA)


def text(img, s, xy, size, col=INK, anchor="mm"):
    xy = tp(xy); size = int(size * S)
    pil = Image.fromarray(img)
    d = ImageDraw.Draw(pil)
    d.text(xy, s, font=ImageFont.truetype(FONT, size), fill=col, anchor=anchor,
           stroke_width=max(1, size // 22), stroke_fill=col)
    img[:] = np.array(pil)


def xmark(img, c, r):
    for s in (1, -1):
        line(img, [(c[0] - r, c[1] - s * r), (c[0] + r, c[1] + s * r)], 36, RED, wob=2)


# ---------------- mascot: Blobbo, a round bean-snail with yellow shell + scarf ----------------
def mascot(img, cx, cy, s=1.0, eyes="open", mouth="smile", arms="down", lie=False, sweat=False):
    R = 190 * s
    # yellow spiral shell on the back
    ell(img, (cx - R * 0.55, cy - R * 0.95), R * 0.62, fill=YEL)
    sp = [(cx - R * 0.55 + R * 0.4 * (t / 9) * np.cos(t * 0.9), cy - R * 0.95 + R * 0.4 * (t / 9) * np.sin(t * 0.9)) for t in np.linspace(0.5, 9, 22)]
    line(img, sp, int(LW * 0.8))
    # body
    ell(img, (cx, cy), R, R * 0.95)
    # little feet
    for dx in (-0.45, 0.45):
        ell(img, (cx + dx * R, cy + R * 0.98), R * 0.2, R * 0.1, fill=BG)
    # scarf (yellow band + tail)
    poly(img, [(cx - R * 0.8, cy + R * 0.42), (cx + R * 0.8, cy + R * 0.42), (cx + R * 0.72, cy + R * 0.7), (cx - R * 0.72, cy + R * 0.7)], YEL)
    poly(img, [(cx + R * 0.45, cy + R * 0.66), (cx + R * 0.75, cy + R * 0.66), (cx + R * 0.8, cy + R * 1.2), (cx + R * 0.5, cy + R * 1.2)], YEL)
    # eyes
    ey = cy - R * 0.25
    for dx in (-0.38, 0.38):
        ex = cx + dx * R
        if eyes == "open":
            dot(img, (ex, ey), 15 * s + 3)
        elif eyes == "closed":
            line(img, [(ex - 28 * s, ey), (ex, ey + 12 * s), (ex + 28 * s, ey)], LW)
        elif eyes == "angry":
            dot(img, (ex, ey + 8), 13 * s + 3)
            line(img, [(ex - 30 * s, ey - 28 * s * (1 if dx < 0 else -1)), (ex + 30 * s, ey - 28 * s * (-1 if dx < 0 else 1) + 0)], LW)
        elif eyes == "wide":
            ell(img, (ex, ey), 26 * s, fill=BG, w=9)
            dot(img, (ex, ey), 10 * s + 2)
    # bulbous nose
    ell(img, (cx, cy + R * 0.02), R * 0.2, R * 0.17, fill=BG)
    # mouth
    my = cy + R * 0.3
    if mouth == "smile":
        ell(img, (cx, my - R * 0.1), R * 0.3, R * 0.17, a0=20, a1=160)
    elif mouth == "o":
        ell(img, (cx, my), R * 0.1, R * 0.12, fill=INK)
    elif mouth == "flat":
        line(img, [(cx - R * 0.2, my), (cx + R * 0.2, my + 4)], LW)
    elif mouth == "frown":
        ell(img, (cx, my + R * 0.2), R * 0.28, R * 0.16, a0=200, a1=340)
    elif mouth == "grin":
        poly(img, [(cx - R * 0.3, my - R * 0.1), (cx + R * 0.3, my - R * 0.1), (cx + R * 0.2, my + R * 0.12), (cx - R * 0.2, my + R * 0.12)], BG)
    if sweat:
        poly(img, [(cx + R * 0.85, cy - R * 0.55), (cx + R * 0.75, cy - R * 0.3), (cx + R * 0.95, cy - R * 0.3)], (120, 190, 240))
    # mitt hands with finger lines
    def mitt(hx, hy):
        ell(img, (hx, hy), 48 * s, 42 * s, fill=BG)
        for k in (-1, 0, 1):
            line(img, [(hx + k * 16 * s, hy - 2 * s), (hx + k * 16 * s, hy - 40 * s)], int(LW * 0.6), wob=0.8)
    if arms == "down":
        for sgn in (-1, 1):
            line(img, [(cx + sgn * R * 0.95, cy + R * 0.1), (cx + sgn * R * 1.25, cy + R * 0.35)], LW)
            mitt(cx + sgn * R * 1.3, cy + R * 0.42)
    elif arms == "up":
        for sgn in (-1, 1):
            line(img, [(cx + sgn * R * 0.95, cy), (cx + sgn * R * 1.35, cy - R * 0.7)], LW)
            mitt(cx + sgn * R * 1.38, cy - R * 0.8)
    elif arms == "hips":
        for sgn in (-1, 1):
            line(img, [(cx + sgn * R * 0.97, cy + R * 0.05), (cx + sgn * R * 1.3, cy + R * 0.3), (cx + sgn * R * 1.0, cy + R * 0.5)], LW)


# ---------------- props ----------------
def calendar(img, x0, y0, cw=200, ch=200, yellow=(), label=True):
    days = "MTWTFSS"
    for i in range(7):
        rect(img, x0 + i * cw, y0, x0 + (i + 1) * cw, y0 + ch, YEL if i in yellow else BG)
        if label:
            text(img, days[i], (x0 + i * cw + cw / 2, y0 + ch / 2), 120)


def hammer(img, x, y, s=1.0, ang=-30):
    a = np.radians(ang)
    d = np.array([np.sin(a), -np.cos(a)])
    nrm = np.array([np.cos(a), np.sin(a)])
    base = np.array([x, y]); tip = base + d * 260 * s
    line(img, [base, tip], 28)
    h = [tip - nrm * 90 * s + d * 20 * s, tip + nrm * 90 * s + d * 20 * s, tip + nrm * 90 * s - d * 60 * s, tip - nrm * 90 * s - d * 60 * s]
    poly(img, h, (170, 170, 170))


def pickaxe(img, x, y):
    line(img, [(x - 130, y + 170), (x + 130, y - 170)], 28)
    ell(img, (x + 130, y - 170), 190, 130, fill=BG, a0=200, a1=340)
    ell(img, (x + 130, y - 170), 150, 90, fill=BG, a0=200, a1=340)


def clock(img, c, r):
    ell(img, c, r)
    line(img, [c, (c[0], c[1] - r * 0.6)], LW + 3)
    line(img, [c, (c[0] + r * 0.45, c[1] + r * 0.2)], LW + 3)
    dot(img, c, 14)


def coins(img, x, y):
    for i, (dx, dy) in enumerate([(0, 0), (150, 20), (75, -120)]):
        ell(img, (x + dx, y + dy), 80, fill=YEL)
        text(img, "$", (x + dx, y + dy), 90)


def sun(img, c, r):
    ell(img, c, r, fill=YEL)
    for k in range(10):
        a = k * 2 * np.pi / 10
        line(img, [(c[0] + np.cos(a) * (r + 25), c[1] + np.sin(a) * (r + 25)), (c[0] + np.cos(a) * (r + 90), c[1] + np.sin(a) * (r + 90))], LW + 3)


def chair(img, x, y):
    line(img, [(x, y), (x + 150, y + 190)], 22)
    line(img, [(x + 150, y + 190), (x + 330, y + 190)], 22)
    line(img, [(x, y), (x + 200, y + 40), (x + 330, y + 190)], 22)
    line(img, [(x + 40, y + 190), (x + 40, y + 280)], 22)
    line(img, [(x + 300, y + 190), (x + 300, y + 280)], 22)


def ball(img, c, r):
    ell(img, c, r)
    poly(img, [(c[0] + r * 0.4 * np.cos(a), c[1] + r * 0.4 * np.sin(a)) for a in np.radians(np.arange(-90, 270, 72))], INK, w=6)


def heart(img, c, s):
    pts = []
    for t in np.linspace(0, 2 * np.pi, 40):
        pts.append((c[0] + s * 16 * np.sin(t) ** 3, c[1] - s * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))))
    poly(img, pts, RED)


def alarm(img, c, r, ring=True):
    ell(img, (c[0] - r * 0.75, c[1] - r * 0.9), r * 0.32, fill=YEL)
    ell(img, (c[0] + r * 0.75, c[1] - r * 0.9), r * 0.32, fill=YEL)
    ell(img, c, r, fill=BG)
    line(img, [c, (c[0], c[1] - r * 0.6)], LW + 3)
    line(img, [c, (c[0] + r * 0.4, c[1] + r * 0.1)], LW + 3)
    line(img, [(c[0] - r * 0.6, c[1] + r * 0.95), (c[0] - r * 0.85, c[1] + r * 1.25)], LW + 3)
    line(img, [(c[0] + r * 0.6, c[1] + r * 0.95), (c[0] + r * 0.85, c[1] + r * 1.25)], LW + 3)
    if ring:
        for sgn in (-1, 1):
            for k in (0, 1):
                line(img, [(c[0] + sgn * (r * 1.3 + k * 50), c[1] - 60 + k * 50), (c[0] + sgn * (r * 1.45 + k * 50), c[1] + 10 + k * 50)], 10)


def factory(img, x, y):
    poly(img, [(x, y), (x, y - 200), (x + 130, y - 120), (x + 130, y - 200), (x + 260, y - 120), (x + 260, y - 200), (x + 390, y - 120), (x + 390, y)], BG)
    for k in range(4):
        rect(img, x + 30 + k * 90, y - 90, x + 85 + k * 90, y - 35, YEL, 9)
    rect(img, x + 300, y - 380, x + 360, y - 200, BG)
    for i, (dx, dy, r) in enumerate([(340, -430, 40), (390, -500, 52), (460, -590, 66)]):
        ell(img, (x + dx, y + dy), r, fill=BG, w=10)


def bed(img, x0, y0, x1):
    rect(img, x0, y0, x1, y0 + 150, BG)
    rect(img, x0 - 30, y0 - 230, x0 + 10, y0 + 230, BG)
    rect(img, x1 - 10, y0 + 30, x1 + 30, y0 + 230, BG)
    poly(img, [(x0 + 260, y0 - 20), (x1, y0 - 20), (x1, y0 + 150), (x0 + 260, y0 + 150)], YEL)
    line(img, [(x0 + 260, y0 + 20), (x1, y0 + 20)], 8)


def zzz(img, x, y):
    for i, sz in enumerate((90, 130, 180)):
        text(img, "Z", (x + i * 120, y - i * 150), sz)


# ---------------- states ----------------
def blank():
    return new()


def s_mascot_q():
    i = new(); mascot(i, 800, 640, 1.5, eyes="wide", mouth="o", arms="up"); text(i, "?", (1450, 480), 420); return i


WORDS = ["WHY", "WEEKENDS", "EXIST?"]


def s_words(k):
    global S
    S = 1.0
    i = new()
    full = " ".join(WORDS)
    sz = 140
    f = ImageFont.truetype(FONT, sz)
    wfull = ImageDraw.Draw(Image.new("RGB", (10, 10))).textlength(full, font=f)
    assert wfull <= 0.9 * W, wfull
    x = 960 - wfull / 2
    shown = " ".join(WORDS[:k])
    # reserve blank space for upcoming words: draw left-anchored at fixed x
    text(i, shown, (x, 540), sz, anchor="lm")
    return i


def s_calendar_peek():
    i = new(); calendar(i, 280, 480, yellow=(5, 6)); mascot(i, 560, 250, 0.85, eyes="wide", mouth="o"); return i


def s_pick():
    i = s_calendar_peek(); pickaxe(i, 1560, 250); return i


def s_bed():
    i = new(); bed(i, 360, 780, 1500); mascot(i, 700, 720, 1.5, eyes="closed", mouth="flat", arms="hips"); zzz(i, 1100, 480); return i


def s_allwork():
    i = new(); calendar(i, 280, 600, cw=200, ch=200, label=False)
    for k in range(7):
        hammer(i, 280 + k * 200 + 100, 760, 0.45, -25)
    mascot(i, 960, 300, 1.15, eyes="angry", mouth="frown", sweat=True, arms="hips"); return i


def s_allwork_x():
    i = s_allwork(); xmark(i, (960, 700), 330); return i


def s_tablet():
    i = new(); poly(i, [(560, 140), (1360, 140), (1360, 820), (560, 820)], BG); sun(i, (1040, 340), 80)
    text(i, "1", (960, 600), 400); text(i, "DAY OFF", (960, 770), 110)
    mascot(i, 330, 760, 0.9, eyes="open", mouth="smile", arms="up"); return i


def s_factory():
    i = new(); factory(i, 760, 900); return i


def s_money():
    i = new(); clock(i, (560, 480), 260); text(i, "=", (1010, 480), 260); coins(i, 1250, 500)
    return i


def s_two():
    i = new(); mascot(i, 760, 640, 1.8, eyes="open", mouth="grin", arms="up"); text(i, "2", (1560, 560), 700); return i


def s_cal52():
    i = new(); calendar(i, 280, 400, yellow=(5, 6)); text(i, "5 + 2", (960, 200), 150); text(i, "WORK  REST", (960, 800), 110); return i


def s_beach():
    i = s_cal52(); i[:] = new()
    sun(i, (1500, 230), 130); chair(i, 560, 640); line(i, [(200, 940), (1720, 940)], 20)
    mascot(i, 460, 680, 0.0001); return i


def s_beach2():
    i = new(); sun(i, (1500, 230), 130); chair(i, 1000, 600); line(i, [(330, 930), (1590, 930)], 20)
    mascot(i, 520, 640, 1.5, eyes="closed", mouth="smile", arms="up"); return i


def s_family():
    i = new(); ball(i, (560, 560), 260); heart(i, (1300, 520), 26); return i


def s_monday():
    i = new(); alarm(i, (700, 520), 260); text(i, "MON", (1450, 520), 300); return i


def s_sleepalarm():
    i = new(); alarm(i, (1300, 640), 200, ring=False); bed(i, 260, 780, 1100)
    mascot(i, 600, 730, 1.3, eyes="closed", mouth="flat"); zzz(i, 820, 480); return i


def s_hide():
    i = new(); calendar(i, 280, 560, yellow=(5, 6)); ell(i, (280 + 100, 660), 120, fill=BG, w=LW)
    ell(i, (380, 660), 150, 150, fill=BG, w=LW, a0=0, a1=360)
    text(i, "MON", (380, 660), 95); return i


def s_peek():
    i = new(); mascot(i, 960, 600, 1.5, eyes="angry", mouth="frown", arms="hips"); return i


def s_final():
    i = new(); bed(i, 300, 800, 1500); mascot(i, 780, 750, 1.5, eyes="closed", mouth="smile", arms="hips")
    text(i, "5 MORE MINUTES", (960, 180), 200); zzz(i, 1180, 640); return i


# ---------------- timeline ----------------
T = [
    (0, "blank", "blank white canvas beat (frame 0 = #FDFDFD)", blank),
    (40, "scene_swap", "mascot Blobbo startled with giant question mark", s_mascot_q),
    (100, "text_build_word1", "word 1 WHY pops (space reserved for next words; line text only)", lambda: s_words(1)),
    (140, "text_build_word2", "word 2 WEEKENDS pops", lambda: s_words(2)),
    (180, "text_build_word3", "word 3 EXIST? pops", lambda: s_words(3)),
    (240, "scene_swap", "week calendar M-S, weekend boxes yellow, mascot peeks over", s_calendar_peek),
    (310, "pop_on_literal", "literal picture of WORK: pickaxe pops on", s_pick),
    (370, "scene_swap_literal", "literal picture of REST: mascot asleep in bed with Zzz", s_bed),
    (440, "scene_swap", "all 7 days filled with hammers, mascot angry and sweating", s_allwork),
    (500, "red_x_negation", "red X pops over the 7-day workweek", s_allwork_x),
    (560, "dip_out", "dip to white, 8 frames out", None),
    (568, "dip_in", "dip in from white, 8 frames, to tablet: 1 DAY OFF", None),
    (650, "pop_on", "factory building pops (factory era), no yellow", s_factory),
    (710, "scene_swap_literal", "literal: time = money (clock = coins), line only", s_money),
    (770, "scene_swap", "mascot cheers beside giant 2 (two days)", s_two),
    (830, "scene_swap", "5 + 2 calendar, work vs rest labels, text and boxes only", s_cal52),
    (900, "scene_swap", "literal weekend rest: sun, beach chair, mascot happy", s_beach2),
    (960, "pop_on", "ball and red heart alone: play and family", s_family),
    (1020, "scene_swap", "big MON text with ringing alarm, black line only", s_monday),
    (1090, "scene_swap", "mascot asleep in bed, alarm silent", s_sleepalarm),
    (1170, "scene_swap", "MON badge circle over calendar, line only", s_hide),
    (1250, "pose_swap", "mascot angry stare, hands on hips", s_peek),
    (1350, "final_joke", "mascot asleep: 5 MORE MINUTES (final hold, no end card)", s_final),
]


def noyel(fn):
    def g():
        global YEL
        old = YEL; YEL = BG
        try:
            return fn()
        finally:
            YEL = old
    return g


NOY = {100, 140, 180, 650, 710, 830, 960, 1020, 1170}


def main():
    global S
    if os.path.exists(FR):
        shutil.rmtree(FR)
    os.makedirs(FR)
    starts = [t[0] for t in T] + [N]
    states = {}
    for st, dev, d, fn in T:
        if fn:
            S = 1.0 if st in (100, 140, 180) else 1.2
            states[st] = (noyel(fn) if st in NOY else fn)()
    ink = []
    # dip bookkeeping
    last_before = states[500]
    after = states[650 - 0] if False else None
    tablet = s_tablet()
    ny = [(np.abs(im.astype(int) - np.array(YEL)[None, None]).sum(2) < 40).any() for im in list(states.values()) + [tablet]]
    for k, im in states.items():
        ys, xs = np.where(np.abs(im.astype(int) - 253).sum(2) > 30)
        if len(xs) and (xs.min() < 96 or xs.max() > 1824 or ys.min() < 54 or ys.max() > 1026):
            print('OUT OF SAFE', k, xs.min(), xs.max(), ys.min(), ys.max())
    print("yellow in %d of %d held states" % (sum(ny), len(ny)))
    states[568] = tablet
    for fi in range(N):
        k = max(j for j, s in enumerate(starts[:-1]) if s <= fi)
        st = starts[k]
        if 560 <= fi < 568:
            t = (fi - 559) / 8
            img = (last_before * (1 - t) + np.array(BG, float) * t).round().astype(np.uint8)
        elif 568 <= fi < 576:
            t = (fi - 567) / 8
            img = (tablet * t + np.array(BG, float) * (1 - t)).round().astype(np.uint8)
        elif 576 <= fi < 650:
            img = tablet
        else:
            img = states[st]
        cv2.imwrite(os.path.join(FR, f"f{fi:05d}.png"), img[:, :, ::-1])
    # timeline csv + ink
    with open(os.path.join(OUT, "intended_timeline.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["start_frame", "end_frame", "device", "description"])
        for k, (st, dev, d, fn) in enumerate(T):
            w.writerow([st, starts[k + 1] - 1, dev, d])
            if fn:
                im = states[st]; ink.append((im.mean(axis=2) < 70).mean())
    print("mean ink coverage held states: %.3f" % np.mean(ink[1:]))
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(FR, "f%05d.png"),
                           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS), "-fps_mode", "cfr", "-crf", "14",
                           os.path.join(OUT, "render.mp4")])
    shutil.rmtree(FR)


if __name__ == "__main__":
    main()
