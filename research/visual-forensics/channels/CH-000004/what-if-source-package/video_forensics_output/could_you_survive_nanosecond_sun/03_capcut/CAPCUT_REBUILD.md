# CapCut rebuild

## Project setup

- Canvas: 16:9 landscape; 1920×1080; 24 fps; duration 03:28.562.
- Background: white unless a state references E03, E04, or E07.
- Master audio: AU01 extracted from source; place at A1, lock, then use timeline timecodes.
- Text: T01 closest hand-lettered all-caps font; T02 red handwritten-style editable overlay. Exact font unknown.
- Global color: black line art on off-white; red only for T02, warning marks, and end/bumper E07. No global motion effects.

## Media to import

Import assets from `../02_analysis/ASSET_MANIFEST.csv`. Build E01 board contents and E05/O08 chart as separate overlays; this keeps observed incremental reveals editable.

## Shot builds

### S01 — 00:00.000–00:15.208

States: F01.0–F01.4. Media: C01, O01, E01, E02, C02, O02, O15, G01. Stack: V4 G01/text; V3 board contents; V2 C01/O01; V1 E01. Start blank F01.0. At 00:01.500 reveal board interior; 00:03.500 add cave/C02/O02/O15; 00:07.000 add cave detail; hold from 00:11.000. Tools: overlay, crop/mask, opacity or split clips. No camera keyframes. Cut at 00:15.208. Audio: AU01.

### S02 — 00:15.208–00:17.208

State: F02.0. Media: E07, G02, T01. Stack: V2 logo/text; V1 red plate. Hard cut in/out; static hold. Audio: AU01 identity segment.

### S03 — 00:17.208–00:29.417

States: F03.0–F03.3. Media: E02, O05, C02, C03, E03, T01/T02. Stack: V4 labels; V3 O05/C03; V2 side C02; V1 E02. Start three-panel layout. At 00:20.000 update center gradient/labels; 00:24.500 add approximately 5800 K; 00:28.000 add TOO MANY NANOSECONDS. Use editable text and replaced center-panel stills, not animated gradients. Hard cut at 00:29.417. Audio: AU01.

### S04 — 00:29.417–00:37.250

States: F04.0–F04.2. Media: E06, O03, C02, C04, O04, O15, T01. Stack: V3 text; V2 C02/C04/O03/O04/O15; V1 E06. Start without C02. 00:31.000 reveal C02. 00:33.500 add callout “30cm / NANOSECOND” with curved line. No keyframes. Cut at 00:37.250. Audio: AU01.

### S05 — 00:37.250–00:42.250

State: F05.0. Media: E03, C03, T01/T02. Stack: V3 text/red BAD line; V2 C03; V1 E03. Compose fixed bright curve at right. Hold. Hard cut at 00:42.250. Fidelity limit: source small technical lettering is only partially legible; recreate only verified readable text.

### S06 — 00:42.250–00:51.625

States: F06.0–F06.2. Media: E04, E03, O06, O07, T01/T02. Stack: V3 labels; V2 O06/O07; V1 E04 or E03 panel. Use split clips/hard cuts at 00:44.208 and within 00:44.208–00:49.292 for observed alternation. At 00:49.292 add equals relation. No motion keyframes. Cut 00:51.625. Audio: AU01.

### S07 — 00:51.625–01:28.958

States: F07.0–F07.5. Media: C01, O01, E05, E03, O08, T01/T02. Stack: V4 labels/FLASH; V3 chart panels/curves; V2 C01/O01 only F07.0; V1 white E05. 00:54.500 reveal axis/sun tile/red arrow; 00:58.000 first branch; 01:03.000 third panel/lower branch; 01:10.000 brain panel; 01:18.000 FLASH badge; fade/remove badge around 01:26.000–01:28.958. Use SVG/PNG state overlays. No camera movement.

### S08 — 01:28.958–01:53.375

States: F08.0–F08.7. Media: E03, C03, C01, O01, T01/T02. Prepare one black exposure composite and one white calculation composite. Hard-cut sequence: black 01:28.958; white 01:36.000; black 01:38.000; white 01:40.000; black 01:42.000; white 01:44.000; black 01:46.000; white 01:49.000. Modify only visible small numeric labels per source. Audio: AU01. No fades.

### S09 — 01:53.375–02:06.083

States: F09.0–F09.1. Media: E03, C03, O09, T01/T02. Hold black panel 01:53.375–01:55.000, then hard-cut full-frame phone ad. Phone centered; heading top; annotations around perimeter. Hold. Audio: AU01.

### S10 — 02:06.083–02:08.083

State: F10.0. Media: E02, O05, C02, C03, E03, T01. Hard cut to cave/doorway question composite; hold 2.000 s; hard cut to S11. Audio: AU01.

### S11 — 02:08.083–02:43.583

States: F11.0–F11.4. Media: E01, C01, O01, C05, O10–O13, T01/T02. Stack: V4 text/sign; V3 O10–O13; V2 characters; V1 E01. 02:08.083 formula board; 02:16.000 explanatory line + C05; 02:22.000 replace formula detail with O11 X-rays; 02:30.000 add O12; 02:38.000 add second O12 + O13. Use discrete overlays; no motion keyframes. Audio: AU01.

### S12 — 02:43.583–03:06.708

States: F12.0–F12.3. Media: E06, O14, O15, C06, T01. Stack: V3 centered text; V2 C06/scale/sun; V1 E06. Start floating C06. At 02:49.000 replace with fall/impact pose and ray marks. Add “TEMPERATURE ≠ HEAT” at 02:55.000; add “HEAT = TEMPERATURE · TIME” at 03:01.000. Static after each change. Audio: AU01.

### S13 — 03:06.708–03:18.500

States: F13.0–F13.1. Media: E02, O05, C02, C03, E03, T01. Hard-cut cave portal. 03:12.000 reveal right speech bubble “EXCEPT A BLACKHOLE.” Hold. Audio: AU01.

### S14 — 03:18.500–03:28.562

State: F14.0. Media: E07, G02, T01. Hard cut to red book/promo card; black graphic left, book/credits grid right. Static hold to end. Audio: AU01.

All A-IDs map to smallest action in `../02_analysis/MOTION_EVENTS.csv`: state replacements use hard cuts or overlay swaps; A23 alone uses opacity fade. No unobserved animation.
