# Validation report — 2026-10-26

Command: `python3 -I scripts/validate.py <audit_root> <repo>`. Result: **141 checks, 0 failures** (`ledger/VALIDATION_RESULTS.json`).

## What was checked
1. **Repository untouched by this audit.**
   - Census ref `d987510b` is an ancestor of live HEAD `df80644a`.
   - All files changed between them are under `research/finance-economics-intelligence/` (concurrent Finance writer, NICK_174–179).
   - The worktree is clean.
   - The registry and inventory DB SHA-256 hashes are unchanged.
2. **Source integrity.** All 19 source files re-hashed. Each hash equals the ledger value and appears in the guide (Part X.1).
3. **Coverage.** Every row of `SOURCE_DISCOVERY_INVENTORY.csv` (found, absent, out-of-scope, inaccessible, secondary) is represented in the guide.
4. **Paths.** Every backticked repo path in the guide exists at the census ref, at the PR #44 ref `badec432`, or as a local ignored file (the two 0-byte DBs).
5. **Video IDs.** Every backticked 11-character ID resolves to the registry/receipts, the DYH register/checkpoint/handoff, or a documented What If, Finance-ledger or Creator Insider ID.
6. **Numbers.** These figures were recomputed from receipts or repo files:
   - 449 at census and live 455/1,157.
   - 1,612.
   - H02 1.35/0.96; H03a 0.75/1.10; H11a 0.74.
   - 0/14 survived.
   - 33-channel concentration.
   - DYH lifetime 8,366 views / 36,159 impressions / 3.0%; 56 videos / 46 curves.
   - VF 507 states / 24.1 cuts/min.
7. **Structure.** Parts I–X are present. Domains A–K each have source-teaching and evidence/technical blocks.

## Re-used, not re-run
- The statistical analysis (`YIOS-Algorithm-Audit-2026-10-26/scripts/analyze.py`) was `RECEIPT_REVIEWED_NOT_RERUN`. Its QA script was re-run today: all PASS.
- DS-000018: 62 of 63 tabs were indexed and keyword-extracted, not read word-for-word.

## Known residual risks
- Official Help pages are undated. Content can change after 2026-10-26.
- T39 is spoken, transcribed by a third party into a Google Doc; wording is approximate.
- DS-000032 figures are DERIVED_PRIVATE_ANALYTICS. Keep this guide private.
- PDF page numbers come from text extraction (form-feeds). Locators for S13/S15 could be off by one where a page begins mid-paragraph.
