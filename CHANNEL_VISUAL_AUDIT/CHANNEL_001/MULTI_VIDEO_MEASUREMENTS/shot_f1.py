"""Per-shot pixel F1 (dil 1 = ~5 px at 1080 wide) for a same-video render. Shot ranges parsed from SCENE_BLUEPRINTS/<id>/SH*.md."""
import pixel_iou as P, an, re, glob, sys, numpy as np
key, rend = sys.argv[1], sys.argv[2]; k = int(sys.argv[3]) if len(sys.argv) > 3 else 1
A, B = P.load(an.find(key)), P.load(rend); n = min(len(A), len(B)); A, B = A[:n], B[:n]
pr = (B & P.dil(A, k)).sum((1, 2)) / np.maximum(1, B.sum((1, 2))); rc = (A & P.dil(B, k)).sum((1, 2)) / np.maximum(1, A.sum((1, 2))); f = 2 * pr * rc / np.maximum(1e-9, pr + rc)
rows = []
for p in sorted(glob.glob(f'../SCENE_BLUEPRINTS/{key}/SH*.md')):
    m = re.search(r'([0-9.]+)-([0-9.]+) s', open(p).read()); a, b = int(float(m[1]) * 6), max(int(float(m[1]) * 6) + 1, int(float(m[2]) * 6))
    rows.append((p.split('/')[-1][:5], float(m[1]), float(m[2]), f[a:b].mean(), pr[a:b].mean(), rc[a:b].mean()))
for r in sorted(rows, key=lambda r: r[3]): print('%s %5.1f-%5.1fs F1 %.2f prec %.2f rec %.2f' % r)
