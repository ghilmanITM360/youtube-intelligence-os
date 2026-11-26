"""Slot 07 animatic V0 + illustrated composition boards (placeholders, not final art).

Everything is geometric placeholder drawn from the beat map, so it exists BEFORE expensive art is generated.
Timeline = approved recording (92.53 s). Event times key off narration/NARRATION_BEAT_MAP.csv (phrase edges measured,
word anchors estimated +-0.12 s).

  python3 tools/animatic.py still 16.1 out.png            one frame
  python3 tools/animatic.py video                         storyboard/animatic/ANIMATIC_V0_540x960_15fps.mp4
  python3 tools/animatic.py boards                        storyboard/panels/S01..S10 sheets + per-beat panels
"""
import csv, math, os, random, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1080, 1920                         # design space (final 1080 x 1920)
TOTAL = 94.0                              # 92.53 s voice + tail

# ---------------------------------------------------------------- palette (one grammar for the whole film)
BG = (7, 11, 26); WARM = (255, 172, 64); COOL = (96, 200, 255); WHITE = (238, 240, 245)
MOONC = (172, 172, 176); MOOND = (64, 64, 72); EARTHD = (10, 26, 62); EARTHL = (44, 108, 196)
REGO = (112, 110, 108); GOLD = (214, 170, 70); GREY = (120, 126, 140); DIM = (60, 66, 84)
LDIR = (-0.62, -0.42)                     # film-wide sun direction (toward the sun, screen space)

# beat-map layout constants (non-scale schematic, Earth bottom / Moon top)
EARTH_C = (540, 2700); EARTH_R = 1300     # limb top at y = 1400
MOON_C = (540, 430); MOON_R = 150
PATH_Y0 = 1400; PATH_Y1 = MOON_C[1] + MOON_R
CAP = (60, 1480, 1020, 1730)              # provisional caption band
SAFE = (60, 150, 1020, 1440)              # provisional safe area for key subjects


def lerp(a, b, x): return a + (b - a) * x
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def seg(t, a, b): return clamp((t - a) / (b - a)) if b > a else (1.0 if t >= b else 0.0)
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)
def mix(c1, c2, x): return tuple(int(lerp(a, b, clamp(x))) for a, b in zip(c1, c2))
def dim(c, k): return tuple(int(v * k) for v in c)

_fonts = {}
def font(size, mono=False, bold=False):
    key = (size, mono, bold)
    if key not in _fonts:
        p = '/System/Library/Fonts/Menlo.ttc' if mono else ('/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Helvetica.ttc')
        _fonts[key] = ImageFont.truetype(p, size)
    return _fonts[key]


class Cv:
    """Canvas with a zoom transform (for pushes) and annotation capture (for boards)."""
    def __init__(self, annotate=False):
        self.im = Image.new('RGB', (W, H), BG); self.d = ImageDraw.Draw(self.im)
        self.z = (1.0, W / 2, H / 2); self.annotate = annotate; self.arrows = []

    def zoom(self, k=1.0, cx=W / 2, cy=H / 2): self.z = (k, cx, cy)
    def T(self, x, y): k, cx, cy = self.z; return (cx + (x - cx) * k, cy + (y - cy) * k)
    def R(self, r): return r * self.z[0]

    def circle(self, c, r, fill=None, outline=None, width=1):
        x, y = self.T(*c); r = self.R(r)
        self.d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=width)

    def ellipse(self, c, rx, ry, fill=None, outline=None, width=1):
        x, y = self.T(*c); k = self.z[0]
        self.d.ellipse([x - rx * k, y - ry * k, x + rx * k, y + ry * k], fill=fill, outline=outline, width=width)

    def poly(self, pts, fill=None, outline=None):
        self.d.polygon([self.T(*p) for p in pts], fill=fill, outline=outline)

    def line(self, p0, p1, fill=WHITE, width=3):
        self.d.line([self.T(*p0), self.T(*p1)], fill=fill, width=max(1, int(width)))

    def path(self, pts, fill=WHITE, width=3):
        self.d.line([self.T(*p) for p in pts], fill=fill, width=max(1, int(width)), joint='curve')

    def rect(self, box, fill=None, outline=None, width=1):
        x0, y0 = self.T(box[0], box[1]); x1, y1 = self.T(box[2], box[3])
        self.d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=width)

    def text(self, xy, s, size=40, fill=WHITE, mono=False, bold=False, anchor='mm'):
        self.d.text(self.T(*xy), s, font=font(max(8, int(size * self.z[0])), mono, bold), fill=fill, anchor=anchor)

    def glow(self, c, r, col, a=70, steps=9):
        x, y = self.T(*c); r = self.R(r); pad = int(r) + 4
        patch = Image.new('RGBA', (2 * pad, 2 * pad), (0, 0, 0, 0)); pd = ImageDraw.Draw(patch)
        for i in range(steps):
            rr = r * (1 - i / steps)
            pd.ellipse([pad - rr, pad - rr, pad + rr, pad + rr], fill=col + (int(a * (i + 1) / steps),))
        base = self.im.convert('RGBA'); base.alpha_composite(patch, (int(x) - pad, int(y) - pad))
        self.im.paste(base.convert('RGB')); self.d = ImageDraw.Draw(self.im)

    def tint(self, box, col, a):
        x0, y0, x1, y1 = box
        patch = Image.new('RGBA', (int(x1 - x0), int(y1 - y0)), col + (int(a),))
        base = self.im.convert('RGBA'); base.alpha_composite(patch, (int(x0), int(y0)))
        self.im.paste(base.convert('RGB')); self.d = ImageDraw.Draw(self.im)

    def arrow(self, p0, p1, label=''):
        if self.annotate: self.arrows.append((p0, p1, label))


# ---------------------------------------------------------------- shared drawing pieces
_rng = random.Random(7)
STARS = [(_rng.randint(0, W), _rng.randint(0, H), _rng.choice([1, 1, 2, 2, 3]), _rng.randint(90, 200)) for _ in range(150)]

def space_bg(cv, k=1.0):
    cv.d.rectangle([0, 0, W, H], fill=BG)
    for x, y, s, b in STARS:
        v = int(b * k); cv.d.ellipse([x - s, y - s, x + s, y + s], fill=(v, v, min(255, v + 20)))

def sphere(cv, c, r, dark, lit, n=26):
    for i in range(n):
        f = i / (n - 1); rr = r * (1 - f * 0.88)
        cc = (c[0] + LDIR[0] * r * f * 0.5, c[1] + LDIR[1] * r * f * 0.5)
        cv.circle(cc, rr, fill=mix(dark, lit, f ** 0.8))

def moon(cv, c=MOON_C, r=MOON_R, craters=True):
    sphere(cv, c, r, (36, 36, 42), MOONC)
    for dx, dy, rr in [(-0.28, -0.12, 0.30), (0.22, -0.28, 0.20), (0.05, 0.25, 0.26), (0.38, 0.12, 0.14)]:
        cv.circle((c[0] + dx * r, c[1] + dy * r), rr * r, fill=mix(MOOND, MOONC, 0.22))   # maria (placeholder)
    if craters:
        for dx, dy, rr in [(-0.5, 0.35, 0.07), (0.45, -0.45, 0.06), (-0.1, -0.6, 0.05)]:
            cv.circle((c[0] + dx * r, c[1] + dy * r), rr * r, outline=dim(MOONC, 0.55), width=2)

def earth(cv, lights=False):
    sphere(cv, EARTH_C, EARTH_R, EARTHD, EARTHL, n=30)
    rg = random.Random(3)
    for _ in range(26):                      # placeholder continents / clouds near the visible arc
        ang = rg.uniform(math.pi * 1.28, math.pi * 1.72); dist = rg.uniform(0.80, 0.95) * EARTH_R
        x = EARTH_C[0] + dist * math.cos(ang); y = EARTH_C[1] + dist * math.sin(ang)
        if 0 < y < H:
            cv.ellipse((x, y), rg.randint(30, 90), rg.randint(10, 30), fill=mix((30, 70, 60), (70, 120, 70), rg.random()) if rg.random() < 0.5 else (200, 215, 235))
    for i in range(3):                        # atmosphere rim: thin, brightest at the edge, fading outward (REF-EARTH ISS limb photo)
        cv.circle(EARTH_C, EARTH_R + 2 + i * 4, outline=mix(COOL, BG, 0.25 + i * 0.3), width=4)
    if lights:
        rg = random.Random(11)
        for _ in range(60):
            ang = rg.uniform(math.pi * 1.5, math.pi * 1.74); dist = rg.uniform(0.9, 0.99) * EARTH_R
            x = EARTH_C[0] + dist * math.cos(ang); y = EARTH_C[1] + dist * math.sin(ang)
            if y < H: cv.circle((x, y), rg.choice([2, 3]), fill=(255, 214, 120))

def pulse(cv, x, y, col, size=1.0, trail=(0, 1), tlen=70):
    for i in range(1, 9):
        f = 1 - i / 9
        cv.circle((x + trail[0] * tlen * i / 8, y + trail[1] * tlen * i / 8), 9 * size * f, fill=mix(BG, col, 0.65 * f))
    cv.glow((x, y), 46 * size, col, 90)
    cv.circle((x, y), 11 * size, fill=mix(col, WHITE, 0.55))

def stopwatch(cv, c, r, val, full=3.0, digits=True, alpha=1.0, label=None):
    col = mix(BG, WHITE, alpha); fc = mix(BG, (22, 30, 56), alpha)
    cv.circle(c, r, fill=fc, outline=col, width=5)
    for i in range(60):
        a = i / 60 * 2 * math.pi - math.pi / 2; l = 0.18 if i % 5 == 0 else 0.08
        cv.line((c[0] + math.cos(a) * r * (0.92 - l), c[1] + math.sin(a) * r * (0.92 - l)),
                (c[0] + math.cos(a) * r * 0.92, c[1] + math.sin(a) * r * 0.92), fill=mix(BG, GREY, alpha), width=2)
    a = (val / full) * 2 * math.pi - math.pi / 2
    cv.line(c, (c[0] + math.cos(a) * r * 0.72, c[1] + math.sin(a) * r * 0.72), fill=mix(BG, WARM, alpha), width=6)
    cv.circle(c, 8, fill=col)
    if digits:
        cv.text((c[0], c[1] + r * 0.42), '%.2f' % val, size=int(r * 0.42), fill=col, mono=True, bold=True)
    if label: cv.text((c[0], c[1] - r - 28), label, size=26, fill=mix(BG, GREY, alpha))

def world_space(cv, moon_on=True, lights=False):
    space_bg(cv); earth(cv, lights)
    if moon_on: moon(cv)

def path_line(cv, a=1.0, dashed=True):
    col = mix(BG, GREY, a)
    y = PATH_Y0
    while y > PATH_Y1:
        cv.line((540, y), (540, max(PATH_Y1, y - 26)), fill=col, width=3); y -= 44 if dashed else 26

def py(p): return lerp(PATH_Y0, PATH_Y1, p)   # p=0 Earth, p=1 Moon

def ground(cv, moon_pos=(740, 470), moon_r=120, dome_open=0.35, tilt=0.0, push=1.0, night=1.0):
    cv.zoom(push, 540, 1100)
    cv.d.rectangle([0, 0, W, H], fill=BG)
    for yy in range(0, 1500, 30):                                # sky gradient
        c = mix((6, 10, 28), (22, 34, 66), yy / 1500); cv.d.rectangle([0, yy, W, yy + 30], fill=c)
    for x, y, s, b in STARS[:110]:
        if y < 1200: cv.d.ellipse([x - s, y - s, x + s, y + s], fill=(b, b, min(255, b + 20)))
    if moon_pos: moon(cv, moon_pos, moon_r)
    cv.poly([(0, 1330), (180, 1180), (360, 1290), (620, 1120), (860, 1260), (1080, 1170), (1080, 1920), (0, 1920)], fill=(14, 18, 30))   # far ridge
    cv.poly([(0, 1480), (240, 1360), (520, 1450), (800, 1340), (1080, 1440), (1080, 1920), (0, 1920)], fill=(9, 12, 20))             # near ridge
    cv.rect((380, 1190, 700, 1400), fill=(70, 74, 88))                                                                                  # building
    dc = (540, 1190); dr = 190
    cv.d.pieslice([cv.T(dc[0] - dr, dc[1] - dr), cv.T(dc[0] + dr, dc[1] + dr)], 180, 360, fill=(188, 194, 206))
    cv.d.pieslice([cv.T(dc[0] - dr * 0.55, dc[1] - dr), cv.T(dc[0] + dr * 1.0, dc[1] + dr)], 270, 360, fill=(150, 156, 170))
    sw = 70 * dome_open                                          # slit
    cv.rect((540 - sw / 2 + 20, 1190 - dr - 4, 540 + sw / 2 + 20, 1190 - 4), fill=mix((6, 10, 28), (20, 30, 60), 0.5))
    ax = 540 + 20; ay = 1170                                      # telescope tube inside slit
    cv.line((ax, ay), (ax + math.sin(tilt) * 140 * 1.0, ay - math.cos(tilt) * 140), fill=(210, 214, 224), width=22 * 1)
    cv.zoom()

def aperture(cv, c=(540, 960), r=170, ring=WHITE):
    cv.circle(c, r + 26, fill=(40, 44, 58)); cv.circle(c, r, fill=(10, 14, 28), outline=ring, width=6)
    cv.circle(c, r * 0.35, fill=(30, 36, 54), outline=GREY, width=3)         # secondary mirror (placeholder)
    for a in (0, 120, 240):
        t = math.radians(a + 90); cv.line((c[0], c[1]), (c[0] + r * math.cos(t), c[1] + r * math.sin(t)), fill=GREY, width=4)

def regolith(cv, hy=860, k=1.0, stones=True, push=1.0):
    cv.zoom(push, 540, 1100)
    cv.d.rectangle([0, 0, W, H], fill=(0, 0, 0))
    for x, y, s, b in STARS[:60]:
        if y < hy - 20: cv.d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(b, b, b))
    for yy in range(int(hy), H, 20):
        f = (yy - hy) / (H - hy); cv.d.rectangle([0, yy, W, yy + 20], fill=mix((70, 69, 68), REGO, f))
    cv.poly([(0, hy), (300, hy - 28), (600, hy - 10), (900, hy - 32), (1080, hy - 8), (1080, hy), (0, hy)], fill=(60, 59, 58))
    if stones:
        rg = random.Random(5)
        for _ in range(26):
            x = rg.randint(0, W); y = rg.randint(int(hy) + 30, 1700); s = 6 + (y - hy) / 14 * rg.random()
            cv.ellipse((x, y), s * 1.2, s * 0.7, fill=(86, 85, 84)); cv.ellipse((x + s * 0.8, y + s * 0.3), s * 1.1, s * 0.4, fill=(40, 40, 40))
    cv.zoom()

def reflector(cv, c, w, alpha=1.0, grid=10, tilt=0.18):
    h = w * 0.52; base = BG if alpha < 1 else None
    pts = [(c[0] - w / 2, c[1] + h / 2), (c[0] + w / 2, c[1] + h / 2), (c[0] + w / 2 - w * tilt, c[1] - h / 2), (c[0] - w / 2 + w * tilt, c[1] - h / 2)]
    cv.poly(pts, fill=mix(BG, (58, 60, 70), alpha), outline=mix(BG, GREY, alpha))
    for i in range(grid):
        for j in range(grid):
            fy = (j + 0.5) / grid; fx = (i + 0.5) / grid
            lx = lerp(c[0] - w / 2 + w * tilt * fy * 0.0, c[0] + w / 2, 0)
            x0 = lerp(c[0] - w / 2 + w * tilt * (1 - fy), c[0] + w / 2 - w * tilt * (1 - fy), fx); y0 = lerp(c[1] + h / 2, c[1] - h / 2, fy)
            cv.ellipse((x0, y0), w / grid * 0.34, w / grid * 0.17, fill=mix(BG, (150, 196, 214), alpha * 0.8), outline=mix(BG, WHITE, alpha * 0.5))

def astronaut(cv, c, s=1.0, pose='kneel'):
    x, y = c
    cv.ellipse((x + 30 * s, y + 56 * s), 70 * s, 14 * s, fill=(30, 30, 30))                                        # shadow (sun from left)
    cv.line((x - 10 * s, y + 20 * s), (x - 46 * s, y + 52 * s), fill=(220, 222, 228), width=24 * s)              # legs
    cv.line((x + 8 * s, y + 24 * s), (x + 34 * s, y + 56 * s), fill=(220, 222, 228), width=24 * s)
    cv.d.rounded_rectangle([cv.T(x - 26 * s, y - 52 * s), cv.T(x + 26 * s, y + 24 * s)], radius=int(10 * s), fill=(232, 234, 240))
    cv.d.rounded_rectangle([cv.T(x + 20 * s, y - 56 * s), cv.T(x + 52 * s, y + 6 * s)], radius=int(8 * s), fill=(196, 198, 206))   # backpack
    cv.line((x - 16 * s, y - 30 * s), (x - 52 * s, y - 2 * s), fill=(220, 222, 228), width=16 * s)              # arm toward panel
    cv.circle((x - 8 * s, y - 76 * s), 28 * s, fill=(236, 238, 244))                                              # helmet
    cv.ellipse((x - 16 * s, y - 76 * s), 17 * s, 20 * s, fill=GOLD)                                               # visor

def cube_geometry(cx=540, cy=900, L=300):
    V = (cx, cy + L * 0.55)
    A = (V[0] + L, V[1] - L); B = (V[0] - L, V[1] - L)
    return V, A, B

def _hit(p, d, q0, q1):
    ex, ey = q1[0] - q0[0], q1[1] - q0[1]; den = d[0] * ey - d[1] * ex
    if abs(den) < 1e-9: return None
    t = ((q0[0] - p[0]) * ey - (q0[1] - p[1]) * ex) / den
    s = ((q0[0] - p[0]) * d[1] - (q0[1] - p[1]) * d[0]) / den
    return t if (t > 1e-6 and -1e-6 <= s <= 1 + 1e-6) else None

def corner_ray(V, A, B, x0, ang_deg, L=300):
    """Ray enters the V-shaped corner from above, bounces on both faces, leaves parallel to how it came in (2-D cross-section)."""
    a = math.radians(ang_deg); d = (math.sin(a), math.cos(a))
    p = (x0, V[1] - L * 1.0 - 60); pts = [p]
    for _ in range(2):
        best = None
        for q0, q1 in ((V, A), (V, B)):
            t = _hit(p, d, q0, q1)
            if t and (best is None or t < best[0]): best = (t, q0, q1)
        if not best: break
        t, q0, q1 = best; p = (p[0] + d[0] * t, p[1] + d[1] * t); pts.append(p)
        ex, ey = q1[0] - q0[0], q1[1] - q0[1]; n = math.hypot(ex, ey); ex, ey = ex / n, ey / n
        dot = d[0] * ex + d[1] * ey; d = (2 * dot * ex - d[0], 2 * dot * ey - d[1])
    lin = math.dist(pts[0], pts[1]) if len(pts) > 1 else 300
    pts.append((p[0] + d[0] * lin, p[1] + d[1] * lin))     # exit as long as the entry, so in/out read as a matched pair
    return pts

def partial(cv, pts, frac, col, width=6):
    tot = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)); need = tot * clamp(frac); out = [pts[0]]
    for i in range(len(pts) - 1):
        l = math.dist(pts[i], pts[i + 1])
        if need >= l: out.append(pts[i + 1]); need -= l
        else:
            f = need / l if l else 0; out.append((lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f))); break
    if len(out) > 1: cv.path(out, fill=col, width=width)
    return out[-1]

def corner_diagram(cv, prog=3.0, rays=((-250, 10), (-30, 20), (230, -10)), alpha=1.0, cx=540, cy=980, L=420):
    """prog 0..len(rays): rays play one after another (entry warm, exit cool); finished rays stay dimmed."""
    V, A, B = cube_geometry(cx, cy, L)
    cv.poly([V, A, (A[0], A[1] - 40), (B[0], B[1] - 40), B], fill=mix(BG, (30, 40, 70), alpha))
    cv.line(V, A, fill=mix(BG, (170, 210, 235), alpha), width=12); cv.line(V, B, fill=mix(BG, (170, 210, 235), alpha), width=12)
    out = []
    for i, (x_off, ang) in enumerate(rays):
        loc = clamp(prog - i)
        if loc <= 0: continue
        k = 1.0 if (prog - i) < 1 else (0.6 if prog >= len(rays) else 0.18)
        pts = corner_ray(V, A, B, cx + x_off, ang, L)
        partial(cv, pts[:3], ease(seg(loc, 0.0, 0.5)), mix(BG, WARM, k), 8)
        if loc > 0.5: partial(cv, pts[2:], ease(seg(loc, 0.5, 1.0)), mix(BG, COOL, k), 8)
        out.append(pts)
    return out

def third_face_inset(cv, c=(180, 470), r=105):
    cv.circle(c, r, fill=(14, 20, 40), outline=GREY, width=4)
    for a in (-90, 30, 150):
        t = math.radians(a); cv.line(c, (c[0] + r * 0.78 * math.cos(t), c[1] + r * 0.78 * math.sin(t)), fill=(170, 210, 235), width=6)
    cv.text((c[0], c[1] + r + 22), 'third face', size=22, fill=GREY)

def footprint_inset(cv, c=(850, 470), r=125, a=1.0):
    cv.circle(c, r, fill=mix(BG, (20, 28, 54), a), outline=mix(BG, GREY, a), width=4)
    cv.glow(c, r * 0.92, WARM, int(70 * a))
    cv.rect((c[0] - 4, c[1] - 4, c[0] + 4, c[1] + 4), fill=mix(BG, WHITE, a))
    cv.text((c[0], c[1] + r + 24), 'magnified', size=22, fill=mix(BG, GREY, a))

# histogram data (deterministic)
_hr = random.Random(21)
HIST = [(_hr.gauss(0, 1), _hr.random() < 0.40, _hr.uniform(-1, 1)) for _ in range(900)]   # (signal offset, is_signal, noise pos)

def hist_view(cv, n, y0=1240, x0=140, x1=940, sharp=1.0, counter=True, bar_w=14, scale=1.0, peak_x=640):
    cv.line((x0, y0), (x1, y0), fill=GREY, width=4)
    for i in range(0, 9): cv.line((x0 + (x1 - x0) * i / 8, y0), (x0 + (x1 - x0) * i / 8, y0 + 14), fill=GREY, width=3)
    bins = {}
    for g, sig, nz in HIST[:int(n)]:
        x = peak_x + g * 38 * sharp if sig else lerp(x0 + 20, x1 - 20, (nz + 1) / 2)
        b = int((x - x0) / bar_w); bins[b] = bins.get(b, 0) + 1
    for b, cnt in bins.items():
        h = min(520, cnt * 9 * scale); bx = x0 + b * bar_w
        cv.rect((bx, y0 - h, bx + bar_w - 2, y0 - 2), fill=mix(COOL, WHITE, 0.15) if abs(bx - peak_x) < 120 else dim(COOL, 0.6))
    if counter: cv.text((x1, 330), 'pulses  %s' % format(int(n * 4), ','), size=34, fill=GREY, mono=True, anchor='rm')

def dots_on_axis(cv, t, y0=1000, events=(0.1, 0.5, 0.9), x0=160, x1=920):
    cv.line((x0, y0), (x1, y0), fill=GREY, width=4)
    for i in range(9): cv.line((x0 + (x1 - x0) * i / 8, y0 - 8), (x0 + (x1 - x0) * i / 8, y0 + 8), fill=GREY, width=3)
    for i, e in enumerate(events):
        a = seg(t, e, e + 0.25)
        if a > 0:
            x = lerp(x0 + 100, x1 - 100, [0.33, 0.62, 0.78][i % 3]); yy = y0 - 260 * (1 - ease(a))
            cv.glow((x, yy), 36, COOL, 90); cv.circle((x, yy), 11, fill=mix(COOL, WHITE, 0.6))


# ---------------------------------------------------------------- scenes
class Tm:
    def __init__(s, t, start, end, anchor): s.t = t; s.tb = t - start; s.span = end - start; s.u = clamp((t - start) / (end - start)); s.ta = t - anchor; s.anchor = anchor; s.start = start

SC = {}
def scene(*ids):
    def deco(f):
        for i in ids: SC[i] = f
        return f
    return deco

@scene('B01')
def s_b01(cv, T):
    ground(cv, moon_pos=(700, lerp(700, 460, ease(seg(T.t, 0.6, 2.4)))), dome_open=ease(seg(T.t, 0.2, 1.6)) * 0.9 + 0.1, tilt=0, push=1 + 0.03 * T.u)
    cv.arrow((700, 700), (700, 470), 'moon rises on "laser"')

@scene('B02')
def s_b02(cv, T):
    ground(cv, dome_open=1.0, tilt=0.35)
    a = ease(seg(T.tb, 0.0, 0.5)) * (1 - ease(seg(T.tb, 0.5, 0.85)))          # imagined floodlight cone, then fades
    for i in range(20):
        f = i / 20; x0 = 560; y0 = 1040; x1 = 700; y1 = 540
        cv.line((lerp(x0, x1, f) - 30 * f, lerp(y0, y1, f)), (lerp(x0, x1, f + .03) + 30 * f, lerp(y0, y1, f + .03)), fill=mix(BG, WARM, a * 0.8), width=3) if i % 2 == 0 else None
    r = ease(seg(T.ta, -0.1, 0.35))
    if r > 0:
        cv.circle((700, 470), 150, outline=mix(BG, (255, 90, 90), r), width=8); cv.line((600, 570), (800, 370), fill=mix(BG, (255, 90, 90), r), width=8)
    cv.arrow((560, 1040), (700, 540), 'imagined cone (rejected)')

@scene('B03')
def s_b03(cv, T):
    p = 1.03 + 0.55 * ease(T.u)
    ground(cv, moon_pos=(700, 460), dome_open=1.0, tilt=0.35 + 0.4 * ease(seg(T.tb, 0.2, 1.0)), push=p)
    a = ease(seg(T.ta, -0.1, 0.5))
    if a > 0:
        for i, (x, y) in enumerate([(400, 560), (440, 520), (500, 500), (560, 520), (570, 570), (540, 620), (500, 660)]):
            cv.circle((x + 100, y - 20 + 20 * (1 - a)), 14, fill=mix(BG, WHITE, a))
        cv.circle((545, 780 + 20 * (1 - a)), 14, fill=mix(BG, WHITE, a))
    cv.arrow((540, 1100), (540, 900), 'push-in')

@scene('B04')
def s_b04(cv, T):
    space_bg(cv, 0.4); aperture(cv)
    f = seg(T.ta, -0.25, 0.1)
    if 0 < f < 1 or T.ta < 0.15 and T.ta > -0.2:
        cv.glow((540, 960), 190 * ease(1 - abs(T.ta) / 0.2 if abs(T.ta) < 0.2 else 0), WARM, 120)
    if T.ta > 0:
        y = 960 - 1200 * ease(seg(T.ta, 0, 0.7)) ** 1.6
        pulse(cv, 540, y, WARM, 1.2, trail=(0, 1), tlen=100)
    cv.arrow((540, 940), (540, 200), 'pulse leaves on "pulse"')

@scene('B05')
def s_b05(cv, T):
    world_space(cv); path_line(cv, 0.5)
    p = ease(seg(T.t, 8.2, 9.85))
    if T.t > 8.2 and p < 1: pulse(cv, 540, py(p), WARM, 1.0, trail=(0, 1))
    r = ease(seg(T.t, 9.85, 10.3))
    if r > 0: cv.circle((540, PATH_Y1 + 2), 20 + 60 * r, outline=mix(BG, WARM, 1 - r * 0.4), width=5)       # ring only, no hardware
    cv.text((900, 1380), 'not to scale', size=24, fill=GREY)
    cv.arrow((540, 1380), (540, 600), 'pulse climbs to the Moon')

def SW_C(T): return (190, 250)

@scene('B06')
def s_b06(cv, T):
    world_space(cv); path_line(cv, 0.4)
    k = seg(T.t, 11.42, 16.14); val = 2.56 * k
    stopwatch(cv, SW_C(T), 100, val, alpha=ease(seg(T.t, 11.3, 11.9)))
    if T.t > 11.42:
        p = seg(T.t, 11.42, 14.0); pulse(cv, 540, py(min(p, 1) if p < 1 else 1), WARM, 1.0, trail=(0, 1)) if p < 1 else None
        if p >= 1:
            q = seg(T.t, 14.0, 16.14); pulse(cv, 540, py(1 - q), COOL, 1.0, trail=(0, -1))
    cv.arrow((190, 350), (190, 380), 'clock starts as pulse leaves')

def _round_trip(cv, T, t0, t1, tmid=None, size=1.0):
    k = seg(T.t, t0, t1); tm = tmid if tmid else (t0 + t1) / 2
    if T.t < t0 or k >= 1: return k
    if T.t < tm: pulse(cv, 540, py(seg(T.t, t0, tm)), WARM, size, trail=(0, 1))
    else: pulse(cv, 540, py(1 - seg(T.t, tm, t1)), COOL, size, trail=(0, -1))
    return k

@scene('B07')
def s_b07(cv, T):
    world_space(cv); path_line(cv, 0.4)
    val = 2.56 * seg(T.t, 11.42, 16.14)
    stopwatch(cv, (540, 330 + 0), 140, val, alpha=1.0) if False else stopwatch(cv, (190, 250), 100, val)
    k = _round_trip(cv, T, 11.42, 16.14, 13.78)
    stopwatch(cv, (540, 1050), 0, 0, digits=False, alpha=0) if False else None
    big = ease(seg(T.tb, 0.0, 0.5))
    if big > 0:
        cv.text((830, 250), '%.2f s' % val, size=int(70 + 30 * big), fill=WHITE, mono=True, bold=True)

@scene('B08')
def s_b08(cv, T):
    world_space(cv); path_line(cv, 0.5)
    stopwatch(cv, (190, 250), 100, 2.56)
    a = ease(seg(T.ta, -0.4, 0.3))
    cv.line((500, py(0.05)), (500, py(0.95)), fill=mix(BG, WARM, 0.35 + 0.65 * a), width=8); cv.poly([(500, py(0.95) - 10), (478, py(0.95) + 34), (522, py(0.95) + 34)], fill=mix(BG, WARM, 0.35 + 0.65 * a))
    cv.line((580, py(0.95)), (580, py(0.05)), fill=mix(BG, COOL, 0.35 + 0.65 * a), width=8); cv.poly([(580, py(0.05) + 10), (558, py(0.05) - 34), (602, py(0.05) - 34)], fill=mix(BG, COOL, 0.35 + 0.65 * a))
    cv.arrow((500, 1300), (500, 700), 'there'); cv.arrow((580, 700), (580, 1300), 'and back')

@scene('B09')
def s_b09(cv, T):
    world_space(cv); path_line(cv, 0.4)
    stopwatch(cv, (190, 250), 100, 2.56)
    br = ease(seg(T.tb, 0.0, 0.4))
    cv.path([(660, py(0.0)), (690, py(0.0)), (690, py(1.0)), (660, py(1.0))], fill=mix(BG, WHITE, br), width=5)
    cv.text((800, py(0.5)), '2.56 s', size=44, fill=mix(BG, WHITE, br), mono=True)
    x = ease(seg(T.t, 20.2, 20.6))
    if x > 0:
        cv.line((640, py(0.25) - 28), (700, py(0.25) + 28), fill=mix(BG, (255, 90, 90), x), width=7); cv.line((700, py(0.25) - 28), (640, py(0.25) + 28), fill=mix(BG, (255, 90, 90), x), width=7)
        cv.text((820, py(0.25)), '2.5 s ?', size=34, fill=mix(BG, (255, 110, 110), x), mono=True)
    sp = ease(seg(T.ta, -0.1, 0.5))
    if sp > 0:
        cv.line((650, py(0.5)), (700, py(0.5)), fill=mix(BG, WARM, sp), width=7)
    cv.arrow((690, py(0.0)), (690, py(1.0)), 'whole trip, then split at the Moon')

@scene('B10')
def s_b10(cv, T):
    world_space(cv); path_line(cv, 0.4)
    k = seg(T.t, 21.83, 23.48); stopwatch(cv, (190, 250), 100, 1.28 * k)
    if 21.83 < T.t < 23.48: pulse(cv, 540, py(k), WARM, 1.0, trail=(0, 1))
    cv.text((820, 780), 'leg %.2f s' % (1.28 * k), size=40, fill=WARM, mono=True)

@scene('B11')
def s_b11(cv, T):
    world_space(cv); path_line(cv, 0.4)
    k = seg(T.t, 24.08, 25.32); stopwatch(cv, (190, 250), 100, 1.28 + 1.28 * k)
    if 24.08 < T.t < 25.32: pulse(cv, 540, py(1 - k), COOL, 1.0, trail=(0, -1))
    cv.text((820, 780), 'leg %.2f s' % (1.28 * k), size=40, fill=COOL, mono=True)

ORB_E = 0.24; ORB_A = 400; ORB_F = (500, 1130)
def orbit_pos(theta):
    r = ORB_A * (1 - ORB_E ** 2) / (1 + ORB_E * math.cos(theta)); return (ORB_F[0] + r * math.cos(theta), ORB_F[1] - r * math.sin(theta)), r

def orbit_scene(cv, T, show_clock):
    space_bg(cv)
    pts = [orbit_pos(i / 90 * 2 * math.pi)[0] for i in range(91)]; cv.path(pts, fill=dim(GREY, 0.7), width=3)
    cv.circle(ORB_F, 70, fill=EARTHL, outline=COOL, width=4)
    th = math.pi * ease(seg(T.t, 26.5, 31.0)); mp, r = orbit_pos(th)
    moon(cv, mp, 56, craters=False)
    rmin = ORB_A * (1 - ORB_E) / (1 - ORB_E ** 2) * (1 - ORB_E ** 2) / (1 + ORB_E); rmax = ORB_A * (1 - ORB_E ** 2) / (1 - ORB_E)
    f = (r - rmin) / (rmax - rmin); km = 357000 + 50000 * f
    cv.line((ORB_F[0] + 70, ORB_F[1]), mp, fill=WARM, width=5)
    cv.text((540, 1450), '%s km' % format(int(round(km, -3)), ','), size=48, fill=WARM, mono=True)
    if show_clock: stopwatch(cv, (190, 250), 100, 2.38 + 0.33 * f)
    cv.text((900, 330), 'orbit exaggerated', size=24, fill=GREY)
    cv.arrow(orbit_pos(0.3)[0], orbit_pos(1.0)[0], 'Moon moves along the ellipse')

@scene('B12')
def s_b12(cv, T): orbit_scene(cv, T, False)
@scene('B13')
def s_b13(cv, T): orbit_scene(cv, T, True)

@scene('B14')
def s_b14(cv, T):
    space_bg(cv)
    g = ease(seg(T.tb, 0.1, 1.3)); r = lerp(56, 560, g); c = (lerp(orbit_pos(math.pi)[0][0], 540, g), lerp(orbit_pos(math.pi)[0][1], 880, g))
    moon(cv, c, r)
    cv.arrow((540, 1100), (540, 900), 'Moon grows to fill the frame')

@scene('B15')
def s_b15(cv, T):
    g = ease(seg(T.tb, 0.0, 0.9))
    if g < 1:
        space_bg(cv); moon(cv, (540, lerp(880, 1100, g)), lerp(560, 1500, g))
    if g > 0.55: regolith(cv, hy=640)
    land = seg(T.t, 32.9, 33.3)
    if 0 < land < 1 and g > 0.9: pulse(cv, 540, lerp(100, 1230, ease(land)), WARM, 1.0, trail=(0, -1))
    sc = ease(seg(T.t, 33.3, 33.9))
    if sc > 0:
        for i in range(14):
            a = math.pi * (1.05 + 0.9 * i / 13) * (1) ; a = math.pi + math.pi * i / 13
            cv.line((540 + 20 * math.cos(a), 1230 + 20 * math.sin(a)), (540 + 360 * sc * math.cos(a), 1230 + 220 * sc * math.sin(a)), fill=mix(BG, WARM, 0.8), width=4)
    cv.arrow((540, 1230), (200, 1100), 'scatter in all directions'); cv.arrow((540, 1230), (880, 1100), '')

@scene('B16')
def s_b16(cv, T):
    regolith(cv, hy=640)
    a = ease(seg(T.tb, 0.1, 0.8))
    pts = [(330, 1330), (750, 1330), (700, 1180), (380, 1180)]
    cv.poly(pts, outline=mix(BG, WHITE, 0.7 * a))
    cv.text((540, 1255), '?', size=100, fill=mix(BG, WHITE, a))
    cv.circle((540, 1020), 70 + 10 * math.sin(T.t * 3), outline=mix(BG, WARM, a), width=5)

@scene('B17')
def s_b17(cv, T):
    regolith(cv, hy=640, push=1 + 0.04 * T.u)
    f = ease(seg(T.ta, -0.35, 0.35))
    cv.zoom(1 + 0.04 * T.u, 540, 1100)
    cv.poly([(330, 1330), (750, 1330), (700, 1180), (380, 1180)], outline=mix(BG, WHITE, 0.7 * (1 - f)))
    reflector(cv, (540, 1255), 440, alpha=f)
    cv.zoom()

@scene('B18')
def s_b18(cv, T):
    z = 1 - 0.45 * ease(seg(T.tb, 0.2, 2.8))
    regolith(cv, hy=760)
    cv.zoom(z, 640, 1300)
    reflector(cv, (700, 1300), 440)
    astronaut(cv, (420, 1220), 1.9)
    cv.zoom()
    cv.arrow((540, 1500), (540, 1400), 'camera eases out and settles')

@scene('B19')
def s_b19(cv, T):
    g = ease(seg(T.tb, 0.0, 1.1)); x = seg(T.ta, -0.2, 0.5)
    if x < 1:
        space_bg(cv, 0.0); cv.d.rectangle([0, 0, W, H], fill=(24, 26, 34))
        cv.zoom(1 + 10 * g, 400, 1000)
        reflector(cv, (540, 1000), 1000, tilt=0.0)
        cv.zoom()
    if x > 0:
        tmp = Cv(); tmp.d.rectangle([0, 0, W, H], fill=BG); corner_diagram(tmp, 0)
        im = Image.blend(cv.im, tmp.im, ease(x)); cv.im.paste(im); cv.d = ImageDraw.Draw(cv.im)
    cv.arrow((540, 1400), (540, 1000), 'macro push to one cube')

@scene('B20')
def s_b20(cv, T):
    cv.d.rectangle([0, 0, W, H], fill=BG)
    corner_diagram(cv, prog=3 * seg(T.tb, 0.1, 1.95))
    third_face_inset(cv, (190, 400), 100)
    a = ease(seg(T.t, 45.55, 46.0))
    if a > 0: footprint_inset(cv, (870, 400), 115, a)
    cv.arrow((300, 540), (300, 740), 'in'); cv.arrow((780, 740), (780, 540), 'out, parallel')

@scene('B21')
def s_b21(cv, T):
    cv.d.rectangle([0, 0, W, H], fill=BG)
    corner_diagram(cv, prog=2 * seg(T.tb, 0.0, 1.3), rays=((-190, 10), (150, -10)), cx=290, cy=980, L=320)
    a = ease(seg(T.tb, 0.0, 0.5)); mid = (790, 1080)
    cv.line((650, 1160), (930, 1000), fill=mix(BG, (200, 205, 215), 0.45), width=10)
    pts = [(650, 700), (760, 1105)]; partial(cv, pts, a, WARM, 7)
    if T.tb > 0.5: partial(cv, [(760, 1105), (1000, 900)], ease(seg(T.tb, 0.5, 1.2)), COOL, 7)
    cv.text((290, 1320), 'cube', size=34, fill=GREY); cv.text((790, 1320), 'flat mirror', size=34, fill=GREY)

@scene('B22')
def s_b22(cv, T):
    ground(cv, moon_pos=None, dome_open=1.0, tilt=0.12, push=1.0)
    p = seg(T.t, 49.58, 50.5)
    if p > 0: pulse(cv, lerp(740, 560, ease(p)), lerp(200, 1050, ease(p)), COOL, 0.9, trail=(0.2, -1))
    cv.arrow((740, 200), (560, 1050), 'return arrives')

@scene('B23')
def s_b23(cv, T):
    cv.d.rectangle([0, 0, W, H], fill=(14, 16, 24))
    cv.rect((380, 420, 700, 1200), fill=(36, 40, 54), outline=GREY, width=5)                       # tube cutaway
    cv.ellipse((540, 1170), 160, 28, fill=(150, 170, 190), outline=WHITE, width=3)               # primary mirror
    cv.rect((700, 1010, 840, 1130), fill=(54, 58, 76), outline=GREY, width=4)                     # detector box
    cv.text((770, 1070), 'detector', size=26, fill=GREY)
    a = ease(seg(T.tb, 0.0, 0.9)); b = ease(seg(T.tb, 0.9, 1.7))
    for x in (440, 540, 640):
        partial(cv, [(x, 360), (x, 1160)], a, COOL, 5)
        if b > 0: partial(cv, [(x, 1160), (770, 1070)], b, COOL, 5)
    r = ease(seg(T.ta, -0.3, 0.3))
    if r > 0: cv.circle((770, 1070), 100, outline=mix(BG, WHITE, r), width=6)

@scene('B24')
def s_b24(cv, T):
    space_bg(cv, 0.4); aperture(cv, (540, 960), 150 + 40 * T.u)
    k = 1 - 0.75 * ease(T.u); cv.tint((0, 0, W, H), (0, 0, 0), 200 * (1 - k))

@scene('B25')
def s_b25(cv, T):
    world_space(cv); path_line(cv, 0.3)
    o = ease(seg(T.tb, 0.0, 1.0)); r = ease(seg(T.tb, 1.2, 2.2))
    if o > 0:
        yt = lerp(PATH_Y0, PATH_Y1 + 20, o); hw = lerp(10, 190, o)
        cv.poly([(530, PATH_Y0), (550, PATH_Y0), (540 + hw, yt), (540 - hw, yt)], fill=mix(BG, WARM, 0.22))
    cv.rect((528, PATH_Y1 + 12, 552, PATH_Y1 + 30), fill=WHITE)
    if r > 0:
        yb = lerp(PATH_Y1 + 40, PATH_Y0 - 10, r); hw = lerp(10, 300, r)
        cv.poly([(530, PATH_Y1 + 40), (550, PATH_Y1 + 40), (540 + hw, yb), (540 - hw, yb)], fill=mix(BG, COOL, 0.2))
        cv.circle((540, PATH_Y0 - 6), 6, fill=WHITE)
    cv.text((900, 1380), 'not to scale', size=24, fill=GREY)
    cv.arrow((540, 1380), (540, 650), 'beam widens'); cv.arrow((700, 650), (700, 1380), 'return widens again')

@scene('B26')
def s_b26(cv, T): space_bg(cv, 0.1); dots_on_axis(cv, T.tb)

@scene('B27')
def s_b27(cv, T):
    space_bg(cv, 0.1); hist_view(cv, 20 + 380 * ease(seg(T.t, 61.65, 63.2)) ** 1.3)

@scene('B28')
def s_b28(cv, T):
    space_bg(cv, 0.1)
    for i, (x, y) in enumerate([(380, 880), (540, 960), (700, 880)]):
        a = ease(seg(T.tb, 0.2 + 0.3 * i, 0.6 + 0.3 * i))
        if a > 0:
            cv.glow((x, y), 70, COOL, int(90 * a)); cv.circle((x, y), 14, fill=mix(BG, mix(COOL, WHITE, 0.6), a)); cv.circle((x, y), 40 + 6 * math.sin(T.t * 4 + i), outline=mix(BG, COOL, 0.5 * a), width=3)

@scene('B29')
def s_b29(cv, T):
    space_bg(cv, 0.3); earth(cv)
    for j in range(5):
        pts = [(x, 1080 - j * 36 + 14 * math.sin(x / 70 + T.t * 3 + j)) for x in range(0, W + 1, 30)]
        cv.path(pts, fill=mix(BG, COOL, 0.25 + 0.05 * j), width=5)
    p = ease(seg(T.tb, 0.0, 2.2)); y = lerp(1400, 300, p)
    wob = 18 * math.sin(T.t * 7) * (1 - ease(seg(T.ta, -0.4, 0.2))) if 1080 - 150 < y < 1100 or p > 0.5 else 0
    pulse(cv, 540 + wob, y, WARM, 0.9, trail=(0, 1))
    cv.ellipse((540 + wob, 520), 90, 26, outline=mix(BG, WARM, 0.5), width=3)
    c = ease(seg(T.ta, -0.1, 0.4)); cv.line((780, 1020), (780, 1100), fill=mix(BG, WHITE, c), width=6); cv.line((750, 1100), (810, 1100), fill=mix(BG, WHITE, c), width=6)
    cv.arrow((540, 1400), (540, 400), 'beam passes the air layer')

@scene('B29b')
def s_b29b(cv, T):
    space_bg(cv, 0.1); hist_view(cv, 420, sharp=lerp(1.0, 0.45, ease(seg(T.tb, 0.6, 3.2))), counter=False, bar_w=14, scale=1.0 + 0.7 * ease(seg(T.tb, 0.6, 3.2)))

@scene('B30')
def s_b30(cv, T):
    space_bg(cv, 0.1); hist_view(cv, 420, sharp=0.45, counter=False, scale=1.7, y0=1240)
    w = lerp(150, 14, ease(seg(T.tb, 0.0, 1.2)))
    cv.line((640 - w, 1300), (640 + w, 1300), fill=WARM, width=8); cv.line((640 - w, 1286), (640 - w, 1314), fill=WARM, width=6); cv.line((640 + w, 1286), (640 + w, 1314), fill=WARM, width=6)
    a = ease(seg(T.ta, -0.3, 0.3)); cv.text((640, 1370), 'about 1 mm = 7 ps', size=34, fill=mix(BG, WHITE, a * 0.0), mono=True)   # figure held back until the owner approves its placement

def path_scene(cv, T, fade=1.0):
    world_space(cv, True); path_line(cv, fade)

@scene('B31')
def s_b31(cv, T):
    path_scene(cv, T); a = ease(seg(T.tb, 0, 0.5)); cv.tint((0, 0, W, H), BG, 160 * (1 - a))
    cv.arrow((540, 1400), (540, 600), 'details fade; path remains')

@scene('B32')
def s_b32(cv, T):
    path_scene(cv, T)
    d = ease(seg(T.tb, 0.0, 0.5)); stopwatch(cv, (190, lerp(-120, 250, d)), 100, 2.56 * seg(T.t, 77.5, 78.9), alpha=d)
    _round_trip(cv, T, 77.5, 78.9, 78.2)

@scene('B33')
def s_b33(cv, T):
    path_scene(cv, T)
    stopwatch(cv, (190, 250), 100, 2.56, digits=False)
    a = ease(seg(T.tb, 0.0, 0.5)); cv.path([(660, py(0.0)), (690, py(0.0)), (690, py(1.0)), (660, py(1.0))], fill=mix(BG, WHITE, a), width=5)
    cv.line((500, py(0.05)), (500, py(0.95)), fill=mix(BG, WARM, 0.5 * a), width=6); cv.line((580, py(0.95)), (580, py(0.05)), fill=mix(BG, COOL, 0.5 * a), width=6)
    k = ease(seg(T.ta, -0.4, 0.3)); cv.text((190, 360), '2.56 s' if k < 0.5 else 't', size=60, fill=WHITE, mono=True, bold=True)
    cv.text((800, py(0.5)), 't', size=70, fill=mix(BG, WHITE, a), mono=True, bold=True)

@scene('B34')
def s_b34(cv, T):
    path_scene(cv, T, 0.5)
    a = ease(seg(T.tb, 0.0, 0.7)); b = ease(seg(T.tb, 0.7, 1.4))
    cv.line((150, 1330), (150 + 780 * a, 1330), fill=WHITE, width=24)            # bar = the whole out-and-back path (2d)
    cv.text((540, 1380), 't', size=44, mono=True, bold=True, fill=mix(BG, WHITE, a))
    if b > 0: cv.text((540, 1270), 't  x  c', size=64, mono=True, bold=True, fill=mix(BG, WARM, b))

@scene('B35')
def s_b35(cv, T):
    path_scene(cv, T, 0.5)
    f = ease(seg(T.tb, 0.0, 0.9))
    cv.line((150, 1330), (540, 1330), fill=WHITE, width=24)
    ex = 540 + 390 * math.cos(math.pi * f); ey = 1330 - 190 * math.sin(math.pi * f)
    cv.path([(540, 1330), ((540 + ex) / 2, (1330 + ey) / 2 - 20), (ex, ey)] if f < 1 else [(540, 1330), (150, 1330)], fill=WHITE, width=24)
    cv.text((540, 1090), 't x c  /  2' if f > 0.7 else 't x c', size=60, mono=True, bold=True, fill=WARM)
    cv.arrow((930, 1330), (150, 1330), 'bar folds in half')

@scene('B36')
def s_b36(cv, T):
    path_scene(cv, T, 0.4)
    f = ease(seg(T.tb, 0.0, 0.6)); cv.line((540, PATH_Y0), (540, lerp(PATH_Y0, PATH_Y1, f)), fill=WARM, width=10)
    for i in range(0, 11):
        y = lerp(PATH_Y0, PATH_Y1, i / 10)
        if i / 10 <= f: cv.line((560, y), (600 if i % 5 else 630, y), fill=WHITE, width=3)
    a = ease(seg(T.ta, -0.2, 0.4)); cv.text((780, 1000), 'd = 384,400 km', size=44, mono=True, bold=True, fill=mix(BG, WHITE, a)); cv.text((780, 1050), 'mean distance', size=28, mono=True, fill=mix(BG, GREY, a))

@scene('B37')
def s_b37(cv, T):
    space_bg(cv); earth(cv, True); moon(cv, (lerp(440, 600, T.u), lerp(420, 380, T.u)), 132)
    cv.arrow((440, 420), (600, 380), 'Moon drifts slowly')

@scene('B38')
def s_b38(cv, T):
    space_bg(cv); earth(cv, True); moon(cv, (600, 380), 132)
    p = ease(seg(T.t, 89.3, 90.0))
    if 0 < p < 1: pulse(cv, 540 + 40 * (1 - p), lerp(560, 1400, p), COOL, 0.55, trail=(0, -1), tlen=40)
    if p >= 1: cv.glow((540, 1400), 50, COOL, 60)

@scene('B39')
def s_b39(cv, T):
    space_bg(cv); earth(cv, True); moon(cv, (600, 380), 132); path_line(cv, 0.3)
    a = ease(seg(T.tb, 0.0, 0.9)); cv.line((650, PATH_Y0), (650, 380 + 132), fill=mix(BG, WARM, 0.8 * a), width=8)
    cv.tint((0, 0, W, H), (0, 0, 0), 255 * ease(seg(T.t, 92.5, 94.0)))


# ---------------------------------------------------------------- timeline
def load_beats():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'narration', 'NARRATION_BEAT_MAP.csv'))))
    vm = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'narration', 'NARRATION_TO_VISUAL_MAP.csv')))}
    beats = []
    for i, r in enumerate(rows):
        s = float(r['start_s']); e = float(rows[i + 1]['start_s']) if i + 1 < len(rows) else TOTAL
        beats.append(dict(id=r['id'], start=s, end=e, anchor=float(r['anchor_s']), text=r['spoken_text'], vm=vm.get(r['id'], {})))
    return beats

BEATS = load_beats()
SCENE_START = {'B05', 'B12', 'B14', 'B22', 'B26', 'B31', 'B37'}      # soft fade-in at scene changes

def beat_at(t):
    cur = BEATS[0]
    for b in BEATS:
        if b['start'] <= t + 1e-9: cur = b
    return cur

def wrap(txt, size, maxw):
    f = font(size, bold=True); words = txt.split(); lines = []; cur = ''
    for w in words:
        if f.getlength((cur + ' ' + w).strip()) <= maxw: cur = (cur + ' ' + w).strip()
        else: lines.append(cur); cur = w
    return lines + [cur]

def draw_caption(cv, text, size=52):
    lines = wrap(text, size, CAP[2] - CAP[0] - 60); h = len(lines) * (size + 10) + 24
    y0 = CAP[1] + 60
    cv.d.rounded_rectangle([CAP[0] + 10, y0, CAP[2] - 10, y0 + h], radius=22, fill=(0, 0, 0))
    cv.tint((CAP[0] + 10, y0, CAP[2] - 10, y0 + h), (0, 0, 0), 0)
    for i, l in enumerate(lines):
        cv.d.text((W / 2, y0 + 12 + i * (size + 10) + size / 2), l, font=font(size, bold=True), fill=WHITE, anchor='mm')

def render_scene(t, annotate=False):
    b = beat_at(t); T = Tm(t, b['start'], b['end'], b['anchor']); cv = Cv(annotate)
    SC[b['id']](cv, T); return cv, b, T

def render(t, annotate=False, captions=True, hud=True):
    cv, b, T = render_scene(t, annotate)
    if b['id'] in SCENE_START and T.tb < 0.25 and t > 0:
        prev = beat_at(b['start'] - 0.01); pcv, _, _ = render_scene(b['start'] - 0.01)
        cv.im = Image.blend(pcv.im, cv.im, ease(T.tb / 0.25)); cv.d = ImageDraw.Draw(cv.im)
    if captions and t < 92.6 and b['text']: draw_caption(cv, b['text'])
    if hud: cv.d.text((24, 18), '%s  %.2f s   ANIMATIC V0 (placeholders)' % (b['id'], t), font=font(22, mono=True), fill=(150, 156, 170))
    return cv, b, T

def frame_image(t, annotate=False): return render(t, annotate)[0].im

def build_video(fps=15, scale=0.5):
    out = os.path.join(ROOT, 'storyboard', 'animatic'); os.makedirs(out, exist_ok=True)
    frames = os.path.join(out, '_frames'); os.makedirs(frames, exist_ok=True)
    n = int(TOTAL * fps)
    for i in range(n):
        im = frame_image(i / fps).resize((int(W * scale), int(H * scale)), Image.LANCZOS); im.save(os.path.join(frames, 'f%05d.png' % i))
        if i % 150 == 0: print('frame', i, '/', n, flush=True)
    dst = os.path.join(out, 'ANIMATIC_V0_540x960_15fps.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(fps), '-i', os.path.join(frames, 'f%05d.png'),
                    '-i', os.path.join(ROOT, 'narration', 'raw', 'SLOT07_NARRATION_RAW.wav'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20',
                    '-af', 'apad', '-c:a', 'aac', '-b:a', '128k', '-t', str(TOTAL), dst], check=True)
    subprocess.run(['rm', '-rf', frames]); print('wrote', dst)

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'still': frame_image(float(sys.argv[2]), annotate=False).save(sys.argv[3])
    elif mode == 'video': build_video()
    elif mode == 'boards':
        import boards; boards.build()
