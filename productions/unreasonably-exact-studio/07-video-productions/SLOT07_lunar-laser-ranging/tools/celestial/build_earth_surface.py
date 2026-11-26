"""EARTH_001 surface + EARTH_004 night lights builders (public-domain NASA inputs in assets/earth/_src).
Run: ~/.venvs/uepipe/bin/python -I tools/celestial/build_earth_surface.py   (-I: do not import from cwd)
Outputs (assets/earth/): earth_surface_4096x2048.png, earth_night_lights_4096x2048.png, _build_report.json
"""
import json, os, sys
import numpy as np, cv2
from PIL import Image
from scipy import ndimage
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noise import fbm, sphere_dirs

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = f'{ROOT}/assets/earth/_src'; OUT = f'{ROOT}/assets/earth'
hexc = lambda s: np.array([int(s[i:i + 2], 16) for i in (1, 3, 5)], np.float32)
OCEAN_DEEP, OCEAN_SHAL, ICE = hexc('#1C5AA8'), hexc('#2C6CC4'), hexc('#E9EEF5')
W, H = 4096, 2048
rep = {}


def smooth(x, a, b):
    t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)


def build_surface():
    west = np.asarray(Image.open(f'{SRC}/bluemarble-west-4096.png').convert('RGB'))
    east = np.asarray(Image.open(f'{SRC}/bluemarble-east-4096.png').convert('RGB'))
    bm = np.concatenate([west, east], 1).astype(np.float32)          # 8192x4096, lon -180..180
    h, w = bm.shape[:2]
    rep['bm_seam_antimeridian_mean_abs_diff_8192'] = float(np.abs(bm[:, 0] - bm[:, -1]).mean())
    rep['bm_seam_join_lon0_mean_abs_diff_8192'] = float(np.abs(bm[:, 4095] - bm[:, 4096]).mean())
    oc_old = np.array([10, 10, 51], np.float32)
    d = np.abs(bm - oc_old).max(-1)
    # BM ocean is one flat colour. Water = d<=3 (lakes included); only a 2-px coastal zone is unmixed. Dark forest is NOT water.
    wet = (d <= 3).astype(np.uint8)
    zone = cv2.dilate(wet, np.ones((5, 5), np.uint8)).astype(bool) & (wet == 0)
    strong = ((d > 60) & ~zone).astype(np.float32)
    # normalised convolution: nearest "pure land" colour, then unmix the coast pixel to a land coverage w
    num = cv2.GaussianBlur(bm * strong[..., None], (0, 0), 3); den = cv2.GaussianBlur(strong, (0, 0), 3)[..., None]
    L = np.where(den > 1e-3, num / np.maximum(den, 1e-3), oc_old)
    v = L - oc_old; wcov = np.clip(((bm - oc_old) * v).sum(-1) / np.maximum((v * v).sum(-1), 1), 0, 1)
    wcov = np.where(wet == 1, 0, np.where(zone, wcov, 1))[..., None]
    # bathymetry cue: luminance of SVS 3615 cloud-free render (bathymetry-shaded), ocean pixels only
    s3615 = np.asarray(Image.open(f'{SRC}/earth_noClouds.0330.tif').convert('RGB')).astype(np.float32)
    lum = s3615 @ np.array([.3, .59, .11], np.float32)
    lum = cv2.resize(lum, (w, h), interpolation=cv2.INTER_CUBIC)
    om = (1 - wcov[..., 0])
    sg = 10
    t = cv2.GaussianBlur(lum * om, (0, 0), sg) / np.maximum(cv2.GaussianBlur(om, (0, 0), sg), 1e-3)
    lat = (90 - (np.arange(h) + .5) / h * 180)[:, None]
    ocean_ok = (np.abs(lat) < 62)
    lo, hi = np.percentile(t[(om > .99) & ocean_ok], [8, 97])
    t = np.clip((t - lo) / (hi - lo), 0, 1); t = np.where(ocean_ok, t, 0) * (1 - smooth(np.abs(lat), 52, 66))
    t = cv2.GaussianBlur(t, (0, 0), 2)
    ocean = OCEAN_DEEP + (OCEAN_SHAL - OCEAN_DEEP) * (t[..., None] ** 1.2)
    # Arctic: BM shows open dark water to the pole (summer). Paint sea ice from sphere noise (pole/seam safe).
    pd_, plat = sphere_dirs(W, H); rows = H // 6
    nz = np.zeros((H, W), np.float32)
    sub = pd_[:, :rows]
    edge = fbm(sub, 3, 5, 11); fine = fbm(sub, 24, 4, 12); crack = 1 - np.abs(fbm(sub, 14, 4, 13))
    latd = np.degrees(plat)[:rows, None]
    ice = smooth(latd + 9 * edge + 2.2 * fine, 77.0, 80.5)     # ragged pack-ice edge near ~78 N
    ice = np.clip(ice, 0, 1)
    icecol = ICE[None, None] * (1 - .035 * smooth(crack, .82, .98)[..., None] * 1.0) + np.array([-8, -4, 4], np.float32) * smooth(crack, .85, .99)[..., None]
    icecol = icecol * (0.985 + .015 * fine[..., None])
    ice_full = np.zeros((h, w), np.float32); ice_full[:h // 6] = cv2.resize(ice, (w, h // 6), interpolation=cv2.INTER_CUBIC)[:h // 6]
    icecol_full = np.tile(ICE, (h, w, 1)); icecol_full[:h // 6] = cv2.resize(icecol.astype(np.float32), (w, h // 6), interpolation=cv2.INTER_CUBIC)
    ocean_layer = ocean * (1 - ice_full[..., None]) + icecol_full * ice_full[..., None]
    out = bm + (1 - wcov) * (ocean_layer - oc_old)
    # Antarctica: BM ice is cream-tinted; pull toward neutral cool ice, keep its texture
    anta = (smooth(-lat, 62, 68) * (bm.mean(-1) > 150))[..., None].astype(np.float32) * wcov
    lum_o = out @ np.array([.3, .59, .11], np.float32)
    ref = np.percentile(lum_o[(anta[..., 0] > .9)], 75)
    cool = ICE[None, None] * np.clip(lum_o[..., None] / ref * .97, .75, 1.04)
    out = out * (1 - .65 * anta) + cool * .65 * anta
    out = cv2.resize(np.clip(out, 0, 255), (W, H), interpolation=cv2.INTER_AREA)   # 8192 -> 4096 area downsample (genuine detail, not an upscale)
    land_mask = cv2.resize(wcov[..., 0], (W, H), interpolation=cv2.INTER_AREA)
    np.save(f'{OUT}/_src/land_mask_4096.npy', land_mask.astype(np.float16))
    rgba = np.dstack([np.clip(out + .5, 0, 255).astype(np.uint8), np.full((H, W), 255, np.uint8)])
    Image.fromarray(rgba).save(f'{OUT}/earth_surface_4096x2048.png', optimize=True)
    a = rgba[..., :3].astype(np.float32)
    rep['surface_seam_col0_vs_col4095_mean_abs_diff'] = float(np.abs(a[:, 0] - a[:, -1]).mean())
    rep['surface_typical_adjacent_col_mean_abs_diff'] = float(np.abs(a[:, 1:] - a[:, :-1]).mean())
    rep['surface_seam_64px_edge_means_diff'] = float(np.abs(a[:, :64].mean((0, 1)) - a[:, -64:].mean((0, 1))).max())
    rep['surface_top_row_std'] = float(a[0].std(0).max()); rep['surface_bottom_row_std'] = float(a[-1].std(0).max())
    return land_mask


def build_lights(land):
    n = np.asarray(Image.open(f'{SRC}/BlackMarble_2016_3km.jpg').convert('RGB')).astype(np.float32)
    R = n[..., 0] * .6 + n[..., 1] * .4              # warm channels; moonlit snow/ice glows blue, so it is rejected here
    bgd = cv2.morphologyEx(cv2.GaussianBlur(R, (0, 0), 1.2), cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    bgd = cv2.GaussianBlur(bgd, (0, 0), 6)
    E = np.clip(R - bgd - 6, 0, None)                  # top-hat: points of light, not the dim moonlit ground
    # snow glow is bluish: suppress where B dominates R strongly and brightness is low
    E *= smooth(n[..., 0] - n[..., 2] + 14, 0, 10) + smooth(R, 70, 110)
    E = np.clip(E, 0, 255) / 255.0
    Es = cv2.resize(E, (W, H), interpolation=cv2.INTER_AREA)
    Em = cv2.resize(cv2.dilate(E, np.ones((3, 3), np.uint8)), (W, H), interpolation=cv2.INTER_AREA)
    I = np.clip((.45 * Es + .55 * Em) * 2.0, 0, 1) ** .8
    land_d = cv2.dilate((land > .08).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(np.float32)
    I = I * cv2.GaussianBlur(land_d, (0, 0), 1.0)      # no lit oceans (gas flares, platforms, boats)
    I = np.where(I < .08, 0, I)
    lat = (90 - (np.arange(H) + .5) / H * 180)[:, None]
    I = I * (lat > -60)                                # no data / noise over Antarctica
    c0, c1 = hexc('#FF9E45'), hexc('#FFE3B8')          # warm orange -> warm white (#FFD9A0 family)
    tt = (I ** 1.3)[..., None]
    rgb = c0 + (c1 - c0) * tt
    rgba = np.dstack([np.where(I[..., None] > 0, rgb, 0), I * 255]).clip(0, 255).astype(np.uint8)
    Image.fromarray(rgba).save(f'{OUT}/earth_night_lights_4096x2048.png', optimize=True)
    rep['lights_nonzero_px'] = int((I > 0).sum()); rep['lights_alpha_max'] = int(rgba[..., 3].max())
    rep['lights_seam_col_alpha_diff'] = float(np.abs(rgba[:, 0, 3].astype(float) - rgba[:, -1, 3]).mean())


if __name__ == '__main__':
    land = build_surface(); build_lights(land)
    json.dump(rep, open(f'{OUT}/_build_report.json', 'w'), indent=1); print(json.dumps(rep, indent=1))
