# YouTube Intelligence OS

A canonical workspace for a persistent, evidence-based intelligence system for multiple YouTube channels. V1 ingestion, provenance, topic, packaging, hook/script, conditional editing/visual, strategy, and orchestration layers are implemented.

**Current state (2026-09-21):** 70 canonical channels, 41 with video data, 36 standard packages, 5 historical-format channels, and 29 identity-only channels. The canonical union contains 1,939 videos, 1,928 verified real transcripts, and 11 explicit placeholders. Generated channel-specific intelligence exists for five historical channels; another 36 channels are input-ready, not already analyzed. Editing/Visual Intelligence remains evidence-gated to CH-000004. No real first-party YouTube Analytics export has been ingested.

## Supported setup

Python 3.12 and Node 22–24 are supported. From a clean clone:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install ".[dev]"
python -m scripts.rebuild_inventory_catalog
python -m scripts.build_youtube_channel_registry --write-ledgers
python -m scripts.validate_dataset_ledgers
python -m scripts.validate_youtube_channel_registry
python -m pytest -q
```

`scripts.rebuild_inventory_catalog.py` creates a valid schema-v10 manifest index. It is semantically reproducible, not byte-identical to the historical operational catalog. Tests requiring ignored historical transcript or forensic raw evidence skip explicitly in a clean clone. Tracker generation additionally needs the external bundled `@oai/artifact-tool`; its path is supplied at runtime and is not an npm dependency.

## Current purpose

Phase 0.5 and Phase 1 established planning, controlled ingestion, inventory, and provenance. Phase 2 classification is closed. V1 now adds evidence-traceable topic, packaging, hook/script, conditional editing/visual, strategy, and unified-plan engines. Generated artifacts remain separate from input readiness: current per-channel artifacts cover five historical channels, while standard packages provide validated inputs for later generation.

## What is (and isn't) in this repository

This repository is the **code, schema, and documentation layer** — it is portable and does not depend on any one machine's file layout. It contains:

- Database schema migrations, ingestion/registration scripts, and their tests (`schemas/`, `scripts/`, `tests/`).
- Durable, database-generated manifests recording what was ingested, from where, and under what disposition (`data/manifests/`).
- Project documentation, decisions, and the project-scoped ingestion skill (`docs/`, `.codex/skills/`).

It does not commit runtime databases or private/local evidence by default:

- `data/catalog/youtube_inventory.db` and `data/catalog/youtube_channel_registry.db` are generated, validated, and gitignored.
- Selected approved canonical raw acquisitions are deliberately tracked with checksums. Other raw, private, or operational evidence remains ignored; durable manifests preserve its provenance and limitations.

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
- `schemas/`, `scripts/`, and `config/` — reserved for justified later-phase additions.
- `logs/` — non-source operational logs when processing is introduced.

## Entering data

Place or provide each new dataset through `data/raw/inbox/`. A dataset may contain archives, documents, tables, images, transcripts, metadata, or other formats not yet known. File extension records physical format; it does not determine semantic role or intelligence value.

## Git and large raw data

Project documentation, decisions, configuration examples, and small manifests are intended for repository control. Raw datasets may be large, binary, private, or unsuitable for Git history. The `.gitignore` deliberately does **not** ignore all of `data/raw/`: each dataset must be inventoried and an explicit storage decision made before it is staged. Secrets and credentials must never be committed.

## Deferred architecture

Database, vector-search, RAG, agent, provider, API, frontend, and cloud infrastructure choices are intentionally deferred until real supplied datasets have been inspected. External developer tools recorded in `docs/TOOLS_INSTALLED.md` are conveniences and do not determine the system's production architecture.
