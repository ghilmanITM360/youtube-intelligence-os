"""Slot 07 look-development: shared compositing engine, photo-derived TEMPORARY assets, and the three treatment panels.

  ~/.venvs/uepipe/bin/python tools/lookdev.py assets      build/refresh look_dev/assets/*.png (cutouts, plate, spheres)
  ~/.venvs/uepipe/bin/python tools/lookdev.py panels      18 panels (3 treatments x 6 beats), contact sheets, comparison sheet

The engine half (Frame, Layer, Cam, sphere renderer, drawing helpers, asset loaders) is also imported by tools/animatic_v1.py,
so the look chosen in look_dev/LOOKDEV_DECISION.md is rendered by the same code that made the panels.

Photo-derived pixels come ONLY from public-domain NASA images listed in research/REFERENCE_MANIFEST.csv; every use is
recorded in look_dev/REFERENCE_USE.csv by `assets`. They are TEMPORARY animatic art, not final production assets.
"""
import csv, functools, math, os, random, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AS = os.path.join(ROOT, 'look_dev', 'assets')
W, H = 1080, 1920
SAFE = (60, 150, 1020, 1440)        # OUR provisional key-subject box (not a platform spec)
CAP = (60, 1480, 1020, 1730)        # OUR provisional caption band

# ----------------------------------------------------------------------------- palette (art direction section 4)
BG = (7, 11, 26); BG2 = (22, 34, 66)
WARM = (255, 172, 64); COOL = (96, 200, 255); WHITE = (230, 233, 240); GREY = (130, 138, 156); DIM = (58, 66, 88)
INK = (174, 180, 194); RED = (255, 98, 98)
SUN = np.array([-0.60, -0.42, 0.68]); SUN = SUN / np.linalg.norm(SUN)       # toward the Sun: left, above, slightly toward viewer


def lerp(a, b, x): return a + (b - a) * x
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def seg(t, a, b): return clamp((t - a) / (b - a)) if b > a else (1.0 if t >= b else 0.0)
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)                        # smoothstep (symmetric)
def eout(x): x = clamp(x); return 1 - (1 - x) ** 3                           # decelerate (arrival)
def ein(x): x = clamp(x); return x ** 2.2                                    # accelerate (departure)
def mix(c1, c2, x): return tuple(int(round(lerp(a, b, clamp(x)))) for a, b in zip(c1, c2))
def dim(c, k): return tuple(int(v * k) for v in c)


@functools.lru_cache(None)
def font(size, kind='bold'):
    sans = '/System/Library/Fonts/Avenir Next.ttc'
    idx = {'bold': 2, 'heavy': 8, 'reg': 7, 'med': 5, 'light': 10, 'ital': 4}
    if kind == 'mono': return ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', size, index=1)
    if kind == 'serif': return ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia.ttf', size)
    if kind == 'serifi': return ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia Italic.ttf', size)
    return ImageFont.truetype(sans, size, index=idx[kind])


# ----------------------------------------------------------------------------- frame + layers + camera
class Cam:
    """Virtual camera. (cx, cy) = point of the focal plane at screen centre, z = zoom. Layer factor p: 0 fixed to screen, 1 on the focal plane, >1 nearer."""
    def __init__(self, cx=W / 2, cy=H / 2, z=1.0): self.cx, self.cy, self.z = cx, cy, z
    def xf(self, p):
        s = 1 + (self.z - 1) * p
        return s, W / 2 + (W / 2 - (W / 2 + (self.cx - W / 2) * p)) * 0, (W / 2 + (self.cx - W / 2) * p), (H / 2 + (self.cy - H / 2) * p)
    def map(self, p, x, y):
        s, _, ex, ey = self.xf(p); return W / 2 + (x - ex) * s, H / 2 + (y - ey) * s


class Layer:
    """RGBA sprite placed at design position (x, y) (top-left, rest camera); res = sprite pixels per design unit."""
    def __init__(self, img, x, y, p=1.0, res=1.0, name=''):
        self.img, self.x, self.y, self.p, self.res, self.name = img.convert('RGBA'), x, y, p, res, name
        self.w, self.h = self.img.size[0] / res, self.img.size[1] / res


class Frame:
    def __init__(self, base=BG, size=(W, H)):
        self.im = Image.new('RGB', size, base) if not isinstance(base, Image.Image) else base.convert('RGB')
        self.d = ImageDraw.Draw(self.im, 'RGBA'); self.keys = []; self.cam = Cam()

    # --- layers
    def put(self, layer, cam=None, ox=0.0, oy=0.0, sc=1.0, anchor=None, alpha=1.0, blur=0.0, key=None):
        cam = cam or self.cam; s, _, ex, ey = cam.xf(layer.p)
        B = s * sc
        ax, ay = anchor if anchor else (W / 2, H / 2)
        x0 = W / 2 + (layer.x - ex) * s + ox; y0 = H / 2 + (layer.y - ey) * s + oy
        x0 = ax + (x0 - ax) * sc; y0 = ay + (y0 - ay) * sc                              # extra scale about anchor (screen space)
        dx1, dy1 = x0 + layer.w * B, y0 + layer.h * B
        if key: self.keys.append((key, (x0, y0, dx1, dy1)))
        ix0, iy0 = max(0, int(math.floor(x0))), max(0, int(math.floor(y0))); ix1, iy1 = min(self.im.size[0], int(math.ceil(dx1))), min(self.im.size[1], int(math.ceil(dy1)))
        if ix1 <= ix0 or iy1 <= iy0 or alpha <= 0: return (x0, y0, dx1, dy1)
        dw, dh = ix1 - ix0, iy1 - iy0; r = layer.res
        ext = ((ix0 - x0) / B * r, (iy0 - y0) / B * r, (ix1 - x0) / B * r, (iy1 - y0) / B * r)
        patch = layer.img.transform((dw, dh), Image.EXTENT, ext, Image.BILINEAR) if B > 0.55 * r or True else None
        if B / r < 0.5: patch = layer.img.resize((max(1, int(layer.w * B)), max(1, int(layer.h * B))), Image.LANCZOS).transform((dw, dh), Image.EXTENT, ((ix0 - x0), (iy0 - y0), (ix1 - x0), (iy1 - y0)), Image.BILINEAR)
        if blur > 0: patch = patch.filter(ImageFilter.GaussianBlur(blur))
        if alpha < 1: a = patch.getchannel('A').point(lambda v: int(v * alpha)); patch.putalpha(a)
        self.im.paste(patch, (ix0, iy0), patch); return (x0, y0, dx1, dy1)

    # --- vector drawing (design space, antialiased by the final 2x downsample)
    def line(self, pts, col=WHITE, w=6, a=1.0, cap=True):
        c = tuple(col) + (int(255 * a),)
        if len(pts) > 1: self.d.line(pts, fill=c, width=max(1, int(w)), joint='curve')
        if cap and w >= 4:
            for p in (pts[0], pts[-1]): self.d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=c)

    def dashed(self, p0, p1, col=GREY, w=4, dash=26, gap=18, a=1.0, off=0.0):
        L = math.dist(p0, p1)
        if L < 1: return
        ux, uy = (p1[0] - p0[0]) / L, (p1[1] - p0[1]) / L; s = -off % (dash + gap) - (dash + gap)
        while s < L:
            a0, a1 = max(0, s), min(L, s + dash)
            if a1 > a0: self.line([(p0[0] + ux * a0, p0[1] + uy * a0), (p0[0] + ux * a1, p0[1] + uy * a1)], col, w, a, cap=False)
            s += dash + gap

    def circle(self, c, r, fill=None, outline=None, w=2, a=1.0):
        f = tuple(fill) + (int(255 * a),) if fill else None; o = tuple(outline) + (int(255 * a),) if outline else None
        self.d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=f, outline=o, width=int(w))

    def poly(self, pts, fill=None, outline=None, a=1.0, w=2):
        f = tuple(fill) + (int(255 * a),) if fill else None; o = tuple(outline) + (int(255 * a),) if outline else None
        self.d.polygon(pts, fill=f, outline=o, width=int(w)) if o else self.d.polygon(pts, fill=f)

    def rrect(self, box, r, fill=None, outline=None, w=2, a=1.0):
        f = tuple(fill) + (int(255 * a),) if fill else None; o = tuple(outline) + (int(255 * a),) if outline else None
        self.d.rounded_rectangle(box, radius=r, fill=f, outline=o, width=int(w))

    def text(self, xy, s, size=40, col=WHITE, kind='bold', anchor='mm', a=1.0):
        self.d.text(xy, s, font=font(int(size), kind), fill=tuple(col) + (int(255 * a),), anchor=anchor)

    def glow(self, c, r, col, a=0.6, core=None):
        r = int(r); k = _glow_mask(r)
        m = k.point(lambda v: int(v * a)); self.im.paste(Image.new('RGB', k.size, col), (int(c[0]) - r, int(c[1]) - r), m)
        if core: self.circle(c, core, fill=mix(col, (255, 255, 255), 0.7))

    def veil(self, col, a, box=None):
        box = box or (0, 0) + self.im.size
        self.im.paste(Image.new('RGB', (int(box[2] - box[0]), int(box[3] - box[1])), col), (int(box[0]), int(box[1])), Image.new('L', (int(box[2] - box[0]), int(box[3] - box[1])), int(255 * clamp(a))))

    def key(self, name, box): self.keys.append((name, tuple(box)))


@functools.lru_cache(None)
def _glow_mask(r):
    yy, xx = np.mgrid[-r:r, -r:r].astype(np.float32); d = np.sqrt(xx * xx + yy * yy) / r
    return Image.fromarray((np.clip(1 - d, 0, 1) ** 2.2 * 255).astype(np.uint8))


# ----------------------------------------------------------------------------- reference access
MAN = None
def ref_path(rid):
    global MAN
    if MAN is None: MAN = {r['ref_id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'research', 'REFERENCE_MANIFEST.csv')))}
    return os.path.join(ROOT, MAN[rid]['local_filename'])

USED = {}
def ref_img(rid, why):
    USED[rid] = why; return Image.open(ref_path(rid)).convert('RGB')


def bleed(rgba, radius=7):
    """Fill RGB under low alpha with nearby colour so resampling does not fringe dark/light halos."""
    a = rgba[..., 3:4].astype(np.float32) / 255; rgb = rgba[..., :3].astype(np.float32)
    num = cv2.GaussianBlur(rgb * a, (0, 0), radius); den = cv2.GaussianBlur(a, (0, 0), radius)[..., None] + 1e-4
    fill = num / den; out = np.where(a > 0.98, rgb, a * rgb + (1 - a) * fill)
    return np.dstack([np.clip(out, 0, 255), rgba[..., 3]]).astype(np.uint8)


def poly_mask(shape, pts, feather=1.6, grow=0):
    m = np.zeros(shape[:2], np.uint8); cv2.fillPoly(m, [np.array(pts, np.int32)], 255)
    if grow > 0: m = cv2.dilate(m, np.ones((3, 3), np.uint8), iterations=grow)
    if grow < 0: m = cv2.erode(m, np.ones((3, 3), np.uint8), iterations=-grow)
    return cv2.GaussianBlur(m, (0, 0), feather) if feather else m


# ----------------------------------------------------------------------------- spheres: equirectangular photo/texture -> lit sphere
def _tex(rid, why, size=None):
    im = ref_img(rid, why)
    return np.array(im)

@functools.lru_cache(None)
def moon_tex(): return _tex('REF-MOON-013', 'Moon sphere texture (LROC colour map, equirectangular)')
@functools.lru_cache(None)
def earth_tex(): return _tex('REF-EARTH-013', 'Earth sphere texture (NASA SVS 3615 surface+clouds, equirectangular)')


def sphere_region(kind, R, box, lon0=0.0, lat0=0.0, light=SUN, ambient=None):
    """Orthographic sphere of radius R (px) centred at (0,0); render only pixel box (x0,y0,x1,y1) relative to the centre.
    kind 'moon' | 'earth'. Returns RGBA uint8. Soft terminator; Earth gets a thin cool atmosphere rim."""
    x0, y0, x1, y1 = box; xs = np.arange(x0, x1) + 0.5; ys = np.arange(y0, y1) + 0.5
    X, Y = np.meshgrid(xs, ys); rr = np.sqrt(X * X + Y * Y) / R
    inside = rr < 1; nx = X / R; ny = Y / R; nz = np.sqrt(np.clip(1 - nx * nx - ny * ny, 0, 1))
    tex = moon_tex() if kind == 'moon' else earth_tex(); th, tw = tex.shape[:2]
    Yv = -ny; Zv = nz; c, s = math.cos(lat0), math.sin(lat0)
    Yp = Yv * c + Zv * s; Zp = -Yv * s + Zv * c
    lat = np.arcsin(np.clip(Yp, -1, 1)); lon = np.arctan2(nx, Zp) + lon0
    mx = ((lon / (2 * math.pi) + 0.5) % 1.0 * tw).astype(np.float32); my = ((0.5 - lat / math.pi) * th).astype(np.float32)
    col = cv2.remap(tex, mx, my, cv2.INTER_CUBIC, borderMode=cv2.BORDER_WRAP).astype(np.float32) / 255
    dot = nx * light[0] + ny * light[1] + nz * light[2]
    if kind == 'moon':
        g = col.mean(-1, keepdims=True); col = g + (col - g) * 0.45                     # desaturate toward art-direction greys
        col = np.clip(col * 1.18 + 0.02, 0, 1) * np.array([0.98, 0.98, 1.0])
        sh = np.clip((dot + 0.06) / 0.42, 0, 1); sh = sh * sh * (3 - 2 * sh)
        amb = 0.045 if ambient is None else ambient
        lit = col * (sh[..., None] * 0.96 + amb * np.array([0.8, 0.9, 1.15]))
        lit *= (1 - 0.22 * np.clip((rr - 0.82) / 0.18, 0, 1))[..., None]               # limb falloff
    else:
        col = col * np.array([0.93, 0.98, 1.04])
        sh = np.clip((dot + 0.20) / 0.62, 0, 1); sh = sh * sh * (3 - 2 * sh)
        amb = 0.05 if ambient is None else ambient
        haze = (np.clip((rr - 0.80) / 0.20, 0, 1) ** 2.2)[..., None] * np.array([0.30, 0.55, 0.85]) * (0.25 + 0.75 * sh[..., None])
        lit = col * (sh[..., None] * 1.0 + amb * np.array([0.5, 0.8, 1.6])) + haze * 0.55
        if True:                                                                       # thin atmosphere rim outside the disc
            rim = np.clip(1 - (rr - 1) / 0.028, 0, 1) ** 2 * (rr >= 1) * (0.25 + 0.75 * np.clip(dot + 0.4, 0, 1))
            lit = np.where(inside[..., None], lit, np.array([0.38, 0.78, 1.0]) * rim[..., None])
    alpha = np.where(inside, np.clip((1 - rr) * R, 0, 1), 0.0)
    if kind == 'earth': alpha = np.maximum(alpha, np.clip(1 - (rr - 1) / 0.028, 0, 1) ** 2 * (rr >= 1) * 0.7 * (0.2 + 0.8 * np.clip(dot + 0.4, 0, 1)))
    return bleed(np.dstack([np.clip(lit, 0, 1) * 255, alpha * 255]).astype(np.uint8), 3)


@functools.lru_cache(None)
def sphere_sprite(kind, r_design, res=2, lon0=0.0, lat0=0.0, ambient=None):
    """Full sphere sprite with a small margin for the rim. Returns (Image, margin_design)."""
    R = r_design * res; m = int(R * 0.05) + 2
    return Image.fromarray(sphere_region(kind, R, (-R - m, -R - m, R + m, R + m), lon0, lat0, ambient=ambient)), m / res


def sphere_layer(kind, c, r, p=1.0, res=2, lon0=0.0, lat0=0.0, ambient=None, name=''):
    im, m = sphere_sprite(kind, r, res, lon0, lat0, ambient); return Layer(im, c[0] - r - m, c[1] - r - m, p, res, name or kind)


@functools.lru_cache(None)
def earth_cap_layer(R=1300, cx=540, cy=2700, top=1330, res=1.5):
    """The top cap of a very large Earth (limb at y = cy - R), authored only for the visible strip."""
    box = (-int((cx + 160) * res), int((top - cy) * res), int((W - cx + 160) * res), int((H - cy) * res))
    im = Image.fromarray(sphere_region('earth', R * res, box, lon0=0.25, lat0=-1.02))
    return Layer(im, cx - 0 + box[0] / res, cy + box[1] / res, 1.0, res, 'earth_cap')


# ----------------------------------------------------------------------------- photo-derived TEMPORARY cutouts / plate
ASTRO_POLY = [(98, 210), (100, 180), (112, 150), (140, 120), (190, 106), (240, 120), (268, 148), (282, 170), (285, 125), (298, 100), (335, 90), (370, 92), (392, 100),
              (402, 130), (410, 200), (440, 235), (468, 290), (485, 380), (490, 470), (482, 520), (450, 545), (395, 555), (380, 575), (372, 640), (372, 700), (392, 790),
              (408, 860), (405, 915), (392, 945), (330, 975), (290, 968), (255, 988), (215, 985), (208, 962), (240, 940), (272, 915), (278, 880), (248, 830), (228, 780),
              (205, 720), (205, 650), (212, 610), (185, 625), (150, 632), (118, 598), (108, 580), (135, 545), (148, 500), (138, 430), (124, 380), (122, 330), (128, 310),
              (148, 290), (142, 255), (122, 245), (110, 240)]
RETRO_POLY = [(112, 292), (200, 222), (300, 150), (400, 103), (480, 112), (495, 108), (600, 128), (640, 165), (660, 200), (668, 300), (668, 400), (672, 412), (640, 440),
              (580, 490), (520, 520), (430, 525), (350, 520), (300, 500), (240, 490), (190, 470), (150, 440), (100, 420), (0, 425), (0, 405), (20, 398), (190, 365), (160, 345), (115, 310)]


def _cached(name, build):
    p = os.path.join(AS, name)
    if os.path.exists(p): return Image.open(p)
    os.makedirs(AS, exist_ok=True); im = build(); im.save(p); return im


def build_astronaut():
    src = np.array(ref_img('REF-ASTRO-003', 'astronaut cutout (side profile, sun from the left)'))[560:1680, 1300:1900]
    m = poly_mask(src.shape, ASTRO_POLY, feather=1.2, grow=-2)
    g = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY); keep = (g > 72).astype(np.uint8) * 255
    keep[:565] = 255; keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    a = (m.astype(np.float32) * (cv2.GaussianBlur(keep, (0, 0), 1.0).astype(np.float32) / 255)).astype(np.uint8)
    ys, xs = np.where(a > 8); box = (xs.min() - 6, ys.min() - 6, xs.max() + 6, ys.max() + 6)
    rgba = bleed(np.dstack([src, a]))[max(0, box[1]):box[3], max(0, box[0]):box[2]]
    return Image.fromarray(rgba)


def _shadow_poly_native():                                   # shadow blob left of the reflector in REF-RETRO-001 (crop coords)
    return [(30, 470), (130, 440), (300, 425), (360, 445), (330, 480), (190, 510), (60, 505)]


def build_reflector():
    full = np.array(ref_img('REF-RETRO-001', 'reflector cutout (Apollo 11 LRRR as deployed; flipped so the Sun is on the left)'))
    crop = full[640:1300, 780:1620]
    m = poly_mask(crop.shape, RETRO_POLY, feather=0, grow=-1)
    g = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)
    face = poly_mask(crop.shape, [(112, 292), (400, 103), (480, 112), (548, 150), (292, 352)], feather=0)
    arm = poly_mask(crop.shape, [(0, 405), (190, 366), (196, 388), (0, 428)], feather=0)
    keep = ((g > 112).astype(np.uint8) * 255); keep = cv2.morphologyEx(keep, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)); keep = cv2.max(cv2.max(keep, face), arm)
    keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, np.ones((33, 33), np.uint8))
    m = cv2.GaussianBlur(cv2.min(m, keep), (0, 0), 1.3)
    rgba = bleed(np.dstack([crop, m]))
    ys, xs = np.where(m > 8); rgba = rgba[max(0, ys.min() - 4):ys.max() + 4, max(0, xs.min() - 4):xs.max() + 4]
    return Image.fromarray(rgba[:, ::-1].copy())            # flip: shadows fall to the right


def build_plate():
    """Ground plate: REF-RETRO-001 with the reflector removed (cloned regolith), flipped, horizon mask, single tile."""
    full = np.array(ref_img('REF-RETRO-001', 'ground plate (regolith + footprints), reflector cloned out, flipped'))
    h, w = full.shape[:2]
    hole = poly_mask(full.shape, [(x + 780, y + 640) for x, y in RETRO_POLY], feather=0, grow=26)
    sh = poly_mask(full.shape, [(x + 780, y + 640) for x, y in _shadow_poly_native()], feather=0, grow=30)
    hole = cv2.max(hole, sh)
    donor = full[1500:1500 + 700, 1000:1000 + 1000].copy()                 # plain regolith near the camera
    dm = full[1180:1180 + 700, 760:760 + 1000].astype(np.float32)           # the area around the hole, for colour matching
    scale = np.clip(dm.mean((0, 1)) / (donor.astype(np.float32).mean((0, 1)) + 1), 0.6, 1.4)
    don = np.clip(donor.astype(np.float32) * scale, 0, 255)
    fill = full.astype(np.float32).copy(); ys, xs = np.where(hole > 0); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    hh, ww = y1 - y0, x1 - x0
    if don.shape[0] >= hh and don.shape[1] >= ww: patch = don[:hh, :ww]                          # native-scale clone (no stretching)
    else:
        big = np.tile(don, (int(np.ceil(hh / don.shape[0])), int(np.ceil(ww / don.shape[1])), 1)); patch = big[:hh, :ww]
    sm = cv2.GaussianBlur(hole, (0, 0), 16)[y0:y1, x0:x1].astype(np.float32)[..., None] / 255
    fill[y0:y1, x0:x1] = fill[y0:y1, x0:x1] * (1 - sm) + patch * sm
    ground = np.clip(fill, 0, 255).astype(np.uint8)[:, ::-1]                # flip -> Sun on the left
    crop = ground[200:, :1650]                                              # drop the lander (now upper right) and most sky
    g = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY); skym = (g < 34).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(skym); keep = np.zeros_like(skym)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_TOP] == 0 and st[i, cv2.CC_STAT_AREA] > 400: keep[lab == i] = 1
    keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8)); keep[: int(crop.shape[0] * 0.42)] = np.maximum(keep[: int(crop.shape[0] * 0.42)], 0)
    alpha = cv2.GaussianBlur(((1 - keep) * 255).astype(np.uint8), (0, 0), 1.3)
    pad = 420; xo = 120; ov = 150; w0 = crop.shape[1]                                  # extend right by cloning a different part of the tile (no mirror symmetry), cross-faded
    donor = crop[:, xo:xo + pad + ov].astype(np.float32); da = alpha[:, xo:xo + pad + ov]
    t = np.clip(np.arange(ov) / ov, 0, 1)[None, :, None]
    blend = crop[:, w0 - ov:].astype(np.float32) * (1 - t) + donor[:, :ov] * t
    ext = np.concatenate([crop[:, :w0 - ov].astype(np.float32), blend, donor[:, ov:]], 1)
    ea = np.concatenate([alpha[:, :w0 - ov], alpha[:, w0 - ov:], da[:, ov:]], 1)
    return Image.fromarray(np.dstack([np.clip(ext, 0, 255).astype(np.uint8), ea]))


def astronaut_sprite(): return _cached('astronaut_apollo11_side_cutout_TEMP.png', build_astronaut)
def reflector_sprite(): return _cached('reflector_apollo11_cutout_flipped_TEMP.png', build_reflector)
def plate_sprite(): return _cached('lunar_ground_plate_TEMP.png', build_plate)
PLATE_CW = 1650     # native width of one tile


# ----------------------------------------------------------------------------- procedural environment layers (shared by every look)
def _noise1d(n, seed, octaves=5, rough=0.5):
    rg = np.random.RandomState(seed); out = np.zeros(n)
    for o in range(octaves):
        k = 2 ** (o + 2); pts = rg.randn(k + 2) * (rough ** o); out += np.interp(np.linspace(0, k, n), np.arange(k + 2), pts)
    return out


def sky_layer(style='photo', w=1300, h=2300, horizon=0.64):
    horizon = min(horizon, 0.99)
    y = np.linspace(0, 1, h)[:, None]; top = np.array([7, 11, 26.]); mid = np.array([14, 22, 46.]); hz = np.array([28, 44, 82.])
    t = np.clip(y / horizon, 0, 1) ** 1.6
    col = np.where(y < horizon, top + (hz - top) * t[..., None] if False else (top + (hz - top) * t), hz)
    img = np.repeat(col[:, None, :] if col.ndim == 2 else col[:, None, :], w, 1).reshape(h, w, 3)
    if style == 'flat':
        img = (img // 14) * 14 + 7
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))


def stars_layer(w=1400, h=2400, n=260, seed=7, res=2):
    rg = random.Random(seed); im = Image.new('RGBA', (w * res, h * res), (0, 0, 0, 0)); d = ImageDraw.Draw(im, 'RGBA')
    for _ in range(n):
        x, y = rg.uniform(0, w), rg.uniform(0, h * 0.62); b = int(rg.choice([90, 120, 150, 190, 230])); r = rg.choice([0.8, 1.0, 1.2, 1.6, 2.1]) * res
        d.ellipse([x * res - r, y * res - r, x * res + r, y * res + r], fill=(b, b, min(255, b + 28), 255))
    return im


def ridge_layer(seed, base, amp, col_far, col_near, w=1300, h=1000, rough=0.55, style='photo', haze=0.0):
    """Silhouette ridge filling downward; returns Layer-ready RGBA (w x h) with the ridge line near y = base."""
    n = _noise1d(w, seed, 6, rough); n = (n - n.mean()) / (np.abs(n).max() + 1e-6)
    top = base + n * amp
    if style == 'flat': top = np.round(top / 40) * 40 + n * 0   # flat look: chunky stepped silhouette removed below
    yy = np.arange(h)[:, None]; inside = yy >= top[None, :]
    g = np.clip((yy - top[None, :]) / 260, 0, 1)
    c = np.array(col_far)[None, None, :] * (1 - g[..., None]) + np.array(col_near)[None, None, :] * g[..., None]
    a = (inside * 255).astype(np.uint8)
    im = np.dstack([c.repeat(1, 0).reshape(h, w, 3), a]).astype(np.uint8)
    if style != 'flat': im[..., 3] = cv2.GaussianBlur(im[..., 3], (0, 0), 1.0)
    return Image.fromarray(im)


@functools.lru_cache(None)
def dome_sprite(style='photo', res=2):
    """Generic observatory (no real site): box base + hemisphere dome, shutter slit region left transparent-free (slit drawn per frame by dome_slit)."""
    Wd, Hd = 760, 660; im = Image.new('RGBA', (Wd * res, Hd * res), (0, 0, 0, 0)); R = 215 * res; cx, cy = 380 * res, 300 * res
    Y, X = np.mgrid[0:Hd * res, 0:Wd * res].astype(np.float32); nx = (X - cx) / R; ny = (Y - cy) / R; r2 = nx * nx + ny * ny
    inside = (r2 < 1) & (Y < cy + 4 * res); nz = np.sqrt(np.clip(1 - r2, 0, 1))
    L = np.array([-0.45, -0.55, 0.70]); L /= np.linalg.norm(L)                       # faint cool top light from the sky side (never the Sun)
    dot = np.clip(nx * L[0] + ny * L[1] + nz * L[2], 0, 1)
    base = np.array([132, 142, 166.]); shade = (0.10 + 0.78 * dot ** 1.3)[..., None]
    col = base * shade + np.array([6, 10, 22.]) * (1 - shade)
    if style == 'flat': col = np.where(dot[..., None] > 0.55, np.array([150, 160, 184.]), np.array([84, 94, 122.]))
    arr = np.zeros((Hd * res, Wd * res, 4), np.float32); arr[..., :3] = col; arr[..., 3] = inside * 255
    # ribs (panel seams)
    for k in range(-5, 6):
        xx = cx + k * R * 0.17
        rib = np.abs((X - xx) - (X - cx) * 0.0) < 1.2 * res
        arr[..., :3] = np.where((rib & inside)[..., None], arr[..., :3] * 0.72, arr[..., :3])
    # building
    bx0, bx1, by0, by1 = int(cx - 270 * res), int(cx + 270 * res), int(cy), int(cy + 175 * res)
    bl = np.array([46, 52, 70.]); arr[by0:by1, bx0:bx1, :3] = bl; arr[by0:by1, bx0:bx1, 3] = 255
    arr[by0:by1, bx0:bx0 + 10 * res, :3] = [74, 82, 104]; arr[by0:by0 + 8 * res, bx0:bx1, :3] = [64, 72, 94]
    # ring beam under the dome + door light (cool work-light)
    arr[by0 - 6 * res:by0 + 6 * res, int(cx - R):int(cx + R), :3] = [88, 96, 118]; arr[by0 - 6 * res:by0 + 6 * res, int(cx - R):int(cx + R), 3] = 255
    dx0, dx1 = int(cx - 200 * res), int(cx - 150 * res); arr[by0 + 40 * res:by1, dx0:dx1, :3] = [18, 22, 34]
    out = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(out, 'RGBA')
    for k in range(5):                                                                  # catwalk rail
        d.line([(bx1, by0 + 10 * res + k * 0), (bx1 + 60 * res, by0 + 10 * res)], fill=(70, 78, 98, 255), width=3 * res) if k == 0 else None
    d.line([(bx1, by0 + 30 * res), (bx1 + 70 * res, by0 + 30 * res)], fill=(70, 78, 98, 255), width=2 * res)
    d.line([(bx1 + 70 * res, by0 + 30 * res), (bx1 + 70 * res, by1)], fill=(70, 78, 98, 255), width=2 * res)
    return out


DOME_C = (380, 300); DOME_R = 215        # inside dome_sprite, design units


def dome_slit(f, layer, cam, open_=1.0, tilt=0.0, sky_col=(18, 28, 56), lamp=0.0, dy=0.0, a=1.0):
    """Draw the shutter slit + telescope silhouette on a dome layer instance (screen space via camera)."""
    s, _, ex, ey = cam.xf(layer.p)
    def S(x, y): return (W / 2 + (layer.x + x - ex) * s, H / 2 + (layer.y + y - ey) * s + dy)
    cx, cy = DOME_C; R = DOME_R; hw = 44 * open_; xo = 0.0
    if hw < 1: return
    top = cy - math.sqrt(R * R - (xo * 1.0) ** 2)
    poly = [S(cx + xo - hw, cy - 40), S(cx + xo - hw * 0.78, cy - R * 0.97), S(cx + xo + hw * 0.78, cy - R * 0.97), S(cx + xo + hw, cy - 40)]
    f.poly(poly, fill=sky_col, a=a)
    f.line([poly[0], poly[1]], (70, 78, 100), 4 * s, a, cap=False); f.line([poly[3], poly[2]], (70, 78, 100), 4 * s, a, cap=False)
    # telescope tube (silhouette, clipped to slit by drawing only inside via mask)
    mask = Image.new('L', f.im.size, 0); ImageDraw.Draw(mask).polygon(poly, fill=255)
    tube = Image.new('RGBA', f.im.size, (0, 0, 0, 0)); td = ImageDraw.Draw(tube, 'RGBA')
    p0 = S(cx, cy - 20); L = 150 * s; ux, uy = math.sin(tilt), -math.cos(tilt)
    p1 = (p0[0] + ux * L, p0[1] + uy * L); nx_, ny_ = -uy, ux; wd = 17 * s
    td.polygon([(p0[0] + nx_ * wd, p0[1] + ny_ * wd), (p1[0] + nx_ * wd, p1[1] + ny_ * wd), (p1[0] - nx_ * wd, p1[1] - ny_ * wd), (p0[0] - nx_ * wd, p0[1] - ny_ * wd)], fill=(26, 32, 48, 255))
    td.line([(p0[0] + nx_ * wd, p0[1] + ny_ * wd), (p1[0] + nx_ * wd, p1[1] + ny_ * wd)], fill=(96, 108, 136, 255), width=max(2, int(3 * s)))      # moonlit rim (upper-left)
    td.ellipse([p1[0] - wd, p1[1] - wd * 0.35, p1[0] + wd, p1[1] + wd * 0.35], fill=(12, 16, 28, 255))
    f.im.paste(tube, (0, 0), ImageChops.multiply(tube.getchannel('A'), mask).point(lambda v: int(v * a)))
    return p1


def foreground_layer(seed=3, w=1300, h=420, style='photo'):
    """Dark near-ground silhouette with rocks and an antenna mast (sits mostly in the caption band: allowed, it is not a key subject)."""
    rg = random.Random(seed); im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im, 'RGBA')
    n = _noise1d(w, seed, 4, 0.5); top = 130 + n * 22
    d.polygon([(0, h)] + [(x, top[x]) for x in range(0, w, 4)] + [(w, h)], fill=(5, 7, 13, 255))
    for _ in range(9):
        x = rg.uniform(30, w - 30); y = top[int(x)] + rg.uniform(-4, 40); r = rg.uniform(20, 60)
        d.ellipse([x - r, y - r * 0.55, x + r, y + r * 0.6], fill=(8, 10, 18, 255)); d.arc([x - r, y - r * 0.55, x + r, y + r * 0.6], 200, 290, fill=(40, 52, 78, 255), width=3)
    mx = 150; d.line([(mx, top[mx] + 6), (mx, top[mx] - 190)], fill=(9, 12, 20, 255), width=6); d.line([(mx - 30, top[mx] - 130), (mx + 30, top[mx] - 130)], fill=(9, 12, 20, 255), width=3)
    d.ellipse([mx - 5, top[mx] - 200, mx + 5, top[mx] - 190], fill=(255, 90, 90, 255)) if False else None
    return im


# ----------------------------------------------------------------------------- final grade + shared small helpers
@functools.lru_cache(None)
def _vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H * 0.46) / (H * 0.7)) ** 2)
    return np.clip(1 - 0.30 * np.clip(r - 0.35, 0, 1) ** 1.5, 0.6, 1)[..., None]


def grade(im, vig=True, lift=(1.0, 1.0, 1.02)):
    a = np.asarray(im).astype(np.float32)
    if vig: a = a * _vignette()
    a = a * np.array(lift)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def to_out(im): return im.resize((W // 2, H // 2), Image.LANCZOS)


# ============================================================================= WORLD BUILDERS (photo-based look, shared with the animatic)
@functools.lru_cache(None)
def ground_layers(style='photo'):
    L = {}
    L['sky'] = Layer(sky_layer(style, 1300, 3400, 0.5), -110, -300, 0.97, 1, 'sky')
    L['stars'] = Layer(stars_layer(1400, 3400, 420 if style != 'flat' else 90), -160, -330, 0.96, 2, 'stars')
    L['ridge_far'] = Layer(ridge_layer(11, 150, 70, (36, 52, 88), (14, 20, 38), 1500, 2200, 0.55, style), -210, 1075, 0.94, 1, 'ridge_far')
    L['ridge_near'] = Layer(ridge_layer(23, 120, 55, (15, 22, 40), (7, 10, 20), 1500, 2200, 0.60, style), -210, 1190, 0.97, 1, 'ridge_near')
    L['dome'] = Layer(dome_sprite(style, 2), 160, 880, 1.0, 2, 'dome')
    L['fg'] = Layer(foreground_layer(3, 1500, 1600, style), -210, 1330, 1.10, 1, 'fg')
    return L


def moon_glow(f, c, r, a=0.18):
    f.glow(c, r * 2.6, (70, 96, 150), a)


def draw_ground(f, cam, moon_c=(540, 430), moon_r=150, open_=1.0, tilt=0.0, moon_a=1.0, with_fg=True, style='photo'):
    L = ground_layers(style)
    f.put(L['sky'], cam); f.put(L['stars'], cam)
    s, _, ex, ey = cam.xf(0.9)
    mc = (W / 2 + (moon_c[0] - ex) * s, H / 2 + (moon_c[1] - ey) * s)
    if moon_a > 0:
        moon_glow(f, mc, moon_r * s, 0.20 * moon_a)
        ml = sphere_layer('moon', (0, 0), moon_r, 0.9, res=2)
        f.put(Layer(ml.img, moon_c[0] - moon_r - 4, moon_c[1] - moon_r - 4, 0.9, 2, 'moon'), cam, alpha=moon_a)
    f.put(L['ridge_far'], cam); f.put(L['ridge_near'], cam)
    f.put(L['dome'], cam); tip = dome_slit(f, L['dome'], cam, open_, tilt)
    if with_fg: f.put(L['fg'], cam)
    return dict(moon=mc, moon_r=moon_r * s, tip=tip)


@functools.lru_cache(None)
def stars_space(seed=5):
    return Layer(stars_layer(1400, 2500, 220, seed, 2), -160, -330, 0.1, 2, 'space_stars')


def draw_schematic_world(f, cam, moon_c=(540, 430), moon_r=150, earth=True, moon=True, stars=True, earth_dim=1.0):
    f.im.paste(Image.new('RGB', f.im.size, BG))
    if stars: f.put(stars_space(), cam, alpha=0.75)
    if earth:
        el = earth_cap_layer(); f.put(el, cam, alpha=earth_dim)
    if moon:
        s, _, ex, ey = cam.xf(0.9); mc = (W / 2 + (moon_c[0] - ex) * s, H / 2 + (moon_c[1] - ey) * s)
        moon_glow(f, mc, moon_r * s, 0.10)
        ml = sphere_layer('moon', (0, 0), moon_r, 0.9, res=2)
        f.put(Layer(ml.img, moon_c[0] - moon_r - 4, moon_c[1] - moon_r - 4, 0.9, 2, 'moon'), cam)


# --- lunar surface: plate (placed so the horizon sits at HZ) + reflector + astronaut
PS = 0.74                      # plate design units per native pixel
PLATE_X0, PLATE_Y0 = -431, 606  # plate top-left at rest
RFL_NATIVE = (893, 543, 676, 429)   # reflector bbox in flipped plate coords: x, y, w, h (w/h = sprite size)
FS = 0.72                      # foreground-object scale relative to the plate (reflector / astronaut)


def surface_points():
    """Design-space contact points for the reflector base centre and the astronaut stance (rest camera)."""
    rx = PLATE_X0 + (RFL_NATIVE[0] + RFL_NATIVE[2] * 0.52) * PS; ry = PLATE_Y0 + (RFL_NATIVE[1] + RFL_NATIVE[3] * 0.92) * PS
    return (rx, ry)


@functools.lru_cache(None)
def surface_layers():
    L = {}
    pl = plate_sprite(); L['plate'] = Layer(pl, PLATE_X0, PLATE_Y0, 1.0, 1 / PS, 'plate')
    # layered depth: a far strip (slower) and a near strip (faster) cut from the same plate, with soft overlap
    h = pl.size[1]; far = pl.copy(); a = np.array(far); fade = np.clip((int(h * 0.50) - np.arange(h)) / (h * 0.30), 0, 1)[:, None]; a[..., 3] = (a[..., 3] * fade).astype(np.uint8)
    near = pl.copy(); b = np.array(near); fade2 = np.clip((np.arange(h) - int(h * 0.12)) / (h * 0.28), 0, 1)[:, None]; b[..., 3] = (b[..., 3] * fade2).astype(np.uint8)
    L['plate_far'] = Layer(Image.fromarray(a), PLATE_X0, PLATE_Y0, 0.94, 1 / PS, 'plate_far')
    L['plate_near'] = Layer(Image.fromarray(b), PLATE_X0, PLATE_Y0, 1.0, 1 / PS, 'plate_near')
    return L


def refl_layer(cam_p=1.0):
    r = reflector_sprite(); rx, ry = surface_points(); k = FS * PS
    return Layer(r, rx - r.size[0] * k / 2, ry - r.size[1] * k, cam_p, 1 / k, 'reflector')


def astro_layer(x, y, cam_p=1.0, k=None):
    a = astronaut_sprite(); k = k or 0.60                       # design units per native pixel (astronaut ~ 545 px tall)
    return Layer(a, x - a.size[0] * k * 0.55, y - a.size[1] * k, cam_p, 1 / k, 'astronaut')


def contact_shadow(f, cam, p, c, w, h, a=0.55, dx=0.35):
    """Hard-edged shadow falling to the right (Sun on the left); three stacked layers give a darker core near the contact."""
    x, y = cam.map(p, *c); s = cam.xf(p)[0]; w *= s * 0.62; h *= s
    for k, al in ((1.0, 0.45), (0.72, 0.35), (0.45, 0.30)):
        f.poly([(x - w * 0.40, y - h * 0.12), (x + w * (0.30 + 0.9 * k), y + h * 0.30 * k), (x + w * (0.40 + 0.9 * k), y + h * (0.55 + 0.1 * k)), (x - w * 0.30, y + h * 0.36)], fill=(3, 3, 5), a=a * al * 1.1)


def draw_surface(f, cam, refl=1.0, astro=None, ghost=0.0, astro_pose=0.0, sprite_shadow=True, dust=None, style='photo'):
    f.im.paste(Image.new('RGB', f.im.size, (0, 0, 0)))
    SL = surface_layers(); f.put(stars_space(11), cam, alpha=0.0)
    f.put(SL['plate_far'], cam); f.put(SL['plate_near'], cam)
    rl = refl_layer(1.0); rx, ry = surface_points()
    if refl > 0:
        contact_shadow(f, cam, 1.0, (rx + 30, ry - 6), 330, 60, 0.5 * refl)
        f.put(rl, cam, alpha=refl, key='reflector')
    if astro is not None:
        ax, ay = astro; contact_shadow(f, cam, 1.0, (ax + 20, ay - 4), 190, 44, 0.55)
        f.put(astro_layer(ax, ay, 1.0), cam, key='astronaut')


# ----------------------------------------------------------------------------- scientific graphics (code-drawn; the second visual language)
TOK = {
    'A': dict(sw=3, lab='serifi', num='serif', glow=1.0, dash=(18, 14), cap=False, face=(200, 205, 214)),
    'B': dict(sw=14, lab='heavy', num='heavy', glow=0.0, dash=(34, 22), cap=True, face=(240, 244, 252)),
    'C': dict(sw=7, lab='bold', num='mono', glow=0.8, dash=(26, 18), cap=True, face=WHITE),
}


def bead(f, x, y, col, size=1.0, trail=(0, 1), tlen=90, T=TOK['C'], a=1.0):
    for i in range(1, 10):
        q = 1 - i / 10; f.circle((x + trail[0] * tlen * i / 9, y + trail[1] * tlen * i / 9), 9 * size * q, fill=col, a=0.55 * q * a)
    if T['glow']: f.glow((x, y), 50 * size, col, 0.5 * T['glow'] * a)
    f.circle((x, y), 12 * size, fill=mix(col, (255, 255, 255), 0.55), a=a)


def stopwatch(f, c, r, val, full=3.0, T=TOK['C'], digits=True, a=1.0, hand_col=WARM, face_fill=(18, 26, 52), big=1.0):
    f.circle(c, r, fill=face_fill, outline=T['face'], w=max(3, T['sw'] - 1), a=a)
    for i in range(60):
        q = i / 60 * 2 * math.pi - math.pi / 2; l = 0.17 if i % 5 == 0 else 0.07
        f.line([(c[0] + math.cos(q) * r * (0.90 - l), c[1] + math.sin(q) * r * (0.90 - l)), (c[0] + math.cos(q) * r * 0.90, c[1] + math.sin(q) * r * 0.90)], GREY, 2 if i % 5 else 3, a, cap=False)
    q = (val / full) * 2 * math.pi - math.pi / 2
    f.line([c, (c[0] + math.cos(q) * r * 0.70, c[1] + math.sin(q) * r * 0.70)], hand_col, max(4, T['sw']), a)
    f.circle(c, 8, fill=T['face'], a=a)
    f.rrect((c[0] - r * 0.12, c[1] - r - r * 0.16, c[0] + r * 0.12, c[1] - r + 4), 4, fill=T['face'], a=a)
    if digits: f.text((c[0], c[1] + r * 0.46), '%.2f' % val, int(r * 0.34 * big), T['face'], 'mono' if T['num'] == 'mono' else T['num'], a=a)


def path_y(p, y0=1400, y1=580): return lerp(y0, y1, p)


def partial_path(pts, frac):
    tot = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)); need = tot * clamp(frac); out = [pts[0]]
    for i in range(len(pts) - 1):
        l = math.dist(pts[i], pts[i + 1])
        if need >= l: out.append(pts[i + 1]); need -= l
        else:
            q = need / l if l else 0; out.append((lerp(pts[i][0], pts[i + 1][0], q), lerp(pts[i][1], pts[i + 1][1], q))); break
    return out


def _hit(p, d, q0, q1):
    ex, ey = q1[0] - q0[0], q1[1] - q0[1]; den = d[0] * ey - d[1] * ex
    if abs(den) < 1e-9: return None
    t = ((q0[0] - p[0]) * ey - (q0[1] - p[1]) * ex) / den; s = ((q0[0] - p[0]) * d[1] - (q0[1] - p[1]) * d[0]) / den
    return t if (t > 1e-6 and -1e-6 <= s <= 1 + 1e-6) else None


def cube_geo(cx=540, cy=980, L=420):
    V = (cx, cy + L * 0.55); return V, (V[0] + L, V[1] - L), (V[0] - L, V[1] - L)


def corner_ray(V, A, B, x0, ang_deg, L=420):
    """2-D cross-section: ray enters from above, reflects once on each face (two right-angle faces), leaves anti-parallel."""
    a = math.radians(ang_deg); d = (math.sin(a), math.cos(a)); p = (x0, V[1] - L - 90); pts = [p]
    for _ in range(2):
        best = None
        for q0, q1 in ((V, A), (V, B)):
            t = _hit(p, d, q0, q1)
            if t and (best is None or t < best[0]): best = (t, q0, q1)
        if not best: break
        t, q0, q1 = best; p = (p[0] + d[0] * t, p[1] + d[1] * t); pts.append(p)
        ex, ey = q1[0] - q0[0], q1[1] - q0[1]; n = math.hypot(ex, ey); ex, ey = ex / n, ey / n; dd = d[0] * ex + d[1] * ey; d = (2 * dd * ex - d[0], 2 * dd * ey - d[1])
    lin = math.dist(pts[0], pts[1]) if len(pts) > 1 else 300; pts.append((p[0] + d[0] * lin, p[1] + d[1] * lin)); return pts


def cube_diagram(f, prog, rays, cx=540, cy=980, L=420, T=TOK['C'], a=1.0, dimmed=0.22, flip=None, wscale=1.0):
    """prog counts rays one by one; finished rays stay dimmed. flip=Y0 mirrors the drawing vertically (y -> Y0 - y) so light enters from below
    (film grammar: Earth at the bottom). Returns the active ray's current tip."""
    V, A, B = cube_geo(cx, cy, L); P = (lambda p: (p[0], flip - p[1])) if flip is not None else (lambda p: p)
    f.poly([P(V), P(A), P((A[0], A[1] - 70)), P((B[0], B[1] - 70)), P(B)], fill=(40, 60, 110), a=0.42 * a)               # glass wedge
    f.poly([P(V), P(A), P((A[0] - 190, A[1] - 12)), P((V[0], V[1] - 250))], fill=(120, 170, 230), a=0.10 * a)           # soft sheen toward the light
    f.line([P(A), P(V), P(B)], (170, 214, 238), T['sw'] * 1.8 * wscale, a, cap=True)
    last = None
    for i, (xo, ang) in enumerate(rays):
        loc = clamp(prog - i)
        if loc <= 0: continue
        active = (prog - i) < 1; k = 1.0 if active else dimmed; pts = [P(q) for q in corner_ray(V, A, B, cx + xo, ang, L)]
        w = T['sw'] * (1.4 if active else 1.1) * wscale
        f.line(partial_path(pts[:3], ease(seg(loc, 0, 0.5))), WARM, w, a * k)
        if loc > 0.5: f.line(partial_path(pts[2:], ease(seg(loc, 0.5, 1.0))), COOL, w, a * k)
        if active: last = partial_path(pts, ease(loc))[-1]
    return last


def hist_bins(n, sharp=1.0, peak=0.64, x0=140, x1=940, bw=16, seed=21, sig=0.45):
    rg = np.random.RandomState(seed); n = int(n); g = rg.randn(900); s = rg.rand(900) < sig; nz = rg.rand(900)
    xs = np.where(s, x0 + (x1 - x0) * peak + g * 40 * sharp, x0 + 20 + (x1 - x0 - 40) * nz)[:n]
    b = np.floor((xs - x0) / bw).astype(int); out = {}
    for k in b: out[k] = out.get(k, 0) + 1
    return out


def hist_draw(f, n, T=TOK['C'], y0=1250, x0=140, x1=940, sharp=1.0, scale=9, bw=16, peak_col=COOL, a=1.0):
    f.line([(x0, y0), (x1, y0)], GREY, max(3, T['sw'] - 2), a, cap=False)
    for i in range(9): f.line([(x0 + (x1 - x0) * i / 8, y0), (x0 + (x1 - x0) * i / 8, y0 + 14)], GREY, 3, a, cap=False)
    px = x0 + (x1 - x0) * 0.64
    for b, c in hist_bins(n, sharp, x0=x0, x1=x1, bw=bw).items():
        h = min(560, c * scale); bx = x0 + b * bw; near = abs(bx - px) < 130
        f.rrect((bx + 1, y0 - h - 3, bx + bw - 2, y0 - 3), 3 if T['cap'] else 0, fill=mix(peak_col, WHITE, 0.15) if near else dim(peak_col, 0.55), a=a)


def bracket(f, x, y0, y1, col=WHITE, T=TOK['C'], a=1.0, side=1, tick=30):
    f.line([(x - side * tick, y0), (x, y0), (x, y1), (x - side * tick, y1)], col, T['sw'], a)


# ============================================================================= FLAT (Treatment B) world pieces
def flat_ground(f, moon_c=(540, 430), moon_r=150, open_=1.0, tilt=0.0):
    f.im.paste(Image.new('RGB', f.im.size, (14, 22, 52)))
    f.rrect((0, 0, W, 1100), 0, fill=(10, 16, 40)); f.rrect((0, 540, W, 1100), 0, fill=(18, 28, 64), a=0.6)
    f.circle(moon_c, moon_r, fill=(214, 218, 230)); f.circle((moon_c[0] + 70, moon_c[1] + 30), moon_r * 0.92, fill=(14, 20, 46))        # flat gibbous: lit disc minus a dark offset disc
    f.circle(moon_c, moon_r, outline=(214, 218, 230), w=3)
    for x, y, r in [(-60, -40, 22), (-20, 40, 30), (-90, 30, 14)]: f.circle((moon_c[0] + x, moon_c[1] + y), r, fill=(176, 182, 200))
    f.poly([(0, 1250), (220, 1130), (420, 1220), (700, 1090), (1080, 1230), (1080, 1920), (0, 1920)], fill=(30, 46, 98))
    f.poly([(0, 1400), (300, 1290), (620, 1370), (1080, 1300), (1080, 1920), (0, 1920)], fill=(20, 30, 70))
    f.rrect((290, 1250, 790, 1400), 0, fill=(70, 86, 140)); f.d.pieslice([325, 1030, 755, 1460], 180, 360, fill=(226, 232, 248))
    f.d.pieslice([540, 1030, 755, 1460], 270, 360, fill=(170, 182, 214))
    hw = 40 * open_; f.poly([(540 - hw, 1245), (540 - hw * 0.8, 1040), (540 + hw * 0.8, 1040), (540 + hw, 1245)], fill=(10, 16, 40))
    f.line([(540, 1245), (540 + 120 * math.sin(tilt + 0.08), 1245 - 120 * math.cos(tilt + 0.08))], (240, 244, 252), 30)


def flat_planet(f, c, r, kind='moon'):
    if kind == 'moon': f.circle(c, r, fill=(214, 218, 230)); f.circle((c[0] + r * 0.46, c[1] + r * 0.2), r * 0.90, fill=(12, 20, 48)); f.circle(c, r, outline=(214, 218, 230), w=3)
    else:
        f.circle(c, r, fill=(30, 98, 190)); f.circle((c[0] - r * 0.25, c[1] - r * 0.4), r * 0.35, fill=(60, 150, 100)); f.circle((c[0] + r * 0.25, c[1] - r * 0.1), r * 0.28, fill=(70, 150, 110))
        f.circle(c, r, outline=(120, 210, 255), w=8)


def flat_surface(f, astro=True, refl=True):
    f.im.paste(Image.new('RGB', f.im.size, (6, 8, 20)))
    f.poly([(0, 780), (1080, 740), (1080, 1920), (0, 1920)], fill=(150, 156, 176)); f.poly([(0, 1100), (1080, 1020), (1080, 1920), (0, 1920)], fill=(120, 126, 150))
    f.poly([(0, 1500), (1080, 1440), (1080, 1920), (0, 1920)], fill=(98, 104, 130))
    if refl:
        f.poly([(560, 1250), (900, 1250), (850, 1120), (610, 1120)], fill=(236, 240, 250)); f.poly([(610, 1120), (850, 1120), (840, 1070), (640, 1070)], fill=(40, 52, 96))
        for i in range(5):
            for j in range(2): f.circle((660 + i * 40, 1090 + j * 22 + (0)), 11, fill=(120, 190, 235))
        f.poly([(900, 1250), (1040, 1290), (960, 1300), (860, 1262)], fill=(70, 76, 100))
    if astro:
        x, y = 360, 1300
        f.poly([(x - 20, y), (x + 220, y + 30), (x + 200, y + 56), (x - 40, y + 30)], fill=(70, 76, 100))
        f.rrect((x - 36, y - 190, x + 36, y - 20), 24, fill=(246, 248, 252)); f.rrect((x - 22, y - 30, x - 2, y + 14), 8, fill=(236, 240, 248)); f.rrect((x + 6, y - 30, x + 30, y + 14), 8, fill=(236, 240, 248))
        f.rrect((x + 24, y - 220, x + 74, y - 70), 12, fill=(196, 204, 224)); f.circle((x - 2, y - 238), 44, fill=(250, 251, 254)); f.d.ellipse([x - 38, y - 256, x + 12, y - 214], fill=(214, 170, 70))
        f.line([(x - 26, y - 150), (x - 90, y - 100)], (240, 244, 252), 22)


# ============================================================================= THREE TREATMENTS x SIX BEATS (stills)
def painterly(im, ss=38, sr=0.28, glaze=0.14, soft=1.0):
    """Treatment A world filter: mean-shift gouache simplification (flat tonal patches, edges kept), a little source detail restored,
    tonal glaze (warm upper-left, cool lower-right), no grain, no outline strokes (art direction)."""
    a = cv2.cvtColor(np.array(im.resize((W // 2, H // 2), Image.LANCZOS)), cv2.COLOR_RGB2BGR)
    m = cv2.pyrMeanShiftFiltering(a, sp=9, sr=22, maxLevel=2); m = cv2.bilateralFilter(m, 7, 30, 7)
    s = cv2.addWeighted(m, 0.72, cv2.GaussianBlur(a, (0, 0), 1.6), 0.28, 0)
    s = cv2.resize(cv2.cvtColor(s, cv2.COLOR_BGR2RGB), (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
    s = cv2.GaussianBlur(s, (0, 0), 1.1)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); t = np.clip((xx / W * 0.5 + yy / H * 0.5), 0, 1)[..., None]
    g = np.array([255, 196, 140.]) * (1 - t) + np.array([70, 110, 190.]) * t
    s = s * (1 - glaze) + (s * g / 200.0) * glaze
    return Image.fromarray(np.clip(s, 0, 255).astype(np.uint8))


@functools.lru_cache(None)
def array_photo():
    im = ref_img('REF-RETRO-006', 'array macro (Apollo 14 LRRR close-up; reference only, temporary)').crop((20, 60, 650, 800))
    return im


def array_window(f, box, T, flat=False, a=1.0):
    x0, y0, x1, y1 = box
    if flat:                                                                    # B: simplified 10 x 10 array, flat shapes
        f.poly([(x0 + 40, y0 + 30), (x1 - 10, y0), (x1 - 40, y1 - 40), (x0, y1)], fill=(226, 232, 248))
        for i in range(10):
            for j in range(10):
                u, v = (i + 0.5) / 10, (j + 0.5) / 10
                px = lerp(lerp(x0 + 80, x1 - 40, u), lerp(x0 + 42, x1 - 80, u), v); py = lerp(lerp(y0 + 60, y0 + 30, u), lerp(y1 - 90, y1 - 60, u), v)
                f.circle((px, py), 17, fill=(40, 64, 140)); f.circle((px - 4, py - 4), 7, fill=(110, 170, 230))
        return
    im = array_photo().resize((x1 - x0, y1 - y0), Image.LANCZOS); m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], 40, fill=255)
    f.im.paste(im, (x0, y0), m); f.rrect((x0, y0, x1, y1), 40, outline=(60, 72, 104), w=3)


def captionless_tag(f, xy, s, T, col=GREY, size=26):
    f.text(xy, s, size, col, T['lab'] if T['lab'] != 'serifi' else 'serifi')


def p_ground(tr):
    f = Frame(); cam = Cam()
    if tr == 'B': flat_ground(f)
    else: draw_ground(f, cam)
    im = grade(f.im, vig=(tr != 'B'))
    return painterly(im) if tr == 'A' else im


def p_roundtrip(tr):
    T = TOK[tr]; f = Frame()
    if tr == 'B':
        f.im.paste(Image.new('RGB', f.im.size, (12, 20, 48))); flat_planet(f, (540, 430), 150, 'moon'); f.circle((540, 2700), 1300, fill=(30, 98, 190)); f.circle((540, 2700), 1300, outline=(120, 210, 255), w=10)
        f.poly([(0, 1560), (240, 1470), (540, 1420), (840, 1470), (1080, 1560), (1080, 1920), (0, 1920)], fill=(60, 150, 100), a=0.0)
        base = f.im
    else:
        draw_schematic_world(f, Cam()); base = f.im
        if tr == 'A': f.im = painterly(grade(f.im)); f.d = ImageDraw.Draw(f.im, 'RGBA')
    y0, y1 = 1400, 590
    if tr == 'A':
        f.dashed((540, y0), (540, y1), (190, 196, 210), 2, 16, 14, 0.9)
        f.line([(500, y0 - 20), (500, y1 + 40)], WARM, 3, 0.9); f.line([(580, y1 + 40), (580, y0 - 20)], COOL, 3, 0.9)
    else:
        f.dashed((540, y0), (540, y1), GREY, T['sw'] - 2, T['dash'][0], T['dash'][1], 0.9)
        f.line([(500, y0 - 20), (500, y1 + 50)], WARM, T['sw'] * 1.2, 1); f.poly([(500, y1 + 20), (478, y1 + 66), (522, y1 + 66)], fill=WARM)
        f.line([(580, y1 + 50), (580, y0 - 20)], COOL, T['sw'] * 1.2, 1); f.poly([(580, y0 - 14), (558, y0 - 60), (602, y0 - 60)], fill=COOL)
    bead(f, 580, y0 - 120, COOL, 1.0, (0, -1), 80, T)
    stopwatch(f, (190, 250), 100, 2.56, T=T, face_fill=(18, 26, 52) if tr != 'B' else (26, 44, 100))
    if tr == 'A': f.text((860, 250), '2.56 s', 76, (226, 230, 238), 'serif')
    else: f.text((860, 250), '2.56 s', 78 if tr == 'B' else 70, T['face'], 'heavy' if tr == 'B' else 'mono')
    captionless_tag(f, (880, 1360), 'not to scale' if tr != 'B' else 'NOT TO SCALE', T)
    return grade(f.im, vig=(tr != 'B'))


def p_surface(tr):
    f = Frame(); rx, ry = surface_points()
    if tr == 'B': flat_surface(f); return f.im
    draw_surface(f, Cam(), astro=(rx + 330, ry + 90)); im = grade(f.im)
    return painterly(im, 34, 0.30, 0.16) if tr == 'A' else im


def p_optics(tr):
    T = TOK[tr]; f = Frame(); f.im.paste(Image.new('RGB', f.im.size, BG if tr != 'B' else (12, 20, 48)))
    rays = ((-250, 10), (-30, 20), (230, -10))
    if tr == 'B':
        array_window(f, (180, 150, 900, 700), T, flat=True)
        f.circle((650, 400), 74, outline=(255, 255, 255), w=10); f.line([(600, 440), (160, 962)], (255, 255, 255), 8); f.line([(700, 450), (920, 962)], (255, 255, 255), 8)
        cube_diagram(f, 1.55, rays, cy=1150, L=380, T=T)
        return f.im
    array_window(f, (150, 170, 930, 800), T)
    f.circle((330, 300), 54, outline=WHITE, w=T['sw']); f.line([(292, 338), (160, 962)], WHITE, T['sw'] - 3, 0.7); f.line([(372, 338), (920, 962)], WHITE, T['sw'] - 3, 0.7)
    cube_diagram(f, 1.55, rays, cy=1200, L=380, T=T)
    im = grade(f.im)
    if tr == 'A':
        im = painterly(im, 30, 0.26, 0.10); f = Frame(im)                      # painterly world, then thin hairline re-ink of the diagram
        f.circle((330, 300), 54, outline=(230, 232, 238), w=3); cube_diagram(f, 1.55, rays, cy=1200, L=380, T=T, a=0.95); im = f.im
    return im


def p_hist(tr):
    T = TOK[tr]; f = Frame(); f.im.paste(Image.new('RGB', f.im.size, BG if tr != 'B' else (12, 20, 48)))
    if tr != 'B': f.put(stars_space(9), Cam(), alpha=0.45)
    if tr == 'A':
        for i, (x, y) in enumerate([(300, 560), (520, 700), (760, 520), (420, 900), (640, 860)]): f.glow((x, y), 70, COOL, 0.35); f.circle((x, y), 9, fill=(230, 244, 255))
        hist_draw(f, 330, T, 1250, 140, 940, 0.55, 9, 16, COOL, 0.95)
        f.im = f.im.filter(ImageFilter.GaussianBlur(1.1)); f.d = ImageDraw.Draw(f.im, 'RGBA'); f.text((900, 330), 'pulses  1,320', 34, (190, 196, 210), 'serifi', 'rm')
    elif tr == 'B':
        for i, (x, y) in enumerate([(300, 560), (520, 700), (760, 520)]): f.circle((x, y), 26, fill=COOL)
        hist_draw(f, 330, T, 1250, 140, 940, 0.55, 12, 20, COOL, 1.0); f.text((900, 330), '1,320', 84, (255, 255, 255), 'heavy', 'rm'); f.text((900, 400), 'PULSES', 34, COOL, 'heavy', 'rm')
    else:
        for i, (x, y) in enumerate([(300, 560), (520, 700), (760, 520)]): f.glow((x, y), 60, COOL, 0.6); f.circle((x, y), 12, fill=(214, 240, 255))
        hist_draw(f, 330, T, 1250, 140, 940, 0.55, 9, 16, COOL, 1.0); f.text((940, 330), 'pulses  1,320', 34, GREY, 'mono', 'rm')
    return grade(f.im, vig=(tr != 'B'))


def fold_bar(f, T, fold, y=1290, x0=150, x1=930, ymid=None, a=1.0, cool_half=True, w=None):
    """Bar of the whole out-and-back path (warm outbound half + cool return half), return half rotating about the midpoint by fold (0..1)."""
    w = w or T['sw'] * 3.2; xm = (x0 + x1) / 2
    f.line([(x0, y), (xm, y)], WARM, w, a)
    q = math.pi * fold; ex, ey = xm + (x1 - xm) * math.cos(q), y - (x1 - xm) * math.sin(q) * 0.55
    f.line([(xm, y), (ex, ey)], COOL, w, a)
    return (ex, ey)


def p_fold(tr):
    T = TOK[tr]; f = Frame()
    if tr == 'B':
        f.im.paste(Image.new('RGB', f.im.size, (12, 20, 48))); flat_planet(f, (540, 330), 90, 'moon'); f.circle((540, 2200), 1000, fill=(30, 98, 190), a=0.35)
    else:
        draw_schematic_world(f, Cam(), moon_r=100, moon_c=(540, 330), earth_dim=0.55)
        if tr == 'A': f.im = painterly(grade(f.im)); f.d = ImageDraw.Draw(f.im, 'RGBA')
    y0, y1 = 1400, 440
    f.dashed((540, y0), (540, y1), GREY, max(2, T['sw'] - 3), T['dash'][0], T['dash'][1], 0.35)
    f.line([(500, y0), (500, y1)], WARM, max(2, T['sw'] - 2), 0.30); f.line([(580, y1), (580, y0)], COOL, max(2, T['sw'] - 2), 0.30)        # the peeled-off legs (ghost of the traced path)
    fold_bar(f, T, 0.38, 1290)
    f.text((340, 1190), 't  x  c', 64 if tr != 'B' else 76, T['face'] if tr != 'A' else (226, 230, 238), 'mono' if tr == 'C' else ('serif' if tr == 'A' else 'heavy'))
    f.text((760, 1190), '/ 2', 64 if tr != 'B' else 76, WARM, 'mono' if tr == 'C' else ('serif' if tr == 'A' else 'heavy'))
    return grade(f.im, vig=(tr != 'B'))


PANELS = [('B01', p_ground, 'B01 observatory + Moon (ground view)'), ('B07', p_roundtrip, 'B07 round-trip schematic, 2.56 s'), ('B17', p_surface, 'B17 reflector + astronaut'),
          ('B19-20', p_optics, 'B19-B20 array to corner-cube optics'), ('B26-27', p_hist, 'B26-B27 faint photons, histogram'), ('B34-35', p_fold, 'B34-B35 round-trip bar folds to one-way')]
TREAT = {'A': 'A  Illustrated science documentary', 'B': 'B  Premium educational motion graphics', 'C': 'C  Hybrid cinematic science explainer'}


def build_panels():
    out = os.path.join(ROOT, 'look_dev', 'panels'); os.makedirs(out, exist_ok=True); got = {}
    for tr in 'ABC':
        for key, fn, _ in PANELS:
            im = to_out(fn(tr)); p = os.path.join(out, 'treatment_%s_%s.png' % (tr, key.replace('-', '_'))); im.save(p); got[(tr, key)] = im
        sh = Image.new('RGB', (270 * 6 + 14 * 7, 480 + 90), (20, 22, 30)); d = ImageDraw.Draw(sh)
        d.text((14, 10), 'Treatment ' + TREAT[tr], font=font(30, 'bold'), fill=(235, 238, 245))
        d.text((14, 50), 'same six beats; 540x960 panels shown at 50%; stills only', font=font(18, 'reg'), fill=(150, 156, 170))
        for i, (key, _, lab) in enumerate(PANELS):
            sh.paste(got[(tr, key)].resize((270, 480), Image.LANCZOS), (14 + i * 284, 82)); d.text((14 + i * 284, 566), lab[:34], font=font(14, 'reg'), fill=(150, 156, 170))
        sh.save(os.path.join(out, 'contact_sheet_%s.png' % tr))
    cs = Image.new('RGB', (270 * 6 + 14 * 7 + 110, 3 * (480 + 52) + 220), (20, 22, 30)); d = ImageDraw.Draw(cs)
    d.text((14, 8), 'Comparison: A (illustrated documentary) / B (motion graphics) / C (hybrid)  -  rows = treatments, columns = beats; bottom strip = 90x160 thumbnails', font=font(22, 'bold'), fill=(235, 238, 245))
    for r, tr in enumerate('ABC'):
        y = 44 + r * 532; d.text((8, y + 220), tr, font=font(64, 'heavy'), fill=(235, 190, 90))
        for i, (key, _, lab) in enumerate(PANELS): cs.paste(got[(tr, key)].resize((270, 480), Image.LANCZOS), (110 + i * 284, y))
    ty = 44 + 3 * 532 + 10; d.text((8, ty), 'thumbnail test (90x160, as seen in a feed)', font=font(18, 'reg'), fill=(150, 156, 170))
    for r, tr in enumerate('ABC'):
        d.text((8, ty + 34 + r * 172 + 60), tr, font=font(40, 'heavy'), fill=(235, 190, 90))
        for i, (key, _, lab) in enumerate(PANELS): cs.paste(got[(tr, key)].resize((90, 160), Image.LANCZOS), (110 + i * 284, ty + 30 + r * 172))
    cs.save(os.path.join(out, 'comparison_sheet.png')); print('panels done')


def write_reference_use():
    p = os.path.join(ROOT, 'look_dev', 'REFERENCE_USE.csv')
    with open(p, 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['ref_id', 'licence_status', 'local_filename', 'used_for', 'status'])
        STATIC = {'REF-ASTRO-003': 'astronaut cutout (side profile, sun from the left)', 'REF-RETRO-001': 'reflector cutout + ground plate (Apollo 11 LRRR as deployed; reflector cloned out of the plate; flipped so the Sun is on the left)'}
        for rid, why in STATIC.items(): USED.setdefault(rid, why)
        for rid, why in sorted(USED.items()): w.writerow([rid, MAN[rid]['licence_status'], MAN[rid]['local_filename'], why, 'TEMPORARY animatic/look-dev art, not a final asset'])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'panels'
    if cmd == 'assets': astronaut_sprite(); reflector_sprite(); plate_sprite(); moon_tex(); earth_tex(); array_photo(); write_reference_use()
    elif cmd == 'panels': build_panels(); write_reference_use()
