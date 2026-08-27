# Phases

A phased roadmap for the YouTube Intelligence OS. Names and boundaries here are directional, not immutable — a later phase may split, merge, or reorder these if real evidence demands it, subject to an explicit decision recorded in `docs/DECISIONS.md`.

Database, RAG/vector-search, MCP servers, and agent-workflow infrastructure are **not** Phase 0.5 or Phase 1 work anywhere in this roadmap. They first appear as design work in Phase 10–11, and even then, only after real datasets justify specific choices (Decision 004).

---

### Phase 0 — Foundation Definition
**Status: COMPLETED**

- **Objective:** Establish the canonical repository, its directory layout, core rules, and initial documentation.
- **Inputs:** None (greenfield).
- **Outputs:** Repository skeleton, `README.md`, `AGENTS.md`, `docs/PROJECT_SCOPE.md`, `docs/DECISIONS.md` (001–009), `docs/DATA_CLASSIFICATION.md`, `docs/DATA_ENTRY_WORKFLOW.md`, `docs/DATA_INVENTORY.md`, `docs/TOOLS_INSTALLED.md`.
- **Allowed:** Documentation, directory scaffolding, external convenience-tool installation.
- **Prohibited:** Real data ingestion, infrastructure, application code.
- **Completion criteria:** Initial commit exists; rules are documented; no real data ingested. Met.
- **Dependencies:** None.

---

### Phase 0.5 — Foundation Hardening & Source Discovery
**Status: CURRENT**

- **Objective:** Add Scrapling as external research tooling; write the architecture/planning documents this roadmap depends on; deeply inspect real external source folders without ingesting them; produce recommendations for controlled ingestion.
- **Inputs:** Four external source folders (read-only); the Scrapling upstream repository.
- **Outputs:** `docs/Architecture.md`, `docs/Phases.md` (this file), `docs/Database.md`, `docs/Prompts.md`, `docs/Security.md`, `docs/Error_Handling.md`; `docs/source-discovery/` reports; Scrapling installed and documented; Decisions 010–011.
- **Allowed:** Read-only inspection, hashing, content reading, safe archive listing, planning documentation, installing external developer tooling in isolated user-level scope.
- **Prohibited:** Modifying/moving/deleting anything in the four source folders; ingesting real data into `data/`; scraping any live target; choosing final database/RAG technology; writing SQL or migrations.
- **Completion criteria:** All six foundation documents exist; all four source folders inspected and reported on; Scrapling installed and verified without live scraping; source-discovery reports exist; source folders provably untouched; Phase 0.5 work committed.
- **Dependencies:** Phase 0.

---

### Phase 1A — Controlled Data Entry & Inventory
**Status: COMPLETED**

- **Objective:** Begin actually copying selected, prioritized source material into `data/raw/` under the workflow `docs/DATA_ENTRY_WORKFLOW.md` already defines, using the priorities `docs/source-discovery/SOURCE_INGESTION_RECOMMENDATIONS.md` proposes; introduce a minimal local SQLite inventory/catalog (Decision 012) alongside the manifests.
- **Inputs:** User decision on which Phase 0.5 recommendation(s) to act on first (DS-000001, DISC-002).
- **Outputs:** Populated `data/raw/`, `data/manifests/DS-000001.md`, `docs/DATA_INVENTORY.md` entry, `schemas/inventory/001_initial.sql`, `scripts/inventory_catalog.py`.
- **Allowed:** Copying explicitly approved source material; hashing; basic inventory; exact-duplicate detection; recording provenance.
- **Prohibited:** Automated bulk ingestion of everything discovered in Phase 0.5; extraction/normalization; any competitor/content analysis; any web research.
- **Completion criteria:** At least one controlled testcase ingested with full provenance and no source modification. Met — DS-000001 ingested, 8/8 tests passing, source hashes verified unchanged.
- **Dependencies:** Phase 0.5 (its manifest and recommendations are the input).

---

### Phase 1B — Structured Source Registration
**Status: COMPLETE**

- **Objective:** Convert a Phase 1A-ingested dataset's raw files into structured, provenance-tracked catalog entities (channels, videos, channel/video snapshots, transcript references) without performing competitor strategy analysis, topic generation, or content scoring.
- **Inputs:** DS-000001's canonical raw files and Phase 1A catalog records.
- **Outputs:** `schemas/inventory/002_structured_registration.sql`, `scripts/register_structured_source.py`, `scripts/source_adapters/`, populated `channels`/`channel_snapshots`/`videos`/`video_snapshots`/`transcripts`/`field_provenance` tables, updated manifest and `docs/DATA_INVENTORY.md` status.
- **Allowed:** Source parsing, structured registration, identity resolution, metric snapshots, transcript metadata, field provenance, source cross-checking, validation, database migration, tests.
- **Prohibited:** Competitor strategy analysis, viral/topic/title/thumbnail/script analysis, content-gap discovery, recommendations, ranking, embeddings, RAG, vectors, web research, scraping.
- **Completion criteria:** Structured entities registered for DS-000001 with 100% field-provenance coverage on required fields, source reconciliation with no unexplained discrepancy, migration tests passing, SQLite integrity clean, manifest/database agreement.
- **Dependencies:** Phase 1A.

---

### Phase 1C — Recursive Multi-Source & Multimodal Ingestion
**Status: COMPLETE**

- **Objective:** Bulk-ingest 12 authorized external source roots (competitor screenshot folders, a YouTube-training document corpus, a standalone forensic-video evidence set, and the historical `Documents/Codex` forensic-video archive) with 100% recursive file coverage and 100% disposition coverage — every discovered filesystem item explicitly classified (`INGEST`/`REFERENCE_ONLY`/`EXACT_DUPLICATE`/`NOISE`/`TOOLING`/`HOLD`/etc.), never silently skipped.
- **Inputs:** 12 user-supplied local folder paths (`BATCH-000001`).
- **Outputs:** `schemas/inventory/003_multimodal_source_registration.sql`, `schemas/inventory/004_discovered_files_fk_indexes.sql`, `scripts/register_batch.py`, `scripts/source_adapters/batch_rules.py`, `scripts/image_pipeline.py`, `scripts/image_text_recognition.swift`, `scripts/load_ocr_results.py`, `scripts/load_semantic_results.py`, `scripts/load_document_results.py`, `scripts/generate_batch_manifests.py`, 15 new registered datasets (`DS-000002`–`DS-000016`), `data/manifests/batches/BATCH-000001.md` + coverage ledger CSV, per-dataset manifests, `.codex/skills/multimodal-source-ingestion/`.
- **Allowed:** Discovery, hashing, deduplication (exact + perceptual), image OCR/metadata/semantic inspection, document characterization, channel/video-page screenshot observation registration, classification (content domain, packaging style — kept independent of editing style), database migration, tests.
- **Prohibited:** Competitor strategy analysis, viral analysis, topic clustering/generation, title/thumbnail/script recommendations, content-gap discovery, ranking, embeddings, RAG, vectors, web research/scraping, inferring editing style from screenshots alone.
- **Completion criteria:** `TOTAL_DISCOVERED_FILES == TOTAL_FILES_WITH_DISPOSITION` (45,774 = 45,774); every unique competitor/evidence screenshot (122) OCR'd and semantically inspected; all 17 training-corpus documents characterized including the Hook-pair content comparison; every image (including 42,535 Codex files) hashed and perceptually clustered; source integrity re-verified (0 mismatches across 42,678 hashed files); migration/registration tests passing; SQLite integrity clean. Met.
- **Dependencies:** Phase 1A, Phase 1B.

---

### Phase 2 — Data Classification & Provenance

- **Objective:** Apply semantic classification (`docs/DATA_CLASSIFICATION.md` classes A–H) and the evidence-layer model (`docs/Database.md`) to ingested material; formalize provenance records.
- **Inputs:** Phase 1 ingested data and manifests.
- **Outputs:** Classified, provenance-tagged records for each ingested file/dataset.
- **Allowed:** Classification, provenance tagging, revision/duplicate resolution beyond exact-hash matching.
- **Prohibited:** Extraction pipelines, database technology selection.
- **Completion criteria:** Every ingested item has a recorded semantic class and evidence layer.
- **Dependencies:** Phase 1.

---

### Phase 3 — Extraction & Normalization

- **Objective:** Turn raw evidence into extracted, then normalized, structured representations (text from PDFs/DOCX, transcripts from video, OCR from images) without interpretation.
- **Inputs:** Classified raw evidence.
- **Outputs:** `data/extracted/`, `data/normalized/` content with provenance links back to raw sources.
- **Allowed:** Deterministic extraction and format normalization.
- **Prohibited:** Analytical interpretation being stored as fact; database technology selection.
- **Completion criteria:** Normalized representations exist and trace to their raw source.
- **Dependencies:** Phase 2.

---

### Phase 4 — Reusable Intelligence Extraction

- **Objective:** Produce the first AI_INTERPRETATION / OBSERVATION layer outputs (see `docs/Database.md` provenance model) from normalized data — e.g., reusable Global YouTube Knowledge (Class A) distilled from training documents.
- **Inputs:** Normalized data from Phase 3.
- **Outputs:** `data/intelligence/` records, each tagged with its evidence layer and confidence.
- **Allowed:** AI-assisted analysis, explicitly labeled as interpretation, never silently promoted to fact.
- **Prohibited:** Treating any AI output as ground truth without labeling.
- **Completion criteria:** Intelligence records exist with evidence-layer tags and traceable provenance.
- **Dependencies:** Phase 3.

---

### Phase 5 — Channel Brains

- **Objective:** Stand up the first Channel-Specific Intelligence partition(s) (`docs/Architecture.md` §3), separating one channel's evidence and interpretations from another's.
- **Inputs:** Classified, channel-tagged evidence and intelligence.
- **Outputs:** At least one working Channel Brain structure.
- **Allowed:** Channel-scoped organization of existing intelligence.
- **Prohibited:** Cross-channel leakage of channel-specific rules or evidence.
- **Completion criteria:** Two channels' material demonstrably does not cross-contaminate.
- **Dependencies:** Phase 4, Decision 006.

---

### Phase 6 — Competitor Intelligence

- **Objective:** Turn Class B (Competitor Evidence) into structured competitor intelligence — packaging patterns, performance benchmarks, content gaps — per Decision 007 (internal evidence before web validation).
- **Inputs:** Competitor evidence ingested and classified in earlier phases.
- **Outputs:** Competitor-intelligence records linked to their source evidence.
- **Allowed:** Internal comparative analysis.
- **Prohibited:** Live web scraping of competitors (still requires explicit authorization).
- **Completion criteria:** At least one competitor's evidence is fully turned into structured, traceable intelligence.
- **Dependencies:** Phase 5.

---

### Phase 7 — Opportunity Engine

- **Objective:** Implement pattern/outlier/gap discovery and topic-hypothesis generation over accumulated intelligence (`docs/Architecture.md` §2 flow, PATTERN/OUTLIER/GAP DISCOVERY → TOPIC HYPOTHESES → INTERNAL RANKING).
- **Inputs:** Channel and competitor intelligence.
- **Outputs:** Ranked internal topic hypotheses.
- **Allowed:** Internal analysis and ranking logic.
- **Prohibited:** Treating a hypothesis as a validated opportunity before Phase 8.
- **Completion criteria:** Hypotheses are generated, ranked, and traceable to the evidence that produced them.
- **Dependencies:** Phase 6.

---

### Phase 8 — Web Research & Validation Loop

- **Objective:** Validate top-ranked hypotheses against live web research, then re-analyze against internal data (Decision 008's iterative loop). This is the first phase where live web acquisition tooling (candidate: Scrapling, Decision 011) may be authorized for real use.
- **Inputs:** Ranked hypotheses from Phase 7.
- **Outputs:** Validated or rejected hypotheses, each with research provenance (source URL, retrieval timestamp).
- **Allowed:** Explicitly authorized, rate-limited, provenance-preserving web research (`docs/Security.md`, Scraping Boundaries).
- **Prohibited:** Uncontrolled/unbounded crawling; scraping without `--ai-targeted` on AI-facing output.
- **Completion criteria:** At least one hypothesis is carried through research and re-analysis to a final opportunity.
- **Dependencies:** Phase 7, explicit authorization for Scrapling use.

---

### Phase 9 — Title / Thumbnail / Script / Visual Intelligence

- **Objective:** Turn a final opportunity into the concrete production surface: title options, thumbnail concepts, script, visual/production plan.
- **Inputs:** Final opportunities from Phase 8.
- **Outputs:** Structured content-production drafts, each traceable to the opportunity and evidence behind it.
- **Allowed:** Prompted generation using the registered prompt templates (`docs/Prompts.md`).
- **Prohibited:** Fabricated performance claims presented as measured fact.
- **Completion criteria:** At least one opportunity is carried through to a complete draft production package.
- **Dependencies:** Phase 8.

---

### Phase 10 — Database & Retrieval Infrastructure

- **Objective:** Select and implement real structured storage and (if warranted) semantic retrieval, based on the conceptual entities in `docs/Database.md` and the actual volume/shape of data accumulated by prior phases.
- **Inputs:** All prior-phase data and its observed scale/shape.
- **Outputs:** A production database (and possibly vector index), migrations, and a retrieval layer.
- **Allowed:** Real technology selection and implementation, now justified by real data.
- **Prohibited:** Selecting technology before this phase (Decision 004).
- **Completion criteria:** Structured storage exists, matches the provenance model, and prior-phase data is migrated without loss.
- **Dependencies:** Phases 1–9 (their accumulated data shape the schema).

---

### Phase 11 — Skills / MCP / Agent Workflows

- **Objective:** Build any repeatable agent workflows, MCP servers, or skills the system genuinely needs, now that the underlying data and database layers are real.
- **Inputs:** Phase 10 infrastructure.
- **Outputs:** Production agent workflows/skills, scoped narrowly to demonstrated needs.
- **Allowed:** Automation of already-proven manual workflows.
- **Prohibited:** Speculative automation with no demonstrated manual precedent.
- **Completion criteria:** Each shipped workflow maps to a manual process it replaces.
- **Dependencies:** Phase 10.

---

### Phase 12 — Automation & Continuous Learning

- **Objective:** Ongoing, scheduled operation — continuous ingestion, competitor monitoring, and opportunity discovery, running with minimal manual intervention.
- **Inputs:** All prior infrastructure.
- **Outputs:** Scheduled/automated pipelines.
- **Allowed:** Automation, subject to the same evidence and provenance rules as every manual phase before it.
- **Prohibited:** Any automation that bypasses classification, provenance, or the fact/interpretation distinction.
- **Completion criteria:** The system operates continuously without silent data-quality regressions.
- **Dependencies:** Phase 11.
