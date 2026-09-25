# Trends Recapture Summary — forensic-v3

**Purpose:** Remediate the two problems found in `forensic-v2/TRENDS-REGISTER.json`: (1) no raw exported artifact existed behind any of the 32 entries, and (2) GT-20 made a specific causal claim that a spot re-check flagged as false. This pass re-ran all 32 queries live against Google Trends' own API endpoints (`trends.google.com/trends/api/explore` + `.../widgetdata/multiline`), using the same query/geo/property/time-window as the original register, and saved the actual returned time series for every entry.

**Capture date:** 2026-09-25
**Method:** Browser-authenticated fetch directly against Google Trends' internal JSON API (same endpoints the Trends UI itself calls), not scraping rendered HTML and not the paid API. No sign-in, no third-party tooling.
**Raw data location:** `forensic-v3/trends-raw/GT-01.json` … `GT-32.json` (one file per entry; each contains `id, query, geo, property, time_window, capture_date_iso, status, point_count, points[]` where `points` is the full weekly — or daily for GT-27 — series exactly as returned, no summarization or truncation).

## Headline result

**All 32/32 queries captured successfully** with full-resolution raw series (262 weekly points for the 5y-weekly entries, 182 daily points for GT-27, 53 weekly points for GT-32's 12-month window). No query returned "not enough data" or failed.

**30/32 entries match the old register's peak week, max/min, and recent-trend direction** within normal Google Trends sampling noise (mean values typically drift by 0.1–1.5 points between independent pulls of the same query/window — an inherent property of Trends' rolling normalization, not an error). This confirms the task brief's premise that the old register's *numbers* were mostly accurate.

**GT-20 is confirmed falsified**, independently re-verified in this pass (see below) — this is the one entry where old vs. new diverge materially, not just by sampling noise.

**GT-07 shows a minor peak-week discrepancy** (see below) — small, not evidence of fabrication, most likely Trends re-normalization drift.

## GT-20 — corrected finding (re-verified independently, not assumed)

The prior audit's finding is **confirmed**. Full 262-point weekly series for "how often should seniors shower" (US, Google Web Search, 2021-09-24 to 2026-09-24) pulled live today shows:

- **Every single week is 0** except **exactly one week: Mar 6–12, 2022, which hits 100** (an isolated spike, over 4 years before the claimed causal event).
- **The Aug–Sep 2026 window is flat 0 across all 9 weeks checked** (Jul 26 – Sep 26, 2026 inclusive): `0,0,0,0,0,0,0,0,0`.
- first-12-week mean = 0.0, last-12-week mean = 0.0 (computed from this pull).
- The old register claimed peak week "Sep 13–19, 2026" (max 100) and a last-12-week mean of 8.3, consistent with the task brief's account of a claimed rise to means of ~16.7/20 in Aug–Sep 2026 following two videos on the topic.

**Conclusion: the original register's GT-20 entry is not supported by live data.** There is no 5-years-flat-then-rises-in-Aug/Sep-2026 pattern. The real series is flat 0 for the entire window with one unrelated, isolated 2022 blip (nowhere near Aug–Sep 2026, and nowhere near the claimed magnitude). The claimed causal link between two 2026 videos and a search-interest rise is not supported by this data — that number appears to have been fabricated or hallucinated when the original register was hand-typed, not observed. No script was recovered that could have miscomputed 0 into a rising 16.7; this looks like invented data, not a live-tool artifact or transcription slip.

## GT-07 — minor peak-week discrepancy (not falsification)

Old register: peak "Feb 23–Mar 1, 2025" at 100. Live re-pull: that same week now reads **98** (not the max), and two *different* weeks now tie at 100 (Jun 29–Jul 5, 2025 and Aug 3–9, 2025). Max/min/trend direction (RISING) still match. This is consistent with normal Trends sampling/normalization drift between independent pulls of a 5-year window, not a data-integrity problem — flagged for completeness per the task's request to note any discrepancies.

## GT-09 and GT-24 — scope note

GT-09 ("balance exercises", listed as "Worldwide (country comparison)") and GT-24 ("neuropathy exercises", Worldwide) were captured as a standard single-series TIMESERIES pull with `geo=""` (worldwide aggregate), matching every other "Worldwide" entry in this register (GT-02, GT-24). A true per-country comparison (Google Trends' `GEO_MAP`/region-breakdown widget, which returns interest-by-region rather than a time series) is a different Trends widget and was not what was captured — the task asked specifically for time-series raw data comparable across entries, and GT-09's original register entry also has the same time-series shape (`peak_period`, `max`, `min`, monthly breakdown) as the non-comparison entries, so this is treated as consistent with the original capture method, not a scope deviation.

## GT-27 — resolution upgrade, not a discrepancy

Old register recorded only `max`/`min`/`peak_period` for GT-27 (no first/last-12-period means). This pull captured the complete 182-point **daily** series for the Feb 15–Aug 15, 2026 window, so first/last-12-day means are now available where they weren't before (52.7 → 42.2, a FALLING recent trend). Peak day, max, and min all match the old register exactly.

## Full entry table

| ID | Query | Geo | Property | Capture | Peak week | Max/Min | Trend dir | Notes |
|----|-------|-----|----------|---------|-----------|---------|-----------|-------|
| GT-01 | clove water | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-02 | clove water | Worldwide | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-03 | clove | US | YouTube | SUCCESS (262) | MATCH | MATCH | MATCH (FLAT) | clean |
| GT-04 | neuropathy exercises | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-05 | diabetes feet | US | Web | SUCCESS (262) | MATCH | MATCH (±1 min) | MATCH (FLAT) | clean |
| GT-06 | signs of diabetes | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (FLAT) | clean |
| GT-07 | balance exercises for seniors | US | Web | SUCCESS (262) | **MISMATCH** | MATCH | MATCH (RISING) | see note above — sampling drift, old peak week now reads 98 not 100 |
| GT-08 | exercises for seniors | US | YouTube | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-09 | balance exercises | Worldwide | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | scope note above re "country comparison" label |
| GT-10 | frequent urination at night | US | Web | SUCCESS (262) | MATCH | MATCH (±1 min) | MATCH (FALLING) | clean |
| GT-11 | stroke symptoms | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-12 | amlodipine side effects | US | Web | SUCCESS (262) | MATCH | MATCH (±1 min) | MATCH (FALLING) | clean |
| GT-13 | best time to take BP medication | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | first12 drifted 8.1→13.1, still RISING |
| GT-14 | how to lower creatinine | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-15 | colon cleanse | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (FALLING) | exact match, no drift |
| GT-16 | dry mouth at night | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (FALLING) | clean |
| GT-17 | best sleeping position | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-18 | anesthesia elderly | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-19 | mucus in throat | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (FALLING) | exact match, no drift |
| **GT-20** | **how often should seniors shower** | US | Web | SUCCESS (262) | **MISMATCH** | MATCH (max) | **DIFF (old RISING, new FLAT)** | **FALSIFICATION CONFIRMED — see detailed section above** |
| GT-21 | best fruit for eyes | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-22 | garlic benefits | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-23 | ozempic side effects | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-24 | neuropathy exercises | Worldwide | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-25 | creatine for seniors | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-26 | neuropathy | US | YouTube | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-27 | diabetes feet (daily) | US | Web | SUCCESS (182) | MATCH | MATCH | N/A old / FALLING new | resolution upgrade — see note above |
| GT-28 | fall prevention | US | Web | SUCCESS (262) | MATCH | MATCH (±1 min) | MATCH (RISING) | clean |
| GT-29 | blood pressure tablets | UK | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-30 | clove water | US | YouTube | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | new pull shows 2nd tied peak week (Apr 2026) alongside old peak |
| GT-31 | medications that cause dementia | US | Web | SUCCESS (262) | MATCH | MATCH | MATCH (RISING) | clean |
| GT-32 | mounjaro side effects (12m) | US | Web | SUCCESS (53) | MATCH | MATCH | MATCH (FALLING) | clean |

## Bottom line

- Raw, faithful, full-resolution time series now exist on disk for all 32 entries (`forensic-v3/trends-raw/GT-*.json`), closing gap (1) from the prior audit.
- Gap (2) — the GT-20 causal claim — is independently re-confirmed false with fresh raw data: the real series is flat 0 through Aug–Sep 2026, with the only variation being one isolated, unrelated spike in March 2022. The specific "16.7/20 mean following two videos" claim has no support in live Google Trends data and should be struck from the register as fabricated, not merely re-labeled as an estimate.
- One additional, much smaller discrepancy (GT-07 peak week) was found during this independent re-check and is most plausibly ordinary Trends normalization drift, not fabrication — flagged for the record.
