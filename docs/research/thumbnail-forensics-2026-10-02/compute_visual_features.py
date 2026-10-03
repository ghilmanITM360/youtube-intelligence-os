"""Objective, reproducible image measurements for every accessible thumbnail (no interpretation).

All values are measurements or proxies of pixels, never psychological claims. 4:3 'hqdefault' images
carry black letterbox bars; they are cropped to the central 16:9 region for measurement and hashing
(the original file is never modified; crop flag recorded).
"""
import csv, json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import cv2, numpy as np, imagehash
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FACE = None


def load16x9(p):
    im = cv2.imread(str(p))
    if im is None:  # e.g. WebP/odd encodings served under .jpg
        im = cv2.cvtColor(np.array(Image.open(p).convert('RGB')), cv2.COLOR_RGB2BGR)
    H, W = im.shape[:2]
    letter = False
    if abs(W / H - 4 / 3) < 0.05:
        ch = int(W * 9 / 16); y0 = (H - ch) // 2
        im = im[y0:y0 + ch]; letter = True
    return im, letter


def feat(args):
    global FACE
    tid, path = args
    if FACE is None: FACE = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    im, letter = load16x9(ROOT / path)
    H, W = im.shape[:2]
    small = cv2.resize(im, (320, 180), interpolation=cv2.INTER_AREA)
    g = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    pil = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    ph = str(imagehash.phash(pil, hash_size=8)); dh = str(imagehash.dhash(pil, hash_size=8))
    edges = cv2.Canny(g, 80, 160)
    # strong-edge block ratio: share of 8x8 blocks where >20% of pixels have a strong gradient. Correlates with
    # text and fine detail but cannot separate them; it is NOT a text-area measurement.
    grad = cv2.morphologyEx(g, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8))
    blk = (grad > 60).astype(np.float32)[:176, :320].reshape(22, 8, 40, 8).mean(axis=(1, 3))
    edgeblocks = float((blk > 0.20).mean())
    # dominant colours via k-means on 5 clusters in a 80x45 sample
    px = cv2.resize(small, (80, 45)).reshape(-1, 3).astype(np.float32)
    _, labels, centers = cv2.kmeans(px, 5, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 2, cv2.KMEANS_PP_CENTERS)
    order = np.argsort(-np.bincount(labels.ravel(), minlength=5))
    dom = ['#%02x%02x%02x' % tuple(int(v) for v in centers[i][::-1]) for i in order[:3]]
    q = (small // 32).reshape(-1, 3); colorcount = len({tuple(v) for v in q})
    faces = FACE.detectMultiScale(g, 1.1, 5, minSize=(14, 14))
    fa = max((w * h for x, y, w, h in faces), default=0) / (320 * 180)
    border = np.ones_like(g, bool); border[30:150, 50:270] = False
    return dict(Thumbnail_ID=tid, Source_Path=path, Letterbox_Cropped=letter, Width=im.shape[1], Height=im.shape[0],
                Mean_Luminance=round(float(g.mean()), 1), Contrast_Std=round(float(g.std()), 1), Mean_Saturation=round(float(hsv[..., 1].mean()), 1),
                Dominant_Colors=' '.join(dom), Color_Count_Proxy=colorcount, Edge_Density=round(float((edges > 0).mean()), 4),
                Background_Edge_Density=round(float((edges[border] > 0).mean()), 4), Strong_Edge_Block_Ratio=round(edgeblocks, 4),
                Face_Count_Haar=len(faces), Largest_Face_Area_Ratio=round(fa, 4), PHash=ph, DHash=dh)


if __name__ == '__main__':
    rows = [(r['Thumbnail_ID'], r['Source_Path']) for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID']]
    with ProcessPoolExecutor(8) as ex:
        out = list(ex.map(feat, rows, chunksize=20))
    with (HERE / 'visual-features.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
    print(len(out), 'feature rows')
