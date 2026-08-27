# Data Catalog

## What this is

`data/catalog/youtube_inventory.db` is a local SQLite database that acts as the Phase 1 machine-readable inventory/catalog for the YouTube Intelligence OS (Decision 012). It indexes datasets, ingestion runs, source locations, physical files, archive members, hashes, and file relationships so the project can answer "what data do we own, where did it come from, and is it still trustworthy" by query instead of by re-reading Markdown.

## What this is not

- Not the final production intelligence database. Final PostgreSQL/Supabase/vector/RAG architecture is undecided until Phase 10 (Decision 004, `docs/Database.md` §5).
- Not a document warehouse. It never stores transcript bodies, raw XLSX/ZIP bytes, images, PDFs, or other BLOB payloads — only metadata, hashes, relationships, and status.
- Not a replacement for the human-readable manifest in `data/manifests/`. The manifest is the durable ingestion record; the catalog is the fast index over the same facts.
- Not authoritative over the raw files. Raw evidence in `data/raw/` remains primary; the catalog describes it.

## Where it lives

`data/catalog/youtube_inventory.db`, plus SQLite `-wal`/`-shm` files while a connection is open. All of it stays local (Decision 013) — see `.gitignore`.

## Why it is local

Decision 013: the operational database is regenerable from source material already under version control (schema + raw canonical files + manifests), so committing it to Git would only bloat history without adding information Git doesn't already have another way to reconstruct.

## How it is recreated

1. Apply `schemas/inventory/001_initial.sql` (and any later `NNN_*.sql` file in order) to a fresh SQLite file — `python3 scripts/inventory_catalog.py init` does this.
2. Re-run `python3 scripts/inventory_catalog.py ingest --source <path> --dataset-id <id> --name <name> --semantic-class <class>` for each dataset described in `data/manifests/*.md`, pointing `--source` at that dataset's canonical copy under `data/raw/`.
3. Run `python3 scripts/inventory_catalog.py verify --dataset-id <id>` to confirm the rebuilt catalog's hashes match the canonical files on disk.

No fact recorded only inside the `.db` and nowhere else is currently load-bearing: every dataset's identity, source path, and file hashes are also written into its `data/manifests/<id>.md` file at ingestion time.

## Schema version

Current: `1` (`schemas/inventory/001_initial.sql`, tracked in the `schema_meta` table). Later schema changes must ship as a new additive `NNN_*.sql` file, never an edit to a file that has already shipped.

## Raw evidence remains authoritative

If the catalog and the raw files on disk ever disagree, the raw files win. The catalog is a derived index, not a source of truth (`AGENTS.md` rules 2–4).
