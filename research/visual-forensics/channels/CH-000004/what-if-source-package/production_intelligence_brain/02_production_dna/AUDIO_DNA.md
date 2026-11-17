# AUDIO DNA

## Overview
Production patterns in narration timing, word delivery, and audio event distribution.

## Word-Level Timing
Phonetic units shape perceived pacing and comprehension speed.

- **Average word duration:** 223.5ms (median: 200.0ms)
- **Range:** 10.0–1400.0ms
- **Variation:** σ = 116.9ms (natural speech variation)
- **Total words analyzed:** 7864

## Sentence-Level Delivery
Narration pacing at the clause level drives viewer comprehension.

Recomputed from the rebuilt `01_master_data/MASTER_SENTENCES.csv` (604 meaningful
sentences; the prior figures here — 141 sentences, 55.8 words/sentence, a
negative-duration row — were wrong; not a real property of the corpus, and are
replaced below with the actual computed values).

- **Average sentence duration:** 3042.8ms (median: 2790.0ms)
- **Range:** 140.0–11620.0ms
- **Average words per sentence:** 13.0
- **Total sentences:** 604

## Vocabulary Patterns
Most common words across all videos (top 20):

| Word | Frequency |
|------|-----------|
| the | 539 |
| a | 271 |
| of | 240 |
| to | 194 |
| would | 173 |
| and | 170 |
| in | 104 |
| is | 95 |
| it | 77 |
| be | 74 |
| you | 73 |
| that | 58 |
| but | 56 |
| for | 49 |
| if | 49 |
| as | 49 |
| on | 46 |
| by | 44 |
| this | 40 |
| from | 40 |

- **Total unique words:** 1859 (case-folded, punctuation-stripped `NORMALIZED_WORD`; recomputed — top-20 frequencies above match the prior figures exactly, confirming this section was already accurate, unlike the sentence-level section above)
- **Average word length:** 4.54 characters

## Audio Events
Non-speech audio regions detected: silence, pauses, music, SFX.

- **Total audio events:** 29
- **Event types:** {'NARRATION': 14, 'SILENCE': 8, 'PAUSE': 7}

| Event Type | Count | Mean Duration (s) | Total Duration (s) |
|-----------|-------|-------------------|--------------------|
| NARRATION | 14 | 146.56 | 2051.86 |
| SILENCE | 8 | 1.41 | 11.29 |
| PAUSE | 7 | 0.73 | 5.1 |

## What is NOT supported by current data
- The schema has no per-word or per-sentence "complexity" measure, so no claim is made here that delivery speed correlates with concept difficulty, or that pauses are placed for cognitive-load management — those would be speculation, not measurement.

