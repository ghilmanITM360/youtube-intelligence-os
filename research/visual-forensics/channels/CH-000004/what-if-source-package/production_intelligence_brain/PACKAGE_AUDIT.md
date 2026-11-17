# Package Audit — production_intelligence_brain (pre-v1.0.0 freeze)

Audit date: 2026-09-17. Read-only investigation; no files inside
`production_intelligence_brain/` were modified, moved, or deleted at the time
this report was written. This report is a point-in-time snapshot of what the
audit found — it is not a live index and is not re-checked by the validator.

> **Post-audit update:** every issue this report flags below has since been
> resolved as part of the v1.0.0 release-hardening pass: the 8 root-level
> duplicate CSVs and `BRAIN_MANIFEST_VALIDATED.json` were moved to
> `legacy/root_master_duplicates/` and `legacy/`; the two superseded
> reconstruction guides were moved to `legacy/reconstruction/` with
> SUPERSEDED notices; `DNA_INDEX.json` and `RECONSTRUCTION_INDEX.json` were
> rebuilt from canonical data. See `CANONICAL_PATHS.md`, `RELEASE_NOTES.md`,
> and `validator/validate_brain.py` (which now checks all of this on every
> run) for current state.

---

## 1. Root-level duplicate CSVs

Byte-for-byte comparison (`shasum`) of every root `MASTER_*.csv` against its
`01_master_data/` counterpart:

| File | Root sha1 | `01_master_data/` sha1 | Result |
|---|---|---|---|
| MASTER_ASSETS.csv | identical | identical | **IDENTICAL** |
| MASTER_AUDIO_EVENTS.csv | identical | identical | **IDENTICAL** |
| MASTER_AUDIO_VISUAL_SYNC.csv | identical | identical | **IDENTICAL** |
| MASTER_MOTIONS.csv | identical | identical | **IDENTICAL** |
| MASTER_SENTENCES.csv | identical | identical | **IDENTICAL** |
| MASTER_SHOTS.csv | identical | identical | **IDENTICAL** |
| MASTER_STATES.csv | identical | identical | **IDENTICAL** |
| MASTER_WORDS.csv | identical | identical | **IDENTICAL** |

All 8 pairs are exact byte-for-byte duplicates. No divergence.

**Reference grep** (all `.py`/`.md`/`.json` in the brain, for
`MASTER_(ASSETS|AUDIO_EVENTS|AUDIO_VISUAL_SYNC|MOTIONS|SENTENCES|SHOTS|STATES|WORDS)\.csv`):
every hit is a bare filename mention inside prose (docs describing "regenerated
from `MASTER_X.csv`" etc.) or the validator's own source. None of the prose
references carry a `01_master_data/` prefix nor a root/absolute-path prefix
that would resolve to the root copies specifically — they are just filename
mentions, not code paths, **except** `validator/validate_brain.py`, which is
the only file that actually opens these CSVs programmatically:

- `validator/validate_brain.py:19-20`: `BRAIN = dirname(dirname(abspath(__file__)))`; `MD = os.path.join(BRAIN, '01_master_data')`
- `validator/validate_brain.py:30-33` (`load()`): opens `os.path.join(MD, name)` — i.e. always `01_master_data/<name>`, never the root.
- `validator/validate_brain.py:44-51`: `load('MASTER_SENTENCES.csv')` etc. — all 8 loads go through `MD`.
- `validator/validate_brain.py:381-382` (`CSV_FILES`) and `:384-386`: width-check loop also builds `path = os.path.join(MD, fname)` — `01_master_data/` only.
- `validator/validate_brain.py:417-418`: the "canonical artifact presence" check requires the 8 files to exist at `BRAIN/01_master_data/<name>` — it does not check or reference the root copies at all.

**Conclusion: nothing reads the root-level copies.** They are pure,
unreferenced duplicates. Every consumer (validator, docs) resolves to
`01_master_data/`. The root copies are dead weight for the v1.0.0 freeze —
candidates for deletion (not performed here, per read-only mandate).

---

## 2. BRAIN_MANIFEST.json vs BRAIN_MANIFEST_VALIDATED.json

`diff BRAIN_MANIFEST.json BRAIN_MANIFEST_VALIDATED.json` → **no output**
(files are identical). `shasum` confirms: both
`b162130056cf368a5ff78f86a02013e550cae92d`.

Grep for `BRAIN_MANIFEST_VALIDATED` across the whole brain directory:
**zero references anywhere** (not from `validate_brain.py`, not from any
`.md`). Grep for `BRAIN_MANIFEST.json`: exactly one reference,
`validator/validate_brain.py:439`, which lists it as one of the required
top-level report files whose presence/non-triviality is checked.

**Conclusion:** `BRAIN_MANIFEST_VALIDATED.json` is an untracked, unreferenced
exact duplicate of `BRAIN_MANIFEST.json` — nothing points to it. Neither file
is stale (see §7 — both match computed counts exactly); the issue is purely
that `BRAIN_MANIFEST_VALIDATED.json` is a redundant, dangling copy that isn't
part of the documented canonical contract.

---

## 3. DNA_INDEX.json staleness

### Independently computed canonical counts (from `01_master_data/` and root `SOURCE_VIDEO_INDEX.csv`, verified two ways: manual `wc -l` row counts AND a full run of `validator/validate_brain.py`, which agree exactly)

| Metric | Computed value |
|---|---|
| Source video count (`SOURCE_VIDEO_INDEX.csv` data rows) | **14** |
| Word count (`MASTER_WORDS.csv`) | **7,864** |
| Sentence count (`MASTER_SENTENCES.csv`) | **604** |
| Shot count (`MASTER_SHOTS.csv`) | **200** |
| State count (`MASTER_STATES.csv`) | **581** |
| Motion count (`MASTER_MOTIONS.csv`) | **438** |
| Asset count (`MASTER_ASSETS.csv`) | **448** |
| Audio event count (`MASTER_AUDIO_EVENTS.csv`) | **29** |
| A/V sync total (`MASTER_AUDIO_VISUAL_SYNC.csv`) | **1,421** |
| — by `VISUAL_EVENT_TYPE` | `STATE_CHANGE` = **581**, `MOTION_START` = **438**, `MOTION_END` = **402** |

Note on "meaningful sentences": `MASTER_SENTENCES.csv` has **no** flag/filter
column distinguishing "meaningful" from "total" (header:
`VIDEO_SLUG,SENTENCE_ID,START_SEC,END_SEC,TEXT,FIRST_WORD_ID,LAST_WORD_ID,WORD_COUNT,CONFIDENCE,NOTES`
— no boolean/flag field). Per `BRAIN_SUMMARY.md`/`CONTINUATION_HANDOFF.md`,
6 zero-duration/zero-word placeholder rows were already removed from the
file; all 604 remaining rows *are* "the meaningful sentences" — there is
nothing left to filter.

### DNA_INDEX.json fields that disagree with computed values

`02_production_dna/DNA_INDEX.json` is a **mixed bag**: its `word_timing` and
`audio_events` blocks are current, but its `sentence_pacing` and
`sync_relationships` blocks are stale leftovers from before the two repair
passes documented in `CONTINUATION_HANDOFF.md`:

| Field (path in DNA_INDEX.json) | Stale value in file | Computed/correct value | Stale? |
|---|---|---|---|
| `sentence_pacing.total_sentences` | **141** | 604 | **YES — the old known-stale figure is still present** |
| `sentence_pacing.mean_words_per_sentence` | **55.8** | 7864/604 ≈ 13.02 (docs say "13.0") | **YES — the old known-stale figure is still present** |
| `sentence_pacing.min_sentence_duration_ms` | **-17260.0** | validator confirms `NEGATIVE_DURATION_ROWS = 0` in the current `MASTER_SENTENCES.csv` — a negative duration cannot exist | **YES — stale negative value still present** |
| `sentence_pacing.mean_sentence_duration_ms` / `median_sentence_duration_ms` / `max_sentence_duration_ms` | 7818.2 / 2920.0 / 41020.0 | not independently recomputed here (no time budget for a full per-sentence recompute), but given `total_sentences` is wrong by 4.3x, these are almost certainly stale too | **LIKELY stale (inherits from same block)** |
| `sync_relationships.total_syncs` | **581** | 1,421 | **YES — only counts the old STATE_CHANGE-only schema** |
| `sync_relationships.visual_event_types` | `{"STATE_CHANGE": 581}` only | `{"STATE_CHANGE": 581, "MOTION_START": 438, "MOTION_END": 402}` | **YES — missing MOTION_START/MOTION_END entirely (they didn't exist when this block was generated)** |
| `word_timing.count` | 7864 | 7864 | matches — **not stale** |
| `audio_events.total_events` / `event_types` | 29 total, 14/8/7 | 29 total, 14 NARRATION / 8 SILENCE / 7 PAUSE | matches — **not stale** |

**All three of the specifically-flagged old-known-stale numbers are
confirmed still present verbatim: "141" sentences, "55.8" words/sentence,
and a negative minimum sentence duration (-17260.0 ms). The old "581 total
A/V events" figure is also still present** (as `sync_relationships.total_syncs`
— it's actually the old STATE_CHANGE-only sync count, now understated
against the true 1,421-row total).

`per_video_statistics` (word/event/sync counts per video) were not
cross-checked in full but are unaffected by the sentence/sync staleness
above.

---

## 4. RECONSTRUCTION_INDEX.json

`03_reconstruction_system/RECONSTRUCTION_INDEX.json` (74 lines):

- **Does NOT reference `CAPCUT_RECONSTRUCTION_GUIDE.md` or
  `IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md` anywhere** (grepped the file
  directly — zero hits for either filename). Its `"systems"` array names the
  systems generically ("CapCut Reconstruction", "Image-to-Video Synthesis")
  and doesn't cite either canonical or legacy doc filenames at all.
- **Embeds the same stale DNA figures as DNA_INDEX.json**, verbatim, under
  `dna_reference`: line 48, `"total_sentences": 141`; line 51,
  `"mean_words_per_sentence": 55.8`; line 52,
  `"min_sentence_duration_ms": -17260.0`; line 56, `"total_syncs": 581`
  (missing MOTION_START/MOTION_END). This is the same staleness as §3,
  copy-pasted into a second file.
- Does **not** assert a hard universal output-format rule. It says (line 34):
  `"resolution": "Match source video (typically 1920×1080)"` — phrased as
  "match source, typically 1920×1080," not a fixed universal rule. However,
  this is itself slightly misleading: the corpus is **8 portrait (9:16) / 6
  landscape (16:9)** per `BRAIN_SUMMARY.md` and confirmed by
  `IMAGE_TO_VIDEO_SYSTEM.md` §1 (which lists all 14 slugs by orientation).
  "Typically 1920×1080" (a 16:9 landscape resolution) is not actually typical
  of the majority orientation split direction-for-direction, though it
  doesn't forbid portrait. No hard "16:9" universal claim is made anywhere in
  this file.

---

## 5. Legacy reconstruction guides

`CAPCUT_RECONSTRUCTION_GUIDE.md` (139 lines) and
`IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md` (195 lines) sit beside
`CAPCUT_PRODUCTION_SYSTEM.md` (37 lines) and `IMAGE_TO_VIDEO_SYSTEM.md`
(29 lines).

- Both canonical docs open with an explicit supersession line:
  `CAPCUT_PRODUCTION_SYSTEM.md:3`: `"Supersedes CAPCUT_RECONSTRUCTION_GUIDE.md. That file's specific numeric guidance (fade durations of 0.1–0.3s, font sizes in pt, "-500ms to word onset" text timing, an "0.8x slow-motion exception," per-object color-coding rules) was checked against the corpus and is not supported by any measured column..."`
  `IMAGE_TO_VIDEO_SYSTEM.md:3`: `"Supersedes IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md. That file's specific prompt templates, "8-word sentence → 1.8–2.0s hard ceiling" timing formulas, and motion-characteristic prescriptions... are generic AI-video-generation best-practice text, not measurements derived from this corpus..."`
- Content comparison confirms the claim: the legacy guides contain specific
  numeric prescriptions (fade durations 0.1–0.3s, font point sizes, ms-offset
  cut-timing rules, a fixed I2V prompt template, an "8-word → 1.8–2.0s"
  duration formula) that are **not derivable from the schema** — e.g. no
  fade transitions exist anywhere in the 200-shot corpus (`CAPCUT_PRODUCTION_SYSTEM.md`
  §1: "Zero fade, cross-dissolve, wipe, or slide transitions appear anywhere
  in the corpus"), yet the legacy guide prescribes fade durations for them.
  The canonical docs cover the same ground (transitions, camera, motion
  timing, audio for CapCut; aspect ratio, motion-continuity criteria,
  duration source for I2V) but ground every rule in an actual measured
  figure from `01_master_data/`, and each has an explicit
  "What is NOT supported by current data (dropped from the prior guide)"
  section.
- **Reference check:** grep for both legacy filenames across the whole brain
  finds them referenced only inside `BRAIN_SUMMARY.md:41` (describing the
  supersession, historically) and inside the two canonical docs' own
  "Supersedes ..." opening lines. **Nothing treats either legacy guide as
  current/canonical** — `RECONSTRUCTION_INDEX.json` doesn't mention them at
  all (§4), and `validate_brain.py`'s canonical-artifact-presence check
  (line 421-422) requires only the 4 canonical docs
  (`CAPCUT_PRODUCTION_SYSTEM.md`, `IMAGE_TO_VIDEO_SYSTEM.md`,
  `ASSET_CREATION_SYSTEM.md`, `DECISION_RULES.md`), not the two legacy files.

**Conclusion: confirmed superseded, confirmed not referenced as canonical
anywhere.**

---

## 6. TRANSITION_PATTERNS.csv placeholder

`04_patterns/TRANSITION_PATTERNS.csv`: **82 data rows** (header + 82 = 83
lines on disk). Columns: `TRANSITION_TYPE, OCCURRENCE_COUNT,
TYPICAL_DURATION_SEC, CONTEXT`.

- **`TYPICAL_DURATION_SEC` is a constant `0.000` across all 82 rows** —
  verified via Python `csv.DictReader` (quote-safe; a naive `cut -d,`
  mis-splits because `CONTEXT`/`TRANSITION_TYPE` values contain embedded
  commas inside quoted fields). `set(unique values) == {'0.000'}`.
- The `CONTEXT` column is *also* constant (`shot_exit`) across all 82 rows —
  not asked for explicitly, but worth flagging as a second placeholder-shaped
  column.
- **This is documented, not hidden**: `CONTINUATION_HANDOFF.md` item 10 and
  `BRAIN_SUMMARY.md`'s "What changed in the second pass" both state the prior
  placeholder was a literal `0.3` constant, and that it was replaced with
  `0.000` after auditing all 186 shot-to-shot boundaries in
  `MASTER_SHOTS.csv` and finding every single one has an exact 0.0s gap (no
  fades exist anywhere in the corpus — confirmed independently by
  `CAPCUT_PRODUCTION_SYSTEM.md` §1's transition-keyword tally). **The current
  constant `0.000` is asserted by the project's own docs to be a genuine
  measured value, not a fabricated placeholder** — but it is impossible to
  independently re-derive "186 shot-to-shot boundaries all measured at
  exactly 0.0s" from `TRANSITION_PATTERNS.csv` alone without re-running that
  audit against `MASTER_SHOTS.csv`, which was outside this audit's scope.
  Flagging as **PLAUSIBLE-BUT-UNVERIFIED-BY-THIS-AUDIT** rather than
  confirmed-fabricated: the column being a hard constant is exactly what a
  placeholder would look like, and the only evidence it's real measurement
  rather than an unchanged placeholder-with-a-different-value is the prose
  claim in `CONTINUATION_HANDOFF.md`/`BRAIN_SUMMARY.md` itself.
  **Contradiction found:** `BRAIN_MANIFEST.json`'s `next_action` field
  (line 52) asserts *"04_patterns (6 tables, TRANSITION_PATTERNS duration now
  measured not placeholder)"` — this is consistent with the `0.000` figure
  being claimed-measured, but a reviewer should note the claim rests entirely
  on prose, not on any distinguishing signal inside the CSV itself (a
  genuinely-zero measurement and an unchanged-but-relabeled placeholder are
  byte-identical).

---

## 7. BRAIN_MANIFEST.json vs computed counts

| Field | BRAIN_MANIFEST.json value | Computed value | Match? |
|---|---|---|---|
| `source_video_count` | 14 | 14 | ✅ |
| `total_words` | 7,864 | 7,864 | ✅ |
| `total_meaningful_sentences` | 604 | 604 | ✅ |
| `total_shots` | 200 | 200 | ✅ |
| `total_states` | 581 | 581 | ✅ |
| `total_motions` | 438 | 438 | ✅ |
| `total_assets` | 448 | 448 | ✅ |
| `total_audio_events` | 29 | 29 | ✅ |
| `total_av_sync_events` | 1,421 | 1,421 | ✅ |
| `motion_start_events` | 438 | 438 | ✅ |
| `motion_end_events` | 402 | 402 | ✅ |

**BRAIN_MANIFEST.json (and its identical duplicate
BRAIN_MANIFEST_VALIDATED.json) is fully current — every count matches the
independently computed value exactly.** This is the opposite finding from
`DNA_INDEX.json` (§3): the manifest was regenerated in the second repair
pass, the DNA index's `sentence_pacing`/`sync_relationships` blocks were not.

One unrelated data-quality note: `BRAIN_MANIFEST.json:6`,
`"project_root": "/Users/ghilmankhan/workprojects/video data of what if"` —
this path does not match the actual project location on this machine
(`/Users/ghilmanislam360/GhilmanProjects/video data of what if`), and the
username `ghilmankhan` also appears baked into `SOURCE_TO_FORENSIC_MAP.csv`'s
`FORENSIC_FOLDER` column for all 14 rows (e.g. row 2:
`/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/...`).
This is a portability/staleness issue (stale absolute paths from a prior
machine/user), not a count-accuracy issue.

---

## 8. Stale numbers in prose docs

Grepped `BRAIN_SUMMARY.md`, `VALIDATION_REPORT.md`, `CONTINUATION_HANDOFF.md`
for the old stale figures (141 sentences, 55.8 words/sentence, negative
duration, 581-as-total-sync-events) and for the current correct figures.

**Result: none of the three prose docs contain the old stale numbers.** All
three are fully up to date and internally consistent with the computed
counts in §3:

- `BRAIN_SUMMARY.md:24,30`: "604 meaningful sentences", "1,421 (581
  STATE_CHANGE, 438 MOTION_START, 402 MOTION_END)".
- `BRAIN_SUMMARY.md:40`: explicitly documents that `AUDIO_DNA.md`/`PACING_DNA.md`
  *used to* have "55.8 words/sentence, a negative-duration range" and were
  "fixed to the real 13.0 words/sentence, 140–11,620ms range" — i.e. the
  prose docs **describe** the old stale numbers as a historical defect that
  was fixed, rather than presenting them as current.
- `VALIDATION_REPORT.md:17,34,85-92`: "TOTAL_SENTENCE_ROWS = 604",
  "TOTAL_SYNC_ROWS = 1421", row-count summary matching §3 exactly.
- `CONTINUATION_HANDOFF.md:15-17`: "7,864 words, 604 meaningful sentences,
  438 motions, 581 states, 200 shots, 448 assets, 29 audio events, 1,421 A/V
  sync events (581 STATE_CHANGE + 438 MOTION_START + 402 MOTION_END)".

**Conclusion: the staleness identified in §3/§4 is isolated to
`DNA_INDEX.json` and `RECONSTRUCTION_INDEX.json`'s embedded copy of it.
Neither `BRAIN_SUMMARY.md`, `VALIDATION_REPORT.md`, `CONTINUATION_HANDOFF.md`,
nor the individual `02_production_dna/*.md` DNA docs (`PACING_DNA.md`,
`AUDIO_DNA.md`, etc.) retain the stale figures** — those were fixed in the
second repair pass; only the two JSON index files were missed.

---

## 9. validator/validate_brain.py summary

`validator/validate_brain.py` is a strict, from-disk integrity checker (no
cached/remembered values — every number is computed at run time from the
CSVs it loads). It performs, in order: (1) sentence validation — empty
meaningful-sentence text, missing/invalid `FIRST_WORD_ID`/`LAST_WORD_ID`,
`WORD_COUNT` vs actual linked-word count, negative sentence duration,
duplicate `(VIDEO_SLUG, WORD_ID)` keys; (2) foreign-key checks for
`MASTER_STATES`/`MASTER_SHOTS`'s `SHOT_ID`/`ASSET_IDS`/`MOTION_IDS`
references; (3) A/V sync event validation — allowed
`VISUAL_EVENT_TYPE`/`SYNC_RELATION` vocabularies, orphan
`MOTION_ID(S)`/`SHOT_ID`/`TARGET_SHOT_ID`/`SOURCE_STATE`/`TARGET_STATE`/
`SENTENCE_ID`/`WORD_ID`/`AUDIO_EVENT_ID` references, duplicate
`(VIDEO_SLUG, SYNC_ID)`; (4) motion start/end linkage completeness (every
motion has a `MOTION_START`; every non-instantaneous motion has a
`MOTION_END`); (5) direct `MASTER_MOTIONS` validation — FK resolution,
`DURATION_SEC` vs `END_SEC-START_SEC` arithmetic (±0.06s tolerance),
duplicate IDs; (6) direct `MASTER_SHOTS`/`MASTER_STATES` validation — state
duration arithmetic, state time-monotonicity within a shot, shot aggregate
fields (`STATE_COUNT`/`MOTION_COUNT`/`FIRST_STATE_ID`/`LAST_STATE_ID`)
recomputed and compared against stored values; (7) raw CSV width check (every
row has the header's exact column count, catching unquoted-comma corruption
`DictReader` would silently swallow); (8) a corpus-wide hard-timestamp rollup
(`END_SEC < START_SEC` or unparseable); (9) canonical-artifact presence/
non-triviality (>50 bytes) for the required file set; (10) a final row-count
summary (echoed as the computed §3 numbers).

**File paths it reads from:** exclusively `01_master_data/` — never the root
copies. `BRAIN = dirname(dirname(abspath(__file__)))` and
`MD = os.path.join(BRAIN, '01_master_data')` (lines 19-20); every `load()`
call and the width-check loop resolve through `MD`. Confirmed by actually
running it: `python3 validator/validate_brain.py` → `RESULT: PASS (all gates
report zero failures)`, with the row-count summary matching §3 exactly. This
directly answers §1: the validator is 01_master_data-only and would behave
identically if the root duplicates were deleted.

---

## 10. Full inventory + classification

```
production_intelligence_brain/
├── SOURCE_VIDEO_INDEX.csv                  CANONICAL
├── SOURCE_TO_FORENSIC_MAP.csv              CANONICAL (see note below)
├── 01_master_data/                         CANONICAL (all 8 files)
├── 02_production_dna/                      MIXED (see per-file table)
├── 03_reconstruction_system/                MIXED (see per-file table)
├── 04_patterns/                             MIXED (see per-file table)
├── 05_blueprints/                           CANONICAL (all 4, per validator's required-file list; content not deep-audited beyond grep)
├── validator/                               CANONICAL (both files)
├── testing/, legacy/                        CONFIRMED ABSENT (do not exist — matches contract)
├── BRAIN_MANIFEST.json                      CANONICAL — current, matches all computed counts (§7)
├── BRAIN_SUMMARY.md                         CANONICAL — current, no stale numbers (§8)
├── VALIDATION_REPORT.md                     CANONICAL — current, matches an actual validator run (§8, §9)
├── CONTINUATION_HANDOFF.md                  CANONICAL — current, most detailed repair log (§8)
├── BRAIN_MANIFEST_VALIDATED.json            DUPLICATE — byte-identical to BRAIN_MANIFEST.json, zero references anywhere (§2). NOT in canonical contract.
├── MASTER_ASSETS.csv (root)                 DUPLICATE — byte-identical to 01_master_data/ copy, unreferenced by any code path (§1). NOT in canonical contract.
├── MASTER_AUDIO_EVENTS.csv (root)           DUPLICATE — ditto
├── MASTER_AUDIO_VISUAL_SYNC.csv (root)      DUPLICATE — ditto
├── MASTER_MOTIONS.csv (root)                DUPLICATE — ditto
├── MASTER_SENTENCES.csv (root)              DUPLICATE — ditto
├── MASTER_SHOTS.csv (root)                  DUPLICATE — ditto
├── MASTER_STATES.csv (root)                 DUPLICATE — ditto
└── MASTER_WORDS.csv (root)                  DUPLICATE — ditto
```

### Per-file classification, `02_production_dna/`

| File | Classification | Reasoning |
|---|---|---|
| `ASSET_DNA.md` | CANONICAL | Regenerated from repaired `MASTER_ASSETS.csv` (448 rows) per its own header; no stale-number grep hits. |
| `AUDIO_DNA.md` | CANONICAL | Recomputed from rebuilt `MASTER_SENTENCES.csv` (604 sentences) per its own header. |
| `AUDIO_VISUAL_SYNC_DNA.md` | CANONICAL | Regenerated after enriching `MASTER_AUDIO_VISUAL_SYNC.csv`; explicitly notes the 1,421-row current schema. |
| `DNA_INDEX.json` | **STALE** | `sentence_pacing`/`sync_relationships` blocks retain pre-repair values (141 sentences, 55.8 words/sentence, -17260ms min duration, 581-as-total-sync) — see §3. |
| `EDITING_DNA.md` | CANONICAL | Regenerated from `MASTER_SHOTS.csv` (200 shots) per its own header. |
| `MOTION_DNA.md` | CANONICAL | Regenerated from repaired `MASTER_MOTIONS.csv` (438 motions) per its own header. |
| `PACING_DNA.md` | CANONICAL | Regenerated from `MASTER_SENTENCES.csv` (604 sentences); explicitly documents the prior 55.8/negative-duration figures as fixed. |
| `VISUAL_DNA.md` | CANONICAL | Regenerated from `MASTER_STATES.csv` (581 states) per its own header. |

### Per-file classification, `03_reconstruction_system/`

| File | Classification | Reasoning |
|---|---|---|
| `ASSET_CREATION_SYSTEM.md` | CANONICAL | Built from `01_master_data/MASTER_ASSETS.csv`; required by validator. |
| `CAPCUT_PRODUCTION_SYSTEM.md` | CANONICAL | Explicitly supersedes the legacy guide with measured-only claims; required by validator. |
| `CAPCUT_RECONSTRUCTION_GUIDE.md` | **SUPERSEDED / LEGACY** | Contains fabricated numeric specifics not supported by the schema; explicitly superseded by `CAPCUT_PRODUCTION_SYSTEM.md` (§5); not in validator's required list; not referenced as current anywhere. |
| `DECISION_RULES.md` | CANONICAL | Required by validator; referenced by other canonical docs (e.g. `CAPCUT_PRODUCTION_SYSTEM.md` §3). |
| `IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md` | **SUPERSEDED / LEGACY** | Same pattern as CapCut legacy guide — fabricated prompt templates/timing formulas; explicitly superseded (§5). |
| `IMAGE_TO_VIDEO_SYSTEM.md` | CANONICAL | Explicitly supersedes the legacy guide; required by validator. |
| `RECONSTRUCTION_INDEX.json` | **STALE (partial)** | Its own `systems`/`decision_criteria`/`constraints` blocks are current and don't reference the legacy guides (§4), but its embedded `dna_reference` block duplicates DNA_INDEX.json's stale figures verbatim (§4). |

### Per-file classification, `04_patterns/`

| File | Classification | Reasoning |
|---|---|---|
| `AUDIO_TRIGGER_PATTERNS.csv` | CANONICAL | 1,221 rows; required by validator; not flagged stale by any doc. |
| `MOTION_PATTERNS.csv` | CANONICAL | 438 rows (matches motion count); regenerated per `BRAIN_SUMMARY.md`. |
| `SHOT_PATTERNS.csv` | CANONICAL | 200 rows (matches shot count). |
| `STATE_PATTERNS.csv` | CANONICAL | 581 rows (matches state count). |
| `TRANSITION_PATTERNS.csv` | **UNKNOWN / placeholder-shaped** | 82 rows, `TYPICAL_DURATION_SEC` constant `0.000` across all rows; docs claim this is a genuine measured constant (§6), but the CSV alone can't be distinguished from an unrepaired placeholder — flagged for reviewer judgment, not a clear PASS. |
| `VISUAL_CHANGE_PATTERNS.csv` | CANONICAL (unaudited in depth) | Only 3 rows; not called out by name in any task item; not flagged stale by any doc; out of this audit's deep-dive scope. |

### Root-level / top-level extras not in the stated canonical contract

| Item | Classification | Reasoning |
|---|---|---|
| `BRAIN_MANIFEST_VALIDATED.json` | **DUPLICATE** | Byte-identical to `BRAIN_MANIFEST.json`, zero references anywhere (§2). |
| Root `MASTER_*.csv` (8 files) | **DUPLICATE** | Byte-identical to `01_master_data/` copies, unreferenced by any code path (§1). |

**Everything else matches the stated canonical contract exactly** — no other
unaccounted files were found (`find . -type f` enumerated all 49 files;
every one is listed above or in the contract).

---

## 11. Git repository check

Checked for `.git` at every level from the project root upward:
`/Users/ghilmanislam360/GhilmanProjects/video data of what if`,
`/Users/ghilmanislam360/GhilmanProjects`, `/Users/ghilmanislam360`, `/Users`.

**Result: PASS — not a git repository.** No `.git` directory found at the
project root or any ancestor directory. (Confirmed independently by the
session environment's own "Is a git repository: false" flag.) No repository
was initialized as part of this audit.

---

## Summary table: staleness verdicts

| Artifact | Verdict |
|---|---|
| Root `MASTER_*.csv` (8 files) | Exact duplicates, zero references, safe to delete |
| `BRAIN_MANIFEST_VALIDATED.json` | Exact duplicate, zero references, safe to delete |
| `BRAIN_MANIFEST.json` | **Current** — all 11 counts match computed values |
| `DNA_INDEX.json` | **Stale** — sentence_pacing + sync_relationships blocks (141 sentences, 55.8 w/s, -17260ms, 581-as-total-sync) |
| `RECONSTRUCTION_INDEX.json` | **Stale (partial)** — embeds the same stale dna_reference block; own systems/constraints content is current and doesn't cite legacy guides |
| `BRAIN_SUMMARY.md` / `VALIDATION_REPORT.md` / `CONTINUATION_HANDOFF.md` | **Current** — no stale figures found |
| `CAPCUT_RECONSTRUCTION_GUIDE.md` / `IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md` | Confirmed superseded, confirmed unreferenced as canonical |
| `TRANSITION_PATTERNS.csv` | Constant `0.000`/`shot_exit` across all 82 rows; docs claim genuine measurement, cannot be independently verified from the CSV alone |
| Git repository | Confirmed: not a git repo |
