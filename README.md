# YouTube Intelligence OS

Start with the [permanent mission and architecture](docs/YIOS_MASTER_PLAN.md) and [dated cross-chat session context](docs/AI_SESSION_CONTEXT.md). These entry points link to the underlying research and evidence authorities.

An evidence-based intelligence system for multiple YouTube channels. **YouTube Intelligence OS V1 is complete**: Topic, Packaging, Hook and Script intelligence feed a unified production-plan orchestrator. Editing/Visual intelligence is available where registered forensic evidence exists; unavailable evidence is explicit. Channel Strategy is GENERALIZED_WORKING with limited cross-niche evidence coverage. V2 does not begin automatically.

**What If integration (2026-10-09):** source contract, read-only adapter, durable normalized staging, promotion and source-backed Editing/Visual production guidance are implemented. Ten existing videos supply 8,327 observations. Two independently verified external IDs remain unregistered with transcript evidence pending; two ID-less sources remain unresolved. Identity and transcript availability are separate; the explicit pending registration path is canonical after PR #17. The validated ten-video Genius History packaging packet is canonical after PR #19. Canonical What If count remains 83. See [live remaining-work audit](docs/audits/REMAINING-WORK-MATRIX-2026-10-11.md), [current project status](PROJECT_STATUS.md) and [integration workflow](docs/WHAT_IF_INTEGRATION_WORKFLOW.md) for exact counts, commands and external blockers.

Catalogs have distinct populations: the selected inventory and the broader channel registry must not be treated as interchangeable sample counts. See `docs/YOUTUBE_CHANNEL_REGISTRY.md` and `data/catalog/README.md`.

## Bootstrap (clean clone)

`youtube_channel_registry.db` is Git LFS-tracked; a clean clone gets only the pointer file until LFS materializes it:

```bash
git lfs install
git lfs pull
python3.12 -m venv .venv && source .venv/bin/activate
python -m pip install ".[dev]"
python -m scripts.rebuild_inventory_catalog
python -m scripts.build_youtube_channel_registry --write-ledgers
python -m scripts.validate_dataset_ledgers
python -m scripts.validate_youtube_channel_registry
python -m pytest -q
```

`scripts/rebuild_inventory_catalog.py` produces a valid schema-v10 manifest index; it is semantically reproducible, not byte-identical to the historical operational catalog. Tests requiring ignored local raw evidence skip explicitly with a stated reason when that evidence isn't present.

## Current purpose

Phase 0.5 hardened the project's planning documentation (`docs/Architecture.md`, `docs/Phases.md`, `docs/Database.md`, `docs/Prompts.md`, `docs/Security.md`, `docs/Error_Handling.md`) and performed read-only discovery of real external source folders. Phase 1A–1C then accepted user-supplied datasets, preserved their originals, inventoried their contents (recursively, with an explicit disposition for every discovered item), extracted descriptive facts from images and documents (OCR, native visual observation, text characterization), and recorded provenance — without performing competitor strategy analysis, topic generation, or any other content-recommendation work. Those historical ingestion boundaries remain documented; the subsequently authorized V1 intelligence layers are now implemented.

## What is (and isn't) in this repository

This repository is the **code, schema, and documentation layer** — it is portable and does not depend on any one machine's file layout. It contains:

- Database schema migrations, ingestion/registration scripts, and their tests (`schemas/`, `scripts/`, `tests/`).
- Durable, database-generated manifests recording what was ingested, from where, and under what disposition (`data/manifests/`).
- Project documentation, decisions, and the project-scoped ingestion skill (`docs/`, `.codex/skills/`).

It deliberately does **not** contain the full operational data payload:

- `data/catalog/youtube_inventory.db` — the selected-inventory SQLite catalog — is committed as a checkpoint under the owner preservation policy. It remains a derived index; original evidence and reviewed manifests are authoritative. See `data/catalog/README.md`.
- `data/catalog/youtube_channel_registry.db` — the complete cross-channel query authority — **is** committed, via Git LFS (see Bootstrap above).
- Most raw source evidence (screenshots, video frames, PDFs, archives, spreadsheets) lives under `data/raw/` on the machine that ingested it and is gitignored; only its provenance (hashes, paths, dispositions, counts) is recorded in the manifests that *are* committed. Explicitly preserved, checksum-registered acquisitions are tracked under per-dataset allowlists. Historical tracked audio, frames and private-derived analytics are listed in `docs/audits/WHAT_IF_REPOSITORY_SAFETY_2026-10-09.md`; their removal or storage migration remains a separate evidence-preservation decision.

## Data layers

```text
RAW
↓
EXTRACTED
↓
NORMALIZED
↓
INTELLIGENCE
```

Raw source files are evidence and must never be modified, rewritten, compressed, renamed destructively, or replaced by AI-generated interpretations. Derived material belongs in the corresponding later layer and must retain provenance back to its source.

## Directory guide

- `data/raw/inbox/` — entry point for every newly supplied dataset.
- `data/raw/` — preserved source evidence, organized only after inspection and classification.
- `data/extracted/` — direct extractions from source evidence.
- `data/normalized/` — consistently structured representations of extracted material.
- `data/intelligence/` — reusable interpretations and analytical outputs.
- `data/manifests/` — file and dataset inventory records.
- `docs/` — scope, workflows, classifications, decisions, and tooling records.
- `channels/` — future separated channel-specific workspaces.
- `schemas/`, `scripts/`, and `config/` — implemented schema, ingestion, intelligence, validation and configuration layers.
- `logs/` — non-source operational logs when processing is introduced.

## Entering data

Place or provide each new dataset through `data/raw/inbox/`. A dataset may contain archives, documents, tables, images, transcripts, metadata, or other formats not yet known. File extension records physical format; it does not determine semantic role or intelligence value.

## Git and large raw data

Project documentation, decisions, configuration examples, and small manifests are intended for repository control. Raw datasets may be large, binary, private, or unsuitable for Git history. The `.gitignore` deliberately does **not** ignore all of `data/raw/`: each dataset must be inventoried and an explicit storage decision made before it is staged. Secrets and credentials must never be committed.

## Deferred architecture

Database, vector-search, RAG, agent, provider, API, frontend, and cloud infrastructure choices are intentionally deferred until real supplied datasets have been inspected. External developer tools recorded in `docs/TOOLS_INSTALLED.md` are conveniences and do not determine the system's production architecture.
