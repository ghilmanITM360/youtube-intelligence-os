# Image-to-video rebuild

Use generated clean plates from `IMAGE_PROMPTS.md`, animation passes only from `ANIMATION_PROMPTS.md`, source audio AU01 on final A1, then cut/composite in one 24-fps 1920×1080 assembly. Add exact text, formulas, time strips, metrics, labels, credits, and book covers as editor overlays. Never bake them into I2V clips. Hard cuts remain hard cuts.

### S01 — 00:00.000–00:10.667
State chain: F01.0, A01, F01.1. Source: IMG01, generate once. I2V: A01. Overlay: T01. Cut: S02.

### S02 — 00:10.667–00:12.667
State: F02.0. Source: IMG30, generate. Animation required: no; hold 2.000 s. Overlay: T02. Cut: S03.

### S03 — 00:12.667–00:22.750
State chain: F03.0, A03, F03.1. Sources: IMG02 start, IMG03 end. I2V: A03 with start/end frame control. Overlay: G03. Cut: S04.

### S04 — 00:22.750–00:30.375
State: F04.0. Source: IMG04. Animation required: no; hold. Overlay: T03. Cut: S05.

### S05 — 00:30.375–00:32.958
State: F05.0. Source: IMG05. Animation required: no; hold. Overlay: T03. Cut: S06.

### S06 — 00:32.958–00:39.542
State: F06.0. Source: IMG06. Animation required: no; hold. Overlay: landmark labels and T03. Cut: S07.

### S07 — 00:39.542–00:45.167
State: F07.0. Source: IMG07. I2V: A07, or use static hold plus text overlay for higher fidelity. Overlay: T03 and exact weights. Cut: S08.

### S08 — 00:45.167–00:50.792
State: F08.0. Source: IMG08. Animation required: no; hold. Cut: S09.

### S09 — 00:50.792–00:56.250
State: F09.0. Source: IMG09. Animation required: no; hold. Cut: S10.

### S10 — 00:56.250–01:05.292
State: F10.0. Source: IMG10. Animation required: no; hold. Cut: S11.

### S11 — 01:05.292–01:11.667
State: F11.0. Source: IMG11. Animation required: no; hold. Overlay: G07/T04. Cut: S12.

### S12 — 01:11.667–01:26.167
State chain: F11.0, A12, F12.0. Source: reuse IMG11. I2V: A12, but editor SVG/text overlays are higher fidelity. Overlay: G08/T03/T04. Cut: S13.

### S13 — 01:26.167–01:30.333
State: F13.0. Source: IMG12. Animation required: no; hold. Overlay: T05. Cut: S14.

### S14 — 01:30.333–01:38.000
State chain: F13.0, A14, F14.0. Source: IMG13. I2V: A14. Better composite: animate G09 rings only over static plate. Cut: S15.

### S15 — 01:38.000–01:47.708
State chain: F14.0, A15, F15.0. Source: IMG14. I2V: none needed; hold image. Overlay: G10/T03. Cut: S16.

### S16 — 01:47.708–01:59.083
State chain: F15.0, A16, F16.0. Source: IMG15. I2V: none needed; hold image. Overlay labels sequentially. Cut: S17.

### S17 — 01:59.083–02:06.375
State chain: F16.0, A17, F17.0. Source: IMG16. I2V: none needed; use SVG draw-on/editor overlay. Cut: S18.

### S18 — 02:06.375–02:13.917
State chain: month panel, A18, city panels. Source: reuse IMG07 for person/scale; generate panel clean plates as needed. I2V: no; hard-replace panel composites. Overlay: T03/T06. Cut: S19.

### S19 — 02:13.917–02:19.208
State: F19.0. Source: IMG17. Animation required: no; hold. Overlay: T03. Cut: S20.

### S20 — 02:19.208–02:24.417
State chain: intact house, A20, deformed house. Source: IMG18. I2V: A20. Fidelity risk: isolate house segments with masks; keep tree/static background out of generation. Cut: S21.

### S21 — 02:24.417–02:30.042
State chain: skyline, A21, curve/aircraft state. Source: IMG19. I2V: A21; preferred composite uses static skyline with independent curve reveal and aircraft layer. Cut: S22.

### S22 — 02:30.042–02:37.042
State: F22.0. Source: reuse IMG14. I2V: no; hold image. Overlay: G10/T03. Cut: S23.

### S23 — 02:37.042–02:42.125
State: F23.0. Source: reuse IMG15. Animation required: no; hold. Overlay gravity metric/T03. Cut: S24.

### S24 — 02:42.125–02:45.208
State: F24.0. Source: reuse IMG07. Animation required: no; hold. Overlay weights/T07. Cut: S25.

### S25 — 02:45.208–02:51.833
State chain: intact aqueduct, A25, rubble. Source: IMG17 start plus generated collapse end state. I2V: A25. Fidelity risk: use illustrated state replacements/masked arch passes; avoid one full-scene deformation. Cut: S26.

### S26 — 02:51.833–02:57.875
State chain: skyline, A26, annotated skyline. Source: IMG20. I2V: no; hold plate. Overlay G15 with editor draw-on. Cut: S27.

### S27 — 02:57.875–03:06.125
State chain: split Earth, A27, ring state. Source: reuse IMG15. I2V: A27; preferred composite is static plate + G16 SVG draw-on. Overlay metric/T03. Cut: S28.

### S28 — 03:06.125–03:15.875
State chain: landscape, A28, pressure diagram. Source: IMG21. I2V: no; hold plate. Overlay G17 with editor draw-on. Cut: S29.

### S29 — 03:15.875–03:22.708
State: F29.0. Source: reuse IMG15 with larger Earth crop. Animation required: no; hold. Overlay metric/T03. Cut: S30.

### S30 — 03:22.708–03:25.625
State: F30.0. Source: IMG22. Animation required: no; hold. Overlay weight/T03. Cut: S31.

### S31 — 03:25.625–03:34.875
State: F31.0. Source: IMG23. Animation required: no; hold. Overlay T08. Cut: S32.

### S32 — 03:34.875–03:47.625
State: F32.0. Source: IMG24. Animation required: no; hold. Overlay exact chart labels/T03. Cut: S33.

### S33 — 03:47.625–03:52.708
State: F33.0. Source: IMG25. Animation required: no; hold. Cut: S34.

### S34 — 03:52.708–04:00.000
State: F34.0. Source: IMG26. Animation required: no; hold. Overlay G19/T09. Cut: S35.

### S35 — 04:00.000–04:11.583
State chain: board baseline, A35, comparison board. Source: IMG27. I2V: no; use static board and editor scale/reveal of large SVG graphic. Overlay T10. Cut: S36.

### S36 — 04:11.583–04:24.000
State chain: comparison, A36, burst, compact disk. Source: reuse IMG27. I2V: no; hard-replace SVG graphics in board right half. Overlay T10. Cut: S37.

### S37 — 04:24.000–04:37.083
State chain: base space, A37, orbit state. Source: IMG28. I2V: A37, or use editor opacity reveals of satellites/orbits. Overlay T03. Cut: S38.

### S38 — 04:37.083–05:05.625
State chain: orbital state, A38, ring build A39, final A40. Source: reuse end frame from A37/IMG28, then IMG29. I2V passes: A38; A39; A40. Composite satellites, ring lines, and final plate separately to prevent motion leakage. Cut: S39.

### S39 — 05:05.625–05:15.675
State: F39.0. Source: IMG31. Animation required: no; hold. Overlay book covers and exact credits/T11. End.

## Final assembly

Maintain locked framing, strict cut times, source audio timing, and 24-fps export. No interpolation between hard-cut source states. Use masks only for S20, S25, S38 local motion/composites.
