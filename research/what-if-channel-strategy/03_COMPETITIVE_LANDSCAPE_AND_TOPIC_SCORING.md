# 03 — Competitive landscape, what xkcd is making, and explicit topic scoring

Observed 2026-11-18 via Claude in Chrome (owner-approved). Builds on 01 (catalog/bank audit) and 02 (30-day scan).
Labels: **FACT** = observed public number · **DERIVED** = computed from observed data · **INTERPRETATION** = analyst reading · **HYPOTHESIS** = to be tested.

## 0. Sources and knowledge used

| ID | What | File | Notes |
|---|---|---|---|
| SRC-XK2 | xkcd channel /videos + /shorts, today | `data/xkcd_channel_snapshot_2026-11-18.tsv` | 30 longs, 46 Shorts, 1.38M subs |
| SRC-DISC | 80 YouTube searches (40 format queries × {this month, all time}) | aggregated in SRC-M1 header | 3,285 results (1,282 long / 2,003 Shorts), 357 channels |
| SRC-M1 | 48-channel census, own-baseline outlier ratio (PI) | `data/channel_census_m1_2026-11-18.tsv` | Playbook Method 1 |
| SRC-M4 | All-time search per topic, 75 topics | `data/m4_demand_supply_scan_2026-11-18.tsv` | Playbook Method 4 |
| SRC-PKG | Visual review of 30 competitor outlier + 10 xkcd thumbnails in-browser | described in §4 | no files downloaded |
| SCORE | `scripts/score_topics.py` → `data/topic_scores_2026-11-18.csv` | | inputs labelled in the script |
| KB-PDF | YouTube Automation Master Playbook (sha256 `c630c24b…`), read pp.33–50 directly; P01–P22 map at `research/finance-economics-channel-forensics/00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md` | | Course heuristics; Part D says its thresholds are **not** official |
| KB-ALG | DS-000018 final validation synthesis (`data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md` §Final) | | only §A "safe platform knowledge" used as platform fact |
| KB-XK-CT | Existing xkcd visual forensics: `research/visual-forensics/channels/CH-000004/CHANNEL_DNA.md` (14 videos, 200 shots, 581 states) | | reused, not re-scanned |
| FRAMEWORK | reference_knowledge.db v1: RM-1f228411d7ab:chunk.3, .11, .60, .65, .100; rules FR-VC-01, FR-TITLE-02/04, FR-SCR-02, FR-16C-05/07 | | all CREATIVE_HEURISTIC |

**Limits:**
- The browser was signed in with region PK.
- Search pages show only the first ~20 results.
- The channel census reads only the first page of each channel (≤30 latest longs).
- Views are rounded display counts.
- **Survivorship bias:** channels were found *through* search, which favours channels that already have a hit.
- Competitor views ≠ our expected views.

## 1. What xkcd is making now (SRC-XK2 vs the 2026-11-04 census)

- **FACT — recent long uploads:**

  | Date | Video | Views |
  |---|---|---|
  | Nov 18 | Eat the sun | 445K in 10 h |
  | Oct 27 | Nuke the Mariana Trench | 2.9M, up from 2.59M on Nov 4 |
  | Sep 15 | Toaster in a freezer | 1.5M |
  | Aug 25 | Earth's water disappears | 1.0M |
  | Jul 7 | Rainbow on Tatooine | 0.7M |
  | Jun 16 | Antimatter except Earth | 1.4M |
  | May 26 | Bowling ball in the Mariana Trench | 2.5M |

- **DERIVED — cadence:** in 2026 the long videos come 3–6 weeks apart, while Shorts stay weekly. Long durations are 2:43–3:33. Every one of the 30 latest longs has ≥700K views.
- **DERIVED — repeating subjects:** xkcd returns to the same subject when it works.
  - Mariana Trench twice: 2.5M, then 2.9M.
  - The Sun twice: "all the sun's power focused", "eat the sun".
  - Oceans/water four times since 2025.

  This matches 01 §2: oceans & water was the best niche.
- **FACT — xkcd topics get copied fast:**
  - "What If We Nuked the Mariana Trench? | 3D Animation" by Visualized in 3D (1.68K subs) reached 497K within 4 weeks of xkcd's video.
  - A nuclear-engineer reaction video got 177K.
  - INTERPRETATION: covering a fresh xkcd topic is a proven but crowded move. It is also an IP and reputation risk if it looks like a copy, so we penalise collision (§6, C).
- **FACT — xkcd invented the "runaway per-second" format** that others now mass-produce:
  - xkcd's own: "Earth grew 1 cm every second" (6.2M) and "floated upwards 1 ft every second" (1.5M).
  - Copies: Minute Zero's "Sped Up and Couldn't Stop" (2.4M) and AfterTheFade's "Sun Moved One Kilometer Closer Every Second" (131K).
- **Packaging (SRC-PKG, OBSERVED):** xkcd thumbnails are wordless black-and-white line art with one red accent and a corner badge. Every one of the 10 sampled has no text. This is the opposite of the competitor norm (§4).

## 2. What others are making: format families with repeated outliers (SRC-M1)

An outlier = views ≥10× the channel's own page median. Families are an analyst classification of outlier titles (INTERPRETATION); counts are DERIVED.

| Family | Channels with ≥10× outlier | Examples (views, PI) | Fit for us |
|---|---|---|---|
| **L — "Every-X" survival/ladder** | Fossil, BeyondTheBlue, FAR SIGNAL, BrainZap, The Paint Explainer, Destiny (6) | Fossil "How Long You'd Last in Every Prehistoric Era" 13M (71×); FAR SIGNAL "How Long You'd Last on Every Planet" 985K (328×); BrainZap "Ancient Humans Evolved at Every Ocean Depth" 800K (143×) | High: it is the escalation ladder from 5 of xkcd's top-10 longs (01 §3) |
| **S — Scale / distance POV simulation** | Lightbound, D.A, Cosmic Witness, ScienceClic, Stargaze, Kian Odyssey, Ridddle (7) | ScienceClic "What would we see at the speed of light?" 8.6M; D.A "Sun From Different Places in the Universe" 2.6M; Lightbound "TON 618 at Different Distances" 1.3M (23×) | High, but heavily supplied by 3D-render channels |
| **T — Disaster / impact timeline** | Tracer Project, The Scale Room, The Last Day, Cosmic Witness, Visualized in 3D (5) | Tracer "What If Asteroid Apophis Hit Earth?" 5.6M (6,829×); Scale Room "Apophis… Hour by Hour" 719K (838×); The Last Day "Moon Crashed Into Earth" 2.0M | High; Apophis is a real 13 Apr 2029 close approach, so a news peg exists |
| **R — Runaway "…and couldn't stop / every second"** | Minute Zero, WhatIfAnimations, AfterTheFade, Runaway POV (4) | Minute Zero 2.4M + 2.1M; WhatIfAnimations "Light Kept Getting Slower" 433K (80×) | High; it is xkcd's own invention, so collision risk |
| **F — Far-future time skip** | OminiAM, Then what? (2+) | "What ACTUALLY happens if you travel back in time" 821K (46×); "One Billion Years Into the Future" 827K (97×) | Medium |
| **P — Personal superpower / human variable** | Ifverse, What if U click, Milo Whatsit, Possiblo, IfLoop (5+) | Ifverse "Reaction Time Was 10x Faster" 4.7M (69×); "You Aged Backwards" 961K (98×) | Low: entertainment, not physics; off-brand |
| **H — Prehistory "worst time to be human"** | Ink Explainer, Barely Evolved | 18M (56×), 9.7M (41×) | Adjacent niche; transplant candidate (Playbook M1 pro-tip) |

### The new-channel wave (DERIVED, important caveat)
- **What the census shows:** 25 of the 48 channels (excluding The Infographics Show) have every visible upload dated within about 1 month. These are new or near-daily channels. Their page medians run from 653 to 152K views, and 21 of the 25 have at least one outlier at ≥10× (up to 6,829×).
- **INTERPRETATION:**
  - This is a hit-lottery pattern: very high volume and a low typical result, with distribution coming from Browse/Suggested on 1–2 videos.
  - We only see the channels search surfaced, so channels with zero hits are invisible.
- **KB-ALG CLM-009 (SUPPORTED):** repetitive mass production carries *policy* risk (inauthentic-content and monetisation eligibility). Varied, materially distinct episodes can qualify. Playbook P04 says the same.
- **So:** do not copy the daily-volume model. Copy the *format families*, with original substance per episode.

### Big incumbents (FACT)
- **Kurzgesagt:** page median 5.8M.
- **"What If" (Underknown):** median 401K. Its titles overlap many bank topics: rings, Jupiter, fuel pool, oxygen.
- **Ridddle:** median 244K, with 4 outliers at ≥10×.
- **ScienceClic:** median 595K.
- **Unveiled and Life Noggin are effectively inactive in science what-ifs** (Unveiled pivoted to UFO interviews). Several old high-demand topics have ageing supply.

## 3. Algorithm knowledge applied (KB-ALG §A safe facts only)

- Ranking is personalised and depends on the surface; watch history matters most on Home (CLM-001/004/011). New channels get discovered through Browse/Suggested, not search keywords. This matches 02-F6, where the premises register 0 on Trends.
- Subscriptions don't guarantee viewers (CLM-008), so the 1–6K-subscriber channels with million-view hits are consistent with documented behaviour.
- Later discovery is documented (CLM-003). The "handful of videos that keep getting found" (FRAMEWORK RM-1f228411d7ab:chunk.65) supports evergreen science topics over news-only ones.
- Different formats can have different viewer preferences (CLM-005). Shorts and longs need to be judged separately; we must not assume Shorts feed long views.
- **Not used as fact:**
  - fixed CTR or retention thresholds
  - ideal length
  - fixed cadence (REC-005/006: no fixed upload frequency is established)
  - "personality premium"
- Series and recognisable formats are supported **creator guidance**, with no automatic ranking boost (REC-006).

## 4. Packaging check (SRC-PKG): 30 competitor outliers vs 10 xkcd

Observed in-browser at thumbnail size; no files were downloaded.

| Feature | Competitor outliers (n=30) | xkcd (n=10) |
|---|---|---|
| Overlaid words | Nearly all: 1–4 words, very large ("TOO SLOW.", "WHY NOT UP?", "NO HELMET?", "HORRIFYING DISTANCES") | 0 |
| Number or contrast device | Frequent: "APRIL 13 2029 · 2.7% CHANCE", "YOU 20 YRS / EARTH 27,000 YRS", "100 LIGHT-YEARS │ 1 LIGHT-YEAR", "AGE 0 / AGE 70", "1,235 km/h" | 0 |
| Split before/after panel | Several (dog today vs 50 years later; light-year split; age split) | 0 |
| Style | Two clusters: (a) dark photoreal 3D render of a cosmic or disaster subject; (b) flat cartoon figure on a coloured background (stickman-style) | Monochrome line art with a red accent and badge |
| Face or emotion | Cartoon faces common; one real face (Luke Davidson) | Stick figure, no expression emphasis |

- **INTERPRETATION:** the competitors converge on "one big subject + 2–4 word tension text or a hard number". xkcd succeeds without text because it is a known brand with 1.38M subscribers. A new channel cannot rely on brand recognition (HYPOTHESIS).
- **Proposal:** original line art for brand fit, plus one number or contrast element per thumbnail (FRAMEWORK RM-1f228411d7ab:chunk.100: packages get the click). Never reuse the xkcd stick-figure look (IP boundary, 01 §6).

## 5. Demand/supply scan (Playbook Method 4) — results and analyst corrections

**Method:** one all-time search per topic. Only on-topic long videos count (a regex on titles):
- supply = number of results with ≥50K views
- demand = sum of on-topic views

The thresholds operationalise the PDF's heuristic; they are not platform facts.

**Analyst corrections (D_OVERRIDE in the script)**, where the regex still admitted off-topic hits:
- WIB-12: game trailer
- WIB-26: country song
- WIB-54: SAT tips
- WIB-SA1: money-printing factory
- WIB-SA3: DIY gutter
- WIB-SA5: fitness
- WIB-07: periodic-table song
- WIB-41: Lego Shorts
- WIB-32: car-sim crashes
- WIB-04, 05, 49, 17: partial matches

### Clear gaps (high demand, ≤3 quality results, little recent supply)

| Topic | Gap evidence |
|---|---|
| WIB-55 neutron-star bullet | Kurzgesagt neutron stars 23.7M; only 3 on-topic results ≥50K, none in the last year |
| WIB-22 alien astronomers | Fermi-type demand ~43M; 4 results, 1 recent |
| WIB-17 little planet | Jumping on other planets 25M, with weak supply |
| WIB-52 loneliest human | RealLifeLore 19M, 9 years old; nothing recent |
| WIB-SA6 internet size | Vsauce 5.9M, 15 years old |
| WIB-24 plane on other planets | Low demand; 1 result (Insider, 9 years old) |
| NEW-10 hollow Earth | minutephysics 10.6M, 14 years old |

### Crowded (B), still viable with a distinct angle
- Black hole fall
- Jupiter fall
- Slower speed of light
- Sun from every planet
- Earth stops spinning
- Sun disappears
- Free fall from space (Red Bull Stratos footage dominates, but not explanation)

### Unusable as long-form (no demand evidence)
WIB-16, 33, 35, 40, 43, 45, 48, 50 and SA4. They may still work as Shorts experiments.

## 6. Explicit scoring (SCORE)

Each criterion is scored 0–5; total = 20 × weighted sum (0–100).

| Code | Criterion | Weight | Source label |
|---|---|---|---|
| D | Demand: sum of on-topic views, banded (≥20M = 5 … <200K = 0) | 0.25 | DERIVED + overrides |
| G | Gap: fewer ≥50K results scores higher; −1 if ≥3 of them are <1 year old | 0.15 | DERIVED |
| F | Fit to a format family with repeated outliers (L/S/T/R = 4–5; H = 4; Q = 1–4) | 0.25 | INTERPRETATION |
| C | Collision: 5 = xkcd never made it; 1 = xkcd made it >12 months ago; 0 = within 12 months; 2 = adjacent to a fresh xkcd hit | 0.15 | DERIVED from upload dates |
| V | Scientific verifiability and safety | 0.10 | INTERPRETATION |
| P | Production feasibility in original 2D/simple-3D | 0.10 | INTERPRETATION |

Excluded (score 0): WIB-25 Yoda (IP), 29 (sensitive), 37 (weapons), SA7 (explosives).

### Top 25 (full list: `data/topic_scores_2026-11-18.csv`)

| # | Score | ID | Topic | xkcd | Family | D G F C V P | Angle note (INTERPRETATION) |
|---|---|---|---|---|---|---|---|
| 1 | 90 | WIB-22 | Alien astronomers | unused | L | 5 3 5 5 4 4 | What aliens could detect of Earth at 10 / 100 / 1,000 / 10,000 light-years |
| 2 | 90 | WIB-55 | Neutron-star bullet | unused | S | 5 4 4 5 5 4 | Matter at neutron-star density in a human setting |
| 3 | 89 | WIB-36 | Free fall | unused | L | 5 2 5 5 5 4 | Falling from every altitude, from 1 m to orbit |
| 4 | 89 | NEW-08 | Slower speed of light | new | R | 5 2 5 5 5 4 | Crowded (WhatIfAnimations 433K); needs a distinct question |
| 5 | 88 | WIB-17 | Little planet | unused | S | 4 5 4 5 5 4 | Living on a tiny, super-dense world: orbit by jumping |
| 6 | 86 | NEW-07 | Fall into Jupiter | new | S | 5 1 5 5 5 4 | Supply recent (Kian Odyssey 356K, "What If" 12M) |
| 7 | 83 | WIB-11 | Last human light | MADE >12 mo | T | 5 4 5 1 5 4 | Remake decision needed |
| 8 | 83 | WIB-24 | Plane on other worlds | unused | L | 2 5 5 5 5 4 | "Flying a small plane on every planet": pure ladder gap |
| 9 | 83 | WIB-52 | Loneliest human | unused | Q | 5 4 3 5 5 3 | Old supply only |
| 10 | 83 | NEW-01 | Fall into a black hole | new | S | 5 0 5 5 5 4 | Saturated |
| 11 | 82 | WIB-15 | Lightning: plane / boat / pool / tower | unused | L | 3 3 5 5 5 4 | Every-location ladder |
| 12 | 82 | NEW-10 | Hollow Earth | new | S | 4 3 4 5 5 4 | |
| 13 | 81 | NEW-02 | Sun from every planet | new | L | 4 1 5 5 5 4 | Lightbound and D.A already did it; twist needed |
| 14 | 80 | WIB-18 | Steak drop | unused | L | 2 4 5 5 5 4 | Altitude ladder |
| 15 | 80 | WIB-44 | Expanding Earth | MADE >12 mo | R | 5 3 5 1 5 4 | xkcd's 6.2M video; remake = high collision |
| 16 | 79 | WIB-27 | Falling with helium | unused | Q | 5 2 3 5 5 4 | |
| 17 | 79 | NEW-11 | Tallest possible mountain | new | L | 4 2 4 5 5 4 | "On every planet" |
| 18 | 77 | WIB-13 | Rising steadily | MADE <12 mo | R | 4 4 5 0 5 5 | Avoid: xkcd made it in Mar 2026 |
| 19 | 76 | NEW-03 | Earth with rings | new | S | 4 1 4 5 5 4 | |
| 20 | 75 | WIB-51 | All the lightning | MADE >12 mo | Q | 5 3 4 1 5 4 | |
| 21 | 75 | WIB-56 | Richter 15 | MADE >12 mo | L | 4 3 5 1 5 4 | xkcd's "magnitude 0" Short got 7.8M |
| 22 | 75 | WIB-SA6 | Internet size | unused | S | 3 4 3 5 5 4 | |
| 23 | 75 | NEW-05 | Gravity doubles | new | R | 2 4 4 5 5 4 | |
| 24 | 74 | WIB-34 | Re-entry without a heat shield | unused | Q | 4 2 3 5 5 4 | |
| 25 | 73 | WIB-32 | Speed bump | unused | L | 3 0 5 5 5 4 | |

**Uncertainty:**
- F, V and P are my ratings. Changing one rating by ±1 moves a score by up to ±5 points.
- Ranks within about 5 points are effectively ties.
- D reflects the demand *topic-cluster* of each search, not demand for our specific angle.

**Not yet scored, candidate addition:**
- **T-01 Apophis 2029** (disaster-timeline family): two channels with 5.6M and 719K hits in the last month, and a real dated event, 13 Apr 2029. The science is verifiable from NASA/JPL.
- Supply is now high and very recent, so it scores as crowded B-tier, but it is timely. Treat as a Shorts/explainer test with a distinct angle (e.g. "how close is 'close'?" in scale terms), not an impact-fantasy remake.

## 7. Long/Short frequency recommendation (HYPOTHESIS for the 30-day test)

**Evidence:**
- Shorts are saturated: 596 this-month "what if" Shorts with a median of about 480 views (02-F1). xkcd's Shorts are 38/40 excerpts of longs (01).
- Long-form breakouts happen on new channels, at 6–16 min median durations in the census, but these channels are hit-driven.
- KB-ALG and KB-PDF Part D establish **no** required cadence (R5/R6); mass volume carries policy risk (CLM-009, P04).

**Proposal for 30 days:**
- **Long-form:** 2 per week, 8–9 longs in total. Front-load 3 in week 1, so each experiment has comparison points by Day 14. Target 6–10 min. Competitors' breakout median is about 9 min; xkcd runs about 3 min; no ideal length is established.
- **Shorts:** 3 per week, about 12 in total. Use about 8 as excerpts of our longs (xkcd's proven pattern) and about 4 standalone topic tests drawn from the low-demand bank items (Q-family). Shorts are judged separately from longs.
- **Experimental design:** each long belongs to one format family (L / S / T / R / Q), with at least 2 longs per family for the main three (L, S, T). Day 14 and Day 30 then compare *families*, not single videos. This will be defined fully with the calendar.
- **Why not daily:** production of original illustrated science with verified sources (01 §6 IP boundary, AGENTS.md slop gate) cannot be daily without becoming the repetitive pattern that CLM-009 flags.

## 8. CT-scan scope (visual-ct-scan standard)

**Done now:**
- Packaging-level visual review of 40 thumbnails (OBSERVED, at thumbnail resolution).
- The existing xkcd visual DNA (KB-XK-CT, 14 videos) is reused for xkcd's production grammar:
  - 89.8% of visual states are LOCKED/STATIC camera
  - median shot 7.77 s
  - the DNA's own caveats apply.

**Not done (honestly):** frame-level CT_SCAN of competitor videos. The standard requires the original MP4 plus ffprobe, hashes and a frame ledger. That means **downloading competitor videos, which needs your explicit approval**.

**Proposed scope if approved:** 3 videos, one per top family, stored under `YIOS_MEDIA_ROOT`, outside Git.
1. Fossil, "How Long You'd Last in Every Prehistoric Era" (L, 13M)
2. Minute Zero, "What If You Sped Up and Couldn't Stop?" (R, 2.4M)
3. Tracer Project, "What If Asteroid Apophis Hit Earth?" (T, 5.6M)

Output would be pacing, visual-state and motion grammar to inform *original* production, never copied.

## 9. Framework record

This is a scoring and landscape analysis, not a content plan. The `--framework-plan` gate (`content_plan_check.py`) will be run on the 30-day calendar.

| Item | Value |
|---|---|
| Framework version | v1 |
| Retrieved sections | RM-1f228411d7ab:chunk.3 (topics not yet covered in video form), chunk.11 (series/viewer journey), chunk.60 (single-topic focus), chunk.65 (evergreen "handful of videos"), chunk.100 (packages get clicks) |
| Rules applied | FR-VC-01, FR-TITLE-02/04, FR-SCR-02, FR-16C-05/07 |
| Rule class | All CREATIVE_HEURISTIC; none treated as platform fact |
| Exceptions | None |

## 10. Decisions needed before the calendar
1. Approve the scoring weights and the top-25 direction, or adjust the F/V/P ratings.
2. Remakes of xkcd-made topics: my recommendation is **no** for anything xkcd made in the last 12 months, and at most 1 remake older than 12 months, with a clearly different angle.
3. Frequency: 2 longs plus 3 Shorts per week, with week 1 front-loaded.
4. CT_SCAN: approve downloading 3 competitor MP4s for frame-level analysis, or skip it.
