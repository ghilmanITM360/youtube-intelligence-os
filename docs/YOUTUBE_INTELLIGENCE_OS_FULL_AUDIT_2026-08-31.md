# YouTube Intelligence OS — Full Read-Only Audit

**Audit date:** 2026-08-31  
**Repository:** `/Users/ghilmanislam360/Documents/youtube-intelligence-os`  
**Audit status:** **PARTIAL**  
**Overall current readiness:** **49/100** against the intended end-state YouTube Intelligence OS  
**Current authorized phase:** **Phase 1D — Controlled Apify YouTube Acquisition, COMPLETE. Phase 2 is pending explicit authorization and has not begun.**

## 1. Executive summary

YouTube Intelligence OS is currently a strong, local, evidence-preserving acquisition and catalog foundation, not yet a complete intelligence operating system. It can safely inventory supplied folders, hash every ordinary file, detect exact duplicates, preserve raw evidence, register datasets and canonical YouTube identities, store one point-in-time set of channel/video metrics, reference transcripts and thumbnails, link selected forensic evidence to canonical videos, and produce three read-only status reports. Its bounded Apify adapter has two registered historical runs and enforces identity and cost controls.

The live catalog is healthy: schema v6, 25 tables, 17 datasets, 4 canonical channels, 274 content items, 273 available transcripts, 1 unavailable transcript, `PRAGMA integrity_check = ok`, and 0 foreign-key violations. The test suite passed all 56 tests with no skips. Git `main`, local `HEAD`, and the live remote `main` all resolve to `f0139efead2a6e75dea1fd4dc14715a0b121b4b2`.

The system is only partially ready relative to its long-term purpose. It has no production competitor benchmarking, script/hook/title/thumbnail intelligence, editing-style classification, cross-channel intelligence, opportunity engine, web-validation loop, recommendation pipeline, automated refresh, scheduler, RAG/vector database, MCP-driven production workflow, or frontend/dashboard. The one xkcd content-performance intelligence artifact is a careful proof of analytical work, but it is a single untracked Markdown artifact rather than a repeatable intelligence pipeline.

The highest-priority audit issues are documentation drift, incomplete direct source-file linkage for legacy structured provenance, seven demonstrably incorrect screenshot-count provenance locators, absence of real longitudinal snapshots, incomplete durable retention of the Dr. Aliza raw Actor result payload, and broad incompleteness of the intelligence/automation layers. No issue was repaired during this audit.

### Verified top-line state

| Measure | Current verified value |
|---|---:|
| Datasets | 17 |
| Canonical channels | 4 |
| Videos/content items | 274 |
| Regular videos | 75 |
| Shorts | 40 |
| Streams | 0 |
| Unknown legacy content type | 159 |
| Transcripts available | 273 |
| Transcripts unavailable | 1 |
| Reconstruction/forensic-labeled datasets | 6 |
| Registered frame-sequence forensic-video datasets | 5 |
| Intelligence artifacts | 1, untracked |
| SQLite schema version | 6 |
| SQLite tables | 25 |
| SQLite size | 47,157,248 bytes (about 45 MiB) |
| Tests | 56 passed, 0 failed, 0 skipped |

The handoff called the forensic dataset count 6. That remains a useful corpus count, but it requires a precision note: `DS-000002` is a forensic reconstruction dataset with two screenshots and no registered frame sequence; the five true registered frame-sequence forensic-video datasets are `DS-000012`–`DS-000016`.

## 2. What the system is intended to solve

The intended system turns heterogeneous YouTube evidence into reusable, channel-separated intelligence while preserving the difference between source facts, measurements, observations, AI interpretations, hypotheses, and recommendations. Its planned flow is:

```text
USER-SUPPLIED EVIDENCE
→ DISCOVERY / INVENTORY / HASHING / DEDUPLICATION
→ CLASSIFICATION
→ EXTRACTION / NORMALIZATION
→ REUSABLE INTELLIGENCE
→ CHANNEL-SPECIFIC INTELLIGENCE
→ COMPETITOR BENCHMARKING
→ PATTERN / OUTLIER / GAP DISCOVERY
→ TOPIC HYPOTHESES
→ WEB VALIDATION
→ FINAL OPPORTUNITIES
→ TITLE / THUMBNAIL / SCRIPT / VISUAL DEVELOPMENT
→ CONTINUOUS LEARNING
```

The problem is not merely to collect YouTube data. It is to make later conclusions auditable: any important value or conclusion should be traceable back to immutable source evidence, and channel-specific knowledge must not leak into another channel's intelligence.

## 3. Audit scope, method, and boundaries

This was a continuation of an interrupted read-only audit. The handoff was accepted after a fast verification of repository identity, Git, database health/counts, artifact inventory, and current phase. Expensive recursive raw-corpus analysis was not repeated.

Evidence used:

- Live SQLite queries against `data/catalog/youtube_inventory.db`.
- Existing manifests, schema migrations, reporting scripts, tests, documentation, and the untracked intelligence artifact.
- JSON output from all three read-only reports in this continuation.
- Prior handoff evidence that all three reports also ran successfully in Markdown mode.
- One fresh full test-suite run.
- Redacted security scans that emitted only `PRESENT` or `NOT PRESENT`.
- A live read-only `git ls-remote` check of remote `main`.

Not performed:

- No Apify Actor call.
- No web scrape or competitor refresh.
- No SQLite mutation.
- No raw-evidence modification.
- No new competitor/video analysis.
- No issue remediation.
- No Phase 2 work.
- No commit or push.

## 4. Current project phase

The authoritative current phase is **Phase 1D complete**. This is supported by `AGENTS.md`, `docs/Phases.md`, schema v6, the Apify adapter, two registered source runs, and the current catalog.

**Phase 2 — Data Classification & Provenance is next, but it requires explicit authorization.** It did not begin as part of this audit.

Documentation is not fully synchronized:

- `AGENTS.md` and `docs/Phases.md` correctly state Phase 1D complete.
- `docs/Architecture.md` correctly describes schema v6 and Phase 1D capability.
- `README.md` still says Phase 1C is current.
- `docs/PROJECT_SCOPE.md` still describes a Phase 1 scope with no scraper, which predates the Decision 018 Apify exception.
- `docs/DATA_INVENTORY.md` lists only `DS-000001`–`DS-000016`, omitting `DS-000017`, and its opening text still says no database is being introduced even though the rest of the file describes SQLite.

## 5. Current architecture

### Implemented architecture

```text
External/user-supplied folders or explicitly authorized Apify result
        ↓
Read-only discovery / validation
        ↓
SHA-256 inventory + explicit per-item disposition
        ↓
Immutable local raw evidence (`data/raw/`, ignored by default)
        ↓
Durable Markdown/JSON manifests (`data/manifests/`)
        ↓
Local SQLite inventory/catalog, schema v6 (`data/catalog/youtube_inventory.db`)
        ↓
Read-only status reports
        ↓
One manual, channel-scoped intelligence artifact
```

The repository stores code, schemas, tests, manifests, and documentation. Raw evidence and the operational SQLite database are local and ignored by Git. Raw files remain authoritative; manifests are the durable ingestion record; SQLite is the queryable index.

### Architectural strengths

- Raw, derived, and intelligence layers are conceptually separated.
- Raw evidence is immutable and SHA-256 anchored.
- Mutable YouTube metrics are separated from stable identities using append-only snapshot tables.
- Dataset, channel, video, transcript, visual, and source-run identities are explicit.
- Foreign keys and uniqueness constraints enforce key relationships.
- Multi-channel identities are separate and no duplicate YouTube video ID crosses channels.
- Apify is a narrow exception with bounded inputs, cost validation, identity reconciliation, sanitized run metadata, and field provenance.
- External tools and memory systems are explicitly non-authoritative.

### Architectural limits

- SQLite is a Phase 1 catalog, not a final intelligence store.
- The raw/manifests/database reconstruction story is not completely automatic: OCR and AI visual observations would need to be rerun to fully rebuild all catalog rows.
- No production intelligence entity model has been implemented for insights, competitors, topic clusters, opportunities, scripts, experiments, or agent runs.
- No job orchestration, scheduler, service API, frontend, or operational monitoring exists.
- The snapshot schema is structurally append-only, but the corpus contains only one observation per channel and per video.

## 6. Repository structure

| Path | Current role | State |
|---|---|---|
| `AGENTS.md` | Canonical operating rules and phase boundary | Current |
| `README.md` | Repository overview | Phase statement stale |
| `docs/` | Architecture, phases, decisions, security, workflows, audit/reporting docs | Broad and useful; some drift |
| `schemas/inventory/` | Six additive SQLite migrations | Implemented and tested |
| `scripts/` | Ingestion, registration, image/OCR loading, Apify, and reporting tools | Implemented |
| `tests/` | Stdlib `unittest` coverage with offline fixtures | 56/56 passing |
| `data/raw/` | Immutable local source evidence | Local/ignored; present |
| `data/manifests/` | Durable dataset/batch/Apify provenance records | Present; inventory index drift for DS-000017 |
| `data/catalog/` | Local operational SQLite catalog | Schema v6, healthy, ignored |
| `data/extracted/` | Future/direct extraction layer | No meaningful production corpus audited |
| `data/normalized/` | Future normalized layer | No meaningful production corpus audited |
| `data/intelligence/` | Derived intelligence | One untracked xkcd artifact |
| `channels/` | Planned separated channel workspaces | No formal channel workspace yet |
| `.codex/skills/` | Project workflow skills | Multimodal ingestion + Graphify skill installed |
| `config/` | Reserved configuration | Placeholder documentation only |
| `logs/` | Operational logs | Placeholder; no scheduler/service logging |

## 7. Documentation and architectural decisions

The documentation suite establishes a coherent evidence-first design, a phased roadmap, a local-database exception, security boundaries, error classes, prompt requirements, and source-ingestion rules. The decision log contains 18 accepted decisions:

| Decision | Effect |
|---|---|
| 001 | No YouTube API in the competitor-data workflow unless explicitly changed |
| 002 | Model/agent memory is auxiliary, never authoritative |
| 003 | Raw evidence is immutable |
| 004 | Derive final architecture from real datasets |
| 005 | No premature Phase 1 infrastructure |
| 006 | Keep multiple channels separated |
| 007 | Analyze internal competitor evidence before web validation |
| 008 | Use an iterative internal-analysis → web-validation opportunity loop |
| 009 | This repository path is canonical |
| 010 | External folders are valid read-only discovery inputs |
| 011 | Scrapling is external research tooling, not architecture |
| 012 | SQLite is the Phase 1 local inventory/catalog |
| 013 | Raw payloads and runtime DB remain local by default |
| 014 | Mutable platform metrics are append-only snapshots |
| 015 | Structured fields require source provenance |
| 016 | Content domain and editing style are independent |
| 017 | The private GitHub repository is the canonical remote |
| 018 | Controlled, cost-bounded Apify acquisition is the narrow Phase 1D exception |

The decisions are directionally sound. The main audit problem is not the design intent; it is drift between current facts and several older overview/discovery documents.

## 8. Dataset inventory

### A. Mandatory dataset table

| Dataset ID | Name | Semantic class | Evidence/source type | Associated channel/video | Status | Important relationships |
|---|---|---|---|---|---|---|
| `DS-000001` | Matty Invests & Mr. Finance Competitor Dataset | B — Competitor Evidence | Supplied XLSX + transcript ZIP; controlled external-folder copy | `CH-000001` Matty Invests; `CH-000002` Mr. Finance; 159 items | `STRUCTURED_REGISTERED` | Created both canonical channels; legacy workbook/transcript provenance |
| `DS-000002` | “7 Things Wealthy Retirees Stopped Buying to Stay Rich” — Forensic Video Reconstruction | C — Forensic Video Intelligence | External-folder copy; 2 screenshots | No canonical channel/video link | `INGESTED` | Forensic-labeled, but no registered frame sequence; finance classification |
| `DS-000003` | Doctor Thomas — Competitor Channel Screenshots | B | 5 screenshots | Dataset-only competitor label | `INGESTED` | Only screenshot competitor with populated packaging-style aggregate |
| `DS-000004` | Dr. Adewale — Competitor Channel Screenshots | B | 13 screenshots | Dataset-only competitor label | `INGESTED` | One of seven incorrect screenshot-count provenance locators |
| `DS-000005` | Dr. Okoro — Competitor Channel Screenshots | B | 10 screenshots | Dataset-only competitor label | `INGESTED` | One of seven incorrect screenshot-count provenance locators |
| `DS-000006` | Dr. Aliza Wright / Advice — Competitor Channel Screenshots | B | 7 screenshots + historical Apify structured acquisition | `CH-000003`; 32 regular videos | `STRUCTURED_REGISTERED` | Exact-handle Tier B→Tier A reconciliation; raw Actor result payload not retained locally |
| `DS-000007` | Dr. Waterling — Competitor Channel Screenshots | B | 13 screenshots | Dataset-only competitor label | `INGESTED` | One of seven incorrect screenshot-count provenance locators |
| `DS-000008` | The Senior Health Podcast — Competitor Channel Screenshots | B | 37 screenshots | Dataset-only competitor label | `INGESTED` | One of seven incorrect screenshot-count provenance locators |
| `DS-000009` | Senior Health Hub — Competitor Channel Screenshots | B | 24 screenshots | Dataset-only competitor label | `INGESTED` | One of seven incorrect screenshot-count provenance locators |
| `DS-000010` | The Health Educator — Competitor Channel Screenshots | B | 11 screenshots | Dataset-only competitor label | `INGESTED` | One of seven incorrect screenshot-count provenance locators |
| `DS-000011` | All Training Data of YouTube — Global Knowledge Corpus | A — Global YouTube Knowledge | 17 fully read documents | Global, not channel-specific | `INGESTED` | Hook PDF pair proven textually identical in catalog notes; older discovery docs still call it unresolved |
| `DS-000012` | Sunset Video Forensic Reconstruction — Case 1 | C | 96 video frames; 60 visual-state clusters | `CH-000004`; video `rGZ6TsXvi8E` | `INGESTED` | Proven xkcd relationship; same source video as DS-000015 |
| `DS-000013` | Moon/Electron Physics Video Forensic Reconstruction | C | 1,393 frames; 107 clusters | `CH-000004`; video `mEUqVgGf4e0` | `INGESTED` | Proven xkcd relationship |
| `DS-000014` | “Weird and Worrying Questions” Video Forensic Reconstruction | C | 766 frames; 117 clusters | `CH-000004`; video `SLd4hnmeW_g` | `INGESTED` | Proven xkcd relationship |
| `DS-000015` | Sunset Video Forensic Reconstruction — Case 2 | C | 2,488 frames; 101 clusters | `CH-000004`; video `rGZ6TsXvi8E` | `INGESTED` | Proven xkcd relationship; second analysis pass over same video as DS-000012; revision relation not formalized |
| `DS-000016` | Retiree Daily-Routines Video Forensic Reconstruction | C | 307 frames; 307 clusters | No canonical channel/video link | `INGESTED` | Real editing/frame evidence but no canonical YouTube identity link |
| `DS-000017` | xkcd's What If? — Apify Channel Acquisition | B | Historical Apify raw result JSON + 83 transcript files | `CH-000004`; 83 content items | `STRUCTURED_REGISTERED` | Exact requested/returned handle; 4 proven forensic-dataset links covering 3 videos |

Dataset status totals: 14 `INGESTED`, 3 `STRUCTURED_REGISTERED`. The `datasets.semantic_class` field exists for all 17, but only 9 have `entity_classifications` rows; 8 remain unclassified at the richer entity-classification layer.

## 9. Canonical channels

### B. Mandatory channel table

| Internal ID | Name | Handle | YouTube Channel ID | Datasets | Tier | Content domain | Videos | Regular | Shorts | Streams | Transcripts available | Transcripts unavailable | Packaging evidence | Editing evidence | Latest snapshot | Acquisition source |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
| `CH-000001` | Matty Invests | `@MattyInvests` | `UCkqzov98m_7niJOXwbRQgBA` | `DS-000001` | A — registered | Unclassified | 94 | 0 known | 0 known | 0 known | 93 | 1 | None registered | None registered | `2026-08-24` | Supplied workbook + transcript archive |
| `CH-000002` | Mr. Finance | `@misterfinanceyt` | `UC6AwWrRKNrwt83CMJqeTUzw` | `DS-000001` | A — registered | Unclassified | 65 | 0 known | 0 known | 0 known | 65 | 0 | None registered | None registered | `2026-08-24` | Supplied workbook + transcript archive |
| `CH-000003` | Dr. Aliza Wright \| Advice | `@Dr.AlizaWrightAdvice` | `UCXZi5JVeuTluazF-fYqQgNA` | `DS-000006` | A — registered | Health | 32 | 32 | 0 | 0 | 32 | 0 | 7 screenshots + 32 thumbnail URL refs; packaging style not classified | None; style `UNKNOWN` | `2026-08-28T12:06:34.708Z` | Screenshots + Apify run `bD7JBsuj7LK5Wt2rk` |
| `CH-000004` | xkcd's What If? | `@xkcd_whatif` | `UC6IxnFzHofFJ5X2PycSMsww` | `DS-000012`–`DS-000015`, `DS-000017` | A — registered | Unclassified | 83 | 43 | 40 | 0 | 83 | 0 | 83 thumbnail URL refs; no screenshot packaging classification | Exists for 3 videos through 4 forensic datasets; style `UNKNOWN` | `2026-08-28T13:16:30.020Z` | Apify run `mzl5dCHF81LbcBamS` + linked forensic evidence |

The 159 legacy `DS-000001` rows have `video_type = NULL`; they must not be retroactively reported as regular videos without evidence. The system therefore reports them as unknown content type.

## 10. Non-canonical, dataset-only competitor evidence

Seven competitor labels have screenshot evidence but no canonical `channels` row. These are Tier B evidence labels, not proven channel identities, and must not be merged by name alone.

| Dataset | Dataset-only competitor label | Screenshots | Transcripts/videos | Packaging-style classification | Editing-style classification |
|---|---|---:|---|---|---|
| `DS-000003` | Doctor Thomas | 5 | None | Present | `UNKNOWN` |
| `DS-000004` | Dr. Adewale | 13 | None | Missing | `UNKNOWN` |
| `DS-000005` | Dr. Okoro | 10 | None | Missing | `UNKNOWN` |
| `DS-000007` | Dr. Waterling | 13 | None | Missing | `UNKNOWN` |
| `DS-000008` | The Senior Health Podcast | 37 | None | Missing | `UNKNOWN` |
| `DS-000009` | Senior Health Hub | 24 | None | Missing | `UNKNOWN` |
| `DS-000010` | The Health Educator | 11 | None | Missing | `UNKNOWN` |

Dr. Aliza is not duplicated in this table because exact-handle reconciliation upgraded its screenshot dataset to the canonical Tier A channel `CH-000003`.

## 11. Video/content and transcript inventory

The catalog contains 274 stable `videos` rows and exactly 274 `video_snapshots` rows:

- `DS-000001`: 159 items, type unknown.
- `DS-000006`: 32 regular videos.
- `DS-000017`: 43 regular videos and 40 Shorts.
- No streams are registered.

Transcript state:

| Source | Available | Unavailable | Local/canonical reference | Hash state |
|---|---:|---:|---|---|
| Supplied archive (`DS-000001`) | 158 | 1 | Linked through `archive_member_file_id`; `canonical_reference` is null | Source archive members are hashed, but `transcripts.transcript_sha256` is null |
| Apify (`DS-000006`, `DS-000017`) | 115 | 0 | Immutable local plaintext files; non-null `canonical_reference` | Non-null transcript SHA-256 |
| **Total** | **273** | **1** | | |

The one unavailable transcript is Matty Invests video `oBJZxDwKgAU`. Every video has exactly one transcript row; there are no videos without a transcript status record and no video has duplicate transcript rows.

Transcript availability is not script intelligence. The system stores/references transcript text, language, caption type, word count, and availability, but it does not yet classify hooks, narrative structure, pacing, rhetoric, evidence quality, or reusable script patterns.

## 12. Screenshot, thumbnail, and packaging evidence

- 122 screenshot/evidence images were ingested across `DS-000002`–`DS-000010`.
- All 122 received OCR and semantic inspection: 122 OCR observations and 122 semantic-inspection observations.
- `thumbnail_evidence` contains 115 URL references covering all 32 Dr. Aliza and all 83 xkcd items.
- A thumbnail URL/reference proves where a thumbnail was reported; it is not a downloaded thumbnail image and is not thumbnail intelligence.
- Only `DS-000003` has a populated aggregate `packaging_style` value.
- `DS-000004`–`DS-000010` have inspected screenshots but empty packaging-style aggregates.
- `DS-000002` also has screenshot observations but no packaging-style aggregate.

The reporting layer correctly separates thumbnail references, screenshot-supported packaging evidence, and actual editing evidence. However, the classification layer is incomplete and seven aggregate provenance locators are wrong, as detailed below.

## 13. Forensic evidence

Actual moving-image/frame evidence must be separated from transcripts, screenshots, and thumbnail references.

| Dataset | Actual evidence | Frames | Visual-state clusters | Canonical channel/video relationship | Editing-style classification |
|---|---|---:|---:|---|---|
| `DS-000002` | Two screenshots only | 0 | 0 | None | `UNKNOWN` |
| `DS-000012` | Sparse frame sequence + canonical report | 96 | 60 | xkcd `rGZ6TsXvi8E` — proven | Not completed |
| `DS-000013` | Dense frame sequence + canonical report | 1,393 | 107 | xkcd `mEUqVgGf4e0` — proven | Not completed |
| `DS-000014` | Dense frame sequence + canonical report | 766 | 117 | xkcd `SLd4hnmeW_g` — proven | Not completed |
| `DS-000015` | Dense frame sequence + canonical report | 2,488 | 101 | xkcd `rGZ6TsXvi8E` — proven | Not completed |
| `DS-000016` | Frame sequence + reconstruction cards/report | 307 | 307 | None | Not completed |

Five datasets contain 5,050 actual frame assets and 692 visual-state clusters. Existing canonical reports give all 692 clusters a traceable semantic coverage locator; 0 are unresolved in the visual-state coverage ledger. That is evidence coverage, not a completed editing-style taxonomy.

For xkcd there are 4 proven dataset relationships covering 3 unique canonical videos. `DS-000012` and `DS-000015` are separate analysis passes over the same source video. The relationship is proven at the video identity level through exact source-download media IDs, title, duration, and source hash; the dataset revision/duplicate relationship is not formally modeled.

No channel-wide xkcd editing style is claimed. Evidence exists for only three of 83 videos, and `editing_style` remains `UNKNOWN`.

## 14. Controlled raw-ingestion system

`BATCH-000001` demonstrates a real controlled multimodal ingestion workflow:

- 12 authorized source roots.
- 45,774 filesystem entries recorded.
- 42,678 ordinary files, all with SHA-256 hashes.
- 3,088 directories and 8 symlinks recorded, not incorrectly hashed as files.
- Every entry has an explicit disposition.
- 4,057 `EXACT_DUPLICATE` entries, all linked to a duplicate target.
- 141 `INGEST`, 5,181 `SUPPORTING_EVIDENCE`, 802 `SUPERSEDED`, 95 `NOISE`, 35,462 `TOOLING`, 10 `REFERENCE_ONLY`, 2 `ALREADY_INGESTED`, and 24 `HOLD` entries.
- 5,172 registered visual assets.
- 17 document records, all marked fully read.
- Source-file table: 6,241 physical files + 160 archive members, all hashed.

Strengths include recursive coverage, hash-first exact duplicate detection, symlink non-following, explicit disposition, source preservation, transactional registration, and manifest generation.

Limits include batch-specific rules, local-only operation, manual authorization, no service/job queue, no automatic recurring ingestion, and incomplete automatic reconstruction of OCR/AI observation rows from durable inputs alone.

The 24 held entries belong to one unrelated mixed-in video under the historical Codex root; they represent 22 distinct hashes. Holding rather than ingesting them is a deliberate privacy/provenance safeguard, not silent data loss.

## 15. Apify acquisition audit

No Apify Actor was called during this audit. Only registered historical runs, manifests, raw local files, catalog rows, code, and tests were inspected.

### Dr. Aliza Wright

| Field | Verified value |
|---|---|
| Channel | `CH-000003` — Dr. Aliza Wright \| Advice |
| Dataset | `DS-000006` |
| Apify source run | `APIFYRUN-000001`; Actor run `bD7JBsuj7LK5Wt2rk` |
| Registration run | `RUN-000018` |
| Actor | `streamers/youtube-scraper`, build `0.0.283` |
| Result | 32 unique regular videos; 0 duplicates |
| Transcripts | 32 available, 0 unavailable |
| Thumbnail references | 32 |
| Run status | `SUCCEEDED` |
| Cost | Initial observation $0.108; finalized charged-event ledger $0.128 |
| Cost control | Default/authorized $0.50 cap; 125-result ceiling at $0.004/result; actual result count and cost below cap |
| Identity reconciliation | Exact handle/canonical URL joined screenshot dataset to one canonical channel |
| Raw retention | 32 transcript files, sanitized run manifest, final cost manifest, and normalized/catalog provenance retained; full raw Actor result JSON not retained locally |

The raw-retention limitation matters: normalized values and record hashes exist, but the exact complete Actor result objects cannot be re-parsed or independently re-registered from a durable local raw payload if the remote Apify dataset disappears.

### xkcd's What If?

| Field | Verified value |
|---|---|
| Channel | `CH-000004` — xkcd's What If? |
| Dataset | `DS-000017` |
| Apify source run | `APIFYRUN-000002`; Actor run `mzl5dCHF81LbcBamS` |
| Registration run | `RUN-000020` |
| Actor | `streamers/youtube-scraper`, build `0.0.283` |
| Result | 83 unique items; 43 regular, 40 Shorts, 0 streams; 0 duplicates |
| Transcripts | 83 available, 0 unavailable |
| Thumbnail references | 83 |
| Run status | `SUCCEEDED` |
| Final cost | $0.332 |
| Cost control | Bounded input ceiling of 83 items; adapter default cap $0.50; actual cost below cap |
| Identity reconciliation | Exact requested/returned handle created one canonical identity |
| Raw retention | Full 643,031-byte raw result JSON retained and SHA-256 recorded; 83 local transcript files retained |
| Forensic links | 4 proven dataset links, 0 unresolved, covering 3 canonical videos |

### Acquisition capability assessment

Implemented and verified:

- Preflight result/cost ceiling calculation.
- Runtime cap validation.
- Exact target input and optional content-type bounds.
- Actor/run/build/input/result/cost metadata.
- Result validation, duplicate ID handling, type preservation, and transactional rollback.
- Append-only normalized snapshots.
- Transcript and thumbnail references.
- Exact-handle and source-media-ID reconciliation.
- Idempotency and safe rejected-run recording.
- Offline test fixtures that do not call Apify.

Not production-ready:

- No scheduler or automatic refresh.
- No operator workflow/approval service.
- No durable per-run `approved_cost_cap` column; bounded input and actual cost are stored, while the approved cap remains implicit in invocation/default behavior.
- Dr. Aliza's full raw Actor result payload is missing.
- No retry/backoff/monitoring service or alerting layer.

## 16. SQLite architecture

SQLite is appropriate for the present local Phase 1 scale. The schema is additive, relational, foreign-key constrained, and migration-tested. It is deliberately not the final production intelligence database.

### C. Mandatory database table

| Table | Purpose | Row count | Primary identity / relationship |
|---|---|---:|---|
| `schema_meta` | Applied migration ledger | 6 | `schema_version` |
| `datasets` | Logical dataset registry | 17 | `dataset_id` |
| `ingestion_runs` | Ingestion/registration audit runs | 20 | `run_id`; optional dataset |
| `source_locations` | Original source roots/locations | 19 | Dataset → source location |
| `source_files` | Physical files and archive members with hashes | 6,401 | `file_id`; dataset/run/optional parent file |
| `file_relationships` | File duplicate/revision relationship model | 0 | From-file → to-file |
| `ingestion_errors` | Structured ingestion failures | 0 | Run/dataset/file error |
| `channels` | Stable canonical channel identities | 4 | `channel_id`; unique YouTube identity fields |
| `channel_snapshots` | Mutable channel metrics over time | 4 | Channel + dataset + observation time |
| `videos` | Stable canonical video identities | 274 | `video_id`; unique YouTube video ID; belongs to channel |
| `video_snapshots` | Mutable title/type/metrics observations | 274 | Video + dataset + observation time |
| `transcripts` | Transcript availability and source references | 274 | Transcript → video/dataset/run/source file |
| `field_provenance` | Per-field source locator/origin/evidence layer | 4,757 | Exactly one target entity per row |
| `source_batches` | Multi-root batch registry | 1 | `batch_id` |
| `batch_roots` | Authorized roots within a batch | 12 | Root → batch |
| `discovered_files` | Complete recursive entry ledger/disposition | 45,774 | Entry → root/batch/dataset/source file/duplicate target |
| `visual_assets` | Image/frame metadata and perceptual clusters | 5,172 | Asset → discovered file/dataset |
| `visual_observations` | OCR and semantic observations | 244 | Observation → visual asset |
| `entity_classifications` | Dataset-level domain/packaging/editing fields | 9 | One classification per dataset |
| `document_records` | Full-read document characterization | 17 | Document → discovered file/dataset |
| `apify_source_runs` | Actor run and sanitized input/result provenance | 2 | Source run → registration run/dataset |
| `channel_dataset_links` | Evidence-qualified channel/dataset relations | 10 | Channel + dataset + relationship type |
| `apify_result_records` | Per-result raw-record hash and canonical video link | 115 | Apify source run + record index/video |
| `thumbnail_evidence` | Source thumbnail URL evidence | 115 | Video/dataset/Apify run |
| `apify_run_cost_observations` | Append-only cost/billing observations | 3 | Cost observation → Apify source run |

Database health:

- `schema_meta` latest version: 6.
- `PRAGMA integrity_check`: `ok`.
- `PRAGMA foreign_key_check`: 0 rows.
- 0 ingestion-error rows.
- 20/20 ingestion runs have `COMPLETED` status.
- Runtime database size: 47,157,248 bytes.

## 17. Snapshot model

The architecture correctly supports append-only snapshots. `UNIQUE (video/channel, dataset, observed_at)` constraints prevent overwriting the same observation and tests prove that a newer run can append a second video snapshot.

The current corpus has **no meaningful longitudinal history**:

| Channel | Channel snapshots | Videos | Video snapshots | Videos with >1 snapshot | Observation date/time |
|---|---:|---:|---:|---:|---|
| Matty Invests | 1 | 94 | 94 | 0 | `2026-08-24` |
| Mr. Finance | 1 | 65 | 65 | 0 | `2026-08-24` |
| Dr. Aliza Wright \| Advice | 1 | 32 | 32 | 0 | `2026-08-28T12:06:34.708Z` |
| xkcd's What If? | 1 | 83 | 83 | 0 | `2026-08-28T13:16:30.020Z` |

Therefore:

- Historical architecture: **SUPPORTED**.
- Actual multi-date observations: **ABSENT**.
- Growth curves, velocity changes, 24-hour performance, decay, thumbnail-change effects, and subscriber trends: **NOT MEASURABLE** from this corpus.

## 18. Provenance model

### Conceptual model

The documented evidence-state model distinguishes `RAW_SOURCE`, `EXTRACTED_FACT`, `MEASURED_FACT`, `OBSERVATION`, `AI_INTERPRETATION`, `HUMAN_INTERPRETATION`, `HYPOTHESIS`, `RECOMMENDATION`, `SUSPECT`, and `SUPERSEDED`. This is a strong conceptual control.

The implemented database uses a narrower operational subset. `field_provenance` currently contains 4,205 `EXTRACTED_FACT`, 548 `MEASURED_FACT`, and 4 `SOURCE_METADATA` rows. `entity_classifications` contains 9 `OBSERVATION` rows. The untracked xkcd intelligence artifact labels measured facts, observations, AI interpretations, and hypotheses in Markdown, but those intelligence records are not database entities.

### Can the system answer “Where did this value come from?”

| Value | Assessment | Evidence |
|---|---|---|
| Channel identity | **GOOD/PARTIAL** | All 4 have field provenance and dataset identity. Apify rows have direct source-file/run links. The 2 legacy channels have workbook cell locators but null `source_file_id`. |
| Video title | **GOOD/PARTIAL** | 274/274 have field provenance and locators. The 159 legacy rows lack direct workbook `source_file_id`; 115 Apify rows are directly linked. |
| Views | **GOOD/PARTIAL** | 274/274 provenance rows; same legacy direct-link limitation. |
| Likes | **GOOD/PARTIAL** | 274/274 provenance rows; same legacy direct-link limitation. |
| Comments | **GOOD/PARTIAL** | 274/274 provenance rows; same legacy direct-link limitation. |
| Subscriber counts | **GOOD/PARTIAL** | 4/4 provenance rows; 2 legacy workbook rows lack direct file FK. |
| Transcript | **GOOD/PARTIAL** | Apify: local reference + SHA-256 + source file. Legacy: archive member FK and header locators, but null transcript hash/canonical reference. |
| Thumbnail | **GOOD where present** | 115/115 Apify thumbnail URLs have source provenance. No thumbnail evidence was supplied/registered for the 159 legacy items. |
| Dataset association | **GOOD** | Stable dataset foreign keys, `created_from_dataset_id`, and evidence-qualified `channel_dataset_links`. Tier B labels remain explicitly non-canonical. |

### Good provenance

- 42,678/42,678 discovered ordinary files hashed.
- 6,401/6,401 source-file/archive-member rows hashed.
- All 4,757 field-provenance rows have non-empty `source_locator`.
- Apify source runs, record hashes, run/build metadata, sanitized input, cost observations, transcript references, and thumbnail URLs are linked.
- Exact source-download media IDs support the four xkcd forensic relationships.
- Dataset/channel/video/transcript rows use foreign keys.

### Partial provenance

- `DS-000001` has 2,556 provenance rows, but 1,920 have null `source_file_id`. Their workbook/sheet/row/column locators are precise text, so provenance is not absent, but it is not a complete direct relational link.
- All 158 available legacy transcript rows link to archive members, but `transcripts.transcript_sha256` and `canonical_reference` are null.
- Four forensic video-ID links use exact external source locators and notes but no direct `source_file_id` because the referenced source videos are outside the canonical raw file table.
- Entity classification exists for only 9/17 datasets.
- Visual observations are linked per asset, but most aggregate packaging classifications are missing.

### Missing or incorrect provenance

Seven classification rows have incorrect source locators that literally say `aggregated from 0 screenshot semantic inspections` even though the database contains the following actual counts:

| Dataset | Claimed count | Actual semantic inspections |
|---|---:|---:|
| `DS-000004` | 0 | 13 |
| `DS-000005` | 0 | 10 |
| `DS-000006` | 0 | 7 |
| `DS-000007` | 0 | 13 |
| `DS-000008` | 0 | 37 |
| `DS-000009` | 0 | 24 |
| `DS-000010` | 0 | 11 |

These are locator-quality defects, not missing screenshot observations. The 115 observations exist; the aggregate locator text is wrong.

## 19. Evidence-state model assessment

The project is careful not to silently promote inference to fact. Decision 016 prevents thumbnail/channel screenshots from becoming editing-style claims, and the xkcd artifact explicitly labels `MEASURED_FACT`, `OBSERVATION`, `AI_INTERPRETATION`, and `HYPOTHESIS`.

Implementation is partial because:

- The full conceptual state vocabulary is not a shared enforced schema across all layers.
- Intelligence records are Markdown, not first-class database entities with structured provenance edges.
- `document_records.evidence_type` describes document genre, not the same evidence-layer taxonomy.
- No `SUSPECT`, `HUMAN_INTERPRETATION`, `HYPOTHESIS`, `RECOMMENDATION`, or `SUPERSEDED` intelligence records exist as normalized entities.
- The seven bad source locators show that an evidence-state label alone does not guarantee a correct locator.

## 20. Intelligence layer

One intelligence artifact exists:

`data/intelligence/channels/CH-000004/content-performance-intelligence-2026-08-28.md`

It is untracked and was preserved unchanged during this audit. It analyzes all 83 xkcd items using one snapshot, separates regular videos and Shorts, uses an age-adjusted within-channel baseline, reports topic/title-structure clusters, labels evidence states, lists limitations, and preserves an explicit provenance boundary to `DS-000017`, `RUN-000020`, and `APIFYRUN-000002`.

This artifact demonstrates that content-performance analysis is possible from the catalog, but the capability is partial:

- It is a one-off Markdown result with no tracked generation script or repeatable test.
- It uses only one snapshot per item.
- Topic clusters and premise families are AI interpretations, not source-declared categories.
- It cannot control for thumbnails, impressions, CTR, watch time, retention, traffic sources, audience segments, or promotion.
- It is channel-specific and does not benchmark against other canonical channels.
- It does not analyze scripts, hooks, thumbnails as creative artifacts, or editing style.
- It is not registered as a structured intelligence entity.

## 21. Reporting layer

Three read-only tools exist:

| Tool | Purpose | Formats | Current result |
|---|---|---|---|
| `scripts/report_corpus_status.py` | Corpus totals, dispositions, visual/document coverage, and gaps | Markdown + JSON | Successful |
| `scripts/report_channel_coverage.py` | Tier A/Tier B channel and evidence coverage | Markdown + JSON | Successful |
| `scripts/report_dataset_matrix.py` | Dataset-by-dataset domain/forensic/transcript/classification/provenance matrix | Markdown + JSON | Successful |

All three previously ran successfully in both formats. JSON mode was rerun successfully during this continuation. They issue only `SELECT` queries and do not modify SQLite or manifests.

Reporting is useful and tested, but it is terminal/Markdown/JSON reporting only. There is no API, scheduled report, dashboard, alert, trend report, or user-facing application.

## 22. Tools and skills

Installed developer/agent tools include Graphify, Ponytail, Claude-Mem, Scrapling, Pillow, and Obsidian-related skills. The repository also has a project-scoped multimodal ingestion skill.

Important boundaries:

- None of these tools is part of the production YouTube Intelligence OS architecture.
- Graphify has no built knowledge graph and was not used in this audit.
- Claude-Mem is auxiliary and cannot override repository evidence.
- Scrapling is reserved for future explicitly authorized web validation; it was not used here.
- Pillow supports image metadata/perceptual hashing locally.
- The multimodal ingestion skill codifies Phase 1C rules but is a workflow aid, not a source of truth.
- No MCP-driven autonomous application workflow exists.

## 23. Tests

Fresh command run once:

```text
.venv/bin/python3 -m unittest discover -s tests -v
```

| Measure | Result |
|---|---:|
| Discovered/run | 56 |
| Passed | 56 |
| Failed | 0 |
| Skipped | 0 |
| Duration | 2.530 seconds |

Coverage represented in the suite includes schema migrations, foreign keys, source immutability, SHA-256, archive inventory, idempotency, revision rejection, rollback, recursive batch coverage, exact duplicate detection, perceptual hashes, classification defaults, Apify normalization, cost caps, identity reconciliation, forensic media links, snapshots, secret non-persistence, reporting, and transcript states.

Testing gaps:

- No CI workflow is present.
- No coverage percentage is measured.
- No load/performance, concurrent writer, disaster-recovery, or production network integration suite exists.
- The content-performance intelligence artifact has no reproducible generator test.

## 24. Security

The security design is appropriate for the current local phase: raw immutability, environment-only tokens, sanitized Actor inputs, no secret output, ignored `.env` files, local raw/database storage, and prompt-injection boundaries for future web research.

The redacted scan searched for token-value patterns and reported only status, never values:

| Scope | APIFY_TOKEN value status |
|---|---|
| Git history | **NOT PRESENT** |
| SQLite | **NOT PRESENT** |
| Documentation | **NOT PRESENT** |
| Tracked/current config | **NOT PRESENT** |
| Logs | **NOT PRESENT** |
| Manifests | **NOT PRESENT** |
| Fixtures | **NOT PRESENT** |
| Tests | **NOT PRESENT** |
| Raw acquisition folders | **NOT PRESENT** |

The identifier `APIFY_TOKEN` appears in documentation/code as an environment-variable name; that is not a persisted credential value. Tests also verify that secret values are not persisted.

Security limits:

- Local raw data and SQLite depend on host filesystem security and backup practices not audited here.
- No role-based access control, encryption-at-rest policy, central audit service, or secret manager is implemented because there is no production service.
- The Dr. Aliza raw payload gap is a reproducibility issue more than a credential issue.

## 25. Git and repository health

| Item | Verified state |
|---|---|
| Branch | `main` |
| Local `HEAD` | `f0139efead2a6e75dea1fd4dc14715a0b121b4b2` |
| Live remote `refs/heads/main` | `f0139efead2a6e75dea1fd4dc14715a0b121b4b2` |
| Synchronized | Yes |
| Existing staged user work | `.codex/environments/environment.toml` preserved |
| Existing untracked user work | `data/intelligence/channels/CH-000004/content-performance-intelligence-2026-08-28.md` preserved |
| Audit-created change | This report only |
| Commit/push | None |

Repository health is good for a local research/code project, with a private canonical remote and sensible ignore rules. Production-readiness is limited by absent CI and the intentional exclusion of raw data/SQLite from Git; durable backup/rebuild validation must therefore exist outside Git before production use.

## 26. End-to-end workflow today

### Supplied-folder path

1. User explicitly supplies a folder/dataset.
2. System performs read-only discovery.
3. Every entry receives an explicit disposition.
4. Ordinary files are SHA-256 hashed; exact duplicates are linked.
5. Approved evidence is copied or reference-indexed without changing the source.
6. Dataset, source files, and batch records enter SQLite.
7. Images receive local metadata/perceptual hashing; selected screenshot assets receive OCR/semantic inspection.
8. Documents are characterized after full read.
9. Database-generated manifests preserve durable provenance.
10. Verification checks hashes, catalog integrity, foreign keys, counts, and tests.

### Structured supplied dataset path

1. Parse canonical XLSX/transcript archive.
2. Resolve channel/video identities.
3. Create stable identities and one observation snapshot.
4. Register transcript state and per-field provenance.
5. Reconcile workbook/archive IDs and refuse malformed/revised inputs.

### Controlled Apify path

1. Exact channel target and result/cost ceiling are planned.
2. User explicitly authorizes a bounded run.
3. Environment-only token calls one Actor target.
4. Result status, cost, IDs, data types, duplicates, and identity are validated.
5. Raw payload should be retained; transcript files are retained.
6. Transaction creates/links canonical identity, snapshots, transcript references, thumbnails, record hashes, provenance, and cost observations.
7. Reports verify the result.

Today, these workflows are command-driven and manually authorized. They are not scheduled or autonomous.

## 27. Intended system versus current system

| Layer | Intended | Current |
|---|---|---|
| Evidence intake | Safe multi-source ingestion | Strong local folder ingestion + narrow Apify adapter |
| Provenance | End-to-end traceability for every fact/interpretation | Strong for current Apify fields; partial legacy and classification gaps |
| Classification | Every item classified by semantic/evidence role | Dataset class exists; 8/17 lack entity-classification rows |
| Extraction/normalization | Reusable normalized corpus | Partial structured registration; no general Phase 3 layer |
| Channel brains | Separate channel-specific intelligence | Separate channel IDs; no formal channel brain |
| Competitor intelligence | Benchmarks, patterns, gaps | Not implemented |
| Script/hook intelligence | Structured analysis and reusable patterns | Not implemented |
| Title/thumbnail intelligence | Analysis and generation | Not implemented; only titles/thumbnail URL references exist |
| Editing intelligence | Evidence-backed style classifications | Frame evidence exists; classifications absent |
| Opportunity engine | Ranked hypotheses | Not implemented |
| Web validation | Provenance-preserving live research | Not implemented/not authorized |
| Recommendations | Validated actionable outputs | Not implemented |
| Retrieval/RAG | Evidence-aware retrieval if justified | Not implemented; not needed yet |
| Automation | Scheduled refresh and continuous learning | Not implemented |
| Product UI | Dashboard/frontend | Not implemented |

## 28. Capability matrix

### D. Mandatory capability table

| Capability | Intended | Implemented | Verified | Production-ready | Evidence | Missing work |
|---|---|---|---|---|---|---|
| Controlled raw ingestion | Safe immutable intake | Yes | Yes | No | `BATCH-000001`, 45,774 dispositions | Operator workflow, backup, scale/concurrency |
| SHA-256 hashing | Anchor file identity | Yes | Yes | Mostly for current scale | 42,678 discovered files; 6,401 source rows hashed | Continuous verification/backup audit |
| Exact duplicate detection | Avoid independent-evidence inflation | Yes | Yes | Current-scale only | 4,057 linked exact duplicates | Cross-batch policy/reporting; relationship normalization |
| Datasets/manifests | Durable dataset provenance | Yes | Yes | Mostly | 17 DB datasets, manifests | Inventory doc drift; full rebuild automation |
| Multi-channel separation | Prevent channel leakage | Identity layer yes | Yes | No | 4 distinct channel IDs; 0 cross-channel video/transcript hashes | Channel brains and ownership/competitor mappings |
| SQLite catalog | Queryable Phase 1 index | Yes | Yes | Yes for current local phase; no for final product | v6, 25 tables, integrity clean | Backup/recovery and eventual production-store decision |
| Channel identity | Stable canonical channel | Yes | Yes | Mostly | 4 IDs; exact reconciliation | More channels and operator resolution UX |
| Video identity | Stable canonical video | Yes | Yes | Mostly | 274 unique YouTube IDs; 0 duplicates/orphans | More source adapters and merge audit UX |
| Channel snapshots | Append-only metric history | Schema only in practice | Yes | No | 4 rows, one/channel | Repeated observations |
| Video snapshots | Append-only metric history | Schema only in practice | Yes | No | 274 rows, one/video | Repeated observations |
| Transcripts | Availability/source references | Yes | Yes | Mostly | 273 available, 1 unavailable | Legacy hashes/references; quality/language checks |
| Thumbnail references | Trace thumbnail source | Yes for Apify | Yes | No | 115 URL records | Image retention, visual features, change history |
| Field provenance | Trace structured values | Partial | Yes | No | 4,757 rows | Direct legacy source FKs; locator corrections |
| Screenshot packaging evidence | Preserve screenshot observations | Partial | Yes | No | 122 OCR + 122 semantic observations | Complete packaging classifications; fix 7 locators |
| Forensic evidence | Link moving-image evidence | Partial | Yes | No | 5,050 frames; 692 clusters; 4 xkcd links | Formal style taxonomy, broader video coverage |
| Apify YouTube acquisition | Bounded structured acquisition | Yes | Yes | No | 2 successful registered runs | Raw retention consistency, automation/ops controls |
| Cost caps | Prevent unbounded spend | Yes | Yes | Mostly | Code + tests; $0.50 default; bounded runs | Persist approved cap explicitly; operator approvals |
| Identity reconciliation | Avoid name-only merges | Yes | Yes | Mostly | Exact handle/media-ID tests and live links | Review UI and broader conflict policy |
| Read-only reporting | Current corpus visibility | Yes | Yes | Current CLI scope | 3 tools, Markdown/JSON | Scheduled/API/dashboard delivery |
| Content-performance intelligence | Evidence-labeled performance analysis | One artifact | Partially | No | xkcd artifact | Tracked generator, tests, more snapshots/channels |
| Full script intelligence | Analyze complete script style | No | No | No | No code/schema/output | Phase 3–4 normalized transcripts + analysis model |
| Hook intelligence | Extract/evaluate hooks | No | No | No | Training docs only | Implemented prompt/schema/workflow |
| Title intelligence | Analyze/generate titles | No | No | No | Titles stored; one descriptive artifact | Dedicated models, evidence, evaluation |
| Thumbnail intelligence | Analyze/generate thumbnails | No | No | No | URL references only | Local images/features/classification/evaluation |
| Editing-style classification | Classify production grammar | No | No | No | Evidence for 3 xkcd videos; all style fields unknown | Taxonomy, representative coverage, validation |
| Cross-channel intelligence | Compare separated channels | No | No | No | No cross-channel artifact/table | Channel brains + common metrics |
| Competitor benchmarking | Performance/packaging baselines | No | No | No | No implemented benchmark | Phase 6 |
| Topic opportunity discovery | Generate ranked gaps/hypotheses | No | No | No | No opportunity entities | Phases 6–7 |
| Web-validation workflow | Validate hypotheses externally | No | No | No | Planning docs/Scrapling only | Phase 8 authorization and provenance workflow |
| Recommendation generation | Produce validated actions | No | No | No | No recommendation records | Evidence-backed validation and review |
| Automated competitor refresh | Reacquire on cadence | No | No | No | Manual Apify only | Scheduler, approvals, cost budgets, diffing |
| Scheduler | Run jobs periodically | No | No | No | No cron/job service | Phase 12 |
| RAG/embeddings/vector DB | Semantic retrieval if justified | No | No | Not needed now | Explicitly deferred | Evaluate only after normalized corpus/query needs |
| MCP-driven autonomous workflows | Agent orchestration | No | No | No | Developer plugins only | Phase 11 after stable manual workflows |
| Frontend/dashboard | User-facing product | No | No | No | No application directory/API | Stable product requirements and API |

## 29. Data-quality findings

| Check | Result |
|---|---|
| Duplicate canonical YouTube video ID groups | 0 |
| Canonical video IDs shared across channels | 0 |
| Orphan videos | 0 |
| Videos missing channel ID | 0 |
| Videos without snapshot | 0 |
| Videos without transcript-status row | 0 |
| Videos with duplicate transcript rows | 0 |
| Transcript hashes shared across channels | 0 |
| Snapshots linked outside channel/dataset identity | 0 |
| Missing transcripts | 1 unavailable caption |
| Foreign-key violations | 0 |
| Ingestion errors | 0 |
| Unresolved xkcd forensic links | 0 |
| Entity-classification rows missing | 8 datasets |
| Incorrect screenshot aggregate locators | 7 datasets |
| Videos with multiple snapshots | 0 |
| Held entries | 24 entries / 22 distinct hashes |

Additional findings:

- `file_relationships` has 0 rows. Batch exact duplicates are represented through `discovered_files.duplicate_of_discovered_file_id`, not the older generic relationship table.
- 802 `SUPERSEDED` discovered entries do not use `duplicate_of_discovered_file_id`; their reason text records the relationship. This is descriptive but less relationally queryable.
- The older source-discovery reports call the two Hook PDFs a probable unresolved revision. Current `document_records` contain a full `pdftotext` comparison proving exact textual identity. The older report is stale, not the current source of truth.
- `DS-000012` and `DS-000015` are proven to map to the same canonical xkcd video, but the dataset-level “independent re-run/revision” relationship remains descriptive rather than formally recorded.
- No cross-channel contamination was detected in canonical video IDs, transcript hashes, or snapshot/dataset links.

## 30. Confirmed issues, risks, and technical debt

### E. Mandatory issues table

| Type | Severity | Finding | Evidence | Impact | Recommended future action |
|---|---|---|---|---|---|
| Documentation drift | High | README states Phase 1C; authoritative state is Phase 1D complete | `README.md` vs `AGENTS.md`/`docs/Phases.md` | New developers may follow wrong boundary | Reconcile all phase declarations under one explicit task |
| Documentation drift | High | `docs/DATA_INVENTORY.md` omits `DS-000017` and contains obsolete “no database” language | DB has 17 datasets; doc lists 16 | Durable inventory is incomplete | Regenerate/update inventory from current catalog |
| Provenance | High | 7 screenshot aggregate locators claim 0 inspections despite 7–37 actual observations | `report_corpus_status.py --json` | Audit trail is factually wrong | Correct locators from linked observation counts; add regression test |
| Provenance | High | 1,920 `DS-000001` field-provenance rows lack direct `source_file_id` | DB query | Source trace relies on text locator, not FK | Backfill workbook file FK without changing locators/values |
| Transcript provenance | Medium | 159 legacy transcript rows lack transcript SHA/reference; 158 available still link to archive members | DB query | Harder independent transcript-body verification | Backfill deterministic transcript hashes/references from immutable archive members |
| Snapshot history | High | Every channel/video has only one observation | 4 channel + 274 video snapshots | No trend/velocity/decay analysis | Collect explicitly authorized second and later snapshots |
| Raw retention | High | Dr. Aliza full Actor result JSON is absent | DS-000006 raw tree and manifest | Exact reprocessing depends on remote Actor dataset/normalized outputs | Adopt mandatory raw-result retention and document exception |
| Classification | High | 8/17 datasets lack entity-classification rows | Corpus status report | Phase 2 coverage incomplete | Execute Phase 2 only after explicit authorization |
| Packaging classification | Medium | Only DS-000003 has populated packaging-style aggregate | 122 inspected screenshots | Evidence cannot be queried as consistent packaging intelligence | Define/validate classification schema in Phase 2+ |
| Forensic classification | High | Editing evidence exists, but no editing-style classification exists | 5 frame datasets; all `UNKNOWN` | Cannot answer channel editing-style questions | Build evidence-scoped style taxonomy; avoid channel-wide extrapolation |
| Dataset relationship | Medium | DS-000012/DS-000015 same-video relationship is not formalized as a dataset relation | Both link to `rGZ6TsXvi8E` | Duplicate analyses may be counted as independent evidence | Add explicit dataset revision/related-analysis relation |
| Historical docs | Medium | Hook PDF relationship resolved in catalog but stale discovery docs call it unresolved | `document_records` vs source-discovery docs | Conflicting developer guidance | Mark historical report superseded or add current resolution note |
| Cost provenance | Low | Approved per-run cost cap lacks dedicated persisted field | Schema/run manifests | Later reviewer infers cap from defaults/input | Store approved cap and price basis on future runs |
| Intelligence reproducibility | High | xkcd artifact has no tracked generator/test and is untracked | Git status + artifact | Analysis cannot be reliably rerun/reviewed | Review, track, and create minimal reproducible generator in authorized phase |
| Intelligence coverage | Critical | Script, hook, title, thumbnail, editing, competitor, cross-channel, opportunity, validation, and recommendation layers absent | Code/schema scan | Core OS outcome unavailable | Follow phased roadmap; do not shortcut provenance |
| Automation | Critical | No refresh, scheduler, autonomous workflow, or continuous learning | Repository scan | Data becomes stale; manual operation only | Automate only after manual workflows and approvals stabilize |
| Product surface | High | No API/frontend/dashboard | Repository scan | Not usable as a product by non-developers | Defer until queries/workflows stabilize |
| Operations | Medium | No CI, load tests, recovery drill, monitoring, or role-based service security | Repository/test scan | Local success does not prove production resilience | Add operations controls when moving beyond local phase |
| Rebuildability | Medium | OCR/AI observations are not fully reproducible from schema+manifests alone without rerunning tools | Catalog README | Disaster recovery is partly procedural | Test/document full rebuild and durable derived-observation inputs |

## 31. Scalability and readiness

### Current-scale readiness

SQLite, stdlib scripts, and local files are sufficient for 17 datasets, 274 videos, 45,774 discovered entries, and a 45 MiB catalog. Queries and tests complete quickly. The single-writer/local-user model is aligned with the current phase.

### Scaling limits

- No concurrent ingestion coordination.
- No incremental/scheduled refresh orchestration.
- No object-storage or backup strategy for raw evidence.
- No retention/lifecycle policy for repeated raw Actor payloads.
- No indexes/query model for large intelligence graphs or semantic retrieval.
- No service API, access control, job queue, metrics, alerts, or retry management.
- No real longitudinal growth yet, so snapshot-volume behavior is untested.
- No performance testing at millions of snapshots/transcripts/frames.

SQLite should not be replaced merely because the eventual system might grow. It should be replaced or complemented only when concurrent writers, remote multi-user access, service uptime, query volume, or intelligence/retrieval requirements exceed the measured local workload.

## 32. Production-readiness scores

Scoring rubric: 0 = absent, 25 = proof of concept, 50 = useful but incomplete, 75 = operational for current scope, 100 = production-hardened.

| Area | Score | Basis |
|---|---:|---|
| Architecture | 72 | Clear phased/evidence-first design; final application architecture intentionally undecided |
| Data model | 72 | Strong Phase 1 identities/provenance/snapshots; intelligence entities absent |
| Data integrity | 92 | Integrity clean, 0 FK violations/orphans/duplicate IDs |
| Provenance | 68 | Strong current Apify links; legacy direct-link and locator defects |
| Raw ingestion | 80 | Complete demonstrated batch coverage; local/manual operations |
| Acquisition | 76 | Two bounded verified runs; no automated ops and one raw payload gap |
| Deduplication | 78 | Hash-first exact duplicate coverage; relationship model fragmented |
| Transcript pipeline | 82 | 273/274 available with complete status; legacy hash/reference gaps |
| Packaging evidence | 48 | 122 inspected screenshots and 115 refs; classification largely missing |
| Forensic evidence | 58 | Deep evidence for 5 datasets/3 linked xkcd videos; no style classifier |
| Reporting | 72 | Three useful dual-format read-only reports; no API/dashboard/scheduling |
| Testing | 78 | 56/56 pass with broad unit/integration coverage; no CI/load/coverage metrics |
| Security | 82 | No persisted token value, good boundaries; no production service controls |
| Intelligence layer | 22 | One careful but untracked, non-repeatable artifact |
| Automation | 5 | Manual commands only |
| Scalability | 42 | Appropriate current scale; untested beyond local single-user workload |
| Documentation | 62 | Extensive and thoughtful, but several high-impact drifts |

**Overall current readiness score: 49/100.**

The overall score is intentionally lower than the simple category average because the intended product's core value lies in intelligence, comparison, opportunity discovery, validation, recommendation, and continuous operation—the least implemented areas. The Phase 1 foundation itself is substantially more mature than the end-to-end product.

## 33. Exact recommended roadmap

No roadmap item was implemented by this audit.

### P0 — Restore audit consistency before new capability work

| Task | Why | Dependency | Expected result |
|---|---|---|---|
| Reconcile phase/inventory documentation, including `DS-000017` | Removes conflicting source-of-truth statements | Explicit documentation task | One consistent current-state narrative |
| Correct the 7 screenshot-count provenance locators and add a regression check | Current locators are factually wrong | Preserve observation rows and provenance | Accurate packaging provenance |
| Backfill direct `source_file_id` links for 1,920 legacy workbook provenance rows | Makes provenance relationally complete | Confirm canonical workbook file ID/hashes | Direct source trace for all legacy structured fields |
| Backfill legacy transcript hashes/canonical references | Improves transcript-body verification | Immutable archive members | Uniform transcript provenance |
| Document/resolve Dr. Aliza raw-payload exception | Prevents future irreproducible acquisitions | Decide retention rule; no Actor rerun required just to audit | Explicit retention policy and known exception |
| Formalize DS-000012↔DS-000015 same-video/related-analysis relation | Prevents double-counting independent evidence | Proven xkcd identity links | Queryable relationship without merging datasets |
| Review and decide whether to track the xkcd artifact | Avoids losing user work and clarifies status | Human review | Deliberate intelligence artifact lifecycle |

### P1 — Phase 2: Data Classification & Provenance

| Task | Why | Dependency | Expected result |
|---|---|---|---|
| Explicitly authorize Phase 2 | Required by repository rules | User decision | Legal phase transition |
| Classify all 17 datasets/items using semantic class and evidence layer | 8 entity classifications are missing | P0 consistency | 100% classification coverage |
| Normalize evidence-state vocabulary across structured, visual, document, and intelligence layers | Current labels are not fully unified | Phase 2 design | Clear fact/observation/interpretation boundaries |
| Complete source-surface and provenance validation | Screenshot and legacy gaps remain | P0 backfills | “Where did this come from?” works uniformly |
| Define dataset relationship types for duplicate/revision/related-analysis | Relationships are split between text and two tables | Proven current cases | Consistent duplicate independence rules |

### P2 — Build evidence before broad intelligence

| Task | Why | Dependency | Expected result |
|---|---|---|---|
| Collect a second authorized snapshot for selected channels | Current metrics have no time dimension | Phase 2 provenance rules + explicit acquisition authorization | First real longitudinal history |
| Execute Phase 3 extraction/normalization for transcripts, titles, thumbnails, and forensic reports | Intelligence should not analyze ad hoc raw forms | Phase 2 complete | Reusable normalized inputs |
| Execute a narrow Phase 4 intelligence pilot with a tracked generator | The one artifact is not reproducible | Normalized inputs | Repeatable evidence-labeled intelligence records |
| Pilot script/hook analysis on one well-proven channel | Tests the highest-value missing intelligence | Transcript normalization | Evidence-backed script/hook schema and output |
| Pilot editing-style classification only on linked forensic videos | Avoids channel-wide extrapolation | Forensic taxonomy + Phase 2 | Video-scoped editing classifications with confidence |
| Retain local thumbnail images and snapshot changes for a pilot | URL references cannot support visual intelligence alone | Explicit acquisition/storage decision | Auditable thumbnail analysis input |

### P3 — Product intelligence and operations, in order

| Task | Why | Dependency | Expected result |
|---|---|---|---|
| Build channel brains and ownership/competitor mappings | Required before safe cross-channel analysis | Phase 4 reusable intelligence | No cross-channel leakage |
| Build competitor benchmarking and cross-channel comparison | Core intended capability | Channel brains + repeated snapshots | Evidence-backed benchmarks |
| Build topic/gap/outlier hypothesis engine | Converts intelligence into opportunities | Competitor intelligence | Ranked traceable hypotheses |
| Add explicitly authorized web-validation loop | Validates rather than replaces internal evidence | Ranked hypotheses + security workflow | Accepted/rejected hypotheses with web provenance |
| Add title/thumbnail/script/visual production outputs | Final content-development surface | Validated opportunities | Traceable production packages |
| Evaluate production DB and semantic retrieval only from measured needs | Avoids premature RAG/vector infrastructure | Real query/scale evidence | Justified storage/retrieval architecture |
| Add API/dashboard | Makes stable capabilities usable | Stable schemas and workflows | User-facing product surface |
| Add scheduler, automated refresh, monitoring, and cost budgets last | Automates proven workflows without bypassing controls | Production workflows + approvals | Safe continuous operation |

## 34. Final system conclusions

The repository has successfully built the hard-to-fake part of an intelligence system: a disciplined evidence intake and provenance foundation. It is healthy, tested, and appropriately conservative about identity, mutability, source authority, secrets, and inference.

It has not yet built most of the product implied by “Intelligence OS.” The current system can tell a developer what evidence exists and where structured values came from, but it cannot yet reliably understand scripts or editing styles, compare competitors, discover validated opportunities, generate recommendations, or run continuously.

The correct next step is not RAG, a dashboard, or automation. It is an explicitly authorized Phase 2 that closes classification and provenance gaps, preceded by the P0 audit-consistency fixes above. Longitudinal data collection should follow soon after because the snapshot architecture has no analytical value until repeated observations exist.

## 35. Direct answers to the 15 required questions

### 1. What is YouTube Intelligence OS today?

A local, evidence-first YouTube dataset ingestion, catalog, provenance, and read-only reporting foundation with one channel-scoped analytical artifact—not yet a complete intelligence product.

### 2. What can it do reliably today?

It can inventory supplied folders, hash files, detect exact duplicates, preserve raw evidence, register datasets/channels/videos/snapshots/transcript states, retain Apify run/cost provenance, reconcile strong identities, link selected forensic datasets, and report corpus/channel/dataset coverage.

### 3. What data currently exists?

17 datasets; 4 canonical channels; 274 content items; 273 available transcripts; 1 unavailable transcript; 122 fully inspected screenshot/evidence images; 115 thumbnail URL references; 5,050 forensic frames across five frame-sequence datasets; 692 covered visual-state clusters; 17 fully read training documents; two historical Apify runs; and one untracked xkcd intelligence artifact.

### 4. What important data is still missing?

Repeated metric snapshots; impressions, CTR, watch time, retention, traffic sources, subscriber conversion, and audience segments; local thumbnails for most channels; full raw Dr. Aliza Actor results; complete entity classification; broader canonical competitor identities; and representative script/editing evidence across channels.

### 5. What is automated?

Command-level discovery, hashing, exact deduplication, registration, migrations, validation, Apify normalization/cost checks, manifest generation, and read-only reports. These are invoked manually; none is scheduled.

### 6. What still requires manual work?

Dataset authorization, ambiguous relationship decisions, Apify run authorization, phase transitions, classification review, intelligence analysis, artifact review, competitor selection, web validation, recommendations, refresh timing, and all production operations.

### 7. Can it safely ingest another YouTube channel today?

**Yes, conditionally.** It can safely ingest a supplied dataset, and the bounded Apify adapter can register another exact channel only with explicit target/cost authorization and the same provenance/retention controls. It is not an automated refresh service.

### 8. Can it analyze a complete competitor today?

**No.** It can register metadata/transcripts and describe available screenshot/forensic coverage, but complete competitor intelligence, benchmarking, packaging analysis, script analysis, and gap discovery are not implemented.

### 9. Can it understand script style today?

**No.** Transcripts exist, but no full script-style or hook-intelligence pipeline exists.

### 10. Can it understand editing style today?

**No.** It has real frame/shot evidence for a small set of videos, but editing-style classification has not been performed and no channel-wide style claim is justified.

### 11. Can it compare multiple channels today?

**Only at a basic reporting level.** It can list channel counts/coverage and one source spreadsheet contains static comparative data, but no production cross-channel intelligence or competitor benchmarking exists.

### 12. Can it autonomously discover content opportunities today?

**No.** There is no opportunity engine, validation loop, recommendation generator, scheduler, or autonomous workflow.

### 13. Is SQLite sufficient for the current stage?

**Yes.** It is sufficient for the current local Phase 1/early-classification scale and should remain until measured concurrency, service, scale, or retrieval needs justify a change.

### 14. Is RAG/vector DB necessary now?

**No.** Classification, provenance completion, normalization, repeated snapshots, and proven intelligence workflows are higher-priority prerequisites. RAG/vector infrastructure should be evaluated from real retrieval needs later.

### 15. What should the NEXT development phase be?

After the P0 audit-consistency corrections, the next development phase should be **Phase 2 — Data Classification & Provenance**, and it must begin only after explicit user authorization. Its completion target should be 100% classified evidence with uniformly valid, direct provenance—not new scraping, intelligence generation, RAG, or automation.

## 36. Audit conclusion

**Audit result: PARTIAL.** The Phase 1D foundation itself passes its principal health checks, but the full YouTube Intelligence OS remains incomplete and has confirmed provenance/documentation/data-history issues. This audit created no fixes, performed no new acquisition or analysis, and did not start Phase 2.
