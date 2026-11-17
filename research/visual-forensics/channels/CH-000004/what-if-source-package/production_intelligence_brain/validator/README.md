# Brain Validator

Strict, from-disk integrity check over `production_intelligence_brain/`.
Nothing in `validate_brain.py` is cached or remembered — every count it
prints is computed from the current CSV/markdown files at run time.

## Run it

```bash
cd "production_intelligence_brain"
python3 validator/validate_brain.py
```

Exit code `0` = PASS. Exit code `1` = FAIL, with each failing check printed
as a `FAIL:` line and the offending count.

## What it checks

1. **Sentences** (`MASTER_SENTENCES.csv` vs `MASTER_WORDS.csv`): no empty
   meaningful sentences, no missing/invalid `FIRST_WORD_ID`/`LAST_WORD_ID`,
   `WORD_COUNT` matches the actual number of linked word rows (never
   `len(TEXT.split())`), no negative-duration rows, no duplicate composite
   `(VIDEO_SLUG, WORD_ID)` keys.
2. **Master foreign keys**: every `SHOT_ID`/`ASSET_IDS`/`MOTION_IDS` reference
   in `MASTER_STATES.csv` and `MASTER_SHOTS.csv` resolves against the real
   `MASTER_SHOTS`/`MASTER_ASSETS`/`MASTER_MOTIONS` tables, scoped per
   `VIDEO_SLUG`. The literal string `"None"` is treated as empty, not as a
   real reference.
3. **A/V sync events** (`MASTER_AUDIO_VISUAL_SYNC.csv`): `VISUAL_EVENT_TYPE`
   and `SYNC_RELATION` are drawn only from the allowed vocabularies; every
   non-empty `MOTION_ID`/`SENTENCE_ID`/`WORD_ID`/`AUDIO_EVENT_ID` resolves;
   no duplicate `(VIDEO_SLUG, SYNC_ID)` keys.
4. **Motion start/end linkage**: every one of the 438 canonical motions has a
   `MOTION_START` event; every motion with a real (non-instantaneous)
   duration has a `MOTION_END` event. Instantaneous transitions
   (`END_SEC == START_SEC`, 36 of the 438 motions) are not required to have a
   separate end event and are not counted as failures — that is a documented,
   evidence-based exception, not an unresolved gap.
5. **`MASTER_MOTIONS.csv` direct validation**: `SHOT_ID`/`TARGET_SHOT_ID`/
   `SOURCE_STATE`/`TARGET_STATE` each resolve against the real
   `MASTER_SHOTS`/`MASTER_STATES` tables (a motion's `SHOT_ID` may never hold
   a pseudo composite like `S01→S02` — cross-shot motions use `SHOT_ID` +
   `TARGET_SHOT_ID` instead); `DURATION_SEC` matches `END_SEC - START_SEC`
   within a ~1.5-frame tolerance; no duplicate `(VIDEO_SLUG, MOTION_ID)` keys.
6. **`MASTER_SHOTS.csv` / `MASTER_STATES.csv` direct validation**: every
   state's `DURATION_SEC` matches its own `END_SEC - START_SEC`; states
   within a shot are time-monotonic (no backwards-running intervals); every
   state's `SHOT_ID` resolves; every shot's `START_SEC`/`END_SEC`/
   `DURATION_SEC`/`FIRST_STATE_ID`/`LAST_STATE_ID`/`STATE_COUNT`/
   `MOTION_COUNT` is recomputed independently from its actual member states
   and motions and compared against the stored value — this is the check
   that catches a shot/state table whose aggregate fields silently drifted
   from real membership (it once caught 114 `STATE_COUNT` and 173
   `MOTION_COUNT` mismatches corpus-wide, plus 74 shots / 257 states with
   `START_SEC=END_SEC=0` despite a positive `DURATION_SEC` — see
   `CONTINUATION_HANDOFF.md`).
7. **A/V sync foreign keys beyond motion**: every non-empty `SHOT_ID`/
   `TARGET_SHOT_ID`/`SOURCE_STATE`/`TARGET_STATE` in
   `MASTER_AUDIO_VISUAL_SYNC.csv` resolves, not just `MOTION_ID`/`MOTION_IDS`.
   A `STATE_CHANGE`/`MOTION_START`/`MOTION_END` row that genuinely relates to
   more than one motion (e.g. two simultaneous camera moves) carries them in
   `MOTION_IDS` (semicolon-separated) with the singular `MOTION_ID` field left
   blank, rather than putting a compound value like `A27;A28` into a field
   documented as a single foreign key.
8. **Raw CSV width**: every one of the 8 master CSVs is re-read with
   `csv.reader` (not `DictReader`) and every data row is checked to have
   exactly as many fields as the header — this catches unquoted-comma
   column-shift corruption that `DictReader` alone would silently absorb
   into `None`/extra keys.
9. **Hard timestamp errors**: a corpus-wide rollup across
   `MASTER_MOTIONS`/`MASTER_STATES`/`MASTER_SHOTS` for any row where
   `END_SEC < START_SEC` or either timestamp fails to parse as a number.
10. **Canonical artifact presence**: the 8 master CSVs, 7 DNA docs, 4
    reconstruction-system docs, 6 pattern tables, 4 blueprints, this
    validator + its README + schemas, the testing-protocol files, and the
    top-level report/manifest files all exist and are non-trivial (> 50 bytes).
11. **Index / manifest consistency**: `02_production_dna/DNA_INDEX.json`,
    `03_reconstruction_system/RECONSTRUCTION_INDEX.json`, and
    `BRAIN_MANIFEST.json` are each re-checked field-by-field against counts
    computed live from `01_master_data/`. A stale index (e.g. an old sentence
    count or A/V sync total left over from before a repair pass) fails
    validation instead of silently shipping. `RECONSTRUCTION_INDEX.json` must
    reference exactly the 4 canonical reconstruction docs and must not
    mention either superseded guide.
12. **Legacy isolation**: `DNA_INDEX.json`, `RECONSTRUCTION_INDEX.json`,
    `BRAIN_MANIFEST.json`, and every blueprint doc are scanned for any
    `legacy/` path reference — none may cite `legacy/` as current authority.
13. **Strict canonical file enumeration**: the top-level directory listing
    must match the canonical contract exactly (nothing unexpected, e.g. a
    stray duplicate CSV left at root); each canonical subdirectory is
    checked for files that don't match its expected glob pattern.
14. **RELEASE_MANIFEST validation** (once `RELEASE_MANIFEST.json` exists):
    every declared file's size and SHA-256 are recomputed from disk and
    compared; every currently-canonical file must be declared (no
    undeclared drift) and every declared file must still be canonical (no
    stale entries). The manifest is never checked against itself — it does
    not list its own file, avoiding a recursive hash dependency. Before that
    file is built, this section is skipped with an explicit note (expected
    pre-freeze).

## Building the release manifest

```bash
python3 validator/build_release_manifest.py
```

Regenerates `RELEASE_MANIFEST.json` from whatever canonical files are
currently on disk (see `validator/_canonical_files.py` for the exact file
list this and the validator both use). Re-run `validate_brain.py` afterward
to confirm the new manifest matches disk.

## Known, documented data limitations (not validator failures)

These are real properties of the source forensic data, not integrity bugs,
and the validator does not fail on them:

- `MASTER_MOTIONS.csv` / `MASTER_AUDIO_VISUAL_SYNC.csv` had rows across the
  per-video `MOTION_EVENTS.csv`/`ASSET_MANIFEST.csv` source CSVs and the
  aggregate sync table with unquoted-comma column shift or literal
  prose/asset-ID values sitting in a `MOTION_ID` field. Every one was
  manually verified against its raw positional fields and either repaired
  (valid ID extracted, rest preserved in `NOTES`) or cleared to empty
  (original text preserved in `NOTES`) — never assigned a newly invented ID.
  See the rebuild scripts' inline docstrings for the exact per-row repair
  mapping.
- `worlds-largest-cities-what-if` motion `R01`-`R03` originally referenced
  `SOURCE_STATE`/`TARGET_STATE` sub-phase labels (`F02.2a`/`F02.2b`, etc.)
  that are not their own rows in `MASTER_STATES` — they are reveal sub-phases
  within one held canonical state. Mapped to the enclosing canonical state
  rather than invented as new states (`DECISION_RULES.md` §8).
- Cross-video asset reuse is not tracked anywhere in the schema; all reuse
  statistics in `ASSET_DNA.md` are within-video only.
