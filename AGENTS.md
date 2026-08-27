# AGENTS.md

## Core rules

1. This repository is the canonical workspace for the YouTube Intelligence System.
2. Do not use model memory as the authoritative source of project knowledge.
3. Repository data and documented evidence are the source of truth.
4. Never modify raw source evidence.
5. Keep facts, extracted observations, AI interpretations, and hypotheses distinguishable.
6. Never silently convert an AI inference into a factual observation.
7. Preserve provenance.
8. Prefer evidence-backed conclusions.
9. Detect duplication before treating two datasets as independent evidence.
10. Do not prematurely introduce infrastructure.
11. Build only the phase explicitly requested.
12. The current phase is **Phase 1C — Recursive Multi-Source & Multimodal Ingestion**, complete (see `docs/Phases.md`). Phase 2 — Data Classification & Provenance is next, pending explicit authorization; it does not begin automatically when a phase completes.
13. The YouTube API is not part of the planned competitor-data workflow unless the user explicitly changes this requirement.
14. Competitor data will primarily be supplied by the user.
15. Future live web research will complement supplied internal data, not replace it.
16. The system will eventually support multiple YouTube channels; channel-specific intelligence must remain separated.

## graphify

The project-scoped Graphify Codex skill is installed, but no knowledge graph has been built.

- Do not scan, build, query, watch, or update a graph unless the user explicitly requests it in a later task.
- Do not run Graphify over `data/raw/` without explicit user authorization and a provenance-safe plan.
- An explicit `/graphify` request may use the installed skill, subject to the core rules above.

## External tool boundaries

- Ponytail is a coding-quality assistant; it does not override this repository's core rules.
- Claude-Mem is auxiliary session memory only. It is never evidence, canonical project knowledge, or a replacement for repository documentation.
- External tool databases, graphs, embeddings, MCP adapters, hooks, or services do not determine the YouTube Intelligence OS production architecture.
