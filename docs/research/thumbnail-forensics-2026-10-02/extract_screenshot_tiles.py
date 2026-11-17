"""Detect full 16:9 video tiles in the competitor channel-page screenshots and save lossless PNG crops.

v2 (2026-10-04): a first geometric pass (page-background difference + aspect ratio) misses tiles with dark
artwork, so the detected tiles are used to infer each window layout's grid (tile size, column x positions,
row pitch), and every fully visible grid cell is added. Rows are snapped to the strongest horizontal edge.
Video mapping is NOT done here: titles are OCR-read from the strip under each tile (Apple Vision, local) and
matched to the canonical registry in map_screenshot_tiles.py.
Crops live in a local-only raw dir; coordinates + hashes are tracked so crops are reproducible.
"""
import csv, hashlib
from collections import Counter, defaultdict
from pathlib import Path
import cv2, numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CROPS = ROOT / 'data/raw/competitors/screenshot-crops-2026-10-04'
SHEETS = CROPS / '_sheets'
BOTTOM_BANNER = 0.905  # "You're a manager" bar; tiles below this line are partial


def detect(im):
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
        if W * 0.08 < w < W * 0.6 and 1.6 < w / h < 1.95 and cv2.contourArea(c) > 0.8 * w * h: out.append((x, y, w, h))
    return out, g, bg


def snap_row(g, y, x, w, h):
    """Snap a predicted tile top to the strongest bg->content edge within +-45 px."""
    best, by = -1, y
    for yy in range(max(0, y - 45), min(g.shape[0] - h, y + 45)):
        e = np.abs(g[yy + 4, x + 20:x + w - 20].astype(int) - g[yy - 4, x + 20:x + w - 20].astype(int)).mean() if yy > 4 else 0
        if e > best: best, by = e, yy
    return by


def grid_tiles(inv):
    per, layout = {}, defaultdict(list)
    ims = {}
    for sid, r in inv.items():
        im = cv2.imread(str(ROOT / r['location'])); ims[sid] = im
        d, g, bg = detect(im)
        per[sid] = d
        layout[im.shape[1]].extend(d)
    out = {}
    for sid, r in inv.items():
        im = ims[sid]; H, W = im.shape[:2]; d = per[sid]
        if not d: out[sid] = []; continue
        w = int(np.median([t[2] for t in d])); h = int(np.median([t[3] for t in d]))
        cnt = Counter(int(round(t[0] / 25) * 25) for t in layout[W] if abs(t[2] - w) < 40)
        cols = sorted(c for c, n in cnt.items() if n >= 3)
        # refine each column to the median real x of its members
        xs = [int(np.median([t[0] for t in layout[W] if abs(t[0] - c) < 30 and abs(t[2] - w) < 40])) for c in cols]
        ys = sorted({t[1] for t in d})
        d_ = [b - a for a, b in zip(ys, ys[1:]) if b - a > h]
        pitch = int(np.median(d_)) if d_ else 0
        if not pitch: pitch = int(h * (1.63 if W < 3400 else 1.52))  # observed row-pitch / tile-height ratios
        y0 = ys[0]
        rows = []
        k = -((y0 - 150) // pitch)
        yy = y0 + k * pitch
        while yy + h <= H * BOTTOM_BANNER:
            if yy > H * 0.2: rows.append(yy)
            yy += pitch
        g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        tiles = []
        for ry in rows:
            sy = snap_row(g, ry, xs[0], w, h) if abs(ry - y0) % pitch else ry
            if any(abs(ry - t[1]) < 25 for t in d): sy = [t[1] for t in d if abs(ry - t[1]) < 25][0]
            for x in xs:
                if x + w > W or sy + h > H * BOTTOM_BANNER: continue
                crop = g[sy:sy + h, x:x + w]
                if crop.std() < 8: continue
                tiles.append((x, sy, w, h))
        out[sid] = sorted(tiles, key=lambda t: (round(t[1] / 100), t[0]))
    return out, ims


if __name__ == '__main__':
    inv = {f'SS-{i:03d}': r for i, r in enumerate(sorted([r for r in csv.DictReader((HERE / 'asset-inventory.csv').open())
                                                          if r['role'] == 'SCREENSHOT_PENDING_THUMBNAIL_EXTRACTION'], key=lambda r: r['location']), 1)}
    CROPS.mkdir(parents=True, exist_ok=True); SHEETS.mkdir(exist_ok=True)
    tiles, ims = grid_tiles(inv)
    rows = []
    for sid, r in inv.items():
        im = ims[sid]
        assert hashlib.sha256((ROOT / r['location']).read_bytes()).hexdigest() == r['sha256']
        sheet = []
        for j, (x, y, w, h) in enumerate(tiles[sid], 1):
            crop = im[y:y + h, x:x + w]
            ok, buf = cv2.imencode('.png', crop)
            p = CROPS / f'{sid}-T{j:02d}.png'; p.write_bytes(buf.tobytes())
            title = im[y + h:y + h + int(h * .42), max(0, x - 0):x + w]
            tp = CROPS / f'{sid}-T{j:02d}-title.png'; cv2.imwrite(str(tp), title)
            rows.append(dict(Screenshot_Source_ID=sid, Screenshot_Path=r['location'], Screenshot_SHA256=r['sha256'], Tile=f'T{j:02d}', X=x, Y=y, W=w, H=h,
                             Crop_Path=str(p.relative_to(ROOT)), Crop_SHA256=hashlib.sha256(buf.tobytes()).hexdigest(), Title_Strip_Path=str(tp.relative_to(ROOT))))
            sheet.append(np.vstack([cv2.resize(crop, (480, int(480 * h / w))), cv2.resize(title, (480, int(480 * title.shape[0] / w)))]))
        if sheet:
            hh = max(s.shape[0] for s in sheet)
            padded = [cv2.copyMakeBorder(s, 0, hh - s.shape[0], 0, 6, cv2.BORDER_CONSTANT, value=(40, 40, 40)) for s in sheet]
            while len(padded) % 3: padded.append(np.zeros_like(padded[0]))
            cv2.imwrite(str(SHEETS / f'{sid}.jpg'), np.vstack([np.hstack(padded[k:k + 3]) for k in range(0, len(padded), 3)]), [cv2.IMWRITE_JPEG_QUALITY, 85])
    with (HERE / 'screenshot-tiles-detected.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(inv), 'screenshots', len(rows), 'tiles')
