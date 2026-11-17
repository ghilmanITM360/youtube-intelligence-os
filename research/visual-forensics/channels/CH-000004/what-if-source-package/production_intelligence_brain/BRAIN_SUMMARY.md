# Production Intelligence Brain — Summary

**Release:** v1.0.0
**Status:** COMPLETE_VALIDATED

14 source "what if" videos, forensically decoded into master reference tables
for reconstruction. This summary reflects the state after **two** integrity
passes: the first rebuilt three of the eight master tables from their
original per-video forensic sources (sentences, assets, motions, plus the
A/V sync table's motion linkage); the second fixed temporal and
referential-integrity defects an independent audit found that the first
pass's validator did not check (zeroed shot/state timestamps, stale shot
aggregate counts, motion foreign-key errors, and a compound-value sync
field). See `CONTINUATION_HANDOFF.md` for the detailed repair log of both
passes.

## Corpus

14 videos, 8 portrait (9:16), 6 landscape (16:9). All 24fps except one 30fps
video (`what_if_all_visible_light_was_a_single_beam`).

## Master Data (`01_master_data/`, all 8 CSVs, real counts)

| Table | Rows |
|---|---|
| MASTER_WORDS | 7,864 |
| MASTER_SENTENCES | 604 meaningful sentences |
| MASTER_MOTIONS | 438 |
| MASTER_STATES | 581 |
| MASTER_SHOTS | 200 |
| MASTER_ASSETS | 448 |
| MASTER_AUDIO_EVENTS | 29 (14 NARRATION, 8 SILENCE, 7 PAUSE) |
| MASTER_AUDIO_VISUAL_SYNC | 1,421 (581 STATE_CHANGE, 438 MOTION_START, 402 MOTION_END) |

## What changed in this pass

- **Sentences:** rebuilt `FIRST_WORD_ID`/`LAST_WORD_ID`/`WORD_COUNT` for all 604 meaningful sentences from real linked `MASTER_WORDS` rows; removed 6 zero-duration, zero-word transcript-generation placeholder rows (the non-speech condition they sat in is already covered by a real measured `PAUSE` audio event).
- **Assets:** rebuilt from the 14 per-video `ASSET_MANIFEST.csv` files (448 rows vs. the previous 351-row aggregate, which had `REUSE_STATUS`/`MEDIA_FORMAT_NEEDED`/`TRANSPARENT_BG`/`SOURCE_OR_RECREATION_METHOD` empty for every row); 28 rows with unquoted-comma column shift were manually repaired against their raw positional fields.
- **Motions:** rebuilt from the 14 per-video `MOTION_EVENTS.csv` files (438 rows vs. the previous 417-row aggregate, which had apparently been built from the corrupted sync-table `MOTION_ID` column instead — 57 of those 417 rows held compound IDs, asset IDs, or bare prose instead of a real motion ID, and the one 30fps video's timestamps had all been zeroed out because its frame-number format wasn't recognized). 22 rows with column shift were repaired the same way as the assets.
- **A/V sync table MOTION_ID orphans:** 88 of the original 581 rows referenced a non-existent motion (compound IDs, asset IDs, `Hard cut`, `N/A`, literal prose, or the literal string `None`). Every one was resolved against the corrected motions table or cleared to empty — never assigned a newly invented ID — with the original text preserved in `NOTES`. Same repair applied to the `MOTION_IDS`/`ASSET_IDS` list columns in `MASTER_STATES`/`MASTER_SHOTS` (82 + 17 orphan tokens).
- **MOTION_START/MOTION_END events:** did not exist before this pass (0 of either). Built from real `MASTER_MOTIONS` timestamps aligned to `MASTER_WORDS`/`MASTER_AUDIO_EVENTS`: 438 `MOTION_START` + 402 `MOTION_END` (36 motions are instantaneous, `END_SEC == START_SEC`, so no separate end event exists for them — documented, not a gap).
- **Pattern tables:** `MOTION_PATTERNS`, `VISUAL_CHANGE_PATTERNS`, `AUDIO_TRIGGER_PATTERNS`, `SHOT_PATTERNS`, `STATE_PATTERNS` regenerated from the corrected master tables. `TRANSITION_PATTERNS` left unchanged — its source column (`MASTER_SHOTS.TRANSITION_OUT`) was not modified.
- **DNA docs (all 7):** `ASSET_DNA.md` and `MOTION_DNA.md` previously stated "Total distinct assets/motion events: 0" against real counts of 351/417 — both fully regenerated. `AUDIO_DNA.md`/`PACING_DNA.md` had a broken sentence-level section (55.8 words/sentence, a negative-duration range) — fixed to the real 13.0 words/sentence, 140–11,620ms range. `VISUAL_DNA.md` had an empty state-type table — filled in. `EDITING_DNA.md` claimed all 200 shots were uniformly "CUT" — replaced with the real, non-uniform transition-type breakdown. `AUDIO_VISUAL_SYNC_DNA.md` regenerated against the enriched 1,421-row sync table.
- **Reconstruction system:** `ASSET_CREATION_SYSTEM.md` and `DECISION_RULES.md` did not exist — both written from the corrected master data. `CAPCUT_RECONSTRUCTION_GUIDE.md`/`IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md` contained extensive fabricated specifics (font point sizes, fade durations, ms-precision text-timing rules, prompt templates) not supported by any column in the schema — superseded by `CAPCUT_PRODUCTION_SYSTEM.md`/`IMAGE_TO_VIDEO_SYSTEM.md`, which keep only what the corpus actually measures (e.g.: zero fade transitions exist anywhere in the corpus — every transition is a hard cut).
- **Blueprints:** the same fabricated offset/duration/fade numbers were also present in the 4 `05_blueprints/` docs and were corrected to reference the real measured values.
- **Validator:** `validator/validate_brain.py` + `validator/README.md` created as real, runnable project files (previously existed only as an ad hoc scratch script).

## What changed in the second (temporal integrity) pass

- **Shot/state timing:** 74/200 shots and 257/581 states across 7 videos had `START_SEC=END_SEC=0` despite a positive `DURATION_SEC` — the per-video `TIMELINE.csv` frame-index (or, for one video, already-in-seconds) IN/OUT values were never converted. An 8th video (`worlds-largest-cities-what-if`) had every state and shot zeroed outright (missed by the original `DURATION_SEC>0` filter). Recomputed from each video's own `TIMELINE.csv` + documented FPS and cross-checked against the independent `STATE_CHANGE.VISUAL_EVENT_SEC` values already in the sync table.
- **Shot aggregates:** 114 `STATE_COUNT` and 173 `MOTION_COUNT` mismatches across all 200 shots corpus-wide — recomputed every shot's timing/count/first-last-state fields directly from real state/motion membership.
- **Sync table:** 33 `STATE_CHANGE` rows (2 videos) had a stale `VISUAL_EVENT_SEC` that silently misresolved their sentence/word/offset linkage — recomputed and re-resolved. 15 rows held a compound value (`A27;A28`) in the singular `MOTION_ID` field — added a `MOTION_IDS` column for the genuinely-simultaneous case.
- **Motion foreign keys:** 1 pseudo `SHOT_ID` (`S01→S02`) and 5 sub-phase state references (`F02.2a` etc., not real `MASTER_STATES` rows) in `worlds-largest-cities-what-if` — resolved via a new `TARGET_SHOT_ID` column and remapping to the enclosing canonical state, respectively.
- **Source metadata:** `SOURCE_TO_FORENSIC_MAP.csv` updated from stale `UNKNOWN`/`OLD_NO_AUDIO_LIMITATION` statuses to current truth; `SOURCE_VIDEO_INDEX.csv` populated with real `ffprobe`-measured duration/resolution/fps/codec/audio fields.
- **`TRANSITION_PATTERNS.csv`:** the `0.3` placeholder duration replaced with the real measured value — every one of the corpus's 186 shot boundaries has an exact `0.0s` gap (zero fades exist), so `0.000` is the genuine figure.
- Dependent DNA docs and blueprints referencing shot-duration or sync-offset statistics recomputed; `SHOT_DESIGN_BLUEPRINT.md` (unsupported pt-size/hex-color/DPI claims) rewritten to contain only measured facts.

## Known, documented limitations

- Cross-video asset reuse is not tracked by the schema; all reuse statistics are within-video only.
- No SHOT_CUT/TEXT_REVEAL/GRAPHIC_REVEAL event types were added to the sync schema — only `STATE_CHANGE`/`MOTION_START`/`MOTION_END` are populated, since adding the others would require frame-level verification not performed in this pass.
- `MASTER_MOTIONS` carries both `A__` (415) and `R__` (23) ID namespaces by design — documented in `DECISION_RULES.md` §9, not renumbered.
- 26 word rows have a 10ms timestamp overlap from Whisper alignment rounding — semantically valid, not a referential-integrity issue.

## Canonical paths

See `CANONICAL_PATHS.md` for the authoritative map of every canonical location. `legacy/` holds superseded/duplicate files for provenance only — never canonical.

## Validator

```bash
python3 validator/validate_brain.py
```

See `VALIDATION_REPORT.md` for the full validator output and `CONTINUATION_HANDOFF.md` for exact next steps.
