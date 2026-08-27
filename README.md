# YouTube Intelligence OS

A canonical workspace for developing a persistent, evidence-based intelligence system for multiple YouTube channels. The long-term vision includes data inventory, competitor analysis, research, topic discovery, and content-development intelligence. This repository is **not** that finished product yet — it is currently the data-ingestion and provenance foundation the later intelligence phases will build on.

**Current Phase: Phase 1C — Recursive Multi-Source & Multimodal Ingestion, COMPLETE** (see `docs/Phases.md`). Phase 2 — Data Classification & Provenance is next, pending explicit authorization; it does not begin automatically.

## Current purpose

Phase 0.5 hardened the project's planning documentation (`docs/Architecture.md`, `docs/Phases.md`, `docs/Database.md`, `docs/Prompts.md`, `docs/Security.md`, `docs/Error_Handling.md`) and performed read-only discovery of real external source folders. Phase 1A–1C then accepted user-supplied datasets, preserved their originals, inventoried their contents (recursively, with an explicit disposition for every discovered item), extracted descriptive facts from images and documents (OCR, native visual observation, text characterization), and recorded provenance — without performing competitor strategy analysis, topic generation, or any other content-recommendation work. That analysis layer is intentionally deferred to a later, separately-authorized phase.

## What is (and isn't) in this repository

This repository is the **code, schema, and documentation layer** — it is portable and does not depend on any one machine's file layout. It contains:

- Database schema migrations, ingestion/registration scripts, and their tests (`schemas/`, `scripts/`, `tests/`).
- Durable, database-generated manifests recording what was ingested, from where, and under what disposition (`data/manifests/`).
- Project documentation, decisions, and the project-scoped ingestion skill (`docs/`, `.codex/skills/`).

It deliberately does **not** contain the operational data payload:

- `data/catalog/youtube_inventory.db` — the local SQLite catalog — is generated from the schema plus the manifests below and is gitignored (Decision 013). It is not committed, and does not need to be for the project's history to be reconstructable.
- Raw source evidence (screenshots, video frames, PDFs, archives, spreadsheets) lives under `data/raw/` on the machine that ingested it and is likewise gitignored; only its provenance (hashes, paths, dispositions, counts) is recorded in the manifests that *are* committed.

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
