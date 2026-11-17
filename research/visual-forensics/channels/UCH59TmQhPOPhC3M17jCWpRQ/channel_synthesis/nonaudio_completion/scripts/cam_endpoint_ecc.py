# Second method for endpoint rows ORB left UNRESOLVED (low texture). Frozen before running: ECC MOTION_AFFINE, half-res,
# 3-level pyramid; VERIFIED if ecc_cc>=0.90 and (|scale-1|>=0.005 or centre shift>=3 px full-res); REJECTED if cc>=0.90,
# |scale-1|<0.002, shift<1.5; else UNRESOLVED (left UNCERTAIN; visual verdict from blind review decides nothing alone).
import csv, cv2, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'
rows = [r for r in csv.DictReader(open(N / 'r13_blind/CAMERA_ENDPOINT_CHECK.csv')) if r['verdict'] == 'UNRESOLVED']; out = []
for r in rows:
    cap = cv2.VideoCapture(str(next(SRC.glob(f"*{r['video']}*.mp4"))))
    def g(i):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, im = cap.read(); return cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), (960, 540)).astype(np.float32) / 255
    A, B = g(int(r['frame_a'])), g(int(r['frame_b'])); W = np.eye(2, 3, dtype=np.float32); cc = -1
    try:
        for lv in [4, 2, 1]:
            a, b = cv2.resize(A, (960 // lv, 540 // lv)), cv2.resize(B, (960 // lv, 540 // lv))
            W[:, 2] *= 1 if lv == 4 else 2
            cc, W = cv2.findTransformECC(a, b, W, cv2.MOTION_AFFINE, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-6), None, 5)
    except cv2.error as e:
        cc = -1
    s = float(np.sqrt(abs(np.linalg.det(W[:, :2])))); c = np.array([480, 270, 1.0]); t = float(np.hypot(*(W @ c - c[:2]))) * 2
    v = 'CAMERA_VERIFIED' if cc >= 0.9 and (abs(s - 1) >= 0.005 or t >= 3) else 'CAMERA_REJECTED' if cc >= 0.9 and abs(s - 1) < 0.002 and t < 1.5 else 'UNRESOLVED'
    out.append(dict(video=r['video'], interval_id=r['interval_id'], frame_a=r['frame_a'], frame_b=r['frame_b'], ecc_cc=round(float(cc), 4), scale=round(s, 5), centre_shift_px=round(t, 2), verdict=v))
    print(out[-1])
with open(N / 'r13_blind/CAMERA_ENDPOINT_CHECK_ECC.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
