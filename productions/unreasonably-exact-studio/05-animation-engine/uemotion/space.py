"""Earth-Moon schematic, ruler / scale bar, directional path indicators, light-pulse bead, badges.
Geometry is a NON-SCALE schematic (declared by an always-visible 'not to scale' mark)."""
import math
import numpy as np
import cv2
from PIL import Image
from . import tokens as T
from .easing import clamp, lerp, seg, smoothstep

# =============================================================== procedural textures (equirectangular, tileable in x)
_tex_cache = {}
def _fbm(w, h, seed, octaves=5, base=(4, 2), gain=0.55):
    key = ('fbm', w, h, seed, octaves, base)
    if key in _tex_cache: return _tex_cache[key]
    rng = np.random.default_rng(seed); out = np.zeros((h, w), np.float32); amp = 1.0; tot = 0
    for o in range(octaves):
        gw, gh = base[0] * 2 ** o, base[1] * 2 ** o
        g = np.tile(rng.random((gh, gw)).astype(np.float32), (1, 3))              # tile x3 so the crop wraps seamlessly
        big = cv2.resize(g, (w * 3, h), interpolation=cv2.INTER_CUBIC)
        out += amp * big[:, w:2 * w]; tot += amp; amp *= gain
    out = out / tot; out = (out - out.min()) / (out.max() - out.min()); _tex_cache[key] = out; return out

def _moon_albedo(w=1024, h=512):
    key = ('moon', w, h)
    if key in _tex_cache: return _tex_cache[key]
    base = _fbm(w, h, 11, 6, (4, 2)); mare = _fbm(w, h, 12, 3, (3, 2))
    alb = 0.62 + 0.30 * (base - 0.5)
    alb = alb * (1 - 0.38 * smooth_arr(mare, 0.52, 0.62))             # dark maria
    rng = np.random.default_rng(3); img = (alb * 255).astype(np.uint8)
    for _ in range(46):
        cx, cy = int(rng.uniform(0, w)), int(h * (0.5 + rng.uniform(-0.28, 0.28))); r = int(rng.uniform(5, 22))
        cv2.circle(img, (cx, cy), r, int(np.clip(alb.mean() * 255 + 22, 0, 255)), 1, cv2.LINE_AA)   # bright rim
        cv2.circle(img, (cx + 1, cy + 1), max(1, r - 2), int(alb.mean() * 255 * 0.86), -1, cv2.LINE_AA)
    img = cv2.GaussianBlur(img, (0, 0), 1.0); _tex_cache[key] = img.astype(np.float32) / 255; return _tex_cache[key]

def smooth_arr(x, a, b): t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)

def _earth_tex(w=4096, h=2048):
    key = ('earth', w, h)
    if key in _tex_cache: return _tex_cache[key]
    land = smooth_arr(_fbm(w, h, 21, 7, (3, 2)), 0.56, 0.60)
    _tex_cache[key] = land; return land

def _cloud_tex(w=4096, h=2048):
    key = ('cloud', w, h)
    if key in _tex_cache: return _tex_cache[key]
    c = smooth_arr(_fbm(w, h, 33, 7, (6, 3)), 0.56, 0.80); _tex_cache[key] = c; return c

# ---- validated texture layers (candidates; provenance in assets/*/_build_report.json, cloud composite report)
import os as _os
_ASSETS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))), 'assets')
REAL_TEX = {'earth': 'earth/earth_surface_4096x2048.png', 'clouds': 'earth/earth_clouds_codexcomp_4096x2048.png',
            'night': 'earth/earth_night_lights_4096x2048.png', 'moon': 'moon/moon_globe_4096x2048.png'}

def real_tex(name):
    """uint8 equirectangular map (lon -180..180 left to right). RGB for earth/moon, alpha only for clouds/night."""
    key = ('real', name)
    if key not in _tex_cache:
        im = Image.open(_os.path.join(_ASSETS, REAL_TEX[name]))
        _tex_cache[key] = np.ascontiguousarray(np.asarray(im.convert('RGBA'))[..., 3] if name in ('clouds', 'night') else np.asarray(im.convert('RGB')))
    return _tex_cache[key]

def preload_real():
    for k in REAL_TEX: real_tex(k)

def _sample(tex, lon, lat, real=False):
    h, w = tex.shape[:2]
    mx = (((lon + (math.pi if real else 0)) / (2 * math.pi)) % 1.0) * (w - 1); my = (0.5 - lat / math.pi) * (h - 1)
    return cv2.remap(tex, mx.astype(np.float32), my.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_WRAP)


def sphere_rgba(cv, c, r, kind, lon0=0.0, cloud_lon=0.0, sun=T.SUN, atmosphere=True, tilt=0.0):
    """Shaded sphere region visible on the canvas as an RGBA array. ONE sun vector (tokens.SUN) lights Earth and Moon:
    Lambert + soft terminator. Earth gets continents/clouds and an atmosphere rim that brightens toward the sun."""
    x, y = cv.P(*c); R = cv.L(r)
    halo = max(2.0, R * 0.035) if (kind == 'earth' and atmosphere) else 2.0
    x0, y0, x1, y1 = int(max(0, x - R - halo)), int(max(0, y - R - halo)), int(min(cv.w, x + R + halo + 1)), int(min(cv.h, y + R + halo + 1))
    if x1 <= x0 or y1 <= y0: return None
    yy, xx = np.mgrid[y0:y1, x0:x1].astype(np.float32)
    u, v = (xx - x) / R, (yy - y) / R; r2 = u * u + v * v; rr = np.sqrt(r2)
    nz = np.sqrt(np.clip(1 - r2, 0, 1)); ndl = u * sun[0] + v * sun[1] + nz * sun[2]
    lit = smooth_arr(ndl, -0.10, 0.45)
    inside = np.clip((1 - rr) * R + 0.5, 0, 1)                                        # 1-px AA edge at working res
    # tilt = rotation about the screen x axis (radians, + tips the north pole away from the viewer)
    yv = -v; y2 = yv * math.cos(tilt) - nz * math.sin(tilt); z2 = yv * math.sin(tilt) + nz * math.cos(tilt)
    lat = np.arcsin(np.clip(y2, -1, 1)); lon = np.arctan2(u, z2) + lon0
    rgb = np.zeros(r2.shape + (3,), np.float32)
    if kind == 'moon':
        alb = _sample(real_tex('moon'), lon, lat, real=True).astype(np.float32)[..., :1] / 255     # LROC albedo (grey)
        ramp = 0.04 + 0.96 * lit[..., None]
        rgb = np.array(T.MOONC, np.float32) * np.clip(alb * 1.55, 0, 1.15) * ramp + np.array((8, 10, 16), np.float32) * (1 - lit[..., None])
        alpha = inside
    else:
        L = lit[..., None]
        surf = _sample(real_tex('earth'), lon, lat, real=True).astype(np.float32)                     # NASA Blue Marble base
        night = _sample(real_tex('night'), lon, lat, real=True).astype(np.float32)[..., None] / 255  # Black Marble lights
        rgb = surf * (0.03 + 0.97 * L) + np.array((255, 196, 120), np.float32) * night * 0.55 * np.clip(1 - L * 3, 0, 1)
        cl = _sample(real_tex('clouds'), lon + cloud_lon, lat, real=True).astype(np.float32)[..., None] / 255 * 0.9
        rgb = rgb * (1 - cl) + np.array((226, 234, 245), np.float32) * (0.18 + 0.82 * lit[..., None]) * cl
        rim = (np.clip(1 - nz, 0, 1) ** 3.0)[..., None] * (0.25 + 0.75 * lit[..., None]) * np.array((70, 150, 255), np.float32) * 0.9
        rgb = rgb + rim
        alpha = inside
        if atmosphere:                                                                 # outside the limb: thin glow, sun side brighter
            dh = np.clip((rr - 1) * R / halo, 0, 1)
            sunside = 0.25 + 0.75 * smooth_arr(u * sun[0] + v * sun[1], -0.2, 0.7)
            ga = (1 - dh) ** 2.2 * 0.75 * sunside * (rr > 1)
            rgb = np.where((rr > 1)[..., None], np.array(T.COOL, np.float32), rgb)
            alpha = np.maximum(alpha, ga)
    out = np.zeros(r2.shape + (4,), np.uint8); out[..., :3] = np.clip(rgb, 0, 255); out[..., 3] = np.clip(alpha * 255, 0, 255)
    return out, x0, y0

def draw_sphere(cv, c, r, kind, alpha=1.0, **kw):
    res = sphere_rgba(cv, c, r, kind, **kw)
    if res is None: return
    arr, x0, y0 = res
    if alpha < 1: arr[..., 3] = (arr[..., 3] * alpha).astype(np.uint8)
    cv.blit_array(arr, x0, y0)


# =============================================================== schematic geometry
# Apache Point Observatory (APOLLO lunar ranging station), 32.78 N, 105.82 W (claims ledger / research atlas)
STATION_LAT, STATION_LON = math.radians(32.78), math.radians(-105.82)
STATION_TILT = math.pi / 2 - STATION_LAT        # puts the station exactly on the top limb (point (0,1,0))

class EarthMoonGeo:
    """Vertical schematic: Earth bottom, Moon top (rule 2). 'earth_top' = y of the limb at x=cx (the launch site)."""
    def __init__(self, cx=540, earth_top=1400, earth_r=1300, moon_y=430, moon_r=150):
        self.cx, self.earth_top, self.earth_r, self.moon_y, self.moon_r = cx, earth_top, earth_r, moon_y, moon_r
        self.earth_c = (cx, earth_top + earth_r); self.moon_c = (cx, moon_y)
        self.y_launch = earth_top - 6                    # pulse leaves from just above the limb station
        self.y_moon = moon_y + moon_r                    # pulse touches the lunar near side (surface facing Earth)
    def lane_x(self, lane): return self.cx + {'out': -26, 'ret': 26, 'mid': 0}[lane]
    def y_at(self, p): return lerp(self.y_launch, self.y_moon, p)      # p = 0 Earth ... 1 Moon
    def pos(self, p, lane='mid'): return (self.lane_x(lane), self.y_at(p))

def draw_earth_moon(cv, geo, t=0.0, cloud_rate=0.012, station=True, moon_alpha=1.0):
    draw_sphere(cv, geo.earth_c, geo.earth_r, 'earth', cloud_lon=t * cloud_rate, lon0=STATION_LON, tilt=STATION_TILT)
    draw_sphere(cv, geo.moon_c, geo.moon_r, 'moon', alpha=moon_alpha)
    if station:                                                          # tiny launch-site mark on the limb
        cv.circle((geo.cx, geo.earth_top - 2), 7, fill=T.WHITE); cv.circle((geo.cx, geo.earth_top - 2), 13, outline=T.GREY, width=2)

# V3: scenes no longer draw their own disclosure pills. The film draws each necessary disclosure ONCE, small and in sentence case,
# from the DISCLOSURES table in animation/roughcut.py. Proof clips rendered on their own keep the old marks (INLINE_DISCLOSURES = True).
INLINE_DISCLOSURES = True

def disclosure(cv, text, xy=(60, 150), alpha=1.0, anchor='lm', size=34):
    """V3 disclosure: small sentence-case note, no pill, no outline. Soft dark halo keeps it legible on bright art."""
    if alpha <= 0: return
    cv.text(xy, text, size, T.mix(T.GREY, T.WHITE, 0.35), anchor=anchor, bold=True, alpha=0.82 * alpha)

def not_to_scale_mark(cv, xy=(120, 150), alpha=1.0):
    """The single 'not to scale' disclosure (declared model: non-scale schematic)."""
    if not INLINE_DISCLOSURES: return
    cv.text(xy, 'NOT TO SCALE', 30, T.GREY, anchor='lm', bold=True, alpha=alpha)
    w = cv.text_width('NOT TO SCALE', 30, bold=True)
    cv.polyline([(xy[0] - 6, xy[1] + 24), (xy[0] + w + 6, xy[1] + 24)], T.GREY, 2, alpha=alpha * 0.8, dash=(6, 6))

def badge(cv, xy, text, size=30, color=T.GREY, fill=T.PANEL, alpha=1.0, anchor='lm', pad=(18, 12), bold=True):
    """pill label. anchor 'lm': xy = left-middle; 'rm': xy = right-middle; 'mm': centred. Returns (x0, x1)."""
    if not INLINE_DISCLOSURES: return (xy[0], xy[0])      # V3: every pill in the film is a disclosure; the film draws them from one table
    w = cv.text_width(text, size, bold=bold) + 2 * pad[0]
    x0 = xy[0] if anchor == 'lm' else (xy[0] - w if anchor == 'rm' else xy[0] - w / 2)
    cv.rect((x0, xy[1] - size / 2 - pad[1], x0 + w, xy[1] + size / 2 + pad[1]), fill=fill, outline=color, width=2, radius=size, alpha=alpha)
    cv.text((x0 + pad[0], xy[1]), text, size, color, anchor='lm', bold=bold, alpha=alpha)
    return (x0, x0 + w)


# =============================================================== ruler / scale bar
def ruler(cv, p0, p1, ticks=10, major=5, color=T.GREY, width=4, fill=0.0, fill_color=T.WHITE, label=None, label_size=34,
          label_offset=(60, 0), alpha=1.0, side=1):
    """Scientific ruler between two points: end caps, minor/major ticks, optional fill (0..1) from p0, optional end label."""
    p0, p1 = np.array(p0, float), np.array(p1, float); d = p1 - p0; L = np.linalg.norm(d); u = d / L; n = np.array([-u[1], u[0]]) * side
    cv.line(p0, p1, color, width, alpha=alpha * 0.8)
    if fill > 0: cv.line(p0, p0 + d * clamp(fill), fill_color, width + 2, alpha=alpha)
    for i in range(ticks + 1):
        q = p0 + d * i / ticks; l = 26 if i % major == 0 else 14
        cv.line(q - n * l / 2, q + n * l / 2, color if i / ticks > fill else fill_color, 3 if i % major == 0 else 2, alpha=alpha)
    if label:
        m = (p0 + p1) / 2
        cv.text((m[0] + label_offset[0], m[1] + label_offset[1]), label, label_size, T.WHITE, bold=True, mono=True, alpha=alpha)

def scale_bar(cv, xy, length, text, color=T.GREY, alpha=1.0):
    """A labelled scale bar (only used where the drawing IS to scale; never on the non-scale Earth-Moon schematic)."""
    x, y = xy
    cv.line((x, y), (x + length, y), color, 4, alpha=alpha); cv.line((x, y - 10), (x, y + 10), color, 3, alpha=alpha); cv.line((x + length, y - 10), (x + length, y + 10), color, 3, alpha=alpha)
    cv.text((x + length / 2, y + 30), text, T.MIN_TEXT, color, alpha=alpha)


# =============================================================== directional path indicators
def arrowhead(cv, tip, direction, color, size=34, alpha=1.0):
    d = np.array(direction, float); d /= np.linalg.norm(d); n = np.array([-d[1], d[0]]); tip = np.array(tip, float)
    cv.polygon([tuple(tip), tuple(tip - d * size + n * size * 0.55), tuple(tip - d * size * 0.7), tuple(tip - d * size - n * size * 0.55)], fill=color, alpha=alpha)

def flow_path(cv, pts, color, t=0.0, progress=1.0, dash=(34, 26), speed=130.0, width=8, head=True, alpha=1.0, head_size=36, rev=False):
    """Dashed path whose dashes FLOW in the direction of travel (phase = -t*speed); drawn up to `progress` of its length with an arrowhead."""
    P = np.asarray(pts, float); L = np.linalg.norm(np.diff(P, axis=0), axis=1); tot = L.sum(); need = tot * clamp(progress)
    if need < 1: return
    out = [tuple(P[0])]; acc = 0
    for i in range(len(P) - 1):
        if acc + L[i] <= need: out.append(tuple(P[i + 1])); acc += L[i]
        else: out.append(tuple(P[i] + (P[i + 1] - P[i]) * (need - acc) / L[i])); break
    ph = -t * speed
    cv.polyline(out, color, width, alpha=alpha, dash=dash, phase=ph)
    if head and len(out) >= 2:
        d = np.array(out[-1]) - np.array(out[-2])
        if np.linalg.norm(d) > 1e-6: arrowhead(cv, out[-1], d, color, head_size, alpha)
    return out[-1]


# =============================================================== light pulse (educational symbol, never a visible beam)
def pulse_bead(cv, pos, direction, color, size=1.0, trail=64, alpha=1.0, gap=True):
    """Single compact bead with a short fading comet trail. `direction` = direction of travel. Clean sky behind (no beam)."""
    d = np.array(direction, float); d /= np.linalg.norm(d); x, y = pos
    n = 9
    for i in range(1, n):
        f = 1 - i / n
        cv.circle((x - d[0] * trail * i / n, y - d[1] * trail * i / n), 8 * size * f, fill=color, alpha=alpha * 0.55 * f)
    cv.glow((x, y), 46 * size, color, 0.55 * alpha)
    cv.circle((x, y), 11 * size, fill=T.mix(color, T.WHITE, 0.55), alpha=alpha)

def ring_ping(cv, c, u, color, r0=14, r1=90, width=4, alpha=1.0):
    """Expanding ring for emission / arrival events, u = 0..1 progress (fades as it grows)."""
    if u <= 0 or u >= 1: return
    cv.circle(c, lerp(r0, r1, 1 - (1 - u) ** 3), outline=color, width=width * (1 - 0.5 * u), alpha=alpha * (1 - u) ** 1.5)


def warm():
    """build the procedural textures once (call before forking render workers so every worker shares them)."""
    preload_real()


# =============================================================== round-trip path bar that FOLDS IN HALF (the 'divide by two' beat)
def fold_bar(cv, x, y_base, half_len, theta, width=34, grow=1.0, alpha=1.0, glow=0.0, lift=16.0, cap_dots=True):
    """Vertical bar standing on y_base (Earth end), total length 2*half_len = the round-trip path length c*t; the lower half is the
    OUTBOUND leg (warm, chevrons up), the upper half the RETURN leg (cool, chevrons down). The hinge is at the Moon level
    (y_base - half_len). theta in [0, pi] folds the upper half about the hinge like a paper strip: its free end travels
    y_end = hinge - half_len*cos(theta) (so at theta = pi it lies exactly on the lower half and the bar has length half_len).
    grow in [0,1] draws the bar out from Earth (first half = outbound). Returns dict(y_hinge, y_end, length_visible)."""
    yh = y_base - half_len; L = half_len
    g_low = clamp(grow * 2.0); g_up = clamp(grow * 2.0 - 1.0)
    w = width / 2
    def quad(ya, yb, xo_a=0.0, xo_b=0.0): return [(x - w + xo_a, ya), (x + w + xo_a, ya), (x + w + xo_b, yb), (x - w + xo_b, yb)]
    # lower (outbound) half
    ylow_end = y_base - L * g_low
    if g_low > 0:
        cv.polygon(quad(y_base, ylow_end), fill=T.mix(T.WARM, T.BG, 0.25), alpha=alpha)
        cv.polyline([(x - w, y_base), (x - w, ylow_end)], T.WARM, 4, alpha=alpha); cv.polyline([(x + w, y_base), (x + w, ylow_end)], T.WARM, 4, alpha=alpha)
        for k in range(1, 5):
            yy = y_base - L * (k / 5.0)
            if yy > ylow_end + 8: _chevron(cv, x, yy, -1, T.mix(T.WARM, T.WHITE, 0.4), alpha * 0.9)
    # upper (return) half, rotating about the hinge; foreshortened by cos(theta); front face for theta<pi/2, back face after
    if g_up > 0:
        Lu = L * g_up; y_end = yh - Lu * math.cos(theta); xo = lift * math.sin(theta)
        front = theta < math.pi / 2; shade = 0.55 + 0.45 * abs(math.cos(theta))
        col = T.mix(T.COOL, T.BG, 0.25 + 0.35 * (1 - shade)) if front else T.mix(T.COOL, T.BG, 0.45 + 0.30 * (1 - shade))
        cv.polygon(quad(yh, y_end, 0.0, xo), fill=col, alpha=alpha)
        cv.polyline([(x - w, yh), (x - w + xo, y_end)], T.COOL, 4, alpha=alpha); cv.polyline([(x + w, yh), (x + w + xo, y_end)], T.COOL, 4, alpha=alpha)
        if abs(math.cos(theta)) > 0.25:
            for k in range(1, 5):
                f = k / 5.0 * g_up; yy = yh - L * f * math.cos(theta)
                if f <= g_up: _chevron(cv, x + xo * f, yy, +1, T.mix(T.COOL, T.WHITE, 0.4), alpha * 0.9 * abs(math.cos(theta)))
        if cap_dots and g_up >= 0.999: cv.circle((x + xo, y_end), 11, fill=T.WHITE, outline=T.COOL, width=3, alpha=alpha)          # 'arrived home' end marker
    # hinge (the Moon turn-around point)
    if g_low >= 0.999:
        cv.circle((x, yh), 10, fill=T.WHITE, alpha=alpha); cv.line((x - w - 12, yh), (x + w + 12, yh), T.WHITE, 3, alpha=alpha * 0.7)
        if glow > 0: cv.circle((x, yh), lerp(14, 70, 1 - glow), outline=T.WHITE, width=3, alpha=alpha * glow)
    y_end = (yh - L * g_up * math.cos(theta)) if g_up > 0 else ylow_end
    top = min(yh, y_end) if g_up > 0 else ylow_end                       # extent of the strip on screen: from Earth up to its highest point
    return dict(y_hinge=yh, y_end=y_end, length_visible=y_base - top)

def _chevron(cv, x, y, d, color, alpha):
    """small chevron: d = -1 points up (outbound), +1 points down (return)."""
    s = 12; cv.polyline([(x - s, y - d * s * 0.6), (x, y + d * s * 0.6), (x + s, y - d * s * 0.6)], color, 4, alpha=alpha)
