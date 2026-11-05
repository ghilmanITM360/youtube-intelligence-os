#!/usr/bin/env python
# RT_P1: "Why do alarm clocks exist?" 1000-frame 1080x1920 50fps animatic. Deterministic.
import os, csv, shutil, subprocess, math
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(HERE, "frames_tmp")
W, H = 1080, 1920
BG = (253, 253, 253); INK = (22, 22, 22); YEL = (42, 212, 242); RED = (30, 50, 232)
RNG = np.random.default_rng(7)
def seed(n):
    global RNG; RNG = np.random.default_rng(n)

def _wob(pts, closed):
    p = np.array(pts, float)
    if closed: p = np.vstack([p, p[:1]])
    out = []
    for a, b in zip(p[:-1], p[1:]):
        n = max(1, int(np.hypot(*(b - a)) / 18))
        out.append(np.linspace(a, b, n, endpoint=False))
    out.append(p[-1:]); q = np.vstack(out)
    off = RNG.normal(0, 2.4, q.shape)
    k = np.array([.25, .5, .25])
    for _ in range(2):
        off = np.stack([np.convolve(np.pad(off[:, i], 1, mode="edge"), k, "valid") for i in (0, 1)], 1)
    q = q + off * 1.6
    if closed: q[-1] = q[0]
    return q

def _sh(q): return (np.asarray(q) * 16).astype(np.int32)

def stroke(img, pts, w=16, closed=False, color=INK, fill=None):
    q = _wob(pts, closed)
    if fill is not None: cv2.fillPoly(img, [_sh(q).reshape(-1, 1, 2)], fill, cv2.LINE_AA, 4)
    cv2.polylines(img, [_sh(q).reshape(-1, 1, 2)], False, color, w, cv2.LINE_AA, 4)
    for e in ([q[0], q[-1]]):
        cv2.circle(img, tuple(_sh(e)), int(w / 2 * 16), color, -1, cv2.LINE_AA, 4)

def ell(cx, cy, rx, ry, a0=0, a1=360, n=48):
    t = np.radians(np.linspace(a0, a1, n))
    return list(zip(cx + rx * np.cos(t), cy + ry * np.sin(t)))

def blob(img, cx, cy, rx, ry, fill=BG, w=16):
    stroke(img, ell(cx, cy, rx, ry, 0, 360, 40)[:-1], w, True, fill=fill)

def dot(img, x, y, r):
    cv2.circle(img, (int(x * 16), int(y * 16)), int(r * 16), INK, -1, cv2.LINE_AA, 4)

def text(img, s, cx, base, scale, th=20, color=INK, maxw=940):
    f = cv2.FONT_HERSHEY_SIMPLEX
    (tw, _), _ = cv2.getTextSize(s, f, scale, th)
    if tw > maxw: scale *= maxw / tw; (tw, _), _ = cv2.getTextSize(s, f, scale, th)
    cv2.putText(img, s, (int(cx - tw / 2), int(base)), f, scale, color, th, cv2.LINE_AA)

def zzz(img, x, y):
    for dx, dy, z in [(0, 0, 40), (50, -70, 56), (115, -160, 74)]:
        stroke(img, [(x + dx, y + dy), (x + dx + z, y + dy), (x + dx, y + dy + z), (x + dx + z, y + dy + z)], 13)

def mascot(img, cx, cy, s=1.0, pose="awake"):
    seed(100)
    t = np.linspace(0, 2 * np.pi, 72, endpoint=False)
    body = list(zip(cx + 190 * s * np.cos(t) * (1 + .12 * np.sin(t)), cy + 230 * s * np.sin(t)))
    for sx in (-1, 1): blob(img, cx + sx * 95 * s, cy + 232 * s, 58 * s, 28 * s)   # feet
    stroke(img, body, 16, True, fill=BG)
    # scarf (yellow) + tail
    stroke(img, [(cx + 95 * s, cy + 30 * s), (cx + 150 * s, cy + 150 * s), (cx + 105 * s, cy + 165 * s), (cx + 62 * s, cy + 45 * s)], 14, True, fill=YEL)
    stroke(img, ell(cx, cy + 12 * s, 168 * s, 40 * s, 0, 360, 40)[:-1], 16, True, fill=YEL)
    # hands (mitts with finger lines)
    up = pose in ("shocked", "yawn")
    for sx in (-1, 1):
        hx, hy = cx + sx * (235 if up else 215) * s, cy + (-110 if up else 80) * s
        stroke(img, [(cx + sx * 175 * s, cy + (-40 if up else 40) * s), (hx - sx * 25 * s, hy + (30 if up else -10) * s)], 18)
        blob(img, hx, hy, 44 * s, 44 * s)
        for a in (-25, 15): stroke(img, [(hx + sx * 8 * s, hy + a * s), (hx + sx * 40 * s, hy + (a + 4) * s)], 8)
    # face
    for sx in (-1, 1):
        ex, ey = cx + sx * 62 * s, cy - 150 * s
        if pose == "sleep": stroke(img, ell(ex, ey - 8 * s, 28 * s, 16 * s, 20, 160, 10), 11)
        elif pose == "shocked": blob(img, ex, ey, 26 * s, 26 * s, w=9); dot(img, ex, ey, 7 * s)
        elif pose == "yawn": stroke(img, [(ex - 24 * s, ey - 8 * s), (ex + 24 * s, ey + 8 * s * sx)], 11)
        else: dot(img, ex, ey, 14 * s)
    if pose == "grumpy":
        for sx in (-1, 1): stroke(img, [(cx + sx * 100 * s, cy - 205 * s), (cx + sx * 30 * s, cy - 180 * s)], 11)
    blob(img, cx, cy - 98 * s, 34 * s, 30 * s)                                       # bulbous nose
    my = cy - 48 * s
    if pose == "sleep": blob(img, cx, my, 12 * s, 9 * s, w=8)
    elif pose in ("yawn", "shocked"): blob(img, cx, my + 2 * s, 30 * s, 26 * s, fill=INK, w=6)
    elif pose == "sad":
        stroke(img, ell(cx, my + 24 * s, 34 * s, 22 * s, 200, 340, 10), 9)
        stroke(img, [(cx + 90 * s, cy - 130 * s), (cx + 100 * s, cy - 100 * s), (cx + 88 * s, cy - 84 * s), (cx + 78 * s, cy - 100 * s)], 8, True)
    elif pose == "grumpy": stroke(img, [(cx - 30 * s, my), (cx + 30 * s, my)], 9)
    else: stroke(img, ell(cx, my - 10 * s, 36 * s, 22 * s, 20, 160, 10), 9)

def clock(img, cx, cy, r, hh=300, mm=0, ring=False, yel=True):
    seed(200); bf = YEL if yel else BG
    for sx in (-1, 1):
        blob(img, cx + sx * .72 * r, cy - .78 * r, .3 * r, .26 * r, fill=bf)
        stroke(img, [(cx + sx * .55 * r, cy + .85 * r), (cx + sx * .78 * r, cy + 1.18 * r)], 18)
    stroke(img, [(cx, cy - r), (cx, cy - 1.18 * r)], 14)
    blob(img, cx, cy, r, r)
    for a, n in ((0, "12"), (90, "3"), (180, "6"), (270, "9")):
        d = np.radians(a)
        if r > 150: text(img, n, cx + .68 * r * math.sin(d), cy - .68 * r * math.cos(d) + r * .12, r / 150, 10)
    for ang, L in ((hh, .42), (mm, .6)):
        d = np.radians(ang); stroke(img, [(cx, cy), (cx + L * r * math.sin(d), cy - L * r * math.cos(d))], 16)
    dot(img, cx, cy, 16)
    if ring:
        for sx in (-1, 1):
            for a in (35, 60, 85):
                d = np.radians(a)
                stroke(img, [(cx + sx * 1.22 * r * math.sin(d), cy - 1.22 * r * math.cos(d)), (cx + sx * 1.4 * r * math.sin(d), cy - 1.4 * r * math.cos(d))], 12)

def coins(img, x, base):
    seed(300)
    for k in range(4):
        y = base - 60 * k
        stroke(img, [(x - 150, y), (x + 150, y), (x + 150, y + 40), (x - 150, y + 40)], 1, True, color=BG, fill=BG)
        for sx in (-1, 1): stroke(img, [(x + sx * 150, y), (x + sx * 150, y + 40)], 14)
        for j in range(-4, 5): stroke(img, [(x + j * 30, y + 52), (x + j * 30, y + 72)], 9)
        stroke(img, ell(x, y + 40, 150, 42, 0, 180, 24), 14)
        blob(img, x, y, 150, 42, fill=BG, w=14)
    text(img, "$", x, base - 180 + 22, 2.4, 12)


def rooster(img):
    seed(400)
    stroke(img, [(60, 1500), (1020, 1500)], 14)
    for x in range(90, 1000, 60): stroke(img, [(x, 1500), (x + 14, 1540)], 10)       # grass ticks
    for sx in (-1, 1): stroke(img, [(480 + sx * 60, 1280), (480 + sx * 70, 1480)], 16)
    for a in (-35, 0, 35):
        d = np.radians(a); blob(img, 240 - 40 * math.cos(d), 1050 + 140 * math.sin(d), 120, 60)
    blob(img, 480, 1130, 240, 170)
    stroke(img, ell(450, 1130, 120, 80, 200, 340, 12), 12)
    for k in range(4): stroke(img, [(400 + 40 * k, 1190), (420 + 40 * k, 1240)], 12)  # belly hatching
    stroke(img, [(640, 1060), (700, 900)], 18)
    blob(img, 700, 840, 100, 100)
    for i in range(3): blob(img, 650 + 50 * i, 735 + (12 if i == 1 else 0), 30, 38, w=14)
    stroke(img, [(790, 800), (930, 770), (800, 850)], 14, True)
    stroke(img, [(800, 870), (940, 900), (800, 910)], 14, True)
    dot(img, 725, 820, 20)
    blob(img, 760, 960, 24, 36, w=12)
    for a in (-25, 0, 25):
        d = np.radians(a); stroke(img, [(960 + 20 * math.cos(d), 840 + 60 * math.sin(d)), (1010 + 20 * math.cos(d), 840 + 90 * math.sin(d))], 12)
    seed(401); sx_, sy_ = 320, 520
    for a in range(0, 360, 40):
        d = np.radians(a); stroke(img, [(sx_ + 170 * math.cos(d), sy_ + 170 * math.sin(d)), (sx_ + 240 * math.cos(d), sy_ + 240 * math.sin(d))], 16)
    blob(img, sx_, sy_, 120, 120)
    text(img, "COCK-A-DOODLE", 540, 200, 3.2, 14)

def canvas(): return np.full((H, W, 3), BG, np.uint8)

def s_blank(): return canvas()
WORDS = [("WHY", 380, 8), ("ALARM", 630, 7), ("CLOCKS?", 880, 7)]
def s_sleep(k=0):
    im = canvas(); mascot(im, 540, 1390, 1.55, "sleep"); zzz(im, 830, 1110)
    for (s, y, sc) in WORDS[:k]: text(im, s, 540, y, sc, 24)
    return im
def s_clock_big():
    im = canvas(); clock(im, 540, 760, 360, 300, 0, True, yel=False); text(im, "BRRRING!", 540, 1450, 7, 24); return im
def s_grump():
    im = canvas(); clock(im, 540, 560, 280, 300, 0, True); mascot(im, 540, 1400, 1.3, "grumpy"); return im
def s_grump_x():
    im = s_grump(); seed(500)
    stroke(im, [(280, 300), (800, 820)], 44, color=RED); stroke(im, [(800, 300), (280, 820)], 44, color=RED); return im
def s_rooster(): im = canvas(); rooster(im); return im
def s_late():
    im = canvas(); text(im, "LATE!", 540, 470, 11, 30); clock(im, 540, 1010, 330, 300, 270, False, yel=False)
    text(im, "!!", 130, 900, 5, 24); text(im, "!!", 950, 900, 5, 24); return im
def s_money(mascot_pose=None, extra=False):
    im = canvas(); clock(im, 285, 730, 210, 250, 130, yel=False)
    seed(600); stroke(im, [(520, 700), (600, 700)], 24); stroke(im, [(520, 780), (600, 780)], 24)
    coins(im, 790, 840)
    text(im, "TIME", 285, 1130, 4.5, 20, maxw=440); text(im, "MONEY", 790, 1130, 4.5, 20, maxw=380)
    if mascot_pose: mascot(im, 540, 1560, 0.95, mascot_pose)
    if extra: text(im, "TOO EARLY!", 540, 1300, 4.6, 20)
    return im
def s_asleep(final=False):
    im = canvas(); mascot(im, 395, 1420, 1.3, "sleep"); zzz(im, 590, 1160); clock(im, 870, 1600, 130, 300, 0, True)
    if final:
        seed(700); stroke(im, [(120, 300), (960, 300), (960, 760), (620, 760), (540, 860), (500, 760), (120, 760)], 15, True)
        text(im, "5 MORE", 540, 470, 5, 9); text(im, "MINUTES", 540, 650, 5, 9)
    return im

# 15 events, end inclusive
EV = [
 (0, 95, "initial", "opening drawing: mascot asleep with Zzz on #FDFDFD canvas", lambda: s_sleep(0)),
 (96, 141, "word build 1/3", "WHY pops on above sleeping mascot", lambda: s_sleep(1)),
 (142, 187, "word build 2/3", "ALARM pops on", lambda: s_sleep(2)),
 (188, 248, "word build 3/3", "CLOCKS? pops on", lambda: s_sleep(3)),
 (249, 314, "literal picture", "giant ringing alarm clock + BRRRING! (key word drawn literally)", s_clock_big),
 (315, 370, "scene swap", "grumpy mascot under ringing clock", s_grump),
 (371, 436, "red X negation", "red X pops over the clock", s_grump_x),
 (437, 444, "dip-to-white OUT", "previous picture fades to white over 8 frames", None),
 (445, 518, "dip-to-white IN + scene swap", "era break: rooster crowing at the sun (fade-in 445-452, held 453-518)", s_rooster),
 (519, 579, "scene swap", "LATE! over clock at 9", s_late),
 (580, 645, "scene swap", "TIME clock = MONEY coins (time is money)", lambda: s_money()),
 (646, 706, "pop-on", "sad mascot pops on below the equation", lambda: s_money("sad")),
 (707, 756, "pop-on text", "TOO EARLY! pops on", lambda: s_money("sad", True)),
 (757, 849, "scene swap", "mascot asleep again beside ringing clock", lambda: s_asleep()),
 (850, 999, "final joke state", "5 MORE MINUTES pops on over sleeper (no end card)", lambda: s_asleep(True)),
]
DOUT, DIN, DEND = 7, 8, 453

def main():
    shutil.rmtree(FR, ignore_errors=True); os.makedirs(FR)
    imgs = {i: ev[4]() for i, ev in enumerate(EV) if ev[4]}
    white = canvas()
    n = 0
    for i, (a, b, *_rest) in enumerate(EV):
        for f in range(a, b + 1):
            t = (f - a + 1) / 9
            if i == DOUT: im = cv2.addWeighted(imgs[DOUT - 1], 1 - t, white, t, 0)
            elif i == DIN and f < DEND: im = cv2.addWeighted(imgs[DIN], t, white, 1 - t, 0)
            else: im = imgs[i]
            cv2.imwrite(os.path.join(FR, "f%04d.png" % f), im); n += 1
    assert n == 1000
    with open(os.path.join(HERE, "intended_timeline.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["start_frame", "end_frame", "device", "description"])
        for a, b, d, desc, _ in EV[1:]: w.writerow([a, b, d, desc])
    ink = [100 * (imgs[k].min(axis=2) < 90).mean() for k in imgs]
    yel = [bool(((imgs[k][..., 0] < 80) & (imgs[k][..., 2] > 200)).any()) for k in imgs]
    print("ink%% mean=%.1f" % np.mean(ink), [round(x, 1) for x in ink]); print("yellow", sum(yel), "of", len(yel))
    subprocess.check_call(["ffmpeg", "-y", "-v", "error", "-framerate", "50", "-i", os.path.join(FR, "f%04d.png"),
                           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14", "-r", "50", "-fps_mode", "cfr",
                           os.path.join(HERE, "render.mp4")])
    shutil.rmtree(FR)

if __name__ == "__main__": main()
