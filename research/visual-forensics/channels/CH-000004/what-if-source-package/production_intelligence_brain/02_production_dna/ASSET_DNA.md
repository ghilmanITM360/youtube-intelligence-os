# ASSET DNA

Regenerated from the repaired `01_master_data/MASTER_ASSETS.csv` (448 asset rows,
rebuilt from the 14 per-video `02_analysis/ASSET_MANIFEST.csv` forensic files,
including 28 rows whose original CSVs had unquoted commas causing column shift;
each was hand-repaired against its raw positional fields — see
`validator/README.md` for the repair log). This document supersedes the prior
version, which stated "Total distinct assets: 0" against the corpus data and is
no longer accurate. Every number below is a real, computed count.

## Asset Inventory

- **Total asset rows:** 448 across 14 videos (min 11 in `worlds-largest-cities-what-if`, max 66 in `what-if-earth-grew-1cm-every-second`)
- **REUSE_STATUS populated:** 448/448 (0/448 in the prior aggregate)
- **MEDIA_FORMAT_NEEDED populated:** 448/448 (0/448 in the prior aggregate)
- **TRANSPARENT_BG populated:** 448/448 (0/448 in the prior aggregate)
- **SOURCE_OR_RECREATION_METHOD populated:** 448/448 (0/448 in the prior aggregate)

## Asset Types (canonical = raw TYPE, case/hyphen/space normalized only — no categories invented)

| Type | Count |
|---|---|
| GRAPHIC | 146 |
| ENVIRONMENT | 91 |
| OBJECT | 91 |
| CHARACTER | 50 |
| TEXT_SYSTEM | 31 |
| AUDIO | 13 |
| TEXT | 11 |
| OBJECT_GROUP | 6 |
| OBJECT/ILLUSTRATION | 4 |
| GRAPHIC_TEMPLATE | 1 |
| UI/HUD_ELEMENT | 1 |
| OBJECT/DETAIL | 1 |
| GRAPHIC/TEXT_SYSTEM | 1 |
| AUDIO_ELEMENT | 1 |

`GRAPHIC`, `ENVIRONMENT`, and `OBJECT` together account for 328/448 (73%) of all assets — the corpus is dominated by static illustrated elements, not characters or text.

## Reuse Pattern (measured, not assumed)

Raw `REUSE_STATUS` is free text (58 distinct strings), not an enum, so exact wording varies per per-video analyst pass. Top values by frequency:

| REUSE_STATUS (raw) | Count |
|---|---|
| UNIQUE | 58 |
| REUSED | 53 |
| RECURRING | 40 |
| SCENE_SPECIFIC | 39 |
| one scene | 32 |
| SINGLE-USE | 32 |
| SINGLE SHOT; internal variants reused | 31 |
| SINGLE_USE | 31 |
| REUSE | 29 |
| Recurring | 16 |

Reading these case-insensitively, values starting with UNIQUE/SINGLE/ONE SCENE/SCENE_SPECIFIC (i.e. not reused) account for roughly 210/448 rows, and values starting with REUSE/RECURRING/GLOBAL account for roughly 150/448 rows — reuse is common but **not** the dominant pattern the prior (fabricated) doc claimed ("high reuse across videos"); it is closer to an even split, skewing slightly toward single-use per-video assets.

## Media Format Needed (top raw values)

| MEDIA_FORMAT_NEEDED | Count |
|---|---|
| PNG | 173 |
| JPG | 36 |
| TEXT | 33 |
| SVG | 30 |
| PNG (TRANSPARENT) | 20 |
| AUDIO | 11 |
| PNG / TEXT | 10 |
| PNG OR VIDEO | 9 |
| JPG/PNG | 9 |

PNG-family values (`PNG`, `PNG (TRANSPARENT)`, `PNG / TEXT`, `PNG OR VIDEO`, `JPG/PNG`, etc.) cover the large majority of visual assets — consistent with transparent-overlay compositing being the dominant recreation format, not full-frame plates.

## Transparency

| TRANSPARENT_BG bucket (prefix-normalized) | Count |
|---|---|
| YES* | 258 |
| NO* | 139 |
| N/A / NA | 47 |
| OPTIONAL | 4 |

Roughly 58% of assets are transparent overlays; ~31% are full-frame/opaque backgrounds.

## Recreation Method

| SOURCE_OR_RECREATION_METHOD pattern | Count |
|---|---|
| Starts with "Recreate..." (explicit recreation instruction) | 225 |
| Other free-text guidance | 150 |
| References original SOURCE (audio track, etc.) | 48 |
| Explicitly mentions GENERATED_IMAGE | 25 |

## What is NOT supported by current data

- No per-asset pixel dimensions, color palette, or font family data exists anywhere in the corpus — any DNA claim about "consistent typography" or "consistent color coding" (as the prior fabricated version asserted) has no measurable support and is omitted here.
- `OTHER_APPEARANCES` is populated for most rows as shot/state ID lists (e.g. `F01.1-F01.2, F01.5-F01.22`), not a normalized count — cross-video asset reuse (the *same* asset appearing in more than one video) is not tracked anywhere in the schema; all reuse figures above are **within-video** reuse only.
