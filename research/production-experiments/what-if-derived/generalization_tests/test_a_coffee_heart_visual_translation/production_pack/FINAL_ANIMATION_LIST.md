# Final Animation List — 15 animations, timeline order

**14 of the 15 are a layer becoming visible or invisible on one frame.**
One is a 4-frame linear wipe. That is the entire animation workload.

```
0 camera moves · 0 fades · 0 transitions · 0 generated video · 1 mask
```

**Placement rule.** Scrub the narration, find the onset frame of the anchor
word, put the operation on that frame. No offset, no padding, no lead-in.

---

## VISUAL 01 — layer stack (bottom → top)

```
1. E01              off-white field          visible at start
2. IMG01            base plate               visible at start
3. G02a             fork left + plate        hidden
4. T01  text        GOOD?                    hidden
5. G02b             fork right + plate       hidden
6. T02  text        BAD?                     hidden
7. C01              Dr. Rehan, arm raised    hidden
8. G03 + wipe mask  red strike               hidden
```

```
M01
Narration trigger:  ON "good" (w3)
Source state:       R01.0   Target state: R01.1
Animation:          Fork-left group and GOOD? appear, one frame
Static anchors:     off-white field, mug, heart, camera
CapCut operation:   Turn on layers 3 and 4 on the same frame
Short prompt:       The left branch and its GOOD? label appear instantly.
                    Nothing else changes. No camera motion.
```
```
M02
Narration trigger:  ON "bad" (w7)
Source state:       R01.1   Target state: R01.2
Animation:          Fork-right group and BAD? appear, one frame
Static anchors:     field, mug, heart, fork lines, left plate, GOOD?, camera
CapCut operation:   Turn on layers 5 and 6 on the same frame
Short prompt:       The right label plate and its BAD? label appear instantly,
                    completing the fork. Nothing else moves. No camera motion.
```
```
M03
Narration trigger:  ON "Rehan" (w11)
Source state:       R01.2   Target state: R01.3
Animation:          Dr. Rehan appears, one frame. No walk-in, no slide, no scale
Static anchors:     field, mug, heart, fork, both plates, both labels, camera
CapCut operation:   Turn on layer 7
Short prompt:       The doctor appears in the empty lower-left corner in a
                    single frame, arm already raised. No camera motion.
```
```
M04
Narration trigger:  ON "wrong" (w16)
Source state:       R01.3   Target state: R01.4
Animation:          Red strike draws left → right, 4 FRAMES ONLY, then holds
Static anchors:     everything else in frame, including the doctor
CapCut operation:   Turn on layer 8; animate its linear wipe mask across
                    4 frames (0.167s ESTIMATED). Not half a second. Not a phrase
Short prompt:       The red strike quickly draws across the two answer branches
                    in a few frames. Coffee mug, heart, labels, doctor and
                    background remain completely static. No camera motion.
```

---

## VISUAL 02 — layer stack

```
1. E01    off-white field                 visible at start
2. IMG02  base plate (line + mug + 2 strokes)  visible at start
3. O02    energy-drink can                hidden
4. G04b   the can's four strokes (group)   hidden
5. G05    caution triangle                hidden
```

```
M05
Narration trigger:  ON "energy" (w26)
Source state:       R02.0   Target state: R02.1
Animation:          Can appears at its exact position, one frame.
                    No drop-in, no bounce, no scale
Static anchors:     field, baseline, mug, the mug's two strokes, camera
CapCut operation:   Turn on layer 3
Short prompt:       The energy-drink can appears standing on the same baseline
                    as the mug, instantly. Nothing else changes. No camera motion.
```
```
M06
Narration trigger:  ON "stronger" (w35)
Source state:       R02.1   Target state: R02.2
Animation:          All four strokes appear TOGETHER, one frame. No stagger
Static anchors:     field, baseline, mug, mug strokes, can, camera
CapCut operation:   Turn on layer 4 — ONE grouped layer, so they cannot stagger
Short prompt:       Four short strokes appear above the can all at once, the
                    same length as the two above the mug. Everything else stays
                    static. No camera motion.
```
```
M07
Narration trigger:  ON "dangerous" (w44)
Source state:       R02.2   Target state: R02.3
Animation:          Caution triangle appears, one frame, then static.
                    No pulse, no flash, no shake, no glow
Static anchors:     everything else in frame, camera
CapCut operation:   Turn on layer 5. No effects applied
Short prompt:       One small red caution triangle appears above the can in a
                    single frame and then holds perfectly still. The mug's side
                    of the frame stays empty. No camera motion.
```

---

## VISUAL 03 — layer stack

```
1. E01            off-white field              visible at start
2. IMG03_base     off-white + doctor only      visible at start
3. IMG03_diagram  mug + lines + empty plates   visible at start
4. T01  text      GOOD?  (repositioned)        visible at start
5. T02  text      BAD?   (repositioned)        visible at start
6. C02            patient                      hidden
```

```
M08
Narration trigger:  ON "patients" (w53)
Source state:       R03.0   Target state: R03.1
Animation:          Patient appears, one frame. No walk-in
Static anchors:     field, Dr. Rehan, diagram, plates, both labels, camera
CapCut operation:   Turn on layer 6.
                    Then NOTHING for ~4.3s ESTIMATED — do not fill this hold
Short prompt:       The patient appears facing the doctor across the diagram,
                    in a single frame, then the whole frame holds completely
                    still while the question is spoken. No camera motion.
```
```
M09
Narration trigger:  ON "not" (w70)
Source state:       R03.1   Target state: R03.2
Animation:          The entire diagram and both labels DISAPPEAR, one frame.
                    No fade, no shrink, no wipe
Static anchors:     field, Dr. Rehan, the patient, camera
CapCut operation:   Turn OFF layers 3, 4 and 5 on the same frame
Short prompt:       The whole good/bad diagram and both its labels vanish in a
                    single frame, leaving the doctor and patient exactly where
                    they were and the space between them empty. No fade, no
                    camera motion.
```

---

## VISUAL 04 — layer stack

```
1. E01    off-white field                       visible at start
2. IMG04  base plate (mug + ground line only)   visible at start
3. C03    figure instance A, x14–36%            visible at start
4. C03    figure instance B, x64–86% — SAME LAYER DUPLICATED   visible at start
5. G07a   left arrow                            hidden
6. G08a   single arc                            hidden
7. G07b   right arrow (mirrored)                hidden
8. G08b   three arcs                            hidden
```

```
M10
Narration trigger:  ON "respond" (w89)
Source state:       R04.0   Target state: R04.1
Animation:          Left arrow AND single arc appear together, complete, one
                    frame. The arrow does NOT draw along its curve
Static anchors:     field, ground line, mug, BOTH figures, camera
CapCut operation:   Turn on layers 5 and 6 on the same frame. No mask,
                    no keyframes
Short prompt:       A curved arrow from the mug to the left person and one red
                    arc at their chest appear together, already complete, in a
                    single frame. The right half of the frame stays unmarked.
                    Nothing moves. No camera motion.
```
```
M11
Narration trigger:  ON "judge" (w100)
Source state:       R04.1   Target state: R04.2
Animation:          Right arrow AND three arcs appear together, complete, one
                    frame. The arrow does NOT draw along its curve
Static anchors:     field, ground line, mug, both figures, left arrow,
                    left arc, camera
CapCut operation:   Turn on layers 7 and 8 on the same frame. No mask,
                    no keyframes
Short prompt:       The mirrored arrow to the right person and three stacked red
                    arcs at their chest appear together in a single frame. The
                    two figures are now identical except for the number of arcs.
                    No camera motion.
```

**Both arrows pop rather than draw** for two reasons that agree: CapCut masks
are linear and cannot follow a curve, and the corpus reveals curved arrows as
completed groups in a handful of frames. Using the same mechanism on both sides
is also what makes the two readings genuinely comparable in the finished edit.

---

## VISUAL 05 — layer stack

```
1. E01           off-white field                 visible at start
2. IMG05_base    off-white + doctor only         visible at start
3. IMG05_plates  three empty plates + connector  visible at start
4. T03  text     BLOOD PRESSURE                  hidden
5. G11           heart icon                      hidden
6. T04  text     HEART RESPONSE                  hidden
7. G12           three-cup icon                  hidden
8. T05  text     QUANTITY                        hidden
9. G13           video card + play mark          hidden
10. T06 text     WATCH THE FULL VIDEO            hidden
```

```
M12
Narration trigger:  ON "blood" (w111)
Source state:       R05.0   Target state: R05.1
Animation:          BLOOD PRESSURE text appears, one frame. TEXT ONLY
Static anchors:     field, Dr. Rehan, all three plates, connector, camera
CapCut operation:   Turn on layer 4. Nothing else — there is no gauge icon
                    in this project
Short prompt:       The words BLOOD PRESSURE appear alone inside the top plate
                    in a single frame. The other two plates stay empty and
                    nothing moves. No camera motion.
```
```
M13
Narration trigger:  ON "heart" (w113)
Source state:       R05.1   Target state: R05.2
Animation:          Heart icon AND its text appear together, one frame.
                    Must not stagger
Static anchors:     field, Dr. Rehan, plates, connector, top plate text, camera
CapCut operation:   Turn on layers 5 and 6 on the same frame
Short prompt:       A small heart and the words HEART RESPONSE appear together
                    in the middle plate in a single frame. Everything else
                    holds still. No camera motion.
```
```
M14
Narration trigger:  ON "quantity" (w116)
Source state:       R05.2   Target state: R05.3
Animation:          Three-cup icon AND its text appear together, one frame.
                    Must not stagger
Static anchors:     field, Dr. Rehan, plates, connector, the two filled plates
                    above, camera
CapCut operation:   Turn on layers 7 and 8 on the same frame
Short prompt:       Three coffee cups in decreasing size and the word QUANTITY
                    appear together in the bottom plate in a single frame,
                    completing the list. No camera motion.
```
```
M15
Narration trigger:  ON "full" (w124)
Source state:       R05.3   Target state: R05.4
Animation:          Whole plate column OUT and video card + CTA IN, on the
                    SAME frame. No fade, no crossfade, no slide
Static anchors:     field, Dr. Rehan, camera
CapCut operation:   On one frame: turn OFF layers 3, 4, 5, 6, 7, 8 and turn ON
                    layers 9 and 10
Short prompt:       In one frame the three-item list and everything in it
                    disappears and a video card with a play mark and the caption
                    WATCH THE FULL VIDEO takes its place. The doctor does not
                    move. No fade, no camera motion.
```

---

## Operation totals

| Operation | Count |
|---|---|
| Single-layer visibility ON | 5 |
| Coupled two-layer visibility ON, same frame | 6 |
| Group visibility OFF | 1 |
| Simultaneous OFF + ON on one frame | 1 |
| Linear wipe mask (4 frames) | 1 |
| Keyframed transforms | 0 |
| Masks other than M04 | 0 |
| Camera moves | 0 |
| Fades / transitions | 0 |
| Generated video clips (I2V) | 0 |

**15 animations.** 14 instant, 1 four-frame draw.

## The 19 anchor words, in order

```
good · bad · Rehan · wrong · People · energy · stronger · dangerous ·
So · patients · not · The · respond · judge · Dr. · blood · heart ·
quantity · full
```

15 reveal anchors + 4 cut anchors (`People`, `So`, `The`, `Dr.`) = 19, plus the
video's first frame.
