# Image-to-video rebuild

Generate only IMG01–IMG13 from `IMAGE_PROMPTS.md`. Build exact text, counters, red callouts and hard cuts in final assembly. This is still Way 2: generated image sources plus required I2V clips and assembly.

### S01 — 00:00.000–00:09.083

State chain: F01.0, A01, F01.1, A02, F01.2, A03, F01.3. Source: IMG01. Action: generate once. I2V: none. Composite: add PORTAL, CHALLENGER DEEP, then hard-replace presenter pose/paper. Audio: AU01. Cut: S02.

### S02 — 00:09.083–00:16.917

State chain: F02.0, A05, F02.1, A06, F02.2. Sources: IMG02 then IMG03/end frame. Action: generate IMG02; reuse its result for A06. I2V: A06. Composite: add Mars label, red line/tiny figure; use A06 only within display mask. Audio: AU01. Cut: S03. Risk: water-line geometry can drift; mask to display.

### S03 — 00:16.917–00:22.583

State chain: F03.0, A08, F03.1. Source: IMG04. Action: generate once. I2V: none. Composite: locator, text, thinker/ellipsis overlays. Audio: AU01. Cut: S04.

### S04 — 00:22.583–00:24.792

State chain: F04.0. Source: IMG05. Action: generate. I2V: none; hold. Text overlay: 20m only. Audio: AU01. Cut: S05.

### S05 — 00:24.792–00:27.125

State chain: F04.0, A10, F05.0. Source: IMG06. Action: generate. I2V: A10. Composite: none unless lower edge stabilisation mask needed. Audio: AU01. Cut: S06. Risk: streak direction and black-form shape drift.

### S06 — 00:27.125–00:41.042

State chain: F06.0, A12, F06.1. Source: IMG07. Action: generate once. I2V: none; hold. Composite: exact depth labels and then checklist. Audio: AU01. Cut: S07.

### S07 — 00:41.042–00:49.625

State chain: F07.0, A14, F07.1, A15, F07.2. Source: IMG08. Action: generate once. I2V: none. Composite: 0m, -50m, C03 pose and red regional set as timestamped discrete layers. Audio: AU01. Cut: S08.

### S08 — 00:49.625–00:54.792

State chain: F08.0. Source: IMG09. Action: generate once. I2V: none; hold. Composite: YOU CANNOT PASS! only. Audio: AU01. Cut: S09.

### S09 — 00:54.792–00:64.500

State chain: F09.0, A18, F09.1. Source: reuse IMG08. I2V: none. Composite: use -50m then -100m counter and F09.1 callout set. Audio: AU01. Cut: S10.

### S10 — 00:64.500–00:68.125

State chain: F10.0. Source: reuse IMG09. I2V: none; hold without warning text. Audio: AU01. Cut: S11.

### S11 — 00:68.125–00:74.292

State chain: F11.0, A21, F11.1. Source: reuse IMG08. I2V: none. Composite: -200m counter then F11.1 callout set. Audio: AU01. Cut: S12.

### S12 — 00:74.292–00:79.417

State chain: F12.0. Source: reuse IMG08. I2V: none; hold. Composite: replace only counter/callout layers with -500m set. Audio: AU01. Cut: S13.

### S13 — 00:79.417–00:83.083

State chain: F13.0. Source: reuse IMG08. I2V: none; hold. Composite: replace only counter/callout layers with -1000m/New Zealand set. Audio: AU01. Cut: S14.

### S14 — 00:83.083–00:95.375

State chain: F14.0, A25, F14.1, A26, F14.2. Source: IMG10. Action: generate once. I2V: none. Composite: -5000m, then DRAINED, then red regional set. Audio: AU01. Cut: S15.

### S15 — 00:95.375–00:100.708

State chain: F15.0. Source: IMG11. Action: generate. I2V: none; hold. Audio: AU01. Cut: S16.

### S16 — 00:100.708–00:105.500

State chain: F16.0. Source: IMG12. Action: generate. I2V: none; hold. Composite: all headline/lower-third text. Audio: AU01. Cut: S17.

### S17 — 00:105.500–00:109.227

State chain: F17.0. Source: IMG13. Action: generate. I2V: none; hold. Composite: HUH, WATER text. Audio: AU01. End.

## Final assembly

Cut clips at `TIMELINE.csv` timestamps; place AU01; add all exact text/graphics; mask A06 inside E01; preserve locked frames; export 1080x1920, 24 fps, 109.227 s.
