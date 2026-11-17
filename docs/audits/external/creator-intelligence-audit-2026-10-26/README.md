# YIOS Creator Intelligence Audit — 2026-10-26

**Primary file:** `YIOS_COMPLETE_CREATOR_INTELLIGENCE_AND_ALGORITHM_MASTER_GUIDE.md`. Everything else exists to verify it.

| Path | Purpose |
|---|---|
| `ledger/SOURCE_DISCOVERY_INVENTORY.csv` | Discovery status, SHA-256, size, pages, coverage per source |
| `ledger/source_sha256_raw.tsv`, `ledger/text_map.tsv` | Raw hash manifest; source-ID ↔ file map |
| `ledger/extraction_notes.md` | Page-located extraction notes, written while reading |
| `ledger/CLAIM_EVIDENCE_MATRIX.csv` | 48 claims → official / YIOS evidence → classification |
| `ledger/EXTERNAL_SOURCES.csv` | Official URLs, publication and access dates |
| `ledger/ds18_targeted_claims.txt` | Numeric-claim extraction across DS-000018 tabs |
| `ledger/VALIDATION_REPORT.md`, `VALIDATION_RESULTS.json` | Checks |
| `ledger/CONTINUATION_HANDOFF.md` | Resume point |
| `scripts/build_ledgers.py`, `scripts/validate.py` | Reproduce (stdlib, `python3 -I`) |
| `sources_text/` | Text extracted from the originals (derived; originals untouched) |

**Privacy:** contains DS-000032 derived first-party analytics. Keep private. Not committed or published.
