# Slot 05 · Short · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
A person on the surface of Phobos jumps with an assumed 2-3 m/s take-off speed. Compare with the isolated-sphere escape speed, then ask what a jump does and whether escaping Phobos means leaving Mars.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V05-C01 | Phobos is a lumpy moon of Mars about 22 km across on average. | observed fact | NASA NSSDC Mars fact sheet (satellites table) | satellites table: mean radius ~11.1 km | SOURCE_CHECKED |
| V05-C02 | As a perfect ball alone in space, escape speed would be about 11 m/s, roughly 40 km/h. | calculation | NASA NSSDC Mars fact sheet (satellites table) | M=1.0659e16 kg, R=11.08 km | CALCULATED_SELF_REVIEW |
| V05-C03 | A strong jump on Earth leaves the ground at about 2-3 m/s; we assume that. | assumption | Creative/structural statement or scenario definition | as V04-C07 | ASSUMPTION |
| V05-C04 | In our simple model you rise for a while then fall back, in a trip lasting tens of minutes. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | blueprint phobos_hill_sim: main sphere 17-31 min; all radii 12-155 min | EXPERT_REVIEW_NEEDED |
| V05-C05 | Real Phobos is not a ball; its shape, spin and Mars's pull all change the number. | limit | Creative/structural statement or scenario definition | Phobos is irregular and tidally locked (general knowledge) | EXPERT_REVIEW_NEEDED |
| V05-C06 | Even if you escaped Phobos you would still be orbiting Mars. | calculation | NASA NSSDC Mars fact sheet (satellites table) | Phobos orbital speed ~2.14 km/s vs escape ~11 m/s | CALCULATED_SELF_REVIEW |
| V05-C07 | Leaving Mars would take hundreds of metres per second more. | calculation | NASA NSSDC Mars fact sheet (satellites table) | (sqrt2 - 1) x v_orb | CALCULATED_SELF_REVIEW |
| V05-C08 | So: not with a jump, and not for good. | conclusion | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | V05-C02..C07 | EXPERT_REVIEW_NEEDED |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| NASA NSSDC Mars fact sheet (satellites table) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html | EXTRACT_SUMMARY (earlier session) |
| Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | scripts/fall_model.py; scripts/finding_checks.py -> scripts/output/finding_checks_stdout.txt | OWN_CALCULATION |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V05-C01 | diameter = 2 x 11.08 km = 22.2 km | mean radius | dimensions vary by axis |
| V05-C02 | sqrt(2GM/R) = 11.33 m/s = 40.8 km/h | isolated uniform sphere | real shape, spin and Mars change it |
| V05-C04 | Hill-equation sim, point-mass gravity, sphere | sphere, Mars as distant mass, 3 m/s | crude; no shape model |
| V05-C06 | relative speed ~0.5% of orbital speed | launch near Phobos | trajectory not simulated |
| V05-C07 | 886 m/s (circular-orbit start, prograde) | circular orbit, prograde direction | depends on start orbit and direction |

## Known
- Phobos mean radius ~11.1 km, mass ~1.0659e16 kg (NSSDC).
- Phobos orbits Mars at ~2.14 km/s (circular approximation).

## Assumed
- Isolated uniform sphere for the 11.3 m/s figure.
- Jump 2-3 m/s (assumption).
- Hill-equation simulation with Mars as a distant mass for the fall-back time.

## Uncertain
- Real Phobos is irregular; escape speed depends on launch point and direction; rotation and Mars tides matter.
- Fall-back time 12-155 min across sphere radii (main case 17-31 min).

## Competing interpretation or earlier statements
- The earlier blueprint's "Mars-pull twist" (lower escape threshold along the Mars line) is a sphere-model hypothesis and is not used.

## Required reviewer or source follow-up
- Planetary dynamicist with a Phobos shape model to confirm fall-back and the escape thresholds.

## What the script may claim
- An isolated sphere of Phobos's mass and size has v_esc about 11.3 m/s (~41 km/h).
- In a simple model a 2-3 m/s jump returns.
- Leaving Mars from Phobos's orbit needs hundreds of m/s more (circular, prograde).

## What the script may NOT claim
- No unconditional statement about a real jump; no claim about a real astronaut's capability.
