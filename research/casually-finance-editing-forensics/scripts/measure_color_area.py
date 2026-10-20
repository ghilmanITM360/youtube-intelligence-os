#!/usr/bin/env python3
"""Per-frame area of a colour (default: yellow highlighter) inside the stage rows (MEASURED, appearance-based).

Usage: python3 -E measure_color_area.py <vid> [rows=0.30:0.665] [color=yellow|orange|red] [min_px=40] [segments=f0:f1,f0:f1]
Decodes the source at 180 px width (passthrough), counts matching pixels per frame, and writes
videos/<vid>/motion/color_<color>.json: per-frame counts plus "runs" (contiguous spans with a count change >= min_px,
with start/end counts) so highlight appear / grow / disappear frames can be cited. The gray stage detector misses slow
highlight growth because each frame changes by only a few pixels.
"""
import json
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_sheet as ms  # noqa: E402

PRED = {
    "yellow": lambda a: (a[..., 0] > 200) & (a[..., 1] > 170) & (a[..., 2] < 150) & (a[..., 0].astype(int) - a[..., 2] > 70),
    "orange": lambda a: (a[..., 0] > 200) & (a[..., 1] > 100) & (a[..., 1] < 190) & (a[..., 2] < 100) & (a[..., 0].astype(int) - a[..., 1] > 40),
    "red": lambda a: (a[..., 0] > 150) & (a[..., 1] < 70) & (a[..., 2] < 70),
}


def main():
    vid = sys.argv[1]
    rows = [float(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "0.30:0.665").split(":")]
    color = sys.argv[3] if len(sys.argv) > 3 else "yellow"
    min_px = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    src, fps = ms.source(vid)
    w, h = 180, 320
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-fps_mode", "passthrough", "-vf", "scale=%d:%d" % (w, h), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       capture_output=True, check=True)
    fr = np.frombuffer(p.stdout, np.uint8).reshape(-1, h, w, 3)
    y0, y1 = int(rows[0] * h), int(rows[1] * h)
    cnt = [int(PRED[color](f[y0:y1]).sum()) for f in fr]
    runs, i = [], 1
    while i < len(cnt):
        if abs(cnt[i] - cnt[i - 1]) > 0:
            j = i
            while j + 1 < len(cnt) and abs(cnt[j + 1] - cnt[j]) > 0:
                j += 1
            if abs(cnt[j] - cnt[i - 1]) >= min_px:
                runs.append({"f0": i, "f1": j, "count_before": cnt[i - 1], "count_after": cnt[j], "frames": j - i + 1})
            i = j + 1
        else:
            i += 1
    segs = []
    for sp in (sys.argv[5].split(",") if len(sys.argv) > 5 else []):
        a, b = [int(x) for x in sp.split(":")]
        c = np.array(cnt[a:b])
        m = int(c.max())
        if m <= 0:
            segs.append({"f0": a, "f1": b, "max_count": 0})
            continue
        d_ = np.diff(c)
        segs.append({"f0": a, "f1": b, "max_count": m, "first_frame": a + int(np.argmax(c > 0.05 * m)), "f95": a + int(np.argmax(c >= 0.95 * m)),
                     "monotone_fraction": round(float((d_ >= 0).sum() / max(1, (d_ != 0).sum() + (d_ == 0).sum())), 3)})
    out = {"kind": "color_area", "video_id": vid, "color": color, "analysis_px": [w, h], "stage_rows": rows, "fps": fps, "frames": len(cnt), "min_px": min_px,
           "runs": runs, "segments": segs, "counts": cnt}
    d = os.path.join(ms.RDIR, "videos", vid, "motion")
    os.makedirs(d, exist_ok=True)
    fn = os.path.join(d, "color_%s.json" % color)
    json.dump(out, open(fn, "w"))
    print(fn)
    for r in runs:
        print(r)
    for sg in segs:
        print(sg)


if __name__ == "__main__":
    main()
