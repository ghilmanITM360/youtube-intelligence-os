# Deliverable 1: Competitor analysis and source-bank audit

New English science-explainer channel (working brief: "inspired by xkcd's What If?").
Prepared 2026-11-18. Covers research steps 1, 2, 3, 5, 6, plus partial work on 4 and 7. **No calendar topics are selected here.** Steps 8–13 wait for approval of this audit.

Labels used throughout: **[FACT]** public or repository data, quoted as measured; **[DERIVED]** a computation on that data, reproducible from the scripts below; **[INTERPRETATION]** my judgment; **[HYPOTHESIS]** something to test, not yet evidence.

## 0. Sources

| ID | What | Location | Provenance |
|---|---|---|---|
| SRC-CENSUS | xkcd's What If? (`@xkcd_whatif`, UC6IxnFzHofFJ5X2PycSMsww) full public catalog, 91 videos, logged-out player view counts | `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/census/census.csv` | snapshot 2026-11-04T01:43Z, sha256 `104e9865…67b1`, tabs exhausted |
| SRC-RSS | Channel RSS feed, latest 15 uploads | `data/xkcd_rss_2026-11-18.xml` | fetched 2026-11-18T06:00Z |
| DS-000017 | 83 transcripts (Apify run mzl5dCHF81LbcBamS) | `data/raw/competitors/DS-000017/…` → `research/what-if-scripts/{long,shorts}` | sha256 per file in `data/manifests/DS-000017.md` |
| SRC-AUDIT | 83 script audits + comparison matrix (earlier "previous script research") | `research/what-if-scripts/analysis/` (`matrix.jsonl`, `audits/V###.md`) | commits 4e499d7e, 5986d1f2 |
| SRC-BOOK | *What If?* (Munroe, HMH 2014), 321 scanned pages, OCR in 15 HTML parts | `~/Downloads/What_If_Full_Book_15_Files/` (outside repo; not copied for copyright) | sha256 list in `data/book_ocr_source_sha256.txt` |
| FRAMEWORK | Reference knowledge framework **v1** | `data/knowledge/reference_knowledge.db` | see §7 |

Derived files: `data/xkcd_census_scored_2026-11-04.json` (niche tag + outlier score per video) and `data/book_chapter_to_video_map.json` (book chapter → transcript overlap). Scripts are in `scripts/`. `niches.py` was re-run from the census CSV and reproduced its output byte for byte.

## 1. Catalog audit (step 1)

- **[FACT]** 92 public videos as of 2026-11-18: 45 long-form and 46 Shorts in the census, plus one later upload (Aony69nO5kI, "What if we tried to eat the sun?", 2026-11-17, format not yet classified). There are no livestreams.
- **[FACT]** 83 of these have transcripts in the repo (DS-000017). **Nine have none:** 9VG0yqq_PHM, alkJ7xScBiw, TIDHee_Q5Gk, X97DDWvxaqQ, alBQCm0QpJg, 35KZm1yiyIE, NxVdO7M2YdM, XwJAbyn5uGY and Aony69nO5kI. The pending-registration contract applies to them; no transcript has been fabricated.
- **[FACT]** Cadence: 89 of 91 uploads went out on a **Tuesday**. The most common gap is 7 days (56 gaps), then 21 days (15) and 14 days (8). No upload on 2026-11-10.
- **[FACT]** Format mix by year: 2023–24 long only (20); 2025 had 14 long and 19 Shorts; 2026 to date 11 long and 27 Shorts. Since mid-2025 the channel has shifted toward Shorts.
- **[FACT, from SRC-AUDIT]** Only 2 of the 40 transcribed Shorts (V065 "Why is the sky blue?" and V080) are independent. The other 38 are verbatim excerpts or deletion-only abridgements of a long video. The channel's Shorts strategy is mostly **re-cutting proven longs**, not creating new Shorts.
- **[FACT]** Total views at the census: about 136.1M long-form (median 2.51M per video) and 68.7M Shorts (median 1.06M).

## 2. Micro-niche performance (step 2)

**Method [DERIVED]:** I tagged each video with one of 11 topic families after reading its title and, where a transcript exists, the script audit (the tag is **[INTERPRETATION]**). Raw views are confounded with age, because the oldest videos have had three years to accumulate. So each video also gets an **outlier score**: its views divided by the median views of the 6 same-format videos published closest to it. A score of 1.0 means typical for its period.

Long-form:

| Micro-niche | n | Median views | Median outlier | Videos ≥1.5× |
|---|---|---|---|---|
| Planet-scale Earth changes (rotation, growth, quakes, jumping) | 5 | 3.48M | **1.80** | 3 |
| Space & orbit | 2 | 4.48M | 1.33 | 1 |
| Absurd engineering | 7 | 1.77M | 1.08 | 0 |
| Units, money & society | 4 | 1.82M | 1.07 | 0 |
| Oceans & water (incl. Mariana Trench) | 7 | 2.59M | 1.05 | **3** |
| Human survival limits | 4 | 1.56M | 0.97 | 1 |
| Sun & stellar extremes | 3 | 1.57M | 0.94 | 1 |
| Exotic matter & particles | 4 | 2.28M | 0.94 | 0 |
| Light & optics | 4 | 2.95M | 0.91 | 1 |
| Moon | 5 | 1.99M | 0.77 | 1 |

Shorts, strongest first: Oceans & water (n=3, median outlier 2.99), Light & optics (n=5, 1.96), Exotic matter (n=2, 1.50). The weakest are Units/money/society (0.61), Space & orbit (0.67) and Human survival (0.72).

**Reading [INTERPRETATION]:** The most consistent signal appears in both formats. It is a **whole-planet or whole-ocean scale change with a concrete, imaginable consequence**: oceans draining, Earth rotating, quake-scale limits, a Mariana Trench depth payoff. Within long-form, "Oceans & water" has the median outlier near 1.0 but contains three hits, including the two newest Mariana Trench videos. Every niche has n ≤ 10 and most have n ≤ 5, so **no niche ranking here is statistically reliable.** Treat these as leads.

**Title features [DERIVED, descriptive only, confounded with topic]:**
- Long titles that do *not* start with "What if" have a slightly higher median outlier (1.25, n=13) than those that do (0.99, n=32).
- Titles with a death or survival word have a median of 2.12 (n=5); titles with a number have 1.83 (n=4).
- All 45 long titles are questions.

None of this is causal, and it says nothing about CTR, which no one outside the channel can observe.

## 3. Top 10 long-form and top 5 Shorts (step 3)

Ranked by lifetime views on 2026-11-04. The outlier score is shown so that age effects stay visible. Script notes come from SRC-AUDIT; they are structural readings, not performance explanations.

| # | Video | Views | Age (d) | Outlier | Script pattern (SRC-AUDIT) |
|---|---|---|---|---|---|
| L1 | 8fADp43wJwU If all humans died, when would the last light go out? (V011) | 10.41M | 889 | 3.37 | Elimination tournament; a false final answer, then a "dark horse" winner; elegiac ending |
| L2 | UXA-Af-JeCE Could you survive a nanosecond on the Sun? (V015) | 9.18M | 791 | 2.42 | Asker's childhood story; safe case, then a deadly variant; myth-reframe moral |
| L3 | e3uk7jU3RHo What would a magnitude 15 earthquake be like? (V002) | 9.05M | 1064 | 2.69 | Two-way scale ladder (up to cosmic, then reversal down to trivial) |
| L4 | pfbzrrcQZjs What if you funneled Niagara Falls through a straw? (V027) | 6.27M | 504 | **3.63** | Three-answer cold open; an apocalypse teaser retracted, then delivered; bureaucratic bookends |
| L5 | -1-ldW4kpLM What if Earth grew 1cm every second? (V017) | 6.22M | 749 | 1.80 | Elapsed-time escalation ladder; audience riddle; wonder ending (Earth gets rings) |
| L6 | JqFSGkFPipM What if everyone pointed a laser at the moon? (V018) | 6.09M | 728 | 1.77 | Seven-rung ladder driven by a "more power" refrain; answer at rung 4, climb continues |
| L7 | EsUBRd1O2dU Would a Submarine Work as a Spaceship? (V007) | 5.81M | 973 | 1.76 | Answer-first, then three nested loops; "technically" reversal |
| L8 | 0EytSWiKrFg What if a glass of water were LITERALLY half empty? (V016) | 4.35M | 770 | 0.95 | Idiom literalised; three-condition micro-timeline; idiom twist |
| L9 | fs28lEq9smw What if all the lightning on Earth struck the same place at once? (V010) | 4.01M | 910 | 1.26 | Proverb bookends; scale-down to real world |
| L10 | gp5G1QG6cXc What if Earth suddenly stopped spinning? (V004) | 3.48M | 1029 | 1.03 | Consequence cascade |

Not in the lifetime top 10 but ≥1.85× outliers: alkJ7xScBiw (nuke in Mariana Trench, 2.59M in 7 days, 2.12; no transcript), FYoHYq8VRt0 (bowling ball in Mariana Trench, 2.09) and WH4g1ptJ-70 (Earth rotated 90°, 1.85).

| # | Short | Views | Age (d) | Outlier | Origin (SRC-AUDIT) |
|---|---|---|---|---|---|
| S1 | FKXVs4UteSc Is there such a thing as a magnitude 0 earthquake? (V029) | 7.80M | 490 | **6.47** | 100% verbatim excerpt of L3, ¶21–34 |
| S2 | aMshLs0YCTQ What if you drained the oceans? (V052) | 4.96M | 322 | 2.99 | Deletion-only abridgement of V012 |
| S3 | TIDHee_Q5Gk What if all visible light was a single beam? | 4.31M | 63 | 3.17 | No transcript; origin not verified |
| S4 | 2p305nzcVQE What if we teleported the oceans to Mars? (V053) | 3.68M | 315 | 3.24 | Abridgement of V013; opens with a recap of S2 |
| S5 | wBLVmEZV2Oc How high could the magnitude of Earthquakes go? (V028) | 3.60M | 497 | 2.98 | 100% verbatim excerpt of L3, ¶5–14 |

**Observations [INTERPRETATION, from SRC-AUDIT rows; to be completed with thumbnails in step 4]:**
1. All 10 top longs open with an attributed reader question. Most then make an early reframing move: answer-first, contradiction, or a flash-forward.
2. Five of the 10 (L1, L3, L5, L6, L7; arguably six with L4's speed ladder) run on an **escalation or elimination ladder** (scale ladder, time ladder, power refrain, elimination tournament): one premise, pushed rung by rung. This is the most repeatable spine in the winners.
3. Endings are a twist, a wonder image or a punch line. No CTA appears in any of the top 10.
4. Four of the top 5 Shorts are excerpts from top longs. Two of them come from **one** long (L3). The Shorts strategy amplifies proven longs, and **a new channel has no proven longs to cut from.** This is the main reason the competitor's Shorts numbers do not transfer.

Thumbnail analysis (part of step 4) is **not done in this deliverable**. Hosted thumbnail URLs exist in SRC-CENSUS, and local forensic material exists for a subset under `research/visual-forensics/channels/CH-000004/`.

## 4. Source-bank audit: 83 transcripts vs the book (steps 5–6)

**What the book contains [FACT, from OCR, checked against the table of contents]:**

| Unit | Count | Has an explanation? |
|---|---|---|
| Answered chapters | 56 (incl. "Drain the Oceans: Part II") | yes |
| Short-Answer Section questions | 7 | yes (short) |
| Multi-question chapters | Lightning (≥3 sub-questions), Orbital Speed (3), Falling with Helium (2) | yes |
| "Weird (and Worrying)" inbox pages | 12 pages, about 25–30 one-line questions (OCR undercounts the "Q." markers) | **no**, joke reply or cartoon only |

**[UNCERTAINTY]** The brief says "90 book questions with explanations". I found **63 explained question units** (56 chapters + 7 short answers), about 70 counting sub-questions, and about 90–97 only if the unanswered Weird & Worrying questions count. I did not find a separate 90-item file in the repo or in Downloads. **If a curated 90-question list exists, please point me to it.** The audit below uses the book itself.

**Method [DERIVED]:** I took word 5-grams of each chapter's OCR text and measured what share of each transcript's 5-grams also occur in the chapter. The split is clean. Every matched transcript scores 0.22–0.76; every unmatched one scores ≤0.007. Nothing falls in the ambiguous middle.

**Results:**
- **20 of 56 chapters are already videos.** These are Global Windstorm, Relativistic Baseball, Spent Fuel Pool, Laser Pointer, Everybody Jump, A Mole of Moles, Last Human Light, Machine-Gun Jetpack, Rising Steadily, Orbital Submarine, Glass Half Empty, No More DNA, Drain the Oceans I and II, Longest Sunset, Expanding Earth, Sunless Earth, Updating a Printed Wikipedia, All the Lightning and Richter 15. Most also have one or more derived Shorts.
- **Weird & Worrying #1, #2 and #4** are partly used, in the Short SLd4hnmeW_g. Its sequel alBQCm0QpJg has no transcript, so further reuse cannot be checked.
- **23 of the 45 long videos come from outside this book**: Hubble, NASCAR, laser umbrella, the Sun nanosecond, the billion-story building, the Moon black hole, the Mariana Trench videos and others. Their source (*What If? 2* from 2022, the blog, or new questions) is **not verified**, because *What If? 2* is not among the inputs.
- **Unused: 36 chapters + all 7 short answers = 43 explained question units.**

**Duplicate check [FACT]:** There are 0 exact-duplicate transcripts (SRC-AUDIT D1). 56 of 83 transcripts share ≥30% 8-grams with another transcript, because Shorts are cut from longs. So the 83 transcripts are about **45 independent content families, not 83 independent data points.** Any pattern count must be per family.

**Collision risk [INTERPRETATION]:** xkcd is still mining this same book (No More DNA in 2026-01, Rising Steadily in 2026-03, plus 2026-10 Shorts). Any "unused" chapter could appear on their channel any Tuesday. An unused chapter is unused *today*, not reserved.

### Preliminary triage of the 43 unused units (step 7, not scored, not final)

This triage uses only fit with the competitor's stronger niches and visible risk. Scoring with explicit criteria is step 10. Google Trends, YouTube search and scientific validation (step 8) have **not** been done.

| Tier | Units | Why |
|---|---|---|
| A: fits a strong niche, evergreen, visual | Raindrop, Free Fall, Everybody Out, Neutron Bullet, Periodic Wall of the Elements, Lethal Neutrinos, Interplanetary Cessna, Little Planet, Hair Dryer, Steak Drop, Speed Bump, Lego Bridge, High Throw, Orbital Speed; short answers: nuke in a hurricane's eye, physical size of the internet | Planet/ocean/stellar scale or a body-limit ladder; map onto the escalation spine |
| B: good, but needs fresh data or has a narrower audience | FedEx Bandwidth, Facebook of the Dead, Twitter (2014 data; a 2026 update is itself an angle), Lightning (boat/plane/tower), Common Cold, Loneliest Human, Weightless Arrow, Stirring Tea, Falling with Helium, Hockey Puck, Human Computer, Alien Astronomers, Soul Mates, Lost Immortals, NY Time Machine, Random Sneeze Call, Sunset on the British Empire, Flyover States (US), SAT Guessing (US); short answers: downspout turbines, star names, biking to warm skin, printer money | Dated numbers or regional scope |
| C: avoid or handle with care | Yoda (Star Wars IP), Sparta (film premise), Self-Fertilization (sensitive reproductive topic), C4 boomerang (explosive weapon; platform-policy risk), Weird & Worrying lines (no explanation to verify) | IP, policy or sensitivity risk |

## 5. What does not transfer to our channel (read this before any calendar)

1. **[INTERPRETATION]** xkcd's views ride on Randall Munroe's existing audience, two bestselling books and the xkcd brand. A new channel posting the same question will **not** get comparable views. Our success thresholds must come from our own Day 14 and Day 30 data, not from these medians.
2. **[FACT]** Nothing here measures CTR, retention, impressions or traffic source for any competitor video. Those cannot be observed from outside. I have not inferred them from views.
3. **[INTERPRETATION]** The Shorts numbers reflect re-cuts of proven longs on an established channel, so they are not a benchmark for cold-start Shorts.
4. **[HYPOTHESIS]** The planet/ocean-scale escalation premise and the ladder spine are the transferable parts: a topic class and a story structure, not a brand.

## 6. Originality and IP boundary (applies to every later step)

- The book's answers, drawings, stick figures, wording and the "This question comes from…" format are Munroe's. We may use a *question* as a topic signal. The science must be **re-derived from primary sources** (NOAA, USGS, NASA, peer-reviewed papers), with our own numbers, structure, characters and art.
- Remaking a question xkcd already turned into a video (for example, draining the oceans) is a separate decision with extra risk: we would compete with their video in search and could look derivative. **Your call; see §8.**
- Every later script passes `scripts/check_slop_risk.py` before delivery, as AGENTS.md requires.

## 7. Reference framework record

Framework **v1** (`data/knowledge/reference_knowledge.db`, FTS5 via `build_reference_kb.search`). Sections retrieved: `RM-d0f681ddcabe:p.28`, `p.30`, `p.55` (new-channel testing), `p.91` and `p.92` (Shorts with long-form), `p.44` and `p.56` (upload frequency), `p.67` (niche expansion), `RM-1f228411d7ab:chunk.100` (outlier scoring).

All of these are reference-corpus claims, **not platform facts**. Note that `p.91` (mixing Shorts and long-form can hurt) and `p.92` (Shorts feed long-form) pull in opposite directions; step 11 will treat both as hypotheses. Rules applied in this audit: FR-TITLE-02 and FR-TITLE-04 (title-to-concept match and an open loop the video pays off, both visible in all top-10 longs); FR-16C-05 (one central question, all top-10); FR-SCR-02 and FR-16C-07 (open loops: V002, V007, V018). All are `CREATIVE_HEURISTIC`.

**Exception:** this deliverable is an audit, not a content plan, so `content_plan_check.py` and `--framework-plan` do not apply yet. They will apply to the calendar.

## 8. Decisions needed from you before steps 7–13

1. **The 90-question list:** is there a curated file, or should I use the 63 explained units found here?
2. **Already-made topics:** allow re-angled versions of questions xkcd has already turned into videos, or restrict the bank to the 43 unused units plus new questions?
3. **Wider competitor set:** the repo holds public data for one relevant channel only (`whatif4k` is a WW2 history channel, not a science channel). Step 2 is therefore single-channel evidence. I recommend a zero-cost public census (the same method as SRC-CENSUS) of 5–8 adjacent science-hypothetical channels before any topic is scored. Approve, or name the channels?
4. **Step 8 tools:** Google Trends and YouTube search validation would use the Chrome browser (logged-out pages, no paid API). Approve?
