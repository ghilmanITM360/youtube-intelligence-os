#!/usr/bin/env python3
"""ASR-only (NOT listening) narration pace vs visual rhythm per video. usage: python3 -I narration_rhythm.py
Writes <lib>/_channel/model_sheets/narration_vs_rhythm.csv. Labels: ASR_UNCERTIFIED; relation = INFERRED."""
import csv, json, os, statistics
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); out = f"{H}/asset_library/_channel/model_sheets"
rh = list(csv.DictReader(open(f"{out}/rhythm_by_video.csv"))); res = []
for r in rh:
    p = f"{H}/videos/{r['video_id']}/asr/asr_small_en.json"
    if not os.path.exists(p): continue
    seg = json.load(open(p))["segments"]; words = sum(len(s["text"].split()) for s in seg)
    led = [x for x in csv.DictReader(open(f"{H}/videos/{r['video_id']}/tables/state_ledger.csv")) if x["kind"] != "HOLD"]
    starts = [s["start"] for s in seg]
    near = sum(1 for x in led if min(abs(float(x["start_pts"]) - t) for t in starts) <= 0.5)
    speech = sum(s["end"] - s["start"] for s in seg)
    res.append(dict(video_id=r["video_id"], format=r["format"], rhythm_type=r["rhythm_type"], events_per_min=r["events_per_min"],
                    asr_words_per_min=f"{words/float(r['duration_s'])*60:.0f}", asr_segments_per_min=f"{len(seg)/float(r['duration_s'])*60:.1f}",
                    speech_share=f"{speech/float(r['duration_s']):.2f}", events_within_0_5s_of_asr_segment_start=f"{near/len(led):.2f}", label="ASR_UNCERTIFIED"))
with open(f"{out}/narration_vs_rhythm.csv", "w", newline="") as f: w = csv.DictWriter(f, list(res[0])); w.writeheader(); w.writerows(res)
def corr(a, b):
    ma, mb = statistics.mean(a), statistics.mean(b); return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
for fm in ("LONG_FORM", "SHORT"):
    s = [x for x in res if x["format"] == fm]
    e = [float(x["events_per_min"]) for x in s]
    print(fm, len(s), "r(events/min, words/min)=", round(corr(e, [float(x["asr_words_per_min"]) for x in s]), 2), "r(events/min, segments/min)=", round(corr(e, [float(x["asr_segments_per_min"]) for x in s]), 2),
          "words/min range", min(float(x["asr_words_per_min"]) for x in s), max(float(x["asr_words_per_min"]) for x in s),
          "median share of events near ASR seg start", statistics.median(float(x["events_within_0_5s_of_asr_segment_start"]) for x in s))
