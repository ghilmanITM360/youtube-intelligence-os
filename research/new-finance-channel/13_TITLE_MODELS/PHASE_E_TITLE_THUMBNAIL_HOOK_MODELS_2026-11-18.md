# Phase E: title, thumbnail and hook models (2026-11-18)

No scripts. Candidate titles, thumbnail briefs and hook structures only, for the two CONDITIONAL topics from Phase D. Everything here is a HYPOTHESIS until tested on our own channel (Studio CTR and watch time are UNKNOWN for competitors and for us).

## 1. What the data says about title formulas (VERIFIED, within-channel)
Script: `title_features.py` (read-only on the DB). 64 channels with 8+ long videos (Mr. Finance excluded), videos 14+ days old; "top" = at least 2x the channel's own long-form median (937 videos), "low" = below median (1,587).

| Title feature | Share of top videos | Share of below-median videos |
|---|---:|---:|
| has a number | 57% | 51% |
| colon or dash | 37% | 30% |
| has $ or % | 20% | 17% |
| ALL-CAPS word | 27% | 26% |
| starts Why/How/What | 19% | 19% |
| question mark | 9% | 10% |
| under 50 characters | 28% | 30% |
| "really/actually/truth/secret" | 8% | 10% |
| you/your | 48% | 52% |

Reading: no title feature separates winners from losers by more than 7 points (colon 37 vs 30, number 57 vs 51; recomputed in the 2026-11-18 audit, identical output). The sets are groups of videos, not independent trials, and 89 titles repeat across channels. **A title formula is not what makes a video outperform its channel** (INFERRED, correlation only; topic, thumbnail and channel size are not controlled). So the plan is a few honest, specific titles per topic, tested, not a template. A rigid template would also add channel-level "mass-produced" risk (Phase A).

UPDATE (primary pull, see `09_TOPIC_DISCOVERY/PRIMARY_DATA_PULL_2026-11-18.md`): BLS prices each rental unit every 6 months (VERIFIED); the lag claim stays INFERRED. IATA press release read: $4.50 per passenger and $350B vs $252B fuel bill (so $98B) are now VERIFIED. Market rent (Apartment List/Zillow) NOT obtained: R1 and T-R1 are blocked.

## 2. Title candidates (to A/B test in Studio, long-form only; Shorts cannot be A/B tested)
Rules used: states the concrete contradiction; numbers only when VERIFIED; no clickbait that the video cannot pay off; no claim without a primary source.

**Topic R: rent (durable)**
| id | Title | Why |
|---|---|---|
| R1 | Rents Are Falling. So Why Is Your Rent Still Rising? | the contradiction in one line; matches "why is rent so" search phrase |
| R2 | ~~Why Is Rent So High? The Number the Government Uses Is a Year Late~~ WITHDRAWN (wrong: BLS re-prices each unit every 6 months). Replacement R2b: Why Is Rent So High? The Official Rent Number Is Only Re-Priced Every Six Months | search phrase first, VERIFIED mechanism (BLS factsheet); does not claim a lag size |
| R3 | Rent Is Down. Rent Inflation Is Up. Both Are True. | BLOCKED like R1: "rent is down" rests on SECONDARY Apartment List summaries, and we have no primary 12-month figure for the CPI rent index itself (only shelter +3.2%) |
CORRECTION HISTORY (final state after the 2026-11-18 audit): (1) the first draft said "a Year Late"; (2) a search-snippet check said "about six months late"; (3) the primary pull read the BLS factsheet: each unit is re-priced every 6 months (VERIFIED), but no BLS sentence says CPI rent "lags" market rent, so any lag wording stays INFERRED. Current rule: use "re-priced every six months", never "late" or "a year". The earlier note that profit fell "from $41B" is also corrected: $41B was IATA's earlier 2026 forecast; 2025 net profit is $45B and 2026 is forecast at $23.0B (press release No. 26, 2026-06-07).
Claim status before any use: R1 and R3 need an Apartment List/Zillow primary series (market rent falling = SECONDARY today) and a primary CPI rent-index 12-month figure. R2b can be used now, with the BLS factsheet on screen.
Search phrase "why is rent so high" is kept in R1/R2 because it is the top autocomplete suggestion.

**Topic A: airfares (news, time-boxed)**
| id | Title | Why |
|---|---|---|
| A1 | Airfares Are Up 22%. Airlines Are Forecast to Make $4.50 a Passenger. | two numbers, one tension; 22.4% (BLS) and $4.50 (IATA press release, a 2026 FORECAST, so "forecast" must stay in the title) both VERIFIED; the BLS fare index is a sample, not every ticket |
| A2 | Why Are Flights So Expensive Right Now? Follow One $400 Ticket | matches search phrase; "follow one ticket" is the visual device |
| A3 | Airlines' Fuel Bill Is Forecast to Rise $98 Billion. Who Pays It? | $252B (2025 estimate) to $350B (2026 forecast), IATA press release, VERIFIED; "$98B" is our subtraction; both years are IATA estimates/forecasts, not audited results |

## 3. Thumbnail briefs (original, not copying any reference channel)
Reference channels' common devices (Phase B): one dominant word or number, one emotion, one concrete object, a real chart with a date. Crayon, Capital Case, Paper Billions share a round-head cartoon look; **we must not copy it**. Brief constraints: own colour palette and layout decided in Phase I; real data chart, not stock art; text in the thumbnail differs from the title; max 4 words.

| id | Concept | Text | Check |
|---|---|---|---|
| T-R1 | Two lines on one chart: market rent flat/down vs CPI rent rising; a single rent-ticket icon | "RENT: DOWN. RENT CPI: UP" | needs the Apartment List and BLS series pulled first |
| T-R2 | A calendar with two pages six months apart and one rent number between them | "EVERY 6 MONTHS" (replaces "A YEAR LATE", which was wrong) | do not imitate a real agency logo |
| T-A1 | One boarding pass split into slices: fuel, crew, planes, profit ($4.50 slice tiny) | "$4.50" | numbers verified before use |
| T-A2 | Chart of BLS airfare index with the +22.4% marked | "+22%" | |
Claim status: A2 "$400 ticket" is ILLUSTRATIVE, not a data point; use a real fare sample (source and date on screen) or drop the number. A3 "$98 billion" = $350B minus $252B, both IATA press-release figures (VERIFIED), subtraction ours.
Legibility test at phone size (about 120 px wide) and a blur test before any publish (HYPOTHESIS: reference thumbnails pass both; not measured here).

## 4. Hook models (structures, not scripts)
From Phase B openings: Casual Finance opens with a precise number then a contradiction; Crayon with a dated scene; Paper Billions with a place and moment.
- **H1 contradiction first (rent):** the verified figure (+3.2% shelter, which includes owners' equivalent rent and is NOT the rent index; use the rent-index figure once read; market rent flat/falling only after a primary series) then "both are true". Payoff promised in the first 30 seconds: one mechanism.
- **H2 one object (airfares):** name one ticket and one price, then split it. Payoff: where each dollar goes.
- Avoid: greeting, channel intro, "in this video"; question-only openings (only 9% of top titles are questions, and hooks that ask a question carry no number).
- Every number in a hook needs a source on screen (policy: not a news read-out).

## 5. Validation plan (what Phase E cannot do)
1. Before publishing: pull Apartment List/Zillow primary series, BLS methodology page on shelter, IATA table text; fix SECONDARY numbers.
2. After publishing: run YouTube's A/B test on titles and thumbnails (up to 3, winner by watch time, desktop Studio, about 2 weeks, official page 16391400).
3. Record Studio impressions, CTR, retention, traffic mix per video; compare only within our own channel.
4. Kill rule (HYPOTHESIS): if two of two Phase E topics show weak impressions after 28 days, return to Phase C and test the TEST-ONLY cluster.

## 6. Status
Titles: 6 candidates plus the replacement R2b (R2 withdrawn; R1 and R3 blocked), 0 approved. Thumbnails: 4 briefs, none designed. Hooks: 2 models. No script written; scripts stay on hold until the owner approves titles and thumbnails. Known limit: public data cannot tell us which candidate wins.
