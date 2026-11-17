#!/usr/bin/env python3
"""Deep-VF B3: ASR sentence cues vs reviewed visual events (local only; ASR_UNCERTIFIED, not listening).
usage: /usr/bin/python3 -I script_beats.py
For every library video: each ASR segment gets cue tags by text rules (INFERRED): QUESTION, NUMBER, SCALE, REVERSAL,
SETUP (question-reading), plus PLAIN. Visual events = state_ledger ACTIVITY rows whose start falls in [seg.start, next.start).
Writes deep_vf/script_beats/segments.csv (per ASR segment) and cue_summary.csv (per format x rhythm x cue)."""
import csv, glob, json, os, re, statistics as st
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); OUT = f"{H}/asset_library/_channel/deep_vf/script_beats"; os.makedirs(OUT, exist_ok=True)
strata = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/asset_library/_channel/deep_vf/strata_map.csv"))}
NUMW = r"\b(\d[\d,.]*|one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|billion|trillion|percent|half|twice|dozen)\b"
SCALE = r"\b(times (bigger|larger|more|as)|bigger|larger|smaller|tiny|huge|size|scale|kilomet|meters?|miles?|tons?|degrees|light.?years?|per (second|hour|day))\b"
REV = r"\b(but|however|actually|unfortunately|turns out|instead|except|although|on the other hand)\b"
def cues(t, i):
    c = []
    if i <= 2 and re.search(r"(question|asks|asked)", t, re.I): c.append("SETUP")
    if "?" in t: c.append("QUESTION")
    if re.search(NUMW, t, re.I): c.append("NUMBER")
    if re.search(SCALE, t, re.I): c.append("SCALE")
    if re.search(REV, t, re.I): c.append("REVERSAL")
    return c or ["PLAIN"]
seg_rows = []
for led in sorted(glob.glob(f"{H}/videos/*/tables/state_ledger.csv")):
    v = led.split("/")[-3]; asr = f"{H}/videos/{v}/asr/asr_small_en.json"
    if not os.path.exists(asr) or v not in strata: continue
    S = [s for s in json.load(open(asr))["segments"] if s["text"].strip()]
    ev = [r for r in csv.DictReader(open(led)) if r["kind"] == "ACTIVITY"]
    for i, s in enumerate(S):
        t0, t1 = s["start"], S[i + 1]["start"] if i + 1 < len(S) else s["end"] + 2
        e = [r for r in ev if t0 <= float(r["start_pts"]) < t1]; words = len(s["text"].split())
        seg_rows.append(dict(video_id=v, format=strata[v]["format"], rhythm_tertile=strata[v]["rhythm_tertile"], seg_index=i, t0=f"{t0:.2f}", t1=f"{t1:.2f}",
                             words=words, words_per_s=f"{words / max(t1 - t0, 0.3):.2f}", cues=";".join(cues(s["text"], i)), events=len(e),
                             events_per_s=f"{len(e) / max(t1 - t0, 0.3):.3f}", subtypes=";".join(r["subtype"] for r in e), text=s["text"].strip()))
with open(f"{OUT}/segments.csv", "w", newline="") as fo: w = csv.DictWriter(fo, list(seg_rows[0])); w.writeheader(); w.writerows(seg_rows)
summ = []
for fm in ("LONG_FORM", "SHORT"):
    for rt in ("BUSY", "MID", "CALM", "ALL"):
        for cue in ("SETUP", "QUESTION", "NUMBER", "SCALE", "REVERSAL", "PLAIN", "ANY"):
            x = [r for r in seg_rows if r["format"] == fm and (rt == "ALL" or r["rhythm_tertile"] == rt) and (cue == "ANY" or cue in r["cues"].split(";"))]
            if len(x) < 5: continue
            dur = sum(float(r["t1"]) - float(r["t0"]) for r in x); ne = sum(r["events"] for r in x)
            subs = [s for r in x for s in r["subtypes"].split(";") if s]
            top = sorted(set(subs), key=subs.count, reverse=True)[:3]
            summ.append(dict(format=fm, rhythm=rt, cue=cue, segments=len(x), videos=len({r["video_id"] for r in x}), events_per_min=f"{60 * ne / dur:.1f}",
                             share_segments_with_event=f"{sum(r['events'] > 0 for r in x) / len(x):.2f}", words_per_s=f"{st.mean(float(r['words_per_s']) for r in x):.2f}",
                             top_subtypes=";".join(f"{s}:{subs.count(s)}" for s in top)))
with open(f"{OUT}/cue_summary.csv", "w", newline="") as fo: w = csv.DictWriter(fo, list(summ[0])); w.writeheader(); w.writerows(summ)
for r in summ: print(r["format"], r["rhythm"], r["cue"], r["segments"], r["videos"], r["events_per_min"], r["share_segments_with_event"], r["words_per_s"], r["top_subtypes"])
