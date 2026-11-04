"""Evaluate held-out videos against the frozen quantitative rules of campaign/HELDOUT_PROTOCOL_v1.md (Q1-Q7).
Ranges come from campaign/aggregate_dev_interim2.csv (the dev set frozen with the protocol), tolerance 15% of range.
Writes campaign/heldout_quant.csv. Usage: python3 -I xk_heldout_eval.py <ws>"""
import csv, json, re, sys, pathlib
W = pathlib.Path(sys.argv[1]); sel = json.load(open(W / "selection/selection_v1.json"))
dev = list(csv.DictReader(open(W / "campaign/aggregate_dev_interim2.csv")))
ho = {r["video_id"]: r for r in csv.DictReader(open(W / "campaign/aggregate_heldout.csv"))}
rng = {}
for role in ("LONG", "SHORT"):
    g = [r for r in dev if r["role"] == role + "_DEV"]
    for k in ("events_per_min", "cuts_per_min", "hold_median_s", "activity_frame_share"):
        v = [float(r[k]) for r in g]; lo, hi = min(v), max(v); t = 0.15 * (hi - lo)
        rng[role, k] = (round(lo - t, 3), round(hi + t, 3))
out = []
for vid in sel["long_heldout"] + sel["short_heldout"]:
    if vid not in ho: out.append(dict(video_id=vid, rule="ALL", value="", range="", result="NOT_EVALUATED")); continue
    r = ho[vid]; role = "LONG" if vid in sel["long_heldout"] else "SHORT"; V = W / "videos" / vid
    for q, k in (("Q1", "events_per_min"), ("Q2", "cuts_per_min"), ("Q3", "hold_median_s"), ("Q4", "activity_frame_share")):
        lo, hi = rng[role, k]; x = float(r[k])
        out.append(dict(video_id=vid, rule=q, value=x, range=f"{lo}-{hi}", result="PASS" if lo <= x <= hi else "FAIL"))
    fp = json.load(open(V / "evidence/ffprobe_full.json")); vs = next(s for s in fp["streams"] if s["codec_type"] == "video")
    want = "1920x1080" if role == "LONG" else "1080x1920"; got = f"{vs['width']}x{vs['height']}"
    out.append(dict(video_id=vid, rule="Q5", value=f"{got} {vs['r_frame_rate']}", range=f"{want} 24/1",
                    result="PASS" if got == want and vs["r_frame_rate"] == "24/1" else "FAIL"))
    m = re.search(r"I:\s*(-?[\d.]+) LUFS", (V / "evidence/ebur128.txt").read_text())
    lufs = float(m.group(1)) if m else None
    out.append(dict(video_id=vid, rule="Q6", value=lufs, range="-17.3--15.7",
                    result="UNAVAILABLE" if lufs is None else "PASS" if -17.3 <= lufs <= -15.7 else "FAIL"))
    if role == "LONG":
        last = list(csv.DictReader(open(V / "tables/segments_v1.csv")))[-1]
        ok = last["kind"] == "HOLD" and int(last["frames"]) in (239, 240)
        out.append(dict(video_id=vid, rule="Q7", value=f"{last['kind']} {last['frames']}f", range="HOLD 239-240f", result="PASS" if ok else "FAIL"))
with open(W / "campaign/heldout_quant.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for o in out: print(o)
