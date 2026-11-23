"""Measure (not copy) head/hair/face/leg geometry from the reference frames as coarse polylines -> hips_traced.json (source px, +-1.5px)."""
import os, json
import numpy as np
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); LM = os.environ['LMDIR']
def ink(f, thr=110): return np.array(Image.open('%s/f%d.png' % (LM, f)).convert('L')) < thr
def mf(m, k): return np.array(Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.MaxFilter(k))) > 0
def nf(m, k): return np.array(Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.MinFilter(k))) > 0
def smooth(v, n=3):
    v = np.array(v, float); return np.mean([np.roll(v, i) for i in range(-n, n + 1)], 0)
out = {}
a = ink(647); n = ink(725)
# hair = thick ink: opening (erode 9, dilate 9) isolates blobs wider than stroke
H = a.copy(); H[860:] = 0; hair = mf(nf(H, 9), 9)
ys, xs = np.where(hair); out['hair_bbox'] = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
hair = mf(hair, 5)
top = []; bot = []
for x in range(xs.min(), xs.max() + 1, 2):
    c = np.where(hair[:, x])[0]
    if len(c): top.append((x, int(c.min()))); bot.append((x, int(c.max())))
out['hair_top'] = top; out['hair_bot'] = bot
# head outline: radial outermost ink beyond hair, centre from non-hair ring
cx, cy = 540, 872; ang = np.arange(0, 360, 5); rr = []
for t in ang:
    d = np.deg2rad(t); best = 0
    for r in range(60, 130):
        x, y = int(round(cx + r * np.cos(d))), int(round(cy - r * np.sin(d)))
        if a[y, x] and not hair[y, x]: best = r
    rr.append(best)
rr = np.array(rr, float)
med = np.array([np.median(np.roll(rr, i)[:0] if False else [rr[(j + k) % len(rr)] for k in range(-3, 4)]) for j, i in enumerate(range(len(rr)))])
bad = (rr < 60) | (np.abs(rr - med) > 5); good = np.where(~bad)[0]
rr = np.interp(np.arange(len(rr)), np.r_[good - len(rr), good, good + len(rr)], np.r_[rr[good], rr[good], rr[good]])
out['head_ring_r'] = [round(float(v) - 2, 1) for v in smooth(rr, 1)]; out['head_ring_c'] = [cx, cy]; out['head_ring_deg'] = ang.tolist()
# eyes (blobs inside face), mouth centreline per column
def blobs(m, box):
    x0, y0, x1, y1 = box; s = m[y0:y1, x0:x1]; ys, xs = np.where(s); return (float(xs.mean() + x0), float(ys.mean() + y0), float(np.sqrt(len(ys) / np.pi))) if len(ys) else None
out['eyeL'] = blobs(a, (495, 815, 525, 850)); out['eyeR'] = blobs(a, (555, 805, 585, 845))
def center(m, box, step=4):
    x0, y0, x1, y1 = box; res = []
    for x in range(x0, x1, step):
        c = np.where(m[y0:y1, x])[0]
        if len(c): res.append((x, float(c.mean() + y0)))
    return res
out['mouth_happy'] = center(a, (485, 868, 585, 915)); out['mouth_neutral'] = center(n, (485, 868, 600, 915))
# legs: per-row runs below hip fork
def legs(m):
    L, R = [], []
    for y in range(1130, 1186, 3):
        c = np.where(m[y, 440:640])[0] + 440
        if not len(c): continue
        runs = np.split(c, np.where(np.diff(c) > 3)[0] + 1)
        if len(runs) >= 2: L.append((float(runs[0].mean()), y)); R.append((float(runs[-1].mean()), y))
    return L, R
out['legL'], out['legR'] = legs(a)
json.dump(out, open(os.path.join(HERE, 'hips_traced.json'), 'w'), indent=1)
print({k: (v if not isinstance(v, list) else len(v)) for k, v in out.items()})
print(out['eyeL'], out['eyeR'], out['hair_bbox']); print(out['legL'][:3], out['legL'][-3:], out['legR'][:3], out['legR'][-3:])
