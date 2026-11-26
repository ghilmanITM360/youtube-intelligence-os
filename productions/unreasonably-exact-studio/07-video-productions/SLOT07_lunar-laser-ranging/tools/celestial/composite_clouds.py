"""EARTH_002 cloud layer = Claude's COMPOSITE of Codex's Batch 1 cloud tiles (artwork stays Codex's; placement is Claude's).

Replaces the rejected procedural layer (earth_clouds_proc_4096x2048.png, see ASSET_GENERATION_FAILURE_ROOT_CAUSE_AUDIT.md).
Each stamp is widened by 1/cos(lat) so it reads undistorted on the globe, and pasted with x-wrap so the seam is clean.
Placement follows real climatology loosely: tropical clusters near the equator, frontal bands and cyclones at 30-60 deg,
cirrus anywhere below 65 deg; nothing poleward of 72 deg (the pole pinch). Deterministic (seed 7).

usage: ~/.venvs/uepipe/bin/python tools/celestial/composite_clouds.py
"""
import json, math, os
import numpy as np, cv2
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'codex_handoff', 'deliveries', 'batch1')
OUT = os.path.join(ROOT, 'assets', 'earth', 'earth_clouds_codexcomp_4096x2048.png')
W, H = 4096, 2048
# tile, count, lat range (abs deg), size range (px at the equator), opacity
PLAN = [('cloud_tropical', 16, (0, 14), (300, 460), 0.85),
        ('cloud_frontal', 12, (30, 58), (420, 640), 0.80),
        ('cloud_cyclone', 5, (30, 50), (260, 380), 0.90),
        ('cloud_cirrus', 14, (10, 62), (360, 560), 0.55)]


def load_alpha(name):
    path = os.path.join(SRC, name + '.png')
    if not os.path.exists(path): path = os.path.join(ROOT, 'codex_handoff', 'runs', 'B1c', name + '.png')   # Codex run B1c variants
    a = np.asarray(Image.open(path).convert('RGBA'))[..., 3].astype(np.float32) / 255
    # Codex tiles keep faint alpha up to their borders; a radial feather removes the rectangular stamp edge
    h, w = a.shape; yy, xx = np.mgrid[0:h, 0:w]; r = np.hypot((xx - w / 2) / (w / 2), (yy - h / 2) / (h / 2))
    return a * np.clip((1.0 - r) / 0.25, 0, 1) ** 1.5


def main():
    rng = np.random.default_rng(7)
    land = np.load(os.path.join(ROOT, 'assets', 'earth', '_src', 'land_mask_4096.npy'))
    land = cv2.resize(land.astype(np.float32), (W, H), interpolation=cv2.INTER_AREA) if land.shape != (H, W) else land.astype(np.float32)
    def over_land(lon, lat): return land[int((0.5 - lat / 180) * (H - 1)), int(lon / 360 * (W - 1))] > 0.5
    acc = np.zeros((H, W), np.float32); log = []
    for name, n, (la0, la1), (s0, s1), op in PLAN:
        tiles = [load_alpha(t) for t in ([name, 'cloud_cyclone_b', 'cloud_cyclone_c'] if name == 'cloud_cyclone' else [name])]
        for k_ in range(n):
            tile = tiles[k_ % len(tiles)]                                                  # cyclone variants rotate so no two storms are clones
            while True:                                                                    # cyclones and tropical clusters only over ocean
                lat = rng.uniform(la0, la1) * rng.choice([-1, 1]); lon = rng.uniform(0, 360)
                if name in ('cloud_cirrus', 'cloud_frontal') or not over_land(lon, lat): break
            s = rng.uniform(s0, s1); rot = rng.uniform(0, 360)
            if name == 'cloud_cyclone' and lat < 0: tile_use = tile[:, ::-1]          # southern cyclones spin the other way
            else: tile_use = tile
            M = cv2.getRotationMatrix2D((tile.shape[1] / 2, tile.shape[0] / 2), rot if name != 'cloud_cyclone' else rot * 0.2, 1.0)
            t = cv2.warpAffine(tile_use, M, tile.shape[::-1])
            sx = s * min(2.5, 1 / math.cos(math.radians(lat))); sy = s
            t = cv2.resize(t, (int(sx), int(sy)), interpolation=cv2.INTER_AREA) * op
            cx = lon / 360 * W; cy = (0.5 - lat / 180) * H
            x0, y0 = int(cx - t.shape[1] / 2), int(cy - t.shape[0] / 2)
            for dx in (-W, 0, W):                                                        # wrap in longitude
                xa, ya = max(0, x0 + dx), max(0, y0); xb, yb = min(W, x0 + dx + t.shape[1]), min(H, y0 + t.shape[0])
                if xb <= xa or yb <= ya: continue
                sub = t[ya - y0:yb - y0, xa - x0 - dx:xb - x0 - dx]
                acc[ya:yb, xa:xb] = 1 - (1 - acc[ya:yb, xa:xb]) * (1 - sub)             # alpha 'over'
            log.append(dict(tile=name, lat=round(float(lat), 1), lon=round(float(lon), 1), size=round(float(s)), rot=round(float(rot))))
    lat_rows = np.abs(90 - (np.arange(H) + 0.5) / H * 180)
    acc *= np.clip((72 - lat_rows) / 8, 0, 1)[:, None]                                  # fade out toward the poles
    rgba = np.zeros((H, W, 4), np.uint8); rgba[..., :3] = (240, 244, 250); rgba[..., 3] = np.clip(acc * 255, 0, 255)
    Image.fromarray(rgba).save(OUT)
    seam = float(np.abs(acc[:, 0] - acc[:, -1]).mean() * 255); adj = float(np.abs(np.diff(acc, axis=1)).mean() * 255)
    rep = dict(file=os.path.basename(OUT), stamps=len(log), coverage=round(float((acc > 0.2).mean()), 3),
               seam_col0_vs_last_mean_abs=round(seam, 3), typical_adjacent_col_mean_abs=round(adj, 3),
               source_tiles='codex_handoff/deliveries/batch1/cloud_*.png (Codex, CANDIDATE)', placements=log)
    json.dump(rep, open(OUT.replace('.png', '_report.json'), 'w'), indent=1)
    assert seam < 3 * adj + 0.5, 'longitude seam visible'
    print({k: v for k, v in rep.items() if k != 'placements'})


if __name__ == '__main__':
    main()
