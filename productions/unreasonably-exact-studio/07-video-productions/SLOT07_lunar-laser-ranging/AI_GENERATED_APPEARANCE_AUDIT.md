# AI-generated appearance and generic-content audit: V1 → V2

**Scope.** Every scene of `ROUGH_CUT_V1_final.mp4` was checked on two labelled contact sheets of 28 frames, plus an 8-frame P13 strip, before any change was made. V2 was checked the same way after rendering (see "Post-render review").

**Purpose.** This audit exists to raise professional quality. It does not hide how the film was made: Codex illustrated the artwork from photo references, and Claude rigged, animated, composited and graded it.

## Defects

### P03 opening, 0.12–0.95 s

- **Defect:** A vertical seam on the observatory wall while the shutter opens.
- **Cause:** The two Codex plates (closed and open) differ in micro-texture everywhere. They were blended through a full-height column.
- **Correction:** The open plate is the base everywhere. The closed plate appears only inside the slit region, with feathered edges.
- **Verification:** The 4-state still check (0, 0.3, 0.6, 1.0) shows no wall seam.

### P13 push, 45.2–45.9 s

- **Defect:** Pixel stair-steps on the cube rims (the "upscaled bitmap" look).
- **Cause:** The array was drawn offscreen at 1 px per design unit and then magnified about 40×.
- **Correction:** The offscreen resolution now follows the on-screen magnification (capped at 4×). The cutaway dissolve starts 0.27 s earlier.
- **Verification:** Stills at 44.9, 45.2 and 45.5 s show smooth rims.

### P13 push, 44.6–45.0 s

- **Defect:** Over-soft frames that read as a focus error.
- **Cause:** The rack-focus gain of 3.2 was too strong.
- **Correction:** Gain reduced to 2.4.
- **Verification:** Still at 44.9 s. Temporal motion blur remains on purpose, because the push is fast.

### P06 → P13 cut, 43.55 s

- **Defect:** The astronaut vanishes mid-action (an abrupt image transition).
- **Cause:** The P06 segment ended before the release.
- **Correction:** P06 now runs to 44.30 s and finishes the release and straighten, followed by a 0.35 s dissolve.
- **Verification:** The CUT list. A dissolve still at 44.6 s shows the expected double exposure.

### All Codex scenes vs vector scenes

- **Defect:** Inconsistent treatment: photoreal plates against flat, clean vector fields read as two productions.
- **Cause:** There was no global grade.
- **Correction:** One grade for the whole film: contrast, slight desaturation, cool shadows and warm highlights, a vignette and fine grain.
- **Verification:** A before/after strip of 4 scenes.

### Top-left badges, whole film

- **Defect:** Badges sat at 5 % of frame height, where the platform UI covers them on phones.
- **Cause:** BADGE_Y was 104.
- **Correction:** Moved to 150.
- **Verification:** Still at 20.0 s. A first move to 200 collided with the stopwatch and was rejected.

### Captions, whole film

- **Defect:** Generic generated-caption look: a dark card and a gold box on each word.
- **Cause:** The V1 caption renderer.
- **Correction:** Phrase-level, hand-lettered-style face, no card, balanced line breaks.
- **Verification:** `CAPTION_STYLE_COMPARISON.png`.

### B29, 67.7–70 s

- **Defect:** The narration had no matching picture (generic: the histogram kept running).
- **Cause:** The scene was missing.
- **Correction:** New G29 atmosphere scene.
- **Verification:** `gaps.check_all` passes; stills at 67.9, 68.7, 69.2 and 70.3 s.

### "A few photons", 65.9 s

- **Defect:** The picture did not match the words.
- **Cause:** P09's three-dot moment had been cut out.
- **Correction:** P09 re-enters from 65.55 to 67.45 s.
- **Verification:** Still at 66.6 s.

### Scatter, detection and measured-point dots

- **Defect:** Too small to read on a phone.
- **Cause:** Small radii.
- **Correction:** Radii enlarged by 1.5–1.7×; glow added on the final points.
- **Verification:** Code diff, plus the post-render review below.

## Checked and found acceptable

- **Floating props:** none. The reflector sits on its base, with a contact shadow that closes as it lands (P06).
- **Shadows:** consistent, Sun upper left, on the Moon scenes.
- **Alpha fringes:** none seen on the astronaut, reflector or observatory layers at full size. The Codex layers were cut on magenta and checked at a restack IoU of at least 0.97.
- **Camera motion:** every move is motivated:
  - the opening push follows the aim;
  - the Moon match-push follows the pulse;
  - the array push follows "corners";
  - the final pull back follows "the Moon isn't just hanging".

## Not fixed in V2 (reasons)

- **"Actually," imagined-mirror box (38.2–39.1 s).** A generic dashed rectangle. It is on screen for only 0.9 s and replaced on "yes.". A proper redesign needs new art. Deferred to V3.
- **Final orbit composition (88–96 s).** Earth and Moon are small with a lot of empty black. Changing the layout means re-checking G37. Deferred to V3.
- **P09/P10 empty fields (60–67 s).** These are data plots with large empty margins. Dots are enlarged; the layout is unchanged. Deferred to V3.
- **Near-photoreal style (owner decision D10).** The brief asks to keep the realism and harmonise it by grading, which V2 does. Nothing was repainted.

## Post-render review

See `FINAL_PRODUCTION_QA.md`, section "V2 full-film review". It is filled in from the 1080×1920 render.

### Post-render review (1080×1920 V2), done by Claude from sampled frames

Method: 4 labelled contact sheets (46 frames), P13 and G29 close strips, and frame differences measured on every frame.

Found and fixed before delivery:

- **G29 labels unreadable at phone size, 67.6–71 s.** Enlarged.
- **"no air" label white on white Arctic ice.** Labels moved to the finish line and the Earth re-tilted.
- **Pulse trail continued past the finish line.** Clamped.
- **Splice jump at 71.0 s.** The patch was extended through the crossfade; the splice-edge difference is now 0.2.

Confirmed in the V2 frames:

- **No dome seam** (0.5–2.5 s).
- **Smooth cube rims** through the push (45.4 s).
- **Captions clear of the Earth-limb station.**
- **Badges inside the safe area.**

Frame-difference peaks: maximum 30.1 → 25.8; frames above threshold 277 → 188.

Still open: the V3 items listed above. This review is not a substitute for continuous real-time viewing, which has not been done.
