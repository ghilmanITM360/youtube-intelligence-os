"""P10 Pulse accumulation (B27 -> B29b, as one uninterrupted histogram): a pulse counter ticks up (accelerating then settling), detections stack
into a histogram, and a peak emerges from the background exactly on 'returns' (B29b anchor 70.59). Counts are illustrative."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, photons as PH, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from . import common as K

N0 = NAR.v1(61.40); DUR = NAR.v1(72.00) - N0
FIELD_BG = (4, 6, 14)
HIST = PH.PulseHistogram(5000, 40, 0.04, 0.25, 0.62, 0.028, seed=2013)
BOX = (150, 520, 930, 1170)              # V3: larger, centred in the shared data panel (was 130,700,950,1260)
N_B27, N_PULSES, N_RETURNS, N_END = NAR.start('B27'), NAR.anchor('B27'), NAR.anchor('B29b'), N0 + DUR
Z_EMERGE = 8.0
NSTAR = HIST.first_significant(Z_EMERGE, 10)
COUNTER = TL.Track([(N_B27, 0, 'in_quad'), (N_RETURNS, NSTAR, 'out_quad'), (N_RETURNS + 1.45, NSTAR * 1.18)])

def scene(cv, ctx):
    n = ctx.n; K.data_background(cv, n)
    cnt = COUNTER(n); K.illustrative_badge(cv, 'ILLUSTRATIVE COUNTS', alpha=smoothstep(seg(n, 61.45, 61.85)))
    al = smoothstep(seg(n, N_B27 - 0.1, N_B27 + 0.35))
    c = PH.draw_histogram(cv, HIST, int(cnt), BOX, alpha=al, peak_alpha=smoothstep(seg(n, N_RETURNS - 0.04, N_RETURNS + 0.22)),
                          peak_pop=spring(seg(n, N_RETURNS, N_RETURNS + 0.7), 0.4, 2.0) if n >= N_RETURNS else 0.0)
    # pulse counter (top right of the plot): number in mono; small laser-shot tick that blinks at the shot rate (capped visually)
    cv.text((BOX[2], 300), 'laser pulses fired', 34, T.GREY, anchor='rm', bold=True, alpha=al)
    cv.text((BOX[2], 370), format(int(cnt), ','), 62, T.WHITE, anchor='rm', mono=True, bold=True, alpha=al)
    # emphasis on 'pulses' (62.60): the counter nudges (follow-through on the word)
    return dict(count=int(cnt))


def check_all(out_dir, results):
    from uemotion.canvas import Canvas
    import hashlib
    checks = []; cs = TL.ClockSet(N0)
    cs_n = lambda t: COUNTER(t)
    # counter monotonic, accelerating then settling
    ts = np.arange(N0, N_END, 1 / 30); ns = np.array([COUNTER(t) for t in ts]); d = np.diff(ns) * 30
    peak_rate_t = ts[1:][np.argmax(d)]
    checks.append(('counter monotonic', bool((np.diff(ns) >= -1e-9).all()), 'final %d pulses' % ns[-1]))
    checks.append(('counter accelerates until "returns" then settles (peak rate near the anchor)', abs(peak_rate_t - N_RETURNS) < 0.35, 'peak rate %.0f pulses/s at %.2f s; anchor %.2f' % (d.max(), peak_rate_t, N_RETURNS)))
    # peak emerges from noise (computed from the simulated data, not from the truth)
    z = {k: HIST.significance(k)[1] for k in (50, 200, 500, 1000, int(NSTAR), 2400)}
    true_bin = int(0.62 * 40)
    j_end = HIST.significance(int(COUNTER(N_END - 0.01)))[0]
    checks.append(('peak not significant early (z < 3 at 200 pulses)', z[200] < 3.0, 'z=%s' % {k: round(v, 1) for k, v in z.items()}))
    checks.append(('peak significant at "returns" (z >= %.0f at n=%d)' % (Z_EMERGE, NSTAR), HIST.significance(int(COUNTER(N_RETURNS)))[1] >= Z_EMERGE, 'z=%.1f' % HIST.significance(int(COUNTER(N_RETURNS)))[1]))
    checks.append(('data-derived peak sits on the true time bin (+-1)', abs(j_end - true_bin) <= 1, 'argmax bin %d, true bin %d' % (j_end, true_bin)))
    checks.append(('peak was NOT already significant 1.5 s before the anchor (emerges, does not pre-exist)', HIST.significance(int(COUNTER(N_RETURNS - 1.5)))[1] < Z_EMERGE, 'z=%.1f' % HIST.significance(int(COUNTER(N_RETURNS - 1.5)))[1]))
    # background flat: bins away from the peak are consistent with Poisson (index of dispersion near 1)
    c = HIST.counts(HIST.n_max).astype(float); bg = np.delete(c, range(true_bin - 3, true_bin + 4)); disp = bg.var() / bg.mean()
    checks.append(('background is flat Poisson noise (variance/mean of off-peak bins)', 0.5 < disp < 2.0, 'dispersion %.2f' % disp))
    # purity: same n -> same pixels; counts only grow
    def h(nv):
        cv = Canvas(0.25, 1, bg=FIELD_BG); PH.draw_histogram(cv, HIST, nv, BOX); return hashlib.md5(cv.im.tobytes()).hexdigest()
    checks.append(('histogram picture is a pure function of the counter (same n -> identical pixels)', h(900) == h(900) and h(900) != h(1100), 'md5 equal for repeat render, different for n=900 vs 1100'))
    mono = all((HIST.counts(k + 25) >= HIST.counts(k)).all() for k in range(0, 2500, 125))
    checks.append(('bin counts never decrease as pulses accumulate', mono, 'sampled every 125 pulses'))
    # visual smoothness: largest per-frame change of the tallest bar (design units)
    hmax = []
    for t in ts:
        cc = HIST.counts(int(COUNTER(t))); mx = max(1, cc.max()); unit = min(22.0, (BOX[3] - BOX[1]) * 0.92 / mx); hmax.append(mx * unit)
    checks.append(('tallest bar height changes smoothly (max step per frame)', np.abs(np.diff(hmax)).max() < 60, 'max step %.1f design units/frame' % np.abs(np.diff(hmax)).max()))
    return checks

INFO = dict(
    title='P10 Pulse accumulation (peak emerges from noise)',
    beats='B27 start 61.65 ("from many laser pulses"), counter ramps through B28/B29 time, peak marker on "returns" (B29b anchor 70.59); clip narration_t 61.40-72.00',
    expected=("Dark field with a time axis. Detections from successive laser pulses stack as one dot per detection in 40 time bins (dots, then bars as counts grow). The pulse counter ticks up, "
              "accelerating until 'returns' and then settling. Flat background builds everywhere, and a peak builds in one bin; the data-derived peak marker (argmax of the smoothed histogram) pops on 'returns' "
              "once it is statistically significant. 'ILLUSTRATIVE COUNTS' badge throughout."),
    science=("The histogram is a deterministic simulation (seed 2013): per pulse Poisson(0.04) signal photons ~ N(0.62, 0.028) plus Poisson(0.25) uniform background, bins = 40. It is labelled illustrative (C08). "
             "Statistics are honest: the width of the signal never narrows artificially, the peak simply rises above Poisson noise as counts grow; the marker position is computed from the data (argmax of the 3-bin smoothed counts), "
             "not placed by hand. NOTE: in the film B28 (three dots) and B29 (atmosphere) are cut between B27 and B29b; the histogram is a pure function of the pulse count so the cut-away costs nothing. "
             "This proof shows it uninterrupted; the narration-aligned captions are therefore not drawn. Error bar shrinking (B30) and the '1 mm = 6.7 ps' figure are not in this clip."),
)

def specs():
    return [ClipSpec('P10', 'P10_pulse_accumulation', N0, DUR, scene, captions=False, cues={'many_pulses_B27_start': N_B27, 'pulses_anchor': N_PULSES, 'returns_peak': N_RETURNS})]
