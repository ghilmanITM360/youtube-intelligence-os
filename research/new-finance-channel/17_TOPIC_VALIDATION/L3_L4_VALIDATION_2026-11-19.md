# L3 / L4 validation (2026-11-19)
Labels: VERIFIED = opened by me in the built-in browser today. Method for YouTube: logged-out built-in browser (sidebar showed "Sign in", so not personalised), first ~10-20 results per query. Limits: one session, 3 queries per topic, US-facing results, view counts are a snapshot.

## L4 gasoline price split: result NOT APPROVED (filter 5 and 7 fail as drafted)
- Primary (VERIFIED, EIA gaspump_hist, released 2026-11-17): Aug-26 $4.058 = crude 50.3%, refining 24.4%, distribution+marketing 12.5%, taxes 12.9%; May-26 $4.479 = 51.9 / 21.7 / 14.8 / 11.5; Jan-26 $2.809 = 50.6 / 19.7 / 11.4 / 18.4. Distribution is a residual (EIA definition, search snippet).
- Our arithmetic (shares are rounded, so about +/-2 cents): tax per gallon was about $0.52 in Jan, May and Aug 2026 (0.517, 0.515, 0.523), so the tax SHARE fell from 18.4% to 11.5-12.9% only because the price rose. Crude per gallon went 1.42 -> 2.32 (May) -> 2.04 (Aug). This framing is ours, not seen in the results below.
- YouTube search "what is in a gallon of gasoline price breakdown": at least 11 videos in the last ~4 weeks use this same EIA table (titles like "Where Your $4.48 Gallon of Gas Actually Goes (2026)", "$4.29", "$4.30", "What You Really Pay For In A Gallon Of Gas"; channels Itemized, Dollargraph, Crude Logic, Plain Numbers, Behind The Barrel, Clackonomics, Turtle Money, Follow the Stash). Views 0 to 107 each; best older item "How Do Gas Prices Work?" 8K over 4 years.
- Verdict: saturated and templated (near-identical titles and data), with no demonstrated demand (max 107 views on fresh ones). Publishing the draft L4 would add a copy of the swarm = high AI-slop/originality risk. L4 REJECTED as drafted. Salvage only as the "tax is a flat ~52 cents, share fell because price rose" angle inside a different video, and only if a primary table is saved; not a slot.
- Shorts S5 and S7 (gas tax) inherit this: REJECTED unless reframed.

## L3 what the jobs number measures: CONDITIONAL
- Primary (VERIFIED, bls.gov/cps/cps_htgm.htm): about 60,000 eligible households, about 110,000 people a month; one quarter of the sample changes each month; 75% overlap month to month; interviews in the week with the 12th; 90 in 100 chance the monthly unemployment estimate is within about 300,000 of a full count (BLS notes it as a statement of precision). Not yet opened: payroll-survey page, response-rate source (one secondary site), GAO-26-107538. So those figures stay SECONDARY and must not be used until opened.
- YouTube (logged-out): "how the jobs report is made survey": WSJ "How to Read the Jobs Report" 83K (4 yr), Schwab 17K (2 yr), Decode Econ 1.7K, Scripps 228; fresh items 2 to 135 views. "why jobs report gets revised": ClearValue Tax "The Jobs Report is Much Worse Than It Looks" 492K (1 mo), ABC11 13K, ABC News 7.4K, rest under 800. Method-only explainers are thin in supply but also low in views; high views come from news-hook framing.
- DB: 0 of 3,832 competitor videos on the topic (our set only).
- Verdict: no copy swarm (good), demand for pure method is weak (hypothesis: needs a news hook). Keep as CONDITIONAL with changed angle: tie the method to a live release (Employment Situation) and revisions, state method only, no forecasts. Needs: open payroll survey page, GAO report, next release date, Trends.

## Filters (L3 / L4)
| Filter | L3 | L4 |
|---|---|---|
| 1 competitor evidence (DB) | none in our set; outlier pattern "why does X work" supports format | none; pattern same |
| 2 historical performance | news-hook jobs videos get 10K-500K; method explainers 0.2K-83K | fresh gas-split videos 0-107 views |
| 3 news | Oct jobs report (165,000 after 29,000 in Sep) is covered by others; not opened by me | gas $4+ is in the news |
| 4 Trends | NOT RUN (browser Trends read not attempted) | NOT RUN |
| 5 YouTube search | thin supply, low views | saturated, identical template |
| 6 Suggested | not measured (UNKNOWN) | not measured |
| 7 gap | method + revisions plus sampling is open; needs hook | gap closed by the swarm |
| Result | CONDITIONAL | REJECTED as drafted |

## Consequence for the calendar
L4 (Mon 2027-01-04) returns to NO TOPIC; S5 and S7 return to NO TOPIC. L3 stays candidate-conditional. Topic-backed slots: L1, L2 (conditional), L3 (conditional), L5, S4, S6 (candidates) = 6 of 13; validated 0. Honest score for REQ-025 does not change from FAIL.
Next if approved: open the BLS payroll page and the GAO report, run Trends, find a different L4 (the "why does X work" pattern with a primary dataset and no swarm; check the YouTube swarm first this time).

---
# ROUND 2 (same day): L3 finished, new L4 found

## L3 jobs number: primary sources opened, Trends run
VERIFIED today (own eyes, built-in browser):
- BLS Employment Situation technical note (2026 M10): household survey about 60,000 eligible households (Census for BLS); establishment survey (CES) about 119,000 businesses and government agencies, about 622,000 worksites, about 26% of all nonfarm payroll jobs; birth-death modelling (imputation plus an ARIMA model) for new firms; benchmark revision: 10-year absolute average 0.2%, range -0.4% to +0.3%; **90% confidence interval for the monthly change in nonfarm payrolls is on the order of plus or minus 122,000.**
- BLS CPS page: about 110,000 people a month, one quarter of households replaced each month, 90-in-100 chance unemployment estimate within about 300,000 of a full count.
- GAO-26-107538 (published 2026-06-02): stakeholders say the report generally meets needs but occasional large revisions reduce usefulness; response rates have fallen (shown in a figure, not in text I could read); BLS met its precision and revision goals FY2020-2025 (relaxed one goal during COVID); agency studies found limited effects of lower response on household data; BLS has not released its establishment-survey nonresponse assessment; an online response option is planned for 2027 but funding may delay it. **The "61% to 42.6%" response-rate numbers from a secondary site are NOT verified: do not use them.**
- BLS release schedule: Employment Situation Dec 4, 2026 (Nov data), **Jan 8, 2027 (Dec data)**, Feb 5, 2027.
Trends (Google Trends, US, past 12 months, read by eye in the built-in browser):
- Web Search: "jobs report" stays low (about 5 to 12 on a 0-100 scale shared with "gas prices"; gas prices peaked at 100 and spiked again later; bar average jobs report roughly one sixth of gas prices).
- YouTube Search: "jobs report" is spiky, repeating peaks roughly monthly (up to 100, many weeks near 0), consistent with release days; "how unemployment is calculated" is flat near 0. Reading: demand follows the release; there is no standing search demand for the method. (Visual reading; causality with release dates not tested.)
Verdict: **L3 CONDITIONAL (strengthened).** Primary sources now cover every number. Must be published right after a release (Jan 8, 2027 => Mon 2027-01-11) and titled around the jobs report, not "how unemployment is calculated". Safe statement-of-method hook: the payroll change carries about plus or minus 122,000 at 90% confidence, so a month's headline change can sit inside the noise. Do NOT cite the Sep/Oct 2026 payroll values until the BLS tables are opened (seen only in YouTube snippets). Open: Trends for the exact title phrase, owner voice policy, script not written.

## New L4: "the shutdown hole in the CPI basket": CONDITIONAL
Why a new topic: generic "why is X expensive" topics are swarmed. Checked "why car insurance premiums keep rising": 14+ fresh near-identical videos (0 to 190 views). CPI "how it is calculated" has big old videos (WSJ 365K, JPMorgan 1.2M, Econ in Many Lessons 404K, EconplusDal 215K) but fresh ones are tiny, and V1/S6 already use the basket weights. So L4 must not be another "what is the CPI".
Candidate: **how BLS patched the missing October and November 2025 Consumer Expenditure Survey data (government-shutdown lapse), what that does to the 2027 CPI spending weights, and what the weight update in February 2027 changes.** VERIFIED (BLS 2027 CPI Weight Information page, last modified 2026-07-30): CE survey data were not collected in Oct and Nov 2025; BLS considered three approaches (survey weight adjustments, unit-level modelling, domain-level modelling incl. interpolation, ARIMA, ESN), consulted NABE and CNSTAT expert panels, and plans a survey-weight adjustment for CPI-U and CPI-W (Interview Survey: July and October 2025 expenditures x3 for the 1/3 shortfall, Aug and September x3/2 for the 2/3 shortfall; for the C-CPI-U, October weights copy September and November copy December); release planned February 2027 as scheduled.
YouTube supply (logged-out): query "shutdown missing data CPI weights consumer expenditure survey" returned 9 results; none explains the weights patch. Nearest: BLS's own "CPI imputation: not just a guess" (1.4K), October 2026 "no yearly inflation number" news explainers (8 to 83 views, 7 to 10 days old), shutdown CPI news (133 to 1.8K, 1 year old). No swarm; but also no proven demand (Trends not run for this phrase; likely low).
Risks: dry topic, audience small; I have not verified WHY the October 2026 table lacks 12-month rates (the news videos assert a link; BLS release not read for that sentence); do not state it until read. Technical wording must be checked by a human (C5).
Status: CONDITIONAL. A "What is inside the basket, and how a hole in the data is patched" video fits the pillar "how official statistics are built". Demand is a hypothesis; test with 1 Short first (see S7/S4 pattern).

## Calendar update (supersedes earlier L-slot mapping in the addendum)
| Date | Slot | Topic | Status |
|---|---|---|---|
| Mon 2026-12-28 | L3-new | CPI basket + shutdown hole (new L4 topic) | CONDITIONAL |
| Mon 2027-01-04 | former L4 | no topic (gas rejected) | NO TOPIC |
| Mon 2027-01-11 | L3 | jobs report: what the number measures (after Jan 8 release) | CONDITIONAL |
| Thu 2027-01-14 | L5 | December CPI (released Wed 01-13) | CANDIDATE |
| Shorts S4 (60,000 homes), S6 (housing 35.3% weight), new S7 (payroll change carries about plus or minus 122,000 at 90% confidence) | | each own hook, VERIFIED facts | CANDIDATE |
S5 (gas tax) and S8 stay NO TOPIC. Topic-backed 8 of 13 (L1, L2, L3, L-Dec28 conditional; L5, S4, S6, S7 candidates); validated 0. Weekdays: 2026-12-28 Mon, 2027-01-04 Mon, 2027-01-11 Mon, 2027-01-14 Thu (python-checked earlier for the Jan dates; Dec 28 follows from Dec 14 Monday plus 14 days).
