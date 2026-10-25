# WAY 2 — Image-to-Video Shot Rebuild — weird_and_worrying_questions

This entire video is one locked-camera shot (S01), so this document proceeds by joke segment rather than by camera shot. References `IMAGE_PROMPTS.md` (IMG01–IMG14) and `ANIMATION_PROMPTS.md` (A01–A25). No generation/rendering has actually been performed — this is a build specification.

## S01 — 00:00.000–00:47.458 (entire video, single locked shot)

### Segment 1 — Shelby / cold teeth (F01.0–F01.7)
STATE CHAIN: F01.0 → A01 → F01.1 → A02 → F01.2 → A03 → F01.3 → A04 → F01.4 → A05 → F01.5 → A06 → F01.6 → A07 → F01.7
SOURCE IMAGE: IMG01 (start), IMG02 (end) — first/last-frame pair
IMAGE ACTION: Generate both.
I2V PASS: A01–A05 chained as ONE guided transition pass from IMG01 to IMG02 (all are sequential parts of a single "drawing reveals itself" build-up and are physically coupled, per spec §24 — no need for five separate generations). A06 (mug-throw) is a SEPARATE independent pass, since it is a distinct physical action layered on top of the already-drawn bubble content. A07 (clear to blank) is produced in final assembly as a simple opacity fade-out, not a generative pass.
EXPECTED RESULT: F01.7
TEXT / GRAPHICS OVERLAY: T01 card #1 (Shelby) added as an editor overlay for the full segment duration until it is removed at F01.7.
AUDIO: AU01 continuous from 00:00.000.
CUT TO: Segment 2.
FIDELITY RISK: forcing A01–A05 into one pass risks the model over- or under-pacing the sub-reveals (teeth → thermometer → mercury drop → shatter → mug); if drift occurs, split into two passes (bubble+teeth+thermometer+mercury as one, shatter+mug as a second) using an intermediate extracted frame as the second pass's source.

### Segment 2 — Mirrors aside + Jeff / new star (F01.8–F01.13)
STATE CHAIN: F01.7 → A08 → F01.8 → A09 → F01.9 → A10 → F01.10 → A11 → F01.11 → A12 → F01.12 → A13 → F01.13
SOURCE IMAGE: IMG03 (reused blank plate) for A08–A09; IMG05 for A10–A11; IMG06 for A12–A13.
IMAGE ACTION: Reuse IMG03; generate IMG05 and IMG06.
I2V PASS: A08 (C02 entrance) and A09 (C02 exit/reset) as two short independent passes from IMG03. A10–A11 (graphic reveal, then swap to standing figure) as one chained pass from IMG05. A12–A13 (caption appears, then clears) as one chained pass from IMG06.
EXPECTED RESULT: F01.13
TEXT / GRAPHICS OVERLAY: T02 caption "HOW MANY MIRRORS..." during F01.8; T01 card #2 (Jeff) for the full segment from F01.9; T02 caption "...MAYBE" during F01.12.
AUDIO: AU01 continuous.
CUT TO: Segment 3.
FIDELITY RISK: A08's C02 entrance is a new-character introduction, historically higher drift risk than a graphic-only change; keep the prompt's static-anchor language on the seated figure and desk explicit.

### Segment 3 — Tomasz / volcano (F01.14–F01.16)
STATE CHAIN: F01.13 → A14 → F01.14 → A15 → F01.15 → A16 → F01.16
SOURCE IMAGE: IMG07 (start), IMG08 (end) — first/last-frame pair
IMAGE ACTION: Generate both.
I2V PASS: A14 (bubble+mountain reveal) from IMG07; A15 (eruption) as the transition pass from IMG07 to IMG08; A16 (clear to blank) produced in final assembly as an opacity fade-out.
EXPECTED RESULT: F01.16
TEXT / GRAPHICS OVERLAY: T01 card #3 (Tomasz) for the full segment.
AUDIO: AU01 continuous.
CUT TO: Segment 4.
FIDELITY RISK: none significant; both states are simple, isolated graphics.

### Segment 4 — AJ / Chernobyl + plaque (F01.17–F01.22)
STATE CHAIN: F01.16 → A17 → F01.17 → A18 → F01.18 → (hold, F01.19) → A19 → F01.20 → A20 → F01.21 → A21 → F01.22
SOURCE IMAGE: IMG09 (F01.17–F01.19), IMG10 (F01.20), IMG11/IMG12 (F01.21–F01.22, first/last-frame pair)
IMAGE ACTION: Generate IMG09, IMG10, IMG11 and IMG12.
I2V PASS: A17–A18 chained from IMG09 (building+icon reveal, then label added); F01.19 is a static hold, ANIMATION REQUIRED: NO — simply hold IMG09 for its measured duration; A19 as the transition pass from IMG09 to IMG10; A20 as an isolated pass (explosion clears, full-frame plaque fades in — a large compositional change, kept separate to avoid drift); A21 as the transition pass from IMG11 to IMG12 (caption area fills, figure's pose changes).
EXPECTED RESULT: F01.22
TEXT / GRAPHICS OVERLAY: T01 card #4 (AJ) for F01.17–F01.20; 'ANTIMATTER →' label recommended as an editor overlay (or lightly baked per IMG09's note) during F01.18–F01.19; T02 caption "FOR GOD'S SAKE, WHAT WERE YOU THINKING?!" added during F01.22 (plaque heading itself is baked into IMG11/IMG12 per that image's TEXT BAKED: YES).
AUDIO: AU01 continuous; a measured 0.10–0.12s near-silence gap falls around 34.5–34.7s (within A19–A20), APPROXIMATE sync only.
CUT TO: Segment 5.
FIDELITY RISK: A20 is the segment's biggest compositional jump (bubble-based diagram → full-frame plaque); the explicit IMG11 first-frame anchor reduces drift versus letting the model free-associate the plaque's layout.

### Segment 5 — Karl / crying (F01.23–F01.26)
STATE CHAIN: F01.22 → A22 → F01.23 → A23 → F01.24 → A24 → F01.25 → A25 → F01.26
SOURCE IMAGE: IMG13 (start), IMG14 (end) — first/last-frame pair, plus reused IMG03/IMG14 endpoints for the closing captions
IMAGE ACTION: Generate IMG13 and IMG14; reuse IMG14's end frame (blank of bubble, figure only) for A24–A25, or reuse IMG03 if the plain base plate matches closely enough.
I2V PASS: A22 (plaque clears, crying-figure bubble appears) as an isolated pass from IMG13; A23 (puddle growth, ~3s) as the transition pass from IMG13 to IMG14; A24 (bubble clears, short caption appears) and A25 (caption extends) chained as one short pass ending the video.
EXPECTED RESULT: F01.26 (video ends)
TEXT / GRAPHICS OVERLAY: T01 card #5 (Karl) for F01.23–F01.24; T02 captions "...KARL" (F01.25) then "...KARL, IS EVERYTHING OK?" (F01.26).
AUDIO: audio's two closing near-silence gaps (~45.5–46.0s, ~46.9–47.3s) land close to the "...KARL" and "...KARL, IS EVERYTHING OK?" caption beats — APPROXIMATE sync only, no transcript available.
CUT TO: end of video.
FIDELITY RISK: none significant; both remaining passes are simple, isolated graphic/caption changes.

---

## Final assembly and export
Assemble all five segments in order at 24fps, 1080x1920, placing AU01 as a single continuous audio track from 00:00.000 with its natural ~0.05s trailing tail preserved. Add every T01 Q-card and T02 caption as editor overlays per the exact wording and timing recorded in `../02_analysis/TIMELINE.csv`, since text was deliberately left off every generated image except the two-word plaque heading in IMG11/IMG12 (TEXT BAKED: NO elsewhere throughout). Insert simple opacity fade-out cuts (not generative passes) for every "clear to blank" transition (A07, A09, A13, A16, A24) to save generation budget, since these involve no new visual content, only removal of the existing content. Total export duration: 47.458s video (1139 frames at 24fps) with the audio track's ~0.05s tail beyond the last video frame preserved. No image, video, or audio has actually been generated or rendered as part of this analysis — this document is a build specification only.
