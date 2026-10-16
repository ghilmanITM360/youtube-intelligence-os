# Reproducible baseline methods

Run `python3 research/finance-economics-intelligence/build_baseline.py` from the repository root. SQLite opens with `mode=ro`; the database hash must be identical before and after. Source videos/transcripts are never rewritten. CSV rows retain dataset IDs and exact evidence locators. Run the companion unittest discovery command in RESUME_HERE.md.

Selection: existing inventory rows where Scope=CANONICAL and Niche!=ADJACENT. Thirteen channels, not all 18 canonical inventory rows. Identity leads and the two research overlays are separate populations.

Metric date: DS-000020/21 use manifest collection/packaging date 2026-09-12; DS-000023/24 use 2026-09-13. Day-level precision is approximate. DS-000022 now uses the source-declared scrape day 2026-09-11 from four immutable workbooks, not their 2026-09-12 ingestion date. Exact A2 statements, hashes and 595-row reconciliation are in METRIC_DATE_EVIDENCE.csv. The original Actor logs and scrape timezone were not supplied. DS-000001 remains undated for ranking; its ingestion date does not certify collection time. No saved views are presented as current.

Format: explicit `Short`/`shorts` becomes SHORTS; `video`/`regular video` becomes LONG_FORM, retaining original values. Null remains UNKNOWN. Duration is never a substitute for format identity. Malformed publication dates remain raw and unparsed.

Performance: require a parseable publication date, collection day, age >=7 days, known format and non-null views. Select up to 10 nearest-age OTHER videos within the same channel, format and snapshot, restricting peer age to 0.5–2 times target age. At least five peers and positive median lifetime views/day required. Ratio = target lifetime views/day / peer median. STRONG >=2; WEAK <0.5; TYPICAL otherwise. Thresholds are analyst choices, not YouTube categories. CSV records exact peer IDs and denominator size. Launch bursts, day-level date error, channel growth, topic selection and distribution remain confounders; rate is not current velocity or causal impact. Old research overlays retain their own methods and must not be pooled with these labels.

Transcript deduplication: SHA256 of stored UTF-8 plaintext, with duplicate pointer; word counts are regex tokens and can differ from source counters. Available text is not certified complete narration or human verification. All text features are lexical proxies. Punctuation-based sentence length is ASR-sensitive. Evidence-marker counts do not verify citations; causal-marker counts do not certify mechanisms. No 3/10/30-second or narration-rate estimates from untimed text. Keyword topic labels may overlap and are not semantic findings. Unknowns are explicit.

These scripts are research utilities, not a new production intelligence layer. All generated tables are research-only.

Legacy follow-up: [LEGACY_METADATA_PROBE.json](LEGACY_METADATA_PROBE.json) records the existing inventory catalog's candidate DS-000001 observation day, 2026-08-24, for all 159 records. The original date provenance still needs verification and all formats remain null; no tiers were promoted. Do not repeat this catalog lookup.

Continuation: run `build_comparisons.py` after `build_baseline.py` to regenerate five-peer sensitivity, DS-000022 ±1-day sensitivity, feature comparisons and current values for the same 30 sampled IDs. Date sensitivity moves the snapshot for the entire matched cohort, retaining publication dates, then recomputes peer eligibility and ranks. It is a sensitivity check, not evidence that the true collection time lay exactly one day either side.

`verify_workbook_dates.py` reopens the four original DS-000022 workbooks read-only using openpyxl, checks source hashes and the exact scrape-day statement, and reconciles IDs/titles/views/publication strings. Explicit source `N/A` views map to missing, never zero. Run with an available Python containing openpyxl; the bundled runtime was used for this check. It writes only research/METRIC_DATE_EVIDENCE.csv. No source workbook is authored or modified.
