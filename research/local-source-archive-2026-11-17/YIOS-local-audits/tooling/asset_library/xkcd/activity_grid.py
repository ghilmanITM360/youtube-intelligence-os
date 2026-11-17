"""Grid of every frame of the given rv1-unviewed activity segments at 1/8 scale (for motion-class verification). usage: activity_grid.py <id> SEG..."""
import csv, sys, pathlib, cv2, numpy as np
v = sys.argv[1]; segs = set(sys.argv[2:]); b = pathlib.Path.home() / f"YIOS-local-audits/xkcd-whatif/videos/{v}"
rows = [r for r in csv.DictReader(open(b / "tables/state_ledger.csv")) if r["seg"] in segs]
fr = sorted({i for r in rows for i in range(int(r["start_frame"]), int(r["end_frame"]) + 1)})
seg_of = {i: r["seg"] for r in rows for i in range(int(r["start_frame"]), int(r["end_frame"]) + 1)}
t = []
for i in fr:
    im = cv2.imread(str(b / f"closure_v1/native/f{i:06d}.png")); s = cv2.resize(im, (135, 240), interpolation=cv2.INTER_AREA)
    cv2.putText(s, f"{i}", (2, 12), 0, .4, (0, 0, 255), 1); t.append(cv2.copyMakeBorder(s, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 255)))
n = 16
while len(t) % n: t.append(np.zeros_like(t[0]))
cv2.imwrite(str(b / "closure_v1/activity_grid.jpg"), np.vstack([np.hstack(t[k:k + n]) for k in range(0, len(t), n)]), [cv2.IMWRITE_JPEG_QUALITY, 85]); print(len(fr), "frames")
