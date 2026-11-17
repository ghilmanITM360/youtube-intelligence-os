# Image-to-Video System

Supersedes `IMAGE_TO_VIDEO_RECONSTRUCTION_GUIDE.md`. That file's specific
prompt templates, "8-word sentence → 1.8–2.0s hard ceiling" timing formulas,
and motion-characteristic prescriptions ("smooth, uniform scaling," "arc
paths matching physics") are generic AI-video-generation best-practice text,
not measurements derived from this corpus — no I2V synthesis was performed
anywhere in this project, so there is no source data to validate those
specifics against. This document keeps only what the corpus's own measured
structure actually implies about when I2V is appropriate.

## 1. Aspect ratio

- **Rule:** inherit the aspect ratio of the reference/target project — do not default to 16:9. Checked directly against each video's `00_source/SOURCE_MANIFEST.md`: 8/14 videos are portrait 9:16 (`Could you power your computer by typing?`, `drained_oceans`, `earthquake-magnitude-shorts-wBLVmEZV2Oc`, `how_long_could_you_drive_towards_the_sunset`, `weird_and_worrying_questions`, `what_if_all_visible_light_was_a_single_beam`, `what_if_the_moon_were_made_of_protons`, `worlds-largest-cities-what-if`) and 6/14 are landscape 16:9 (`could_you_survive_nanosecond_sun`, `if_all_humans_died`, `if_toaster_in_freezer`, `what-if-earth-grew-1cm-every-second`, `what_if_earths_water_suddenly_disappear`, `what_would_a_magnitude_15_earthquake_be`). The split is close to even — a fixed default in either direction would be wrong for close to half the corpus.

## 2. When continuous/organic motion is actually present

- 438 motions exist in `MASTER_MOTIONS.csv`. Of these, `SEQUENTIAL` (131), `SIMULTANEOUS_COUPLED` (36), `SIMULTANEOUS_INDEPENDENT` (29), and `PERSISTENT_LOOP` (7) — 203/438 (46%) — describe a genuine multi-frame progression (a growth, a reveal that plays out over time, a looped implied motion) rather than an instantaneous swap. These are the only motions with a plausible case for I2V generation.
- `STATE_REPLACEMENT` (230/438, 53%) is, by definition, one static illustration being discretely swapped for another — these are **not** continuous motion and should remain deterministic image swaps, not I2V-generated, per the original task's own instruction (step 24: "static plates, exact diagrams, maps, text, and deterministic state replacements should normally remain deterministic").

## 3. Duration source

- Use the real per-motion `DURATION_SEC` from `MASTER_MOTIONS.csv` for whichever specific motion is being reconstructed, not a formula derived from sentence word-count. No measured relationship between sentence length and motion duration was established in this pass (deriving one would require correlating `MASTER_SENTENCES` durations against `MASTER_MOTIONS` durations per matched event, which was not done here and should not be assumed without that check).

## What is NOT supported by current data (dropped from the prior guide)

- The specific prompt-template structure (`[START_STATE]/[END_STATE]/[NARRATION]/[DURATION]`) and the worked examples in the old guide are illustrative text, not derived from any measured field.
- The "3-word sentence → 0.8s, 5-word → 1.3s, 8-word → 1.8–2.0s hard ceiling" timing formula is not supported by any correlation actually computed in this project.
- No claim is made about "natural" motion paths (arcs, physics-matching movement) — the schema records `DIRECTION_OR_PATH` as free text per motion; consult that field for the specific motion being reconstructed rather than a general rule.
