"""P05 Apollo astronaut movement (RIG_003_ASTRONAUT_POSE, arm rig v1) on Codex artwork.

Layers: Codex run B5L (torso without arms + near arm + far arm, each with painted overlap past the shoulder), master B5M.
Pivots and draw order: assets/rigs/astronaut/RIG_003_astronaut_arms.json. Background: Codex run B3M lunar plate.
Action (a reach-down gesture, the motion of setting something on the ground): settle -> anticipation (near arm back,
body rises a touch) -> reach (arm forward/down, body leans from the boots) -> overshoot and settle -> recover. The far arm
follows 0.12 s later with half the amplitude (overlapping action); a slow breathing scale keeps the hold alive.
Rig v2: shoulder skinning (weight 0 at the joint -> 1 down the upper arm) replaces the rigid swing + cap of v1, which left a 473 px gap; still no elbow; a deeper kneel is a whole-pose replacement.
"""
import json, math, os
import numpy as np
from PIL import Image
from uemotion import tokens as T, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.canvas import Canvas
from uemotion.camera import T3, S3, R3

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RIG = json.load(open(os.path.join(ROOT, 'assets/rigs/astronaut/RIG_003_astronaut_arms.json')))
IMG = {k: Image.open(os.path.join(ROOT, 'assets/rigs/astronaut', v['file'])).convert('RGBA') for k, v in RIG['layers'].items()}
PLATE = Image.open(os.path.join(ROOT, 'codex_handoff/runs/B3M/lunar_env_master.png')).convert('RGBA')
N0 = NAR.start('B18'); DUR = 5.0
SC = 0.86; FEET_WORLD = (430.0, 1520.0)            # where the boots stand (design units); figure scale (layer px -> units)
PN, PF = RIG['layers']['arm_near']['pivot_shoulder'], RIG['layers']['arm_far']['pivot_shoulder']; PFEET = RIG['layers']['torso']['pivot_feet']
CAP_R = 64.0
def _cap():
    """shoulder cap = the torso's own painted shoulder inside a feathered disc at the near pivot, drawn OVER the near arm so the
    arm's overlap sleeve tucks under it when it rotates (compositing mask by Claude; Codex pixels unchanged)."""
    t = np.asarray(IMG['torso']).copy(); yy, xx = np.mgrid[0:t.shape[0], 0:t.shape[1]]
    m = np.clip((CAP_R - np.hypot(xx - PN[0], yy - PN[1])) / 14.0, 0, 1)
    t[..., 3] = (t[..., 3] * m).astype(np.uint8); return Image.fromarray(t, 'RGBA')
CAP = _cap()

# Shoulder skinning (rig v2, 2026-11-26): instead of swinging the arm as a rigid piece about one pivot (which opened a 473 px gap),
# each arm pixel rotates by ang * w, with w = 0 inside the shoulder (the sleeve stays attached to the torso) rising smoothly to 1
# down the upper arm: the sleeve bends like fabric (mesh-style deformation in code; Codex pixels unchanged).
import cv2
_YY, _XX = np.mgrid[0:1536, 0:1024].astype(np.float32)
SKIN = {'arm_near': ((372.0, 405.0), 55.0, 215.0), 'arm_far': ((630.0, 420.0), 45.0, 190.0)}   # joint centre, r0 (w=0), r1 (w=1)
def _w(k):
    (cx, cy), r0, r1 = SKIN[k]; t = np.clip((np.hypot(_XX - cx, _YY - cy) - r0) / (r1 - r0), 0, 1); return t * t * (3 - 2 * t)
WMAP = {k: _w(k) for k in SKIN}
ARR = {k: np.asarray(IMG[k], np.uint8) for k in ('arm_near', 'arm_far')}
def skinned(k, pivot, ang):
    """layer-space RGBA of arm k bent by ang (radians, + = clockwise on screen) about pivot with the shoulder weight map."""
    if abs(ang) < 1e-4: return ARR[k]
    th = -ang * WMAP[k]; c, s_ = np.cos(th), np.sin(th); dx, dy = _XX - pivot[0], _YY - pivot[1]
    mx = (pivot[0] + c * dx - s_ * dy).astype(np.float32); my = (pivot[1] + s_ * dx + c * dy).astype(np.float32)
    return cv2.remap(ARR[k], mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))

# key poses (degrees; + = arm swings forward/toward screen-left and down, body lean + = forward)
ARM = TL.Track([(0.0, 0.0, 'in_out_cubic'), (0.7, 0.0, 'in_out_cubic'), (1.05, -9.0, 'in_out_cubic'), (1.75, 30.0, 'out_back'),
                (2.3, 26.0, 'in_out_cubic'), (3.1, 26.0, 'in_out_cubic'), (3.9, 0.0, 'out_back'), (5.0, 0.0)])
LEAN = TL.Track([(0.0, 0.0, 'in_out_cubic'), (0.7, 0.0, 'in_out_cubic'), (1.05, -1.2, 'in_out_cubic'), (1.85, 5.0, 'out_quad'),
                 (3.1, 5.0, 'in_out_cubic'), (4.0, 0.0, 'out_quad'), (5.0, 0.0)])
DELAY = 0.12
def far_arm(a): return 0.5 * ARM(a - DELAY)
def breath(a): return 1.0 + 0.004 * math.sin(2 * math.pi * a / 2.6)

def scene(cv, ctx):
    a = ctx.a
    cv.clear(T.BG)
    with cv.xf(T3(-150 + 8 * a, -80) @ S3(1.4)): cv.blit_image(PLATE)                    # plate, slow camera drift
    lean, an, af = math.radians(LEAN(a)), math.radians(ARM(a)), math.radians(far_arm(a))
    # figure local (layer px) -> world: feet pivot at FEET_WORLD, scale SC, lean about the boots, breathing about the boots
    body = T3(*FEET_WORLD) @ R3(-lean) @ S3(SC) @ np.array([[1, 0, 0], [0, breath(a), 0], [0, 0, 1.0]]) @ T3(-PFEET[0], -PFEET[1])
    def arm(img, p, ang): return body @ T3(*p) @ R3(ang) @ T3(-p[0], -p[1])      # + = hand swings toward screen-left (forward)
    # contact shadow (code, sun upper-left -> shadow to the right)
    cv.ellipse((FEET_WORLD[0] + 70, FEET_WORLD[1] - 6), 190, 20, fill=(16, 16, 18), alpha=0.5)             # contact shadow under the boots, falling right
    with cv.xf(body): cv.blit_image(Image.fromarray(skinned('arm_far', PF, af), 'RGBA'))
    with cv.xf(body): cv.blit_image(IMG['torso'])
    with cv.xf(body): cv.blit_image(Image.fromarray(skinned('arm_near', PN, an), 'RGBA'))
    # (v1 shoulder CAP removed 2026-11-26: with skinning the shoulder never moves, and the cap drew a second shoulder over the bent sleeve)
    return {}

def _stack_alpha(ang_n, ang_f):
    """alpha of the three layers in layer space at the given arm angles (degrees), for the gap test."""
    import cv2
    out = np.zeros((1536, 1024), np.float32)
    for k, p, ang in (('arm_far', PF, ang_f), ('torso', None, 0.0), ('arm_near', PN, ang_n)):
        al = (skinned(k, p, math.radians(ang)) if p is not None else np.asarray(IMG[k]))[..., 3].astype(np.float32) / 255
        out = 1 - (1 - out) * (1 - al)
    return out

def check_all(out_dir, results):
    checks = []
    rest = _stack_alpha(0, 0) > 0.5
    for name, p, rng in (('near', PN, (-12, 32)), ('far', PF, (-6, 18))):
        worst = 0
        for ang in np.linspace(*rng, 9):
            st = _stack_alpha(ang if name == 'near' else 0, ang if name == 'far' else 0) > 0.5
            yy, xx = np.mgrid[0:1536, 0:1024]; near = (xx - p[0]) ** 2 + (yy - p[1]) ** 2 < 70 ** 2
            holes = int((rest & ~st & near).sum()); worst = max(worst, holes)
        checks.append(('no gap at the %s shoulder over %s deg (opaque-at-rest pixels uncovered within 70 px of the pivot)' % (name, rng), worst < 150, 'worst %d px of %d' % (worst, int(near.sum()))))
    pk = max(np.linspace(0, DUR, 500), key=lambda t: ARM(t)); pf = max(np.linspace(0, DUR, 500), key=lambda t: far_arm(t))
    checks.append(('overlapping action: far arm peaks after the near arm', pf > pk, 'near peak %.2f s, far %.2f s' % (pk, pf)))
    checks.append(('anticipation: near arm swings back before the reach', min(ARM(t) for t in np.linspace(0.7, 1.4, 50)) < -5, 'min %.1f deg' % min(ARM(t) for t in np.linspace(0.7, 1.4, 50))))
    checks.append(('overshoot then settle on the reach', max(ARM(t) for t in np.linspace(1.7, 2.3, 60)) > ARM(2.3) + 1, 'peak %.1f vs settle %.1f' % (max(ARM(t) for t in np.linspace(1.7, 2.3, 60)), ARM(2.3))))
    return checks

INFO = dict(
    title='P05 Apollo astronaut movement (arm rig v2: shoulder skinning, Codex layers)',
    beats='B18 window (narration_t %.2f + 5.0 s); a rig proof, not the final B18 choreography' % N0,
    expected=('Astronaut stands on the lunar plate; small anticipation (near arm back, body up), then the near arm reaches forward and down while the body leans '
              'from the boots, overshoots a little and settles; the far arm follows a beat later with half the swing; then recovers. Breathing keeps the hold alive. '
              'No gaps open at the shoulders.'),
    science=('Anonymous A7L-style suit (no names, flags or patches). Motion is stylised; low lunar gravity is not simulated in this clip (it matters for walking and dust, '
             'not for an arm reach). Rig v1 has no elbow: the reach is a shoulder swing; the kneel/align pose (no photo evidence, gap G-ASTRO) will be a whole-pose replacement.'),
)

def specs():
    return [ClipSpec('P05', 'P05_astronaut_arm_rig', N0, DUR, scene, captions=False, audio=False, blur=(3, 0.5))]
