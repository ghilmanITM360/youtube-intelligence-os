"""Formula transformation: tokens (text pieces) that move along arcs, scale and cross-fade into one another.
d = c * t / 2 is built from the SAME objects that were the stopwatch value and the path-bar labels, not typed onto the screen."""
import math
import numpy as np
from . import tokens as T
from .easing import clamp, lerp, seg, ease_in_out_cubic, ease_out_back
from .camera import T3, S3


class Token:
    """text token with tracks: pos(t)->(x,y), alpha(t), scale(t). Any may be a constant or a callable of t."""
    def __init__(self, text, size=96, color=T.WHITE, pos=(540, 300), alpha=1.0, scale=1.0, bold=True, mono=False):
        self.text, self.size, self.color, self.bold, self.mono = text, size, color, bold, mono
        self._pos, self._alpha, self._scale = pos, alpha, scale
    def at(self, name, t):
        v = getattr(self, '_' + name); return v(t) if callable(v) else v
    def draw(self, cv, t):
        a = self.at('alpha', t)
        if a <= 0.003: return
        x, y = self.at('pos', t); s = self.at('scale', t)
        with cv.xf(T3(x, y) @ S3(s) @ T3(-x, -y)):
            cv.text((x, y), self.text, self.size, self.color, bold=self.bold, mono=self.mono, alpha=a, math=True)

def arc_path(p0, p1, t0, t1, ease=ease_in_out_cubic, bow=0.0):
    """position function moving p0 -> p1 over [t0,t1] along a circular-ish arc (bow = sideways bulge in units; arcs principle)."""
    p0, p1 = np.array(p0, float), np.array(p1, float); d = p1 - p0; n = np.array([-d[1], d[0]]); n = n / (np.linalg.norm(n) + 1e-9)
    def f(t):
        u = ease(seg(t, t0, t1)); p = p0 + d * u + n * bow * math.sin(math.pi * u); return (float(p[0]), float(p[1]))
    return f

def fade(t0, t1, a0=0.0, a1=1.0, ease=ease_in_out_cubic): return lambda t: lerp(a0, a1, ease(seg(t, t0, t1)))

def row_positions(cv, texts, size, cx, y, gap=26, bold=True, mono=False):
    """centre a row of tokens horizontally; returns x centres (design units)."""
    ws = [cv.text_width(s, size, bold=bold, mono=mono, math=True) for s in texts]; tot = sum(ws) + gap * (len(ws) - 1); x = cx - tot / 2; out = []
    for w in ws: out.append(x + w / 2); x += w + gap
    return out
