# MOTION DNA

Regenerated from the repaired `01_master_data/MASTER_MOTIONS.csv` (438 motions,
rebuilt from the 14 per-video `02_analysis/MOTION_EVENTS.csv` forensic files —
the prior `MASTER_MOTIONS.csv` had apparently been built from the corrupted
per-video `AUDIO_VISUAL_SYNC.csv` MOTION_ID column instead, producing 57 rows
with compound/prose/asset-ID values and losing all real timing for the one
30fps video in the corpus). This document supersedes the prior version, which
stated "Total motion events: 0". Every number below is computed directly.

## Motion Density

- **Total motion events:** 438 across 14 videos
- **Average per video:** 31.3 (min 14 in `earthquake-magnitude-shorts-wBLVmEZV2Oc`, max 66 in `Could you power your computer by typing?`)

## Duration Distribution (measured, DURATION_SEC = END_SEC − START_SEC)

| Bucket | Count |
|---|---|
| Instant / < 0.5s | 144 |
| 0.5–2s | 105 |
| 2–5s | 108 |
| > 5s | 81 |

Instant transitions (36 rows with END_SEC == START_SEC, i.e. a hard cut with no tracked duration) are included in the "< 0.5s" bucket. There is no single dominant duration band — the corpus mixes fast reveals, medium-length reveals, and multi-second sustained/looping motions in roughly comparable proportions, not the "sparse but strategic" single mode the prior (fabricated) doc claimed.

## What is NOT supported by current data

- `MASTER_MOTIONS.csv` has no field distinguishing "reveal" vs "transition" vs "emphasis" vs "explanation" as motion purposes — the prior doc's "Motion Purpose Hierarchy" ranking was not derived from any column in this schema and is omitted here.
- No corpus-wide claim about narration-boundary alignment for motion start/end is made in this document; that comparison now lives in `AUDIO_VISUAL_SYNC_DNA.md`, computed from the actual `MOTION_START`/`MOTION_END` sync events (438 + 402 rows respectively).
