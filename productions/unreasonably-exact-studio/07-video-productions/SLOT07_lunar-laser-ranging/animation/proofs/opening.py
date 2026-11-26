"""OPENING: three competing treatments of narration 0 - 9.6 s (HumanCraft V4 three-candidate judgement), rendered as real clips.

  A  ground-level cinematic : observatory + Moon in one frame from frame 0; slit opens, telescope rises, camera tilts toward the Moon.
  B  close-up to wide       : starts inside the opening slit on the telescope; pull-back reveals the dome, then the Moon.
  C  Earth-to-Moon          : Earth limb + Moon; push to the station on the limb, then the aim line to the Moon.

Shared beats (V2 word timings): 'Imagine pointing a powerful laser at the moon.' = aim; 'Not to light it up.' = the WRONG idea
(a floodlight cone that brightens the Moon, then a 'no' mark and the cone collapses); 'To ask it a question.' = the telescope
locks on (reticle); 'You fire a pulse' = one small pulse leaves the aperture and reaches the Moon in 1.28 s REAL time
(it arrives on the word 'reflector'). No continuous beam is ever drawn to the Moon.
"""
import math
import numpy as np
from uemotion import tokens as T, space as S, camera as C2, timeline as TL
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.video import ClipSpec
from . import common as K, obs_rig as R

N_MOON, N_NOT, N_UP, N_TO, N_Q, N_QEND, N_FIRE, N_REFL = NAR.ws(7), NAR.ws(8), NAR.we(12), NAR.ws(13), NAR.ws(17), NAR.we(17), NAR.ws(19), NAR.ws(24)
N_AT, N_MOON_END = NAR.ws(5), NAR.we(7)          # V3: 'at the moon.' = the aim trace; the pause after it = the laser charging (no static hold)
ONE_WAY = 1.28                       # s, Earth -> Moon light time (C02)
T_LAUNCH = N_FIRE + 0.08             # the pulse leaves a beat after 'fire' begins
T_ARRIVE = T_LAUNCH + ONE_WAY        # real time: lands on 'reflector'
DUR = 9.7

LEAN = TL.Track([(0.0, 38.0, 'in_out_cubic'), (0.9, 38.0, 'in_out_cubic'), (2.75, 6.0, 'linear'), (DUR, 4.5)])   # mount drive: smooth, no overshoot; then sidereal-like tracking
OPEN = TL.Track([(0.0, 0.0, 'in_out_cubic'), (0.12, 0.0, 'in_out_cubic'), (0.95, 1.0)])
OPEN_B = TL.Track([(0.0, 0.45, 'in_out_cubic'), (0.75, 1.0)])          # B opens on the telescope already half revealed

# ---------------------------------------------------------------- shared overlays (screen space)
def wrong_idea(cv, ap, mc, mr, a):
    """'Not to light it up': floodlight cone + over-lit Moon, a 'no' mark, then the cone collapses into a thin line and vanishes."""
    grow = smoothstep(seg(a, N_NOT + 0.05, N_NOT + 0.40)); kill = smoothstep(seg(a, N_UP + 0.02, N_UP + 0.50))
    if grow <= 0 or kill >= 1: return
    width = mr * 1.25 * (1 - kill) ** 1.3; al = grow * (1 - kill)
    d = np.subtract(mc, ap); n = np.array([-d[1], d[0]]) / (np.linalg.norm(d) + 1e-9)
    tip = np.add(mc, n * width), np.subtract(mc, n * width)
    for k, f in ((1.0, 0.10), (0.65, 0.10), (0.35, 0.12)):                       # soft layered cone (stage-light look)
        cv.polygon([ap, tuple(np.add(mc, n * width * k)), tuple(np.subtract(mc, n * width * k))], fill=(255, 236, 190), alpha=al * f)
    cv.glow(mc, mr * 1.9, (255, 240, 200), 0.55 * al)
    cv.circle(mc, mr * 0.98, fill=(255, 246, 225), alpha=0.35 * al)               # the Moon washed out = 'lit up'
    no = smoothstep(seg(a, N_UP - 0.35, N_UP - 0.10)) * (1 - smoothstep(seg(a, N_UP + 0.30, N_UP + 0.55)))
    if no > 0:
        c = tuple(np.add(ap, d * 0.5)); r = 54 * (0.85 + 0.15 * ease_out_back(seg(a, N_UP - 0.35, N_UP - 0.05)))
        cv.circle(c, r + 6, fill=T.BG, alpha=0.55 * no); cv.circle(c, r, outline=T.ALERT, width=7, alpha=no)
        q = r * 0.70; cv.line((c[0] - q, c[1] - q), (c[0] + q, c[1] + q), T.ALERT, width=7, alpha=no)

def reticle(cv, mc, mr, a):
    """'To ask it a question': four brackets converge on the Moon and lock with a brief flash on 'question.'."""
    u = seg(a, N_TO, N_Q + 0.15); out = smoothstep(seg(a, N_FIRE + 0.6, N_FIRE + 1.2))
    if u <= 0 or out >= 1: return
    s = lerp(2.3, 1.32, ease_out_back(u, 1.2)); al = smoothstep(u * 3) * (1 - out)
    flash = math.exp(-((a - N_QEND) / 0.12) ** 2); col = T.mix(T.WHITE, T.WARM, flash)
    L = mr * 0.55
    for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
        x, y = mc[0] + sx * mr * s, mc[1] + sy * mr * s
        cv.polyline([(x, y - sy * L), (x, y), (x - sx * L, y)], col, width=5 + 3 * flash, alpha=al)

def aim_line(cv, ap, mc, mr, a):
    """V3: dashed aim guide (a graphic, not light). It TRACES from the aperture to the Moon on 'at the moon.' (the opening's
    0:02-0:04 action), stays as the line the wrong-idea cone grows out of, returns under 'To ask it a question', fades at 'fire'."""
    tr = ease_out_cubic(seg(a, N_AT, N_MOON + 0.10))
    if tr <= 0: return
    cone = smoothstep(seg(a, N_NOT, N_NOT + 0.3)) * (1 - smoothstep(seg(a, N_UP + 0.2, N_UP + 0.6)))
    al = (1 - 0.7 * cone) * (1 - smoothstep(seg(a, N_FIRE - 0.3, N_FIRE + 0.1)))
    if al <= 0: return
    d = np.subtract(mc, ap); e = np.subtract(mc, d / np.linalg.norm(d) * mr * 1.1); tip = tuple(np.add(ap, (e - np.array(ap)) * tr))
    cv.line(ap, tip, T.WHITE, width=3.5, alpha=0.55 * al, dash=(14, 16), phase=a * 40)
    S.ring_ping(cv, tuple(e), seg(a, N_MOON + 0.05, N_MOON + 0.65), T.WHITE, 8, 60, 3, alpha=0.8)   # the line 'touches' the Moon on 'moon.'
    ch = smoothstep(seg(a, N_MOON_END - 0.1, N_MOON_END + 0.5)) * (1 - smoothstep(seg(a, N_NOT + 0.05, N_NOT + 0.35)))
    if ch > 0:                                                        # anticipation in the pause: the laser 'charges' in the aperture
        cv.glow(ap, 26 + 10 * smoothstep(seg(a, N_MOON_END, N_NOT)), T.WARM, 0.55 * ch * (0.85 + 0.15 * math.sin(a * 19)))
        cv.circle(ap, 6, fill=T.mix(T.WARM, T.WHITE, 0.5), alpha=0.9 * ch)

def pulse(cv, ap, mc, mr, a):
    """one pulse, constant speed (light), 1.28 s real time; muzzle ping at launch, arrival ping at the Moon."""
    S.ring_ping(cv, ap, seg(a, T_LAUNCH - 0.02, T_LAUNCH + 0.45), T.WARM, 10, 70, 5)
    u = (a - T_LAUNCH) / ONE_WAY
    d = np.subtract(mc, ap); end = np.subtract(mc, d / np.linalg.norm(d) * mr * 0.9)
    if 0 <= u <= 1: S.pulse_bead(cv, tuple(np.add(ap, (end - np.array(ap)) * u)), d, T.WARM, 1.35, trail=90)
    S.ring_ping(cv, tuple(end), seg(a, T_ARRIVE, T_ARRIVE + 0.5), T.WARM, 10, 80, 5)

def overlays(cv, ap, mc, mr, a):
    aim_line(cv, ap, mc, mr, a); wrong_idea(cv, ap, mc, mr, a); reticle(cv, mc, mr, a); pulse(cv, ap, mc, mr, a)
    # V3: the 'PULSE DRAWN AS A DOT · REAL TIME' pill is gone (implementation note); the film shows a small 'Real speed' note (roughcut DISCLOSURES)

# ---------------------------------------------------------------- A / B: ground level, shared world
MOON_W, MOON_R, MOON_P = (800.0, 330.0), 100.0, 0.12
def ground_layers(cam, open_tr=OPEN):
    return C2.Layer2_5D([
        C2.Layer('plate', R.draw_plate, parallax=0.30, z=0, extent=(R.PLATE_EXTENT[0], None, R.PLATE_EXTENT[2], R.PLATE_EXTENT[3])),
        C2.Layer('moon', lambda cv, ctx: S.draw_sphere(cv, MOON_W, MOON_R, 'moon'), parallax=MOON_P, z=1),
        C2.Layer('observatory', lambda cv, ctx: R.draw_observatory(cv, open_tr(ctx.a), LEAN(ctx.a)), parallax=1.0, z=2,
                 extent=(R.O[0], None, R.O[0] + 1024 * R.K, R.O[1] + 1536 * R.K))], cam)

WIDE = ((600, 905), 1.10)                       # framing that holds dome + Moon after the landing on 'moon.'
# V3 camera: settle on the dome while the telescope rises, then a purposeful tilt-up ALONG the aim line on 'at the moon.' that keeps
# drifting through the pause (no static hold 0:02-0:04); the pulse later flies through this framing.
CAM_A = C2.Camera2D(pos=TL.Track([(0.0, (540, 1120), 'in_out_cubic'), (0.75, (540, 1112), 'in_out_cubic'), (N_NOT + 0.7, (632, 852), 'linear'), (DUR, (642, 826))]),
                    zoom=TL.Track([(0.0, 1.00, 'in_out_cubic'), (0.75, 1.01, 'in_out_cubic'), (N_NOT + 0.7, 1.17, 'linear'), (DUR, 1.22)]))
SLIT_W = R.to_world((500, 880))
CAM_B = C2.Camera2D(pos=TL.Track([(0.0, SLIT_W, 'in_out_cubic'), (1.0, (SLIT_W[0], SLIT_W[1] - 20), 'in_out_cubic'), (N_MOON + 0.05, WIDE[0], 'in_out_cubic'), (DUR, (612, 880))]),
                    zoom=TL.Track([(0.0, 2.45, 'in_out_cubic'), (1.0, 2.30, 'in_out_cubic'), (N_MOON + 0.05, WIDE[1], 'in_out_cubic'), (DUR, 1.16)]))
LAY_A, LAY_B = ground_layers(CAM_A), ground_layers(CAM_B, OPEN_B)

def ground_points(cam, a):
    s = cam.state(a)
    ap = C2.Camera2D.project(s, R.to_world(R.aperture_layer(LEAN(a))), 1.0)
    mc = C2.Camera2D.project(s, MOON_W, MOON_P); mr = MOON_R * s.zoom ** MOON_P
    return ap, mc, mr

def scene_ground(lay, cam):
    def scene(cv, ctx):
        cv.clear(T.BG); lay.render(cv, ctx); overlays(cv, *ground_points(cam, ctx.a), ctx.a); return {}
    return scene

# ---------------------------------------------------------------- C: Earth-to-Moon
EARTH_C, EARTH_R = (540.0, 2350.0), 1150.0
STATION = (540.0, EARTH_C[1] - EARTH_R)               # STATION_TILT puts the station on the top limb
MOON_C_W, MOON_C_R, MOON_C_P = (700.0, 470.0), 150.0, 0.35
CAM_C = C2.Camera2D(pos=TL.Track([(0.0, (540, 960), 'in_out_cubic'), (1.9, (545, 1150), 'in_out_cubic'), (N_MOON + 0.1, (600, 900), 'in_out_cubic'), (DUR, (610, 870))]),
                    zoom=TL.Track([(0.0, 1.00, 'in_out_cubic'), (1.9, 1.55, 'in_out_cubic'), (N_MOON + 0.1, 1.05, 'in_out_cubic'), (DUR, 1.12)]))
ICON = None
def _station_icon():
    global ICON
    if ICON is None:
        from PIL import Image
        im = Image.fromarray(R.compose(1.0, 6.0, ridge=False)).crop((150, 600, 870, 1260)); ICON = im
    return ICON
LAY_C = C2.Layer2_5D([K.stars_layer(seed=31, parallax=0.06),
                      C2.Layer('moon', lambda cv, ctx: S.draw_sphere(cv, MOON_C_W, MOON_C_R, 'moon'), parallax=MOON_C_P, z=1),
                      C2.Layer('earth', lambda cv, ctx: S.draw_sphere(cv, EARTH_C, EARTH_R, 'earth', lon0=S.STATION_LON - 0.01 * ctx.a, tilt=S.STATION_TILT,
                                                                     cloud_lon=0.004 * ctx.a), parallax=1.0, z=2)], CAM_C)

def scene_c(cv, ctx):
    a = ctx.a; cv.clear(T.BG); s = LAY_C.render(cv, ctx)
    st = C2.Camera2D.project(s, STATION, 1.0); mc = C2.Camera2D.project(s, MOON_C_W, MOON_C_P); mr = MOON_C_R * s.zoom ** MOON_C_P
    pin = ease_out_back(seg(a, 1.2, 1.75))
    if pin > 0:                                                      # station pin with a small observatory icon (Codex B4 art, scaled)
        from uemotion.camera import T3, S3
        h = 80 * pin; ic = _station_icon(); k = h / ic.size[1]
        cv.line(st, (st[0], st[1] - 30 * pin), T.WHITE, width=3, alpha=pin)
        with cv.xf(T3(st[0] - ic.size[0] * k / 2, st[1] - 30 * pin - h) @ S3(k)): cv.blit_image(ic, alpha=min(1, pin))
        cv.circle(st, 9, fill=T.WARM, alpha=min(1, pin))
    S.not_to_scale_mark(cv, alpha=smoothstep(seg(a, 3.0, 3.6)))
    overlays(cv, st, mc, mr, a); return {}

# ---------------------------------------------------------------- checks
def _speed(fn, a): return math.hypot(*np.subtract(fn(a + 1 / 30), fn(a))) * 30

def check_all(out_dir, results):
    checks = []
    for name, cam, pts in (('A', CAM_A, lambda a: ground_points(CAM_A, a)), ('B', CAM_B, lambda a: ground_points(CAM_B, a)),
                           ('C', CAM_C, None)):
        if pts is None:
            def pts(a, cam=cam):
                s = cam.state(a); return (C2.Camera2D.project(s, STATION, 1), C2.Camera2D.project(s, MOON_C_W, MOON_C_P), MOON_C_R * s.zoom ** MOON_C_P)
        ap0, mc0, mr0 = pts(0.0); ap1, mc1, mr1 = pts(N_MOON + 0.3)
        on = lambda p, m=0: 0 + m <= p[0] <= 1080 - m and 0 + m <= p[1] <= 1920 - m
        checks.append(('%s: at "moon." (%.2f s) the Moon AND the aperture/station are both on screen' % (name, N_MOON), on(mc1, mr1) and on(ap1, 40), 'moon %s r%.0f, aperture %s' % (tuple(round(v) for v in mc1), mr1, tuple(round(v) for v in ap1))))
        checks.append(('%s: frame 0 shows the subject (aperture/station on screen)' % name, on(ap0, 0), 'aperture at t=0 %s; Moon on screen at t=0: %s' % (tuple(round(v) for v in ap0), on(mc0, 0))))
        if name == 'A':      # V3: the camera keeps a slow purposeful drift through 2-4 s; check there is no static hold instead
            sp = [_speed(lambda a: pts(a)[1], x) + _speed(lambda a: pts(a)[0], x) for x in np.arange(2.0, 4.0, 0.1)]
            checks.append(('A (V3): no static hold 2.0-4.0 s (Moon/aperture keep moving on screen)', min(sp) > 3, 'min screen speed %.1f u/s' % min(sp)))
        else:
            v_after = _speed(lambda a: pts(a)[1], N_MOON + 0.3); v_before = _speed(lambda a: pts(a)[1], N_MOON - 0.9)
            checks.append(('%s: camera move lands on "moon." (Moon screen speed falls)' % name, v_after < 0.4 * v_before + 5, 'before %.0f u/s, 0.3 s after %.0f u/s' % (v_before, v_after)))
        checks.append(('%s: Moon readable at phone size (screen radius >= 45 units at "moon.")' % name, mr1 >= 45, 'r = %.0f' % mr1))
    for lay, nm in ((LAY_A, 'A'), (LAY_B, 'B'), (LAY_C, 'C')):
        rep = lay.assert_overscan(0, DUR); checks.append(('%s: layer overscan (assert)' % nm, True, 'min margin %.0f' % min(rep.values())))
    checks.append(('pulse travels in real time: arrival - launch = 1.28 s and lands on "reflector" (%.2f)' % N_REFL, abs(T_ARRIVE - N_REFL) < 0.15, 'launch %.2f, arrive %.2f' % (T_LAUNCH, T_ARRIVE)))
    checks.append(('no premature answer: no pulse before "fire" (%.2f)' % N_FIRE, T_LAUNCH >= N_FIRE, 'launch %.2f' % T_LAUNCH))
    checks.append(('the wrong idea (cone) is gone before "To ask" (%.2f)' % N_TO, N_UP + 0.50 <= N_TO, 'cone off at %.2f' % (N_UP + 0.5)))
    checks.append(('telescope drive has no overshoot (lean is monotonic while slewing)', all(LEAN(t) >= LEAN(t + 0.02) - 1e-9 for t in np.arange(0, 2.8, 0.02)), 'lean %.0f -> %.0f deg' % (LEAN(0), LEAN(2.8))))
    return checks

INFO = dict(
    title='OPENING candidates A/B/C (narration 0 - %.1f s)' % DUR,
    beats='B01-B04: "Imagine pointing a powerful laser at the moon. / Not to light it up. / To ask it a question. / You fire a pulse at a reflector"',
    expected=('A: dome and Moon both visible from frame 0; the slit opens and the telescope rises while the camera tilts toward the Moon, landing on "moon". '
              'B: starts inside the opening slit on the telescope, pulls back to dome + Moon by "moon". C: Earth limb + Moon; push to the station pin, '
              'pull up to the Moon. All: on "Not to light it up" a floodlight cone washes the Moon, a red NO mark appears and the cone collapses; on '
              '"To ask it a question" brackets lock on the Moon; on "fire" one pulse leaves and reaches the Moon 1.28 s later, on "reflector".'),
    science=('No continuous beam to the Moon is drawn (the cone is the marked WRONG idea). The pulse is a symbol, drawn as a dot, moving in REAL time '
             '(1.28 s Earth-Moon, C02). Observatory = generic illustration (Codex B4M/B4L/B4L2/B4P), never captioned as Apache Point. Moon = LRO colour map; '
             'Earth = Blue Marble. C carries NOT TO SCALE.'),
)

def specs():
    S.preload_real()
    cues = {'moon': N_MOON + 0.3, 'not_light': N_UP - 0.15, 'question': N_QEND, 'fire': T_LAUNCH + 0.4, 'arrive': T_ARRIVE + 0.1}
    return [ClipSpec('OPEN', 'OPEN_A_ground_cinematic', 0.0, DUR, scene_ground(LAY_A, CAM_A), captions=True, blur=(3, 0.5), cues=cues),
            ClipSpec('OPEN', 'OPEN_B_closeup_to_wide', 0.0, DUR, scene_ground(LAY_B, CAM_B), captions=True, blur=(3, 0.5), cues=cues),
            ClipSpec('OPEN', 'OPEN_C_earth_to_moon', 0.0, DUR, scene_c, captions=True, blur=(3, 0.5), cues=cues)]
