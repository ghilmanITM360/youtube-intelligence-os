"""Shared building blocks for the proof scenes (not part of the reusable uemotion package)."""
import math
import numpy as np
from uemotion import tokens as T, space as S, camera as C
from uemotion.easing import *      # noqa
from uemotion.timeline import Track, phase

BADGE_Y = 150          # V2: was 104; 200 collided with the P08 stopwatch; 150 is inside the mobile top safe area (platform UI covers ~8%)

def conceptual_badge(cv, alpha=1.0, text='CONCEPTUAL'):
    S.badge(cv, (60, BADGE_Y), text, 30, T.GREY, alpha=alpha)

def illustrative_badge(cv, text='ILLUSTRATIVE', alpha=1.0, xy=(60, BADGE_Y)):
    return S.badge(cv, xy, text, 30, T.GOLD, alpha=alpha)

def space_background(cv, extent=(-400, -600, 1480, 2520), seed=5):
    from uemotion.camera import starfield
    cv.clear(T.BG); starfield(extent, seed=seed)(cv, None)

def aim_ray(cube, face_idx, frac, angle_deg, y_start):
    """x of the start point on y=y_start so that a ray at angle_deg (up, + = leaning right) strikes face `face_idx`
    at fraction `frac` of its length."""
    q0, q1 = cube.faces[face_idx]; hit = q0 + (q1 - q0) * frac
    a = math.radians(angle_deg); d = np.array([math.sin(a), -math.cos(a)]); t = (hit[1] - y_start) / d[1]
    return float((hit - d * t)[0])


# ====================================================================== shared Earth-Moon journey (P08 / P11 / P12 / P13)
from uemotion import camera as C2, stopwatch as SW, timeline as TL
from uemotion.narration import NAR

GEO = S.EarthMoonGeo()                   # Earth bottom / Moon top, animatic layout (non-scale)
ROUND_TRIP = 2.56                        # s, displayed value (C01: mean 2.564 s derived; stopwatch lands on 2.56)
ONE_WAY = ROUND_TRIP / 2                 # 1.28 s (C02)
SW_C = (205, 372); SW_R = 140            # stopwatch placement (top-left; Moon is top-centre)
STAR_EXTENT = (-420, -620, 1500, 2540)

def stars_layer(seed=5, parallax=0.2):
    return C2.Layer('stars', C2.starfield(STAR_EXTENT, seed=seed), parallax=parallax, z=0, extent=STAR_EXTENT)

def journey(m):
    """state of the pulse as a pure function of the MODEL clock m (0..2.56 s). Light moves at constant speed (linear)."""
    if m <= 0: return dict(phase='ready', p=0.0, lane='out', dir=(0, -1))
    if m < ONE_WAY: return dict(phase='out', p=m / ONE_WAY, lane='out', dir=(0, -1))
    if m < ROUND_TRIP: return dict(phase='ret', p=1 - (m - ONE_WAY) / ONE_WAY, lane='ret', dir=(0, 1))
    return dict(phase='done', p=0.0, lane='ret', dir=(0, 1))

def pulse_xy(m):
    j = journey(m); return GEO.pos(j['p'], j['lane'])

def draw_lanes(cv, m, t, out_alpha=1.0, ret_alpha=1.0, arrows=True):
    """flowing dashed lanes drawn up to the pulse (outbound warm, return cool)."""
    j = journey(m)
    if j['phase'] in ('out', 'ret', 'done'):
        po = 1.0 if j['phase'] != 'out' else j['p']
        S.flow_path(cv, [GEO.pos(0, 'out'), GEO.pos(1, 'out')], T.WARM, t=t, progress=po, width=7, head=(j['phase'] == 'out'), alpha=out_alpha * (1.0 if j['phase'] == 'out' else 0.55))
    if j['phase'] in ('ret', 'done'):
        pr = 1 - j['p'] if j['phase'] == 'ret' else 1.0
        S.flow_path(cv, [GEO.pos(1, 'ret'), GEO.pos(0, 'ret')], T.COOL, t=t, progress=pr, width=7, head=(j['phase'] == 'ret'), alpha=ret_alpha)

def draw_pulse(cv, m, size=1.0, alpha=1.0):
    j = journey(m)
    if j['phase'] in ('out', 'ret'):
        S.pulse_bead(cv, GEO.pos(j['p'], j['lane']), j['dir'], T.WARM if j['phase'] == 'out' else T.COOL, size, alpha=alpha)

def target_ring(cv, t, alpha=1.0, pulse=0.0):
    """B05 'reflector' marker: ring and dot only (NOT hardware: the reveal of the real array is B17-B18)."""
    c = (GEO.cx, GEO.y_moon - 34)
    cv.circle(c, 30 + 3 * math.sin(t * 3.0), outline=T.WHITE, width=3.5, alpha=alpha * 0.9)
    cv.circle(c, 6, fill=T.WHITE, alpha=alpha)
    if pulse > 0: S.ring_ping(cv, c, pulse, T.WARM, 30, 110, 4, alpha=alpha)

def top_hud(cv, alpha=1.0, slow=None, slow_alpha=1.0):
    S.not_to_scale_mark(cv, (60, BADGE_Y), alpha=alpha)
    if slow is not None:
        S.badge(cv, (1020, BADGE_Y), 'SLIGHTLY SLOWED DOWN', 26, T.GOLD, alpha=slow_alpha, anchor='rm')


# ====================================================================== V3 shared pieces
def draw_toy_mirror(cv, c, s=1.0, alpha=1.0, t=0.0, earth=True):
    """V3 'Did someone leave a mirror on the moon?': an ordinary household stand mirror (oval glass, brass frame, two splayed legs),
    the intuitive everyday object the viewer imagines. Its glass reflects black sky, a few stars and a small Earth, with one diagonal
    sheen. Origin c = centre of the glass; s = scale (1.0 = 300 x 400 glass). Drawn as the imagined idea (callers fade it)."""
    if alpha <= 0: return
    x, y = c; rx, ry = 150 * s, 200 * s; foot = y + ry + 190 * s
    brass, brass_d = (196, 158, 92), (120, 92, 50)
    for sx in (-1, 1):                                                 # splayed legs + pivot screws (behind the glass)
        cv.line((x + sx * rx * 0.55, y + ry * 0.55), (x + sx * rx * 1.05, foot), brass_d, 14 * s, alpha=alpha)
        cv.line((x + sx * rx * 0.55, y + ry * 0.55), (x + sx * rx * 1.05, foot), brass, 8 * s, alpha=alpha)
        cv.circle((x + sx * (rx + 10 * s), y), 11 * s, fill=brass, outline=brass_d, width=3 * s, alpha=alpha)
    cv.ellipse((x, foot + 6 * s), rx * 1.3, 14 * s, fill=(8, 8, 12), alpha=0.5 * alpha)            # contact shadow
    cv.ellipse((x, y), rx + 18 * s, ry + 18 * s, fill=brass_d, alpha=alpha)
    cv.ellipse((x, y), rx + 12 * s, ry + 12 * s, fill=brass, alpha=alpha)
    cv.ellipse((x, y), rx, ry, fill=(18, 24, 40), alpha=alpha)                                     # glass: reflects the black lunar sky
    rng = np.random.default_rng(7)
    for _ in range(int(26 * s ** 0.5) + 4):
        a = rng.uniform(0, 2 * math.pi); r = math.sqrt(rng.uniform(0, 0.85))
        cv.circle((x + rx * r * math.cos(a), y + ry * r * math.sin(a)), rng.choice([1.6, 2.2, 3.0]) * max(0.6, s), fill=(225, 230, 248), alpha=alpha * rng.uniform(0.4, 0.9))
    if earth: S.draw_sphere(cv, (x - rx * 0.32, y - ry * 0.38), 40 * s, 'earth', alpha=alpha)
    ph = 0.5 + 0.5 * math.sin(t * 1.3)                                                             # slow sheen drift: it is glass
    for k, (w, a) in enumerate(((46, 0.16), (16, 0.22))):
        off = (-40 + 70 * ph + k * 70) * s
        cv.polygon([(x - rx * 0.62 + off, y + ry * 0.55), (x - rx * 0.62 + off + w * s, y + ry * 0.55), (x + rx * 0.25 + off + w * s, y - ry * 0.62), (x + rx * 0.25 + off, y - ry * 0.62)],
                   fill=(235, 242, 255), alpha=alpha * a)
    cv.ellipse((x, y), rx, ry, outline=(240, 220, 170), width=3 * s, alpha=alpha * 0.8)

DATA_PANEL = (70, 190, 1010, 1250)        # V3: P09 and P10 share one framed 'detector log' so the cuts between them read as one display
def data_background(cv, ctx_n=0.0):
    """V3: the data scenes sit in the film's night-sky tone (not flat black) inside a soft framed panel."""
    cv.vgradient((10, 16, 34), (3, 5, 12))
    cv.glow((540, 760), 760, (24, 40, 80), 0.35)
    x0, y0, x1, y1 = DATA_PANEL
    cv.rect((x0, y0, x1, y1), fill=(8, 12, 26), outline=(52, 66, 100), width=3, radius=28, alpha=0.92)
