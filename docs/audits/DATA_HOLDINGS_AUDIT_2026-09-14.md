# YouTube Intelligence OS Data Holdings Audit

**Audit date:** 2026-09-14

**Repository baseline:** `a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8`

**Remediation commit reviewed:** `c024d13a8d41e7f6cc0958556036372ea1f2c158`

**Scope:** data already stored in this repository and its local ignored catalog; no new acquisition was run.

## Executive answer

The repository contains two distinct channel-data systems that must not be added together:

1. The historical canonical catalog covers `DS-000001` through `DS-000019`, with 5 canonical channels and 303 cataloged videos. Of those transcripts, 302 are real and 1 is an explicit unavailable-caption placeholder.
2. The newer channel-package layer covers `DS-000020` through `DS-000025`, with 35 channel packages and 1,601 unique videos. It contains 1,591 real transcripts and 10 explicit members-only placeholders. Fourteen videos have no description. No referenced package transcript file is missing.

The package layer has not been loaded into the historical 303-video SQLite catalog. The numbers `303` and `1,601` describe different populations and are not an independent-evidence total. Seven older screenshot datasets identify channel-like subjects but lack canonical channel IDs and video records. The claimed original 44-channel target list is not stored as a reproducible artifact, so target membership is reported as a qualified claim, not a repository-proven fact.

The exact per-channel ledger is [CHANNEL_COVERAGE_LEDGER_2026-09-14.csv](CHANNEL_COVERAGE_LEDGER_2026-09-14.csv).

## Evidence and method

This audit used repository files, manifests, package workbooks, transcript ZIPs, Git tracking state, and the local SQLite catalog. It did not use model memory as project evidence.

- All 35 package workbooks were opened read-only with the bundled Python/OpenPyXL runtime.
- Every package workbook contained the five expected sheets: `Channel Overview`, `All Videos`, `Descriptions`, `Verification`, and `Analysis`.
- All 35 transcript ZIPs passed CRC inspection. Workbook video IDs and transcript references were compared to ZIP members.
- Combined JSON/CSV/XLSX files were compared where present.
- Catalog table counts and channel/video/transcript records were queried directly from `data/catalog/youtube_inventory.db`.
- Dataset manifests and Git tracking/ignore state were checked independently.
- Facts below are separated from limitations and prior-audit claims.

## Population boundaries

| Population | Stored scope | Channels or channel-like subjects | Videos | Transcript state | Boundary |
| --- | ---: | ---: | ---: | --- | --- |
| Historical canonical catalog | DS-000001–DS-000019 | 5 canonical channels | 303 | 302 real; 1 explicit unavailable placeholder | Local ignored SQLite catalog plus historical raw/manifests |
| Historical screenshot-only evidence | DS-000003–DS-000005 and DS-000007–DS-000010 | 7 identity-incomplete subjects | Not derivable | Not available | Screenshot evidence, not channel/video rows |
| Channel-package layer | DS-000020–DS-000025 | 35 canonical YouTube IDs | 1,601 | 1,591 real; 10 explicit placeholders; 0 missing references | Tracked raw and extracted packages; not in SQLite catalog |
| Claimed original target list | External/prior-session claim | 44 unique targets from 47 ordered rows | Not applicable | Not applicable | Source list itself absent; exact reconciliation cannot be reproduced |
| Real first-party analytics | None ingested | 0 own channels | 0 | Not applicable | Only import contracts and synthetic tests exist |

The per-channel ledger has 47 evidence rows: 40 rows with canonical identities (5 historical plus 35 packages) and 7 screenshot-only subjects. That row count is not a unique-channel total across an externally defined target list.

## Repository storage map

| Layer | What is stored | Principal formats | Path | Git state | Limitation |
| --- | --- | --- | --- | --- | --- |
| Raw/source evidence, historical | Original workbooks, archives, transcripts, screenshots, forensic media/exports, and global knowledge corpora | XLSX, ZIP, TXT, PNG, JPG, JSON, CSV, TSV, PSV, PDF, DOCX, MD, SRT, M4A, WAV, source-code files | `data/raw/competitors/DS-*`, `data/raw/forensic-analysis/DS-*`, `data/raw/global-youtube-knowledge/DS-*` | Ignored local evidence; manifests tracked | Not portable in Git checkout; some catalog paths are absolute to the main worktree |
| Raw/source evidence, packages | Apify result JSON, user-supplied source artifacts, recovery output, and preflight records | JSON, XLSX, ZIP, TXT, PNG, MD | `data/raw/channel-data/DS-000020`–`DS-000025` | Tracked | DS-000022 lacks original actor run identifiers/raw for the supplied packages |
| Extracted package records | Per-channel master workbooks and transcript ZIPs; dataset-level combined exports where available | XLSX, ZIP/TXT, JSON, CSV, MD | `data/extracted/channel-data/DS-000020`–`DS-000025` | Tracked | DS-000022 has no dataset-level combined master; ten transcripts are explicit members-only placeholders |
| Normalized layer | Placeholder only | `.gitkeep` | `data/normalized/` | Tracked | No normalized production records are stored here |
| Canonical catalog | Dataset/file/run/channel/video/transcript/provenance/visual/document/classification metadata | SQLite | `data/catalog/youtube_inventory.db` | Ignored local artifact; README tracked | Covers DS-000001–DS-000019 only; two additional `.db` files are zero-byte placeholders |
| Dataset manifests | Provenance, file lists, source-artifact mappings, preflight and verification records | MD, CSV, JSON | `data/manifests/` | Tracked | A manifest describes evidence; it is not a substitute for absent raw files |
| Intelligence outputs | Topic, packaging, hook/script, editing/visual, strategy, comparisons, plans, system status, and global source analysis | JSON, MD | `data/intelligence/` | Tracked except a local `.DS_Store` | Derived interpretations; availability differs by channel |
| Templates | Reusable channel-package workbook | XLSX | `data/templates/youtube-channel-package-template.xlsx` | Tracked | Template, not evidence |
| Schemas | SQLite migrations and schema documentation | SQL, MD | `schemas/` | Tracked | Defines catalog contracts, not stored observations |
| Code | Ingestion, validation, reporting, orchestration, and utility programs | Python, shell | `scripts/` | Tracked | Executable logic, not evidence |
| Tests | Unit/integration contract tests and synthetic fixtures | Python, JSON/CSV fixtures | `tests/` | Tracked | Synthetic first-party analytics tests are not real analytics data |
| Documentation/reports | Architecture, workflows, status, source discovery, audits, and plans | MD, CSV | `docs/` | Mixed: canonical docs tracked; current audit files initially untracked | Reports may summarize mutable local state and must carry an audit date |
| Local generated artifacts | SQLite databases, Python caches, OS metadata, and audit-working files | DB, PYC, directories, DS_Store, MD/CSV | ignored paths and worktree-local untracked paths | Ignored or untracked | Machine-local; not durable until explicitly committed |

At audit time, the main data directories contained approximately 1,819 raw files (813 MB), 119 extracted files (108 MB), 1 normalized placeholder file, 67 intelligence files (8.6 MB, including an ignored `.DS_Store`), 71 manifest files (13 MB), and 4 catalog entries (46 MB). These filesystem populations overlap with archive members and catalog rows and therefore are not additive record counts.

## Historical datasets: DS-000001–DS-000019

| Dataset | Stored content | Registered physical/reference content | Formats represented | Canonical relationship and limitation |
| --- | --- | ---: | --- | --- |
| DS-000001 | Matty Invests and Mr. Finance workbook/transcript archive | 2 physical files; 160 archive members | XLSX, ZIP, TXT | CH-000001: 94 videos, 93 real transcripts and 1 explicit unavailable-caption placeholder. CH-000002: 65 videos/transcripts. Video type is not stored. |
| DS-000002 | One forensic video reconstruction package | 4 physical files; 2 visual assets, 4 observations | CSV, JPG, MD | Not linked to a canonical channel; cannot support per-channel counts. |
| DS-000003 | Doctor Thomas channel screenshots | 5 physical/visual files; 10 observations | PNG | Screenshot-only; handle, channel ID, videos, descriptions, and transcripts are not established. |
| DS-000004 | Dr. Adewale channel screenshots | 13 physical/visual files; 26 observations | PNG | Screenshot-only; canonical identity and video records unavailable. |
| DS-000005 | Dr. Okoro channel screenshots | 10 physical/visual files; 20 observations | PNG | Screenshot-only; canonical identity and video records unavailable. |
| DS-000006 | Dr. Aliza Wright structured channel records plus screenshots | 41 physical files; 7 visual assets; 64 classifications | PNG, JSON, TXT | CH-000003: 32 regular videos, descriptions, and real transcripts. |
| DS-000007 | Dr. Waterling channel screenshots | 13 physical/visual files; 26 observations | PNG | Screenshot-only; canonical identity and video records unavailable. |
| DS-000008 | The Senior Health Podcast screenshots | 37 physical/visual files; 74 observations | PNG | Screenshot-only; canonical identity and video records unavailable. |
| DS-000009 | Senior Health Hub screenshots | 24 physical/visual files; 48 observations | PNG | Screenshot-only; canonical identity and video records unavailable. |
| DS-000010 | The Health Educator screenshots | 11 physical/visual files; 22 observations | PNG | Screenshot-only; canonical identity and video records unavailable. |
| DS-000011 | Global strategy/training document corpus | 17 physical/document records | PDF, DOCX, MD | Global knowledge, not a channel dataset. |
| DS-000012 | xkcd forensic analysis export | 103 physical paths: 7 copied, 96 referenced; 96 visual assets | JPG, PNG, MD, Swift, TXT | Mapped to CH-000004. Reference-heavy and worktree-path-dependent. |
| DS-000013 | xkcd forensic analysis export | 1,422 paths: 63 copied, 1,359 referenced; 1,393 visual assets | CSV, JPG, JSON, M4A, MD, PNG, Python, Swift, TSV, TXT, WAV | Mapped to CH-000004. Reference-heavy. |
| DS-000014 | xkcd forensic analysis export | 798 paths: 54 copied, 744 referenced; 766 visual assets | JPG, JSON, M4A, MD, PNG, Python, TSV, TXT, WAV | Mapped to CH-000004. Reference-heavy. |
| DS-000015 | xkcd forensic analysis export | 2,520 paths: 50 copied, 2,470 referenced; 2,488 visual assets | CSV, JPG, JSON, M4A, MD, PNG, Python, Swift, TSV, TXT, WAV | Mapped to CH-000004. Overlaps DS-000012 source material; the registered relationship prevents treating them as independent evidence. |
| DS-000016 | Retiree daily-routines forensic export | 1,136 paths: 1,135 copied, 1 referenced; 307 visual assets | CSV, JPG, JSON, MD, PNG, PSV, Python, SRT, Swift, TXT, WAV | No canonical channel relationship; must not be assigned to a channel without new evidence. |
| DS-000017 | xkcd Apify channel acquisition | 85 physical files | JSON, TXT | CH-000004: 83 videos, 43 regular and 40 Shorts, all with descriptions and real transcripts. |
| DS-000018 | 2026 YouTube algorithm creator-claim corpus | 1 ZIP; 64 members (63 MD, 1 JSON) | ZIP, MD, JSON | Global, mixed-source and partly unverified creator claims; not channel evidence. |
| DS-000019 | Supplied Dr. Elias channel export | 31 physical files; 58 classifications | XLSX, TXT | CH-000005: 29 regular videos with descriptions and real transcripts. |

Historical raw paths are grouped under `data/raw/competitors/` (DS-000001, DS-000003–DS-000010, DS-000017, DS-000019), `data/raw/forensic-analysis/` (DS-000002, DS-000012–DS-000016), and `data/raw/global-youtube-knowledge/` (DS-000011, DS-000018). Their tracked manifests are `data/manifests/DS-000001.md` through `DS-000019.md` with associated snapshots where present.

## Local catalog contents and limits

The ignored local catalog `data/catalog/youtube_inventory.db` was 46 MB with SHA-256 `3751021d…` at audit time. It contained:

| Table | Rows | Meaning |
| --- | ---: | --- |
| `datasets` | 19 | DS-000001–DS-000019 dataset registrations |
| `ingestion_runs` | 23 | Historical ingestion/registration runs |
| `source_locations` | 22 | Source roots/locations |
| `source_files` | 6,497 | Registered source files and references |
| `discovered_files` | 45,774 | Discovery-time paths, including nested/reference populations |
| `channels` / `channel_snapshots` | 5 / 5 | Canonical historical channels and snapshots |
| `videos` / `video_snapshots` | 303 / 303 | Historical canonical video records and snapshots |
| `transcripts` | 303 | 302 real transcripts and 1 explicit placeholder |
| `field_provenance` | 5,372 | Field-level source links |
| `visual_assets` / `visual_observations` | 5,172 / 244 | Visual evidence registrations and observations |
| `document_records` | 17 | DS-000011 document corpus records |
| `content_classifications` | 604 | Registered content classifications |
| `entity_classifications` | 9 | Entity-level classifications |
| `dataset_relationships` | 1 | Proven DS-000012/DS-000015 relationship |
| `apify_source_runs` / `apify_result_records` | 2 / 115 | Historical structured acquisition metadata/records |
| `thumbnail_evidence` | 115 | Thumbnail evidence rows |

`data/catalog/youtube-intelligence-os.db` and `data/catalog/youtube_intelligence.db` are zero-byte local placeholders. All `data/catalog/*.db` files are ignored. Consequently, a clean Git checkout contains schema and manifest definitions but not a populated catalog.

## Channel-package layer: DS-000020–DS-000025

| Dataset | Channels | Videos | Regular | Shorts | Live | Descriptions | Real transcripts | Placeholders | Dataset-level exports | Principal raw evidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| DS-000020 | 5 | 132 | 118 | 14 | 0 | 118 | 132 | 0 | Combined JSON, CSV, XLSX and validation MD | Three Apify run directories under `data/raw/channel-data/DS-000020/apify/` |
| DS-000021 | 11 | 216 | 216 | 0 | 0 | 216 | 216 | 0 | Combined JSON, CSV, XLSX and validation MD | Apify run `hh3hyA9bbe6NWbzSh` |
| DS-000022 | 7 | 732 | 732 | 0 | 0 | 732 | 722 | 10 | No combined master; per-channel packages, source/canonical workbooks, overlap/validation records, and Lucas recovery JSON/CSV | User source artifacts plus Lucas recovery run `dmUFY1GHENjMdqsB9`; original actor raw absent |
| DS-000023 | 5 | 110 | 110 | 0 | 0 | 110 | 110 | 0 | Combined JSON, CSV, XLSX and validation MD | Apify run `YlTuIQD7ejSlxe2Ox` plus preflight evidence |
| DS-000024 | 4 | 178 | 178 | 0 | 0 | 178 | 178 | 0 | Combined JSON, CSV, XLSX and validation MD | Apify run `2ZEXd8nKLPegjIi8L` plus preflight evidence |
| DS-000025 | 3 | 233 | 233 | 0 | 0 | 233 | 233 | 0 | Combined JSON, CSV, XLSX and validation MD | Apify runs `HLqdr5AbPI0c1iYfN` and `fgU7aFRXEXiBF9qQJ` plus preflight evidence |
| **Package total** | **35** | **1,601** | **1,587** | **14** | **0** | **1,587** | **1,591** | **10** | — | — |

The 14 absent descriptions are one Apesthetic video and 13 Primate Economics Shorts. The 10 placeholders are Lucas Grant members-only videos. Those placeholders are present files with explicit status, not missing transcript files.

Each channel package directory under `data/extracted/channel-data/<dataset>/packages/<channel>/` contains one master XLSX workbook and one transcript ZIP. The workbooks store channel identity/overview, per-video metadata, descriptions, transcript filename/status, verification information, and analysis fields. Transcript text is stored as individual TXT members inside ZIP files. Package paths and raw evidence roots are listed row by row in the companion CSV.

DS-000020, DS-000021, DS-000023, DS-000024, and DS-000025 also contain dataset-level combined JSON/CSV/XLSX exports. DS-000022 deliberately remains a set of per-channel packages and supporting reconciliation artifacts; no combined dataset master is present.

Package video IDs were unique both within and across all 35 packages at audit time. This proves package-level identity uniqueness; it does not prove independence from every historical dataset or an absent external target list.

## Original 44-channel target list

No repository file contains the claimed original 47 ordered target rows or its deduplicated 44 unique channels. Therefore the repository cannot independently reproduce exact target membership, duplicate positions, missing-target identities, or a 44-row coverage percentage.

Prior local audit notes assert that the source had 47 ordered rows, 44 unique targets, 34 stored matches, 10 missing targets, and one stored non-target (`Tp Dossier`). Because the source list itself is absent, the companion CSV labels the 34 package matches `CLAIMED_YES_SOURCE_LIST_ABSENT`, Tp Dossier `CLAIMED_NO_SOURCE_LIST_ABSENT`, and all unrelated historical rows `NOT_PROVABLE_SOURCE_LIST_ABSENT`. These are provenance-qualified claims, not independently verified target facts.

To make this population auditable later, store the original list as immutable raw evidence with ordered rows, source URL/identifier, acquisition date, and a manifest. This audit does not create or infer that missing source.

## Intelligence outputs by canonical channel

| Canonical channel | Topic opportunity | Packaging | Hook/script | Editing/visual | Strategy | Unified plan | Material limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH-000001 Matty Invests | Available | Available, title-only | Available | `NOT_AVAILABLE` | Diagnosis plus finance benchmark | Available | No canonical thumbnail references; no timed transcript segments |
| CH-000002 Mr. Finance | Available | Available, title-only | Available | `NOT_AVAILABLE` | Diagnosis plus finance benchmark | Available | No canonical thumbnail references; no timed transcript segments |
| CH-000003 Dr. Aliza Wright | Available | Available | Available | `NOT_AVAILABLE` | Health benchmark participant | Available | Screenshot/structured evidence exists, but no registered forensic video evidence |
| CH-000004 xkcd's What If? | Available | Available | Available | Available | No channel diagnosis file | Available | Editing intelligence is limited to the registered forensic evidence; transcript positions are approximations where timing is absent |
| CH-000005 Dr. Elias Senior Health | Available | Available, including thumbnail annotations | Available | `NOT_AVAILABLE` | Diagnosis plus health benchmark | Available | No registered forensic video evidence; transcript positions are approximations where timing is absent |

Derived files live under `data/intelligence/channels/CH-000001` through `CH-000005`. Cross-channel comparisons and availability reports live under `data/intelligence/cross-channel/`; assembled content plans under `data/intelligence/plans/`; strategy blueprints under `data/intelligence/blueprints/`; system capability, freshness, training, calibration, and refresh-run records under `data/intelligence/system/`; and algorithm source analysis under `data/intelligence/global/`.

These outputs contain AI interpretations and heuristic conclusions derived from evidence. They are not raw observations. Cross-niche strategy calibration covers only two channels per niche; no heuristic has enough coverage to be called a robust cross-niche pattern. First-party analytics ingestion is implemented and tested with synthetic fixtures, but no real first-party export has been ingested.

## Code, tests, templates, and reports

At the audited baseline, the repository tracked 38 script files, 29 test-tree files (23 named `test_*.py`), 11 schema files, and 23 documentation files before adding this report. These populations include:

- Inventory/catalog creation, registration, verification, structured acquisition, package validation, intelligence reporting, and orchestration scripts under `scripts/`.
- SQLite schema migrations `schemas/inventory/001_initial.sql` through `010_supplied_channel_evidence.sql`.
- Unit/integration tests plus synthetic fixtures under `tests/`.
- The reusable XLSX package template under `data/templates/`.
- Architecture, data classification, workflow, database, security, phase, status, source-discovery, and audit documents under `docs/`.
- Reserved/minimal directories documented by `config/README.md`, `channels/README.md`, and `logs/README.md`.

These are implementation or explanatory artifacts. They must not be counted as channel evidence.

## Independent review of `c024d13`

**Decision:** `NECESSARY_AND_VALIDATED`.

The commit changes exactly five files:

- `scripts/inventory_catalog.py`
- `scripts/register_structured_source.py`
- `tests/test_first_party_analytics.py`
- `tests/test_inventory_catalog.py`
- `tests/test_register_structured_source.py`

It makes two production corrections and hardens their tests:

1. Inventory verification now accepts a null canonical path only when the record is legitimately uncopied, while explicitly rejecting a copied record with a null path.
2. Structured-source verification uses the exact provenance contract of each existing producer (`register_structured_source.py/1`, `apify_youtube_ingest.py/1`, and `register_supplied_channel.py/1`) instead of applying one incompatible global shape. Unknown producers and missing/extra provenance continue to fail.

It also removes an undeclared `pytest` dependency from the first-party analytics test module and exposes all 19 legacy function tests to standard-library `unittest` discovery.

### A/B result

| Behavior | Base `a22c8d2` | `c024d13` | Desired/result |
| --- | --- | --- | --- |
| Legitimately uncopied null canonical paths, DS-000012–DS-000016 | Crashes with `TypeError: Path(None)` | Accepted; verification completes | Accepted |
| Copied record with null canonical path | Crashes before a useful verdict | Explicit mismatch and failed verification | Rejected |
| DS-000006 producer agreement | 118.5% apparent coverage; failed manifest agreement | 100%; verified | Verified |
| DS-000017 producer agreement | 118.7% apparent coverage; failed manifest agreement | 100%; verified | Verified |
| DS-000019 producer agreement | 130.9% apparent coverage; failed manifest agreement | 100%; verified | Verified |
| Missing required provenance | Failed | Failed | Strictness preserved |
| Unexpected extra provenance | Not producer-aware | Failed (100.2%); explicit mismatch | Strictness strengthened |
| Unknown producer | Not producer-aware | Failed; coverage unavailable | Rejected |
| Existing DS-000001 producer contract | Valid | Valid at 100% | Unchanged |
| First-party analytics discovery | Module import error: undeclared `pytest` | 19 tests discovered and passed | All executed |
| Focused inventory tests | 8 passed | 10 passed | Passed |
| Focused structured-source tests | 17 passed | 19 passed | Passed |
| Clean mirrored full suite | 265 discovered; one import error | 287 passed | No regression |

The clean A/B environments contained the same ignored catalog and required ignored historical fixtures, with catalog paths relocated only inside the temporary copies. This separated code behavior from worktree-local missing-fixture and absolute-path effects. Negative databases were isolated temporary copies; canonical evidence was not modified.

`git show --check` and the committed diff check passed. The commit contains no raw-evidence changes and no unrelated files. A high-confidence credential-pattern scan of tracked content returned no matches. The commit is retained unamended.

## Known limits and safe interpretation

- Raw historical evidence and the populated catalog are ignored local state; Git alone cannot reproduce every historical verification.
- Historical catalog absolute paths can fail in another worktree even when the underlying data is valid.
- DS-000022 package provenance begins with user-supplied artifacts; original actor identifiers/raw are absent except for the Lucas recovery run.
- Spreadsheet cell length limits affect presentation of very long text in some workbooks; transcript ZIP TXT members remain the authoritative full transcript payload.
- Screenshot-only datasets do not establish channel handles, canonical IDs, or complete video populations.
- The package layer and historical catalog are separate; do not sum or deduplicate them without a registered cross-layer reconciliation.
- The absent original target list prevents exact 44-target coverage verification.
- Intelligence JSON/MD files contain derived interpretations. Their claims remain bounded by their cited source records and stated availability.
- No real first-party analytics export is stored.
- No DS-000026 work, Apify run, credit spend, `ui/v1` merge, or raw evidence mutation was performed for this audit.
