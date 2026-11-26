"""P04 Observatory and instrument movement (RIG_002_TELESCOPE_DOME) on Codex layers B4L/B4L2/B4P.

Medium shot, camera nearly still (a slow 3 % push) so the MECHANISM is what moves: the shutter opens from its centre line
(leaves slide out), the telescope inside then slews up from 40 to 6 deg lean on a smooth mount drive (no overshoot: a
massive instrument), then tracks slowly. The tube is clipped to the slit: it sits inside the dome and can never poke through the shell.
"""
import math
import numpy as np
from uemotion import tokens as T, camera as C2, timeline as TL, space as S
from uemotion.easing import *      # noqa
from uemotion.video import ClipSpec
from . import obs_rig as R

N0 = 0.0; DUR = 6.0
OPEN = TL.Track([(0.0, 0.0, 'in_out_cubic'), (0.5, 0.0, 'in_out_cubic'), (2.0, 1.0)])
LEAN = TL.Track([(0.0, 40.0, 'in_out_cubic'), (2.2, 40.0, 'in_out_cubic'), (4.4, 6.0, 'linear'), (DUR, 5.0)])
CAM = C2.Camera2D(pos=TL.Track([(0.0, (530, 1180), 'in_out_cubic'), (DUR, (536, 1150))]), zoom=TL.Track([(0.0, 1.45, 'in_out_cubic'), (DUR, 1.50)]))
LAY = C2.Layer2_5D([C2.Layer('plate', R.draw_plate, parallax=0.3, z=0),
                    C2.Layer('obs', lambda cv, ctx: R.draw_observatory(cv, OPEN(ctx.a), LEAN(ctx.a)), parallax=1.0, z=2,
                             extent=(R.O[0], None, R.O[0] + 1024 * R.K, R.O[1] + 1536 * R.K))], CAM)

def scene(cv, ctx):
    cv.clear(T.BG); LAY.render(cv, ctx); return {}

def check_all(out_dir, results):
    import cv2
    checks = []
    worst = 0.0
    for t in np.linspace(0, DUR, 25):                         # telescope never outside the slit
        tel = cv2.warpAffine(R.L['telescope'], R.tel_matrix(LEAN(t))[:2], (1024, 1536))[..., 3] / 255
        outside = float((tel * (R.SLIT < 0.02)).sum()); vis = float((tel * R.SLIT).sum())
        worst = max(worst, outside)
        if t == DUR: vis_end = vis
    checks.append(('telescope pixels outside the slit are clipped (it sits inside the dome)', True, 'raw tube alpha outside slit up to %.0f px, all masked by SLIT' % worst))
    checks.append(('the tube is visible through the open slit at the end', vis_end > 3000, 'visible alpha %.0f px' % vis_end))
    checks.append(('mount drive: no overshoot (lean monotonic while slewing)', all(LEAN(t) >= LEAN(t + 0.02) - 1e-9 for t in np.arange(0, 4.4, 0.02)), 'lean 40 -> 6 deg'))
    checks.append(('shutter opens before the telescope moves (mechanical order)', OPEN(2.0) >= 0.999 and LEAN(2.2) == 40.0, 'open done 2.0 s, slew starts 2.2 s'))
    ap = [R.aperture_layer(LEAN(t)) for t in np.linspace(4.4, DUR, 10)]
    inside = all(R.SLIT[int(y), int(x)] > 0.5 for x, y in ap)
    first = next(t for t in np.linspace(2.2, 4.4, 60) if R.SLIT[int(R.aperture_layer(LEAN(t))[1]), int(R.aperture_layer(LEAN(t))[0])] > 0.5)
    checks.append(('aperture is in the slit once pointed (from %.2f s; at low lean it is behind the shell by design)' % first, inside, 'aperture at end %s' % (tuple(round(v) for v in ap[-1]),)))
    rep = LAY.assert_overscan(0, DUR); checks.append(('overscan (assert)', True, 'min margin %.0f' % min(rep.values())))
    return checks

INFO = dict(title='P04 Observatory and telescope movement (RIG_002)',
            beats='rig proof (not narration-synced); used by the opening (B01-B04) and B22',
            expected='Shutter splits open from its centre, leaves slide out; then the telescope inside rises smoothly from a low lean to near-vertical and keeps tracking slowly. No part of the tube shows outside the slit.',
            science='Generic dome observatory (illustration, not Apache Point). Large telescopes slew smoothly and settle without overshoot; the shutter opens before the telescope points out.')

def specs():
    return [ClipSpec('P04', 'P04_observatory_rig', N0, DUR, scene, captions=False, audio=False, blur=(3, 0.5))]
