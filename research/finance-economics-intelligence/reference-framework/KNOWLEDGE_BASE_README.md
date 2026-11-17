# Reference knowledge base (v1) — storage, retrieval, rebuild, enforcement

Database: `data/knowledge/reference_knowledge.db`, built with the project's own `schemas/inventory/001–011` migrations (schema_meta version 11 = `011_reference_knowledge.sql`). It is a separate file because `validate_research.py` pins `data/catalog` as frozen input (diff against `03a6cd0` must be empty); the inventory DB is unchanged. Sources link to existing identities by SRC id and SHA-256 (`ref_source_member.source_id`); no second source registry is created.

| Table | Content |
|---|---|
| `ref_source_member` | 20 ZIP members, SHA-256, alias/canonical links, disposition |
| `ref_section` (+`ref_section_fts`) | 1,260 locator-addressed sections; raw text only for canonical members (aliases keep hashes) |
| `ref_constituent_video` | 63 title-marked videos of the algorithm compilation (v2 index; see `REFERENCE_DISCREPANCY_RESOLUTION_v1.md`), title + line range |
| `ref_rule`, `ref_rule_conflict` | 33 rules v1 (30 applicable), class, evidence required, applicability; 3 conflict/overlap rows |
| `ref_platform_verification` | 9 claims vs official YouTube pages (accessed 2026-11-02) |
| `ref_analysis_run`, `ref_video_assessment`, `ref_plan_application` | reanalysis judgments with witness offsets; plan applications |

Retrieval: `python -c "import sqlite3,build_reference_kb as k; print(k.search(sqlite3.connect('data/knowledge/reference_knowledge.db'),'open loop'))"` (FTS5, no paid vector service). Retrieve by rule dimension from `ref_rule` first, then FTS for passages.

Rebuild / portability: `python build_reference_kb.py <new-path>.db --fresh` (the target must not already exist; build to a temporary path, then copy over `data/knowledge/reference_knowledge.db` after reassessment files change) applies all migrations and loads from versioned sources (`corpus/REFERENCE_SECTIONS_v1.jsonl.gz`, the three CSVs, constituent JSON, `reanalysis/videos/*.json`). Verified 2026-11-02: a fresh rebuild reproduces the live tables (section-hash digest equal, 33 rules, same assessment count) and `sqlite3 .backup` restores with `integrity_check` ok. The ZIP itself stays outside Git (SHA-256 `d2114224…15f`).

## Coverage status (honest)
- **Stored and locator-addressed:** all 20 members, 1,260 sections (`REFERENCE_CORPUS_COVERAGE_v1.csv`). One blank page: Title Analyzer p.6. The DOCX/MD/TXT/XLSX algorithm compilation is one body (aliases of the DOCX).
- **Defects not resolved:** PDF text layers drop `f`/`fi` glyphs; no OCR engine (tesseract) is installed, so those pages are text-extracted but not glyph-verified. DOCX embedded images are unread. Text is never guessed-repaired.
- **Rule extraction is partial:** 30 analytical rules (27 creative heuristics, 2 superseded duplicates, 1 empirical hypothesis; plus 3 NOT_APPLICABLE records = 33) come from Viral Checklist, Intro/Title/Script Analyzer, BUT/THEREFORE, 16 Commandments, SEO and Hook guide pages. Not yet rule-extracted: the bulk of the Hook guide (58 pp.), Renae blueprint, VIDEO EDITING, VEO 3 and Nano-Banana prompting guides, the 117-page algorithm guide, `new YT algorithms updates` and the 63 constituent videos beyond their index. **The corpus is therefore NOT declared fully processed.**

## Enforcement
- `python reference_comparison.py check-all` — fails if any accepted NICK_281+ batch lacks a validating comparison or any reanalysis file fails validation.
- `python content_plan_check.py data/knowledge/reference_knowledge.db <plan.json>` — a content plan must retrieve existing sections, cover all 7 stages and give an implementation or exception per rule; empty retrieval fails explicitly (`RETRIEVAL_EMPTY`). Structural only; it never certifies semantic quality.
- Rules never become automatic scores: hedged retention rules, platform claims and "dead channel / fresh email / fixed schedule" theories stay hypotheses. Specificity earns no credit when a figure is wrong (see FR-VC-05 in `-CbNGP9H4xw`).


## Enforcement entry points (2026-11-02)
- `scripts/run_youtube_intelligence.py --framework-plan <plan.json>`: plan must pass `content_plan_check.py` against `data/knowledge/reference_knowledge.db` (retrieval present, real and applicable rules, rule dimension fits stage, rule source section retrieved, non-trivial text, each of seven stages implemented or reasonably excepted, at least one rule implemented) before any plan is written; exit 2 otherwise. Without the flag the plan carries no `reference_framework` block and must not be described as framework-guided.
- `research/finance-economics-intelligence/validate_audit_966.py`: now runs `reference_comparison.check_coverage()` (accepted NICK_281+ batches need a comparison that validates and matches the batch and video; every ledger reanalysis file must validate). Failing it fails the canonical audit validation.
- `AGENTS.md` records the requirement. All gates are structural; none set a record to semantically reviewed.
- Tests: `reference-framework/test_reference_comparison.py` (missing retrieval, invalid rule, missing implementation fail; valid plan and an explicit exception pass).
