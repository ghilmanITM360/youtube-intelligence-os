# Architectural Decision Log

### Decision 001 — No YouTube API for competitor-data ingestion

**Status:** Accepted

The user will supply competitor datasets directly. The YouTube API is not part of the competitor-data workflow unless the user explicitly changes this requirement.

### Decision 002 — Model memory is not the permanent knowledge store

**Status:** Accepted

Repository data, documented decisions, and preserved evidence remain authoritative. Agent or session memory is auxiliary only.

### Decision 003 — Raw evidence must remain immutable

**Status:** Accepted

Raw source files must never be modified, rewritten, compressed, renamed destructively, or replaced by AI-generated interpretations.

### Decision 004 — Derive architecture from real datasets

**Status:** Accepted

The final database and RAG infrastructure will be chosen only after the real supplied datasets have been inspected and understood.

### Decision 005 — No premature Phase 1 infrastructure

**Status:** Accepted

Do not introduce Supabase, RAG, vector search, MCP, custom agents, or automation during Phase 1. External developer tooling remains separate and does not alter this application-level rule.

### Decision 006 — Support multiple separate YouTube channels

**Status:** Accepted

Channel-specific intelligence must remain separated so evidence or rules from one channel do not silently affect another.

### Decision 007 — Analyze internal competitor intelligence first

**Status:** Accepted

Internal competitor intelligence will be analyzed before external web validation. Future web research will complement supplied internal evidence, not replace it.

### Decision 008 — Iterative topic discovery

**Status:** Accepted

Future topic discovery should follow this pattern:

```text
Internal Data
→ Analysis
→ Topic Hypothesis
→ Web Research
→ Re-analysis
→ Final Opportunity
```

## Decision 009 — Permanent Canonical Project Location

**Status:** Accepted

The permanent canonical repository is:

`/Users/ghilmanislam360/Documents/youtube-intelligence-os`

It lives directly under the user's `Documents` directory.

It must not be treated as a temporary Codex task workspace.

Directories under:

`/Users/ghilmanislam360/Documents/Codex/`

may contain:

- historical Codex sessions
- dated task outputs
- research
- experiments
- audits
- old datasets
- temporary working material

but they are **not** the canonical location of the YouTube Intelligence OS.

There must be only one authoritative working repository:

`/Users/ghilmanislam360/Documents/youtube-intelligence-os`

**Reason:** The long-term YouTube Intelligence System requires one stable, easy-to-find location independent of Codex-generated task folders or dated workspaces.

## Decision 010 — External Source Folders Are Valid Ingestion Inputs

**Status:** Accepted

The system may receive a local folder path rather than uploaded/copied files, e.g.:

```text
Ingest this folder:
/path/to/source-folder
```

The first operation on any such folder must be read-only discovery. The system must inspect → inventory → hash → classify → identify logical datasets → propose ingestion, before copying or transforming any source material. See `docs/Architecture.md` §5 for the conceptual flow and `docs/source-discovery/` for the Phase 0.5 demonstration of this procedure against four real folders.

Original external folders remain source evidence and must not be modified, moved, renamed, or reorganized automatically. A folder is not assumed to be exactly one logical dataset — it may contain several, or a dataset may span more than one folder.

**Reason:** The user works from local folders that already hold real evidence (screenshots, exports, analysis documents); the system must be able to reason about that material safely before any of it becomes part of the repository.

## Decision 011 — Scrapling Is External Research Tooling

**Status:** Accepted

Scrapling (`docs/TOOLS_INSTALLED.md`) may later support explicitly authorized web-research/data-acquisition tasks. It is developer/research tooling, installed in an isolated user-level environment, and it does not determine:

- the production database or data model (`docs/Database.md`);
- RAG/retrieval architecture;
- the memory system;
- competitor-ingestion policy.

No automated scraping is enabled during Phase 0.5 or Phase 1. Live scraping is not authorized before Phase 8 (`docs/Phases.md`), and even then only under the boundaries in `docs/Security.md` §6, including mandatory use of `--ai-targeted` for any AI-facing extraction (`docs/Security.md` §5, `docs/TOOLS_INSTALLED.md`).

**Reason:** Scrapling was added as a convenience research tool per this task's request, but the project's existing rule that external tooling never determines production architecture (`AGENTS.md`, External tool boundaries) applies to it exactly as it applies to every other installed tool.
