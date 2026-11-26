# Measured ledgers for 20 long videos and 24 Shorts (built 2026-11-23)

Status: **MEASURED from frame differences, NOT VIEWED, NOT INTERPRETED.** Self-review; no second reviewer. These are not the campaign's visually reviewed ledgers: the campaign's `VERIFIED_VISUAL` tier needs a person or model to look at the frames. These give the same timing skeleton (when the picture changes) for videos the campaign never analysed.

## What a ledger is
- **Shot ledger** (`shot_ledger.csv`): one row per shot = the span between two hard changes of the picture. Says when each shot starts and ends, how long it is, how many visual events happen in it, what was said during it (ASR text), and a still image of it (`keyframes/SHxxx.jpg`).
- **Visual event ledger** (`visual_event_ledger.csv`): one row per **visual event** = a burst of consecutive frames where part of the picture changes (a drawing appears, text is written on, a scene is swapped). Says when it starts and ends, how big and where on the frame the change is, and whether ink was added or removed.
- Together they answer "how often does the picture change, and where" without anyone looking at the video. They do **not** say what the change is (that is the empty interpretation columns).

## Where
Folder: `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/ledgers_measured/`
- `INDEX.csv`: one row per video (47 targets: 44 built, 3 `UNAVAILABLE_NO_MEDIA`: `alkJ7xScBiw`, `NxVdO7M2YdM`, `XwJAbyn5uGY`).
- `ALL_SHOT_LEDGER.csv` (719 shots) and `ALL_EVENT_LEDGER.csv` (2,160 events): every video in one file each.
- `<video_id>/`: `shot_ledger.csv`, `visual_event_ledger.csv`, `summary.json`, `keyframes/`.
- `VALIDATION_vs_campaign.csv`: per-video comparison with the campaign ledgers (see below).

## Columns
Shot ledger: `video_id, shot_id, start/end_pts_seconds, start/end_frame, duration_s, boundary_evidence, boundary_strength` (share of pixels that changed at the boundary), `events_in_shot, events_per_min, asr_words, asr_text` (whisper.cpp small.en, uncertified), `keyframe, evidence_label`, then empty `subject, setting, framing, camera_motion, graphics_text, narrative_function` and `interpretation_status = NOT_VIEWED`.
Event ledger: `video_id, shot_id, event_id, start/end_pts_seconds, start/end_frame, frames, event_scope` (FULL_FRAME / REGIONAL / LOCAL by the changed area), `event_tempo` (INSTANT up to 3 frames, PROGRESSIVE longer, e.g. writing on), `ink_direction` (INK_ADDED / INK_REMOVED / INK_NEUTRAL), `ink_delta, peak_changed_fraction, bbox_x0..y1` (normalised box of the change), `contains_shot_boundary_candidate`, `event_class = UNCLASSIFIED`, `evidence_label`, `interpretation_status = NOT_VIEWED`.

## Method (`scripts/ledger_lib.py`, `ledger_build.py`)
Decode each file to a small grey frame (256x144, or 144x256 for Shorts), difference consecutive frames. A pixel counts as changed above 24 grey levels. A frame is active if at least 0.04% of pixels changed; active frames up to 2 frames apart merge into one event. A frame is a shot-boundary candidate if at least 8% of pixels changed and the change box spans at least half the frame width and height. Thresholds were tuned on 5 campaign videos (`ledger_tune.py`, `ledger_tune2.py`) and frozen before the validation.

## Validation against the campaign's reviewed ledgers (38 videos not used for tuning, `ledger_validate.py`)
| | Campaign | Measured | Matched | Precision | Recall |
|---|---|---|---|---|---|
| Events (onset within 3 frames), 38 videos | 2,219 | 2,226 | 2,120 | 0.95 | 0.96 |
| Shot boundaries (within 2 frames), 38 videos | 548 | 676 | 472 | 0.70 | 0.86 |
| Shot boundaries, long (20) / Shorts (18) | 398 / 150 | 522 / 154 | 359 / 113 | 0.69 / 0.73 | 0.90 / 0.75 |
Cross-check on the 20 long videos against the campaign's own measurement tables (`tables/segments_v1.csv`, `scenedetect_candidates.csv`): events / campaign ACTIVITY segments median ratio 1.03; shots / campaign scenes median ratio 1.77.

## How to read the numbers
- **Event timing is reliable** at the level tested (about 95% agreement with reviewed ledgers). Use events for "how often does the picture change" (20 long videos: median 21.9 events per minute; 24 Shorts: 19.8; the campaign's reviewed long-form median was 22.5).
- **Shot boundaries over-count by about 30%** (large in-shot drawings trigger them). Measured median shot is 6.75 s for these 20 long videos against the campaign's reviewed 8.44 s on other videos; do not compare the two as a finding. Use `boundary_strength` to filter, and check a boundary against its keyframes before relying on it. Whether strength predicts correctness was not tested.
- Whisper text is uncertified and cut into segments; `asr_words` per shot is approximate.

## Limits
Not viewed; no event classes, no subjects, no camera or graphics notes. Frame-difference measurement misses changes below the threshold and splits slow dissolves. 3 videos have no media. Validation used the campaign's ledgers as the reference, which are themselves same-model-family reviewed.

## To make them reviewed ledgers
Look at each shot's keyframe (and frames around each event), fill the interpretation columns and `event_class`, set `interpretation_status`, then a second reviewer. That is new perception work: about 720 keyframes and 2,160 events here.

## Recompute
`uv run --no-project --with numpy python scripts/ledger_build.py` (about 8 minutes; needs ffmpeg, ffprobe, the media library and `phase7b_asr/`, `phase7c_asr/`), `ledger_validate.py` for the validation.


## Small additions (added 2026-11-23)

`SMALL_ADDITIONS_ALL.csv` and each `<id>/small_additions.csv`: 74 small objects (58 from the compact/mid review, 16 from the scattered review; column review_pass) that appear in HOLD stretches (typed characters, dashes, strikes, small figures), coded by one reviewer from stills and an x8 difference image (status OBSERVED). They are NOT counted in the event totals or events per minute above. `description` is one reader's reading from the viewed cells (9 of 58 marked read uncertain). 18 of the 33 videos have no ledger folder; theirs are in `../ledgers_small_additions_only/`.
