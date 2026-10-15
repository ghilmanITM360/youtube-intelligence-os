"""V3 procedural limb rigs: redraw the existing characters' limbs (same stroke widths/colours as the SVG parts) from a
joint-level cycle, so both legs / both arms really move. Body, head, face, torso stay the original SVG rasters.

RunRig  (sam-run-warm): two-bone IK legs on a parametric gait (stance 40 % of cycle, toe-off at 40 %, a flight phase
        each step; Hamner, Seth & Delp 2010, J Biomech, PMC2973845), contralateral elbow-bent arm swing, small vertical
        oscillation (lowest at mid-stance). Stance ankle moves back linearly in the body frame at the ground speed.
SwimRig (june-swim-warm): alternating front-crawl arms (catch -> pull -> push -> exit -> above-water recovery, the two
        arms half a cycle apart; Hsu et al. 2024, Sports Health, PMC11531034), elbow flexion in pull and high-elbow
        recovery, gentle shoulder roll, 6-beat flutter kick from the hips, water effects at real hand/foot contacts.
Asset coordinates throughout (the SVG canvas); images are drawn with 3x supersampling.
python3 rig.py  -> self-check (limb lengths, ground contact, slip, loop closure, frame-to-frame continuity)."""
import functools, math
from PIL import Image, ImageDraw

INK, SKIN, SHOE = (41, 42, 45), (237, 195, 162), (244, 234, 220)
SS = 3


def lerp(a, b, u):
    return a + (b - a) * u


def smooth(u):
    u = min(1.0, max(0.0, u))
    return u * u * (3 - 2 * u)


def cyc(keys, p, wrap=0.0):
    """Cyclic cubic (Catmull-Rom style) through [(phase, value)]; the value advances by `wrap` per cycle."""
    p %= 1.0
    ext = [(k[0] - 1, k[1] - wrap) for k in keys[-2:]] + list(keys) + [(k[0] + 1, k[1] + wrap) for k in keys[:2]]
    i = max(j for j in range(1, len(ext) - 2) if ext[j][0] <= p)
    (t0, v0), (t1, v1), (t2, v2), (t3, v3) = ext[i - 1:i + 3]
    m1, m2 = (v2 - v0) / (t2 - t0) * (t2 - t1), (v3 - v1) / (t3 - t1) * (t2 - t1)
    u = (p - t1) / (t2 - t1)
    return ((2 * u ** 3 - 3 * u ** 2 + 1) * v1 + (u ** 3 - 2 * u ** 2 + u) * m1 + (-2 * u ** 3 + 3 * u ** 2) * v2
            + (u ** 3 - u ** 2) * m2)


def ik(h, a, l1, l2, front=1):
    """Knee for hip h, ankle a; the knee bends toward +x*front (anatomically forward). Returns (knee, ankle)."""
    dx, dy = a[0] - h[0], a[1] - h[1]
    d = math.hypot(dx, dy)
    dc = min(max(d, abs(l1 - l2) + 1e-3), l1 + l2 - 1e-3)
    a = (h[0] + dx / d * dc, h[1] + dy / d * dc)                 # (clamp never triggers in the cycles below)
    ang = math.atan2(dy, dx)
    off = math.acos((l1 * l1 + dc * dc - l2 * l2) / (2 * l1 * dc))
    ks = [(h[0] + l1 * math.cos(ang + sg * off), h[1] + l1 * math.sin(ang + sg * off)) for sg in (1, -1)]
    k = min(ks, key=lambda k: dx * (k[1] - h[1]) - dy * (k[0] - h[0]) if front > 0 else
            -(dx * (k[1] - h[1]) - dy * (k[0] - h[0])))
    return k, a


def rot(pt, deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return pt[0] * c - pt[1] * s, pt[0] * s + pt[1] * c


def polar(o, deg, l):
    return o[0] + l * math.cos(math.radians(deg)), o[1] + l * math.sin(math.radians(deg))


class Canvas:
    def __init__(self, w, h, m, k):
        self.m, self.K = m, k * SS
        self.im = Image.new("RGBA", (round((w + 2 * m) * self.K), round((h + 2 * m) * self.K)))
        self.d = ImageDraw.Draw(self.im)

    def P(self, p):
        return (p[0] + self.m) * self.K, (p[1] + self.m) * self.K

    def line(self, pts, w, col):
        q = [self.P(p) for p in pts]
        r = w * self.K / 2
        self.d.line(q, fill=col, width=max(1, round(w * self.K)), joint="curve")
        for x, y in (q[0], q[-1]):
            self.d.ellipse([x - r, y - r, x + r, y + r], fill=col)

    def limb(self, pts, w_out, w_in, col):
        self.line(pts, w_out, INK)
        self.line(pts, w_in, col)

    def poly(self, pts, fill, w=0, outline=INK):
        q = [self.P(p) for p in pts]
        self.d.polygon(q, fill=fill)
        if w:
            self.line(pts + [pts[0]], w, outline)

    def oval(self, c, rx, ry, deg, fill, w=0, outline=INK):
        self.poly([(c[0] + v[0], c[1] + v[1]) for v in
                   (rot((rx * math.cos(a / 24 * 2 * math.pi), ry * math.sin(a / 24 * 2 * math.pi)), deg)
                    for a in range(24))], fill, w, outline)

    def dot(self, c, r, fill, outline=None, w=0):
        x, y = self.P(c)
        R = r * self.K
        self.d.ellipse([x - R, y - R, x + R, y + R], fill=fill, outline=outline, width=round(w * self.K))

    def done(self):
        return self.im.resize((round(self.im.width / SS), round(self.im.height / SS)), Image.LANCZOS)


# ------------------------------------------------------------------ running
# Shoe outline relative to the ankle, taken from the sam-run-warm legs SVG (front shoe, ankle at 259,547).
_Q = [((1 - u) ** 2 * 32 + 2 * (1 - u) * u * 7 + u * u * -20, (1 - u) ** 2 * 19 + 2 * (1 - u) * u * 31 + u * u * 16)
      for u in [i / 8 for i in range(1, 9)]]
SHOE_PTS = [(-17, -12), (15, -3), (32, 19)] + _Q


class RunRig:
    W, H, M = 400, 620, 140
    parts = ("legs", "rear-arm", "front-arm")

    def __init__(self, duty=0.40, reach=40, back=50, lift=58, bounce=6.0, arm_amp=24.0):
        self.hips = ((176, 380), (224, 381))          # image-left leg, image-right leg (SVG hip points)
        self.sh = ((143, 244), (258, 245))            # rear-arm (image-left), front-arm (image-right) shoulders
        self.l1, self.l2, self.ground = 103.0, 88.0, 574.0
        self.duty, self.reach, self.back, self.lift, self.b, self.arm_amp = duty, reach, back, lift, bounce, arm_amp
        self.stride = reach + back                    # ankle travel during one stance (asset px)

    def bounce(self, p):
        """Body rise (asset px) above its lowest point; lowest at each mid-stance, highest in each flight phase."""
        return self.b * (1 - math.cos(4 * math.pi * (p - self.duty / 2))) / 2

    def ground_shift(self, cycles):
        """Ground travel (asset px, body frame) after `cycles` gait cycles = stance ankle speed x time."""
        return self.stride / self.duty * cycles

    @staticmethod
    def sole_drop(alpha):
        """Lowest shoe point below the ankle for foot angle alpha (deg, + = toes down), and the rolling contact x
        offset (soft-min over the sole, so the contact rolls heel -> mid-sole -> toe without jumping)."""
        pts = [rot(p, alpha) for p in SHOE_PTS]
        lo = max(q[1] for q in pts)
        wts = [math.exp((q[1] - lo) / 2.0) for q in pts]
        return lo, sum(w * q[0] for w, q in zip(wts, pts)) / sum(wts)

    def foot(self, q, hip, gb):
        """Ankle (x,y) and foot angle for leg phase q (0 = foot contact); gb = ground y in the body frame."""
        q %= 1.0
        D = self.duty
        a_on, a_off = -8.0, 28.0                      # heel-first contact (toes up), plantarflexed toe-off
        x_on = hip[0] + self.reach - self.sole_drop(a_on)[1]
        x_off = hip[0] - self.back - self.sole_drop(a_off)[1]
        if q < D:                                     # stance: contact point moves back linearly = ground speed
            u = q / D
            alpha = lerp(a_on, 0, smooth(u / 0.2)) + a_off * smooth((u - 0.6) / 0.4)
            drop, cx = self.sole_drop(alpha)
            return (hip[0] + self.reach - self.stride * u - cx, gb - drop), alpha
        u = (q - D) / (1 - D)                         # swing: heel recovery behind, then the leg swings through
        alpha = lerp(a_off, 8, smooth(u / 0.45)) if u < 0.45 else lerp(8, a_on, smooth((u - 0.45) / 0.55))
        s = 1 - (1 - u) ** 1.4
        y = gb - self.sole_drop(alpha)[0] - self.lift * math.sin(math.pi * s)
        return (lerp(x_off, x_on, smooth(u)), y), alpha

    def pose(self, p):
        gb = self.ground + self.bounce(p)             # body moved up by bounce => ground lower in the body frame
        legs = []
        for i, hip in enumerate(self.hips):
            (ax, ay), al = self.foot(p + 0.5 * i, hip, gb)
            knee, ank = ik(hip, (ax, ay), self.l1, self.l2, front=1)
            legs.append(dict(hip=hip, knee=knee, ankle=ank, alpha=al))
        arms = []
        for i, sh in enumerate(self.sh):              # arm on side i is forward when the opposite leg is forward
            # biased forward (3/4-front torso: a full back-swing would fold the near forearm across the belly)
            th = 8 + self.arm_amp * math.cos(2 * math.pi * (p - (0.5 if i == 0 else 0.0)))
            el = 90 + 14 * (th - 8) / self.arm_amp    # a little more elbow bend on the forward swing
            e = (sh[0] + 72 * math.sin(math.radians(th)), sh[1] + 72 * math.cos(math.radians(th)))
            h = (e[0] + 56 * math.sin(math.radians(th + el)), e[1] + 56 * math.cos(math.radians(th + el)))
            arms.append(dict(sh=sh, elbow=e, hand=h))
        return dict(legs=legs, arms=arms, ground=gb)

    def draw(self, part, p, k):
        po = self.pose(p)
        c = Canvas(self.W, self.H, self.M, k)
        if part == "legs":
            for lg in po["legs"]:
                c.limb([lg["hip"], lg["knee"], lg["ankle"]], 43, 34, (69, 83, 92))
                a = lg["ankle"]
                c.poly([(a[0] + q[0], a[1] + q[1]) for q in (rot(v, lg["alpha"]) for v in SHOE_PTS)], SHOE, 6)
        else:
            ar = po["arms"][0 if part == "rear-arm" else 1]
            c.limb([ar["sh"], ar["elbow"], ar["hand"]], 36, 27, (50, 124, 121))
            c.oval(ar["hand"], 15, 20, 0, SKIN, 5)
        return c.done()


# ------------------------------------------------------------------ swimming
# Upper-arm / forearm screen angles (deg, 0 = +x i.e. backward for this left-swimming figure, 90 = down) per phase.
# 0.00 entry ahead of the head -> 0.12 extend -> 0.25 high-elbow catch -> 0.40 pull under the shoulder ->
# 0.52 push to the hip -> 0.60 exit -> 0.72 / 0.86 above-water recovery (elbow high) -> entry. Unwrapped: -360/cycle.
UPPER = [(0.00, 186), (0.12, 168), (0.25, 140), (0.40, 95), (0.52, 30), (0.60, -15), (0.72, -70), (0.86, -130)]
# elbow flexes one way only (forearm angle <= upper-arm angle): 5-40 deg in the pull, 15-30 deg in a relaxed
# near-straight-arm recovery (a hanging forearm would dip the hand: forearm 89 > upper arm 87 at a waterline shoulder)
FORE = [(0.00, 181), (0.12, 160), (0.25, 100), (0.40, 60), (0.52, 10), (0.60, -30), (0.72, -95), (0.86, -160)]


class SwimRig:
    W, H, M = 680, 290, 150
    parts = ("rear-arm", "rear-leg", "front-leg", "front-arm", "fx")
    WATER = 160.0                                     # waterline in asset y (project_v2: SY = WT - 160*SS)

    def __init__(self, kick_amp=7.0, roll=5.0):
        self.arms = {"front-arm": dict(sh=(216, 165), l=(87, 89), w=(32, 23), ph=0.0, roll=-1),
                     "rear-arm": dict(sh=(229, 129), l=(87, 80), w=(31, 22), ph=0.5, roll=1)}
        self.legs = {"front-leg": dict(hip=(437, 189), l=(99, 88), w=(39, 30), base=12, ph=0.0),
                     "rear-leg": dict(hip=(435, 165), l=(98, 86), w=(37, 28), base=9, ph=0.5)}
        self.kick_amp, self.roll = kick_amp, roll

    @staticmethod
    def bounce(p):
        """Gentle body rise/fall with the stroke (two per cycle, asset px)."""
        return 2.0 * math.sin(4 * math.pi * p)

    def arm(self, name, p):
        a = self.arms[name]
        q = p + a["ph"]
        rl = a["roll"] * self.roll * math.sin(2 * math.pi * (p - 0.55))   # near shoulder lifts in its recovery
        sh = (a["sh"][0], a["sh"][1] + rl)
        e = polar(sh, cyc(UPPER, q, -360), a["l"][0])
        h = polar(e, cyc(FORE, q, -360), a["l"][1])
        return sh, e, h

    def leg(self, name, p):
        g = self.legs[name]
        q = 3 * p + g["ph"]                                                  # 6-beat kick: 3 per leg per stroke
        th = g["base"] + self.kick_amp * math.sin(2 * math.pi * q)
        flex = 4 + 14 * (0.5 - 0.5 * math.sin(2 * math.pi * q + 0.6))        # knee most bent at top of the downbeat
        k = polar(g["hip"], th, g["l"][0])
        return g["hip"], k, polar(k, th - flex, g["l"][1])

    def draw(self, part, p, k):
        c = Canvas(self.W, self.H, self.M, k)
        if part in self.arms:
            sh, e, h = self.arm(part, p)
            a = self.arms[part]
            c.limb([sh, e, h], a["w"][0], a["w"][1], SKIN)
            fa = math.degrees(math.atan2(h[1] - e[1], h[0] - e[0]))
            c.oval(polar(h, fa, 6), 18, 11, fa, SKIN, 5)
        elif part in self.legs:
            g = self.legs[part]
            c.limb(list(self.leg(part, p)), g["w"][0], g["w"][1], SKIN)
        else:
            self.fx(c, p)
        return c.done()

    def fx(self, c, p):
        """Water effects at real contacts: entry splash + foam, bubble trail behind the pulling hand, bow ripples,
        small spray where a kicking foot breaks the surface. All functions of phase -> loop-continuous."""
        WL, foam, spray = self.WATER, (255, 255, 255, 235), (214, 236, 242, 255)
        for name, a in self.arms.items():
            q = (p + a["ph"]) % 1.0
            if q < 0.2:                                                     # entry splash at the hand's entry point
                u = q / 0.2
                ex = self.arm(name, (0.0 - a["ph"]) % 1.0)[2][0]
                for j, (vx, vy) in enumerate(((-34, -46), (-14, -60), (8, -52), (26, -40), (-48, -28))):
                    x, y = ex + vx * u, WL + vy * u + 120 * u * u
                    if y < WL + 2:
                        c.dot((x, y), 5.5 * (1 - 0.6 * u), spray, (120, 170, 190, 255), 1.5)
                c.oval((ex, WL), 22 + 30 * u, 6 + 3 * u, 0, (255, 255, 255, round(200 * (1 - u))))
            if 0.15 < q < 0.62:                                             # bubbles along the pull path
                for j in range(1, 6):
                    hx, hy = self.arm(name, (q - 0.03 * j - a["ph"]) % 1.0)[2]
                    if hy > WL + 10:
                        c.dot((hx + 4 * j, hy - 5 * j), 6 - 0.7 * j, (255, 255, 255, round(170 * (1 - j / 6))),
                              (120, 170, 190, round(170 * (1 - j / 6))), 1.2)
        for j in range(2):                                                  # bow ripples ahead of the head
            u = (2 * p + 0.5 * j) % 1.0
            c.oval((112 - 30 * u, WL + 2), 26 + 40 * u, 5 + 3 * u, 0, None, 3,
                   (120, 170, 190, round(200 * (1 - u))))
        for name, g in self.legs.items():                                   # spray where a foot breaks the surface
            a0, a1 = self.leg(name, p - 0.004)[2], self.leg(name, p)[2]
            if a1[1] < WL + 8 and a1[1] > a0[1]:
                for j, (dx, dy) in enumerate(((-10, -14), (6, -20), (18, -10))):
                    c.dot((a1[0] + dx, WL + dy), 4.5, spray, (120, 170, 190, 255), 1.2)
            c.oval((a1[0], WL + 2), 18, 4, 0, None, 2.5, (150, 190, 205, 150))


@functools.lru_cache(maxsize=192)
def image(rig, part, p, k):
    return rig.draw(part, p, k)


# ------------------------------------------------------------------ self-check
def check_run(r, n=240):
    rep = dict(stance_contact_err_px=0.0, stance_slip_px=0.0, thigh_err=0.0, shin_err=0.0, max_joint_step_px=0.0)
    prev = None
    ranges = [[1e9, -1e9], [1e9, -1e9]]
    for i in range(n + 1):
        p = i / n
        po = r.pose(p)
        for j, lg in enumerate(po["legs"]):
            rep["thigh_err"] = max(rep["thigh_err"], abs(math.dist(lg["hip"], lg["knee"]) - r.l1))
            rep["shin_err"] = max(rep["shin_err"], abs(math.dist(lg["knee"], lg["ankle"]) - r.l2))
            q = (p + 0.5 * j) % 1
            lo = lg["ankle"][1] + r.sole_drop(lg["alpha"])[0]
            if q < r.duty:
                rep["stance_contact_err_px"] = max(rep["stance_contact_err_px"], abs(lo - po["ground"]))
            else:
                assert lo <= po["ground"] + 0.5, (p, j, lo, po["ground"])          # never below the ground
            kn = math.degrees(math.pi - math.acos(max(-1, min(1, (r.l1 ** 2 + r.l2 ** 2 - math.dist(lg["hip"], lg["ankle"]) ** 2) / (2 * r.l1 * r.l2)))))
            ranges[j] = [min(ranges[j][0], kn), max(ranges[j][1], kn)]
        if prev:
            rep["max_joint_step_px"] = max(rep["max_joint_step_px"], *(math.dist(a[k], b[k]) for a, b in
                                           zip(prev["legs"], po["legs"]) for k in ("knee", "ankle")))
        prev = po
    # slip: stance contact point vs ground travel, both in the body frame (zero = planted)
    for j in range(2):
        q0 = 0.05
        p0, p1 = (q0 - 0.5 * j) % 1, (q0 + 0.25 - 0.5 * j) % 1
        x0 = r.pose(p0)["legs"][j]["ankle"][0] + r.sole_drop(r.pose(p0)["legs"][j]["alpha"])[1]
        x1 = r.pose(p1)["legs"][j]["ankle"][0] + r.sole_drop(r.pose(p1)["legs"][j]["alpha"])[1]
        rep["stance_slip_px"] = max(rep["stance_slip_px"], abs((x0 - x1) - r.ground_shift(0.25)))
    a, b = r.pose(0.0), r.pose(1.0)
    rep["loop_closure_px"] = max(math.dist(x[k], y[k]) for x, y in zip(a["legs"] + a["arms"], b["legs"] + b["arms"])
                                 for k in x if isinstance(x[k], tuple))
    rep["knee_flexion_range_deg"] = [[round(v, 1) for v in rg] for rg in ranges]
    return rep


def check_swim(r, n=360):
    rep = dict(loop_closure_px=0.0, max_hand_step_px=0.0, arm_len_err=0.0)
    ys = {k: [] for k in r.arms}
    for name in r.arms:
        a0, a1 = r.arm(name, 0.0), r.arm(name, 1.0)
        rep["loop_closure_px"] = max(rep["loop_closure_px"], max(math.dist(x, y) for x, y in zip(a0, a1)))
        prev = None
        for i in range(n + 1):
            sh, e, h = r.arm(name, i / n)
            rep["arm_len_err"] = max(rep["arm_len_err"], abs(math.dist(sh, e) - r.arms[name]["l"][0]),
                                     abs(math.dist(e, h) - r.arms[name]["l"][1]))
            if prev:
                rep["max_hand_step_px"] = max(rep["max_hand_step_px"], math.dist(prev, h))
            prev = h
            ys[name].append(h[1])
    WL = r.WATER
    for name, a in r.arms.items():                      # recovery above water, pull below, entry at the surface
        rec = [r.arm(name, (q - a["ph"]) % 1)[2][1] for q in (0.7, 0.75, 0.8, 0.85, 0.9)]
        pull = [r.arm(name, (q - a["ph"]) % 1)[2][1] for q in (0.25, 0.32, 0.4, 0.46)]
        rep[f"{name}_recovery_hand_y_max"] = round(max(rec), 1)
        rep[f"{name}_pull_hand_y_min"] = round(min(pull), 1)
        assert max(rec) < WL and min(pull) > WL, (name, rec, pull)
    return rep


if __name__ == "__main__":
    import json
    rr = check_run(RunRig())
    assert rr["stance_contact_err_px"] < 0.01 and rr["thigh_err"] < 0.01 and rr["shin_err"] < 0.01, rr
    assert rr["loop_closure_px"] < 1e-6 and rr["max_joint_step_px"] < 8, rr
    sr = check_swim(SwimRig())
    assert sr["loop_closure_px"] < 1e-6 and sr["arm_len_err"] < 1e-6, sr
    print(json.dumps(dict(run=rr, swim=sr), indent=1))
