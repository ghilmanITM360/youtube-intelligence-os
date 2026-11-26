# Slot 03 · Short · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
A radio signal travelling at light speed from Earth to Voyager 1 at its November 2026 distance of about 25.9 billion km.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V03-C01 | Light covers about 300,000 km every second and reaches the Moon in just over a second. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | Moon mean distance 384,400 km (NSSDC) / c | CALCULATED_SELF_REVIEW |
| V03-C02 | Light reaches the Sun in a little over eight minutes. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | 1 au / c | CALCULATED_SELF_REVIEW |
| V03-C03 | In November 2026 NASA announced Voyager 1 reached one light-day from Earth, about 26 billion km. | observed fact | NASA release 'Voyager 1 makes history reaching one light-day' (2026-11-19) and NASA Voyager blog 2026-11-18 (page updated 2026-11-20) | release 2026-11-19; blog 2026-11-18: 25.9 billion km (16.1 billion mi) | TIME_SENSITIVE_RECHECK |
| V03-C04 | A light-day is the distance light travels in twenty-four hours. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | c x 86,400 s | CALCULATED_SELF_REVIEW |
| V03-C05 | A command takes about a day to arrive, a reply about a day to return: two days for one exchange. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | t = d / c = 24.0 h each way | CALCULATED_SELF_REVIEW |
| V03-C06 | The delay grows by about five seconds every day because Voyager keeps moving away. | calculation | NASA Voyager 1 mission pages (launch date, speed) via web search | speed ~17.0 km/s relative to the Sun (NASA, 2024 figure) x 86,400 s / c = 4.9 s | CALCULATED_SELF_REVIEW |
| V03-C07 | Radio waves travel at the speed of light. | fact | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | textbook (electromagnetic waves) | CALCULATED_SELF_REVIEW |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | - | OWN_CALCULATION |
| NASA release 'Voyager 1 makes history reaching one light-day' (2026-11-19) and NASA Voyager blog 2026-11-18 (page updated 2026-11-20) | https://science.nasa.gov/blogs/voyager/2026/11/18/voyager-1-engineers-analyze-data-issue-ready-to-confirm-light-day/ | EXTRACT_SUMMARY (fetch tool) |
| NASA Voyager 1 mission pages (launch date, speed) via web search | https://science.nasa.gov/mission/voyager/voyager-1/ | SNIPPET_ONLY |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V03-C01 | 384,400 / 299,792.458 = 1.282 s | mean distance | varies 1.19-1.36 s with orbit |
| V03-C02 | 149,597,870.7 / 299,792.458 = 499.0 s = 8.32 min | mean distance | +-4% over the year |
| V03-C04 | 25,902,068,371 km = 173.14 au | c exact | exact by definition |
| V03-C05 | d = 25.9e9 km | straight-line light path; excludes spacecraft/ground processing | +-8.3 min with Earth's orbit position |
| V03-C06 | dt/day = v x 86,400 / c | speed unchanged; radial motion | speed from a 2024 NASA figure; snippet-level |

## Known
- NASA: Voyager 1 reached one light-day from Earth about 18 Nov 2026 (25.9 billion km); signals take 24 h each way.

## Assumed
- Straight-line vacuum travel at c; no processing delay.
- Speed ~17.0 km/s from a 2024 NASA figure (snippet).

## Uncertain
- Exact distance changes daily; Earth's orbit changes the delay by up to ~8.3 min.

## Competing interpretation or earlier statements
- None on the physics; NASA rounds to 25.9 billion km.

## Required reviewer or source follow-up
- Re-open NASA release/blog on the release day; confirm the one-light-day wording and current speed.

## What the script may claim
- A one-way signal takes about 24 h; an exchange about 48 h; the delay grows ~5 s per day.

## What the script may NOT claim
- No claim about whether Voyager is answering; no claim about its health.
