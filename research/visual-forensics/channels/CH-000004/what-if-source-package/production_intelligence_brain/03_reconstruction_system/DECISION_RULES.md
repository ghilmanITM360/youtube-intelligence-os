# Decision Rules

Built strictly from the validated `01_master_data/` master tables (`MASTER_SHOTS`,
`MASTER_STATES`, `MASTER_MOTIONS`, `MASTER_ASSETS`, `MASTER_AUDIO_VISUAL_SYNC`)
after this pass's repairs. `04_patterns/TRANSITION_PATTERNS.csv`'s
`TYPICAL_DURATION_SEC` column used to be a `0.3` placeholder constant; it has
since been replaced with the real measured value (`0.000`s — see rule 7
below) and can now be used as a source. Every rule below states its real
support count.

## 1. Shot transition type

- **Support:** 200 shots.
- **Rule:** 146/200 shots (73%) enter via a hard-cut-family transition (`TRANSITION_IN` matching CUT/HARD CUT in any casing); 50/200 (25%) enter via a specific named motion carried over from the previous shot's exit action.
- **Exit side differs:** 125/200 shots (62.5%) exit via a named motion description; only 60/200 (30%) exit via a bare cut keyword; 15/200 (7.5%, the final shot of a video) have no exit.
- **Confidence:** OBSERVED (directly read from per-video `TIMELINE.csv`/`MOTION_EVENTS.csv`).
- **Exceptions:** `worlds-largest-cities-what-if` S02 is a single 70s shot with no internal cuts (see `ASSET_DNA.md`'s backbone-map note) — do not force a cut-based reconstruction on that shot.

## 2. Camera behavior

- **Support:** 581 states.
- **Rule:** 521/581 states (89.7%) report a LOCKED- or STATIC-family `CAMERA_STATE`. Default a reconstructed shot to a locked camera; only deviate where a specific state's `CAMERA_STATE` says otherwise (e.g. `PAN`, `PUSH-IN`, `HOLD` — all present in `worlds-largest-cities-what-if`, the corpus's one continuously-panned-map video).
- **Confidence:** OBSERVED.

## 3. Motion duration by relationship type

- **Support:** 438 motions.

| RELATIONSHIP | n | Avg duration |
|---|---|---|
| STATE_REPLACEMENT | 230 | 1.60s |
| SEQUENTIAL | 131 | 3.51s |
| SIMULTANEOUS_COUPLED | 36 | 4.26s |
| SIMULTANEOUS_INDEPENDENT | 29 | 4.50s |
| PERSISTENT_LOOP | 7 | 9.42s |
| CAMERA_SUBJECT_COUPLED | 4 | 7.66s |

- **Rule:** a `STATE_REPLACEMENT` motion (53% of all motions) should be reconstructed as a fast (~1.6s) discrete swap, not a slow animated transform. `PERSISTENT_LOOP` motions are rare (n=7) but long (~9.4s) — these are held/looping elements (e.g. the rotation-arrow glyph in `earthquake-magnitude-shorts-wBLVmEZV2Oc`), not one-shot reveals.
- **Confidence:** mixed — see rule 6 below for the corpus's own confidence tiering; do not treat all 438 motions as equally certain.

## 4. Motion-to-speech alignment

- **Support:** 438 `MOTION_START` + 402 `MOTION_END` sync events (see `AUDIO_VISUAL_SYNC_DNA.md`).
- **Rule:** 99.5% of motion starts and 98.8% of motion ends occur during or immediately adjacent to an active spoken word (`DURING_WORD`, `BETWEEN_WORDS`, `ON_WORD_START`, `ON_WORD_END`, or `AFTER_WORD`) — when reconstructing a new video from a script, trigger motion starts on the nearest word boundary rather than an arbitrary fixed delay.
- **Exception:** 2 motion starts and 5 motion ends (~1%) occur during measured silence/pause (`DURING_SILENCE`/`DURING_PAUSE`) — these should NOT be forced onto a word.
- **Confidence:** MEASURED (word/motion timestamps are both directly observed).

## 5. Asset format/transparency by type

- See `ASSET_CREATION_SYSTEM.md` for the full per-type breakdown (n=448). Summary: CHARACTER assets are 96% transparent PNG; ENVIRONMENT assets are 88% opaque full-frame plates; the remaining types split more evenly.

## 6. Trust the corpus's own confidence tiers

- **Support:** 438 motions carry a `CONFIDENCE` field.
- **Rule:** 152/438 (35%) are `OBSERVED` (directly verified from frame evidence), 104/438 (24%) are `LIKELY` (inferred but not frame-confirmed), 6/438 (1%) are explicitly `APPROXIMATE`, 1 is `POSSIBLE`. The remaining 175 (40%) carry a non-standard confidence string (e.g. combined qualifiers) rather than one of these four tiers.
- **When reconstructing:** prefer `OBSERVED` motions as ground truth for exact timing; treat `LIKELY`/`POSSIBLE`/`APPROXIMATE` motions as needing a frame-check against `01_evidence/frames/` before committing to sub-second precision, per the original task's own instruction not to fabricate motion precision.

## 7. Shot-boundary transition duration

- **Support:** all 186 internal shot-to-shot boundaries across the 14-video corpus (`MASTER_SHOTS`, sorted by `START_SEC` per video).
- **Rule:** every single shot boundary has a measured gap of exactly `0.0s` — the next shot's `START_SEC` always equals the previous shot's `END_SEC`. There is no fade, cross-dissolve, or hold frame at any cut in this corpus; every transition is instantaneous at the measured (1-frame) resolution. `04_patterns/TRANSITION_PATTERNS.csv`'s `TYPICAL_DURATION_SEC` reflects this (`0.000` for all 82 transition-text groupings).
- **Confidence:** MEASURED. Do not add a fade/cross-dissolve duration when reconstructing from this corpus's patterns.

## 8. Cross-shot motions and reveal sub-phases (schema conventions)

- **Cross-shot motion:** a motion whose action spans two shots (e.g. a whip-zoom that starts the tail of one shot and lands in the next) is assigned to its **originating** shot in `SHOT_ID`, with the destination shot recorded separately in `TARGET_SHOT_ID`. `SHOT_ID` never holds a composite value like `S01→S02` — that string was found once (`worlds-largest-cities-what-if` motion A02) and was corrected to `SHOT_ID=S01, TARGET_SHOT_ID=S02`. `MASTER_AUDIO_VISUAL_SYNC.csv` carries the same `TARGET_SHOT_ID` column for its `MOTION_START`/`MOTION_END` rows.
- **Reveal sub-phases:** a handful of motions (`worlds-largest-cities-what-if` R01–R03) originally referenced `SOURCE_STATE`/`TARGET_STATE` values like `F02.2a`/`F02.2b` that do not exist as their own rows in `MASTER_STATES` — they are internal pin-reveal sub-phases occurring *within* one held canonical state (`F02.2`, `F02.3`), not real state transitions. These are mapped to the enclosing canonical state on both ends (e.g. `F02.2a`→`F02.2`, `F02.2b`→`F02.2`) rather than invented as new states.
- **Confidence:** OBSERVED (source `MOTION_EVENTS.csv` for this video explicitly describes these as "fade/pop-in while camera holds" — a same-state reveal, not a cut).

## 9. Motion ID namespace

- **Support:** 438 motions use either an `A__` or `R__` prefix.
- **Rule:** `A__` (415 motions) is the general action/camera-motion namespace. `R__` (23 motions, all in `worlds-largest-cities-what-if`) is a distinct **reveal-event** namespace for static pop-in/fade annotations (pins, stickers, callouts) that occur without camera movement, as opposed to `A__`'s pans/pushes/zooms. Both are accepted canonical namespaces — do not renumber `R__` motions into the `A__` sequence; downstream `MASTER_AUDIO_VISUAL_SYNC` rows reference them by their existing IDs.
- **Confidence:** OBSERVED (the source `MOTION_EVENTS.csv` for this video already separates them this way; not a naming scheme imposed by this pass).

## What is NOT supported by current data

- No rule is given for SHOT_CUT/TEXT_REVEAL/GRAPHIC_REVEAL timing beyond what's in `AUDIO_VISUAL_SYNC_DNA.md`, because the sync schema does not currently contain those event types (only `STATE_CHANGE`/`MOTION_START`/`MOTION_END` — adding them would require the same per-motion frame verification described in the original task's step 15/16, which is out of scope for a data-derived document and was not fabricated here).
