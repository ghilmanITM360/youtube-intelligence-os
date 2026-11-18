# 05 — 30-day experimental calendar (v1, 2026-11-18)

**Status:** owner-approved inputs, as of 2026-11-18:
- scoring weights and top-25 (03 §6)
- remake rule: none from the last 12 months, at most one older
- cadence: 2 longs + 3 Shorts per week, week 1 front-loaded
- competitor CT pass (04)

**Calendar approved by the owner: 2026-11-18** (after the science pre-check in 06; open items closed the same day). Still pending: start date and channel CH-id.


**APPROVED by the owner, 2026-11-18.** Day 1 = **Monday 2026-11-23** (owner choice).

**Production-time risk (flagged, not blocking):** The calendar assumed about 10 production days for the first 3 longs (Days 1, 3, 5). This start leaves 5 days. If a long is not ready, the existing fallback applies (drop the Q control first, then the R long). Do not move week-1 longs later; they feed the Day 14 comparison.

### Dated schedule

| Day | Date | Slot |
|---|---|---|
| 1 | Mon 23 Nov 2026 | Long WIB-36 |
| 2 | Tue 24 Nov 2026 | Short WIB-36 |
| 3 | Wed 25 Nov 2026 | Long WIB-55 |
| 4 | Thu 26 Nov 2026 | Short WIB-55 |
| 5 | Fri 27 Nov 2026 | Long NEW-06 |
| 6 | Sat 28 Nov 2026 | Short T-01 |
| 8 | Mon 30 Nov 2026 | Long WIB-22 |
| 9 | Tue 01 Dec 2026 | Short NEW-06 |
| 10 | Wed 02 Dec 2026 | Short WIB-22 |
| 11 | Thu 03 Dec 2026 | Long NEW-08 |
| 13 | Sat 05 Dec 2026 | Short WIB-18 |
| 14 | Sun 06 Dec 2026 | Day 14 evaluation (§4) |
| 15 | Mon 07 Dec 2026 | Long WIB-17 |
| 16 | Tue 08 Dec 2026 | Short NEW-08 |
| 18 | Thu 10 Dec 2026 | Long WIB-11 |
| 19 | Fri 11 Dec 2026 | Short WIB-17 |
| 20 | Sat 12 Dec 2026 | Short WIB-53 |
| 22 | Mon 14 Dec 2026 | Long WIB-24 |
| 23 | Tue 15 Dec 2026 | Short WIB-11 |
| 25 | Thu 17 Dec 2026 | Long WIB-52 |
| 26 | Fri 18 Dec 2026 | Short WIB-24 |
| 27 | Sat 19 Dec 2026 | Short NEW-07 |
| 28 | Sun 20 Dec 2026 | Short WIB-52 |
| 29 | Mon 21 Dec 2026 | Long Chosen Day 14 |
| 30 | Tue 22 Dec 2026 | Day 30 evaluation (§5) |

**Not included:** scripts. Scripts are written only after the start date is set, and each one goes through `scripts/check_slop_risk.py` under `productions/`.

**Framework:** `calendar_plan_framework_2026-11-18.json` passes `content_plan_check.py` → `OK (structural only)`. The check covers shape and provenance; it says nothing about quality. `run_youtube_intelligence.py --framework-plan` was not run, because the new channel has no registered CH-id yet. Register the channel first, then run it.

**Day numbering:** Day 1 = first publish day = Monday 2026-11-23 (see the dated schedule above).

## 1. What the calendar is testing

**Primary question (HYPOTHESIS):** for a new What-If-style science channel, which **format family** earns the most Browse/Suggested-driven viewing per video? The candidates come from repeated outliers (03 §2) and the CT pass (04):
- L — every-X ladder
- S — scale/POV simulation
- T — timeline
- R — runaway

**Secondary questions:**
- Do Shorts excerpted from a long outperform standalone Shorts?
- Does thumbnail text with a number ("number/contrast") work for a new brand?

**Unit of comparison:** a format family, never a single video. n is tiny (L = 3, S = 2, T = 2, R = 1, Q = 1), so the results guide the *next 30 days*. They are not proof.

**Constants held across all videos**, so that families are comparable:
- original line-art visual identity
- one persistent progress tracker per episode (CT finding, 04 §3: present in all three scanned outliers)
- cold open on the most extreme rung or end state
- labelled evidence layers (e.g. "SIMULATION / REAL DATA / THE MATH") with on-screen primary-source citations (04 §2, Tracer)
- same voice
- 6–10 min target
- same publish hour
- end screen pointing to the next video of the same family

**IP boundary (01 §6):**
- no xkcd stick-figure look, characters, script lines or titles
- no third-party footage (the Fossil video is built from documentary and paleo-art clips; we do not do that)
- every number recomputed from primary sources

## 2. Calendar

Columns: Fmt = Long (L) / Short (S); Fam = format family; Score = 03 §6.

| Day | Fmt | Bank ID | Working title (HYPOTHESIS) | Fam | Score | Thumbnail concept (original) | Experiment role |
|---|---|---|---|---|---|---|---|
| 1 | Long | WIB-36 | What If You Fell From Every Height — 1 Metre to the Edge of Space? (06: "orbit" reframed) | L | 89 | Falling figure beside an altitude ruler; one label "39 km: fastest fall ever" | L #1 |
| 2 | Short | WIB-36 | Excerpt: why jumping from higher makes you slow down before landing (06 reframe) | L | — | Same art, cropped | Excerpt test |
| 3 | Long | WIB-55 | What If a Bullet Were Made of Neutron Star? | S | 90 | Level balance: glowing 0.7 cm³ pellet vs a 412 m rock cube; "AT LEAST 190 MILLION TONNES" (06; changed at scripting to show the bullet itself) | S #1 |
| 4 | Short | WIB-55 | Excerpt: if something held it together and you dropped it (assumption stated, SIMULATION label; 06) | S | — | — | Excerpt test |
| 5 | Long | NEW-06 | What If the Moon Vanished Tonight? Night One to a Million Years (06: "hour by hour" overpromised) | T | 73 | Night sky with an empty dashed circle; "HOUR 1" | T #1 |
| 6 | Short | T-01 | What Will Apophis Look Like on 13 April 2029? (owner choice 2026-11-18: "What will" only for real future events) | T | (unscored, timely) | Earth, Moon and asteroid path to scale; "13 APR 2029 · 31,640 km" (06, JPL) | Standalone test |
| 8 | Long | WIB-22 | What Could Aliens See of Earth From 10, 100 and 10,000 Light-Years? | L | 90 | Split panel: "10 LY" vs "10,000 LY" | L #2 |
| 9 | Short | NEW-06 | Excerpt: the tides on night one | T | — | — | Excerpt test |
| 10 | Short | WIB-22 | Excerpt: what aliens see of us *right now* | L | — | — | Excerpt test |
| 11 | Long | NEW-08 | What If Light Were as Slow as a Car? | R | 89 | Road scene with a speed readout "100 km/h = c"; a distinct angle from WhatIfAnimations' "kept getting slower" | R #1 |
| 13 | Short | WIB-18 | How High Would You Drop a Steak to Cook It? | L | 80 | Steak with heat streaks; "100 km: a seared crust, seconds long" (06: answer is that no height cooks it) | Standalone test |
| **14** | — | — | **Day 14 evaluation (§4)**: picks the Day 29 slot | — | — | — | — |
| 15 | Long | WIB-17 | What If You Lived on a Planet So Small You Could Orbit It by Jumping? | S | 88 | Figure leaping around a tiny sphere; "ORBIT: 1 JUMP" | S #2 |
| 16 | Short | NEW-08 | Excerpt: why your headlights still outrun you (06: "traffic jam of light" was a false premise) | R | — | — | Excerpt test |
| 18 | Long | WIB-11 | When All Humans Are Gone, Which Light Goes Out Last? | T | 83 | Dark Earth with a few lights, each labelled with a time range | T #2; **the single allowed remake** (xkcd long 2024-05-28, >12 months). New angle: ranked timeline of light sources (ranges, power plants qualitative only), different title |
| 19 | Short | WIB-17 | Excerpt: why you can't walk normally there | S | — | — | Excerpt test |
| 20 | Short | WIB-53 | What If a Whole Storm Fell as One Raindrop? | Q | 65 | Single huge drop over a town | Standalone test |
| 22 | Long | WIB-24 | What If You Flew a Small Plane on Every Planet? | L | 83 | Small plane silhouettes over 4 planet strips; "MARS: 530 km/h JUST TO STAY UP" (06: corrected from "0 LIFT?") | L #3 |
| 23 | Short | WIB-11 | Excerpt: the light that lasts longest | T | — | — | Excerpt test |
| 25 | Long | WIB-52 | Who Was the Loneliest Human Ever? | Q | 83 | One figure at a distance marker; "3,596 km" (06: Guinness) | Q control: classic one-off calculation |
| 26 | Short | WIB-24 | Excerpt: flying on Titan | L | — | — | Excerpt test |
| 27 | Short | NEW-07 | What Would Falling Into Jupiter Feel Like? (60 s) | S | 86 | — | Standalone test (long-form supply crowded) |
| 28 | Short | WIB-52 | Excerpt: farthest from Earth ≠ loneliest (06: Artemis II contrast) | Q | — | — | Excerpt test |
| 29 | Long | Chosen Day 14 | Next-ranked unused topic from the leading family. Defaults: L → WIB-15 Lightning in every location (82); S → NEW-10 Hollow Earth (82); T → WIB-04 Time machine on one spot (69); R → NEW-05 Gravity doubles (75) | winner | — | — | Exploitation slot (Playbook P01: repeat what worked) |
| **30** | — | — | **Day 30 evaluation (§5)** | — | — | — | — |

**Totals:**
- 10 longs: L 3, S 2, T 2, R 1, Q 1, plus 1 winner slot.
- 13 Shorts: 9 excerpts (Days 2, 4, 9, 10, 16, 19, 23, 26, 28) and 4 standalone (Day 6 T-01, Day 13 WIB-18, Day 20 WIB-53, Day 27 NEW-07).

**Cadence:** week 1 has 3 longs; then 2 per week. Shorts come about 3 per week.

**Why this order:** the first two weeks give each of L, S and T at least one long, published before Day 14 (L: Days 1 and 8; S: Day 3; T: Day 5; R: Day 11). Day 14 therefore compares all four families with at least 3 days of data each.

**Fallback if production slips:** drop the Q control (Day 25) first, then the R long. Never drop the second L/S/T video: those pairs are the test.

## 3. Per-video pre-production gates (before any script)

1. **Science verification table (brief requirement).** For every quantitative claim, record: claim, primary source (NASA/JPL, peer-reviewed paper, standard handbook), computed value, uncertainty. Pre-script pass done 2026-11-18 in `06_SCIENCE_VERIFICATION.md`: all 23 items checked; the former OPEN items (Days 18/23/27) are closed (see 06), with Day 18 power-plant rungs qualitative only. The per-claim table is still needed per script. Starting points:

   | Video | Sources to start from |
   |---|---|
   | WIB-36 | Red Bull Stratos (2012) and the 2014 Eustace record documentation; terminal-velocity physics by altitude from the US Standard Atmosphere |
   | WIB-55 | Neutron-star density ranges from review literature (e.g. Lattimer & Prakash); the thumbnail figure must be recomputed |
   | NEW-06 | Tidal contributions of the Moon vs the Sun (NOAA tides primer); axial-stability literature, presented as uncertain (Laskar et al. vs later work) |
   | WIB-22 | Detectability of radio leakage, atmospheric biosignatures and city lights vs distance (peer-reviewed SETI and exoplanet-transit papers) |
   | NEW-08 | Relativity at low *c*: present as a thought experiment with explicitly stated simplifications |
   | WIB-17 | Escape and orbital velocity vs radius and density (standard mechanics) |
   | WIB-11 | Lifetimes of light sources (radioisotope sources, solar-powered lights, Voyager-type RTGs); dates as ranges |
   | WIB-24 | Atmospheric density and gravity per planet (NASA planetary fact sheets); lift equation |
   | WIB-52 | Apollo command-module pilots' farthest distances from other humans (NASA mission reports) |
   | T-01 | JPL Small-Body Database / CNEOS for the 2029 Apophis close approach. **Impact ruled out**; state the miss distance from JPL |
2. **Collision check:** confirm no xkcd upload on the topic since 2026-11-18, and that title and thumbnail differ from every competitor title listed in 03 and 04.
3. **AI-slop gate:** each script is saved as `productions/<project>/**/*SCRIPT*.md` and must pass `scripts/check_slop_risk.py`. You see the verdict, the findings and the C1–C5 checklist.
4. **Packaging check (FR-TITLE-03):** no overpromise; the title question is answered on screen at a known timestamp.

## 4. Day 14 evaluation procedure

**Inputs (first-party only; never competitor numbers):**
- YouTube Studio exports for every video published Days 1–13:
  - Content/Video performance: views, watch time, average view duration, average % viewed
  - Reach: impressions, impression CTR
  - Traffic sources: Browse, Suggested, Search, Shorts feed, Channel pages, External
  - Audience: new vs returning viewers, subscribers gained
- Ingest with `scripts/ingest_youtube_analytics.py`. Raw exports go to `data/raw/inbox/first-party-analytics/`; normalised output goes to `data/intelligence/first-party/`.
- Record each video's age at export. Compare at **equal ages**: use the 72-hour value for every long; if Studio cannot give it, use the value at the youngest common age.

**Steps:**
1. **Data check:** every published video is present, and no export covers a partial day.
2. **Per long, compute:**
   - views at a common age
   - Browse + Suggested share of views
   - average % viewed
   - impression CTR
   - subscribers per 1,000 views

   These are *diagnostics*. KB-ALG REC-001: no thresholds, no ranking guarantees.
3. **Per family:** take the median of each metric. Rank families on views at a common age, with Browse+Suggested share as the tie-breaker.
4. **Decision rule for Day 29 (owner can override):**
   - The family ranked first on views at a common age gets the Day 29 slot.
   - If the top two families are within 20% of each other, choose the one with the higher average % viewed. Reason: with n = 1–2, a viewing-quality signal is less noisy than raw views.
5. **Shorts:** compare the median views of excerpt Shorts vs standalone Shorts, and record each excerpt Short's "related video" click-through to its long where Studio shows it. No conclusion if n < 3 per group.
6. **Packaging:** if any long has 2+ days with impressions but CTR below the channel's own median, test an alternative thumbnail. Use Test & Compare where the video is eligible: per R8 it decides by watch-time share and excludes Shorts. Otherwise do a manual swap, logged with its date.
7. **Write-up** (`06_DAY14_EVALUATION.md`): results table, decision, and what would change it. Label everything FACT (Studio numbers) or INTERPRETATION.

**What Day 14 must not conclude:**
- that a family "doesn't work" from a single video
- that the algorithm "punished" anything
- anything that compares our numbers with competitors' numbers

## 5. Day 30 evaluation procedure

**Inputs:** the same exports for Days 1–29, plus a 7-day value for every long published by Day 23.

**Steps:**
1. **Family table:** for each family, median views at 7 days, Browse+Suggested share, average % viewed, subscribers per 1,000 views, and returning-viewer share.
2. **Own-baseline outliers** (the same method used on competitors in 03): PI = views at 7 days ÷ the channel median at 7 days. Flag any long with PI ≥ 2 as an internal outlier. Then apply Playbook P01: plan 2–3 follow-ups on its topic or format next month.
3. **Shorts verdict:** keep excerpt Shorts if they match or beat standalone ones on median views. Otherwise switch the ratio for month 2. Also report whether Shorts viewers turned into long-form viewers: subscribers from Shorts, plus the related-video clicks from step 5 of Day 14.
4. **Cadence check:** actual production hours per long vs the 2/week plan. If quality gates (verification, slop gate) were squeezed, reduce to 1.5 per week rather than lowering the gates (CLM-009 / P04: repetitive mass production is a policy risk).
5. **Topic-bank refresh:** re-run the Method-4 scan and the 30-day search scan (02) for the next 20 ranked topics, and re-score with the same script, replacing F/V/P with any learned evidence.
6. **Decision memo** (`07_DAY30_EVALUATION_AND_MONTH2_PLAN.md`): the family mix for month 2 (e.g. 60% leading family, 30% second, 10% exploration), the cadence, and the packaging rules kept or dropped. It is a new content plan, so it must pass the framework gate again.

**Stopping or escalation signals:**
- Any video flagged for policy or copyright: stop and review the whole pipeline before the next upload.
- All families below 50% of the channel's own median by Day 30: **this means data is insufficient, not that the channel failed**. Extend the test by 30 days rather than pivoting the niche (FRAMEWORK RM-1f228411d7ab:chunk.60: topic consistency).

## 6. Assumptions and open risks

- **Competitor data:** competitor results come from a personalised (PK, signed-in) browser and only show survivors. Our expected views are unknown.
- **Remake:** WIB-11 is the only remake, and it still carries reputational collision risk. If xkcd re-covers the topic before Day 18, swap in WIB-15.
- **Apophis Short (T-01):** it peaks with news; if no 2029-related news arrives, treat its result as a weak test.
- **Q control:** one video cannot tell us whether xkcd-style one-off calculations work without the brand. It is a sanity check only.
