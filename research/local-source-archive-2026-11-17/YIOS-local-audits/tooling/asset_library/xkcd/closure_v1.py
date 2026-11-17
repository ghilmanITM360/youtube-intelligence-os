"""Per-video visual closure evidence (contract v1). Reads existing ledgers, never edits them.
Writes videos/<id>/closure_v1/{checks.json, native/*.png, holds_*.jpg, diff_*.png, activity_curves.csv}.
usage: closure_v1.py <video_id> [extra frame indices...]"""
import csv, hashlib, json, subprocess, sys, pathlib
import numpy as np, cv2

ROOT = pathlib.Path.home() / "YIOS-local-audits/xkcd-whatif/videos"
vid = sys.argv[1]; extra = [int(x) for x in sys.argv[2:]]
V = ROOT / vid; OUT = V / "closure_v1"; NAT = OUT / "native"; NAT.mkdir(parents=True, exist_ok=True)
man = json.load(open(V / "source_manifest.json"))["source"]
rows = list(csv.DictReader(open(V / "tables/state_ledger.csv")))
meas = list(csv.DictReader(open(V / "tables/FULL_FRAME_MEASUREMENTS.csv")))
qg = json.load(open(V / "quality_gate.json"))
src = man["file_path"]; chk = {"video_id": vid}

# V1 identity
h = hashlib.sha256()
with open(src, "rb") as f:
    for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
chk["V1"] = {"sha_recomputed": h.hexdigest(), "sha_manifest": man["sha256"], "match": h.hexdigest() == man["sha256"],
             "decoded_frames_manifest": man["decoded_frames"], "ledger_last_frame": int(rows[-1]["end_frame"])}
chk["V1"]["pass"] = chk["V1"]["match"] and man["decoded_frames"] == int(rows[-1]["end_frame"]) + 1

# V2 coverage: every frame in exactly one segment, every frame measured
cov = np.zeros(man["decoded_frames"], int)
for r in rows: cov[int(r["start_frame"]):int(r["end_frame"]) + 1] += 1
chk["V2"] = {"frames_measured": len(meas), "frames_cov_once": int((cov == 1).sum()), "pass": bool((cov == 1).all()) and len(meas) == man["decoded_frames"]}

# V5 measurements: hold stillness, activity progress curves
px = np.array([int(m["px_diff_ge12"]) for m in meas])
holds = [r for r in rows if r["kind"] == "HOLD"]; acts = [r for r in rows if r["kind"] == "ACTIVITY"]
hold_max = {r["seg"]: int(px[int(r["start_frame"]) + 1:int(r["end_frame"]) + 1].max()) if int(r["frames"]) > 1 else 0 for r in holds}
chk["V5_hold_max_px_diff_ge12_native"] = hold_max
with open(OUT / "activity_curves.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["seg", "start_frame", "end_frame", "frames", "subtype", "px_diff_ge12_per_frame"])
    for r in acts:
        a, b = int(r["start_frame"]), int(r["end_frame"])
        w.writerow([r["seg"], a, b, r["frames"], r["subtype"], " ".join(str(px[i]) for i in range(a, min(b + 2, len(px))))])

# frames to decode natively
unres = [r for r in rows if "UNRESOLVED" in (r["subtype"] + r["description"]).upper() or r["confidence"] == "LOW"]
unv = qg["review_scope"]["unreviewed_or_unverified_intervals"]
want = set(extra)
for r in holds: want.add(int(r["end_frame"]))
for r in acts:  # before/after every activity (cuts included)
    want.update([max(int(r["start_frame"]) - 1, 0), int(r["end_frame"]) + 1 if int(r["end_frame"]) + 1 < man["decoded_frames"] else int(r["end_frame"])])
for r in unres: want.update(range(max(int(r["start_frame"]) - 1, 0), min(int(r["end_frame"]) + 2, man["decoded_frames"])))
for u in unv if isinstance(unv, list) else []:
    r = next(x for x in rows if x["seg"] == u["seg"]); want.update(range(int(r["start_frame"]), int(r["end_frame"]) + 1))
for r in holds:  # within-hold residue frames (pair) for noise classification
    a, b = int(r["start_frame"]), int(r["end_frame"])
    for i in [i for i in range(a + 1, b + 1) if px[i] > 50][:40]: want.update([i - 1, i])
want = sorted(want)
missing = [i for i in want if not (NAT / f"f{i:06d}.png").exists()]
if missing:  # sequential decode (decode order == frame index for these CFR sources); writes only listed frames
    cap = cv2.VideoCapture(src); ms = set(missing); n = 0; last = max(missing)
    while n <= last:
        ok, fr = cap.read()
        if not ok: break
        if n in ms: cv2.imwrite(str(NAT / f"f{n:06d}.png"), fr)
        n += 1
    cap.release()
    assert all((NAT / f"f{i:06d}.png").exists() for i in missing), "decode short"
chk["native_frames"] = len(want)
img = lambda i: cv2.imread(str(NAT / f"f{i:06d}.png"))

# hold sheets at 1/2 scale, 4 per sheet, labelled
for s in range(0, len(holds), 4):
    tiles = []
    for r in holds[s:s + 4]:
        t = cv2.resize(img(int(r["end_frame"])), None, fx=.5, fy=.5, interpolation=cv2.INTER_AREA)
        cv2.putText(t, f"{r['seg']} {r['visual_state_id']} f{r['end_frame']}", (8, 30), 0, .9, (0, 0, 255), 2); tiles.append(t)
    while len(tiles) < 4: tiles.append(np.zeros_like(tiles[0]))
    cv2.imwrite(str(OUT / f"holds_{s // 4 + 1:02d}.jpg"), np.vstack([np.hstack(tiles[:2]), np.hstack(tiles[2:])]), [cv2.IMWRITE_JPEG_QUALITY, 88])

# diffs for unresolved: native |f - f-1| amplified, plus bbox of change
res = {}
for r in unres:
    a = int(r["start_frame"]); d = cv2.absdiff(img(a), img(a - 1)).max(2)
    ys, xs = np.nonzero(d >= 12); res[r["seg"]] = {"changed_px_ge12_native": int(len(xs)),
        "bbox": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())] if len(xs) else None,
        "next_frame_changed_px": int((cv2.absdiff(img(a + 1), img(a)).max(2) >= 12).sum())}
    cv2.imwrite(str(OUT / f"diff_{r['seg']}.png"), np.clip(d.astype(int) * 8, 0, 255).astype(np.uint8))
chk["unresolved"] = res

# camera-drift test between consecutive holds in the same shot: phase correlation shift + scale proxy
drift = {}
for p, q in zip(holds, holds[1:]):
    if p["shot_id"] != q["shot_id"]: continue
    A = cv2.cvtColor(img(int(p["end_frame"])), cv2.COLOR_BGR2GRAY).astype(np.float32)
    B = cv2.cvtColor(img(int(q["end_frame"])), cv2.COLOR_BGR2GRAY).astype(np.float32)
    (dx, dy), resp = cv2.phaseCorrelate(A, B)
    drift[f"{p['seg']}->{q['seg']}"] = {"dx": round(dx, 2), "dy": round(dy, 2), "response": round(resp, 3)}
chk["hold_to_hold_shift"] = drift

# review strips for unresolved + rv1-unviewed segments: frames start-1..end+1 cropped to the union change bbox
segs = {r["seg"] for r in unres} | {u["seg"] for u in (unv if isinstance(unv, list) else [])}
for sg in sorted(segs):
    r = next(x for x in rows if x["seg"] == sg); a, b = int(r["start_frame"]), int(r["end_frame"])
    allfr = [i for i in range(max(a - 1, 0), min(b + 2, man["decoded_frames"]))]
    if r["kind"] == "HOLD": allfr = allfr[:3]  # hold: onset frames only; stillness is measured (hold_frames_gt50px)
    for k in range(0, len(allfr), 12):  # every frame shown; chunks of 12 per strip
      fr = allfr[k:k + 12]; part = "" if len(allfr) <= 12 else f"_{k // 12 + 1:02d}"
      ims = [img(i) for i in fr]; m = np.zeros(ims[0].shape[:2], bool)
      for x, y in zip(ims, ims[1:]): m |= cv2.absdiff(x, y).max(2) >= 12
      ys, xs = np.nonzero(m)
      if len(xs): x0, y0, x1, y1 = max(xs.min() - 30, 0), max(ys.min() - 30, 0), xs.max() + 30, ys.max() + 30
      else: x0, y0, x1, y1 = 0, 0, ims[0].shape[1], ims[0].shape[0]
      cr = [x[y0:y1, x0:x1] for x in ims]; sc = min(1.0, 700 / max(1, y1 - y0), 2400 / (len(cr) * max(1, x1 - x0)))
      cr = [cv2.putText(cv2.resize(c, None, fx=sc, fy=sc, interpolation=cv2.INTER_AREA).copy(), f"f{i}", (4, 18), 0, .6, (0, 0, 255), 2) for c, i in zip(cr, fr)]
      cv2.imwrite(str(OUT / f"strip_{sg}{part}.png"), np.hstack([cv2.copyMakeBorder(c, 0, 0, 0, 4, cv2.BORDER_CONSTANT, value=(0, 0, 255)) for c in cr]))
chk["review_strips"] = sorted(segs)
resid = {}
for r in holds:
    a, b = int(r["start_frame"]), int(r["end_frame"])
    for i in range(a + 1, b + 1):
        if px[i] > 50: resid[i] = int(px[i])
# classify residue: scattered noise if largest 8-connected changed component <= 20 px (decode frame pair natively)
for i in list(resid)[:40]:
    d = cv2.absdiff(img(i), img(i - 1)).max(2); n, _, st, _ = cv2.connectedComponentsWithStats((d >= 12).astype(np.uint8))
    big = int(st[1:, 4].max()) if n > 1 else 0
    resid[i] = {"px": resid[i], "max_diff": int(d.max()), "largest_component_px": big, "class": "NOISE" if big <= 20 else "DRAWN_CHANGE_VIEW_REQUIRED"}
chk["hold_frames_gt50px"] = resid
json.dump(chk, open(OUT / "checks.json", "w"), indent=1)
print(json.dumps({k: chk[k] for k in ("V1", "V2", "native_frames", "unresolved", "review_strips", "hold_frames_gt50px")}, indent=None))
print("shift max:", max([max(abs(d["dx"]), abs(d["dy"])) for d in drift.values()] or [0]))
print("hold max px:", max(hold_max.values()) if hold_max else None)
