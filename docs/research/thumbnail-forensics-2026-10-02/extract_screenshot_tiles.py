"""Detect full 16:9 video tiles in the competitor channel-page screenshots and save lossless PNG crops.

Detection is geometric only (page-background difference + aspect ratio). Video mapping is NOT done here;
it is done by visual title reading and recorded in screenshot-thumbnail-register.csv.
Crops live in a local-only raw dir; coordinates + hashes are tracked so crops are reproducible.
"""
import csv, hashlib, glob, sys
from pathlib import Path
import cv2, numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CROPS = ROOT / 'data/raw/competitors/screenshot-crops-2026-10-04'
SHEETS = ROOT / 'data/raw/competitors/screenshot-crops-2026-10-04/_sheets'


def tiles(im):
    H, W = im.shape[:2]
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    reg = g[int(H * .55):int(H * .95), int(W * .2):int(W * .95)]
    bg = np.bincount(reg.ravel()).argmax()
    m = (np.abs(g.astype(int) - bg) > 20).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out = []
    for c in cs:
        x, y, w, h = cv2.boundingRect(c)
        if W * 0.08 < w < W * 0.6 and 1.6 < w / h < 1.95 and cv2.contourArea(c) > 0.8 * w * h:
            out.append((x, y, w, h))
    return sorted(out, key=lambda t: (round(t[1] / 100), t[0]))


if __name__ == '__main__':
    inv = [r for r in csv.DictReader((HERE / 'asset-inventory.csv').open()) if r['role'] == 'SCREENSHOT_PENDING_THUMBNAIL_EXTRACTION']
    CROPS.mkdir(parents=True, exist_ok=True); SHEETS.mkdir(exist_ok=True)
    rows = []
    for i, r in enumerate(sorted(inv, key=lambda r: r['location']), 1):
        sid = f'SS-{i:03d}'
        im = cv2.imread(str(ROOT / r['location']))
        assert hashlib.sha256((ROOT / r['location']).read_bytes()).hexdigest() == r['sha256']
        sheet = []
        for j, (x, y, w, h) in enumerate(tiles(im), 1):
            crop = im[y:y + h, x:x + w]
            ok, buf = cv2.imencode('.png', crop)
            sha = hashlib.sha256(buf.tobytes()).hexdigest()
            p = CROPS / f'{sid}-T{j:02d}.png'
            p.write_bytes(buf.tobytes())
            rows.append(dict(Screenshot_Source_ID=sid, Screenshot_Path=r['location'], Screenshot_SHA256=r['sha256'], Tile=f'T{j:02d}',
                             X=x, Y=y, W=w, H=h, Crop_Path=str(p.relative_to(ROOT)), Crop_SHA256=sha))
            title = im[y + h:y + h + int(h * .42), x:x + w]
            sheet.append(np.vstack([cv2.resize(crop, (480, int(480 * h / w))), cv2.resize(title, (480, int(480 * title.shape[0] / w)))]))
        if sheet:
            cols = 3
            hh = max(s.shape[0] for s in sheet)
            padded = [cv2.copyMakeBorder(s, 0, hh - s.shape[0], 0, 6, cv2.BORDER_CONSTANT, value=(40, 40, 40)) for s in sheet]
            while len(padded) % cols: padded.append(np.zeros_like(padded[0]))
            grid = np.vstack([np.hstack(padded[k:k + cols]) for k in range(0, len(padded), cols)])
            cv2.imwrite(str(SHEETS / f'{sid}.jpg'), grid, [cv2.IMWRITE_JPEG_QUALITY, 85])
    with (HERE / 'screenshot-tiles-detected.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(inv), 'screenshots', len(rows), 'tiles')
