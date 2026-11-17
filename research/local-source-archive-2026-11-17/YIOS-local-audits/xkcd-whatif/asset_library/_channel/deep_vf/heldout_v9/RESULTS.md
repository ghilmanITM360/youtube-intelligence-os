# Held-out v9 results — FROZEN_RULES_v3 (Shorts colour + motion; LOCAL ONLY)

## Setup
- **Rules:** frozen 2026-11-08T23:26:29Z (`../FROZEN_RULES_v3.sha256`). The eval re-checked every frozen hash before running.
- **Picks:** two Shorts chosen by title rule (`../heldout_v9_selection.json`) from the **13** local Shorts that no set had used.
- **Source SHAs** match `census.csv`:
  - 19gun1mffWs: bb276f97…
  - FKXVs4UteSc: ceae7efb…
- **Order:** both were ingested and segmented after the freeze. M0, the F_* flags and C3 were recorded (`M0_F_labels.json`) **before** the labeller ran.
- **Viewed:**
  - `*_holds.jpg` (both);
  - `19gun1mffWs_nondefault.jpg`;
  - `FKXVs4UteSc_camera_ruler_pairs.jpg` (the frames before and after each camera and ruler segment).
- **Earlier results unchanged:** v7 19/23 and v8 32/34.

## Parent / asset overlap (MEASURED: share of the Short's ASR words covered by 6-grams of the parent's ASR, `../v3/parent_asr_overlap.txt`)
| Short | Parent | Overlap | Parent status | Independence |
|---|---|---|---|---|
| 19gun1mffWs | gp5G1QG6cXc "What if Earth suddenly stopped spinning?" | 0.993 | ingested for quant only, never viewed | Independent of every viewed set. Art is probably reused from the parent. |
| FKXVs4UteSc | e3uk7jU3RHo "magnitude 15 earthquake" | 0.947 | v7 held-out (viewed) and v8 tool check | **Not independent** of v7 |

## Scores
| Check | 19gun1mffWs (MAP_TOUR, 9/23 map holds) | FKXVs4UteSc (**JOURNEY_LADDER**: magnitude ruler in 24/25 holds) |
|---|---|---|
| C1 red full frames | PASS 0 | PASS 0 |
| C2 conditional colour (viewed) | PASS 4/4: DARK_FIELD tiles are black city-skyline silhouettes with wind-blown debris | PASS (trivial, 0 non-default tiles) |
| C3 photographs | PASS (none) | PASS (none) |
| M1 camera instances / all ACTIVITY | PASS 1/22 = 0.045 ≤ 0.45 (raw 1 move) | **UNDEFINED**: the frozen rules have no Short limit for JOURNEY_LADDER. Measured 2 instances / 24 = 0.083 (2 single moves). |
| M3 object / all | PASS 3/22 | PASS 4/24 |

- **Colour verdict: 6/6 → HOLDS.** One of the two C2 passes is trivial.
- **Motion verdict: 3/3 scorable → HOLDS.** If the UNDEFINED check is counted as a non-pass, it is 3/4.
- **Overall: 9/9 scorable = 100%.** Counting the undefined check as a non-pass gives 9/10 = 90%, which still meets the bar.

## Feature-present result (reported separately, as frozen)
| Feature | Present? | Result on feature-present cases |
|---|---|---|
| F_MAP (saturated MAP_FILL map) | **ABSENT.** The 19gun maps are grey and achromatic (class LINE_ART, saturation 0.0). | **0 cases → the MAP_FILL C2 change is UNTESTED** |
| F_SCROLL (one camera instance with ≥2 whole-frame moves of a strip, axis or stack) | **ABSENT.** FKXV has 2 camera moves 52 s apart, each its own instance, and the viewed pairs show scene transitions, not a strip scroll. | **0 cases → the instance-merge M1 change is UNTESTED** |

**This is a coverage gap.** v9 passes the v3 rules but does **not** test either v3 change. The title rules did not predict the features:
- the "population" map is drawn in grey;
- the "earthquake" Short scrolls a **ruler**, not a film strip.

What is left:
- The remaining unused Shorts (11) include ERieN5pee7A, but it is from the same parent, gp5G, so it is probably grey maps too.
- No title in the pool points to a saturated map or a film strip.
- A feature-present test needs either a screen pass over the pool **before** the freeze (a disclosed exposure) or new Shorts.

## Journey finding (not a scored v3 rule)
- **FKXV is a scale-ladder Short.** A persistent magnitude ruler sits on the left edge with a fixed pointer, and its scale shifts with each magnitude step (1 → 0 → −1 … −8 → −15).
- **Measured motion:**
  - 9 RULER_SCROLL labels; the viewed before/after pairs confirm the scale ticks move;
  - whole-frame camera 2/24 = 0.083;
  - object 4/24.
- **What this matches:** the frozen JOURNEY_LADDER claim for longs (M1 ≤ 0.13; M2 ruler ≥3). The ladder's motion is ruler scroll, not extra camera.
- **Why it is only descriptive:**
  1. it is a Short, and M2 is long-only;
  2. it is an excerpt of e3uk, which was already used as the ruler tool check.
- It does **not** validate the long JOURNEY_LADDER arm.

## Production consequences
1. **A ladder Short is a real format.** Use a persistent side ruler with a pointer, a "MAGNITUDE n" header per step, and a new subject per step. The ruler scrolls, and the camera mostly stays still.
2. **Maps in Shorts can be grey/achromatic.** MAP_TOUR does not imply colour, so the TINT/MAP_FILL choice is a style decision, not a format requirement.
3. **Rule gap to close in v4:** a Short JOURNEY_LADDER M1 limit. Proposal: use the long value of 0.13. It is not frozen.
