# Project Scope

## Current scope

The repository is in **Phase 1 — Data Entry & Inventory**. Current work is limited to safely receiving user-supplied data, preserving originals, describing datasets, recording provenance, and preparing for basic duplicate detection and semantic classification.

No production database, vector store, embeddings, RAG system, MCP server, custom agent workflow, YouTube API integration, scraper, frontend, dashboard, generator, or scheduled research automation is part of this phase.

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
