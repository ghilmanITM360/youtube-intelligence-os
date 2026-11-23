# Checkpoint 1: xkcd What If complete forensics (2026-11-23)

**Done (Phases 0 to 4):** `00_PHASE0_WORKSPACE_STATE.md`, `01_*` (3 files), `02_*` (5 files), `03_CHANNEL_MASTER_INVENTORY.csv`, `03_VIDEO_IDENTITY_CROSSWALK.csv`, `03_CORPUS_COMPLETENESS_REPORT.md`. Data: `media_probe_88.csv`, `rss_2026-11-23.xml`. Code: `scripts/` (census_check, media_match, probe_all, scan_folders, build_master).

**Repo state:** untouched. Branch `research/what-if-channel-strategy-2026-11-18`, HEAD `9eb4f5ab`, no pushes.

**Self-review only.** No independent reviewer. No new visual or audio analysis was run in this checkpoint.

**Not done:** Phase 5 (cross-video script synthesis, playbook), Phases 6 to 13. They depend on one owner decision: build on the existing campaign (manual v0.7, 64 videos measured) rather than restart visual forensics. See `01_STRATEGY_GAPS_AND_CONFLICTS.md` G2 and G7.

**Resume:** re-run `python3 -I scripts/build_master.py` after any change to media or campaign data.

## Checkpoint 2 (2026-11-23, later): Phases 5 to 13
Done: `05_*` (synthesis, playbook, family and metrics tables), `06_*` (layer reconciliation, aligned timing), `07_10_*` (status), `09_AUDIO_LEVELS_88.csv`, `11_EVIDENCE_REGISTER_PHASE5_13.csv`, `12_*`, `13_FINAL_REPORT.md`. Correction to G3 appended in `01_STRATEGY_GAPS_AND_CONFLICTS.md`. Owner decision taken: build on the existing campaign. Still blocked or not done: listening, science-visual layer, new frame analysis, independent QA (see `13_FINAL_REPORT.md`).

## Checkpoint 3 (2026-11-23): Phase 7 done as a targeted pass; Phases 8 to 13 updated

- New perception: 47 still frames viewed and coded (24 coding + 23 holdout, 24 long videos). Files: `07_SCIENCE_VISUAL_PASS.md`, `07_SCIENCE_VISUAL_CODING_SAMPLE.csv`, `07_SCIENCE_VISUAL_CODING_HOLDOUT.csv`, `07_SAMPLE_FRAMES.csv`, `07_HOLDOUT_FRAMES.csv`, frame sheets in `phase7_frames/` and `holdout7/`, `scripts/phase7_*.py`.
- Updated: `07_10_*` (Phase 7 and 10 rows), `05_MASTER_SCRIPT_PLAYBOOK.md` (section F2), `11_*` (P16 re-rated OBSERVED, P18, P19 added), `12_*`, `13_*`.
- Still unavailable: listening, independent QA, second coder, Shorts and 20 long videos for Phase 7, DEEP_VISUAL tier (0). Self-review throughout.

## Checkpoint 4 (2026-11-23): Phase 7 extended to the other 20 long videos

- 20 local whisper.cpp small.en transcripts (`phase7b_asr/`), 40 frames coded with scheme v1.1 (`07b_SCIENCE_VISUAL_PASS_20_LONG.md`, `07b_SCIENCE_VISUAL_CODING_20LONG.csv`, `07b_SAMPLE_FRAMES.csv`, `phase7b_frames/`, `scripts/phase7b_*.py`). Pooled with Phase 7: 87 frames, 44 long videos. Register now 21 rows (P20, P21 added, P16 updated).
- Still unavailable: listening, independent QA or second coder, Shorts, `alkJ7xScBiw` media, DEEP_VISUAL (0). Self-review.

## Checkpoint 5 (2026-11-23): Phase 7 extended to the Shorts

- 24 more local whisper transcripts (`phase7c_asr/`), one frame per Short, 38 frames coded with scheme v1.1 (`07c_SCIENCE_VISUAL_PASS_SHORTS.md`, `07c_SCIENCE_VISUAL_CODING_SHORTS.csv`, `07c_SAMPLE_FRAMES.csv`, `07c_SHORTS_INVENTORY.csv`, `phase7c_frames/`, `scripts/phase7c_*.py`). All frames: 125. Register 23 rows (P22, P23 added; P16 updated).
- Still unavailable: listening, independent QA or second coder, 2 Shorts and 1 long video without media, DEEP_VISUAL (0). Self-review.

## Checkpoint 6 (2026-11-23): measured ledgers and file index

- `00_START_HERE.md` lists every file with its absolute path. `ledgers_measured/` holds machine-measured shot and event ledgers for the 20 long videos and 24 Shorts that had none (44 videos, 719 shots, 2,160 events; 3 videos without media), plus keyframes, `README_LEDGERS.md` and a held-out validation (events P 0.95 R 0.96; shot boundaries P 0.70 R 0.86). Not viewed or interpreted. Register 25 rows.

## Checkpoint 7 (2026-11-23): first review of the measured ledgers

- 24 measured shots (12 long, 12 Shorts) viewed as before, keyframe, after stills and coded (`review_sample/`). 22 of 24 shot boundaries are true cuts; boundary_strength did not separate the 2 false ones. Interpretation columns filled for these 24 only; 695 shots and 2,160 events stay NOT_VIEWED. Self-review, one coder. Register 26 rows (P26).

## Checkpoint 8 (2026-11-23): review sample extended to 60 shots

- 36 more measured shots viewed and coded (`review_sample/`, 60 rows over 42 videos). 50 of 60 boundaries true cuts, 8 progressive, 2 borderline; boundary_strength not a usable filter. New finding: the red book-promo end card closes 20 of 20 measured long videos (none of the 24 Shorts), which qualifies the playbook's no-CTA statement to wording only (`05_` section E). Register 27 rows (P26 updated, P27 added). Self-review, one coder; 659 shots and 2,160 events still NOT_VIEWED.

## Checkpoint 9 (2026-11-23): end cards for all long videos and a CT_SCAN pilot

- End card: the other 24 long videos also close on the red book-promo card, so 44 of 44 long videos do and 0 of 24 Shorts; about 10 s long (P27 updated).
- CT_SCAN pilot on `9VG0yqq_PHM` (`ct_scan_pilot_9VG0yqq_PHM/`): all 3,893 frames measured, 104 change spans viewed in native-frame windows (10.5% of frames viewed), ledgers, coverage and gates. 92.7% of frames are holds; changes are one-frame pops, typed text at about a character a frame, and a few gradual fades the frozen detector misses. Register 30 rows (P28 to P30). One coder; not every frame viewed.

## Checkpoint 10 (2026-11-23): one 30 s span viewed frame by frame

- Frames 960 to 1679 of `9VG0yqq_PHM` (40 to 70 s): all 720 frames viewed (15 sheets) and checked at full resolution (`ct_scan_pilot_9VG0yqq_PHM/span_960_1679/`). No visible change missed by the ledger; 54 residual HOLD frames are codec settling. Whole-video viewed share now 27.2% (event windows plus this span; `coverage.json`). Register 31 rows (P31). One coder.

## Checkpoint 11 (2026-11-23): whole pilot video viewed frame by frame

- Frames 0 to 959 and 1680 to 3892 of `9VG0yqq_PHM` viewed (67 sheets) on top of the middle span: all 3,893 frames viewed, plus full-resolution differencing. Found five tiny eye-pair pop-ons the detector and the sheets missed (frames 3236 to 3252, one every 4 frames), corrected two toast events, and showed that apparent motion in the sheets was still at full resolution. Ledger now 109 rows (X001 to X005 added). Register 34 rows (P32 to P34). One coder; no audio.

## Checkpoint 12 (2026-11-23): CT_SCAN machine stage on all 88 videos

- `scripts/ct_batch.py` run on 88 videos (44 long, 44 Shorts; 313,650 frames): per-frame full-resolution differencing, strong and faint layers, state intervals, HOLD residual runs (`ct_scan_batch/`, P35 and P36). Nothing viewed; strong-event counts match the measured ledgers on 44 of 44; the pilot reproduces. 1,585 long and 204 Short faint-layer events are missing from the ledgers.

## Checkpoint 13 (2026-11-23): flagged runs and outlier videos viewed (the unviewed-scattered statements below are superseded by Checkpoint 15)

- 153 compact and mid residual runs and 36 random scattered runs viewed (`ct_scan_batch/run_review/`, P37 to P39). 58 runs in 33 videos are real small additions no ledger lists; 0 of 36 control runs were. 1,443 scattered runs not viewed. The two low-HOLD videos are genuine continuous motion. One coder, stills only.

## Checkpoint 14 (2026-11-23): 58 real small additions joined to the ledgers

- `scripts/ledger_add_small.py` writes `small_additions.csv` per video (58 rows, 33 videos) plus `ledgers_measured/SMALL_ADDITIONS_ALL.csv` (P40). No existing ledger file edited; the 15 videos with a ledger folder get shot_id, the 18 without are in `ledgers_small_additions_only/`. Descriptions then filled for all 58 from the viewed cells (`scripts/small_descriptions.py`; 9 marked read uncertain; mostly typed characters such as 2, Y, S, =, 0, plus red strikes, dashes and a few small figures). Event counts and events per minute are unchanged.

## Checkpoint 15 (2026-11-23): all remaining scattered runs viewed

- 1,443 scattered runs viewed by 8 same-model reader agents, with every non-NOISE cell re-viewed by the main session (`ct_scan_batch/run_review/scat_REVIEWED_RUNS.csv`, P41, P42). 16 real small additions, 11 uncertain, 3 larger motion, 1,413 noise; a 96-cell spot-check of the NOISE codes found 0 disagreements. Ledger additions now 74 rows in 35 videos (P40 updated); P38 marked SUPERSEDED. Not covered: changes under 15 px, 1,585 + 204 faint-layer events, 11 uncertain runs; no independent coder.

## Checkpoint 16 (2026-11-23): continuation from checkpoint 15, stale records reconciled and Phases 3 to 12 extended
- Reconciled: live recount 92 (46 long + 46 Shorts); ASR validated for 88 videos (X97DDWvxaqQ and alBQCm0QpJg provisional, duration and title consistent); inventory v2, corpus report, availability, claim matrix, register rewritten with v1 kept; pacing corrected by definition (the "same quantity" wording withdrawn); DEEP_VISUAL = 1 (visual-only); Phase 3 register attributes added (rule-derived).
- New work: Phase 5 verification (41 of 43 openings and no-CTA, era split of length); Phase 6.2 style measurements on 125 frames; review batch 3 (108 shots viewed over all 44 ledger videos; 77% true cuts); 10 physics claims recomputed (v2: lightning reopened as OPEN, 0 discrepant); machine AV alignment (56% vs 33 to 37% chance) and a 4,439-row listening pack; asset recipes and 10 scene breakdowns; hypotheses H1 to H9; knowledge-base draft (14 documents + 23-rule ledger); workflow v2; final report v2; register P43 to P57.
- Not done: listening (blocked), independent review (unavailable), interpretation of 611 shots and 2,160 events, the ten directive physics episodes in depth, book-art comparison, article correspondence, Machine A. Repo untouched (HEAD 9eb4f5ab, clean).

## Checkpoint 17 (2026-11-23): third pass after the independent-audit request
- Independent audit file `WHAT_IF_INDEPENDENT_AUDIT.md` **not found** on this machine; only its lightning point (as quoted in the request) was addressed.
- SC03 lightning reopened as OPEN (`07_SC03_LIGHTNING_REWORK.md`); SC05 relation-dependent; 10-claim set now 4 / 3 / 1 / 1 / 1 with 0 discrepant (`07_SCIENCE_CLAIM_CHECKS.md` v2).
- Ten directive episodes studied (sampled and viewed, not deep): `07e_TEN_EPISODE_PHYSICS_STUDIES.md`, 51 rows, 1 discrepant as stated (E09g).
- 23 rules audited (`11_RULE_AUDIT_2026-11-23.csv`); KB wording revised; ledger has audit columns.
- Shot review batch 4: 156 of 719 viewed (`06_LEDGER_REVIEW_METHOD_AND_COVERAGE.md` addendum). Listening still blocked; priority list `09_LISTENING_PRIORITY_ITEMS.csv`.
- New scripts: `phase7_sc03_rework.py`, `phase7e_episode_checks.py`, `phase7e_sheets.py`, `phase11_rule_recompute.py`, `phase11_rule_audit_table.py`, `review_sample4.py`, `review_sample_code4.py`. Repo untouched.


## Checkpoint 18 (2026-11-23, reconciliation pass)
Reconciled Codex F01 to F14 and the supplied external audit (`14_RECONCILIATION_...md`). Changed: operative text of 22 of 23 rules; H2, H6, H7, H9 wording; SC02 to QUALIFIED; E09g benchmark; Wilson intervals withdrawn; playbook B2; KB documents; evidence register P68 to P76; final report v4. Added: sample-design analysis, 16 motion sequences (15 confirmed), 88 hash recomputation (88 match), preregistered topic-family check (20 of 20 pass), coverage plan, 9 listening items. Repo: HEAD `a0c0391c`, no git writes. Not done: listening, independent validation, 563 shots / 2,160 events, six open owner or evidence items listed in the final report section I.
