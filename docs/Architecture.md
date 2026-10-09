# Architecture

This document describes the architectural vision for the YouTube Intelligence OS. It records current implementation alongside longer-term planning. Every section is labeled:

- **CURRENT** — actually built and running today.
- **PLANNED** — decided in direction, not yet implemented.
- **FUTURE / UNDECIDED** — a real future need whose concrete design (technology, schema, provider) is intentionally not chosen yet.

See `docs/Phases.md` for how these arrive over time, `docs/Database.md` for the conceptual data model, and `docs/DECISIONS.md` for the accepted decisions this document assumes.

## 1. What exists today — CURRENT

- A documentation-first repository at the canonical path (Decision 009) with stdlib ingestion, registration, validation, and read-only reporting scripts.
- The broader registry validates 75 canonical channels and 33 datasets (2026-10-09); the selected inventory contains 10 channels and 26 datasets. These populations have distinct roles — see `docs/YOUTUBE_CHANNEL_REGISTRY.md` and `data/catalog/README.md`.
- Two generated SQLite databases with distinct roles: the committed selected-inventory catalog (`data/catalog/youtube_inventory.db`) and the Git LFS-tracked, committed cross-channel query registry (`data/catalog/youtube_channel_registry.db`). Neither is the final production database.
- Structured channels/videos, append-only snapshots, transcript references, screenshot/multimodal evidence, field provenance, and bounded Apify source-run provenance through Phase 1D.
- External developer/agent tooling (Graphify, Ponytail, Claude-Mem, Obsidian skills, Scrapling) recorded in `docs/TOOLS_INSTALLED.md`. None of it is part of the application.

### V1 intelligence and What If forensic flow — CURRENT

Topic, Packaging, Hook/Script and evidence-eligible Editing/Visual builders feed `scripts/run_youtube_intelligence.py`. The orchestrator reads canonical artifacts and catalog identities to produce traceable production plans. Channel Strategy is generalized with explicit evidence-coverage limitations; UI/RAG/agents/API services remain outside this V1 architecture.

What If external corpus (configured `YIOS_WHAT_IF_CORPUS_ROOT`) is validated by release/table/media hashes. The read-only adapter loads eight canonical MASTER tables; normalized staging lives under ignored `data/staging/what-if-forensic/v1.0.0/`. Promotion validates staging and commits a compact identity/provenance index. The evidence-query layer validates that index against staged bytes, summarizes matching existing videos, and enriches production-plan Editing/Visual blueprints with cited hypotheses. It never adds forensic rows to channel sample counts or overwrites catalog snapshots. Missing local staging is unavailable, while changed evidence fails closed.

See [integration lifecycle](WHAT_IF_INTEGRATION_WORKFLOW.md) for update, regeneration, rollback and privacy boundaries. Remaining conceptual sections retain their own PLANNED or FUTURE labels where implementation has not been authorized.

## 2. The conceptual end-to-end flow — PLANNED (sequence), FUTURE / UNDECIDED (implementation of each stage)

```text
USER-SUPPLIED SOURCE
        ↓
SOURCE DISCOVERY
        ↓
DATASET INVENTORY
        ↓
HASHING / DEDUPLICATION
        ↓
SEMANTIC CLASSIFICATION
        ↓
RAW PRESERVATION
        ↓
EXTRACTION
        ↓
NORMALIZATION
        ↓
EVIDENCE / OBSERVATIONS
        ↓
REUSABLE INTELLIGENCE
        ↓
CHANNEL-SPECIFIC INTELLIGENCE
        ↓
COMPETITOR ANALYSIS
        ↓
PATTERN / OUTLIER / GAP DISCOVERY
        ↓
TOPIC HYPOTHESES
        ↓
INTERNAL RANKING
        ↓
WEB RESEARCH / VALIDATION
        ↓
RE-ANALYSIS
        ↓
FINAL OPPORTUNITY
        ↓
TITLE / THUMBNAIL / SCRIPT / VISUAL PLAN / PRODUCTION PLAN
```

Notes on this flow:

- Every stage after RAW PRESERVATION reads from, and never overwrites, the layer before it. A source's raw bytes stay reachable from any later output through provenance links (see `docs/Database.md`, provenance model).
- SOURCE DISCOVERY and DATASET INVENTORY are what this Phase 0.5 task exercised manually against four external folders (`docs/source-discovery/`). They are not yet automated tooling — they are a demonstrated, repeatable procedure.
- WEB RESEARCH / VALIDATION is downstream of internal analysis (Decision 007): the system reasons over supplied evidence first, and only reaches outward to validate or fill gaps. Scrapling (`docs/TOOLS_INSTALLED.md`, Decision 011) is a candidate tool for that stage only, and only when a later phase explicitly authorizes it.
- TITLE / THUMBNAIL / SCRIPT / VISUAL PLAN / PRODUCTION PLAN is the eventual output surface. No format, template, or generation pipeline for these is decided.

## 3. Future channel separation — PLANNED (concept), FUTURE / UNDECIDED (mechanism)

```text
GLOBAL KNOWLEDGE
        │
        ├── Channel A Brain
        ├── Channel B Brain
        ├── Channel C Brain
        └── Channel D Brain
```

GLOBAL KNOWLEDGE holds material that is true regardless of which channel uses it — algorithm mechanics, storytelling craft, editing grammar, retention principles (Class A in `docs/DATA_CLASSIFICATION.md`). A "Channel Brain" holds everything specific to one channel: its own videos, its own competitors, its own audience, its own prior experiments (Class F). Decision 006 already requires this separation; what is undecided is how a Channel Brain is physically represented (a folder convention, a database partition, a namespaced vector index, or something else) and how much of GLOBAL KNOWLEDGE a Channel Brain is allowed to override.

## 4. Boundaries — PLANNED

- **Canonical repository** — the single source of truth for documentation, decisions, and (once ingested) manifests and small structured records. Never a temporary Codex task workspace (Decision 009).
- **Source folders** — user-owned, external, read-only until a controlled ingestion decision is made for them (Decision 010). The system reads them; it does not adopt them as extensions of the repository.
- **External tools** — Graphify, Ponytail, Claude-Mem, Obsidian skills, Scrapling. Convenience layers only. Their internal graphs, caches, embeddings, or memory stores are never canonical project knowledge and never override repository evidence (`docs/AGENTS.md`, `docs/Security.md`).
- **Agent memory** — session or cross-session memory used by an agent while working. Auxiliary only, same rule as external tools.
- **Future structured database** — where inventory, provenance, and evidence records eventually live once real datasets justify a schema. Not chosen yet (`docs/Database.md`).
- **Future semantic retrieval** — embeddings/RAG over normalized or intelligence-layer content, for stages like pattern discovery or topic hypothesis generation. Not chosen yet, and explicitly out of scope for Phase 0.5 and Phase 1.
- **Future web research** — Scrapling remains reserved for the WEB RESEARCH / VALIDATION stage. The separately authorized, bounded Apify competitor-acquisition adapter is limited to structured Phase 1D registration (Decision 018), not research or analysis.

No final database, vector-search, or web-acquisition architecture is chosen in this document. That choice is deferred until real ingested datasets make the tradeoffs concrete (Decision 004).

## 5. Source-folder architecture — PLANNED

The system must support being pointed at an arbitrary external folder and asked to understand it before anything is copied or transformed:

```text
Ingest this folder:
/path/to/source
```

Conceptual behavior:

```text
External Source Folder
        ↓
READ-ONLY DISCOVERY
        ↓
Inventory
        ↓
Hashes
        ↓
Logical Dataset Detection
        ↓
Noise Detection
        ↓
Canonical Evidence Detection
        ↓
Manifest
        ↓
Controlled Ingestion Decision
```

Rules that follow from this shape:

- The original external folder is never modified, moved, renamed, or reorganized by discovery. Discovery only reads and records.
- "Logical Dataset Detection" is explicitly not "one folder = one dataset" — a single folder can contain multiple unrelated logical datasets, and a dataset can span multiple folders (an archive plus its already-extracted copy, for example). `docs/source-discovery/SOURCE_DATASET_INVENTORY.md` demonstrates this against real folders.
- "Controlled Ingestion Decision" is a recommendation, not an action. Discovery produces a manifest and a proposed priority; a separate, later, explicit step performs any actual copy into `data/raw/`.
- This is the procedure Phase 0.5 exercised by hand. Whether it becomes a script, a skill, or an agent workflow in a later phase is FUTURE / UNDECIDED — Phase 0.5 only establishes that the procedure works and what it must preserve.
