# Image-to-Video Rebuild — what_if_earths_water_suddenly_disappear

One compact block per shot. Source images: `IMAGE_PROMPTS.md`. Animation prompts: `ANIMATION_PROMPTS.md`. Final export target: 1920x1080, 24fps, 183.792s.

## S01 — 00:00.000–00:08.292
STATE CHAIN: F01.0 → A01 → F01.1 → A02 → F01.2 → A03 → F01.3
SOURCE IMAGE: IMG01 (start), IMG02 (end) — first/last-frame pair
IMAGE ACTION: Generate both.
I2V PASS: A01, A02, A03 chained as one guided sequence from IMG01 to IMG02 (all three are minor additive reveals on the same static host+blackboard composition).
EXPECTED RESULT: F01.3.
TEXT/GRAPHICS OVERLAY: Q-card question text (not baked; overlay per IMG01 notes).
AUDIO: continuous narration (UNKNOWN exact words).
CUT TO: S02.

## S02 — 00:08.292–00:10.292
STATE CHAIN: F02.0 (static hold)
SOURCE IMAGE: IMG03
IMAGE ACTION: Reuse as a static hold — ANIMATION REQUIRED: NO.
EXPECTED RESULT: F02.0.
AUDIO: near-silence gap 9.48–10.35s.
CUT TO: S03.

## S03 — 00:10.292–00:17.375
STATE CHAIN: F03.0 → A04 → F03.1 → A05 → F03.2
SOURCE IMAGE: IMG04 (F03.0, F03.2 — reused), IMG05 (F03.1)
IMAGE ACTION: Generate IMG04 and IMG05; reuse IMG04 for both bookend states.
I2V PASS: A04 (IMG04→IMG05), A05 (IMG05→IMG04, reusing the same source frame as the target).
EXPECTED RESULT: F03.2.
TEXT/GRAPHICS OVERLAY: "VACUUM" label (baked-adjacent per IMG05 clean-plate note).
AUDIO: continuous narration.
CUT TO: S04.

## S04 — 00:17.375–00:26.792
STATE CHAIN: F04.0 → A06 → F04.1 → A07 → F04.2
SOURCE IMAGE: IMG06 (start), IMG07 (end) — first/last-frame pair
IMAGE ACTION: Generate both.
I2V PASS: A06, A07 chained from IMG06 to IMG07 (continuous seafloor-exposure reveal).
EXPECTED RESULT: F04.2.
AUDIO: continuous narration.
CUT TO: S05.
FIDELITY RISK: exact exposure-growth rate is APPROXIMATE (2-second sampling only).

## S05 — 00:26.792–00:39.625
STATE CHAIN: F05.0 → A08 → F05.1 → A09 → F05.2 → A10 → F05.3 → A11 → F05.4
SOURCE IMAGE: IMG04 (reused start), IMG08 (end)
IMAGE ACTION: Reuse IMG04; generate IMG08.
I2V PASS: A08–A11 chained as one guided sequence from IMG04 to IMG08 (debris accumulation, then timer overlay + boat sinking).
EXPECTED RESULT: F05.4.
TEXT/GRAPHICS OVERLAY: "1 SECOND" timer, "5m" scale bar (per IMG08 clean-plate note).
AUDIO: measured near-silence gap 32.4–32.6s falls within this shot.
CUT TO: S06.

## S06 — 00:39.625–00:58.750
STATE CHAIN: F06.0 → A12 → F06.1 → A13 → F06.2
SOURCE IMAGE: IMG09 (start), IMG10 (end)
IMAGE ACTION: Generate both.
I2V PASS: A12 (IMG09→IMG10, fleet growth), A13 (IMG10→gray fade, no additional image needed — solid-color fade handled in final assembly).
EXPECTED RESULT: F06.2 (ending on a full-frame gray hold).
AUDIO: near-silence gap 58.744–58.921s coincides with the fade.
CUT TO: S07.

## S07 — 00:58.750–01:04.375
STATE CHAIN: F07.0 (static hold after fade-in)
SOURCE IMAGE: IMG11
IMAGE ACTION: Generate; ANIMATION REQUIRED: NO (static hold).
EXPECTED RESULT: F07.0.
COMPOSITE: fade in from the S06 gray hold in final assembly.
AUDIO: continuous narration.
CUT TO: S08.

## S08 — 01:04.375–01:09.208
STATE CHAIN: F08.0 (static hold)
SOURCE IMAGE: IMG12
IMAGE ACTION: Generate (reuses IMG11's left panel content as part of its own prompt); ANIMATION REQUIRED: NO.
EXPECTED RESULT: F08.0.
AUDIO: continuous narration.
CUT TO: S09.

## S09 — 01:09.208–01:18.333
STATE CHAIN: F09.0 → A14 → F09.1
SOURCE IMAGE: IMG12 (reused as zoom-out source), IMG13 (end)
IMAGE ACTION: Reuse IMG12; generate IMG13.
I2V PASS: A14 (zoom-out transform from IMG12 to IMG13).
EXPECTED RESULT: F09.1.
TEXT/GRAPHICS OVERLAY: "MARIANA TRENCH" label, deep depth-scale.
AUDIO: continuous narration.
CUT TO: S10.

## S10 — 01:18.333–01:47.458
STATE CHAIN: F10.0 → A15 → F10.1 → A16 → F10.2 → A17 → F10.3 → A18 → F10.4 → A19 → F10.5
SOURCE IMAGE: IMG14 (F10.0, F10.1), IMG15 (F10.2–F10.4), IMG16 (F10.5)
IMAGE ACTION: Generate IMG14, IMG15, IMG16.
ADDITIONAL INDEPENDENT PASSES: A15 (background fade, isolated on IMG14) generated separately from A16–A19 (jar-diagram sequence, isolated on IMG15/IMG16) since the seaplane and the jar-diagram graphics are visually independent elements — composite the jar-diagram region over the seaplane pass only where evidenced (F10.2's inset).
EXPECTED RESULT: F10.5.
TEXT/GRAPHICS OVERLAY: "GASP!", "WHEEZE!" captions.
AUDIO: continuous narration.
CUT TO: S11.
FIDELITY RISK: the seaplane/jar-diagram interleave timing (F10.0–F10.3) is APPROXIMATE — no scdet cut was detected in this 29-second span, so the insert boundary was resolved from 2-second visual sampling only.

## S11 — 01:47.458–01:54.333
STATE CHAIN: F11.0 → A20 → F11.1
SOURCE IMAGE: IMG17 (reused for both states)
IMAGE ACTION: Generate once, reuse for the target state.
I2V PASS: A20 (departure motion on IMG17; no first/last-frame pair needed for this simple translation).
EXPECTED RESULT: F11.1.
AUDIO: continuous narration.
CUT TO: S12.

## S12 — 01:54.333–02:16.792
STATE CHAIN: F12.0 → A21 → F12.1 → A22 → F12.2 → A23 → F12.3 → A24 → F12.4 → A25 → F12.5
SOURCE IMAGE: IMG18 (start), IMG19 (end) — first/last-frame pair
IMAGE ACTION: Generate both.
I2V PASS: A21–A25 chained as one guided sequence from IMG18 to IMG19 (rain, then drought, then ignition, then spread, then CO2 buildup — a single physically coupled progression).
EXPECTED RESULT: F12.5.
TEXT/GRAPHICS OVERLAY: footnote note box (per IMG19 clean-plate note).
AUDIO: continuous narration.
CUT TO: S13.

## S13 — 02:16.792–02:23.583
STATE CHAIN: F13.0 → A26 → F13.1
SOURCE IMAGE: IMG20 (reused for both states)
IMAGE ACTION: Generate once, reuse for the target state.
I2V PASS: A26 (caption reveal only).
EXPECTED RESULT: F13.1.
TEXT/GRAPHICS OVERLAY: "WORSE? FOR WHO?" caption (not baked).
AUDIO: near-silence gap 140.99–141.23s falls near the caption reveal.
CUT TO: S14.

## S14 — 02:23.583–02:35.208
STATE CHAIN: F14.0 → A27 → F14.1
SOURCE IMAGE: IMG21 (reused for both states)
IMAGE ACTION: Generate once; the heat-gradient intensification is an animated overlay wash, not a new base image.
I2V PASS: A27.
EXPECTED RESULT: F14.1.
AUDIO: near-silence gap 154.86–155.12s falls at this shot's end.
CUT TO: S15.

## S15 — 02:35.208–02:46.750
STATE CHAIN: F15.0 → A28 → F15.1 → A29 → F15.2
SOURCE IMAGE: IMG22 (reused for all three states)
IMAGE ACTION: Generate once; ray intensify/fade is an animated overlay effect.
I2V PASS: A28, A29 chained as one guided sequence (ray intensify then fade).
EXPECTED RESULT: F15.2.
TEXT/GRAPHICS OVERLAY: "~1,000,000,000 YEARS FROM NOW", "BYE!".
AUDIO: continuous narration.
CUT TO: S16.

## S16 — 02:46.750–02:50.792
STATE CHAIN: F16.0 (static/idle hold)
SOURCE IMAGE: IMG23
IMAGE ACTION: Generate; ANIMATION REQUIRED: minimal idle swim-loop only, no material position change observed at 2-second sampling.
EXPECTED RESULT: F16.0.
AUDIO: continuous narration.
CUT TO: S17.

## S17 — 02:50.792–02:53.792
STATE CHAIN: F17.0 (single reveal)
SOURCE IMAGE: IMG23 (reused)
IMAGE ACTION: Reuse; composite C06 greeter figure as a separate transparent-PNG overlay entering from the right edge, per final assembly.
COMPOSITE: C06 + "Hi!" caption layered over IMG23's right edge.
EXPECTED RESULT: F17.0.
AUDIO: continuous narration.
CUT TO: S18.

## S18 — 02:53.792–03:03.792
STATE CHAIN: F18.0 (static hold to video end)
SOURCE IMAGE: IMG24
IMAGE ACTION: Generate/reuse a studio-provided end card; ANIMATION REQUIRED: NO (static hold, ~10s).
EXPECTED RESULT: F18.0 (video end).
AUDIO: extensive near-silence from ~172–184s.

## Final assembly and export
Assemble all 18 shots in sequence per the CUT TO chain above, apply the text/graphics overlays noted per shot (none baked except tombstone wording, volcano chemistry formulas, the title card, and the credits card), place AU01 on the master audio track for the full runtime, and export at 1920x1080, 24fps, matching the measured 183.792s source duration. No actual image, video, or audio generation has been performed as part of this analysis — this document specifies the generation and assembly plan only.
