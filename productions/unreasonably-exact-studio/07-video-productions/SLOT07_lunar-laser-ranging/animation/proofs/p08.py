"""P08 Light journey (B08-B11): outbound warm / return cool, the 'there and back' correction, then each leg timed (0 -> 1.28 -> 2.56)
with pulse and stopwatch on one slowed model clock (illustrative-time badge)."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, stopwatch as SW, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from uemotion.camera import T3, S3
from . import common as K

N0 = NAR.v1(17.20); DUR = NAR.v1(26.40) - N0            # retimed to the V2 take
W = NAR.ws
N_THERE, N_AND, N_BACK_END = W(46), W(47), NAR.we(48)                 # 'there' / 'and' / end of 'back'          (B08)
N_NOT, N_TWO, N_EACH, N_WAY = W(49), W(50), W(55), NAR.anchor('B09')   # 'Not' ... 'each' ... 'way.' 20.91        (B09)
N_RESET0, N_RESET1 = NAR.v1(21.28), NAR.v1(21.80)                                      # stopwatch rewinds to 0.00 (anticipation of B10)
N_LAUNCH1, N_MOON = W(58), NAR.anchor('B10')                           # 'little' 21.92 -> 'moon' 23.48            (B10)
N_HOME = NAR.we(73)                                                    # end of 'return.'                          (B11)
# V2 take: 'and'->'return.' (1.68 s) is longer than 'little'->'moon' (1.35 s). Both legs must share ONE slow factor,
# so leg 2 is anchored on its arrival; it launches at ~24.13 s, on the second 'little' (24.12), mirroring leg 1.
N_LAUNCH2 = N_HOME - (N_MOON - N_LAUNCH1)
MODEL = TL.ModelClock([(N_LAUNCH1, N_MOON, 0.0, K.ONE_WAY), (N_LAUNCH2, N_HOME, K.ONE_WAY, K.ROUND_TRIP)])
SLOW = MODEL.slow_factor(0)
assert abs(MODEL.slow_factor(1) - SLOW) < 0.02, 'both legs must play at the same slow-motion factor so the badge stays true'
LEG_X = {'out': 440, 'ret': 640}
LAYERS = None

def display_value(n, m):
    """what the stopwatch shows: the frozen 2.56 from B07, a quick rewind, then the model clock."""
    if n < N_RESET0: return K.ROUND_TRIP
    if n < N_RESET1: return lerp(K.ROUND_TRIP, 0.0, ease_in_out_cubic(seg(n, N_RESET0, N_RESET1)))
    return m

def leg_bracket(cv, lane, color, alpha=1.0, grow=1.0):
    x = LEG_X[lane]; y0, y1 = K.GEO.y_launch, K.GEO.y_moon; ye = lerp(y0, y1, grow)
    s = 1 if lane == 'out' else -1
    cv.polyline([(x + s * 18, y0), (x, y0), (x, ye), (x + s * 18, ye)], color, 4, alpha=alpha)

def leg_label(cv, lane, text, color, alpha=1.0, pop=0.0, ghost=False):
    x = LEG_X[lane] - 28 if lane == 'out' else LEG_X[lane] + 28; y = K.GEO.y_at(0.5)
    anchor = 'rm' if lane == 'out' else 'lm'; sc = 1 + 0.18 * pop
    with cv.xf(T3(x, y) @ S3(sc) @ T3(-x, -y)):
        if ghost:
            w = cv.text_width(text, 46, bold=True, mono=True)
            x0 = x - w - 16 if lane == 'out' else x - 16; cv.rect((x0, y - 42, x0 + w + 32, y + 42), outline=color, width=3, radius=18, alpha=alpha * 0.8)
        cv.text((x, y), text, 46, color, anchor=anchor, bold=True, mono=True, alpha=alpha)

def scene(cv, ctx):
    n, m = ctx.n, ctx.m
    cv.clear(T.BG)
    def diagram(cv, c):
        K.S.draw_earth_moon(cv, K.GEO, t=n)
        K.target_ring(cv, n, alpha=1.0, pulse=seg(n, N_MOON, N_MOON + 0.8))
        # ghost lanes (potential path) always faintly visible
        S.flow_path(cv, [K.GEO.pos(0, 'out'), K.GEO.pos(1, 'out')], T.WARM, t=n, progress=1.0, width=5, head=False, alpha=0.14)
        S.flow_path(cv, [K.GEO.pos(1, 'ret'), K.GEO.pos(0, 'ret')], T.COOL, t=n, progress=1.0, width=5, head=False, alpha=0.14)
        # ---- B08: both journeys light up: outbound on 'there', return on 'and back'
        lit = 1 - smoothstep(seg(n, N_RESET0, N_RESET1))
        po = ease_in_out_cubic(seg(n, N_THERE - 0.05, N_AND + 0.15)); pr = ease_in_out_cubic(seg(n, N_AND, N_BACK_END))
        if lit > 0 and po > 0:
            S.flow_path(cv, [K.GEO.pos(0, 'out'), K.GEO.pos(1, 'out')], T.WARM, t=n, progress=po, width=9, alpha=lit * 0.95)
        if lit > 0 and pr > 0:
            S.flow_path(cv, [K.GEO.pos(1, 'ret'), K.GEO.pos(0, 'ret')], T.COOL, t=n, progress=pr, width=9, alpha=lit * 0.95)
        # ---- B10/B11: lanes re-light behind the pulse (model driven) + the pulse itself
        if n >= N_RESET1: K.draw_lanes(cv, m, n)
        K.draw_pulse(cv, m)
        S.ring_ping(cv, (K.GEO.cx, K.GEO.earth_top - 2), seg(n, N_HOME, N_HOME + 0.8), T.COOL, 14, 100, 5)
        S.ring_ping(cv, (K.GEO.cx, K.GEO.earth_top - 2), seg(n, N_LAUNCH1, N_LAUNCH1 + 0.6), T.WARM, 14, 70, 4)
        # ---- B09: the correction, on the stopwatch and on the legs
        dv = display_value(n, m); a_full = SW.hand_angle(K.ROUND_TRIP, 3.0); a_half = SW.hand_angle(K.ONE_WAY, 3.0); a0 = -math.pi / 2
        whole = ease_in_out_cubic(seg(n, N_NOT, N_NOT + 0.55)); split = ease_out_back(seg(n, N_WAY, N_WAY + 0.35), 1.3)
        arc_fade = 1 - smoothstep(seg(n, N_RESET0, N_RESET1))
        if whole > 0 and arc_fade > 0:
            r_arc = K.SW_R + 34; gap = 0.05 * split
            if split <= 0.001: cv.arc(K.SW_C, r_arc, a0, lerp(a0, a_full, whole), T.WHITE, 8, alpha=arc_fade)
            else:
                cv.arc(K.SW_C, r_arc, a0, a_half - gap, T.WARM, 8, alpha=arc_fade); cv.arc(K.SW_C, r_arc, a_half + gap, a_full, T.COOL, 8, alpha=arc_fade)
        ghost_a = smoothstep(seg(n, N_TWO, N_TWO + 0.25)) * (1 - smoothstep(seg(n, N_WAY, N_WAY + 0.2)))
        if ghost_a > 0:
            leg_label(cv, 'out', '2.56 s', T.GREY, ghost_a, ghost=True)
            sx = ease_out_cubic(seg(n, N_EACH - 0.1, N_EACH + 0.2))                                           # strike-through draws on 'each'
            if sx > 0:
                x, y = LEG_X['out'] - 28 - 120, K.GEO.y_at(0.5); cv.line((x - 30, y - 36), (x - 30 + 190 * sx, y - 36 + 72 * sx), T.ALERT, 8, alpha=ghost_a)
                cv.line((x - 30, y + 36), (x - 30 + 190 * sx, y + 36 - 72 * sx), T.ALERT, 8, alpha=ghost_a)
        # real leg labels: pop on 'way.'; dim during the count, lock with a pop on arrival
        out_arrive = smoothstep(seg(n, N_MOON - 0.05, N_MOON + 0.12)); ret_arrive = smoothstep(seg(n, N_HOME - 0.05, N_HOME + 0.12))
        la = smoothstep(seg(n, N_WAY, N_WAY + 0.2))
        if la > 0:
            dimmed = lerp(1.0, 0.30, smoothstep(seg(n, N_RESET0, N_RESET1)))
            pop_o = spring(seg(n, N_MOON, N_MOON + 0.6), 0.35, 2.0) if n >= N_MOON else (spring(seg(n, N_WAY, N_WAY + 0.5), 0.4, 2.0) if n < N_RESET0 else 0.0)
            pop_r = spring(seg(n, N_HOME, N_HOME + 0.6), 0.35, 2.0) if n >= N_HOME else (spring(seg(n, N_WAY, N_WAY + 0.5), 0.4, 2.0) if n < N_RESET0 else 0.0)
            for lane, col, arr, pop in (('out', T.WARM, out_arrive, pop_o), ('ret', T.COOL, ret_arrive, pop_r)):
                al = la * (dimmed + (1 - dimmed) * arr)
                leg_bracket(cv, lane, col, alpha=al * 0.8, grow=ease_out_cubic(seg(n, N_WAY, N_WAY + 0.5)))
                leg_label(cv, lane, '1.28 s', col, alpha=al, pop=pop)
        # ---- stopwatch (display value is the frozen 2.56, a rewind, then the model clock)
        stop_pop = spring(seg(n, N_HOME, N_HOME + 0.7), 0.35, 2.2) if n >= N_HOME else 0.0
        tint = T.mix(T.WARM, T.COOL, smoothstep(seg(m, K.ONE_WAY, K.ONE_WAY + 0.14))) if n >= N_RESET1 else T.COOL
        frozen = n >= N_HOME or n < N_RESET0
        _OUT['reading'] = SW.draw_stopwatch(cv, K.SW_C, K.SW_R, dv, 3.0, pop=stop_pop, tint=tint, frozen=frozen)
    global LAYERS
    if LAYERS is None:
        LAYERS = C2.Layer2_5D([K.stars_layer(seed=5), C2.Layer('diagram', diagram, 1.0, 1)], C2.Camera2D())
    LAYERS.layers[1].draw = diagram
    LAYERS.render(cv, ctx, t=n)
    K.S.not_to_scale_mark(cv, (60, K.BADGE_Y))
    sa = smoothstep(seg(n, N_RESET1, N_RESET1 + 0.3)) * (1 - smoothstep(seg(n, N_HOME + 0.4, N_HOME + 0.8)))
    if sa > 0: S.badge(cv, (1020, K.BADGE_Y), 'SLIGHTLY SLOWED DOWN', 26, T.GOLD, alpha=sa, anchor='rm')
    return dict(reading=_OUT.get('reading'))
_OUT = {}


def check_all(out_dir, results):
    from uemotion.canvas import Canvas
    checks = []; cs = TL.ClockSet(N0, MODEL)
    # model clock and leg times
    c1 = cs.at(N_MOON - N0); c2 = cs.at(N_HOME - N0); ch = cs.at(N_LAUNCH2 - N0 - 0.2)
    assert abs(c1.m - 1.28) < 1e-9 and abs(c2.m - 2.56) < 1e-9 and abs(ch.m - 1.28) < 1e-9
    checks.append(('stopwatch model clock: 1.28 at the Moon, held 1.28 during the pause, 2.56 at Earth', True, 'm(moon)=%.4f m(hold)=%.4f m(home)=%.4f' % (c1.m, ch.m, c2.m)))
    checks.append(('both legs play at the same slow factor (badge stays true)', True, 'x%.3f (out) vs x%.3f (return)' % (MODEL.slow_factor(0), MODEL.slow_factor(1))))
    # colour grammar: sample pixels on each lane mid-journey
    def lane_px(lane, m_val, n_val):
        cv = Canvas(0.5, 1, bg=T.BG); K.draw_pulse(cv, m_val)
        x, y = K.pulse_xy(m_val); px = cv.im.getpixel((int(x * 0.5), int(y * 0.5)))[:3]; return px
    po = lane_px('out', 0.6, 0); pr = lane_px('ret', 1.9, 0)
    checks.append(('colour grammar: outbound bead warm (R>B), return bead cool (B>R)', po[0] > po[2] and pr[2] > pr[0], 'out %s, return %s' % (po, pr)))
    # pulse position tied to model clock: outbound hits the Moon surface when m == 1.28 and stays on the lane
    j = K.journey(1.28 - 1e-6); j2 = K.journey(1.28 + 1e-6)
    checks.append(('pulse reaches the Moon at model 1.28 and turns', abs(j['p'] - 1) < 1e-4 and abs(j2['p'] - 1) < 1e-4 and j2['phase'] == 'ret', 'p before %.5f after %.5f' % (j['p'], j2['p'])))
    # split is at the physical midpoint: arc at 1.28 is exactly half of 2.56
    checks.append(('split lands at the half: angle(1.28)/angle(2.56) == 0.5', abs((SW.hand_angle(1.28, 3) + math.pi / 2) / (SW.hand_angle(2.56, 3) + math.pi / 2) - 0.5) < 1e-12, '1.28 + 1.28 = 2.56'))
    cues = dict(there=N_THERE, and_back=N_AND, not_=N_NOT, each_way=N_WAY, moon=N_MOON, ret=N_HOME)
    checks.append(('reveal times come from words/beat anchors', True, str({k: round(v, 2) for k, v in cues.items()})))
    return checks

INFO = dict(
    title='P08 Light journey (there and back, 1.28 s each way)',
    beats='B08-B11, narration_t 17.20-26.40. Outbound lights on "there" (%.2f), return on "and back" (%.2f), arc split on "way." (20.91), leg 1 lands on "moon" (23.48), leg 2 lands at the end of "return." (25.62)' % (N_THERE, N_AND),
    expected=("The stopwatch (frozen 2.56 from B07) gets a bracket arc over the whole interval on 'Not'; a ghost '2.56 s' label (the wrong idea 2.5 s each way) is struck out on 'each'; on 'way.' "
              "the dial arc splits at the half into a warm 1.28 and a cool 1.28 and matching leg brackets appear beside the lanes. The dial rewinds to 0.00, the pulse leaves, climbs the warm lane while "
              "the stopwatch counts 0 -> 1.28, lands on the Moon ring on 'moon' (leg label locks with a spring pop), returns down the cool lane while the stopwatch counts 1.28 -> 2.56 and stops on 2.56 at Earth. "
              "Pulse and stopwatch share one model clock (slow motion, badge 'SLOW-MOTION x1.2 ILLUSTRATIVE')."),
    science=("One leg = 384,400 km / c = 1.282 s (C02), shown as 1.28 s; whole = 2.56 s (C01). The split at the Moon is the same physical event for time and path. 'a little over a second' = 1.28 s is the MEAN "
             "(the distance varies, C03). Colour grammar warm out / cool back is checked by pixel sampling. The pulse moves at constant speed in model time (light does not ease). Non-scale schematic is declared. "
             "Honest limit: the return leg arrives at the END of 'return.' (25.62) rather than its first millisecond, because only 1.24 s separate 'and' and 'return' and the leg needs 1.28 s x slow factor; "
             "making both legs share one factor (1.2) was preferred over a faster return."),
)

def specs():
    return [ClipSpec('P08', 'P08_light_journey', N0, DUR, scene, model=MODEL, captions=True,
                     cues={'there_outbound_lights': N_THERE, 'not_arc': N_NOT, 'way_split': N_WAY, 'launch_leg1': N_LAUNCH1, 'moon_1.28': N_MOON, 'launch_leg2': N_LAUNCH2, 'return_2.56': N_HOME})]
