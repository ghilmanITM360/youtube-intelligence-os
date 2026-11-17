# Image-to-Video Rebuild

Reference `IMAGE_PROMPTS.md` (IMG01/IMG02/IMG03a/IMG03b) and `ANIMATION_PROMPTS.md`. Reference `02_analysis/*.csv` for IDs — literal frame descriptions are not repeated here.

## S01 — 00:00.000–00:04.420
STATE CHAIN: F01.0 → A01 → F01.1
SOURCE IMAGE: IMG01a (F01.0), IMG01b (F01.1)
IMAGE ACTION: Generate both (same style prompt, differ only in board content — see IMAGE_PROMPTS.md note on generating twice if in-place edit isn't available).
I2V PASS: NONE — ANIMATION REQUIRED: NO. Hold IMG01a ~0–2.0s, hard-cut to IMG01b ~2.0–4.42s.
EXPECTED RESULT: F01.1.
TEXT/GRAPHICS OVERLAY: T01 title card, added as a text+shape overlay in final assembly, on screen the full 4.42s.
COMPOSITE: none needed.
AUDIO: AU01 starts at 0:00.
CUT TO: S02, via optional A02 transition effect (see ANIMATION_PROMPTS.md) or a plain blur transition.
FIDELITY RISK: none (static holds only).

## S02 — 00:04.420–00:83.333
STATE CHAIN: F02.0 → A03 → F02.1 → A04 → F02.2 → A05 → F02.3 → A06 → F02.4 → A07 → F02.5 → A08 → F02.6 → A09 → F02.7 → A10 → F02.8
SOURCE IMAGE: IMG02 (one master plate, reused for the entire shot)
IMAGE ACTION: Generate IMG02 once, at the largest resolution available.
I2V PASS: NONE — ANIMATION REQUIRED: NO for the whole shot. Camera movement across IMG02 is done as crop/scale/position keyframes in your assembly tool (a "Ken Burns" pan), exactly matching the CapCut keyframe list in `03_capcut/CAPCUT_REBUILD.md`'s S02 build section — do not duplicate that keyframe timing table here.
EXPECTED RESULT: F02.8 (final held frame).
ADDITIONAL INDEPENDENT PASSES: IMG03a (G04) and IMG03b (G05) are each a separate static image, composited as their own overlay layer, not animated themselves — only their host layer's position moves (to stay map-anchored, per MOTION_EVENTS A08's CAMERA_SUBJECT_COUPLED relationship), matched by hand to the same crop keyframes used for IMG02 in that time window.
TEXT/GRAPHICS OVERLAY: 20x G02 city pin+label overlays, added at their observed appearance windows (see TIMELINE.csv / MOTION_EVENTS.csv R01/R02/R05); G03 red-circle overlay active only 0:30.00–0:35.40; continent name labels (NORTH AMERICA/ASIA/EUROPE/AFRICA/AUSTRALIA/SOUTH AMERICA) either baked into IMG02 or added as overlays — your choice depending on how reliably your generator renders legible hand-lettering.
COMPOSITE: G04 window ~0:44.50–0:55.00; G05 window ~0:76.00–0:83.333; both masked to their own circular region, everything outside the circle transparent.
AUDIO: AU01 continues unbroken from S01; no further confirmed sync cue points within S02 (see AUDIO_MAP.md — narration wording unknown, so word-level cues cannot be placed).
CUT TO: end of file.
FIDELITY RISK: IMG02 must be generated wide/tall enough to cover every crop window in the table above without running off the edge of the source art — if your generator caps resolution, generate IMG02 in 2–3 overlapping tiles and stitch, rather than re-generating separate unrelated map images per state (which would break continent-shape and color continuity between states).
