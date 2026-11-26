"""Keyframe tracks and the three named clocks.

narration_t : seconds on the master voice recording (0 .. 92.53). Every reveal is keyed to this.
anim_t      : clip-local seconds (0 at the first frame of a proof/clip). anim_t = narration_t - clip.n0.
model_t     : the physical light-travel clock (0 .. 2.56 s). ModelClock maps narration_t -> model_t piecewise-linearly, so a
              pulse and a stopwatch that both read model_t can never disagree. A segment whose narration length exceeds its
              model length is slow motion; ModelClock.slow_factor() reports it for the on-screen 'illustrative time' badge.
"""
from dataclasses import dataclass
import numpy as np
from . import easing as E


class Track:
    """Keyframes [(t, value, ease_to_next)], value scalar or vector. Holds first/last value outside the range.
    ease_to_next: callable, name in easing.EASES, or None (= linear). The ease belongs to the segment STARTING at that key."""
    def __init__(self, keys):
        self.keys = sorted(((float(t), np.asarray(v, float), self._ease(e)) for t, v, *r in keys for e in [r[0] if r else None]),
                           key=lambda k: k[0])
        self.vec = self.keys[0][1].ndim > 0

    @staticmethod
    def _ease(e):
        if e is None: return E.linear
        return E.EASES[e] if isinstance(e, str) else e

    def __call__(self, t):
        ks = self.keys
        if t <= ks[0][0]: v = ks[0][1]
        elif t >= ks[-1][0]: v = ks[-1][1]
        else:
            for i in range(len(ks) - 1):
                if ks[i][0] <= t < ks[i + 1][0]:
                    u = (t - ks[i][0]) / (ks[i + 1][0] - ks[i][0]); k = ks[i][2](u)
                    v = ks[i][1] + (ks[i + 1][1] - ks[i][1]) * k; break
        return tuple(float(x) for x in v) if self.vec else float(v)


def phase(t, t0, t1, ease=None):
    """Progress 0..1 of a phase [t0,t1] with the named ease (used everywhere for one-off events)."""
    return Track._ease(ease)(E.seg(t, t0, t1))


class ModelClock:
    """Piecewise-linear narration_t -> model_t. segments = [(n0, n1, m0, m1), ...]; held between/outside segments."""
    def __init__(self, segments):
        self.seg = sorted(segments)
        for (a0, a1, b0, b1) in self.seg: assert a1 > a0 and b1 >= b0
    def __call__(self, n):
        m = self.seg[0][2]
        for (n0, n1, m0, m1) in self.seg:
            if n < n0: return m
            if n < n1: return m0 + (m1 - m0) * (n - n0) / (n1 - n0)
            m = m1
        return m
    def slow_factor(self, i=0):
        n0, n1, m0, m1 = self.seg[i]; return (n1 - n0) / (m1 - m0)
    def running(self, n):
        return any(n0 <= n < n1 for n0, n1, _, _ in self.seg)


@dataclass(frozen=True)
class Ctx:
    """What a scene function receives. n/a/m are the three clocks; scale and fps are for information only."""
    n: float        # narration_t
    a: float        # anim_t
    m: float        # model_t
    frame: int = 0
    fps: float = 30.0
    scale: float = 0.5


@dataclass
class ClockSet:
    n0: float                       # narration_t at anim_t = 0
    model: ModelClock = None        # optional narration->model mapping
    def at(self, a, frame=0, fps=30.0, scale=0.5):
        n = self.n0 + a
        return Ctx(n=n, a=a, m=self.model(n) if self.model else 0.0, frame=frame, fps=fps, scale=scale)
