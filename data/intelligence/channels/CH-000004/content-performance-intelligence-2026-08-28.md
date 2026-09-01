# xkcd's What If? — Content + Performance Intelligence

## Artifact identity

| Field | Value |
|---|---|
| Artifact ID | `INT-CH-000004-CONTENT-PERFORMANCE-20260828` |
| Channel | `CH-000004` — xkcd's What If? (`@xkcd_whatif`) |
| YouTube channel ID | `UC6IxnFzHofFJ5X2PycSMsww` |
| Evidence cutoff | `2026-08-28T13:16:30.020Z` |
| Registered source dataset | `DS-000017` |
| Structured registration run | `RUN-000020` |
| Apify source run | `APIFYRUN-000002` / Actor run `mzl5dCHF81LbcBamS` |
| Analysis scope | All 83 registered content items and their latest registered snapshot |
| Artifact evidence layer | Mixed: `MEASURED_FACT`, `OBSERVATION`, `AI_INTERPRETATION`, and `HYPOTHESIS`, labeled below |
| Excluded | Web research, new acquisition, editing style, scripts, thumbnails as creative treatments, and causal claims |

This is a channel-scoped intelligence artifact. It uses the SQLite catalog only. It does not modify the catalog or raw evidence.

## Evidence and method

### Source evidence

- **EXTRACTED_FACT:** The channel has 83 unique registered items: 43 `video` records and 40 `shorts` records; no streams are registered.
- **EXTRACTED_FACT:** All 83 latest snapshots share the observation timestamp `2026-08-28T13:16:30.020Z` and contain title, content type, publish date, duration, views, likes, comments, and description.
- **EXTRACTED_FACT:** The source run was `streamers/youtube-scraper` run `mzl5dCHF81LbcBamS`, registered through `DS-000017` and `RUN-000020`.
- **MEASURED_FACT:** Exactly one latest snapshot was selected per canonical video. No title, topic, or metric from another channel was included.

### Relative-performance baseline

Raw lifetime views are reported, but never used alone to rank relative performance. Older items have had more time to accumulate views, and regular videos and Shorts have different distributions.

For each format separately, this artifact fits the following descriptive channel baseline across the 2026-08-28 snapshot:

```text
age_days = max(1, observed_at - published_at)
ln(baseline_views) = a + b * ln(age_days)
relative_performance = actual_views / baseline_views

regular videos: a = 12.1386255132, b = 0.4156419037
Shorts:         a = 12.0175152206, b = 0.3252782586
```

- **MEASURED_FACT:** `1.00x` means the item matches the fitted same-format, same-channel age baseline; `2.00x` means twice the baseline; `0.50x` means half.
- **OBSERVATION:** This is a within-channel descriptive normalization, not a forecast or causal model.
- **HYPOTHESIS:** None of the performance relationships below establishes that its topic or title caused the observed views.

## Corpus baseline

| Evidence layer | Measure | Regular videos | Shorts |
|---|---|---:|---:|
| MEASURED_FACT | Items | 43 | 40 |
| MEASURED_FACT | Median lifetime views | 2,186,774 | 814,527 |
| MEASURED_FACT | Median duration | 196 sec | 75.5 sec |
| MEASURED_FACT | Median like/view rate | 3.688% | 4.496% |
| MEASURED_FACT | Median comments per 1,000 views | 1.379 | 0.809 |
| MEASURED_FACT | Publish-date range | 2023-11-29 to 2026-08-25 | 2025-06-24 to 2026-08-18 |
| MEASURED_FACT | Median gap between releases | 21.00 days | 7.04 days |
| MEASURED_FACT | Tuesday releases | 42/43 | 39/40 |

**OBSERVATION:** Regular videos have a roughly three-week cadence in this corpus; Shorts have a roughly weekly cadence. The raw median-view difference is not a format-effect estimate because regular videos are older as a group and the formats are normalized separately.

## Topic taxonomy

Primary-topic assignment is **AI_INTERPRETATION** of registered titles and descriptions. Each item receives one primary cluster for counting; overlapping themes still exist.

“Recurring” means at least five items. Cluster performance is the median item-level relative-performance score, not the ratio of aggregate views.

| Primary topic cluster | Items | Regular | Shorts | Median relative performance | Reading |
|---|---:|---:|---:|---:|---|
| Earth systems, geography & disasters | 22 | 11 | 11 | 1.142x | Above baseline; recurring |
| Space & celestial scenarios | 16 | 8 | 8 | 0.841x | Below baseline; recurring |
| Extreme physics, energy & radiation | 15 | 9 | 6 | 0.956x | Near baseline; recurring |
| Human survival, biology & civilization | 10 | 5 | 5 | 1.163x | Above baseline; recurring |
| Engineering, transport & infrastructure | 10 | 6 | 4 | 0.834x | Below baseline; recurring |
| Scale, math, computation & economics | 6 | 3 | 3 | 0.769x | Below baseline; recurring |
| History & cultural hypotheticals | 3 | 1 | 2 | 0.296x | Lowest, but small sample |
| Mixed-question anthology | 1 | 0 | 1 | 1.881x | Not recurring; do not generalize |

### Main recurring categories and subtopics

- **AI_INTERPRETATION — Earth systems, geography & disasters:** earthquake magnitude; Earth rotation/spin; oceans and disappearing water; waterfalls and deep-ocean scenarios; lightning and planetary-scale physical changes.
- **AI_INTERPRETATION — Space & celestial scenarios:** Moon transformations; Sun exposure or failure; Mars relocation; Hubble observation; extraterrestrial environments.
- **AI_INTERPRETATION — Extreme physics, energy & radiation:** lasers; nuclear/radiation scenarios; relativistic objects; matter/antimatter; extreme energy conversion.
- **AI_INTERPRETATION — Human survival, biology & civilization:** extinction aftermath; mass human behavior; survivability limits; DNA/biology; cannibalism.
- **AI_INTERPRETATION — Engineering, transport & infrastructure:** implausible machines; racing/transport limits; mega-structures; unconventional power devices; movement through extreme environments.
- **AI_INTERPRETATION — Scale, math, computation & economics:** enormous quantities; Wikipedia printing; circumference; all-world money; unit/wordplay questions.
- **AI_INTERPRETATION — History & cultural hypotheticals:** alternate physical consequences of the wise men's journey.

### Topic-performance reading

- **MEASURED_FACT:** Among recurring clusters, human survival/biology/civilization has the highest median relative score (`1.163x`), followed by Earth systems/geography/disasters (`1.142x`).
- **MEASURED_FACT:** Scale/math/computation/economics is the weakest recurring cluster (`0.769x`), followed by engineering/transport/infrastructure (`0.834x`) and space/celestial scenarios (`0.841x`).
- **MEASURED_FACT:** History/cultural hypotheticals is lower (`0.296x`) but has only three items, so it is not treated as a stable recurring-cluster result.
- **OBSERVATION:** The strongest recurring clusters contain several high-consequence or survival-stakes premises, while weak clusters include both abstract scale problems and multiple narrow follow-ups.
- **AI_INTERPRETATION:** The Earth and human-survival clusters appear to provide especially legible stakes—destruction, survival, disappearance, or civilization-scale consequence—in the title premise.
- **HYPOTHESIS:** Legible high-stakes consequences may be associated with stronger relative viewing, but topic, title, thumbnail, release context, and source-material familiarity are confounded here.

## Recurring question and title structures

The buckets below are mutually exclusive deterministic title-prefix counts. Their labels are descriptive; their performance remains correlational.

| Structure | Items | Regular | Shorts | Median relative performance |
|---|---:|---:|---:|---:|
| `What if…` counterfactual | 44 | 31 | 13 | 0.969x |
| `What would…` consequence | 9 | 2 | 7 | 0.510x |
| `Could/Can…` feasibility | 11 | 6 | 5 | 0.904x |
| `How…` limit/duration | 8 | 1 | 7 | 1.172x |
| Other direct question | 7 | 2 | 5 | 0.849x |
| Statement, imperative, or anthology | 4 | 1 | 3 | 0.632x |

- **MEASURED_FACT:** `What if…` is the dominant structure (44/83), especially for regular videos (31/43).
- **MEASURED_FACT:** Shorts use `What if…` less often (13/40) and use more consequence, feasibility, and limit/duration questions.
- **OBSERVATION:** The `How…` group is above baseline (`1.172x`), while the `What would…` group is below (`0.510x`). Seven of eight `How…` titles and seven of nine `What would…` titles are Shorts, so structure and format/topic series are entangled.
- **AI_INTERPRETATION:** Common premise constructions include extreme numerical scaling, sudden removal or transformation, impossible substitution, collective action, feasibility tests, and survivability limits.
- **HYPOTHESIS:** A concrete limit or duration in a `How…` question may make the payoff easier to anticipate than a broad consequence question, but the sample is small and does not isolate wording from topic.

## Top 10 relative performers

All rankings use the age- and format-relative channel baseline above.

| Rank | YouTube ID | Type | Published | Views | Baseline views | Relative | Title |
|---:|---|---|---|---:|---:|---:|---|
| 1 | `FKXVs4UteSc` | Short | 2025-07-01 | 7,779,036 | 1,184,077 | 6.57x | Is there such a thing as a magnitude 0 earthquake? |
| 2 | `aMshLs0YCTQ` | Short | 2025-12-16 | 4,940,989 | 1,004,137 | 4.92x | What if you drained the oceans? |
| 3 | `8fADp43wJwU` | Regular | 2024-05-28 | 9,534,650 | 3,042,529 | 3.13x | If all humans died, when would the last light go out? |
| 4 | `rGZ6TsXvi8E` | Short | 2026-08-18 | 1,055,791 | 348,502 | 3.03x | How long could you drive towards the sunset? |
| 5 | `wBLVmEZV2Oc` | Short | 2025-06-24 | 3,581,311 | 1,190,455 | 3.01x | How high could the magnitude of Earthquakes go? |
| 6 | `UXA-Af-JeCE` | Regular | 2024-09-03 | 8,521,062 | 2,886,272 | 2.95x | Could you survive a nanosecond on the Sun? |
| 7 | `2p305nzcVQE` | Short | 2025-12-23 | 2,600,869 | 995,156 | 2.61x | What if we teleported the oceans to Mars? |
| 8 | `Uj10jGq2O8o` | Short | 2025-10-28 | 2,671,498 | 1,063,272 | 2.51x | What if you tried to hit a baseball pitched at 90% the speed of light? |
| 9 | `e3uk7jU3RHo` | Regular | 2023-12-05 | 7,933,044 | 3,296,805 | 2.41x | What would a magnitude 15 earthquake be like? |
| 10 | `pfbzrrcQZjs` | Regular | 2025-06-17 | 5,147,802 | 2,339,721 | 2.20x | What if you funneled Niagara Falls through a straw? |

`rGZ6TsXvi8E` was only 9.8 days old at observation and is therefore a provisional relative outlier.

## Bottom 10 relative performers

| Rank | YouTube ID | Type | Published | Views | Baseline views | Relative | Title |
|---:|---|---|---|---:|---:|---:|---|
| 1 | `ERieN5pee7A` | Short | 2025-10-14 | 249,498 | 1,079,041 | 0.23x | What would happen to the Earth if it suddenly stopped spinning? |
| 2 | `GgEGcxJRDik` | Short | 2026-05-19 | 184,978 | 742,823 | 0.25x | What would the world's largest cities be like if the land masses were rotated by 90 degrees? |
| 3 | `d5TD3r1nLqM` | Short | 2026-03-17 | 232,243 | 869,783 | 0.27x | Which path would the three wise men have walked? |
| 4 | `pMMo3XvoKD4` | Short | 2026-03-10 | 260,948 | 881,703 | 0.30x | Where would the three wise men go if they followed a planet? |
| 5 | `zJNmUWZXj2M` | Short | 2026-04-21 | 244,598 | 804,408 | 0.30x | What would happen in Minnesota if the world rotated by 90 degrees? |
| 6 | `YL2VNtus4xk` | Regular | 2025-03-04 | 1,087,683 | 2,558,886 | 0.43x | What if the wise men kept walking after Jesus’s birth? |
| 7 | `mtTbwHzhUiM` | Short | 2025-08-12 | 495,831 | 1,144,462 | 0.43x | Petition to send a swimming pool to the moon! |
| 8 | `XvvXDEtMfhw` | Short | 2026-04-28 | 358,431 | 789,964 | 0.45x | What would Earth's climate be like if the land masses were rotated by 90°? |
| 9 | `n_KUCunjMwQ` | Short | 2026-04-02 | 428,866 | 841,261 | 0.51x | What would happen if the Sun went dark? |
| 10 | `X7sbn9LMZOg` | Regular | 2025-04-15 | 1,335,412 | 2,474,298 | 0.54x | What if the sun suddenly went out? |

## Highest and lowest lifetime views

These are raw point-in-time counts, paired with relative scores so age and format context remain visible.

### Highest viewed

| Rank | YouTube ID | Type | Views | Relative | Title |
|---:|---|---|---:|---:|---|
| 1 | `8fADp43wJwU` | Regular | 9,534,650 | 3.13x | If all humans died, when would the last light go out? |
| 2 | `UXA-Af-JeCE` | Regular | 8,521,062 | 2.95x | Could you survive a nanosecond on the Sun? |
| 3 | `e3uk7jU3RHo` | Regular | 7,933,044 | 2.41x | What would a magnitude 15 earthquake be like? |
| 4 | `FKXVs4UteSc` | Short | 7,779,036 | 6.57x | Is there such a thing as a magnitude 0 earthquake? |
| 5 | `JqFSGkFPipM` | Regular | 5,899,108 | 2.12x | What if everyone pointed a laser at the moon? |
| 6 | `EsUBRd1O2dU` | Regular | 5,287,786 | 1.67x | Would a Submarine Work as a Spaceship? |
| 7 | `-1-ldW4kpLM` | Regular | 5,191,681 | 1.84x | What if Earth grew 1cm every second? |
| 8 | `pfbzrrcQZjs` | Regular | 5,147,802 | 2.20x | What if you funneled Niagara Falls through a straw? |
| 9 | `aMshLs0YCTQ` | Short | 4,940,989 | 4.92x | What if you drained the oceans? |
| 10 | `0EytSWiKrFg` | Regular | 4,136,504 | 1.45x | What if a glass of water were LITERALLY half empty? |

### Lowest viewed

| Rank | YouTube ID | Type | Views | Relative | Title |
|---:|---|---|---:|---:|---|
| 1 | `GgEGcxJRDik` | Short | 184,978 | 0.25x | What would the world's largest cities be like if the land masses were rotated by 90 degrees? |
| 2 | `d5TD3r1nLqM` | Short | 232,243 | 0.27x | Which path would the three wise men have walked? |
| 3 | `zJNmUWZXj2M` | Short | 244,598 | 0.30x | What would happen in Minnesota if the world rotated by 90 degrees? |
| 4 | `ERieN5pee7A` | Short | 249,498 | 0.23x | What would happen to the Earth if it suddenly stopped spinning? |
| 5 | `pMMo3XvoKD4` | Short | 260,948 | 0.30x | Where would the three wise men go if they followed a planet? |
| 6 | `oBWqlxDd8sU` | Short | 342,587 | 0.63x | What if half the human population ate the other half 🍽️ |
| 7 | `XvvXDEtMfhw` | Short | 358,431 | 0.45x | What would Earth's climate be like if the land masses were rotated by 90°? |
| 8 | `n_KUCunjMwQ` | Short | 428,866 | 0.51x | What would happen if the Sun went dark? |
| 9 | `jjzYUOd5HAA` | Short | 434,451 | 0.76x | How long could the human race survive on only cannibalism? |
| 10 | `mtTbwHzhUiM` | Short | 495,831 | 0.43x | Petition to send a swimming pool to the moon! |

## Regular-video versus Shorts differences

- **MEASURED_FACT:** Topic distribution is broadly similar: Earth is 11/43 regular videos and 11/40 Shorts; space is 8/43 and 8/40; human survival is 5/43 and 5/40.
- **MEASURED_FACT:** Regular videos lean slightly more toward extreme physics (9 vs. 6) and engineering (6 vs. 4). Shorts include two of the three history/cultural items and the one mixed anthology.
- **MEASURED_FACT:** Regular titles use `What if…` in 31/43 cases; Shorts use it in 13/40.
- **OBSERVATION:** Shorts more often split a premise into narrower consequences or limit questions. Examples include separate population/Earth consequences for stopped rotation and four geographic/climate consequences for the 90-degree-rotation premise.
- **OBSERVATION:** Same-premise Shorts do not move uniformly. The earthquake group is strong (`2.41x`, `3.01x`, `6.57x`), while the wise-men group is consistently weak (`0.43x`, `0.30x`, `0.27x`). Ocean-topic Shorts outperform their corresponding regular items, while other adaptations are mixed.
- **AI_INTERPRETATION:** Shorts function partly as narrower premise slices, but no formal source-to-Short derivation field exists; similarity is based on titles and descriptions, not a registered lineage relationship.
- **HYPOTHESIS:** A premise can support multiple Shorts, but later/narrower slices may face diminishing interest. The stopped-Earth and 90-degree-rotation groups are consistent with this possibility, while earthquake and ocean groups show that it is not a universal rule.

## Important outliers

- **MEASURED_FACT:** Thirteen items are at or above `2.00x` their age- and format-relative baseline. Eleven were at least 30 days old at observation; two were recent and provisional.
- **OBSERVATION:** The strongest stable outlier is magnitude-0-earthquake Short `FKXVs4UteSc` (`6.57x`). The strongest regular-video outlier is last-human-light `8fADp43wJwU` (`3.13x`).
- **OBSERVATION:** Both registered earthquake Shorts and the magnitude-15 regular video exceed `2.4x`, making earthquake magnitude the clearest repeated strong-premise group in this snapshot.
- **OBSERVATION:** The wise-men regular video and both related Shorts are all below `0.43x`, the clearest repeated weak-premise group, though it has only three items.
- **OBSERVATION:** `rGZ6TsXvi8E` (`3.03x`, age 9.8 days) and `4ZVtHknKuvg` (`2.02x`, age 2.8 days) are early-window outliers and should not be treated as settled lifetime results.
- **HYPOTHESIS:** Repeated success around earthquake magnitude may reflect unusually clear scalar contrast (“0” and “15”), destructive stakes, or prior topic familiarity. The available data cannot separate those explanations.

## Publish-date and format patterns

- **MEASURED_FACT:** 42/43 regular videos and 39/40 Shorts were published on Tuesday.
- **MEASURED_FACT:** The median release gap is about 21 days for regular videos and 7 days for Shorts.
- **OBSERVATION:** The corpus supports a stable Tuesday-led cadence, with Shorts filling more weekly slots after their first registered publication in June 2025.
- **HYPOTHESIS:** No day-of-week performance comparison is supportable because almost all items share Tuesday; there is no meaningful control group.

## Data limitations

1. **MEASURED_FACT:** There is one registered metric snapshot per item. View trajectories, first-24-hour performance, and later decay cannot be observed.
2. **MEASURED_FACT:** No impressions, click-through rate, watch time, retention, traffic-source, subscriber-conversion, or audience-segment metrics are registered.
3. **OBSERVATION:** The power-law age baseline is a compact within-channel control, not a model of YouTube distribution dynamics. It can reduce obvious age bias but cannot remove release-era or recommendation-system effects.
4. **OBSERVATION:** Items under 30 days old have unstable lifetime comparisons. They are retained but explicitly marked where material.
5. **AI_INTERPRETATION:** Topic clusters and premise-family links are semantic judgments from titles/descriptions. They are not source-declared categories or proven production relationships.
6. **HYPOTHESIS:** Topic and title effects cannot be isolated from thumbnail packaging, audience familiarity, external promotion, or the content itself. No causal conclusion is warranted.
7. Editing style was not analyzed. Transcript availability does not establish editing-style evidence.

## Auditable primary-cluster membership

These assignments are **AI_INTERPRETATION**. The ID sets cover all 83 canonical items exactly once.

- **Earth systems, geography & disasters (22):** `e3uk7jU3RHo`, `gp5G1QG6cXc`, `fs28lEq9smw`, `Jpy55EgMQgY`, `-1-ldW4kpLM`, `WH4g1ptJ-70`, `pfbzrrcQZjs`, `U8F7UNK9jco`, `r7B0MzvwDcA`, `FYoHYq8VRt0`, `4ZVtHknKuvg`, `wBLVmEZV2Oc`, `FKXVs4UteSc`, `19gun1mffWs`, `ERieN5pee7A`, `aMshLs0YCTQ`, `QZIEjvSlOMQ`, `zJNmUWZXj2M`, `XvvXDEtMfhw`, `U4cONnQxgvo`, `GgEGcxJRDik`, `rGZ6TsXvi8E`.
- **Space & celestial scenarios (16):** `2LSyizrk8-0`, `FkUNHhVbQ1Q`, `UXA-Af-JeCE`, `JqFSGkFPipM`, `aIIBBj6KR-Y`, `X7sbn9LMZOg`, `UQgw50GQu1A`, `BO8rOs05v48`, `sFTRRdHqZIQ`, `mtTbwHzhUiM`, `TgA0lXEW7dw`, `i6e4NnFnQi0`, `2p305nzcVQE`, `m1aMh7z8Y7I`, `n_KUCunjMwQ`, `n2XRulD_IVs`.
- **Extreme physics, energy & radiation (15):** `3EI08o-IGYk`, `zgBTwtg7H8E`, `EFRUL7vKdU8`, `0EytSWiKrFg`, `jgafb8G7i4o`, `DiWFXv9N0Vs`, `TFhrRrRdUbA`, `BnGqPxnQh9A`, `qu8nx1qUwEU`, `_efsqO-4OoQ`, `Uj10jGq2O8o`, `xA9aqKGBeOs`, `vBfR2Zb0dkc`, `oLoxdLfB6Gs`, `mEUqVgGf4e0`.
- **Human survival, biology & civilization (10):** `8fADp43wJwU`, `p2M8Y0z9Rl0`, `PUtI3xoaHx0`, `s3oLIDaElaE`, `oTzW-mTQd5w`, `kNry0bf7eC0`, `eSPcp-tfGbA`, `Ny9m2l6h478`, `jjzYUOd5HAA`, `oBWqlxDd8sU`.
- **Engineering, transport & infrastructure (10):** `JcXpCyPc2Xw`, `EsUBRd1O2dU`, `Z_xJ40QXu7Q`, `WYf9-xfm6t8`, `0L44GEJ5pLE`, `IdlQsjq5vKo`, `rgUfcFAPicY`, `J-E8rjWR9rM`, `oMtAHGv-DU4`, `DDNMLh1I_jY`.
- **Scale, math, computation & economics (6):** `RgBYohJ7mIk`, `saj7b5C6TCM`, `lLlwvmu1ZeA`, `5k8ciEx__5w`, `WQTNLuhfkwk`, `jVy3qd70AqU`.
- **History & cultural hypotheticals (3):** `YL2VNtus4xk`, `pMMo3XvoKD4`, `d5TD3r1nLqM`.
- **Mixed-question anthology (1):** `SLd4hnmeW_g`.

## Provenance boundary

The factual inputs are the registered `channels`, `videos`, and latest `video_snapshots` rows for `CH-000004`, traced through `DS-000017`, `RUN-000020`, and `APIFYRUN-000002`. This artifact is derived intelligence and is not raw evidence. Re-running against a newer snapshot must create a new dated artifact; it must not silently overwrite this 2026-08-28 view.
