# Topic, demand and publication timing

All 966 canonical titles received overlapping provisional keyword labels; 30 received contextual transcript interpretation. **936 still lack semantic review.** “Economics” in a business-model title does not prove macroeconomics, and a date/year does not prove news-driven demand. See [semantic labels](SEMANTIC_REVIEWS.csv), [video source rows](VIDEO_MASTER.csv) and [methods](METHODS.md). Most reviewed money-status stories are enduring scenarios; this is an editorial classification, not measured search demand.

## Clusters with useful evidence

- **Institutional mechanisms with personal stakes:** bank service tiers (`2LXED3ENhck`), credit-card interest (`QvaHDxdxQFg`), hidden financial fragility (`UB-UphJ0omU`). The first is a reach outlier; the second typical; the third unrankable. Useful research territory, not uniformly strong performance.
- **Small actions, long consequences:** Sonny's `$5/day` (`vb7UojsINvg`) is strong, Shaami's similar question (`ENUs_Bzh2lI`) typical. Repeated topic availability is supported; universal success is not.
- **Economic systems behind familiar objects:** Brimm. airline layout (`m5WPi3LX9z0`) strong versus Walmart/Amazon (`IOBcBqb6igM`) weak and IKEA (`6-pxbfLfGGU`) typical. Hidden mechanism specificity is a testable interpretation.
- **Financial history:** inherited Casually Finance 1973 crash (`DKyJABtbF2o`) and Casual Economics Great Depression (`qF3ekm9Gx_E`) outperform their respective baselines. The Europe Depression follow-up (`VTx478EUybo`) is weak and Crayon's crisis compilation (`KHLY6SyLvgQ`) weak. A narrow event/problem may be more useful than a generic history label; evidence is observational.
- **Status/wealth scenarios:** several winners, but near-identical sampled structures also appear in weak videos. This is already crowded within the supplied corpus. No conclusion that the entire niche is saturated.

## Reused Google Trends evidence

No redundant Trends download was performed. Reuse exact blobs **REUSE-09** (TRENDS_WINDOWS.csv) and **REUSE-10** (TRENDS_RAW.json) in [REUSED_SOURCE_REGISTER.csv](REUSED_SOURCE_REGISTER.csv). The register retains commit, blob hash and immutable URL. Twenty-two window rows cover eleven videos, each with one query per request and both YouTube/web search. Geography WORLDWIDE; the original fetch occurred 2026-10-14 18:16–18:19 UTC. Values are normalized 0–100 **within each request**; 100 is that request's maximum, not search volume. Different windows/terms cannot be numerically ranked against each other.

| Example | Query / search / period | Observed within-request values | Interpretation |
|---|---|---|---|
| Strong evergreen history: `qF3ekm9Gx_E`, published 2025-03-19 | great depression; YouTube; WORLDWIDE; 2024-12-19–2025-05-18; fetched 2026-10-14T18:16:59Z | Mean days -30 to -8 =35.7; -7 to -1 =40.7; publication week =35.1; peak 100 on 2025-04-09 | The peak was **after** publication. A later attention cycle may matter, but views cannot be attributed to search. |
| Elevated interest, weak video: `VTx478EUybo`, 2025-11-11 | great depression; YouTube; WORLDWIDE; 2025-08-13–2026-01-10; fetched 2026-10-14T18:19:11Z | Mean -30 to -8 =51.0; -7 to -1 =74.9; publication week =63.1; peak 100 on 2025-11-05 | Higher local prepublication interest coexists with weak public performance. This is the requested counterexample to a simplistic trend→views claim. |
| Strong historical story without a publication peak: `Iwz0fhJWN9Q`, 2026-07-29 | the big short; YouTube; WORLDWIDE; 2026-04-30–2026-09-27; fetched 2026-10-14T18:18:19Z | Mean -30 to -8 =59.9; -7 to -1 =66.9; publication week =62.3; peak 2026-06-01 | Existing evergreen/pop-culture interest is compatible with success; no verified fresh event trigger. |
| Inadequate search evidence: `x_MZu-QF-6o` | japan lost decade; YouTube; WORLDWIDE; 2025-03-13–2025-08-10; fetched 2026-10-14T18:17:25Z | 99% zero share; web request NO_POINTS | Do not interpret zeros as no audience demand. |

The Europe query is broad and not specific to the video's European angle. Series may be sampled by Google. No traffic-source data links these searches to those viewers. This is inherited data checked for provenance and internal interpretation, not a fresh independent replication.

## Event chronology

The [March 19, 2025 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20250319a.htm) shares the Great Depression video's publication date. That coincidence alone does not establish a connection. The [April 2, 2025 tariff order](https://www.whitehouse.gov/presidential-actions/2025/04/regulating-imports-with-a-reciprocal-tariff-to-rectify-trade-practices-that-contribute-to-large-and-persistent-annual-united-states-goods-trade-deficits/) came **14 days later**, before the reused April Trends peaks. It therefore cannot be described as a preceding publication trigger. Both primary sources checked 2026-10-16.

Inherited Casually Finance evidence ties housing publication `Uumnx2Fo6cE` (2026-09-29) to a Redfin report first dated September 10 and updated September 25. This establishes available context, not search demand or creator motivation. MicroStrategy `dlBhLhn8lL0` is weak despite preceding company news. See REUSE-05 and the original source checks it cites. No new verification of those financial claims is claimed here.

## News-reactive research queue

Track a rate, housing, credit or trade-policy announcement only when it changes a concrete mechanism. Separate announcement date, effective date, observation period and video publication. Ask “what changes for whom?” and pair it with an evergreen explainer of the mechanism. Do not infer an optimal weekday/hour from one historical snapshot. New-channel publication schedule is a production experiment, not an algorithm rule.
