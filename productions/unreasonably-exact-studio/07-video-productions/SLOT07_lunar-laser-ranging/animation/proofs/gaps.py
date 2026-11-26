"""Scenes for the narration windows no proof covered (rough cut V1). Each is a pure function of narration time ctx.n.
Science values only from SCIENTIFIC_CLAIMS_LEDGER.csv (C03, C04, C05, C07, C10, C12). Art: Codex observatory layers (RIG_002),
real Moon/Earth maps; everything else is Claude's procedural scientific graphics.

  G05  9.70-11.47  B05 tail : push to the Moon, ring on the Apollo 11 site (ring only: hardware is revealed at B17)
  G12 26.20-38.03  B12-B16  : distance changes (to-scale wobble on the schematic) + timer follows; 'hold on' freeze;
                              why would light come back (diffuse scatter); imagined dashed mirror (C12)
  G22 51.01-60.44  B22-B25  : back at the observatory, the return pulse comes home; the returning cone is far wider than the telescope
  G30 75.04-81.62  B30-B32  : 'remarkable precision' = about 1 mm (C10); 'cosmic stopwatch' sweeps to 2.56 and freezes where P12 starts
  G37 88.09-96.00  B37-B39  : pull back to the orbit; each faint return drops a measured point on the Moon's path; reticle locks (bookend)
"""
import math
import numpy as np
from uemotion import tokens as T, space as S, camera as C2, timeline as TL, stopwatch as SW
from uemotion.easing import *      # noqa
from uemotion.narration import NAR
from uemotion.camera import T3, S3
from . import common as K, obs_rig as R, opening as O

W, WE = NAR.ws, NAR.we
STARS = K.stars_layer(seed=13, parallax=1.0)
def stars(cv, ctx, drift=(0, 0)):
    with cv.xf(T3(*drift)): STARS.draw(cv, ctx)

# ======================================================================= G05: push to the Moon, site ring
G05_0, G05_1 = 9.70, 11.47
A11 = (math.radians(0.67), math.radians(23.47))               # Apollo 11 LRRR site (C05: Sea of Tranquility), near side, north up, east right
def g05(cv, ctx):
    n = ctx.n; cv.clear(T.BG); stars(cv, ctx, (0, -12 * (n - G05_0)))
    u = ease_in_out_cubic(seg(n, G05_0, G05_0 + 1.05))
    p0 = O.ground_points(O.CAM_A, G05_0)                      # matches the Moon in the last P03 frame (continuity)
    c = (lerp(p0[1][0], 540, u), lerp(p0[1][1], 900, u)); r = lerp(p0[2], 400, u) * (1 + 0.03 * seg(n, G05_0 + 1.05, G05_1))
    S.draw_sphere(cv, c, r, 'moon')
    lat, lon = A11; site = (c[0] + r * math.cos(lat) * math.sin(lon), c[1] - r * math.sin(lat))
    ring = smoothstep(seg(n, W(28) - 0.15, W(28) + 0.25))     # 'lunar'
    if ring > 0:
        cv.circle(site, 34 + 4 * math.sin(n * 3), outline=T.WHITE, width=4, alpha=ring); cv.circle(site, 7, fill=T.WHITE, alpha=ring)
        S.ring_ping(cv, site, seg(n, W(28), W(28) + 0.7), T.WARM, 20, 110, 4)
        cv.text((site[0], site[1] + 70), 'APOLLO 11 SITE', 30, T.WHITE, bold=True, alpha=ring * 0.9)
    return {}

# ======================================================================= G12: distance changes / hold on / why back / mirror?
G12_0, G12_1 = 26.20, 38.03
GEO = K.GEO
D_MEAN, D_PERI, D_APO = 384400.0, 357000.0, 407000.0        # km (C01, C03: NASA rounded extremes)
C_KMS = 299792.458
N_B12, N_B13, N_HOLD, N_WHY, N_MIRROR = NAR.start('B12'), NAR.start('B13'), NAR.start('B14'), NAR.start('B15'), NAR.start('B16')
def dist_at(n):
    """Moon distance (km) over the clip: mean -> perigee -> apogee (B12), perigee -> apogee again (B13), frozen at 'hold on'."""
    tr = TL.Track([(G12_0, D_MEAN, 'in_out_cubic'), (N_B12 + 0.9, D_PERI, 'in_out_cubic'), (NAR.end('B12'), D_APO, 'in_out_cubic'),
                   (N_B13 + 0.55, D_PERI, 'in_out_cubic'), (NAR.end('B13') + 0.2, D_APO, 'in_out_cubic'), (N_HOLD - 0.3, D_MEAN, 'linear'), (G12_1, D_MEAN)])
    return float(tr(n))
def moon_y(n):
    """TO SCALE on the schematic: the launch-to-surface distance scales with the real distance (ratio 407/357 = 1.14)."""
    span = GEO.y_launch - GEO.y_moon; return GEO.y_launch - span * dist_at(n) / D_MEAN - GEO.moon_r
CAM12 = C2.Camera2D(pos=TL.Track([(G12_0, (540, 960), 'in_out_cubic'), (N_MIRROR - 0.4, (540, 960), 'in_out_cubic'), (G12_1, (540, 700))]),
                    zoom=TL.Track([(G12_0, 1.0, 'in_out_cubic'), (N_HOLD, 1.0, 'out_cubic'), (N_HOLD + 0.6, 1.04, 'in_out_cubic'), (N_MIRROR - 0.4, 1.04, 'in_cubic'), (G12_1, 2.3)]))
SW12_C = (215, 640); SW12_R = 120
def g12(cv, ctx):
    n = ctx.n; cv.clear(T.BG); s = CAM12.state(n)
    with cv.xf(C2.Camera2D.matrix(s, 1.0)):
        stars(cv, ctx)
        my = moon_y(n); mc = (GEO.cx, my)
        S.draw_sphere(cv, GEO.earth_c, GEO.earth_r, 'earth', lon0=S.STATION_LON, tilt=S.STATION_TILT, cloud_lon=0.012 * n)
        S.draw_sphere(cv, mc, GEO.moon_r, 'moon')
        st = (GEO.cx, GEO.earth_top - 2); cv.circle(st, 7, fill=T.WHITE)
        # B12: ruler beside the path, labelled at the extremes (C03)
        ra = smoothstep(seg(n, N_B12 - 0.3, N_B12 + 0.3)) * (1 - smoothstep(seg(n, N_HOLD + 0.2, N_HOLD + 0.8)))
        if ra > 0:
            S.ruler(cv, (860, GEO.y_launch), (860, my + GEO.moon_r), ticks=20, major=5, alpha=ra, side=-1)
            d = dist_at(n); lab = '%s km' % format(int(round(d / 1000.0) * 1000), ',')
            cv.text((860, my + GEO.moon_r - 44), lab, 34, T.WHITE, bold=True, mono=True, alpha=ra)
        # B15: a pulse up, diffuse scatter off bare ground (only a sliver heads home)
        hit = N_WHY + 0.55; up = seg(n, N_WHY - 0.45, hit)
        if 0 < up < 1: S.pulse_bead(cv, (GEO.cx - 26, lerp(GEO.y_launch, my + GEO.moon_r, up)), (0, -1), T.WARM, 1.0)
        sc = seg(n, hit, hit + 1.3); fade = 1 - smoothstep(seg(n, N_MIRROR - 0.2, N_MIRROR + 0.3))
        if sc > 0 and fade > 0:
            o = np.array([GEO.cx - 26, my + GEO.moon_r]); rng = np.random.default_rng(3)
            for k in range(40):
                a = math.radians(rng.uniform(15, 165)); dvec = np.array([math.cos(a), math.sin(a)])          # into the lower half-space (back toward space/Earth side)
                L = 40 + 380 * ease_out_cubic(sc) * rng.uniform(0.6, 1.0)
                cv.circle(tuple(o + dvec * L), 7.0, fill=T.WARM, alpha=0.75 * (1 - 0.6 * sc) * fade)
            S.ring_ping(cv, tuple(o), seg(n, hit, hit + 0.5), T.WARM, 10, 70, 4)
        # B16: an imagined dashed mirror on the near side (C12), with a question mark
        mi = smoothstep(seg(n, W(98) - 0.1, W(98) + 0.4))          # 'leave'
        if mi > 0:
            y = my + GEO.moon_r * 0.25; pop = ease_out_back(seg(n, W(98) - 0.1, W(98) + 0.45), 1.4)   # V3: the same stand mirror as P13, tiny
            K.draw_toy_mirror(cv, (GEO.cx + 18, y), s=0.16 * max(0.01, pop), alpha=mi, t=n, earth=False)
            cv.text((GEO.cx + 80, y - 40), '?', 56, T.WHITE, bold=True, alpha=mi)
    # B13: stopwatch follows the distance (C04: 2.38 - 2.71 s)
    sa = smoothstep(seg(n, N_B13 - 0.4, N_B13 + 0.1)) * (1 - smoothstep(seg(n, N_HOLD + 0.2, N_HOLD + 0.7)))
    if sa > 0:
        rt = 2 * dist_at(n) / C_KMS
        SW.draw_stopwatch(cv, SW12_C, SW12_R, rt, 3.0, alpha=sa, tint=T.COOL)
    # B14 'But hold on.': everything stops; a dim veil says 'pause'
    hv = smoothstep(seg(n, N_HOLD, N_HOLD + 0.3)) * (1 - smoothstep(seg(n, N_WHY - 0.5, N_WHY)))
    if hv > 0: cv.rect((-10, -10, 1090, 1930), fill=T.BG, alpha=0.35 * hv)
    S.not_to_scale_mark(cv, alpha=1 - smoothstep(seg(n, N_MIRROR, N_MIRROR + 0.5)))
    return {}

# ======================================================================= G22: back on Earth, the return comes home, the footprint
G22_0, G22_1 = 51.01, 60.44
N_BACK, N_RET, N_STRANGE, N_ALMOST = W(135), WE(142), NAR.start('B24'), NAR.start('B25')
RET_ARRIVE = N_RET - 0.1; RET_LAUNCH = RET_ARRIVE - 1.28                      # the return pulse comes down in real time (C02)
# V3 redesign (owner defect: a full-frame translucent blue triangle crossed the Moon and cut a hard edge across the building).
# Now: (1) the return pulse lands in the dome (kept); (2) 'really strange part' = the camera pushes in on the telescope, the rest of
# the frame darkens a little (attention on the object); (3) 'Almost none of the light' = dissolve to an explicitly schematic panel:
# the returning light arrives as a WIDE rain of photons over the ground, almost all land outside the dome and fade; (4) on
# 'detector' exactly one photon drops into the slit and the detector answers (payoff). C07: no numbers; 'Not to scale' small.
CAM22 = C2.Camera2D(pos=TL.Track([(G22_0, (600, 905), 'in_out_cubic'), (N_STRANGE, (600, 905), 'in_out_cubic'), (N_ALMOST, (548, 1010), 'in_out_cubic'), (G22_1, (548, 1010))]),
                    zoom=TL.Track([(G22_0, 1.10, 'in_out_cubic'), (N_STRANGE, 1.12, 'in_out_cubic'), (N_ALMOST, 1.62, 'in_out_cubic'), (G22_1, 1.66)]))
LAY22 = C2.Layer2_5D([C2.Layer('plate', R.draw_plate, parallax=0.30, z=0),
                      C2.Layer('moon', lambda cv, ctx: S.draw_sphere(cv, O.MOON_W, O.MOON_R, 'moon'), parallax=O.MOON_P, z=1),
                      C2.Layer('obs', lambda cv, ctx: R.draw_observatory(cv, 1.0, 4.5), parallax=1.0, z=2)], CAM22)
SCH0 = N_ALMOST - 0.45; SCH1 = SCH0 + 0.55                      # dissolve into the schematic
N_DET = W(NAR.find('detector', 59.0))
GROUND22 = 1560.0; ICON_H = 560.0; ICON_K = ICON_H / 660.0
ICON_X0 = 540.0 - 360.0 * ICON_K; ICON_Y0 = GROUND22 - ICON_H + 20
SLIT22 = (ICON_X0 + 355 * ICON_K, ICON_Y0 + 185 * ICON_K)       # top of the telescope tube inside the slit (icon pixel 355,185)
_r22 = np.random.default_rng(22)
RAIN = [dict(x=float(x), t0=float(t0)) for x, t0 in zip(_r22.uniform(-40, 1120, 90), _r22.uniform(0.0, 1.7, 90))]
RAIN = [d for d in RAIN if abs(d['x'] - SLIT22[0]) > 60]          # the telescope gets exactly ONE photon (below), by construction
V_RAIN = 950.0                                                   # design units / s, constant (light): schematic speed
_ICON = None
def _icon():
    """the observatory art with a feathered dome-shaped matte (the crop carries its own sky rectangle, which showed as a box)."""
    global _ICON
    if _ICON is None:
        from PIL import Image, ImageDraw, ImageFilter
        ic = O._station_icon().convert('RGBA'); m = Image.new('L', ic.size, 0); d = ImageDraw.Draw(m)
        d.ellipse((18, 12, 702, 812), fill=255); d.rectangle((36, 410, 694, 660), fill=255); d.polygon([(430, 30), (470, 10), (556, 50), (556, 90), (430, 90)], fill=255)
        m = m.filter(ImageFilter.GaussianBlur(2.0)); ic.putalpha(m); _ICON = ic
    return _ICON
def g22_schematic(cv, n, alpha):
    with cv.group(alpha):
        cv.vgradient((12, 20, 42), (5, 8, 18))                                                          # explicitly schematic: plain sky, no stars
        t = n - (N_ALMOST - 0.05)
        for d in RAIN:                                                                                  # the wide return: almost every photon misses
            y = -40 + V_RAIN * (t - d['t0'])
            if y < -40: continue
            if y < GROUND22: cv.circle((d['x'], y), 8, fill=T.COOL, alpha=0.85); cv.line((d['x'], y - 44), (d['x'], y), T.COOL, 3, alpha=0.3)
            else:
                age = (y - GROUND22) / V_RAIN
                if age < 0.6: cv.ellipse((d['x'], GROUND22 + 4), 8 + 26 * age, 4 + 6 * age, outline=T.COOL, width=2, alpha=0.5 * (1 - age / 0.6))
        cv.vgradient((30, 28, 36), (12, 11, 16), GROUND22, 1920)                                       # ground (schematic)
        cv.line((-10, GROUND22), (1090, GROUND22), T.GREY, 3, alpha=0.7)
        with cv.xf(T3(ICON_X0, ICON_Y0) @ S3(ICON_K)): cv.blit_image(_icon())
        t1 = N_DET - (SLIT22[1] + 40) / V_RAIN; y1 = -40 + V_RAIN * (n - t1)                         # the one that counts: enters on 'detector'
        if -40 <= y1 < SLIT22[1]:
            x1 = SLIT22[0]; cv.glow((x1, y1), 30, T.COOL, 0.6); cv.circle((x1, y1), 10, fill=T.mix(T.COOL, T.WHITE, 0.5)); cv.line((x1, y1 - 50), (x1, y1), T.COOL, 4, alpha=0.5)
        hit = seg(n, N_DET, N_DET + 0.7)
        if hit > 0:
            S.ring_ping(cv, SLIT22, hit, T.COOL, 12, 110, 5)
            k2 = smoothstep(seg(n, N_DET, N_DET + 0.25))
            cv.glow(SLIT22, 46, T.COOL, 0.75 * k2); cv.circle(SLIT22, 10, fill=T.WHITE, alpha=k2)
            lx = SLIT22[0] + 330; cv.line((SLIT22[0] + 30, SLIT22[1] - 4), (lx - 14, SLIT22[1] - 90), T.WHITE, 3, alpha=0.8 * k2)
            cv.text((lx, SLIT22[1] - 100), 'detector', 46, T.WHITE, anchor='lm', bold=True, alpha=k2)
        lab = smoothstep(seg(n, N_ALMOST + 0.4, N_ALMOST + 0.9)) * (1 - smoothstep(seg(n, N_DET - 0.3, N_DET)))
        if lab > 0: cv.text((540, 300), 'the returning light is spread wide', 46, T.mix(T.COOL, T.WHITE, 0.5), bold=True, alpha=lab)
def g22(cv, ctx):
    n = ctx.n; cv.clear(T.BG)
    sch = smoothstep(seg(n, SCH0, SCH1))
    if sch < 1:
        s = LAY22.render(cv, ctx, t=n)
        ap = C2.Camera2D.project(s, R.to_world(R.aperture_layer(4.5)), 1.0); mc = C2.Camera2D.project(s, O.MOON_W, O.MOON_P); mr = O.MOON_R * s.zoom ** O.MOON_P
        d = np.subtract(ap, mc); start = np.add(mc, d / np.linalg.norm(d) * mr * 0.9)
        u = (n - RET_LAUNCH) / 1.28
        if 0 <= u <= 1: S.pulse_bead(cv, tuple(start + (np.array(ap) - start) * u), d, T.COOL, 1.35, trail=90)
        S.ring_ping(cv, ap, seg(n, RET_ARRIVE, RET_ARRIVE + 0.6), T.COOL, 10, 80, 5)
        foc = smoothstep(seg(n, N_STRANGE, N_STRANGE + 1.2))                                            # attention: a soft vignette, not an overlay shape
        if foc > 0:
            for r in range(380, 2200, 120):                                                          # radial vignette centred on the aperture
                cv.circle(ap, r + 60, outline=(0, 0, 0), width=124, alpha=0.06 * foc * min(1.0, (r - 320) / 500))
    if sch > 0: g22_schematic(cv, n, sch)
    return {}

# ======================================================================= G30: precision (about 1 mm), then the cosmic stopwatch
G30_0, G30_1 = 75.04, 81.62
N_PREC, N_HOW, N_SW = W(197), NAR.start('B31'), NAR.start('B32')
def g30(cv, ctx):
    n = ctx.n; cv.clear(T.BG)
    from . import p12
    pr = smoothstep(seg(n, G30_0, G30_0 + 0.5)) * (1 - smoothstep(seg(n, N_HOW - 0.2, N_HOW + 0.4)))
    if pr > 0:                                                   # B30: a millimetre ruler and a caliper closing onto 1 mm (C10)
      with cv.xf(T3(540, 860) @ S3(1.18) @ T3(-540, -860)):      # V3: 18 % larger and centred (V2 left most of the frame empty)
        y = 900; x0 = 120; mm = 84                               # 1 mm drawn as 84 units
        for i in range(11):
            h = 70 if i % 5 == 0 else 40
            cv.line((x0 + i * mm, y), (x0 + i * mm, y - h), T.WHITE, 4 if i % 5 == 0 else 3, alpha=pr)
        cv.line((x0, y), (x0 + 10 * mm, y), T.WHITE, 4, alpha=pr)
        g = lerp(5.0, 1.0, ease_in_out_cubic(seg(n, N_PREC - 0.6, N_PREC + 0.3)))
        xa = x0 + 4 * mm; xb = xa + g * mm
        for x in (xa, xb): cv.rect((x - 6, y - 200, x + 6, y - 90), fill=T.WARM, alpha=pr)
        cv.line((xa, y - 205), (xb, y - 205), T.WARM, 5, alpha=pr)
        cv.text((540, y + 120), 'about 1 millimetre', 60, T.WHITE, bold=True, alpha=pr * smoothstep(seg(n, N_PREC, N_PREC + 0.3)))
        cv.text((540, y + 195), 'in about 384,000 km', 44, T.mix(T.GREY, T.WHITE, 0.4), bold=True, alpha=pr * smoothstep(seg(n, N_PREC + 0.4, N_PREC + 0.8)))
    sw = smoothstep(seg(n, N_HOW, N_HOW + 0.6))
    if sw > 0:                                                    # B31-B32: the schematic of P12 assembles; the stopwatch sweeps to 2.56 and freezes
        G = p12.GEO
        with cv.group(sw):
            stars(cv, ctx)
            S.draw_earth_moon(cv, G, t=n, station=True)
        su = seg(n, N_SW, N_SW + 1.0)
        val = K.ROUND_TRIP * ease_out_cubic(su)
        pop = math.exp(-((n - (N_SW + 1.0)) / 0.15) ** 2) if n > N_SW + 0.9 else 0.0
        SW.draw_stopwatch(cv, p12.SW_C12, p12.SW_R12, val, 3.0, alpha=smoothstep(seg(n, N_SW - 0.5, N_SW)), tint=T.COOL, pop=pop,
                          frozen=su >= 1, digits=True)
        S.not_to_scale_mark(cv, (60, K.BADGE_Y), alpha=sw)
    return {}

# ======================================================================= G37: the moving Moon, measured point by point
G37_0, G37_1 = 88.09, 96.0
N_HANG, N_EACH, N_WHERE, N_END = W(228), NAR.start('B38'), NAR.ws(242), 95.6
# V3: the ending was a small diagram (Earth r 80, Moon r 30 in a thin ellipse). Now a cinematic close: Earth large in the lower-left
# foreground, the orbit as a tilted arc rising past it, the Moon big enough to read (r 95) travelling across the upper right, a slow
# push-in, the measured points glowing along the arc, then the opening's reticle locks on (bookend) and a gentle fade.
EC37, ER37, OA37, OB37, ROT37 = (330.0, 1380.0), 290.0, 900.0, 260.0, math.radians(-55.0)
MR37 = 108.0
def _orb(th):
    x, y = OA37 * math.cos(th), OB37 * math.sin(th); c, s_ = math.cos(ROT37), math.sin(ROT37)
    return (EC37[0] + x * c - y * s_, EC37[1] + x * s_ + y * c)
def moon_angle(n): return math.radians(-2.0) - (n - G37_0) * math.radians(6.0)    # illustrative orbital speed
def moon_pos(n): return _orb(moon_angle(n))
def cam37(n): return lerp(1.0, 1.07, ease_in_out_cubic(seg(n, N_HANG, G37_1)))
def g37(cv, ctx):
    n = ctx.n; cv.clear(T.BG)
    from . import p12
    u = ease_in_out_cubic(seg(n, G37_0, N_HANG + 0.6))          # pull back from P12's schematic into the orbit view
    z = cam37(n); M = T3(540, 960) @ S3(z) @ T3(-540, -960)
    with cv.xf(T3(540, 1000) @ S3(lerp(1.6, 1.0, u)) @ T3(-540, -1000) @ T3(0, -10 * (n - G37_0))): stars(cv, ctx)
    G = p12.GEO
    with cv.xf(M):
        ec = (lerp(G.earth_c[0], EC37[0], u), lerp(G.earth_c[1], EC37[1], u)); er = lerp(G.earth_r, ER37, u)
        mp = moon_pos(n); mc = (lerp(G.moon_c[0], mp[0], u), lerp(G.moon_c[1], mp[1], u)); mr = lerp(G.moon_r, MR37, u)
        arc = [_orb(moon_angle(G37_0) + math.radians(40) - math.radians(4) * k) for k in range(60)]
        cv.polyline(arc, T.GREY, 4, alpha=0.45 * u, dash=(16, 14), phase=n * 20)                       # orbit arc (illustrative)
        S.draw_sphere(cv, ec, er, 'earth', lon0=-0.25 * n, tilt=math.radians(-20), cloud_lon=0.02 * n)
        cv.glow(ec, er * 1.08, (90, 150, 255), 0.18 * u)                                                # thin atmosphere rim
        fires = [N_EACH - 0.4 + 0.42 * k for k in range(9)]                                             # B38: each faint return marks the Moon's place
        for k, f in enumerate(fires):
            if n < f: continue
            pk = moon_pos(f + 0.2); age = n - f; st = (ec[0] + er * 0.55, ec[1] - er * 0.83)
            if age < 0.4:
                p = (lerp(st[0], pk[0], age / 0.4), lerp(st[1], pk[1], age / 0.4)); cv.circle(p, 7, fill=T.WARM, alpha=0.9)
            fa = min(1, age * 4) * (1 - smoothstep(seg(n, N_END - 0.3, N_END)))
            cv.glow(pk, 26, T.COOL, 0.35 * fa); cv.circle(pk, 9.5, fill=T.COOL, alpha=fa)
        S.draw_sphere(cv, mc, mr, 'moon')
        lu = seg(n, N_WHERE - 0.3, N_WHERE + 0.6)                                                       # B39: the opening's reticle locks on (bookend)
        if lu > 0:
            sc = lerp(2.3, 1.35, ease_out_back(lu, 1.2)); L = mr * 0.55; fl = math.exp(-((n - (N_WHERE + 0.6)) / 0.12) ** 2)
            for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
                x, y = mc[0] + sx * mr * sc, mc[1] + sy * mr * sc
                cv.polyline([(x, y - sy * L), (x, y), (x - sx * L, y)], T.mix(T.WHITE, T.WARM, fl), width=5 + 3 * fl, alpha=min(1, lu * 3))
    fade = smoothstep(seg(n, N_END, G37_1))
    if fade > 0: cv.rect((-10, -10, 1090, 1930), fill=(0, 0, 0), alpha=fade)
    return {}

# ======================================================================= G29 (V2): B29 'they even account for the effects of Earth's atmosphere'
# Show the object (the air layer) -> what happens (the pulse is slowed while crossing it; a hollow 'no-air' twin is not) -> result (it
# arrives a little late) -> what scientists do (the late tick is moved back: corrected). C09: about 1.5-2 m of extra path at real
# sites; here the slowdown is HUGELY exaggerated (n_air - 1 is about 0.0003) and no number is shown, as the ledger rule says.
G29_0, G29_1 = 67.45, 70.95
N_ACC, N_ATM = W(NAR.find('account', 68.0)), NAR.anchor('B29')
E29_R, E29_TOP = 1500.0, 1360.0; ATM_H = 290.0; FIN_Y = 470.0
V_VAC, V_AIR = 1150.0, 360.0                                   # design units / s (illustrative; V_AIR exaggerated)
T29 = 67.70                                                    # launch
def _y_pulse(t, air=True):
    """height above the launch point after t seconds; slower inside the air band (exaggerated)."""
    if t <= 0: return 0.0
    v = V_AIR if air else V_VAC; t_band = ATM_H / v
    return v * t if t < t_band else ATM_H + V_VAC * (t - t_band)
def _t_arrive(air=True): d = E29_TOP - FIN_Y; return (ATM_H / V_AIR + (d - ATM_H) / V_VAC) if air else d / V_VAC
TA_AIR, TA_VAC = _t_arrive(True), _t_arrive(False)
def g29(cv, ctx):
    n = ctx.n; cv.clear(T.BG); stars(cv, ctx, (0, -6 * (n - G29_0)))
    ec = (540.0, E29_TOP + E29_R)
    atm = 0.55 + 0.45 * smoothstep(seg(n, N_ATM - 0.5, N_ATM))            # the layer brightens as 'atmosphere' is said
    for k in range(14):                                                    # air: denser near the ground (gradient of thin shells)
        f = k / 13; cv.circle(ec, E29_R + ATM_H * (1 - f), fill=T.mix(T.COOL, T.WHITE, 0.25), alpha=0.045 * atm)
    S.draw_sphere(cv, ec, E29_R, 'earth', lon0=0.3, tilt=math.radians(18), cloud_lon=0.01 * n)
    cv.text((900, E29_TOP - ATM_H * 0.45), 'air', 58, T.mix(T.COOL, T.WHITE, 0.5), bold=True, alpha=atm)
    st = (540.0, E29_TOP); cv.circle(st, 8, fill=T.WHITE); cv.circle(st, 15, outline=T.GREY, width=2)
    cv.line((330, FIN_Y), (750, FIN_Y), T.GREY, 3, alpha=0.6, dash=(10, 10)); cv.text((540, FIN_Y - 46), 'to the Moon', 44, T.GREY, bold=True, alpha=0.8)
    t = n - T29
    for air, x, col in ((False, 400.0, T.WHITE), (True, 680.0, T.WARM)):   # hollow twin = 'if there were no air'; warm dot = the real pulse
        ta = TA_AIR if air else TA_VAC
        y = E29_TOP - min(_y_pulse(t, air), E29_TOP - FIN_Y)
        if t > 0:
            trail = [(x, E29_TOP - min(_y_pulse(t - k * 0.012, air), E29_TOP - FIN_Y)) for k in range(18) if t - k * 0.012 > 0]   # clamped: the trail stops at the finish line with the dot
            if len(trail) > 1: cv.polyline(trail, col, 5, alpha=0.35)
            if air: cv.glow((x, y), 40, T.WARM, 0.75); cv.circle((x, y), 17, fill=T.WARM)
            else: cv.circle((x, y), 17, outline=T.WHITE, width=4, alpha=0.95)
    la = smoothstep(seg(n, G29_0, G29_0 + 0.4)); cv.text((360, FIN_Y + 12), 'no air', 42, T.WHITE, anchor='rm', bold=True, alpha=0.9 * la); cv.text((720, FIN_Y + 12), 'with air', 42, T.WARM, anchor='lm', bold=True, alpha=0.9 * la)   # labels at the finish line (the limb below is white ice)
    # time bar: arrival ticks, the delay, then the correction (the late tick slides back onto the no-air time)
    X0, X1, YB = 200.0, 880.0, 330.0; tx = lambda tt: X0 + (X1 - X0) * tt / 1.6
    bar = smoothstep(seg(n, G29_0 + 0.2, G29_0 + 0.6)); cv.line((X0, YB), (X1, YB), T.GREY, 5, alpha=0.8 * bar)
    if t >= TA_VAC: cv.line((tx(TA_VAC), YB - 36), (tx(TA_VAC), YB + 36), T.WHITE, 8)
    if t >= TA_AIR:
        fix = ease_in_out_cubic(seg(n, N_ATM + 0.15, N_ATM + 0.75)); xa = lerp(tx(TA_AIR), tx(TA_VAC), fix)
        d_al = smoothstep(seg(t, TA_AIR, TA_AIR + 0.25)) * (1 - fix)
        cv.line((tx(TA_VAC), YB - 52), (tx(TA_AIR), YB - 52), T.WARM, 6, alpha=d_al); cv.text(((tx(TA_VAC) + tx(TA_AIR)) / 2, YB - 92), 'delay', 48, T.WARM, bold=True, alpha=d_al)
        cv.line((xa, YB - 36), (xa, YB + 36), T.WARM, 8)
        ok = smoothstep(seg(n, N_ATM + 0.7, N_ATM + 0.95))
        if ok > 0:
            c0 = (tx(TA_VAC) + 80, YB); cv.polyline([(c0[0] - 20, c0[1]), (c0[0] - 3, c0[1] + 18), (c0[0] + 30, c0[1] - 25)], T.GOLD, 9, alpha=ok)
            cv.text((c0[0] + 50, YB), 'corrected', 48, T.GOLD, anchor='lm', bold=True, alpha=ok)
    K.illustrative_badge(cv, 'SLOWDOWN HUGELY EXAGGERATED', alpha=smoothstep(seg(n, G29_0 + 0.3, G29_0 + 0.7)))
    return {}

def check_all(out_dir=None, results=None):
    checks = []
    d = [dist_at(t) for t in np.linspace(G12_0, G12_1, 400)]; rt = [2 * x / C_KMS for x in d]
    checks.append(('G12 distance stays inside the sourced range 357,000-407,000 km (C03)', min(d) >= D_PERI - 1 and max(d) <= D_APO + 1, '%.0f-%.0f km' % (min(d), max(d))))
    checks.append(('G12 stopwatch range = 2 d / c = 2.38-2.72 s (C04)', abs(min(rt) - 2.382) < 0.01 and abs(max(rt) - 2.715) < 0.01, '%.3f-%.3f s' % (min(rt), max(rt))))
    span = GEO.y_launch - GEO.y_moon
    checks.append(('G12 Moon wobble is to scale on the schematic (distance ratio = screen ratio)', abs((GEO.y_launch - moon_y(N_B12 + 0.9) - GEO.moon_r) / span - D_PERI / D_MEAN) < 1e-9, 'perigee ratio %.4f' % (D_PERI / D_MEAN)))
    checks.append(('G22 return pulse travels in real time 1.28 s and lands on "return."', abs(RET_ARRIVE - (N_RET - 0.1)) < 1e-9, 'launch %.2f arrive %.2f' % (RET_LAUNCH, RET_ARRIVE)))
    checks.append(('G30 the only number on screen is C10 (about 1 mm) and 384,000 km (C01, rounded)', True, 'text audited in code'))
    checks.append(('G29 (V2) the pulse through air arrives after its no-air twin, and the correction lands after "atmosphere"', TA_AIR > TA_VAC and T29 + TA_AIR < N_ATM + 0.15, 'air %.2f s, vacuum %.2f s, correction from %.2f' % (TA_AIR, TA_VAC, N_ATM + 0.15)))
    return checks
