# Asset Creation List

**Make them in this order.** The first three are reused everywhere — drawing
them first and reusing the files is what keeps the five plates consistent.
Nothing here is generated twice.

```
FORMAT legend:   PNG-T = transparent PNG   PLATE = full-frame base image
                 TEXT = CapCut native text layer (never generated)
```

## Group 1 — Reusable core pieces (draw once, reuse forever)

```
01. COFFEE MUG  (O01)
    USED IN:    VISUAL 01 (large), VISUAL 02 (on baseline), VISUAL 03 (small),
                VISUAL 04 (small top-centre), VISUAL 05 (×3 inside G12)
    FORMAT:     PNG-T, then rescaled
    BACKGROUND: transparent
    REUSE:      RECURRING — the most reused object in the plan.
                Draw ONCE. Rescale for each use. Never redraw.
                Handle always on the right. Brown band always inside the rim.

02. HEART  (G01 → G11)
    USED IN:    VISUAL 01 (large, x42–58% y34–43%), VISUAL 05 (small, in the
                middle list plate)
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      RECURRING — rescale for VISUAL 05, do not draw a second heart.
                Plain outline, not filled, not anatomical.

03. DR. REHAN  (C01 + poses B and C)
    USED IN:    VISUAL 01 (arm raised), VISUAL 03 (arms down, facing right),
                VISUAL 05 (arms down, facing left)
    FORMAT:     PNG-T for pose A; poses B and C are drawn into IMG03 / IMG05
    BACKGROUND: transparent (pose A)
    REUSE:      RECURRING — see DR_REHAN_CHARACTER_MASTER.md.
                Rectangular glasses + short beard + side hair. No coat,
                no stethoscope.
```

## Group 2 — The five base plates

```
04. IMG01 — mug + heart, empty bottom 56%
    USED IN:    VISUAL 01, all 5 states
    FORMAT:     PLATE 2160×3840
    BACKGROUND: flat off-white, opaque
    REUSE:      single shot
    NOT BAKED:  fork lines, label plates, text, doctor, red strike

05. IMG02 — baseline + mug + the mug's 2 strokes
    USED IN:    VISUAL 02, all 4 states
    FORMAT:     PLATE
    BACKGROUND: flat off-white, opaque
    REUSE:      single shot
    NOT BAKED:  can, the can's 4 strokes, caution triangle

06. IMG03 — doctor + compact binary diagram
    USED IN:    VISUAL 03, all 3 states
    FORMAT:     PLATE — then SPLIT into IMG03_base + IMG03_diagram
    BACKGROUND: off-white (base) / transparent (diagram)
    REUSE:      single shot
    NOT BAKED:  patient, GOOD?/BAD? text. NO red strike in this shot at all

07. IMG04 — mug top-centre + one ground line. NOTHING ELSE
    USED IN:    VISUAL 04, all 3 states
    FORMAT:     PLATE
    BACKGROUND: flat off-white, opaque
    REUSE:      single shot
    NOT BAKED:  the two figures (they are C03 duplicated), both arrows,
                all arcs

08. IMG05 — doctor + three EMPTY plates + connector line
    USED IN:    VISUAL 05, all 5 states
    FORMAT:     PLATE — then SPLIT into IMG05_base + IMG05_plates
    BACKGROUND: off-white (base) / transparent (plates)
    REUSE:      single shot
    NOT BAKED:  all text, heart icon, cup icon, video card.
                NO gauge or dial exists in this project
```

## Group 3 — Character overlays

```
09. C02 PATIENT
    USED IN:    VISUAL 03 (R03.1, R03.2)
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      single use. Deliberately featureless — no face at all

10. C03 PLAIN FIGURE — GENERATE EXACTLY ONE
    USED IN:    VISUAL 04, all 3 states, placed TWICE
    FORMAT:     PNG-T, one instance
    BACKGROUND: transparent
    REUSE:      DUPLICATE THE LAYER IN CAPCUT. Never generate a second figure.
                The shot's argument depends on the two being identical
```

## Group 4 — Object overlay

```
11. O02 ENERGY-DRINK CAN
    USED IN:    VISUAL 02 (R02.1–R02.3)
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      single use. Unbranded: no logo, no lettering, no brand colour.
                Must not resemble any real product
```

## Group 5 — Graphic overlays

```
12. G02a FORK LEFT HALF   (left branch line + empty left plate)
13. G02b FORK RIGHT HALF  (right branch line + empty right plate)
    USED IN:    VISUAL 01 (R01.1 / R01.2 onward)
    FORMAT:     PNG-T, two SEPARATE files
    BACKGROUND: transparent
    REUSE:      single shot. Two files is what makes the two word-anchored
                reveals possible. The plates must be identical to each other

14. G03 RED STRIKE STROKE
    USED IN:    VISUAL 01 (R01.4) — ONCE in the whole video
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      SINGLE USE. Revision 1 removed the second strike.
                One stroke, not a cross, not an X

15. G04b THE CAN'S FOUR STROKES
    USED IN:    VISUAL 02 (R02.2, R02.3)
    FORMAT:     PNG-T, one grouped file
    BACKGROUND: transparent
    REUSE:      single shot. Individual stroke length MUST match the mug's two
                strokes in IMG02 — draw both groups in one sitting

16. G05 CAUTION TRIANGLE
    USED IN:    VISUAL 02 (R02.3)
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      single use. Muted red outline, no fill. One mark, one object

17. G07 CONNECTOR ARROW  (generate one, mirror for the second)
    USED IN:    VISUAL 04 (R04.1 left, R04.2 right)
    FORMAT:     PNG-T, one file + its horizontal mirror
    BACKGROUND: transparent
    REUSE:      mirrored reuse. ONE complete stroke — no segmented versions,
                the arrows no longer draw along their curve

18. G08 RESPONSE ARCS  (two versions: 1 arc, 3 arcs)
    USED IN:    VISUAL 04 (R04.1 single, R04.2 triple)
    FORMAT:     PNG-T, two files
    BACKGROUND: transparent
    REUSE:      single shot. Same stroke weight and spacing in both.
                Unlabelled — no numbers, no scale, no ECG trace

19. G12 THREE-CUP QUANTITY ICON
    USED IN:    VISUAL 05 (R05.3)
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      DERIVED FROM ASSET 01 — rescale and repeat the mug, decreasing
                size left to right. No count label, no volume figure

20. G13 VIDEO CARD + PLAY MARK
    USED IN:    VISUAL 05 (R05.4)
    FORMAT:     PNG-T
    BACKGROUND: transparent
    REUSE:      single use. Empty panel + hollow right-pointing triangle.
                No logo, no thumbnail, no subscribe button
```

## Group 6 — Text (never generated as an image)

```
21. T01 GOOD?              VISUAL 01 + VISUAL 03   TEXT   recurring
22. T02 BAD?               VISUAL 01 + VISUAL 03   TEXT   recurring
23. T03 BLOOD PRESSURE     VISUAL 05               TEXT   single shot
24. T04 HEART RESPONSE     VISUAL 05               TEXT   single shot
25. T05 QUANTITY           VISUAL 05               TEXT   single use
26. T06 WATCH THE FULL VIDEO  VISUAL 05            TEXT   single use
```
One text style for all six. `BLOOD PRESSURE` is set largest — it owns its plate.

## Group 7 — Audio and background

```
27. E01 OFF-WHITE FIELD    all states   solid colour layer or one flat PNG
28. AU01 NARRATION TRACK   all states   supplied recording, unmodified.
                                        No music bed, no sound effects
```

## Deleted — do not create

```
G10 BLOOD-PRESSURE GAUGE / DIAL — removed in Revision 1. Do not draw a dial,
    needle, meter or up/down arrow for blood pressure anywhere in this project.

SECOND RED STRIKE (VISUAL 03) — removed in Revision 1. VISUAL 03 deletes the
    diagram instead of striking it.

SEGMENTED ARROW VARIANTS — no longer needed; the arrows pop complete.
```

## Count

```
Reusable core pieces        3
Base plates                 5   (2 of them split-exported → 7 files)
Character overlays          2   (C03 generated once, placed twice)
Object overlays             1
Graphic overlays            9
Text layers                 6
Background + audio          2
-------------------------------
Generated / drawn artwork  20 files
```
