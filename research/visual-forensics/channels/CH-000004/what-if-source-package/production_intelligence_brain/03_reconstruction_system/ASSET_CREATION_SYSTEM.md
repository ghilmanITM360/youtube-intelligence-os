# Asset Creation System

Built strictly from `01_master_data/MASTER_ASSETS.csv` (448 asset rows, rebuilt
from the 14 per-video `02_analysis/ASSET_MANIFEST.csv` forensic files — see
`validator/README.md` for the repair log of 28 rows that had unquoted-comma
column shift in their source CSVs). This document did not exist previously
because the aggregate `MASTER_ASSETS.csv` in use at the time had every
relevant column (`REUSE_STATUS`, `MEDIA_FORMAT_NEEDED`, `TRANSPARENT_BG`,
`SOURCE_OR_RECREATION_METHOD`) empty or uniformly `UNKNOWN` for all 351 rows —
there was no real signal to build creation rules from. The rebuilt table has
all four columns populated for all 448 rows, so this document is now written
from real, evidence-backed distributions, per type.

## By Asset Type

### GRAPHIC (n=146, 33% of corpus)
- Format: PNG (42), SVG (16), PNG (TRANSPARENT) (13), remainder split across PNG/JPG variants
- Transparency: 111 YES / 32 NO / 3 other
- **Rule:** default to a transparent PNG overlay unless the manifest explicitly says opaque/full-frame.

### ENVIRONMENT (n=91, 20%)
- Format: JPG (36), PNG (18), SVG (10)
- Transparency: 80 NO / 11 YES
- **Rule:** environments are overwhelmingly full-frame opaque plates (88% NO), not overlays — recreate as a background plate, not a transparent element.

### OBJECT (n=91, 20%)
- Format: PNG (72), SVG or PNG (6), PNG variants (4)
- Transparency: 71 YES / 20 NO
- **Rule:** default to transparent PNG (78% of objects).

### CHARACTER (n=50, 11%)
- Format: PNG (41), PNG (TRANSPARENT) (4), PNG variants (3)
- Transparency: 48 YES / 2 NO
- **Rule:** characters are almost always (96%) transparent PNG cutouts — matches the corpus's recurring stick-figure illustration style documented in `02_production_dna/ASSET_DNA.md`.

### TEXT_SYSTEM (n=31, 7%)
- Format: TEXT (14), TEXT (editor overlay) (4), CapCut native text layer (2), remainder mixed
- **Rule:** recreate as native editor text layers/style presets, not baked-in images, wherever the manifest says `TEXT` or `CapCut native text layer` (18/31 rows).

### AUDIO (n=13, 3%) and TEXT (n=11, 2%)
- AUDIO rows are the per-video full-mix audio track reference (not separable into stems per the source manifests — do not fabricate a stem split).
- TEXT rows (distinct from TEXT_SYSTEM) are single caption/label instances rather than a reusable style system.

## Recreation Method (corpus-wide, n=448)

| Pattern in SOURCE_OR_RECREATION_METHOD | Count |
|---|---|
| Explicit "Recreate..." instruction | 231 |
| References original SOURCE (e.g. audio track) | 48 |
| Explicitly GENERATED_IMAGE | 25 |
| Explicit TEXT OVERLAY | 11 |
| Other free-text guidance | 133 |

Most assets (52%) carry an explicit per-asset recreation instruction written by the original forensic pass — use that instruction verbatim where present rather than inferring a generic rule; only fall back to the type-level defaults above when `SOURCE_OR_RECREATION_METHOD` is generic or absent.

## What is NOT supported by current data

- No pixel dimensions, color values, or font names exist anywhere in the schema for any asset — recreation must reference the per-video `DESCRIPTION` field and, where needed, the source frame evidence (`01_evidence/frames/`), not this table alone.
- `REUSE_STATUS` is free text (58 distinct raw strings; see `ASSET_DNA.md`) rather than a boolean — do not treat any single asset's reuse status as certain beyond what its literal text says.
- Cross-video asset reuse (the same illustrated asset appearing in more than one of the 14 videos) is not tracked by this schema; all reuse figures are within-video only.
