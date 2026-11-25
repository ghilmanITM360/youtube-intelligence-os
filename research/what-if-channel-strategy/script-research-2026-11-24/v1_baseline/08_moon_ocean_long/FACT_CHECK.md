# Slot 08 · Long · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
The Moon is removed instantly and cleanly; Earth's spin and orbit around the Sun are unchanged. The question is limited to ocean tides and motion.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V08-C01 | The Moon disappears instantly with no debris; Earth keeps spinning once a day and keeps circling the Sun. | scenario | Creative/structural statement or scenario definition | script opening | ASSUMPTION |
| V08-C02 | The sea does not drain or flood; the Moon was never holding the water up. | claim | Creative/structural statement or scenario definition | reasoning: Earth's gravity holds the ocean | CALCULATED_SELF_REVIEW |
| V08-C03 | A tide comes from a difference in pull across Earth, which stretches the ocean into two bulges; many coasts get two high tides a day. | observed fact | NOAA Ocean Service, What causes tides? | tidal-force explanation | SOURCE_CHECKED |
| V08-C04 | With the Moon removed the stretching goes, but the water keeps moving, so the old rhythm fades rather than stopping at once. | claim | Creative/structural statement or scenario definition | momentum of existing tidal motion | HYPOTHESIS |
| V08-C05 | How long the old rhythm takes to fade is not known here. | limit | Creative/structural statement or scenario definition | script | UNRESOLVED |
| V08-C06 | The Sun pulls on Earth about 180 times harder than the Moon does. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | (Ms/Mm)(dm/ds)^2 | CALCULATED_SELF_REVIEW |
| V08-C07 | The Sun is almost 400 times farther, so its pull barely changes across Earth; its tide-raising force is about 46% of the Moon's. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | (Ms/Mm)(dm/ds)^3; ds/dm = 389 | CALCULATED_SELF_REVIEW |
| V08-C08 | In an ideal ocean the solar tide would be a bit under half the lunar one; real oceans differ by place, so there is no single number; most places would see smaller tides than today. | claim | NOAA CO-OPS harmonic constituents, 8 stations (raw JSON) | S2/M2 amplitude ratios at 8 stations 0.15-0.54 (context only, not used as a percent) | EXPERT_REVIEW_NEEDED |
| V08-C09 | Today high tide arrives about fifty minutes later each day because the Moon moves across the sky. | calculation | Creative/structural statement or scenario definition | lunar day = 24 h / (1 - 1/29.53) = 24.84 h | CALCULATED_SELF_REVIEW |
| V08-C10 | Without the Moon the main rhythm follows the Sun, repeating every twelve hours exactly; a given beach would see high tides at about the same times each day, with each coast having its own offset, and some places more complicated. | claim | NOAA CO-OPS harmonic constituents, 8 stations (raw JSON) | S2 period = 12.000 h by definition; local phase differs by station | EXPERT_REVIEW_NEEDED |
| V08-C11 | The fortnightly swing between bigger and smaller tides needs two tide-raisers, so it disappears with one. | observed fact | NOAA Ocean Service, What causes tides? | spring/neap explained by Sun-Moon alignment | SOURCE_CHECKED |
| V08-C12 | This video does not answer what would happen to Earth's tilt, seasons or day length; some of that is debated. | limit | Li & Batygin 2014, spin-axis dynamics of a moonless Earth (arXiv:1404.7505) | Li & Batygin 2014 abstract read; Lissauer 2012 and Laskar not read | UNRESOLVED |
| V08-C13 | (Removed) Moonless Earth's axial tilt would wander slowly/chaotically. | claim | Li & Batygin 2014, spin-axis dynamics of a moonless Earth (arXiv:1404.7505) | abstract only | REMOVED |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| NOAA Ocean Service, What causes tides? | https://oceanservice.noaa.gov/education/tutorial_tides/tides02_cause.html | EXTRACT_SUMMARY (earlier session) |
| Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | - | OWN_CALCULATION |
| NOAA CO-OPS harmonic constituents, 8 stations (raw JSON) | blueprint package scripts/data/*.json; scripts/output/light_tides_isolation_stdout.txt | FULL_DATA |
| Li & Batygin 2014, spin-axis dynamics of a moonless Earth (arXiv:1404.7505) | https://arxiv.org/abs/1404.7505 | ABSTRACT_ONLY (earlier session) |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V08-C06 | 178.9 (NOAA: more than 177) | Ms 1.989e30, Mm 7.342e22 kg, d_m 384,400 km, d_s 149.6e6 km | mean distances |
| V08-C07 | 0.4596 | mean distances | equilibrium forcing ratio only |
| V08-C08 | forcing ratio 0.46 | equilibrium picture; S2 includes a radiational part (~10-18% of S2, snippet) | S2/(M2+S2) is NOT 'what remains' |
| V08-C09 | ~50 min | mean synodic month 29.53 d | varies with location and season |
| V08-C10 | harmonic constituents | linear response; transients decayed | not every coast; diurnal constituents; local response unquantified |

## Known
- NOAA: tides arise from a difference in gravitational pull; two bulges; spring and neap tides from Sun-Moon alignment.
- Sun/Moon pull ratio ~179; distance ratio ~389; tide-raising ratio ~0.46 (own arithmetic).

## Assumed
- Instant, clean removal; no debris; Earth spin/orbit unchanged.
- Linear ocean response in the idealised picture.

## Uncertain
- Decay time of existing tidal motion (unsourced).
- Local amplitude and phase of the solar tide at each coast; S2 includes a radiational part.
- Earth's tilt, seasons and day length (not answered).

## Competing interpretation or earlier statements
- The earlier blueprint stated "high tide on the 12.00 h solar clock" and S2/(M2+S2) = 13-35%; both are withdrawn (findings C, D).

## Required reviewer or source follow-up
- Physical oceanographer for the transient decay, local response and the "same times each day" sentence.
- Astronomer for the tilt question if the owner wants it covered.

## What the script may claim
- Tides would not vanish: the Sun still raises them, about 46% of the Moon's stretching in the idealised picture.
- The fortnightly spring/neap swing would disappear; the main rhythm would follow the Sun.

## What the script may NOT claim
- No percentage of today's tide; no claim that every coast has high tide at the same clock time; no claim about tilt or day length.
