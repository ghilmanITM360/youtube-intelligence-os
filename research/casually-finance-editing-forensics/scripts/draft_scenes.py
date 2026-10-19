#!/usr/bin/env python3
"""Print candidate scene boundaries: frames where the stage band changes by >= MINPX pixels in one frame.
Usage: python3 -E draft_scenes.py <video_id> <local_evidence_root> [minpx=2500]"""
import json, os, sys
import numpy as np
RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vid, ev = sys.argv[1], sys.argv[2]
minpx = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
g = np.load(os.path.join(ev, vid, "gray.npy")).astype(np.int16)
b = json.load(open(os.path.join(RDIR, "videos", vid, "auto", "bands.json")))
n, h, w = g.shape
a0, a1 = int(b["stage"][0] * h), int(b["stage"][1] * h)
px = [0] + [int((np.abs(g[i, a0:a1] - g[i - 1, a0:a1]) > 16).sum()) for i in range(1, n)]
c = [(i, px[i]) for i in range(1, n) if px[i] >= minpx]
runs = []
for i, v in c:
    if runs and i - runs[-1][1] <= 2:
        runs[-1][1] = i; runs[-1][2] = max(runs[-1][2], v); runs[-1][3] += 1
    else:
        runs.append([i, i, v, 1])
print("frames=%d stage px=%d; change runs>=%d (start-end,peak,len; len 1 = cut candidate):" % (n, (a1 - a0) * w, minpx))
print(" ".join(("%d(%d)" % (a, v)) if l == 1 else ("%d-%d(%d)" % (a, b, v)) for a, b, v, l in runs))
