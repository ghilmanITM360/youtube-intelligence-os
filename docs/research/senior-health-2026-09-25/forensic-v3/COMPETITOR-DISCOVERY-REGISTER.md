# Senior Health Competitor Discovery Register — 2026-09-25

Status: FINAL for this pass. Local, untracked file — not committed per instructions. Repository was
treated as read-only; nothing in `data/`, `docs/audits/`, or the canonical DBs was modified.

## 0. Provenance correction on the Part A brief

The task brief assumed `data/extracted/channel-data/DS-000028/combined/youtube_1_channels_master.json`
and `data/raw/competitors/DS-000028/apify/*/raw/dataset.json` contained a broader discovery/candidate
list. Verified directly: both files contain **only Dr. Okoro's own 66-video catalog** (single
`channelId=UCMJxAeBJ0d1JC937de1eZ0Q` throughout every record). They are per-channel acquisition
data, not a discovery list.

The actual prior discovery work lives on the unmerged branch `origin/research/senior-health-forensic-v2`,
in two repo-root files that don't exist on this checked-out branch:

- `SENIOR-HEALTH-ACQUISITION-AND-REPO-SYNC-REPORT-2026-09-22.md` — the 8 original seed channels.
- `SENIOR-HEALTH-CHANNEL-DISCOVERY-2026-09-22.md` — 24 additional discovered candidates with
  tiered qualification; this is the source of the "five direct competitors qualified" claim
  named in the task brief. That claim is accurate to the source document (quoted verbatim in
  §2 below) — no named leads ("Dr. Brooks", "Dr. Nora Khalil", etc.) were invented or lost; all
  24 are accounted for.

Also read for context (same branch): `docs/research/senior-health-2026-09-25/forensic-v2/*`, a
much later, deeper forensic pass over the 6 channels that *were* acquired. It independently
references a large (~130-name) network of "Dr. [First Name] Senior Health"-style channels as
external benchmarks and a documented AI-avatar/content-mill duplicate network
(`DUPLICATE-NETWORK.json`). Those names are treated here as **already known to the project** and
excluded from "newly discovered" in Part B, per the task's anti-duplication instruction.

---

## Part A — Recovered from prior research

### A1. Original eight seed channels

Source: `SENIOR-HEALTH-ACQUISITION-AND-REPO-SYNC-REPORT-2026-09-22.md` (2026-09-22), cross-checked
against `data/catalog/youtube_channel_registry.db` (`channels` table) and re-verified live on
2026-09-25.

| Channel (as named in source) | Canonical Channel ID | Verified current name / handle / URL | Registry status (2026-09-25) | Qualification decision recovered (reasoning/evidence) |
|---|---|---|---|---|
| Dr. Okoro | `UCMJxAeBJ0d1JC937de1eZ0Q` | Dr. Okoro / @drmarcusokoro / youtube.com/channel/UCMJxAeBJ0d1JC937de1eZ0Q | **In registry**, `STANDARD_PACKAGE`, `COMPLETE` (DS-000028, 66 videos, 66 transcripts) | Acquired. Was screenshot-only (DS-000005) before; full Apify catalog run completed 2026-09-22/23, $0.264. |
| Dr. Adewale | `UC5qNIOYcXj-uIh6n5dWfLLg` | — | **Not in registry** (historical identity only) | **Do not acquire.** Confirmed live 2026-09-25: "This channel was removed because it violated our Community Guidelines." Same status as recorded on 2026-09-22 — no change. |
| Dr. Aliza Wright \| Advice | `UCXZi5JVeuTluazF-fYqQgNA` | Dr. Aliza Wright \| Advice / @Dr.AlizaWrightAdvice | **In registry**, `HISTORICAL_CATALOG`, `COMPLETE` (DS-000006, 32 videos, 32 transcripts) | Existing complete snapshot at time of discovery; no redundant paid run authorized or needed. |
| Doctor Thomas | `UCFuGMi0idGeyXl6wYK9hg7Q` | Doctor Thomas / @DrThomasSeniorHealthTips | **In registry**, `STANDARD_PACKAGE`, `COMPLETE_WITH_LIMITATIONS` (DS-000029, 22 videos, 21 real transcripts + 1 explicit gap) | Acquired 2026-09-23, $0.088. |
| The Health Educator | `UC8ycZesiOH1DSgZl_qjruvg` | — | **Not in registry** (historical identity only) | **Do not acquire.** Confirmed live 2026-09-25: "This channel was removed because it violated our Community Guidelines." No change since 2026-09-22. |
| Senior Health Hub | `UCAYG0fzUyxv6OevH88qA45w` | Senior Health Hub / @Health.Hub.Senior | **In registry**, `HISTORICAL_CATALOG`, `COMPLETE_WITH_LIMITATIONS` (DS-000030, 122 videos, 122 transcripts) | Acquired 2026-09-24, $0.488. |
| The Senior Health Podcast | `UCeY8vK104Gbzp4aqnTz4gzQ` | — | **Not in registry**; was an active, unacquired lead as of 2026-09-22 (@theseniorhealthpodcast, 385 Videos-tab results estimated) | **STATUS CHANGE — live-verified 2026-09-25 twice (clean, consistent result both times): the account is now "terminated for violating YouTube or Google's Terms of Service."** This channel was fully active 3 days ago and had the single largest catalog of all identified leads (385 videos). It is no longer acquirable. |
| Dr. Waterling | `UCLVvBoFiBC6oj7mT62GFAEA` | Dr. Waterling / @Mr.Greendude | **Not in registry**; unacquired lead | Still active, live-verified 2026-09-25: 329K subscribers, 71 videos. **Observation:** despite the "Yes" senior-health fit recorded on 2026-09-22, the live catalog sampled today skews general clickbait health content ("YOU'RE TAKING VITAMIN D WRONG", "NEVER REHEAT THIS — IT CAUSES PANCREATIC CANCER") rather than exclusively senior-framed; only a minority of visible titles say "After 60." Fit should be downgraded to adjacent/mixed pending fuller sampling, not treated as a clean direct match. |

**Requested: 8; active with data or live: 6; removed/terminated: 2 as of 2026-09-22, now 3 as of 2026-09-25** (The Senior Health Podcast newly terminated).

### A2. 24 additional discovery candidates

Source: `SENIOR-HEALTH-CHANNEL-DISCOVERY-2026-09-22.md`. Original document quote on the "five direct
competitors" claim: *"Tier A is **five** verified direct competitors, 424 displayed Videos-tab
results... Tier A, direct: Better Health While Aging; Senior Wellness; Dr. Brooks; Senior Health
Today; Dr. Nora Khalil."* Two more were held at Tier B pending fuller catalog sampling: Dr. Franklin
Senior Health and Senior Vital Health. None of the 24 were ever acquired (Apify was unavailable at
the time); none matched the canonical registry by ID then, and none match it now.

| Channel | Canonical Channel ID | Registry status (2026-09-25) | Original tier / reasoning | Live status 2026-09-25 |
|---|---|---|---|---|
| Better Health While Aging | `UCFpxvukIqCAUA7YizI-q9Dw` | Not in registry | **Tier A, direct.** Geriatrician-led (Dr. Leslie Kernisan, MD MPH — independently verifiable; runs betterhealthwhileaging.net), broad clinical topics, 7/10 recent titles explicitly older-adult, uploaded 3 days before observation. | **Confirmed active.** 190K subs, 98 videos — unchanged. Most recent video 6 days old at check time. Credential is real and verifiable, not just claimed — the strongest identity-verification case in the whole candidate set. |
| Senior Wellness | `UCslmaJaMSw8F8BId4CxByJw` | Not in registry | **Tier A, direct.** 10/10 recent titles explicit older-adult, senior exercise/mobility concentration, uploaded 3 days before observation. | **Confirmed active**, grew slightly: 276K subs / 99 videos (was 275K/98). |
| Dr. Brooks \| Senior Health | `UClzqmRzoC-7r8GiB_XQUn_A` | Not in registry | **Tier A, direct.** 9/10 explicit older-adult titles, broad senior-health topics; "Dr." credential explicitly flagged in the source doc as unverified for medical-claim purposes ("High for niche, not medical claims"). | **Confirmed active**, unchanged: 29.9K subs / 107 videos. "Dr." title remains an on-channel claim only — no license/credential evidence found in either pass. |
| Senior Health Today | `UCLxLjL1XVaKqZg-wZ2EBspA` | Not in registry | **Tier A, direct.** 10/10 explicit older-adult titles, focused over-60 mobility/strength catalog, uploaded 4 days before observation. | **Confirmed active**, +1 video: 24.4K subs / 57 videos (was 56). Uploads as recent as 1 day before this check. |
| Dr. Nora Khalil | `UCX_cW2SeHF1iBxbjx41vfrA` | Not in registry | **Tier A, direct, lower priority.** 6/10 explicit older-adult titles, mixed general/senior health, moderate confidence. | **Confirmed active**, unchanged: 39.7K subs / 65 videos. "Dr." title again unverified — no credential evidence found. |
| Dr. Franklin Senior Health | `UCPjG4ZRBkiO1y_vHlnj8jIg` | Not in registry | **Tier B, direct but needs more sampling.** 5/10 explicit older-adult titles, smaller/less-recent catalog at observation (uploaded ~2 months prior). | **Confirmed active**, unchanged: 119K subs / 37 videos. Catalog size did not grow in 3 days — consistent with the "less recent" characterization. |
| Senior Vital Health | `UCUUKjcYdqOHk2j-pbUnWDNw` | Not in registry | **Tier B, direct but needs more sampling.** Only 2/10 latest titles identify older adults despite a large catalog — moderate confidence for niche fit. | **Confirmed active**, unchanged: 104K subs / 195 videos. |
| Healthy Aging with Dr. Doctor | `UCZyMQ8q7rq83_705upHZyTA` | Not in registry | Tier B, adjacent. Dermatology/holistic aging, broader than senior health specifically. | Not re-verified live (adjacent, not prioritized). |
| Dr. Holloway After 60 | `UC5pKio2JgSLI2vkBzny6nEg` | Not in registry | Tier B, adjacent/smaller direct. Small (54 subs) but relevant 49-video catalog. | Not re-verified live. |
| Healthy Aging - Senior Health Tips | `UCk6fYu-O4DR1x2taFkAu_BA` | Not in registry | Tier B, adjacent/smaller direct. Small, apparently inactive (5 videos). | Not re-verified live. |
| Dr. James Senior Health Tips | `UCP8RIWduYwo86eX_bbOrK4w` | Not in registry | Tier B, adjacent/smaller direct. Relevant but limited (16 videos), older catalog. | Not re-verified live. |
| Wisdom After 60 | `UC5MkHMM9vnjSb0MFp4AmKgQ` | Not in registry | Tier C, mixed/sparse. Mixed lifestyle/health, only 6 videos. | Not re-verified live. |
| ElderfitTV | `UCTDTzy68kOwNdyJVLgDf8Og` | Not in registry | Tier B, adjacent/smaller direct. Senior fitness adjacent, distinct mobility/balance evidence, 326K subs / 190 videos. | Not re-verified live (large, likely stable). |
| Body Fix Exercises | `UC9QgDBvyfbflM9zCBqp2GNA` | Not in registry | Tier B, adjacent/smaller direct. Over-50 fitness adjacent, strong catalog but broad age range (727K subs / 229 videos). | Not re-verified live. |
| Senior Book | `UCVrDYU1DiPbgrUVuBPrXrnw` | Not in registry | Tier C, mixed/sparse. Mixed lifestyle, health is only a podcast segment. | Not re-verified live. |
| Healthy Aging | `UCfC4q2PEmYGaem9_w4HqkcQ` | Not in registry | Tier B, adjacent/smaller direct. Small (235 subs), active; verify claims before use. | Not re-verified live. |
| Dr. Dani Fisher | `UCK5aB2dkLd7Nijh9cTdGNEw` | Not in registry | Tier B, adjacent/smaller direct. Medical-expert-adjacent, current aging/medical topics. | Not re-verified live. |
| Life After 60+ | `UCWMQjQav8YSbAq17YVrqjKg` | Not in registry | Tier C, mixed/sparse. Mixed lifestyle/health, health share needs sampling. | Not re-verified live. |
| Health Science Daily | `UC_l_kwmbc2aAYB6HoBFQ8Jw` | Not in registry | Tier C, mixed/sparse. Mixed health, limited catalog, attribution concern. | Not re-verified live. |
| Healthy After 60 | `UCHKL5CjA8WbYb1M-FsECINA` | Not in registry | Tier B, adjacent/smaller direct. Small niche-specific catalog (9 subs / 31 videos). | Not re-verified live. |
| Dr. Misha Kogan | `UCOftxdr17X7h_7OicYB5chw` | Not in registry | Tier B, adjacent/smaller direct. Integrative-medicine/healthy-aging adjacent, distinct perspective. | Not re-verified live. |
| Richard Kelley M.D. | `UCjPqI2_Ym14ufiF5rFvTt_w` | Not in registry | Tier B, adjacent/smaller direct. Over-50 medical/fitness adjacent, doctor-led creatine/fitness/longevity content. | Not re-verified live. |
| Senior Health Protect | `UC1kEG25q-JE69jVw5ITXCrA` | Not in registry | **Rejected for acquisition** at discovery: identity existed (400K subs) but zero visible public videos. | **STATUS CHANGE — confirmed live 2026-09-25: fully terminated** ("This account has been terminated for violating YouTube or Google's Terms of Service"), not merely content-empty as recorded 3 days ago. |
| Ageless Science | `UCEKEI-mj_sFPB6uU_SPPLNg` | Not in registry | **Rejected for acquisition** at discovery: identity existed (47 subs) but zero visible public videos. | Confirmed live 2026-09-25, unchanged: channel exists, "This channel doesn't have any content." |

Identity verified at original discovery: 24. Direct channels with visible content: 12 (5 Tier A +
7 Tier B-direct-or-adjacent named "direct" in the source). Adjacent/mixed with content: 10. No-content
rejects: 2 (one of which is now fully terminated, confirmed above).

### A3. Recovery summary against the task's named leads

All seven leads named in the task brief were located in `SENIOR-HEALTH-CHANNEL-DISCOVERY-2026-09-22.md`:
Dr. Brooks, Dr. Nora Khalil, Dr. Franklin Senior Health, Senior Health Today, Senior Wellness, Better
Health While Aging, Senior Vital Health. None were previously acquired; none are in the canonical
registry by ID. The "five direct competitors" claim is accurate and fully reconstructed above (§A2).

---

## Part B — Newly discovered candidates

Live YouTube/web research conducted 2026-09-25, independent of and excluding every channel named in
Part A (32 identities: 8 seeds + 24 discovery candidates) and the ~130-name persona-clone/external-benchmark
network already referenced in `docs/research/senior-health-2026-09-25/forensic-v2/EXTERNAL-BENCHMARKS.json`
and `DUPLICATE-NETWORK.json` on the research branch. Every candidate below was opened directly (About +
Videos tab), not judged from search snippets.

| Canonical Channel ID | Verified current name | Current handle | Canonical URL | Senior Health relevance | Sub-niche | Channel positioning | Public catalog summary | Observed upload activity | Existing repository match | Available internal data | Data gap | Acquisition decision | Acquisition priority | Reason | Identity verification source | Verification date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — (not in registry) | Healthy Aging Hub | @HealthyAgingHubb | youtube.com/@HealthyAgingHubb | High — explicit "Over 60"/"Over 50" longevity/vitality framing | General senior health/longevity | Faceless branded channel, no named host, high-cadence | 51.3K subscribers, 516 videos | Very active — new video roughly every 2 days | None | None | Full: no descriptions/transcripts/thumbnails acquired | Candidate for standard observation | High | Large, active, genuinely senior-targeted catalog; good high-cadence benchmark | YouTube About/Videos tab, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | More Life Health Seniors | @MoreLifeHealth | youtube.com/c/MoreLifeHealth | High — content explicitly "For Seniors & Over 60s" | Senior fitness/mobility | Branded platform founded by Mike Kutcher, physiotherapist (per morelifehealth.com, corroborates on-channel claim) | 272K subscribers, 162 videos | Active — recent videos 3 weeks–2 months old | None | None | Full | Candidate for standard observation | High | Large, credentialed founder independently verifiable outside YouTube, consistent senior-specific catalog | YouTube About/Videos tab + morelifehealth.com, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | Senior Fitness With Meredith | @SeniorFitnessWithMeredith | youtube.com/channel/UC2BaKQ5vqal9yaC-VbpD5ZQ | High — seated/standing workouts explicitly for seniors and beginners | Senior fitness | Named instructor Meredith Chen; has own podcast and site, 6+ years on platform | 150K subscribers, 454 videos | Very active — videos 11 days and 2 weeks old at check | None | None | Full | Candidate for standard observation | High | Large, highly active, long operating history, real named instructor | YouTube About/Videos tab, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | The Senior Centered PT | @TheSeniorCenteredPT | youtube.com/c/theseniorcenteredpt | High — bone health, balance, diabetic exercise, senior-specific Pilates | Geriatric physical therapy | Hosted by Dr. Katie Landier, PT, DPT — Board Certified Clinical Specialist in Geriatric PT (verifiable credential) | 28.6K subscribers, 66 videos | **Slowing** — most recent (a livestream) ~7 months old; bulk of catalog ~2 years old | None | None | Full | Candidate, but monitor cadence before committing budget | Medium | Verified real, credentialed geriatric-PT specialist — the strongest doctor-led/clinician credibility case in Part B — but upload activity has dropped off | YouTube About/Videos tab, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | Senior Meal Coach | @SeniorMealCoachUS | youtube.com/channel/UCHOrUqhgZmEwhmXqvLwghpg | High — sarcopenia, kidney/blood-pressure diet content explicitly "After 60" | Senior nutrition | Faceless branded channel; **caution:** several videos are co-credited to sibling channels "Senior Motion" and "Senior Food & Health," indicating a cross-branded content network | 68.6K subscribers, 94 videos | Active but slowing — most recent video ~2 months old | None | None | Full | Candidate; flag cross-branding before treating as fully independent evidence source | Medium | Sizeable senior-nutrition-specific catalog, but no identifiable dietitian/nutritionist and clear shared-content-network risk | YouTube About/Videos tab, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | Senior Mobility Care | @SeniorMobilityCare | youtube.com/channel/UCj-4CkWt2waFCjt5h7fZSiA | High — muscle loss after 70, "Over 60" exercise framing throughout | Senior mobility/strength | Faceless branded channel, no named host or doctor claim | 5.07K subscribers, 15 videos | Active — videos 4 and 6 months old | None | None | Full | Candidate — small-channel breakout watch | Medium | Small, genuinely senior-focused, thin catalog so far; useful as a breakout-research small channel | YouTube About/Videos tab, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | Ageless Balance \| Balance & Fall Prevention | @agelessbalance | youtube.com/@agelessbalance | High — full-length "55+"/"60+" seated/standing balance classes, explicit fall-prevention focus | Senior balance/fall prevention | Affiliated with qolfitness.com (Quality of Life Fitness); runs live Zoom classes for the same audience | 717 subscribers, 62 videos | Active — weekly cadence (several videos ~3 weeks old) | None | None | Full | Candidate — small-channel breakout watch | Medium | Small but consistently weekly and tightly on-niche, real studio/business behind it | YouTube About/Videos tab + qolfitness.com, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | Healthy Living After 60 | @TheHealthyLivingOfficial | youtube.com/@TheHealthyLivingOfficial | High — vitamin/medication-interaction and balance content specifically "After 60" | Senior nutrition/medication interactions | Faceless branded channel, no named host or doctor claim | 714 subscribers, 99 videos | Active — most recent video 9 days old, steady near-biweekly cadence for 9+ months | None | None | Full | Candidate — small-channel breakout watch | Medium | Small subscriber base but large, consistently-updated catalog on an underused sub-niche (medication interactions) | YouTube Videos tab, opened 2026-09-25 (independently re-verified twice) | 2026-09-25 |
| — (not in registry) | Living Our Best With Memory Loss | @LivingOurBestWithMemoryLoss | youtube.com/channel/UC-utlT1CFaucWho9VNvafOw | Medium-High — dementia/Alzheimer's patient & caregiver support; adjacent to core "senior health tips" format | Memory/cognitive health & caregiving | Podcast affiliated with nonprofit livingourbest.org; interviews named, checkable guests (clinicians and dementia-care experts) | 6.14K subscribers, 80 videos | Active — recent videos ~7-8 months old | None | None | Full | Candidate — reference/adjacent, not a tips-format direct competitor | Medium | Distinct sub-niche (lived-experience/caregiver-voice vs. typical tips format); real nonprofit affiliation, named guests | YouTube About/Videos tab + livingourbest.org, opened 2026-09-25 | 2026-09-25 |
| — (not in registry) | Her Health 60+ | @HerHealth60 | youtube.com/channel/UC_2ODzPSUYDfGA_wdUSnCOA | Medium — "After 60" framing but leans cosmetic/dermatological ("crepey skin," "double chin") over clinical health | Women's health/appearance after 60 | Faceless branded channel; "Doctor Explains"/"Surgeon Approved" language appears in titles but **no named physician anywhere in About or the videos checked — treat every "doctor"/"surgeon" claim as unverified** | 120K subscribers, 139 videos | Very active — near-daily uploads | None | None | Full | Adjacent reference, not a priority acquisition | Low | Large and fast-growing, but templated clickbait title formulas closely resemble the content-mill pattern already documented in this project's forensic-v2 pass; unverified credential claims | YouTube About/Videos tab, opened 2026-09-25 | 2026-09-25 |

**10 new candidates qualified** (7 High/Medium direct, 2 Medium adjacent/flagged, 1 Low adjacent-reference)
out of a substantially larger set inspected and rejected — see exclusions below. No unverified "Dr."-branded
channel is included as the channel's *own* host identity; where "doctor" language appears it is a title
trope and is called out as unverified in the Reason column, consistent with the task's instruction not to
assume a "Dr." prefix implies a real license.

### Excluded during Part B vetting (channels opened and rejected, with reason)

| Channel | Reason excluded |
|---|---|
| Dr. William Parker Senior Health, Doctor Christopher Carter \| Senior Health, Senior Doctor (@SeniorDoctorV), Senior Health (@SeniorHealthV), Dr. Emily Waterly \| Health After 60, Dr. Michael Kent \| Senior Health, Dr. Constantin | Match the "Dr. [First Name] Senior Health" persona-clone naming/format already documented in this project's forensic-v2 pass as an AI-avatar/content-mill network (`DUPLICATE-NETWORK.json`). Not re-discovered as independent evidence per the task's anti-duplication instruction. |
| Senior Health Care Explained (@SeniorHealthCareExplained) | Opened directly: only 3 videos. Catalog too thin to assess. |
| Senior Citizen Well-being Channel (custom URL) | Resolves to canonical channel ID `UCeY8vK104Gbzp4aqnTz4gzQ` — this is **The Senior Health Podcast**, an already-known Part A seed, now confirmed terminated (see §A1). Not a new candidate. |
| @SeniorShapeFitness | Handle now redirects to Dr. Waterling (@Mr.Greendude), an already-known Part A seed — apparent handle reuse/rebrand, not new. |
| Senior Wellness Podcast (@SeniorWellnessPodcast), Senior Life Nutrition (@seniorlifenutrition), @SeniorHealthCares | Handles return 404 — dead or renamed. |
| SENIOR NUTRITION, Smart Senior Nutrition, Senior Health Blog | All three opened directly: terminated by YouTube for Terms of Service violations. |
| Memory Health (@memoryhealthnutrition) | Channel exists but has zero uploads ("doesn't have any content"). |
| Falling Solutions for Seniors | Inactive; only two visible videos, both roughly 10 years old. |
| Vitality After 60 | Dormant (last upload ~8 months ago); ~68 video titles are near-identical repeating templates ("Eat THESE 3/4 Foods Before Bed to Repair Your Eyes/Vision While You Sleep"), matching the same templated content-mill pattern already flagged elsewhere in this project. Excluded on inactivity plus duplication-risk grounds. |
| Longevity Science News, Peter Attia, Huberman Lab-adjacent general-longevity channels | General health/longevity audience, not senior-specific (all ages); out of niche scope, not listed as candidates. |

---

## Direct vs. adjacent vs. excluded — consolidated view

**DIRECT competitors (senior-health-specific, catalog-verified):**
- Already acquired (Part A, complete data in registry): Dr. Okoro, Doctor Thomas, Senior Health Hub, Dr. Ares Senior, Dr. Elias Senior Health, Dr. Aliza Wright | Advice.
- Recovered leads, Tier A qualified, not yet acquired: Better Health While Aging, Senior Wellness, Dr. Brooks, Senior Health Today, Dr. Nora Khalil.
- Recovered leads, Tier B direct (needs fuller sampling): Dr. Franklin Senior Health, Senior Vital Health.
- Newly discovered, High/Medium priority: Healthy Aging Hub, More Life Health Seniors, Senior Fitness With Meredith, The Senior Centered PT, Senior Meal Coach, Senior Mobility Care, Ageless Balance, Healthy Living After 60.

**ADJACENT / reference channels (broader audience, different sub-niche emphasis, or credibility caveats):**
- Recovered: Healthy Aging with Dr. Doctor, ElderfitTV, Body Fix Exercises, Dr. Dani Fisher, Dr. Misha Kogan, Richard Kelley M.D., Dr. Holloway After 60, Healthy Aging - Senior Health Tips, Dr. James Senior Health Tips, Healthy Aging (@HealthyAging-r5z), Healthy After 60, Wisdom After 60, Senior Book, Life After 60+, Health Science Daily.
- Recovered seed: Dr. Waterling (general clickbait-health leaning despite "Yes" fit rating on file — see §A1).
- Newly discovered: Living Our Best With Memory Loss (caregiver/patient-voice, not tips format), Her Health 60+ (appearance-leaning, unverified "doctor" claims).

**EXCLUDED (with reason):**
- Dr. Adewale, The Health Educator — banned/removed by YouTube, confirmed unchanged on 2026-09-25.
- The Senior Health Podcast — **newly terminated** as of this check (was an active, high-catalog lead 3 days ago).
- Senior Health Protect — **newly terminated** as of this check (was content-empty but identity-present 3 days ago).
- Ageless Science — confirmed still an empty shell (0 content), unchanged.
- All Part B exclusions listed in the table above (persona clones, terminated channels, dead handles, thin/dormant catalogs).

---

## Summary of live-verification findings (2026-09-25 vs. 2026-09-22 discovery)

- All 5 Tier A and both Tier B direct candidates are confirmed still live and essentially unchanged
  (subscriber/video counts match within normal 3-day growth).
- **Two real status changes surfaced:** The Senior Health Podcast (an original seed, 385-video
  estimated catalog, previously listed active) and Senior Health Protect (a discovery candidate,
  previously "identity present, no visible content") have both been **terminated by YouTube**
  since the 2026-09-22 pass. Neither is acquirable now.
- Dr. Adewale and The Health Educator remain confirmed removed, no change.
- Ageless Science remains a confirmed empty shell, no change.
