# Slot 09 · Short · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
Earth with the Sun but no Moon; qualitative question only.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V09-C01 | Yes, without the Moon Earth would still have tides, because the Sun makes tides too. | observed fact | NOAA Ocean Service, What causes tides? | solar tides | SOURCE_CHECKED |
| V09-C02 | A tide is not just a pull; it is a difference in pull. | observed fact | NOAA Ocean Service, What causes tides? | tidal-force explanation | SOURCE_CHECKED |
| V09-C03 | The Sun pulls on Earth about 180 times harder than the Moon does, but it is almost 400 times farther away. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | (Ms/Mm)(dm/ds)^2 = 178.9; ds/dm = 389 | CALCULATED_SELF_REVIEW |
| V09-C04 | That makes the stretching the Sun causes only about 46% of the Moon's. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | (Ms/Mm)(dm/ds)^3 = 0.4596 | CALCULATED_SELF_REVIEW |
| V09-C05 | When the Sun and Moon line up (new and full Moon) their tides add up to bigger spring tides; at right angles tides are smaller. | observed fact | NOAA Ocean Service, What causes tides? | spring and neap tides | SOURCE_CHECKED |
| V09-C06 | With no Moon, many coasts would still have two high and two low tides a day, smaller, by an amount that depends on the coast. | claim | NOAA CO-OPS harmonic constituents, 8 stations (raw JSON) | semidiurnal solar constituent S2 exists at all stations checked | EXPERT_REVIEW_NEEDED |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| NOAA Ocean Service, What causes tides? | https://oceanservice.noaa.gov/education/tutorial_tides/tides02_cause.html | EXTRACT_SUMMARY (earlier session) |
| Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | - | OWN_CALCULATION |
| NOAA CO-OPS harmonic constituents, 8 stations (raw JSON) | blueprint package scripts/data/*.json; scripts/output/light_tides_isolation_stdout.txt | FULL_DATA |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V09-C03 | as V08-C06 | mean distances | - |
| V09-C04 | as V08-C07 | equilibrium forcing | not a prediction of real tide height |

## Known
- NOAA: tides arise from pull differences; Sun contributes; spring/neap tides.
- Pull ratio ~179, distance ratio ~389, tide-raising ratio ~0.46 (arithmetic).

## Assumed
- Linear ocean response for the "many coasts still have two highs and lows" sentence.

## Uncertain
- Real solar tide size varies by coast; S2 contains a radiational part; some coasts are diurnal.

## Competing interpretation or earlier statements
- S2/(M2+S2) percentages (13-35%) from the blueprint are not used.

## Required reviewer or source follow-up
- Oceanographer review of the last paragraph.

## What the script may claim
- The Sun still raises tides; its stretching is about 46% of the Moon's in the idealised picture; spring and neap tides are visible evidence.

## What the script may NOT claim
- No numeric share of real tides; no claim about specific coasts.
