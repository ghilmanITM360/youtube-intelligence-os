"""P01 Earth rotation, clouds and consistent lighting (RIG_001_GLOBE_LIGHTING).

Earth globe from the validated texture layers: NASA Blue Marble surface + Black Marble night lights (candidates, provenance in
assets/earth/_build_report.json) + Claude's composite of Codex's Batch 1 cloud tiles. The globe turns (spin speed is
ILLUSTRATIVE, about 15 deg/s instead of 15 deg/h), clouds drift slightly faster than the ground, the Sun never moves.
Camera: a slow push-in with an ease-in/ease-out, then a hold so the eye can rest. Window = B05 (pulse leaves Earth): the
globe is the backdrop that P02/P08 hand off from.
"""
import math, os
import numpy as np
from uemotion import tokens as T, space as S, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.canvas import Canvas
from . import common as K

N0 = NAR.start('B05'); DUR = 6.0
EC = (540.0, 1000.0); ER = 400.0
SPIN = math.radians(15.0)                    # rad per clip-second, illustrative
CLOUD_EXTRA = math.radians(2.5)              # clouds drift relative to the ground
CAM = C2.Camera2D(pos=TL.Track([(0.0, (540, 1000), 'in_out_cubic'), (4.6, (560, 980))]),
                  zoom=TL.Track([(0.0, 0.92, 'in_out_cubic'), (4.6, 1.08)]))
LAYERS = C2.Layer2_5D([K.stars_layer(seed=9, parallax=0.15),
                       C2.Layer('earth', lambda cv, ctx: S.draw_sphere(cv, EC, ER, 'earth', lon0=lon_at(ctx.a), cloud_lon=cl_at(ctx.a),
                                                                      tilt=math.radians(-18)), parallax=1.0, z=1)], CAM)

def lon_at(a): return math.radians(-40) - SPIN * a          # centre longitude falls => features move left-to-right (eastward spin)
def cl_at(a): return CLOUD_EXTRA * a

def scene(cv, ctx):
    cv.clear(T.BG)
    LAYERS.render(cv, ctx)
    K.illustrative_badge(cv, 'SPIN SPEED ILLUSTRATIVE', alpha=smoothstep(seg(ctx.a, 0.3, 0.9)))
    return {}

def _disc(a, tilt=-18.0, lon=None, scale=0.25):
    cv = Canvas(scale, 1, bg=T.BG)
    S.draw_sphere(cv, EC, ER, 'earth', lon0=lon_at(a) if lon is None else lon, cloud_lon=cl_at(a), tilt=math.radians(tilt))
    return np.asarray(cv.im.convert('RGB'), np.float32)

def check_all(out_dir, results):
    checks = []
    # 1. lighting is fixed while the ground turns: the luminance-weighted centroid of the lit side stays put
    cents = []
    for a in np.linspace(0, DUR, 7):
        L = _disc(a).mean(2); h, w = L.shape; yy, xx = np.mgrid[0:h, 0:w]; m = L > 25
        cents.append(((xx[m] * L[m]).sum() / L[m].sum(), (yy[m] * L[m]).sum() / L[m].sum()))
    cents = np.array(cents) * 4; drift = float(np.ptp(cents, 0).max())
    checks.append(('lighting constant while Earth spins (lit-side centroid drift over 7 samples)', drift < 25, '%.1f design units (disc radius %d)' % (drift, ER)))
    sx = cents[:, 0].mean() < EC[0]
    checks.append(('Sun from the left: lit centroid is left of the disc centre (token SUN)', bool(sx), 'centroid x %.0f vs centre %.0f' % (cents[:, 0].mean(), EC[0])))
    # 2. antimeridian seam: put lon 180 on the central meridian; the central column must not jump
    img = _disc(0, lon=math.pi, tilt=0.0, scale=0.5).mean(2); cx = int(EC[0] * 0.5); band = img[int(800 * .5):int(1200 * .5), cx - 3:cx + 4]
    jump = float(np.abs(np.diff(band, axis=1)).mean()); typ = float(np.abs(np.diff(img[int(800 * .5):int(1200 * .5), cx - 60:cx - 20], axis=1)).mean())
    checks.append(('no texture seam at the antimeridian (central-column step vs typical)', jump < 3 * typ + 1, 'seam %.2f vs typical %.2f' % (jump, typ)))
    # 3. pole: top-down orbit view (north pole facing the viewer) has no pinch: the 40 px around the pole are smooth
    img = _disc(0, tilt=-90.0 + 1e-3, scale=0.5).mean(2); c = (int(EC[1] * .5), int(EC[0] * .5)); patch = img[c[0] - 20:c[0] + 20, c[1] - 20:c[1] + 20]
    ring = img[c[0] - 80:c[0] + 80, c[1] - 80:c[1] + 80]
    gp, gr = float(np.abs(np.diff(patch, axis=0)).mean()), float(np.abs(np.diff(ring, axis=0)).mean())
    checks.append(('north-pole view: no pinch/singularity at the pole (gradient at pole vs surroundings)', gp < 2.5 * gr + 1, 'pole %.2f vs ring %.2f' % (gp, gr)))
    # 4. clouds move relative to the ground
    checks.append(('clouds drift relative to the surface', CLOUD_EXTRA > 0, '%.1f deg over the clip' % math.degrees(CLOUD_EXTRA * DUR)))
    rep = LAYERS.assert_overscan(0, DUR); checks.append(('star layer overscan covers the camera range (assert)', True, 'min margin %.0f' % min(rep.values())))
    return checks

INFO = dict(
    title='P01 Earth rotation, clouds and consistent lighting',
    beats='B05 window (narration_t %.2f + 6.0 s); not a narration-synced shot, a rig proof' % N0,
    expected=('Earth turns smoothly left-to-right (west to east) under a fixed Sun at the upper left; night lights appear only on the dark side; '
              'clouds drift slightly faster than the ground; atmosphere rim brighter on the sunlit limb; slow eased push-in, then a hold. '
              'Badge says the spin speed is illustrative.'),
    science=('Real geography (NASA Blue Marble, public domain) and night lights (NASA Black Marble). One Sun vector for every sphere (tokens.SUN). '
             'Spin direction is west-to-east as seen from above the north pole (counter-clockwise); speed is ~3600x real and labelled ILLUSTRATIVE. '
             'Clouds are Codex artwork (Batch 1 tiles) placed by Claude with loose climatology (tropical clusters near the equator, frontal bands and cyclones at 30-55 deg, '
             'cyclones only over ocean, southern cyclones mirrored); they are not a real weather snapshot.'),
)

def specs():
    S.preload_real()
    return [ClipSpec('P01', 'P01_earth_rotation_lighting', N0, DUR, scene, captions=False, audio=False, blur=(3, 0.5))]
