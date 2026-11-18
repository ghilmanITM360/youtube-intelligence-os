# Primary data pull (2026-11-18)

Labels: VERIFIED = read on the primary site today (by a fetch subagent; its report, not our own eyes); SECONDARY = news only; UNKNOWN = not obtained.

## 1. BLS rent methodology (VERIFIED, factsheet read in full; calculation page only first ~40k of 111k chars verbatim)
Source: bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm (last modified 2026-02-13), bls.gov/opub/hom/cpi/calculation.htm.
- Each sampled rental unit is priced "every 6 months" (reason given: rents are locked for a lease term).
- Sample is split into six panels; panel 1 is collected in January and July, panel 2 in February and August, and so on.
- Monthly change = sixth root of (current average rent / average rent 6 months earlier), chained monthly.
- Vacant units get an imputed change from newly occupied units; each repricing applies an aging adjustment.
- NOT found: any BLS sentence saying "CPI rent lags market rents". So "6-month collection cycle" is VERIFIED; "therefore CPI lags market rents" is still INFERRED (the lag size and direction depend on the data; do not state a number of months as fact).

## 2. IATA June 2026 outlook (VERIFIED, press release read; full report PDF and slide deck NOT read)
Source: iata.org press release No. 26, 2026-06-07, "Middle East Disruptions and High Fuel Prices Halve Airline Industry Profitability" (2025 = IATA estimate).
| Metric | 2026 forecast | 2025 est. |
|---|---|---|
| Net profit | $23.0B | $45B |
| Net margin | 2.0% | 4.2% |
| Net profit per passenger | $4.50 | $9.10 |
| Fuel bill | $350B | $252B |
| Jet fuel | $152/bbl | $90/bbl |
| Load factor | 84.0% | 83.5% |
Also: operating profit $48.0B (from $76.4B), revenue $1.165T, Brent assumed $95, jet crack spread $57, fuel 31.4% of costs, about one third hedged.
Corrections to earlier notes: 2025 net profit is $45B, not $41B ($41B was the earlier 2026 forecast); the 4.2% margin and $9.10 are 2025 figures, so "$4.50 a passenger" is correct for 2026. Fuel-bill rise is $98B ($350B minus $252B) = VERIFIED arithmetic on primary figures.

## 3. Market rent: Apartment List and Zillow (NOT obtained)
- apartmentlist.com: DNS error from the fetch tool. zillow.com/research/data: HTTP 403.
- Market-rent figures (Apartment List Sep 2026 $1,388, -0.1% m/m) remain SECONDARY. Title R1 "Rents Are Falling" and the thumbnail T-R1 stay blocked until a primary series is read (try via the browser tab or an owner-supplied export).

## 3b. BLS release tables opened by me in Chrome (audit pass, 2026-11-18, VERIFIED, own eyes)
Source: bls.gov/news.release/archives/cpi_10142026.htm (September 2026 CPI, released 2026-10-14), Table 1.
| Item | 12-month to Sep 2026 | Month (SA) |
|---|---:|---:|
| All items | 3.7% (Aug 12-month: 3.4%) | +0.6% |
| All items less food and energy | 2.6% | +0.3% |
| Shelter | 3.2% | +0.4% |
| **Rent of primary residence** | **2.8%** | +0.2% |
| Owners' equivalent rent | 3.3% | +0.3% |
| Airline fares | +22.4% | +1.2% (2.0% not seasonally adjusted) |
| Energy / gasoline | +20.4% / +34.2% | +5.2% / +9.1% |
Consequences: (1) the rent index itself is +2.8% a year, lower than shelter's 3.2%; the earlier notes quoted only shelter. Any "rent inflation" title must use 2.8%, not 3.2%. (2) An earlier note said shelter was "Aug 3.0%" (a secondary figure); the release does not state it and it is dropped. (3) BLS release notes: ~6,000 housing units and ~22,000 retail establishments priced; CPI is a sample with sampling error.
**Newer release exists:** the October 2026 CPI was published 2026-11-10 (bls.gov/news.release/cpi.nr0.htm, "2026 M10 Results"; next one, November, is due 2026-12-10). Summary page: all items +0.4% (month), shelter +0.3%, rent +0.2%, owners' equivalent rent +0.3%, energy +0.7%; the summary does not print 12-month rates, and airline fares are listed only as "increased". So the +22.4% airfare figure is the September one and is now superseded as "latest" by October data that I have not tabulated. Title numbers must be re-checked against the October table before use. Phase D/E used September as the latest: stale by one release.

## 3c. Follow-up reads (same day, VERIFIED, own eyes in Chrome)
- **October CPI full table** (bls.gov/news.release/archives/cpi_11102026.htm): no 12-month rates are printed (Oct 2025 comparison missing). Rent index 450.402 (Sep) to 451.486 (Oct), +0.2%; OER +0.3%; airline fares index 315.948 to 327.822, +3.8% not seasonally adjusted, +0.4% seasonally adjusted. So "+22.4%" stays the latest 12-month airfare figure (to September).
- **Zillow Observed Rent Index, US, smoothed** (files.zillowstatic.com/research/public_csvs/zori/Metro_zori_uc_sfrcondomfr_sm_month.csv): Sep 2025 $1,862.87; Sep 2026 $1,913.14 (+2.70%); Oct 2025 $1,859.20; Oct 2026 $1,913.29 (+2.91%); Oct vs Sep +0.01%. Zillow was reachable this time (earlier 403). **Consequence: market rent is NOT falling per Zillow; it rose about 2.7 to 2.9% a year, about the same as CPI rent (+2.8% to September).** The "two numbers disagree" premise for rent is NOT supported; titles R1, R3 and thumbnail T-R1 ("rents are falling") are dead, and the Apartment List -0.1% month (SECONDARY) is a different series. V1 is rebuilt as "what a rent number measures" (see the V1 script).
- Apartment List still not read (residency gate; not answered on the owner's behalf).

## 4. Effect on Phase E
- A1 and A3 numbers are now primary-backed (BLS airfares +22.4%, IATA $4.50 and $98B).
- R2 / T-R2: use "every six months" (verified fact), not "a year late"; avoid "lag" wording until the lag is shown from data.
- R1 / T-R1: still blocked on market-rent primary data.
- Still 0 approved, no scripts.
