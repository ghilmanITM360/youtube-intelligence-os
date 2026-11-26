"""Easing library. All functions map x in [0,1] -> y with y(0)=0, y(1)=1 (spring/elastic settle to 1; back overshoots).
There is deliberately no 'default' ease: every call site names the ease that matches the object (HumanCraft rule)."""
import math

def clamp(x, a=0.0, b=1.0): return a if x < a else b if x > b else x
def lerp(a, b, x): return a + (b - a) * x
def seg(t, a, b):
    """0 before a, 1 after b, linear between (the 'progress of a phase' helper)."""
    return clamp((t - a) / (b - a)) if b > a else (1.0 if t >= b else 0.0)
def remap(x, a, b, c, d): return lerp(c, d, clamp((x - a) / (b - a)))

def linear(x): return clamp(x)
def smoothstep(x): x = clamp(x); return x * x * (3 - 2 * x)
def ease_in_quad(x): x = clamp(x); return x * x
def ease_out_quad(x): x = clamp(x); return 1 - (1 - x) ** 2
def ease_in_cubic(x): x = clamp(x); return x ** 3
def ease_out_cubic(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_in_out_cubic(x):
    x = clamp(x); return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2
def ease_out_expo(x): x = clamp(x); return 1.0 if x >= 1 else 1 - 2 ** (-10 * x)
def ease_in_expo(x): x = clamp(x); return 0.0 if x <= 0 else 2 ** (10 * x - 10)
def ease_in_out_expo(x):
    x = clamp(x)
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    return 2 ** (20 * x - 10) / 2 if x < 0.5 else (2 - 2 ** (-20 * x + 10)) / 2
def ease_out_back(x, s=1.70158):
    x = clamp(x) - 1; return 1 + (s + 1) * x ** 3 + s * x ** 2
def ease_in_back(x, s=1.70158):
    x = clamp(x); return (s + 1) * x ** 3 - s * x ** 2
def ease_in_out_back(x, s=1.70158 * 1.525):
    x = clamp(x)
    return ((2 * x) ** 2 * ((s + 1) * 2 * x - s)) / 2 if x < 0.5 else ((2 * x - 2) ** 2 * ((s + 1) * (x * 2 - 2) + s) + 2) / 2

def spring(x, damping=0.45, freq=2.5, settle=1.0):
    """Damped-spring step response, x in [0,1] (1 = `settle`-times-the-period window). damping ratio zeta (<1 overshoots),
    freq = natural cycles over the window. Forced to exactly 1 at x>=1 so clips end on the target (tiny residual blended out)."""
    x = clamp(x)
    if x <= 0: return 0.0
    w = 2 * math.pi * freq; z = min(damping, 0.999); wd = w * math.sqrt(1 - z * z)
    y = 1 - math.exp(-z * w * x * settle) * (math.cos(wd * x * settle) + z / math.sqrt(1 - z * z) * math.sin(wd * x * settle))
    end = 1 - math.exp(-z * w * settle) * (math.cos(wd * settle) + z / math.sqrt(1 - z * z) * math.sin(wd * settle))
    return y + (1 - end) * x ** 8           # residual at the window end blended in so y(1)==1 exactly

def bezier(x1, y1, x2, y2):
    """CSS-style cubic-bezier(x1,y1,x2,y2) ease factory (Newton + bisection solve for t at given x)."""
    def bx(t): return 3 * (1 - t) ** 2 * t * x1 + 3 * (1 - t) * t * t * x2 + t ** 3
    def by(t): return 3 * (1 - t) ** 2 * t * y1 + 3 * (1 - t) * t * t * y2 + t ** 3
    def dbx(t): return 3 * (1 - t) ** 2 * x1 + 6 * (1 - t) * t * (x2 - x1) + 3 * t * t * (1 - x2)
    def f(x):
        x = clamp(x)
        if x in (0.0, 1.0): return x
        t = x
        for _ in range(8):
            e = bx(t) - x; d = dbx(t)
            if abs(e) < 1e-7: return by(t)
            if abs(d) < 1e-6: break
            t -= e / d
        lo, hi = 0.0, 1.0; t = x
        for _ in range(40):
            e = bx(t) - x
            if abs(e) < 1e-7: break
            if e > 0: hi = t
            else: lo = t
            t = (lo + hi) / 2
        return by(t)
    return f

def hold_then(ease, hold=0.2):
    """Anticipation helper: stay at 0 for `hold` of the span, then run `ease` over the rest."""
    return lambda x: ease(seg(x, hold, 1.0))

EASES = dict(linear=linear, smoothstep=smoothstep, in_quad=ease_in_quad, out_quad=ease_out_quad, in_cubic=ease_in_cubic,
             out_cubic=ease_out_cubic, in_out_cubic=ease_in_out_cubic, out_expo=ease_out_expo, in_expo=ease_in_expo,
             in_out_expo=ease_in_out_expo, out_back=ease_out_back, in_back=ease_in_back, in_out_back=ease_in_out_back,
             spring=spring)
