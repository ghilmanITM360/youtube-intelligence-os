"""P13 Narration-aligned sample, beats B16 end -> B21 (37.00-48.90 s): ghost mirror -> real reflector array on 'yes', set-down + ballistic dust on 'left',
push into one corner cube and cutaway on 'trick', rays enter / reflect / exit with the C06 footprint inset on 'tiny fraction', exit lines up with entry on 'from'.
Code-only: the astronaut and final reflector art are NOT in this clip (placeholder geometry only)."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, optics as O, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.camera import T3, S3, R3
from . import common as K
from . import p07

N0 = NAR.v1(37.00); DUR = NAR.v1(48.90) - N0
W = NAR.ws
N_YES = NAR.anchor('B17')                 # 'yes.' 37.90
N_LEFT = W(108)                           # 'left'  39.58 (beat map: astronaut sets the array on "left")
N_TRICK = NAR.anchor('B19')
N_PUSH0 = NAR.start('B19') - 0.75       # push starts in the pause after 'surface.' (was B19 start): 2.34 s instead of 1.59 s for the same 42x zoom, peak speed -33 % (strobe fix 2026-11-26)
N_REDIRECT, N_TINY, N_FRACTION = W(122), W(124), W(125)   # 44.91, 45.59, 45.96
N_LIGHT = NAR.anchor('B20')               # 'light' 46.92: key ray exits
N_BACK = W(129)                           # 'back' 46.98: A/B mirror inset
N_FROM = NAR.anchor('B21')                # 'from.' 48.31: exit lines up with entry

# ---------------------------------------------------------------- lunar surface geometry (placeholder art; one sun direction: shadows fall right)
CX, CY = 540.0, 1010.0                    # array centre (world)
PANEL = 460.0; PITCH = 41.0; FACE_R = 17.0; GROUND_Y = CY + PANEL / 2 + 28
HORIZON = 960.0

# ---------------------------------------------------------------- Codex artwork layers (CANDIDATES), composited by Claude
# Ground: codex_handoff/runs/B3M/lunar_env_master.png (1024x1536, horizon ~25 %), split into a far band (parallax 0.30) and the
# ground (0.75) with feathered masks; the black sky is keyed out so the star layer shows. Array face: assets/retro/
# retro_array_assembled_1254.png (Codex Batch 0b parts, 100 instances assembled by Claude) registered to the code grid by a
# least-squares fit of the 100 measured cube centres. At deep zoom the vector face fades in (illustration -> diagram), so
# the match to the cutaway stays sharp.
from PIL import Image as _Im
import json as _json, os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
def _load_plate():
    a = np.asarray(_Im.open(_os.path.join(_ROOT, 'codex_handoff/runs/B3M/lunar_env_master.png')).convert('RGB')).astype(np.float32)
    lum = a.mean(2); H_, W_ = lum.shape
    hz = np.array([int(np.argmax(lum[:, x] > 30)) for x in range(W_)])                 # first non-sky row per column
    hz_med = int(np.median(hz)); rows = np.arange(H_)[:, None]
    sky = np.clip((rows - hz[None, :] + 1) / 2.0, 0, 1)                                   # 2 px feather at the skyline
    far = sky * np.clip((hz_med + 150 - rows) / 60.0, 0, 1)                               # far band fades out 90-150 px below the horizon
    ground = np.broadcast_to(np.clip((rows - (hz_med + 60)) / 60.0, 0, 1), (H_, W_))                               # ground band starts under the far band (overlap)
    mk = lambda m: _Im.fromarray(np.dstack([a, m[..., None] * 255]).astype(np.uint8), 'RGBA')
    return mk(far), mk(ground), hz_med
PLATE_FAR, PLATE_GROUND, PLATE_HZ = _load_plate()
PLATE_S = 1.6; PLATE_X0 = -340.0; PLATE_Y0 = HORIZON - PLATE_HZ * PLATE_S            # horizon row lands on HORIZON

def _fit_array():
    d = _json.load(open(_os.path.join(_ROOT, 'assets/retro/retro_array_instances.json')))
    src = np.array([(q['x'], q['y'] * d['y_scale_applied']) for q in d['instances']]); dst = np.array([(CX + (q['col'] - 5.5) * PITCH, CY + (q['row'] - 5.5) * PITCH) for q in d['instances']])
    (sx, tx), rx = np.linalg.lstsq(np.c_[src[:, 0], np.ones(100)], dst[:, 0], rcond=None)[:2]
    (sy, ty), ry = np.linalg.lstsq(np.c_[src[:, 1], np.ones(100)], dst[:, 1], rcond=None)[:2]
    res = np.hypot(src[:, 0] * sx + tx - dst[:, 0], src[:, 1] * sy + ty - dst[:, 1])
    return (sx, sy, tx, ty), float(res.max()), d['disc_px'] / 2 * (sx + sy) / 2
ARR_FIT, ARR_RES, ARR_FACE_R = _fit_array()
ARR_IMG = _Im.open(_os.path.join(_ROOT, 'assets/retro/retro_array_assembled_1254.png')).convert('RGBA')

def draw_plate(img, cv):
    with cv.xf(T3(PLATE_X0, PLATE_Y0) @ S3(PLATE_S)): cv.blit_image(img)

TARGET_CUBE = (5, 4)
TARGET = (CX + (TARGET_CUBE[0] - 4.5) * PITCH, CY + (TARGET_CUBE[1] - 4.5) * PITCH)
CUBE13, START13, RAYS13 = p07.build(apex_y=480, y0=1370)       # same geometry as P07, lifted so the ray origins sit above the caption band
TICK13 = [1010, 1100, 1190]
SPEED13 = p07.SPEED
def ray_len13(i): return O.polyline_len(RAYS13[i]['points'])
APERTURE_Y = float(CUBE13.left[1]); APERTURE_HALF = float((CUBE13.right[0] - CUBE13.left[0]) / 2)
FACE_R = ARR_FACE_R                       # measured from the Codex face art (was 17.0 for the vector placeholder)
Z_END = APERTURE_HALF / FACE_R            # the face circle fills the aperture of the cutaway: registration for the match dissolve
Z_FAR = 0.62
class LogTrack:
    def __init__(self, keys): self.t = TL.Track([(t, math.log(v), e) for t, v, e in keys])
    def __call__(self, t): return math.exp(self.t(t))

ZOOM_A = LogTrack([(NAR.v1(37.0), 1.0, 'in_out_cubic'), (NAR.v1(38.65), 1.06, 'in_out_cubic'), (NAR.v1(41.6), Z_FAR, 'linear'), (N_PUSH0, Z_FAR, 'linear')])
POS_A = TL.Track([(NAR.v1(37.0), (540, 1000), 'in_out_cubic'), (NAR.v1(38.65), (540, 1000), 'in_out_cubic'), (NAR.v1(41.6), (452, 1040), 'linear'), (N_PUSH0, (452, 1040))])
def _screen_of_target(z, cam): return (540 + z * (TARGET[0] - cam[0]), 960 + z * (TARGET[1] - cam[1]))
_S0 = _screen_of_target(Z_FAR, (452, 1040))
def _push_u(t): return smoothstep(seg(t, N_PUSH0, N_TRICK))      # peak slope 1.5 (in_out_cubic was 3): strobe fix 2026-11-26
def cam_zoom(t):
    return math.exp(lerp(math.log(Z_FAR), math.log(Z_END), _push_u(t))) if t >= N_PUSH0 else ZOOM_A(t)
def cam_pos(t):
    if t < N_PUSH0: return POS_A(t)
    z = cam_zoom(t); s = (lerp(_S0[0], 540, _push_u(t)), lerp(_S0[1], APERTURE_Y, _push_u(t)))
    return (TARGET[0] - (s[0] - 540) / z, TARGET[1] - (s[1] - 960) / z)       # keeps the target cube gliding straight onto the aperture centre
CAM = C2.Camera2D(pos=type('P', (), {'__call__': staticmethod(cam_pos)})(), zoom=type('Z', (), {'__call__': staticmethod(cam_zoom)})())

# ---------------------------------------------------------------- art (placeholder geometry, no text)
def _noise(x, seed): return math.sin(x * 1.7 + seed) * 0.5 + math.sin(x * 3.1 + seed * 2.3) * 0.3 + math.sin(x * 7.3 + seed * 0.7) * 0.2
RIDGE_PTS = [(x, HORIZON - 14 - 30 * (0.5 + 0.5 * _noise(x * 0.004, 1.0)) - 12 * _noise(x * 0.013, 2.0)) for x in range(-1500, 2641, 30)]
_r = np.random.default_rng(13)
STONES = [(float(x), float(y), float(2.0 + (y - HORIZON) / 160 * _r.uniform(0.5, 1.4))) for x, y in zip(_r.uniform(-1400, 2500, 260), HORIZON + 20 + (_r.random(260) ** 1.6) * 1500)]

EXT_FAR = (-1700, -700, 2800, 2600)
EXT_GROUND = (-1600, None, 2700, 3200)

def draw_ridge(cv, ctx):
    draw_plate(PLATE_FAR, cv); return
    pts = RIDGE_PTS + [(2640, HORIZON + 40), (-1500, HORIZON + 40)]
    cv.polygon(pts, fill=(40, 40, 47)); cv.polyline(RIDGE_PTS, (104, 104, 114), 3, alpha=0.9)

def draw_ground(cv, ctx):
    draw_plate(PLATE_GROUND, cv); return
    cv.polygon([(-1600, HORIZON), (2700, HORIZON), (2700, 3200), (-1600, 3200)], fill=(88, 87, 86))
    for k in range(10):                                             # tonal fall-off toward the viewer (hard sun: horizon band brightest)
        y0 = HORIZON + k * 24; cv.polygon([(-1600, y0), (2700, y0), (2700, y0 + 24), (-1600, y0 + 24)], fill=T.mix((126, 124, 120), (88, 87, 86), k / 9), alpha=0.9)
    for (x, y, r) in STONES:
        cv.ellipse((x, y), r * 1.6, r, fill=(60, 59, 58)); cv.ellipse((x - r * 0.25, y - r * 0.2), r * 1.0, r * 0.6, fill=(132, 130, 126), alpha=0.8)

LEAN_WIDE = math.sin(math.radians(23.0)) * 1.0 + 0.03     # wide shot: face foreshortened as a panel lying ~23 deg off the ground (seen from a low eye height)
def draw_array(cv, c=(CX, CY), alpha=1.0, tilt=0.0, vector_alpha=0.0, lean=1.0):
    """lean = vertical foreshortening about the base (1 = face seen straight on, as from Earth; LEAN_WIDE = lying back toward the sky).
    Vector strokes need similarity transforms, so a leaning panel is drawn face-on into an offscreen layer (1 px = 1 design unit,
    sharp enough below zoom ~2.5 where lean < 1) and that bitmap is warped; at lean == 1 it draws directly (registration path)."""
    x, y = c; h = PANEL / 2; yb = y + h + 28
    if lean < 0.999:
        from uemotion.canvas import Canvas as _C
        # V2 root-cause fix for the pixel stair-steps seen at 45.2 s in V1: the offscreen layer was 1 px per design unit and the push
        # magnified it ~40x. Its resolution now follows the on-screen magnification (capped at 4x for memory/time).
        rs = min(4.0, max(1.0, cv.k * cv.px))
        OX, OY = x - h - 40, y - h - 40; off = _C(scale=rs, ss=1, W=int(2 * h + 120), H=int(2 * h + 120))
        with off.xf(T3(-OX, -OY)): _draw_array_flat(off, c, 1.0, 0.0, vector_alpha)
        with cv.xf(T3(x, yb) @ R3(tilt) @ np.array([[1, 0, 0], [0, lean, 0], [0, 0, 1.0]]) @ T3(-x, -yb) @ T3(OX, OY) @ S3(1 / rs)):
            cv.blit_image(off.im, alpha=alpha)
        return
    _draw_array_flat(cv, c, alpha, tilt, vector_alpha)

def _draw_array_flat(cv, c, alpha, tilt, vector_alpha):
    x, y = c; h = PANEL / 2
    with cv.xf(T3(x, y + h + 28) @ R3(tilt) @ T3(-x, -(y + h + 28))), cv.group(alpha):
        cv.polygon([(x - h, y + h + 28), (x + h, y + h + 28), (x + h - 40, y + h + 4), (x - h + 40, y + h + 4)], fill=(188, 188, 194))        # bright base plate
        cv.rect((x - h, y - h, x + h, y + h), fill=(104, 107, 116), outline=(176, 181, 194), width=4, radius=10)                                 # aluminium frame
        cv.polygon([(x + h, y - h + 8), (x + h + 24, y - h + 24), (x + h + 24, y + h + 4), (x + h, y + h)], fill=(76, 78, 86))                   # shaded side (sun is on the left)
        sx, sy, tx, ty = ARR_FIT
        with cv.xf(T3(tx, ty) @ np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1.0]])): cv.blit_image(ARR_IMG)                                         # Codex face art, registered
        vec = vector_alpha
        if vec <= 0: return
        for i in range(10):
            for j in range(10):
                fx, fy = x + (i - 4.5) * PITCH, y + (j - 4.5) * PITCH
                cv.circle((fx, fy), FACE_R + 3, fill=(72, 75, 86), alpha=vec); cv.circle((fx, fy), FACE_R, fill=(20, 28, 42), alpha=vec)
                for a in (-90, 30, 150):                                                                                                         # three facets seen end-on
                    t = math.radians(a); cv.line((fx, fy), (fx + FACE_R * 0.92 * math.cos(t), fy + FACE_R * 0.92 * math.sin(t)), (58, 78, 108), 1.6, alpha=vec)
                cv.arc((fx, fy), FACE_R * 0.7, math.radians(200), math.radians(260), (190, 205, 225), 2.0, alpha=0.5 * vec)                           # sky glint, upper left

def draw_shadow(cv, c=(CX, CY), alpha=1.0, sharp=1.0):
    x, y = c; h = PANEL / 2; yb = y + h + 28
    cv.polygon([(x - h + 20, yb), (x + h - 20, yb), (x + h + 250, yb + 62), (x - h + 270, yb + 62)], fill=(14, 14, 18), alpha=0.55 * alpha)
    cv.ellipse((x + 10, yb + 6), h + 30, 12, fill=(10, 10, 14), alpha=0.5 * alpha * sharp)                                                     # contact shadow

def draw_ghost_mirror(cv, c=(CX, CY), alpha=1.0, t=0.0):
    """V3: the imagined mirror is an everyday stand mirror (K.draw_toy_mirror), not a dashed box. It floats a few units (it is an idea)."""
    x, y = c; bob = 6 * math.sin(t * 2.2)
    K.draw_toy_mirror(cv, (x, y - 40 + bob), s=1.0, alpha=alpha * 0.95, t=t)

def qmark_dots(cv, c, alpha=1.0, drop=0.0):
    """question mark made of dots (as at B03); drop 0..1 lets the dots fall away"""
    pts = [(c[0] + 38 * math.cos(math.radians(a)), c[1] - 40 + 38 * math.sin(math.radians(a))) for a in range(190, 360 + 50, 22)]
    pts += [(c[0] + 6 - 6 * (k / 3), c[1] - 6 + 20 * k) for k in range(0, 3)] + [(c[0], c[1] + 66)]
    for i, (px, py) in enumerate(pts):
        d = drop * (60 + 40 * ((i * 7) % 5)) * drop
        cv.circle((px, py + d), 7, fill=T.WHITE, alpha=alpha * (1 - drop))

# dust: ballistic particles, gravity scaled for a low-g look (Earth-like would be ~6x larger); no air: no billowing, straight x, parabolic y
G_DUST = 175.0
_dr = np.random.default_rng(39)
DUST = [dict(x0=CX + float(_dr.uniform(-190, 190)), vx=float(_dr.uniform(-70, 70)), vy=-float(_dr.uniform(70, 150)), r=float(_dr.uniform(2.5, 5.5)), land=float(_dr.uniform(10, 46))) for _ in range(16)]
def dust_state(p, t):
    """position at time t after launch (pure function); lands on the ground and stays"""
    tau = max(0.0, t); y0 = GROUND_Y - 4
    t_land = (-p['vy'] + math.sqrt(p['vy'] ** 2 + 2 * G_DUST * p['land'])) / G_DUST
    tt = min(tau, t_land); return p['x0'] + p['vx'] * tt, y0 + p['vy'] * tt + 0.5 * G_DUST * tt * tt, tau >= t_land
def draw_dust(cv, t_since):
    if t_since <= 0: return
    for p in DUST:
        x, y, landed = dust_state(p, t_since); cv.circle((x, y), p['r'], fill=(168, 164, 158), alpha=0.9 if not landed else 0.55)

# ---------------------------------------------------------------- scenes
LUNAR = C2.Layer2_5D([C2.Layer('stars', C2.starfield(EXT_FAR, seed=17, density=6e-4), 0.08, 0, EXT_FAR),
                      C2.Layer('ridge', draw_ridge, 0.30, 1, (-1500, None, 2640, None)),
                      C2.Layer('ground', draw_ground, 0.75, 2, EXT_GROUND),
                      C2.Layer('array', None, 1.0, 3)], CAM)

def array_layer(cv, ctx):
    n = ctx.n
    real = smoothstep(seg(n, N_YES, N_YES + 0.28)); ghost = 1 - smoothstep(seg(n, N_YES - 0.02, N_YES + 0.28))
    pop = ease_out_back(seg(n, N_YES, N_YES + 0.4), 1.6)
    tilt = 0.028 * (1 - spring(seg(n, N_LEFT, N_LEFT + 0.9), 0.30, 3.0)) if n >= N_LEFT else 0.0
    squash = 1 - 0.02 * math.sin(math.pi * seg(n, N_LEFT, N_LEFT + 0.25)) if N_LEFT <= n < N_LEFT + 0.25 else 1.0   # tiny uniform 'thud' compress about the base
    draw_shadow(cv, alpha=real)
    if ghost > 0:
        draw_ghost_mirror(cv, alpha=ghost, t=n); qmark_dots(cv, (CX, CY - PANEL / 2 - 110), alpha=ghost, drop=smoothstep(seg(n, N_YES, N_YES + 0.35)))
    if real > 0:
        bx, by = CX, GROUND_Y
        with cv.xf(T3(bx, by) @ S3(lerp(0.94, 1.0, pop) * squash) @ T3(-bx, -by)):
            draw_array(cv, alpha=real, tilt=tilt, vector_alpha=smoothstep(seg(cam_zoom(n), 4.0, 8.0)),
                       lean=lerp(LEAN_WIDE, 1.0, _push_u(n)))      # camera rises to look down the face: Earth's view
        S.ring_ping(cv, (CX, CY), seg(n, N_YES, N_YES + 0.7), T.WHITE, 262, 440, 3, alpha=0.5)          # thin non-flash ring: 'real equipment'
    draw_dust(cv, n - N_LEFT)

def lunar_scene(cv, ctx):
    LUNAR.layers[3].draw = array_layer; LUNAR.render(cv, ctx, t=ctx.n)

def neutral_bg(cv): p07.neutral_bg(cv)

def footprint_pop(n): return ease_out_back(seg(n, N_TINY - 0.05, N_TINY + 0.30), 1.5)
def cutaway_scene(cv, ctx):
    n = ctx.n; neutral_bg(cv)
    cube = CUBE13; a = smoothstep(seg(n, N_TRICK - 0.1, N_TRICK + 0.25))
    O.draw_cube(cv, cube, alpha=a)                                    # the housing becomes a cutaway (dissolved in centred on 'trick.')
    S.badge(cv, (60, K.BADGE_Y), 'CONCEPTUAL', 30, T.GREY, alpha=a)
    KEY = 1
    T0 = [0.0] * 3; L = [ray_len13(i) for i in range(3)]
    T0[KEY] = N_LIGHT - L[KEY] / SPEED13; T0[0] = T0[KEY] - 0.55; T0[2] = T0[KEY] + 0.55
    fin = smoothstep(seg(n, N_FROM - 0.35, N_FROM))                    # 'from.': the KEY pair is lit alone, the others step back (one clear focal action)
    for i, (sx, sy, ang) in enumerate(START13):
        pts = RAYS13[i]['points']; sl = p07._seglens(pts)
        cv.circle((sx, sy), 14, outline=T.GREY, width=3, alpha=a * 0.7)
        S.ring_ping(cv, (sx, sy), seg(n, T0[i] - 0.28, T0[i] + 0.25), T.WARM, 12, 60, 4)
        prog = seg(n, T0[i], T0[i] + L[i] / SPEED13)
        if prog <= 0: continue
        trav = prog * L[i]; done = prog >= 1.0
        nxt = T0[i + 1] if i + 1 < 3 else N_LIGHT + 0.5
        ak = lerp(1.0, 0.35, smoothstep(seg(n, nxt - 0.1, nxt + 0.4)))
        ak = lerp(ak, 1.0 if i == KEY else 0.30, fin)
        head, hd = O.draw_ray(cv, pts, prog, alpha=ak, width=8)
        if not done: S.pulse_bead(cv, head, hd, T.WARM if trav < sl[0] + sl[1] else T.COOL, 0.8)
        for hp, dh in ((pts[1], sl[0]), (pts[2], sl[0] + sl[1])): O.hit_spark(cv, hp, seg(trav, dh, dh + 160))
        if trav > sl[0] * 0.5: S.arrowhead(cv, tuple(np.array(pts[0]) + (np.array(pts[1]) - np.array(pts[0])) * 0.45), RAYS13[i]['d_in'], T.WARM, 24, alpha=ak)
        if trav > sl[0] + sl[1] + sl[2] * 0.55: S.arrowhead(cv, tuple(np.array(pts[2]) + (np.array(pts[3]) - np.array(pts[2])) * 0.55), RAYS13[i]['d_out'], T.COOL, 24, alpha=ak)
    # insets: third face (cutaway start) -> fades as the A/B mirror inset arrives; footprint inset on 'tiny fraction' (C06 picture rule, no numbers)
    third = smoothstep(seg(n, N_TRICK + 0.3, N_TRICK + 0.7)) * (1 - smoothstep(seg(n, N_BACK - 0.05, N_BACK + 0.2)))
    if third > 0: O.third_face_inset(cv, (880, 330), 92, alpha=third * (0.55 if n > N_REDIRECT else 1.0))
    fp = footprint_pop(n); fpa = (1 - smoothstep(seg(n, N_LIGHT + 0.0, N_LIGHT + 0.3)))
    if fp > 0 and fpa > 0:
        c = (200, 340); sc = max(0.01, fp)
        with cv.xf(T3(*c) @ S3(sc) @ T3(-c[0], -c[1])): O.footprint_inset(cv, c, 105, alpha=min(1.0, fp) * fpa)
    mir = smoothstep(seg(n, N_BACK, N_BACK + 0.3))
    if mir > 0: mirror_inset(cv, (880, 330), 120, alpha=mir * 0.9)
    for i in range(3):                                                 # guide ticks land on 'from.' (key pair strong, the others faint)
        ta = fin * (0.9 if i == KEY else 0.3)
        if ta > 0: O.guide_ticks(cv, RAYS13[i]['points'][:2], RAYS13[i]['points'][2:], TICK13[i], alpha=ta)
    pulse = math.sin(math.pi * seg(n, N_FROM, N_FROM + 0.7))
    if pulse > 0:
        pts = RAYS13[KEY]['points']
        cv.polyline([tuple(p) for p in pts[:2]], T.WARM, 8 + 6 * pulse, alpha=0.35 * pulse); cv.polyline([tuple(p) for p in pts[2:]], T.COOL, 8 + 6 * pulse, alpha=0.35 * pulse)

def mirror_inset(cv, c, r, alpha=1.0):
    """B21 A/B contrast in a small round inset: a ghosted flat mirror sends the ray AWAY (not back). No text."""
    k = r / 105.0
    cv.circle(c, r, fill=(14, 20, 40), outline=T.GREY, width=4, alpha=alpha)
    m = O.flat_mirror_ray((c[0] - 50 * k, c[1] + 62 * k), 26.0, c[1] - 8 * k, end_y=c[1] + 62 * k)
    cv.polyline([(c[0] - 72 * k, c[1] - 8 * k), (c[0] + 72 * k, c[1] - 8 * k)], T.GLASS, 6, alpha=alpha * 0.75, dash=(12, 9))
    pts = [tuple(p) for p in m['points']]; cv.polyline(pts[:2], T.WARM, 6, alpha=alpha); cv.polyline(pts[1:], T.COOL, 6, alpha=alpha * 0.8, dash=(10, 8))
    e = pts[-1]; cv.line((e[0] - 10, e[1] - 20), (e[0] + 10, e[1] - 0), T.ALERT, 6, alpha=alpha); cv.line((e[0] - 10, e[1] - 0), (e[0] + 10, e[1] - 20), T.ALERT, 6, alpha=alpha)

def scene(cv, ctx):
    n = ctx.n; cv.clear(T.BG)
    x = smoothstep(seg(n, N_TRICK - 0.45, N_TRICK + 0.17))           # V2: dissolve starts earlier (was -0.18): the crisp cutaway takes over before the photo is magnified past its native resolution (pixel stair-steps seen at 45.2 s in V1); still completes on 'trick.'
    if x < 1:
        with cv.group(1 - x): lunar_scene(cv, ctx)
    if x > 0:
        with cv.group(x): cutaway_scene(cv, ctx)
    # push 'rack focus' (strobe fix 2026-11-26): during the fast part of the push the lens softens in proportion to the zoom speed,
    # removing the fine cube-grid frequencies that alias (wagon-wheel) when the grid moves ~a cell per frame. Captions are drawn later, sharp.
    if N_PUSH0 < n < N_TRICK:
        v = (math.log(cam_zoom(n + 0.02)) - math.log(cam_zoom(n - 0.02))) / 0.04          # d ln(zoom)/dt
        rad = 2.4 * clamp(v / 2.4) * cv.px * (1 - x)                # V2: 3.2 -> 2.4 (V1 read as over-soft at 44.8 s)
        if rad > 0.3:
            from PIL import ImageFilter
            cv.im = cv.im.filter(ImageFilter.GaussianBlur(rad))


# ---------------------------------------------------------------- checks
def check_all(out_dir, results):
    from uemotion.canvas import Canvas
    checks = []
    ev = {'yes (real array replaces ghost)': (N_YES, NAR.anchor('B17')), 'left (set-down + dust)': (N_LEFT, NAR.ws(108)), 'trick. (dissolve centre)': (N_TRICK, NAR.anchor('B19')),
          'light (key ray exits)': (N_LIGHT, NAR.anchor('B20')), 'from. (exit lines up with entry)': (N_FROM, NAR.anchor('B21'))}
    for k, (a, b) in ev.items(): assert abs(a - b) < 1e-9
    checks.append(('event times are the beat-map anchor / word times', True, '; '.join('%s %.2f' % (k.split(' ')[0], v[0]) for k, v in ev.items())))
    # antiparallel (same geometry as P07, re-asserted here for the shown rays)
    for i in range(3): assert abs(np.dot(RAYS13[i]['d_in'], RAYS13[i]['d_out']) + 1) < 1e-12
    checks.append(('ASSERT exit rays antiparallel to entry rays for the three rays shown', True, 'dots %s' % [round(float(np.dot(RAYS13[i]['d_in'], RAYS13[i]['d_out'])), 12) for i in range(3)]))
    # key ray exit completes on 'light'
    L = ray_len13(1); t0 = N_LIGHT - L / SPEED13
    checks.append(('key ray reaches its exit end exactly on "light" (%.2f s)' % N_LIGHT, abs((t0 + L / SPEED13) - N_LIGHT) < 1e-9 and t0 - 0.55 > N_REDIRECT - 0.5, 'enters %.2f, exits %.2f; first ray enters %.2f (word "redirect" %.2f)' % (t0, N_LIGHT, t0 - 0.55, N_REDIRECT)))
    # match cut registration: target cube centre/radius at the dissolve = cutaway aperture
    zc = cam_zoom(N_TRICK); st = C2.CamState(*cam_pos(N_TRICK), zc, 0.0); sp = C2.Camera2D.project(st, TARGET, 1.0)
    rad = zc * FACE_R
    checks.append(('match dissolve registration: cube face centre -> cutaway aperture centre (px error)', math.hypot(sp[0] - 540, sp[1] - APERTURE_Y) < 0.5 and abs(rad - APERTURE_HALF) < 1.0,
                   'face centre (%.2f, %.2f) vs aperture (540, %.1f); face radius %.1f vs aperture half-width %.1f design units' % (sp[0], sp[1], APERTURE_Y, rad, APERTURE_HALF)))
    # parallax: displacement ratio per layer equals its parallax factor
    s0 = C2.CamState(500, 1000, 1.0, 0.0); s1 = C2.CamState(560, 1000, 1.0, 0.0); rat = {}
    for l in LUNAR.layers:
        a0 = C2.Camera2D.project(s0, (700, 1000), l.parallax); a1 = C2.Camera2D.project(s1, (700, 1000), l.parallax); rat[l.name] = round((a0[0] - a1[0]) / 60.0, 4)
    checks.append(('parallax: apparent shift / camera shift equals each layer factor (stars .08, ridge .30, ground .75, array 1.0)', all(abs(rat[l.name] - l.parallax) < 1e-9 for l in LUNAR.layers), str(rat)))
    rep = LUNAR.assert_overscan(N0, N0 + (N_TRICK - N0)); checks.append(('overscan: every layer covers the camera path (assert, B16-B19 push)', True, 'min margin per layer %s' % {k: round(v) for k, v in rep.items() if v != math.inf}))
    # dust is ballistic: constant vx, apex height = vy^2/2g, no horizontal acceleration
    p = DUST[0]; xs = [dust_state(p, t)[0] for t in np.linspace(0, 0.8, 9)]; ddx = np.diff(np.diff(xs)); t_apex = -p['vy'] / G_DUST
    y_ap = dust_state(p, t_apex)[1]; exp_ap = GROUND_Y - 4 - p['vy'] ** 2 / (2 * G_DUST)
    checks.append(('dust follows parabolic arcs (a_x = 0, apex = v^2/2g), no billowing', np.abs(ddx).max() < 1e-9 and abs(y_ap - exp_ap) < 1e-6, 'apex %.3f vs %.3f ; max a_x %.2e ; g = %.0f units/s^2' % (y_ap, exp_ap, np.abs(ddx).max(), G_DUST)))
    # pixel tests around 'yes': ghost dashes before, real array after
    def frame(nv):
        cv = Canvas(0.5, 1, bg=T.BG); scene(cv, TL.ClockSet(N0).at(nv - N0)); return np.asarray(cv.im.convert('RGB'), np.float32)
    f_b, f_a = frame(N_YES - 0.10), frame(N_YES + 0.45)
    # faces = blue glass of the Codex face art (b clearly above r), counted only inside the array's screen box (the lunar plate has dark craters)
    def dark_face(f):
        sp = C2.Camera2D.project(CAM.state(N_YES), (CX, CY), 1.0); x0, y0 = int((sp[0] - PANEL / 2) * 0.5), int((sp[1] - PANEL / 2) * 0.5)
        b = f[max(0, y0):y0 + int(PANEL * 0.5), max(0, x0):x0 + int(PANEL * 0.5)]
        return int(((b[..., 2] - b[..., 0] > 18) & (b[..., 2] > 60)).sum())
    ghostpx = lambda f: int(((f[..., 2] > 200) & (f[..., 1] > 190) & (f[..., 0] < 190)).sum())
    checks.append(('before "yes": ghost mirror visible, no array faces; after: array faces present, ghost gone', ghostpx(f_b) > 150 and dark_face(f_a) > 2000 and dark_face(f_a) > 4 * dark_face(f_b) and ghostpx(f_a) < 0.3 * ghostpx(f_b),   # before: only the bluish ghost dashes
                   'ghost px %d -> %d ; face px %d -> %d' % (ghostpx(f_b), ghostpx(f_a), dark_face(f_b), dark_face(f_a))))
    return checks

INFO = dict(
    title='P13 Narration-aligned sample, B17-B21 (code part)',
    beats='narration_t 37.00-48.90 (B16 tail, B17-B21). yes 37.90, left 39.58, trick. 43.96, redirect 44.91, tiny fraction 45.59-46.2, light 46.92, back 46.98, from. 48.31',
    expected=("Ghost mirror + dot-built question mark (B16 end state) -> on 'yes' the ghost dissolves and the real reflector array (10 x 10 dark-glass faces, aluminium frame, bright base; placeholder geometry) "
              "pops into the SAME place with a thin ring. Camera (Camera2D, log zoom) pulls back with 4-layer parallax (stars .08, ridge .30, ground .75, array 1.0); on 'left' the array settles with a damped tilt and ballistic dust arcs "
              "(low-g look, no billowing). A push-in glides one cube face onto the screen centre and dissolves, centred on 'trick.', into the neutral cutaway whose aperture circle it matches. Rays enter staggered from 'redirect', "
              "the key ray exits on 'light'; on 'tiny fraction' a magnified inset shows the wide beam footprint with the array as a tiny marker (no numbers; main-frame rays keep returning in full); on 'back' the third-face inset gives way to a small "
              "flat-mirror A/B inset (ray sent away); on 'from.' guide ticks land and all three exit rays line up with their entry rays together."),
    science=("Optics as in P07 (exact two-reflection geometry, antiparallel asserted; exit offset, not collinear). C06 picture rule is implemented: footprint inset on 'tiny fraction', no numbers, array a tiny marker, "
             "and the main frame's ray returns in full with no absorption; the inset fades before the A/B mirror inset so reflect-to-source and tiny-fraction never share visual weight (rule 7). "
             "Array: 10 x 10 faces per C05 (Apollo 11/14: 100 cubes, 46 cm panel); film shows one array (Apollo 11). No astronaut is drawn or named (C05 naming still open). Dust gravity is a stylised low-g value, not a physical simulation. "
             "ALL ART IN THE LUNAR SCENE IS PLACEHOLDER GEOMETRY, not Codex's final reflector/astronaut art."),
    open_issues=["B18 astronaut kneel-and-set sequence is NOT in this clip (needs rigged art). The 'left' event is represented by array settle + dust only.",
                 "Lunar scene art is procedural placeholder; final art comes from Codex assets."],
)

def specs():
    return [ClipSpec('P13', 'P13_B17-B21_narration_aligned', N0, DUR, scene, captions=True, blur=(7, 0.9),
                     cues={'yes_real_array': N_YES, 'left_settle_dust': N_LEFT, 'push_mid': (N_PUSH0 + N_TRICK) / 2, 'trick_cutaway': N_TRICK, 'redirect_ray1': N_REDIRECT,
                           'tiny_fraction_inset': N_FRACTION, 'light_key_ray_exits': N_LIGHT, 'back_mirror_inset': N_BACK + 0.35, 'from_aligned': N_FROM + 0.25})]
