# RESEARCH CHANGELOG

| Date | Change | Reason |
|---|---|---|
| 2026-11-18 | Monkey Economics (60) + Primate Science (10) Apify data merged to main (PR #62, cf2dbb2); about $0.27 | owner request; data now in `finance_economics_complete.db` |
| 2026-11-18 | Workspace created with 24 folders | new-channel research branch |
| 2026-11-18 | Master inventory generated from DB (read-only) | deliverable 1 |
| 2026-11-18 | Refresh status, missing-data report, paid-refresh estimate | deliverables 2 to 4; no spend |
| 2026-11-18 | R1 approved by owner but NOT run: Apify Console billing shows $9.73 of $10.00 free usage used, $0.27 left (period Nov 11 to Dec 10); R1 estimate about $0.40 | budget blocker, no spend |
| 2026-11-18 | Owner switched Apify account (free $5.00). R1 executed: 2 runs, 56 videos, $0.236. Raw in `05_FRESH_COMPETITOR_DATA/raw/` + CSV. DB not yet updated | R1 approval |
| 2026-11-18 | R2 executed (owner approved): 2 runs, 180 videos, $0.716; real dates for 6 channels. Raw + CSV in `05_FRESH_COMPETITOR_DATA/`. DB not yet updated | R2 approval |
| 2026-11-18 | R3 executed (owner approved): 4 runs, 243 videos, $1.004; 12 additional channels. Account total $1.956 of $5.00. Raw + CSV in `05_FRESH_COMPETITOR_DATA/`. DB not yet updated. Flags: Mr. Finance anomaly, Nostalgic Wheels renamed | R3 approval |
| 2026-11-18 | R1+R2+R3 ingested into `finance_economics_complete.db` (138 new videos, 341 updated, 2 new channels, 152 dated); not committed | owner approved ingest |
| 2026-11-18 | Phase A written: `01_PROJECT_OVERVIEW/01_KNOWLEDGE_BASE_FORENSIC_ANALYSIS.md`; 6 official YouTube Help pages fetched and verified | phase A |
| 2026-11-18 | Phase B part 1: inventory regenerated from refreshed DB; metrics for 23 channels; 61 primary thumbnails downloaded (public, i.ytimg.com, 7 MB); strength matrix + additional-channel learnings written | Phase B |
| 2026-11-18 | Reuse/stale audit of the 11-13/14 blueprint | deliverable 5 |

- 2026-11-18: Phase C part 1. Added `10_SUB_NICHE_RESEARCH/` (metrics script, 4 CSVs, `SUB_NICHE_DISCOVERY.md`). Title-keyword classification of 3,486 long videos; 5 candidates shortlisted. No paid run, no Trends/Search validation, nothing committed.
- 2026-11-18: Review of Phases A-C: corrected Shorts counts (Monkey Economics 42/60, Casual Finance 185/223), excluded Mr. Finance from Phase C stats (business-economics ratio 1.48 to 1.34), refreshed stale MASTER_INDEX lines. Phase D round 1: 25 seed topics screened (search supply CSV, Trends by eye, 2 news hooks); 0 approved, 2 advance (rent, airlines with angle). Nothing committed.

- 2026-11-18: Phase D round 2 (rent, airlines): autocomplete, 7 alternate search phrasings, 4 transcripts, BLS/IATA via web search. 0 approved; 2 conditional, 1 rejected. File `09_TOPIC_DISCOVERY/TOPIC_VALIDATION_ROUND2_2026-11-18.md`.

- 2026-11-18: Phase D closure (BLS CPI release opened: shelter +3.2%, airline fares +22.4%; pipeline-copy check; old rejects spot-checked) and Phase E (title feature lift over 64 channels, 6 title candidates, 4 thumbnail briefs, 2 hook models). No scripts, nothing committed.

## 2026-11-18 Primary data pull
- BLS rent methodology and IATA release verified; Apartment List and Zillow failed. See `09_TOPIC_DISCOVERY/PRIMARY_DATA_PULL_2026-11-18.md`.

## 2026-11-18 Full re-audit and Phases Four, Eight to Fourteen
- Re-audit: recomputed Phase B/C/E numbers from the DB and fixed about 15 errors and stale lines (see DECISION_LOG row). Read BLS Sep and Oct CPI in Chrome; Apartment List gate not answered on the owner's behalf; Suggested sidebar test failed (personalised).
- New files: Phase Four scorecard, Phase Five addendum (hook_features.py), Phases Eight, Nine, Ten, Eleven, Twelve, Thirteen, Fourteen, final recommendation. No spend, no commit, no scripts. Chrome tabs I opened were closed or restored.

## 2026-11-18 Scripts and last data reads
- Read Oct CPI table and Zillow ZORI in Chrome; wrote draft scripts V1, V2 under `productions/` (gate WARN R7 only). No spend, no commit.

## 2026-11-18 Phase G format and duration
- `16_.../PHASE_G_FORMAT_DURATION_2026-11-18.md`; Phase F defaults adopted on "take best decision". No data, no spend, nothing committed.

## 2026-11-18 Phase F positioning
- `16_CHANNEL_POSITIONING/PHASE_F_POSITIONING_2026-11-18.md`: 3 concepts, recommendation, owner decisions. No data pulled, no spend, nothing committed.

## 2026-11-18 Phase E claim check
- Fixed stale MASTER_INDEX validated-topics line.
- Phase E: R2/T-R2 "a Year Late" corrected to a ~6-month CPI rent lag (BLS snippets; read full page before use). A2 $400 illustrative. A3 fuel figures consistent across outlets, SECONDARY.

## 2026-11-19 Audit P0 fixes
- Independent audit written to `audit/` (20 files, score 55.5/100, REJECTED - REWORK REQUIRED). P0 work: transcript manifest (3,617 rows) + READMEs for the 5 empty folders (08 stays "NOT DONE"); calendar addendum with 12 of 13 slots researched (0 validated) and a date defect found (L5 before the 2027-01-13 CPI release). No spend, no scripts, nothing committed.

## 2026-11-19 L3/L4 validation
- Opened EIA pump-components table and BLS CPS page; logged-out YouTube search for both topics. L4 rejected, L3 conditional. No spend, nothing committed.

## 2026-11-19 L3 finish and new L4
- Opened BLS Employment Situation note and release schedule, GAO-26-107538, BLS 2027 CPI weight page; ran Trends (US, 12 months) and 4 logged-out YouTube searches. L3 conditional, new L4 conditional, gas L4 stays rejected. No spend, nothing committed.
