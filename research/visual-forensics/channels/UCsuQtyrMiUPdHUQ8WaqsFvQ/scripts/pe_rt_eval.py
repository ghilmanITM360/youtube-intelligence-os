"""Score a reconstruction render against reconstruction/ACCEPTANCE_RT_v1.md (measured checks C1-C10 only).
Usage: python3 -I pe_rt_eval.py <rt_attempt_dir>  (format from ffprobe). Writes RT_EVALUATION.json."""
import csv, json, statistics, sys, pathlib
R = pathlib.Path(sys.argv[1]).resolve()
st = json.load(open(R / "evidence/ffprobe_full.json"))["streams"][0]
W, H, fps = st["width"], st["height"], st["r_frame_rate"]
L = W > H
segs = list(csv.DictReader(open(R / "tables/segments_v1.csv")))
want = list(csv.DictReader(open(R.parent / "intended_timeline.csv"))) if not (R / "intended_timeline.csv").exists() else list(csv.DictReader(open(R / "intended_timeline.csv")))
pal = json.load(open(R / "tables/palette_measured.json")); stroke = json.load(open(R / "tables/stroke_measured.json"))
N = sum(int(s["frames"]) for s in segs); dur = N / 50
acts = [s for s in segs if s["kind"] == "ACTIVITY"]; holds = [s for s in segs if s["kind"] == "HOLD"]
ph = {p["seg"]: p for p in pal["per_hold"]}
on = [int(s["start_frame"]) for s in acts]
matched = sum(any(abs(o - int(w["start_frame"])) <= 2 for o in on) for w in want)
unexpl = [o for o in on if all(abs(o - int(w["start_frame"])) > 2 and not (int(w["start_frame"]) <= o <= int(w["end_frame"])) for w in want)]
bg = pal["background_exact_rgb"]; bgv = [int(bg[i:i + 2], 16) for i in (1, 3, 5)]
v = dict(C1=(fps == "50/1" and (W, H) in [(1920, 1080), (1080, 1920)], f"{W}x{H} {fps} frames={N}"),
         C2=(min(bgv) >= 0xFA, bg),
         C3=statistics.median(int(s["frames"]) / 50 for s in holds),
         C4=sum(int(s["frames"]) == 1 for s in acts) / len(acts),
         C5=len(acts) / dur * 60, C6=pal["mean_dark_ink_frac"],
         C7=sum(ph[s["seg"]]["yellow_frac"] > 0.0005 for s in holds if s["seg"] in ph) / len(holds),
         C8=stroke["per_frame"][0]["median"], C9=matched / len(want), C10=len(unexpl) / len(acts))
rng = dict(C3=((0.50, 1.57), (0.89, 1.34)), C4=((0.833, 1), (0.923, 1)), C5=((34.1, 59.7), (35.7, 47.9)), C6=((0.071, 0.104), (0.079, 0.129)),
           C7=((0.24, 0.62), (0.43, 0.75)), C8=((10, 14), (10, 20)), C9=((0.90, 1), (0.90, 1)), C10=((0, 0.10), (0, 0.10)))
out = {}
for k, x in v.items():
    if k in ("C1", "C2"): out[k] = dict(value=x[1], result="PASS" if x[0] else "FAIL")
    else:
        lo, hi = rng[k][0 if L else 1]; out[k] = dict(value=round(x, 4), range=[lo, hi], result="PASS" if lo <= x <= hi else "FAIL")
res = dict(format="LANDSCAPE" if L else "PORTRAIT", render_sha256=(R / "evidence/render_sha256.txt").read_text().split()[0], checks=out,
           measured_pass=sum(c["result"] == "PASS" for c in out.values()), measured_total=len(out), unexplained_onsets=unexpl,
           intended_events=len(want), measured_activities=len(acts), note="Measured checks only; V1-V6 judged by primary in RT_EVALUATION.md. Audio sync BLOCKED.")
(R / "RT_EVALUATION.json").write_text(json.dumps(res, indent=1)); print(json.dumps(res, indent=0))
