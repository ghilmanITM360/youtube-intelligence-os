# Validation Report

Generated from an actual run of `validator/validate_brain.py` against the
current on-disk state (2026-09-17), after a temporal + referential integrity
pass that fixed defects an independent audit found beyond the previous
validator's scope (zeroed shot/state timestamps, stale shot aggregate
counts, motion foreign-key errors, and a compound-value sync field — see
`CONTINUATION_HANDOFF.md` for the full repair log). Re-run the validator
yourself to reproduce every number below.

```
======================================================================
PRODUCTION INTELLIGENCE BRAIN — STRICT VALIDATOR
======================================================================

--- 26. SENTENCE VALIDATION ---
TOTAL_SENTENCE_ROWS = 604
EMPTY_MEANINGFUL_SENTENCES = 0
MISSING_FIRST_WORD_ID = 0
MISSING_LAST_WORD_ID = 0
INVALID_FIRST_WORD_ID = 0
INVALID_LAST_WORD_ID = 0
WORD_COUNT_MISMATCHES = 0
NEGATIVE_DURATION_ROWS = 0
DUPLICATE_WORD_IDS = 0

--- 27. MASTER FOREIGN KEY VALIDATION ---
MASTER_STATES orphan SHOT_ID refs = 0
MASTER_STATES orphan ASSET_IDS refs = 0
MASTER_STATES orphan MOTION_IDS refs = 0
MASTER_SHOTS orphan ASSET_IDS refs = 0

--- 28. A/V SYNC EVENT VALIDATION ---
TOTAL_SYNC_ROWS = 1421
INVALID_VISUAL_EVENT_TYPE = 0
INVALID_SYNC_RELATION = 0
REQUIRED_ORPHAN_MOTION_REFS = 0
AV_ORPHAN_SHOT_REFS = 0
AV_ORPHAN_TARGET_SHOT_REFS = 0
AV_ORPHAN_SOURCE_STATE_REFS = 0
AV_ORPHAN_TARGET_STATE_REFS = 0
ORPHAN_SENTENCE_REFS = 0
ORPHAN_WORD_REFS = 0
ORPHAN_AUDIO_EVENT_REFS = 0
DUPLICATE_COMPOSITE_SYNC_IDS = 0

--- 29. MOTION START/END LINKAGE ---
TOTAL_MOTIONS = 438
MOTION_START_LINKED = 438
MOTION_START_UNRESOLVED = 0
MOTION_END_LINKED = 402
MOTION_END_UNRESOLVED_UNDOCUMENTED = 0
(36 motions are instantaneous, END_SEC == START_SEC — a documented exception,
not an unresolved gap)

--- 31. MASTER_MOTIONS DIRECT VALIDATION ---
MOTION_ORPHAN_SHOT_REFS = 0
MOTION_ORPHAN_TARGET_SHOT_REFS = 0
MOTION_ORPHAN_SOURCE_STATE_REFS = 0
MOTION_ORPHAN_TARGET_STATE_REFS = 0
MOTION_DURATION_MISMATCHES = 0
MOTION_DUPLICATE_IDS = 0

--- 32. MASTER_SHOTS / MASTER_STATES DIRECT VALIDATION ---
STATE_DURATION_MISMATCHES = 0
STATE_NON_MONOTONIC_ERRORS = 0
STATE_ORPHAN_SHOT_REFS = 0
SHOT_DURATION_MISMATCHES = 0
SHOT_STATE_COUNT_MISMATCHES = 0
SHOT_MOTION_COUNT_MISMATCHES = 0
SHOT_FIRST_STATE_ERRORS = 0
SHOT_LAST_STATE_ERRORS = 0

--- 33. RAW CSV WIDTH VALIDATION ---
MALFORMED_CSV_ROWS = 0

--- HARD TIMESTAMP ERRORS (rollup across motions/states/shots) ---
HARD_TIMESTAMP_ERRORS = 0

--- 30. CANONICAL ARTIFACT PRESENCE ---
MISSING_CANONICAL_FILES = 0
TRIVIAL_(NON_SUBSTANTIVE)_FILES = 0

--- ROW COUNT SUMMARY ---
sentences (meaningful): 604
words: 7864
motions: 438
states: 581
shots: 200
assets: 448
audio_events: 29
av_sync total: 1421 (581 STATE_CHANGE, 438 MOTION_START, 402 MOTION_END)

======================================================================
RESULT: PASS (all gates report zero failures)
======================================================================
```

## What changed since the previous validator PASS

An independent audit found that the prior validator's foreign-key/reference
checks all passed while several other defects went undetected because
nothing checked them:

- **74/200 `MASTER_SHOTS` and 257/581 `MASTER_STATES` rows** had
  `START_SEC=END_SEC=0` despite a positive `DURATION_SEC`, across 7 videos
  whose per-video `TIMELINE.csv` encodes shot/state boundaries as frame
  indices (or, for `what_would_a_magnitude_15_earthquake_be`, had even
  `DURATION_SEC` corrupted to a constant `24.0`, the literal FPS value).
  Recomputed from each video's own `TIMELINE.csv` + documented FPS, and
  cross-checked against the independent `STATE_CHANGE.VISUAL_EVENT_SEC`
  values already in `MASTER_AUDIO_VISUAL_SYNC.csv`. An 8th video,
  `worlds-largest-cities-what-if`, had **all 11 states and both shots**
  zeroed (missed by the original audit's `DURATION_SEC > 0` filter, since
  its `DURATION_SEC` was also 0) and was fixed the same way.
- **114 `STATE_COUNT` and 173 `MOTION_COUNT` mismatches** across all 200
  shots corpus-wide (not limited to the 7/8 timing-broken videos) — these
  aggregate fields had never been kept in sync with real state/motion
  membership. All 200 shots' `START_SEC`/`END_SEC`/`DURATION_SEC`/
  `FIRST_STATE_ID`/`LAST_STATE_ID`/`STATE_COUNT`/`MOTION_COUNT` were
  recomputed directly from the corrected `MASTER_STATES`/`MASTER_MOTIONS`.
- **33 `STATE_CHANGE` sync rows** (23 in `earthquake-magnitude-shorts-wBLVmEZV2Oc`,
  10 in `worlds-largest-cities-what-if`) had a stale `VISUAL_EVENT_SEC` that
  no longer matched the corrected state's real onset time — in the first
  video's case, the original value had been divided by 24 a second time,
  silently misresolving every `SENTENCE_ID`/`WORD_ID`/`OFFSET_MS`/
  `SYNC_RELATION` for those rows. Recomputed and re-resolved with the same
  word/audio-event alignment algorithm used to build `MOTION_START`/
  `MOTION_END` events.
- **1 pseudo `SHOT_ID`** (`worlds-largest-cities-what-if` motion `A02`,
  `SHOT_ID="S01→S02"`) and **matching `MASTER_AUDIO_VISUAL_SYNC` rows** —
  resolved by adding a `TARGET_SHOT_ID` column to both tables rather than
  inventing a new shot or dropping the cross-shot relationship.
- **3 invalid `SOURCE_STATE` / 2 invalid `TARGET_STATE` refs** in
  `MASTER_MOTIONS` (motions `R01`-`R03`, same video) pointed at reveal
  sub-phase labels (`F02.2a`/`F02.2b` etc.) that are not real
  `MASTER_STATES` rows — remapped to the enclosing canonical state.
- **15 `STATE_CHANGE` rows** held a compound value (`A27;A28` etc.) in the
  singular `MOTION_ID` field. Added a `MOTION_IDS` column: single-motion rows
  mirror it, genuinely-simultaneous rows carry the list there and leave
  `MOTION_ID` blank.
- **`SOURCE_TO_FORENSIC_MAP.csv`** still had `STATUS=UNKNOWN`/
  `OLD_NO_AUDIO_LIMITATION` and `AUDIO_REANALYSIS_REQUIRED=CHECK/YES` for
  all 14 rows despite every video being fully transcribed and sync-mapped.
  Updated to `AUDIO_VERIFIED / TRANSCRIPT_COMPLETE / SYNC_COMPLETE` /
  `NO`, with the old no-audio issue for `SRC03` marked historically resolved.
- **`SOURCE_VIDEO_INDEX.csv`** was missing `DURATION_SEC`/`WIDTH`/`HEIGHT`/
  `ASPECT_RATIO`/`FPS`/codec/audio fields. Populated directly via `ffprobe`
  against the actual source files (not copied from any manifest text).
- **`04_patterns/TRANSITION_PATTERNS.csv`**'s `TYPICAL_DURATION_SEC` was a
  constant `0.3` placeholder. Replaced with the real measured value: every
  one of the corpus's 186 shot-to-shot boundaries has an exact `0.0s` gap
  (no fades exist), so `0.000` is now the genuinely measured figure, not a
  fabricated one.
- Dependent DNA docs (`EDITING_DNA.md`, `VISUAL_DNA.md`,
  `AUDIO_VISUAL_SYNC_DNA.md`) and blueprints referencing shot-duration or
  sync-offset statistics were recomputed against the corrected data.
  `05_blueprints/SHOT_DESIGN_BLUEPRINT.md` (generic pt-size/hex-color/DPI
  claims with no supporting schema column) was rewritten to contain only
  measured camera/transition/duration/asset facts.

None of `MASTER_WORDS`, `MASTER_SENTENCES`, `MASTER_ASSETS`,
`MASTER_AUDIO_EVENTS`, or the `MOTION_START`/`MOTION_END` sync rows needed
any change in this pass — they were already validated clean in the prior
pass and remain so.

## What this run does NOT claim

The validator checks referential integrity, schema conformance, timestamp
arithmetic, and canonical-file presence. It does not (and cannot) verify
that free-text fields (`DESCRIPTION`, `ACTION`, `NOTES`, etc.) are
semantically correct — those were checked manually during the rebuild by
cross-referencing raw per-video source CSVs, not by this script.

## Pre-existing data quality notes (not failures)

- 26 word rows have a 10ms timestamp overlap with the following word — a
  Whisper alignment rounding artifact, verified present in the source
  `TRANSCRIPT_WORDS.csv` files themselves. Semantically valid; does not
  affect sentence membership or any foreign-key relationship.
- Cross-video asset reuse is not tracked anywhere in the schema.
- The sync schema populates only `STATE_CHANGE`/`MOTION_START`/`MOTION_END`;
  no `SHOT_CUT`/`TEXT_REVEAL`/`GRAPHIC_REVEAL` event types exist.
