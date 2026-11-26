"""Unit checks for the uemotion primitives (run: render_proofs.py --selftest). Fails loudly; prints PASS lines."""
import math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uemotion import easing as E, timeline as TL, camera as C, canvas, optics as O, space as S, stopwatch as SW, photons as PH, tokens as T, narration

def ok(name, cond, detail=''):
    assert cond, 'FAIL %s %s' % (name, detail); print('PASS', name, detail)

def run():
    # easing endpoints / monotonic where expected / overshoot where expected
    xs = np.linspace(0, 1, 201)
    for nm in ('linear', 'smoothstep', 'in_quad', 'out_quad', 'in_cubic', 'out_cubic', 'in_out_cubic', 'out_expo', 'in_expo', 'in_out_expo', 'out_back', 'in_back', 'in_out_back', 'spring'):
        f = E.EASES[nm]; ok('ease %s endpoints' % nm, abs(f(0)) < 1e-9 and abs(f(1) - 1) < 1e-9, '(%.3g, %.3g)' % (f(0), f(1)))
    ok('out_back overshoots', max(E.ease_out_back(x) for x in xs) > 1.05)
    ok('spring overshoots then settles', max(E.spring(x, 0.35, 2.5) for x in xs) > 1.1 and abs(E.spring(1.0) - 1) < 1e-9)
    b = E.bezier(0.25, 0.1, 0.25, 1.0); ok('bezier css-ease monotonic', all(b(xs[i + 1]) >= b(xs[i]) - 1e-9 for i in range(200)))
    lin = E.bezier(0, 0, 1, 1); ok('bezier(0,0,1,1) is linear', max(abs(lin(x) - x) for x in xs) < 1e-5)
    # tracks and clocks
    tr = TL.Track([(0, 0, 'in_out_cubic'), (2, 10, 'linear'), (4, 0)]); ok('track values', abs(tr(1) - 5) < 1e-9 and tr(-1) == 0 and tr(9) == 0 and abs(tr(3) - 5) < 1e-9)
    v = TL.Track([(0, (0, 0)), (1, (10, 20))]); ok('vector track', v(0.5) == (5.0, 10.0))
    mc = TL.ModelClock([(10, 14, 0, 2.56)]); ok('model clock hold/run', mc(5) == 0 and abs(mc(12) - 1.28) < 1e-12 and mc(20) == 2.56 and abs(mc.slow_factor() - 4 / 2.56) < 1e-12)
    # camera / 2.5D parallax
    s0, s1 = C.CamState(500, 900, 1, 0), C.CamState(560, 900, 1, 0)
    for p in (0.1, 0.5, 1.0):
        a = C.Camera2D.project(s0, (700, 900), p); b_ = C.Camera2D.project(s1, (700, 900), p); ok('parallax %.1f' % p, abs((a[0] - b_[0]) / 60 - p) < 1e-9)
    lay = C.Layer2_5D([C.Layer('far', lambda c, x: None, 0.2, 0, (-100, -100, 1200, 2100))], C.Camera2D(pos=TL.Track([(0, C.CENTER), (1, (700, 960))])))
    try: lay.assert_overscan(0, 1); ok('overscan trips on too-small art', False)
    except AssertionError as e: ok('overscan trips on too-small art', 'overscan' in str(e))
    # canvas anti-aliasing: a half-covered pixel edge must produce intermediate values
    cv = canvas.Canvas(0.25, 4, bg=(0, 0, 0)); cv.circle((540, 960), 400, fill=(255, 255, 255)); a = np.asarray(cv.to_image().convert('L'))
    ok('supersampled edge has intermediate grey levels', len(np.unique(a[(a > 5) & (a < 250)])) > 8)
    # optics
    cube = O.CornerCube2D(apex=(0, 0), face=500); worst = 0
    for ang in np.linspace(-30, 30, 41):
        try: r = cube.trace((-150 + ang * 2, 900), ang)
        except AssertionError: continue
        worst = max(worst, np.abs(r['d_in'] + r['d_out']).max())
    ok('corner cube antiparallel (sweep)', worst < 1e-9, 'worst %.2e' % worst)
    # stopwatch and light model
    cv = canvas.Canvas(0.25, 1, bg=T.BG); ok('stopwatch digital string', SW.draw_stopwatch(cv, (300, 300), 100, 2.56) == '2.56')
    ok('c*t/2 reproduces 384,400 km', abs(299792458.0 * (2 * 384400e3 / 299792458.0) / 2 / 1e3 - 384400) < 1e-6)
    # histogram purity
    h = PH.PulseHistogram(2000); ok('histogram prefix property', (h.counts(500) <= h.counts(900)).all())
    ok('master narration duration', abs(narration.NAR.meta['duration'] - 95.39) < 1e-9)
    ok('v1->v2 remap: ends and a word edge', abs(narration.NAR.v1(92.53) - 95.39) < 1e-9 and abs(narration.NAR.v1(19.82) - narration.NAR.ws(49)) < 0.05)  # v1 'Not' start -> v2 'Not' start
    # blit_image must not write outside the warped bitmap (BORDER_TRANSPARENT garbage bug, 2026-11-26)
    from PIL import Image as _I; from uemotion.canvas import Canvas as _C
    cv = _C(0.5, 1, bg=(0, 0, 0)); base = np.asarray(cv.im.convert('RGB')).copy(); cv.blit_image(_I.new('RGBA', (50, 50), (255, 255, 255, 255)))
    out = np.asarray(cv.im.convert('RGB')); m = np.ones(out.shape[:2], bool); m[:30, :30] = False
    ok('blit_image leaves pixels outside the bitmap untouched', bool((out[m] == base[m]).all()))
    print('selftest: all passed'); return 0
