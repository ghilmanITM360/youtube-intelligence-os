# WAY 2 — Image-to-video reconstruction



This route starts from generated source artwork in IMAGE_PROMPTS.md. Use the animation contracts in ANIMATION_PROMPTS.md only for measured changes. Most of this reference is held illustration: a generated video model must not invent motion during those holds. Exact text, one-frame replacements, masks and audio placement are final assembly within WAY 2, not a third workflow.



## Setup and media

Use 1080×1920, 9:16, 24 fps, 2,419 output frames. Generate the 18 unique images specified; crop/reuse local objects and retain previous composite states. Add the exact text/diagram overlays identified by G/T IDs in ASSET_MANIFEST.csv. All wording/timing remains canonical in TIMELINE.csv. No source audio exists.



## Assembly controls

- Generate each initial image with the source frame visible as composition authority if the chosen service supports image guidance. No particular generator is implied or claimed.

- For held portions, ANIMATION REQUIRED: NO. Extend the still or completed state to the next event frame. Do not submit a video generation merely to fill the hold.

- For instantaneous changes, place the prepared patch at full opacity on the measured frame. Do not ask a video model to interpolate a falling probe, growing books, raised reading book or facepalm.

- For exact letters and diagrams, animate only their masks in final assembly. Keep generated background and character pixels frozen. Where S07 red/black reveals overlap, use independent layers, not a fresh image per line.

- The S11 dark/light pair is the only continuous non-text/annotation appearance change. An isolated I2V light pass is possible, but a fixed-artwork opacity/mask treatment gives more reliable timing. In either case use the previous complete state as input, retain cloud increments, and stop at the exact endpoint.

- If a service only returns a longer clip, sample/trim its controlled change to the measured interval without creating slow movement over the source holds. If this cannot preserve the endpoints, use the documented final-assembly opacity operation.

- Composite only necessary regions. Preserve a clean base under replacement poses so old limbs do not remain. Never regenerate a whole frame to add a small label.



Exact global timing is in TIMELINE.csv; A-ID intervals are in MOTION_EVENTS.csv. Millisecond rounding must not change the integer frame counts.



## S01 — 00:00.000–00:04.500

STATE CHAIN: F01.0 → A01 → F01.1; F01.1 → A02 → F01.2.

SOURCE IMAGE: IMG01.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A01, A02 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F01.2 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G01, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S02



## S02 — 00:04.500–00:07.625

STATE CHAIN: F02.0 → A03 → F02.1; F02.1 → A04 → F02.2.

SOURCE IMAGE: IMG02; IMG03 contact endpoint and reusable probe crop.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A03, A04 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F02.2 held until shot OUT.

TEXT / GRAPHICS OVERLAY: T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S03

COMPOSITE: Crop the striped probe from IMG03, place above IMG02 for the hover state; switch to registered pressed diagram at contact. No motion interpolation.

FIDELITY RISK: Generating transitions between held drawings can introduce geometry/identity drift. Keep replacements instantaneous and limit each patch to its documented region.



## S03 — 00:07.625–00:10.375

STATE CHAIN: F03.0 (hold).

SOURCE IMAGE: IMG04.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No pass: entirely static.

EXPECTED RESULT: F03.0 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G02. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S04



## S04 — 00:10.375–00:19.292

STATE CHAIN: F04.0 → A05 → F04.1; F04.1 → A06 → F04.2.

SOURCE IMAGE: IMG05.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A05, A06 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F04.2 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G03, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S05

FIDELITY RISK: Exact hand lettering, tiny scientific/calendar text and dense page texture are unreliable if regenerated. Use source-derived overlays; do not hallucinate unreadable content.



## S05 — 00:19.292–00:30.042

STATE CHAIN: F05.0 → A07 → F05.1; F05.1 → A08 → F05.2; F05.2 → A09 → F05.3.

SOURCE IMAGE: IMG06.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A07, A08, A09 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F05.3 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G04, G05, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S06

COMPOSITE: Mask out later elements initially, then expose droplet and squirrel regions. Add reference lines/local squirrel correction at the last event, preserving all other pixels.



## S06 — 00:30.042–00:35.833

STATE CHAIN: F06.0 → A10 → F06.2; F06.2 → A11 → F06.4.

SOURCE IMAGE: IMG07.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A10, A11 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F06.4 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G06, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S07

FIDELITY RISK: Exact hand lettering, tiny scientific/calendar text and dense page texture are unreliable if regenerated. Use source-derived overlays; do not hallucinate unreadable content.



## S07 — 00:35.833–00:43.542

STATE CHAIN: F07.0 → A12 → F07.1; F07.1 → A13 → F07.3; F07.3 → A14 → F07.5; F07.5 → A15 → F07.7; F07.7 → A16 → F07.9; F07.9 → A17 → F07.11; F07.11 → A18 → F07.13; F07.13 → A19 → F07.15; F07.15 → A20 → F07.17; F07.17 → A21 → F07.19; F07.19 → A22 → F07.21; F07.21 → A23 → F07.23; F07.23 → A24 → F07.25; F07.25 → A25 → F07.27; F07.27 → A26 → F07.29; F07.28 → A27 → F07.30; F07.30 → A28 → F07.32; F07.31 → A29 → F07.33; F07.32 → A30 → F07.34; F07.34 → A31 → F07.36; F07.35 → A32 → F07.37; F07.37 → A33 → F07.39; F07.39 → A34 → F07.41; F07.40 → A35 → F07.42.

SOURCE IMAGE: REUSE IMG06 blank field / E01; no new source image.

IMAGE ACTION: Reuse existing off-white canvas; construct exact text layers.

I2V PASS: No generative movement required. Execute A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23, A24, A25, A26, A27, A28, A29, A30, A31, A32, A33, A34, A35 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F07.42 held until shot OUT.

TEXT / GRAPHICS OVERLAY: T01, G07. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S08

ADDITIONAL INDEPENDENT PASSES: Black text strips and red stroke strips have independently timed masks; they overlap on several frames. Use measured line extents in evidence, not a single full-frame typewriter preset.

FIDELITY RISK: Exact hand lettering, tiny scientific/calendar text and dense page texture are unreliable if regenerated. Use source-derived overlays; do not hallucinate unreadable content.



## S08 — 00:43.542–00:56.917

STATE CHAIN: F08.0 → A36 → F08.1; F08.1 → A37 → F08.2; F08.2 → A38 → F08.3; F08.3 → A39 → F08.4; F08.4 → A40 → F08.5; F08.5 → A41 → F08.6; F08.6 → A42 → F08.7.

SOURCE IMAGE: IMG08 + IMG09 reusable book.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A36, A37, A38, A39, A40, A41, A42 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F08.7 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G08, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S09

COMPOSITE: Isolate IMG09. Build registered 1/2/3/10-book variants with the bottom edge on the tabletop; use the measured replacements. Keep labels as independent overlays.



## S09 — 00:56.917–01:06.792

STATE CHAIN: F09.0 → A43 → F09.1; F09.1 → A44 → F09.2; F09.2 → A45 → F09.3.

SOURCE IMAGE: IMG10 + IMG11 reading endpoint/connection crop.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A43, A44, A45 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F09.3 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G09, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S10

COMPOSITE: Reuse only the cable/outlet region of IMG11 first, preserving IMG10’s typing pose. Later switch the person/book region to IMG11 reading pose. Do not reset or remove the existing labels/cable.

FIDELITY RISK: Generating transitions between held drawings can introduce geometry/identity drift. Keep replacements instantaneous and limit each patch to its documented region.



## S10 — 01:06.792–01:10.583

STATE CHAIN: F10.0 → A46 → F10.1.

SOURCE IMAGE: IMG12 + IMG13 lower callout.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A46 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F10.1 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G10, G11, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S11

COMPOSITE: Keep IMG12 stationary, then add IMG13 lower drawing and exact speech group; do not shift the calendar.

FIDELITY RISK: Exact hand lettering, tiny scientific/calendar text and dense page texture are unreliable if regenerated. Use source-derived overlays; do not hallucinate unreadable content.



## S11 — 01:10.583–01:31.125

STATE CHAIN: F11.0 → A47 → F11.2; F11.2 → A48 → F11.4; F11.4 → A49 → F11.5; F11.5 → A50 → F11.6; F11.6 → A51 → F11.8; F11.8 → A52 → F11.9; F11.9 → A53 → F11.10; F11.10 → A54 → F11.12; F11.12 → A55 → F11.13.

SOURCE IMAGE: IMG14 + IMG15 final pose patch.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: Optional isolated lighting passes A51, A54; all other A-IDs are exact final-assembly replacements/reveals.

EXPECTED RESULT: F11.13 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G01, G12, G13, G14, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S12

COMPOSITE: Keep words, furniture and character as registered separate layers. Light treatment covers the whole scene with a feathered bright monitor/face region. Preserve the two extra cloud increments during the dark hold. At pose change use IMG15 only inside the person region.

FIDELITY RISK: Generating transitions between held drawings can introduce geometry/identity drift. Keep replacements instantaneous and limit each patch to its documented region.



## S12 — 01:31.125–01:35.667

STATE CHAIN: F12.0 → A56 → F12.1; F12.1 → A57 → F12.2; F12.2 → A58 → F12.3.

SOURCE IMAGE: IMG16 + IMG18 tilted book.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A56, A57, A58 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F12.3 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G01, G15, G14. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: S13

COMPOSITE: Add source-traced cable/plug and white head rim/light pool together. Keep desk/books/laptop fixed. Add IMG18 at source icon location, then radiating marks/cloud/time overlay.

FIDELITY RISK: Generating transitions between held drawings can introduce geometry/identity drift. Keep replacements instantaneous and limit each patch to its documented region.



## S13 — 01:35.667–01:40.792

STATE CHAIN: F13.0 → A59 → F13.2.

SOURCE IMAGE: IMG17.

IMAGE ACTION: Generate the listed unique master(s) once; reuse for all later states in this shot.

I2V PASS: No generative movement required. Execute A59 as the measured overlay/mask events in final assembly.

EXPECTED RESULT: F13.2 held until shot OUT.

TEXT / GRAPHICS OVERLAY: G16, T01. Exact content and placement: corresponding canonical state rows; source-letter crops/traces for fidelity.

AUDIO: Entire-source availability rule in AUDIO_MAP.md; leave audio empty.

CUT TO: END; hold last state through frame 2418, no fade.



## Final assembly/export

Place completed states and clips on the canonical frame grid, apply only A-ID events, and export H.264 MP4 at 1080×1920/24 fps with 2,419 frames. No audio, music, movement, particles, page turns or leaf/runner cycles are supported by the source. Compare image registration, every event endpoint and text masks with the evidence. No generation or final video export has been performed as part of this analysis package.
