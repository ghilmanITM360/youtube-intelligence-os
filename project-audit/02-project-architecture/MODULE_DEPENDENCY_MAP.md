# Module Dependency Map

Measured with an AST import scan of `scripts/**/*.py` on `origin/main` (66 modules). External imports are stdlib plus `openpyxl`, `PIL` and `docx`. `docx` (python-docx) is **undeclared** in `pyproject.toml` (debt D2, still open). Declared runtime deps: `openpyxl`, `Pillow`. Dev: `pytest`, `pytest-cov`, `ruff`.

## Hubs

| Module | Imported by | Role |
|---|---:|---|
| `inventory_catalog` | 14 | DB connection, schema, hashing, IDs: the core library |
| `report_common` | 10 | read-only connect + shared report helpers |
| `stage_what_if_forensics` / `validate_what_if_source_contract` | 3 / 3 | What If evidence chain |
| `source_adapters/youtube_master_data` | 3 | workbook parsing |

## Graph

```mermaid
flowchart LR
  IC[inventory_catalog]
  RC[report_common] --> IC
  subgraph Ingest
    RB[register_batch] --> IC
    RB --> BRU[batch_rules]
    RSS[register_structured_source] --> IC
    RSS --> YMD[youtube_master_data]
    RSC[register_supplied_channel] --> IC
    RSC --> YMD
    API[apify_youtube_ingest] --> IC
    GBM[generate_batch_manifests] --> IC
    LOAD[load_ocr/semantic/document_results] --> IC
    CCP[classify_content_pilot] --> IC
    RIC[rebuild_inventory_catalog] --> IC
    IYA[ingest_youtube_analytics] --> YMD
  end
  subgraph Intelligence
    TOP[report_topic_opportunity] --> RC
    TOP --> IC
    PKG[report_packaging_intelligence] --> RC
    HS[report_hook_script_intelligence] --> RC
    HS --> IC
    EV[report_editing_visual_intelligence] --> RC
    CS[report_channel_strategy_intelligence] --> ORCH
    ORCH[run_youtube_intelligence] --> RC
    ORCH --> QW[query_what_if_forensics]
    ORCH --> SW[stage_what_if_forensics]
    FPD[report_first_party_channel_diagnosis]
  end
  subgraph WhatIf
    QW --> PW[promote_what_if_forensics]
    PW --> SW
    PW --> VW[validate_what_if_source_contract]
    PW --> WB[what_if_forensic_brain]
    SW --> VW
    SW --> WB
    WB --> VW
  end
  REF[refresh_youtube_intelligence] --> PLN[plan_intelligence_refresh]
  REF --> TOP & PKG & HS & EV & CS & FPD & ORCH & IYA
  VR[validate_youtube_channel_registry] --> BYR[build_youtube_channel_registry]
```

## Standalone modules (no internal imports)

Registry builder (`build_youtube_channel_registry`, 1,230 lines), validators (`validate_dataset_ledgers`, `validate_legacy_dataset_manifests`, `validate_supplied_channel_packages`, `validate_packaging_research`), `check_slop_risk`, `scan_tracked_secrets`, channel-specific builders (`build_dr_rehan_package`, `build_doctor_thomas_package`, `build_better_health_while_aging_package`, `build_bhwa_deep_investigations`, Decode Your Heart scripts), Node packagers (`package_*_dataset.mjs`, `build_youtube_channel_master_tracker.mjs`) and the macOS OCR helper (`image_text_recognition.swift`).

## Observations

1. **Clean core.** One library hub (`inventory_catalog`) and one read helper (`report_common`). That gives a thin read API a natural place to start.
2. **Inversion:** `report_channel_strategy_intelligence → run_youtube_intelligence`. A future service layer should move the shared functions into `report_common` (or a new `yios_read` module) to break it.
3. **Channel-specific scripts** (Dr Rehan, Doctor Thomas, BHWA, Decode) are one-off builders. Keep them out of any service API.
4. **Branch-only modules** that a UI would call if merged: `scripts/yios*.py` (coordination), `scripts/media_cache.py` + `build_local_media_library.py`, `scripts/build_reviewed_channel_workbooks.py`, `scripts/build_finance_economics_complete_db.py`, `scripts/backfill_senior_health_transcripts.py`, and the finance-lineage `research/finance-economics-intelligence/*.py` validators plus `reference-framework/build_reference_kb.py`.
