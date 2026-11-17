"""Programmatic all-frame scan of RT4 attempt_1 (frozen V1/V2 proxies). Writes rv_full/full_render_scan.csv + summary json. Proxies, not visual judgement."""
import cv2, numpy as np, csv, json
cap = cv2.VideoCapture("RT4_animatic.mp4"); k = 0; rows = []
BG = np.array((240, 244, 246)); TEAL = np.array((138, 138, 31))
while True:
    ok, im = cap.read()
    if not ok: break
    im16 = im.astype(np.int16)
    nonbg = (np.abs(im16 - BG).max(axis=2) > 12)
    banner = im[130:240, 60:1020].reshape(-1, 3).mean(0)
    banner_ok = bool(np.abs(banner - TEAL).max() < 40)
    out = [int(nonbg[:116].sum()), int(nonbg[1705:].sum()), int(nonbg[:, :55].sum()), int(nonbg[:, 1025:].sum())]
    lower = im16[1004:1696, 64:1016]; pc = np.array((252, 248, 240))
    low_ink = int((np.abs(lower - pc).max(axis=2) > 40).sum())
    top = im16[264:896, 64:1016]
    tbg = top[5, 5]
    top_ink = int((np.abs(top - tbg).max(axis=2) > 40).sum())
    rows.append((k, banner_ok, *out, low_ink, top_ink)); k += 1
w = csv.writer(open("rv_full/full_render_scan.csv", "w", newline="")); w.writerow("frame banner_ok out_top out_bottom out_left out_right lower_ink top_ink".split()); w.writerows(rows)
a = np.array([[r[1], *r[2:]] for r in rows], dtype=float)
low = a[:, 5]; first_low = int(np.argmax(low > 5300)) if (low > 5300).any() else None
sm = dict(frames=len(rows), banner_ok_frames=int(a[:, 0].sum()), frames_with_ink_outside_safe=int(((a[:, 1:5].sum(1)) > 0).sum()),
          outside_max=a[:, 1:5].max(0).tolist(), lower_ink_min=int(low.min()), lower_ink_max=int(low.max()),
          lower_empty_frames_le5300px=int((low <= 5300).sum()), lower_first_content_frame=first_low,
          lower_empty_ranges=[])
e = None
for i, v in enumerate(low <= 5300):
    if v and e is None: e = i
    if (not v) and e is not None: sm["lower_empty_ranges"].append([e, i - 1]); e = None
if e is not None: sm["lower_empty_ranges"].append([e, len(rows) - 1])
json.dump(sm, open("rv_full/full_render_scan_summary.json", "w"), indent=1); print(json.dumps(sm))
