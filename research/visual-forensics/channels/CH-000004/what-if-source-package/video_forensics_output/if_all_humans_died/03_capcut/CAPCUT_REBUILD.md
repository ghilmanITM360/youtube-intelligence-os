# CapCut rebuild

## Project setup

- Canvas: 16:9 landscape, 1920×1080.
- Frame rate: 24 fps. Duration: 05:03.856.
- Background: off-white `#f5f4f0` unless TIMELINE.csv specifies charcoal, black, or red.
- Master audio: AU01, unmodified, beginning 00:00.000. Keep one A1 track. No claimed music/SFX recreation.
- Text: T01; closest installed hand-lettered font. Add exact readable labels as CapCut text, not raster text. Unknown/illegible copy stays unknown.
- Color: black/grey line art; red only disappearance/alerts/end card; cyan only Cs-137 radiation/glow.
- Global effects: none. No automatic camera movement, stabilization, grain, parallax, or transitions.

## Media to import

Use reconstruction assets in `../02_analysis/ASSET_MANIFEST.csv`: C01–C03, E01–E14, O01–O16, G01–G08, T01 and AU01. Build any legible diagram/card as editable shapes + text where manifest says so. For direct branded art/credits, use authorized source art or preserve reference only; do not claim ownership.

## Shot build blocks

All times are sequence time. "Approx." means visual placement estimated from 1920×1080 reference.

### S01 — 00:00.000–00:08.667

Source states: F01.0, F01.1, F01.2. Media: E01, C01, C02/C03, O01, G01. Tracks: V4 G01, V3 C01, V2 C02/C03, V1 E01, A1 AU01. Initial composition: presenter left; display right; quote top. Build: hold E01/O01/G01; overlay C01/C02. Keyframes: 02.000 replace black overlays with red; 04.000–08.667 use C03 opacity 100–0 and darken display/lamp overlay. Tools: overlay, opacity, blend/mask only for local speckles. Audio sync: opening narration. Transition: hard cut at 08.667. End: F01.2.

### S02 — 00:08.667–00:10.667

Source state: F02.0. Media: G02. Tracks: V1 G02, A1 AU01. Build: full-frame static red card. No keyframes. Transition: hard cuts both sides. End: F02.0.

### S03 — 00:10.667–00:15.750

Source states: F03.0, F03.1. Media: E02. Tracks: V2 window-light mask, V1 E02, A1 AU01. Initial: skyline full frame. Build: duplicate E02; mask white window areas on top copy. Keyframes: approx. 13.500–15.750 top-copy opacity 100–0 or replace lit-window plate with dark-window plate. No camera change. End: F03.1.

### S04 — 00:15.750–00:20.667

Source state: F04.0. Media: E02, E03. Tracks: V2 E03, V1 E02, A1 AU01. Initial: E02 full frame; E03 begins right of canvas. Keyframes: 15.750–20.667 E03 position X moves left to fill frame; retain city left edge until covered. Tools: position/crop. End: F04.0.

### S05 — 00:20.667–00:30.792

Source states: F05.0, F05.1, F05.2. Media: E04, O02, C03. Tracks: V2 C03, V1 E04, A1 AU01. Initial: red people along ground. Build: static E04; use figure overlays. Keyframes: approx. 22.500–28.000 replace figures with speckled C03 and opacity 100–0. No movement in plant/smoke/pylon. End: F05.2; hard cut.

### S06 — 00:30.792–00:38.583

Source states: F06.0, F06.1, F06.2. Media: E05, C02/C03, G03. Tracks: V4 G03, V3 C03, V2 C02, V1 E05, A1 AU01. Build: hold room; add warning triangles around 34.000; replace people with C03 and lower a full-frame charcoal overlay 36.500–38.583. Tools: overlay, opacity. End: F06.2.

### S07 — 00:38.583–00:40.917

Source state: F07.0. Media: E04, O02, O03, C03. Tracks: V3 O03, V2 C03, V1 E04, A1 AU01. Build: locked exterior; no keyframes. End: F07.0; hard cut.

### S08 — 00:40.917–00:49.625

Source states: F08.0, F08.1. Media: O04, E04, O02, O03, G03, T01. Tracks: V3 O04/text, V1 E04, A1 AU01. Build: hard-cut to editable energy card/strip at 40.917; hard-cut back to exterior with sparse alert icons about 46.500. No tween. End: F08.1.

### S09 — 00:49.625–00:56.792

Source states: F09.0, F09.1. Media: E04, O02, O03, G03, T01. Tracks: V3 callout/icons, V1 exterior, A1 AU01. Keyframes: none required; pop icons by cuts; add exact `MAYDAY!` callout about 53.000. End: F09.1.

### S10 — 00:56.792–01:12.875

Source states: F10.0, F10.1, F10.2. Media: E06, E07, O05, O06, O10, C02/C03. Tracks: V2 C02/C03, V1 scene plates, A1 AU01. Build: hard-cut collage at 56.792; hard-cut island about 66.000; replace island figure with C03 at ~72.000. Static lamps/environment. End: F10.2.

### S11 — 01:12.875–01:16.500

Source state: F11.0. Media: O05, O06, O09, T01. Tracks: V1 icon sheet, A1 AU01. Build: full-frame static vector layout. No keyframes. End: F11.0.

### S12 — 01:16.500–01:21.917

Source states: F12.0, F12.1. Media: E08, O02, O05, C02, G03, T01. Tracks: V3 text/light, V2 C02, V1 E08, A1 AU01. Build: hard-cut wide geothermal plate; hard-cut close worker/machine scene about 80.000. Add speech text and small warning lamp as static layers. End: F12.1.

### S13 — 01:21.917–01:27.750

Source state: F13.0. Media: E08, O05, C03, T01. Tracks: V3 `<3 YEARS`, V2 C03/decay texture, V1 machinery, A1 AU01. Build: darken machinery, replace worker with C03, add grime texture and text. Keyframes: slow opacity 0–100 for damage only. End: F13.0.

### S14 — 01:27.750–01:38.667

Source states: F14.0, F14.1. Media: E09, O06, G04. Tracks: V3 G04, V2 blade overlays, V1 E09, A1 AU01. Build: static farm; use separate blade PNGs centered on hubs. Keyframes: continuous rotation only on blades, approx. 01:27.750–01:38.667. Insert/remove G04 by cut. End: F14.1.

### S15 — 01:38.667–01:48.333

Source states: F15.0, F15.1. Media: O07, T01. Tracks: V2 labels/inset, V1 panel shapes, A1 AU01. Build: two panels first, then add right `>20 YEARS` panel and component inset around 01:43.667. Use hard reveal, not animated camera. End: F15.1.

### S16 — 01:48.333–01:58.083

Source states: F16.0, F16.1. Media: E10, O02, C02/C03, G03, T01. Tracks: V3 callouts, V2 C02/C03/damage, V1 E10, A1 AU01. Build: initial figure and `I DON'T ACTUALLY DO ANYTHING HERE`; around 01:54 replace with C03, add `OOPS!`, then fade in local damage texture. End: F16.1.

### S17 — 01:58.083–02:06.000

Source states: F17.0, F17.1. Media: O08, T01. Tracks: V1 cards/plate, A1 AU01. Build: hard-cut Eternal Light card; hard-cut battery tray about 02:02.000. Reduce red battery fills by simple opacity/mask. End: F17.1.

### S18 — 02:06.000–02:10.083

Source state: F18.0. Media: O09, T01. Tracks: V2 labels, V1 icon plate, A1 AU01. Build: static six-icon taxonomy. No keyframes. End: F18.0.

### S19 — 02:10.083–02:18.667

Source state: F19.0. Media: O10, O11, T01. Tracks: V2 divider/labels, V1 house/pole/component plates, A1 AU01. Build: hard-cut house, then side-by-side house/pole and close component diagram by hard cuts. No motion. End: F19.0.

### S20 — 02:18.667–02:38.083

Source states: F20.0, F20.1, F20.2. Media: E11, O11, G05, T01. Tracks: V4 rain/text, V3 sign/card, V2 dirt texture, V1 E11, A1 AU01. Build: hold road; fade in panel grime; replace sign art; add `~100 YEARS`; add G05 rain only at final state. Lamp light pool stays fixed. End: F20.2.

### S21 — 02:38.083–02:42.125

Source state: F21.0. Media: G06, O05, O06, O09, O11. Tracks: V2 panel light masks, V1 G06, A1 AU01. Build: static five-panel layout. Keyframes: sequential opacity down for five local light masks; never move objects. End: F21.0.

### S22 — 02:42.125–02:45.708

Source state: F22.0. Media: E12, O12, T01. Tracks: V1 barrel room, A1 AU01. Build: static plate. No keyframes. End: F22.0.

### S23 — 02:45.708–02:58.458

Source states: F23.0, F23.1. Media: E13, O13, C02. Tracks: V3 C02/table, V2 watch hands/face, V1 E13, A1 AU01. Build: hold concentric rings/body; animate only watch hands/face states; pop C02/table in near 02:52.000. End: F23.1.

### S24 — 02:58.458–03:11.208

Source state: F24.0. Media: E14, O14, T01. Tracks: V3 text/waves, V2 cyan glow, V1 E14, A1 AU01. Build: hold wave diagram; fade cyan glow/wavy line overlay in. Add exact `CHERENKOV RADIATION` as text. Hard-cut vial next. End: F24.0.

### S25 — 03:11.208–03:18.458

Source state: F25.0. Media: E14, O15. Tracks: V2 cyan glow, V1 vial/screen, A1 AU01. Build: static vial plus cyan outer glow. No movement. End: F25.0.

### S26 — 03:18.458–03:26.125

Source state: F26.0. Media: O16, T01. Tracks: V2 text/label, V1 white field, A1 AU01. Build: cut `CESIUM 137` text, then cut to outlined label bar. No tween. End: F26.0.

### S27 — 03:26.125–03:45.167

Source state: F27.0. Media: O16, G07, T01. Tracks: V3 G07, V2 O16/glow, V1 dark field, A1 AU01. Build: dark field + cyan label; pop graph card above. No keyframes after arrival. End: F27.0.

### S28 — 03:45.167–03:53.792

Source state: F28.0. Media: O16. Tracks: V2 label halves, V1 black field/cyan glow, A1 AU01. Build: replace single label with separated mirrored stacks. No simulated physical break required; use state replacement. End: F28.0.

### S29 — 03:53.792–05:03.856

Source state: F29.0. Media: G08, AU01. Tracks: V1 G08, A1 AU01. Build: static authorized end card. No keyframes. Preserve factual credits/URLs only from authorized source. End: final frame.

## Fidelity limits

Exact hand-drawn font, original particles, original branded art, and source credits are UNKNOWN. Closest CapCut result uses recreated line-art plates, local opacity/mask substitutions, editable text, and hard cuts; it should not add inferred animation.
