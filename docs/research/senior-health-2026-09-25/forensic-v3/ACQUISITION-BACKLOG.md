> **CORRECTION (2026-09-25, live re-verification):** Group A is not uniformly complete and Group B is not empty. Better Health While Aging (acquired after this file was written, DS-000033) is PARTIAL: 4 oldest Shorts missing. Dr. Elias (+12), Dr. Ares (+2) and Senior Health Hub (+1) have post-snapshot uploads. Senior Fitness With Meredith's 454 items include 100 archived streams. Current counts, exact missing IDs and the run plan are in `SENIOR-HEALTH-MASTER-INVENTORY-REPORT.md`. The body below is preserved as a historical record.

# Senior Health Acquisition Backlog (Phase 8) — 2026-09-25

**Status:** Planning only. Zero-spend. No Apify run has been started from this document. Cost figures use the last independently-verified live price (`$4.00 / 1,000 videos` = `$0.004/video`, Free plan, confirmed 2026-09-22/23 in `docs/audits/SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md`) — **this must be re-verified live before any run** (see Phase 9 note at the end); it is not re-checked here because that step touches the live Apify account and is intentionally left for explicit authorization.

Sources: `COMPETITOR-DISCOVERY-REGISTER.md` (Parts A and B), `CHANNEL-REGISTRY-CLASSIFICATION.md`, `data/catalog/youtube_channel_registry.db`.

---

## Group A — Existing Senior Health channels with complete datasets (no reacquisition needed)

| Channel | Canonical ID | Dataset | Status |
|---|---|---|---|
| Dr. Okoro | `UCMJxAeBJ0d1JC937de1eZ0Q` | DS-000028 | STANDARD_PACKAGE, 66 videos, 66 transcripts — complete |
| Doctor Thomas | `UCFuGMi0idGeyXl6wYK9hg7Q` | DS-000029 | STANDARD_PACKAGE, 22 videos, 21 real transcripts + 1 explicit gap — complete with a disclosed gap, not a blocker |
| Senior Health Hub | `UCAYG0fzUyxv6OevH88qA45w` | DS-000030 | HISTORICAL_CATALOG, 122 videos, 122 transcripts — complete |
| Dr. Ares Senior | `UC356D-NzdnznBOftTpYoBLw` | (pre-existing) | 35 videos, complete per Stage 2 re-verification |
| Dr. Elias Senior Health | `UCQcBYZxFW7YwNMU8-DsT3Uw` | (pre-existing) | 29 videos, complete per Stage 2 re-verification |
| Dr. Aliza Wright \| Advice | `UCXZi5JVeuTluazF-fYqQgNA` | DS-000006 | HISTORICAL_CATALOG, 32 videos, 32 transcripts — complete |

**Action: none.** Do not reacquire. (Caveat carried from `STAGE2-CORRECTION-LEDGER.md` NC-06: 2 of these 6 share verbatim-duplicate titles with each other — a content-mill signal, not a data-completeness issue — see that ledger before treating all 6 as fully independent evidence.)

## Group B — Existing Senior Health channels with missing metadata

**None identified.** All 6 Group-A channels are already `STANDARD_PACKAGE` or `HISTORICAL_CATALOG` with full video/transcript coverage; no partial-metadata cohort channel exists to prioritize here.

## Group C — Previously discovered and newly qualified competitors (acquisition candidates, pending budget authorization)

Priority tiers: **P1** = highest confidence + largest evidentiary value; **P2** = solid direct fit; **P3** = qualified but lower priority or needs monitoring before committing budget.

| Priority | Channel | Canonical ID | Source | Videos (observed) | Est. cost @ $0.004/video | Reason |
|---|---|---|---|---|---|---|
| P1 | Better Health While Aging | `UCFpxvukIqCAUA7YizI-q9Dw` | Recovered (Tier A) | 98 | ~$0.39 | Only candidate anywhere in this research with an independently, externally verifiable clinical credential (Dr. Leslie Kernisan, MD MPH, betterhealthwhileaging.net) — highest-value addition for medical-review comparison work |
| P1 | Senior Wellness | `UCslmaJaMSw8F8BId4CxByJw` | Recovered (Tier A) | 99 | ~$0.40 | Large, 10/10 explicit senior-fit titles, active cadence |
| P1 | More Life Health Seniors | (not registered) | New (Part B) | 162 | ~$0.65 | Large catalog, externally-verifiable physiotherapist founder |
| P1 | Senior Fitness With Meredith | (not registered) | New (Part B) | 454 | ~$1.82 | Largest catalog of any unacquired candidate, named instructor, 6+ year history — highest statistical power for a new-cohort addition |
| P2 | Senior Health Today | `UCLxLjL1XVaKqZg-wZ2EBspA` | Recovered (Tier A) | 57 | ~$0.23 | Focused, active, explicit senior-fit |
| P2 | Dr. Brooks \| Senior Health | `UClzqmRzoC-7r8GiB_XQUn_A` | Recovered (Tier A) | 107 | ~$0.43 | Active, broad senior-health topics; "Dr." unverified (flag in analysis, not a disqualifier) |
| P2 | Healthy Aging Hub | (not registered) | New (Part B) | 516 | ~$2.06 | Largest catalog in the entire candidate set; highest cadence (~every 2 days) — valuable for upload-cadence/breakout research at scale |
| P2 | The Senior Centered PT | (not registered) | New (Part B) | 66 | ~$0.26 | Strongest doctor-led/clinician credibility case (Board Certified Geriatric PT specialist, verifiable) in the whole candidate set, though upload cadence has slowed |
| P3 | Dr. Nora Khalil | `UCX_cW2SeHF1iBxbjx41vfrA` | Recovered (Tier A, lower priority) | 65 | ~$0.26 | Mixed general/senior, moderate confidence |
| P3 | Dr. Franklin Senior Health | `UCPjG4ZRBkiO1y_vHlnj8jIg` | Recovered (Tier B) | 37 | ~$0.15 | Smaller, less-recent catalog |
| P3 | Senior Vital Health | `UCUUKjcYdqOHk2j-pbUnWDNw` | Recovered (Tier B) | 195 | ~$0.78 | Large but only 2/10 recent titles are explicitly senior-framed — needs the acquired transcripts to confirm topic fit before treating as core cohort |
| P3 | Senior Meal Coach | (not registered) | New (Part B) | 94 | ~$0.38 | Fills the senior-nutrition sub-niche gap, but cross-branded with sibling channels — flag before treating as independent |
| P3 (small-channel/breakout watch — lower per-run cost, valuable for the breakout-forensics line of research, not general cohort expansion) | Senior Mobility Care | (not registered) | New (Part B) | 15 | ~$0.06 | Thin catalog, genuinely senior-focused, good small-channel breakout candidate |
| P3 (breakout watch) | Ageless Balance | (not registered) | New (Part B) | 62 | ~$0.25 | Small but weekly-consistent, real business behind it |
| P3 (breakout watch) | Healthy Living After 60 | (not registered) | New (Part B) | 99 | ~$0.40 | Small subscriber base, large consistent catalog, underused sub-niche (medication interactions) |

**Group C subtotal if all 14 acquired: 2,131 videos, ≈ $8.52** — well above the last-known remaining campaign budget (~$3.66; see Phase 9 note). A full-group run is not proposed; this is a ranked menu for partial authorization.

## Group D — Adjacent reference channels (acquire selectively, not full-catalog by default)

| Channel | Canonical ID | Source | Why adjacent, not direct | Suggested scope if acquired |
|---|---|---|---|---|
| Living Our Best With Memory Loss | `UC-utlT1CFaucWho9VNvafOw` | New (Part B) | Caregiver/patient-voice podcast format, not the tips format the rest of the cohort uses | Sample only (10-15 videos), not full 80-video catalog — for sub-niche contrast, not cohort expansion |
| Her Health 60+ | `UC_2ODzPSUYDfGA_wdUSnCOA` | New (Part B) | Appearance/cosmetic leaning, unverified "doctor"/"surgeon" title claims, templated clickbait pattern resembling the already-documented content-mill network | Not recommended for acquisition — reference by public metadata only (title/thumbnail observation), no paid run |
| Dr. Waterling | `UCLVvBoFiBC6oj7mT62GFAEA` | Recovered (Part A seed) | Live-resampled 2026-09-25: catalog skews general clickbait health, not consistently senior-framed despite original "Yes" fit rating | Not recommended for acquisition until/unless a fuller title sample changes this assessment |
| ElderfitTV, Body Fix Exercises, Richard Kelley M.D., Dr. Misha Kogan, Dr. Dani Fisher, Dr. Holloway After 60, Healthy Aging - Senior Health Tips, Dr. James Senior Health Tips | (various, all recovered, unregistered) | Recovered (Tier B adjacent) | Broader age range or smaller/less-recent catalogs; listed in `COMPETITOR-DISCOVERY-REGISTER.md` §A2 | Not prioritized; revisit only if Group C results show a gap these would fill |

## Group E — Removed, duplicate, irrelevant, or unverifiable channels (excluded from paid runs, evidence preserved)

| Channel | Canonical ID | Reason |
|---|---|---|
| Dr. Adewale | `UC5qNIOYcXj-uIh6n5dWfLLg` | Removed by YouTube (Community Guidelines) — confirmed unchanged since 2026-09-22 |
| The Health Educator | `UC8ycZesiOH1DSgZl_qjruvg` | Removed by YouTube (Community Guidelines) — confirmed unchanged since 2026-09-22 |
| The Senior Health Podcast | `UCeY8vK104Gbzp4aqnTz4gzQ` | **Newly terminated** by YouTube since 2026-09-22 — was the largest-catalog original seed (385 videos est.), now unacquirable |
| Senior Health Protect | `UC1kEG25q-JE69jVw5ITXCrA` | **Newly terminated** by YouTube since 2026-09-22 (was content-empty, now fully terminated) |
| Ageless Science | `UCEKEI-mj_sFPB6uU_SPPLNg` | Confirmed empty shell (0 content), unchanged |
| "Dr. [First Name] Senior Health" persona-clone cluster (7 channels named in `COMPETITOR-DISCOVERY-REGISTER.md`) | various | Match the already-documented AI-avatar/content-mill naming pattern (`forensic-v2/DUPLICATE-NETWORK.json`) — excluded per Core Rule 9, not independent evidence |
| SENIOR NUTRITION, Smart Senior Nutrition, Senior Health Blog | various | Terminated by YouTube |
| 4 dead/renamed handles, 2 zero-content channels, 2 inactive/dormant channels (Falling Solutions for Seniors, Vitality After 60) | various | Full list and individual reasons in `COMPETITOR-DISCOVERY-REGISTER.md` Part B exclusions table |

---

## Phase 9 note (not performed here — requires live account access and, beyond the free-tier headroom, spending authorization)

This backlog is deliberately stopped short of Phase 9 (live Apify balance/pricing preflight) and Phase 10 (actual acquisition). Both require:
1. A live, current check of the Apify account's authenticated identity, current Actor build, current price, and current remaining credit — the last verified figures (2026-09-22/23: `$4.00/1,000 videos`, ~$3.66 of a $4.50 approved cap remaining after the Senior Health Hub run) are now 3 days old and explicitly flagged in that checkpoint as needing re-verification, not re-used blindly.
2. A decision on how much of Group C to actually acquire — even the cheapest useful subset (the 4 P1 candidates, 813 videos, ≈ $3.25) is close to the entire last-known remaining balance, and the full Group C list (≈ $8.52) exceeds it.

Per the master brief's own Phase 9 instruction: if authorization or account state cannot be verified, complete all zero-spend work and stop before initiating paid runs — which is exactly this stopping point.
