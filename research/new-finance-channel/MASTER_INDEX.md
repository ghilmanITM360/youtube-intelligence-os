# NEW FINANCE CHANNEL — RESEARCH & INTELLIGENCE: MASTER INDEX

Working title only; the real channel name is decided in Phase I. Created 2026-11-18. Location: `research/new-finance-channel/` (untracked in the checkout on `data/apify-monkey-economics-primate-science-2026-11-18`; not committed). Source-of-truth folders are never edited: `research/finance-economics-channel-forensics/`, `research/finance-economics-intelligence/`, `data/catalog/`, `data/raw/`.

## Status of the 24 folders
| Folder | Status |
|---|---|
| 01_PROJECT_OVERVIEW | README + execution plan written |
| 02_FINANCE_CHANNEL_MASTER_INVENTORY | DONE: `MASTER_INVENTORY.md/.csv` (72 channels) |
| 03_PRIMARY_REFERENCE_CHANNELS | `STRENGTH_MATRIX_AND_LEARNINGS.md`, metrics CSVs, script (Phase B part 1 done; editing analysis NA) |
| 04_ADDITIONAL_FINANCE_CHANNELS | `ADDITIONAL_CHANNELS_LEARNINGS.md` |
| 05_FRESH_COMPETITOR_DATA | R1-R3 run and ingested (raw JSON, CSVs, status doc); account has about $3.04 left |
| 07_THUMBNAIL_LIBRARY | 61 primary thumbnails + montages + manifest |
| 10_SUB_NICHE_RESEARCH | `SUB_NICHE_DISCOVERY.md`, metrics CSVs, script (Phase C part 1; no demand validation yet) |
| 09_TOPIC_DISCOVERY, 11_GOOGLE_TRENDS_AND_NEWS, 12_YOUTUBE_SEARCH_AND_SUGGESTED | Phase D round 1 (25 seeds screened, 0 approved) |
| 13_TITLE_MODELS | Phase E: title/thumbnail/hook models, feature-lift script and CSV |
| 16 to 23 | filled by Phases F to Fourteen (see Reports available); 17 holds scorecard and Phase Ten, 18 packaging, 19 calendar, 20 branding, 21 workflow, 22 originality audit, 23 final strategy |
| 06, 08, 14, 15 | empty (no transcript library, visual-intelligence pass, winning-thumbnail or script-model folders were built; see the Phase Five addendum for what was computed) |
| 13_WINNING_TITLE_MODELS | empty duplicate of 13_TITLE_MODELS (left in place, nothing deleted) |
| 24_SOURCE_DATA_AND_REFERENCES | reuse/stale audit written |

## Reports available (this branch)
- `02_.../MASTER_INVENTORY.md`, `MASTER_INVENTORY.csv`
- `05_.../REFRESH_STATUS_AND_MISSING_DATA.md`
- `24_.../EXISTING_RESEARCH_REUSE_AND_STALE_AUDIT.md`
- `01_.../README.md`
- `01_.../01_KNOWLEDGE_BASE_FORENSIC_ANALYSIS.md` (Phase A)
- `10_.../SUB_NICHE_DISCOVERY.md` (Phase C)
- `09_.../TOPIC_VALIDATION_ROUND1_2026-11-18.md` (Phase D round 1)
- `09_.../TOPIC_VALIDATION_ROUND2_2026-11-18.md` (Phase D round 2: rent, airlines)
- `09_.../PHASE_D_CLOSURE_2026-11-18.md` (Phase D closure)
- `13_TITLE_MODELS/PHASE_E_TITLE_THUMBNAIL_HOOK_MODELS_2026-11-18.md`, `title_features.py`, `TITLE_FEATURE_LIFT_2026-11-18.csv` (Phase E)
- `09_.../PRIMARY_DATA_PULL_2026-11-18.md` (BLS and IATA primary check)
- `16_CHANNEL_POSITIONING/PHASE_F_POSITIONING_2026-11-18.md` (Phase F, master Phase Six: 3 concepts, recommendation, pending owner decision)
- `16_CHANNEL_POSITIONING/PHASE_G_FORMAT_DURATION_2026-11-18.md` (Phase G, master Phase Seven)
- `17_TOPIC_VALIDATION/PHASE_FOUR_TOPIC_SCORECARD_2026-11-18.md` (master Phase Four: 12 topics scored, revised weights, gates, categories)
- `12_.../SUGGESTED_OVERLAP_NOTE_2026-11-18.md` (Filter 6: UNKNOWN, test failed)
- `13_TITLE_MODELS/PHASE_FIVE_SCRIPT_AND_THUMBNAIL_INTELLIGENCE_ADDENDUM_2026-11-18.md`, `hook_features.py`
- `22_ORIGINALITY_AND_AI_SLOP_AUDIT/PHASE_EIGHT_ORIGINALITY_COPYRIGHT_SLOP_AUDIT_2026-11-18.md`
- `18_CONTENT_PACKAGING/PHASE_NINE_TOPIC_TITLE_THUMBNAIL_PACKAGING_2026-11-18.md`
- `17_TOPIC_VALIDATION/PHASE_TEN_FINAL_TOPIC_VALIDATION_2026-11-18.md`
- `19_30_DAY_CONTENT_CALENDAR/PHASE_ELEVEN_30_DAY_CALENDAR_2026-11-18.md`
- `20_CHANNEL_BRANDING/PHASE_TWELVE_BRANDING_DIRECTIONS_2026-11-18.md`
- `21_PRODUCTION_WORKFLOW/PHASE_THIRTEEN_PRODUCTION_WORKFLOW_2026-11-18.md`
- `23_FINAL_STRATEGY/PHASE_FOURTEEN_LAUNCH_AND_MEASUREMENT_2026-11-18.md`, `FINAL_STRATEGIC_RECOMMENDATION_2026-11-18.md` (includes the map to the master's 21 files)
- `DECISION_LOG.md`, `RESEARCH_CHANGELOG.md`

## Phase map (our working letters vs the master prompt)
A = master knowledge audit; B = Phase One; C = Phase Two; D = Phase Three; Four = scorecard (done 2026-11-18 audit pass); E = Phase Five (titles; script/thumbnail addendum); F = Phase Six; G = Phase Seven; then master Phases Eight to Fourteen by their own names. All 14 are now drafted; none is approved.

## Source datasets (read-only references)
- `data/catalog/finance_economics_complete.db`: 72 channels, 3,832 videos (3,804 dated), after the R1-R3 ingest of 2026-11-18 (uncommitted)
- `data/catalog/apify-2026-11-18-monkey-primate/` (raw Apify, SHA256SUMS)
- `research/finance-economics-channel-forensics/` (71 reports; `04_FINAL_SYNTHESIS`; `05_OWNER_QA/APIFY_SPOT_SCRAPES_*`)
- `research/finance-economics-intelligence/` (966/1,612 audits, thumbnail library, market gaps)
- Knowledge: `data/raw/global-youtube-knowledge/DS-000011`, `DS-000018`, `DS-000011-supplement-2026-11-11`, `DS-000031`; `DS-000011-DS-000018-DEEP-KNOWLEDGE-AUDIT.md`; `~/Downloads/YouTube_Automation_Complete_Master_Playbook.pdf` (556 pp, outside repo); `data/knowledge/reference_knowledge.db`; `scripts/check_slop_risk.py`

## Reference channels
P0: Casual Finance, Monkey Economics, MonkeyExplains, Crayon Capital, PaperBillionsTV, Capital Case. Others: see inventory (P1 15, P2 11, P3 40).

## Sub-niches: 5 candidates shortlisted in `10_.../SUB_NICHE_DISCOVERY.md` (S1 industry mechanisms, S2 company/history stories, S3 Shorts mechanisms, S4 news to balance sheets, S5 economics-of-owning format); none validated. Topic candidates: 16 earlier rejects + 1 conditional (C1) listed in the old `APPROVED_FIRST_10...` file; no topic is validated. Validated topics: 0 approved. After Phase D round 2 and closure (2026-11-18): rent (durable) and airfares (news, time-boxed) are CONDITIONAL and went to Phase E; generic "how airlines make money" rejected. Final decisions: see DECISION_LOG.md.

## Pending decisions
1. R1 DONE ($0.236), R2 DONE ($0.716), R3 DONE ($1.004). Apify account: about $3.04 left. Ingested into the DB (uncommitted working-tree change; commit/PR needs your go). Inventory CSV regenerated (72 channels).
1c. Check Mr. Finance anomaly by hand (fresh 20 videos not in DB).
1b. Commit the DB change on a branch / PR? (not done; two-Mac policy, no branch switch without your go).
2. Is the 2026-11-23 launch date still firm? Recommendation: NO; earliest 2026-12-14 (Phase Eleven). 0 topics approved.
2b. Approve, revise or reject the Phase Nine packages (V3 ports withdrawn); confirm voice, capacity, channel-separation (C2); answer the Apartment List gate yourself or supply a rent export; authorise a new topic pass for slots L3 to L5.
3. Keep the "adjacent" categories (retirement/senior, wealth-POV) as P3 reference only?

## Stale research
Trends/News/YouTube search of 2026-11-13/14; 30-day calendar; first-10 list; last-30-day windows for Casual Finance, MonkeyExplains, Crayon Capital.

## Missing data
See `05_.../REFRESH_STATUS_AND_MISSING_DATA.md` section 3. External sources used so far: 6 official YouTube Help pages (support.google.com/youtube answer ids 7628154, 16391400, 1311392, 6175006, 14328491, 9314355), fetched 2026-11-18.
