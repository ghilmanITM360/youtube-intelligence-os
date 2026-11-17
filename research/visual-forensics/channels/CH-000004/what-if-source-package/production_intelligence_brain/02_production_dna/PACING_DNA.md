# PACING DNA

## Overview
Temporal grammar governing how information is delivered and consumed.

## Sentence Rhythm
Sentence duration patterns across the corpus, recomputed from the rebuilt
`01_master_data/MASTER_SENTENCES.csv` (604 sentences; the prior figures here —
7818.2ms mean, 55.8 words/sentence, a negative-duration row — were wrong).

- **Mean sentence:** 3042.8ms
- **Median sentence:** 2790.0ms
- **Range:** 140.0–11620.0ms
- **Words per sentence:** avg 13.0

## Word Delivery Speed Distribution (measured, from `MASTER_WORDS.csv` durations)

| Bucket | Count | Share |
|---|---|---|
| Fast (< 150ms/word) | 2283 | 29.0% |
| Medium (150–250ms/word) | 2880 | 36.6% |
| Slow (> 250ms/word) | 2701 | 34.3% |

The three bands are close to evenly split — there is no dominant delivery speed. No claim is made linking a given band to concept complexity: the schema has no complexity/topic field to correlate against.

## Silence and Pause Regions

- **SILENCE events:** 8 (mean 1.41s, total 11.29s)
- **PAUSE events:** 7 (mean 0.73s, total 5.10s)
- **Combined:** 15 non-speech regions across 14 videos (~1.1 per video)

## What is NOT supported by current data

- No corpus data ties silence/pause placement to "high-complexity sentences," and no data ties shot cuts to "complex explanation" — these were unsupported claims in the prior version and are omitted. The measured shot-cut ↔ speech relationship that *is* supported is in `AUDIO_VISUAL_SYNC_DNA.md` (66.8% of STATE_CHANGE events occur during/near an active word).

