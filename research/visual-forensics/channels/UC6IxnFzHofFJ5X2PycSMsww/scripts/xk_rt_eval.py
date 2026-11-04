"""Evaluate a reconstruction render with the SAME measurement+segmentation used on source videos.
Expects <rt_dir>/tables/segments_v1.csv (from xk_segment.py) and <rt_dir>/RT1_intended_timeline.csv.
Compares measured rhythm to manual v0.2 targets and matches measured ACTIVITY onsets to intended events (±2 frames).
Writes <rt_dir>/RT_EVALUATION.json. Usage: python3 -I xk_rt_eval.py <rt_dir>"""
import csv, json, statistics, sys, pathlib
R = pathlib.Path(sys.argv[1])
segs = list(csv.DictReader(open(R / "tables/segments_v1.csv")))
want = list(csv.DictReader(open(R / "RT1_intended_timeline.csv")))
N = sum(int(s["frames"]) for s in segs); dur = N / 24
acts = [s for s in segs if s["kind"] == "ACTIVITY"]
holds = [int(s["frames"]) / 24 for s in segs if s["kind"] == "HOLD"]
cuts = [s for s in acts if "D2" in s["detectors"]]
m = dict(frames=N, duration_s=round(dur, 2), segments=len(segs), activities=len(acts),
         events_per_min=round(len(acts) / dur * 60, 1), d2_cut_candidates_per_min=round(len(cuts) / dur * 60, 2),
         hold_median_s=round(statistics.median(holds), 2), one_frame_activity_share=round(sum(int(s["frames"]) == 1 for s in acts) / len(acts), 2),
         activity_frame_share=round(sum(int(s["frames"]) for s in acts) / N, 3))
targets = dict(events_per_min=(18.4, 39.2), hold_median_s=(1.13, 2.84), one_frame_activity_share=(0.5, 1.0), activity_frame_share=(0.013, 0.243))
checks = {k: dict(value=m[k], target=v, result="PASS" if v[0] <= m[k] <= v[1] else "FAIL") for k, v in targets.items()}
on = [int(s["start_frame"]) for s in acts]
match = []
for w in want:
    a = int(w["start_frame"]); hit = min(on, key=lambda x: abs(x - a)) if on else None
    match.append(dict(intended=a, device=w["device"], nearest_measured=hit, delta=None if hit is None else hit - a,
                      matched=hit is not None and abs(hit - a) <= 2))
unexplained = [o for o in on if all(abs(o - int(w["start_frame"])) > 2 and not (int(w["start_frame"]) <= o <= int(w["end_frame"])) for w in want)]
out = dict(measured=m, rhythm_checks=checks, intended_events=len(want), intended_matched=sum(x["matched"] for x in match),
           unexplained_measured_onsets=unexplained, matches=match,
           note="Silent render; audio/narration sync not testable. Device-type correctness requires visual review of the render (separate).")
(R / "RT_EVALUATION.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ("measured", "rhythm_checks", "intended_events", "intended_matched", "unexplained_measured_onsets")}, indent=0))
