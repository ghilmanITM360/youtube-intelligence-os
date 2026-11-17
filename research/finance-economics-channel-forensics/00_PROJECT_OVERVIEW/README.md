# Finance & Economics — 69-Channel Forensic Channel Intelligence

Started 2026-11-12. One investigation area inside the existing YIOS repository (branch `data/finance-economics-complete-2026-11-11`, next to the database it studies). No new project root, no duplicated dataset: the database stays in `data/catalog/`, thumbnails and the computed feature tables stay in the local durable audit folder `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/` (not committed; raw media never goes through GitHub).

## Judges
- **Source A (judge):** YouTube Automation Master Playbook PDF → `PDF_KNOWLEDGE_MAP.md` (22 testable principles P01-P22).
- **Source B (supporting):** `data/raw/global-youtube-knowledge/` → `GLOBAL_KNOWLEDGE_MAP.md`.
- **Performers:** 69 channels in `data/catalog/finance_economics_complete.db` → `DATABASE_INVENTORY.md`.

## Layout
```
00_PROJECT_OVERVIEW/   README, MASTER_TRACKER.csv, DATABASE_INVENTORY.md, PDF_KNOWLEDGE_MAP.md, GLOBAL_KNOWLEDGE_MAP.md
01_CHANNEL_REPORTS/NNN_channel/   CHANNEL_REPORT.md (22 sections), EVIDENCE_DOSSIER.md, VIDEO_INVENTORY.csv,
                                  WINNING_VIDEOS.csv, FAILED_VIDEOS.csv, TOPIC_MAP.csv, SOURCE_MAP.csv
02_SHARED_EVIDENCE/    PDF_PRINCIPLE_EVALUATION(_AUTO).csv, RESEARCH_SOURCE_REGISTER.csv, EVIDENCE_LEDGER.csv
03_CROSS_CHANNEL_FINDINGS/   written only after all channel reports
04_FINAL_SYNTHESIS/          written only after cross-channel findings
05_OWNER_QA/                 OWNER_QA_REPORT.md (owner questions + answers, appended per question), CHANNEL_TIER_RANKING.csv
_analysis/             analyst text per channel (merged into CHANNEL_REPORT.md by _scripts/04_assemble.py)
_scripts/              01 build evidence · 02 dossiers · 03 PDF-principle metrics · 04 assemble reports
```

## Rebuild
Run with the audit venv: `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/.venv/bin/python _scripts/0N_*.py` in order 01→04. Inputs are read-only.

## Evidence discipline
VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN labels; no CTR, retention, impressions or traffic-source claims (not in data); correlation ≠ causation; Shorts separated from long-form; views always age-adjusted against the channel's own baseline.

## Status (2026-11-12)
All 69 channel reports saved (`MASTER_TRACKER.csv`: 69 COMPLETE, incl. 3 documented low-data exceptions — 064 Chronofold, 068 The Wealth Engine (6 videos), 069 Wealth Logic (removed by YouTube)). Cross-channel findings in `03_CROSS_CHANNEL_FINDINGS/`, final answers and blueprint in `04_FINAL_SYNTHESIS/`.
Evidence ledgers: `02_SHARED_EVIDENCE/CROSS_CHANNEL_CONCEPT_LEDGER.csv` (concept × channel × date × PI — serves as the EVIDENCE_LEDGER), `PDF_PRINCIPLE_EVALUATION.csv` (final verdicts) and `_AUTO.csv` (rule drafts), `RESEARCH_SOURCE_REGISTER.csv` (external checks). Start reading at `04_FINAL_SYNTHESIS/FINAL_RESEARCH_CONCLUSIONS.md`.
