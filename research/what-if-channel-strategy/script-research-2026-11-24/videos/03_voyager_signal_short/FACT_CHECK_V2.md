# Fact check V2 · slot 03

Allowed statuses: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED.
"CALCULATED_SELF_REVIEW" means I (Claude) ran the arithmetic or model myself; it is not expert confirmation. Access date for web sources: 2026-11-24 unless stated.

| ID | Claim as spoken or implied | Status | Value / calculation | Source or method | Accessed | Reading depth | Note |
|---|---|---|---|---|---|---|---|
| V03-C01 | Light travels about 300,000 km every second | SOURCE_CHECKED | 299,792.458 km/s (exact by definition) | SI definition of the metre | 2026-11-24 | known constant | — |
| V03-C02 | Light takes a little over a second to reach the Moon | CALCULATED_SELF_REVIEW | 384,400 km / 299,792 km/s = 1.28 s | mean Earth–Moon distance (NASA NSSDC) | 2026-11-24 | own calculation | Distance varies, so 1.2–1.35 s |
| V03-C03 | Light takes about eight minutes to reach the Sun | CALCULATED_SELF_REVIEW | 149,597,870.7 km / 299,792 km/s = 499 s = 8.3 min | 1 au (exact) | 2026-11-24 | own calculation | — |
| V03-C04 | On 18 November 2026 NASA said Voyager 1 reached one light-day from Earth | TIME_SENSITIVE_RECHECK | milestone 2026-11-18 02:16 PST; release dated 2026-11-19 | NASA news release 'NASA's Voyager 1 Makes History Reaching One Light-Day From Earth' (RELEASE26-098) | 2026-11-24 | full page via fetch extract | Newest NASA text found is dated 2026-11-20 (blog update) |
| V03-C05 | One light-day is about 26 billion km | CALCULATED_SELF_REVIEW | 299,792.458 × 86,400 = 25.902 billion km = 173.14 au; NASA: 25.9 billion km | NASA release; own arithmetic | 2026-11-24 | full page + calculation | — |
| V03-C06 | A reply takes about a day each way, about two days per exchange | SOURCE_CHECKED | ~24 h one way (NASA release) | NASA release 2026-11-19 | 2026-11-24 | full page via fetch extract | In April 2024 NASA gave 22.5 h one way |
| V03-C07 | The exact delay changes from day to day by a few seconds while staying near a day | CALCULATED_SELF_REVIEW | JPL Horizons, Earth-centred: +6.7 s/day on 2026-11-24, +3.1 s/day (2026-05-24), about −2 s/day in Feb–Mar 2027, up to +11.7 s/day in Sep 2027; Sun-relative growth 4.87 s/day | JPL Horizons API query for target -31 (Voyager 1), observer Earth centre, 2026-11 to 2027-11 | 2026-11-24 | query tables read in full | The 'about five seconds per day' used in v1 holds only for speed relative to the Sun and is not what an Earth-based observer sees |

## Title promise check
The script gives the distance, the speed and the resulting day; it does not claim a growth rate any more.

## Removed or rewritten from v1
REMOVED (V03-C08): 'the delay keeps growing, by about five seconds every day, because Voyager keeps moving away'. It used Voyager's speed relative to the Sun (16.9 km/s ≈ 4.9 s/day) and ignored Earth's orbital motion; Earth-relative values range from about −2 to +12 s/day over a year.
