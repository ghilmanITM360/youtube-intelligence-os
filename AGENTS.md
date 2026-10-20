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

## Permanent worktree rule

- Never create a new worktree for an ordinary task. Use the existing canonical
  repository whenever it is safe, or reuse an existing owner-approved worktree
  when branch isolation is required.
- Create another worktree only after explicit owner approval.
- Before switching branches, verify a clean Git state, branch ownership, and
  that no agent on either Mac is modifying the same branch. Never overwrite
  another machine's unpushed work.
- Never merge a pull request automatically. Preserve branches, stashes,
  untracked files, ignored evidence, and interrupted-work handoffs.
- Aim for one canonical checkout and at most one necessary existing long-lived
  auxiliary worktree per Mac. This target never authorizes removal of an active,
  dirty, unverified, or uniquely data-bearing worktree.
- Keep private media in durable storage outside temporary directories. On
  Machine B the configured root is
  `/Users/ghilmanislam360/Documents/YIOS-Media-Library/`; set
  `YIOS_MEDIA_ROOT` to that path. Machine A must establish and document its own
  verified durable root from a Machine A session.

Current ownership: Machine B canonical checkout
`/Users/ghilmanislam360/Documents/youtube-intelligence-os` owns ongoing branch
`research/finance-economics-intelligence`. Machine A canonical checkout is
`/Users/ghilmankhan/workprojects/youtube-intelligence-os`; do not infer its
branch, cleanliness, worktree ownership, or media inventory from Machine B.

## graphify

The project-scoped Graphify Codex skill is installed, but no knowledge graph has been built.

- Do not scan, build, query, watch, or update a graph unless the user explicitly requests it in a later task.
- Do not run Graphify over `data/raw/` without explicit user authorization and a provenance-safe plan.
- An explicit `/graphify` request may use the installed skill, subject to the core rules above.

## External tool boundaries

- Ponytail is a coding-quality assistant; it does not override this repository's core rules.
- Claude-Mem is auxiliary session memory only. It is never evidence, canonical project knowledge, or a replacement for repository documentation.
- External tool databases, graphs, embeddings, MCP adapters, hooks, or services do not determine the YouTube Intelligence OS production architecture.
