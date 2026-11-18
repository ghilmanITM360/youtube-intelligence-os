# What-If-style science channel — research, calendar and brand (2026-11-18)

**Status:**
- Calendar **APPROVED** by the owner on 2026-11-18. Day 1 = **Monday 2026-11-23**.
- Channel name **decided 2026-11-18: Unreasonably Exact** (07). The handle must still be claimed in Studio.
- Day 1 script **APPROVED** (v1.1): `productions/unreasonably-exact-01-free-fall/`.
- Day 3 script drafted (v1.1, slop gate PASS): `productions/unreasonably-exact-03-neutron-bullet/`.
- Scripts are not written yet. Each one goes in `productions/<project>/**/*SCRIPT*.md` and must pass `scripts/check_slop_risk.py`.

## Read in this order

| # | File | What it answers | Brief step |
|---|---|---|---|
| 01 | [01_COMPETITOR_AND_SOURCE_BANK_AUDIT.md](01_COMPETITOR_AND_SOURCE_BANK_AUDIT.md) | xkcd catalog audit, micro-niches, top 10 longs and top 5 Shorts, 83 transcripts vs the book, IP boundary | 1, 2, 3, 5, 6, 7 |
| 02 | [02_LAST_30_DAYS_MARKET_SCAN.md](02_LAST_30_DAYS_MARKET_SCAN.md) | What uploads from the last 30 days and Google Trends show | 8, 9 |
| 03 | [03_COMPETITIVE_LANDSCAPE_AND_TOPIC_SCORING.md](03_COMPETITIVE_LANDSCAPE_AND_TOPIC_SCORING.md) | xkcd now, 48-channel census, format families, packaging, Method-4 demand/supply, scoring and top 25, cadence | 4, 8, 10, 11 |
| 04 | [04_COMPETITOR_CT_FINDINGS.md](04_COMPETITOR_CT_FINDINGS.md) | Forensics on 3 outlier videos (STRUCTURAL+, not a full CT scan) | 4 (deep) |
| 05 | [05_30_DAY_EXPERIMENTAL_CALENDAR.md](05_30_DAY_EXPERIMENTAL_CALENDAR.md) | **The approved calendar**, dated schedule, pre-production gates, Day 14 and Day 30 evaluations | 12, 13 |
| 06 | [06_SCIENCE_VERIFICATION.md](06_SCIENCE_VERIFICATION.md) | Science check of all 23 items; corrections applied to 05 | brief rule: "independently verify" |
| 07 | [07_CHANNEL_BRANDING.md](07_CHANNEL_BRANDING.md) | Name shortlist, logo, banner, watermark, descriptions | owner follow-up |
| 08 | [08_XKCD_OPENINGS_AND_COPYING.md](08_XKCD_OPENINGS_AND_COPYING.md) | How xkcd opens long videos (37/43 open with an attributed reader question), what we do instead, and what happens if a channel copies | owner follow-up |

**Framework record:** [calendar_plan_framework_2026-11-18.json](calendar_plan_framework_2026-11-18.json). It passes `content_plan_check.py`, which is a STRUCTURAL check only.

## Folders

- `data/`: dated, read-only observation snapshots plus derived tables. Each report's Sources section gives the ID and sha256.
  - `question_bank_63.csv`: **paraphrased** premises only, never book text.
  - `book_chapter_to_video_map.json`: chapter titles plus transcript matches.
  - `book_ocr_source_sha256.txt`: hashes of the private book OCR. The OCR text is not in the repo.
  - `channel_census_*.tsv`, `m4_demand_supply_scan_*.tsv`, `yt_search_thismonth_*.tsv`, `google_trends_*.tsv`, `xkcd_*`: Chrome observations from 2026-11-18. They are personalised (signed-in) and biased toward surviving videos.
  - `topic_scores_2026-11-18.csv`: output of `scripts/score_topics.py`.
  - `name_collision_checks_2026-11-18.tsv`: brand-name and handle checks.
- `scripts/`: reproducible derivations.
  - `book_vs_transcripts.py`, `niches.py`: report 01.
  - `score_topics.py`: report 03.
  - `verify_science.py`: report 06; recomputes every number, about 6 s.
- `branding/`: SVG sources, PNG uploads at YouTube sizes, plus the generator.
  - Regenerate: `python3 make_brand_assets.py && sh render.sh` (needs Google Chrome and the macOS fonts Avenir Next and Menlo).

## Evidence kept outside Git (by rule: no private media in the repo)

| What | Where (Machine B) |
|---|---|
| 3 competitor MP4s (owner-approved download) | `$YIOS_MEDIA_ROOT/WhatIfCompetitors-MP4/` = `/Users/ghilmanislam360/Documents/YIOS-Media-Library/WhatIfCompetitors-MP4/` |
| CT-pass evidence: manifest, coverage, quality gate, contact sheets, transcripts | `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-18/WHATIF_COMPETITOR_CT/` |

The SHA-256 prefixes of the MP4s are in 04. Machine A does not have these files.

## Owner decisions on record

| Date | Decision |
|---|---|
| 2026-11-18 | Use the 63-question bank; Chrome/YouTube census and last-30-days scan approved |
| 2026-11-18 | All 4 decisions in 03 §10 approved: scoring weights and top 25; no xkcd remake within 12 months (at most one older remake); 2 longs + 3 Shorts per week, week 1 front-loaded; download 3 competitor videos |
| 2026-11-18 | Titles: "What if" for hypotheticals; "What will" **only** for real future events (Day 6 → "What Will Apophis Look Like on 13 April 2029?") |
| 2026-11-18 | Calendar approved; Day 1 = Monday 2026-11-23 |
| 2026-11-18 | Channel name: Unreasonably Exact |

## Open before Day 1 (owner)

1. Claim @unreasonablyexact in YouTube Studio, plus the same name on other platforms (not checked).
2. Register the channel's CH-id, then run `scripts/run_youtube_intelligence.py --framework-plan calendar_plan_framework_2026-11-18.json`.
3. Production-time risk: the calendar assumed about 10 production days for the Day 1/3/5 longs, and only 5 remain. The fallback is in 05.

## Known limits

- No first-party analytics exist yet. Competitor numbers are public display counts.
- The CT pass is STRUCTURAL+ only (04 §4).
- The science pass is an AI pre-check that no human expert reviewed (06). Each script still needs its own claim table.
