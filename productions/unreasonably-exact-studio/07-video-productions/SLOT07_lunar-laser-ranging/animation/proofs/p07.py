"""P07 Retroreflection: conceptual 2-D corner-cube cross-section, exit rays ANTIPARALLEL to entry rays (asserted),
plus the flat-mirror contrast variant (B21 A/B). Educational only: no dimensions, no device design."""
import json, math, os
import numpy as np
from uemotion import tokens as T, space as S, optics as O
from uemotion.easing import *      # noqa
from uemotion.video import ClipSpec
from . import common as K

DUR = 9.6
# (face struck first, fraction along that face, entry angle off vertical in degrees): three different entry angles, staggered
RAY_DEFS = [(0, 0.35, -4.0), (1, 0.40, -16.0), (0, 0.45, 20.0)]
def build(apex_y=560, y0=1520):
    """cube + the three ray set for a given apex height and entry height (P13 re-uses this above its caption band)."""
    cube = O.CornerCube2D(apex=(540, apex_y), face=640)
    start = [(K.aim_ray(cube, f, fr, a, y0), y0, a) for f, fr, a in RAY_DEFS]
    return cube, start, [cube.trace((x, y), a, end_y=y0) for x, y, a in start]
CUBE, START, RAYS = build()
Y0 = 1520
T0 = [0.9, 2.7, 4.5]            # entry start time of each ray (anim_t)
SPEED = 1500.0                  # design units / s along the ray (constant: light does not ease)
ALIGN_T = 6.3                   # pair-by-pair alignment highlight starts
ALIGN_STEP = 0.65
TICK_Y = [1250, 1340, 1430]

def ray_len(i): return O.polyline_len(RAYS[i]['points'])
def _seglens(pts): return [float(np.linalg.norm(np.array(pts[j + 1]) - np.array(pts[j]))) for j in range(len(pts) - 1)]

def ray_alpha(i, t):
    """ONE ray pair at a time: a finished ray steps back to 0.15 the moment the next ray starts; in the alignment stage the pair being
    explained is lit alone (others 0.15); the final hold keeps all rays quiet (0.22) so the crossings do not clutter the last frame."""
    if t < ALIGN_T:
        if i + 1 < 3: return lerp(1.0, 0.15, smoothstep(seg(t, T0[i + 1] - 0.1, T0[i + 1] + 0.3)))
        return lerp(1.0, 0.15, smoothstep(seg(t, ALIGN_T - 0.3, ALIGN_T)))
    t_i = ALIGN_T + ALIGN_STEP * i
    lit = smoothstep(seg(t, t_i, t_i + 0.25)) * (1 - smoothstep(seg(t, t_i + ALIGN_STEP, t_i + ALIGN_STEP + 0.3)))
    rest = 0.15 if t < ALIGN_T + ALIGN_STEP * 3 else lerp(0.15, 0.22, smoothstep(seg(t, ALIGN_T + ALIGN_STEP * 3, ALIGN_T + ALIGN_STEP * 3 + 0.4)))
    return lerp(rest, 1.0, lit)

def neutral_bg(cv):
    cv.clear(T.BG); cv.vgradient((14, 21, 42), (6, 9, 22))

def scene(cv, ctx):
    t = ctx.a
    neutral_bg(cv)
    u = ease_out_back(seg(t, 0.0, 0.9), 1.2); a = smoothstep(seg(t, 0.0, 0.5))
    from uemotion.camera import T3, S3
    cx, cy = CUBE.apex[0], CUBE.apex[1] + 250
    with cv.xf(T3(cx, cy) @ S3(lerp(0.93, 1.0, u)) @ T3(-cx, -cy)):
        O.draw_cube(cv, CUBE, alpha=a)
    K.conceptual_badge(cv, alpha=a)
    O.third_face_inset(cv, (880, 330), 92, alpha=smoothstep(seg(t, 0.5, 1.1)))
    for i, (sx, sy, ang) in enumerate(START):
        pts = RAYS[i]['points']; L = ray_len(i); sl = _seglens(pts)
        cv.circle((sx, sy), 14, outline=T.GREY, width=3, alpha=a * 0.7)                          # source marker
        S.ring_ping(cv, (sx, sy), seg(t, T0[i] - 0.28, T0[i] + 0.25), T.WARM, 12, 60, 4)         # anticipation ping
        prog = seg(t, T0[i], T0[i] + L / SPEED)                                                  # LINEAR: light speed does not ease
        if prog <= 0: continue
        ak = ray_alpha(i, t); done = prog >= 1.0; trav = prog * L
        head, hd = O.draw_ray(cv, pts, prog, alpha=ak, width=8)
        if not done: S.pulse_bead(cv, head, hd, T.WARM if trav < sl[0] + sl[1] else T.COOL, 0.8)
        for hp, dh in ((pts[1], sl[0]), (pts[2], sl[0] + sl[1])): O.hit_spark(cv, hp, seg(trav, dh, dh + 160))
        if trav > sl[0] * 0.5: S.arrowhead(cv, tuple(np.array(pts[0]) + (np.array(pts[1]) - np.array(pts[0])) * 0.45), RAYS[i]['d_in'], T.WARM, 24, alpha=ak)
        if trav > sl[0] + sl[1] + sl[2] * 0.55: S.arrowhead(cv, tuple(np.array(pts[2]) + (np.array(pts[3]) - np.array(pts[2])) * 0.55), RAYS[i]['d_out'], T.COOL, 24, alpha=ak)
    for i in range(3):                                                                           # guide ticks: exit lines up with entry
        on = smoothstep(seg(t, ALIGN_T + ALIGN_STEP * i, ALIGN_T + ALIGN_STEP * i + 0.3)); done_ = smoothstep(seg(t, ALIGN_T + ALIGN_STEP * (i + 1), ALIGN_T + ALIGN_STEP * (i + 1) + 0.3))
        ga = on * lerp(0.85, 0.30, done_)
        if ga > 0: O.guide_ticks(cv, RAYS[i]['points'][:2], RAYS[i]['points'][2:], TICK_Y[i], alpha=ga)


# ---------------------------------------------------------------- flat mirror contrast variant (stacked A over B, same rays)
PANEL_SPLIT = 990; MIR_Y = 450; YA = 900; YB = 1700; RING_R = 90
CUBE_B = O.CornerCube2D(apex=(540, 1040), face=420)
C_ANG = [12.0, 26.0]
def _cube_ray(ang):
    """aim near the apex so the (parallel, offset) return lands close to its source: offset = 2 x perpendicular distance of the entry line from the apex."""
    best = None
    for fr in np.linspace(0.08, 0.7, 63):
        for fi in (0, 1):
            try:
                x = K.aim_ray(CUBE_B, fi, fr, ang, YB); r = CUBE_B.trace((x, YB), ang, end_y=YB)
            except AssertionError: continue
            off = abs(O.cross2(np.array(r['points'][-1]) - np.array(r['points'][0]), r['d_in']))
            if abs(off - 62) < (best[0] if best else 1e9): best = (abs(off - 62), x, r)
    return best[1], best[2]
def _contrast_rays():
    out = []
    for ang in C_ANG:
        cx, c = _cube_ray(ang)
        m = O.flat_mirror_ray((cx, YA), ang, MIR_Y, end_y=YA)
        out.append((m, c, (cx, YA), (cx, YB)))
    return out
CRAYS = _contrast_rays()
CT0 = [1.0, 3.4]; CSPEED = 1000.0
CDUR = 9.0
VERDICT_T = 6.3

def _cross(cv, c, s, color, alpha):
    cv.line((c[0] - s, c[1] - s), (c[0] + s, c[1] + s), color, 8, alpha=alpha); cv.line((c[0] - s, c[1] + s), (c[0] + s, c[1] - s), color, 8, alpha=alpha)
def _tick(cv, c, s, color, alpha):
    cv.polyline([(c[0] - s, c[1]), (c[0] - s * 0.3, c[1] + s * 0.8), (c[0] + s, c[1] - s * 0.8)], color, 9, alpha=alpha)

def contrast_scene(cv, ctx):
    t = ctx.a
    neutral_bg(cv)
    a = smoothstep(seg(t, 0, 0.6))
    cv.line((120, PANEL_SPLIT), (960, PANEL_SPLIT), T.DIM, 2, alpha=a)
    # panel A: ghosted flat mirror (dashed + translucent = the rejected idea, not hardware)
    cv.polyline([(160, MIR_Y), (920, MIR_Y)], T.GLASS, 8, alpha=a * 0.55, dash=(26, 18))
    cv.rect((160, MIR_Y - 40, 920, MIR_Y), fill=T.GLASS, alpha=a * 0.08)
    # panel B: corner cube
    O.draw_cube(cv, CUBE_B, alpha=a, width=10)
    K.conceptual_badge(cv, alpha=a)
    for i, (m, c, sa, sb) in enumerate(CRAYS):
        for src in (sa, sb):
            cv.circle(src, RING_R, outline=T.DIM, width=3, alpha=a); cv.circle(src, 9, fill=T.GREY, alpha=a)
        for ray in (m, c):
            pts = ray['points']; sl = [float(np.linalg.norm(np.array(pts[j + 1]) - np.array(pts[j]))) for j in range(len(pts) - 1)]; L = sum(sl)
            u = seg(t, CT0[i], CT0[i] + L / CSPEED)
            S.ring_ping(cv, tuple(pts[0]), seg(t, CT0[i] - 0.28, CT0[i] + 0.25), T.WARM, 10, 50, 3)
            if u <= 0: continue
            nxt = CT0[i + 1] if i + 1 < len(CT0) else VERDICT_T
            dimk = lerp(1.0, 0.35, smoothstep(seg(t, nxt - 0.1, nxt + 0.4)))
            if i + 1 == len(CT0): dimk = lerp(1.0, 0.7, smoothstep(seg(t, VERDICT_T, VERDICT_T + 0.5)))
            head, hd = O.draw_ray(cv, pts, u, alpha=dimk, width=7)
            if u < 1: S.pulse_bead(cv, head, hd, T.WARM if u * L < sl[0] else T.COOL, 0.7)
            acc = 0.0
            for j in range(1, len(pts) - 1):
                acc += sl[j - 1]; O.hit_spark(cv, pts[j], seg(u * L, acc, acc + 130))
            S.arrowhead(cv, tuple(np.array(pts[0]) + (np.array(pts[1]) - np.array(pts[0])) * 0.45), ray['d_in'], T.WARM, 22, alpha=dimk) if u * L > sl[0] * 0.5 else None
            if u >= 1: S.arrowhead(cv, tuple(np.array(pts[-2]) + (np.array(pts[-1]) - np.array(pts[-2])) * 0.55), ray['d_out'], T.COOL, 22, alpha=dimk)
    va = smoothstep(seg(t, VERDICT_T, VERDICT_T + 0.5)); bounce = ease_out_back(seg(t, VERDICT_T, VERDICT_T + 0.5))
    if va > 0:
        for (m, c, sa, sb) in CRAYS:
            _cross(cv, (sa[0], sa[1] + 0), 24 * bounce, T.ALERT, va * 0.9)                                  # nothing came home to this ring
            cv.circle(tuple(m['points'][-1]), 12, outline=T.COOL, width=3, alpha=va * 0.8)                      # where the mirror sent it
            _tick(cv, (sb[0], sb[1]), 24 * bounce, T.COOL, va)                                                # came home to this ring


INFO = dict(
    extra_files=['assert_results.json'],
    title='P07 Retroreflection (conceptual corner cube) + flat-mirror contrast',
    beats='B19-B21 (V7). Standalone clip on anim_t (not narration-bound); the same scene functions are re-timed to the anchor words inside P13.',
    expected=("Clip 1: a 2-D corner-cube cross-section (two perpendicular faces, opening down toward Earth, third face as a magnified inset). "
              "Three rays at three different entry angles enter one after another (warm = outbound), bounce off both faces and leave (cool = home) "
              "ANTIPARALLEL to how they entered: parallel to the entry ray but laterally offset, never collinear. Finished rays step back so one pair is read at a time; "
              "then each pair is lit in turn with a faint pair of guide ticks across entry and exit. Clip 2 (B21 A/B): the same rays against a ghosted FLAT mirror "
              "(dashed, translucent): the mirror sends each ray away (X in the source ring), the cube returns it to its source ring (tick). Light moves at constant speed (linear), "
              "no beam is drawn into space, no number, no dimension."),
    science=("Specular reflection is computed, not drawn by hand: a 90 degree corner is two mirror reflections, whose product is a 180 degree rotation about the apex, so the exit "
             "direction is exactly minus the entry direction in the plane. This is asserted for every shown ray and for 3000 random rays "
             "(max |d_out + d_in| reported in assert_results.json). The exit is offset by 2 x (distance of the entry line from the apex): the film must say 'parallel', never 'the same line' "
             "(research note in PROGRESS_LOG: B21 exit ray is parallel but OFFSET). A flat mirror is asserted NOT antiparallel for any tilted ray. 2-D cross-section only shows two of three "
             "reflections; the third face is the inset. Claim C06 picture rule (km-wide footprint inset at B20) is NOT part of this clip; it is in P13. No operational equipment design."),
)

def check_all(out_dir, results):
    """programmatic geometry checks; also written to assert_results.json. returns [(name, passed, detail)]."""
    rng = np.random.default_rng(0); worst = 0.0; trials = 0
    cube = O.CornerCube2D(apex=(0, 0), face=600)
    while trials < 3000:
        ang = rng.uniform(-30, 30); fi = int(rng.integers(0, 2)); fr = rng.uniform(0.15, 0.95)
        try:
            sx = K.aim_ray(cube, fi, fr, ang, 900.0); r = cube.trace((sx, 900.0), ang)
        except AssertionError:
            continue
        worst = max(worst, float(np.abs(r['d_out'] + r['d_in']).max())); trials += 1
    pairs = []
    for i, r in enumerate(RAYS):
        din, dout = r['d_in'], r['d_out']; pts = r['points']; off = abs(O.cross2(np.array(pts[-1]) - np.array(pts[0]), din))
        pairs.append(dict(ray=i, angle_deg=START[i][2], d_in=[round(float(x), 9) for x in din], d_out=[round(float(x), 9) for x in dout],
                          dot=round(float(np.dot(din, dout)), 12), lateral_offset_units=round(float(off), 2)))
        assert abs(np.dot(din, dout) + 1) < 1e-12 and off > 1.0       # antiparallel AND offset (not collinear)
    flat = []
    for ang in (-26, -9, 17, 30):
        f = O.flat_mirror_ray((540, 900), ang, 500, end_y=900); flat.append(dict(angle_deg=ang, dot=round(float(np.dot(f['d_in'], f['d_out'])), 6)))
    cont = []
    for (m, c, sa, sb) in CRAYS:
        dm = float(np.linalg.norm(np.array(m['points'][-1]) - np.array(sa))); dc = float(np.linalg.norm(np.array(c['points'][-1]) - np.array(sb)))
        cont.append(dict(mirror_exit_miss=round(dm, 1), cube_exit_miss=round(dc, 1), ring_radius=RING_R)); assert dm > RING_R > dc, (dm, dc)
    prev_dim = [ray_alpha(i, T0[i + 1] + 0.35) for i in (0, 1)]; final_a = [ray_alpha(i, DUR - 0.05) for i in range(3)]; lit_alone = [ray_alpha(i, ALIGN_T + ALIGN_STEP * i + 0.4) for i in range(3)]
    angs = sorted(set(round(p['angle_deg']) for p in pairs))
    json.dump(dict(random_ray_trials=trials, max_abs_deviation_of_dout_plus_din=worst, shown_rays=pairs, flat_mirror_dots=flat, contrast=cont), open(os.path.join(out_dir, 'assert_results.json'), 'w'), indent=1)
    return [('exit = -entry for the 3 shown rays (assert, tol 1e-12)', True, 'dots=%s' % [p['dot'] for p in pairs]),
            ('exit = -entry for %d random rays (assert)' % trials, worst < 1e-9, 'max |d_out+d_in| = %.2e' % worst),
            ('exit offset from entry (not collinear)', True, 'lateral offsets %s units' % [p['lateral_offset_units'] for p in pairs]),
            ('one ray at a time: an earlier ray is <= 0.16 bright once the next ray has started', max(prev_dim) <= 0.16, 'alphas %s' % [round(x, 3) for x in prev_dim]),
            ('final hold is quiet: all rays <= 0.23 bright; in the alignment stage the explained pair is lit alone (>= 0.95)', max(final_a) <= 0.23 and min(lit_alone) >= 0.95, 'final %s ; lit %s' % ([round(x, 3) for x in final_a], [round(x, 3) for x in lit_alone])),
            ('three distinct entry angles', len(angs) == 3, str(angs)),
            ('flat mirror is NOT antiparallel for tilted rays (assert)', all(f['dot'] > -0.999 for f in flat), 'dots=%s' % [f['dot'] for f in flat]),
            ('contrast: mirror return misses source ring, cube return lands inside it', True, '%s' % cont)]

def specs():
    return [ClipSpec('P07', 'P07_retroreflection', 0.0, DUR, scene, audio=False),
            ClipSpec('P07', 'P07_flat_mirror_contrast', 0.0, CDUR, contrast_scene, audio=False)]
