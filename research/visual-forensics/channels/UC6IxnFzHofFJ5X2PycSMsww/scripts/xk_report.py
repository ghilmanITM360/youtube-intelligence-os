"""Assemble visual_ct_scan_report.md for a reviewer-annotated video from measured data + validated reviewer observations
+ primary spot-check record. Usage: python3 -I xk_report.py <video_dir> <reviewer_id>"""
import csv, json, sys, pathlib
V = pathlib.Path(sys.argv[1]).resolve(); RV = sys.argv[2]; vid = V.name
sm = json.load(open(V / "source_manifest.json"))["source"]; cov = json.load(open(V / "coverage.json"))
pal = json.load(open(V / "tables/palette_measured.json")); asrc = json.load(open(V / "asr/asr_vs_catalog_caption.json"))
val = json.load(open(V / "review" / RV / "validation.json")); spot = json.load(open(V / "review/primary_spotcheck.json"))
cen = {r["video_id"]: r for r in csv.DictReader(open(V.parents[1] / "census/census.csv"))}[vid]
shots = list(csv.DictReader(open(V / "shot_ledger.csv"))); S = list(csv.DictReader(open(V / "tables/state_ledger.csv")))
acts = [x for x in S if x["kind"] == "ACTIVITY"]
from collections import Counter
cls = Counter(c for x in acts for c in x["event_class"].split("+"))
obs = (V / "review" / RV / "observations.md").read_text()
txt = f"""# Visual CT scan — {vid} "{cen['title']}" ({cen['format_class']})

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: {cen['format_evidence']}; published {cen['publish_datetime']}; public views at census {cen['views_player']} (single snapshot; no CTR/retention).
- Source `{sm['file_path']}` sha256 `{sm['sha256']}`, {sm['resolution']} {sm['video_codec']}, {sm['frame_rate_avg']} ({sm['vfr_status']}), time_base {sm['time_base']}, {sm['decoded_frames']} decoded frames, {sm['duration_seconds']:.3f} s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `{RV}` (Claude Code sonnet subagent; transcript audit: {val['provenance'].get('unique_sheets_opened')}/{val['provenance'].get('sheets_expected')} sheets opened, {val['provenance'].get('image_results')} image results, validator errors {len(val['errors'])}); primary spot-check: {spot['summary']}.

## 1. Coverage (MEASURED)
All {cov['frames_total']} frames measured. {cov['segments']} segments = {cov['holds']} HOLD states ({cov['hold_frames']} frames, measured static; settled frame viewed) + {cov['activities']} ACTIVITY events ({cov['activity_frames']} frames; {cov['activity_frames_viewed']} viewed in tiles; {cov['activities_fully_viewed']} activities viewed at every frame). Encoder-refresh frames absorbed by rule: {cov['encoder_artifact_frames_absorbed']}. Unresolved segments: {', '.join(val['unresolved']) or 'none'}.

## 2. Structure (OBSERVED, from ledgers)
- {len(shots)} shots (composition replacements incl. cuts back), {len(acts)} activity events: GRAPHIC/TEXT {cls['GRAPHIC/TEXT']}, CAMERA {cls['CAMERA']}, CHARACTER {cls['CHARACTER']}, LIGHT/COLOR/EFFECT {cls['LIGHT/COLOR/EFFECT']}, SHOT_CUT {cls['SHOT_CUT']}, FALSE_POSITIVE {cls['FALSE_POSITIVE']}.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/{RV}/observations.md`)

{obs.split(chr(10), 1)[1] if obs.startswith('#') else obs}

## 4. Art direction (MEASURED palette)
Background exact {pal['background_exact_rgb']}; top quantised bins {', '.join(b['hex_bin_centre'] + ' ' + str(b['share']) for b in pal['top_bins'][:5])}; mean settled dark-ink coverage {pal['mean_dark_ink_frac']*100:.1f}% (max {pal['max_dark_ink_frac']*100:.1f}%); red accent present in {pal['holds_with_red_accent']}/{pal['holds']} holds; any saturated colour in {pal['holds_with_any_saturation']}/{pal['holds']} holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio {asrc.get('ratio')} ({asrc.get('matched_words')}/{asrc.get('caption_words')} caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
"""
(V / "visual_ct_scan_report.md").write_text(txt); print("report", len(txt.split()), "words")
