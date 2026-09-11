# UI ↔ Backend Handoff (2026-09-11)

Scoped specifically for whoever picks up UI development next. Companion to
`docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md`, which explains the
whole system; this document is the action-oriented summary for starting UI work.

Backend verified state at handoff time: `main` HEAD `5629687`, matching `origin/main` and
live remote main exactly. 285/285 tests passing, DB integrity `ok`, 0 FK violations,
freshness registry 32/32 `CURRENT`. This UI branch (`ui/v1`) was cut directly from that
verified `origin/main` and contains **no backend changes** — only this handoff doc and the
companion audit doc.

---

## Backend Capabilities (summary)

- Ingestion/registration for structured YouTube exports and multimodal sources (documents,
  images, OCR/semantic pipelines).
- Classification engine: topic (AI-assisted, `PROPOSED`) + format (deterministic,
  `VERIFIED`) per video, with full provenance.
- Topic, packaging, hook, and script intelligence: generalized, working across all 5
  channels via unmodified generic reporters.
- Editing/visual intelligence: working, but evidence-gated — real output only for
  CH-000004 (the only channel with registered forensic video evidence); graceful
  `NOT_AVAILABLE` elsewhere.
- Channel strategy intelligence: one generic engine, validated bidirectionally across 2
  niches (finance, health); produces an evidence-backed action taxonomy (`CONTINUE`,
  `DOUBLE_DOWN`, `FIX`, `REDUCE`, `STOP`, `TEST`, `WATCH`).
- Competitor benchmark + new-channel blueprint: working for the 2 benchmarked niches only.
- Cross-niche calibration: working, but current evidence depth (2 channels/niche, 2 niches)
  yields low-confidence cross-niche conclusions — this is expected and honestly reported,
  not a defect.
- Unified orchestrator: composes all layers into a per-channel content plan with graceful
  per-layer degradation.
- Incremental refresh: deterministic dependency-graph-based planner + executor, with a
  freshness registry, dry-run mode, and full historical versioning of artifacts. Verified
  live: `NO_REFRESH_REQUIRED`, 32/32 artifacts current.
- First-party YouTube Analytics ingestion (CSV/TSV/XLSX): capability-complete and fully
  tested against synthetic fixtures; own-channel diagnostic enrichment ready for real data;
  **no real first-party export has been ingested** — this is the single biggest evidence
  gap in the system today.

## Backend Data Sources

- **Canonical SQLite catalog:** `data/catalog/youtube_inventory.db` (gitignored,
  machine-local). 27 tables, schema migrations 1–10. Read-only access pattern already
  established via `scripts/report_common.py`'s `connect()` helper (`mode=ro` URI).
- **Derived intelligence artifacts:** versioned JSON + Markdown under
  `data/intelligence/{channels,cross-channel,blueprints,plans,system}/` (committed to git,
  except gitignored `data/intelligence/first-party/` for private analytics).
- **Freshness registry:** `data/intelligence/system/intelligence-freshness-registry.json` —
  the single authoritative index of which artifacts exist and whether they're current.
- **Manifests:** `data/manifests/` — dataset/batch provenance records (committed).

## UI-Readable Artifacts Today

Channel/cross-channel/system intelligence JSON files are already reasonably
UI-friendly: consistent envelope conventions (evidence layer, generation method, source
hashes, channel scoping), machine-parseable, versioned by filename date. A UI could read
these directly as static files for a first read-only pass, but see the recommended adapter
below before building anything that needs to stay in sync live.

## Recommended Read Model

See the full per-concept table in §33 of the companion audit doc
(`YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md`). Summary: most
intelligence-artifact-backed UI concepts (Topic, Packaging, Hook, Script, Editing, Strategy
Diagnosis, Competitor Benchmark, Blueprint, Content Plan, Refresh Status) are **High
readiness** with **no adapter needed** beyond a query wrapper. Concepts that need raw DB
access (Channels, Channel Profile, Videos, Evidence/Provenance, System Health) need a **thin
read-service layer** — none exists yet.

## Proposed UI Modules/Screens

Overview · Channels · Channel Detail · Videos · Intelligence · Strategy Diagnosis ·
Competitor Compare · Blueprints · Content Plans · Evidence Explorer · Import Data · Refresh
Center · System Health. (Full rationale per module in §34 of the companion audit.)

## Actions and Permissions

| Tier | Examples | UI Permission Implication |
|---|---|---|
| READ_ONLY | View any intelligence artifact, view system health/freshness | Available to any authenticated UI user |
| SAFE_DERIVED_ACTION | Refresh dry-run, confirmed refresh execution, registry regeneration | Available to any authenticated UI user, but should require an explicit confirm click |
| CANONICAL_MUTATION | Ingest first-party analytics, register a channel/dataset/classification, acquire thumbnails | Should require a distinct, higher permission tier + explicit confirmation |
| EXTERNAL_ACTION | Apify acquisition (network + cost), any live YouTube publish action | Apify: higher tier + cost-cap visibility. Publish: **currently entirely unsupported** by this backend — do not build a UI affordance implying it exists |

Full classification and rationale: §35 of the companion audit.

## Missing Adapter/Service Layer

This is the **primary blocker** for UI development, not data or intelligence coverage:

- No HTTP/API boundary exists between the SQLite catalog + JSON artifacts and any client.
- No stable, typed contract exists for "list channels," "get channel profile," "list videos
  for a channel," or "get current system health" — these require new, thin wrapper code
  around the existing read-only `report_common.connect()` pattern.
- Recommendation: build this as a **new, additive** layer (e.g. a small local read API or a
  typed Python query module the UI's backend-for-frontend calls into) that wraps existing
  scripts/queries rather than modifying them — preserves the 285-test baseline and the
  freshness registry untouched.
- Mutating actions (ingestion, refresh execution, thumbnail acquisition) should be exposed
  through explicit, individually-confirmed endpoints/commands — never a generic
  "run arbitrary script" affordance.

## UI-Specific Risks

- **Don't let the UI imply capabilities the backend doesn't have** — most importantly, do
  not build any "publish to YouTube," live-API, or auto-generated-content affordance; none
  of that exists or is planned per current project scope (`AGENTS.md`, `docs/Phases.md`).
- **Don't fabricate example data** for channels/niches without a benchmark/blueprint (e.g.
  CH-000004's science niche) — render this as an honest empty/unavailable state, consistent
  with how the backend itself reports `NOT_AVAILABLE`.
- **Don't expose the raw SQLite file or its schema directly to any client boundary** — build
  the adapter layer first.
- **Respect the evidence-layer distinction in the UI itself** — if a value is
  `AI_INTERPRETATION`/`PROPOSED`/`HYPOTHESIS`, the UI should visually distinguish it from
  `EXTRACTED_FACT`/`VERIFIED`/`MEASURED_FACT` rather than flattening everything into one
  visual style. This is the system's core value proposition; a UI that erases the
  distinction defeats the point of the backend.
- **First-party analytics privacy:** first-party data is intentionally gitignored/local-only
  and never shared as competitor evidence. Any UI import flow must preserve this — never
  surface one channel's first-party metrics as another channel's data, and never sync
  first-party artifacts to a shared/remote store without the user's explicit, separate
  authorization.

## Recommended First UI Milestone

Build the **read-only Overview + Channels + Channel Detail** modules against a small new
read-service layer (wrapping SQLite read-only access + freshness-registry-aware artifact
loading), with **no mutating actions** in this first milestone. This validates the
adapter-layer approach on the best-covered part of the backend (topic/packaging/hook/script
intelligence exists for all 5 channels) before extending to Strategy Diagnosis, Competitor
Compare, and eventually the CANONICAL_MUTATION-tier Import Data / Refresh Center screens.
