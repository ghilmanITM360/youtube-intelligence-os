# 07d Physics and units check of 10 claims in the xkcd What If? videos (continuation, 2026-11-23)

Status: **independent recomputation by the main session plus four sources fetched this session** (scientific verification, not video review). Same model family as the rest of the audit, so it is **not independent expert review**: every number below should be re-run by a person who can check the sources. Data: `07_SCIENCE_CLAIM_CHECKS.csv` (claim, video ID, script locator, ASR time, quote, assumptions, recomputed value, reference, verdict, visual device). Code: `scripts/phase7_claim_checks.py`.

Selection: 10 claims in 9 videos with a stated number that can be recomputed from first principles; chosen from the script locators, not at random, and **not** the directive's ten high-value episodes (those need a deeper per-episode pass: Earth stops spinning, relativistic baseball, draining the oceans, laser pointer, billion-story building beyond the geostationary line, submarine in space, nanosecond on the Sun in full). Claims about what is drawn were not tested for physical accuracy of the drawing; only the spoken quantity was.

| ID | Video, locator, ASR time | Claim | Recomputed | Verdict |
|---|---|---|---|---|
| SC01 | `-1-ldW4kpLM` V017 para15, 107.8 s | Earth +26 km after a month (+0.4%) at 1 cm/s | 25.92 km, 0.41% | CONSISTENT |
| SC02 | `-1-ldW4kpLM` V017 para26, 215.0 s | over 6 g after 100 years | 5.95 g (constant density) | CONSISTENT with caveat: "over 6" vs 5.95, density assumption unstated |
| SC03 | `fs28lEq9smw` V010 para5, 36.9 s | one lightning strike powers a house about two days | house 102 MJ/day (EIA); 1-5 GJ typical flash = 10 to 50 days | **DISCREPANT** with the checked sources (needs the authors' source) |
| SC04 | `0L44GEJ5pLE` V051 para3, 51.3 s | 1.5 mJ heats a drop by 1% of a degree, lifts a squirrel 300 microns | 0.5 kg squirrel, 0.036 g drop (0.7% for 0.05 g) | CONSISTENT with caveat (rounding) |
| SC05 | `e3uk7jU3RHo` V002 para3 and 18, 9.6 s | a magnitude 25 quake explodes the Sun | 2.0e42 J vs Sun binding energy 2e41 to 7e41 J | CONSISTENT with caveat (law extrapolated far beyond measurement) |
| SC06 | `WYf9-xfm6t8` V026 para19, 70.5 s | melting 1 g of snow takes about 335 J | 333.55 J/g | CONSISTENT (ignores sub-zero warming) |
| SC07 | `UQgw50GQu1A` V030 para3, 18.1 s | a Moon-mass black hole has a horizon the size of a sand grain | r_s 0.109 mm | CONSISTENT |
| SC08 | `PUtI3xoaHx0` V042 para2, 11.6 s | 500 trillion calories of human | own range 360 to 1,190 trillion kcal | NOT_VERIFIED (no authoritative source; plausible order of magnitude) |
| SC09 | `gp5G1QG6cXc`, 14.1 s (and on-screen "470 m/s (1040 mph)") | equator moves about 1,000 mph | 465.1 m/s = 1,040 mph | CONSISTENT with caveat: "470 m/s" is not 1,040 mph (it is 1,051); "a thousand" is 4% low |
| SC10 | `Z_xJ40QXu7Q` V021 para32, 166.7 s | effects equalise just over a tenth of the way to the Moon | 42,164 / 384,400 = 0.110 | CONSISTENT (measured from Earth's centre) |

Counts: 4 consistent, 4 consistent with a caveat, 1 discrepant, 1 not verified. n = 10: this says nothing about the error rate of the channel.

## Sources fetched this session (via web search, standard mode; summaries, not full-page reads)
- Lightning flash energy: NOAA expert quoted by National Geographic, [typical 1,000 to 5,000 MJ, range about 100 to 30,000 MJ](https://www.nationalgeographic.com/science/article/120308-energy-in-forces-of-nature) (a secondary report of an expert, not an NSSL publication); [1.5e9 J typical flash in a research paper](https://arxiv.org/pdf/2101.12361).
- Household electricity: [EIA, 865 kWh per month in 2024; 10,791 kWh per year in 2022](https://www.eia.gov/tools/faqs/faq.php?id=97&t=3).
- [NIF 500 TW and 1.85 MJ on target, 2012, LLNL](https://www.llnl.gov/article/38161/national-ignition-facility-makes-history-record-500-terawatt-shot) (found while preparing SC for the "2 x 10^24 W" laser array frame, which was not recomputed here).
- [NASA NSSDC Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html): equatorial radius 6378.137 km, g0 9.80665 m/s2 (CODATA 2018).
- **Not fetched** (standard textbook constants used from the author's knowledge, to be confirmed): G, c, sigma, solar mass, radius and binding energy, ice latent heat, geostationary radius, Moon distance, Wentworth sand classes, body energy density. A reviewer should check these.

## Schematic vs quantitative, and likely misreadings (OBSERVED + INFERRED, one coder)
- The frames in these claims are **quantity labels on schematic drawings**, not simulations: the globe with a thin shell (SC01), a "1G | 6G" comparison (SC02), a household-and-lightning comparison (SC03), grey bands with "470 m/s" on a flat map (SC09). Proportions in them were not measured against the stated numbers.
- Misreading risks: SC02 reads as exact when the true value (5.95 g) is a constant-density extrapolation; SC03 may mislead a viewer by about a factor of 5 to 25 if the sources above are right; SC05 can be read as geophysics when it is an extrapolation of a scale; SC09's band shows speed as a flat stripe although it varies with cos(latitude).
- No hidden animation software or simulation method is inferred from appearance.
