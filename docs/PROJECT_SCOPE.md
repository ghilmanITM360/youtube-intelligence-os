# Project Scope

## Current scope

**Phase 1D — Controlled Apify YouTube Acquisition is complete. Phase 2 — Data Classification & Provenance is also closed** (`AGENTS.md` rule 12; 604 classification rows across 303 canonical content items, 5 canonical channels). Topic Opportunity, Packaging, Hook/Script, and Editing/Visual Intelligence have since been authorized and piloted for one or more channels, and a first unified content-intelligence orchestrator (`scripts/run_youtube_intelligence.py`) composes existing layers into evidence-traceable plans without regenerating or fabricating intelligence. The phase numbering in `docs/Phases.md` has not been fully updated to reflect this progression and should be reconciled separately.

Decision 018 authorizes controlled, cost-bounded Apify acquisition as the narrow Phase 1D exception to the no-scraper boundary. No production database, vector store, embeddings, RAG system, MCP server, custom agent workflow, YouTube API integration, other scraper, frontend, dashboard, generator, or scheduled research automation is part of the current scope.

## Long-term concept

The system may eventually turn heterogeneous, user-supplied YouTube evidence into reusable intelligence while keeping source evidence, observations, interpretations, and hypotheses distinct. It will support multiple channels without mixing channel-specific knowledge.

**Long-term architecture — not yet implemented.**

```text
USER-SUPPLIED DATA
        ↓
DATA INVENTORY
        ↓
DEDUPLICATION
        ↓
CLASSIFICATION
        ↓
EXTRACTION
        ↓
NORMALIZATION
        ↓
REUSABLE INTELLIGENCE
        ↓
CHANNEL-SPECIFIC INTELLIGENCE
        ↓
COMPETITOR ANALYSIS
        ↓
PATTERN / OUTLIER / GAP DISCOVERY
        ↓
NEW TOPIC HYPOTHESES
        ↓
INTERNAL RANKING
        ↓
WEB RESEARCH / VALIDATION
        ↓
RE-ANALYSIS AGAINST INTERNAL DATA
        ↓
FINAL CONTENT OPPORTUNITIES
        ↓
TITLE / THUMBNAIL / SCRIPT / VISUAL DEVELOPMENT
```

External developer and agent tools may assist repository work, but their graphs, databases, memory stores, embeddings, services, or conventions are not automatically part of this architecture.
