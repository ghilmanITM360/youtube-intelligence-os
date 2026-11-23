# V1 Rent R9: claim verification and source register (2026-11-21)
Scope: every factual claim spoken or shown in `V1_RENT_FULL_R9_assembled.mp4`. Reconciled with `RESEARCH_DOSSIER.md` (C-01...C-23) and the three segment registers. "V" = verified against a primary page read this session or preserved data. Status words are about evidence, not about publication approval (owner and human checks still open).

## 1. Claims in the final narration
| Dossier | R9 time | Claim (on screen / spoken) | Evidence | Status |
|---|---|---|---|---|
| C-01 | 0-5 s | BLS rent of primary residence, 12 months to Sep 2026: +2.8% (index 450.402) | BLS CPI release Oct 14, 2026, Table 1 (read 2026-11-21; `evidence/bls/BLS_EVIDENCE_RECORD.md`) | V |
| C-02, C-15 | 5-11 s, 164 s | Zillow, Sep 2026, 12 months: 2.7% | Zillow September Rent Report page read 2026-11-21: "...2.7% from a year ago" (level $1,932 in that vintage, not shown) | V (upgraded from B) |
| C-03/04/05 | 44-64 s | Rent 7.7%, OER 25.9%, shelter 35.3% of CPI (Aug 2026 weights: 7.728 / 25.902 / 35.323) | BLS Oct 14 release Table 1, rows read 2026-11-21. Note: the factsheet shows Dec 2025 weights (rent 7.840, OER of residences 26.204, shelter 35.625). The video labels Aug 2026 weights on screen; the two vintages are never mixed. | V |
| C-06 | none | Sep 2026 weights differ (7.707, 25.853, 35.238) | BLS Nov 10 release; not shown | V (context) |
| C-07/C-08 | 75-122 s | Each sampled unit priced every 6 months; six panels; panel 1 Jan and Jul | BLS factsheet "Measuring Price Change in the CPI: Rent and Rental Equivalence", Last Modified Feb 13, 2026 | V |
| C-09 | ~110-122 s | Monthly change is the sixth root of the six-month relative; chained into the index | same factsheet, "Price Change" section | V |
| C-10 | 124-131 s | Vacant units are estimated from the average change of newly rented units | same factsheet, Imputation: vacant unit's previous rent times the average change of newly occupied units | V |
| C-11 | 131-135 s | Age adjustment on each new price | same factsheet: "an age-bias factor is applied to the previous rent" | V |
| (new) | 124-147 s | "BLS prices a fixed set of homes at six-month steps; not the average price on the market this week" | same factsheet: samples of units (usually 5 per segment), repriced every 6 months. Wording "fixed set of homes" = the same sampled units over time. | V |
| C-12 | 150-157 s | Zillow smoothed U.S. rent index Oct 2026 = $1,913 | ZORI CSV (sha a02ae5e8...12036, re-downloaded byte-identical): Oct 2026 1913.29. Zillow Oct report page read: "$1,913 in October, flat month-over-month" | V |
| C-13 | 157-161 s | A year earlier: $1,859 | ZORI CSV Oct 2025 1859.20 (same vintage). Screen says "from the Zillow data file (ZORI)". Not a figure Zillow prints in its report. | V (data file) |
| C-14 | 161-164 s | Rise of 2.9% | CSV: 1913.29/1859.20 = +2.91%. Dossier C-14: Zillow's own report says "Rents are now 2.9% up from last year" (recorded earlier; the second read of that page was denied this session) | V |
| (new) | 169-177 s | Zillow figure = level (dollars) + change in that level; BLS figure = change only | BLS publishes index levels and percent changes, not dollar rents (dossier C-21) | V |
| C-18 | 232-243 s | BLS printed no 12-month rent change in its October release; no Oct-to-Oct comparison | BLS Nov 10 release, "October 2026 12-Month Percent Changes": BLS did not collect October 2025 data (lapse in appropriations), so it cannot publish 12-month changes for October 2026 where Oct 2025 is missing. Rent: Oct 2026 index 451.486 was published (one-month +0.2%). R9 screen text now says so ("no October 2025 survey data (funding lapse)"). | V |
| C-16 | 226-231 s | BLS rent index +0.2% in October (one month) | Nov 10 release: 450.402 to 451.486, +0.2 | V |
| C-17 | 226-231 s | Zillow almost flat that month | Oct report: "flat month-over-month"; CSV Oct/Sep +0.008% | V |
| C-19 | removed | "matches the market measure today within a fraction of a point" | True for September only; cut from the audio (P1-1). The Sep comparison (2.8 vs 2.7, labelled "12 months to September 2026") remains at 216-226 s. | removed |
| C-09 caveat | 247-251 s | "The official rent number moves in six-month steps" | The BLS rent index is published monthly. Each unit is priced every six months and the monthly change is the sixth root of the six-month relative (C-09). "Moves in six-month steps" is shorthand for "built from six-month price observations". Accurate in spirit; flagged for the owner as a wording watch item (not changed: narration approved). | V with caveat |
| (new) | 210-217 s | "We looked for a BLS sentence that says CPI rent trails market rents. We did not find one." | BLS factsheet text searched for such a sentence: none found. Absence claim limited to that one page; not "BLS never said it". Screen now says "no such sentence in the BLS factsheet". | V (scope: one page) |
| C-20 | 5-11 s, tags | Zillow "typical market rent" (spoken) | Zillow's wording is "typical asking rent" in the report; the ZORI index is a smoothed repeat-rent index. On screen: "Zillow's smoothed U.S. rent index" / "(typical U.S. rent)". Low risk. | V with wording note |

## 2. Removed or never shown (do not reintroduce)
C-21 "BLS average rent $1,497" and C-22 "Zillow $2,131": not found in sources. Not in the recorded cut (S027-S049 block is in the removed 124.00-254.80 s audio of the original Take 2).

## 3. Zillow vintage rule
Zillow revises history. Every Zillow figure on screen comes from the single preserved CSV vintage (retrieved 2026-11-21) except the September 2.7%, which is the figure printed in Zillow's September report. No line mixes the September report level ($1,932) with the October level ($1,913).

## 4. Source register (URL, title, date accessed 2026-11-21, how read)
| # | Publisher / document | URL | Used for | Read how |
|---|---|---|---|---|
| 1 | BLS, Consumer Price Index News Release, September 2026 results (Oct 14, 2026) | https://www.bls.gov/news.release/archives/cpi_10142026.htm | 2.8%, index 450.402, weights | built-in browser, Table 1 rows |
| 2 | BLS, CPI News Release, October 2026 results (Nov 10, 2026) | https://www.bls.gov/news.release/archives/cpi_11102026.htm | +0.2% one month; no 12-month; Oct 2025 missing | built-in browser |
| 3 | BLS, "Measuring Price Change in the CPI: Rent and Rental Equivalence" (modified Feb 13, 2026) | https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm | six-month collection, panels, sixth root, vacancy, age, sample | built-in browser, full text |
| 4 | BLS, "October 2026 12-Month Percent Changes" notice | https://www.bls.gov/cpi/notices/2026/12m-changes-202610.htm | reason for missing 12-month change | built-in browser (title and passage match) |
| 5 | Zillow Research, ZORI data file (smoothed, all homes + multifamily, metro file, US row) | https://files.zillowstatic.com/research/public_csvs/zori/Metro_zori_uc_sfrcondomfr_sm_month.csv (page https://www.zillow.com/research/data/) | $1,913, $1,859, +2.9% | downloaded twice; sha256 a02ae5e8abaa692f411276fe75714c5148cae0a09cdaa687638241a86b212036; `evidence/zillow/` |
| 6 | Zillow Research, October Rent Report (Nov 12, 2026) | https://www.zillow.com/research/october-2026-rent-report/ | $1,913, flat m/m | built-in browser (one read; later 403) |
| 7 | Zillow Research, September Rent Report | https://www.zillow.com/research/september-2026-rent-report/ | 2.7% y/y | built-in browser |
| 8 | Zillow Research, ZORI methodology | https://www.zillow.com/research/methodology-zori-repeat-rent-27092/ | background only | 403 denied; NOT read, not used for any on-screen claim |

## 5. Title and description accuracy
Title: "Why Is Rent So High? How the Official Rent Number Is Measured". The video does explain how the BLS rent number is built and how it differs from Zillow's index; it does not answer "why rent is high" in a causal sense, and it says rent is high versus rent is rising are separate claims. Title implies BLS measures a sample, not every rental: the video says "a fixed set of homes" and the description repeats it. See `V1_RENT_YOUTUBE_PACKAGE_SCRIPT.md`.
