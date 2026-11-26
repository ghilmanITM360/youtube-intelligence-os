"""Slot 07 ANIMATIC V1 (reference informed). Temporary art, real layered 2.5D compositing, same engine as look_dev (tools/lookdev.py).

  ~/.venvs/uepipe/bin/python tools/animatic_v1.py still 15.2 out.png [nocap]   one frame (1080x1920 -> 540x960)
  ~/.venvs/uepipe/bin/python tools/animatic_v1.py video                        storyboard/animatic/ANIMATIC_V1_REFERENCE_INFORMED.mp4
  ~/.venvs/uepipe/bin/python tools/animatic_v1.py audit                        caption + key-subject safe-band audit for every frame (no video)
  ~/.venvs/uepipe/bin/python tools/animatic_v1.py camera                       print the CAMERA_NOTES markdown table

Timeline = the unmodified master recording (92.53 s) + 1.47 s tail; fade-out 93.2 -> 94.0 s.
The caption band / safe box below are OUR provisional mask, not a platform specification.
"""
import csv, json, math, os, random, subprocess, sys
from multiprocessing import Pool
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lookdev as LD
from lookdev import (W, H, SAFE, CAP, BG, WARM, COOL, WHITE, GREY, DIM, RED, lerp, clamp, seg, ease, eout, ein, mix, dim, Frame, Layer, Cam, TOK)

ROOT = LD.ROOT
FPS = 24; TOTAL = 97.0; NARR_END = 95.39; FADE0 = 96.2          # V2 take (was 94.0 / 92.53 / 93.2 for V1)
T = TOK['C']
LIMB_Y = 1400; MOON_C = (540, 430); MOON_R = 150; PATH_TOP = 590     # schematic constants (design space)
TIP = (540, 1010)                                                       # telescope tip in dome world coordinates (rest camera)


# ----------------------------------------------------------------------------- beats, words, captions
def load_beats():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'narration', 'v1_historical', 'NARRATION_BEAT_MAP.csv'))))
    words = json.load(open(os.path.join(ROOT, 'narration', 'v1_historical', 'WORD_TIMESTAMPS.json')))['words']
    beats = []
    for i, r in enumerate(rows):
        s = float(r['start_s']); e = float(rows[i + 1]['start_s']) if i + 1 < len(rows) else TOTAL
        wi = [w for w in words if int(r['first_word']) <= w['i'] <= int(r['last_word'])]
        beats.append(dict(id=r['id'], start=s, end=e, anchor=float(r['anchor_s']), text=r['spoken_text'], words=wi, voice_end=float(r['end_s'])))
    return beats

BEATS = load_beats()
def beat_at(t):
    cur = BEATS[0]
    for b in BEATS:
        if b['start'] <= t + 1e-9: cur = b
    return cur
def B(i): return next(b for b in BEATS if b['id'] == i)


def build_captions():
    """Chunk each beat's words so every chunk fits in <= 2 balanced lines; a chunk is on screen from its first word to just after its last word."""
    fnt = LD.font(54, 'bold'); maxw = 880; chunks = []
    def width(ws): return fnt.getlength(' '.join(w['word'] for w in ws))
    def two_lines(ws):
        if width(ws) <= maxw: return [' '.join(w['word'] for w in ws)]
        if len(ws) < 2: return None
        k = min(range(1, len(ws)), key=lambda k: max(width(ws[:k]), width(ws[k:])))
        return [' '.join(w['word'] for w in ws[:k]), ' '.join(w['word'] for w in ws[k:])] if max(width(ws[:k]), width(ws[k:])) <= maxw else None
    for bi, b in enumerate(BEATS):
        ws = b['words']
        if not ws: continue
        for k in range(1, 6):                                   # smallest number of near-equal chunks that all fit in two lines
            cum = np.cumsum([len(w['word']) + 1 for w in ws]); cuts = [int(np.searchsorted(cum, cum[-1] * j / k)) + 1 for j in range(1, k)]
            parts = [ws[i:j] for i, j in zip([0] + cuts, cuts + [len(ws)]) if ws[i:j]]
            ls = [two_lines(p) for p in parts]
            if all(ls): break
        nxt_start = BEATS[bi + 1]['words'][0]['start'] if bi + 1 < len(BEATS) and BEATS[bi + 1]['words'] else TOTAL
        for gi, (g, l) in enumerate(zip(parts, ls)):
            last = gi == len(parts) - 1; t0 = g[0]['start'] - 0.04
            t1 = (parts[gi + 1][0]['start'] - 0.02) if not last else min(g[-1]['end'] + 0.45, nxt_start - 0.02)
            chunks.append(dict(t0=max(0, t0), t1=t1, lines=l, beat=b['id']))
    return chunks

CAPS = build_captions()


def caption_layout(lines):
    size = 54; fnt = LD.font(size, 'bold'); lh = 68
    tw = max(fnt.getlength(l) for l in lines); w = tw + 72; h = len(lines) * lh + 36
    cx, cy = W / 2, (CAP[1] + CAP[3]) / 2 + 6
    box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    return box, size, lh


def assert_caption_band():
    worst = 0
    for c in CAPS:
        box, _, _ = caption_layout(c['lines'])
        assert box[0] >= CAP[0] and box[2] <= CAP[2] and box[1] >= CAP[1] and box[3] <= CAP[3], ('caption outside band', c, box)
        assert len(c['lines']) <= 2
        worst = max(worst, box[2] - box[0])
    return worst


def draw_caption(f, t):
    for c in CAPS:
        if c['t0'] <= t < c['t1']:
            box, size, lh = caption_layout(c['lines']); a = ease(seg(t, c['t0'], c['t0'] + 0.12)) * (1 - ease(seg(t, c['t1'] - 0.10, c['t1'])))
            if a <= 0: return
            f.rrect(box, 26, fill=(4, 6, 16), a=0.64 * a)
            y = box[1] + 18 + lh / 2
            for l in c['lines']:
                f.text((W / 2 + 2, y + 3), l, size, (0, 0, 0), 'bold', a=0.5 * a); f.text((W / 2, y), l, size, (246, 248, 252), 'bold', a=a); y += lh
            return


# ----------------------------------------------------------------------------- key-subject registry (for the safe-band audit)
def wb(f, cam, p, box, name, transient=False):
    """Register a world-space box (design units at rest camera) as a key subject, mapped through the camera."""
    x0, y0 = cam.map(p, box[0], box[1]); x1, y1 = cam.map(p, box[2], box[3]); f.keys.append(('~' + name if transient else name, (x0, y0, x1, y1)))

def audit_keys(keys):
    bad = []
    for name, b in keys:
        if b[3] < 0 or b[1] > H: continue
        if name.startswith('~'): continue
        if b[3] > SAFE[3] + 1: bad.append((name, 'below safe box', tuple(round(v) for v in b)))
        if not (b[2] < CAP[0] or b[0] > CAP[2] or b[3] <= CAP[1] or b[1] >= CAP[3]): bad.append((name, 'intersects caption band', tuple(round(v) for v in b)))
    return bad


# ----------------------------------------------------------------------------- shared drawing helpers
def sph(kind, r, res=2, p=1.0):
    return LD.sphere_layer(kind, (0, 0), r, p, res)

def moon_layer(c, r, big=False, p=0.9):
    ml = LD.sphere_layer('moon', (0, 0), 700 if big else MOON_R, p, 1 if big else 2); m = (700 if big else MOON_R)
    ml.x, ml.y = c[0] - ml.w / 2, c[1] - ml.h / 2
    return ml, (r / m)

def put_moon(f, cam, c=MOON_C, r=MOON_R, p=0.9, big=False, alpha=1.0, glow=0.14, key=True):
    ml, sc = moon_layer(c, r, big, p); s, _, ex, ey = cam.xf(p)
    mc = (W / 2 + (c[0] - ex) * s, H / 2 + (c[1] - ey) * s)
    if glow > 0: LD.moon_glow(f, mc, r * s * sc if not big else r * s, glow * alpha)
    anchor = mc
    f.put(ml, cam, ox=0, oy=0, sc=sc if not big else sc, anchor=anchor if False else mc, alpha=alpha)
    if key: f.keys.append(('moon', (mc[0] - r * s, mc[1] - r * s, mc[0] + r * s, mc[1] + r * s)))
    return mc, r * s

def space(f, cam=None, a=0.8):
    f.im.paste(Image.new('RGB', f.im.size, BG)); f.put(LD.stars_space(), cam or f.cam, alpha=a)

def earth(f, cam, oy=0.0, alpha=1.0, dimk=1.0):
    f.put(LD.earth_cap_layer(), cam, oy=oy, alpha=alpha * dimk)

def guide(f, a=0.55, y0=LIMB_Y - 4, y1=PATH_TOP, x=540, dash=(26, 18), col=GREY, grow=1.0):
    ye = lerp(y0, y1, clamp(grow)); f.dashed((x, y0), (x, ye), col, 4, dash[0], dash[1], a)

def yp(p, y0=LIMB_Y - 20, y1=PATH_TOP + 8): return lerp(y0, y1, p)      # p = 0 Earth, 1 Moon

def bead(f, x, y, col, size=1.0, trail=(0, 1), tlen=90, a=1.0): LD.bead(f, x, y, col, size, trail, tlen, T, a)

def stopwatch(f, val, a=1.0, c=(190, 250), r=100, digits=True, hand=WARM, big=1.0, key=True):
    LD.stopwatch(f, c, r, val, 3.0, T, digits, a, hand, big=big)
    if key and a > 0.3: f.key('stopwatch', (c[0] - r, c[1] - r - 20, c[0] + r, c[1] + r))

def num(f, xy, s, size, col=WHITE, a=1.0, anchor='mm'): f.text(xy, s, size, col, 'mono', anchor, a)

def tag(f, xy, s, a=1.0, size=26, anchor='mm'): f.text(xy, s, size, GREY, 'med', anchor, a)

def leg_traces(f, up=1.0, down=1.0, a=1.0, w=None, x0=500, x1=580):
    w = w or T['sw'] * 1.1
    if up > 0: f.line([(x0, yp(0.02)), (x0, lerp(yp(0.02), yp(0.97), up))], WARM, w, a)
    if up >= 1: f.poly([(x0, yp(0.97) - 8), (x0 - 20, yp(0.97) + 30), (x0 + 20, yp(0.97) + 30)], fill=WARM, a=a)
    if down > 0: f.line([(x1, yp(0.97)), (x1, lerp(yp(0.97), yp(0.02), down))], COOL, w, a)
    if down >= 1: f.poly([(x1, yp(0.02) + 8), (x1 - 20, yp(0.02) - 30), (x1 + 20, yp(0.02) - 30)], fill=COOL, a=a)

def ring(f, c, r, col=WARM, w=5, a=1.0, dashed=False):
    if not dashed: f.circle(c, r, outline=col, w=w, a=a); return
    n = 16
    for i in range(n):
        a0 = i / n * 2 * math.pi; a1 = (i + 0.55) / n * 2 * math.pi
        f.line([(c[0] + r * math.cos(a0), c[1] + r * math.sin(a0)), (c[0] + r * math.cos(a1), c[1] + r * math.sin(a1))], col, w, a, cap=False)

def blend(a, b, u): return Image.blend(a, b, clamp(u))

def wipe_up(a, b, u, soft=220):
    """b revealed from the bottom edge upward (Earth is at the bottom in every schematic)."""
    y = lerp(H + soft, -soft, clamp(u)); yy = np.arange(H, dtype=np.float32)[:, None]
    m = np.clip((yy - y) / soft, 0, 1) * np.ones((1, W), np.float32)
    return Image.composite(b, a, Image.fromarray((m * 255).astype(np.uint8)))

def fade_veil(f, a, col=BG): f.veil(col, a)

def ballistic(f, cam, origin, t, t0, n=16, seed=4, vmax=420, g=380, col=(176, 172, 168), size=7, life=1.1):
    """1/6-g-like dust: parabolic arcs, no billowing. Origin is a world point on the focal plane."""
    rg = random.Random(seed); tt = t - t0
    if tt < 0 or tt > life: return
    for i in range(n):
        ang = math.radians(rg.uniform(25, 75)); v = rg.uniform(0.35, 1.0) * vmax; dirx = rg.choice([-1, 1]) if i % 3 else 1
        x = origin[0] + dirx * v * math.cos(ang) * tt * 0.45; y = origin[1] - v * math.sin(ang) * tt * 0.45 + 0.5 * g * 0.45 * tt * tt
        sx, sy = cam.map(1.0, x, y); k = cam.xf(1.0)[0]; al = (1 - tt / life) ** 1.5
        f.circle((sx, sy), size * k * (0.6 + 0.8 * rg.random()), fill=col, a=0.8 * al)


def put_moon(f, cam, c=MOON_C, r=MOON_R, p=0.9, big=False, alpha=1.0, glow=0.14, key=True, glow_col=(70, 96, 150)):
    ml, sc = moon_layer(c, r, big, p); s, _, ex, ey = cam.xf(p)
    mc = (W / 2 + (c[0] - ex) * s, H / 2 + (c[1] - ey) * s); rs = r * s
    if glow > 0: f.glow(mc, rs * 2.6, glow_col, glow * alpha)
    f.put(ml, cam, sc=sc, anchor=mc, alpha=alpha)
    if key: f.keys.append(('moon', (mc[0] - rs, mc[1] - rs, mc[0] + rs, mc[1] + rs)))
    return mc, rs


CAMERA_NOTES = []        # (beats, time, move, reason)
def cam_note(beats, tt, move, reason): CAMERA_NOTES.append((beats, tt, move, reason))
cam_note('B01', '0.6-2.7 s', 'tilt up 640 px (ease in-out), layers p 0.94-1.10 so the near ground shifts slightly more than the sky', 'reveals the target on the word "laser"; the Moon enters at the top as the word lands')
cam_note('B02', '3.47-5.0 s', 'locked', 'the rejected floodlight idea is the only event; nothing else may move')
cam_note('B03-B04', '5.05-8.04 s', 'push-in 1.0 -> 1.40 (+0.08 creep) toward the dome slit', 'moves from "a place" to "the instrument"; the question becomes one pulse leaving the aperture')
cam_note('B04-B05', '8.04-8.90 s', 'pull back to 1.0 while the ground group drops 1100 px and the Earth limb rises from below', 'movement handoff: the pulse leaves Earth, we leave with it; the Moon lands exactly on its schematic spot (540, 430)')
cam_note('B05-B11', '8.9-26.46 s', 'locked schematic', 'the stopwatch and the pulse are the only motion; a moving camera would corrupt the distance reading')
cam_note('B12-B13', '26.46-31.06 s', 'soft upward wipe into the orbit diagram', 'a change of model (top-down), so a change of view; wipe runs upward (Earth is at the bottom)')
cam_note('B14-B15', '31.75-33.6 s', 'exponential push-in on the Moon (r 56 -> 1500), then dissolve to the surface', 'scale change from "the Moon in space" to "the ground under the pulse"; exponential so the zoom feels constant')
cam_note('B15-B17', '33.15-38.65 s', 'near-locked at z 2.0 (+0.02 drift) on the target spot', 'ghost mirror and real reflector must share spot and scale for the match cut')
cam_note('B18', '38.65-41.5 s', 'ease out 2.0 -> 1.0 with a pan right (490 -> 600); far/near ground slices at p 0.90/1.00', 'reveals the astronaut for scale as he walks in; differential ground slices give depth')
cam_note('B19', '42.62-43.85 s', 'anticipation dip (-3%), then push-in 1.0 -> 2.6 to the array face, circular iris opens at 43.6 s', 'scale change into the optics; the iris is a magnifier ring, the same device as the B20 inset')
cam_note('B20-B21', '44.8-48.5 s', 'locked; the diagram shrinks and slides left in B21 (by the diagram, not the camera)', 'one idea at a time; B21 needs room for the flat-mirror comparison')
cam_note('B22', '49.58-50.45 s', 'hard cut from the exit ray (travelling down) to a bead travelling down; push-in 1.0 -> 1.7 on the tube tip in the last 0.4 s', 'match cut on direction of travel (Earth at the bottom in both); push-in hands over to the cutaway')
cam_note('B23', '50.1-53.1 s', 'locked cutaway, quiet hold after the detector lights', 'restraint moment: the detector lighting is the event')
cam_note('B24', '53.1-55.0 s', 'slow push-in 1.0 -> 1.05 while the frame dims', 'hush: the image narrows and darkens before the surprise')
cam_note('B25', '55.0-55.7 s', 'the same Earth-rise handoff as B04-B05', 'return to the schematic where the two widening cones can be read')
cam_note('B26-B30', '58.7-75.3 s', 'locked', 'statistics are read as a static chart; only the data move')
cam_note('B31', '75.5-76.2 s', 'upward wipe back to the model view', 'the details drop away: Earth-Moon line only')
cam_note('B32-B36', '77-86 s', 'locked', 'the bar peeling off the path, folding, and returning is the whole event')
cam_note('B37', '86.4-89.4 s', 'slow pull-back 1.5 -> 1.0 (ease out), layers p 0.1 / 0.9 / 1.0 (stars / Moon / Earth)', 'the wide shot for "not just hanging in the sky"; parallax proves it is a space, not a flat picture')
cam_note('B38-B39', '89.4-94 s', 'locked, then fade to black 93.2-94.0 s', 'stillness for the conclusion')


# ============================================================================= scenes
def ground_cam(t):
    k = ease(seg(t, 0.6, 2.7)); cy = lerp(1600, 960, k)
    zk = ease(seg(t, 5.05, 6.6)); z = lerp(1.0, 1.40, zk) + 0.08 * seg(t, 6.6, 8.04)
    return Cam(540, cy + (1075 - 960) * zk, z)


def world(f, cam, u, open_=1.0, tilt=0.0, moon_p=0.96, moon_glow=0.2, warm_glow=0.0):
    """Ground view (u=0) -> Earth-Moon schematic (u=1) in one layer stack: the ground group falls, the limb rises, the Moon stays."""
    f.cam = cam; f.im.paste(Image.new('RGB', f.im.size, BG)); f.put(LD.stars_space(), cam, alpha=0.8 * ease(seg(u, 0.15, 1.0)))
    L = LD.ground_layers(); ga = 1 - u; tip = None
    if ga > 0.001: f.put(L['sky'], cam, alpha=ga); f.put(L['stars'], cam, alpha=ga)
    mc, mr = put_moon(f, cam, p=moon_p, glow=moon_glow)
    if warm_glow > 0: f.glow(mc, mr * 2.2, WARM, warm_glow)
    if ga > 0.001:
        oy = u * 1100
        f.put(L['ridge_far'], cam, oy=oy * 0.9, alpha=ga); f.put(L['ridge_near'], cam, oy=oy, alpha=ga)
        f.put(L['dome'], cam, oy=oy, alpha=ga); tip = LD.dome_slit(f, L['dome'], cam, open_, tilt, dy=oy, a=ga)
        f.put(L['fg'], cam, oy=oy * 1.1, alpha=ga)
        wb(f, cam, 1.0, (270, 965, 810, 1355), 'dome', transient=u > 0.02)
    ea = ease(seg(u, 0.0, 0.7))
    if ea > 0: f.put(LD.earth_cap_layer(), cam, oy=(1 - u) * 560, alpha=ea)
    return mc, mr, tip


def question_dots():
    return [(450, 700), (468, 648), (516, 616), (572, 622), (602, 664), (588, 712), (548, 746), (540, 790), (540, 850)]


def bead_world_y(t):
    tau = t - 7.73
    if tau < 0: return None
    s = 157 * tau + 90 * (1 - math.exp(-tau / 0.18))
    return TIP[1] - s if s <= 430 else None


def trip_bead(f, cam, t, t0, tm, t1, size=1.0):
    if t0 <= t < tm: bead(f, 540, cam.map(1.0, 540, yp(seg(t, t0, tm)))[1], WARM, size, (0, 1), 90)
    elif tm <= t < t1: bead(f, 540, cam.map(1.0, 540, yp(1 - seg(t, tm, t1)))[1], COOL, size, (0, -1), 90)


def target_ring(f, cam, t, a=1.0, flash=0.0):
    c = cam.map(0.96, 540, 548); s = cam.xf(0.96)[0]
    ring(f, c, 30 * s, WARM, 5, 0.95 * a, dashed=True); f.circle(c, 5 * s, fill=WARM, a=a)
    if flash > 0: ring(f, c, 30 * s + 60 * s * flash, WARM, 5, (1 - flash) * 0.9, False)


def sc_open(t):
    f = Frame(); u = ease(seg(t, 8.04, 8.9)); g8 = ground_cam(8.04)
    cam = ground_cam(t) if t < 8.04 else (Cam(540, lerp(g8.cy, 960, u), lerp(g8.z, 1.0, u)) if t < 8.9 else Cam())
    open_ = 0.12 + 0.88 * ease(seg(t, 0.2, 1.6)); k3 = seg(t, 5.1, 6.2)
    tilt = 0.22 * (1 - ease(k3)) - 0.025 * math.sin(math.pi * k3) ** 2 * (1 - k3)
    cone = ease(seg(t, 3.55, 4.1)) * (1 - ease(seg(t, 4.35, 4.85)))
    mc, mr, tip = world(f, cam, u, open_, tilt, warm_glow=0.30 * cone)
    s = cam.xf(1.0)[0]
    # B02: the rejected floodlight idea (dashed outline only, never a real beam)
    if cone > 0.01 and t < 5.2:
        P = lambda x, y: cam.map(1.0, x, y)
        poly = [P(520, 990), P(560, 990), P(715, 590), P(365, 590)]
        f.poly(poly, fill=WARM, a=0.10 * cone)
        f.dashed(poly[0], poly[3], WARM, 4, 22, 16, 0.85 * cone, off=t * 30); f.dashed(poly[1], poly[2], WARM, 4, 22, 16, 0.85 * cone, off=t * 30)
        rr = ease(seg(t, 4.2, 4.5)) * (1 - ease(seg(t, 4.9, 5.2)))
        if rr > 0:
            c = (mc[0], mc[1]); R = mr * 1.35; ring(f, c, R, RED, 8, rr); f.line([(c[0] - R * 0.7, c[1] + R * 0.7), (c[0] + R * 0.7, c[1] - R * 0.7)], RED, 8, rr)
    # B03: a question made of pulse-marker dots, then they collapse into one bead
    if 5.3 < t < 7.5 and tip:
        for i, (dx, dy) in enumerate(question_dots()):
            a_in = eout(seg(t, 5.3 + 0.07 * i, 5.75 + 0.07 * i)); a_out = ein(seg(t, 6.75 + 0.03 * i, 7.35 + 0.03 * i))
            q = a_in * (1 - a_out); sx, sy = cam.map(1.0, dx, dy); tx, ty = tip
            px, py = lerp(tx, sx, a_in), lerp(ty, sy, a_in); px, py = lerp(px, tx, a_out), lerp(py, ty, a_out)
            py += 4 * math.sin(t * 2 + i) * (1 - a_out) * a_in
            f.glow((px, py), 28 * s, WARM, 0.45 * (a_in * (1 - a_out))); f.circle((px, py), 11 * s, fill=mix(WARM, (255, 255, 255), 0.6), a=min(1, q * 1.4))
    if tip and 7.3 < t < 7.73:
        g = ease(seg(t, 7.3, 7.73)); f.glow(tip, 70 * s, WARM, 0.6 * g); f.circle(tip, 9 * s * g, fill=mix(WARM, (255, 255, 255), 0.7))          # anticipation: the aperture charges
    # the launched pulse (symbol, time-stretched): quick kick, then steady climb on the Earth-Moon line
    by = bead_world_y(t)
    if by is not None and t < 9.95:
        sx, sy = cam.map(1.0, 540, by); bead(f, sx, sy, WARM, 1.0 * (0.7 + 0.3 * min(1, s)), (0, 1), 110); f.keys.append(('~bead', (sx - 30, sy - 30, sx + 30, sy + 30)))
    # B05: target ring on the Moon, guide path, one 'not to scale'
    if t > 8.43:
        a = ease(seg(t, 8.43, 8.75)); fl = seg(t, 9.90, 10.45)
        target_ring(f, cam, t, a * (1 - 0.0), flash=fl if 0 < fl < 1 else 0)
    if t > 8.9:
        guide(f, 0.42 * ease(seg(t, 8.9, 9.4)), grow=eout(seg(t, 8.9, 9.5)))
        ta = ease(seg(t, 9.0, 9.4)) * (1 - ease(seg(t, 11.2, 11.8)))
        if ta > 0: tag(f, (880, 1350), 'NOT TO SCALE', ta, 28)
    if t >= 11.28: trip_overlays(f, cam, t)
    return f


def trip_overlays(f, cam, t):
    """B06-B11: stopwatch, round-trip pulse (slowed 1.84x), traces, brackets and leg timers."""
    sa = ease(seg(t, 11.30, 11.85))
    if t < 21.55: val = 2.56 * seg(t, 11.42, 16.14)
    elif t < 21.83: val = 2.56 * (1 - ease(seg(t, 21.55, 21.83)))
    elif t < 24.08: val = 1.28 * seg(t, 21.83, 23.48)
    else: val = 1.28 + 1.28 * seg(t, 24.08, 25.32)
    if t < 26.4: stopwatch(f, val, sa, big=1.0)
    trip_bead(f, cam, t, 11.42, 13.78, 16.14) if t < 17 else None
    fl = seg(t, 13.78, 14.3)
    if 0 < fl < 1: target_ring(f, cam, t, 1.0, flash=fl)
    if t > 16.14 and t < 16.5: f.glow((540, LIMB_Y - 14), 60, COOL, 0.5 * (1 - seg(t, 16.14, 16.5)))
    # B07 big readout
    if 15.7 < t < 17.5:
        pop = ease(seg(t, 15.85, 16.2)); sc = 0.86 + 0.14 * pop + 0.06 * math.sin(math.pi * seg(t, 16.0, 16.5)) * (1 - seg(t, 16.0, 16.5))
        a = pop * (1 - ease(seg(t, 17.2, 17.5))); num(f, (850, 250), '2.56 s', int(74 * sc), WHITE, a); f.key('readout', (680, 205, 1020, 295))
    # B08 traces: out, then back (the traced path survives to B33-34)
    tr_a = ease(seg(t, 17.65, 17.9)) * (1 - 0.65 * ease(seg(t, 21.6, 21.9))) if t < 26.4 else 0
    if t >= 17.65 and t < 26.4:
        leg_traces(f, up=eout(seg(t, 17.7, 18.55)), down=eout(seg(t, 18.65, 19.35)), a=tr_a)
        f.key('trace', (470, PATH_TOP, 610, LIMB_Y))
    # B09: bracket, struck "2.5 s", then split in two at the Moon turn-around
    ba = ease(seg(t, 19.85, 20.15)) * (1 - ease(seg(t, 21.55, 21.85)))
    if ba > 0:
        sp = ease(seg(t, 20.9, 21.35)); y0, y1 = yp(0), yp(1); ym = (y0 + y1) / 2
        if sp < 0.01: LD.bracket(f, 690, y0, y1, WHITE, T, ba)
        else:
            gap = 18 * sp; LD.bracket(f, 690, y0, ym + gap, WHITE, T, ba); LD.bracket(f, 690, ym - gap, y1, WHITE, T, ba)
        if sp < 0.01: num(f, (835, ym), '2.56 s', 44, WHITE, ba)
        else:
            num(f, (835, lerp(ym, (ym + y0) / 2 + 0, sp)), '1.28 s', 44, COOL, ba * sp); num(f, (835, lerp(ym, (ym + y1) / 2, sp)), '1.28 s', 44, WARM, ba * sp)
        x = ease(seg(t, 20.25, 20.55)) * (1 - ease(seg(t, 20.85, 21.1)))
        if x > 0:
            cx_, cy_ = 835, yp(0.5) - 120; num(f, (cx_, cy_), '2.5 s', 42, mix(BG, RED, x) if False else RED, x * 0.9)
            f.line([(cx_ - 70, cy_ - 34), (cx_ + 70, cy_ + 34)], RED, 7, x); f.line([(cx_ + 70, cy_ - 34), (cx_ - 70, cy_ + 34)], RED, 7, x)
    # B10 / B11 leg timers pinned to their legs
    if 23.3 < t < 26.4:
        a = ease(seg(t, 23.3, 23.7)); num(f, (390, yp(0.5)), '1.28 s', 40, WARM, a * 0.95, 'mm')
    if t > 25.2 and t < 26.4: num(f, (690, yp(0.5)), '1.28 s', 40, COOL, ease(seg(t, 25.2, 25.5)) * 0.95)
    if 21.83 <= t < 23.5: pass
    if 21.83 <= t < 23.48: bead(f, 540, cam.map(1.0, 540, yp(seg(t, 21.83, 23.48)))[1], WARM, 1.0, (0, 1), 90)
    if 24.08 <= t < 25.32: bead(f, 540, cam.map(1.0, 540, yp(1 - seg(t, 24.08, 25.32)))[1], COOL, 1.0, (0, -1), 90)
    if 23.48 <= t < 24.0:
        target_ring(f, cam, t, 1.0, flash=seg(t, 23.48, 24.0))
    guide(f, 0.30)


# ---- orbit
ORB_F = (560, 1080); ORB_A = 360; ORB_E = 0.22
def orb_pos(th):
    r = ORB_A * (1 - ORB_E ** 2) / (1 + ORB_E * math.cos(th)); return (ORB_F[0] + r * math.cos(th), ORB_F[1] - r * math.sin(th)), r
RMIN = ORB_A * (1 - ORB_E ** 2) / (1 + ORB_E); RMAX = ORB_A * (1 - ORB_E ** 2) / (1 - ORB_E)
def orb_theta(t): return 0.25 + (math.pi - 0.25) * ease(seg(t, 26.9, 30.9))


def sc_orbit(t):
    f = Frame(); cam = Cam(); space(f, cam, 0.6)
    gfade = 1 - ease(seg(t, 31.35, 31.9))                       # B14: graphics fade after the hold
    th = orb_theta(t); mp, r = orb_pos(th); fr = (r - RMIN) / (RMAX - RMIN); km = int(round((357000 + 50000 * fr) / 1000.0) * 1000)
    pts = [orb_pos(i / 120 * 2 * math.pi)[0] for i in range(121)]
    f.line(pts, (150, 158, 176), 3, 0.55 * gfade, cap=False)
    ea = 1 - ease(seg(t, 32.2, 33.0))
    f.put(Layer(sph('earth', 70).img, ORB_F[0] - 70 - 4, ORB_F[1] - 70 - 4, 1.0, 2), cam, alpha=ea)
    # Moon: orbit sprite (r 56) until it begins to grow, then the big sprite
    g = seg(t, 31.75, 33.55); rr = 56 * (1500 / 56) ** g if g > 0 else 56
    cpos = (lerp(mp[0], 540, ease(seg(t, 31.75, 33.2))), lerp(mp[1], 900, ease(seg(t, 31.75, 33.2))))
    mal = 1 - ease(seg(t, 33.15, 33.6))
    if mal > 0:
        if g > 0: put_moon(f, cam, cpos, rr, 1.0, big=True, alpha=mal, glow=0.0, key=False)
        else: put_moon(f, cam, mp, 56, 1.0, big=False, alpha=1.0, glow=0.0, key=False)
        f.keys.append(('~moon' if rr > 480 else 'moon', (cpos[0] - min(rr, 560), cpos[1] - min(rr, 560), cpos[0] + min(rr, 560), cpos[1] + min(rr, 560))) if g > 0 else ('moon', (mp[0] - 56, mp[1] - 56, mp[0] + 56, mp[1] + 56)))
    if gfade > 0:
        ex = (ORB_F[0] + 74 * (mp[0] - ORB_F[0]) / math.dist(mp, ORB_F), ORB_F[1] + 74 * (mp[1] - ORB_F[1]) / math.dist(mp, ORB_F))
        mx = (mp[0] - 60 * (mp[0] - ORB_F[0]) / math.dist(mp, ORB_F), mp[1] - 60 * (mp[1] - ORB_F[1]) / math.dist(mp, ORB_F))
        f.line([ex, mx], WARM, 6, 0.95 * gfade)
        num(f, (540, 1310), '%s km' % format(km, ','), 50, WARM, gfade); f.key('km', (300, 1270, 780, 1350))
        tag(f, (880, 330), 'orbit exaggerated', ease(seg(t, 26.6, 27.1)) * (1 - ease(seg(t, 29.0, 29.6))) * gfade, 24)
        if t >= 28.72: stopwatch(f, 2.38 + 0.33 * fr, ease(seg(t, 28.72, 29.2)) * gfade)
    return f


# ---- surface (reflector, ghost mirror, astronaut)
RX, RY = LD.surface_points()
AST_STANCE = (800, 1372)

def surf_cam(t):
    if t < 38.65: return Cam(490, 1180, 2.0 + 0.02 * clamp((t - 33.1) / 5.55))
    if t < 42.62:
        k = ease(seg(t, 38.65, 41.5)); return Cam(lerp(490, 545, k), lerp(1180, 1130, k), lerp(2.02, 1.0, k))
    ee = ease(seg(t, 42.8, 43.85)); z = lerp(1.0, 2.6, ee) - 0.03 * math.sin(math.pi * seg(t, 42.62, 42.82))
    return Cam(lerp(545, 486, ee), lerp(1130, 1151, ee), z)


def walk_s(w): return w if w < 0.72 else 0.72 + 0.28 * (1 - (1 - (w - 0.72) / 0.28) ** 2)


def sc_surface(t):
    f = Frame(); cam = surf_cam(t); f.cam = cam; f.im.paste(Image.new('RGB', f.im.size, (0, 0, 0)))
    SL = LD.surface_layers(); f.put(SL['plate_far'], cam); f.put(SL['plate_near'], cam)
    s = cam.xf(1.0)[0]
    # B15: faint pulse lands, scatters everywhere, nothing comes straight back
    imp = (RX, RY - 40)
    if 33.1 < t < 34.6:
        lan = seg(t, 33.15, 33.5)
        if 0 < lan < 1:
            sx, sy = cam.map(1.0, imp[0], lerp(620, imp[1], lan)); bead(f, sx, sy, WARM, 0.75, (0, -1), 80, 0.9)
        sc_ = ease(seg(t, 33.5, 33.95)) * (1 - ease(seg(t, 34.1, 34.5)))
        if sc_ > 0:
            ix, iy = cam.map(1.0, *imp)
            for i in range(9):
                ang = math.pi * (1.06 + 0.88 * i / 8); ln = (150 + 60 * ((i * 5) % 3)) * sc_ * s
                x1, y1 = ix + ln * math.cos(ang), iy + ln * 0.62 * math.sin(ang)
                f.line([(ix + 14 * math.cos(ang), iy + 9 * math.sin(ang)), (x1, y1)], WARM, 5, 0.78 * (1 - 0.3 * sc_)); f.poly([(x1, y1), (x1 - 18 * math.cos(ang + 0.45), y1 - 18 * 0.62 * math.sin(ang + 0.45)), (x1 - 18 * math.cos(ang - 0.45), y1 - 18 * 0.62 * math.sin(ang - 0.45))], fill=WARM, a=0.78)
        if t > 33.49:
            a2 = ease(seg(t, 33.49, 33.9)) * (1 - ease(seg(t, 34.2, 34.5)))
            x0_, y0_ = cam.map(1.0, imp[0], imp[1] - 10); f.dashed((x0_, y0_), (x0_, max(120, y0_ - 560)), GREY, 4, 22, 18, 0.7 * a2)
    # reflector + ghost mirror (same spot, same scale: match cut)
    ghost = ease(seg(t, 34.65, 35.3)) * (1 - ease(seg(t, 37.62, 38.05)))
    real = ease(seg(t, 37.62, 38.05)) if t < 38.1 else 1.0
    settle = 0.0
    if t > 39.95: tau = t - 39.95; settle = 7 * math.exp(-tau / 0.14) * math.cos(2 * math.pi * tau / 0.36)
    P = lambda x, y: cam.map(1.0, x, y)
    if ghost > 0.01:
        gp = [P(RX - 170, RY - 6), P(RX + 165, RY - 6), P(RX + 112, RY - 196), P(RX - 112, RY - 196)]
        f.poly(gp, fill=(236, 240, 250), a=0.16 * ghost)
        for i in range(4): f.dashed(gp[i], gp[(i + 1) % 4], (240, 244, 252), 5, 24, 16, 0.9 * ghost, off=t * 24)
        f.line([P(RX - 60, RY - 40), P(RX + 10, RY - 160)], (240, 244, 252), 4, 0.35 * ghost, cap=False)
        pr = 70 + 8 * math.sin(t * 3.2); c = P(RX, RY - 360); ring(f, c, pr * s, WARM, 6, 0.9 * ghost, dashed=False)
        f.text(c, '?', int(110 * s), WHITE, 'heavy', a=ghost)
    if real > 0.01:
        k = LD.FS * LD.PS; rl = LD.refl_layer(1.0)
        LD.contact_shadow(f, cam, 1.0, (RX + 30, RY - 6), 330, 60, 0.5 * real)
        f.put(rl, cam, oy=settle * s, alpha=real, key='reflector')
        wb(f, cam, 1.0, (RX - 190, RY - 235, RX + 190, RY + 10), 'reflector')
    # B18: astronaut walks in (whole-cutout translation + bob: placeholder for a rig)
    if t > 38.65:
        w = seg(t, 38.7, 39.85); ax = lerp(1330, AST_STANCE[0], walk_s(w)); moving = 0 < w < 1
        bob = -7 * abs(math.sin(2 * math.pi * 1.7 * (t - 38.7))) * (1 if moving else 0)
        ay = AST_STANCE[1] + bob
        LD.contact_shadow(f, cam, 1.0, (ax + 20, AST_STANCE[1] - 4), 190, 44, 0.55)
        f.put(LD.astro_layer(ax, ay, 1.0), cam)
        wb(f, cam, 1.0, (ax - 130, AST_STANCE[1] - 560, ax + 130, AST_STANCE[1]), 'astronaut', transient=moving or w < 0.01 or cam.z > 1.3)
        ballistic(f, cam, (RX + 40, RY - 20), t, 39.95, 16, 4, 420, 380, (176, 172, 168), 7, 1.2)
    return f


# ---- optics (B19-B21): light enters from BELOW (Earth at the bottom in the film's grammar) and leaves back down
FLIP = 1700
RAYS20 = ((-250, 10), (-30, 20), (230, -10))

def check(f, c, s, col, a=1.0, w=9):
    f.line([(c[0] - s * 0.5, c[1]), (c[0] - s * 0.1, c[1] + s * 0.4), (c[0] + s * 0.55, c[1] - s * 0.45)], col, w, a)

def cross(f, c, s, col, a=1.0, w=9):
    f.line([(c[0] - s * 0.5, c[1] - s * 0.5), (c[0] + s * 0.5, c[1] + s * 0.5)], col, w, a); f.line([(c[0] + s * 0.5, c[1] - s * 0.5), (c[0] - s * 0.5, c[1] + s * 0.5)], col, w, a)


def sc_optics(t, with_iris=False):
    f = Frame(); f.im.paste(Image.new('RGB', f.im.size, (9, 14, 32)))
    k = ease(seg(t, 46.98, 47.55))
    cx = lerp(540, 300, k); L = lerp(380, 240, k); cy = 980
    if t < 47.0 + 0.0 or t < 47.55:
        prog = clamp((t - 44.95) / 0.62, 0, 3.0); a3 = 1 - ease(seg(t, 47.2, 47.55))
        LD.cube_diagram(f, prog, RAYS20, cx, cy, L, T, a=1.0 if a3 >= 1 else 1.0, flip=FLIP) if a3 > 0.99 else LD.cube_diagram(f, 3.0, RAYS20, cx, cy, L, T, a=a3, flip=FLIP)
    else:
        LD.cube_diagram(f, seg(t, 47.55, 48.3), ((-165, 12),), cx, cy, L, T, flip=FLIP, dimmed=1.0)
    V, A, Bc = LD.cube_geo(cx, cy, L); f.key('cube', (cx - L, FLIP - V[1] - 10, cx + L, FLIP - V[1] + L + 330))
    if 44.25 < t < 45.4: tag(f, (540, 1380), 'simplified 2-D cutaway', ease(seg(t, 44.25, 44.6)) * (1 - ease(seg(t, 45.0, 45.4))), 26)
    # footprint inset enters on "tiny fraction" (45.55 s); the main ray keeps returning in full
    ia = ease(seg(t, 45.55, 45.95)) * (1 - ease(seg(t, 47.0, 47.35)))
    if ia > 0.01:
        c = (880, 330 + 18 * (1 - ia)); r = 112 * (0.8 + 0.2 * ia)
        f.circle(c, r, fill=(14, 22, 46), outline=GREY, w=T['sw'], a=ia); f.glow(c, r * 0.95, WARM, 0.55 * ia)
        f.rrect((c[0] - 6, c[1] - 6, c[0] + 6, c[1] + 6), 2, fill=(255, 255, 255), a=ia); f.circle(c, r + 8, outline=(10, 14, 28), w=2, a=0)
        f.line([(c[0] + r * 0.72, c[1] + r * 0.72), (c[0] + r * 0.98, c[1] + r * 0.98)], GREY, 9, ia)           # magnifier tab
        tag(f, (c[0], c[1] + r + 34), 'magnified', ia, 24); f.key('inset', (c[0] - r, c[1] - r, c[0] + r, c[1] + r + 50))
    # B21: the flat mirror beside the cube
    if t >= 47.2:
        ma = ease(seg(t, 47.35, 47.8)); M = (800, 930); th = math.radians(-28); m = (math.cos(th), math.sin(th)); n = (-m[1], m[0])
        p0 = (M[0] - m[0] * 135, M[1] - m[1] * 135); p1 = (M[0] + m[0] * 135, M[1] + m[1] * 135)
        f.line([p0, p1], (200, 206, 220), 14, ma, cap=False); f.line([(p0[0] - n[0] * 7, p0[1] - n[1] * 7), (p1[0] - n[0] * 7, p1[1] - n[1] * 7)], (120, 128, 148), 4, ma, cap=False)
        d = (math.sin(math.radians(12)), -math.cos(math.radians(12))); dn = d[0] * n[0] + d[1] * n[1]; r_ = (d[0] - 2 * dn * n[0], d[1] - 2 * dn * n[1])
        S0 = (M[0] - d[0] * 320, M[1] - d[1] * 320)
        f.line(LD.partial_path([S0, M], ease(seg(t, 47.55, 48.0))), WARM, T['sw'] * 1.4, ma)
        if t > 48.0: f.line(LD.partial_path([M, (M[0] + r_[0] * 250, M[1] + r_[1] * 250)], ease(seg(t, 48.0, 48.35))), COOL, T['sw'] * 1.4, ma * 0.65)
        f.key('mirror', (640, 700, 1010, 1260))
        if t > 48.25:
            va = ease(seg(t, 48.25, 48.5)); check(f, (cx - 30, 1250), 64, COOL, va); cross(f, (960, 1130), 64, RED, va)
    return f


def sc_iris(t):
    """B19: push into the array face, then a magnifier-ring iris opens onto the cross-section."""
    a = sc_surface(t); R = lerp(0, 1330, ease(seg(t, 43.6, 44.4)))
    if R <= 2: return a
    b = sc_optics(t); m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).ellipse([W / 2 - R, H / 2 - R, W / 2 + R, H / 2 + R], fill=255)
    out = Frame(Image.composite(b.im, a.im, m)); out.keys = b.keys if R > 1150 else a.keys + b.keys
    if R < 1150: out.circle((W / 2, H / 2), R, outline=WHITE, w=T['sw'], a=1 - R / 1200)
    return out


# ---- B22-B24: back on Earth, the telescope
def telescope_cutaway(f, t):
    f.im.paste(Image.new('RGB', f.im.size, (11, 15, 28)))
    x0, x1, y0, y1 = 380, 700, 430, 1240
    f.rrect((x0 - 14, y0 - 10, x1 + 14, y1 + 14), 34, fill=(44, 52, 74)); f.rrect((x0, y0, x1, y1), 24, fill=(18, 24, 42))
    f.line([(x0 - 14, y0 + 20), (x0 - 14, y1 - 20)], (130, 142, 170), 4, 0.9, cap=False)                      # light catches the left edge (upper-left light)
    f.line([(540, y0 - 40), (540, y1)], GREY, 3, 0.18)
    f.d.pieslice([x0 + 8, y1 - 150, x1 - 8, y1 + 70], 0, 180, fill=(138, 156, 186)); f.d.pieslice([x0 + 36, y1 - 128, x1 - 36, y1 + 50], 0, 180, fill=(70, 88, 120))
    f.line([(x0 + 14, y1 - 38), (x1 - 14, y1 - 38)], (190, 204, 226), 6, 0.8, cap=False)
    f.poly([(508, 668), (576, 612), (588, 628), (520, 684)], fill=(196, 206, 226)); f.line([(540, 640), (540, 430)], (70, 80, 106), 5, 0.8, cap=False)    # diagonal flat + spider
    f.rrect((700, 590, 840, 700), 10, fill=(56, 64, 90), outline=GREY, w=4); f.line([(x1, 645), (700, 645)], (56, 64, 90), 18, cap=False)
    det = (770, 645); lit = ease(seg(t, 51.39, 51.75))
    rx_ = [440, 485, 595, 640]; dn = ease(seg(t, 50.55, 51.1)); up = ease(seg(t, 51.0, 51.38))
    for x in rx_:
        f.line(LD.partial_path([(x, y0 - 70), (x, y1 - 40)], dn), COOL, 6, 0.9)
        if up > 0: f.line(LD.partial_path([(x, y1 - 40), (540, 640)], up), COOL, 6, 0.9)
    if up > 0: f.line(LD.partial_path([(540, 640), det], ease(seg(t, 51.2, 51.39))), COOL, 8, 0.95)
    if lit > 0:
        f.glow(det, 110 * lit, COOL, 0.55 * lit); f.circle(det, 120 * lit, outline=WHITE, w=6, a=0.8 * lit); f.circle(det, 16, fill=mix(COOL, (255, 255, 255), 0.7), a=lit)
    f.key('telescope', (x0 - 20, y0 - 80, 860, y1 + 20))


def sc_return(t):
    """B22 ground view (cool bead descending) -> push into the tube; B23 cutaway; B24 dim ground view."""
    f = Frame()
    if t < 53.1:
        cam = Cam(540, lerp(960, 1010, ease(seg(t, 50.0, 50.4))), lerp(1.0, 1.7, ease(seg(t, 50.0, 50.4))))
        world(f, cam, 0.0, 1.0, 0.0)
        if t >= 50.2: f.keys = [k for k in f.keys if k[0] != 'dome']
        by = lerp(-60, 1010, seg(t, 49.58, 50.38)); sx, sy = cam.map(1.0, 540, by)
        if t < 50.45: bead(f, sx, sy, COOL, 1.0, (0, -1), 120); f.keys.append(('~bead', (sx - 30, sy - 30, sx + 30, sy + 30)))
        if t >= 50.2:
            c = Frame(); telescope_cutaway(c, t); f.im = blend(f.im, c.im, ease(seg(t, 50.2, 50.5))); f.d = ImageDraw.Draw(f.im, 'RGBA'); f.keys += c.keys if t > 50.35 else []
    else:
        cam = Cam(540, 960, 1.0 + 0.05 * ease(seg(t, 53.1, 55.0)))
        world(f, cam, 0.0, 1.0, 0.0)
        f.veil(BG, 0.55 * ease(seg(t, 53.3, 54.1)))
        if t < 53.5:
            c = Frame(); telescope_cutaway(c, 53.1); f.im = blend(c.im, f.im, ease(seg(t, 53.1, 53.5))); f.d = ImageDraw.Draw(f.im, 'RGBA')
    return f


# ---- B25: two widening cones
def sc_cones(t):
    f = Frame(); cam = Cam(); u = ease(seg(t, 55.0, 55.7))
    mc, mr, _ = world(f, cam, u, 1.0, 0.0)
    if t < 55.0 + 0.0: return f
    o = ease(seg(t, 55.25, 56.45)); r = ease(seg(t, 56.3, 57.55)); shrink = ease(seg(t, 57.4, 58.4))
    yb = LIMB_Y - 6; ym = PATH_TOP + 18
    if o > 0:
        yt = lerp(yb, ym, o); hw = lerp(8, 66, o)
        f.poly([(540 - 6, yb), (540 + 6, yb), (540 + hw, yt), (540 - hw, yt)], fill=WARM, a=0.26)
        f.line([(540 - 6, yb), (540 - hw, yt)], WARM, 3, 0.6, cap=False); f.line([(540 + 6, yb), (540 + hw, yt)], WARM, 3, 0.6, cap=False)
    if o > 0.95:
        f.rrect((540 - 6, ym - 5, 540 + 6, ym + 7), 2, fill=(255, 255, 255)); f.key('array', (520, ym - 20, 560, ym + 20))
    if r > 0:
        yt = lerp(ym + 12, yb - 8, r); hw = lerp(8, 215, r) * (1 - 0.0)
        a = 0.24 * (1 - 0.85 * shrink)
        f.poly([(540 - 6, ym + 12), (540 + 6, ym + 12), (540 + hw, yt), (540 - hw, yt)], fill=COOL, a=a)
        f.line([(540 - 6, ym + 12), (540 - hw, yt)], COOL, 3, 0.55 * (1 - 0.85 * shrink), cap=False); f.line([(540 + 6, ym + 12), (540 + hw, yt)], COOL, 3, 0.55 * (1 - 0.85 * shrink), cap=False)
    if r > 0.9:
        f.circle((540, LIMB_Y - 6), 6, fill=(255, 255, 255)); ring(f, (540, LIMB_Y - 6), 18 + 4 * math.sin(t * 5), WHITE, 3, 0.7 * (1 - 0.8 * shrink))
    if t > 58.2: f.veil(BG, ease(seg(t, 58.2, 58.69)))
    return f


# ---- B26-B30: counting photons
def photon_base():
    f = Frame(); f.im.paste(Image.new('RGB', f.im.size, BG)); f.put(LD.stars_space(2), Cam(), alpha=0.28); return f

AX_Y = 1250
def time_axis_notes(f, a=1.0, X0=140, X1=940):
    f.circle((X0 - 4, AX_Y - 34), 12, fill=WARM, a=a); f.glow((X0 - 4, AX_Y - 34), 30, WARM, 0.4 * a)
    f.line([(X0 + 20, AX_Y + 64), (X1 - 40, AX_Y + 64)], GREY, 3, 0.55 * a, cap=False); f.poly([(X1 - 40, AX_Y + 54), (X1 - 18, AX_Y + 64), (X1 - 40, AX_Y + 74)], fill=GREY, a=0.55 * a)
    tag(f, (X0 + 20, AX_Y + 104), 'pulse sent', 0.9 * a, 24, 'lm'); tag(f, (X1 - 20, AX_Y + 104), 'time', 0.9 * a, 24, 'rm')

def sc_photons(t):
    f = photon_base(); X0, X1 = 140, 940
    if t < 61.65:
        a = ease(seg(t, 58.69, 59.2)); LD.hist_draw(f, 0, T, AX_Y, X0, X1, a=a); time_axis_notes(f, a)
        tag(f, (X0, AX_Y + 58), 'time of flight', a * 0.9, 24, 'lm') if False else None
        for i, (fx, te) in enumerate(((0.52, 59.85), (0.64, 60.55), (0.60, 61.29))):
            x = X0 + (X1 - X0) * fx; fall = ein(seg(t, te - 0.6, te)); y = lerp(640, AX_Y - 8, fall)
            if t > te - 0.6 and t < te: f.glow((x, y), 60, COOL, 0.5); f.circle((x, y), 15, fill=mix(COOL, WHITE, 0.6))
            if t >= te:
                q = seg(t, te, te + 0.5); ring(f, (x, AX_Y - 8), 10 + 46 * eout(q), COOL, 3, (1 - q) * 0.9)
                f.rrect((x - 6, AX_Y - 70, x + 6, AX_Y - 4), 3, fill=mix(COOL, WHITE, 0.2)); f.key('mark', (x - 20, AX_Y - 80, x + 20, AX_Y))
        # clicks echo the word "photons"
    else:
        n = 6 + 394 * ease(seg(t, 61.65, 63.35)) ** 1.3; fade = 1 - ease(seg(t, 63.75, 64.2))
        LD.hist_draw(f, n, T, AX_Y, X0, X1, 1.0, 9, 16, COOL, fade); time_axis_notes(f, fade)
        f.key('hist', (X0, AX_Y - 560, X1, AX_Y + 20))
        num(f, (X1, 330), 'pulses  %s' % format(int(n * 4), ','), 36, GREY, fade, 'rm')
        tag(f, (X1, 380), 'illustrative', ease(seg(t, 62.0, 62.4)) * fade * 0.8, 24, 'rm')
        if t >= 63.71:
            for i, (x, y) in enumerate(((380, 900), (540, 980), (700, 900))):
                a = ease(seg(t, 63.95 + 0.2 * i, 64.3 + 0.2 * i))
                if a > 0:
                    f.glow((x, y), 84, COOL, 0.62 * a); f.circle((x, y), 15, fill=mix(COOL, WHITE, 0.65), a=a); ring(f, (x, y), 44 + 6 * math.sin(t * 4 + i), COOL, 3, 0.55 * a); f.key('dot', (x - 50, y - 50, x + 50, y + 50))
    return f


def sc_atmos(t):
    f = Frame(); cam = Cam(); space(f, cam, 0.7); f.put(LD.earth_cap_layer(), cam)
    ba = ease(seg(t, 65.7, 66.1)) * (1 - ease(seg(t, 67.8, 68.4)))
    def band(x): return 1090 + 16 * math.sin(x / 90 + t * 1.4) + 9 * math.sin(x / 37 - t * 2.1)
    xs = list(range(0, W + 1, 24))
    f.poly([(x, band(x)) for x in xs] + [(W, LIMB_Y + 20), (0, LIMB_Y + 20)], fill=COOL, a=0.10 * ba)
    for j in range(3): f.line([(x, band(x) + 40 * j + 8 * math.sin(x / 70 + j + t)) for x in xs], COOL, 3, (0.35 - 0.08 * j) * ba, cap=False)
    if t < 66.0: yb = None
    elif t < 67.0: yb = lerp(LIMB_Y - 6, 1090, seg(t, 66.0, 67.0))
    else: yb = lerp(1090, -60, seg(t, 67.0, 67.65))
    inband = 66.0 < t < 67.0; wob = 16 * math.sin(t * 11) * (1 - ease(seg(t, 66.85, 67.2))) * ease(seg(t, 66.0, 66.2))
    if yb is not None and yb > -50:
        bead(f, 540 + (wob if yb > 1050 else wob * 0.3), yb, WARM, 1.0, (0, 1), 100); f.keys.append(('~bead', (500, yb - 30, 580, yb + 30)))
    if t > 66.2:
        e = ease(seg(t, 66.3, 66.8)); ew = 74 + 6 * math.sin(t * 7) * (1 - ease(seg(t, 66.9, 67.2)))
        for k_ in (-1, 0, 1):
            amp = abs(wob) * (0.5 if k_ else 0)
            f.circle((540, 760), 1, a=0) if False else None
            f.d.ellipse([540 - ew + k_ * amp * 1.6, 760 - 26, 540 + ew + k_ * amp * 1.6, 760 + 26], outline=WARM + (int(255 * 0.5 * e * (0.5 if k_ else 1)),), width=3)
    if t > 67.21:
        c = ease(seg(t, 67.21, 67.5)); check(f, (810, 1170), 70, WHITE, c); f.key('tick', (760, 1130, 860, 1210))
    return f


def sc_hist2(t):
    f = photon_base(); X0, X1 = 140, 940
    sh = lerp(1.0, 0.42, ease(seg(t, 69.4, 72.0))) if t < 72.65 else 0.42
    sc_ = lerp(9, 15, ease(seg(t, 69.4, 72.0)))
    a = ease(seg(t, 68.56, 68.95)); LD.hist_draw(f, 420, T, AX_Y, X0, X1, sh, sc_, 16, COOL, a); time_axis_notes(f, a); f.key('hist', (X0, AX_Y - 600, X1, AX_Y + 20))
    if t >= 72.65:
        w = lerp(150, 14, ease(seg(t, 72.7, 73.9))); px = X0 + (X1 - X0) * 0.64
        f.line([(px - w, AX_Y + 62), (px + w, AX_Y + 62)], WARM, 8, 1); f.line([(px - w, AX_Y + 46), (px - w, AX_Y + 78)], WARM, 6); f.line([(px + w, AX_Y + 46), (px + w, AX_Y + 78)], WARM, 6)
        f.key('errbar', (px - 160, AX_Y + 40, px + 160, AX_Y + 84))
    return f


# ---- B31-B36: the formula as a transformation
Y_BAR = 1290; BX0, BXM, BX1 = 150, 540, 930
def schem_base(f, cam, dimk=0.55):
    space(f, cam, 0.7); f.put(LD.earth_cap_layer(), cam, alpha=dimk); put_moon(f, cam, p=0.96, glow=0.10)

def lerp2(a, b, u): return (lerp(a[0], b[0], u), lerp(a[1], b[1], u))

def sc_formula(t):
    f = Frame(); cam = Cam(); schem_base(f, cam)
    ga = 0.55 * (1 - 0.3 * ease(seg(t, 80.9, 82.2))) if t < 84.3 else 0.55
    guide(f, ga * (1 - 0.5 * ease(seg(t, 80.9, 82.2)) * (1 if t < 84.3 else 0)))
    ws = LD.TOK['C']['sw']
    # B32: stopwatch drops in and the pulse makes one trip (77.5 - 78.9)
    if 77.0 <= t < 79.0:
        d = ease(seg(t, 77.0, 77.5)); stopwatch(f, 2.56 * seg(t, 77.5, 78.9), d, c=(190, lerp(-120, 250, d)))
        trip_bead(f, cam, t, 77.5, 78.2, 78.9)
        fl = seg(t, 78.2, 78.7)
        if 0 < fl < 1: target_ring(f, cam, t, 1.0, flash=fl)
    elif t >= 79.0: stopwatch(f, 2.56, 1.0, digits=False) if t < 80.0 else None
    # B33 traced path (warm up, cool down) + bracket 't'
    P0w, P1w = (500, yp(0.02)), (500, yp(0.97)); P0c, P1c = (580, yp(0.97)), (580, yp(0.02))
    q = ease(seg(t, 79.0, 79.55)); u1 = ease(seg(t, 80.95, 82.15)); u2 = ease(seg(t, 81.15, 82.35))
    # B35 fold angle (cool half rotates about the midpoint with a small anticipation)
    fold = ease(seg(t, 82.95, 83.6)); ant = 0.14 * math.sin(math.pi * seg(t, 82.78, 82.96)) * (1 if fold == 0 else 0)
    # B36 return to the line
    u3 = ease(seg(t, 84.35, 85.3))
    if t < 80.95:
        a = q * (1 if t < 80.95 else 0)
        if a > 0:
            leg_traces(f, 1, 1, a); LD.bracket(f, 690, yp(0), yp(1), WHITE, T, a)
            lab = 't' if t > 79.76 else '2.56 s'; num(f, (800, yp(0.5)), lab, 70 if lab == 't' else 44, WHITE, a)
            f.key('trace', (470, PATH_TOP, 700, LIMB_Y))
        if 79.0 <= t < 80.0: stopwatch(f, 2.56, 1.0, digits=(t < 79.76))
        if t >= 79.76 and t < 80.9: num(f, (190, 360), 't', 60, WHITE, ease(seg(t, 79.76, 80.0)))
    elif t < 84.35 or True:
        # warm leg: line state -> bar state; cool leg: line state -> bar state (staggered). The traced path peels off the Earth-Moon line.
        wq0, wq1 = (BX0, Y_BAR), (BXM, Y_BAR); cq0, cq1 = (BXM, Y_BAR), (BX1, Y_BAR)
        if t < 84.35:
            w0, w1 = lerp2(P0w, wq0, u1), lerp2(P1w, wq1, u1); c0, c1 = lerp2(P0c, cq0, u2), lerp2(P1c, cq1, u2)
            wid_w = lerp(ws * 1.1, ws * 3.2, u1); wid_c = lerp(ws * 1.1, ws * 3.2, u2)
            if fold > 0 or ant != 0:
                q_ = math.pi * fold - ant; ex = BXM + (BX1 - BXM) * math.cos(q_); ey = Y_BAR - (BX1 - BXM) * math.sin(q_) * 0.62
                c0, c1 = (BXM, Y_BAR), (ex, ey)
                if fold >= 1: c0, c1 = (BXM, Y_BAR - 24), (BX0, Y_BAR - 24)
            f.line([w0, w1], WARM, wid_w, 1); f.line([c0, c1], COOL, wid_c, 1)
            f.key('bar', (BX0 - 20, Y_BAR - 200, BX1 + 20, Y_BAR + 40) if u1 > 0.9 else (470, PATH_TOP, 610, LIMB_Y))
            lb = ease(seg(t, 81.7, 82.05)) if t < 83.1 else 1.0
            lab = 'c  x  t' if t < 83.13 else 'c  x  t  /  2'
            if u2 > 0.6: num(f, (540, 1140), lab, 62, WHITE, lb); f.key('formula', (240, 1100, 840, 1180))
        else:
            m0 = lerp2((BX0, Y_BAR), (540, LIMB_Y - 20), u3); m1 = lerp2((BXM, Y_BAR), (540, PATH_TOP + 8), u3)
            col_w = mix(WARM, (240, 236, 224), u3); col_c = mix(COOL, (240, 236, 224), u3)
            f.line([m0, m1], col_w, ws * 3.2 * (1 - 0.55 * u3), 1); f.line([(m0[0], m0[1] - 24 * (1 - u3)), (m1[0], m1[1] - 24 * (1 - u3))], col_c, ws * 3.2 * (1 - 0.55 * u3), 1 - 0.7 * u3 if u3 > 0.5 else 1)
            if u3 > 0.55:
                ra = ease(seg(u3, 0.55, 1.0))
                for i in range(0, 11):
                    y = lerp(LIMB_Y - 20, PATH_TOP + 8, i / 10); f.line([(566, y), (606 if i % 5 else 640, y)], WHITE, 3, ra * 0.9, cap=False)
            lbl = 1 - ease(seg(t, 84.35, 84.8)); num(f, (540, 1140), 'c  x  t  /  2', 62, WHITE, lbl)
            f.key('ruler', (500, PATH_TOP, 660, LIMB_Y))
            da = ease(seg(t, 84.6, 85.1)); num(f, (835, 1000), 'd = 384,400 km', 40, WHITE, da); tag(f, (835, 1054), 'mean distance', da, 28); f.key('readout', (660, 970, 1010, 1080))
    return f


# ---- B37-B39: pull-back, last faint return, settle
def sc_close(t):
    f = Frame(); k = eout(seg(t, 86.4, 89.4)); cam = Cam(540, lerp(700, 960, k), lerp(1.5, 1.0, k)); f.cam = cam
    space(f, cam, 0.9); f.put(LD.stars_space(7), cam, alpha=0.0)
    f.put(LD.earth_cap_layer(), cam)
    drift = seg(t, 86.3, 92.5); mcen = (MOON_C[0] + 34 * drift, MOON_C[1] - 8 * drift)
    mc, rs = put_moon(f, cam, mcen, MOON_R, 0.9, glow=0.12)
    ex, ey = cam.map(1.0, 540, LIMB_Y - 10); top = (mc[0], mc[1] + rs * 0.98)
    ra = 0.55 * ease(seg(t, 86.3, 86.7)) * (1 - 0.45 * ease(seg(t, 87.0, 89.4)))
    f.line([(ex, ey), top], (240, 236, 224), 5, ra)
    for i in range(0, 11):
        p = (lerp(ex, top[0], i / 10), lerp(ey, top[1], i / 10)); f.line([(p[0] + 20, p[1]), (p[0] + (44 if i % 5 == 0 else 32), p[1])], WHITE, 3, ra * 0.9, cap=False)
    if t < 87.0:
        num(f, (835, 1000), 'd = 384,400 km', 40, WHITE, (1 - ease(seg(t, 86.35, 86.9))) * 0.9)
    if 89.3 <= t < 90.15:
        p = seg(t, 89.3, 90.0); bx = lerp(top[0], ex, p); by = lerp(top[1], ey, p)
        if p < 1: bead(f, bx, by, COOL, 0.55, (0, -1), 50, 0.9)
        else: pass
    if t >= 90.0:
        g = ease(seg(t, 90.0, 90.5)); f.glow((ex, ey), 56, COOL, 0.45 * g * (1 - 0.35 * ease(seg(t, 90.6, 92.0))))
    if t >= 91.0:
        a = ease(seg(t, 91.0, 91.4)); s_ = ease(seg(t, 91.2, 91.99)); val = int(round(lerp(384250, 384400, s_)))
        num(f, (835, 1000), '%s km' % format(val, ','), 44, WHITE, a); tag(f, (835, 1056), 'mean distance', a * 0.9, 28); f.key('readout', (660, 970, 1010, 1090))
    return f


# ============================================================================= dispatcher + output
def hud(f, t):
    b = beat_at(TO_V1(t)); f.text((24, 30), '%s  %5.2f s   ANIMATIC V1 retimed to V2 take - temporary art, not approved' % (b['id'], t), 21, (130, 138, 156), 'mono', 'lm', a=0.8)


def scene(t):
    """Frame at absolute time t (seconds on the master clock) before grade / captions."""
    if t < 26.46: return sc_open(t)
    if t < 31.06 + 1.31:
        f = sc_orbit(t)
        if t < 27.0: pr = sc_open(26.45); f2 = Frame(wipe_up(pr.im, f.im, seg(t, 26.46, 27.0))); f2.keys = f.keys; return f2
        return f
    if t < 33.15: return sc_orbit(t)
    if t < 33.6: a = sc_orbit(t); b = sc_surface(t); r = Frame(blend(a.im, b.im, ease(seg(t, 33.15, 33.6)))); r.keys = b.keys; return r
    if t < 43.6: return sc_surface(t)
    if t < 49.58: return sc_iris(t) if t < 44.4 else sc_optics(t)
    if t < 55.0: return sc_return(t)
    if t < 58.69: return sc_cones(t)
    if t < 61.65: return sc_photons(t)
    if t < 65.52: return sc_photons(t)
    if t < 68.56:
        f = sc_atmos(t)
        if t < 65.85: pr = sc_photons(65.0); f2 = Frame(blend(pr.im, f.im, ease(seg(t, 65.52, 65.85)))); f2.keys = f.keys; return f2
        return f
    if t < 75.29: return sc_hist2(t)
    if t < 86.31:
        f = sc_formula(t)
        if t < 76.2: pr = sc_hist2(75.2); f2 = Frame(wipe_up(pr.im, f.im, seg(t, 75.5, 76.2))); f2.keys = f.keys; return f2
        return f
    return sc_close(t)


# V2 retime (2026-11-26): this animatic was authored against the V1 take (92.53 s) with V1 times baked into the scene code.
# Instead of editing every literal, each output frame at V2 time t shows the V1 scene at the SAME SPOKEN MOMENT:
# tv = inverse of the word-edge warp (narration/v1_historical vs narration/WORD_TIMESTAMPS.json). Beat/caption data are read
# from v1_historical so scene and captions stay in one time domain; the audio is the V2 take.
def _warp():
    import numpy as np
    a = json.load(open(os.path.join(ROOT, 'narration', 'v1_historical', 'WORD_TIMESTAMPS.json')))['words']
    b = json.load(open(os.path.join(ROOT, 'narration', 'WORD_TIMESTAMPS.json')))['words']
    pts = sorted({(0.0, 0.0), (95.39, 92.53)} | {(y[k], x[k]) for x, y in zip(a, b) for k in ('start', 'end')})
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return lambda t: float(np.interp(t, xs, ys)) if t <= 95.39 else 92.53 + (t - 95.39)
TO_V1 = _warp()

def render(t, captions=True, with_hud=True):
    tv = TO_V1(t)
    f = scene(tv); keys = list(f.keys); im = LD.grade(f.im); out = Frame(im)
    if captions and tv < 92.53 + 0.5: draw_caption(out, tv)
    if with_hud: hud(out, t)
    img = out.im
    if t > FADE0: img = Image.blend(img, Image.new('RGB', img.size, (0, 0, 0)), clamp((t - FADE0) / (TOTAL - FADE0)))
    return img, keys


def frame_bytes(i):
    t = i / FPS; img, keys = render(t); small = img.resize((W // 2, H // 2), Image.LANCZOS)
    return i, small.tobytes(), audit_keys(keys)


def build_video(out=None, quick=None):
    out = out or os.path.join(ROOT, 'storyboard', 'animatic', 'ANIMATIC_V1_REFERENCE_INFORMED.mp4')
    n = int(round(TOTAL * FPS)); bad = []
    assert_caption_band()
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W // 2, H // 2), '-r', str(FPS), '-i', '-',
           '-i', os.path.join(ROOT, 'narration', 'raw_v2', 'SLOT07_NARRATION_V2_RAW.wav'), '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'medium',
           '-af', 'apad', '-c:a', 'aac', '-b:a', '192k', '-t', str(TOTAL), '-movflags', '+faststart', out]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(9) as pool:
        for k, (i, b, bd) in enumerate(pool.imap(frame_bytes, range(n), chunksize=6)):
            pr.stdin.write(b)
            if bd: bad.append((i / FPS, bd))
            if k % 240 == 0: print('frame', k, '/', n, flush=True)
    pr.stdin.close(); pr.wait(); print('wrote', out)
    json.dump(bad, open(os.path.join(ROOT, 'storyboard', 'animatic', 'ANIMATIC_V1_SAFE_AUDIT.json'), 'w'), indent=1)
    print('safe-band violations in', len(bad), 'frames')


def audit_all():
    widest = assert_caption_band(); bad = []
    for i in range(int(TOTAL * FPS)):
        t = i / FPS; f = scene(t); bd = audit_keys(f.keys)
        if bd: bad.append((round(t, 2), bd))
    print('caption chunks', len(CAPS), 'widest caption box', round(widest), 'px; frames with key-subject violations:', len(bad))
    for b in bad[:40]: print(b)
    return bad


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'still':
        img, keys = render(float(sys.argv[2]), captions=(len(sys.argv) < 5)); img.resize((W // 2, H // 2), Image.LANCZOS).save(sys.argv[3]); print(audit_keys(keys))
    elif cmd == 'video': build_video(os.path.join(ROOT, 'storyboard', 'animatic', 'ANIMATIC_V1_RETIMED_V2_TAKE.mp4'))   # V1 file kept as history
    elif cmd == 'audit': audit_all()
    elif cmd == 'camera':
        print('| Beats | Time | Move | Reason |\n|---|---|---|---|')
        for b, tt, m, r in CAMERA_NOTES: print('| %s | %s | %s | %s |' % (b, tt, m, r))
