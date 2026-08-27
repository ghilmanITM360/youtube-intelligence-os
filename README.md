# YouTube Intelligence OS

A canonical workspace for developing a persistent, evidence-based intelligence system for multiple YouTube channels. The long-term vision includes data inventory, competitor analysis, research, topic discovery, and content-development intelligence, but this repository currently contains only the documentation-first data foundation.

**Current Phase: Phase 1C — Recursive Multi-Source & Multimodal Ingestion, COMPLETE** (see `docs/Phases.md`). Phase 2 — Data Classification & Provenance is next, pending explicit authorization.

## Current purpose

Phase 0.5 hardens the project's planning documentation (`docs/Architecture.md`, `docs/Phases.md`, `docs/Database.md`, `docs/Prompts.md`, `docs/Security.md`, `docs/Error_Handling.md`) and performs read-only discovery of real external source folders (`docs/source-discovery/`) so that Phase 1 begins with real recommendations instead of guesses. Phase 1, once authorized, accepts user-supplied datasets, preserves their originals, inventories their contents, records provenance, and prepares for later classification and duplicate detection. Neither phase ingests or analyzes datasets automatically.

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
