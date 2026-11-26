"""Supersampled vector-style canvas. All coordinates are design units (1080 x 1920); `scale` picks the output size
(1.0 = 1080x1920 final, 0.5 = 540x960 proof) and `ss` the anti-aliasing supersample factor (shapes are rasterised at
scale*ss and box-filtered down). A similarity transform stack (camera / layer / local) maps world -> design units."""
import math
from contextlib import contextmanager
import numpy as np
from PIL import Image, ImageDraw
from . import tokens as T


def _alpha_mask(mask, alpha):
    if alpha >= 0.999: return mask
    lut = [int(round(v * alpha)) for v in range(256)]
    return mask.point(lut)


class Canvas:
    def __init__(self, scale=0.5, ss=2, bg=None, W=T.DESIGN_W, H=T.DESIGN_H):
        self.scale, self.ss, self.W, self.H = scale, ss, W, H
        self.px = scale * ss                                   # design unit -> working pixel
        self.w, self.h = int(round(W * self.px)), int(round(H * self.px))
        self.out_size = (int(round(W * scale)), int(round(H * scale)))
        self.im = Image.new('RGBA', (self.w, self.h), (bg + (255,)) if bg else (0, 0, 0, 0))
        self.M = np.eye(3)
        self._stack = []

    # ------------------------------------------------------------------ transforms
    @contextmanager
    def xf(self, M):
        """Apply local->parent matrix M (3x3, similarity) for the duration of the block."""
        self._stack.append(self.M); self.M = self.M @ np.asarray(M, float)
        try: yield
        finally: self.M = self._stack.pop()

    @property
    def k(self):
        """uniform scale of the current transform (asserts it is a similarity)."""
        a, b, c, d = self.M[0, 0], self.M[0, 1], self.M[1, 0], self.M[1, 1]
        s = math.sqrt(abs(a * d - b * c))
        assert abs(math.hypot(a, c) - s) < 1e-6 * max(1, s), 'non-similarity transform'
        return s

    def P(self, x, y):
        v = self.M @ np.array([x, y, 1.0]); return (v[0] * self.px, v[1] * self.px)
    def D(self, x, y):
        """design-unit position after the transform stack (for hit tests / placing overlays)."""
        v = self.M @ np.array([x, y, 1.0]); return (float(v[0]), float(v[1]))
    def L(self, d): return d * self.k * self.px                # length in working px

    # ------------------------------------------------------------------ low level stamp
    def _stamp(self, box, fn, color, alpha=1.0):
        x0, y0, x1, y1 = [int(math.floor(box[0])), int(math.floor(box[1])), int(math.ceil(box[2])), int(math.ceil(box[3]))]
        x0, y0, x1, y1 = max(0, x0), max(0, y0), min(self.w, x1), min(self.h, y1)
        if x1 <= x0 or y1 <= y0 or alpha <= 0: return
        mask = Image.new('L', (x1 - x0, y1 - y0), 0)
        fn(ImageDraw.Draw(mask), x0, y0)
        mask = _alpha_mask(mask, alpha)
        patch = Image.new('RGBA', mask.size, tuple(int(c) for c in color) + (255,)); patch.putalpha(mask)
        self.im.alpha_composite(patch, (x0, y0))

    def clear(self, color):
        self.im.paste(tuple(color) + (255,), (0, 0, self.w, self.h))

    def vgradient(self, top, bottom, y0=0, y1=None):
        """vertical gradient over design rows [y0,y1] (screen space, ignores transform)."""
        y1 = self.H if y1 is None else y1
        r0, r1 = int(y0 * self.px), int(y1 * self.px); n = max(1, r1 - r0)
        f = np.linspace(0, 1, n)[:, None, None]
        arr = (np.array(top)[None, None, :] * (1 - f) + np.array(bottom)[None, None, :] * f)
        arr = np.repeat(arr, self.w, axis=1).astype(np.uint8)
        arr = np.concatenate([arr, np.full((n, self.w, 1), 255, np.uint8)], axis=2)
        self.im.paste(Image.fromarray(arr, 'RGBA'), (0, r0))

    # ------------------------------------------------------------------ shapes
    def circle(self, c, r, fill=None, outline=None, width=2, alpha=1.0):
        x, y = self.P(*c); R = self.L(r); wpx = max(1.0, self.L(width)) if outline else 0
        pad = R + wpx + 2
        if fill is not None:
            self._stamp((x - pad, y - pad, x + pad, y + pad), lambda d, ox, oy: d.ellipse([x - R - ox, y - R - oy, x + R - ox, y + R - oy], fill=255), fill, alpha)
        if outline is not None:
            ro = R + wpx / 2
            def f(d, ox, oy):
                d.ellipse([x - ro - ox, y - ro - oy, x + ro - ox, y + ro - oy], fill=255)
                ri = ro - wpx
                if ri > 0: d.ellipse([x - ri - ox, y - ri - oy, x + ri - ox, y + ri - oy], fill=0)
            self._stamp((x - pad, y - pad, x + pad, y + pad), f, outline, alpha)

    def polygon(self, pts, fill=None, outline=None, width=2, alpha=1.0):
        p = [self.P(*q) for q in pts]
        xs, ys = [q[0] for q in p], [q[1] for q in p]
        wpx = self.L(width) if outline else 0; pad = wpx + 2
        box = (min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad)
        if fill is not None:
            self._stamp(box, lambda d, ox, oy: d.polygon([(a - ox, b - oy) for a, b in p], fill=255), fill, alpha)
        if outline is not None:
            self._stamp(box, lambda d, ox, oy: self._pl(d, [(a - ox, b - oy) for a, b in p + [p[0]]], wpx), outline, alpha)

    @staticmethod
    def _pl(d, pts, wpx):
        if len(pts) < 2: return
        d.line(pts, fill=255, width=max(1, int(round(wpx))), joint='curve')
        if wpx > 2.5:
            r = wpx / 2
            for (x, y) in (pts[0], pts[-1]) if len(pts) == 2 else pts:
                d.ellipse([x - r, y - r, x + r, y + r], fill=255)

    def line(self, p0, p1, color=T.WHITE, width=3, alpha=1.0, dash=None, phase=0.0):
        self.polyline([p0, p1], color, width, alpha, dash, phase)

    def polyline(self, pts, color=T.WHITE, width=3, alpha=1.0, dash=None, phase=0.0):
        """dash=(on, off) in design units along the path; phase shifts the pattern (use t*speed for flowing dashes)."""
        if len(pts) < 2: return
        wpx = max(1.0, self.L(width)); pad = wpx + 2
        if dash:
            pieces = self._dashes(pts, dash[0], dash[1], phase)
        else:
            pieces = [pts]
        pp = [[self.P(*q) for q in pc] for pc in pieces if len(pc) >= 2]
        if not pp: return
        xs = [q[0] for pc in pp for q in pc]; ys = [q[1] for pc in pp for q in pc]
        def f(d, ox, oy):
            for pc in pp: self._pl(d, [(a - ox, b - oy) for a, b in pc], wpx)
        self._stamp((min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad), f, color, alpha)

    @staticmethod
    def _dashes(pts, on, off, phase):
        """on-intervals of the dash pattern as sub-polylines (pattern origin shifted forward by `phase` along the path)."""
        P = np.asarray(pts, float); seglen = np.linalg.norm(np.diff(P, axis=0), axis=1); cum = np.concatenate([[0], np.cumsum(seglen)])
        total = cum[-1]; period = on + off; out = []
        s = -(phase % period)
        def at(d):
            i = min(np.searchsorted(cum, d, side='right') - 1, len(seglen) - 1); i = max(i, 0)
            u = (d - cum[i]) / seglen[i] if seglen[i] > 0 else 0
            return P[i] + (P[i + 1] - P[i]) * u, i
        while s < total:
            a_, b_ = max(s, 0.0), min(s + on, total)
            if b_ > a_:
                pa, ia = at(a_); pb, ib = at(b_)
                mid = [tuple(P[j]) for j in range(ia + 1, ib + 1) if a_ < cum[j] < b_]
                out.append([tuple(pa)] + mid + [tuple(pb)])
            s += period
        return out

    def arc(self, c, r, a0, a1, color=T.WHITE, width=3, alpha=1.0, n=48):
        """arc from angle a0 to a1 (radians, screen coords: 0 = +x, positive = clockwise on screen)."""
        m = max(2, int(abs(a1 - a0) / (2 * math.pi) * n) + 2)
        pts = [(c[0] + r * math.cos(a0 + (a1 - a0) * i / (m - 1)), c[1] + r * math.sin(a0 + (a1 - a0) * i / (m - 1))) for i in range(m)]
        self.polyline(pts, color, width, alpha)

    def rect(self, box, fill=None, outline=None, width=2, radius=0, alpha=1.0):
        x0, y0, x1, y1 = box
        if radius <= 0:
            self.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, outline, width, alpha); return
        r = min(radius, (x1 - x0) / 2, (y1 - y0) / 2); pts = []
        for (cx, cy, a) in ((x1 - r, y0 + r, -90), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180)):
            for i in range(9):
                t = math.radians(a + 90 * i / 8); pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
        self.polygon(pts, fill, outline, width, alpha)

    def ellipse(self, c, rx, ry, rot=0.0, fill=None, outline=None, width=2, alpha=1.0, n=64):
        pts = [(c[0] + rx * math.cos(2 * math.pi * i / n) * math.cos(rot) - ry * math.sin(2 * math.pi * i / n) * math.sin(rot),
                c[1] + rx * math.cos(2 * math.pi * i / n) * math.sin(rot) + ry * math.sin(2 * math.pi * i / n) * math.cos(rot)) for i in range(n)]
        self.polygon(pts, fill, outline, width, alpha)

    def dots(self, pts, radii, color, alphas):
        """Many small discs in few stamps (alphas are bucketed to 5 levels): used for star fields and noise dots."""
        P = [self.P(*p) for p in pts]; R = [self.L(r) for r in radii]
        lv = np.clip(np.round(np.asarray(alphas) * 4).astype(int), 0, 4)
        for L_ in range(1, 5):
            idx = [i for i in range(len(P)) if lv[i] == L_ and -20 < P[i][0] < self.w + 20 and -20 < P[i][1] < self.h + 20]
            if not idx: continue
            def f(d, ox, oy, idx=idx):
                for i in idx:
                    x, y = P[i]; r = R[i]; d.ellipse([x - r - ox, y - r - oy, x + r - ox, y + r - oy], fill=255)
            self._stamp((0, 0, self.w, self.h), f, color, L_ / 4)

    # ------------------------------------------------------------------ text
    def text(self, xy, s, size=40, color=T.WHITE, anchor='mm', bold=False, mono=False, alpha=1.0, rot=0.0, math=False):
        x, y = self.P(*xy); f = T.font(size * self.k * self.px, mono, bold, math)
        l, t_, r_, b_ = f.getbbox(s, anchor=anchor); pad = 3
        def fn(d, ox, oy): d.text((x - ox, y - oy), s, font=f, fill=255, anchor=anchor)
        self._stamp((x + l - pad, y + t_ - pad, x + r_ + pad, y + b_ + pad), fn, color, alpha)

    def text_width(self, s, size, bold=False, mono=False, math=False):
        return T.font(size * self.px, mono, bold, math).getlength(s) / self.px          # design units, un-transformed

    # ------------------------------------------------------------------ soft things
    def glow(self, c, r, color, alpha=0.6, power=2.0):
        x, y = self.P(*c); R = self.L(r)
        if R < 1: return
        x0, y0, x1, y1 = int(max(0, x - R)), int(max(0, y - R)), int(min(self.w, x + R + 1)), int(min(self.h, y + R + 1))
        if x1 <= x0 or y1 <= y0: return
        yy, xx = np.mgrid[y0:y1, x0:x1]
        d = np.sqrt((xx - x) ** 2 + (yy - y) ** 2) / R
        a = np.clip(1 - d, 0, 1) ** power * alpha
        arr = np.zeros((y1 - y0, x1 - x0, 4), np.uint8); arr[..., :3] = color; arr[..., 3] = (a * 255).astype(np.uint8)
        self.im.alpha_composite(Image.fromarray(arr, 'RGBA'), (x0, y0))

    def blit_array(self, arr, x0, y0):
        """composite an RGBA uint8 array at working-pixel (x0,y0), clipped."""
        h, w = arr.shape[:2]
        sx0, sy0 = max(0, -x0), max(0, -y0); dx0, dy0 = max(0, x0), max(0, y0)
        dx1, dy1 = min(self.w, x0 + w), min(self.h, y0 + h)
        if dx1 <= dx0 or dy1 <= dy0: return
        self.im.alpha_composite(Image.fromarray(np.ascontiguousarray(arr[sy0:sy0 + dy1 - dy0, sx0:sx0 + dx1 - dx0]), 'RGBA'), (dx0, dy0))

    def blit_image(self, img, alpha=1.0):
        """Warp an RGBA PIL/np image (in design-unit pixel space, 1 px = 1 unit) through the current transform (bitmap layers)."""
        import cv2
        a = np.asarray(img.convert('RGBA'), np.uint8)
        A = (self.M[:2, :] * self.px).astype(np.float32)
        # BORDER_TRANSPARENT without a dst leaves UNINITIALISED memory outside the image (streak bug, 2026-11-26): use constant 0
        out = cv2.warpAffine(a, A, (self.w, self.h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
        if alpha < 1: out[..., 3] = (out[..., 3] * alpha).astype(np.uint8)
        self.im.alpha_composite(Image.fromarray(out, 'RGBA'))

    @contextmanager
    def group(self, alpha=1.0):
        """Draw a sub-scene into a transparent buffer and composite it with group opacity (fade whole assemblies)."""
        parent = self.im
        self.im = Image.new('RGBA', (self.w, self.h), (0, 0, 0, 0))
        try: yield
        finally:
            g = self.im; self.im = parent
            if alpha < 0.999:
                r, gg, b, a = g.split(); g = Image.merge('RGBA', (r, gg, b, _alpha_mask(a, max(0.0, alpha))))
            if alpha > 0: self.im.alpha_composite(g)

    # ------------------------------------------------------------------ output
    def to_image(self):
        im = self.im.convert('RGB') if self.im.getextrema()[3][0] == 255 else self.im
        return im.resize(self.out_size, Image.BOX) if self.ss > 1 else im
