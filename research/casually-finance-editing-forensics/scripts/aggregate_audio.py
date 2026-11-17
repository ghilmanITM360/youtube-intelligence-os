#!/usr/bin/env python3
"""Aggregate MEASURED audio-signal statistics over all validated videos (no listening; signal + Whisper ASR only).

Usage: python3 -E aggregate_audio.py        -> prints a summary and writes evidence/audio_aggregate.json
Per video: voiced fraction (50 ms windows within 14 dB of the 90th-percentile RMS), words/min over the whole video, phrase rate
(NARRATION_PHRASE rows with >= 4 words), pauses >= 0.25 s per minute and their length, speech level (median RMS of voiced windows),
pause noise floor (median RMS inside PAUSE rows), spectral flux at hard-cut times versus all windows, cut-to-ASR-word offsets.
"""
import csv, json, os
import numpy as np
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = {}
for d in sorted(os.listdir(os.path.join(R, "videos"))):
    q = os.path.join(R, "videos", d, "QA.json")
    if not os.path.exists(q) or not json.load(open(q)).get("all_checks_pass"):
        continue
    vd = os.path.join(R, "videos", d)
    am = list(csv.DictReader(open(os.path.join(vd, "auto", "audio_metrics.csv"))))
    t = np.array([float(x["t_sec"]) for x in am]); db = np.array([float(x["rms_db"]) for x in am]); fx = np.array([float(x["flux"]) for x in am])
    dur = t[-1] + 0.05
    voiced = db > np.percentile(db, 90) - 14
    ae = list(csv.DictReader(open(os.path.join(vd, "AUDIO_EVENTS.csv"))))
    ph = [float(x["Words_Per_S"]) for x in ae if x["Type"] == "NARRATION_PHRASE" and int(x["Words"]) >= 4]
    pa = [(float(x["Start_S"]), float(x["End_S"])) for x in ae if x["Type"] == "PAUSE"]
    pl = [b - a for a, b in pa]
    pf = []
    for a, b in pa:
        m = (t >= a) & (t < b)
        if m.any():
            pf.append(float(np.median(db[m])))
    words = len(list(csv.DictReader(open(os.path.join(vd, "auto", "asr_words.csv")))))
    me = list(csv.DictReader(open(os.path.join(vd, "MOTION_EVENTS.csv"))))
    cut_t = [float(x["Start_S"]) for x in me if x["Operation"] == "HARD_CUT_REPLACE"]
    def fmax(c):
        i = int(round(c / 0.05)); return float(fx[max(i - 2, 0):min(i + 3, len(fx))].max())  # +-100 ms window
    cf = [fmax(c) for c in cut_t]
    rs = np.random.RandomState(7)
    rf = [fmax(float(c)) for c in rs.uniform(0.2, dur - 0.2, size=max(len(cut_t), 5))]
    al = list(csv.DictReader(open(os.path.join(vd, "NARRATION_VISUAL_ALIGNMENT.csv"))))
    co = [int(x["Offset_To_Nearest_Word_ms"]) for x in al if x["Composition_Reset_At_Event"] == "True"]
    rows[d] = dict(duration_s=round(dur, 2), voiced=float(voiced.mean()), wpm=words / (dur / 60), phrase_wps=ph, pauses_per_min=len(pa) / (dur / 60), pause_len=pl,
                   speech_db=float(np.median(db[voiced])), rand_flux=rf, pause_floor_db=(float(np.median(pf)) if pf else None), cut_flux=cf, all_flux_median=float(np.median(fx)), cut_offsets_ms=co)
def rng(v): v = [x for x in v if x is not None]; return [round(float(np.median(v)), 2), round(float(min(v)), 2), round(float(max(v)), 2)]
allco = sum([r["cut_offsets_ms"] for r in rows.values()], []); allph = sum([r["phrase_wps"] for r in rows.values()], []); allpl = sum([r["pause_len"] for r in rows.values()], [])
allcf = sum([r["cut_flux"] for r in rows.values()], [])
out = dict(videos=len(rows), minutes=round(sum(r["duration_s"] for r in rows.values()) / 60, 1),
           voiced_pct_median_min_max=[round(100 * x, 1) for x in rng([r["voiced"] for r in rows.values()])],
           wpm_median_min_max=rng([r["wpm"] for r in rows.values()]),
           phrase_wps_pooled=dict(n=len(allph), median=round(float(np.median(allph)), 2), p10=round(float(np.percentile(allph, 10)), 2), p90=round(float(np.percentile(allph, 90)), 2)),
           pauses_per_min_median_min_max=rng([r["pauses_per_min"] for r in rows.values()]),
           pause_length_pooled=dict(n=len(allpl), median=round(float(np.median(allpl)), 2), longest=round(float(max(allpl)), 2)),
           speech_db_median_min_max=rng([r["speech_db"] for r in rows.values()]),
           pause_floor_db_median_min_max=rng([r["pause_floor_db"] for r in rows.values()]),
           cut_flux_max100ms_median=round(float(np.median(allcf)), 2), random_time_flux_max100ms_median=round(float(np.median(sum([r["rand_flux"] for r in rows.values()], []))), 2),
           cut_to_word_pooled=dict(n=len(allco), median_ms=round(float(np.median(allco)), 1), p10=round(float(np.percentile(allco, 10)), 1), p90=round(float(np.percentile(allco, 90)), 1),
                                   within_100ms_pct=round(100 * float(np.mean(np.abs(allco) <= 100)), 1), lead_pct=round(100 * float(np.mean(np.array(allco) < 0)), 1)),
           per_video={k: {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items() if kk in ("duration_s", "voiced", "wpm", "pauses_per_min", "speech_db", "pause_floor_db")} for k, v in rows.items()})
json.dump(out, open(os.path.join(R, "evidence", "audio_aggregate.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "per_video"}, indent=1))
