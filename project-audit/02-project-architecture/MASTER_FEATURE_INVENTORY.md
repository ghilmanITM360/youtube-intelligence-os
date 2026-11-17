# Master Feature Inventory

Status: **Complete** = on main with passing tests in CI (main green 2026-11-17). **Branch-complete** = implemented and tested on an unmerged branch. **Partial / Experimental / Deprecated** as named. Status comes from code + tests + CI, never from branch names alone. Features were not executed end-to-end against live data in this audit.

| # | Feature | Branches | Implementation | Status | Data used / produced | Current UI | Recommendation |
|---|---|---|---|---|---|---|---|
| F01 | Raw inventory, hashing, dedup, disposition | main | `inventory_catalog.py`, `register_batch.py`, `batch_rules.py` | Complete | `discovered_files` 45,774 (TOOLING 35,462, DUPLICATE 4,057, SUPERSEDED 802, INGEST 141 …) | none | Retain; surface as "Evidence Library" |
| F02 | Structured channel/video registration with field provenance | main | `register_structured_source.py`, `register_supplied_channel.py`, `youtube_master_data.py` | Complete | `channels` 10, `videos` 667, `field_provenance` 12,335 | none | Retain; provenance drawer in UI |
| F03 | Dataset ledgers and provenance validation | main | `validate_dataset_ledgers.py`, `data/manifests/` | Complete | 26 datasets (semantic class A 3 / B 17 / C 6) | none | Retain; dataset detail page |
| F04 | Channel registry (75 channels, coverage matrix, FTS) | main | `build_youtube_channel_registry.py`, `validate_youtube_channel_registry.py` | Complete | 75 channels, 2,303 videos, 600 coverage cells, 216 availability gaps | none | Retain; core of "Channels" and "Coverage" screens |
| F05 | Topic Opportunity Intelligence | main | `report_topic_opportunity.py` | Complete | `data/intelligence/channels/*/topic-*` | MD files | Retain |
| F06 | Packaging (title/thumbnail) Intelligence | main | `report_packaging_intelligence.py` | Complete (title-only where no thumbnail ref) | packaging JSON | MD | Retain |
| F07 | Hook + Script Intelligence | main | `report_hook_script_intelligence.py` | Complete | hook/script JSON | MD | Retain |
| F08 | Editing/Visual Intelligence | main | `report_editing_visual_intelligence.py` | Partial by design (CH-000004 only) | forensic observation index | MD | Retain; show NOT_AVAILABLE honestly |
| F09 | Channel Strategy Intelligence (labels, benchmark, blueprint) | main | `report_channel_strategy_intelligence.py` | Complete, evidence-limited (2 niches × 2 channels) | benchmarks, blueprints, calibration | MD | Retain; flag low confidence |
| F10 | Unified content-plan orchestrator | main | `run_youtube_intelligence.py` | Complete | 5 plans (`CH-000001…5`) + What If plan | MD | Retain; "Content Plan" screen |
| F11 | Incremental refresh + freshness registry | main | `plan_intelligence_refresh.py`, `refresh_youtube_intelligence.py` | Complete | freshness registry, refresh-runs | none | Retain; "System Health" screen |
| F12 | First-party YouTube Analytics ingestion + diagnosis | main | `ingest_youtube_analytics.py`, `report_first_party_channel_diagnosis.py` | Ready, **no real data** | import contract JSON | none | Retain; local-only import screen later |
| F13 | What If forensic integration (contract → adapter → staging → promotion → query) | main | 5 What If scripts | Complete (corpus optional) | staged forensic observations | none | Retain |
| F14 | Transcript recovery + FTS search | main | `apply_youtube_transcript_recovery.py`, `transcript_fts` | Complete | 2,291 searchable transcripts | none | Retain; global search |
| F15 | Thumbnail acquisition for registered videos | main | `acquire_registered_thumbnails.py` | Complete | `thumbnail_evidence` 479 | none | Retain |
| F16 | OCR / semantic / document result loaders | main | `load_*_results.py`, `image_text_recognition.swift` | Complete | `visual_observations` 244, `document_records` 17 | none | Retain |
| F17 | Content classification (topic AI-proposed, format verified) | main | `classify_content_pilot.py` | Complete | `content_classifications` 604 | none | Retain; facet filters |
| F18 | Apify acquisition with cost tracking | main | `apify_youtube_ingest.py` | Complete (mocked tests; no retry, D5) | `apify_source_runs` 9, cost obs 10 | none | Retain; show cost, never trigger from UI v1 |
| F19 | AI-slop risk gate | main (#51); alerts on #52 | `check_slop_risk.py` | Complete; #52 open | `*.slop-risk.json` | CLI | Merge #52; show verdicts in Production view |
| F20 | Secret scan | main | `scan_tracked_secrets.py` | Complete | — | CI | Retain |
| F21 | Reference knowledge base + framework gate | finance lineage, current branch | `build_reference_kb.py`, migration 011, `content_plan_check.py` | Branch-complete | 33 rules, 1,260 sections, 722 video assessments | none | **Integrate** (needed for "Rules" screen) |
| F22 | Finance/Economics 1,612-video audit + reanalysis | finance lineage (#36) | `research/finance-economics-intelligence/*.py` | Partial: 558/1,612 accepted; 26/558 reanalysed | NICK_xxx audits, queue, cohort comparisons | MD/CSV/XLSX | Integrate after DB policy |
| F23 | Finance CI gates + frozen-registry separation | `fix/finance-audit-validators` (#45) | workflow + 3 tests | Branch-complete, CI green | — | — | **Integrate first** |
| F24 | Finance complete DB + owner PDF reports | `data/finance-economics-complete-2026-11-11` | `build_finance_economics_complete_db.py` | Branch-complete | 69 channels, 3,634 videos, 3,450 transcripts | PDF/HTML | Integrate builder + manifest (DB policy b) |
| F25 | Senior Health core DB + Apify + transcript backfill | #50, `data/exercise-apify` | `backfill_senior_health_transcripts.py` | Branch-complete; CI fails on DB rule | 159 channels, 5,802 videos, 2,433 transcript index | HTML blueprint | Integrate builder + manifest |
| F26 | Senior Health Reports 1-6 + forensics reports 41-43 | current branch, #50 | report build scripts | Partial (several marked PARTIAL) | derived tables | MD/PDF | Unstack onto main |
| F27 | Visual forensics / CT scan per video | xkcd, CF, BE, PE, editing-forensics branches | per-video ledgers, validators | Partial (CF 19/20, xkcd 29/91) | ledgers, seals, frames (local) | MD/CSV | Keep pinned; index in UI |
| F28 | Packaging/thumbnail forensics QA | thumbnail-forensics-complete, packaging-rollup | docs/research | Branch-complete | QA records | MD | Integrate after stash decision |
| F29 | Local media library + selective cache | #41 | `build_local_media_library.py`, `media_cache.py` | Branch-complete; CI did not run | media manifest | — | **Integrate** (UI media) |
| F30 | Reviewed channel workbooks importer | #46 | `build_reviewed_channel_workbooks.py` | Branch-complete; own trial records validator failure | workbooks | — | Fix, then integrate |
| F31 | Two-Mac claims/checkpoints CLI | `codex/yios-dual-machine-coordination` | `scripts/yios*.py` | Branch-complete (3 test files) | git-ref claims | CLI | Owner decision |
| F32 | Production pipeline: voiceover → CapCut package | current branch | `production_pipeline.py` | Experimental (hardcoded keywords, D9) | package JSON | — | Generalize later |
| F33 | Keyframe animation renderers / gait rigs / Remotion & HTML demos | 5 production branches, CF playbook | per-production code | Experimental, per asset | MP4/PNG | HTML demo | Archive as records |
| F34 | Owner-facing blueprint/launch manuals | finance-complete, senior-health | HTML/PDF builders | Branch-complete | PDFs | **PDF is the owner's real UI today** | Learn from them for UX |
| F35 | Start-here index + consolidation maps | main (#48), cleanup branch | `docs/START_HERE.md`, `research/consolidation/*.csv` | Complete (draft on main) | evidence maps, seal verification | MD | Retain; becomes the Explorer home |
| F36 | What If script study (83 transcripts) | untracked in working tree | `research/what-if-scripts/` | Partial, uncommitted | coverage ledger | — | Commit to a branch |
| F37 | UI backend handoff plan | `ui/v1` (preserved on main as historical) | docs only | Deprecated plan | — | — | Superseded by this audit |
| F38 | Web UI / API / RAG / agents / YouTube API | none | — | **Not implemented** (V2, needs explicit authorization) | — | — | Proposed (see 06/07) |
