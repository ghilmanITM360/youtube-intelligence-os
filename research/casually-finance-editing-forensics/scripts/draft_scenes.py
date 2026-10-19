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
print("stage px=%d; boundaries>=%d:" % ((a1 - a0) * w, minpx), " ".join("%d(%d)" % x for x in c))
