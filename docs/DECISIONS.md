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
