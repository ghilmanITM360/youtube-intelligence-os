# CH-000003 Topic Opportunity Intelligence Pilot

**Status:** Complete

**Pilot date:** 2026-09-09

**Public-metric cutoff:** 2026-08-28T12:06:34.708Z

**Evidence layers:** `INTERNAL_CANONICAL_EVIDENCE`, `DERIVED_OBSERVATION`, `HYPOTHESIS`, `EXTERNAL_WEB_VALIDATION`, `FINAL_OPPORTUNITY`

## Executive Summary

This pilot tests one narrow capability: use registered channel evidence to find topic opportunities, then validate only the strongest hypotheses against current public evidence. Internal evidence is frozen below before web research. External evidence does not overwrite the canonical corpus.

## Scope

- Channel: `CH-000003`, Dr. Aliza Wright | Advice (`@Dr.AlizaWrightAdvice`)
- Source dataset: `DS-000006`
- Acquisition run: `APIFYRUN-000001`; Actor run `bD7JBsuj7LK5Wt2rk`; registration run `RUN-000018`
- Canonical videos: 32 of 32 accounted for
- Canonical transcripts: 32 of 32 available, 93,911 words total
- Formats: 32 long-form, 0 Shorts, 0 live
- Excluded: private analytics, packaging generation, medical-advice generation, automated scraping, API acquisition, and cross-channel generalization

## Evidence Base

### INTERNAL_CANONICAL_EVIDENCE

The read-only report loads `videos`, the `DS-000006` `video_snapshots`, active topic/format classifications, transcripts, and source-file references from `data/catalog/youtube_inventory.db`. All 32 rows share the same public-metric cutoff. The source manifest records Tier A controlled acquisition.

Canonical item IDs: `VID-000160` through `VID-000191`, inclusive. The reporting script requires exactly 32 unique IDs and requires its derived family map to match that exact set.

### DERIVED_OBSERVATION

All metrics, family assignments, outlier flags, and transcript-pattern summaries in this document are derived observations. They are not YouTube ranking facts.

### HYPOTHESIS

Candidate opportunities are hypotheses until current web validation and final evidence review are complete.

## Data Availability / Limitations

Available public metrics: views, likes, comments, duration, publish time, observation time, and derived age. Derived ratios use only these fields.

Unavailable: impressions, click-through rate, retention, watch time, subscriber conversion, traffic sources, unique viewers, returning viewers, viewer demographics, and private audience overlap. No unavailable metric is estimated or proxied. Likes and comments are weak interaction signals, not satisfaction measures. All items are long-form, so this corpus cannot support a cross-format performance comparison.

## Channel Profile

- Upload window: 2026-06-05 through 2026-07-25
- Upload chronology: 31 intervals across 32 uploads; median gap 1.0434 days, mean 1.5896, range 0.3480–4.2767 days
- Age at cutoff: 34.42–83.69 days; median 61.19 days
- Duration: 491–1,402 seconds; median 1,098 seconds
- Views: 31–219,009; median 217
- Likes: 0–7,100; median 6
- Comments: 0–930; median 2
- Canonical topic mix: `CARDIOVASCULAR_HEALTH` 24, `HEALTHY_AGING` 6, `METABOLIC_HEALTH` 2
- Transcript length: 1,334–3,832 words; median 2,937

## Performance Normalization

For each item:

1. `age_days = max(1, metric_cutoff - published_at)`
2. `views_per_day = views / age_days`
3. `channel_median_ratio = views_per_day / channel median views_per_day`
4. `family_median_ratio = views_per_day / derived-family median views_per_day`
5. `like_rate = likes / views` and `comment_rate = comments / views` when views are nonzero

Channel median is 3.4019 views/day; quartiles are 2.3761, 3.4019, and 7.6353. Robust channel outliers use 1.5-IQR Tukey fences on `log1p(views_per_day)`. This transformation limits leverage from extreme values while preserving order. No composite or “algorithm score” is used.

## Topic Families

These channel-specific families refine, but do not replace, the canonical three-topic vocabulary.

| Derived family | Videos | Median views/day | Mean title-token Jaccard | Strongest | Weakest | Repeatability observation |
|---|---:|---:|---:|---|---|---|
| BLOOD_PRESSURE_MEDICATION_SAFETY | 16 | 3.1305 | 0.1868 | VID-000187 | VID-000169 | Dense coverage but one extreme winner; typical follow-ups remain near baseline |
| BLOOD_PRESSURE_LIFESTYLE_HOME | 4 | 2.8509 | 0.2079 | VID-000172 | VID-000171 | Repeated coverage without a positive channel outlier |
| CARDIAC_WARNING_SELF_TESTS | 3 | 2.1684 | 0.1849 | VID-000170 | VID-000161 | Low family median; prediction/test wording carries factual risk |
| FUNCTIONAL_AGING_SELF_ASSESSMENT | 3 | 18.8284 | 0.1555 | VID-000182 | VID-000176 | Two items materially above channel median; one near baseline |
| MOBILITY_GAIT_FALL_PREVENTION | 3 | 315.4202 | 0.1311 | VID-000162 | VID-000185 | Strongest repeated family: two statistical outliers plus a newer item at 7.09× channel median |
| METABOLIC_DIABETES | 2 | 5.7672 | 0.0000 | VID-000173 | VID-000184 | Above channel median, but sample too small for repeatability claims |
| FOOD_SAFETY_LONGEVITY | 1 | 3.3667 | n/a | VID-000160 | VID-000160 | Single item; no repeatability evidence |

Mean pairwise Jaccard over normalized title tokens is a transparent lexical proxy for semantic cohesion, not an embedding or proof of audience equivalence. Low scores show that derived families depend on reviewed title/transcript meaning rather than copied wording. Family membership and full item metrics are reproducible with `scripts/report_topic_opportunity_pilot.py`.

## Outlier Analysis

### Positive statistical outliers

| Video | Views | Views/day | Channel median ratio | Family median ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| VID-000162 | 219,009 | 3,495.4296 | 1,027.49× | 11.08× | Exceptional mobility/gait result and family leader |
| VID-000187 | 47,032 | 613.1131 | 180.23× | 195.85× | Medication-safety anomaly; not repeated across 15 family peers |
| VID-000163 | 20,701 | 315.4202 | 92.72× | 1.00× | Second independent mobility/gait outlier |

### Negative performance

No item falls below the formal lower Tukey fence. Therefore this pilot reports no negative *statistical* outlier. Lowest relative performers are `VID-000169` (0.4508 views/day), `VID-000161` (0.8344), `VID-000171` (0.9043), and `VID-000186` (1.2556). They are negative relative performers, not statistical anomalies.

### Recent acceleration candidates

At one cutoff, true acceleration cannot be measured. Newer items with above-median velocity are only candidates: `VID-000179` (12.2620 views/day), `VID-000182` (21.8738), and `VID-000185` (24.1225). A later snapshot is required to confirm acceleration.

## Repeated Winning Patterns

1. Mobility, gait, and functional independence after 70 repeat across `VID-000162`, `VID-000163`, and `VID-000185`; the first two are robust outliers and the third remains 7.09× channel median.
2. Functional self-assessment has repeatable above-median evidence in `VID-000166` and `VID-000182`, while `VID-000176` is counter-evidence.
3. Blood-pressure medication safety has one huge success (`VID-000187`) but a 16-item family median below channel median. This is a one-off viral anomaly until repeated.
4. Medication timing shows moderate recent strength (`VID-000179`, `VID-000181`, `VID-000175`) but no statistical outlier and heavy internal repetition.

## Transcript-Derived Topic Patterns

Review of all 32 canonical transcripts found recurring topic-discovery signals:

- Audience identity: “after 60,” “after 70,” seniors, and older adults recur across nearly the full corpus.
- Viewer problems: walking instability, balance, falls, heavy legs, standing from a chair, medication side effects, blood-pressure control, kidney concerns, and diabetes decisions.
- Framing: symptom/problem questions, warning/prevention, list/count structures, time-of-day risk, age-specific functional decline, and “simple change/test” angles.
- Entities: amlodipine, losartan, lisinopril, metoprolol, beta blockers, calcium-channel blockers, blood pressure, kidney function, walking, balance, gait, falls, metformin, insulin, and food choices.
- Repetition risk: medication-name clusters and “doctors won’t tell you” framing recur far more often than their family-level performance supports.

These observations describe topic/angle recurrence only. They do not instantiate title, hook, or script intelligence.

## Internal Candidate Pool

This pool was frozen before web research. Confidence is internal-only.

| Candidate | Topic and angle | Internal evidence / supporting videos | Performance signal | Coverage | Why it may be an opportunity | Initial confidence |
|---|---|---|---|---|---|---|
| CAND-01 | Balance recovery and safer turning after 70 | Mobility family; VID-000162, VID-000163, VID-000185 | Repeated winning family; median 315.42 views/day | Under-covered sub-angle | Extends strongest repeatable problem cluster beyond generic walking | HIGH |
| CAND-02 | Foot clearance, gait change, and trip prevention | VID-000162, VID-000163 | Two robust positive outliers | No direct dedicated item | Specific adjacent mechanism inside proven family | HIGH |
| CAND-03 | Heavy legs: mobility problem versus warning sign | VID-000185, VID-000163 | VID-000185 at 7.09× channel median | One direct item | Follow-up can clarify distinct causes without claiming diagnosis | HIGH |
| CAND-04 | Practical functional-mobility checks for older adults | VID-000182, VID-000166, VID-000176, VID-000162 | Two above-median items; one counterexample | Partial | Connects self-assessment interest to strongest mobility family | HIGH |
| CAND-05 | Blood-pressure medicines, dizziness, and fall risk | VID-000187 plus mobility family | Bridges one medication outlier with repeated mobility success | No dedicated bridge item | Strong channel fit and audience-problem adjacency | HIGH |
| CAND-06 | Individualized blood-pressure pill timing and adherence | VID-000179, VID-000181, VID-000175 | 12.26, 8.27, 5.63 views/day | Repeated, dense | Moderate repeatability but high saturation risk | MEDIUM |
| CAND-07 | Accurate home blood-pressure measurement | VID-000172, VID-000168, VID-000171, VID-000188 | Family median 2.85 views/day; mixed | Partial | Evergreen practical problem; current angle may be more useful than generic mistakes | MEDIUM |
| CAND-08 | Medication side effects by class, with clear escalation boundaries | VID-000187, VID-000174, VID-000183 | One extreme outlier; follow-ups typical | Dense generic coverage | Safer specificity may improve usefulness, but one-off risk is high | MEDIUM |
| CAND-09 | Kidney monitoring questions for seniors taking BP medicine | VID-000183, VID-000187 | Direct item at 0.87× channel median | One weak direct item | Potential factual freshness and follow-up gap | LOW |
| CAND-10 | Diabetes medicines and hypoglycemia risk in older adults | VID-000184, VID-000173 | Family median 5.77 views/day | Only two items | Above-median small family; important audience-specific problem | MEDIUM |
| CAND-11 | Older-adult food choices spanning diabetes and blood pressure | VID-000173, VID-000189 | Both above/near family medians; neither outlier | Sparse | Adjacent metabolic/cardio audience problem | LOW |
| CAND-12 | Heart-attack warning signs versus unreliable self-tests | VID-000170, VID-000161, VID-000188 | Family median 2.17 views/day | Three weak items | Could replace overclaiming with safer education, but channel demand is weak | LOW |
| CAND-13 | Food handling and reheating safety for older adults | VID-000160 | 0.99× channel median | One item | Audience-specific safety gap possible, but no internal repeatability | LOW |

## Web Validation Method

After the 13-candidate internal pool was frozen, eight candidates (`CAND-01` through `CAND-07`, plus `CAND-10`) were checked on 2026-09-09. Searches were candidate-specific. Official health sources determine factual freshness; public video/search results inform only qualitative saturation and gap assessment. Search-result absence is weak evidence, not proof of no competition. No page was scraped or added to the canonical corpus.

External sources used:

- [E1 — NIA: Falls and fractures in older adults](https://www.nia.nih.gov/health/falls-and-falls-prevention/falls-and-fractures-older-adults-causes-and-prevention): gait, balance, postural hypotension, medication effects, and fall prevention.
- [E2 — CDC STEADI clinical resources](https://www.cdc.gov/steadi/hcp/clinical-resources/index.html): current functional assessments for chair stand, balance, mobility, and orthostatic blood pressure.
- [E3 — NIA: Older adults and balance problems](https://www.nia.nih.gov/health/balance-problems-and-disorders): balance/dizziness causes and independence context.
- [E4 — NHLBI: Peripheral artery disease symptoms](https://www.nhlbi.nih.gov/health/peripheral-artery-disease/symptoms): exertional leg heaviness, weakness, numbness, and escalation context.
- [E5 — American Heart Association: Blood pressure explained](https://www.heart.org/en/health-topics/high-blood-pressure/blood-pressure-explained): current home measurement technique and repeated-reading guidance.
- [E6 — 2025 AHA/ACC blood-pressure update](https://international.heart.org/en/news-and-events/2025/august-high-blood-pressure): fresh hypertension-management context and home-monitoring guidance.
- [E7 — BedMed randomized clinical trial](https://pubmed.ncbi.nlm.nih.gov/40354045/): no cardiovascular advantage for bedtime versus morning dosing; timing should reflect preferences and tolerability.
- [E8 — NIDDK: Low blood glucose](https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/low-blood-glucose-hypoglycemia.): adults 65+ and users of insulin or some other medicines have elevated hypoglycemia risk.
- [E9 — CDC: Low blood sugar](https://www.cdc.gov/diabetes/about/low-blood-sugar-hypoglycemia.html): current symptom and unawareness context.
- [E10 — CDC: Medicines risk fact sheet](https://www.cdc.gov/older-adult-drivers/medicine/index.html): current medication-side-effect and fall-risk context.
- [E11 — Current public fall-prevention result](https://www.youtube.com/watch?v=jfqohbop3Xk): a high-view generic senior circulation/exercise example, used only as saturation evidence.
- [E12 — Current public chair-stand result](https://www.youtube.com/watch?v=KIXzy6tqQS8): an existing senior chair-test example, used only as saturation evidence.
- [E13 — Current public blood-pressure timing result](https://www.youtube.com/watch?v=Ula_-vwiaKQ): recent high-claim timing/fall framing, used only as saturation and quality-risk evidence.
- [E14 — NIDDK diabetes video inventory](https://www.niddk.nih.gov/health-information/professionals/diabetes-discoveries-practice/top-videos-health-professionals): existing older-adult diabetes video coverage, used as market/staleness context.

## Candidate Validation

| Candidate | Freshness / demand | Saturation / gap | Factual boundary | Gap classification | Decision |
|---|---|---|---|---|---|
| CAND-01 | Falls, balance, gait, and independence remain active NIA/CDC priorities [E1–E3] | Generic balance exercise is crowded; turning and obstacle recovery are less directly served in reviewed results | Avoid unsupervised prescriptive exercise for high-risk viewers | UNDERCOVERED_ANGLE; AUDIENCE_SPECIFIC_GAP | Advance as OP-001 |
| CAND-02 | Foot and gait problems are recognized fall factors [E1] | Exact foot-clearance demand was not established; overlaps CAND-01 | Do not imply a single gait correction prevents falls | INSUFFICIENT_EVIDENCE; UNDERCOVERED_ANGLE | Merge evidence into OP-001; not standalone |
| CAND-03 | NHLBI describes exertional leg heaviness as one possible PAD symptom [E4] | Generic “circulation exercise” content is established [E11]; cause-versus-warning differentiation remains useful | Never diagnose PAD from heaviness; include urgent/routine-care boundaries | UNDERCOVERED_ANGLE; FOLLOW_UP_GAP | Advance as OP-002 |
| CAND-04 | CDC currently publishes three distinct functional assessments [E2]; public interest in mobility tests remains current | Chair-stand content exists [E12], so a single “longevity test” is saturated and overclaims; a safety-bounded comparison is narrower | Tests screen different domains and do not predict individual lifespan | UNDERCOVERED_ANGLE; FOLLOW_UP_GAP | Advance as OP-003 |
| CAND-05 | NIA and CDC connect medication effects, dizziness/postural hypotension, and falls [E1, E2, E10] | Medication danger content exists, often with drug-level overclaims; symptom-to-medication-review boundaries are less visible | Do not tell viewers to stop, switch, or retime medicine | AUDIENCE_SPECIFIC_GAP; UNDERCOVERED_ANGLE | Advance as OP-004 |
| CAND-06 | BedMed is recent and directly relevant [E7] | Recent public videos repeat “dangerous time” claims [E13]; internal family already has three timing videos | No universal best time; adherence, drug class, preferences, and clinician advice matter | SATURATED_NO_GAP | Reject |
| CAND-07 | 2025 AHA guidance renews home-monitoring relevance [E5, E6] | Generic mistake/technique coverage is dense; internal family is below channel median | One reading is a snapshot; no diagnosis from one home result | SATURATED_NO_GAP; FOLLOW_UP_GAP | Keep as reserve, not top five |
| CAND-10 | NIDDK and CDC identify older age and insulin/some medicines as hypoglycemia risk factors [E8, E9] | Existing institutional video coverage is present but much is older/general [E14]; channel has only two metabolic items | Avoid individualized medication adjustment; separate recognition from treatment advice | AUDIENCE_SPECIFIC_GAP; STALE_COVERAGE | Advance as OP-005 |

### Transparent opportunity assessment

No dimensions are combined into a hidden score.

| Final opportunity | Internal performance | Repeatability | Channel fit | Coverage gap | Current relevance | Saturation risk | Evidence quality |
|---|---|---|---|---|---|---|---|
| OP-001 | HIGH | HIGH | HIGH | HIGH | HIGH | MEDIUM | HIGH |
| OP-002 | HIGH | MEDIUM | HIGH | HIGH | HIGH | MEDIUM | HIGH |
| OP-003 | HIGH | MEDIUM | HIGH | MEDIUM | HIGH | HIGH | HIGH |
| OP-004 | HIGH | MEDIUM | HIGH | HIGH | HIGH | HIGH | HIGH |
| OP-005 | MEDIUM | LOW | MEDIUM | HIGH | HIGH | MEDIUM | HIGH |

## Final Top 5 Opportunities

### OP-001 — Dynamic balance during turns and everyday obstacles after 70

- **Specific angle:** Explain why turning, changing direction, and clearing ordinary obstacles can expose balance problems, with safe assessment/referral boundaries rather than a generic exercise list.
- **Why this channel:** Mobility/gait is the strongest repeatable family.
- **Internal evidence:** `VID-000162`, `VID-000163`, `VID-000185`; 3-item family median 315.4202 views/day. `VID-000162` and `VID-000163` are robust positive outliers; `VID-000185` is 7.09× channel median.
- **External validation:** NIA identifies gait/balance problems as fall risks [E1, E3]; CDC uses mobility and balance assessments [E2]. Generic balance exercise is saturated, but reviewed results offered less direct turning/obstacle framing.
- **Why now:** Current CDC/NIA material keeps fall prevention active, while the channel has not directly covered this sub-angle.
- **Gap type:** `UNDERCOVERED_ANGLE`, `AUDIENCE_SPECIFIC_GAP`.
- **Risks / counter-evidence:** Generic senior balance content is crowded; no private audience data confirms demand; unsafe demonstrations could harm high-risk viewers.
- **Confidence:** HIGH.
- **Falsification:** A new comparable snapshot shows the mobility family reverting to channel median, or current YouTube Trends/private search data shows low audience interest and no content gap for turning/obstacle problems.

### OP-002 — Heavy legs after 70: movement limitation versus vascular warning pattern

- **Specific angle:** Distinguish common functional complaints from patterns that warrant clinical review, without diagnosing a cause.
- **Why this channel:** It follows a newer above-median mobility item while connecting established cardiovascular identity.
- **Internal evidence:** `VID-000185`, `VID-000163`, `VID-000162`; `VID-000185` reached 24.1225 views/day, 7.09× channel median, within the strongest repeatable family.
- **External validation:** NHLBI says exertional leg heaviness can occur with PAD and lists other warning patterns [E4]. A large generic circulation/exercise video [E11] demonstrates saturation around remedies, leaving a differentiation/safety gap.
- **Why now:** One direct channel item shows traction; authoritative context supports a careful follow-up before the signal becomes stale.
- **Gap type:** `FOLLOW_UP_GAP`, `UNDERCOVERED_ANGLE`.
- **Risks / counter-evidence:** One direct internal item; many possible causes; “circulation” content is saturated and prone to medical overclaiming.
- **Confidence:** MEDIUM.
- **Falsification:** Follow-up mobility snapshots do not sustain above-median velocity, or reviewed market results show recent high-quality cause-versus-warning coverage already dominates this angle.

### OP-003 — What different senior mobility checks can and cannot tell you

- **Specific angle:** Compare chair stand, balance stance, and timed mobility as distinct screening concepts, emphasizing limits and safety rather than lifespan prediction.
- **Why this channel:** Functional self-assessment repeats above baseline and naturally connects to mobility winners.
- **Internal evidence:** `VID-000182`, `VID-000166`, `VID-000176`, `VID-000162`; functional-family median 18.8284 views/day. `VID-000182` is 6.43× channel median and `VID-000166` is 5.53×; `VID-000176` near median is counter-evidence.
- **External validation:** CDC separately documents chair-stand, 4-stage balance, and Timed Up and Go assessments [E2]. Existing chair-test video coverage [E12] shows saturation for the generic test, supporting a limits/comparison gap.
- **Why now:** Current public interest in mobility self-tests is rising, while the channel’s prior “predicts how long you’ll live” framing needs a safer adjacent direction.
- **Gap type:** `UNDERCOVERED_ANGLE`, `FOLLOW_UP_GAP`.
- **Risks / counter-evidence:** High saturation; formal tests belong in clinical settings; one family item underperformed.
- **Confidence:** MEDIUM.
- **Falsification:** Audience/search data shows no interest beyond single-test novelty, or a new video using careful multi-test framing performs below channel median despite comparable exposure.

### OP-004 — Blood-pressure medicines, dizziness on standing, and fall-risk review after 60

- **Specific angle:** Help viewers recognize when dizziness or wobbliness should trigger blood-pressure measurement and a clinician/pharmacist medication review; no stop/switch advice.
- **Why this channel:** It bridges the channel’s dominant medication coverage with its proven mobility/fall audience problem.
- **Internal evidence:** `VID-000187`, `VID-000179`, `VID-000183`, plus `VID-000162`/`VID-000163`; `VID-000187` is a 613.1131 views/day outlier, but the 16-item medication-family median is only 3.1305, so the opportunity depends on the bridge angle, not generic medication repetition.
- **External validation:** NIA links postural hypotension and medication side effects to falls [E1]; CDC provides orthostatic measurement and medication-risk resources [E2, E10]. Current drug-danger content demonstrates demand and high saturation/quality risk.
- **Why now:** Authoritative medication/fall resources are current, and internal evidence has not directly joined these two audience problems.
- **Gap type:** `AUDIENCE_SPECIFIC_GAP`, `UNDERCOVERED_ANGLE`.
- **Risks / counter-evidence:** Medication family is dominated by one anomaly; individualized medical factors are essential; current market has many sensational claims.
- **Confidence:** MEDIUM.
- **Falsification:** A dedicated bridge item cannot exceed the medication-family median, or private analytics show the medication outlier drew viewers with no mobility/fall overlap.

### OP-005 — Hypoglycemia signs older adults may miss while using insulin or certain diabetes medicines

- **Specific angle:** Recognition and clinician-review boundaries for older adults, including dizziness/confusion and why symptoms may be missed; no medication adjustment.
- **Why this channel:** It tests a sparse but above-median metabolic family while retaining the channel’s senior medication-safety fit.
- **Internal evidence:** `VID-000173`, `VID-000184`; 2-item family median 5.7672 views/day, above channel median, but too small for a repeatability claim.
- **External validation:** NIDDK identifies age 65+ and insulin/some other medicines as risk factors [E8]; CDC documents symptoms and hypoglycemia unawareness [E9]. Existing institutional video coverage is available but often older/general [E14].
- **Why now:** Strong authoritative relevance plus sparse internal coverage creates a controlled diversification test.
- **Gap type:** `AUDIENCE_SPECIFIC_GAP`, `STALE_COVERAGE`.
- **Risks / counter-evidence:** Only two internal videos; lower channel fit than mobility/cardio; acute-care guidance demands careful clinical review.
- **Confidence:** MEDIUM.
- **Falsification:** A comparable diabetes-safety item remains below channel median, or current Trends/private audience data shows little interest among this channel’s viewers.

## Rejected / Weak Opportunities

- `CAND-02` was merged into OP-001 because standalone demand evidence was weak and overlap was high.
- `CAND-06` was rejected: three internal timing videos already exist, recent public content is saturated with “dangerous time” claims, and BedMed does not support a universal morning/bedtime advantage [E7].
- `CAND-07` remains a reserve: official guidance is fresh, but generic technique content is dense and the internal family median is below channel median.
- `CAND-08` and `CAND-09` were not promoted because one medication outlier does not validate broad class-by-class repetition, and the kidney item underperformed.
- `CAND-11` lacks a repeatable internal family signal.
- `CAND-12` has a low family median and high overclaim risk around “predicts a heart attack.”
- `CAND-13` is a one-item, near-median hypothesis with sensational cancer framing and no repeatability evidence.

## Confidence & Limitations

Overall confidence is MEDIUM. Internal limitations: one public snapshot, 32 videos from one channel, all long-form, missing private analytics, no causal inference, and medically sensitive topics requiring expert review. Public search results are personalized, incomplete, and unsuitable for precise saturation counts. No result proves future performance. Candidate confidence must be recalibrated after a later metric snapshot and, when available, channel-owned Analytics/Trends evidence.

## Safe Platform Guardrails Used

DS-000018 is `MIXED_RELIABILITY`; this pilot uses only its bounded safe knowledge and creator-heuristic guardrails:

- Recommendations are personalized and surface-dependent; this report does not infer Home, Up Next, Search, or Shorts-feed behavior from public views.
- Appeal, engagement, and satisfaction are distinct. Public views, likes, and comments do not collapse them into one score.
- No universal ranking metric, ideal duration, cadence, CTR target, retention target, or hidden weight is asserted.
- Genuine content gaps and breakout examples can inspire hypotheses, but copying does not guarantee results.
- All items are long-form; no cross-format behavior is inferred.
- Policy and medical-quality concerns are not encoded as recommendation suppression.

## Pilot Evaluation

**Raw-view baseline:** the five highest-view videos are `VID-000162`, `VID-000187`, `VID-000163`, `VID-000166`, and `VID-000185`. This already reveals that mobility matters, so the pilot does not claim to discover that fact from nothing.

**Added intelligence:** normalization reverses `VID-000166`/`VID-000185` because the newer mobility item has higher velocity; family grouping shows mobility repeats while the #2 raw-view medication result is a one-off inside a 16-item near-baseline family; external review rejects the saturated timing angle despite moderate internal velocity; gap analysis exposes the mobility/cardio bridge and older-adult diabetes safety, neither obtainable from raw-view sorting alone.

**False positives avoided:** generic medication repetition from one viral item; a universal “dangerous” pill time; heart-attack prediction tests; lifespan claims from one chair test; and food/cancer repetition from one near-median item.

**Verdict:** PASS. The pilot adds meaningful but bounded value beyond sorting: repeatability, age context, adjacent gaps, factual freshness, saturation risk, counter-evidence, and falsification conditions. Missing impressions, retention, traffic sources, and audience overlap prevent causal or packaging conclusions.

## Next System Capability

Capture a later read-only public metric snapshot for CH-000003 and evaluate whether OP-001 through OP-005 signals persist. If channel-owned Analytics becomes available, validate traffic-source, retention, and audience-overlap assumptions before any packaging intelligence. Do not begin title, thumbnail, hook, or script intelligence automatically.
