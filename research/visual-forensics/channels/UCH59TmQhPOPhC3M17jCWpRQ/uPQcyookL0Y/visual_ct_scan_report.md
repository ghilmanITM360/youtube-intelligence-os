# Visual CT scan report — uPQcyookL0Y (Barely Evolved) — checkpoint J — PARTIAL

Status: `VISUAL_ANALYSIS_PARTIAL`. Not `CT_SCAN_COMPLETE`. No audio listening (`FULL_AV_SIGNOFF` pending). All states `DRAFT_UNVALIDATED`.
Source: 1920x1080 h264, 29.97 fps CFR, 14,647 frames, 488.78 s audio; sha256 1416669f…a0c69d.

## What is MEASURED
- All 14,647 frames measured (FULL_FRAME_MEASUREMENTS.csv); PTS CFR, every delta 1001 ticks.
- states_v4_draft.csv: 89 shot-level states, frames 0-14646, 0 gaps / 0 overlaps (script asserts). Duration (seconds = frames*1001/30000): mean 5.49, median 4.2, p10 2.17, p90 9.38, max 29.53; 10.9 states/min.
- ASR (PROVISIONAL, not listening): 76 segments, 1,141 words, 140 words/min overall; per-chapter table tables/chapter_pacing_v4.csv.

## What is OBSERVED (by reviewers/orchestrator looking at downscaled stills; scope per row)
- 113/113 intra-state BURST candidates: sparse 4-frame review (SCALE_OR_CAMERA_MOVE 46, FADE_OR_WIPE 23, OBJECT_ENTRY_OR_EXIT 20, HARD_CUT 9 [all at existing state starts], TEXT_OR_GRAPHIC_CHANGE 7, CHARACTER_ACTION 4, UNCLEAR 4 -> resolved at dense scope by reviewer_9).
- 52/52 STILL_ONSET/MOTION_ONSET candidates: 6-tile 320px review (reviewer_10). Of 16 'new shot' calls, 13 coincide with known v3 starts, 2 refuted (seq132, seq148), 1 confirmed (seq150) -> the only v4 change.
- 10 merge boundaries + X001/X059 + 4 bursts + 3 in-state candidates: consecutive frames at 480x270 (reviewers 9, 11). Details: tables/v4_corrections_and_annotations.csv.
- Chapter structure (from PROVISIONAL ASR, corroborated by on-screen cards at f2602 '5. Ice Age' = 86.9 s and 'Yersinia pestis' f10244-10326 = 341.9-344.6 s): hook 0-86 s; #5 Ice Age 86-172; #4 Agriculture 172-264; #3 Mongol invasions 264-318; #2 Black Death 318-387; #1 Toba 387-474; outro 474-488.

## What is INFERRED (not observed)
- Shot-vs-card-swap is a convention: a white card whose figures swap in place is ONE state here; a different reading would raise the shot count. Flat-vector/cut-out explainer style is the working description, not a certified production method.
- Narration<->visual relation is only checked at the two anchor points above; audio_visual_alignment.csv leaves visual_relation NOT_ASSESSED.

## UNAVAILABLE / NOT DONE
Audio listening; sound design; native-resolution (1080p) review of any window (all reviews used downscaled montages); per-state art-direction audit (palette sampling, type, line weight) for 89 states; per-state image/video prompts; second-model/human review of the dense calls; YouTube identity check beyond filename+hash+duration; retention/CTR data (none supplied).

## Review independence
Reviewers 1-11 are same-model fresh-context subagents (each a single viewer), audited by transcript (image reads confirmed) and file write. This is not human or different-model review; the kit's acceptance text (ref 13) does not require one for VISUAL_ANALYSIS_PARTIAL, and none is claimed. Structural validation (gaps, overlaps, checksums) is separate from semantic review.
