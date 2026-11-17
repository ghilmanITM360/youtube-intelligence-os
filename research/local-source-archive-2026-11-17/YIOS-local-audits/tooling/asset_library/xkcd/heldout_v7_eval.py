#!/usr/bin/env python3
"""Deep-VF held-out v7 measurement half (rules: _channel/deep_vf/FROZEN_RULES_v1.md, checked against its sha file first).
usage: <venv python> -I heldout_v7_eval.py
Per held-out video: verify source SHA, decode the middle frame of every automated HOLD (one sheet, in memory, no frame
files) and the middle frame of every ACTIVITY > 6 frames (second sheet); measure S1/S2/S3 (Shorts) and S7 (Short A vs
parent, automated segments both sides). Viewed rules (S4-S6, L1-L3) are judged by looking at the sheets afterwards."""
import csv, hashlib, json, os, subprocess
import numpy as np, cv2
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); D = f"{H}/asset_library/_channel/deep_vf"; OUT = f"{D}/heldout_v7"; os.makedirs(OUT, exist_ok=True)
for line in open(f"{D}/FROZEN_RULES_v1.sha256").read().split("\n")[1:]:
    if line.strip():
        h, f = line.split(); assert hashlib.sha256(open(f"{D}/{f}", "rb").read()).hexdigest() == h, f"FROZEN FILE CHANGED {f}"
sel = json.load(open(f"{D}/heldout_v7_selection.json"))
vids = [sel["short_excerpt_with_library_parent"], sel["short_no_caption_standalone"]] + list(sel["long_pop6_by_period"].values())
cen = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/census/census.csv"))}
def source(v):
    exp = open(f"{H}/videos/{v}/evidence/source_sha256.txt").read().split()[0]
    for c in cen[v]["local_paths"].split(" | "):
        h = hashlib.sha256()
        with open(c, "rb") as f:
            for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
        if h.hexdigest() == exp: return c, exp
    raise SystemExit(f"SHA mismatch {v}")
def grab(path, frames, w, hgt):
    sel_ = "+".join(f"eq(n\\,{n})" for n in frames)
    p = subprocess.run(["ffmpeg", "-v", "error", "-nostdin", "-i", path, "-an", "-vf", f"select='{sel_}',scale={w}:{hgt}", "-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], capture_output=True, check=True)
    return np.frombuffer(p.stdout, np.uint8).reshape(-1, hgt, w, 3)
def sheet(imgs, labels, name, cols):
    th, tw = imgs.shape[1:3]; rows = (len(imgs) + cols - 1) // cols; S = np.full((rows * (th + 16), cols * tw, 3), 40, np.uint8)
    for i, (im, lb) in enumerate(zip(imgs, labels)):
        X, Y = (i % cols) * tw, (i // cols) * (th + 16); S[Y + 16:Y + 16 + th, X:X + tw] = im; cv2.putText(S, lb, (X + 2, Y + 12), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 255), 1)
    cv2.imwrite(f"{OUT}/{name}", S, [cv2.IMWRITE_JPEG_QUALITY, 85])
res = {}
for v in vids:
    path, sha = source(v); seg = list(csv.DictReader(open(f"{H}/videos/{v}/tables/segments_v1.csv")))
    port = cen[v]["format_class"] == "SHORT"; w, hgt = (180, 320) if port else (320, 180)
    holds = [s for s in seg if s["kind"] == "HOLD"]; mids = [(int(s["start_frame"]) + int(s["end_frame"])) // 2 for s in holds]
    sheet(grab(path, mids, w, hgt), [f"{s['seg']} {float(s['start_pts']):.1f}s" for s in holds], f"{v}_holds.jpg", 10 if port else 6)
    acts = [s for s in seg if s["kind"] == "ACTIVITY" and int(s["frames"]) > 6]
    if acts: sheet(grab(path, [(int(s["start_frame"]) + int(s["end_frame"])) // 2 for s in acts], w, hgt), [f"{s['seg']} {s['frames']}f {float(s['start_pts']):.1f}s" for s in acts], f"{v}_long_activities.jpg", 10 if port else 6)
    a = [int(s["frames"]) for s in seg if s["kind"] == "ACTIVITY"]
    ffm = list(csv.DictReader(open(f"{H}/videos/{v}/tables/FULL_FRAME_MEASUREMENTS.csv")))
    red = sum(float(x["mean_r"]) > 150 and float(x["mean_g"]) < 110 and float(x["mean_b"]) < 110 for x in ffm)
    full = grab(path, mids[:: max(1, len(mids) // 8)], 270 if port else 480, 480 if port else 270).reshape(-1, 3).astype(int)
    bright = full[full.min(1) > 230]; vals, cnt = np.unique(bright, axis=0, return_counts=True); modal = vals[cnt.argmax()][::-1] if len(vals) else None
    r = dict(format=cen[v]["format_class"], sha256=sha, holds=len(holds), activities=len(a), long_activities_gt6=len(acts), act_per_min=round(len(a) / (len(ffm) / 24 / 60), 1),
             S1_red_frames=red, S2_one_frame_share=round(sum(n == 1 for n in a) / max(1, len(a)), 3), S3_modal_bright_rgb="#%02X%02X%02X" % tuple(modal) if modal is not None else None)
    res[v] = r; print(v, r)
# S7: Short A vs parent on matched ASR sentences, automated ACTIVITY counts on both sides
A, P = sel["short_excerpt_with_library_parent"], "WH4g1ptJ-70"
def asr_rate(v):
    S = [s for s in json.load(open(f"{H}/videos/{v}/asr/asr_small_en.json"))["segments"] if s["text"].strip()]
    ev = [float(s["start_pts"]) for s in csv.DictReader(open(f"{H}/videos/{v}/tables/segments_v1.csv")) if s["kind"] == "ACTIVITY"]
    return [(s["text"].lower().split(), s["start"], S[i + 1]["start"] if i + 1 < len(S) else s["end"] + 2, ev) for i, s in enumerate(S)]
sa, sp = asr_rate(A), asr_rate(P); se = pe = sd = pd = m = 0
for w, t0, t1, ev in sa:
    b = max(sp, key=lambda x: len(set(w) & set(x[0])))
    if len(set(w) & set(b[0])) >= 0.6 * len(set(w)):
        m += 1; se += sum(t0 <= e < t1 for e in ev); sd += t1 - t0; pe += sum(b[1] <= e < b[2] for e in b[3]); pd += b[2] - b[1]
res["S7"] = dict(short=A, parent=P, short_segments=len(sa), matched=m, short_rate=round(60 * se / max(sd, 1), 1), parent_rate_same_sentences=round(60 * pe / max(pd, 1), 1))
print(res["S7"]); json.dump(res, open(f"{OUT}/measured.json", "w"), indent=1)
