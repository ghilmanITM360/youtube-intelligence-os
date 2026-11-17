#!/usr/bin/env python3
"""One-line layout profile to choose banded (segment_events.py + bands.json) vs full-bleed (segment_full.py) analysis."""
import sys, numpy as np
g = np.load("%s/%s/gray.npy" % (sys.argv[2], sys.argv[1]))
n, h, w = g.shape
d = np.abs(np.diff(g.astype(np.int16), axis=0)) > 16
ra = d.mean((0, 2)); ink = (g < 200).mean((0, 2)); b = h // 20
print("row act x1e3:", [round(float(ra[i*b:(i+1)*b].mean()*1000), 1) for i in range(20)])
print("row ink  x1e2:", [round(float(ink[i*b:(i+1)*b].mean()*100), 1) for i in range(20)])
zero = [round(i / 20, 2) for i in range(20) if ra[i*b:(i+1)*b].mean() < 1e-5 and ink[i*b:(i+1)*b].mean() > 0.01]
print("rows with ink but zero activity (persistent header/frame) at y:", zero or "none -> likely FULL-BLEED")
fr = d.mean((1, 2))
print("frames>0.3%% changed: %d of %d; cuts(>=20%%): %d" % ((fr > 0.003).sum(), n - 1, int((fr >= 0.20).sum())))
