"""Population-6 measurement-only checks (HELDOUT_PROTOCOL_v6.md). Usage: python3 -I xk_pop6_quant.py <ws>"""
import csv, json, re, statistics as st, sys, pathlib
W = pathlib.Path(sys.argv[1]); ids = json.load(open(W / "selection/selection_v6_pop6.json"))["long_pop6"]
dev = [r for r in csv.DictReader(open(W / "campaign/aggregate_dev_final.csv")) if r["role"] == "LONG_DEV"]
a = [float(r["activity_frame_share"]) for r in dev]; t = 0.15 * (max(a) - min(a))
R = dict(Q1=(15.75, 32.65), Q3=(1.02, 2.58), Q4=(round(min(a) - t, 3), round(max(a) + t, 3)))
out = []
def add(v, q, x, rng, ok): out.append(dict(video_id=v, rule=q, value=x, range=rng, result=ok))
for v in ids:
    V = W / "videos" / v
    if not (V / "tables/segments_v1.csv").exists(): add(v, "ALL", "", "", "NOT_EVALUATED"); continue
    S = list(csv.DictReader(open(V / "tables/segments_v1.csv"))); N = sum(int(s["frames"]) for s in S); dur = N / 24
    acts = [s for s in S if s["kind"] == "ACTIVITY"]; holds = [int(s["frames"]) / 24 for s in S if s["kind"] == "HOLD"]
    for q, x in (("Q1", round(len(acts) / dur * 60, 1)), ("Q3", round(st.median(holds), 2)), ("Q4", round(sum(int(s["frames"]) for s in acts) / N, 3))):
        lo, hi = R[q]; add(v, q, x, f"{lo}..{hi}", "PASS" if lo <= x <= hi else "FAIL")
    vs = next(s for s in json.load(open(V / "evidence/ffprobe_full.json"))["streams"] if s["codec_type"] == "video")
    got = f"{vs['width']}x{vs['height']} {vs['r_frame_rate']}"; add(v, "Q5", got, "1920x1080 24/1", "PASS" if got == "1920x1080 24/1" else "FAIL")
    m = re.search(r"I:\s*(-?[\d.]+) LUFS", (V / "evidence/ebur128.txt").read_text()); x = float(m.group(1)) if m else None
    add(v, "Q6", x, "-17.3..-15.6", "UNAVAILABLE" if x is None else "PASS" if -17.3 <= x <= -15.6 else "FAIL")
    last = S[-1]; add(v, "Q7", f"{last['kind']} {last['frames']}f", "HOLD 235..240f", "PASS" if last["kind"] == "HOLD" and 235 <= int(last["frames"]) <= 240 else "FAIL")
with open(W / "campaign/pop6_quant.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
p = sum(o["result"] == "PASS" for o in out); print(f"PASS {p}/{len(out)} = {p/len(out):.1%}")
for o in out:
    if o["result"] != "PASS": print(o)
print("share>=0.15:", [o["video_id"] for o in out if o["rule"] == "Q4" and float(o["value"]) >= 0.15])
