# Data Catalog

## What this is

`data/catalog/youtube_inventory.db` is a local SQLite database that acts as the Phase 1 machine-readable inventory/catalog for the YouTube Intelligence OS (Decision 012). Phase 1A (schema v1) indexes datasets, ingestion runs, source locations, physical files, archive members, hashes, and file relationships. Phase 1B (schema v2, Decisions 014–015) adds structured registration — channels, channel/video snapshots, transcript references, and field-level provenance. Phase 1C (schema v3–v4) adds a batch/discovery layer for bulk multi-root ingestion — every discovered filesystem item gets an explicit disposition record — plus image (OCR + native semantic inspection + perceptual hashing/clustering), classification (Decision 016), and document-characterization tables — so the project can answer "what data do we own, where did it come from, what values does it contain, and is it still trustworthy" by query instead of by re-reading Markdown or a workbook.

## What this is not

- Not the final production intelligence database. Final PostgreSQL/Supabase/vector/RAG architecture is undecided until Phase 10 (Decision 004, `docs/Database.md` §5).
- Not a document warehouse. It never stores transcript bodies, video descriptions, raw XLSX/ZIP bytes, images, PDFs, or other BLOB payloads — only metadata, hashes, structured field values, relationships, and status. Transcript text stays in the canonical ZIP archive; `transcripts` rows carry only availability/caption metadata and a pointer (`archive_member_file_id`) back to it.
- Not a replacement for the human-readable manifest in `data/manifests/`. The manifest is the durable ingestion record; the catalog is the fast index over the same facts.
- Not authoritative over the raw files. Raw evidence in `data/raw/` remains primary; the catalog describes it.
- Not a competitor-intelligence or content-analysis store. `video_snapshots`/`channel_snapshots` hold source-reported and source-computed metrics only — no strategy analysis, topic generation, or scoring (Phase 1B/1C boundary, `docs/Phases.md`). `visual_observations`/`entity_classifications` hold descriptive extraction (what a screenshot shows) only — never a strategic recommendation.

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

No fact recorded only inside the `.db` and nowhere else is currently load-bearing: every dataset's identity, source path, and file hashes are also written into its `data/manifests/<id>.md` file at ingestion/registration time.

## Schema version

Current: `4` (`001_initial.sql` + `002_structured_registration.sql` + `003_multimodal_source_registration.sql` + `004_discovered_files_fk_indexes.sql`, tracked in the `schema_meta` table). Later schema changes must ship as a new additive `NNN_*.sql` file, never an edit to a file that has already shipped.

## Raw evidence remains authoritative

If the catalog and the raw files on disk ever disagree, the raw files win. The catalog is a derived index, not a source of truth (`AGENTS.md` rules 2–4).
