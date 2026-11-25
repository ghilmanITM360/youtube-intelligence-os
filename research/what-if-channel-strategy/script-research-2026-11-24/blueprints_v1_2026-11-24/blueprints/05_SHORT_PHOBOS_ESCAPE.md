# Blueprint 05 — SHORT — Phobos escape (Day 13)

**STATUS: PARTIAL — NEEDS SOURCE/CALCULATION.** The safe core ("a normal jump falls back; 11.3 m/s is the textbook escape speed; escaping Phobos is not leaving Mars") is sourced and calculated. The interesting twist (Mars's pull lowers the best-case speed) is a hypothesis from a crude sphere model and must not be stated as a result until a shape-model trajectory is reviewed. SELF-REVIEW.

## A. IDENTITY
- **Calendar:** Day 13, Short (50–60 s).
- **Current working title:** "Could You Jump Off a Moon and Never Come Back?"
- **Issue:** "a Moon" can be misread as Earth's Moon; the question concerns Phobos.
- **Proposed alternatives:**
  1. "Could You Jump Off Mars's Moon Phobos and Never Come Back?"
  2. "Could You Jump Off Phobos?" (Claude review's title)
- **Central question:** Could a jump off Phobos send you away for good, or would you fall back?
- **One-sentence answer (qualified):** A normal jump (≈ 3 m/s) falls back — in our sphere model after roughly 15–30 minutes (12–155 min across the shapes we tried) — because Phobos's escape speed is about 11 m/s (40 km/h); and even if you escaped Phobos you would still be in orbit around Mars, which needs another ≈ 0.9 km/s to leave.
- **Viewer expects:** "tiny gravity, so yes".
- **Viewer actually learns:** escape speed in km/h; why a jump is far below it; the difference between leaving a moon and leaving its planet.

## B. PRECISE SCENARIO
- **Changes (ASSUMPTION):** one person jumps straight up at ≈ 3 m/s (a 0.45 m jump on Earth; V05-C07), unaided.
- **Normal:** Phobos as it is (mass 10.6e15 kg; semi-axes 13.0/11.4/9.1 km; V05-C02), in orbit around Mars at 9,378 km.
- **Model (labelled):** point-mass sphere of the volume-equivalent radius 11.05 km, with Mars's pull added as a Hill-equation term; shape, rotation-induced bumps, Mars's oblateness and orbit eccentricity ignored.
- **Known vs hypothetical:** known — NASA's mass, size and 11.3 m/s (V05-C01); hypothetical — the 3 m/s jump and everything from the Hill simulation.

## C. DEPENDENCY MAP
| Needed | Source | Status |
|---|---|---|
| Escape speed ~11.3 m/s | NASA NSSDC mass + NASA 2012 slide (V05-C01) | agrees with own point-mass number |
| 3 m/s jump | assumption (V05-C07) | unsourced |
| Fall-back time and height | Hill sim: 17–31 min and 0.75–1.25 km for the volume-equivalent sphere; 12–155 min and 0.5–3.6 km across the three radii (V05-C05); uniform-g estimate 17 min | HYPOTHESIS-grade |
| Mars escape from Phobos's orbit | 2.138 km/s orbital; 3.022 km/s escape; +884 m/s (V05-C03) | arithmetic |
| Mars's pull at the surface | Hill radius 16.56 km ≈ 1.5 body radii (V05-C04); best-direction thresholds 4–7 m/s (V05-C06) | **OPEN — expert needed** |

## D. CAUSE-AND-EFFECT STORY (compact)
| # | Cause / question | Science | Result | Leads to | Visual | Claim |
|---|---|---|---|---|---|---|
| 1 | Hook: "Phobos is so small you could escape it with a jump… could you?" | — | the guess | "how fast would you need to go?" | Phobos as a lumpy potato with 13.0/11.4/9.1 km marked | V05-C02 |
| 2 | THEREFORE escape speed | v_esc = √(2GM/R) ≈ 11.3 m/s = 40 km/h (NASA agrees) | "a quick cycle ride's speed" | "how fast do you jump?" | speed dial at 11.3 m/s next to a small jump arrow at 3 m/s | V05-C01 |
| 3 | BUT a jump is only ~3 m/s | a 3 m/s jump rises ≈ 0.75–1.25 km and falls back after ~17–31 min (volume-equivalent sphere model; other shapes 12–155 min) | you fall back | "and if you did escape?" | arc with a clock, labelled "model" | V05-C05, V05-C07 |
| 4 | THEREFORE leaving Phobos isn't leaving Mars | Phobos moves at 2.14 km/s about Mars; Mars's escape speed there is 3.02 km/s | you'd still orbit Mars; leaving needs ≈ +0.88 km/s | answer | Mars with Phobos's orbit ring and two speeds | V05-C03 |
| 5 | **GATED beat (only after a shape-model check):** BUT Mars is pulling too | Hill radius is only ~1.5 body radii; best-direction thresholds look like 4–7 m/s in a sphere model | the "11 m/s" is the wrong ruler; direction matters | closing | arrow toward/away from Mars on the lumpy body | V05-C04, C06 |

## E. NUMBERS INTO IMAGINABLE SCALE
- 11.3 m/s = 40.7 km/h — "a quick bicycle ride" (comparison; conversion exact).
- 3 m/s ≈ 10.8 km/h — "a jog" (so a jog-speed jump).
- 884 m/s extra vs 2.14 km/s orbital speed — "a bit more than a rifle bullet's muzzle speed" is **not** used (unsourced comparison); show the km/s numbers.
- 17–31 min: "the length of a TV episode" (comparison approximate); qualification: sphere model; other sphere sizes gave 12–155 min, so say "roughly half an hour or less".

## F. HOOK, ESCALATION AND ENDING
- Hook (0–5 s): "Phobos is so small you might jump off it. Could you?"
- First non-obvious reason: the answer depends on two bodies, not one.
- Escalation: one step — from leaving Phobos to leaving Mars — no more.
- Direct answer: "A normal jump falls back. And escaping Phobos still leaves you circling Mars."
- Dry humor option: "the cheapest launch pad in the Solar System, unfortunately aimed at the wrong planet." (optional) No-joke alternative: end on the two speeds.

## G. VISUAL COMMUNICATION (text only)
- Lumpy body to scale with the three semi-axes; Mars not to scale unless labelled.
- Two speed dials: 11.3 m/s and 3 m/s, units clear; the orbit-speed numbers in km/s.
- Must not depict: a smooth sphere as if it were Phobos; an astronaut flying free of Mars; the gated beat's thresholds as results.

## H. ORIGINALITY AND PRIOR ART
- Closest: Munroe "Little Planet" (pp.103-104): escape speed is a speed (not a velocity) — you can leave in any direction away from the body; Phobos appears only as a photo mention in the OCR of p.103 (verify on the page). No video with this premise among registry titles; the channel's own search was not achieved (NOT CHECKED).
- Ours: a real, named moon with real numbers; "leaving Mars" as the second step; Mars's pull as the limit of the textbook ruler.
- Do not copy: the Little-Prince/asteroid framing or the "dunk a basketball" line.

## I. SCIENCE AND EDITORIAL REVIEW (SELF-REVIEW)
- Qualified: 11.3 m/s (two sources + own calculation); Mars escape arithmetic.
- Open: everything in the Hill-sim claims; shape and rotation (Phobos is synchronous so the surface is at rest in the rotating frame); the slide's own gravity values are garbled and unused.
- Highest-risk misunderstanding: "You can jump off Phobos at 5 m/s" if the gated beat is shown as a fact. Mitigation: keep the gated beat out until reviewed.
- Reviewer: planetary dynamicist with a Phobos shape model.
- Blockers: shape-model trajectory check; decide whether the gated beat ships.
- Confidence: research 0.7 for the core, 0.2 for the gated beat; story clarity high.

## J. FORMAT AND DEPENDENCIES
- **Distinct from the Long (blueprint 04):** the Long is horizontal orbit on a toy sphere; the Short is vertical escape on a real two-body moon.
- **Repeated for standalone clarity:** what escape speed means; the jump speed assumption.
- **Why after the Long (Day 13):** the Long builds the idea of speed thresholds; the Short adds the real-world complication.
- **If the Long is delayed:** publishes alone. **If the shape-model check isn't done:** publish with beats 1–4 only (still a complete question and answer).
