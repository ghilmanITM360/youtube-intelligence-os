# Day 1: three-way comparison — decision for owner

The approved [Day 1 V3](../unreasonably-exact-01-free-fall/SCRIPT.md) remains approved and untouched. This is a proposal, not a replacement.

| Dimension | Owner-approved V3 | Claude research V2 | Codex draft |
|---|---|---|---|
| Scenario | Ladder 1 m to 400 km, vertical rest start | 1 km vs 100 km, vertical rest start | Same locked 1 km vs 100 km comparison; fixed shape, no wind |
| Speed | ~204 km/h model impact; ~320 km/h peak at 10 km | ~190 km/h impact, ~299 peak at 10 km (Short); 100 km ~3585 peak | ~190 km/h impact, ~3600 peak at 100 km; simplified model explicitly labeled |
| Parameter | CdA/m = 0.00505 m²/kg, calibrated to Baumgartner peak | B: 0.60×1.19/121.2 = 0.005891 m²/kg | Same B, reproduced locally; this is model output, not observed impact speed |
| Time/peak/impact | Ladder and HUD separate peak from landing; 400 km cold-open | Contrasts ~22 s vs ~6 min; peak vs impact | Contrasts ~22 s vs ~6 min; separates speedometer peak and ground |
| Model limits | Fixed coefficient, atmospheric approximations; V3 suggests ±15% for above 39 km despite not having a validated error bound | High-Mach drag, heating and recalled density flagged; no survival prediction | Same cautions spoken; precise 100 km peak flagged as especially uncertain |
| Packaging | Title and existing thumbnail compare 1 km and 100 km at 204; ladder includes 400 km | Title explicitly compares 1 and 100 km | Title asks if space makes impact faster; no new thumbnail |
| Narrative | Ambitious ladder, real jump, graphic tracker and orbit coda | Focused single comparison, clear model accounting | Focused 2-question reveal and visual speedometer, omits unsupported survival and universal error band |

**Reproduction:** `python3 productions/unreasonably-exact-codex-drafts-2026-11-24/model-reproduction/fall_model.py` runs a copy of the existing stdlib RK4 model with output directory in this draft package. A: 1 km ground 204.0, 100 km ground 204.3 km/h. B: 1 km 188.85 km/h in 22.47 s; 100 km peak 3585.17 km/h, ground 188.96 km/h in 357.57 s; 10 km peak 299.13 and ground 188.96 km/h. The output CSV rounds its `cdam` column to 0.01; use actual parameters in source code, not that rounded field. This reruns the same model, not an independent validation. Above 86 km the script explicitly says density table was recalled, and drag is constant across regimes. The old V3 fit to one observation is a consistency check, not proof of a universal ±15% band. No calculation here establishes injury or survival.

**Dependencies:** `NARRATION_NOTES.md` instructs owner to record the exact approved words, with segment timings and emphasis; `thumbnail_day01.svg/png` and the approved script show 204 values; peak/landing HUD and the Day 2 Short excerpt use V3's numbers. A change to script, numbers, timing or picture requires revised assets, narration notes and renewed owner review, plus aerodynamicist review for material science; it does not automatically revoke prior approval. README contains old version/status wording, but the script itself records owner approval.

**Recommendation:** For the newly locked comparison, use the Codex script as the review candidate: it directly addresses the two heights and separates peak, elapsed time and impact with visible caveats. Retain the approved V3 as the existing production choice until the owner decides. Consider salvaging its clear ladder/HUD and real-flight distinction if the owner prefers its broader scope, after scientific review. Do not interchange 190 and 204; they arise from different inputs.
