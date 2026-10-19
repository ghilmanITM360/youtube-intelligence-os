#!/usr/bin/env python3
"""Compose videos/<vid>/FORENSIC_REVIEW.md = automatic facts block (from inventory + QA.json + tables) + authored findings.

Usage: python3 -E write_review.py <video_id>     (authored bullets in videos/<vid>/review/findings.md)
"""
import csv, json, os, sys
import numpy as np
RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vid = sys.argv[1]
vd = os.path.join(RDIR, "videos", vid)
inv = [r for r in csv.DictReader(open(os.path.join(RDIR, "SOURCE_MEDIA_INVENTORY.csv"))) if r["Video_ID"] == vid and r["Canonical_For_Analysis"] == "True"][0]
q = json.load(open(os.path.join(vd, "QA.json")))
d = q["derived_statistics"]
al = list(csv.DictReader(open(os.path.join(vd, "NARRATION_VISUAL_ALIGNMENT.csv"))))
cuts = [int(r["Offset_To_Nearest_Word_ms"]) for r in al if r["Composition_Reset_At_Event"] == "True"]
am = list(csv.DictReader(open(os.path.join(vd, "auto", "audio_metrics.csv"))))
db = np.array([float(r["rms_db"]) for r in am]); thr = np.percentile(db, 90) - 14
ae = list(csv.DictReader(open(os.path.join(vd, "AUDIO_EVENTS.csv"))))
pauses = [r for r in ae if r["Type"] == "PAUSE"]
sc = [float(s["Duration_S"]) for s in csv.DictReader(open(os.path.join(vd, "SCENE_TIMELINE.csv")))]
ops = q["counts"]["operations"]
cad = d["native_cadence"]["interpretation"]
fp = d["frame_classes_pct"]
status = "VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED" if q["analysis_depth"].startswith("DEPTH_A") else "VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED"
txt = f"""# Forensic review — {vid} "{inv['Public_Title']}"

Status: `{status}` (single reviewer, no independent QA). Machine checks: {'all pass' if q['all_checks_pass'] else 'FAILURES - see QA.json'} (`QA.json`).

## Source (MEASURED)
`{inv['Filename']}` (`{inv['Source_ID']}`), SHA256 `{inv['SHA256'][:8]}...{inv['SHA256'][-5:]}`, H.264/AAC, {inv['Width']}x{inv['Height']}, {inv['FPS_Avg']} fps, {inv['Video_Frames_Counted']} frames (decoded = ffprobe), {inv['Duration_S']} s. {inv['Video_Type']} uploaded {inv['Upload_Date']}, {int(inv['Public_Views_Snapshot']):,} views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). {'360p limits line weight and small-motion measurement.' if int(inv['Width']) <= 360 else ''}

## Depth
{q['analysis_depth']}. Audio: whole track measured ({100*float((db > thr).mean()):.0f} % voiced, {len(pauses)} pauses >=0.25 s, {sum(1 for p in pauses if p['Aligned_Visual_Event'])} of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-{q['coverage']['frames_decoded']-1}.

## Measured statistics
- {q['counts']['scenes']} scenes (median {np.median(sc):.2f} s, p10 {np.percentile(sc,10):.2f}, p90 {np.percentile(sc,90):.2f}, longest {max(sc):.2f}); {d['hard_cuts']} hard cuts ({d['hard_cuts_per_min']}/min); {q['counts']['events']} events ({d['visual_events_per_min']}/min), {q['counts']['instant_events']} of them one-frame.
- Operations: {', '.join(f'{k} {v}' for k, v in sorted(ops.items(), key=lambda kv: -kv[1]))}.
- Frame-weighted: static hold {fp['STATIC_HOLD']} %, plausibly conventional keyframe/compositing {fp['CONV']} %, screen recording {fp['SCREENREC']} %, complex continuous animation {fp['COMPLEX']} %, change of undetermined method {fp.get('INDET', 0)} %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median {np.median(cuts):.0f} ms (p10 {np.percentile(cuts,10):.0f}, p90 {np.percentile(cuts,90):.0f}; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: {cad}.

## Findings
"""
fn = os.path.join(vd, "review", "findings.md")
txt += open(fn).read() if os.path.exists(fn) else "(authored findings missing)\n"
open(os.path.join(vd, "FORENSIC_REVIEW.md"), "w").write(txt)
print("wrote", os.path.join(vd, "FORENSIC_REVIEW.md"))
