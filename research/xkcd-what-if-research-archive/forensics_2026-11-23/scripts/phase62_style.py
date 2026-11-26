"""Phase 6.2 style measurements on the 125 viewed science frames (native-resolution frames re-extracted from the library MP4 at the coded timestamp).
Per frame: background colour, ink / red / other-accent / grey area shares, stroke width (2 x median distance-transform value on the ink skeleton), connected-component density,
negative space (share of 48x48-px grid cells containing no non-background pixel), label-sized component height. All thresholds are written below; this is MEASUREMENT of pixels, not interpretation.
usage: uv run --no-project --with numpy --with pillow --with scipy --with scikit-image python scripts/phase62_style.py"""
import csv, os, subprocess, json, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage.morphology import skeletonize
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = A + '/phase62_style'; os.makedirs(OUT + '/frames', exist_ok=True)
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
srcs = [('07_SAMPLE_FRAMES.csv', 'p7_code'), ('07_HOLDOUT_FRAMES.csv', 'p7_holdout'), ('07b_SAMPLE_FRAMES.csv', 'p7b'), ('07c_SAMPLE_FRAMES.csv', 'p7c')]
items = []
for f, tag in srcs:
    for r in csv.DictReader(open(A + '/' + f)): items.append((r['video_id'], float(r['t']), tag))
def grab(v, t):
    jp = f'{OUT}/frames/{v}_{t:.2f}.jpg'
    if not os.path.exists(jp):
        tmp = f'{OUT}/frames/_tmp.png'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.3f}', '-i', inv[v]['local_media_path'], '-frames:v', '1', tmp], check=True)
        Image.open(tmp).convert('RGB').save(jp, quality=88); os.remove(tmp)
    return jp
def measure(jp):
    im = np.asarray(Image.open(jp).convert('RGB')).astype(np.int16); H, W, _ = im.shape
    q = (im // 16).reshape(-1, 3); key = q[:, 0] * 256 + q[:, 1] * 16 + q[:, 2]
    vals, cnt = np.unique(key, return_counts=True); bgk = vals[cnt.argmax()]; bg = tuple(int(x) * 16 + 8 for x in (bgk // 256, (bgk // 16) % 16, bgk % 16))
    bg_share = float(cnt.max()) / key.size
    mx = im.max(2); mn = im.min(2); sat = (mx - mn) / np.maximum(mx, 1); lum = (0.299 * im[..., 0] + 0.587 * im[..., 1] + 0.114 * im[..., 2])
    bgd = np.abs(im - np.array(bg)).sum(2)  # distance from the dominant background colour
    nonbg = bgd > 60
    bg_lum = 0.299 * bg[0] + 0.587 * bg[1] + 0.114 * bg[2]; dark_bg = bg_lum < 80
    ink = nonbg & (sat < 0.25) & ((lum > 150) if dark_bg else (lum < 110))  # ink polarity follows the background (white-on-black frames exist)
    red = nonbg & (im[..., 0] > 140) & (im[..., 1] < 110) & (im[..., 2] < 110) & (sat > 0.45)
    other = nonbg & (sat > 0.45) & (mx > 90) & ~red
    grey = nonbg & (sat < 0.25) & (lum >= 110)
    n = H * W
    lab, nc = ndi.label(ndi.binary_dilation(ink, iterations=2))
    sk = skeletonize(ink); dt = ndi.distance_transform_edt(ink)
    skt = sk & (dt <= 8)  # thin strokes only; skeleton points inside filled regions (dt>8) are excluded
    sw = float(2 * np.median(dt[skt])) if skt.sum() > 50 else float('nan')
    fill_share = float((dt > 8).sum()) / max(1, int(ink.sum()))
    rsk = skeletonize(red); rdt = ndi.distance_transform_edt(red); rsk = rsk & (rdt <= 8); rsw = float(2 * np.median(rdt[rsk])) if rsk.sum() > 50 else float('nan')
    g = 48; gh, gw = H // g, W // g; cells = nonbg[:gh * g, :gw * g].reshape(gh, g, gw, g).any(axis=(1, 3)); neg = 1 - float(cells.mean())
    objs = ndi.find_objects(lab); hts = [s[0].stop - s[0].start for s in objs if s is not None]; small = [h for h in hts if 10 <= h <= 90]
    ys, xs = np.where(nonbg); bbox = (float((xs.max() - xs.min()) * (ys.max() - ys.min())) / n) if len(xs) else 0
    return dict(width=W, height=H, bg_rgb='%d,%d,%d' % bg, bg_share=round(bg_share, 3), nonbg_share=round(float(nonbg.mean()), 4), ink_share=round(float(ink.mean()), 4), red_share=round(float(red.mean()), 4),
                other_accent_share=round(float(other.mean()), 4), grey_share=round(float(grey.mean()), 4), dark_bg=int(dark_bg), fill_share_of_ink=round(fill_share, 3), stroke_px=round(sw, 2), red_stroke_px=round(rsw, 2), ink_components=int(nc),
                negative_space=round(neg, 3), nonbg_bbox_share=round(bbox, 3), label_comp_median_h=(float(np.median(small)) if small else float('nan')), label_comps=len(small))
rows = []
for i, (v, t, tag) in enumerate(items):
    jp = grab(v, t); m = measure(jp)
    rows.append(dict(video_id=v, t_s=t, set=tag, fmt=inv[v]['format'], frame_ref=os.path.relpath(jp, A), **m))
    if i % 20 == 0: print(i, v, m['stroke_px'], file=sys.stderr)
w = csv.DictWriter(open(A + '/06_STYLE_MEASUREMENTS_125.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), 'frames', len({r['video_id'] for r in rows}), 'videos')
