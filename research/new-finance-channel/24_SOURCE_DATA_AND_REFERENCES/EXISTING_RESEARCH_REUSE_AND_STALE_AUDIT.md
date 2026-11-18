# Existing research: reuse vs stale audit (2026-11-18)

Scope: first pass from the heads of the key files in `research/finance-economics-channel-forensics/04_FINAL_SYNTHESIS/` and the DB. I did not re-verify every claim. Anything marked "re-check" needs a fresh read. Nothing was modified; this branch only references the originals (paths relative to `research/finance-economics-channel-forensics/` unless noted).

## 1. Verdicts

| Existing item | Verdict | Why | Action |
|---|---|---|---|
| 71 channel reports (`01_CHANNEL_REPORTS`) | REUSE as historical base | Built from the DB through about 2026-11-12. Missing: Monkey Economics (no folder; added today), dates for 192 videos | Add Monkey Economics report; refresh primary 6 |
| Cross-channel findings, winning/failure patterns, sub-niche comparison (`03_`) | REUSE with caution | Selection by views creates bias; the blueprint itself says so | Re-test after refresh |
| 966 / 1,612-video audits (`research/finance-economics-intelligence/`) | REUSE, treat as one evidence base with the 69-channel work | Overlapping channels; not independent | Do not count twice |
| Thumbnail pattern library, 966-thumbnail CSV | REUSE patterns, re-sample new ones | Thumbnails of videos older than ~Oct 2026 | Add 2026-11 samples |
| `CHANNEL_BLUEPRINT_2026-11-14` | RECONSIDER | Everything predictive is labelled HYPOTHESIS; narrow niche "dated money event tied to viewer's money" | Re-evaluate against sub-niche discovery (Phase C) |
| `APPROVED_FIRST_10_VIDEOS_2026-11-14` | **Not a list of approved videos**: result is 0 of 10 approved, 16 candidates screened and rejected, 1 conditional (C1 card-delinquency vintages) | Strict rule rejected topics with demand because they were already covered | Treat as a screening log and rejection list. The 16 rejections are a useful "do not repeat" base but are 4 days old; re-check |
| `TREND_AND_COMPETITOR_RECHECK_2026-11-14` | STALE for Trends/News/search | Time-sensitive, dated 11-14; some inputs were news spikes | Redo for shortlist (Phase D) |
| `TOPIC_DISCOVERY_PILOT_2026-11-13` | STALE data, REUSE method | Pilot of the 7-filter method | Reuse the method |
| Competitive set: "nine-channel study" | REUSE | Primary-6 only partly overlap with those nine | Extend to the six you named |
| 30-day plan / launch manual (`*_30_DAY*`, `LAUNCH_MANUAL`) | RE-DATE | Built around topics that failed screening; launch date now 2026-11-23 | Rebuild in the calendar phase (master Phase Eleven) from validated topics. Phase letters in this file's older rows (F, H) follow the original master-prompt list; see the phase map in `MASTER_INDEX.md` |
| `SCRIPTS_VIDEO_1_AND_2_2026-11-16` | **ON HOLD** | You said no scripts until topics/titles/thumbnails are validated | Leave untouched |
| `PLAYBOOK_RUBRIC_SCORECARD` | REUSE; per-channel page-numbered scores were a gap (gap map) | | Phase A |
| `MASTER_PROMPT_GAP_MAP_2026-11-13` | REUSE as checklist | Lists blockers: no Studio data, PDF pipeline untested, Chrome searches pending | Merge into this branch's plan |
| `FINANCE_ECONOMICS_WINNING_MODELS` | RE-TEST | Based on an older sample | Phase E |
| `ORIGINAL_FINANCE_CHANNEL_OPPORTUNITIES` (intelligence folder) | REUSE as candidate pool | 7 provisional treatments, none validated | Phase D scoring input |
| DS-000011 / DS-000018 audit (repo root, 2026-09-24) | REUSE | 33 claims: 10 supported, 12 partial, 1 contradicted, 8 lacking primary support, 2 not verifiable. DS-000018 is one third-party Google Doc, not official | Re-verify only the algorithm claims we rely on |

## 2. Findings that look still valid (INFERRED, re-check on fresh data)
- Real, dated event plus viewer-money link outperformed abstract institution/concept videos in most of the nine channels.
- Topics with measurable demand were mostly already covered by large channels (the 16-candidate screen).
- No universal CTR/retention threshold is supported by evidence; competitor CTR/retention are UNKNOWN.

## 3. Findings that are weak or stale
- "No Shorts in the first 10" conflicts with the data: Monkey Economics has 42 of 60 items as Shorts, Casual Finance 185 of 223 (83%), Primate Economics' top video is a Short (15.7M views). Re-evaluate formats in Phase F.
- Any claim about "last 30 days" for Casual Finance, MonkeyExplains and Crayon Capital: the DB has 0 videos in that window.
- Trends and news interest as of 11-13/14.

## 4. Source of truth preserved
No file under `research/finance-economics-channel-forensics/`, `research/finance-economics-intelligence/`, `data/catalog/` or `data/raw/` was changed. New work lives only in `research/new-finance-channel/` (untracked, current checkout `data/apify-monkey-economics-primate-science-2026-11-18`, no branch switch).
