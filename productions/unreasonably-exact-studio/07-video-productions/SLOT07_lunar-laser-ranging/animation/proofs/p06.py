"""P06 Astronaut sets the laser reflector down (astronaut-equipment interaction) on Codex layers.

Art: Codex B5P (interaction master: gloved hand on the reflector's carry handle) cut by Codex into B5PA (astronaut only,
hidden leg painted) and B5PR (reflector only, hidden handle/frame painted); Claude stacks, rigs and animates them.
Rig: the astronaut rotates about the planted boot; the reflector is carried by the handle, so its offset is solved every
frame from the GLOVE position (the grip can never slip). The glove is re-drawn over the bar (occlusion patch).
Action: carry low -> anticipation (a small lift) -> lower -> touch-down with a tiny settle -> ballistic dust (no air: clean
parabolas, no billowing) -> the glove lets go and the astronaut straightens. Shadows: hard, to the right (Sun upper left);
the reflector's shadow closes on its base as it lands (height cue).
"""
import math, os
import numpy as np
from PIL import Image
from uemotion import tokens as T, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.camera import T3, S3, R3

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, 'assets/rigs/astronaut_retro')
ASTRO = Image.open(os.path.join(D, 'interaction_astronaut_only.png')).convert('RGBA')
REFL = Image.open(os.path.join(D, 'interaction_reflector_arraycomp.png')).convert('RGBA')   # B5PR + 10x10 cube array composited by Claude (tools/composite_reflector_array.py)
PLATE = Image.open(os.path.join(ROOT, 'codex_handoff/runs/B3M/lunar_env_master.png')).convert('RGBA')
FOOT = np.array([140.0, 1420.0]); GLOVE = np.array([705.0, 900.0]); GLOVE_R = 72.0       # measured on B5PA/B5PR (Claude)
def _glove_patch():
    a = np.asarray(ASTRO).copy(); yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    a[..., 3] = (a[..., 3] * np.clip((GLOVE_R - np.hypot(xx - GLOVE[0], yy - GLOVE[1])) / 12, 0, 1)).astype(np.uint8)
    return Image.fromarray(a, 'RGBA')
GLOVE_IMG = _glove_patch()

N0 = NAR.start('B18'); DUR = 6.0
SC = 0.74; FOOT_W = (300.0, 1500.0)                       # layer px -> design units; planted boot in the world
LEAN = TL.Track([(0.0, -3.2, 'in_out_cubic'), (0.6, -3.2, 'in_out_cubic'), (0.95, -4.0, 'in_out_cubic'), (1.9, 0.0, 'out_quad'),   # deg, + = leans forward (clockwise)
                 (2.05, 0.25, 'in_out_cubic'), (2.3, 0.0, 'in_out_cubic'), (3.4, 0.0, 'in_out_cubic'), (4.3, -2.2, 'out_quad'), (DUR, -2.0)])
T_LAND, T_RELEASE = 1.9, 3.4
RELEASE = TL.Track([(0.0, 0.0, 'linear'), (T_RELEASE, 0.0, 'out_cubic'), (4.1, 1.0)])     # 0 = gripping, 1 = let go

def body_m(a):
    lean = math.radians(LEAN(a)); br = 1.0 + 0.004 * math.sin(2 * math.pi * a / 2.8) * smoothstep(seg(a, T_RELEASE, T_RELEASE + 0.6))   # breathing only once his hands are free (keeps the grip exact)
    return T3(*FOOT_W) @ R3(lean) @ S3(SC) @ np.array([[1, 0, 0], [0, br, 0], [0, 0, 1.0]]) @ T3(-FOOT[0], -FOOT[1])

def glove_world(a):
    v = body_m(a) @ np.array([GLOVE[0], GLOVE[1], 1.0]); return v[:2]

def refl_m(a):
    """reflector follows the glove until release; after release it stays where it landed."""
    rest = T3(*FOOT_W) @ S3(SC) @ T3(-FOOT[0], -FOOT[1])          # the master pose (lean 0) = reflector on the ground
    g0 = (rest @ np.array([GLOVE[0], GLOVE[1], 1.0]))[:2]
    ta = min(a, T_LAND)                                           # after touch-down the grip follows the body, the reflector does not
    off = glove_world(ta) - g0
    if a > T_LAND: off = off * 0                                  # landed exactly at the master pose (LEAN = 0 at T_LAND)
    return T3(*off) @ rest

def glove_offset(a):
    """after release the glove lifts off the bar along the forearm (up-left)."""
    r = RELEASE(a); return np.array([-10.0, -26.0]) * r

def dust(cv, a):
    """ballistic regolith from the two front feet at touch-down: parabolas under lunar g, no drag (no air), fade on landing."""
    t = a - T_LAND
    if t <= 0 or t > 1.6: return
    g = 900.0                                                     # design units / s^2 (1.62 m/s^2 at ~560 units per metre on this figure scale)
    rng = np.random.default_rng(4)
    rest = T3(*FOOT_W) @ S3(SC) @ T3(-FOOT[0], -FOOT[1])
    for fx in (300.0, 940.0):
        p0 = (rest @ np.array([fx, 1480.0, 1.0]))[:2]
        for _ in range(26):
            ang = rng.uniform(math.radians(15), math.radians(75)) * rng.choice([-1, 1]); v = rng.uniform(80, 230)
            vx, vy = v * math.sin(ang), -v * math.cos(ang); tt = t - rng.uniform(0, 0.08)
            if tt <= 0: continue
            y = p0[1] + vy * tt + 0.5 * g * tt * tt
            if y > p0[1] + 4: continue                            # back on the ground: gone (it does not hang in the air)
            cv.circle((p0[0] + vx * tt, y), rng.uniform(1.6, 3.2), fill=(150, 146, 140), alpha=0.85)

def scene(cv, ctx):
    a = ctx.a
    cv.clear(T.BG)
    with cv.xf(CAM6(a)): _scene(cv, a)
    return {}

def CAM6(a):
    """framing: tighter than the rig proof v1 (the plate's black sky filled the top third); a slow 4 % push toward the hands."""
    z = 1.22 + 0.05 * smoothstep(seg(a, 0.0, DUR)); c = (560.0, 1180.0)
    return T3(540, 1000) @ S3(z) @ T3(-c[0], -c[1])

def _scene(cv, a):
    with cv.xf(T3(-150 + 6 * a, -80) @ S3(1.4)): cv.blit_image(PLATE)
    # hard contact shadows to the right (Sun upper left); reflector shadow offset grows with its height above the ground
    h = float((refl_m(a) @ np.array([600, 1480, 1.0]))[1] - (T3(*FOOT_W) @ S3(SC) @ T3(-FOOT[0], -FOOT[1]) @ np.array([600, 1480, 1.0]))[1])
    cv.ellipse((FOOT_W[0] + 60, FOOT_W[1] - 2), 150, 16, fill=(14, 14, 16), alpha=0.55)
    rc = (T3(*FOOT_W) @ S3(SC) @ T3(-FOOT[0], -FOOT[1]) @ np.array([700, 1470, 1.0]))[:2]
    cv.ellipse((rc[0] + 70 - 0.6 * h, rc[1] + 4), 250, 26, fill=(12, 12, 14), alpha=0.5 * (1 - min(1, -h / 120)))
    with cv.xf(body_m(a)): cv.blit_image(ASTRO)
    with cv.xf(refl_m(a)): cv.blit_image(REFL)
    with cv.xf(body_m(a) @ T3(*glove_offset(a))): cv.blit_image(GLOVE_IMG)        # glove over the bar (occlusion patch)
    dust(cv, a)
    return {}

def check_all(out_dir, results):
    checks = []
    # grip: while gripping, the glove point and the bar point coincide (same world position)
    errs = []
    for a in np.linspace(0, T_LAND, 40):
        bar = (refl_m(a) @ np.array([GLOVE[0], GLOVE[1], 1.0]))[:2]; errs.append(float(np.hypot(*(bar - glove_world(a)))))
    checks.append(('grip holds while carrying: glove-to-bar error (design units)', max(errs) < 1.0, 'max %.3f' % max(errs)))
    rest = T3(*FOOT_W) @ S3(SC) @ T3(-FOOT[0], -FOOT[1])
    lift = float((rest @ np.array([600, 1480, 1.0]))[1] - (refl_m(0.0) @ np.array([600, 1480, 1.0]))[1])
    checks.append(('reflector starts lifted and lands exactly at the master pose', lift > 15 and np.allclose(refl_m(T_LAND + 0.01), rest), 'start height %.1f units' % lift))
    checks.append(('anticipation: a small lift before lowering', LEAN(0.95) < LEAN(0.6), 'lean %.1f -> %.1f deg' % (LEAN(0.6), LEAN(0.95))))
    checks.append(('release comes after touch-down (cause before effect)', T_RELEASE > T_LAND + 1.0, 'land %.1f s, release %.1f s' % (T_LAND, T_RELEASE)))
    # dust: under lunar g a particle launched at 230 u/s at 75 deg lands within ~0.5 s and never hangs
    tmax = 2 * 230 * math.cos(math.radians(15)) / 900
    checks.append(('dust is ballistic (no drag): longest flight time = 2 v cos / g', tmax < 0.6, '%.2f s' % tmax))
    # layer restack vs the Codex master (measured at the master pose)
    M = np.asarray(Image.open(os.path.join(D, 'astro_retro_interaction.png')))[..., 3] > 128
    S_ = (np.asarray(ASTRO)[..., 3] > 128) | (np.asarray(REFL)[..., 3] > 128)
    iou = (M & S_).sum() / (M | S_).sum()
    checks.append(('Codex layer cut re-stacks onto the B5P master (silhouette IoU >= 0.97, rule R12)', iou >= 0.97, 'IoU %.3f' % iou))
    return checks

INFO = dict(
    title='P06 Astronaut sets the reflector down (Codex B5P/B5PA/B5PR, Claude rig)',
    beats='B18 window (narration_t %.2f + 6.0 s); rig proof for the B17-B18 placement' % N0,
    expected=('The astronaut, holding the reflector by its handle, gives a small lift (anticipation), lowers it to the ground while leaning from the planted boot, '
              'it touches down with a tiny settle and two small fans of dust that fly in clean arcs and drop straight back; then the glove lets go and he straightens. '
              'His glove stays exactly on the bar until release; shadows are hard and fall right.'),
    science=('Apollo-style suit, anonymous. Reflector proportions follow the Apollo 11 LRRR master (Codex, AS11-40-5952 reference). Dust: ballistic under lunar '
             'gravity (1.62 m/s^2) with no air drag: parabolas, no billowing cloud. Pose = illustration; the real deployment involved levelling and aiming, shown here as a set-down.'),
)

def specs():
    return [ClipSpec('P06', 'P06_astronaut_sets_reflector', N0, DUR, scene, captions=False, audio=False, blur=(3, 0.5))]
