# Finance & Economics Viral Intelligence — Forensic Database Analysis

Run date: 2026-11-12. Source database: `data/catalog/finance_economics_complete.db` on branch `data/finance-economics-complete-2026-11-11` (commit `933f236e`), read-only copy, SHA-256 `fa6fd1b24d07da39870100168306b99d1e9b84f61831d97a9946ded49b8c9d20` (identical to original). No source records were modified.

Work directory: `~/YIOS-local-audits/finance-viral-forensics-2026-11-12/` (scripts `01_…13_*.py`, intermediates `out/`, deliverables `deliverables/`, thumbnails `thumbs/`, extracted knowledge text `knowledge/`).

Evidence classes used throughout: **Verified** (counted/computed directly), **Observation** (descriptive, unmodelled), **Exploratory** (pattern chosen after looking at data; needs holdout), **Hypothesis**, **Untested**.

---

## 1. Verified inventory (Deliverable 1)

| Item | Reported | Verified | Explanation |
|---|---:|---:|---|
| Channels | 69 | 69 | 1 channel (Wealth Logic) has 0 videos; 24 have no subscriber count; 8 have no `sub_niche` |
| Video records | 3,634 | 3,634 | |
| **Unique videos** | 3,410 | **3,634** | 3,634 distinct video IDs and URLs. **3,410 is not the unique-video count: it is the number of distinct videos that have ≥1 transcript.** 224 videos (6.2%) have no transcript |
| Distinct titles | – | 3,515 | 119 rows are surplus duplicates of a title already present (9 same-channel duplicate groups; others cross-channel, see independence check below) |
| Transcript rows | 3,450 | 3,450 | = 3,410 videos + 40 extra rows from a second source on 29 videos |
| Complete transcripts | – | 3,449 COMPLETE/ASR, 1 PARTIAL | 199 are Whisper-base ASR marked `ASR_UNCERTIFIED`; 29 local Whisper small.en; 2,334 YouTube auto-captions; 173 creator captions; 715 registry-sourced |
| Thumbnail URLs | 3,634 | 3,634 distinct | HTTP 200: **3,576**; HTTP 404: 56; SSL error: 2. 3,089 are recorded as `captured`, **545 are derived `hqdefault` patterns** |
| Shorts / Long-form | – | 222 / 3,412 | `video_type` labels were inconsistent (8 variants); Shorts = labelled Short or ≤60 s |
| Missing publish date | – | 192 (212 are date-only) | |
| Missing views | – | 10 | |
| Date range | – | 2024-08-09 → 2026-11-11 | **94.9% of dated videos are from 2026** (newest ~100 per channel capture) |

Data-quality limits: no per-video collection timestamp is exposed in `videos` (views are a lifetime snapshot at build time, 2026-11-11 or earlier by source); transcripts are **untimed**, so "first 5/10/30 seconds" are approximated by word position (≈2.5 words/s); likes/comments are missing for ~11%.

Files: `01_inventory_verified.csv`, `01_channel_coverage.csv`, `01_duplicate_title_groups.csv`, `01_near_duplicate_scripts.csv`, `01_thumbnail_accessibility.csv`.

**Independence check (AGENTS rule 9).** 73 near-duplicate script pairs (131 videos, Jaccard ≥0.25 on first 400 words), 31 of them cross-channel, concentrated in senior-benefit channels (Kevin Explains↔Housing 8 pairs, Mark Calloway↔Housing 4). These are not independent observations; sensitivity analyses below exclude them. 170 videos share a title with another channel, and 44 of them (26%) are Breakouts vs 13% overall — consistent with channels cloning proven titles (hypothesis; direction not provable from this data).

---

## 2. Method (Deliverables 2–4, 20)

**Scope.** Long-form videos are classified (n=3,412 → 3,056 classifiable across 60 channels). Shorts (n=222) are kept separate; 201 classifiable, summarised only.

**Baseline.** For each video: median views of the 15 temporally nearest *other* long-form videos from the same channel (≥6 comparables; channels with ≥12 eligible videos; videos ≥14 days old). This controls for channel size, channel growth, and publication period together. Undated videos (192) use the channel median (flagged `baseline_method`).

**Performance Index (PI)** = views ÷ baseline. **Relative Performance** = PI × 100.
Classes: **Breakout** PI ≥ 5; **Successful** 2–5; **Average** 0.5–2; **Underperforming** < 0.5. (Thresholds set from the empirical PI distribution: median 0.98, 75th pct 2.11, 90th 6.9.) Result: 398 / 424 / 1,451 / 783, with 356 not classified. Percentile-based sensitivity (top-quartile within channel) was run for headline patterns.

**Inference.** Feature → log(PI) via OLS with **channel-clustered standard errors**; Benjamini-Hochberg FDR within each test family; **per-channel replication** (share of channels where the effect has the claimed sign); matched pairs (same channel, ≤150 days apart, duration ratio 0.6–1.67; 692 Breakout/Successful vs Underperforming pairs in 54 channels) with sign tests; held-out-**channel** prediction (GroupKFold by channel, shuffled-label control). Thumbnails: OpenCV (luminance, saturation, colourfulness, Canny edge density, Haar face detection) and Tesseract OCR on 320×180 copies of 3,577 images; plus visual inspection of three contact sheets (Robin MBA, Alicia Invests, Tom Talks Money; six sheets were generated, three viewed).

**Caveat on proxies.** All hook/title/script features are lexical or regex proxies of the source principles (documented in `02_features.py`, `06_claims.py`). A null result means *no effect detectable with this proxy*, not that the principle is false.

Files: `02_channel_performance_report.csv` (Deliverable 2), `03_unique_video_performance_database.csv`, `04_video_success_classification.csv`, `04_classification_counts.csv`.

---

## 3. Core finding: what explains why videos outperform?

1. **Channel identity dominates absolute views.** Channel alone explains **52.9%** of log-view variance (n=3,402); on the dated subset (n=3,210) channel alone R²=0.435, age alone 0.010, channel+age 0.448 (F07). Median of channel-median views: business/economics explainers **151,880**, wealth-POV 7,227, retirement/senior 5,129, investing/personal finance 1,798 (Kruskal p=0.0004; **confounded with channel scale and age**).
2. **Within a channel, surface wording barely predicts relative performance.** None of 17 title features survives FDR; no hook feature survives FDR; best held-out-channel AUCs: title-surface **0.504**, hook/intro 0.527, script 0.585, all text 0.576, topic-only 0.510 (shuffled-label ≈0.49). Script signal is small and mostly length/evidence density (word count rho 0.071 q=0.003; data-term density rho 0.060 q=0.011; duration rho 0.057 q=0.011).
3. **Topic matters statistically but modestly.** Joint topic effect on log PI p=2.7e-5, R²=0.01.
4. **Thumbnails.** In the inspected channels winners and losers share an identical template. Face presence ratio 1.12 (CI 1.01–1.25, q=0.13, 21/37 channels positive); OCR text amount, brightness, saturation, colourfulness, contrast: null. Only edge density is marginal (rho 0.054, q=0.048).
5. **Same template, wildly different results** (Observation, `14_counterexample_same_title_template.csv`): "If You're Over 60, **X** Will Give You These N Things" — Costco `A4hPtQsiWoA` 569k views (PI 445.6), Aldi `BfOcC1094eo` 348k (PI 158.9), Amazon `L1pvT-arh9g` 4.6k (PI 2.1), Airlines `mRbrwzG4Jow` 0.8k (PI 0.17). Same channel, same thumbnail layout, same title shape. The *subject* (and unobserved distribution factors) separated them, not the packaging template.

**Interpretation (inference, not proof).** In this data, *who published* and *what specific subject* explain far more than hook/title/thumbnail *style*. Style features are too homogeneous within channels, and our proxies too coarse, to isolate CTR-driven effects; CTR/retention data would be required.

---

## 4. Hook, Introduction, Title, Script, Thumbnail intelligence (Deliverables 5–9)

Full tables: `05-09_binary_feature_tests_title_hook_script.csv`, `05-09_continuous_feature_tests.csv`, `08_thumbnail_feature_tests.csv`, `20_claim_tests.csv`.

**Hook (first ≈75 words ≈30 s; n=2,858).** Only "you/your" in the opening is notable: PI ratio **1.16** (CI 1.06–1.27, p=0.002 uncorrected, q=0.052), but positive in only 23/43 channels. Null: question in opening, number, dollar/percent, contrastive "but/however", contrarian wording, stakes words, open-loop phrases, explicit promise, story opening, credibility claim (0.69, CI 0.54–0.89, but 0/4 channels).
**Introduction.** Title-word overlap in first 30 s/150 words (rho 0.009/0.014), promise position (rho 0.015), background markers: null. Sponsor/subscribe plug in first 300 words: null.
**Title.** Opposite to common advice: ≤60 characters **0.89** (CI 0.80–0.99), enhancer words (secret/money/mistake…) **0.86** (0.77–0.95), titles ending in a question **0.79** (0.69–0.90). Numbers, dollar amounts, year, fear/risk words, urgency, named entities, "you", POV: null. Playbook title families 01–05, 09, 10: null (all q ≥0.66).
**Script.** Word count, evidence density, number density: small positive. Open-loop, BUT/THEREFORE, example density, CTA-at-end (0.90, q=0.46): null.

**Unexpected/sub-niche patterns (Exploratory — chosen after viewing top results; not validated on unseen data).** `20_discovered_pattern_tests.csv`:
- **Concrete-entitlement framing ("free", "owes you", "can't take/touch")** in senior content: ratio **2.46** (CI 1.20–5.02; n=60); **2.48** (1.27–4.86) after excluding cross-channel shared titles; breakout rate 33% vs 17%.
- **True deadline/new-rule framing** in senior content: **1.45** (1.06–1.97, p=0.020, n=132); pooled niche 1.30 (1.01–1.67); **no effect in investing** (0.95).
- **Not robust:** "senior formula" (audience-age target + "most miss" gap): 1.69 (p=0.075) with near-duplicates → **1.22 (p=0.38)** without; age-targeting alone 1.36 (1.10–1.69) → 1.18 (0.96–1.46). An earlier "deadline/changes in investing = 1.30" result came from a loose regex and one title shared across two channels; it does not survive a true-deadline definition.
- These patterns widen the tails (higher Breakout rate **and** higher Underperforming rate) more than they move the median; top-quartile rates barely differ.

Total exploratory tests run across families: ≈120; only within-family BH correction was applied.

---

## 5. Topic, audience, cross-channel (Deliverables 10, 11, 15)

- `10_topic_cluster_database.csv`: 18 data-derived clusters (TF-IDF title SVD + KMeans; silhouette 0.15, i.e. weak structure). Highest within-channel median PI: net-worth/POV (1.29, n=114), bank-account/freeze for seniors (1.18, n=95), dividend/ETF math (1.09, n=156). Lowest: Social Security checks (0.75), retirement "afford" (0.78). All cluster median-PI CIs are wide and most include 1.0. Highest absolute views: "explained/bananas" (median 228k) and "economy/world/company" (83k) — channel-scale confounded.
- `11_audience_problem_database.csv`: 11 rule-based audience-problem tags (multi-label on title + first 150 words). Median PI is within 0.77–1.03 for all; **supply share ≠ demand**: ELI5/concept explainers have the lowest supply (6.7%) yet the highest median absolute views (18,106); taxes/IRS and Social Security-changes have high Breakout rates (16–20%) but the *highest* Underperforming rates (34–35%) → high-variance topics.
- `15_*`: sub-niche group differences, subscriber-tier outcomes (Breakout rate 13.6/14.0/15.8/14.6% for <5k/5–20k/20–100k/100k+), per-channel class counts, and per-feature channel replication. Breakouts occur in 53 of 60 channels; top 5 channels hold 24.6% of Breakouts. The four largest explainer channels (Economics Explained, How Money Works, Money & Macro, MonkeyExplains) have 0% Breakouts because their baselines are already high — PI is channel-relative.

---

## 6. Forensics and matched comparison (Deliverables 12–14)

- `12_successful_video_forensics_top60.csv`, `13_underperforming_video_forensics_60.csv`: IDs, titles, baselines, PI, opening 60 words, feature flags. Breakouts typically open with a specific consequence for the viewer ("Your bank made three changes to your checking account and never called you", `oPZjqx_6d1g`); but the same openings occur in underperformers.
- `14_matched_pairs.csv` (692 pairs, 54 channels) and `14_matched_pair_feature_tests.csv`: no feature differs between matched winner/loser after FDR (smallest sign-test p: "you" in title 0.017, losers more often; q=0.28). Counterexample file documents identical templates with PI 0.15–445.
- Class medians (long-form): Breakout duration 1,102 s / 3,050 words; Underperforming 1,051 s / 2,837 words (small difference, consistent with the weak length signal).

---

## 7. Knowledge validation (Deliverables 16–19)

Matrices: `19_combined_knowledge_validation_matrix.csv` (all rows), `16_ds000011_validation.csv`, `17_ds000018_validation.csv`, `18_global_playbook_validation.csv`.

Totals (n=51 rows): **Supported 3** (duration relationship, evidence-density, outliers occur at all subscriber tiers), **Contradicted 3** (title ≤60 chars, enhancer words, monotonic Viral-Checklist "more boxes = higher odds"), **Mixed 35** (mostly "no detectable effect" — 11 where the point estimate is in the opposite direction), **Untested 10** (CTR/retention/first-10-seconds/algorithm-pipeline/48-hour/Shorts/algorithm-change).

Notes that must travel with these results:
- **DS-000011** is a mixed collection of SOPs, AI-prompt sets and chat-summaries (e.g. the BUT/THEREFORE file is an assistant's absorption summary of a mind-map; Hook guide is a transcript analysis of one creator video plus comments). Principles were taken *as stated* and operationalised with proxies.
- **DS-000018** is a 63-tab Google-Docs snapshot of creator videos about the 2026 algorithm; tab 39 is an interview with YouTube's senior director of growth & discovery, the rest are third-party creators' claims. The dataset **cannot** test a platform-wide change: no impressions/CTR/retention, no pre/post panel, no update date, 94.9% of videos from 2026. One third-party quantitative claim could be compared (tab 35: question-ending titles ≈0.82× lift): our estimate is **0.79 (0.69–0.90)** — same direction and similar magnitude, but only 6/12 channels replicate, and the populations differ (that creator's "4M videos" cross-niche).
- **Playbook** (556 pages): only the Outlier Concept (Module 2.1) and the 100-Title-Formats families were testable. Outlier Ratio (views/subs) agrees with own-baseline PI (rho 0.62, n=2,449; 87 of 101 videos ≥10× are Breakouts), so as a **screening rule it is supported**; the clause that outliers are driven "by topic and packaging, not the channel" is **contradicted in magnitude** (channel explains ~44–53% of log-view variance).

**What this means for the knowledge base (inference):** most surface-level packaging/hook rules are *not detectable* as within-channel discriminators in this niche; this is not evidence that they never matter (no CTR/retention data; homogeneous templates; lexical proxies).

---

## 8. Statistical analysis & prediction (Deliverables 20, 23)

`20_*`, `23_predictive_analysis.csv`. Held-out-channel prediction of Breakout/Successful vs Underperforming (n=1,605; 822 positives; 5-fold GroupKFold):

| Features | AUC (unseen channels) | Shuffled-label AUC |
|---|---:|---:|
| Title surface | 0.504 | 0.494 |
| Hook/intro | 0.527 | 0.484 |
| Script | 0.585 | 0.494 |
| All text | 0.576 | 0.488 |
| Topic only | 0.510 | 0.476 |
| All text + topic | 0.577 | 0.487 |

**Prediction is not supported at a useful level (AUC ≤0.59). No expected view ranges are offered as forecasts.**

---

## 9. External research (Deliverable 21) — NOT EXECUTED

VidIQ, Google Trends US, and live YouTube checks were not run. Blockers: VidIQ metrics require the owner's logged-in account/session; Google Trends historical windows were not collected. The only external verification performed was the HTTP status check of thumbnail URLs (2026-11-12). Every "external demand evidence" field in the opportunity database is `NOT COLLECTED`. Missing input to continue: owner approval/session for VidIQ and a browser pass on the five opportunity topics.

---

## 10. Opportunities (Deliverable 22) — ranked by evidence strength

`22_content_opportunity_database.csv` (title/thumbnail/hook concepts, example IDs, competition from DB only, experiments).

1. Concrete-entitlement framing for seniors (2.5×, n≈58–60; Low-Moderate)
2. True deadline/new-rule framing for senior content (1.45×; Low-Moderate)
3. Bank-account rules/freeze topic (descriptive; Low)
4. "Real math"/life-stage money pivots (cross-channel title repeats, not independent; Low)
5. Company/macro ELI5 explainers (highest absolute views, scale-confounded; Low)

None of these is a promise of performance; all are post-hoc and need holdout experiments.

---

## 11. Research limitations (Deliverable 24)

- No CTR, impressions, retention, traffic source, or historical snapshots; no velocity claims.
- Capture = newest ~100 per channel (+ top-ups): selection and recency bias; 94.9% from 2026; views snapshot dates not recorded per video.
- Proxies are regex-level; transcripts untimed (word-position approximation); caption provenance mixed (auto, creator, registry, Whisper-base ASR uncertified); stylistic punctuation varies by source.
- Near-duplicate scripts and cross-channel title copying violate independence (flagged, sensitivity-tested).
- PI is channel-relative: it cannot rank large vs small channels or reveal channel-level demand.
- Group labels (`sub_niche` → 4 groups) derived by keyword rules; 8 channels with null `sub_niche` were assigned by channel name (analyst judgement). 24 channels lack subscribers.
- Thumbnails: low-resolution copies; OCR and face detection approximate (AI-illustrated faces often undetected); only three of six contact sheets viewed by the analyst; 545 URLs are derived patterns, not captured evidence.
- Exploratory pattern tests (~120 incl. post-hoc); only within-family FDR.
- **Source coverage:** all 17 DS-000011 files and the playbook PDF were extracted to text. Fully read: Packaging SOP, Viral Checklist, Intro Analyzer, Script Analyzer, BUT/THEREFORE. Partially read: Hook guide (~first 150 lines + comment summary), SEO checklist (title and keyword sections), "new YT algorithms updates" (keyword scan only), Title Analyzer (not read in full). **Not read in depth:** "YouTube algorithm guide" (379 KB), Seven-Engine, Renae Blueprint, personality-lens, prompt guides. DS-000018: read tabs 35, 39 (partially), 40, 54; remaining 59 tabs scanned by keyword only. Playbook: TOC, Module 2.1, title-formats intro and families 01–02 read; the rest keyword-scanned. Principles outside this read coverage are not represented in the matrix.

---

## 12. Future experiment plan (Deliverable 25)

1. **Holdout confirmation** of the two surviving patterns (entitlement, true deadline) on channels/periods not used here; pre-register thresholds.
2. **Subject-recognisability test** in a fixed template (Costco/Aldi vs Airlines/Amazon finding).
3. **Collect first-party or time-series data**: weekly view snapshots for 30 days on a sample of 300 videos to enable velocity and decay analysis; impressions/CTR/retention for own-channel videos (the repo's READY file-based Analytics ingestion).
4. **Human-coded hook/title labels** on ~600 stratified videos to replace regex proxies.
5. **Thumbnail A/B** on owned channel with controlled topic.
6. **Title-clone provenance** check for the 170 shared-title videos.
7. **External demand pass** (VidIQ + Google Trends US) for the five opportunities.
8. Transcript timing: re-pull timed captions for the 3,410 videos to measure true first-5/10/30-second structure.

---

## 13. Deliverable index

| # | Deliverable | File |
|---|---|---|
| 1 | Inventory | §1; `01_*` |
| 2 | 69-channel report | `02_channel_performance_report.csv`, `15_channel_class_counts.csv` |
| 3 | Unique video DB | `03_unique_video_performance_database.csv` |
| 4 | Success classification | `04_*` |
| 5–9 | Hook, intro, title, thumbnail, script | §4; `05-09_*`, `08_*`, `20_claim_tests.csv`, `18_playbook_title_family_tests.csv` |
| 10 | Topic clusters | `10_topic_cluster_database.csv` |
| 11 | Audience problems | `11_*` |
| 12–14 | Forensics, matched comparison | `12_*`, `13_*`, `14_*` |
| 15 | Cross-channel | `15_*` |
| 16–19 | Validation | `16_*`, `17_*`, `18_*`, `19_*` |
| 20 | Statistics | `20_*`, §3, §8 |
| 21 | External research | **not executed** (§9) |
| 22 | Opportunities | `22_content_opportunity_database.csv` |
| 23 | Prediction | `23_predictive_analysis.csv` |
| 24–26 | Limitations, plan, executive summary | §11, §12, `EXECUTIVE_SUMMARY.md` |
| 27 | Evidence ledger | `27_evidence_ledger.csv` |
