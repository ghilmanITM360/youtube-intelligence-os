# One labelled thumbnail per state (middle native rep frame) -> 6x6 contact sheets for asset crosswalk review.
import cv2, csv, glob, sys, numpy as np, json
from pathlib import Path
B = Path('/Users/ghilmankhan/YIOS-local-audits/barely-evolved'); O = Path(sys.argv[1])
V = {'uPQcyookL0Y': ('2026-11-02-uPQcyookL0Y-deep-ct-scan', 'tables/states_v6_draft.csv', 'state_v4', 'tables/k_rep_frames_batch*.csv', 'state_v5'),
     'mNLNb-Z4T0M': ('2026-11-03-mNLNb-Z4T0M-deep-ct-scan', 'tables/states_v1.csv', 'state', 'tables/rep_frames_b*.csv', 'state'),
     'GNaBxt_zIRA': ('2026-11-03-GNaBxt_zIRA-deep-ct-scan', 'tables/states_v1.csv', 'state', 'tables/rep_frames_b*.csv', 'state')}
idx = {}
for vid, (d, stf, sk, rp, rk) in V.items():
    p = B / d; reps = {}
    for f in sorted(glob.glob(str(p / rp))):
        for r in csv.DictReader(open(f)): reps.setdefault(r[rk], []).append((int(r['frame']), r['native_png']))
    tiles = []
    for s in csv.DictReader(open(p / stf)):
        c = sorted(reps.get(s[sk], [])); 
        if not c: tiles.append((s[sk], None, None)); continue
        fr, png = c[len(c) // 2]; tiles.append((s[sk], fr, p / png))
    for n in range(0, len(tiles), 36):
        sh = np.full((6 * 216, 6 * 384, 3), 255, np.uint8)
        for k, (st, fr, png) in enumerate(tiles[n:n + 36]):
            im = cv2.imread(str(png)) if png and png.exists() else None
            t = cv2.resize(im, (384, 216), interpolation=cv2.INTER_AREA) if im is not None else np.full((216, 384, 3), 200, np.uint8)
            cv2.rectangle(t, (0, 0), (150, 26), (255, 255, 255), -1); cv2.putText(t, f'{st} f{fr}', (3, 19), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 220), 2)
            sh[(k // 6) * 216:(k // 6 + 1) * 216, (k % 6) * 384:(k % 6 + 1) * 384] = t
        out = O / f'{vid}_states_{n // 36 + 1:02d}.jpg'; cv2.imwrite(str(out), sh, [cv2.IMWRITE_JPEG_QUALITY, 85]); idx[out.name] = [t[0] for t in tiles[n:n + 36]]
    print(vid, len(tiles), sum(1 for t in tiles if t[2] is None or not t[2].exists()), 'missing')
json.dump(idx, open(O / 'SHEET_INDEX.json', 'w'), indent=1)
