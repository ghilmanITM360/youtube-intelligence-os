# Blueprint 02 — SHORT — Skydiver slow-down (Day 4)

**STATUS: BLUEPRINT READY FOR OWNER REVIEW** (research/blueprint status only). Same model and same reviewer holds as blueprint 01; this Short uses only the mechanism, not the 100 km extrapolation. SELF-REVIEW.

## A. IDENTITY
- **Calendar:** Day 4, Short (target 45–60 s).
- **Current working title:** "Why Can a Skydiver Slow Down Without a Parachute?"
- **Issue:** true only for jumps from high up; a viewer may think every fall slows down.
- **Proposed alternatives:**
  1. "Why Does a High Skydiver Slow Down Before Landing — With No Parachute?"
  2. "How Can You Slow Down in Free Fall?" (shorter; keep "from high up" in the first sentence)
- **Central question:** If gravity never switches off, how can a falling skydiver lose speed with no parachute open?
- **One-sentence answer (qualified):** If you start high enough (above about 2 km in our model), you pick up more speed in thin air than thick air allows, so when the air thickens its drag exceeds your weight and you slow toward the ground's limit — if you start lower, you never slow down.
- **Viewer expects:** a trick (a hidden brake).
- **Viewer actually learns:** weight vs drag, why the limit depends on air density, and that the slow-down needs a high start.

## B. PRECISE SCENARIO
- **Changes (ASSUMPTION):** released from rest at 39 km (the real Stratos height is 38,969 m), belly-down, no parachute opened.
- **Normal:** standard atmosphere, windless, ground at sea level.
- **Model:** set B (Cd 0.60, A 1.19 m², m 121.2 kg; V01-C14); numbers are model results, not measurements.
- **Known vs hypothetical:** real jumper reached a peak of 1,357.6 km/h at 28.8 km (V02-C05); the slowing curve after the peak is modelled, not read.

## C. DEPENDENCY MAP
- Weight vs drag balance: `v_t = √(2mg/(ρ·Cd·A))` → ≈ 188 km/h at sea level (V01-C04). Source: Stratos paper inputs + own arithmetic.
- Air thicker at the ground than at 39 km: ρ₀/ρ ≈ 265 (V02-C02).
- Net deceleration after the peak ≈ 0.66 g; felt ≈ 1.65 g (V02-C03).
- Threshold release height for any slow-down ≈ 1.85 km (V02-C04).
- Gap: reviewer for the drag value (V01-C03).

## D. CAUSE-AND-EFFECT STORY (compact)
| # | Cause / question | Science | Result | Leads to | Visual | Claim |
|---|---|---|---|---|---|---|
| 1 | Hook: "Gravity keeps pulling, yet this skydiver loses speed." | — | the paradox in one sentence | "what else pushes?" | one arrow down (weight) and one up (drag) on a falling figure silhouette (no detail) | — |
| 2 | THEREFORE the air must be pushing back | drag grows with speed² and air density; at the ground it balances weight at ≈ 190 km/h | the ground's speed limit | "what if you're going faster than that?" | balance scale: weight vs drag; the drag side grows | V01-C04 |
| 3 | BUT at 39 km the air is ~265× thinner | with little air, drag is small, so speed overshoots | peak ≈ 1,315 km/h at ~28 km after ~50 s (real: 1,357.6 km/h) | "what happens as the air thickens?" | speed-vs-altitude line rising to a hump, real peak as a dot | V02-C02, V02-C05, V01-C06 |
| 4 | THEREFORE the air thickens and drag beats weight | net slowing ≈ 0.66 g; speed drops back toward ~190 km/h by the ground | no parachute needed to slow — a gentle ~1.7 g | "does this happen to every fall?" | the same line descending to the landing mark | V02-C01, V02-C03 |
| 5 | BUT only from high up | from < ~1.85 km the peak equals the landing speed | no slow-down from a normal jump height | answer | two curves: one with a hump, one flat | V02-C04 |

## E. NUMBERS INTO IMAGINABLE SCALE
- 1,315 km/h → ~190 km/h: "faster than sound at that height, down to a fast-car speed" (speed of sound varies with altitude: qualify). Model, not measured.
- ~265× thinner air at 39 km: show a density bar, not an analogy.
- 0.66 g net: "a gentle press — at most about 1.7 times your normal weight" (1.65 g felt); qualification: model.

## F. HOOK, ESCALATION AND ENDING
- Hook (0–5 s): "Gravity never stops pulling. So how can a skydiver slow down with no parachute?" State the condition "from high up" immediately.
- First non-obvious reason: slowing needs *more* speed than the air allows.
- Escalation: none beyond one real example.
- Direct answer: "Because thick air takes back what thin air let you gain — but only if you start high enough."
- Dry humor option: "no parachute, just air" (optional). No-joke alternative: end on the two curves, hump vs flat.

## G. VISUAL COMMUNICATION (text only)
- Beat 2: balance of two arrows; labels "weight (constant)" and "drag (grows with speed and air thickness)". Do not draw a detailed person.
- Beat 3–4: speed-vs-altitude curve, x-axis altitude (km, decreasing to the right), y-axis km/h; real peak point labelled "measured 1,357.6 km/h".
- Beat 5: two thumbnails of curves (high start, low start).
- Must not depict: a falling body in distress; real footage; any survival claim.

## H. ORIGINALITY AND PRIOR ART
- Closest: Munroe "Steak Drop" (pp.107-110) shows objects slowing to terminal speed from any height; "Free Fall" (p.195-196). No xkcd video with this exact premise among registry titles (titles only).
- Same broad science (terminal speed). Ours: the *slow-down mechanism as the question*, the weight-vs-drag balance, the "only from high up" threshold.
- Do not copy: steak framing, jokes, drawings.

## I. SCIENCE AND EDITORIAL REVIEW (SELF-REVIEW)
- Qualified: mechanism (physics); numbers (model).
- Open: drag value (V01-C03); threshold depends on drag (V02-C04).
- Highest-risk misunderstanding: "everyone slows down before landing" or "terminal speed is a fixed 200 km/h". Mitigation: the threshold beat and "model" labels.
- Reviewer: aerodynamics expert (drag; shared with blueprint 01).
- Blockers: reviewed drag range; re-open the Stratos paper PDF.
- Confidence: research 0.6, story clarity high (subjective).

## J. FORMAT AND DEPENDENCIES
- **Distinct from the Long:** the Long compares heights (peak vs landing); the Short explains *why speed can drop* with one curve and one force balance.
- **Repeated for standalone clarity:** what terminal speed is; the no-parachute, from-rest rules; "from high up".
- **Why after the Long (Day 4):** it answers the reflex question the Long raises ("it slowed down?") without needing the ladder.
- **If the Long is delayed:** can publish (self-contained). If this Short is delayed: no effect.
