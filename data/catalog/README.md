# Data Catalog

## What this is

`data/catalog/youtube_inventory.db` is the local SQLite inventory/catalog for the YouTube Intelligence OS (Decision 012). Phase 1A (schema v1) indexes datasets, ingestion runs, source locations, physical files, archive members, hashes, and file relationships. Phase 1B (schema v2, Decisions 014–015) adds structured registration. Phase 1C (schema v3–v4) adds recursive multimodal registration. Phase 1D (schema v5–v6, Decision 018) adds bounded Apify run/result/cost provenance, channel identity links, description/type snapshots, transcript references, and thumbnail evidence. Schema v8 adds the minimal Phase 2 foundation for provenance-linked content topic and format classifications; it does not populate or analyze the corpus.

## What this is not

- Not the final production intelligence database. Final PostgreSQL/Supabase/vector/RAG architecture is undecided until Phase 10 (Decision 004, `docs/Database.md` §5).
- Not a raw-payload warehouse. It never stores transcript bodies, raw Actor result payloads, XLSX/ZIP bytes, images, PDFs, or other BLOB payloads. Phase 1D video descriptions are normalized snapshot text; transcript bodies stay in canonical ZIP members or immutable local raw text files referenced by `transcripts.canonical_reference` and `source_files` hashes.
- Not a replacement for the human-readable manifest in `data/manifests/`. The manifest is the durable ingestion record; the catalog is the fast index over the same facts.
- Not authoritative over the raw files. Raw evidence in `data/raw/` remains primary; the catalog describes it.
- Not a competitor-intelligence or recommendation store. `video_snapshots`/`channel_snapshots` hold source-reported and source-computed metrics only. `visual_observations`/`entity_classifications` hold descriptive extraction, while `content_classifications` holds provenance-linked topic/format assertions with an explicit evidence layer and review status.

## Where it lives

`data/catalog/youtube_inventory.db`, plus SQLite `-wal`/`-shm` files while a connection is open. All of it stays local (Decision 013) — see `.gitignore`.

## Why it is local

Decision 013: the operational database is regenerable from source material already under version control (schema + raw canonical files + manifests), so committing it to Git would only bloat history without adding information Git doesn't already have another way to reconstruct.

## How it is recreated

1. Apply `schemas/inventory/001_initial.sql` through `004_discovered_files_fk_indexes.sql` (and any later `NNN_*.sql` file, in order) to a fresh SQLite file — `python3 scripts/inventory_catalog.py init` does this.
2. Re-run `python3 scripts/inventory_catalog.py ingest --source <path> --dataset-id <id> --name <name> --semantic-class <class>` for each Phase 1A/1B dataset described in `data/manifests/*.md`, pointing `--source` at that dataset's canonical copy under `data/raw/`.
3. Run `python3 scripts/inventory_catalog.py verify --dataset-id <id>` to confirm the rebuilt catalog's hashes match the canonical files on disk.
4. Run `python3 scripts/register_structured_source.py register --dataset-id <id>` to re-derive channels/videos/snapshots/transcripts/provenance from the same canonical files, then `python3 scripts/register_structured_source.py verify --dataset-id <id>` to confirm agreement.
5. For Phase 1C's `BATCH-000001` (DS-000002–DS-000016), re-run `python3 scripts/register_batch.py discover`, `register --batch-id BATCH-000001`, and `images --batch-id BATCH-000001` against the same 12 source roots — this rebuilds `discovered_files`/`visual_assets` from scratch. OCR and native semantic-inspection observations are not regenerable purely from the catalog (they came from an on-device Vision pass and an AI-agent visual inspection pass respectively); their outputs are preserved in `data/manifests/DS-*.md` and `data/manifests/batches/BATCH-000001_FILES.csv` for reference even though the raw observation rows themselves would need to be re-run to fully repopulate.
6. For Phase 1D, use the sanitized run manifests in `data/manifests/apify/` plus canonical local transcript files under `data/raw/competitors/<dataset>/apify/<run>/`; do not re-run an Actor merely to rebuild a local catalog without explicit cost authorization.
7. Run `python3 scripts/classify_forensic_dataset_relationship.py` to verify and register the proven `DS-000012`/`DS-000015` `SAME_SOURCE_INDEPENDENT_ANALYSIS` relationship from its dedicated relationship evidence manifest.

No fact recorded only inside the `.db` and nowhere else is currently load-bearing: every dataset's identity, source path, and file hashes are also written into its `data/manifests/<id>.md` file at ingestion/registration time.

## Schema version

Current: `8` (`001_initial.sql` through `008_content_classifications.sql`, tracked in `schema_meta`). Later schema changes must ship as a new additive `NNN_*.sql` file, never an edit to a file that has already shipped.

## Raw evidence remains authoritative

If the catalog and the raw files on disk ever disagree, the raw files win. The catalog is a derived index, not a source of truth (`AGENTS.md` rules 2–4).

## Classification evidence eligibility

The classification pipeline accepts a transcript archive member without a standalone `canonical_path` only when its catalog hash, unique member locator, parent-archive provenance, parent hash, and current member bytes all verify. No member is extracted or copied to create eligibility. A sourced title plus a verified available transcript is sufficient topic evidence when the snapshot has no description; the recorded classification provenance must omit `description` in that case. Duration evidence remains required separately for `CONTENT_FORMAT`.
