"""V12 skydiver slowdown — editable production source (picture). Shots: tools/v13_shots.py. Rig: tools/build_rig.py.

Design space 360x640 units, rendered at 1080x1920 / 24 fps.
World: pinhole camera over an irregular illustrated field mesh (metres), palette from the Codex V11 landscape study.
Physics curves come from model.py (fixed posture, NASA Glenn troposphere fit).
Characters: Codex V11 whole-pose candidates (side / three-quarter / back), repaired in tools/fix_boots.py and
tools/recolour.py; glance head registered onto the side canvas. Wrist device: Codex V11 wrist compositions with a
code-authored SLOW..FAST face (tools/instrument11.py). Close-up reaction face, aircraft and clouds: Codex V9 layers.

  python tools/v13.py --check            # self-checks (physics + continuity)
  python tools/v13.py --stills T1 T2 ... # write review PNGs
  python tools/v13.py --render           # parallel render -> SKYDIVER_SLOWDOWN_V13_picture.mp4
"""
import argparse, json, math, os, random, subprocess, sys
from functools import lru_cache
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import rig_renderer as R
import model as PHYS
import instrument11 as I

ROOT = Path(__file__).resolve().parents[1]
R.ROOT = ROOT
C = R.C
FPS, W, H, DUR = 24, 1080, 1920, 78.2
NFRAMES = round(DUR * FPS)  # 1877

# ---------------------------------------------------------------- palette (one grammar per quantity)
INK = '#2A2B27'; MUTED = '#5A6268'
WEIGHT = '#9A4F2C'      # gravity / weight  : solid rust arrow from centre of mass, pointing down
DRAG = '#2F7F7A'        # aerodynamic drag  : solid teal arrow from centre of mass, pointing up
VEL = '#2F5D8C'         # velocity          : dashed blue arrow in a separate lane beside the body
NET = '#6A4C9C'         # net force         : violet double-shaft arrow, derived = drag - weight
AIR = '#5E8FB3'         # relative airflow  : thin moving dashes, no arrowheads (chevrons only)
HAZE = (0.86, 0.91, 0.94)

def rgb(h): return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
def col(c, h, a=1.0):
    if isinstance(h, str): c.set_source_rgba(*rgb(h), a)
    else: c.set_source_rgba(*h, a)
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def smooth(u): u = clamp(u); return u * u * (3 - 2 * u)
def ease_out(u): u = clamp(u); return 1 - (1 - u) ** 3
def ease_io(u): u = clamp(u); return 4*u*u*u if u < .5 else 1 - (-2*u + 2) ** 3 / 2
def lerp(a, b, u): return a + (b - a) * u
def mix(c1, c2, k): return tuple(lerp(a, b, k) for a, b in zip(c1, c2))
def ramp(t, a, b): return smooth((t - a) / (b - a)) if b > a else float(t >= a)
def wobble(t, f, seed, amp=1.0):
    return amp * (math.sin(t * f * 6.283 + seed) * .6 + math.sin(t * f * 2.71 * 6.283 + seed * 1.7) * .4)

# ---------------------------------------------------------------- text
def text(c, s, x, y, size=12, h=INK, bold=False, align='c', alpha=1.0):
    c.select_font_face('Helvetica Neue', C.FONT_SLANT_NORMAL, C.FONT_WEIGHT_BOLD if bold else C.FONT_WEIGHT_NORMAL)
    c.set_font_size(size); e = c.text_extents(s)
    x0 = x - e[2] / 2 - e[0] if align == 'c' else (x - e[2] - e[0] if align == 'r' else x)
    col(c, h, alpha); c.move_to(x0, y); c.show_text(s)
    return e[2]
def label(c, s, x, y, h, size=10.5, alpha=1.0, align='c', bg=True):
    if alpha <= 0.01: return
    c.save(); c.select_font_face('Helvetica Neue', 0, C.FONT_WEIGHT_BOLD); c.set_font_size(size)
    e = c.text_extents(s); w = e[2] + 12
    x0 = x - w / 2 if align == 'c' else (x - w if align == 'r' else x)
    if bg:
        col(c, '#FFFFFF', .82 * alpha); rrect(c, x0, y - size - 3, w, size + 8, 4); c.fill()
    col(c, h, alpha); c.move_to(x0 + 6, y); c.show_text(s); c.restore()
def rrect(c, x, y, w, h, r):
    c.new_sub_path(); c.arc(x + w - r, y + r, r, -math.pi / 2, 0); c.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    c.arc(x + r, y + h - r, r, math.pi / 2, math.pi); c.arc(x + r, y + r, r, math.pi, 1.5 * math.pi); c.close_path()

PHRASES = json.loads((ROOT / 'audio/phrases.json').read_text())
CUES = json.loads((ROOT / 'audio/captions_v13.json').read_text())   # tools/align_captions.py (whisper.cpp + VAD)
CAPTION_TOP = set()      # shot kinds whose lower third carries graphics: caption goes to the top band instead
def caption(c, t):
    """Optional caption overlay. One cue = one spoken phrase (<= 40 chars), shown exactly over its aligned window,
    never overlapping the next cue. Two lines max, ~24 chars per line."""
    p = next((p for p in CUES if p['start'] <= t < p['end']), None)
    if not p: return
    words, lines, cur = p['text'].split(), [], ''
    for wd in words:
        if len(cur) + len(wd) + 1 > 24 and cur: lines.append(cur); cur = wd
        else: cur = (cur + ' ' + wd).strip()
    lines.append(cur)
    a = min(1, (t - p['start']) / .08 + .25, (p['end'] - t) / .08)
    top = 'shot_at' in globals() and shot_at(t)['kind'] in CAPTION_TOP
    c.save(); c.select_font_face('Helvetica Neue', 0, C.FONT_WEIGHT_BOLD); c.set_font_size(15)
    y0 = (70 if top else 578 - 19 * (len(lines) - 1))
    for i, s in enumerate(lines):
        e = c.text_extents(s); w = e[2] + 16
        col(c, '#FFFFFF', .88 * a); rrect(c, 180 - w / 2, y0 + 19 * i - 15, w, 21, 5); c.fill()
        col(c, INK, a); c.move_to(180 - e[2] / 2 - e[0], y0 + 19 * i); c.show_text(s)
    c.restore()

# ---------------------------------------------------------------- arrows
def arrow(c, x, y, dx, dy, h, w=3.2, head=8, dashed=False, alpha=1.0, double=False, dash_off=0.0):
    L = math.hypot(dx, dy)
    if L < 1.5 or alpha <= 0: return
    ux, uy = dx / L, dy / L; hl = min(head, L * .6)
    c.save(); col(c, h, alpha); c.set_line_width(w); c.set_line_cap(C.LINE_CAP_ROUND)
    if dashed: c.set_dash([5, 4], dash_off)
    ex, ey = x + dx - ux * hl * .6, y + dy - uy * hl * .6
    if double:
        nx, ny = -uy * w * .75, ux * w * .75
        c.set_line_width(w * .55)
        for s in (-1, 1):
            c.move_to(x + nx * s, y + ny * s); c.line_to(ex + nx * s, ey + ny * s); c.stroke()
    else:
        c.move_to(x, y); c.line_to(ex, ey); c.stroke()
    c.set_dash([])
    tx, ty = x + dx, y + dy; px, py = -uy, ux
    c.move_to(tx, ty); c.line_to(tx - ux * hl + px * hl * .55, ty - uy * hl + py * hl * .55)
    c.line_to(tx - ux * hl - px * hl * .55, ty - uy * hl - py * hl * .55); c.close_path(); c.fill()
    c.restore()

# ---------------------------------------------------------------- world / camera
class Cam:
    """Pinhole camera at height h (m) above flat ground, pitch p (deg, + = look down), focal F (units)."""
    def __init__(s, h, pitch=0.0, F=420.0, cx=180.0, cy=320.0, x=0.0, z=0.0):
        s.h, s.p, s.F, s.cx, s.cy, s.x, s.z = h, math.radians(pitch), F, cx, cy, x, z
        s.sp, s.cp = math.sin(s.p), math.cos(s.p)
    def proj(s, X, Y, Z):
        dy, Zr, Xr = Y - s.h, Z - s.z, X - s.x
        zc = -dy * s.sp + Zr * s.cp
        yc = dy * s.cp + Zr * s.sp
        if zc <= 1.0: return None
        return s.cx + s.F * Xr / zc, s.cy - s.F * yc / zc, zc
    def horizon_y(s): return s.cy - s.F * math.tan(s.p)

def hrand(*k):
    import zlib  # deterministic across processes (built-in hash() is salted per process)
    return random.Random(zlib.crc32(repr(k).encode()))
# V11 terrain: irregular fields on a jittered mesh (no checkerboard), palette sampled from the Codex V11
# flat landscape study (environment/landscape_reference.png); forests are rounded clumps, roads curve.
FIELD = [rgb(h) for h in ('#A4BC86', '#C3CD93', '#B4C28C', '#B4C898', '#A0BC92', '#D2C9A4', '#91B08C', '#8AA97D')]
FOREST = rgb('#779771'); TOWN = rgb('#D6CFC2'); WATER = rgb('#A6C8E0'); ROAD = rgb('#E4DDC8'); HEDGE = rgb('#6E8A68')
NEAR = 9000.0; CELL = 520.0
def tint(c0, r, amt=.02): return tuple(clamp(x + r.uniform(-amt, amt)) for x in c0)
@lru_cache(None)
def vtx(i, j, cell):
    r = hrand('v', i, j, cell); return i * cell + r.uniform(-.38, .38) * cell, j * cell + r.uniform(-.38, .38) * cell
def _mesh(tag, i0, i1, j0, j1, cell, forest_p):
    out, colours = [], {}
    for j in range(j0, j1):
        for i in range(i0, i1):
            r = hrand(tag, i, j)
            if (i - 1, j) in colours and r.random() < .42: c0 = colours[(i - 1, j)]          # merge -> long irregular fields
            elif (i, j - 1) in colours and r.random() < .25: c0 = colours[(i, j - 1)]
            else: c0 = tint(FOREST if r.random() < forest_p else FIELD[r.randrange(len(FIELD))], r)
            colours[(i, j)] = c0
            quad = [vtx(i, j, cell), vtx(i + 1, j, cell), vtx(i + 1, j + 1, cell), vtx(i, j + 1, cell)]
            edge = r.random() < .35                                                    # occasional hedge line only
            out.append((quad, c0, 1 if c0 != FOREST else 2, edge))
    return out
@lru_cache(None)
def near_patches():
    n = int(NEAR / CELL); return _mesh('n', -n, n, -n, n, CELL, .0)
@lru_cache(None)
def far_patches():
    out, z = [], NEAR
    while z < 240000:   # widening depth bands of larger irregular cells
        cell = max(CELL, z * .16); j = int(z / cell)
        nx = int(min(60, 1.2 * z / cell))
        out += _mesh('f%d' % int(cell), -nx, nx, j, j + 1, cell, .0)
        z = (j + 1) * cell + 1
    return out
@lru_cache(None)
def forests():
    r = random.Random(17); out = []
    for _ in range(220):
        X, Z = r.uniform(-NEAR, NEAR), r.uniform(-NEAR, 60000); n = r.randint(5, 14)
        out.append([(X + r.gauss(0, 160), Z + r.gauss(0, 160), r.uniform(60, 140)) for _ in range(n)])
    return out
def river_pts():
    return [(-2600 + 900 * math.sin(z / 2300.0) + 300 * math.sin(z / 700.0), z) for z in range(-9000, 240000, 150)]
RIVER = river_pts()
ROADS = [[(x0 + 1400 * math.sin(z / 3100.0 + k) + 500 * math.sin(z / 900.0 + 2 * k), z) for z in range(-9000, 60000, 200)]
         for k, x0 in enumerate((-6500, 1800, 7400))]   # three winding country roads
CLOUDS = []
_r = random.Random(7)
for i in range(240):
    z = _r.uniform(-8000, 160000); x = _r.uniform(-.7, .7) * max(9000, z * .8)
    CLOUDS.append((x, _r.uniform(1900, 2300), z, _r.uniform(700, 1500), _r.random()))

def haze_k(cam, dist):
    return 1 - math.exp(-dist / 40000.0)   # visibility scale ~40 km: blue haze, ground still legible from 10 km

def sky(c, cam):
    hy = cam.horizon_y()
    top = mix(rgb('#86B6DA'), rgb('#A9CDE6'), clamp(1 - cam.h / 10000))   # deeper blue only when high
    g = C.LinearGradient(0, min(hy - 560, -60), 0, hy + 2)
    g.add_color_stop_rgb(0, *top); g.add_color_stop_rgb(.7, *rgb('#CBE1F0')); g.add_color_stop_rgb(1, *HAZE)
    c.set_source(g); c.paint()
    return hy

def _poly(c, cam, X, Z, sx, sz):
    pts = [cam.proj(X, 0, Z), cam.proj(X + sx, 0, Z), cam.proj(X + sx, 0, Z + sz), cam.proj(X, 0, Z + sz)]
    if any(p is None for p in pts): return None
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    if max(xs) < -5 or min(xs) > 365 or max(ys) < -5 or min(ys) > 645: return None
    return pts, max(xs) - min(xs)
def _line(c, cam, a, b, wm, colr, alpha=1.0):
    pa = cam.proj(*a); pb = cam.proj(*b)
    if not pa or not pb: return
    w = cam.F * wm / ((pa[2] + pb[2]) / 2)
    if w < .12: return
    d = (pa[2] + pb[2]) / 2
    c.set_source_rgba(*mix(colr, HAZE, haze_k(cam, math.hypot(d, cam.h))), alpha)
    c.set_line_width(w); c.move_to(*pa[:2]); c.line_to(*pb[:2]); c.stroke()

def ground(c, cam, detail=True):
    """Draw terrain (with distance haze) below the horizon for any pitch."""
    hy = cam.horizon_y()
    if hy > 640: return
    col(c, mix(rgb('#BFC8B0'), HAZE, .75)); c.rectangle(0, max(hy, 0), 360, 700); c.fill()
    for quad, c0, kind, edge in far_patches() + near_patches():
        pts = [cam.proj(X, 0, Z) for X, Z in quad]
        if any(p is None for p in pts): continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if max(xs) < -5 or min(xs) > 365 or max(ys) < -5 or min(ys) > 645: continue
        span = max(xs) - min(xs)
        Xc = sum(q[0] for q in quad) / 4; Zc = sum(q[1] for q in quad) / 4
        k = haze_k(cam, math.hypot(math.hypot(Zc - cam.z, Xc - cam.x), cam.h))
        c.set_source_rgb(*mix(c0, HAZE, k)); c.move_to(*pts[0][:2])
        for p in pts[1:]: c.line_to(*p[:2])
        c.close_path(); c.fill_preserve()
        c.set_line_width(.6); c.stroke()        # same colour: closes hairline seams between cells
        if span > 40 and kind == 1:              # close up: crop rows inside the field (direction varies per field)
            rr = hrand('s', round(Xc), round(Zc)); nstr = rr.randint(3, 6); horiz = rr.random() < .5
            P0, P1, P2, P3 = [p[:2] for p in pts]
            if horiz: P0, P1, P2, P3 = P1, P2, P3, P0
            c.set_source_rgba(*mix(HEDGE, HAZE, k), .16); c.set_line_width(.5 + span / 400)
            for q in range(1, nstr):
                f = q / nstr
                c.move_to(P0[0] + (P3[0] - P0[0]) * f, P0[1] + (P3[1] - P0[1]) * f)
                c.line_to(P1[0] + (P2[0] - P1[0]) * f, P1[1] + (P2[1] - P1[1]) * f); c.stroke()
        if edge and span > 14:
            c.set_source_rgba(*mix(HEDGE, HAZE, k), .35); c.set_line_width(.3 + min(.7, span / 220))
            c.move_to(*pts[0][:2]); c.line_to(*pts[1][:2]); c.stroke()
    for clump in forests():   # rounded tree clumps (flat fill + darker rim), like the Codex landscape study
        for X, Z, rr in clump:
            p = cam.proj(X, 0, Z)
            if not p: continue
            w = cam.F * rr / p[2]
            if w < .25 or p[0] < -w or p[0] > 360 + w or p[1] < -w or p[1] > 660: continue
            k = haze_k(cam, math.hypot(math.hypot(Z - cam.z, X - cam.x), cam.h))
            c.set_source_rgb(*mix(FOREST, HAZE, k)); c.save(); c.translate(p[0], p[1]); c.scale(1, max(.25, abs(math.sin(cam.p)) + .15))
            c.arc(0, 0, w, 0, 6.283); c.restore(); c.fill()
    for road in ROADS:
        for a_, b_ in zip(road, road[1:]):
            _line(c, cam, (a_[0], 0, a_[1]), (b_[0], 0, b_[1]), 10, ROAD, .9)
    # river
    prev = None
    c.set_line_cap(C.LINE_CAP_ROUND)
    for X, Z in RIVER:
        p = cam.proj(X, 0, Z)
        if p and prev and -20 < p[1] < 680:
            wdt = cam.F * 70 / p[2]
            if wdt > .15:
                c.set_source_rgb(*mix(WATER, HAZE, haze_k(cam, math.hypot(Z - cam.z, cam.h))))
                c.set_line_width(wdt); c.move_to(*prev[:2]); c.line_to(*p[:2]); c.stroke()
        prev = p
    if hy < 660 and cam.p < math.radians(35):   # distant hills, very low contrast
        c.set_source_rgba(*mix(rgb('#9FB0B8'), HAZE, .6), 1)
        c.move_to(0, hy + 1)
        for i in range(0, 37):
            c.line_to(i * 10, hy - 1.0 - 2.0 * (.5 + .5 * math.sin(i * 1.7) * math.cos(i * .63)))
        c.line_to(360, hy + 1); c.close_path(); c.fill()
    g = C.LinearGradient(0, hy - 34, 0, hy + 46)
    g.add_color_stop_rgba(0, *HAZE, 0); g.add_color_stop_rgba(.45, *HAZE, .9); g.add_color_stop_rgba(1, *HAZE, 0)
    c.set_source(g); c.rectangle(0, hy - 34, 360, 80); c.fill()

CLOUD_KINDS = ['cumulus_01', 'cumulus_02', 'cumulus_03', 'cumulus_04', 'cumulus_05', 'cumulus_06', 'wisp_01', 'wisp_02', 'wisp_03']
def cloud_sprite(c, x, y, wpx, kind='cumulus_01', alpha=1.0):
    """Codex EN-01 cloud layer, scaled so its artwork is wpx units wide, centred at x, base near y."""
    surf, ox, oy, k = R.drawing(f'assets/codex/clouds/{kind}.png', 640)
    sw = surf.get_width() / k
    if sw <= 0 or alpha <= 0: return
    s = wpx / sw
    c.save(); c.translate(x - wpx / 2, y - surf.get_height() / k * s * .6); c.scale(s / k, s / k)
    c.set_source_surface(surf, 0, 0); c.get_source().set_filter(C.FILTER_GOOD); c.paint_with_alpha(alpha); c.restore()

def cloud_deck(c, cam):
    items = []
    for X, Y, Z, size, r in CLOUDS:
        p = cam.proj(X, Y, Z)
        if not p: continue
        wpx = cam.F * size / p[2]
        if wpx < 1.2 or wpx > 900: continue
        if p[0] < -wpx or p[0] > 360 + wpx or p[1] < -wpx or p[1] > 700: continue
        items.append((p[2], p[0], p[1], wpx, r))
    for zc, x, y, wpx, r in sorted(items, reverse=True):
        a = (1 - haze_k(cam, zc) * .9) * clamp((zc - 150) / 400)
        cloud_sprite(c, x, y, wpx, CLOUD_KINDS[int(r * 8.99)], a)

def environment(c, cam):
    sky(c, cam); ground(c, cam); cloud_deck(c, cam)

def air_streaks(c, t, rate, alpha=.5, seed=3, count=16, up=True):
    """Sparse near-field specks of relative air: travel speed and length follow model speed. Schematic.
    Kept short and faint so they never read as rain."""
    r = random.Random(seed)
    for i in range(count):
        x = r.uniform(6, 354); ph = r.uniform(0, 700); depth = r.uniform(.35, 1.0)
        y = (ph - t * rate * depth) % 760 - 60
        L = min(26, 2 + rate * .045 * depth)
        col(c, '#FFFFFF', alpha * .6 * depth); c.set_line_width(.5 + .5 * depth); c.set_line_cap(C.LINE_CAP_ROUND)
        c.move_to(x, y); c.line_to(x, y + L); c.stroke()

def passing_wisps(c, t, rate, seed=11, alpha=.55):
    r = random.Random(seed)
    for i in range(4):
        x = r.uniform(-40, 330); ph = r.uniform(0, 1100); s = r.uniform(130, 220)
        y = (ph - t * rate * 1.6) % 1300 - 250
        cloud_sprite(c, x, y, s, CLOUD_KINDS[6 + i % 3], alpha)

# ---------------------------------------------------------------- characters
def actor(c, view, ch, x, y, scale):
    R.actor(c, view, ch, x, y, scale)
COM = {'side': (325, 210), 'three_quarter': (327, 214), 'back': (321, 212), 'front': (320, 216)}
def com_screen(view, x, y, scale):
    px, py = COM[view]; return x + (px - 320) * scale, y + (py - 200) * scale

def perf_flutter(t, amt=1.0, seed=0):
    """Secondary motion from airflow on limbs: small, layered, non-repeating within a shot."""
    return {
        'head': wobble(t, .23, seed + 1, 2.5 * amt),
        'near_upper_arm': wobble(t, .31, seed + 2, 3 * amt), 'far_upper_arm': wobble(t, .27, seed + 3, 3 * amt),
        'near_forearm': wobble(t, .53, seed + 4, 5 * amt), 'far_forearm': wobble(t, .47, seed + 5, 5 * amt),
        'near_hand': wobble(t, 1.3, seed + 6, 7 * amt), 'far_hand': wobble(t, 1.1, seed + 7, 7 * amt),
        'near_thigh': wobble(t, .19, seed + 8, 2 * amt), 'far_thigh': wobble(t, .21, seed + 9, 2 * amt),
        'near_shin': wobble(t, .37, seed + 10, 4 * amt), 'far_shin': wobble(t, .33, seed + 11, 4 * amt),
        'near_foot': wobble(t, .9, seed + 12, 6 * amt), 'far_foot': wobble(t, .8, seed + 13, 6 * amt),
        'torso': wobble(t, .13, seed + 14, .8 * amt), 'pack': 0,
    }
def add(a, b):
    out = dict(a)
    for k, v in b.items(): out[k] = out.get(k, 0) + v
    return out

exec(open(Path(__file__).with_name('v13_shots.py')).read())

# ---------------------------------------------------------------- render
def frame_surface(t):
    f = C.ImageSurface(C.FORMAT_ARGB32, W, H); c = C.Context(f); c.scale(W / 360, H / 640)
    c.rectangle(0, 0, 360, 640); c.clip()
    draw(c, t); f.flush(); return f

def caption_surface(t):
    f = C.ImageSurface(C.FORMAT_ARGB32, W, H); c = C.Context(f); c.scale(W / 360, H / 640)
    caption(c, t); f.flush(); return f

def render_chunk(args):
    i0, i1, out = args
    if str(out).endswith('.mov'):   # caption overlay pass: transparent frames, PNG-in-MOV keeps alpha
        p = subprocess.Popen(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgra',
                              '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'png', str(out)], stdin=subprocess.PIPE)
        for i in range(i0, i1):
            f = caption_surface(i / FPS); p.stdin.write(bytes(f.get_data())); del f
        p.stdin.close(); assert p.wait() == 0
        return out
    p = subprocess.Popen(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgra',
                          '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
                          '-pix_fmt', 'yuv420p', str(out)], stdin=subprocess.PIPE)
    for i in range(i0, i1):
        f = frame_surface(i / FPS); p.stdin.write(bytes(f.get_data())); del f   # keep surface alive while writing
    p.stdin.close(); assert p.wait() == 0
    return out

def render(out='SKYDIVER_SLOWDOWN_V13_picture.mp4', workers=9, start=0, end=NFRAMES):
    from multiprocessing import Pool
    ext = '.mov' if out.endswith('.mov') else '.mp4'
    tmp = ROOT / ('qa/_chunks' + ext.replace('.', '_')); tmp.mkdir(parents=True, exist_ok=True)
    step = math.ceil((end - start) / (workers * 2))
    jobs = [(a, min(a + step, end), tmp / f'c{a:05}{ext}') for a in range(start, end, step)]
    with Pool(workers) as pool:
        for o in pool.imap_unordered(render_chunk, jobs): print('chunk', o.name, flush=True)
    lst = tmp / 'list.txt'; lst.write_text(''.join(f"file '{j[2]}'\n" for j in jobs))
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst),
                    '-c', 'copy', str(ROOT / out)], check=True)
    print(ROOT / out)

def stills(times, folder='qa/stills', width=540):
    d = ROOT / folder; d.mkdir(parents=True, exist_ok=True)
    for t in times:
        f = frame_surface(t); p = d / f't{t:06.2f}.png'; f.write_to_png(str(p))
    return d

def selfcheck():
    assert SHOT_OBJS[0]['start_frame'] == 0 and SHOT_OBJS[-1]['end_frame'] == NFRAMES
    assert all(a['end_frame'] == b['start_frame'] for a, b in zip(SHOT_OBJS, SHOT_OBJS[1:]))
    # model time monotonic; velocity never reverses; speed only falls after the crossing
    ts = [i / FPS for i in range(NFRAMES)]
    ms = [model_t(t) for t in ts if model_t(t) is not None]
    assert all(b >= a for a, b in zip(ms, ms[1:])), 'model time must not run backwards'
    vs = [state(m)[1] for m in ms]; hs = [state(m)[0] for m in ms]
    assert min(vs) >= 0 and all(b <= a + 1e-6 for a, b in zip(hs, hs[1:])), 'never rises'
    after = [state(model_t(t))[1] for t in ts if t >= 47.71]
    assert all(b <= a + 1e-6 for a, b in zip(after, after[1:])), 'needle must not rise during slowdown'
    assert all(state(model_t(t))[1] > 0 for t in ts if t >= 21.2), 'needle stays above zero once falling'
    assert min(hs) > 300, 'no ground contact depicted'
    for i in range(0, NFRAMES, 8): frame_surface(i / FPS)   # every 8th frame must draw without error
    print(f'self-check ok: {len(SHOT_OBJS)} shots continuous, model time monotonic, v>=0, no rise, needle monotonic after 47.7 s, min alt', round(min(hs)), 'm')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true'); ap.add_argument('--render', action='store_true')
    ap.add_argument('--stills', nargs='*', type=float); ap.add_argument('--out', default='SKYDIVER_SLOWDOWN_V13_picture.mp4')
    a = ap.parse_args()
    if a.check: selfcheck()
    if a.stills: print(stills(a.stills))
    if a.render: render(a.out)
