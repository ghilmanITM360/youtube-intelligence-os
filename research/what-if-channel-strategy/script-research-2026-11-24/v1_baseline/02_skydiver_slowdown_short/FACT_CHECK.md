# Slot 02 · Short · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
A person released from rest at 10 km altitude, belly-down, fixed shape, no wind, no parachute, vertical fall; only the speed history is discussed.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V02-C01 | Start ten kilometres up, falling from rest. | scenario | Creative/structural statement or scenario definition | script | ASSUMPTION |
| V02-C02 | At ten kilometres the air is thin, so you speed up and reach about 300 km/h around twenty seconds in. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | finding_checks section A: 10 km, set B | CALCULATED_SELF_REVIEW |
| V02-C03 | As the air thickens it pushes harder than gravity pulls, so you slow down while still falling. | model | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | net deceleration after peak up to 0.04 g (10 km case) | CALCULATED_SELF_REVIEW |
| V02-C04 | By the ground the model has you down to about 190 km/h, the speed of someone who jumped from one kilometre. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | 10 km landing 189.0 vs 1 km landing 188.8 (set B) | CALCULATED_SELF_REVIEW |
| V02-C05 | The slowing is gradual, a bit over two minutes of it. | calculation | Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | 10 km total 2.6 min, peak at 20 s -> ~2.3 min | CALCULATED_SELF_REVIEW |
| V02-C06 | Real suits and body positions change the numbers; this is a model, not a safety guide. | limit | Creative/structural statement or scenario definition | script | ASSUMPTION |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| Own 1-D vertical-fall model (stdlib Python, RK4, quadratic drag) | scripts/fall_model.py; scripts/finding_checks.py -> scripts/output/finding_checks_stdout.txt | OWN_CALCULATION |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V02-C02 | peak 299 km/h at 8.8 km altitude, t=20 s (set A 320 km/h) | CdA/m set B (Stratos paper inputs) | range 264-320 km/h across sets |
| V02-C03 | same | quadratic drag | gradual slowing; no comfort claim |
| V02-C04 | same | CdA/m set B | 164-204 km/h across sets |
| V02-C05 | same | set B | 2.4-2.9 min of total fall across sets |

## Known
- Air density rises as you descend (standard atmosphere).
- Drag grows with speed and density.

## Assumed
- Quadratic drag, constant CdA/m = 0.00589 (Stratos paper inputs).
- USSA-1976 densities.
- Vertical fall from rest.

## Uncertain
- Peak 264-320 km/h across sets; landing 164-204 km/h; slowing duration 2.3 min (set B).
- Real suits/postures change all values.

## Competing interpretation or earlier statements
- Existing Day 2 draft states 320 km/h peak and 204 km/h landing (calibrated set A); this draft uses set B (299 / 189).

## Required reviewer or source follow-up
- Aerodynamics reviewer.
- Owner: choose between this Short and the existing Day 2 draft.

## What the script may claim
- In a simple model a 10 km faller peaks near 300 km/h about 20 s in and lands near 190 km/h.
- The slowing is gradual (net deceleration at most ~0.04 g).

## What the script may NOT claim
- No safety, comfort or survival statement; no universal threshold height.
