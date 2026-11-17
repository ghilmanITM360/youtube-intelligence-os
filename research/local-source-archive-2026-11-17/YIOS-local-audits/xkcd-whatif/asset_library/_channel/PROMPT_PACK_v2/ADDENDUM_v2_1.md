# Prompt pack v2.1 addendum (clarifications; STYLE_BIBLE_AND_PROMPTS_v2.md unchanged; this file wins where they differ)

## 1. Shorts opening: target vs acceptance
- **Target (SHT-002):** question chip or subject visual pops at **f <= 6** (0.25 s).
- **Acceptance limit (§C, rule A3 opening check):** something must be on screen by **f < 24** (1.0 s), measured as > 2000 px change vs f0.
- A render between f7 and f23 PASSES acceptance but MISSES target: report both. Attempt 3 9:16 = f6 (meets both).

## 2. Class-specific exceptions to the shared locks (explicit)
The shared lock text (black monoline, flat fills, no gradients, no texture, no outline glow) applies to LINE_ART, RED_MARK, RED_SOLID, TINT_REGION and MAP_FILL **as written**. Exceptions:
| Class | Overrides | Keeps |
|---|---|---|
| DARK_FIELD | line colour **white #FCFCFC** on #0C0C0C/#1C1C1C/#343434; silhouettes pure black | uniform line weight, wobble, round ends, flat fills, faceless figures, no shading |
| GLOW | one **soft radial gradient** allowed (the only gradient), on a dark field; enters by 6-frame linear dissolve | no rays, no lens flare, no texture, objects drawn over it keep the locks |
| DARK_FIELD + GLOW combined (lamp, sun, beam) | both overrides above | everything else |
When a prompt uses one of these classes, replace the lock clause it overrides with the class wording; never drop the other lock clauses.

## 3. Observed but NOT adopted (owner decision)
- Film grain over the whole frame and soft radial ground/lamp glows appear in several source videos (closure evidence: kNry0bf7eC0, TIDHee_Q5Gk `closure_v1/CLOSURE.md`). The pack keeps "no texture"; a FILM_GRAIN option is listed here only so the gap is visible.
