"""Photon-event illustrations: faint detection markers (no bright flash) and the pulse-accumulation histogram.
Everything is illustrative and labelled as such by the caller (C08: counts are illustrative)."""
import math
import numpy as np
from . import tokens as T
from .easing import clamp, lerp, seg, smoothstep, ease_out_cubic

MARK_COLOR = T.COOL
MARK_PEAK_ALPHA = 0.72          # core alpha cap: with COOL on BG the core never exceeds luma ~140 -> no flash

def detection_marker(cv, x, y, age, hold=True, size=1.0, ring_max=46, strength=1.0, fade_after=None, hold_ring=False):
    """One detection: core fades in over 0.18 s (no flash), a single thin ring expands once and fades, then a faint dot holds.
    age = seconds since the click (<0: not yet)."""
    if age <= 0: return
    core = smoothstep(age / 0.18) * MARK_PEAK_ALPHA * strength
    if fade_after is not None: core *= 1 - smoothstep((age - fade_after) / 0.8)
    if not hold and age > 1.2: core *= max(0, 1 - (age - 1.2) / 0.8)
    u = seg(age, 0.0, 0.8)
    if 0 < u < 1: cv.circle((x, y), lerp(12, ring_max * 1.2, ease_out_cubic(u)) * size, outline=MARK_COLOR, width=2.5, alpha=0.38 * strength * (1 - u))
    if hold_ring and u >= 1: cv.circle((x, y), ring_max * size * 0.55, outline=MARK_COLOR, width=2.5, alpha=0.30 * strength)   # soft ring stays (B28: 'each with a soft ring')
    cv.circle((x, y), 9.5 * size, fill=MARK_COLOR, alpha=core)            # V2: 6.5 -> 9.5 (D08 phone readability)

def time_axis(cv, x0, x1, y, alpha=1.0, progress=1.0, label_t=True):
    xe = lerp(x0, x1, clamp(progress))
    cv.line((x0, y), (xe, y), T.GREY, 4, alpha=alpha)
    for i in range(9):
        xi = lerp(x0, x1, i / 8)
        if xi <= xe + 0.5: cv.line((xi, y - 9), (xi, y + 9), T.GREY, 3, alpha=alpha)
    if label_t and progress >= 1: cv.text((x1 + 36, y), 't', 36, T.GREY, bold=True, alpha=alpha, anchor='lm')


class PulseHistogram:
    """Deterministic simulated detection record. Each laser pulse k (in order) yields Poisson(lam_s) signal photons at times
    ~ N(mu, sigma) plus Poisson(lam_b) uniform background photons. histogram(n) uses the first n pulses only, so the picture
    is a pure function of the pulse counter n (re-renderable at any fps)."""
    def __init__(self, n_max=6000, bins=40, lam_s=0.30, lam_b=0.70, mu=0.62, sigma=0.032, seed=2013):
        rng = np.random.default_rng(seed); self.bins = bins; self.n_max = n_max; self.mu, self.sigma = mu, sigma
        ks = rng.poisson(lam_s, n_max); kb = rng.poisson(lam_b, n_max)
        pulse, tt, sig = [], [], []
        for k in range(n_max):
            for _ in range(ks[k]): pulse.append(k); tt.append(rng.normal(mu, sigma)); sig.append(True)
            for _ in range(kb[k]): pulse.append(k); tt.append(rng.uniform(0, 1)); sig.append(False)
        self.pulse = np.array(pulse); self.t = np.clip(np.array(tt), 0, 0.9999); self.is_sig = np.array(sig)
        self.bin = (self.t * bins).astype(int)
        self.lam_b_per_bin = lam_b / bins
    def counts(self, n):
        i = int(np.searchsorted(self.pulse, int(n), side='left')); return np.bincount(self.bin[:i], minlength=self.bins)
    def smoothed(self, n): c = self.counts(n).astype(float); return np.convolve(c, [0.25, 0.5, 0.25], mode='same')
    def significance(self, n):
        """(argmax bin, z) of the smoothed histogram vs a flat background estimated from the median bin - computed from the data only."""
        c = self.smoothed(n); med = np.median(c); sd = math.sqrt(max(med, 0.25) / 1.0) * 0.8
        j = int(np.argmax(c)); return j, (c[j] - med) / max(sd, 0.5)
    def first_significant(self, z=5.0, step=10):
        for n in range(step, self.n_max + 1, step):
            if self.significance(n)[1] >= z: return n
        return self.n_max


def draw_histogram(cv, hist, n, box=(120, 560, 960, 1180), alpha=1.0, peak_alpha=0.0, peak_pop=0.0, color=T.COOL, dots_until=14):
    """box = (x0,y0,x1,y1); bars grow upward from y1. While the tallest bin has <= dots_until counts the counts are drawn as stacked dots
    (one dot per detection); they cross-fade into bars. peak_alpha draws the data-derived peak marker."""
    x0, y0, x1, y1 = box; B = hist.bins; bw = (x1 - x0) / B; c = hist.counts(n); mx = max(1, c.max()); H = y1 - y0
    pitch = 22.0; unit = min(pitch, H * 0.92 / mx)
    to_bars = smoothstep((mx - dots_until * 0.6) / (dots_until * 0.8))
    cv.line((x0 - 10, y1 + 2), (x1 + 10, y1 + 2), T.GREY, 4, alpha=alpha)
    for i in range(0, 9): cv.line((lerp(x0, x1, i / 8), y1 + 2), (lerp(x0, x1, i / 8), y1 + 18), T.GREY, 3, alpha=alpha)
    for b in range(B):
        if c[b] == 0: continue
        bx = x0 + b * bw
        if to_bars < 1:
            for k in range(min(int(c[b]), int(H / unit))):
                cv.circle((bx + bw / 2, y1 - unit * (k + 0.5)), min(bw * 0.38, unit * 0.42), fill=color, alpha=alpha * (1 - to_bars) * 0.8)
        if to_bars > 0:
            cv.rect((bx + 1.5, y1 - c[b] * unit, bx + bw - 1.5, y1 - 1), fill=T.mix(color, T.WHITE, 0.1), alpha=alpha * to_bars * 0.85, radius=2)
    if peak_alpha > 0:
        j, z = hist.significance(n); px = x0 + (j + 0.5) * bw; ytop = y1 - c.max() * unit - 34 - 18 * peak_pop
        cv.polygon([(px - 15, ytop - 20), (px + 15, ytop - 20), (px, ytop + 4)], fill=T.WHITE, alpha=alpha * peak_alpha)
        cv.line((px, ytop + 10), (px, y1), T.WHITE, 2, alpha=alpha * peak_alpha * 0.35, dash=(8, 8))
    return c
