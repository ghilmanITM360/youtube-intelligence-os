"""Animated graph primitives: axes that draw on, polylines that trace, bars that grow, error bars that shrink."""
import numpy as np
from . import tokens as T
from .easing import clamp, lerp, ease_out_cubic

class Axes:
    def __init__(self, box, xr=(0, 1), yr=(0, 1)): self.box, self.xr, self.yr = box, xr, yr
    def X(self, x): b = self.box; return lerp(b[0], b[2], (x - self.xr[0]) / (self.xr[1] - self.xr[0]))
    def Y(self, y): b = self.box; return lerp(b[3], b[1], (y - self.yr[0]) / (self.yr[1] - self.yr[0]))
    def draw(self, cv, progress=1.0, alpha=1.0, ticks=8):
        x0, y0, x1, y1 = self.box
        cv.line((x0, y1), (lerp(x0, x1, clamp(progress)), y1), T.GREY, 4, alpha=alpha); cv.line((x0, y1), (x0, lerp(y1, y0, clamp(progress))), T.GREY, 4, alpha=alpha)
        for i in range(ticks + 1):
            xi = lerp(x0, x1, i / ticks)
            if xi <= lerp(x0, x1, clamp(progress)) + 0.5: cv.line((xi, y1), (xi, y1 + 14), T.GREY, 3, alpha=alpha)

def trace_line(cv, ax, xs, ys, progress, color=T.COOL, width=6, alpha=1.0):
    """polyline through (xs,ys) drawn up to `progress` of its x-range (subsegment interpolated)."""
    n = len(xs); k = clamp(progress) * (n - 1); i = int(k); pts = [(ax.X(xs[j]), ax.Y(ys[j])) for j in range(min(i, n - 1) + 1)]
    if i < n - 1: f = k - i; pts.append((ax.X(lerp(xs[i], xs[i + 1], f)), ax.Y(lerp(ys[i], ys[i + 1], f))))
    if len(pts) > 1: cv.polyline(pts, color, width, alpha=alpha)
    return pts[-1]

def bars(cv, ax, xs, hs, progress=1.0, color=T.COOL, w=14, alpha=1.0, stagger=0.02):
    for i, (x, h) in enumerate(zip(xs, hs)):
        g = ease_out_cubic(clamp((progress - i * stagger) / max(1e-6, 1 - len(xs) * stagger)))
        cv.rect((ax.X(x) - w / 2, ax.Y(h * g), ax.X(x) + w / 2, ax.Y(0)), fill=color, alpha=alpha, radius=3)

def error_bar(cv, x, y, half, color=T.WHITE, alpha=1.0, cap=14):
    cv.line((x, y - half), (x, y + half), color, 4, alpha=alpha); cv.line((x - cap, y - half), (x + cap, y - half), color, 4, alpha=alpha); cv.line((x - cap, y + half), (x + cap, y + half), color, 4, alpha=alpha)
