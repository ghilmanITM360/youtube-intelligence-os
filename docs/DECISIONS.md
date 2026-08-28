# Architectural Decision Log

### Decision 001 — No YouTube API for competitor-data ingestion

**Status:** Accepted

The user will supply competitor datasets directly. The YouTube API is not part of the competitor-data workflow unless the user explicitly changes this requirement.

### Decision 002 — Model memory is not the permanent knowledge store

**Status:** Accepted

Repository data, documented decisions, and preserved evidence remain authoritative. Agent or session memory is auxiliary only.

### Decision 003 — Raw evidence must remain immutable

**Status:** Accepted

Raw source files must never be modified, rewritten, compressed, renamed destructively, or replaced by AI-generated interpretations.

### Decision 004 — Derive architecture from real datasets

**Status:** Accepted

The final database and RAG infrastructure will be chosen only after the real supplied datasets have been inspected and understood.

### Decision 005 — No premature Phase 1 infrastructure

**Status:** Accepted

Do not introduce Supabase, RAG, vector search, MCP, custom agents, or automation during Phase 1. External developer tooling remains separate and does not alter this application-level rule.

### Decision 006 — Support multiple separate YouTube channels

**Status:** Accepted

Channel-specific intelligence must remain separated so evidence or rules from one channel do not silently affect another.

### Decision 007 — Analyze internal competitor intelligence first

**Status:** Accepted

Internal competitor intelligence will be analyzed before external web validation. Future web research will complement supplied internal evidence, not replace it.

### Decision 008 — Iterative topic discovery

**Status:** Accepted

Future topic discovery should follow this pattern:

```text
Internal Data
→ Analysis
→ Topic Hypothesis
→ Web Research
→ Re-analysis
→ Final Opportunity
```

## Decision 009 — Permanent Canonical Project Location

**Status:** Accepted

The permanent canonical repository is:

`/Users/ghilmanislam360/Documents/youtube-intelligence-os`

It lives directly under the user's `Documents` directory.

It must not be treated as a temporary Codex task workspace.

Directories under:

`/Users/ghilmanislam360/Documents/Codex/`

may contain:

- historical Codex sessions
- dated task outputs
- research
- experiments
- audits
- old datasets
- temporary working material

but they are **not** the canonical location of the YouTube Intelligence OS.

There must be only one authoritative working repository:

`/Users/ghilmanislam360/Documents/youtube-intelligence-os`

**Reason:** The long-term YouTube Intelligence System requires one stable, easy-to-find location independent of Codex-generated task folders or dated workspaces.

## Decision 010 — External Source Folders Are Valid Ingestion Inputs

**Status:** Accepted

The system may receive a local folder path rather than uploaded/copied files, e.g.:

```text
Ingest this folder:
/path/to/source-folder
```

The first operation on any such folder must be read-only discovery. The system must inspect → inventory → hash → classify → identify logical datasets → propose ingestion, before copying or transforming any source material. See `docs/Architecture.md` §5 for the conceptual flow and `docs/source-discovery/` for the Phase 0.5 demonstration of this procedure against four real folders.

Original external folders remain source evidence and must not be modified, moved, renamed, or reorganized automatically. A folder is not assumed to be exactly one logical dataset — it may contain several, or a dataset may span more than one folder.

**Reason:** The user works from local folders that already hold real evidence (screenshots, exports, analysis documents); the system must be able to reason about that material safely before any of it becomes part of the repository.

## Decision 011 — Scrapling Is External Research Tooling

**Status:** Accepted

Scrapling (`docs/TOOLS_INSTALLED.md`) may later support explicitly authorized web-research/data-acquisition tasks. It is developer/research tooling, installed in an isolated user-level environment, and it does not determine:

- the production database or data model (`docs/Database.md`);
- RAG/retrieval architecture;
- the memory system;
- competitor-ingestion policy.

No automated scraping is enabled during Phase 0.5 or Phase 1. Live scraping is not authorized before Phase 8 (`docs/Phases.md`), and even then only under the boundaries in `docs/Security.md` §6, including mandatory use of `--ai-targeted` for any AI-facing extraction (`docs/Security.md` §5, `docs/TOOLS_INSTALLED.md`).

**Reason:** Scrapling was added as a convenience research tool per this task's request, but the project's existing rule that external tooling never determines production architecture (`AGENTS.md`, External tool boundaries) applies to it exactly as it applies to every other installed tool.

## Decision 012 — Phase 1 Local SQLite Inventory Catalog

**Status:** Accepted

During Phase 1, the YouTube Intelligence OS may use a local SQLite database as a machine-readable inventory/catalog alongside the human-readable manifests in `data/manifests/`. The SQLite catalog is **not** the final production intelligence database.

Its Phase 1 purpose is limited to recording:

- datasets
- ingestion runs
- source locations
- source files
- archive members
- SHA-256 hashes
- basic file metadata
- classifications
- provenance
- duplicate/revision relationships
- ingestion status
- verification status
- ingestion errors

It must **not** yet become the storage system for:

- embeddings
- vectors
- RAG
- generated content ideas
- final insights
- title intelligence
- thumbnail intelligence
- script intelligence
- content recommendations

Final PostgreSQL/Supabase/vector/RAG architecture remains undecided (Decision 004). The SQLite design (`schemas/inventory/`) must remain migration-friendly — additive, versioned schema files, no destructive changes to shipped tables.

**Reason:** Phase 0.5's Markdown-only discovery reports proved sufficient for four small folders, but reliably answering "what data do we own, where did it come from, and is it still trustworthy" at real ingestion volume needs a queryable, hash-indexed catalog. A minimal SQLite catalog gives that without prematurely choosing (or building) production infrastructure.

## Decision 013 — Raw Payloads and Runtime Database Stay Local by Default

**Status:** Accepted

Large/raw source payloads and the operational SQLite database must not be blindly committed into Git history.

Git versions:

- source code
- database schema
- migrations
- documentation
- manifests
- non-sensitive metadata
- project decisions
- tests

Local filesystem storage holds:

- copied immutable raw datasets (`data/raw/`)
- operational `.db` files (`data/catalog/*.db`)
- SQLite WAL/SHM files
- other potentially large runtime data

The actual source files remain primary evidence. The human-readable manifest is the durable ingestion record. The SQLite catalog is the fast machine-readable index.

```text
ORIGINAL SOURCE
=
PRIMARY EVIDENCE

MANIFEST
=
DURABLE INGESTION RECORD

SQLITE
=
MACHINE-READABLE CATALOG / INDEX
```

The SQLite database must be rebuildable from the canonical raw files, manifests, and schema where practical (`data/catalog/README.md`).

**Reason:** Repository size and history hygiene matter as raw datasets grow; the project's existing rule that Git does not blindly absorb `data/raw/` (`README.md`, "Git and large raw data") extends naturally to the new runtime database, which is regenerable and not itself evidence.

## Decision 014 — Mutable Platform Metrics Are Append-Only Snapshots

**Status:** Accepted

YouTube/video/channel metrics change over time. Fields such as views, likes, comments, subscriber counts, views/day, and engagement calculations must never be treated as permanent properties of a video or channel.

They must be stored as timestamped source snapshots (`channel_snapshots`, `video_snapshots`, `schemas/inventory/002_structured_registration.sql`). Future ingestion of the same video/channel at another date must create another snapshot rather than overwrite historical evidence — enforced by a `UNIQUE (video_id/channel_id, dataset_id, observed_at)` constraint, not just convention.

Stable identity (`channels`, `videos`) and mutable observations (`channel_snapshots`, `video_snapshots`) must remain separate tables.

**Reason:** `YouTube_Master_Data.xlsx` captures a single scrape date (24 Aug 2026); a later re-scrape of the same channels/videos is a certainty, not a hypothetical, and overwriting the 24 Aug 2026 values in place would destroy the only historical evidence this project has of that point in time.

## Decision 015 — Structured Fields Require Source Provenance

**Status:** Accepted

Every important structured value registered from supplied datasets must remain traceable to its evidence source. Where practical, provenance must identify: the dataset; the source file; the workbook sheet/row/column, or the archive member and header/body location; the extraction method; the observed/scraped date; and the value's origin and evidence type.

The system must distinguish `SOURCE_EXTRACTED` (e.g. a workbook cell copied directly from scraper output), `SOURCE_DECLARED` (e.g. a workbook verification/notes statement), `SOURCE_COMPUTED` (e.g. the "Views/Day" and "Engagement" columns, which the workbook itself computes via live formulas), `TRANSCRIPT_METADATA` (a transcript file's own header fields), `ARCHIVE_OBSERVED`, and `SYSTEM_VERIFIED` (a count or hash our own tooling produced). No computed workbook metric may be silently represented as if directly reported by YouTube.

Implemented as `field_provenance` (`schemas/inventory/002_structured_registration.sql`) with a `CHECK` constraint requiring exactly one target entity per row, so a provenance record can never float free of the value it documents.

**Reason:** `docs/Database.md` §1 already requires distinguishing fact from interpretation at the record level; Phase 1B is the first phase that registers real structured values, so this decision extends that requirement from a design principle into an enforced schema constraint before any value/formula distinction could be lost.

## Decision 016 — Content Domain and Editing Style Are Independent Dimensions

**Status:** Accepted

A channel or video's subject-matter niche (`content_domain`, `sub_niche`, `target_audience`) and its production/editing grammar (`editing_style`, camera/motion/transition vocabulary) must never be collapsed into one concept or inferred from each other. A health channel and a finance channel may share an editing style; two channels in the same niche may use completely different production styles — neither direction may be assumed.

`editing_style` may only be set from evidence of actual moving-image content — real video, representative frames, keyframes, shot manifests, or an equivalent forensic report (`docs/Database.md`, `visual_reconstruction_cards`-style evidence). It must remain `UNKNOWN` when only channel-page or video-thumbnail screenshots exist, even when those screenshots strongly suggest a niche or packaging pattern. Packaging/thumbnail-style observations (doctor-led, warning framing, before/after, number-led, high-contrast, etc.) are a separate, screenshot-supportable dimension (`packaging_style`) and must never be reported as `editing_style`.

Implemented as independent columns on `entity_classifications` (`schemas/inventory/003_multimodal_source_registration.sql`): `content_domain`, `sub_niche`, `target_audience`, `content_format`, `packaging_style`, `thumbnail_style`, `presenter_style`, `editing_style` — the last defaulting to `UNKNOWN` and never populated from screenshot-only evidence during Phase 1C.

**Reason:** Phase 1C ingested 8 competitor folders that are channel/video-page screenshots only, with no actual video frames — a real, immediate case where niche is screenshot-evidenced but editing style is not, and where collapsing the two would have silently fabricated a production-style claim with no supporting evidence.

## Decision 017 — Canonical GitHub Remote

**Status:** Accepted

The local canonical repository:

`/Users/ghilmanislam360/Documents/youtube-intelligence-os`

now has a canonical GitHub remote:

`ghilmanITM360/youtube-intelligence-os` — https://github.com/ghilmanITM360/youtube-intelligence-os

- **Visibility:** PRIVATE
- **Default branch:** `main`
- **`origin`** points at this repository; `main` tracks `origin/main`.

GitHub stores the durable project layer only: code, schema migrations, scripts, tests, documentation, database-generated manifests, and project skills. GitHub does **not** store the raw ingested corpus or the operational SQLite catalog (`data/catalog/youtube_inventory.db`) — both remain local-only per Decision 013. No credentials, tokens, or other secrets are recorded in this decision or anywhere else in the repository.

The local repository remains the working copy; GitHub is a remote backup/collaboration target, not a second source of truth.

**Reason:** Phase 1C's ingestion work is now substantial enough (16 datasets, 45,774 discovered files, a tested ingestion pipeline) that it needs off-machine durability and a reviewable history, without changing where raw evidence or the operational database actually live.

## Decision 018 — Controlled Apify YouTube Acquisition

**Status:** Accepted

`streamers/youtube-scraper` is the approved provider for explicitly authorized competitor-channel acquisition. This is a narrow Phase 1D registration workflow, not competitor strategy analysis or uncontrolled web research.

Each run must be bounded before execution by current event pricing and a user-approved cost cap; omit Shorts, livestreams, date filtering, and paid AI add-ons unless separately authorized. Actor/run/build metadata, sanitized input, result counts, exact finalized cost, channel URL, transcript configuration, and field-level provenance are recorded. `APIFY_TOKEN` is environment-only and is never printed or persisted.

Platform metrics remain append-only snapshots. Existing screenshot evidence remains unchanged and can be linked to a registered channel only by strong identity evidence such as an exact handle, canonical URL, or YouTube channel ID. Similar names alone never authorize a merge. Transcript/script evidence does not establish editing-style evidence.

**Reason:** The Dr. Aliza Wright pilot demonstrated a bounded, provenance-safe acquisition with an existing Tier B screenshot dataset and a live structured source. A durable decision is required because this is an explicit exception to the earlier no-live-scraping Phase 1 boundary, while preserving every other evidence, security, and analysis boundary.
