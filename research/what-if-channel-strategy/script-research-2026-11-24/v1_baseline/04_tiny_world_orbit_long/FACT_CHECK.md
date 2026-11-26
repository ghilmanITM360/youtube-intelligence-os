# Slot 04 · Long · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
A smooth, uniform, non-rotating, airless sphere of density 2,000 kg/m3 and radius 3 km (worked example). A person launches horizontally from the surface; what speeds give landing, grazing orbit, ellipse or escape, and what stops a real jump from reaching orbit?

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V04-C01 | The world is a smooth ball of ordinary rock, about 2,000 kg/m3, with no air, spin or hills; it is a model, not a real asteroid. | scenario | Creative/structural statement or scenario definition | script | ASSUMPTION |
| V04-C02 | Orbit needs a sideways speed of about 28,000 km/h on Earth. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | v = sqrt(gR) | CALCULATED_SELF_REVIEW |
| V04-C03 | On a world of 3 km radius, gravity is less than two ten-thousandths of Earth's; a person presses on the ground like a couple of coins. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | g=(4/3)piG rho R | CALCULATED_SELF_REVIEW |
| V04-C04 | The grazing-orbit speed there is a little over 2 m/s, about 8 km/h. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | v_c = R sqrt(4piG rho/3) | CALCULATED_SELF_REVIEW |
| V04-C05 | At 99% of that speed you land further on; at 100% you skim around; 10% faster you swing out ~1.5 km and return; ~41% faster (just over 3 m/s) you escape. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | blueprint orbit_stdout; finding_checks | CALCULATED_SELF_REVIEW |
| V04-C06 | Running to orbital speed there would take about twenty minutes of sprinting because feet barely grip. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | a_max = mu g; t = v_c/(mu g) | ASSUMPTION |
| V04-C07 | A strong jump on Earth leaves the ground at about 2-3 m/s. | assumption | Creative/structural statement or scenario definition | v = sqrt(2 g h) for jump heights 0.2-0.45 m | ASSUMPTION |
| V04-C08 | If take-off speed is unchanged on a small world, a world 3-4 km in radius puts orbit within reach. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | R = v / sqrt(4piG rho/3) | ASSUMPTION |
| V04-C09 | Tilting the launch up half a degree puts the path's low point ~26 m underground; five degrees, over 250 m. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | periapsis of the conic through the launch point | CALCULATED_SELF_REVIEW |
| V04-C10 | An ordinary jump near that speed, tilted upward, is a hop of roughly an hour. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | blueprint RK4 hop: 45 deg, 0.9 v_c lands after 68.6 min | CALCULATED_SELF_REVIEW |
| V04-C11 | A grazing lap takes about two hours twenty minutes at this density regardless of size; about 84 minutes for Earth's density. | calculation | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | T = sqrt(3 pi /(G rho)) (circular orbit) | CALCULATED_SELF_REVIEW |
| V04-C12 | You would arrive back where you started at the same level; your feet start about a metre up, so a bump taller than a metre stops you; real worlds are lumpy, spin and have neighbours. | limit | Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | periapsis = launch radius | ASSUMPTION |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| Defined constants: c = 299,792.458 km/s (exact), 1 au (exact), G = 6.6743e-11 (CODATA) | - | OWN_CALCULATION |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V04-C02 | 7.90 km/s = 28,456 km/h | g=9.80665, R=6,371 km, no air | speed just above the surface |
| V04-C03 | 1.677 mm/s2 = 0.0171% of Earth g; weight-equivalent of ~12 g of mass for 70 kg | uniform sphere | comparison approximate |
| V04-C04 | 2.243 m/s = 8.07 km/h | R=3,000 m, rho=2,000 | scales with R |
| V04-C05 | 1.10 v_c -> apoapsis +1,595 m; v_esc = sqrt2 v_c = 3.17 m/s | level launch at surface, R=3 km | toy model |
| V04-C06 | 22 min, 1.5 km for mu=1 | friction coefficient 1 | a rough illustration; real surface/dust unknown |
| V04-C07 | 1.98-2.97 m/s | jump height unsourced | not a sourced biomechanics figure |
| V04-C08 | 2.65-3.97 km for v=2.0-3.0 m/s | same take-off speed on small world (assumed) | assumption, not tested |
| V04-C09 | -26 m (0.5 deg), -261 m (5 deg) at v = v_c, R=3 km | exactly circular launch speed | other speeds give other depths (e.g. 1.1 v_c: -0.7 m, -63 m) |
| V04-C10 | R=3 km | single case | time shorter at lower speed (0.5 v_c: 19.8 min) |
| V04-C11 | 140.0 min (rho=2000); 84.3 min (rho=5514) | circular grazing orbit only; elliptical laps are longer (1.01 v_c: 144 min) | - |
| V04-C12 | clearance ~1 m (centre of mass height) | jumper height assumption | qualitative |

## Known
- Newtonian gravity of a uniform sphere: g=(4/3)piG rho R; circular speed v_c=R*sqrt(4piG rho/3); T_circ=sqrt(3pi/(G rho)).
- Earth surface circular speed sqrt(gR)=7.9 km/s.

## Assumed
- Uniform sphere, rho=2,000 kg/m3, no spin, no air, no terrain.
- Jump take-off speed about 2-3 m/s, unchanged on the small world (assumption).
- Friction coefficient 1 (illustration).

## Uncertain
- Real small bodies are lumpy and spinning; tides and neighbours matter.
- Human jump speed unsourced.

## Competing interpretation or earlier statements
- Earlier blueprint wording implied a "level jump" is feasible; this script says an ordinary tilted jump falls back.

## Required reviewer or source follow-up
- Physicist check of the model statement; biomechanics source for jump speeds.

## What the script may claim
- In the toy world a grazing orbit needs about 2.2 m/s (R=3 km); a lap takes 140 min (circular); a tilted launch dips below ground.

## What the script may NOT claim
- No claim that any real asteroid works this way; no claim that an ordinary jump reaches orbit.
