# Measure source scenes for style/full-scene RT specs: event timing (from dense CSV), palette, 8-frame strip (local only).
import csv, json, sys, cv2, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'
SC = {'uPQcyookL0Y': ('W021', 3609, 3766), 'mNLNb-Z4T0M': ('S067', 6209, 6416), 'GNaBxt_zIRA': ('S057', 7521, 7699)}
res = {}
for vid, (st, a, b) in SC.items():
    d = [r for r in csv.DictReader(open(N / f'dense/DENSE_MOTION_{vid}.csv')) if a <= int(r['frame']) <= b]
    ev = [dict(frame=int(r['frame']), off=int(r['frame']) - a, dx=float(r['dx']), dy=float(r['dy']), dscale=float(r['dscale']), mad=float(r['global_mad']), bbox=r['residual_bbox'])
          for r in d if float(r['global_mad']) > 0.5 or abs(float(r['dscale']) - 1) > 0.002 or abs(float(r['dx'])) > 0.5]
    cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4')))); cap.set(cv2.CAP_PROP_POS_FRAMES, a); F = []
    for i in range(a, b + 1): ok, im = cap.read(); F.append(im)
    mid = F[len(F) // 2]; q = (mid // 16 * 16 + 8).reshape(-1, 3); u, c = np.unique(q, axis=0, return_counts=True); o = np.argsort(-c)[:8]
    pal = [dict(hex='#%02x%02x%02x' % tuple(int(x) for x in u[i][::-1]), frac=round(c[i] / len(q), 3)) for i in o]
    picks = np.linspace(0, len(F) - 1, 8).astype(int); tiles = [cv2.resize(F[i], (480, 270)) for i in picks]
    for t, i in zip(tiles, picks): cv2.putText(t, f'+{i} f{a+i}', (6, 20), 0, 0.6, (0, 0, 255), 2)
    cv2.imwrite(str(N / f'style_rt/strip_local_only_{vid}_{st}.jpg'), np.vstack([np.hstack(tiles[:4]), np.hstack(tiles[4:])]), [cv2.IMWRITE_JPEG_QUALITY, 82])
    res[vid] = dict(state=st, start=a, end=b, frames=b - a + 1, palette_mid=pal, change_frames=ev)
(N / 'style_rt/SOURCE_SCENE_MEASUREMENTS.json').write_text(json.dumps(res, indent=1))
for v, r in res.items(): print(v, r['state'], r['frames'], 'changes', len(r['change_frames']), [ (e['off'], round(e['mad'],1), round(e['dscale'],3)) for e in r['change_frames']][:40])
