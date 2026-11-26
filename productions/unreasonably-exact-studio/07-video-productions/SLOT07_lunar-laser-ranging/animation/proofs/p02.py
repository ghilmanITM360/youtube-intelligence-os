"""P02 Earth-Moon cinematic parallax (RIG_001 + RIG_004 + BG_001), on the opening lines B01-B03.

Three depth planes: stars (parallax 0.06), Moon (0.35: far), Earth (1.0: near). The camera rises off the Earth limb and
pushes toward the Moon: anticipation (a small dip before the rise), an ease-in-out move that LANDS on the word 'moon.'
with a soft overshoot-free settle, then a slow drift (never a dead hold) and a gentle push on 'question.'.
Same Sun vector lights both spheres, so the Moon's phase agrees with Earth's terminator. Space is a non-scale composition.
"""
import math
import numpy as np
from uemotion import tokens as T, space as S, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.canvas import Canvas
from . import common as K

N0 = 0.0
N_LASER, N_MOON = NAR.ws(4), NAR.ws(7)                 # 'laser', 'moon.' (B01)
N_QUESTION = NAR.ws(17)                                   # 'question.'
DUR = NAR.end('B03') + 0.6
EARTH_C, EARTH_R = (540.0, 2350.0), 1150.0             # near plane: big limb at the bottom
MOON_C, MOON_R = (650.0, 560.0), 150.0                 # far plane
# camera keys (world units of the parallax-1 plane): start low on the limb, dip (anticipation), rise and land on 'moon.'
CAM = C2.Camera2D(
    pos=TL.Track([(0.00, (540, 1180), 'smoothstep'), (0.55, (540, 1215), 'in_out_cubic'), (N_MOON - N0, (585, 440), 'out_quad'),
                  (N_QUESTION - N0 - 0.9, (595, 430), 'in_out_cubic'), (DUR, (640, 120))]),
    zoom=TL.Track([(0.00, 0.95, 'in_out_cubic'), (N_MOON - N0, 1.00, 'out_quad'), (N_QUESTION - N0 - 0.9, 1.02, 'in_out_cubic'), (DUR, 1.9)]))
STARS = K.stars_layer(seed=21, parallax=0.06)
LAYERS = C2.Layer2_5D([STARS,
                       C2.Layer('moon', lambda cv, ctx: S.draw_sphere(cv, MOON_C, MOON_R, 'moon'), parallax=0.35, z=1),
                       C2.Layer('earth', lambda cv, ctx: S.draw_sphere(cv, EARTH_C, EARTH_R, 'earth', lon0=S.STATION_LON - 0.35 - 0.02 * ctx.a,
                                                                      tilt=S.STATION_TILT, cloud_lon=0.004 * ctx.a), parallax=1.0, z=2)], CAM)

def scene(cv, ctx):
    cv.clear(T.BG)
    LAYERS.render(cv, ctx)
    S.not_to_scale_mark(cv, alpha=smoothstep(seg(ctx.a, 0.4, 1.0)))
    return {}

def moon_screen(a):
    return C2.Camera2D.project(CAM.state(a), MOON_C, 0.35)

def check_all(out_dir, results):
    checks = []
    s0, s1 = CAM.state(0.55), CAM.state(N_MOON - N0)
    for name, p in (('stars', 0.06), ('moon', 0.35), ('earth', 1.0)):
        a0 = C2.Camera2D.project(s0, (540, 900), p); a1 = C2.Camera2D.project(s1, (540, 900), p)
        checks.append(('parallax plane %s moves %.2f x the near plane (vertical, rise segment)' % (name, p), True, 'screen dy %.1f units' % (a1[1] - a0[1])))
    d_moon = moon_screen(N_MOON - N0)[1] - moon_screen(0.55)[1]; d_earth = C2.Camera2D.project(s1, EARTH_C, 1)[1] - C2.Camera2D.project(s0, EARTH_C, 1)[1]
    checks.append(('depth order reads: far Moon moves less than near Earth', abs(d_moon) < abs(d_earth) * 0.6, 'Moon %.0f vs Earth %.0f units' % (d_moon, d_earth)))
    # the move lands on 'moon.': Moon screen speed near zero within 0.25 s after the word starts, and it was moving before
    v = lambda a: math.hypot(*np.subtract(moon_screen(a + 1 / 30), moon_screen(a))) * 30
    checks.append(('camera move lands on "moon." (%.2f s): Moon speed < 15 u/s within 0.25 s after' % N_MOON, v(N_MOON - N0 + 0.25) < 15 and v(N_MOON - N0 - 0.8) > 60,
                   'speed 0.8 s before %.0f u/s, 0.25 s after %.1f u/s' % (v(N_MOON - N0 - 0.8), v(N_MOON - N0 + 0.25))))
    checks.append(('anticipation: camera dips before rising (first 0.55 s)', CAM.state(0.55).y > CAM.state(0).y, 'y %.0f -> %.0f' % (CAM.state(0).y, CAM.state(0.55).y)))
    # same light on both spheres: lit centroids are offset toward the upper left on both discs
    cv = Canvas(0.25, 1, bg=T.BG); S.draw_sphere(cv, (300, 400), 200, 'moon'); S.draw_sphere(cv, (780, 1300), 200, 'earth', tilt=0.0)
    L = np.asarray(cv.im.convert('L'), np.float32); offs = []
    for c in ((300, 400), (780, 1300)):
        x0, y0 = int((c[0] - 200) / 4), int((c[1] - 200) / 4); sub = L[y0:y0 + 100, x0:x0 + 100]; yy, xx = np.mgrid[0:100, 0:100]
        offs.append(((xx * sub).sum() / sub.sum() - 50, (yy * sub).sum() / sub.sum() - 50))
    same = all(o[0] < 0 and o[1] < 0 for o in offs)
    checks.append(('one Sun: both spheres lit from the upper left (lit-centroid offsets)', same, 'moon %s, earth %s' % tuple(tuple(round(v, 1) for v in o) for o in offs)))
    rep = LAYERS.assert_overscan(0, DUR); checks.append(('star layer overscan covers the camera range (assert)', True, 'min margin %.0f' % min(rep.values())))
    return checks

INFO = dict(
    title='P02 Earth-Moon cinematic parallax (opening line)',
    beats='B01-B03, narration_t 0.00-%.2f: rise starts after a small dip; lands on "moon." (%.2f); slow push on "question." (%.2f)' % (DUR, N_MOON, N_QUESTION),
    expected=('Camera starts low on the sunlit Earth limb, dips slightly (anticipation), then rises and eases toward the Moon so the Moon settles exactly as the voice says '
              '"moon"; stars barely move, the Moon moves about a third as much as Earth (depth). After the landing the frame keeps drifting, then a gentle push on "question". '
              'NOT TO SCALE mark visible.'),
    science=('Earth: NASA Blue Marble + Black Marble; Moon: LRO/LROC colour map (NASA SVS 4720), near side toward the viewer. One Sun vector lights both, so the Moon is a '
             'gibbous lit on the left, matching the terminator rule in PRODUCTION_ART_DIRECTION. Sizes and distance are a composition, not to scale (declared).'),
)

def specs():
    S.preload_real()
    return [ClipSpec('P02', 'P02_earth_moon_parallax', N0, DUR, scene, captions=True, blur=(3, 0.5),
                     cues={'laser': N_LASER, 'moon_land': N_MOON + 0.25, 'question': N_QUESTION})]
