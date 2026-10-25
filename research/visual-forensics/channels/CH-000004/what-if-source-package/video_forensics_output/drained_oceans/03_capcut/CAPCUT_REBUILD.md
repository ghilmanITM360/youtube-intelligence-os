# CapCut rebuild

## Project setup

- Canvas: 9:16 portrait; 1080 x 1920; 24 fps; 01:49.227.
- Background: white for board scenes; black behind C03/map lower field.
- Master audio: AU01 on A1, unchanged. Align first sample to 00:00.000.
- Text: T01 closest hand-drawn uppercase. Do not claim original font. White text over black, black over white, red only for G01/G02/G03/G08.
- Effects: none globally. No camera keyframes, glow, parallax, drift or added motion.

## Media to import

Import all recreation media listed in `../02_analysis/ASSET_MANIFEST.csv`; AU01 is required. Build SVG/PNG plates at 1080x1920 or their native upper-panel dimensions. Use text/shapes for T01 and G01–G09 where exact wording matters.

## Shot build

### S01 — 00:00.000–00:09.083

States: F01.0, F01.1, F01.2, F01.3. Media: E01, E02, C01, C02, O01, G01, T01. Stack: V4 text; V3 C/O; V2 display artwork; V1 white. Place E01/E02 upper 51%; C01 centered around x=0.28, y=0.74. Build display, then C01 and paper.

- 00:01.500: add PORTAL + arrow (A01). 00:04.500: add CHALLENGER DEEP (A02). No tween.
- 00:07.625: hard-cut C01 to C02; move O01 to lower-left, APPROXIMATE x=0.08 y=0.82 (A03).
- Tools: overlay, text, shape, cut. Audio: AU01. End: F01.3.

### S02 — 00:09.083–00:16.917

States: F02.0, F02.1, F02.2. Media: E01, E03, E04, C02, O01, G02, T01. Stack: V4 text/line; V3 water; V2 display; V1 white. Keep C02/O01 from S01.

- 00:09.083: hard cut E02 to E03. 00:11.917: add G02 and C04 (A05).
- 00:13.625: put E04 above E03, crop/mask from 0 to full display height by 00:14.250 (A06); then hold.
- Tools: cut, overlay, crop or rectangle mask, text, shape. End: F02.2.

### S03 — 00:16.917–00:22.583

States: F03.0, F03.1. Media: E05, G01, C04, T01. Stack: V3 text/locator; V2 globe; V1 white. Globe centered upper half, diameter APPROXIMATE 62% canvas width.

- 00:16.917: hard cut from S02. Add MARlANA TRENCH PORTAL and red locator. 00:20.542: add C04 and ellipsis (A08).
- Tools: cut, overlay, text, shape. No keyframes. End: F03.1.

### S04 — 00:22.583–00:24.792

State: F04.0. Media: G03, T01. Stack: V2 diagram; V1 light grey. Center diagram mid-canvas, scale APPROXIMATE 86% width.

- 00:22.583: hard cut in. Hold. Tools: cut, overlay. End: F04.0.

### S05 — 00:24.792–00:27.125

State: F05.0. Media: E06, G04. Stack: V2 descending black form; V1 tunnel/streak animation. Fill canvas.

- Use prebuilt 2.333 s E06/G04 clip; no CapCut camera transform. If recreating: animate only streak-layer scale/position toward bottom center and black form downward, APPROXIMATE 00:24.792 top-center to 00:27.125 lower-center.
- Tools: overlay, position keyframes. End: F05.0.

### S06 — 00:27.125–00:41.042

States: F06.0, F06.1. Media: E07, G05, G06, T01. Stack: V3 checklist/text; V2 profile; V1 white/black plate. Cross-section spans lower 60%; no presenter.

- 00:27.125: hard cut in E07/G05. 00:36.000: add G06 at lower-left (A12). Hold all other layers.
- Tools: cut, overlay, text, shape. End: F06.1.

### S07 — 00:41.042–00:49.625

States: F07.0, F07.1, F07.2. Media: E08, C03, G07, G08, T01. Stack: V4 counter/callouts; V3 map; V2 C03; V1 black. E08 occupies upper 38%; C03 lower-left.

- 00:41.042: hard cut in 0m map. 00:42.708: replace text 0m with -50m and C03 pose (A14). 00:45.500: add G08 whole red callout set (A15).
- Tools: cut, text, overlay. No tween. End: F07.2.

### S08 — 00:49.625–00:54.792

State: F08.0. Media: E09, C04, T01. Stack: V3 warning text/C04; V2 E09; V1 white. Full-canvas silhouette; text above central mound.

- 00:49.625: hard cut; add YOU CANNOT PASS! and tiny person. Hold.
- Tools: cut, text, overlay. End: F08.0.

### S09 — 00:54.792–00:64.500

States: F09.0, F09.1. Media: E08, C03, G07, G08, T01. Same stack/layout S07.

- 00:54.792: hard cut to baseline map. Replace counter with -50m, then -100m at 00:60.083 (A17); use discrete text replacements.
- 00:60.083: add only F09.1 G08 callout set (A18). Tools: cut, text, overlay. End: F09.1.

### S10 — 00:64.500–00:68.125

State: F10.0. Media: E09, C04. Use S08 plate but omit warning text. 00:64.500 hard cut; hold. Tools: cut, overlay. End: F10.0.

### S11 — 00:68.125–00:74.292

States: F11.0, F11.1. Media: E08, C03, G07, G08, T01. Same S07 stack.

- 00:68.125: hard cut; counter -200m. 00:72.208: add F11.1 G08 annotations, including THE NETHERLANDS. Tools: cut, text, overlay. End: F11.1.

### S12 — 00:74.292–00:79.417

State: F12.0. Media: E08, C03, G07, G08, T01. 00:74.292: hard replace counter/callouts with -500m state (A22). Keep map and presenter unmoved. Tools: cut, text, overlay. End: F12.0.

### S13 — 00:79.417–00:83.083

State: F13.0. Media: E08, C03, G07, G08, T01. 00:79.417: hard replace counter/callouts with -1000m/New Zealand state (A23). Tools: cut, text, overlay. End: F13.0.

### S14 — 00:83.083–00:95.375

States: F14.0, F14.1, F14.2. Media: E10, C03, G07, G08, G09, T01. Stack: V4 titles/callouts; V3 map; V2 C03; V1 black.

- 00:83.083: hard cut E08 to E10 with -5000m counter. 00:86.917: add DRAINED title (A25). 00:90.500: add final G08 set (A26).
- Tools: cut, text, overlay. End: F14.2.

### S15 — 00:95.375–00:100.708

State: F15.0. Media: E11. 00:95.375 hard cut to full-canvas valley/pool. Hold. Tools: cut, overlay. End: F15.0.

### S16 — 00:100.708–00:105.500

State: F16.0. Media: G10, C05, T01. Place standalone news card centered. 00:100.708 hard cut; hold. Keep exact readable text as editor text or precomposed graphic. Tools: cut, overlay, text. End: F16.0.

### S17 — 00:105.500–00:109.227

State: F17.0. Media: E01, E12, C04, T01. Place framed board in upper half, tiny figure on slope, HUH, WATER above. 00:105.500 hard cut; hold to end. Tools: cut, overlay, text. End: F17.0.

## Fidelity limits

- Original font, source illustrations, edit software and audio stems are UNKNOWN.
- S05 is closest with a prebuilt animated streak overlay; CapCut keyframes cannot establish original easing from evidence.
