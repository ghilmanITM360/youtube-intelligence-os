# Release Notes — Production Intelligence Brain v1.0.0

First validated stable release of the Production Intelligence Brain, following semantic versioning:
`1.0.0` = first validated stable release. Corrections become `1.0.1`; backward-compatible additions become `1.1.0`; breaking schema changes become `2.0.0`. **The frozen v1.0.0 release is never modified in place.**

## What this release contains

- 14-video forensic corpus (8 portrait 9:16, 6 landscape 16:9), audio-semantic recovery via Whisper transcription + word/sentence alignment
- 7,864 aligned words, 604 meaningful sentences
- 200 shots, 581 states, 438 motions, 448 assets
- 29 audio events (14 NARRATION, 8 SILENCE, 7 PAUSE)
- 1,421 audio/visual sync events (581 STATE_CHANGE, 438 MOTION_START, 402 MOTION_END)
- Temporal normalization and referential-integrity repair across all 8 master tables (see `CONTINUATION_HANDOFF.md` for the full repair log)
- Regenerated production DNA (7 docs + `DNA_INDEX.json`, recomputed from canonical data — no stale statistics)
- Regenerated reconstruction system index (`RECONSTRUCTION_INDEX.json`), referencing exactly the 4 canonical reconstruction docs
- Strict validator (`validator/validate_brain.py`) covering CSV structural integrity, foreign keys, timestamp arithmetic, aggregate counts, and index/manifest consistency
- Package cleanup: root-level duplicate master CSVs and a duplicate manifest moved to `legacy/`; two superseded reconstruction guides moved to `legacy/reconstruction/` with explicit supersession notices; one clear canonical location for every table and doc

## Known, genuine limitations (not validation failures)

- Cross-video asset identity/reuse is not modeled — all reuse statistics are within-video only.
- A/V sync semantic event types currently populate only `STATE_CHANGE`, `MOTION_START`, and `MOTION_END`. Additional types (e.g. `SHOT_CUT`, `TEXT_REVEAL`) are defined in the schema's allowed set but not yet frame-verified against the corpus, so they are left unpopulated rather than guessed.
- 26 word-timestamp overlaps of ~10ms are retained as source-derived Whisper alignment rounding artifacts — semantically valid, not a referential-integrity issue.
- `04_patterns/TRANSITION_PATTERNS.csv`'s `TYPICAL_DURATION_SEC` is a genuine measured constant of `0.000` (every one of the corpus's 186 shot boundaries is a hard cut with zero fade) — not a placeholder, but worth noting since a future corpus with real cross-fades would need this recomputed, not assumed.
- `MASTER_MOTIONS` carries two ID namespaces (`A__` action motions, `R__` static reveal-event motions) by design, documented in `DECISION_RULES.md` §9.

## Distinguishing validation failures from source-evidence limitations

A **validation failure** is something the schema promises and the data fails to deliver (a broken foreign key, a malformed row, a stale index). A **source-evidence limitation** is something the schema never promised and the evidence genuinely doesn't support (e.g. no cross-video asset identity model). The validator enforces the former; `RELEASE_NOTES.md`/`BRAIN_MANIFEST.json.known_limitations` document the latter. None of the limitations above cause the validator to fail.
