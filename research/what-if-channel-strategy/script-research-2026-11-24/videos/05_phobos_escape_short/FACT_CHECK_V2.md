# Fact check V2 · slot 05

Allowed statuses: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED.
"CALCULATED_SELF_REVIEW" means I (Claude) ran the arithmetic or model myself; it is not expert confirmation. Access date for web sources: 2026-11-24 unless stated.

| ID | Claim as spoken or implied | Status | Value / calculation | Source or method | Accessed | Reading depth | Note |
|---|---|---|---|---|---|---|---|
| V05-C01 | Phobos is about 22 km across on average (mean radius about 11 km) | SOURCE_CHECKED | mean radius 11.08 ± 0.04 km; dimensions 25.9 × 22.6 × 18.3 km | Wikipedia 'Phobos (moon)' citing Ernst et al. 2023 (secondary; paper not opened); NASA says 27 × 22 × 18 km | 2026-11-24 | part of Wikipedia page; NASA page summary | Primary paper not read |
| V05-C02 | Escape speed of a perfect ball of Phobos's mass and radius is about 11 m/s (about 40 km/h) | CALCULATED_SELF_REVIEW | √(2GM/R)=√(2×6.6743e-11×1.0637e16/11,080)=11.3 m/s = 40.8 km/h; Wikipedia lists 11.39 m/s | own arithmetic; mass from secondary source | 2026-11-24 | calculation | Uses mass 1.0637e16 kg; NSSDC lists 10.6e15 kg |
| V05-C03 | A very strong jump leaves the floor at about 2–3 m/s | ASSUMPTION | √(2 g h) for h≈0.4–0.5 m | own arithmetic | 2026-11-24 | calculation | Spoken as an assumption |
| V05-C04 | With 2–3 m/s in a ball model the jumper falls back after about a quarter of an hour | CALCULATED_SELF_REVIEW | t=2v/g, g=0.0057 m/s²: 700–1,050 s (12–18 min) | own arithmetic; g from secondary source | 2026-11-24 | calculation | Real surface gravity ranges roughly 0.002–0.008 m/s² in reports |
| V05-C05 | Local surface acceleration on Phobos includes self-gravity, spin (centrifugal) and Mars tidal terms and varies by place and time | SOURCE_CHECKED | qualitative | Herreros & Charnoz 2026, arXiv:2607.10445, Appendix A (part of paper read by sub-agent) | 2026-11-24 | part of paper | No numeric escape-speed range in the passages read |
| V05-C06 | Reported local escape speeds differ between sources and no primary source settling the lowest value was found | UNRESOLVED | secondary: ~1.4–10 m/s (blog on a 2018 paper), ~4–10 m/s (MDPI snippet), 11.4 m/s global (Wikipedia) | secondary only | 2026-11-24 | snippets and summaries | Spoken as 'reported values differ'; no number from these sources is spoken |
| V05-C07 | Leaving Phobos still leaves you in orbit around Mars; leaving Mars needs hundreds of m/s more | CALCULATED_SELF_REVIEW | at Phobos's orbit (r≈9,376 km) circular speed ≈2.14 km/s and escape ≈3.02 km/s: ~0.88 km/s more | own arithmetic with Mars GM 4.2828e13 m³/s² and orbit radius recalled from memory | 2026-11-24 | calculation; constants recalled | Constants not re-sourced today; wording kept at 'hundreds of metres per second' |

## Title promise check
Answer is conditional and consistent with the evidence: ball model says no; real moon unsettled; leaving Phobos is not leaving Mars.

## Removed or rewritten from v1
v1 ending 'So: not with a jump, and not for good' removed: it contradicted the stated uncertainty. v1 'a trip lasting tens of minutes' replaced by 'about a quarter of an hour' (calculated).
