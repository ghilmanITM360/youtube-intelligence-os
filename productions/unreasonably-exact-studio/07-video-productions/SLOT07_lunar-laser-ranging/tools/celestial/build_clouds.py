"""PLACEHOLDER procedural cloud layer (RGBA, alpha = density, flat-lit #F0F4FA). Authored from multi-octave
3D sphere noise (seam- and pole-safe) with domain warp + latitude bands: equatorial belt, dry subtropics,
mid-latitude storm tracks, thin poles. NOT NASA data. Codex's cloud tiles (EARTH_002) will replace it.
Run: ~/.venvs/uepipe/bin/python -I tools/celestial/build_clouds.py"""
import os, sys, json
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noise import fbm, sphere_dirs
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); OUT = f'{ROOT}/assets/earth'
W, H = 4096, 2048
sm = lambda x, a, b: (lambda t: t * t * (3 - 2 * t))(np.clip((x - a) / (b - a), 0, 1))
p, lat = sphere_dirs(W, H)
lat = np.degrees(lat)[:, None] * np.ones((1, W), np.float32)
al = np.abs(lat)
# domain warp -> swirls; shear with latitude so mid-latitude features stretch along the flow
wv = np.stack([fbm(p, 3.0, 3, 101), fbm(p, 3.0, 3, 202), fbm(p, 3.0, 3, 303)])
q = p + .16 * wv; q /= np.linalg.norm(q, axis=0, keepdims=True)
base = fbm(q, 4.5, 7, 7, gain=.6)                         # big weather systems down to ~3 px detail
detail = fbm(q, 22, 3, 8)
n = base * 2.1 + .35 * detail
band = (.28 * np.exp(-(al / 7) ** 2)                       # equatorial belt
        - .30 * np.exp(-((al - 24) / 9) ** 2)               # dry subtropics
        + .30 * np.exp(-((al - 55) / 12) ** 2)              # storm tracks
        - .55 * sm(al, 72, 90))                             # thin polar cloud
dens = n + band
thr = np.percentile(dens, 52)                      # ~50% sky cover like the Apollo 17 / Blue Marble references
tex = fbm(q, 40, 3, 9)
a = sm(dens, thr - .06, thr + .22) ** 1.2 * (.80 + .20 * sm(tex + .6 * detail, -.4, .4))
a = np.clip(a * 1.02, 0, 1)
col = np.array([0xF0, 0xF4, 0xFA], np.float32)
# soft shading by density only (flat-lit: no directional light baked): dense cores a hair whiter, thin edges a hair bluer
core = sm(dens, thr + .1, thr + .6)[..., None]
rgb = col * (.965 + .035 * core) + np.array([-6, -3, 0], np.float32) * (1 - core)
rgba = np.dstack([np.clip(rgb, 0, 255), a * 255]).astype(np.uint8)
rgba[..., :3][rgba[..., 3] == 0] = 0
Image.fromarray(rgba).save(f'{OUT}/earth_clouds_proc_4096x2048.png', optimize=True)
f = rgba[..., 3].astype(np.float32)
rep = dict(coverage_alpha_mean=float(f.mean() / 255), seam_col_alpha_mean_abs_diff=float(np.abs(f[:, 0] - f[:, -1]).mean()),
           typical_adjacent_col_alpha_mean_abs_diff=float(np.abs(f[:, 1:] - f[:, :-1]).mean()))
print(json.dumps(rep, indent=1)); json.dump(rep, open(f'{OUT}/_clouds_report.json', 'w'), indent=1)
