"""P11 Stopwatch sync: stopwatch fades in on 'how long', the pulse leaves on 'light', stopwatch + pulse both run on ONE model clock
(slow motion, badge shown), and the stopwatch freezes on exactly 2.56 s as the pulse reaches Earth on 'seconds' (B06-B07)."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, stopwatch as SW, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from . import common as K

N0 = NAR.v1(10.80); DUR = NAR.v1(18.00) - N0
N_FADE = NAR.ws(31)                       # 'how'   11.42  stopwatch fades in at 0.00
N_EMIT = NAR.ws(35)                       # 'light' 12.81  pulse leaves, clock starts
N_STOP = NAR.anchor('B07')                # 'seconds.' 16.14 pulse back home, clock stops
MODEL = TL.ModelClock([(N_EMIT, N_STOP, 0.0, K.ROUND_TRIP)])
SLOW = MODEL.slow_factor()
N_MOON = N_EMIT + K.ONE_WAY * SLOW        # narration time of the turn-around (model 1.28)
CAM = C2.Camera2D(pos=TL.Track([(N_STOP - 1.4, C2.CENTER, 'in_out_cubic'), (N_STOP, (C2.CENTER[0] - 74, C2.CENTER[1] - 118))]),
                  zoom=TL.Track([(N_STOP - 1.4, 1.0, 'in_out_cubic'), (N_STOP, 1.14)]))
LAYERS = C2.Layer2_5D([K.stars_layer()], CAM)

def state(ctx):
    """everything that is drawn is derived from this (also used by the tests): the three clocks stay separate."""
    n, m = ctx.n, ctx.m
    pop = spring(seg(n, N_STOP, N_STOP + 0.7), 0.35, 2.2) if n >= N_STOP else 0.0
    tint = T.mix(T.WARM, T.COOL, smoothstep(seg(m, K.ONE_WAY, K.ONE_WAY + 0.14)))
    return dict(n=n, m=m, pop=pop, tint=tint, frozen=n >= N_STOP)

_OUT = {}
def diagram(cv, ctx):
    """world layer: Earth, Moon, ring, lanes, pulse, stopwatch (all on the one model clock via ctx.m)."""
    n, m = ctx.n, ctx.m; st = state(ctx)
    K.S.draw_earth_moon(cv, K.GEO, t=n)
    K.target_ring(cv, n, alpha=smoothstep(seg(n, 10.9, 11.3)), pulse=seg(n, N_MOON, N_MOON + 0.8))
    # emission anticipation: ring CONTRACTS onto the station, then the bead leaves (cause before effect)
    ea = seg(n, N_EMIT - 0.42, N_EMIT)
    if 0 < ea < 1: cv.circle((K.GEO.cx, K.GEO.earth_top - 2), lerp(70, 12, ease_in_cubic(ea)), outline=T.WARM, width=3, alpha=0.8 * ea)
    S.ring_ping(cv, (K.GEO.cx, K.GEO.earth_top - 2), seg(n, N_EMIT, N_EMIT + 0.6), T.WARM, 14, 70, 4)
    K.draw_lanes(cv, m, n)
    K.draw_pulse(cv, m)
    S.ring_ping(cv, (K.GEO.cx, K.GEO.earth_top - 2), seg(n, N_STOP, N_STOP + 0.8), T.COOL, 14, 100, 5)           # home arrival ring
    u = seg(n, N_FADE, N_FADE + 0.45); sc = lerp(0.82, 1.0, ease_out_back(u, 1.4)); al = smoothstep(u)        # drop-in on 'how long'
    cx, cy = K.SW_C
    from uemotion.camera import T3, S3
    with cv.xf(T3(cx, cy) @ S3(sc) @ T3(-cx, -cy)):
        _OUT['reading'] = SW.draw_stopwatch(cv, K.SW_C, K.SW_R, m, 3.0, alpha=al, pop=st['pop'], tint=st['tint'], frozen=st['frozen'])

LAYERS = C2.Layer2_5D([K.stars_layer(), C2.Layer('diagram', diagram, parallax=1.0, z=1)], CAM)

def scene(cv, ctx):
    n = ctx.n; cv.clear(T.BG); LAYERS.render(cv, ctx, t=n)
    K.top_hud(cv, alpha=1.0, slow=SLOW if n > N_FADE + 0.6 else None, slow_alpha=smoothstep(seg(n, N_FADE + 0.6, N_FADE + 1.0)))
    return dict(reading=_OUT.get('reading'), state=state(ctx))


def check_all(out_dir, results):
    from uemotion.video import render_frame
    spec = specs()[0]; checks = []
    # 1. THE assertion: final reading is exactly 2.56 s (displayed string and model value), asserted on every frame after the stop
    fin = []
    for i in range(math.ceil((N_STOP - N0) * 30), int(DUR * 30)):
        ctx = TL.ClockSet(N0, MODEL).at(i / 30.0)
        assert ctx.m == K.ROUND_TRIP, (i, ctx.m)
    from uemotion.canvas import Canvas
    last = TL.ClockSet(N0, MODEL).at(DUR - 1 / 30.0); cv = Canvas(0.25, 1, bg=T.BG); out = scene(cv, last)
    assert out['reading'] == '2.56', out['reading']
    assert abs(K.ROUND_TRIP - 2.56) < 1e-12
    c_si = 299792458.0; derived = 2 * 384400e3 / c_si
    assert round(derived, 2) == 2.56
    open(os.path.join(out_dir, 'ASSERT_RESULT_final_reading.txt'), 'w').write(
        'ASSERT final reading == "2.56": PASS\nlast frame displayed reading string: %r\nmodel_t at stop and after: %r (must equal 2.56)\n'
        'derived mean round trip 2*384400 km / c = %.5f s -> rounds to %.2f (claim C01)\nslow-motion factor (narration seconds per model second): %.4f\n'
        'emission at narration_t %.2f (word "light"), stop at %.2f (word "seconds.", beat B07 anchor)\n' % (out['reading'], last.m, derived, round(derived, 2), SLOW, N_EMIT, N_STOP))
    checks.append(('ASSERT: displayed final reading is exactly "2.56" and model_t == 2.56 on every frame after the stop', True,
                   'reading=%r, model_t=%r; written to ASSERT_RESULT_final_reading.txt' % (out['reading'], last.m)))
    checks.append(('derived value consistent with claim C01', True, '2*384400 km / c = %.4f s, rounds to 2.56' % derived))
    # 2. sync at pixel level: the rendered bead position must agree with the digital reading drawn in the same frame
    errs = []; samples = 0
    for k in range(40):
        tt = N_EMIT + 0.1 + (N_STOP - N_EMIT - 0.2) * k / 39; ctx = TL.ClockSet(N0, MODEL).at(tt - N0)
        cv = Canvas(0.5, 1, bg=T.BG)
        # draw only the pulse and read the digital string from the stopwatch function for the same ctx
        K.draw_pulse(cv, ctx.m); rd = SW.draw_stopwatch(Canvas(0.25, 1, bg=T.BG), K.SW_C, K.SW_R, ctx.m, 3.0)
        arr = np.asarray(cv.im.convert('RGB'), np.float32).sum(2); ys, xs = np.nonzero(arr > 300)
        if len(ys) == 0: continue
        w = arr[ys, xs]; yc = float((ys * w).sum() / w.sum()) / 0.5
        m_shown = float(rd); j = K.journey(m_shown); exp = K.GEO.y_at(j['p']); errs.append(abs(yc - exp)); samples += 1
    # tolerance: reading is rounded to 0.01 s => 0.01/1.28 of the lane = 5.3 units, plus trail centroid bias
    checks.append(('pulse position vs displayed reading (pixel centroid, %d sampled frames)' % samples, max(errs) < 40, 'max |dy| = %.1f design units (reading quantised to 0.01 s = 5.3 units/step; trail biases centroid backward)' % max(errs)))
    # 3. the turn-around happens at model 1.28 (reading 1.28)
    ctx = TL.ClockSet(N0, MODEL).at(N_MOON - N0); checks.append(('turn-around at the Moon at reading 1.28', abs(ctx.m - 1.28) < 1e-9, 'n=%.3f m=%.4f' % (N_MOON, ctx.m)))
    checks.append(('slow-motion factor is shown (badge) and finite', 1.0 < SLOW < 2.0, 'x%.2f; beat-map note: "2.56 s inside 3.3 s of speech"' % SLOW))
    # 4. clock monotonic and slow factor constant during the run
    ms = [TL.ClockSet(N0, MODEL).at(i / 30).m for i in range(int(DUR * 30))]; d = np.diff(ms)
    checks.append(('model clock monotonic, constant rate while running', bool((d >= -1e-12).all()), 'rate %.5f model s per frame while running' % (d[(d > 0)].mean())))
    # 5. overscan
    rep = LAYERS.assert_overscan(N0, N0 + DUR); checks.append(('star layer overscan covers the camera range (assert)', True, 'min margin %.0f world units' % min(rep.values())))
    return checks

INFO = dict(
    title='P11 Stopwatch sync (final reading exactly 2.56 s)',
    beats='B06-B07, narration_t 10.80-18.00: stopwatch on "how" (11.42), pulse and clock start on "light" (12.81), stop on "seconds." (16.14)',
    expected=("Stopwatch (analog dial + digital) fades in at 0.00 on 'how long'. On 'light' the emission ring contracts onto the launch station (anticipation) and the pulse bead leaves, "
              "the clock starts. Pulse and stopwatch both read the same model clock, played in slow motion (badge 'SLOW-MOTION xN ILLUSTRATIVE'; never real time). The bead touches the Moon "
              "ring exactly at reading 1.28, returns on the cool lane, and the stopwatch freezes on 2.56 as the bead reaches Earth on 'seconds.' (spring kick, hand and digits lock). "
              "A gentle punch-in toward the stopwatch lands with the stop. NOT TO SCALE mark visible."),
    science=("2 x 384,400 km / c = 2.5645 s (claim C01, verified, derived from the NASA mean semi-major axis); displayed value 2.56. One leg = 1.28 s (C02). The picture is a non-scale "
             "schematic (declared). The pulse is an educational symbol (no visible beam). The slow-motion badge states the time stretch; the stopwatch ends on the TRUE value. "
             "Departure from SCIENTIFIC_VISUAL_DESIGN V2 (which proposes the whole 11.4-16.1 s window, factor ~1.8): the clock here starts when the voice says 'light' (factor ~1.3), matching the "
             "beat map's 'pulse starts on light' and 'real time (2.56 s inside 3.3 s of speech)'. No speed-of-light or distance number appears."),
    extra_files=['ASSERT_RESULT_final_reading.txt'],
)

def specs():
    return [ClipSpec('P11', 'P11_stopwatch_sync', N0, DUR, scene, model=MODEL, captions=True,
                     cues={'how_stopwatch_in': N_FADE, 'light_emit': N_EMIT, 'moon_turn_1.28': N_MOON, 'seconds_stop_2.56_(+0.1s)': N_STOP + 0.1})]
