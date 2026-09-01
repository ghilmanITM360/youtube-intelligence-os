# Database

## FINAL DATABASE ARCHITECTURE — NOT YET IMPLEMENTED

The Phase 1 local SQLite inventory/catalog is implemented through schema v6 (see §5). It is deliberately not the final production intelligence database. Final technology selection (relational, document, vector, or a mix) happens only in Phase 10 (`docs/Phases.md`), after real ingested datasets have shown what shape the data actually needs (Decision 004).

Everything below is a **conceptual entity list**, not a schema. Entities may be renamed, merged, split, or dropped once real data volume and query patterns are known.

## 1. Provenance model — the part that must not wait

One design constraint is not deferred: the system must be able to tell the difference between a fact and an interpretation, permanently, at the record level. Forensic material already inspected in this Phase 0.5 pass (`docs/source-discovery/SOURCE_DISCOVERY_REPORT.md`) demonstrates why — a single video-analysis document mixes directly measured values (shot durations, pixel offsets from frame-differencing) with AI-generated narrative claims, and explicitly flags where its own confidence drops (`HIGH CONFIDENCE` / `MEDIUM CONFIDENCE` / `LOW CONFIDENCE`, and sections marked `BLOCKED`/`NOT ATTEMPTED` rather than fabricated). Any future database must preserve at least that level of honesty, not silently flatten it.

Every fact-bearing record must carry one of these states:

```text
RAW_SOURCE          — the original supplied bytes/file. Immutable.
EXTRACTED_FACT       — deterministically pulled from a raw source (e.g. a CSV cell, a video's frame rate from ffprobe).
MEASURED_FACT        — computed via a defined, repeatable measurement (e.g. shot-length statistics, hash digests).
OBSERVATION          — a human- or tool-noted fact about a source that isn't a raw field (e.g. "this screenshot shows a vidIQ overlay").
AI_INTERPRETATION    — an AI-generated reading, summary, or judgment. Always traceable to the source(s) it was drawn from.
HUMAN_INTERPRETATION — a person's judgment, recorded as theirs, not as fact.
HYPOTHESIS           — an unvalidated idea (e.g. a topic hypothesis in Phase 7), explicitly not yet a recommendation.
RECOMMENDATION       — a validated, actionable suggestion, still distinct from fact.
SUSPECT              — a claim that looks like fact but has NOT been independently verified (e.g. an unlabeled number in a generated report). Must be surfaced, never silently trusted.
SUPERSEDED           — a record that a newer revision has replaced; kept, not deleted, for audit trail.
```

Rules that follow from this:

- No process may promote `AI_INTERPRETATION` to `EXTRACTED_FACT` or `MEASURED_FACT` without an explicit, separate verification step.
- A `SUPERSEDED` record is never deleted outright; the newer record links back to it. This directly matters for the source material found in Phase 0.5 — see the revision relationships in `docs/source-discovery/SOURCE_DUPLICATE_REPORT.md` (e.g. `Hook (1).pdf` vs. `Hook guide.pdf`, both present, near-identical size, undetermined which is authoritative).
- Every record — regardless of layer — carries a source path/hash back to a `RAW_SOURCE`, all the way down the derivation chain. A `RECOMMENDATION` must be traceable through every intermediate `AI_INTERPRETATION`/`OBSERVATION` back to the `RAW_SOURCE` it ultimately rests on.

## 2. Conceptual entities

For each entity: purpose, probable relationships, provenance requirements, structured vs. unstructured content, and whether the Phase 0.5 source folders actually contain evidence for it yet.

### channels
Purpose: one record per YouTube channel the system tracks (own or competitor). Relationships: has many `videos`, `channel_snapshots`, `content_projects`. Provenance: itself mostly `EXTRACTED_FACT` (channel ID, handle) once scraped/supplied. Structured: yes (ID, handle, URL, join date). Evidence today: `YouTube_Master_Data.xlsx` (`files (1)fulldata (1)`) already contains a full "Channel Overview" sheet for two real channels — directly maps to this entity.

### competitors
Purpose: marks a `channels` record as a tracked competitor rather than an owned channel, with relationship to the owning channel(s) it's compared against. Relationships: many-to-many with `channels`. Provenance: `HUMAN_INTERPRETATION` (a person decided this is a competitor). Evidence today: `Dr. Adewale` folder (screenshots of a 151K-subscriber cardiology-content channel) is exactly this — competitor evidence with no formal `competitors` record yet.

### videos
Purpose: one record per YouTube video, own or competitor. Relationships: belongs to `channels`; has many `video_snapshots`, `transcripts`, `forensic_evidence`. Provenance: `EXTRACTED_FACT` for scraped fields. Structured: yes. Evidence today: `YouTube_Master_Data.xlsx` "All Videos" sheet — 159 rows with title, views, likes, comments, duration, publish date, per video.

### video_snapshots
Purpose: point-in-time metric capture for a video (views/likes/comments change over time; a single `videos` row can't hold history). Relationships: belongs to `videos`. Provenance: `EXTRACTED_FACT`, timestamped. Evidence today: none observed yet — the xlsx captures one scrape date only (24 Aug 2026); no repeated-snapshot data exists in the inspected sources.

### channel_snapshots
Purpose: same idea as `video_snapshots`, at channel level (subscriber count over time). Relationships: belongs to `channels`. Evidence today: none observed — single point-in-time only.

### source_files
Purpose: one record per physical file as supplied (a PDF, a screenshot, an archive member). Relationships: belongs to `datasets`; is the root of the provenance chain for everything derived from it. Provenance: `RAW_SOURCE`. Structured: file-level metadata (path, size, hash, mtime) is structured; the file's own content is not. Evidence today: this is exactly what the SHA-256 hashing in `docs/source-discovery/SOURCE_DUPLICATE_REPORT.md` was computed against.

### datasets / dataset_files
Purpose: `datasets` groups a logical set of `source_files` that belong together (Discovery IDs `DISC-00N` in Phase 0.5 are a preview of this); `dataset_files` is the join table. Relationships: `datasets` has many `dataset_files`, each pointing at one `source_files`. Provenance: the grouping decision is `HUMAN_INTERPRETATION` or `AI_INTERPRETATION`, even though the member files are `RAW_SOURCE`. Evidence today: directly demonstrated — e.g. the 159-video transcript/metadata pair spans two physical files (`Transcripts_All_159_Videos.zip` + `YouTube_Master_Data.xlsx`) that are one logical dataset.

### documents / document_sections
Purpose: `documents` represents a text-bearing source (PDF, DOCX, MD) once its structure is known; `document_sections` breaks it into headings/chapters for retrieval. Relationships: `documents` belongs to `source_files` (extracted from); has many `document_sections`. Provenance: `EXTRACTED_FACT` (text) with `document_sections` boundaries as `OBSERVATION`/`AI_INTERPRETATION` if auto-segmented. Evidence today: the 15 PDFs/DOCX in `all training data of youtube` are unambiguous candidates — e.g. `FORENSIC_RECONSTRUCTION.md` already has clean numbered sections (§0–§13) that would map directly to `document_sections`.

### screenshots
Purpose: one record per image captured from a screen (competitor channel pages, analytics dashboards). Relationships: belongs to `source_files`; may link to `competitors`/`channels`/`videos` once its content is read. Provenance: `RAW_SOURCE` for the image; any read-off values (view counts, titles) are `OBSERVATION`, not `EXTRACTED_FACT`, unless independently corroborated. Evidence today: the 13 `Dr. Adewale` screenshots are exactly this class, complete with legible per-video view counts and VPH figures.

### keyframes
Purpose: individual frames pulled from a video for visual analysis. Relationships: belongs to `videos`/`forensic_evidence`. Evidence today: none directly present, but `EVIDENCE_seven_title_cards.jpg` and `EVIDENCE_temporal_average.jpg` (in `files (1)`) are the aggregate/composite outputs of exactly this kind of frame-level work.

### transcripts
Purpose: full text transcript of a video's spoken audio. Relationships: belongs to `videos`. Provenance: `EXTRACTED_FACT` if auto-captioned by YouTube (as labeled), but the label itself (`auto_generated`) must be preserved — auto-captions carry known error rates. Evidence today: 158 of 159 real transcripts exist in `Transcripts_All_159_Videos.zip`, each with a metadata header naming caption type as `auto_generated`.

### forensic_evidence / forensic_blueprints
Purpose: `forensic_evidence` holds measured, reproducible findings about a specific video's construction (shot count, cut timing, motion parameters); `forensic_blueprints` holds the synthesized reconstruction guidance built from that evidence (reusable prompts, production rules). Relationships: both belong to a `videos` record. Provenance: `forensic_evidence` is largely `MEASURED_FACT` (frame-differencing, SIFT/RANSAC residuals); `forensic_blueprints` is `AI_INTERPRETATION` built on top of it, and must say so. Evidence today: `FORENSIC_RECONSTRUCTION.md` + `EDL_216_shots.csv` is a complete real instance of both — and it already self-labels its own confidence per finding, which is the standard this schema must not regress from.

### research_sources / research_findings
Purpose: `research_sources` = a URL or document consulted during Phase 8 web validation; `research_findings` = what was learned from it. Relationships: `research_findings` belongs to `research_sources` and to whatever `content_ideas`/`insights` it validated. Provenance: `research_sources` carries retrieval timestamp + URL (`docs/Security.md`, Scraping Boundaries); `research_findings` is `EXTRACTED_FACT` or `AI_INTERPRETATION` depending on how it was derived. Evidence today: none — no live web research has occurred in this project.

### insights
Purpose: a distilled, reusable piece of intelligence (a pattern, a principle) drawn from one or more sources. Relationships: many-to-many with the `source_files`/`documents` it was drawn from. Provenance: `AI_INTERPRETATION` or `HUMAN_INTERPRETATION`. Evidence today: the "Notes" and "Comparative Analysis" content inside `YouTube_Master_Data.xlsx`'s Analysis sheet (e.g., like-rate/comment-rate/upload-cadence comparisons between two channels) is a real, present example of exactly this — currently trapped in a spreadsheet, not a structured record.

### topic_clusters
Purpose: groups of related `insights`/`content_ideas` (Phase 7 gap discovery). Evidence today: none yet — no clustering has been performed.

### content_ideas / content_projects
Purpose: `content_ideas` = a candidate video concept (Phase 7 output); `content_projects` = one actually taken into production. Relationships: `content_ideas` may become a `content_projects`; both link back to the `insights`/evidence that motivated them. Evidence today: none yet.

### scripts / thumbnail_concepts
Purpose: Phase 9 production artifacts belonging to a `content_projects`. Evidence today: none directly, though the "training" corpus (`all training data of youtube`) contains prompt frameworks intended to eventually produce these (e.g. `Script Analyzer.pdf`, `Renae_Creative_Engine_v2.5...pdf`).

### content_calendar
Purpose: scheduling for `content_projects` across channels. Evidence today: none.

### experiments
Purpose: a recorded test (e.g. a title A/B, a thumbnail swap) with its outcome. Relationships: belongs to `channels`/`content_projects`. Evidence today: none in the inspected sources.

### channel_analytics
Purpose: aggregated performance metrics over time, distinct from a single `channel_snapshots` point read. Evidence today: `YouTube_Master_Data.xlsx`'s "Comparative Analysis" sheet computes exactly these kinds of aggregates (uploads/week, views/subscriber, like rate) — currently as static spreadsheet formulas, not a queryable table.

### agent_runs
Purpose: audit record of an automated/agent process that touched the system (what ran, when, what it read/wrote). Relationships: may reference any entity it created or modified. Provenance requirement: this is the mechanism that lets a later reviewer answer "did an AI write this, and from what." Evidence today: none — no automation has run yet; this Phase 0.5 task itself is the kind of event such a record would eventually capture.

### ingestion_jobs
Purpose: audit record of a controlled ingestion action (Phase 1) — what was copied from where, by whom/what process, under which manifest decision. Relationships: references `datasets`/`source_files`. Evidence today: none — no ingestion has occurred yet. `docs/source-discovery/SOURCE_INGESTION_RECOMMENDATIONS.md` is the human-readable precursor to what this table would eventually formalize.

## 3. Whether these entities are sufficient

The four inspected source folders (`docs/source-discovery/SOURCE_DISCOVERY_REPORT.md`) map cleanly onto this list — nothing found required inventing a new entity. The clearest gap is **temporal data**: every real dataset found so far is a single point-in-time snapshot (one scrape date, one screenshot session). `video_snapshots` and `channel_snapshots` exist conceptually above but have zero supporting evidence yet; whether they're worth building before repeated-capture data exists is a Phase 2+ decision, not a Phase 0.5 one.

## 4. Data types — illustrative only

Future fields will likely draw from: `INTEGER`, `TEXT`, `BOOLEAN`, `DATE`/`TIMESTAMP`, `JSON` (for variable/nested fields like hashtags or per-shot measurement arrays), foreign-key relationships between the entities above, content hashes (SHA-256, matching `docs/DATA_INVENTORY.md`'s existing rule), and confidence/status enums (the provenance states in §1, plus per-field confidence like the `HIGH`/`MEDIUM`/`LOW CONFIDENCE` labels already used in `FORENSIC_RECONSTRUCTION.md`).

No SQL, no migrations, and no engine (PostgreSQL, Supabase, or otherwise) are part of this document or of Phase 0.5.

## 5. Phase 1 Inventory Catalog

```text
CURRENT:
SQLite inventory/catalog (data/catalog/youtube_inventory.db, schemas/inventory/)

FUTURE:
final structured intelligence database — the ~24 conceptual entities in §2
(channels, videos, transcripts, insights, etc.)

UNDECIDED:
PostgreSQL / Supabase / vector / semantic retrieval architecture (Decision 004, Phase 10)
```

Phase 1A (Decision 012) intentionally implemented only the minimal inventory subset needed to answer "what data do we own, where did it come from, and is it still trustworthy" — `schema_meta`, `datasets`, `ingestion_runs`, `source_locations`, `source_files`, `file_relationships`, `ingestion_errors`. `source_files` rows track physical files and archive members only — one row per file, not one row per video, competitor, or transcript.

Phase 1B (Decisions 014, 015) added `channels`, `channel_snapshots`, `videos`, `video_snapshots`, `transcripts`, and `field_provenance` (`schemas/inventory/002_structured_registration.sql`) — a deliberately small slice of the §2 conceptual model, scoped to structured *registration*, not analysis. `video_snapshots`/`channel_snapshots` implement the append-only snapshot pattern §2 already anticipated for `video_snapshots`/`channel_snapshots` but had no supporting evidence for; DS-000001's single scrape date (24 Aug 2026) is now that first snapshot.

Phase 1C (`schemas/inventory/003_multimodal_source_registration.sql`, `004_discovered_files_fk_indexes.sql`) added a batch/discovery layer (`source_batches`, `batch_roots`, `discovered_files`) so every filesystem item encountered during a bulk multi-root ingestion gets an explicit disposition record, plus generic image (`visual_assets`, `visual_observations`), classification (`entity_classifications`, Decision 016), and document (`document_records`) tables — again a minimal slice scoped to registration/observation, not analysis, insight generation, or embeddings.

Phase 1D (`005_apify_youtube_acquisition.sql`, `006_apify_cost_observations.sql`) reuses those stable identities and append-only snapshots for bounded live acquisition. It adds Apify source-run/record provenance, channel-to-dataset identity links, snapshot descriptions/types, transcript source/reference metadata, thumbnail URL evidence, and append-only billing observations. Full transcript text remains in immutable local raw text files referenced by the catalog. Successful new Apify registrations require a locally retained, cataloged, hash-verified raw Actor result payload; `DS-000006` / `APIFYRUN-000001` is the documented historical exception whose missing raw payload is not reconstructed.

**IMPLEMENTED** (schema versions 1–6, `data/catalog/youtube_inventory.db`):
`schema_meta`, `datasets`, `ingestion_runs`, `source_locations`, `source_files`, `file_relationships`, `ingestion_errors`, `channels`, `channel_snapshots`, `videos`, `video_snapshots`, `transcripts`, `field_provenance`, `source_batches`, `batch_roots`, `discovered_files`, `visual_assets`, `visual_observations`, `entity_classifications`, `document_records`, `apify_source_runs`, `channel_dataset_links`, `apify_result_records`, `thumbnail_evidence`, `apify_run_cost_observations`.

**PLANNED / NOT IMPLEMENTED** (remaining §2 conceptual entities):
`competitors`, `research_sources`/`research_findings`, `insights`, `topic_clusters`, `content_ideas`/`content_projects`, `scripts`/`thumbnail_concepts`, `content_calendar`, `experiments`, `channel_analytics`, `agent_runs`, `ingestion_jobs`.

The catalog exists to make the provenance model in §1 mechanically enforceable (hash-verified, queryable) rather than only documented, without pulling forward any decision this document defers to Phase 10. It is migration-friendly by design (Decision 012) so its data can move into whatever production database Phase 10 selects, rather than being re-derived from scratch.
