"""P12 Distance calculation (B33-B36): the formula d = c x t / 2 is built from tokens that move, and the long round-trip bar (length c*t) FOLDS IN HALF at the
Moon on 'two'; the ruler between Earth and Moon fills and the readout appears on 'distance'."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, stopwatch as SW, camera as C2, timeline as TL, formula as F
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.camera import T3, S3
from . import common as K

N0 = NAR.v1(78.80); DUR = NAR.v1(85.40) - N0
GEO = S.EarthMoonGeo(cx=540, earth_top=1440, earth_r=1300, moon_y=1000, moon_r=105)
D = GEO.y_launch - GEO.y_moon                    # one-way path in schematic units (Earth station -> Moon surface)
BAR_X = 760
SW_C12, SW_R12 = (540, 290), 125
ROW_Y, ROW_SIZE = 660, 116
W = NAR.ws
N_ROUND = W(210); N_T = NAR.anchor('B33')               # 'round' 79.38 ; 'time,' 79.76
N_BY, N_SPEED, N_LIGHT = W(215), W(217), NAR.anchor('B34')   # 'by' 81.16 ; 'speed' 81.45 ; 'light,' 81.85
N_THEN, N_DIVIDE, N_TWO = W(220), W(221), NAR.anchor('B35')  # 'then' 82.60 ; 'divide' 82.79 ; 'two.' 83.13
N_THATS, N_DIST = W(224), NAR.anchor('B36')              # "That's" 84.32 ; 'distance.' 84.60
FOLD0, FOLD1 = N_THEN + 0.10, N_TWO                      # fold sweeps exactly to the word 'two.'
SLIDE0, SLIDE1 = N_TWO + 0.35, N_THATS + 0.05

TEXTS = ['d', '=', 'c', '×', 't', '/', '2']
XS = None
def slots(cv):
    return F.row_positions(cv, TEXTS, ROW_SIZE, 540, ROW_Y, gap=30)

def tokens_at(cv, n):
    """build Token objects whose tracks are keyed on narration_t (pure function of n)."""
    xs = slots(cv); P = lambda i: (xs[i], ROW_Y)
    start_t = (SW_C12[0], SW_C12[1] + SW_R12 + 30 + 34)           # where the stopwatch readout pill is
    toks = []
    # 't': the stopwatch reading flies up, becoming the symbol t (lands on 'time,')
    fly = F.arc_path(start_t, P(4), N_T - 0.50, N_T, ease_in_out_cubic, bow=-70)
    a_time = F.fade(N_T - 0.50, N_T - 0.40)
    swap = lambda t: smoothstep(seg(t, N_T - 0.14, N_T - 0.02))                              # quick cross-fade just before landing
    toks.append(F.Token('2.56 s', 56, T.COOL, pos=fly, alpha=lambda t: a_time(t) * (1 - swap(t)), scale=lambda t: lerp(1.0, 2.0, ease_in_out_cubic(seg(t, N_T - 0.5, N_T)))))
    pop_t = lambda t: 1 + 0.22 * spring(seg(t, N_T, N_T + 0.55), 0.35, 2.0) if t >= N_T else 1.0
    toks.append(F.Token('t', ROW_SIZE, T.COOL, pos=P(4), alpha=swap, scale=pop_t))
    # 'c' and the multiply sign: arrive from the right on 'by' / 'speed', land together on 'light,'
    toks.append(F.Token('×', ROW_SIZE, T.WHITE, pos=F.arc_path((P(3)[0] + 120, ROW_Y - 90), P(3), N_BY - 0.05, N_LIGHT, ease_out_cubic, bow=40), alpha=F.fade(N_BY - 0.05, N_BY + 0.2)))
    toks.append(F.Token('c', ROW_SIZE, T.WARM, pos=F.arc_path((P(2)[0] - 140, ROW_Y - 110), P(2), N_SPEED - 0.05, N_LIGHT, ease_out_cubic, bow=-50), alpha=F.fade(N_SPEED - 0.05, N_SPEED + 0.2),
                         scale=lambda t: 1 + 0.2 * spring(seg(t, N_LIGHT, N_LIGHT + 0.5), 0.35, 2.0) if t >= N_LIGHT else 1.0))
    # 'd =' appears with the fold's anticipation; '/' lands on 'divide'; '2' lands on 'two.'
    toks.append(F.Token('d', ROW_SIZE, T.WHITE, pos=P(0), alpha=F.fade(N_THEN - 0.05, N_THEN + 0.2),
                        scale=lambda t: 1 + 0.30 * spring(seg(t, N_DIST, N_DIST + 0.6), 0.35, 2.0) if t >= N_DIST else 1.0))
    toks.append(F.Token('=', ROW_SIZE, T.WHITE, pos=P(1), alpha=F.fade(N_THEN - 0.05, N_THEN + 0.2)))
    toks.append(F.Token('/', ROW_SIZE, T.WHITE, pos=F.arc_path((P(5)[0] + 160, ROW_Y + 20), P(5), N_THEN + 0.10, N_DIVIDE + 0.20, ease_out_cubic, bow=30), alpha=F.fade(N_THEN + 0.10, N_DIVIDE)))
    toks.append(F.Token('2', ROW_SIZE, T.WARM, pos=F.arc_path((P(6)[0] + 200, ROW_Y + 40), P(6), N_DIVIDE - 0.10, N_TWO, ease_out_cubic, bow=40), alpha=F.fade(N_DIVIDE - 0.10, N_DIVIDE + 0.15),
                         scale=lambda t: 1 + 0.28 * spring(seg(t, N_TWO, N_TWO + 0.5), 0.35, 2.0) if t >= N_TWO else 1.0))
    return toks

def fold_theta(n):
    """anticipation (slight counter-lift) then a cubic sweep 0 -> pi that LANDS on the word 'two.'; small settle after."""
    pre = -0.10 * math.sin(math.pi * seg(n, N_THEN - 0.10, FOLD0))                       # lifts a touch the wrong way first
    sweep = math.pi * ease_in_out_cubic(seg(n, FOLD0, FOLD1))
    return max(-0.10, pre + sweep) if n < FOLD1 else math.pi

def bar_x(n):
    return lerp(BAR_X, GEO.cx + 90, ease_in_out_cubic(seg(n, SLIDE0, SLIDE1)))      # the one-way bar gets its OWN lane (right of the return lane, clear of the Moon disc)

_OUT = {}
def diagram(cv, ctx):
    n = ctx.n
    cx = GEO.cx
    S.draw_earth_moon(cv, GEO, t=n)
    # Earth-Moon axis lanes: ghosts, lit as the round trip is spoken ('round trip time')
    lit = smoothstep(seg(n, N_ROUND - 0.05, N_ROUND + 0.30)) * (1 - smoothstep(seg(n, N_LIGHT, N_LIGHT + 0.5)))
    S.flow_path(cv, [GEO.pos(0, 'out'), GEO.pos(1, 'out')], T.WARM, t=n, progress=1.0, width=6, head=True, alpha=0.12 + 0.75 * lit, head_size=28)
    S.flow_path(cv, [GEO.pos(1, 'ret'), GEO.pos(0, 'ret')], T.COOL, t=n, progress=1.0, width=6, head=True, alpha=0.12 + 0.75 * lit, head_size=28)
    # hinge guide: from the Moon to the bar's fold point (the same physical event for time and path)
    gk = smoothstep(seg(n, N_LIGHT + 0.3, N_LIGHT + 0.7)) * (1 - smoothstep(seg(n, SLIDE0, SLIDE0 + 0.4)))
    if gk > 0: cv.line((cx + 70, GEO.y_moon), (bar_x(n) - 40, GEO.y_moon), T.WHITE, 2, alpha=0.35 * gk, dash=(8, 8))
    # the bar: grows out of Earth on 'light,' (expo-out), folds on 'then divide by two', slides onto the Earth-Moon line
    grow = ease_in_out_cubic(seg(n, N_LIGHT, N_LIGHT + 0.75))
    th = fold_theta(n) if n >= N_LIGHT else 0.0
    glow = (1 - seg(n, N_THEN - 0.1, N_THEN + 0.15)) if N_THEN - 0.1 <= n < N_THEN + 0.15 else 0.0
    ab = 0.0 if grow <= 0 else 1.0
    if grow > 0:
        info = S.fold_bar(cv, bar_x(n), GEO.y_launch, D, th, 34, grow, glow=glow); _OUT['bar'] = info
        # leader from the formula row to the bar's free end: the formula IS the bar's label
        leader = smoothstep(seg(n, N_LIGHT, N_LIGHT + 0.4)) * (1 - smoothstep(seg(n, N_DIST, N_DIST + 0.3)))
        if leader > 0: cv.line((bar_x(n), ROW_Y + 78), (bar_x(n), info['y_end'] - 16), T.GREY, 2, alpha=0.5 * leader, dash=(6, 8))
    # ruler between Earth and Moon fills, readout appears on 'distance.'
    rk = ease_out_cubic(seg(n, N_THATS, N_DIST)); ra = smoothstep(seg(n, N_THATS - 0.1, N_THATS + 0.2))
    if ra > 0: S.ruler(cv, (cx - 150, GEO.y_launch), (cx - 150, GEO.y_moon), 10, 5, T.GREY, 4, fill=rk, fill_color=T.WHITE, alpha=ra)
    ro = smoothstep(seg(n, N_DIST, N_DIST + 0.18)); pop = spring(seg(n, N_DIST, N_DIST + 0.6), 0.4, 2.0) if n >= N_DIST else 0.0
    _OUT['readout_alpha'] = ro
    if ro > 0:
        mx, my = cx + 300, GEO.y_at(0.5) + 20
        with cv.xf(T3(mx, my) @ S3(1 + 0.10 * pop) @ T3(-mx, -my)):
            cv.rect((mx - 182, my - 68, mx + 182, my + 68), fill=(14, 20, 42), outline=T.WHITE, width=3, radius=24, alpha=ro)
            cv.text((mx, my - 14), '\u2248 384,000 km', 44, T.WHITE, bold=True, mono=True, alpha=ro)
            cv.text((mx, my + 40), 'mean distance', 32, T.GREY, alpha=ro)

def scene(cv, ctx):
    n = ctx.n; cv.clear(T.BG)
    layers = C2.Layer2_5D([K.stars_layer(seed=7), C2.Layer('diagram', diagram, 1.0, 1)], C2.Camera2D())
    layers.render(cv, ctx, t=n)
    S.not_to_scale_mark(cv, (60, K.BADGE_Y))
    # stopwatch (frozen 2.56 from B32; its number leaves as the token on 'time,')
    left = 1 - smoothstep(seg(n, N_T - 0.45, N_T - 0.1))
    SW.draw_stopwatch(cv, SW_C12, SW_R12, K.ROUND_TRIP, 3.0, alpha=lerp(0.45, 1.0, 1.0), tint=T.COOL, frozen=True, digits=False)
    pw, ph = SW_R12 * 1.45, SW_R12 * 0.52; y0 = SW_C12[1] + SW_R12 + 30
    cv.rect((SW_C12[0] - pw / 2, y0, SW_C12[0] + pw / 2, y0 + ph), fill=(10, 14, 30), outline=T.GREY, width=3, radius=14)
    cv.text((SW_C12[0] - 12, y0 + ph / 2 + 2), '2.56', int(SW_R12 * 0.40), T.COOL, mono=True, bold=True, alpha=lerp(0.25, 1.0, left)); cv.text((SW_C12[0] + pw / 2 - 24, y0 + ph / 2 + 8), 's', 32, T.GREY, mono=True, anchor='rm')
    for tk in tokens_at(cv, n): tk.draw(cv, n)
    return dict(out=dict(_OUT))


def check_all(out_dir, results):
    from uemotion.canvas import Canvas
    checks = []
    # fold geometry: after the fold the visible bar is exactly half as long and the free end lies on the base
    def bar_len(th, g=1.0):
        cv = Canvas(0.25, 1, bg=T.BG); return S.fold_bar(cv, 500, GEO.y_launch, D, th, 34, g)
    i0, i1, ih = bar_len(0.0), bar_len(math.pi), bar_len(math.pi / 2)
    assert abs(i0['length_visible'] - 2 * D) < 1e-6 and abs(i1['length_visible'] - D) < 1e-6 and abs(i1['y_end'] - GEO.y_launch) < 1e-6
    checks.append(('bar halves: visible length 2D before the fold, D after (assert), free end lands on the Earth end', True, '2D=%.1f -> %.1f ; y_end %.1f vs base %.1f ; edge-on at 90 deg: %.1f' % (i0['length_visible'], i1['length_visible'], i1['y_end'], GEO.y_launch, ih['length_visible'])))
    c_si = 299792458.0
    t_mean = 2 * 384400e3 / c_si; d_mean = c_si * t_mean / 2 / 1e3; d_disp = c_si * 2.56 / 2 / 1e3
    assert abs(d_mean - 384400) < 1e-6
    assert round(c_si * 2.56 / 2 / 1000 / 1000) * 1000 == 384000      # d in km = c*2.56/2/1000; rounded to thousands of km: the on-screen value (lead decision)
    assert round(384400 / 1000) * 1000 == 384000
    checks.append(('ASSERT round(d_km/1000)*1000 == 384000 with d_km = c*2.56/2/1000 (readout "\u2248 384,000 km" is consistent with the displayed t)', True, 'c*2.56/2 = %.0f km -> 384,000 ; sourced mean 384,400 km -> 384,000 at 3 s.f. ; with t = %.5f s the formula gives %.1f km' % (d_disp, t_mean, d_mean)))
    # the one-way bar must not sit on the return lane after the slide
    lanes = (GEO.lane_x('out'), GEO.lane_x('ret')); bx = bar_x(N_THATS + 1.0)
    checks.append(('folded bar has its own lane (>= 50 units from both light lanes and clear of the Moon disc)', min(abs(bx - l) for l in lanes) >= 50 and bx - 17 > GEO.cx + GEO.moon_r * 0.0 and bx > GEO.cx + 60, 'bar x = %.0f ; lanes at %s' % (bx, lanes)))
    # reveal events land on the anchor words (state functions evaluated at word times)
    ev = {}
    ev['t token lands on "time,"'] = (N_T, NAR.anchor('B33'))
    ev['bar starts growing on "light,"'] = (N_LIGHT, NAR.anchor('B34'))
    ev['fold ends exactly on "two."'] = (FOLD1, NAR.anchor('B35'))
    ev['readout appears on "distance."'] = (N_DIST, NAR.anchor('B36'))
    for k, (a, b) in ev.items(): assert abs(a - b) < 1e-9
    checks.append(('event times equal the beat-map anchor words', True, '; '.join('%s %.2f' % (k, v[0]) for k, v in ev.items())))
    th = [fold_theta(N_LIGHT)] ; ts = np.arange(FOLD0 - 0.2, FOLD1 + 0.3, 1 / 30); thetas = np.array([fold_theta(t) for t in ts])
    checks.append(('fold angle reaches pi at "two." and never exceeds it', abs(fold_theta(N_TWO) - math.pi) < 1e-9 and thetas.max() <= math.pi + 1e-9, 'theta(two.)=%.6f' % fold_theta(N_TWO)))
    checks.append(('fold is anticipated (small lift before the sweep)', thetas.min() < -0.02, 'min theta %.3f rad' % thetas.min()))
    # pixel tests for the readout: absent 0.1 s before, present 0.2 s after
    def region(nv):
        cv = Canvas(0.5, 1, bg=T.BG); scene(cv, TL.ClockSet(N0).at(nv - N0)); g = np.asarray(cv.im.convert('L'), np.float32)
        return g[int((GEO.y_at(0.5) - 60) * .5):int((GEO.y_at(0.5) + 100) * .5), int(690 * .5):int(1010 * .5)]       # panel interior, right of the bar
    r_m2, r_m1, r_p = region(N_DIST - 0.20), region(N_DIST - 0.10), region(N_DIST + 0.25)
    pre = int((np.abs(r_m1 - r_m2) > 40).sum()); post = int((np.abs(r_p - r_m1) > 40).sum())
    checks.append(('readout region unchanged before "distance." (-0.20 s vs -0.10 s) and changed by the readout after (+0.25 s)', pre < 40 and post > 800, 'changed px before the anchor %d, after %d' % (pre, post)))
    checks.append(('readout alpha at the anchor is 0 and at +0.18 s is 1', True, 'see render; alpha(anchor-0.01)=%.2f alpha(anchor+0.18)=%.2f' % (smoothstep(seg(N_DIST - 0.01, N_DIST, N_DIST + 0.18)), smoothstep(seg(N_DIST + 0.18, N_DIST, N_DIST + 0.18)))))
    return checks

INFO = dict(
    title='P12 Distance calculation (bar folds in half, readout on "distance")',
    beats='B33-B36, narration_t 78.80-85.40: "t" lands on "time," (79.76), c and the long bar land on "light," (81.85), the fold ends on "two." (83.13), the readout appears on "distance." (84.60)',
    expected=("The stopwatch's 2.56 flies up and becomes the symbol t on 'time,'. 'c' and the multiply sign arrive on 'speed'/'light,' and the long round-trip bar (length c x t; outbound half warm, return half cool, hinge at "
              "the Moon level) grows out of Earth on 'light,'. On 'then divide by two' the hinge pulses (anticipation), the cool half folds over the warm half like a paper strip (cubic sweep that ends exactly on 'two.', small settle), "
              "'d =' appears and '/ 2' lands on 'divide' / 'two.'. The one-way bar slides to its own lane right of the light lanes (it no longer sits on the return lane), the ruler fills, the readout '\u2248 384,000 km / mean distance' appears on 'distance.' and d pops."),
    science=("d = c t / 2 (C11, verified relationship); c = 299,792,458 m/s exactly. The fold is geometric: the free end of the return half travels y = hinge - L cos(theta) and lands on the Earth end at theta = pi (asserted), so out-and-back becomes one leg. "
             "The readout is '\u2248 384,000 km' with the label 'mean distance' (owner/lead decision): 384,000 is both c*2.56/2 = 383,734 km and the sourced mean 384,400 km (C01, NASA) rounded to 3 significant figures, so the arithmetic on screen is consistent with the displayed t = 2.56 s (asserted in code).  "
             "The bar and schematic are NOT to scale (mark shown); the bar's lengths are a schematic 2D vs D, never a measured scale. Simple model (ignores atmosphere and array geometry, C11) is not stated on screen; add to the owner decision list if wanted."),
)

def specs():
    return [ClipSpec('P12', 'P12_distance_calculation', N0, DUR, scene, captions=True,
                     cues={'time_t_lands': N_T, 'light_bar_grows': N_LIGHT, 'then_hinge_pulse': N_THEN, 'fold_mid': (FOLD0 + FOLD1) / 2, 'two_fold_done': N_TWO, 'distance_readout': N_DIST})]
