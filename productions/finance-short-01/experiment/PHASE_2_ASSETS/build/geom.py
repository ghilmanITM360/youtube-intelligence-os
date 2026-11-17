"""Small 2D geometry helpers: affine matrices and tapered limb outlines."""
import math


def mat(a=1, b=0, c=0, d=1, e=0, f=0):
    return (a, b, c, d, e, f)


def mul(m, n):
    a, b, c, d, e, f = m
    a2, b2, c2, d2, e2, f2 = n
    return (a * a2 + c * b2, b * a2 + d * b2, a * c2 + c * d2, b * c2 + d * d2,
            a * e2 + c * f2 + e, b * e2 + d * f2 + f)


def T(x, y):
    return (1, 0, 0, 1, x, y)


def R(deg, cx=0, cy=0):
    r = math.radians(deg)
    co, si = math.cos(r), math.sin(r)
    return mul(T(cx, cy), mul((co, si, -si, co, 0, 0), T(-cx, -cy)))


def S(sx, sy=None):
    return (sx, 0, 0, sx if sy is None else sy, 0, 0)


def apply(m, p):
    a, b, c, d, e, f = m
    return (a * p[0] + c * p[1] + e, b * p[0] + d * p[1] + f)


def svg_matrix(m):
    return "matrix(" + " ".join(f"{v:.4f}".rstrip("0").rstrip(".") if v else "0" for v in m) + ")"


def fmt(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def capsule(p1, r1, p2, r2):
    """Outline of a tapered limb: circles r1 at p1 and r2 at p2 joined by straight sides."""
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    length = math.hypot(dx, dy) or 1
    ux, uy = dx / length, dy / length
    nx, ny = -uy, ux
    a1 = (p1[0] + nx * r1, p1[1] + ny * r1)
    a2 = (p2[0] + nx * r2, p2[1] + ny * r2)
    b2 = (p2[0] - nx * r2, p2[1] - ny * r2)
    b1 = (p1[0] - nx * r1, p1[1] - ny * r1)
    f = fmt
    return (f"M{f(a1[0])} {f(a1[1])}L{f(a2[0])} {f(a2[1])}"
            f"A{f(r2)} {f(r2)} 0 0 0 {f(b2[0])} {f(b2[1])}"
            f"L{f(b1[0])} {f(b1[1])}A{f(r1)} {f(r1)} 0 0 0 {f(a1[0])} {f(a1[1])}Z")
