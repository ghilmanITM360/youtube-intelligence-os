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
12. **Phase 2 — Data Classification & Provenance** is closed. **YouTube Intelligence OS V1 is complete**: Topic Opportunity Intelligence is generalized across all canonical channels; Packaging Intelligence is generalized across all canonical channels (title-only where no canonical thumbnail reference exists); Hook and Script Intelligence are generalized across all canonical channels; Editing/Visual Intelligence is attached only where forensic video evidence is registered (currently CH-000004) and otherwise reported `NOT_AVAILABLE`; a unified orchestrator (`scripts/run_youtube_intelligence.py`) composes these layers into evidence-traceable content plans for every channel (see `docs/Phases.md`). Channel Strategy Intelligence (`scripts/report_channel_strategy_intelligence.py`: success/failure labeling, competitor benchmarking, new-channel blueprint assembly) is now **GENERALIZED_WORKING** — validated on two independent niches (health: CH-000005 vs CH-000003; finance: CH-000001 vs CH-000002, bidirectionally) with the same unmodified core engine and no niche-specific branching. A cross-niche calibration pass exists (`data/intelligence/system/cross-niche-strategy-calibration-2026-09-11.json`); no heuristic has yet reached `ROBUST_CROSS_NICHE_PATTERN` with only 2 channels per niche, which is an evidence-coverage limitation, not a code gap. File-based first-party YouTube Analytics ingestion is **READY**, and own-channel diagnostic enrichment is **READY_FOR_REAL_DATA**; no real first-party export has been ingested. No V2 work (UI, RAG, agents, API, automation, YouTube API integration) begins automatically.
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

## Explicitly requested two-Mac coordination

- Read `docs/YIOS_TWO_MAC_WORKFLOW.md` and `research/coordination/CHANNELS.md` before task writes or handoffs.
- The new CLI does not itself transfer legacy authority. Finance's published Machine B sole-writer record and protected Video003 checkpoint remain enforceable until their explicit release and real two-Mac acceptance gates pass.
- One remote claim per video; a separate exclusive coordinator publishes canonical updates. Do not delete claim refs, bypass a competing writer, infer release from idleness, or overwrite canonical data from a task branch.
- Small partial checkpoints use separate task branches and exact remote SHA verification. UNSYNCED work remains local until verified. Original media recovery is a separate hash-checked gate.
