# Barely Evolved — three-video audit v2 (non-audio completion, 2026-11-05)

- **Session:** 1e8761b1.
- **Kit:** visual-ct-scan v1.0.
- **Branch:** research/barely-evolved-visual-forensics.
- **Supersedes:** `FINAL_THREE_VIDEO_AUDIT.md` (kept unchanged) for the non-audio rows.
- **Scope:** uPQcyookL0Y (v1), mNLNb-Z4T0M (v2), GNaBxt_zIRA (v3) only.

## Decision

- **Non-audio verdict:** `NON_AUDIO_WORK_REMAINS`. Two items remain, and neither can be closed inside this session:
  - **R20 portability: `STORAGE_DESTINATION_REQUIRED`.** The source MP4s and RT renders exist only on Machine A. No approved durable destination is documented, and the only mounted volume is the boot disk. Raw video must not go through GitHub.
  - **R13 reviewer independence: PARTIAL.** Every reviewer is a fresh Claude context from the same vendor. Deterministic measurements provide partial independence. A reviewer from a different vendor, or a human, is outside this environment.
- **Audio:** R08 (ASR-based) is PARTIAL, and R09 listening and R21 AV sign-off stay BLOCKED. These are excluded by instruction and were not attempted.
- **R22 `CT_SCAN_COMPLETE`:** FAIL. It is not awarded, and status stays `VISUAL_ANALYSIS_PARTIAL`.

## Matrix

The full matrix is `FINAL_AUDIT_MATRIX_v2.csv`. Each requirement has the same status in all three videos.

| Status | Rows |
|---|---|
| PASS | R01–R07, R10–R12, R14–R19 |
| PARTIAL | R08, R13, R20 |
| BLOCKED | R09, R21 |
| FAIL | R22 |

Per-video gates are in `kit_outputs/<vid>_<sha8>/quality_gate_NAC.json`. The earlier `quality_gate_FINAL.json` files are kept unchanged.

## What was done for the non-audio rows

**R05/R07 dense review.**
- **Measurement.** Every decoded frame of the 850 previously uninspected intervals (47,655 frames in total) was given a frame-to-previous similarity fit and a residual. These are MEASURED.
- **Visual naming.** Every interval was named visually by one bounded sonnet reviewer at a time, using six tiles per interval (pre, start, 1/3, 2/3, end, post). Intervals the tiles left ambiguous were re-checked on native-resolution crops.

| Video | Intervals | Named from tiles | Checked on native crops | Crop verdicts | Intervals where every frame was viewed |
|---|---|---|---|---|---|
| v1 | 282 | 183 | 99 | 54 confirmed, 45 corrected | 70 |
| v2 | 288 | 188 | 100 | 55 confirmed, 45 corrected | 68 |
| v3 | 280 | 152 | 127 + 1 resolved by orchestrator (U0042, codec flicker) | 101 confirmed, 26 corrected | 48 |

- **Ledgers:** `nonaudio_completion/dense_review/DENSE_REVIEW_LEDGER_<vid>.csv`. Each row records its interior viewing density ("n/N interior frames viewed").
- **Camera claims, cross-checked against the measured trajectory:** v1 16/18 supported, v2 12/20, v3 7/8. Unsupported claims are flagged UNCERTAIN.
- **What PASS means here.** Every frame was measured, and every change interval was visually named from sampled tiles or native crops. Not every frame was viewed, and that limitation is recorded in the ledgers and not hidden.

**R04 (v1).** Evidence is in `nonaudio_completion/v1_closure/`.
- **W085b:** fades in over f13993–13999, swaps one word at f14029, then exits hard at f14059. The earlier "fade to black" claim is NOT_SUPPORTED.
- **f2835 and f5429:** recorded as single-frame punch-in camera events. The partition stays at 89 states.

**R10 asset crosswalk.**
- `nonaudio_completion/crosswalk/ASSET_CROSSWALK_v1.csv` holds 733 rows covering 86 canonical assets.
- Verdicts: 473 SAME, 209 VARIANT, 51 UNCERTAIN. Similar-looking assets were not merged.
- The orchestrator checked BE-CHR-003 at native resolution in all three videos. It was re-viewed in N14 (`ORCHESTRATOR_REVERIFY_N14.csv`).

**Camera ease** (`nonaudio_completion/camera_ease/`).
- RT-V2-01 keeps its FAIL. The diagnosis: the source move at S080 is a horizontal pan that was mislabelled as a push, the texture-dependent criterion was unsuitable, and so was the flat test scene.
- RT-V2-02 was run on a pre-registered criterion and PASSed. The RT-V2-01 render, used as a negative control, fails 6/7 of its criteria.

**R11/R15 style and full-scene reconstruction** (`RECONSTRUCTION_TESTS_v2.csv`).
- **Method.** Fresh sonnet workers saw only `SPEC_GIVEN_TO_WORKER.json`. Each criterion was pre-registered and calibrated on a source extract before any render. A failed test was never re-scored: the spec was corrected and a new render made.
- **v1 (W021):** RT-V1-S01 PASS.
- **v1 punch-in:** RT-V1-P01 PASS.
  - Criterion v1 failed on the source itself and is kept. v2 was registered before the render.
  - Measured: the image is scaled 2.139× around (627, 818).
  - The visual check (C5) was re-viewed in N14.
- **v2 (S067):** S01, S02 and S03 failed and are kept. S04 PASSed on C3 v2, which was registered before that render.
- **v3 (S057):** S01 and S02 failed and are kept; both failures were my spec errors (a wrong pan; a missing screen-anchored teacher layer). S03 PASSed.
- **Out of scope for all tests:** fonts, software, easing source and sound remain UNKNOWN.

**R16.** `../CHANNEL_SYNTHESIS_v1_2.md` (production manual v1.2) and this report.

**R18/R19.** These were re-run for this close-out. See `FINAL_VALIDATION_v2.json`.

## Corrections kept, not overwritten

All raw reviewer outputs, earlier failed evaluations, criteria that failed on their source, `FINAL_AUDIT_MATRIX.csv`, `FINAL_THREE_VIDEO_AUDIT.md` and `quality_gate_FINAL.json` are unchanged.

Reviewer deviations are recorded in `nonaudio_completion/dense_review/REVIEWER_DEVIATIONS.md`.

## Remaining

1. **R20.** The owner names an approved durable storage destination. The three source MP4s and twelve RT renders, with SHA-256 hashes listed in `PORTABILITY_INVENTORY.json`, are then copied there and their hashes verified.
2. **R13.** If wanted, an independent reviewer outside Claude re-checks a sample of the dense ledger.
3. **Excluded audio work:** R08, R09 and R21 need actual listening.
