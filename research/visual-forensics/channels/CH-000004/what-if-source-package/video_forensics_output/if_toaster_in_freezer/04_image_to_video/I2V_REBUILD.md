# Image-to-video rebuild

Generate IMG01–IMG12 from `IMAGE_PROMPTS.md`; preserve one master per shot. Use generated end frames/state plates when a state follows an I2V pass. Text, equations, arrows, diagrams, and hard cuts remain final-assembly overlays, not generator text.

### S01 — 00:00.000–00:10.750

State chain: F01.0 / A01 / F01.1 / A02 / F01.3. Source image: IMG01. Image action: generate once. I2V: A01, A02. Composite: G01 plus separate board-sketch layers. Audio: AU01 master. Cut to S02. Fidelity risk: generated draw-on can wobble; editor masks are preferred.

### S02 — 00:10.750–00:25.250

State chain: F02.0 / A04 / F02.1 / A05 / F02.2 / A06 / F02.4 / A07 / F02.5. Source image: IMG02. Image action: generate once. I2V: A04–A07. Composite: add heat, frost, toast, arcs, grey wash, and caption as isolated overlays. Audio: AU01. Cut to S03. Fidelity risk: never animate refrigerator/background for local overlays.

### S03 — 00:25.250–00:29.250

State chain: F03.0. Source image: IMG03. Image action: generate once. Animation required: no; hold 4.000 s. Composite: exact title text in editor. Audio: AU01. Cut to S04.

### S04 — 00:29.250–00:42.000

State chain: F04.0 / A10 / F04.1 / A11 / F04.2 / A12 / F04.4 / A13 / F04.5. Source image: IMG04. Image action: generate once. I2V: A10–A13. Composite: toaster master, headings, heat strokes, coil-state plate, glow, and 600°C text. Audio: AU01. Cut to S05.

### S05 — 00:42.000–00:58.000

State chain: F05.0 / A15 / F05.3. Source image: IMG05. Image action: generate once. I2V: A15. Composite: all markers/bracket as vector/text overlays. Audio: AU01. Cut to S06. Fidelity risk: use editor vectors; generated diagram text will drift.

### S06 — 00:58.000–01:03.250

State chain: F06.0 / A17 / F06.1. Source image: IMG06. Image action: generate once. I2V: A17. Composite: speech bubble and exact wording overlay. Audio: AU01. Cut to S07.

### S07 — 01:03.250–01:15.000

State chain: F07.0 / A19 / F07.1 / A20 / F07.2 / A21 / F07.3. Source image: IMG07. Image action: generate once. I2V: A19–A21. Composite: use closed-door end frame, then local glow/icicle/power overlays. Audio: AU01. Cut to S08. Fidelity risk: door and toaster are coupled; do one door pass, never include people motion.

### S08 — 01:15.000–01:45.000

State chain: F08.0 / A23 / F08.3 / A24 / F08.4 / A25 / F08.5 / A26 / F08.7. Source image: IMG08. Image action: generate once. I2V: A23–A26. Composite: all labels/arrows/equations as editor vectors; toaster and glow on separate local layers. Audio: AU01. Cut to S09. Fidelity risk: high text/geometry drift; prefer editor-drawn diagram states over a broad I2V pass.

### S09 — 01:45.000–01:58.000

State chain: F09.0 / A28 / F09.3. Source image: IMG09. Image action: generate once. I2V: A28. Composite: toaster/glow/600°C/-18°C and caption overlays. Audio: AU01. Cut to S10.

### S10 — 01:58.000–02:26.000

State chain: F10.0 / A30 / F10.1 / F10.2 / A31 / F10.3 / A32 / F10.4 / A33 / F10.5 / A34 / F10.7. Source image: IMG10. Image action: generate once. I2V: A30–A34. Composite: dark wash, location text, stool/toaster/bread, figure pose-state cutouts, and ALWOOO... overlay. Audio: AU01. Cut to S11. Fidelity risk: use still source plus isolated toaster/pose passes; no tree/snow drift.

### S11 — 02:26.000–02:33.000

State chain: F11.0 / A36 / F11.1 / A37 / F11.2. Source image: IMG11. Image action: generate once. I2V: A36, A37. Composite: conclusion text as editor layers. Audio: AU01. Cut to S12.

### S12 — 02:33.000–02:42.261

State chain: F12.0. Source image: IMG12. Image action: generate once or use a source-derived end-card plate. Animation required: no; hold 14.011 s. Composite: exact book covers and small copy. Audio: AU01. End.

## Final assembly

At 24 fps, place each state/clip at `TIMELINE.csv` in/out values, hard-cut all listed cut events, place AU01 first, add exact readable text, then export 1920x1080. This is final assembly for Way 2, not a third production path.
