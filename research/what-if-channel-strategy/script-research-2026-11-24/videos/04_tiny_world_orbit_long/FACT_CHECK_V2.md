# Fact check V2 · slot 04

Allowed statuses: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED.
"CALCULATED_SELF_REVIEW" means I (Claude) ran the arithmetic or model myself; it is not expert confirmation. Access date for web sources: 2026-11-24 unless stated.

| ID | Claim as spoken or implied | Status | Value / calculation | Source or method | Accessed | Reading depth | Note |
|---|---|---|---|---|---|---|---|
| V04-C01 | Earth's low orbit speed is about 28,000 km/h; orbit is sideways motion balanced by falling | CALCULATED_SELF_REVIEW | √(GM/r) ≈ 7.8 km/s | own arithmetic | 2026-11-24 | calculation | — |
| V04-C02 | Toy world: radius 3 km, density 2,000 kg/m³, smooth, no air, no spin | ASSUMPTION | definition of the model | model statement | 2026-11-24 | — | Labelled as a model in the script |
| V04-C03 | Surface gravity is less than two ten-thousandths of Earth's | CALCULATED_SELF_REVIEW | g=4/3 π G ρ R = 1.68e-3 m/s² = 1.7e-4 g | work/models/orbit_checks.py | 2026-11-24 | own run | — |
| V04-C04 | Grazing circular orbit speed is about 2.2 m/s (about 8 km/h) | CALCULATED_SELF_REVIEW | v=R√(4πGρ/3)=2.24 m/s=8.1 km/h | work/models/orbit_checks.py | 2026-11-24 | own run | — |
| V04-C05 | 99% of that speed falls back; 110% reaches ~1.6 km above; ~141% escapes (3.2 m/s) | CALCULATED_SELF_REVIEW | apoapsis 1.5316 r0 → 1.59 km above for 110%; √2 × 2.24 = 3.17 m/s | work/models/orbit_checks.py | 2026-11-24 | own run | Horizontal launch at ground level |
| V04-C06 | Even with perfect grip, reaching 2.2 m/s by sprinting takes about twenty minutes | CALCULATED_SELF_REVIEW | a = μ g with μ = 1: 2.24 / 1.68e-3 = 1,330 s ≈ 22 min | own arithmetic | 2026-11-24 | calculation | Assumes friction coefficient 1 and ignores that a runner could not push at all at this weight |
| V04-C07 | A strong jump on Earth leaves the ground at about 2–3 m/s; a world 3–4 km in radius puts orbit in reach if the same take-off speed is assumed | ASSUMPTION | v=√(2 g h) for h=0.4–0.5 m gives 2.8–3.1 m/s; R = v / 7.48e-4 s⁻¹ = 2.7–4.0 km | own arithmetic; no biomechanics source read | 2026-11-24 | calculation | EXPERT_REVIEW_NEEDED for the take-off speed; spoken as an assumption |
| V04-C08 | Tilting a launch at orbital speed upward by 0.5° puts the path's lowest point 26 m below the ground; 5° gives 261 m | CALCULATED_SELF_REVIEW | periapsis = r0 (1 − sin α) below r0 by r0 sin α = 26.2 m and 261.5 m | derived from conic orbit with a=r0 | 2026-11-24 | derivation + run | Launch at v=v_circ from radius r0 |
| V04-C09 | An ordinary tilted jump becomes a hop of about an hour | CALCULATED_SELF_REVIEW | returns to launch radius after half an orbit (180°−2α), ≈ 70 min × (1 − α/90°) | derivation | 2026-11-24 | derivation | Rounded to 'about an hour' |
| V04-C10 | Grazing lap is 140 min at 2,000 kg/m³ and 84 min at Earth's mean density | CALCULATED_SELF_REVIEW | T=√(3π/(Gρ)): 8,402 s = 140 min; with ρ=5,514 kg/m³: 5,061 s = 84.3 min | work/models/orbit_checks.py | 2026-11-24 | own run | Applies to a circular orbit just skimming the surface of a uniform ball |
| V04-C11 | A body's centre sits about a metre above the feet; any bump taller than that blocks a skimming path | CALCULATED_SELF_REVIEW | 1 m / 3,000 m = 0.03% of the radius | own reasoning | 2026-11-24 | reasoning | Clearance, not a precise statement |
| V04-C12 | Real small worlds are lumpy, spinning and perturbed, which changes the answer | ASSUMPTION | stated limitation | — | 2026-11-24 | — | Not modelled |

## Title promise check
Last paragraphs answer the title (on the idealised world, yes, barely) and state that an ordinary jump hops. The ~140-minute figure is attached to the circular grazing orbit of the uniform ball.

## Removed or rewritten from v1
v1 'Orbit is a speed' became 'Orbit is a path … sideways speed'. v1 'At this density it is about two hours and twenty minutes' now says 'For a circular orbit that just skims a smooth ball'. v1 'a couple of coins' became 'a few coins' (weight ≈ 14 gram-force for an 80 kg person).
