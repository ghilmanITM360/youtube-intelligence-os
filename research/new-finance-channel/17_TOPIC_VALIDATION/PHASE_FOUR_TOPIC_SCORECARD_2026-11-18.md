# Phase Four: topic scoring and final selection (master "Phase Four"), 2026-11-18

Status: scoring of the 12 topic groups that had real evidence in Phases C and D. Nothing is approved. Scores are my judgement on a 0 to 5 scale per dimension, converted to the weights below; they are not predictions. Labels: VERIFIED / INFERRED / HYPOTHESIS / UNKNOWN. Evidence files: `../09_TOPIC_DISCOVERY/*`, `../10_SUB_NICHE_RESEARCH/SUB_NICHE_DISCOVERY.md`, `../11_.../TRENDS_AND_NEWS_CAPTURE_2026-11-18.md`, `../12_.../YOUTUBE_SEARCH_SUPPLY_2026-11-18.csv`.

## 1. Challenge to the master weighting (Rule 5)
The master model (competitor evidence 15, demand 15, YouTube 15, suggested 15, search 10, evergreen 10, visual 10, gap/originality 5, feasibility 5) has four weaknesses for a new channel:
1. **Competitor evidence is survivor-biased** (we only studied channels that perform) and cannot show CTR or retention: 15 points is too many.
2. **Suggested relevance cannot be measured** from public data (no Studio data, UNKNOWN): 15 points on an unmeasurable item is mostly guessing.
3. **Gap and originality gets only 5**, yet it decides look-alike risk and the "inauthentic / mass-produced" monetization exposure (official page 1311392) and Phase D found every high-demand topic already served. It should weigh most.
4. **Feasibility gets 5**, yet capacity is UNKNOWN and each video needs primary-source work.
Revised weights (my proposal, HYPOTHESIS): competitor evidence 10, current demand 12, YouTube demand and competition 15, suggested relevance 10, search opportunity 10, evergreen 8, visual 5, gap and originality 20, feasibility 10. Both sets are shown; the order of the top topics barely changes, which is itself a result.

Hard gates (a topic cannot reach A or B unless it passes all): G1 original angle possible with primary sources; G2 not a news read-out; G3 the key numbers are VERIFIED from a primary source; G4 no recent substantial video already owns the exact angle.

## 2. Scores (0 to 5 per dimension)
Columns: CPE competitor performance evidence, CD current demand, YTD YouTube demand and competition (5 = open), SAR suggested relevance (INFERRED), SO search opportunity, EG evergreen, VS visual storytelling, CGO content gap and originality, PF production feasibility.

| Topic | CPE | CD | YTD | SAR | SO | EG | VS | CGO | PF | Master weights /100 | Revised /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T1 Rent: why it is high, CPI vs market rent (durable) | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 67 | 67 |
| T2 Airfares now: BLS +22.4% vs IATA $4.50 (news) | 2 | 5 | 3 | 3 | 3 | 1 | 4 | 3 | 4 | 62 | 63 |
| T3 How airlines make money (generic) | 4 | 3 | 1 | 3 | 4 | 5 | 4 | 1 | 4 | 64 | 56 |
| T4 How banks create money | 3 | 3 | 2 | 3 | 3 | 5 | 4 | 2 | 4 | 63 | 59 |
| T5 How credit scores work | 2 | 1 | 3 | 2 | 2 | 4 | 2 | 2 | 4 | 46 | 48 |
| T6 Industry follow-the-dollar cluster (cruise, hotel, supermarket, port) | 4 | 1 | 3 | 3 | 1 | 4 | 5 | 4 | 2 | 59 | 59 |
| T7 Container shipping | 4 | 2 | 1 | 3 | 2 | 3 | 4 | 1 | 3 | 52 | 45 |
| T8 Data centres | 3 | 3 | 1 | 3 | 3 | 2 | 3 | 1 | 3 | 50 | 44 |
| T9 Toys R Us / IKEA / Costco stories | 3 | 3 | 1 | 3 | 3 | 4 | 4 | 1 | 3 | 56 | 49 |
| T10 Blockbuster / Kodak / Nokia / WeWork / Boeing | 2 | 1 | 2 | 2 | 1 | 4 | 4 | 1 | 3 | 43 | 39 |
| T11 Inflation / why groceries cost more | 3 | 2 | 1 | 3 | 3 | 4 | 3 | 1 | 4 | 52 | 47 |
| T12 Mortgage lock-in (old reject, re-checked) | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 56 | 53 |
Arithmetic: score = sum(raw / 5 x weight); computed by script, not by hand.

## 3. Evidence behind the scores (one line per topic, with the master's required fields)
| Topic | Sub-niche | Competitor evidence | Trends / news | YouTube evidence | Gap and original angle | Confidence |
|---|---|---|---|---|---|---|
| T1 Rent | Housing, cost of living | Casual Finance housing long videos 0.6M+; Money & Macro rent control 402K; no DB video answers "why is rent so high" | Trends about 14 steady (read by eye, US, 12 months); BLS Sep release: rent index +2.8% a year, shelter +3.2% (VERIFIED) | 7 recent results, none over 100K; big videos 2 to 4 years old; 8 tiny pipeline copies of the exact angle | Angle: official rent number is re-priced every six months (VERIFIED) vs market rent (SECONDARY only) | LOW to MEDIUM |
| T2 Airfares | Industry, cost of living | CNBC 91.6K (3 months old) best recent; Neu 17.9K | BLS airfares +22.4% (Sep), IATA 2026 profit $23.0B and $4.50 a passenger (press release, VERIFIED); October CPI is newer and not yet tabulated | 4 uploads in 3 days, 1 to 96 views | Angle: price vs thin margin; time-boxed; read-out risk | LOW |
| T3 Generic airlines | Industry | Jet Crumbs 692K, Dhruv Rathee 11.7M, Wendover 7.4M, WSJ 1.4M | Trends about 40 steady | 3 of 4 recent over 100K | No gap | MEDIUM (that it is crowded) |
| T4 Banks create money | Economics concepts | Primal Space 1.86M | about 18 to 25 steady | 7 recent, median 76K | Weak: textbook explainer | MEDIUM |
| T5 Credit scores | Personal finance | none in primary six | about 9 | only 2 recent | Personal-finance crowd (Phase C) | LOW |
| T6 Industry cluster | Industry, logistics | Neu and Brimm. outliers (553K, 1.12M); recent single hits cruise 5.8M, hotels 7.0M in search CSV | about 0 (not measurable) | thin recent medians | Open, but evidence rests on 2 channels | LOW |
| T7 Container shipping | Industry | Neu 652K and 505K | about 0 | owned by Neu | None | MEDIUM |
| T8 Data centres | AI infrastructure | Maxinomics 2.78M | high in 2025, about 30 now | crowded | None | MEDIUM |
| T9 Toys R Us / IKEA / Costco | Company stories | IKEA 4.8M, Costco 1.59M | Toys R Us spike Sep-Oct 2026, cause unchecked | many 100K+ | None | MEDIUM |
| T10 Dead brands | Company stories | old big videos | about 0 to 16 | small recent | Search-dead | MEDIUM |
| T11 Inflation / groceries | Economics concepts | Primate 1.8M, Johnny Harris 2.5M | inflation interest fell to about 10 | saturated | None | MEDIUM |
| T12 Mortgage lock-in | Housing | not in our primaries | not captured as a series | 24K video 2 days old, ABC 16.6K | No clear gap | LOW |
Suggested/audience-overlap evidence: UNKNOWN for all (see section 6).

## 4. Gates and final categories
| Topic | G1 original angle | G2 not read-out | G3 numbers primary | G4 no owner of exact angle | Category |
|---|---|---|---|---|---|
| T1 Rent | yes (two series, one mechanism) | yes if analysis added | PARTIAL (BLS yes; market rent no) | yes (copies have no traction) | **B: high-priority evergreen, BLOCKED until a primary market-rent series is read** |
| T2 Airfares | yes (price vs margin) | risk, needs analysis | yes (BLS Sep, IATA) but October CPI newer | yes | **C: trend-dependent; publish within days or drop** |
| T3 Generic airlines | no | yes | yes | no | **E** |
| T4 Banks create money | weak | yes | yes | no (Primal Space) | **E** (or D only with a very different angle) |
| T5 Credit scores | no | yes | yes | yes | **E** (personal-finance crowd, low demand) |
| T6 Industry cluster | yes | yes | needs per-video sourcing | yes | **D: experimental** (one test video; no search demand measurable) |
| T7 to T11 | no | yes | n/a | no | **E** |
| T12 Mortgage lock-in | weak | yes | not pulled | no | **E** (kept as a watch item) |
No topic is category A. The reason is explicit: no topic passes all four gates with verified data.

## 5. What the scorecard says (INFERRED, LOW to MEDIUM confidence)
1. The two Phase D conditional topics are also the two top scores under both weightings (67 and 62/63). That agreement is partly circular, because they were the topics we researched most deeply (more evidence raises scores). Treat the order as "best of a thin pool", not "best topics in the market".
2. Re-weighting moves generic airlines from 64 to 56: the master weights would have rewarded a topic that Phase D rejected for having no gap. That is the strongest argument for the revised weights.
3. One experimental slot (T6) tests Concept 2 (industry mechanism) without claiming demand.
4. Not scored because there was no evidence: "how CPI is built" (Concept 1 pillar), jobs/wages, central-bank rates. They need a Phase D pass first.

## 6. Gaps and limits
- Scores are single-rater (my judgement); no second reviewer. Raw scores for SAR are INFERRED.
- Filter 6 (suggested and audience overlap) has not been measured; see `../12_YOUTUBE_SEARCH_AND_SUGGESTED/SUGGESTED_OVERLAP_NOTE_2026-11-18.md`.
- Trends were read by eye; no CSV export.
- The 90, 180-day historical check (Filter 2) was done through DB view totals and recent-vs-old supply, not through a full time series.
