"""MOON_001 globe builder. Input: SVS 4720 lroc_color_poles_8k.tif (public domain NASA/LRO, 8192x4096).
Output assets/moon/moon_globe_4096x2048.png (opaque RGBA alpha=255) + moon_globe_notes.json + _check/ crops.
Run: ~/.venvs/uepipe/bin/python -I tools/celestial/build_moon.py
Grade only (no baked phase, no limb darkening): luminance remapped into the art-direction palette
(maria #55555D..#6A6A72, highlands #8A8A90..#ACACB0), chroma reduced to 40% + faint cool tint."""
import json, os
import numpy as np, cv2
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); OUT = f'{ROOT}/assets/moon'
W, H = 4096, 2048
A11 = dict(lat=0.67408, lon=23.47297)       # Apollo 11 Tranquility Base, standard published coordinates
TYCHO = dict(lat=-43.31, lon=-11.36)


def px(lon, lat): return (lon + 180) / 360 * W, (90 - lat) / 180 * H


m = np.asarray(Image.open(f'{ROOT}/assets/moon/_src/lroc_color_poles_8k.tif').convert('RGB')).astype(np.float32)
s = cv2.resize(m, (W, H), interpolation=cv2.INTER_AREA)                  # genuine 2:1 area downsample from 8192
lum = s.mean(-1)
xs = [0, 55, 90, 130, 165, 200, 255]; ys = [0, 62, 94, 130, 158, 172, 184]
l2 = np.interp(lum, xs, ys).astype(np.float32)
chroma = (s - lum[..., None]) * (l2 / np.maximum(lum, 1))[..., None] * .4
out = l2[..., None] + chroma + np.array([-2, -2, 3], np.float32) * (l2 / 172)[..., None]
out = np.clip(out, 0, 255).astype(np.uint8)
Image.fromarray(np.dstack([out, np.full((H, W), 255, np.uint8)])).save(f'{OUT}/moon_globe_4096x2048.png', optimize=True)
f = out.astype(np.float32)
x11, y11 = px(**{'lon': A11['lon'], 'lat': A11['lat']}); xt, yt = px(TYCHO['lon'], TYCHO['lat'])
notes = dict(file='moon_globe_4096x2048.png', projection='equirectangular, lon -180..180 left to right, lat +90 top; near side centred at u=0.5 (lon 0)',
             apollo11_lonlat=[A11['lon'], A11['lat']], apollo11_px_4096x2048=[round(x11, 1), round(y11, 1)],
             apollo11_uv=[round(x11 / W, 4), round(y11 / H, 4)], tycho_lonlat=[TYCHO['lon'], TYCHO['lat']], tycho_px=[round(xt, 1), round(yt, 1)],
             seam_col0_vs_col4095_mean_abs_diff=float(np.abs(f[:, 0] - f[:, -1]).mean()), typical_adjacent_col_mean_abs_diff=float(np.abs(f[:, 1:] - f[:, :-1]).mean()),
             lum_percentiles_near_side_1_50_99=[float(v) for v in np.percentile(f[500:1500, 1024:3072].mean(-1), [1, 50, 99])],
             resampling='8192x4096 -> 4096x2048 INTER_AREA (downsample; no upscale)', baked_phase=False, baked_limb_darkening=False)
json.dump(notes, open(f'{OUT}/moon_globe_notes.json', 'w'), indent=1); print(json.dumps(notes, indent=1))
os.makedirs(f'{OUT}/_check', exist_ok=True)
c = Image.fromarray(out).crop((int(x11) - 200, int(y11) - 150, int(x11) + 200, int(y11) + 150)).resize((800, 600), Image.LANCZOS)
d = ImageDraw.Draw(c); cx, cy = 400, 300
d.line([(cx - 40, cy), (cx - 12, cy)], fill=(255, 80, 60), width=2); d.line([(cx + 12, cy), (cx + 40, cy)], fill=(255, 80, 60), width=2)
d.line([(cx, cy - 40), (cx, cy - 12)], fill=(255, 80, 60), width=2); d.line([(cx, cy + 12), (cx, cy + 40)], fill=(255, 80, 60), width=2)
c.save(f'{OUT}/_check/apollo11_locator_crop.png')
Image.fromarray(out).resize((2048, 1024), Image.LANCZOS).save(f'{OUT}/_check/moon_overview_2048.png')
