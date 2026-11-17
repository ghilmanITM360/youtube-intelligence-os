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

def clock(img, cx, cy, r, hh=300, mm=0, ring=False):
    seed(200)
    for sx in (-1, 1):
        blob(img, cx + sx * .72 * r, cy - .78 * r, .3 * r, .26 * r, fill=YEL)
        stroke(img, [(cx + sx * .55 * r, cy + .85 * r), (cx + sx * .78 * r, cy + 1.18 * r)], 18)
    stroke(img, [(cx, cy - r), (cx, cy - 1.18 * r)], 14)
    blob(img, cx, cy, r, r)
    for a in (0, 90, 180, 270):
        d = np.radians(a); stroke(img, [(cx + .78 * r * math.sin(d), cy - .78 * r * math.cos(d)), (cx + .9 * r * math.sin(d), cy - .9 * r * math.cos(d))], 12)
    for ang, L in ((hh, .45), (mm, .68)):
        d = np.radians(ang); stroke(img, [(cx, cy), (cx + L * r * math.sin(d), cy - L * r * math.cos(d))], 16)
    dot(img, cx, cy, 14)
    if ring:
        for sx in (-1, 1):
            for a in (35, 60, 85):
                d = np.radians(a)
                stroke(img, [(cx + sx * 1.3 * r * math.sin(d), cy - 1.3 * r * math.cos(d)), (cx + sx * 1.5 * r * math.sin(d), cy - 1.5 * r * math.cos(d))], 12)

def coins(img, x, base):
    seed(300)
    for k in range(3):
        y = base - 60 * k
        stroke(img, [(x - 150, y), (x + 150, y), (x + 150, y + 40), (x - 150, y + 40)], 1, True, color=YEL, fill=YEL)
        for sx in (-1, 1): stroke(img, [(x + sx * 150, y), (x + sx * 150, y + 40)], 14)
        stroke(img, ell(x, y + 40, 150, 42, 0, 180, 24), 14)
        blob(img, x, y, 150, 42, fill=YEL, w=14)
    text(img, "$", x, base - 120 + 22, 2.4, 12)

def rooster(img):
    seed(400)
    stroke(img, [(60, 1500), (1020, 1500)], 14)
    for sx in (-1, 1): stroke(img, [(480 + sx * 60, 1280), (480 + sx * 70, 1480)], 16)
    for i, a in enumerate((-35, 0, 35)):                                       # tail
        d = np.radians(a); blob(img, 240 - 40 * math.cos(d), 1050 + 140 * math.sin(d), 120, 60, fill=YEL)
    blob(img, 480, 1130, 240, 170)                                              # body
    stroke(img, ell(450, 1130, 120, 80, 200, 340, 12), 12)                      # wing
    stroke(img, [(640, 1060), (700, 900)], 18)
    blob(img, 700, 840, 100, 100)                                               # head
    for i in range(3): blob(img, 650 + 50 * i, 735 + (12 if i == 1 else 0), 30, 38, fill=YEL, w=14)  # comb
    stroke(img, [(790, 800), (930, 770), (800, 850)], 14, True, fill=YEL)       # beak
    stroke(img, [(800, 870), (940, 900), (800, 910)], 14, True, fill=YEL)
    dot(img, 725, 820, 13)
    blob(img, 760, 960, 24, 36, fill=YEL, w=12)                                 # wattle
    for a in (-25, 0, 25):
        d = np.radians(a); stroke(img, [(960 + 20 * math.cos(d), 840 + 60 * math.sin(d)), (1010 + 20 * math.cos(d), 840 + 90 * math.sin(d))], 12)
    # sun
    seed(401); sx_, sy_ = 250, 420
    for a in range(0, 360, 40):
        d = np.radians(a); stroke(img, [(sx_ + 170 * math.cos(d), sy_ + 170 * math.sin(d)), (sx_ + 240 * math.cos(d), sy_ + 240 * math.sin(d))], 16)
    blob(img, sx_, sy_, 120, 120, fill=YEL)

def canvas(): return np.full((H, W, 3), BG, np.uint8)

def s_blank(): return canvas()
def s_sleep(words=()):
    im = canvas(); mascot(im, 540, 1330, 1.15, "sleep"); zzz(im, 760, 1090)
    for (s, y, sc) in words[:]: text(im, s, 540, y, sc)
    return im
WORDS = [("WHY", 400, 7), ("ALARM", 640, 6), ("CLOCKS?", 880, 6)]
def s_clock_big():
    im = canvas(); clock(im, 540, 800, 330, 300, 0, True); text(im, "RING!", 540, 1500, 6, 22); return im
def s_grump():
    im = canvas(); clock(im, 540, 560, 250, 300, 0, True); mascot(im, 540, 1330, 1.15, "grumpy"); return im
def s_grump_x():
    im = s_grump(); seed(500)
    stroke(im, [(300, 320), (780, 800)], 44, color=RED); stroke(im, [(780, 320), (300, 800)], 44, color=RED); return im
def s_rooster(): im = canvas(); rooster(im); return im
def s_late():
    im = canvas(); text(im, "LATE!", 540, 420, 9, 28); clock(im, 540, 760, 170, 300, 270)
    mascot(im, 540, 1450, 1.0, "shocked"); return im
def s_money(pose):
    im = canvas(); clock(im, 250, 700, 190, 90, 0)
    seed(600); stroke(im, [(490, 660), (590, 660)], 22); stroke(im, [(490, 740), (590, 740)], 22)
    coins(im, 830, 760); mascot(im, 540, 1450, 0.95, pose); return im
def s_final():
    im = canvas(); text(im, "5 MORE", 540, 330, 6.5, 22); text(im, "MINUTES", 540, 560, 6.5, 22)
    mascot(im, 400, 1330, 1.05, "sleep"); zzz(im, 560, 1090); clock(im, 880, 1530, 125, 300, 0, True); return im

# (start, end, device, description, state fn)  -- 14 events, end inclusive
EV = [
 (0, 39, "initial blank", "empty #FDFDFD canvas", s_blank),
 (40, 139, "scene swap", "mascot asleep with Zzz", lambda: s_sleep()),
 (140, 179, "word build 1/3", "WHY pops on above sleeping mascot", lambda: s_sleep(WORDS[:1])),
 (180, 219, "word build 2/3", "ALARM pops on", lambda: s_sleep(WORDS[:2])),
 (220, 299, "word build 3/3", "CLOCKS? pops on", lambda: s_sleep(WORDS[:3])),
 (300, 399, "literal picture", "giant ringing alarm clock + RING! (key word drawn literally)", s_clock_big),
 (400, 459, "scene swap", "grumpy mascot under ringing clock", s_grump),
 (460, 539, "red X negation", "red X pops over the clock", s_grump_x),
 (540, 547, "dip-to-white OUT", "previous picture fades to white over 8 frames", None),
 (548, 655, "dip-to-white IN + scene swap", "era break: rooster crowing at the sun (fade-in 548-555, held 556-655)", s_rooster),
 (656, 745, "scene swap + pose", "shocked mascot, LATE! over clock at 9", s_late),
 (746, 835, "scene swap", "clock = coins (time is money), cheerful mascot", lambda: s_money("awake")),
 (836, 915, "pose swap", "same picture, mascot sad", lambda: s_money("sad")),
 (916, 999, "final joke state", "asleep again beside ringing clock: 5 MORE MINUTES (no end card)", s_final),
]

def main():
    shutil.rmtree(FR, ignore_errors=True); os.makedirs(FR)
    imgs = {i: ev[4]() for i, ev in enumerate(EV) if ev[4]}
    white = canvas()
    n = 0
    for i, (a, b, *_rest) in enumerate(EV):
        for f in range(a, b + 1):
            if i == 8: im = cv2.addWeighted(imgs[7], 1 - (f - a + 1) / 9, white, (f - a + 1) / 9, 0)
            elif i == 9 and f < 556: im = cv2.addWeighted(imgs[9], (f - a + 1) / 9, white, 1 - (f - a + 1) / 9, 0)
            else: im = imgs[i]
            cv2.imwrite(os.path.join(FR, "f%04d.png" % f), im); n += 1
    assert n == 1000
    with open(os.path.join(HERE, "intended_timeline.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["start_frame", "end_frame", "device", "description"])
        for a, b, d, desc, _ in EV: w.writerow([a, b, d, desc])
    for k in (1, 4, 6, 9, 13):
        print(k, "ink%%=%.1f" % (100 * (imgs[k].max(axis=2) < 80).mean()))
    subprocess.check_call(["ffmpeg", "-y", "-v", "error", "-framerate", "50", "-i", os.path.join(FR, "f%04d.png"),
                           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14", "-r", "50", "-fps_mode", "cfr",
                           os.path.join(HERE, "render.mp4")])
    shutil.rmtree(FR)

if __name__ == "__main__": main()
