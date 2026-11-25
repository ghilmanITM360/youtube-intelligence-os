# Slot 01 · Long · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
Two people are released from rest, one at 1 km and one at 100 km altitude, in pressure suits, belly-down, no wind, no parachute, vertical fall to sea level. The question: which reaches the ground "faster" - sooner, or at a higher landing speed? This is not orbital re-entry and not a survival analysis.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V01-C01 | Two people step off, one a kilometre up and one a hundred kilometres up; both start at rest, fall straight down, no parachute. | scenario | Creative/structural statement or scenario definition | script opening | ASSUMPTION |
| V01-C02 | A hundred kilometres is the Karman line, a common convention for where space begins. | fact | FAI Karman line reports (web-search results) | FAI 100 km; US agencies commonly 80 km (50 mi) | SOURCE_CHECKED |
| V01-C03 | From one kilometre the fall lasts about twenty seconds. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | finding_checks section H; fall_model T1 | CALCULATED_SELF_REVIEW |
| V01-C04 | From a hundred kilometres the fall lasts about six minutes in our simple model. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | finding_checks section H | CALCULATED_SELF_REVIEW |
| V01-C05 | You speed up by almost ten metres per second, every second. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | g(h)=g0(R/(R+h))^2 | CALCULATED_SELF_REVIEW |
| V01-C06 | The air's push grows with the square of speed; at around two hundred km/h it would match your weight and you would stop speeding up. | model | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | terminal speed sqrt(2g/(rho*CdA/m)) at sea level | CALCULATED_SELF_REVIEW |
| V01-C07 | The person from one kilometre lands at around one hundred and ninety km/h; the number moves from about 160 to 200 across our versions. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | fall_results.csv / finding_checks section A | EXPERT_REVIEW_NEEDED |
| V01-C08 | At a hundred kilometres the air is about two million times thinner than at the ground. | calculation | US Standard Atmosphere 1976 (own implementation) | density ratio 1.225 / 5.604e-7 = 2.19e6 | CALCULATED_SELF_REVIEW |
| V01-C09 | For the first minute and a half the air hardly matters. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | free fall 100 km to 60 km takes ~91 s with density below 0.03% of sea level | CALCULATED_SELF_REVIEW |
| V01-C10 | By forty kilometres up you cover about a kilometre per second, around three and a half thousand km/h, about three times the speed of sound there. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | finding_checks section H | EXPERT_REVIEW_NEEDED |
| V01-C11 | The two landing speeds differ by less than a fifth of one percent in our model. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | landing ratio 100 km / 1 km | CALCULATED_SELF_REVIEW |
| V01-C12 | The tall faller spends about six minutes in the air, passes through the speed of sound and meets heavy braking; the model leaves out heating. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | supersonic ~88 s; felt load ~4.6 g | CALCULATED_SELF_REVIEW |
| V01-C13 | In 2012 Felix Baumgartner stepped off from almost 39 km and reached about 1,358 km/h. | observed fact | Guerster & Walter 2017, PLoS ONE 12(12):e0187798 (Stratos flight-data aerodynamics) | peak 377.1 m/s = 1,357.6 km/h; exit 38,969.4 m | SOURCE_CHECKED |
| V01-C14 | In 2014 Alan Eustace jumped from about 41 km; nobody has jumped from anywhere near 100 km. | observed fact | Guinness World Records / news reports: Alan Eustace 2014 jump (web-search results) | Guinness/NBC/NPR snippets: 135,890 ft (41.4 km), FAI-verified 2015 | TIME_SENSITIVE_RECHECK |
| V01-C15 | Head-down, a rough bound puts both landings near 280-290 km/h, within about 3% of each other. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | set E: 279.3 (1 km) vs 287.1 (100 km) | CALCULATED_SELF_REVIEW |
| V01-C16 | Spacecraft come home at around 28,000 km/h because they were already moving sideways at orbital speed; these two people start from rest. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | circular speed sqrt(gR)=7.90 km/s=28,456 km/h at the surface; ~28,200 km/h at 100 km | CALCULATED_SELF_REVIEW |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| FAI Karman line reports (web-search results) | https://www.space.com/karman-line-where-does-space-begin | SNIPPET_ONLY |
| Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | scripts/fall_model.py; scripts/finding_checks.py -> scripts/output/finding_checks_stdout.txt | OWN_CALCULATION |
| US Standard Atmosphere 1976 (own implementation) | scripts/fall_model.py atm(); blueprint package scripts/atmosphere_check.py | OWN_CALCULATION (layers 0-86 km from memory of the standard; 86-120 km values recalled) |
| Guerster & Walter 2017, PLoS ONE 12(12):e0187798 (Stratos flight-data aerodynamics) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5720713/ | FULL_TEXT_EXTRACTION (fetch-tool; earlier session) |
| Guinness World Records / news reports: Alan Eustace 2014 jump (web-search results) | https://www.guinnessworldrecords.com/world-records/107938-highest-freefall-parachute-jump | SNIPPET_ONLY |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V01-C03 | RK4 vertical fall from rest | belly-down CdA/m sets A-D (+E) | 18-25 s across sets (set B 22 s) |
| V01-C04 | RK4 vertical fall, USSA density, constant CdA/m | same; density above 86 km recalled | 5.6-6.7 min (belly-down sets); 4.4 min head-down bound |
| V01-C05 | g = 9.51 m/s2 at 100 km; 9.81 at ground | spherical Earth | - |
| V01-C06 | 164-204 km/h across belly-down sets A-D | quadratic drag, constant Cd | depends on posture/suit; head-down bound 283 km/h |
| V01-C07 | 1 km release, sets A-D | CdA/m 0.0050-0.0078 | ground speed 164.2-204.0 km/h (set B 188.8); sets are assumptions (A inherited, C/D unsourced) |
| V01-C08 | USSA-1976 value at 100 km | table values above 86 km recalled, not re-read | order of magnitude only |
| V01-C09 | kinematics + density | - | qualitative |
| V01-C10 | peak 3,521-3,763 km/h at 36-43 km altitude; Mach 3.06-3.40 | constant Cd to Mach ~3; ideal-gas speed of sound | real hypersonic drag differs; heating not modelled |
| V01-C11 | 1.0001-1.0015 for belly-down sets A-D | fixed posture | head-down bound differs by 2.8% (1.0277) |
| V01-C12 | same model | heating, ablation, body response not modelled | no survival or comfort claim |
| V01-C15 | CdA/m 0.0026 (smallest suit cross-section) | stability of that posture not established | bound only; not a claim anyone can hold that posture |
| V01-C16 | orbital mechanics | - | re-entry speeds vary by mission |

## Known
- Baumgartner jumped from 38,969.4 m and reached 377.1 m/s (1,357.6 km/h) (Guerster & Walter 2017).
- Eustace jumped from about 41.4 km in 2014 (Guinness/news snippets).
- The Karman line (100 km) is the FAI convention; US agencies use 80 km (snippets).
- Orbital circular speed at the surface radius is 7.9 km/s.

## Assumed
- Quadratic drag with constant CdA/m for the whole fall (Cd held constant to Mach ~3).
- Density: own implementation of USSA-1976, layers above 86 km recalled from memory.
- Vertical fall from rest; no wind, no spin, no parachute; fixed belly-down posture.
- CdA/m sets: A 0.00505 (inherited fit), B 0.00589 (Stratos paper inputs), C 0.00611 and D 0.00778 (assumed brackets), E 0.00260 (head-down bound).

## Uncertain
- Landing speed 164-204 km/h across sets A-D (head-down bound 287 km/h).
- Peak speed 3,521-3,763 km/h at 36-43 km altitude; hypersonic drag, heating and body response not modelled.
- Total time 5.6-6.7 min (belly-down sets).
- Density table above 86 km.

## Competing interpretation or earlier statements
- Claude review: 164-205 km/h; Codex review: ~186-229 km/h under a 20% drag variation; existing v3 prints 204 km/h (calibrated fit) - all model outputs, not measurements.
- "Faster" as arrival time: the tall faller is clearly slower to arrive (about 6 min vs 20 s).

## Required reviewer or source follow-up
- Aerodynamics/atmospheric-flight reviewer for the drag range and the hypersonic extrapolation.
- Re-read the published USSA-1976 table above 86 km.
- Owner decision: use this draft, the approved v3, or a merged version.

## What the script may claim
- In a simple model the landing speeds from 1 km and from 100 km agree to within about 0.2%.
- The tall fall takes about six minutes and peaks at roughly 3,500 km/h near 40 km.
- Baumgartner (2012) and Eustace (2014) jumps happened; nobody has jumped from near 100 km.

## What the script may NOT claim
- No claim about survival, safety, pain or comfort.
- No exact decimals as facts; no claim that real air behaves like the constant-drag model at Mach 3.
- No claim that this is how spacecraft return.
