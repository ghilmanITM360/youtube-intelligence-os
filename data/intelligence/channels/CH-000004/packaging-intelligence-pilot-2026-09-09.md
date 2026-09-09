# CH-000004 Packaging Intelligence Pilot

## Scope

All 83 canonical CH-000004 titles are analyzed against the committed Topic Intelligence snapshot. The five opportunities are loaded unchanged from the web-validation artifact. Output separates historical observations from generated package hypotheses. No Hook or Script Intelligence was started.

## Evidence Availability

- Canonical items/titles/transcripts: **83/83**.
- Registered thumbnail URLs: **83/83**.
- Locally preserved thumbnail images: **0**.
- Inspectable thumbnails: **0**; registered URLs alone are not treated as visual evidence.
- Packaging screenshot evidence: **0**. Existing forensic frames show video content, not the historical thumbnail surface.
- Non-packaging video-frame evidence exists for `VID-000211`, `VID-000212`, and `VID-000221`; excluded from thumbnail claims.
- Thumbnail acquisition was not performed: no established controlled binary-thumbnail acquisition workflow exists, and raw/source acquisition records must remain unchanged.

## Semantic Quality Gate

| Family | Quality | Use |
|---|---|---|
| `SURVIVE` | `LOW_COHESION` | ITEM_LEVEL_ONLY; no family-wide packaging conclusion. |
| `MAGNITUDE_EARTHQUAKE` | `HIGH_COHESION` | Item-pair context; sample remains insufficient for winner status. |
| `MOON_MADE` | `HIGH_COHESION` | Item-pair context; severe performance variance retained. |
| `POWER` | `LOW_COHESION` | DIRECT_LIGHTNING_ITEM_PRIMARY; no family-wide packaging conclusion. |
| `DRAINED_OCEANS` | `HIGH_COHESION` | Exact-premise pair only; duplication and uneven performance limit generalization. |

Low-cohesion families remain usable only through cited items. No family-wide package conclusion is drawn for `SURVIVE` or `POWER`.

## Title Intelligence

| Archetype | Items | Median channel-relative | Long-form / Shorts | Repeatability |
|---|---:|---:|---:|---|
| `CONSEQUENCE_QUESTION` | 10 | 1.0068x | 2 / 8 | `MIXED_ASSOCIATION` |
| `DIRECT_QUESTION_OR_STATEMENT` | 8 | 0.3833x | 1 / 7 | `REPEATED_LOW_ASSOCIATION` |
| `FEASIBILITY_TEST` | 12 | 0.8642x | 3 / 9 | `MIXED_ASSOCIATION` |
| `LIMIT_OR_MEASUREMENT` | 9 | 1.7734x | 1 / 8 | `REPEATED_HIGH_ASSOCIATION` |
| `WHAT_IF_SCENARIO` | 44 | 1.0507x | 20 / 24 | `MIXED_ASSOCIATION` |

Strongest repeated textual signal is `LIMIT_OR_MEASUREMENT`: 9 items, 1.7734x median channel-relative performance. Eight are Shorts, so long-form transfer remains unproven. `WHAT_IF_SCENARIO` dominates frequency (44/83) but is mixed. Direct question/statement packaging is weak in this snapshot (8 items, 0.3833x median). These are associations, not causes.

## Thumbnail Intelligence

No thumbnail visual archetype is supported. `thumbnail_archetypes` is empty in JSON. Three `HYPOTHESIS_*` concepts are vocabulary for proposed tests only: single hero with scale, comparative split, and consequence chain.

## Title + Thumbnail Pair Patterns

No historical pair can be classified as redundant, complementary, title-led, or thumbnail-led without inspectable images. Proposed relationships are labeled `HYPOTHESIS` and require later testing.

## Packaging Archetypes

| ID | Observed title basis | Proposed visual basis | Evidence |
|---|---|---|---|
| `PKG-ARCH-001` | LIMIT_OR_MEASUREMENT | HYPOTHESIS_SINGLE_HERO_SCALE; no historical visual evidence. | `OBSERVATION_PLUS_HYPOTHESIS`, confidence `MEDIUM` |
| `PKG-ARCH-002` | WHAT_IF_SCENARIO with concrete transformation or substitution | HYPOTHESIS_COMPARATIVE_SPLIT; no historical visual evidence. | `OBSERVATION_PLUS_HYPOTHESIS`, confidence `LOW` |
| `PKG-ARCH-003` | FEASIBILITY_TEST | HYPOTHESIS_SINGLE_HERO_SCALE; no historical visual evidence. | `OBSERVATION_PLUS_HYPOTHESIS`, confidence `LOW` |
| `PKG-ARCH-004` | CONSEQUENCE_QUESTION | HYPOTHESIS_CONSEQUENCE_CHAIN; no historical visual evidence. | `OBSERVATION_PLUS_HYPOTHESIS`, confidence `LOW` |

No archetype is labeled a proven winner. Parenthetical usage is a one-item `ONE_OFF_HYPOTHESIS`.

## Opportunity Packaging

### `CH-000004-OP-001` — Extreme solar exposure

Family gate: LOW_COHESION; item-level support only. Format: `UNRESOLVED`.

- **A. Could You Survive One Nanosecond in Any Layer of the Sun?**
  - Frame: `CURIOSITY_FEASIBILITY`; title `FEASIBILITY_TEST`.
  - Thumbnail hypothesis: Human silhouette crossing three labeled solar layers; same silhouette repeated at one scale. Hero: Sun cross-section and human silhouette. Optional text: `1 ns`.
  - Pair: `QUESTION_PLUS_VISUAL_ANSWER_SETUP`.
  - Evidence: VID-000261 is a 2.5057x high-relative long-form performer; VID-000237 is 2.3494x. IDs: `VID-000261`, `VID-000237`.
  - Risk: Could imply survivability has one simple answer; layer assumptions must be explicit. No historical thumbnail evidence.
  - Boundary: Do not promise survival or rank solar layers without stated exposure assumptions. Confidence: `MEDIUM`.
- **B. One Nanosecond, Three Solar Layers: What Hits You Hardest?**
  - Frame: `SCALE_LIMIT`; title `LIMIT_OR_MEASUREMENT`.
  - Thumbnail hypothesis: Three equal panels for photosphere, corona, and interior with one shared 1 ns clock. Hero: Solar layers and stopwatch. Optional text: `1 ns`.
  - Pair: `TITLE_ADDS_CONTEXT`.
  - Evidence: LIMIT_OR_MEASUREMENT has 9 items and 1.7734x median channel-relative performance; mostly Shorts, so long-form transfer is unproven. IDs: `VID-000261`, `VID-000214`, `VID-000216`.
  - Risk: “Hits hardest” needs a defined hazard metric. Three-panel visual may be complex at small size.
  - Boundary: Do not treat title pattern association as causal performance proof. Confidence: `MEDIUM`.
- **C. The Corona Is Hotter—So Which Solar Layer Is More Dangerous?**
  - Frame: `CONTRADICTION_COMPARISON`; title `DIRECT_QUESTION_OR_STATEMENT`.
  - Thumbnail hypothesis: Hot sparse corona on one side; cooler dense photosphere on other; equal human silhouette between. Hero: Split Sun layers. Optional text: `HOTTER ≠ DENSER`.
  - Pair: `THUMBNAIL_ADDS_CONCRETE_VISUAL`.
  - Evidence: VID-000261 is 2.5057x; VID-000242 is 1.0894x. Broad SURVIVE family is not used as package proof. IDs: `VID-000261`, `VID-000242`.
  - Risk: Comparative premise requires careful units and exposure geometry. Direct-statement historical archetype is weak overall.
  - Boundary: Do not claim hotter is safer or denser is always deadlier. Confidence: `LOW`.
- Initial favorite: `CH-000004-OP-001-PKG-B` — `HYPOTHESIS_FOR_TESTING`. Best match to repeated limit/measurement title evidence; visual remains unvalidated.

### `CH-000004-OP-002` — Physical limits of earthquake magnitude

Family gate: HIGH_COHESION; only two family items. Format: `UNRESOLVED`.

- **A. Could Earth Ever Produce a Magnitude 10 Earthquake?**
  - Frame: `CURIOSITY_FEASIBILITY`; title `FEASIBILITY_TEST`.
  - Thumbnail hypothesis: Earth with one fault line beside a magnitude dial ending at 10. Hero: Earth and fault line. Optional text: `M10?`.
  - Pair: `QUESTION_PLUS_VISUAL_ANSWER_SETUP`.
  - Evidence: VID-000214=3.9161x Short, VID-000216=1.7734x Short, VID-000272=1.694x long-form. IDs: `VID-000214`, `VID-000216`, `VID-000272`.
  - Risk: Disaster premise is saturated. Question must not imply magnitude 10 has occurred.
  - Boundary: Do not claim the scale itself has a hard maximum. Confidence: `HIGH`.
- **B. Magnitude Has No Maximum—Earth Does**
  - Frame: `CONTRADICTION`; title `DIRECT_QUESTION_OR_STATEMENT`.
  - Thumbnail hypothesis: Open-ended magnitude scale rising off-frame versus a finite fault constrained by Earth. Hero: Scale and finite fault. Optional text: `SCALE vs EARTH`.
  - Pair: `TITLE_ADDS_CONTEXT`.
  - Evidence: Both exact family items exceed channel median, but n=2 is insufficient for repeatable-winner status. IDs: `VID-000214`, `VID-000272`.
  - Risk: Declarative titles have weak channel-wide evidence. “Earth does” compresses a practical limit that depends on fault geometry.
  - Boundary: Do not present an exact universal maximum magnitude. Confidence: `MEDIUM`.
- **C. How Big Would a Fault Need to Be for a Magnitude 10 Earthquake?**
  - Frame: `SCALE_MECHANISM`; title `LIMIT_OR_MEASUREMENT`.
  - Thumbnail hypothesis: Fault-length bracket stretched across a globe with a small magnitude marker. Hero: Earth-scale fault. Optional text: `HOW LONG?`.
  - Pair: `THUMBNAIL_ADDS_SCALE`.
  - Evidence: Limit/measurement titles show 1.7734x median channel-relative performance across 9 items; exact quake pair is high but sparse. IDs: `VID-000214`, `VID-000216`, `VID-000272`.
  - Risk: Wording can imply a physically available fault exists. Requires clear distinction between rupture length and intensity.
  - Boundary: Do not imply fault length alone determines all earthquake effects. Confidence: `HIGH`.
- Initial favorite: `CH-000004-OP-002-PKG-C` — `HYPOTHESIS_FOR_TESTING`. Strongest fit to limit/measurement evidence and mechanism gap.

### `CH-000004-OP-003` — Moon composition under impossible substitutions

Family gate: HIGH_COHESION; severe two-item performance variance. Format: `UNRESOLVED`.

- **A. Which Breaks First: a Moon of Protons or a Moon of Electrons?**
  - Frame: `COMPARATIVE_CURIOSITY`; title `LIMIT_OR_MEASUREMENT`.
  - Thumbnail hypothesis: Moon split into red proton and blue electron halves; first-failure marker between. Hero: Two altered Moons. Optional text: `WHICH FIRST?`.
  - Pair: `QUESTION_PLUS_VISUAL_ANSWER_SETUP`.
  - Evidence: VID-000211 is a 8.6256x positive outlier; VID-000271 is 0.7666x. One-outlier pattern is not generalized. IDs: `VID-000211`, `VID-000271`.
  - Risk: Particle colors are diagram conventions, not literal appearance. Two-item evidence is unstable.
  - Boundary: Do not call either historical package a proven winner or imply stable particle Moons. Confidence: `MEDIUM`.
- **B. Replace Every Atom in the Moon With One Particle—What Happens?**
  - Frame: `EXTREME_SUBSTITUTION`; title `WHAT_IF_SCENARIO`.
  - Thumbnail hypothesis: Normal layered Moon collapsing into one repeated particle symbol. Hero: Moon cross-section transforming. Optional text: `ONE PARTICLE`.
  - Pair: `TITLE_ADDS_CONTEXT`.
  - Evidence: WHAT_IF_SCENARIO has 44 items, 1.0507x median, mixed association; comparison feature has strong but confounded signal. IDs: `VID-000211`, `VID-000271`, `VID-000235`.
  - Risk: “Every atom” is shorthand; exact replacement rules must be stated. Broad What-if archetype has many weak counterexamples.
  - Boundary: Do not imply the hypothetical is physically constructible. Confidence: `MEDIUM`.
- **C. The Real Moon Has Layers. A One-Particle Moon Would Not Last.**
  - Frame: `REALITY_CONTRADICTION`; title `DIRECT_QUESTION_OR_STATEMENT`.
  - Thumbnail hypothesis: Real core-mantle-crust cross-section versus a uniform particle Moon dispersing. Hero: Real and substituted Moon. Optional text: `REAL vs REPLACED`.
  - Pair: `THUMBNAIL_ADDS_CONCRETE_VISUAL`.
  - Evidence: Exact family median is high but driven by one outlier; the paired item is below channel median. IDs: `VID-000211`, `VID-000271`.
  - Risk: Declarative “would not last” needs explicit timescale and assumptions. Direct-statement archetype is weak channel-wide.
  - Boundary: Do not claim NASA studied these impossible substitutions. Confidence: `LOW`.
- Initial favorite: `CH-000004-OP-003-PKG-A` — `HYPOTHESIS_FOR_TESTING`. Most distinct from historical wording and exposes a clear comparison.

### `CH-000004-OP-004` — Capturing extreme natural energy

Family gate: LOW_COHESION; direct lightning item is primary. Format: `UNRESOLVED`.

- **A. Could One Lightning Bolt Power a City?**
  - Frame: `CURIOSITY_FEASIBILITY`; title `FEASIBILITY_TEST`.
  - Thumbnail hypothesis: Single bolt hitting a city-size battery with an incomplete charge bar. Hero: Lightning bolt and city battery. Optional text: `ONE BOLT?`.
  - Pair: `QUESTION_PLUS_VISUAL_ANSWER_SETUP`.
  - Evidence: Direct lightning item is 0.8422x normal range; feasibility archetype median is 0.8642x and mixed. IDs: `VID-000217`, `VID-000228`, `VID-000239`.
  - Risk: City demand and bolt energy vary widely. Could invite a simplistic yes/no answer.
  - Boundary: Do not imply one bolt can supply continuous city power. Confidence: `LOW`.
- **B. Lightning Has Huge Energy—Why Can’t We Use It?**
  - Frame: `MISCONCEPTION_CONTRADICTION`; title `DIRECT_QUESTION_OR_STATEMENT`.
  - Thumbnail hypothesis: Bright bolt and energy burst on left; thin intermittent grid output on right. Hero: Bolt versus grid line. Optional text: `ENERGY ≠ POWER`.
  - Pair: `TITLE_ADDS_CONTEXT`.
  - Evidence: VID-000217 is normal-range 0.8422x; VID-000242 is 1.0894x. No repeated direct lightning winner exists. IDs: `VID-000217`, `VID-000242`.
  - Risk: Question overstates impossibility; some capture is possible at small scale. No historical thumbnail evidence.
  - Boundary: Do not claim lightning energy is literally unusable. Confidence: `MEDIUM`.
- **C. What Would a Lightning-Powered Grid Actually Need?**
  - Frame: `SYSTEM_REQUIREMENTS`; title `CONSEQUENCE_QUESTION`.
  - Thumbnail hypothesis: Bolt feeding three labeled bottlenecks: capture, storage, frequency. Hero: Lightning-to-grid chain. Optional text: `CAPTURE / STORE / REPEAT`.
  - Pair: `THUMBNAIL_ADDS_CONCRETE_VISUAL`.
  - Evidence: Power family is low-cohesion; cited items only establish mixed energy-feasibility precedent. IDs: `VID-000217`, `VID-000228`, `VID-000239`.
  - Risk: Three-part thumbnail may be too dense. Title may sound less immediate than the bolt-versus-city frame.
  - Boundary: Do not claim title structure predicts watch time or CTR. Confidence: `LOW`.
- Initial favorite: `CH-000004-OP-004-PKG-B` — `HYPOTHESIS_FOR_TESTING`. Best expression of validated energy-versus-power gap despite weak historical package evidence.

### `CH-000004-OP-005` — Earth after ocean loss

Family gate: HIGH_COHESION; exact-premise pair is uneven. Format: `UNRESOLVED`.

- **A. If the Oceans Vanished, What Water Would Be Left?**
  - Frame: `CURIOSITY_INVENTORY`; title `CONSEQUENCE_QUESTION`.
  - Thumbnail hypothesis: Dry ocean basins with small highlighted ice, groundwater, and cloud reservoirs. Hero: Dry Earth and remaining reservoirs. Optional text: `WHAT REMAINS?`.
  - Pair: `THUMBNAIL_ADDS_CONCRETE_VISUAL`.
  - Evidence: VID-000194 is 4.1288x Short; VID-000264 is 0.8426x long-form. Same premise, uneven result. IDs: `VID-000194`, `VID-000264`.
  - Risk: “Vanished” differs from gradual draining; content must define scenario. Small reservoir icons may be unreadable.
  - Boundary: Do not claim all water or all oxygen disappears instantly. Confidence: `MEDIUM`.
- **B. What Fails First on an Oceanless Earth?**
  - Frame: `CONSEQUENCE_PRIORITY`; title `CONSEQUENCE_QUESTION`.
  - Thumbnail hypothesis: Dry globe followed by three large consequence symbols: weather, food web, heat transport. Hero: Oceanless Earth. Optional text: `FIRST?`.
  - Pair: `THUMBNAIL_ADDS_STAKES`.
  - Evidence: Exact ocean pair is mixed; consequence titles are format-dependent, with 2.0819x long-form versus 0.6219x Shorts median in small samples. IDs: `VID-000194`, `VID-000264`, `VID-000263`.
  - Risk: “First” needs a defined timescale and failure criterion. Chain visualization can imply false certainty.
  - Boundary: Do not present speculative biosphere timing as measured fact. Confidence: `MEDIUM`.
- **C. Remove 97% of Earth’s Water—What Happens to the Rest?**
  - Frame: `SCALE_CONTRADICTION`; title `LIMIT_OR_MEASUREMENT`.
  - Thumbnail hypothesis: Earth as a nearly empty water gauge with small remaining ice, groundwater, and atmosphere markers. Hero: Earth water gauge. Optional text: `97% GONE`.
  - Pair: `THUMBNAIL_ADDS_SCALE`.
  - Evidence: Scale/magnitude feature appears in 21 titles with 1.2767x median channel-relative performance; association is non-causal. IDs: `VID-000194`, `VID-000264`, `VID-000192`.
  - Risk: 97% refers approximately to ocean share of Earth’s water and needs sourcing. Could be read as all water removal if visual is unclear.
  - Boundary: Do not equate ocean removal with a dry planet or immediate loss of all oxygen. Confidence: `MEDIUM`.
- Initial favorite: `CH-000004-OP-005-PKG-A` — `HYPOTHESIS_FOR_TESTING`. Strongest distinction from saturated exact premise and clearest factual gap.

## A/B Test Sets

For an eligible long-form production, test each opportunity’s A/B/C title-thumbnail combinations on the same finished upload. Keep video, visibility, audience settings, and native test window constant. Variants differ by curiosity/feasibility, scale/mechanism, and consequence/contradiction. Evaluate with native YouTube output, whose winner uses watch-time share rather than external CTR-only judgment. Shorts are currently excluded. This is experiment design only.

## Counter-Evidence

- Limit/measurement title evidence is mostly Shorts: 8 of 9 items; long-form transfer is unproven.
- What-if titles are common but mixed: 44 items, 1.0507x median channel-relative performance, with low performers.
- Direct question/statement titles are repeatedly weak in this snapshot: 8 items, 0.3833x median.
- Consequence questions differ by format: 2.0819x median for 2 long-form items versus 0.6219x for 8 Shorts.
- Extreme-condition wording alone is not strong: 25 items, 0.8126x median.
- Parenthetical usage occurs once; it is a ONE_OFF_HYPOTHESIS and cannot support a winner archetype.
- No historical title-thumbnail relationship is observable because no thumbnail image is locally inspectable.

## Limitations

- One registered public-metric snapshot per item; no performance trajectory.
- No impressions, CTR, watch time, retention, traffic source, subscriber conversion, unique viewers, or audience overlap.
- Title associations are observational and confounded by topic, thumbnail, format, release context, and content.
- Registered thumbnail URLs are references, not locally preserved images; no visual attributes are inferred from them.
- Long-form and Shorts evidence remains separated; transfer between formats is unproven.

## Pilot Verdict

**PARTIAL.** Title Intelligence, performance joins, format separation, traceability, 15 package hypotheses, and test design work. Historical Thumbnail Intelligence and title-thumbnail pair validation do not: 83 URLs are registered, but zero thumbnail images are locally preserved or inspectable. Acquiring and registering immutable thumbnail binaries through an approved controlled workflow is the required next gate.

Official guardrails: [content performance](https://support.google.com/youtube/answer/16559650?hl=en), [custom thumbnails](https://support.google.com/youtube/answer/72431), and [native title/thumbnail A/B testing](https://support.google.com/youtube/answer/16391400?hl=en).

Provenance: `DS-000017`, `RUN-000020`, `APIFYRUN-000002`; Topic Intelligence and DS-000018 validation remain unchanged.
