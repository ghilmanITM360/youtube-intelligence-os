# Fact check V2 · slot 02

Allowed statuses: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED.
"CALCULATED_SELF_REVIEW" means I (Claude) ran the arithmetic or model myself; it is not expert confirmation. Access date for web sources: 2026-11-24 unless stated.

| ID | Claim as spoken or implied | Status | Value / calculation | Source or method | Accessed | Reading depth | Note |
|---|---|---|---|---|---|---|---|
| V02-C01 | From 10 km you reach about 300 km/h after about 20 s | CALCULATED_SELF_REVIEW | set B peak 299 km/h at 20.4 s (8.8 km altitude) | work/models/fall_model.py | 2026-11-24 | own run | set A gives 320 km/h at 21 s |
| V02-C02 | At 10 km the air pushes back only a little | CALCULATED_SELF_REVIEW | density at 10 km ≈ 0.41 kg/m³ (about a third of sea level) | US Standard Atmosphere 1976 layers 0–86 km (own implementation, constants from memory) | 2026-11-24 | not re-read | Qualitative wording only |
| V02-C03 | Air push grows with speed squared and exceeds weight after the peak | CALCULATED_SELF_REVIEW | drag = ½ρ C A v²; net deceleration after peak | model | 2026-11-24 | own calculation | Standard quadratic drag |
| V02-C04 | Arrival near 190 km/h, same as the 1 km fall | CALCULATED_SELF_REVIEW | 10 km: 189.0 km/h; 1 km: 188.8 km/h (set B) | work/models/fall_model.py | 2026-11-24 | own run | Difference 0.1%; this is computed, not a chosen threshold. The earlier '1.85 km within 5%' criterion is not used anywhere |
| V02-C05 | The slowing lasts a little over two minutes | CALCULATED_SELF_REVIEW | peak at 20 s, ground at 154 s: 134 s ≈ 2.2 min | work/models/fall_model.py | 2026-11-24 | own run | Set A: 122 s |
| V02-C06 | Real suits and positions change the numbers | ASSUMPTION | head-down bound 287 km/h; belly sets 163–204 | fall_model drag sets | 2026-11-24 | own run | No survivability claim made |

## Title promise check
The video explains why speed falls after a peak; it never says the landing is survivable or recommended.

## Removed or rewritten from v1
v1 sentence 'a higher jump just gives the air more speed to take back' kept. No '1.85 km' or '5%' wording appears in V2. Day 2 draft numbers (320 → 265 → 204) differ because that draft used the calibrated-fit drag set A; V2 uses published suit and body data (set B).
