# Data Lineage

```mermaid
flowchart LR
  subgraph S[Sources]
    W[Supplied workbooks / exports / zips]
    SC[Screenshots]
    AP[Apify actor runs]
    BR[Browser collection: Chrome, watch-page player data]
    MP[MP4 / MP3 local media]
    TR[Reference training corpus]
    FP[Studio exports: private]
  end
  W -->|hash, register_batch| RAW[data/raw + ledgers]
  SC --> RAW
  RAW -->|register_structured_source| INV[(inventory.db)]
  AP -->|apify_youtube_ingest + cost rows| INV
  SC -->|image_text_recognition.swift, load_ocr_results| INV
  INV -->|build_youtube_channel_registry| REG[(registry.db + FTS)]
  REG -->|frozen copy pin| FRZ[(frozen registry: audit baseline)]
  REG -->|build_finance_economics_complete_db, meta.built_from_registry_sha256| FE[(finance_complete.db)]
  AP --> FE
  AP --> SHA[(senior_health_apify.db)]
  BR --> SHC[(senior_health_core.db + shards)]
  SHA --> SHC
  MP -->|ffmpeg frames, Whisper base ASR| LA[~/YIOS-local-audits: local only]
  LA --> VF[visual forensic ledgers + SHA256SUMS seals]
  VF --> MAP[VISUAL_EVIDENCE_MAP.csv]
  TR -->|build_reference_kb| KB[(reference_knowledge.db)]
  FRZ --> AUD[NICK finance audits]
  AUD --> KB
  INV & REG --> INT[report_* layers]
  INT --> ART[data/intelligence JSON/MD]
  KB -.gate.-> ORCH[run_youtube_intelligence]
  ART --> ORCH --> PLAN[content plans]
  FP -->|ingest_youtube_analytics, gitignored| FPD[first-party diagnosis]
  FPD --> ORCH
  PLAN --> SCRIPT[scripts / recording packs]
  SCRIPT -->|check_slop_risk| PKG[production packages]
  FE & SHC & VF --> REP[owner PDF/HTML reports]
```

## Lineage guarantees today

| Guarantee | Mechanism | Gap |
|---|---|---|
| Raw immutability | ledger SHA-256 + `validate_dataset_ledgers` in CI | local-only media has no remote check |
| Field-level provenance | `field_provenance` (inventory only) | registry and branch DBs keep provenance in `raw_json`/`evidence_locator`/`sources` columns, not per field |
| Derived-artifact freshness | freshness registry `dependency_graph`, `invalidation_basis` | covers `data/intelligence` only, not branch reports or branch DBs |
| Builder reproducibility | FE `meta.built_from_registry_sha256` | SH DBs have no build hash recorded in-DB |
| AI vs fact separation | evidence layers; slop gate for scripts | semantic review is human-only and backlogged (26/558 pending) |

## Update frequency (observed)

| Data | Cadence |
|---|---|
| Competitor metadata | ad hoc batches (registry generated 2026-09-28; SH Chrome refresh 2026-11-11; exercise Apify 2026-11-14) |
| Finance audits | continuous agent sessions (NICK_xxx commits, ~2 per commit) |
| Intelligence artifacts | on refresh (latest V1 set 2026-09-09 to 09-11) |
| Reference KB | rebuilt on corpus change (2026-11-02) |

**UI implication:** every screen needs an "as of" date and a source-store badge, because the stores were captured at different times.
