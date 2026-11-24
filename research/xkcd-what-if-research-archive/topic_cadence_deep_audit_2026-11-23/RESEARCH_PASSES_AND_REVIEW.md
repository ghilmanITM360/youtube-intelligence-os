# RESEARCH_PASSES_AND_REVIEW — all review is SELF-REVIEW by one model (not independent)
| Pass | Done | Not done / limits |
|---|---|---|
| A inventory | 30 calendar rows traced; 23 video slots; scores recomputed | — |
| B discovery | question bank (63 units, REPORTED), prior audits' extras, 3 competitor channels found by search | no What If? 2; no comment mining; bank candidates WIB-30/32/34 not researched |
| C live windows | 17 topic groups × 30 queries × 5 YouTube filters (681 rows, retrieved 2026-11-23 ~21:15-21:45 PKT, gl=US, no cookies); Google Trends 12 terms × web/YouTube × 12-mo/3-mo (24 usable 12-mo series) | publish dates/views for search results NOT captured (HTTP 429); filters are YouTube's labels; "last 4 hours" = YouTube "last hour" filter only, titles only; Trends single-term series, each 0-100 vs own peak (not comparable between terms); no country comparison; Trends is an unofficial endpoint |
| D book/xkcd | question bank crosswalk for 13 topic ids; xkcd live listing reconciled to 92 IDs (0 missing, 0 reclassified) | book text unavailable (only SHA list); What If? 2 not checked |
| E packaging | directions for serious candidates | packaging PDFs not opened |
| F science | fall, neutron, orbit, tide ratio, light-day recomputed; Worden, Voyager, Apophis search-confirmed | no expert; WIB-22/24/NEW-07 not recomputed |
| G adversarial | saturation check found exact-title copies for NEW-06, NEW-08, WIB-18, WIB-53, NEW-07; found plane-on-every-planet absent; found audit1/audit2 disagreements; found WhatIfAnimations 433K vs 3.82K discrepancy; found that 10 of 13 topic ids are chapters of the printed book | no check of whether found titles are thin/AI content; no counterevidence hunt for WIB-36/17 beyond titles |
## What changed after each pass
- C changed NEW-06/NEW-08/WIB-53/WIB-18 to REPLACE (saturation) and downgraded WIB-22/T-01.
- D changed the collision story: the original "xkcd never made it" counts videos only; book chapters are the same questions.
- F changed WIB-55 wording (range not "at least").
## Verification run (scripts/verify_all.py, 11 checks, all PASS)
slot counts; schedule counts; XLSX=CSV cell-by-cell; score totals reproduce; every original bank id traced; inventory unique; 25 random cadence cells recomputed from inventory (0 mismatches). Weak spot: "every decision has evidence id" passes with `n/a` for 3 NEEDS-MORE-DATA rows. Not done: URL sampling of search results (YouTube 429), Trends reproducibility rerun.
## Open in this review
Prior-audit files not fully read (evidence register, competitor audit, limitations, next-steps, audit-1 xlsx); Day-14 plan claims rely on original-calendar dates.
