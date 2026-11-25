# CT_SCAN machine stage on all 88 videos (NOT viewed)

Status: MEASURED, NOT_VIEWED. One coder, no audio. Script: `scripts/ct_batch.py` (+ `ct_batch_aggregate.py`). Per video folder: `source_manifest.json`, `per_frame_table.csv`, `state_intervals.csv`, `hold_residual_runs.csv`, `summary.json`. Table of all videos: `BATCH_SUMMARY.csv`.

## What was done
- 88 videos (44 long, 44 Shorts), 313,650 frames, every frame differenced against the previous one at full resolution (>2, >8, >24 grey levels) and on the 256x144 layers (strong at the frozen threshold, faint layer from the pilot).
- All 88 have constant frame rate (per-frame PTS from ffprobe). No failures.
- Checks: strong-event counts equal the measured ledgers on all 44 videos that have one; the pilot `9VG0yqq_PHM` reproduces its earlier numbers (64 strong events, 92.7% HOLD, 48.8% zero-change transitions, 19.6% HOLD frames with 15+ px).

## Numbers (median, min to max across videos)
| | LONG (44) | SHORT (44) |
|---|---|---|
| HOLD share at ledger threshold | 93.3% (31.1 to 97.1) | 94.1% (54.7 to 98.7) |
| transitions with no change above 2 grey levels | 52.1% (20.7 to 63.8) | 66.1% (25.0 to 86.0) |
| HOLD frames with 15+ px above 8 grey levels | 9.7% (4.5 to 22.3) | 1.8% (0.4 to 11.3) |
| faint-layer events per video | 35.5 (15 to 76) | 3 (0 to 23) |
| strong events per video | 76 (38 to 125) | 29.5 (8 to 72) |

Faint-layer events total 1,585 (long) and 204 (Shorts): changes the frozen-threshold ledgers do not list. In the pilot 13 of 77 visible changes were of this kind; the share elsewhere was not checked by eye.
Outlier: `oTzW-mTQd5w` (long, 31.1% HOLD) and `ERieN5pee7A` (Short, 54.7%) hold far less than the rest; both viewed later and are genuine continuous motion (see `RUN_REVIEW_REPORT.md`).

## Limits
- No frame of these 87 new videos was viewed. Residual runs are not classified: `candidate_for_viewing=1` marks runs with 150+ px above 8 grey levels (1,394 long, 238 Shorts), a heuristic from the pilot (noise runs up to 121 px, drawn eye pairs about 200 px), not validated.
- Changes under 15 px or 8 grey levels not examined. The pilot hold shares must not be read as channel values from one video; these tables are the wider measurement.
- Tier for these videos stays at most MEASURED; DEEP_VISUAL remains 0 channel-wide.
