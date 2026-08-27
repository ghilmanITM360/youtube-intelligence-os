# Source Duplicate Report

SHA-256-backed duplicate and revision analysis across the four Phase 0.5 source folders and their immediately adjacent zip-archive variants in `~/Downloads`. No duplicate was deleted, merged, or otherwise acted on — this is a report only, per the Phase 0.5 read-only rule.

## Method

`shasum -a 256` was computed for every file inside all four target folders, plus every adjacent zip file whose name pattern suggested a relationship to one of the four (see `SOURCE_DISCOVERY_REPORT.md`, Source Paths). For zip archives, both whole-archive hashes and (where feasible) `unzip -l` member-size listings were used, since a zip's own hash changes with compression metadata/timestamps even when its extracted content is identical — member sizes are the more reliable signal for archive-vs-folder comparison.

## Exact duplicate files (byte-identical, confirmed by SHA-256)

### Within `files (1)` ≡ `files` (folder-level, all 4 members)

| File | SHA-256 |
|---|---|
| `EDL_216_shots.csv` | `e0aa029066b316cb8b3f6540ff04abceb43cb153704167fe6e1e101b4f0bd1c5` |
| `EVIDENCE_seven_title_cards.jpg` | `510df44a064fa5b7c48407ce5a0e313f05c6e86fdcd53d6a7b62e5c5cfc9e2b9` |
| `EVIDENCE_temporal_average.jpg` | `44d8e3e470d04963ff031316184441a262782a03c76b10a513643bdee1907ec9` |
| `FORENSIC_RECONSTRUCTION.md` | `a536eaba06df7acd44d6178892a7df68b4ea126e9d7c9e9ef275bedd293b5af8` |

**Classification: EXACT_DUPLICATE.** The entire `files` folder is a byte-identical copy of `files (1)`. `docs/source-discovery/SOURCE_DATASET_INVENTORY.md` treats these as a single logical dataset (DISC-001).

### Adjacent zip archives, whole-file hash

| File | SHA-256 | Group |
|---|---|---|
| `files.zip` | `315ac31efd64389546fb9bbe757530c536e63ab70bcfe3d9c5c32d89025009f8` | A |
| `files (1).zip` | `315ac31efd64389546fb9bbe757530c536e63ab70bcfe3d9c5c32d89025009f8` | A |
| `files (2).zip` | `9e3e6d1c974c1df942b0de40a310cde0296e3a768f6b1d1dae590d6a3dbc0f78` | B |
| `files (1)fulldata.zip` | `9e3e6d1c974c1df942b0de40a310cde0296e3a768f6b1d1dae590d6a3dbc0f78` | B |
| `files (1)fulldata (1).zip` | `9e3e6d1c974c1df942b0de40a310cde0296e3a768f6b1d1dae590d6a3dbc0f78` | B |

**Group A — EXACT_DUPLICATE.** `files.zip` and `files (1).zip` are byte-identical to each other (same whole-archive hash).

**Group B — EXACT_DUPLICATE.** `files (2).zip`, `files (1)fulldata.zip`, and `files (1)fulldata (1).zip` are byte-identical to each other (same whole-archive hash).

## Archive → extracted-folder relationships

| Archive | Target folder | Evidence | Confidence |
|---|---|---|---|
| `files.zip` / `files (1).zip` (Group A) | `files (1)` / `files` (DISC-001) | `unzip -l` shows all 4 members with uncompressed sizes exactly matching the folder's 4 files (64,242 / 38,594 / 140,065 / 458,504 bytes) | **Confirmed** (size-exact on every member) |
| `files (2).zip` / `files (1)fulldata.zip` / `files (1)fulldata (1).zip` (Group B) | `files (1)fulldata (1)` (DISC-002) | Matching name pattern and comparable total size (1.6 MB archive vs. 1.6 MB folder, consistent with a folder whose contents — an xlsx and a zip — are already compressed and don't shrink further) | **Probable**, not member-size-verified |
| `all training data of youtube 2.zip` | `all training data of youtube` (DISC-003) | `unzip -l` lists the same 15 real filenames (plus `__MACOSX` noise); at least two match the folder's file sizes exactly (`Hook guide.pdf` 682,682 bytes both places; `Hook (1).pdf` 682,676 bytes both places) | **High**, not every one of the 15 members size-checked |
| `Dr. Adewale.zip` | `Dr. Adewale` (DISC-004) | `unzip -l` lists 13 screenshot entries (plus `__MACOSX` noise); several sizes match the folder's files exactly (e.g. 5,700,829 and 5,880,720 bytes) | **High**, not every one of the 13 members size-checked |

None of these four archives were extracted over or beside their originals; comparisons used listing (`unzip -l`) only, or extraction into the session scratchpad for the xlsx internals (never touching the original file).

## Probable duplicates / revisions (not byte-identical, not confirmed distinct content)

| File A | File B | Sizes | SHA-256 A | SHA-256 B | Assessment |
|---|---|---|---|---|---|
| `all training data of youtube/Hook (1).pdf` | `all training data of youtube/Hook guide.pdf` | 682,676 B / 682,682 B (6-byte difference) | `4129b210dba81ecb527d42730e3ed7458e68feb7b0d921c82baaa3d6a6e433e9` | `4bbe6c6e34b2279aacbd584e26c4ce8e6155eaba1e4193387f8a1a1161ee3c54` | **PROBABLE_DUPLICATE or REVISION** — near-identical size strongly suggests the same underlying content (likely re-exported from the same source with a trivial difference, e.g. a metadata timestamp or single edit). Content was not diffed line-by-line in this pass. Do not assume either is authoritative without further comparison. |

No other near-duplicate size pairs were found among the sampled/hashed files.

## Cross-folder duplicates

No file content was found duplicated **across** DISC-001, DISC-002, DISC-003, and DISC-004 with each other (i.e., no file inside `files (1)` matches any file inside `all training data of youtube`, etc.). The only cross-file relationships found are the archive↔folder pairs above, each of which stays within one Discovery ID's own content, plus the intra-folder `Hook (1).pdf`/`Hook guide.pdf` pair.

## Related-but-not-duplicate material

- DISC-001 (`files (1)`) and DISC-002 (`files (1)fulldata (1)`) share a naming lineage (`files (1)` → `files (1)fulldata (1)`, suggesting they were downloaded/exported in the same session or from the same tool run) but contain **unrelated subject matter** — DISC-001 is a single-video forensic teardown, DISC-002 is two channels' full metadata/transcripts. They are not evidence of the same underlying dataset.
- DISC-003's `Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf` and `Engine-by-Engine Personality & Lens (Cinematic-Psychological Profiles).docx.pdf` are plausibly companion documents by naming convention ("Engine" terminology in both) but this was not confirmed by content comparison — the second document was not read in this pass.

## What was not attempted

- Byte-for-byte member verification of every file inside Group B, `all training data of youtube 2.zip`, and `Dr. Adewale.zip` against their target folders (only size-listing spot checks were done).
- A textual diff of `Hook (1).pdf` vs. `Hook guide.pdf` to characterize what actually changed between them.
- Perceptual/near-duplicate image hashing across the `Dr. Adewale` screenshots or the two DISC-001 evidence JPGs (only cryptographic SHA-256 was computed; two visually similar but non-identical images would not be caught by this method).
