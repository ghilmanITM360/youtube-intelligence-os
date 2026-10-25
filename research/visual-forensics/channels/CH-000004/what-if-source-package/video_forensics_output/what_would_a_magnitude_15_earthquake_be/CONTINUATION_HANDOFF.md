# Continuation Handoff — what_would_a_magnitude_15_earthquake_be

PROJECT ROOT: `/Users/ghilmanislam360/GhilmanProjects/video data of what if`
VIDEO_SLUG: `what_would_a_magnitude_15_earthquake_be`
REFERENCE VIDEO: `/Users/ghilmanislam360/Downloads/YTDown.com_YouTube_What-would-a-magnitude-15-earthquake-be-_Media_e3uk7jU3RHo_002_720p.mp4`
CURRENT VIDEO SUBFOLDER: `video_forensics_output/what_would_a_magnitude_15_earthquake_be/`
GOVERNING SPEC: VIDEO_FORENSIC_REBUILD_SYSTEM v8.0-COMPACT

## Status: COMPLETE (not a checkpoint stop)
This project was completed in a single pass; this handoff exists per the governing spec's required per-video file set, not because of a 90%-usage stop.

## What was completed and validated
All applicable stages: source+audio inspection, evidence/frame extraction (93 overview frames at 0.5fps + 185 dense frames at 1fps + targeted native-resolution grabs), shot detection (**16 shots**, all 16 boundaries corroborated by measured `ffmpeg scdet` score spikes >=5.4), visual-state detection (47 states), canonical timeline, visual DNA, asset manifest (39 assets), motion event map (33 motions), audio map (26 measured silence gaps; transcript unavailable, on-screen text only partially covers narration), CapCut rebuild (16 per-shot recipes), image inventory (29 numbered entries, extensive reuse including 3 first/last-frame pairs), image prompts, animation prompts (33, all <=500 chars), I2V rebuild (16 per-shot blocks), master report, and final validation (`00_source/verify.py`).

## What is partial
Nothing.

## What was not started
N/A — no further stage remains for this video under the governing spec.

## Canonical ID counts / last IDs
- Shots: S01-S16 (last: S16)
- States: 47 total (last: F16.0)
- Motion events: A01-A33 (last: A33)
- Images: IMG01-IMG29 (last: IMG29; notable reuse — IMG14 reused across S10 and S12; IMG16 reused across three S12 sub-states; IMG17 reused across S12/S13)
- Assets: 39 (C01-C05, E01-E06, O01-O17, G01-G07, T01-T03, AU01)

LAST COMPLETED SHOT: S16 (credits)
LAST COMPLETED STATE: F16.0
LAST COMPLETED MOTION EVENT: A33
LAST COMPLETED IMAGE: IMG29
LAST COMPLETED CAPCUT SHOT: S16
LAST COMPLETED I2V SHOT: S16
LAST AUDIO RANGE ANALYZED: full 0.000s-185.341678s (silence-scan complete)

## Important file paths
See `MASTER_REPORT.md` §10 File index for the full list.

## Raw evidence status
- Original source video: untouched, SHA-256 `b7b66d11af29d37aea735e94e5df5c97a589e060d44c009abc38661ac45aa1e7` (see `00_source/SOURCE_MANIFEST.md`).
- Extracted audio: `00_source/audio/audio_original.aac` (lossless stream copy) and `00_source/audio/audio.wav` (mono 16kHz PCM, analysis only).
- 93 overview frame JPGs (1 per 2s) in `01_evidence/frames/`; 185 dense frame JPGs (1 per 1s) in `01_evidence/dense/`; 3 overview contact sheets; 8 tiled dense-inspection sheets (`DENSE_A` through `DENSE_H`) used to pin exact per-second transitions; 4 targeted native-resolution single-frame grabs in `01_evidence/cuts/` used to read exact on-screen text. All safe to keep or prune; not required for downstream stages beyond what's already extracted into the CSVs/MDs.

## Known issues (do not silently "fix" by guessing)
1. No speech transcript — local whisper/mlx-whisper install failed in this environment (broken system pip / `truststore` macOS-version-parsing bug), consistent with every other video in this project. On-screen text here covers only headlines/captions/gag props (newspaper, phone alert, LIVE-TV box), not the narrator's actual explanation of each magnitude value — that content is genuinely UNKNOWN. If a working transcription tool becomes available later, re-run it against `00_source/audio/audio.wav` and update `SCRIPT_OR_AUDIO_CUE` in `TIMELINE.csv` — do not regenerate the visual analysis, it does not depend on the transcript.
2. All 16 shot boundaries are OBSERVED (measured `ffmpeg scdet` score spikes >=5.4: 16.916667, 18.916667, 24.041667, 27.458333, 46.25, 66.666667, 74.583333, 77.625, 83.291667, 92.75, 97.083333, 125.958333, 132.583333, 170.958333, 175.291667). A much larger set of lower-score spikes (2.0-4.9) corresponds to intra-shot magnitude-value swaps and is captured as visual-state transitions / motion events, not as additional shots — this interpretation is LIKELY, confirmed visually at 1fps sampling but not independently re-verified at native frame rate for every single sub-3.0 spike.
3. The S10->S12 boundary at 92.75s (sun/sunquake -> magnetar -> Magnitude-25-sun region, approx. t83-103s) could not be pinned to an obvious visual swap at 1fps sampling resolution — the magnetar image appears to visually persist across this measured cut. F12.0's exact start content is flagged APPROXIMATE in `TIMELINE.csv`, `MOTION_EVENTS.csv` (motion A17), `CAPCUT_REBUILD.md`, and `I2V_REBUILD.md`. Do not "correct" this to a precise timestamp without new evidence (e.g. native-fps frame-by-frame extraction of that exact window).
4. A single-frame "MAGNITUDE 0" flicker was measured at approximately t=7s within S01 (between the Magnitude-15 and Magnitude-25 example states). This is treated as a source-rendering artifact per the spec's "ignore compression noise and insignificant frame differences" rule and is deliberately not reproduced in either rebuild pathway.
5. This is a single-topic, single-continuous-scale production (unlike the multi-topic `what_if_earths_water_suddenly_disappear` video) — do not conflate the two videos' structural patterns when reasoning about either.

## Exact next action
None required for completion. If resuming anyway (e.g. to add the transcript per issue #1 above): re-extracting `00_source/audio/audio.wav` is not needed (it already exists); just run a working STT tool against it and patch `TIMELINE.csv`, then re-run `python3 00_source/verify.py`.

## Do-not-redo items
- Do not re-extract frames, contact sheets, or dense-inspection sheets — `01_evidence/` is complete and sufficient.
- Do not renumber any S/F/A/IMG/asset ID.
- Do not regenerate `TIMELINE.csv`, `ASSET_MANIFEST.csv`, or `MOTION_EVENTS.csv` from scratch; patch in place if a specific cell needs correction.
- Do not merge or split any of the 16 shots without new scdet/visual evidence — the shot list was deliberately anchored to measured scene-cut-detector timestamps (score >=5.4), not guessed.

## Git status
Not a Git repository (confirmed via `git rev-parse --is-inside-work-tree` at session start). No Git action was taken or is required.

## Command to resume (if ever needed)
```
cd "/Users/ghilmanislam360/GhilmanProjects/video data of what if"
python3 "video_forensics_output/what_would_a_magnitude_15_earthquake_be/00_source/verify.py"
```
