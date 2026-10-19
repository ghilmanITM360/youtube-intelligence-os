#!/usr/bin/env python3
"""Measure continuous motion in a frame window and fit easing (MEASURED, appearance-based).

Usage:
  python3 -E measure_motion.py camera <vid> <ev_root> <f0> <f1> [rows=y0:y1]   # zoom/pan of a flat image
  python3 -E measure_motion.py blob   <vid> <ev_root> <f0> <f1> <color> [rows] # single-colour pointer/element path
  python3 -E measure_motion.py extent <vid> <ev_root> <f0> <f1> [rows]         # ink bbox growth (write-on / reveal)
Writes videos/<vid>/motion/<kind>_<f0>_<f1>.json with per-frame curves and easing fits.

camera: per consecutive frame pair, brute-force the best isotropic scale s about the stage centre, then phase-correlate
the residual translation. Cumulative scale S(t) and the tracked image centre give measured keyframes.
Easing is fitted on normalised progress p(u), u=(t-t0)/(t1-t0), against linear / ease-in / ease-out / ease-in-out (smoothstep).
Caveat: 30 fps sampling, 180-px analysis size; fits with fewer than 8 moving samples are flagged LOW_SAMPLE.
"""
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image

RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EASES = {
    "linear": lambda u: u,
    "ease_in_quad": lambda u: u * u,
    "ease_out_quad": lambda u: 1 - (1 - u) ** 2,
    "ease_in_out_smoothstep": lambda u: u * u * (3 - 2 * u),
    "ease_out_cubic": lambda u: 1 - (1 - u) ** 3,
}


def fit_easing(t, v):
    """t seconds, v measured value. Returns best-fit family on normalised progress and all RMSEs."""
    t = np.asarray(t, float)
    v = np.asarray(v, float)
    if len(t) < 4 or abs(v[-1] - v[0]) < 1e-9:
        return {"best": "UNDETERMINED", "reason": "too few samples or no net change"}
    u = (t - t[0]) / (t[-1] - t[0])
    p = (v - v[0]) / (v[-1] - v[0])
    res = {k: float(np.sqrt(np.mean((p - f(u)) ** 2))) for k, f in EASES.items()}
    best = min(res, key=res.get)
    srt = sorted(res.values())
    return {"best": best, "rmse": {k: round(x, 4) for k, x in res.items()},
            "margin_over_second": round(srt[1] - srt[0], 4),
            "confidence": "LOW_SAMPLE" if len(t) < 8 else ("AMBIGUOUS" if srt[1] - srt[0] < 0.02 else "SUPPORTED"),
            "n_samples": int(len(t))}


def scale_about_centre(img, s):
    h, w = img.shape
    im = Image.fromarray(img)
    cx, cy = w / 2.0, h / 2.0
    # output(x) = input(cx + (x-cx)/s)
    a = 1.0 / s
    return np.asarray(im.transform((w, h), Image.AFFINE, (a, 0, cx - a * cx, 0, a, cy - a * cy), Image.BICUBIC, fillcolor=255), np.float32)


def phase_corr(a, b):
    win = np.outer(np.hanning(a.shape[0]), np.hanning(a.shape[1]))
    A = np.fft.fft2((a - a.mean()) * win)
    B = np.fft.fft2((b - b.mean()) * win)
    R = A * np.conj(B)
    R /= np.abs(R) + 1e-9
    r = np.real(np.fft.ifft2(R))
    iy, ix = np.unravel_index(np.argmax(r), r.shape)
    h, w = r.shape
    # sub-pixel parabola refinement
    def refine(arr, i, n):
        l, c, rr = arr[(i - 1) % n], arr[i], arr[(i + 1) % n]
        den = l - 2 * c + rr
        return 0.0 if abs(den) < 1e-12 else 0.5 * (l - rr) / den
    dy = iy + refine(r[:, ix], iy, h)
    dx = ix + refine(r[iy, :], ix, w)
    if dy > h / 2:
        dy -= h
    if dx > w / 2:
        dx -= w
    return dx, dy, float(r[iy, ix])


def reg_pair(prev, cur, grid):
    best = None
    for s in grid:
        ps = scale_about_centre(prev, s) if abs(s - 1) > 1e-6 else prev.astype(np.float32)
        dx, dy, pk = phase_corr(cur.astype(np.float32), ps)
        if best is None or pk > best[3]:
            best = (s, dx, dy, pk)
    return best


def camera(vid, ev_root, f0, f1, rows):
    g = np.load(os.path.join(ev_root, vid, "gray.npy"))
    h, w = g.shape[1:]
    y0, y1 = int(rows[0] * h), int(rows[1] * h)
    seq = g[f0:f1 + 1, y0:y1, :]
    grid = np.linspace(0.96, 1.06, 41)
    out = []
    S, cx, cy = 1.0, 0.0, 0.0  # tracked point: initial stage-centre offset from stage-centre
    px, py = 0.0, 0.0
    for k in range(1, len(seq)):
        s, dx, dy, pk = reg_pair(seq[k - 1], seq[k], grid)
        # tracked point p (relative to stage centre): p' = s*p + d
        px, py = s * px + dx, s * py + dy
        S *= s
        out.append({"frame": f0 + k, "pair_scale": round(float(s), 4), "dx_px": round(float(dx), 2), "dy_px": round(float(dy), 2),
                    "peak": round(pk, 3), "S_cum": round(float(S), 4), "centre_dx_px": round(float(px), 2), "centre_dy_px": round(float(py), 2)})
    fps = json.load(open(os.path.join(RDIR, "videos", vid, "auto", "AUTO_SUMMARY.json")))["fps"]
    t = [(o["frame"] - f0) / fps for o in out]
    moving = [o for o in out if abs(o["pair_scale"] - 1) > 0.0004 or abs(o["dx_px"]) > 0.15 or abs(o["dy_px"]) > 0.15]
    res = {"kind": "camera", "video_id": vid, "f0": f0, "f1": f1, "analysis_px": [w, h], "stage_rows": rows, "fps": fps,
           "curves": out, "moving_pairs": len(moving),
           "scale_fit": fit_easing(t, [o["S_cum"] for o in out]),
           "pan_x_fit": fit_easing(t, [o["centre_dx_px"] for o in out]),
           "pan_y_fit": fit_easing(t, [o["centre_dy_px"] for o in out]),
           "net": {"scale": out[-1]["S_cum"], "dx_px_analysis": out[-1]["centre_dx_px"], "dy_px_analysis": out[-1]["centre_dy_px"]}}
    return res


def rgb_frames(vid, f0, f1):
    inv = os.path.join(RDIR, "SOURCE_MEDIA_INVENTORY.csv")
    import csv
    r = [x for x in csv.DictReader(open(inv)) if x["Video_ID"] == vid and x["Canonical_For_Analysis"] == "True"][0]
    src = os.path.join("/Users/ghilmankhan/Downloads/CasuallyFinance", r["Relative_Path"])
    W, H = int(r["Width"]), int(r["Height"])
    tw, th = (180, int(round(180 * H / W))) if H >= W else (int(round(180 * W / H)), 180)
    cmd = ["ffmpeg", "-v", "error", "-i", src, "-vf", "select='between(n,%d,%d)',scale=%d:%d:flags=area" % (f0, f1, tw, th),
           "-fps_mode", "passthrough", "-pix_fmt", "rgb24", "-f", "rawvideo", "-"]
    b = subprocess.run(cmd, capture_output=True).stdout
    n = len(b) // (tw * th * 3)
    return np.frombuffer(b, np.uint8).reshape(n, th, tw, 3), tw, th


COLORS = {
    "red": lambda a: (a[..., 0] > 140) & (a[..., 1] < 70) & (a[..., 2] < 80),
    "orange": lambda a: (a[..., 0] > 170) & (a[..., 1] > 90) & (a[..., 1] < 190) & (a[..., 2] < 110) & (a[..., 0] - a[..., 2] > 100),
    "green": lambda a: (a[..., 1] > 150) & (a[..., 0] < 120) & (a[..., 2] < 130),
}


def blob(vid, ev_root, f0, f1, color, rows):
    fr, w, h = rgb_frames(vid, f0, f1)
    y0, y1 = int(rows[0] * h), int(rows[1] * h)
    fps = json.load(open(os.path.join(RDIR, "videos", vid, "auto", "AUTO_SUMMARY.json")))["fps"]
    out = []
    for k in range(len(fr)):
        m = COLORS[color](fr[k][y0:y1].astype(np.int16))
        ys, xs = np.where(m)
        if len(xs) < 3:
            out.append({"frame": f0 + k, "n": int(len(xs)), "cx": None, "cy": None})
            continue
        out.append({"frame": f0 + k, "n": int(len(xs)), "cx": round(float(xs.mean() / w), 4), "cy": round(float((ys.mean() + y0) / h), 4),
                    "x0": round(float(xs.min() / w), 4), "x1": round(float((xs.max() + 1) / w), 4), "y0": round(float((ys.min() + y0) / h), 4),
                    "y1": round(float((ys.max() + 1 + y0) / h), 4)})
    ok = [o for o in out if o["cx"] is not None]
    t = [(o["frame"] - f0) / fps for o in ok]
    return {"kind": "blob", "color": color, "video_id": vid, "f0": f0, "f1": f1, "fps": fps, "curves": out,
            "x_fit": fit_easing(t, [o["cx"] for o in ok]) if ok else None,
            "y_fit": fit_easing(t, [o["cy"] for o in ok]) if ok else None,
            "extent_fit": fit_easing(t, [o["n"] for o in ok]) if ok else None}


def extent(vid, ev_root, f0, f1, rows):
    g = np.load(os.path.join(ev_root, vid, "gray.npy"))
    h, w = g.shape[1:]
    y0, y1 = int(rows[0] * h), int(rows[1] * h)
    fps = json.load(open(os.path.join(RDIR, "videos", vid, "auto", "AUTO_SUMMARY.json")))["fps"]
    out = []
    for k in range(f0, f1 + 1):
        m = g[k, y0:y1] < 235
        ys, xs = np.where(m)
        out.append({"frame": k, "ink_px": int(m.sum()), "x0": round(float(xs.min() / w), 4) if len(xs) else None,
                    "x1": round(float((xs.max() + 1) / w), 4) if len(xs) else None,
                    "y0": round(float((ys.min() + y0) / h), 4) if len(xs) else None,
                    "y1": round(float((ys.max() + 1 + y0) / h), 4) if len(xs) else None})
    t = [(o["frame"] - f0) / fps for o in out]
    return {"kind": "extent", "video_id": vid, "f0": f0, "f1": f1, "fps": fps, "curves": out,
            "ink_fit": fit_easing(t, [o["ink_px"] for o in out])}


def main():
    kind, vid, ev_root, f0, f1 = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    rest = sys.argv[6:]
    parse_rows = lambda s: [float(x) for x in s.split(":")]
    if kind == "camera":
        rows = parse_rows(rest[0]) if rest else [0.30, 0.665]
        res = camera(vid, ev_root, f0, f1, rows)
    elif kind == "blob":
        rows = parse_rows(rest[1]) if len(rest) > 1 else [0.30, 0.665]
        res = blob(vid, ev_root, f0, f1, rest[0], rows)
    else:
        rows = parse_rows(rest[0]) if rest else [0.30, 0.665]
        res = extent(vid, ev_root, f0, f1, rows)
    od = os.path.join(RDIR, "videos", vid, "motion")
    os.makedirs(od, exist_ok=True)
    p = os.path.join(od, "%s_%d_%d.json" % (kind, f0, f1))
    json.dump(res, open(p, "w"), indent=1)
    keys = [k for k in res if k.endswith("_fit") or k == "net"]
    print(p)
    for k in keys:
        v = res[k]
        print(" ", k, json.dumps(v)[:300])


if __name__ == "__main__":
    main()
