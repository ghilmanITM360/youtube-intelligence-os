# AUDIO-VISUAL SYNCHRONIZATION DNA

Regenerated after enriching `01_master_data/MASTER_AUDIO_VISUAL_SYNC.csv` with
real `MOTION_START`/`MOTION_END` events (per task step 20 — this doc was
intentionally left stale until that enrichment existed). The table grew from
581 rows (1 event/state, all `STATE_CHANGE`) to 1421 rows across three event
types, each computed from measured `MASTER_MOTIONS.csv` / `MASTER_WORDS.csv`
timestamps using a 20ms edge window to classify `ON_WORD_START`/`ON_WORD_END`
vs `DURING_WORD` (reverse-engineered from, and verified against, the 388
originally-classified rows) and real measured `MASTER_AUDIO_EVENTS.csv`
regions for `DURING_PAUSE`/`DURING_SILENCE`.

## Visual Event Types

| Event Type | Count |
|---|---|
| STATE_CHANGE | 581 |
| MOTION_START | 438 |
| MOTION_END | 402 |

(438 motions total; 402 of them have a distinct, non-instantaneous `MOTION_END` — the remaining 36 are instant transitions where END_SEC == START_SEC, so no separate end event was created for them; see `MOTION_DNA.md`.)

## Sync Relationship Distribution, by event type

**STATE_CHANGE ↔ speech** (n=581): DURING_WORD 293, NO_SPEECH 193, ON_WORD_START 62, BETWEEN_WORDS 14, ON_WORD_END 19. Mean offset 75.5ms, median 37.0ms. Only 66.8% of state changes land during/near an active word — a third occur with no covering word at that instant (`NO_SPEECH`). (A temporal-integrity pass corrected 33 `STATE_CHANGE` rows across 2 videos whose `VISUAL_EVENT_SEC` had been mis-derived from corrupted state timing — see `CONTINUATION_HANDOFF.md`; the figures above reflect the corrected data.)

**MOTION_START ↔ speech** (n=438): DURING_WORD 218, BETWEEN_WORDS 166, ON_WORD_START 36, ON_WORD_END 14, AFTER_WORD 2, DURING_SILENCE 2. Mean offset −14.6ms, median 33.0ms. 99.5% occur during or adjacent to speech — motions in this corpus almost never start during real silence.

**MOTION_END ↔ speech** (n=402): DURING_WORD 210, BETWEEN_WORDS 126, ON_WORD_START 28, ON_WORD_END 27, AFTER_WORD 6, DURING_SILENCE 4, DURING_PAUSE 1. Mean offset 14.8ms, median 56.0ms. 98.8% near-speech.

## Timing Offsets

Offset = (visual event time − covering/nearest word's START_SEC) × 1000, in ms. Positive = visual follows the word's start; negative = visual precedes it (only possible for `BETWEEN_WORDS`/`AFTER_WORD` cases anchored to the next word).

- STATE_CHANGE: mean 75.5ms, median 37.0ms
- MOTION_START: mean −14.6ms, median 33.0ms
- MOTION_END: mean 14.8ms, median 56.0ms

## Audio Event Linkage

7 of 1421 sync rows (0.5%) reference a `MASTER_AUDIO_EVENTS` row (`DURING_PAUSE`/`DURING_SILENCE` cases where a visual event's timestamp falls inside a measured PAUSE or SILENCE region). The remaining rows have no audio-event overlap because they fall inside the single long `NARRATION` region per video, which is not itself referenced per-row (only pauses/silences are — a `NARRATION` link would be true for nearly every row and would carry no discriminating information).

## What is NOT supported by current data

- SHOT_CUT ↔ sentence-boundary, TEXT_REVEAL/GRAPHIC_REVEAL ↔ keyword, and PAUSE ↔ visual-hold comparisons are not included here: `MASTER_AUDIO_VISUAL_SYNC.csv` has no `SHOT_CUT`, `TEXT_REVEAL`, or `GRAPHIC_REVEAL` event rows in the current schema (only `STATE_CHANGE`/`MOTION_START`/`MOTION_END` — see `03_reconstruction_system/DECISION_RULES.md` for why those categories were not fabricated).
