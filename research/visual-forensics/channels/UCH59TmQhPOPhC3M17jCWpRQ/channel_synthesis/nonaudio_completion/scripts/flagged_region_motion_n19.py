# N19: for flagged rows, per-tile displacement (phaseCorrelate, grey) between interval endpoints, chained over links of 5 frames,
# plus one zoom/translate fit. Diagnostic only: first/last native pixels, no threshold tuned, M3 unchanged. Writes CSV to argv[1].
import csv, cv2, sys, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / "Downloads/videos in mp3/BarelyEvolved-MP4"
V = {"mNLN": "mNLNb-Z4T0M", "GNaB": "GNaBxt_zIRA"}; rows = []
IDS = sys.argv[2:]
for pre, vid in V.items():
    L = {r["interval_id"]: r for r in csv.DictReader(open(N / f"dense_review/DENSE_REVIEW_LEDGER_{vid}.csv"))}
    cap = cv2.VideoCapture(str(next(SRC.glob(f"*{vid}*.mp4"))))
    def fr(i):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i); return cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY).astype(np.float32)
    for iid in [i for i in IDS if i.startswith(pre)]:
        a, b = int(L[iid]["start_frame"]), int(L[iid]["end_frame"])
        if a == b: a -= 1
        H, W = 1080, 1920; nx, ny = 8, 5; tw, th = W // nx, H // ny; A, B = fr(a), fr(b); pts = []; grid = []
        for j in range(ny):
            line = []
            for i in range(nx):
                x, y = i * tw, j * th; p, q = A[y:y+th, x:x+tw], B[y:y+th, x:x+tw]
                if p.std() < 4: line.append("  --  "); continue
                (dx, dy), resp = cv2.phaseCorrelate(p, q, cv2.createHanningWindow((tw, th), cv2.CV_32F))
                if resp < 0.15: line.append("  ??  "); continue
                line.append(f"{dx:+3.0f},{dy:+3.0f}"); pts.append((x + tw/2 - W/2, y + th/2 - H/2, dx, dy))
            grid.append(" ".join(line))
        P = np.array(pts) if pts else np.zeros((0, 4)); s = tx = ty = rms = moving = float("nan")
        if len(P) >= 4:
            M = np.zeros((2 * len(P), 3)); M[::2, 0] = P[:, 0]; M[1::2, 0] = P[:, 1]; M[::2, 1] = 1; M[1::2, 2] = 1
            d = P[:, 2:].ravel(); sol = np.linalg.lstsq(M, d, rcond=None)[0]; s, tx, ty = sol; rms = float(np.sqrt(((M @ sol - d) ** 2).mean()))
            moving = float((np.hypot(P[:, 2], P[:, 3]) >= 2).mean())
        rows.append(dict(interval_id=iid, frame_a=a, frame_b=b, tiles_used=len(P), share_tiles_moved_ge_2px=round(moving, 3), fit_scale_minus_1=round(s, 4), fit_tx=round(tx, 1), fit_ty=round(ty, 1), fit_rms_px=round(rms, 2)))
        print(iid, a, b, rows[-1]); print("\n".join(grid))
with open(sys.argv[1], "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
