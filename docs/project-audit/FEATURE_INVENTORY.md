# Feature Inventory — 2026-11-11

Status key: WORKING = covered by tests that passed in this audit (462 pass / 1 skip) or validators that passed; IMPLEMENTED/UNVERIFIED = code exists, not executed here; NOT IMPLEMENTED = referenced as future. "Evidence" cites what I actually ran or read. I did not execute individual features end-to-end against live data.

| Feature | Entry point | Status | Evidence / notes |
|---|---|---|---|
| Raw dataset inventory, hashing, dedup | `scripts/inventory_catalog.py`, `register_batch.py` | WORKING | tests pass; inventory DB integrity ok; 45,774 discovered files |
| Structured registration (channels/videos/snapshots/provenance) | `register_structured_source.py`, `register_supplied_channel.py` | WORKING | tests pass; 10 channels / 667 videos / 12,335 provenance rows |
| Dataset ledger + provenance validation | `python -m scripts.validate_dataset_ledgers` | WORKING | ran: all `clean` |
| Channel registry build + validation (75 channels) | `build_youtube_channel_registry.py`, `validate_youtube_channel_registry` | WORKING (validator) / IMPLEMENTED-UNVERIFIED (builder not re-run) | validator `PASS` |
| Topic Opportunity Intelligence | `report_topic_opportunity.py` | WORKING | tests; artifacts in `data/intelligence/channels/` (5 channel dirs) |
| Packaging Intelligence | `report_packaging_intelligence.py` | WORKING | tests |
| Hook/Script Intelligence | `report_hook_script_intelligence.py` | WORKING | tests |
| Editing/Visual Intelligence | `report_editing_visual_intelligence.py` | PARTIAL by design | only where forensic evidence is registered; else `NOT_AVAILABLE` |
| Channel Strategy Intelligence | `report_channel_strategy_intelligence.py` | WORKING; evidence-limited | 2 niches, 2 channels each; no heuristic reached `ROBUST_CROSS_NICHE_PATTERN` (AGENTS.md) |
| Unified content-plan orchestrator | `run_youtube_intelligence.py` | WORKING | tests; read-only, no network |
| Reference knowledge base + framework gate | `build_reference_kb.py`, `--framework-plan` | IMPLEMENTED; gate not run in CI | KB: 33 rules, 1,260 sections, integrity ok; validators structural only by design |
| Finance/Economics 1,612-video audit program | `research/finance-economics-intelligence/` | IN PROGRESS | 558/1,612 accepted; historical reanalysis 26/558 `SEMANTIC_REVIEW_PENDING` (git log) |
| Apify YouTube acquisition | `apify_youtube_ingest.py` | IMPLEMENTED / UNVERIFIED | tests with mocks; no live call made; 9 historical runs recorded |
| First-party YouTube Analytics ingestion & diagnosis | `ingest_youtube_analytics.py`, `report_first_party_channel_diagnosis.py` | READY, no real data | tests pass; AGENTS.md says no real export ingested |
| What If forensic integration | `scripts/source_adapters/what_if_forensic_brain.py`, staging/promotion scripts | WORKING with external corpus optional | tests skip when corpus absent |
| Transcript recovery / FTS search | `apply_youtube_transcript_recovery.py`, registry `transcript_fts` (2,291 rows) | WORKING | tests; registry integrity ok |
| Secret scan | `scan_tracked_secrets.py` | WORKING | ran: 0 findings (no pytest coverage) |
| Voiceover -> CapCut package demo | `production_pipeline.py` | PARTIAL | 1 test skipped (media fixture absent); demo-specific heuristics (D9) |
| Own-channel UI, API, RAG/vector search, agents, automation, YouTube API | — | NOT IMPLEMENTED | V2; explicitly not authorized (AGENTS.md rules 12–13); a UI handoff doc exists (`docs/UI_BACKEND_HANDOFF_2026-09-11.md`), branch `ui/v1` |
| LLM generation of titles/scripts | — | NOT IMPLEMENTED | no model calls in shipped code (grep) |

## Is the intelligence real or placeholder?
Computation is deterministic rules/statistics over supplied, hash-pinned evidence with explicit `NOT_AVAILABLE`/`SEMANTIC_REVIEW_PENDING` states and a "no CTR/retention inference" policy. I found no mock-data fallbacks masquerading as results in the orchestrator (`PRIVATE_METRICS` always reported `NOT_AVAILABLE` unless measured). The weakest link is semantic judgement: Finance reanalysis records still await human review, and cross-niche heuristics lack sample size.
