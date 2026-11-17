# CapCut rebuild

## Project setup

- Canvas: 16:9 landscape, 1920 x 1080, 24 fps; total 02:42.261.
- Background: white for line-art shots; use E03/E12 red full-frame plates where called.
- Master audio: AU01 extracted from source MP4; lock before visual editing.
- Text: T01 closest hand-drawn uppercase/handwriting match. Use native text for exact readable words; never bake generator text.
- Color: black line art on near-white; red only for heat, diagrams, title/end-card fields.
- Global effects: none. Use local red glow only in F04.5, F07.2, F08.7, F09.2, F10.4–F10.7; grey opacity wash only F02.5 and F10.1 onward.

## Media to import

`C01–C04, E01–E12, O01–O05, G01–G03, T01, AU01` from `ASSET_MANIFEST.csv`. Build each E plate clean; use transparent overlays for objects/graphics that change. For each listed state replacement, an exported state plate is valid and closer than invented interpolation.

## Shot build

### S01 — 00:00.000–00:10.750

Source states: F01.0, F01.1, F01.2, F01.3. Media: E01, C01, C02, O01, O03, G01. Tracks: V4 text, V3 board drawing, V2 characters/objects, V1 E01; A1 AU01.

Initial composition: C01 left margin; whiteboard centered-right. Build: hold F01.0; fade/type-on question banner at 00:01.000; reveal board drawing in two cropped groups at 00:05.750 and 00:07.000. Keyframes: only opacity/mask progress for G01 and board-drawing layers. Transition: whole-frame state replacement into S02 at 00:10.750. Audio sync: AU01 question lead-in. End: F01.3.

### S02 — 00:10.750–00:25.250

Source states: F02.0–F02.5. Media: E02, C02, O01, O02, O03, O04, G01, G03. Tracks: V4 caption/electrical arcs, V3 frost/heat/bread, V2 observer/toaster, V1 E02; A1 AU01.

Initial composition: use flattened F02.0 plate. Build: opacity-reveal heat strokes at 00:12.250; replace with frost plate at 00:14.750; pop O02 upward at 00:17.750 then use F02.4 state plate; add 35–45% grey overlay plus arc PNGs/caption at 00:23.000. Keyframes: G03 opacity only; O02 Y position APPROXIMATE 6–10% frame height. Transition: hard cut at 00:25.250. End: F02.5.

### S03 — 00:25.250–00:29.250

Source state: F03.0. Media: E03. Tracks: V1 E03; A1 AU01. Build: static full-frame plate. No keyframes. Hard cut in/out. End: F03.0.

### S04 — 00:29.250–00:42.000

Source states: F04.0–F04.5. Media: E04, O01, O03, G02, G03. Tracks: V4 labels/600°C, V3 heat/coil/glow, V2 toaster, V1 E04; A1 AU01.

Initial composition: E04 with O03 left. Build: reveal O01 at 00:30.250; native heading text at 00:32.750; heat strokes at 00:34.500; coil-face state at 00:37.500; red glow and 600°C at 00:40.500. Keyframes: opacity/mask only. Transition: hard cut at 00:42.000. End: F04.5.

### S05 — 00:42.000–00:58.000

Source states: F05.0–F05.3. Media: E05, G02. Tracks: V3 labels/bracket, V1 E05; A1 AU01.

Build: static axis plate; add room marker 00:44.750, fridge/freezer markers 00:46.500, then curved COLD (FOR TOASTER) bracket at 00:48.250. Keyframes: draw-mask or opacity on each vector group only. Transition: hard cut 00:58.000. End: F05.3.

### S06 — 00:58.000–01:03.250

Source states: F06.0, F06.1. Media: E06, C01, O01, G01, G03. Tracks: V3 bubble, V2 smoke/fire, V1 E06/C01/O01; A1 AU01.

Build: hold burning-toaster plate; reveal bubble caption at 01:00.250. No motion on figure or smoke beyond observed static scribble state. Hard cut 01:03.250. End: F06.1.

### S07 — 01:03.250–01:15.000

Source states: F07.0–F07.3. Media: E07, C03, O01, O03, O04, G02, G03. Tracks: V4 ~1000W text, V3 glow/icy trails, V2 door state, V1 E07; A1 AU01.

Build: start open-door plate; replace upper door with closed state at 01:08.500; add rim glow/icicle overlay 01:10.250; reveal ~1000W at 01:12.000. Keyframes: door can use a 0.2 s mask wipe if desired, otherwise state replacement; G03/G02 opacity only. Hard cut 01:15.000. End: F07.3.

### S08 — 01:15.000–01:45.000

Source states: F08.0–F08.7. Media: E08, O01, O03, O04, G02, G03. Tracks: V5 equations/power text, V4 arrows/heat rays, V3 toaster/glow, V1 E08; A1 AU01.

Build: hold clean fridge cutaway. Draw/reveal compressor, EOUT, COP≈3, EIN in order from 01:17.000–01:25.500; place toaster and upward arrow 01:25.500; add COP≈1 at 01:28.000; add ambient arrows/heat rays 01:32.000; add ~1000W text and red toaster state 01:37.000. Keyframes: draw-mask or opacity only; no camera motion. Hard cut 01:45.000. End: F08.7.

### S09 — 01:45.000–01:58.000

Source states: F09.0–F09.3. Media: E09, C03, O01, G01, G02, G03. Tracks: V4 labels/caption, V3 glow, V2 toaster, V1 E09; A1 AU01.

Build: clean vignette plus exact caption; toaster appears 01:49.500, red glow/600°C at 01:51.500, -18°C at 01:54.000. Keyframes: opacity only. Hard cut 01:58.000. End: F09.3.

### S10 — 01:58.000–02:26.000

Source states: F10.0–F10.7. Media: E10, C04, O01, O02, O05, G01, G03. Tracks: V5 captions, V4 dark wash/reaction mark, V3 toaster/bread/stool, V2 C04, V1 E10; A1 AU01.

Build: bright Winnipeg plate to 02:01.250; fade a full-frame grey overlay to target darkness by 02:03.000 while changing location text to include (-20°C); hold. Reveal O05/O01 at 02:07.000; glow and arm-pose state at 02:09.000; pop O02 at 02:11.000; replace C04 with reaction and hunched pose states, then add ALWOOO... at 02:15.500. Keyframes: dark overlay opacity 0–about 60% APPROXIMATE; O02 Y position only. Hard cut 02:26.000. End: F10.7.

### S11 — 02:26.000–02:33.000

Source states: F11.0–F11.2. Media: E11, C03, G01. Tracks: V3 conclusion text, V1 E11/C03; A1 AU01.

Build: static conclusion plate; reveal TOASTERS BEAT FREEZERS. at 02:28.000; reveal BUT WOLVES BEAT TOASTERS. at 02:31.000. Keyframes: text opacity only. Hard cut 02:33.000. End: F11.2.

### S12 — 02:33.000–02:42.261

Source state: F12.0. Media: E12. Tracks: V1 E12; A1 AU01. Build: static red end card. No keyframes. End of source.

## Fidelity limits

- Frame times are sampled to 0.25 s; use AU01 waveform and frame matching to refine in/out to individual 24 fps frames.
- Source font, exact effects, and original assets are UNKNOWN. State plates are more faithful than adding non-evidenced motion.
