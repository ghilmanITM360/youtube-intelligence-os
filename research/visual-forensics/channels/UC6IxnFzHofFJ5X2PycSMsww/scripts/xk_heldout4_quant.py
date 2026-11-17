"""Held-out-4 measurement-only checks (HELDOUT_PROTOCOL_v4.md) from segments_v1.csv, before any reviewer.
Q2 (hard cuts) needs reviewer SHOT_CUT classes -> PENDING_REVIEWER here. Usage: python3 -I xk_heldout4_quant.py <ws>"""
import csv, json, re, statistics as st, sys, pathlib
W = pathlib.Path(sys.argv[1]); ids = json.load(open(W / "selection/selection_v4_heldout4.json"))["long_heldout4"]
dev = [r for r in csv.DictReader(open(W / "campaign/aggregate_dev_final.csv")) if r["role"] == "LONG_DEV"]
a = [float(r["activity_frame_share"]) for r in dev]; t = 0.15 * (max(a) - min(a))
R = dict(Q1=(15.75, 32.65), Q3=(1.02, 2.58), Q4=(round(min(a) - t, 3), round(max(a) + t, 3)), Q6=(-17.3, -15.6))
out = []
def add(v, q, x, rng, ok): out.append(dict(video_id=v, rule=q, value=x, range=rng, result=ok))
for v in ids:
    V = W / "videos" / v
    if not (V / "tables/segments_v1.csv").exists(): add(v, "ALL", "", "", "NOT_EVALUATED"); continue
    S = list(csv.DictReader(open(V / "tables/segments_v1.csv")))
    fp = json.load(open(V / "evidence/ffprobe_full.json")); vs = next(s for s in fp["streams"] if s["codec_type"] == "video")
    N = sum(int(s["frames"]) for s in S); fps = 24; dur = N / fps
    acts = [s for s in S if s["kind"] == "ACTIVITY"]; holds = [int(s["frames"]) / fps for s in S if s["kind"] == "HOLD"]
    for q, x in (("Q1", round(len(acts) / dur * 60, 1)), ("Q3", round(st.median(holds), 2)),
                 ("Q4", round(sum(int(s["frames"]) for s in acts) / N, 3))):
        lo, hi = R[q]; add(v, q, x, f"{lo}..{hi}", "PASS" if lo <= x <= hi else "FAIL")
    if v != "qu8nx1qUwEU":  # Q3b: v0.5 2026 claim, 2026 videos only
        x = round(st.median(holds), 2); add(v, "Q3b", x, "1.10..1.90", "PASS" if 1.10 <= x <= 1.90 else "FAIL")
    add(v, "Q2", "", "2.69..8.26", "PENDING_REVIEWER")
    got = f"{vs['width']}x{vs['height']} {vs['r_frame_rate']}"; add(v, "Q5", got, "1920x1080 24/1", "PASS" if got == "1920x1080 24/1" else "FAIL")
    m = re.search(r"I:\s*(-?[\d.]+) LUFS", (V / "evidence/ebur128.txt").read_text()); x = float(m.group(1)) if m else None
    add(v, "Q6", x, "-17.3..-15.6", "UNAVAILABLE" if x is None else "PASS" if -17.3 <= x <= -15.6 else "FAIL")
    last = S[-1]; add(v, "Q7", f"{last['kind']} {last['frames']}f", "HOLD 235..240f",
                      "PASS" if last["kind"] == "HOLD" and 235 <= int(last["frames"]) <= 240 else "FAIL")
with open(W / "campaign/heldout4_quant.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for o in out: print(o["video_id"], o["rule"], o["value"], o["result"])
