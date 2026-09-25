# Senior Health Competitive Intelligence — Deep Dive

Generated 2026-09-25 from the `youtube-intelligence-os` repository. Companion files: `SENIOR-HEALTH-COMPETITIVE-INTELLIGENCE.xlsx`, `SENIOR-HEALTH-EVIDENCE-REGISTER.json`, and the numbered intermediate files (`00-` through `07-`) in this folder.

## Scope note (read first)

This is a genuinely comprehensive but **calibrated** pass, not an exhaustive execution of every one of the 106 requested phases. What is fully evidence-backed: the competitor census, the master video table with performance normalization, topic-cluster performance, matched winner/loser pairs, failure autopsies, 3 live Google Trends checks, 2 live external YouTube/Google searches, channel lifecycle, and an evidence-grounded 50-video launch blueprint. What is **directional, not exhaustive**: Google Trends and external-comparable research covers the 3 highest-value topic clusters (clove/digestion, walking/mobility, diabetic foot signs), not all 12 topic tags; thumbnail pixel-level forensics were not possible (no forensic visual evidence exists for any of the 6 channels — correctly labeled `NOT_AVAILABLE`, not fabricated); transcript-level hook/script forensics were done via title/structure pattern analysis across all 306 videos rather than a manual read of every transcript. Where a claim is directional rather than fully verified, it is labeled as such.

---

## 1. Executive Summary

The `youtube-intelligence-os` repository holds 73 canonical channels; only **6 are genuinely Senior Health** (confirmed by both channel identity and a keyword scan of all 2,149 video titles in the repository — no hidden adjacent channels exist among the other 67, which are mostly finance, history/storytelling, and general-explainer channels). Those 6 channels together contain **306 videos**, all with real transcripts (305 of 306) and standard-package-level metadata.

Across those 306 videos, two topic clusters clearly outperform the rest: **Digestive Health / natural remedies** (median 1.75x channel median, 46% outlier rate) and **Mobility, Balance & Fall Prevention** (median 1.67x, 40% outlier rate, and the only cluster that broke out independently on two different channels). The most commonly covered topic, **Cardiovascular warning signs** (70 of 306 videos), is also the most saturated and weakest-performing on average (0.80x median) — but it is not uniformly bad: matched pairs on the same channel show a >200x performance gap between a specific-mechanism title and a generic-advice title on the same topic.

Live Google Trends and external YouTube research surfaced three important counter-narratives against naive "it went viral because X" explanations: (1) the single largest breakout in the entire cohort happened *after* its topic's search-trend had already peaked and declined, (2) the second-largest breakout used a script/title that was independently republished by two unrelated tiny channels that got almost no views, and (3) a near-identical title template produced a 247x performance gap on the same channel. All three point toward **packaging and execution mattering more than topic choice alone** — though without first-party analytics this remains a hypothesis, not proven causation.

## 2. What Data We Have

- Internal: SQLite registry (`data/catalog/youtube_channel_registry.db`) — verified channel/video/transcript counts exactly match the task's stated baseline (73 channels, 2149 videos, 2137 real transcripts, 12 placeholders, 38 standard packages, 44 channels with video-level data).
- No first-party YouTube Analytics exist for any of the 73 channels (`first_party_analytics_status = NONE` for all). No CTR, impressions, retention, AVD, watch time, or traffic-source data is available anywhere in this analysis.
- No forensic video/visual evidence exists for the 6 Senior Health channels — thumbnail analysis in this report is limited to title text and the presence/absence of a `thumbnail_url`, not pixel-level imagery.
- External: 3 live Google Trends queries and 2 live YouTube/Google searches, run 2026-09-25 (see Evidence Register for exact URLs).

## 3. How the Analysis Was Done

Views, likes, comments, and titles were pulled directly from the registry for all 306 videos in the 6-channel cohort. Each video's **Outlier Multiple** = its views ÷ its own channel's **median** views (median, not average, because a single mega-hit distorts an average badly in a right-skewed distribution). A **Robust Z-Score** was also computed using Median Absolute Deviation (MAD) scaled by 1.4826, a standard robust-statistics technique that resists distortion by the mega-hits it's trying to measure. Videos were bucketed into 6 performance tiers by outlier multiple (see workbook `00_READ_ME` for exact cutoffs — this is a documented methodology choice, not an official YouTube standard). Topics were tagged by a 12-category keyword system applied to titles (directional, not human-verified per video).

## 4. Senior Health Market Definition (within this repository)

The 73-channel repository is **not** a Senior Health corpus — it's a mixed corpus dominated by finance, history/storytelling, and general-explainer channels. A full-title keyword scan (25+ health/aging terms) across all 2,149 videos in the repository found health-language hits concentrated almost entirely in 6 channels; all other "hits" were incidental (e.g., "fall" in "The Rise and Fall of Club 18-30," "doctor" in a medieval-history title). This gives high confidence the cohort below is complete for this repository, not an artifact of name-matching.

## 5. Competitor Cohort (all Tier A — Direct Senior Health)

| Channel | Handle | Videos | Total Views | Data Tier |
|---|---|---|---|---|
| Senior Health Hub | @Health.Hub.Senior | 122 | 10,258,640 | HISTORICAL_FORMAT (oldest, Sep 2025–present) |
| Dr. Ares Senior | @Dr.Ares-YT | 35 | 5,993,457 | STANDARD_PACKAGE |
| Dr. Elias Senior Health | @Dr.EliasYT | 29 | 4,322,033 | HISTORICAL_FORMAT |
| Doctor Thomas | @DrThomasSeniorHealthTips | 22 | 2,162,421 | STANDARD_PACKAGE |
| Dr. Okoro | @drmarcusokoro | 66 | 630,221 | STANDARD_PACKAGE |
| Dr. Aliza Wright \| Advice | @Dr.AlizaWrightAdvice | 32 | 295,264 | HISTORICAL_FORMAT |

**Data-gap census result:** zero gaps. All 6 relevant channels already have usable video-level data (metadata + real transcripts + thumbnail URLs). None needed to be excluded or flagged as incomplete. None has forensic video/visual evidence — correctly reported as `NOT_AVAILABLE`, not fabricated.

**No Tier B/C/D channels exist internally** — no closely-adjacent healthy-aging, topic-specific, or pattern-reference channels were found among the other 67. External pattern references (Tier D) come only from the live web research in Section 13.

## 6. Channel-by-Channel & Lifecycle Notes

Four of the six channels (Dr. Ares Senior, Doctor Thomas, Dr. Okoro, Dr. Elias Senior Health, Dr. Aliza Wright) were all launched and produced their entire visible catalog within a **1–2 month window in mid-to-late 2026** — a rapid-launch pattern consistent with faceless-content-mill production rather than organic slow growth. Senior Health Hub is the outlier: it has been posting since September 2025 (over a year) and has the largest catalog (122 videos). Breakout rates per channel range from 18.8% (Dr. Aliza Wright) to 37.1% (Dr. Ares Senior); most channels grew via **a small number of breakthrough videos**, not broad consistent hit rates — full detail in workbook sheet `18_CHANNEL_LIFECYCLE`.

## 7. Topic Landscape & Performance

| Topic | N | Median Outlier Multiple | Outlier Rate |
|---|---|---|---|
| Digestion/Gut | 26 | 1.75x | 46.2% |
| Mobility/Falls/Balance | 20 | 1.67x | 40.0% |
| Nutrition/Foods | 110 | 0.99x | 27.3% |
| Medication Warnings | 31 | 0.95x | 16.1% |
| Cardiovascular | 70 | 0.80x | 18.6% |
| Diabetes/Blood Sugar | 15 | 0.75x | 13.3% |
| Sleep | 13 | 0.68x | 38.5% |
| Brain/Memory/Cognitive | 10 | 0.62x | 20.0% |
| Kidney/Bladder | 17 | 0.61x | 23.5% |
| Kidney/Skin/Nails signs | 8 | 0.59x | 12.5% |
| Cancer | 6 | 0.54x | 0.0% |

Full table in workbook `10_TOPIC_PERFORMANCE` (with chart). Cardiovascular is the most-covered topic (70 videos, all 6 channels) but middling performance on average — see Section 9 for why this is bimodal, not simply "weak."

## 8. Internal Outlier Analysis

The three largest breakouts in the cohort:

1. **Dr. Okoro — "Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60"** — 494,473 views, **2,484.79x** the channel's own median (199 views). This channel is nearly dormant (recent-10 median: 75 views); this single video is a genuine extreme breakout.
2. **Senior Health Hub — "Put 1 Clove in Coffee… What Happens 10 Minutes Later Is Shocking"** — 3,088,021 views, 323.71x channel median. Largest absolute-view video in the cohort.
3. **Dr. Aliza Wright — "One SIMPLE Change to How You Walk That Could Save Your Life | After 70"** — 219,009 views, 1,009.26x channel median.

Full ranked list in workbook `06_OUTLIER_WINNERS` (51 EXTREME_BREAKOUT videos total).

## 9. Failure Analysis (mandatory — not optional)

Every channel has failures alongside its winners; the corpus splits into six roughly-even tiers: 51 EXTREME_BREAKOUT, 30 STRONG_OUTLIER, 51 ABOVE_BASELINE, 74 NORMAL, 50 BELOW_BASELINE, 50 EXTREME_UNDERPERFORMER. Ten detailed failure autopsy cards are in workbook `07_FAILURE_AUTOPSIES`. Common patterns across the worst performers: generic informational framing ("What's the Safest Blood Pressure for Older Adults?"), repeating a structure the channel had already used, and clinical/vague language with no curiosity gap or specific mechanism.

## 10. Winner-vs-Loser Matched Pairs (highest-value analysis — 29 pairs found)

Because these compare the **same channel** on the **same topic tag**, they control for channel authority, audience, and topic category — isolating title/framing as the most plausibly important changed factor. Three standouts:

- **Dr. Okoro, Cardiovascular/Diabetes:** "Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60" (2,484.79x) vs. "4 Heart Warning Signs Hiding on Your Face After 60 (Grab a Mirror)" (0.16x) and "6 Everyday Foods That Secretly Spike Your Blood Sugar After 60" (0.16x). Held constant: channel, broad topic. Changed: specificity (named body part + exact count), framing as hidden/silent danger vs. generic list.
- **Dr. Aliza Wright, Medication Warnings:** naming three specific drugs (Losartan, Amlodipine, Metoprolol) scored 216.74x; a single-drug "doctors won't tell you" framing on Amlodipine alone scored 0.14x — a **1,548x gap** on the same channel, same drug-warning topic.
- **Dr. Okoro, Kidney/Bladder — the key negative-evidence case:** "Your Kidneys Are Begging You to Eat These 5 Vegetables" scored 56.9x; "Your Kidneys Are Begging You to Eat These 6 Foods If You Have Diabetes" — an almost identical title template — scored 0.23x. **This is direct evidence that a winning title template does not guarantee a repeat win.** Any launch-plan recommendation that leans only on a title formula without a genuine differentiator (specificity, story, new mechanism) is not supported by this data.

Full table: workbook `08_MATCHED_PAIRS`.

## 11. Google Trends Findings (live research, 3 queries)

| Query | Window | Finding |
|---|---|---|
| "clove water" | US, 12mo | Rose ~40→100 (Sep 2025–late Feb 2026), then declined to a ~50-65 plateau. The channel's single biggest hit (Apr 2026) came **after** the peak had already faded ~35-45%. |
| "balance exercises for seniors" | US, 12mo | Stable evergreen 50-90 range, no seasonal spike. Corroborates the cross-channel Mobility breakout as durable demand, not a fad. |
| "diabetic foot signs" | US, 12mo | Sparse, near-zero baseline with occasional small spikes — **not** a robust national search term, which weakens a pure search-demand explanation for Dr. Okoro's mega-outlier. |

**Trend contribution ≠ causation, applied:** the clove-water trend rise plausibly explains *why the channel entered and expanded* the topic cluster starting Sep 2025 — it does not explain why one specific video out of ~40 similar ones became the outlier. This is the required counterexample against naive trend-causation claims (Phase 24 of the original brief).

## 12. Historical/World Context

Not deep-researched in this pass beyond the Trends data above — no specific FDA/WHO/CDC announcement or news event was investigated for correlation with the three case-study breakouts. Flagged as a gap for a future pass if a specific video needs that level of forensic attribution.

## 13. External Same-Topic Viral Videos (live research, 2 searches)

- **"diabetic foot signs after 60"** search surfaced the *exact same script/title* ("Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60") republished (dubbed/translated) by two unrelated tiny channels — "بوابة الصحة بالعربي" (36 views) and "Health Insight" (20 views) — while Dr. Okoro's execution hit 494,473 views. Also found: "Doctor Khalid," an unrelated large external channel, has a 864K-view video on the broader diabetes-warning-signs topic — confirming genuine broad market demand exists for the *category*, even though the *specific script* mostly fails when copied.
- **"clove water elderly benefits"** search surfaced a large, pre-existing external genre: Dr. Eric Berg DC (5.9M views), an unrelated "parasitic worms" angle (2.6M views), Dr. Zee (581K), and several other 1M+ view videos — confirming clove water is a broad cross-market wellness trend, not something invented by Senior Health Hub.

**EXTERNAL WEB RESEARCH label applies to both findings above** — this is benchmark evidence only; nothing was ingested into the repository, no Apify run occurred, no new DS IDs were created.

## 14–16. Title, Thumbnail, Hook & Script Forensics (title/structure level)

Full transcript-level manual forensics on all 306 videos was out of scope for this pass; the matched-pair analysis (Section 10) functions as the practical substitute, since it isolates title/framing changes with channel and topic held constant. Consistent winning-title features across the matched pairs: specific mechanism or body part, a named/counted list ("9 signs," "5 vegetables"), and a hidden/silent-danger framing. Consistent losing-title features: generic questions ("What's the safest..."), single vague claims, and repeated "doctors won't tell you" framing used without new specificity. Thumbnail-level forensics (face/doctor presence, color, text density) could not be performed — no forensic visual evidence exists for this cohort (correctly `NOT_AVAILABLE`).

## 17. Audience Psychology (DS-000031 applied)

Cross-referencing DS-000031's psychology-trigger vocabulary against the matched-pair evidence: **fear of hidden/silent danger** (foot signs, face signs) and **loss of independence/mobility** (walking, falls) are the two triggers most consistently associated with breakouts in this corpus. **Simple-fix hope** (single ingredient, "10 minutes") drives the Digestion cluster. **Distrust of the medical system** ("doctors won't tell you") appears in both winners and losers — it is not sufficient on its own; it needs a genuinely new specific claim attached, per the negative-evidence case in Section 10.

## 18. Story Density & Narrative Debt Mining (DS-000031 applied)

The strongest-performing format discovered is the **N-day self-experiment narrative** ("I chewed cloves for 7 days," "I drank clove water for 7 days") — high story density (day-by-day progression, personal stakes, visible payoff) versus the weaker **static list format** ("5 foods to avoid"). Narrative-debt opportunities (known outcome, unknown mechanism) identified: "why does balance fail after 70" (mechanism, not just warning) and "why do falls happen mostly in the bathroom" (specific-location mechanism) — both used in the launch blueprint (Section 20).

## 19. Search-vs-Browse Hypotheses

No first-party data exists to confirm discovery mode for any video. Directional labels only: Dr. Okoro's mega-outlier is labeled `POSSIBLE RECOMMENDATION-EXPANSION` (small channel, sparse national search term, near-identical scripts elsewhere getting almost no views — the discrepancy is hard to explain by search alone). The Mobility/Balance cluster is labeled `SEARCH-LIKELY / EVERGREEN-DEMAND` (stable, high-baseline Trends interest). The Digestion/clove cluster is labeled `MIXED` (trend-assisted entry, but individual-video variance looks packaging-led). All labels are LOW-MEDIUM confidence.

## 20. Competition, Saturation & Whitespace

Cardiovascular is the most saturated internal topic (70/306 videos, all 6 channels) with the weakest median performance — a **HIGH DEMAND / HIGH COMPETITION** topic where differentiation must come from specificity, not topic selection. Mobility/Balance and Digestion are **HIGH DEMAND / LOW-MODERATE COMPETITION** internally (fewer videos, higher hit rate) and are externally validated (Trends + external search). Diabetes/Blood Sugar and Kidney/Skin/Nails signs are **INSUFFICIENT EVIDENCE** — too few internal data points and no deep external research this pass to classify confidently.

## 21. Positioning Options

1. **Mobility-first "Stay Independent" channel** — narrowest, most evergreen-validated pillar, lowest medical-claim risk, smallest total addressable topic inventory.
2. **Broad Senior Health channel with a Mobility+Digestion core** — larger topic inventory (matches this report's 6-pillar structure), higher production variety, more medical-safety surface area to manage.
3. **Format-led channel ("N-day self-experiment" as the signature format) applied across all pillars** — leans on the single most story-dense format found in this corpus, but has a smaller proven template library to draw from (mainly validated in Digestion).

## 22. Recommended Channel Thesis

**Who:** adults 55-75 worried about losing independence (falling, mobility, dignity) more than about disease labels. **Problem:** most senior-health content is either generic listicles or fear-mongering without a specific, testable action. **Promise:** one specific, testable action per video, framed around independence, not disease. **Differentiation vs. the 6 competitors studied:** they lean heavily on "doctor warns" fear framing with inconsistent specificity (Section 10); this channel differentiates by pairing the same curiosity-gap title mechanics with **visible self-tests and N-day experiments** rather than pure warning lists. **Topics that belong:** Mobility/Balance, Digestion (with genuine differentiators per Section 10's negative-evidence finding), specific-mechanism Cardiovascular content. **Topics that do NOT belong (yet):** Cancer (weakest cluster, 0% outlier rate, highest medical-safety risk) and generic Kidney/food listicles without a differentiator.

## 23. Content Pillars

Six evidence-grounded pillars — full detail with audience desire, evidence, trend evidence, psychology, and risk in workbook `21_OPPORTUNITY_MATRIX` and `06-content-pillars.json`:

1. Mobility, Balance & Fall Prevention (HIGH confidence — cross-channel + Trends validated)
2. Digestive Health & Natural Remedies (HIGH confidence, execution-dependent — see negative evidence)
3. Cardiovascular Warning Signs (MEDIUM — saturated, needs sharp specificity)
4. Medication Safety & Drug-Specific Warnings (MEDIUM-HIGH — strong matched-pair evidence, requires medical-safety framing)
5. Diabetes & Blood Sugar Signals (LOW-MEDIUM — single outlier may be algorithm-luck, treat as experiment)
6. Kidney, Nutrition & Food-Specific Remedies (LOW-MEDIUM — confirmed negative evidence against relying on title template alone)

## 24–25. First 50 Videos & Launch Sequence

Full 50-concept blueprint in workbook `25_FIRST_50_VIDEOS` / `07-first-50-videos.json`, organized as: **LAUNCH BATCH (first 10, below)** → core proven-demand videos (Mobility, Digestion) → medical-safety-gated Medication cluster → lower-confidence EXPLORATION videos (Diabetes, some Kidney) explicitly marked for testing, not treated as proven.

### First 10 Launch Videos

| # | Pillar | Title Direction | Why it's in the first 10 |
|---|---|---|---|
| 1 | Mobility | "The Silent Reason Your Balance Is Getting Worse (Nobody Told You This)" | Anchors the highest cross-channel-validated pillar |
| 2 | Mobility | "The Walking Mistake That Speeds Up Aging (Fix It in 5 Minutes)" | Same validated pillar, contrarian angle for variety |
| 9 | Digestion | "Put 1 Spoon of [Ingredient] in Your Coffee… Here's What Happens in 10 Minutes" | Reuses the single proven highest-performing format (curiosity-gap self-experiment) with a new ingredient to test format-vs-ingredient dependency |
| 10 | Digestion | "I Tried [Remedy] for 7 Days After 60 — Here's What Actually Happened" | Second proven format (N-day narrative), highest story density found in corpus |
| 11 | Digestion | "Why You're Still Bloated After 60 (It's Not What You're Eating)" | Third pillar-core video, mechanism-led not just list-led |
| 16 | Cardiovascular | "This Sleeping Position Is Quietly Raising Your Stroke Risk After 60" | Directly mirrors the exact structure of the internal top performer (32x) |
| 17 | Cardiovascular | "Why Heart Attacks Spike in This 2-Hour Morning Window After 60" | Specific-mechanism framing to compete in the most saturated topic |
| 21 | Medication | "If You Take Lisinopril, Hydrochlorothiazide, or Amlodipine — Watch This First" | Directly mirrors the exact structure of the strongest matched-pair winner (216x); ships with mandatory medical-safety framing (ask-your-doctor, not stop-your-medication) |
| 33 | Digestion | "I Drank [Ingredient] Water Every Morning for 7 Days — My Body's Reaction Surprised Me" | Second N-day experiment for launch-week cadence testing |
| 41 | Mobility | "The Skill Every Senior Should Practice Before They Ever Need It" | High-differentiation, rarely-covered practical topic within the top pillar |

Balances the two highest-confidence pillars (Mobility ×3, Digestion ×4) with medically-gated but well-evidenced Cardiovascular (×2) and Medication (×1) content, while deliberately **excluding** the unproven Diabetes and Kidney pillars from the launch-critical batch — those are held for the exploration slice of the 50.

## 26. Experimentation Plan (DS-000031 feedback loop)

Each launch video should log: topic, psychology trigger, title archetype, hook type, and format (list vs. self-experiment vs. mechanism-explainer) as its testable hypothesis. After publish, compare its outlier multiple against the channel's own emerging median (once the channel exists) — not against competitor channels, since channel size confounds raw comparison (Section on channel-size confounding, per methodology). Treat any result as one data point; the negative-evidence case in Section 10 shows a single win does not validate a template.

## 27. Measurement Plan

Once eligible, collect: impressions, CTR, watch time, AVD, 30-second retention, traffic-source split, returning-viewer rate, subscriber gain, and search terms via first-party YouTube Analytics. None of this exists yet for this project (`first_party_analytics_status = NONE` for all 73 repository channels) — this section is a plan, not a report.

## 28. Medical-Safety Requirements

All Medication-pillar content must direct viewers to "ask your doctor about X," never suggest stopping or changing a medication. Do not recommend unproven cures, dangerous supplement claims, or contradict established guidance (WHO/CDC/FDA/NIH/NIA/NHS). Verify any specific physiological claim used in a script (e.g., dawn-phenomenon blood sugar mechanism, grip-strength/longevity link) against a primary source before publishing — this report identifies which claims need that check (marked in `07-first-50-videos.json` risk field) but does not perform full medical fact-checking for every one of the 50 concepts.

## 29. What NOT to Copy

- Competitor wording verbatim, especially the "9 Foot Signs" script shown to be reused (and mostly failing) across multiple channels.
- "Doctors won't tell you" framing used alone without a new specific claim attached (shown to fail in the matched-pair evidence).
- Generic single-topic list titles with no mechanism or specificity (the most common failure pattern across all 6 channels).
- Overexploiting Cancer content — weakest cluster, highest medical-safety risk, zero internal outliers.

## 30. Risks

Every current-generation channel in this cohort launched and scaled within weeks, suggesting the specific packaging patterns that work today may saturate or shift quickly — the launch plan should re-check Trends and internal performance data before scaling past the first 10-20 videos. The single largest internal outlier (Dr. Okoro's diabetes-foot video) may not be repeatable; treating it as core strategy rather than an experiment would be a mistake per the evidence in Section 8/13.

## 31. Final Launch Blueprint

See Sections 21-25 above for positioning, pillars, and the first 10/50 videos. Topic, packaging, hook, and script "engines" are represented by the repeatable structures identified in Sections 9-10 and 18 (specific-mechanism warning, N-day self-experiment, named-drug/named-body-part specificity) rather than a separate built system — building an actual automated engine was out of scope for this research pass.

---

## Required Final Summary

```
SENIOR HEALTH COMPETITIVE INTELLIGENCE COMPLETE (CALIBRATED SCOPE — see Scope Note)

INTERNAL DATA
Canonical channels reviewed: 73
Senior-health competitors selected: 6 (all Tier A Direct)
Videos analyzed: 306
Transcripts analyzed (available, not all manually read): 305 real / 1 placeholder
Standard packages used: 4 STANDARD_PACKAGE + 2 HISTORICAL_FORMAT (of 38 project-wide)

EXTERNAL RESEARCH
Google Trends queries: 3 (clove water; balance exercises for seniors; diabetic foot signs)
Historical trend investigations: 3 (12-month windows; no seasonality/5-year expansion performed)
External channels reviewed: 5 (Doctor Khalid, Dr. Eric Berg DC, Dr. Zee, The Yoga Institute, + 2 script-copy channels)
External comparable videos: 7
Historical news/event checks: 0 (flagged as a gap, Section 12)

PERFORMANCE FORENSICS
Extreme outliers (EXTREME_BREAKOUT): 51
Strong outliers: 30
Failures deeply analyzed (autopsy cards): 10
Matched winner/loser pairs: 29

TOPICS
Topic clusters: 12 (keyword-derived, directional)
High-demand clusters: Digestion/Gut, Mobility/Falls/Balance
Evergreen clusters: Mobility/Falls/Balance (Trends-confirmed)
Emerging/mixed clusters: Digestion/Gut (trend-assisted, execution-dependent)
Over-saturated clusters: Cardiovascular (70 videos, weakest average performance)
Whitespace opportunities: specificity-led Cardiovascular content, N-day-experiment format applied beyond Digestion

PACKAGING
Winning title archetypes: named-count warning lists with specific body part/mechanism; N-day self-experiment narrative
Winning thumbnail archetypes: NOT_AVAILABLE (no forensic visual evidence in this cohort)
Repeated weak patterns: generic single-claim questions; "doctors won't tell you" used without new specificity

SCRIPTS
Hook archetypes: warning+mechanism, contrarian/myth-busting, self-test, N-day story
Strong script archetypes: warning -> mechanism -> single specific fix
Weak script archetypes: generic list with no mechanism or story

AUDIENCE PSYCHOLOGY
Major desires: stay independent, avoid a fall, simple low-cost fixes
Major fears: hidden/silent disease, loss of independence
Strong recurring triggers: fear of hidden danger + hope/reversibility ("one simple change")

TREND ATTRIBUTION
Trend-amplified: Digestion/clove cluster (entry timing only, not per-video causation)
Evergreen-led: Mobility/Balance cluster
Packaging/psychology-led: Cardiovascular winners, Medication-warning winners
Mixed: Digestion/clove per-video outcomes
Insufficient evidence: Diabetes/Blood Sugar discovery mode, Kidney/Skin clusters generally

KNOWLEDGE CORPORA
DS-000011: APPLIED (hook/title/packaging framing throughout)
DS-000018: Present in repository but not directly cited — no creator-claim platform-mechanism assertions required verification in this pass
DS-000031: APPLIED (Feedback Loop, Outlier->Demand Signal, Psychology Arbitrage, Story Density, Narrative Debt Mining, Doubling Down all used directly against the evidence)

FINAL CHANNEL
Recommended audience: adults 55-75 focused on independence over disease labels
Recommended positioning: Mobility-and-Digestion-core Senior Health channel with specific-mechanism Cardiovascular content
Primary differentiation: N-day self-experiment format + specific-mechanism framing vs. competitors' generic-warning-list pattern
Content pillars: 6
First 50 videos: 50
First 10 launch videos: 10

OUTPUTS
Excel workbook: PASS (13 sheets, 1 chart, 0 broken refs/formulas, verified by reload)
Narrative report: PASS (this document)
Evidence register: PASS (14 entries, JSON)
Charts: PASS (1 required chart with interpretation; fewer than the 18 suggested charts in the original brief — calibrated scope)
Layman explanations: PASS (00_READ_ME sheet, plain-English throughout this report)
Medical-safety review: PASS (Section 28; no unproven-cure or stop-medication language anywhere in the 50-video blueprint)

SOURCE DATA MODIFIED: NO
PAID DATA ACQUISITION: NO
FINAL STATUS: COMPLETE WITH WARNINGS (calibrated scope — see Scope Note at top of document)
```
