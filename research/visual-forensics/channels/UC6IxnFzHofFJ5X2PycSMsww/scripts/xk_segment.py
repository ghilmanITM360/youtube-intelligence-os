"""xkcd per-video candidate segmentation into HOLD states and ACTIVITY events (candidates, not verified truth).
Detectors (complementary):
  D1 low-res global change: changed_frac_thr10_320 >= T1
  D2 PySceneDetect ContentDetector(12) scene starts
  D3 full-res sparse-ink change: px_diff_ge12 >= N3 (calibrated from this source's own noise floor)
  D4 hold drift: first-vs-last frame of a candidate hold differs (catches slow sub-threshold pans/fades)
Calibration (per source, written to tables/detector_calibration.json):
  noise floor = 99th percentile of px_diff_ge12 over frames whose low-res MAD is in the lowest 60% ; N3 = max(3*floor, 40 px)
Every frame is assigned to exactly one HOLD or ACTIVITY interval (full timeline coverage by construction).
Outputs: tables/detector_calibration.json, tables/segments_v1.csv
Usage: python -I xk_segment.py <video_dir>"""
import csv, json, sys, pathlib, numpy as np, cv2

V = pathlib.Path(sys.argv[1])
m = list(csv.DictReader(open(V / "tables/FULL_FRAME_MEASUREMENTS.csv")))
N = len(m)
pts = np.array([float(r["pts_time"]) if r["pts_time"] else np.nan for r in m])
cf = np.array([float(r["changed_frac_thr10_320"]) for r in m]); mad = np.array([float(r["mean_abs_diff_320"]) for r in m])
p12 = np.array([int(r["px_diff_ge12"]) for r in m])
quiet = mad[1:] <= np.percentile(mad[1:], 60)
floor = float(np.percentile(p12[1:][quiet], 99)) if quiet.any() else 0.0
N3 = max(3 * floor, 40.0); T1 = 0.002
sd = [int(r["start_frame"]) for r in csv.DictReader(open(V / "tables/scenedetect_candidates.csv"))][1:]
act = (cf >= T1) | (p12 >= N3); act[0] = False
p150 = np.array([int(r["px_diff_ge150"]) for r in m]); mx = np.array([int(r["max_abs_diff"]) for r in m])
pict = [r["pict"] for r in m]
# encoder-refresh artifact candidates: change seen only by D3, no high-contrast pixels, low max diff (periodic I-frame requantisation)
enc = act & (cf < T1) & (p150 == 0) & (mx < 80)
act &= ~enc
for f in sd: act[f] = True
src = (V / "evidence/source_path.txt").read_text().strip()

# raw intervals
iv = []; i = 0
while i < N:
    j = i
    while j + 1 < N and act[j + 1] == act[i]: j += 1
    iv.append(["ACTIVITY" if act[i] else "HOLD", i, j]); i = j + 1
# merge activity runs separated by tiny holds (<3 frames) -> one event interval
merged = []
for t, a, b in iv:
    if merged and t == "HOLD" and b - a + 1 < 3 and merged[-1][0] == "ACTIVITY": merged[-1][2] = b; continue
    if merged and t == "ACTIVITY" and merged[-1][0] == "ACTIVITY": merged[-1][2] = b; continue
    merged.append([t, a, b])
# D4 hold drift: compare first/last frame of each hold at full res
need = sorted({f for t, a, b in merged if t == "HOLD" for f in (a, b)})
cap = cv2.VideoCapture(src); got = {}; k = 0; ni = 0
while ni < len(need):
    ok, im = cap.read()
    if not ok: break
    if k == need[ni]: got[k] = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); ni += 1
    k += 1
assert len(got) == len(need), (len(got), len(need))
rows = []
for n, (t, a, b) in enumerate(merged, 1):
    drift = int((cv2.absdiff(got[a], got[b]) >= 60).sum()) if t == "HOLD" else None
    dets = []
    if t == "ACTIVITY":
        seg = slice(a, b + 1)
        if (cf[seg] >= T1).any(): dets.append("D1")
        if any(a <= f <= b for f in sd): dets.append("D2")
        if (p12[seg] >= N3).any(): dets.append("D3")
    elif drift >= N3: dets.append("D4")
    ea = [int(i) for i in np.nonzero(enc[a:b + 1])[0] + a] if t == "HOLD" else []
    rows.append(dict(seg=f"G{n:04d}", kind=t, start_frame=a, end_frame=b, frames=b - a + 1,
                     start_pts=round(pts[a], 4), end_pts=round(pts[b], 4), detectors="+".join(dets),
                     peak_cf=round(float(cf[a:b + 1].max()), 4), peak_px12=int(p12[a:b + 1].max()),
                     hold_drift_px60=drift if drift is not None else "", enc_artifact_frames=";".join(map(str, ea))))
with open(V / "tables/segments_v1.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
cal = dict(encoder_artifact_frames=[int(i) for i in np.nonzero(enc)[0]], encoder_artifact_I_frames=sum(pict[i] == "I" for i in np.nonzero(enc)[0]),
           encoder_rule="D3-only frames with px_diff_ge150==0 and max_abs_diff<80 are ENCODER_REFRESH candidates absorbed into holds (visual spot-check required)",
           source=src, frames=N, T1_changed_frac=T1, noise_floor_px12_p99_quiet=floor, N3_px12=N3, scenedetect_starts=len(sd),
           holds=sum(r["kind"] == "HOLD" for r in rows), activities=sum(r["kind"] == "ACTIVITY" for r in rows),
           drift_flagged_holds=sum("D4" in r["detectors"] for r in rows),
           coverage_frames=sum(r["frames"] for r in rows), method=__doc__.split("Outputs")[0])
assert cal["coverage_frames"] == N
(V / "tables/detector_calibration.json").write_text(json.dumps(cal, indent=1))
print({k: v for k, v in cal.items() if k != "method"})
