# Review of flagged residual runs and the two outlier videos (viewed, self-review)

Status: OBSERVED (viewed by one coder, no second reviewer, no audio). Table: `run_review/REVIEWED_RUNS.csv`; sheets `run_review/view_01-13.jpg`, `control_01-03.jpg`, `outlier_*.jpg`. Scripts: `scripts/ct_runs_triage.py`, `ct_runs_sheets.py`, `ct_runs_code.py`.

## What was viewed
The 1,632 candidate runs (peak 150+ px above 8 grey levels in HOLD frames) were first sorted by shape, then viewed as cells of [frame before | peak frame | difference amplified x8], cropped to the run:
- COMPACT (bbox under 2% of the frame): 54 runs, all viewed.
- MID (2% to 15%): 99 runs, all viewed.
- SCATTERED (15% or more, 1,479 runs): 36 random runs viewed as a control; the other 1,443 were NOT viewed at this stage (SUPERSEDED: all viewed later, see the last section).
The shape rule is a heuristic from the pilot, tested only by the control below.

## Result
| shape | viewed | small drawn object | uncertain | noise |
|---|---|---|---|---|
| COMPACT | 54 | 46 | 1 | 7 |
| MID | 99 | 12 | 3 | 84 |
| SCATTERED (random control) | 36 | 0 | 0 | 36 |

- 58 runs in 33 videos (36 long, 22 Shorts) are real small additions that no ledger lists: a character typed ("2", "=", "S", "Y", "0."), a dash or red strike-through drawn, a "+" or a small figure appearing, the eye pairs already known in the pilot (3 of the 5 appear here). Each is at most a few hundred pixels, so neither the 256x144 detector nor its faint layer saw it.
- The rest of the viewed compact and mid runs show speckle along line edges or a faint outline of a texture (for example the shimmering moon), with no compact new object. Noise is a judgement from the amplified difference, not a measurement.
- Control: 0 of 36 scattered runs showed a new object. With 36 clean samples the real rate in the unviewed 1,443 could still be up to about 8% (rule of three, 95%); it was not measured. (SUPERSEDED by the last section.)
- The 4 uncertain runs are tiny blobs I could not read at this size.

## Outlier videos (low HOLD share)
- `oTzW-mTQd5w` (long, 31.1% HOLD): a falling and rising figure with moving cloud and streak backgrounds; one 535-frame event (frames 1240 to 1774, median 11,870 px changed per frame) is continuous movement, not noise.
- `ERieN5pee7A` (Short, 54.7% HOLD): a rotating globe with a sweeping day-night edge and gradient fades; one 394-frame event (frames 924 to 1317, median 8,187 px) is continuous animation.
- Both are genuine motion. The ledgers fold such a stretch into one event, so events per minute undercounts continuous animation. Four frames of each were viewed, not every frame.

## Limits
- One coder; stills and a difference image, not playback.
- (At this stage) 1,443 scattered runs unviewed, since viewed; changes under 15 px not examined; the viewing does not cover the 1,585 + 204 faint-layer events.
- The tier for these 87 videos stays MEASURED with a small OBSERVED sample; DEEP_VISUAL stays 0.

## Remaining scattered runs viewed (added 2026-11-23, Checkpoint 15)

- All 1,443 remaining SCATTERED runs viewed: 121 sheets (`scat_01..121.jpg`, 12 cells each) split across 8 reader agents. The readers are the same model as the main session, not an independent coder. Each coded every cell as REAL_SMALL_OBJECT, UNCERTAIN, OTHER_CHANGE or NOISE; the main session then re-viewed all 14 sheets that hold a non-NOISE cell.
- Result after re-check: 16 real small additions, 11 uncertain, 3 larger motion (cells 594 to 596: a plane, a crowd, red map routes), 1,413 noise. Three reader REAL claims (cells 734, 1080, 1341) were too small to read on the sheet and were downgraded to UNCERTAIN.
- With the 36 control runs, 16 of 1,479 scattered runs (about 1%) are real small additions, against 58 of 153 compact and mid runs. All 16 are in long videos (2LSyizrk8-0, 3EI08o-IGYk, IdlQsjq5vKo, WH4g1ptJ-70, lLlwvmu1ZeA): typed text (Ra, the letter I completing DELHI, KARACHI, MUMBAI), red underline strokes, a graph stroke, mole-number handwriting.
- Spot-check of the NOISE codes: 8 random unflagged sheets (96 cells) re-viewed, 0 disagreements (upper bound about 3% at 95%, clustered sample).
- Limits: same-model readers; stills plus an x8 difference image; changes under 15 px and the 1,585 + 204 faint-layer events not viewed; 11 uncertain runs unresolved; shape rule is a heuristic.
- Files: `run_review/scat_REVIEWED_RUNS.csv` (every cell, reader code, final code), `scat_coded_*.csv` (reader output), `scat_cells.csv`, `scripts/ct_scat_merge.py`. The 16 real runs are in `ledgers_measured/SMALL_ADDITIONS_ALL.csv` (now 74 rows, 35 videos; register P40 to P42).
