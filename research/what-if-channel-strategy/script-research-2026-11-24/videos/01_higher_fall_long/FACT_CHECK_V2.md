# Fact check V2 · slot 01

Allowed statuses: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED.
"CALCULATED_SELF_REVIEW" means I (Claude) ran the arithmetic or model myself; it is not expert confirmation. Access date for web sources: 2026-11-24 unless stated.

| ID | Claim as spoken or implied | Status | Value / calculation | Source or method | Accessed | Reading depth | Note |
|---|---|---|---|---|---|---|---|
| V01-C01 | The Kármán line (100 km) is a common convention for where space begins | SOURCE_CHECKED | FAI uses 100 km; US agencies commonly use 80 km (50 miles) | Secondary summaries via web search (Britannica, Space.com snippets); FAI page not opened | 2026-11-24 | search snippets only | Script says 'one common convention' |
| V01-C02 | A fall from 1 km lasts roughly twenty seconds | CALCULATED_SELF_REVIEW | 21–22 s (drag sets A, B); 18 s head-down | work/models/fall_model.py | 2026-11-24 | own run | Model, no wind |
| V01-C03 | A fall from 100 km lasts between 5.5 and 6 minutes | CALCULATED_SELF_REVIEW | set A 337 s (5.6 min); set B 358 s (6.0 min); head-down 264 s (4.4 min) | work/models/fall_model.py | 2026-11-24 | own run | Head-down bound is shorter; spoken range covers belly-down sets |
| V01-C04 | Early acceleration is almost ten metres per second every second | CALCULATED_SELF_REVIEW | g falls from 9.80 to 9.5 m/s² across the first 100 km | g(h)=g0 (R/(R+h))² | 2026-11-24 | own calculation | Air negligible at the start |
| V01-C05 | Terminal speed is about 190 km/h; range about 160–205 | CALCULATED_SELF_REVIEW | set B 189 (published suit/body data); set A 204 (fit); sets C, D 184 and 163 (assumed brackets) | Guerster & Walter 2017 (PLoS ONE 12(12):e0187798) for set B; others are assumptions | 2026-11-24 (paper read earlier via PMC summary) | part of paper (summary) | Posture and suit dependent; head-down bound 287 |
| V01-C06 | At 100 km the air is more than a million times thinner than at the ground | ASSUMPTION | 1.225 / 5.6e-7 ≈ 2.2 million in the model's table | US Standard Atmosphere 1976 above 86 km values recalled from memory, not re-read | 2026-11-24 | not re-read | Wording kept conservative ('more than a million') |
| V01-C07 | Peak speed about 3,600 km/h near 40 km, about Mach 3 | EXPERT_REVIEW_NEEDED | set A 3,620 km/h at 40.4 km; set B 3,585 at 41.3 km; Mach 3.15–3.19 | work/models/fall_model.py; constant Cd to Mach 3 is an assumption | 2026-11-24 | own run | Real drag coefficient varies with Mach number; needs aerodynamics review |
| V01-C08 | Arrival speeds of the two fallers differ by far less than 1% (belly-down); about 3% for a head-down bound | CALCULATED_SELF_REVIEW | A: 204.0 vs 204.3 km/h (0.15%); B: 188.8 vs 189.0 (0.1%); E: 279.3 vs 287.1 (2.8%) | work/models/fall_model.py | 2026-11-24 | own run | Model result, not a measured one |
| V01-C09 | Baumgartner 2012: exit about 39 km, peak about 1,358 km/h | SOURCE_CHECKED | exit 38,969 m; peak 1,357.6 km/h | FAI record listings (fai.org/node/193240 cited in Day 1 v3); Guerster & Walter 2017 | earlier session; FAI page not reopened today | paper summary + prior citation | Recheck record wording on production day |
| V01-C10 | Eustace 2014: jump from about 41 km; highest jump on record | SOURCE_CHECKED | 135,890 ft = 41,419 m (several news outlets); one source lists 135,908 ft | NBC News, Smithsonian Air & Space, Scientific American (search results 2026-11-24) | 2026-11-24 | search snippets only | FAI ratification of the altitude not confirmed by a primary FAI page in this session |
| V01-C12 | Spacecraft return from orbit at about 28,000 km/h | CALCULATED_SELF_REVIEW | 7.8 km/s × 3.6 ≈ 28,000 km/h | circular low-Earth-orbit speed v=√(GM/r), r≈6,780 km | 2026-11-24 | own calculation | Entry speeds vary by mission |
| V01-C13 | Model assumes a fixed drag shape and omits heating | ASSUMPTION | stated limitation | model header | 2026-11-24 | own code | Spoken as a limit, not a result |

## Title promise check
Last paragraph answers the title: neither is faster at arrival in the model; the tall fall is longer. The title does not promise real-world certainty and the script says where measurement stops (41 km).

## Removed or rewritten from v1
v1 sentence 'The air is about two million times thinner' became 'more than a million' (table above 86 km was recalled). v1 header said 4:45 and body said 3.5–4 min: replaced by one range. v1 said 'for the first minute and a half it hardly matters': changed to 'first minute or so' (the model reaches Mach 1 at ~50 s). v1 'the model also leaves out heating, which at these speeds matters' kept in softer form.
