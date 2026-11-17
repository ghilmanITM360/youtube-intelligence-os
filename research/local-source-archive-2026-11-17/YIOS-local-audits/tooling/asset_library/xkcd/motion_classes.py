#!/usr/bin/env python3
"""Deep-VF v2 motion labeller for ACTIVITY segments > 6 frames (automated; OpenCV Farneback flow on 320x180 grey).
Frame pairs (f, f+2) spread evenly over the activity, 3..20 pairs (one per ~12 f). Flow is read only on edge pixels (dilated Canny of the
first frame), because the flat canvas carries no motion signal. Per pair: M = share of edge pixels moving > 0.7 px.
  WHOLE_FRAME_CAMERA  any pair with M >= 0.60 and moving pixels spread over >= 60% of the frame width
  RULER_SCROLL        any pair where >= 70% of moving edge pixels sit in an outer 22% side band, |vy| > |vx| there, and band M >= 0.5
  OBJECT_MOTION       any pair with M >= 0.03 (and not the above)
  NO_TRANSLATION      otherwise (dissolves, write-ons, pops, colour changes)
Activity label: the most frequent moving label if >= 1/3 of pairs move (ties: RULER > CAMERA > OBJECT), else NO_TRANSLATION.
usage: <venv python> -I motion_classes.py <out_csv> <video_id> [...]   (source SHA verified against videos/<id>/evidence or campaign hash list)"""
import csv, hashlib, json, os, subprocess, sys
import numpy as np, cv2
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif")
CEN = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/census/census.csv"))}
HASHES = json.load(open(f"{H}/campaign/source_hashes_all_2026-11-06.json"))

def expected(v):
    p = f"{H}/videos/{v}/evidence/source_sha256.txt"
    if os.path.exists(p): return open(p).read().split()[0]
    e = HASHES.get(v); return e if isinstance(e, str) else (e or {}).get("sha256")

def source(v):
    exp = expected(v)
    for c in CEN[v]["local_paths"].split(" | "):
        h = hashlib.sha256()
        with open(c, "rb") as f:
            for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
        if h.hexdigest() == exp: return c, exp
    raise SystemExit(f"SHA mismatch {v}")

def grab(path, frames, w, hgt):
    """stream-decode the whole video at w x hgt grey and keep only the wanted frame indices (no frame files)"""
    want, out, n, sz = set(frames), {}, 0, w * hgt
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-nostdin", "-i", path, "-an", "-vf", f"scale={w}:{hgt},format=gray", "-fps_mode", "passthrough", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    while want - out.keys():
        buf = p.stdout.read(sz)
        if len(buf) < sz: break
        if n in want: out[n] = np.frombuffer(buf, np.uint8).reshape(hgt, w)
        n += 1
    p.kill(); p.wait(); return out

def label_pair(a, b):
    edges = cv2.dilate(cv2.Canny(a, 40, 120), np.ones((3, 3))) > 0
    if edges.sum() < 50: return "NO_TRANSLATION", 0.0
    fl = cv2.calcOpticalFlowFarneback(a, b, None, 0.5, 4, 21, 3, 5, 1.1, 0)
    mag = np.hypot(fl[..., 0], fl[..., 1]); mov = edges & (mag > 0.7); M = mov.sum() / edges.sum()
    W = a.shape[1]; xs = np.nonzero(mov)[1]
    if mov.sum() >= 30:
        for lo, hi in ((0, int(.22 * W)), (int(.78 * W), W)):
            band = np.zeros_like(mov); band[:, lo:hi] = True
            inb = mov & band; eb = edges & band
            if inb.sum() >= 0.7 * mov.sum() and eb.sum() and inb.sum() / eb.sum() >= 0.5 and abs(fl[..., 1][inb]).mean() > abs(fl[..., 0][inb]).mean():
                return "RULER_SCROLL", M
        if M >= 0.60 and (xs.max() - xs.min()) >= 0.6 * W: return "WHOLE_FRAME_CAMERA", M
    return ("OBJECT_MOTION" if M >= 0.03 else "NO_TRANSLATION"), M

PRI = ["RULER_SCROLL", "WHOLE_FRAME_CAMERA", "OBJECT_MOTION", "NO_TRANSLATION"]

def acts(v):
    """automated segments_v1 ACTIVITY > 6 f (same population v7 L3 used); reviewed subtype attached by max frame overlap when a ledger exists"""
    seg = [r for r in csv.DictReader(open(f"{H}/videos/{v}/tables/segments_v1.csv")) if r["kind"] == "ACTIVITY" and int(r["frames"]) > 6]
    p = f"{H}/videos/{v}/tables/state_ledger.csv"
    led = [r for r in csv.DictReader(open(p)) if r["kind"] == "ACTIVITY"] if os.path.exists(p) else None
    for r in seg:
        s, e = int(r["start_frame"]), int(r["end_frame"])
        if led is None: r["subtype"] = "UNREVIEWED"; continue
        ov = [(min(e, int(x["end_frame"])) - max(s, int(x["start_frame"])), x["subtype"]) for x in led]
        best = max(ov, default=(0, "")); r["subtype"] = best[1] if best[0] >= 0 else "NO_REVIEWED_OVERLAP"
    return seg

def demo():
    a = np.full((180, 320), 249, np.uint8); cv2.putText(a, "ABC", (120, 100), 0, 1.5, 0, 3)
    for y in range(0, 180, 12): cv2.line(a, (5, y), (40, y), 0, 2)
    b = np.roll(a, 4, axis=1); assert label_pair(a, b)[0] == "WHOLE_FRAME_CAMERA", label_pair(a, b)
    c = a.copy(); c[:, :60] = np.roll(a[:, :60], 5, axis=0); assert label_pair(a, c)[0] == "RULER_SCROLL", label_pair(a, c)
    assert label_pair(a, a)[0] == "NO_TRANSLATION"

if __name__ == "__main__":
    demo(); out = sys.argv[1]; rows = []
    for v in sys.argv[2:]:
        path, sha = source(v); A = acts(v)
        port = CEN[v]["format_class"] == "SHORT"; w, hgt = (180, 320) if port else (320, 180)
        pairs = []
        for r in A:
            s, e = int(r["start_frame"]), int(r["end_frame"]); m = (s + e) // 2
            k = max(3, min(20, (e - s) // 12))  # ponytail: <=20 sampled pairs per activity, denser sampling if short moves get missed
            pairs.append([(f, f + 2) for f in np.linspace(s + 1, e - 3, k).astype(int)])
        F = grab(path, [f for p in pairs for pr in p for f in pr], w, hgt) if pairs else {}
        for r, p in zip(A, pairs):
            labs = [label_pair(F[x], F[y]) for x, y in p if x in F and y in F]
            mv = [l for l, _ in labs if l != "NO_TRANSLATION"]
            lab = max(PRI[:3], key=lambda c: (mv.count(c), -PRI.index(c))) if len(mv) * 3 >= len(labs) and mv else "NO_TRANSLATION"
            rows.append(dict(video_id=v, sha256=sha[:12], seg=r["seg"], start_frame=r["start_frame"], frames=r["frames"], start_pts=r["start_pts"],
                             reviewed_subtype=r["subtype"], moving_pairs=f"{len(mv)}/{len(labs)}", motion_label=lab, max_M=round(max((m for _, m in labs), default=0), 3)))
        print(v, len(A), flush=True)
    with open(out, "w", newline="") as fo:
        wr = csv.DictWriter(fo, list(rows[0])); wr.writeheader(); wr.writerows(rows)
