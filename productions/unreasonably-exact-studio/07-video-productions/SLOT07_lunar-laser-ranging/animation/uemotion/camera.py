"""Camera2D (pan / zoom / rotate) and the Layer2_5D compositor (per-layer parallax, occlusion order, overscan checking)."""
import math
from dataclasses import dataclass, field
import numpy as np
from . import tokens as T
from .timeline import Track

CENTER = (T.DESIGN_W / 2, T.DESIGN_H / 2)


@dataclass(frozen=True)
class CamState:
    x: float = CENTER[0]        # world point seen at the screen centre
    y: float = CENTER[1]
    zoom: float = 1.0
    rot: float = 0.0            # radians, camera roll


def T3(tx, ty): return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1.0]])
def S3(s): return np.array([[s, 0, 0], [0, s, 0], [0, 0, 1.0]])
def R3(a): c, s = math.cos(a), math.sin(a); return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])


class Camera2D:
    """Tracks are optional: pos (vec2), zoom, rot. Rest state = looking at the screen centre, zoom 1, no roll."""
    def __init__(self, pos=None, zoom=None, rot=None):
        self.pos = pos or Track([(0, CENTER)]); self.zoom = zoom or Track([(0, 1.0)]); self.rot = rot or Track([(0, 0.0)])
    def state(self, t):
        x, y = self.pos(t); return CamState(x, y, self.zoom(t), self.rot(t))
    @staticmethod
    def matrix(s, parallax=1.0, ref=CENTER):
        """world -> design-unit matrix for a layer with parallax factor p (1 = locked to the world, 0 = infinitely far).
        apparent camera = ref + (cam - ref) * p ; apparent zoom = zoom ** p ; roll applies to all layers."""
        cx = ref[0] + (s.x - ref[0]) * parallax; cy = ref[1] + (s.y - ref[1]) * parallax
        return T3(*CENTER) @ S3(s.zoom ** parallax) @ R3(s.rot) @ T3(-cx, -cy)
    @staticmethod
    def project(s, pt, parallax=1.0):
        v = Camera2D.matrix(s, parallax) @ np.array([pt[0], pt[1], 1.0]); return (float(v[0]), float(v[1]))
    @staticmethod
    def visible_world_rect(s, parallax=1.0):
        """world-space bounding box of what the screen sees on a layer with this parallax."""
        Minv = np.linalg.inv(Camera2D.matrix(s, parallax))
        c = np.array([[0, 0, 1], [T.DESIGN_W, 0, 1], [T.DESIGN_W, T.DESIGN_H, 1], [0, T.DESIGN_H, 1]], float).T
        w = (Minv @ c)[:2]; return (w[0].min(), w[1].min(), w[0].max(), w[1].max())


@dataclass
class Layer:
    """One depth layer. draw(cv, ctx) draws in the layer's own world coordinates (the compositor installs the transform).
    z orders occlusion (low = far, drawn first). extent = world rect the layer art covers (None = unbounded procedural; an individual side may be None = open by design)."""
    name: str
    draw: callable
    parallax: float = 1.0
    z: float = 0.0
    extent: tuple = None
    alpha: float = 1.0


class Layer2_5D:
    def __init__(self, layers, camera):
        self.layers = sorted(layers, key=lambda l: l.z); self.cam = camera

    def render(self, cv, ctx, t=None):
        s = self.cam.state(ctx.a if t is None else t)
        for L in self.layers:
            with cv.xf(Camera2D.matrix(s, L.parallax)):
                if L.alpha < 0.999:
                    with cv.group(L.alpha): L.draw(cv, ctx)
                else: L.draw(cv, ctx)
        return s

    def overscan_report(self, t0, t1, n=121):
        """Min margin (world units) between the visible world rect and each layer's extent over [t0,t1]; <0 means the
        camera reveals an empty edge on that layer."""
        rep = {}
        for L in self.layers:
            if L.extent is None: rep[L.name] = math.inf; continue
            m = math.inf
            for i in range(n):
                vx0, vy0, vx1, vy1 = Camera2D.visible_world_rect(self.cam.state(t0 + (t1 - t0) * i / (n - 1)), L.parallax)
                for v, e, sign in ((vx0, L.extent[0], 1), (vy0, L.extent[1], 1), (vx1, L.extent[2], -1), (vy1, L.extent[3], -1)):
                    if e is not None: m = min(m, (v - e) * sign)           # None = that side is open by design (sky above a ridge, etc.)
            rep[L.name] = m
        return rep

    def assert_overscan(self, t0, t1):
        rep = self.overscan_report(t0, t1)
        bad = {k: v for k, v in rep.items() if v < 0}
        assert not bad, 'layer overscan too small (world units short): %s' % bad
        return rep


def starfield(extent, density=1.6e-3, seed=5, rmax=2.6):
    """Procedural star layer drawer covering `extent` (world rect). Positions are fixed by the seed (pure function of nothing)."""
    x0, y0, x1, y1 = extent; rng = np.random.default_rng(seed)
    n = int((x1 - x0) * (y1 - y0) * density)
    pts = np.stack([rng.uniform(x0, x1, n), rng.uniform(y0, y1, n)], 1)
    r = rng.choice([1.0, 1.4, 2.0, rmax], n, p=[.5, .3, .15, .05]); a = rng.uniform(0.25, 0.9, n)
    def draw(cv, ctx):
        cv.dots([tuple(p) for p in pts], r, (225, 230, 248), a)
    return draw
