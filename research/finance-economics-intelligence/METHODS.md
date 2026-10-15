# Reproducible baseline methods

Run `python3 research/finance-economics-intelligence/build_baseline.py` from the repository root. SQLite opens with `mode=ro`; the database hash must be identical before and after. Source videos/transcripts are never rewritten. CSV rows retain dataset IDs and exact evidence locators. Run the companion unittest discovery command in RESUME_HERE.md.

Selection: existing inventory rows where Scope=CANONICAL and Niche!=ADJACENT. Thirteen channels, not all 18 canonical inventory rows. Identity leads and the two research overlays are separate populations.

Metric date: DS-000020/21 use manifest collection/packaging date 2026-09-12; DS-000023/24 use 2026-09-13. Day-level precision is approximate. DS-000001/22 ingestion dates do not certify observation time; their metrics remain undated for ranking until original metadata establishes collection time. No saved views are presented as current.

Format: explicit `Short`/`shorts` becomes SHORTS; `video`/`regular video` becomes LONG_FORM, retaining original values. Null remains UNKNOWN. Duration is never a substitute for format identity. Malformed publication dates remain raw and unparsed.

Performance: require a parseable publication date, collection day, age >=7 days, known format and non-null views. Select up to 10 nearest-age OTHER videos within the same channel, format and snapshot, restricting peer age to 0.5–2 times target age. At least five peers and positive median lifetime views/day required. Ratio = target lifetime views/day / peer median. STRONG >=2; WEAK <0.5; TYPICAL otherwise. Thresholds are analyst choices, not YouTube categories. CSV records exact peer IDs and denominator size. Launch bursts, day-level date error, channel growth, topic selection and distribution remain confounders; rate is not current velocity or causal impact. Old research overlays retain their own methods and must not be pooled with these labels.

Transcript deduplication: SHA256 of stored UTF-8 plaintext, with duplicate pointer; word counts are regex tokens and can differ from source counters. Available text is not certified complete narration or human verification. All text features are lexical proxies. Punctuation-based sentence length is ASR-sensitive. Evidence-marker counts do not verify citations; causal-marker counts do not certify mechanisms. No 3/10/30-second or narration-rate estimates from untimed text. Keyword topic labels may overlap and are not semantic findings. Unknowns are explicit.

These scripts are research utilities, not a new production intelligence layer. All generated tables are research-only.
