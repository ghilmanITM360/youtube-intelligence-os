"""P09 Faint detection (B26-B28): a sparse raster of faint detection markers (one row per laser pulse, x = arrival time), no bright flash,
then everything dims and exactly three individual markers hold ('A few photons')."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, photons as PH
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from . import common as K

N0 = NAR.v1(58.30); DUR = NAR.v1(66.20) - N0
FIELD_BG = (4, 6, 14)
X0, X1 = 150, 930; AXIS_Y = 1130; ROW0_Y = AXIS_Y - 70; PITCH = 62; ROWS = 14
N_PHOTONS = NAR.anchor('B26')                    # 'photons' 61.29: a click lands exactly on it
N_FEW = NAR.anchor('B28')                        # 'few' 64.02: three dots light and hold
ROW_DT = 0.36
T_ROW = lambda r: N_PHOTONS - 0.10 - 6 * ROW_DT + r * ROW_DT   # row 6: pulse-sent tick, then its detection click 0.10 s later lands on 'photons'
rng = np.random.default_rng(26)
# deterministic events: (row, x_frac). Mostly empty rows: sparse. Row 6 is forced onto the anchor word.
EVENTS = []
for r in range(ROWS):
    if r == 6 or rng.random() < 0.38: EVENTS.append((r, float(rng.choice([rng.uniform(0.08, 0.95), rng.normal(0.62, 0.04)]))))
EVENTS = [(r, min(0.95, max(0.05, x))) for r, x in EVENTS]
T_FADE0, T_FADE1 = N_FEW - 0.55, N_FEW - 0.05                   # raster dims in the pause before 'A few photons'
THREE = [(395, 985, 0.00), (548, 925, 0.34), (690, 995, 0.68)]    # (x, y, delay after 'few')

def scene(cv, ctx):
    n = ctx.n
    K.data_background(cv, n)                                           # V3: framed panel in the film's sky tone (was flat black)
    lg = smoothstep(seg(n, 60.9, 61.4)) * (1 - smoothstep(seg(n, T_FADE0 - 0.2, T_FADE0 + 0.2)))
    if lg > 0:
        cv.text((X0 - 28, K.DATA_PANEL[1] + 52), 'each row = one laser pulse', 32, T.GREY, anchor='lm', bold=True, alpha=lg)
        cv.circle((X0 - 28, K.DATA_PANEL[1] + 95), 6, fill=T.WARM, alpha=lg); cv.text((X0 - 8, K.DATA_PANEL[1] + 95), 'sent', 28, T.WARM, anchor='lm', bold=True, alpha=lg)
        cv.circle((X0 + 90, K.DATA_PANEL[1] + 95), 7, fill=T.COOL, alpha=lg); cv.text((X0 + 110, K.DATA_PANEL[1] + 95), 'photon back', 28, T.COOL, anchor='lm', bold=True, alpha=lg)
    field = 1 - smoothstep(seg(n, T_FADE0, T_FADE1))
    ax = smoothstep(seg(n, NAR.v1(58.55), NAR.v1(59.3)))
    PH.time_axis(cv, X0, X1, AXIS_Y, alpha=lerp(0.28, 1.0, field) * (ax if ax < 1 else 1), progress=ease_in_out_cubic(seg(n, 58.55, 59.4)))
    K.illustrative_badge(cv, 'ILLUSTRATIVE', alpha=smoothstep(seg(n, 58.5, 58.9)))
    if field > 0:
        for r in range(ROWS):
            tr = T_ROW(r); y = ROW0_Y - r * PITCH
            tick = seg(n, tr - 0.05, tr + 0.35)                                   # 'pulse sent' tick at the row start (very faint)
            if 0 < tick < 1: cv.circle((X0 - 28, y), 6 + 8 * tick, outline=T.WARM, width=2.5, alpha=0.8 * (1 - tick) * field)
            if tick > 0: cv.circle((X0 - 28, y), 6, fill=T.WARM, alpha=0.75 * field)          # V3: warm = sent (was a faint grey dot)
        for (r, xf) in EVENTS:
            y = ROW0_Y - r * PITCH; PH.detection_marker(cv, lerp(X0, X1, xf), y, n - (T_ROW(r) + 0.10), hold=True, size=1.8, ring_max=60, strength=field)
    for (x, y, d) in THREE:
        PH.detection_marker(cv, x, y, n - (N_FEW + d), hold=True, size=2.4, ring_max=80, strength=1.0, hold_ring=True)


def check_all(out_dir, results):
    from uemotion.canvas import Canvas
    from scipy import ndimage
    checks = []; cs = ClipSpec('P09', 'x', N0, DUR, scene)
    ml, mx, nz, areas = [], 0.0, 0, []
    prev = None; steps = []
    for i in range(int(DUR * 30)):
        cv = Canvas(0.5, 1, bg=FIELD_BG); scene(cv, type('C', (), dict(n=N0 + i / 30, a=i / 30, m=0.0))())
        g = np.asarray(cv.im.convert('L'), np.float32); ml.append(float(g.mean())); mx = max(mx, float(g.max())); areas.append(float((g > 40).mean()))
    steps = np.abs(np.diff(ml))
    checks.append(('no bright flash: max pixel luma over all frames (captions excluded)', mx < 190, 'max luma %.0f of 255 (flash would be > 230)' % mx))
    checks.append(('no brightness pop: max frame-to-frame change of mean luma', steps.max() < 0.6, 'max step %.3f (0-255 scale)' % steps.max()))
    checks.append(('sparse: lit pixels (luma>40) never exceed % of the frame', max(areas) < 0.01, 'max %.3f %%' % (100 * max(areas))))
    # event lands on the anchor word
    r6 = [e for e in EVENTS if e[0] == 6][0]; t_click = T_ROW(6) + 0.10
    checks.append(('a detection click lands on "photons" (%.2f s)' % N_PHOTONS, abs(t_click - N_PHOTONS) < 0.12, 'click at %.3f s, anchor %.3f (word edges are +-0.12 s estimates)' % (t_click, N_PHOTONS)))
    # exactly three markers hold at the end
    cv = Canvas(0.5, 1, bg=FIELD_BG); scene(cv, type('C', (), dict(n=N0 + DUR - 0.02, a=DUR, m=0.0))())
    g = np.asarray(cv.im.convert('L'), np.float32); g[int(1100 * .5):, :] = 0; g[:int(200 * .5), :] = 0       # ignore the dim axis and the badge text
    lab, k = ndimage.label(g > 60); sizes = ndimage.sum(g > 60, lab, range(1, k + 1)); big = int((sizes > 12).sum())
    checks.append(('exactly three markers hold at the end (connected blobs luma>60, area>12 px)', big == 3, 'blobs=%d (all sizes %s)' % (big, sorted(int(x) for x in sizes))))
    checks.append(('events: %d rows, %d detections, %d of 14 rows empty' % (ROWS, len(EVENTS), ROWS - len(EVENTS)), len(EVENTS) <= 8, 'sparse by construction'))
    return checks

INFO = dict(
    title='P09 Faint detection (sparse markers, no flash)',
    beats='B26-B28, narration_t 58.30-66.20. Axis draws on at 58.55; a pulse-sent tick per row every 0.36 s; the click of row 6 lands on "photons" (61.29); the raster dims at 63.5; three markers light and hold from "few" (64.02).',
    expected=("Dark field, a thin time axis. One tiny hollow tick per laser pulse appears at the left of its row; a detection (if any) shows as a small cool dot that fades in over 0.18 s with ONE thin expanding ring "
              "and then holds faintly. Most rows stay empty. In the pause before 'A few photons' the raster dims to black; three single markers (larger, soft ring) light one after another from 'few' and hold. "
              "'ILLUSTRATIVE' marks the counts as not data."),
    science=("C08: LLR works in the single-photon regime; the best station sees about 1 photon per shot, most see far fewer, so 'a few photons' (three dots) is a fair illustration while sparse rows are the common case. "
             "The marker is an educational symbol (photons are not visible objects). The three dots are illustrative, not a data claim, and are labelled ILLUSTRATIVE. No number on screen."),
)

def specs():
    return [ClipSpec('P09', 'P09_faint_detection', N0, DUR, scene, captions=True, cues={'photons_click': N_PHOTONS, 'raster_dims': T_FADE0, 'few_three_dots': N_FEW})]
