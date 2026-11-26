"""Conceptual corner-cube retroreflection (2-D cross-section) and flat-mirror contrast. Educational only: no device design,
no dimensions, no instrument settings. Geometry is exact (specular reflection off two perpendicular faces) and ASSERTED."""
import math
import numpy as np
from . import tokens as T
from .easing import clamp, lerp, seg, smoothstep, ease_in_out_cubic


class CornerCube2D:
    """Two perpendicular reflecting faces meeting at `apex` (90 deg), opening DOWN (toward Earth, y grows downward).
    Up is out, down is home (cross-cutting rule 2)."""
    def __init__(self, apex=(540, 640), face=520, half_angle_deg=45.0):
        a = math.radians(half_angle_deg); self.apex = np.array(apex, float); self.face = face
        self.left = self.apex + face * np.array([-math.sin(a), math.cos(a)]); self.right = self.apex + face * np.array([math.sin(a), math.cos(a)])
        assert abs(2 * half_angle_deg - 90.0) < 1e-9, 'faces must be perpendicular'
        self.faces = [(self.apex, self.left), (self.apex, self.right)]

    @staticmethod
    def _hit(p, d, q0, q1):
        e = q1 - q0; den = d[0] * e[1] - d[1] * e[0]
        if abs(den) < 1e-12: return None
        t = ((q0[0] - p[0]) * e[1] - (q0[1] - p[1]) * e[0]) / den; s = ((q0[0] - p[0]) * d[1] - (q0[1] - p[1]) * d[0]) / den
        return t if (t > 1e-7 and -1e-9 <= s <= 1 + 1e-9) else None

    def trace(self, start, angle_deg, end_y=None):
        """Trace a ray travelling UP (toward the Moon) from `start` at `angle_deg` off vertical (+ = leaning right).
        Returns dict(points=[start, hit1, hit2, end], d_in, d_out). Asserts exactly two reflections and d_out = -d_in."""
        a = math.radians(angle_deg); d = np.array([math.sin(a), -math.cos(a)]); p = np.array(start, float); pts = [p.copy()]; d_in = d.copy()
        for _ in range(2):
            best = None
            for q0, q1 in self.faces:
                t = self._hit(p, d, q0, q1)
                if t is not None and (best is None or t < best[0]): best = (t, q0, q1)
            assert best is not None, 'ray missed the cube faces (start=%s angle=%s)' % (start, angle_deg)
            t, q0, q1 = best; p = p + d * t; pts.append(p.copy())
            e = (q1 - q0) / np.linalg.norm(q1 - q0); n = np.array([-e[1], e[0]]); d = d - 2 * np.dot(d, n) * n
        # a third hit would mean the geometry is wrong for a 90-degree corner
        assert all(self._hit(p, d, q0, q1) is None for q0, q1 in self.faces), 'unexpected third reflection'
        ey = start[1] if end_y is None else end_y
        L = (ey - p[1]) / d[1] if d[1] > 1e-9 else 0.0
        pts.append(p + d * max(L, 0.0))
        # ---- THE assertion of this module: entry and exit are antiparallel (exit direction = - entry direction)
        assert np.allclose(d, -d_in, atol=1e-9), 'exit ray not antiparallel to entry ray: %s vs %s' % (d, -d_in)
        return dict(points=pts, d_in=d_in, d_out=d)


def flat_mirror_ray(start, angle_deg, mirror_y, end_y=None):
    """Ray going up hits a horizontal flat mirror at y=mirror_y; ordinary specular reflection (angle in = angle out)."""
    a = math.radians(angle_deg); d = np.array([math.sin(a), -math.cos(a)]); p = np.array(start, float)
    t = (mirror_y - p[1]) / d[1]; hit = p + d * t; d2 = np.array([d[0], -d[1]])
    ey = start[1] if end_y is None else end_y; L = (ey - hit[1]) / d2[1]
    end = hit + d2 * L
    if abs(angle_deg) > 1e-6: assert np.dot(d, d2) > -1 + 1e-3, 'a tilted ray must NOT retro-reflect from a flat mirror'
    return dict(points=[p, hit, end], d_in=d, d_out=d2)


def cross2(a, b): return float(a[0] * b[1] - a[1] * b[0])

def polyline_len(pts): return float(sum(np.linalg.norm(np.array(pts[i + 1]) - np.array(pts[i])) for i in range(len(pts) - 1)))

def partial_polyline(pts, frac):
    tot = polyline_len(pts); need = tot * clamp(frac); out = [tuple(pts[0])]
    for i in range(len(pts) - 1):
        l = np.linalg.norm(np.array(pts[i + 1]) - np.array(pts[i]))
        if need >= l - 1e-9: out.append(tuple(pts[i + 1])); need -= l
        else: out.append(tuple(np.array(pts[i]) + (np.array(pts[i + 1]) - np.array(pts[i])) * (need / l if l else 0))); break
    return out

def draw_cube(cv, cube, alpha=1.0, glass_alpha=0.16, face_color=T.GLASS, width=11):
    ap, l, r = cube.apex, cube.left, cube.right
    cv.polygon([tuple(ap), tuple(l), tuple(r)], fill=face_color, alpha=alpha * glass_alpha)
    cv.polyline([tuple(l), tuple(r)], face_color, 3, alpha=alpha * 0.45, dash=(14, 12))        # open aperture (dashed)
    cv.polyline([tuple(l), tuple(ap), tuple(r)], face_color, width, alpha=alpha)
    cv.circle(tuple(ap), width * 0.65, fill=T.WHITE, alpha=alpha * 0.9)

def draw_ray(cv, pts, progress, split_frac=None, alpha=1.0, width=8, head=True):
    """Ray polyline drawn up to `progress` (0..1 of total length): warm until the second hit, cool after (entry out / exit home).
    Returns the head position and the direction at the head."""
    from .space import pulse_bead
    pts = [tuple(p) for p in pts]; L = [np.linalg.norm(np.array(pts[i + 1]) - np.array(pts[i])) for i in range(len(pts) - 1)]; tot = sum(L)
    need = tot * clamp(progress); acc = 0; head_pos = pts[0]; head_dir = np.array(pts[1]) - np.array(pts[0])
    for i, l in enumerate(L):
        col = T.WARM if i < len(L) - 1 else T.COOL
        if need <= 0: break
        f = clamp(need / l) if l > 0 else 1.0
        end = tuple(np.array(pts[i]) + (np.array(pts[i + 1]) - np.array(pts[i])) * f)
        cv.line(pts[i], end, col, width, alpha=alpha)
        head_pos, head_dir = end, np.array(pts[i + 1]) - np.array(pts[i]); need -= l; acc += l
    return head_pos, head_dir

def hit_spark(cv, p, u, alpha=1.0):
    """tiny non-flash reflection mark: a thin ring that expands and fades"""
    if 0 < u < 1: cv.circle(tuple(p), lerp(8, 34, u), outline=T.WHITE, width=2.5, alpha=alpha * 0.55 * (1 - u))

def guide_ticks(cv, entry_pts, exit_pts, y, alpha=1.0, color=T.WHITE):
    """Faint pair of ticks across the entry ray and the exit ray at the same height, showing they are parallel (and offset)."""
    def x_at(pts, yy):
        for i in range(len(pts) - 1):
            (xa, ya), (xb, yb) = pts[i], pts[i + 1]
            if (ya - yy) * (yb - yy) <= 0 and ya != yb: return xa + (xb - xa) * (yy - ya) / (yb - ya)
    xa, xb = x_at(entry_pts, y), x_at(exit_pts, y)
    if xa is None or xb is None: return
    for x in (xa, xb): cv.line((x - 20, y), (x + 20, y), color, 3, alpha=alpha * 0.8)
    cv.line((xa, y), (xb, y), color, 2, alpha=alpha * 0.4, dash=(7, 7))
    return xa, xb

def third_face_inset(cv, c, r=100, alpha=1.0):
    """Magnified inset: the third face seen end-on (three mutually perpendicular faces meet at the apex). Magnifier tab, no text."""
    cv.circle(c, r, fill=(14, 20, 40), outline=T.GREY, width=4, alpha=alpha)
    for a in (-90, 30, 150):
        t = math.radians(a); cv.line(c, (c[0] + r * 0.78 * math.cos(t), c[1] + r * 0.78 * math.sin(t)), T.GLASS, 6, alpha=alpha)
    cv.circle((c[0] + r * 0.72, c[1] + r * 0.72), 17, outline=T.GREY, width=3, alpha=alpha); cv.line((c[0] + r * 0.72 + 12, c[1] + r * 0.72 + 12), (c[0] + r * 0.72 + 28, c[1] + r * 0.72 + 28), T.GREY, 5, alpha=alpha)

def footprint_inset(cv, c, r=105, alpha=1.0):
    """C06 binding picture rule: magnified inset, NO numbers: wide beam footprint (soft disc) with the array a tiny marker inside it."""
    cv.circle(c, r, fill=(14, 20, 40), outline=T.GREY, width=4, alpha=alpha)
    cv.glow(c, r * 0.9, T.WARM, 0.5 * alpha, power=1.4)
    cv.rect((c[0] - 4, c[1] - 3, c[0] + 4, c[1] + 3), fill=T.WHITE, alpha=alpha)
    cv.circle((c[0] + r * 0.72, c[1] + r * 0.72), 17, outline=T.GREY, width=3, alpha=alpha); cv.line((c[0] + r * 0.72 + 12, c[1] + r * 0.72 + 12), (c[0] + r * 0.72 + 28, c[1] + r * 0.72 + 28), T.GREY, 5, alpha=alpha)
