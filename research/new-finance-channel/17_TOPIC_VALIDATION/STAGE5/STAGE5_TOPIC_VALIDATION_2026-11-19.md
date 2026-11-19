# Stage 5 — Topic Validation (2026-11-19)

Scope: the 16 topics that advanced from Stage 4. Evidence: Stage 4 winners table (competitor URLs/views/dates are in `winners_2026-11-19.csv`); YouTube search (fetched 2026-11-19, ytInitialData); Google Trends US web search, past 12 months, read visually from charts (INFERRED, relative within each 5-term comparison, anchored on 'mortgage rates'); news by web search (secondary, some sources conflicting, marked UNVERIFIED).

## Limits
- Trends numbers are visual estimates, not exports; ratios to the anchor are approximate. Web-search phrase demand does not equal YouTube demand (RAM prices shows the conflict).
- News results were search summaries; several figures conflict (mortgage rate level, 10-year yield, Anthropic IPO) and are marked UNVERIFIED. Nothing here is a final fact for scripting.
- Framework evaluation: Stage 3 found no framework rule that survives correction; the framework therefore contributes cluster medians and checks, not predictions.
- Original-angle claims are hypotheses. No CTR, retention or revenue data exist.

## Decision summary

| ID | Topic | Decision |
|---|---|---|
| E01 | Housing lock-in: sellers outnumber buyers, prices hold | **GO** |
| E02 | Rent: why official rent inflation lags what you pay | **GO-CONDITIONAL** |
| E03 | Rates: how the 10-year/30-year yield hits a household | **GO** |
| E04 | National debt: the interest bill per household | **GO-CONDITIONAL** |
| E06 | Inflation basket: which prices are rising and which are not | **GO** |
| E07 | One price decomposed: why RAM/hardware got expensive | **GO-CONDITIONAL** |
| E08 | Airfares: what an airline ticket pays for (owner V2) | **GO-CONDITIONAL** |
| E09 | Fuel shocks: how a strait closure becomes a pump price | **HOLD** |
| E11 | Jobs report: what it measures and why it is revised | **GO** |
| E12 | Ageing economies: what a shrinking population does to growth | **HOLD** |
| F01 | AI companies: revenue-versus-spend arithmetic | **GO-CONDITIONAL** |
| F02 | How an IPO works and why mega-IPOs worry markets | **GO** |
| F04 | Crashes people forgot: one chart for 1929, 1973, 2000, 2008 | **GO** |
| F05 | AI boom vs dot-com and railroads: is the spending bigger? | **GO-CONDITIONAL** |
| F08 | How the credit-card fee system works | **GO-CONDITIONAL** |
| F10 | Japan, the yen and its bond market | **GO-CONDITIONAL** |

Counts: GO 6, GO-CONDITIONAL 8, HOLD 2

## E01 — Housing lock-in: sellers outnumber buyers, prices hold

- **Decision: GO** — Highest demand, timely data, competitor winners exist; needs a data angle that Casual Finance and the farm copies lack.
- Competitor evidence (six channels): Casual Finance 13 housing titles (long 2.42M, 738K); Monkey Economics mortgage Short 2.07M; MonkeyExplains housing-bubble long 276K (1.0x median). Source: Stage 4 winners table.
- YouTube search: ~10 near-duplicate videos in 3 weeks from tiny channels (1-111 views) copying the 58%-sellers-over-buyers angle: content-farm saturation, no strong recent big-channel video.
- Google Trends (US, 12 mo): 'mortgage rates' = the highest term in every batch (anchor, 1.0). Falling from ~100 to ~30 over 12 months. INFERRED, visual reading.
- News (2026-11): Existing-home sales at a 16-year low (RISMedia 2026-11-12); inventory 1.59M, 5.1 months supply, highest since Nov 2015 (NAR via RealEstateNews); prices mixed (NAR up, Redfin down). Rate level conflicts between sources (above 7% vs 6.3%): verify before scripting.
- Framework evaluation: Stage 3: housing cluster is covered by one channel only strongly (Casual Finance). No framework rule predicts success; topic cluster evidence only.
- Original angle (HYPOTHESIS): Lock-in by rate gap and metro, from FRED/Freddie Mac plus inventory series.

## E02 — Rent: why official rent inflation lags what you pay

- **Decision: GO-CONDITIONAL** — Low demand evidence; justified by owner theme, low competition and the data-artefact hook. Must be framed on the CPI artefact, not on the phrase 'rent inflation'.
- Competitor evidence (six channels): No video on rent in the six channels (0 titles). Indirect only: housing winners above.
- YouTube search: Best: Bloomberg 36.8K (3 yr), 62K (2 yr); recent videos from tiny channels (3-130 views). Low competition, modest proven demand.
- Google Trends (US, 12 mo): 'rent inflation' ~0.02 of the anchor (near floor). Search demand for this exact phrase is very low. INFERRED.
- News (2026-11): Oct 2026 CPI (released 2026-11-10): shelter +0.3% m/m, rent +0.2%, OER +0.3%; BLS could not publish 12-month changes for October because of missing Oct 2025 data after the 2025 shutdown, and warned rent lines are atypical. Next CPI 2026-12-10 (BLS). This is a real, checkable hook.
- Framework evaluation: No competitor winner and no framework support: owner-driven topic (V1). Not evidence-chosen.
- Original angle (HYPOTHESIS): CPI shelter method plus the missing-October-2025 artefact; Zillow ZORI for market rent.

## E03 — Rates: how the 10-year/30-year yield hits a household

- **Decision: GO** — Best-performing competitor cluster; moderate search demand; High saturation at Casual Finance means execution must differ; confirm the yield level first.
- Competitor evidence (six channels): Casual Finance 3 winners (1.43M-1.81M) among 8 rates titles; Monkey Economics and MonkeyExplains 4 more; Fed/rates cluster median PI 1.88x (highest in Stage 3).
- YouTube search: WSJ bond yields 1.43M (4 yr); Eurodollar University 52K (3 mo); '5% yield trap' 51.8K; others small.
- Google Trends (US, 12 mo): 'treasury yield' ~0.23 of anchor; jobs-report-level. INFERRED.
- News (2026-11): Search reports 10-year above 5.3% (highest since 2002) and mortgage above 7%, federal interest ~$1T in FY2026; yield figures are undated in the results and conflict with other mortgage-rate reports: UNVERIFIED. Treasury daily curve must be opened before use.
- Framework evaluation: Fed/rates cluster has the best cluster median in Stage 3 (1.88x), but cluster-level only and CF-dominated.
- Original angle (HYPOTHESIS): One yield move turned into mortgage, car loan and card payment, worked per release.

## E04 — National debt: the interest bill per household

- **Decision: GO-CONDITIONAL** — Big videos exist but the cluster is weak and large channels hold it; only worth doing with the interest-per-household angle.
- Competitor evidence (six channels): MonkeyExplains 1.92M breakout (7.0x); Casual Finance 119K and 88K; debt cluster median PI 0.21x: one-off breakout, weak cluster.
- YouTube search: National debt videos 1.98M, 2.73M, 1.2M (2 mo), Billionaire Files 286K (4 days); interest-specific: WSJ 28K, PBS 88K.
- Google Trends (US, 12 mo): 'national debt' ~0.25 of anchor. INFERRED.
- News (2026-11): Net interest ~$1T in FY2026, deficit ~$2T in 11 months, TD Securities projects $1.4T in FY2027 (search summaries, secondary).
- Framework evaluation: Stage 3: debt cluster 0.21x = weakest big cluster; the breakout was not repeatable.
- Original angle (HYPOTHESIS): Interest outlays vs defence, Medicare, education per household from the Monthly Treasury Statement.

## E06 — Inflation basket: which prices are rising and which are not

- **Decision: GO** — High search demand and a fresh data hook (missing annual rates).
- Competitor evidence (six channels): Monkey Economics 21.5K winner (2.1x); Casual Finance Short 389K (17.5x); Fed/rates/inflation cluster 1.88x.
- YouTube search: WSJ 366K (4 yr), Explains 101 686K (2 yr), Think Econ 68K; recent videos small.
- Google Trends (US, 12 mo): 'inflation' ~1.4x anchor; 'CPI' ~0.6x. Second-highest demand after mortgage rates. INFERRED.
- News (2026-11): Oct CPI +0.4% m/m, shelter >30% of the increase; BLS could not publish most 12-month changes (shutdown gap); last official annual rate Sept 3.7%; gasoline 12-month figure was published. Vanguard raised core forecast. Next CPI 2026-12-10.
- Framework evaluation: Cluster 1.88x; no rule evidence.
- Original angle (HYPOTHESIS): One chart per component for the latest release; explain the missing-October gap.

## E07 — One price decomposed: why RAM/hardware got expensive

- **Decision: GO-CONDITIONAL** — Strong news and views elsewhere, but tech channels own it and search demand is not shown; finance/economics framing (price mechanism) is the only reason to enter.
- Competitor evidence (six channels): MonkeyExplains only (688K, 2.5x).
- YouTube search: Linus Tech Tips 1.66M (10 mo), MonkeyExplains 692K, Infographics Show 570K, TechWiser 565K (3 wk), Lazy Assassin 218K: strong tech-channel competition.
- Google Trends (US, 12 mo): 'RAM prices' ~0 of anchor in US web search (floor). Conflicts with high YouTube views: unexplained, UNKNOWN (video demand may not show in web-search).
- News (2026-11): Counterpoint: Q3 2026 DRAM revenue ~$200B, +369% y/y, bit shipments +4%; TrendForce Q4 PC DRAM +13-18%; 32GB DDR5 kit $59 (Apr 2025) to $456 (Oct 2026); SK hynix says shortage could last to 2030; class action vs Samsung/SK hynix/Micron survived dismissal 2026-11-14.
- Framework evaluation: Single-channel winner, no framework support.
- Original angle (HYPOTHESIS): 'Who gets each dollar': DRAM contract price vs AI data-centre demand.

## E08 — Airfares: what an airline ticket pays for (owner V2)

- **Decision: GO-CONDITIONAL** — News hook is real but the V2 date is too late for a holiday angle; either move earlier or make it a fuel/capacity explainer. Owner decision.
- Competitor evidence (six channels): No video on airfares in the six channels (0 titles). No competitor winner.
- YouTube search: Wendover 5.0M (10 yr), Zerodha India 321K, The Hindu 151K (11 days), CNBC 92K; recent small.
- Google Trends (US, 12 mo): 'airfares' ~0.05 of anchor in the 12-month window. INFERRED.
- News (2026-11): Strongest news of the set: Hopper holiday index, domestic Thanksgiving round-trip $402 (+31%), Christmas $452 (+23%), decade highs; jet fuel record $4.90/gal 2026-10-22 (Argus via NPR); airlines cut capacity. TIMING: Thanksgiving is 2026-11-26 and the planned V2 date is 2026-12-21, after most holiday booking.
- Framework evaluation: No framework or competitor support.
- Original angle (HYPOTHESIS): BLS airline-fare CPI and IATA cost split; fuel pass-through.

## E09 — Fuel shocks: how a strait closure becomes a pump price

- **Decision: HOLD** — Weak cluster, news peak passing, mainstream competition. Earlier gasoline rejection stands.
- Competitor evidence (six channels): Capital Case 250K (4.6x), MonkeyExplains 283K, Casual Finance 137K; Iran/oil cluster median 0.62x.
- YouTube search: Spectrum News 1.31M (7 mo), Mr Global 52K, CBS 102K: mainstream news dominates.
- Google Trends (US, 12 mo): 'Strait of Hormuz' ~0.6x anchor with a spike. INFERRED.
- News (2026-11): Gasoline fell to $3.91 (2026-11-12, AAA via IER), Brent ~-21% since early November, EIA Nov STEO Brent ~$104; tankers still hit in the strait. The shock is easing, so the news peak has passed.
- Framework evaluation: Cluster 0.62x: weak.
- Original angle (HYPOTHESIS): EIA price decomposition.

## E11 — Jobs report: what it measures and why it is revised

- **Decision: GO** — Recurring monthly demand, low competition, repeatable format; competitor evidence is modest.
- Competitor evidence (six channels): MonkeyExplains 301K (1.1x); Monkey Economics careers 212K (20.7x, career-framed, not report mechanics).
- YouTube search: WSJ 84K (4 yr); recent tiny (3-136 views). Low competition.
- Google Trends (US, 12 mo): 'jobs report' ~0.22 of anchor. INFERRED.
- News (2026-11): Sept payrolls +29K, unemployment 4.2% (search result); Oct report was due 2026-11-06 (results not found: UNKNOWN); next release 2026-12-04.
- Framework evaluation: Jobs cluster small; no rule evidence.
- Original angle (HYPOTHESIS): Household vs payroll survey and revisions, using the actual release.

## E12 — Ageing economies: what a shrinking population does to growth

- **Decision: HOLD** — Evergreen reserve topic; large channels own it and no timing.
- Competitor evidence (six channels): MonkeyExplains 501K; Casual Finance Short 279K (12.5x).
- YouTube search: Kurzgesagt South Korea 16.0M (1 yr), FT Japan 3.15M, Infographics Japan 376K: top channels hold it.
- Google Trends (US, 12 mo): 'aging population' ~0.02 of anchor. INFERRED.
- News (2026-11): No time hook; evergreen. Only background sources found (fertility ~0.7-0.8 Korea; figures vary).
- Framework evaluation: China/other-countries cluster 1.48x.
- Original angle (HYPOTHESIS): Working-age population vs GDP per worker.

## F01 — AI companies: revenue-versus-spend arithmetic

- **Decision: GO-CONDITIONAL** — Highest demand and also highest saturation; only with a distinct filings-based angle.
- Competitor evidence (six channels): 5 channels, 28 long videos, 19.4M views, 7 winners (most saturated cluster).
- YouTube search: Infographics 1.59M, 643K, 343K; Bloomberg 496K; Vanessa Wingardh 925K: very saturated.
- Google Trends (US, 12 mo): 'OpenAI' ~2.8x anchor: highest demand in the set. INFERRED.
- News (2026-11): OpenAI/Anthropic combined ARR ~$150B (one source), Morgan Stanley capex-to-sales ~34% vs 32% dot-com peak. IPO status conflicting across sources: UNVERIFIED.
- Framework evaluation: Cluster 1.56x.
- Original angle (HYPOTHESIS): Capex per dollar of revenue from filings, per company.

## F02 — How an IPO works and why mega-IPOs worry markets

- **Decision: GO** — Competitor winners plus low recent competition; fact-check the live IPOs first.
- Competitor evidence (six channels): Casual Finance 1.71M, 1.46M, Short 145K; Crayon 1.12M; Capital Case 55K; cluster 1.25x.
- YouTube search: Plain Bagel 252K (7 yr), Yahoo 8K: low recent competition.
- Google Trends (US, 12 mo): 'IPO' ~1.1x anchor with a recent spike (term ambiguous). INFERRED.
- News (2026-11): Anthropic IPO timing/valuation conflicts (mid-Nov 2026 vs October; $965B vs $1.4T vs $2T); SpaceX reportedly priced $135 on 2026-06-11 with staged lock-ups to Nov/Dec (aggregator blogs). Facts unconfirmed: check SEC filings.
- Framework evaluation: Cluster 1.25x.
- Original angle (HYPOTHESIS): Lock-up, float, index inclusion with a worked example; no prediction.

## F04 — Crashes people forgot: one chart for 1929, 1973, 2000, 2008

- **Decision: GO** — Low recent competition, proven big winners for the topic; evergreen so no news dependency.
- Competitor evidence (six channels): 5 channels, 13 long videos, 6 winners, cluster 1.65x; Casual Finance 'nobody remembers' 1.28M.
- YouTube search: Mostly tiny (6-668 views); dedicated 2008 story 507K.
- Google Trends (US, 12 mo): 'stock market crash' ~0.1x anchor. INFERRED.
- News (2026-11): No time hook found; evergreen.
- Framework evaluation: Crisis-title family failed multiple-test correction in Stage 3 (HYPOTHESIS).
- Original angle (HYPOTHESIS): Common-axis drawdown and recovery for each crash.

## F05 — AI boom vs dot-com and railroads: is the spending bigger?

- **Decision: GO-CONDITIONAL** — Comparison angle is open but search demand for the phrase is near zero.
- Competitor evidence (six channels): Crayon dot-com 393K (1.3x), AI bubble 438K.
- YouTube search: Infographics 643K, CNBC 579K, Internet of Bugs 155K, Al Jazeera 58K.
- Google Trends (US, 12 mo): 'dot-com bubble' ~0.01x anchor. INFERRED.
- News (2026-11): Morgan Stanley capex-to-sales ~34% vs ~32% (secondary).
- Framework evaluation: Intersection of two top clusters.
- Original angle (HYPOTHESIS): Capex % of GDP across three booms.

## F08 — How the credit-card fee system works

- **Decision: GO-CONDITIONAL** — Evergreen, low competition, low proven demand.
- Competitor evidence (six channels): MonkeyExplains only (666K, 2.4x).
- YouTube search: WSJ 1.13M (4 yr), Visa 109K, others small.
- Google Trends (US, 12 mo): 'credit card fees' ~0.08x anchor. INFERRED.
- News (2026-11): Credit Card Competition Act reintroduced Jan 2026, stalled (July 2026); swipe fees $187.2B in 2024; no November 2026 news found.
- Framework evaluation: Single winner.
- Original angle (HYPOTHESIS): Where a $100 swipe goes.

## F10 — Japan, the yen and its bond market

- **Decision: GO-CONDITIONAL** — Timely (December BoJ meeting) but Casual Finance already owns it.
- Competitor evidence (six channels): Casual Finance long 779K (1.4x), Shorts 279K (12.5x), 16K.
- YouTube search: Bloomberg 696K (2 yr), Preet Banerjee 28K, Behind Asia 99K.
- Google Trends (US, 12 mo): 'yen carry trade' ~0.01x anchor. INFERRED.
- News (2026-11): BoJ held at 1.25% (Oct 29-30); Summary of Opinions out 2026-11-10; markets price ~76-85% chance of a December hike (rate level and date partly conflicting across sources).
- Framework evaluation: Casual Finance 11 Japan titles = saturated.
- Original angle (HYPOTHESIS): Carry trade as one number path; no forecast.
