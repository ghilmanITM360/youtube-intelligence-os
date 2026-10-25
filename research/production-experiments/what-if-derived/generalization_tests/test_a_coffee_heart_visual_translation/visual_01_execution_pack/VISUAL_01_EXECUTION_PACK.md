# VISUAL 01 — EXECUTION PACK

**The main file. Read this one; the others are the copy-paste material.**

```
Shot ID:        SH01
Base image:     IMG01
States:         R01.0 → R01.1 → R01.2 → R01.3 → R01.4   (5)
Animations:     M01  M02  M03  M04                      (4)
Words:          w1–w17
Est. duration:  4.33s  ESTIMATED — no audio has been supplied
Build method:   CAPCUT   ·   I2V: 0   ·   Camera moves: 0   ·   Fades: 0
Canvas:         2160 × 3840, 9:16 vertical
```

**Authority:** `../production_pack/` (approved) and `../revision_1/` (frozen).
Nothing here is redesigned. No state added, none removed, no representation
changed.

```
VISUAL_01_BASE_IMAGE_PROMPT.md   the plate
VISUAL_01_OVERLAY_PROMPTS.md     the four transparent PNGs
VISUAL_01_TEXT_OVERLAYS.md       the two editor text layers
VISUAL_01_ASSET_CHECKLIST.md     tick-list, generation order
VISUAL_01_LAYER_STACK.md         bottom-to-top stack
VISUAL_01_ANIMATION_PROMPTS.md   the four short animation prompts
VISUAL_01_CAPCUT_BUILD.md        editor instructions
```

---

## Narration

> "Is coffee good for your heart—or bad for it? Dr. Rehan says that's actually
> the wrong question."

Words 1–17 of the 130-word script. Not one word is changed.

---

## Purpose

Build the good-or-bad model in the viewer's head, then have the named doctor
strike it out. The shot has to make the viewer briefly own the binary before it
is rejected — a model rejected before it is understood rejects nothing.

---

## Start Frame

Flat warm off-white portrait field.

A coffee mug seen from the side, black outline, handle on its right, sits
centred in the upper third at **x36–64%, y18–30%**. Inside its top rim, a flat
coffee-brown horizontal band at x39–61%, y19–22% — the only colour in frame.

Directly below it, a single-stroke symmetrical outline heart, not filled, at
**x42–58%, y34–43%**. The mug is roughly twice the heart's width.

**Everything below y44% is empty off-white — the bottom 56% of the frame is
blank.** No text. No arrows. No lines. No figures. No other objects.

That empty lower half is not spare room. It is where the entire argument gets
built, and it is why nothing may be baked into the plate.

---

## State Sequence

### R01.0 — opening frame
```
Visible:    off-white field, mug, heart
Added:      —
Removed:    —
Moved:      —
Unchanged:  (first frame of the video)
```

### R01.1 — ON "good" (w3)
```
Visible:    field, mug, heart, left fork line, left plate, GOOD?
Added:      G02a left branch + left plate; T01 text GOOD? inside it
Removed:    —
Moved:      nothing
Unchanged:  mug, heart, field, camera
```
Two straight thin lines now descend from the heart's bottom point at x50%,y44%
— one to x18%,y56%, one to x82%,y56% — forming a wide inverted V. Only the left
one ends in a plate. The right line ends in empty field.

### R01.2 — ON "bad" (w7)
```
Visible:    field, mug, heart, both fork lines, both plates, GOOD?, BAD?
Added:      G02b right plate; T02 text BAD? inside it
Removed:    —
Moved:      nothing
Unchanged:  mug, heart, left plate, GOOD?, field, camera
```
The model is now symmetrical: one mug, one heart, two branches, two labels.
Below y68% still empty.

### R01.3 — ON "Rehan" (w11)
```
Visible:    everything above, plus Dr. Rehan lower-left
Added:      C01 at x8–30%, y70–95%, facing right, near arm raised toward the fork
Removed:    —
Moved:      nothing
Unchanged:  entire model, field, camera
```
Lower-right field stays empty.

### R01.4 — ON "wrong" (w16)
```
Visible:    everything above, plus the red strike
Added:      G03 — one thick muted-red stroke from x14%,y68% up to x86%,y52%,
            crossing both branch lines and clipping the top edge of both plates
Removed:    —
Moved:      nothing
Unchanged:  mug, heart, fork, both plates, both text labels, Dr. Rehan, camera
```
Both labels stay legible under the stroke. Held to the cut.

---

## What stays static through the whole visual

```
The off-white field          never changes value, never moves
The coffee mug               never moves, never rescales, never redraws
The outline heart            never moves, never fills, never beats
The camera                   locked. Zero pans, zooms, pushes, tilts, shakes
Everything already revealed  nothing that appears ever moves or leaves
```

**Nothing is ever removed in Visual 01.** All four operations are additions.
This is the only visual in the video with no deletion, which is why IMG01 needs
no split export.

---

## Assets Needed

| ID | What | Format | Background | Reuse |
|---|---|---|---|---|
| E01 | Off-white field | solid layer or flat PNG | — | RECURRING, whole video |
| IMG01 | Base plate: mug + heart | 2160×3840 image | off-white, opaque | Visual 01 only |
| G02a | Fork left half | PNG-T | transparent | Visual 01 only |
| G02b | Fork right half | PNG-T | transparent | Visual 01 only |
| C01 | Dr. Rehan, arm raised | PNG-T | transparent | RECURRING, 3 visuals |
| G03 | Red strike stroke | PNG-T | transparent | SINGLE USE, whole video |
| T01 | Text `GOOD?` | CapCut text | — | returns in Visual 03 |
| T02 | Text `BAD?` | CapCut text | — | returns in Visual 03 |

Full prompts: `VISUAL_01_BASE_IMAGE_PROMPT.md`, `VISUAL_01_OVERLAY_PROMPTS.md`.

**Must NOT be baked into IMG01:** fork lines, either label plate, any text, the
doctor, the red strike, any red at all.

---

## Text Overlays

```
T01   GOOD?   left plate,  x10–40% y56–66%   ON "good" (w3)
T02   BAD?    right plate, x60–90% y56–66%   ON "bad"  (w7)
```

Both are CapCut native text. Neither is generated in an image. Same typeface,
same size, same weight, same black — `BAD?` is the shorter word and must not be
scaled up to fill its plate, or the shorter answer reads as the emphasised one.
Details in `VISUAL_01_TEXT_OVERLAYS.md`.

---

## Animations

```
M01   ON "good"   (w3)    fork left + GOOD? appear        1 frame
M02   ON "bad"    (w7)    fork right + BAD? appear        1 frame
M03   ON "Rehan"  (w11)   Dr. Rehan appears               1 frame
M04   ON "wrong"  (w16)   red strike draws left → right   4 frames, then holds
```

All four are CapCut. Camera static in all four. No fades, no easing, no
entrance presets.

**Placement rule:** scrub the narration, find the onset frame of the anchor
word, put the operation on that frame. No offset, no padding, no lead-in.

**M04's four frames are a hard spec.** It is a flick of the pen that completes
before the next word — not a gesture spread across the phrase "the wrong
question."

Short prompts: `VISUAL_01_ANIMATION_PROMPTS.md`.

---

## CapCut Build

```
Layer 8 — G03 red strike + wipe mask        hidden at start
Layer 7 — C01 Dr. Rehan                     hidden at start
Layer 6 — T02 text BAD?                     hidden at start
Layer 5 — G02b fork right half              hidden at start
Layer 4 — T01 text GOOD?                    hidden at start
Layer 3 — G02a fork left half               hidden at start
Layer 2 — IMG01 base plate                  VISIBLE at start
Layer 1 — E01 off-white field               VISIBLE at start
```

Each label sits directly above its own plate so the two switch as a pair. The
strike sits on top of everything so it visibly crosses the diagram rather than
hiding behind it. Full editor instructions in `VISUAL_01_CAPCUT_BUILD.md`.

---

## Transition to Visual 02

```
HARD CUT on the onset of "People" (w18)
```

No transition effect. Butt cut. The off-white background layer runs across the
cut unbroken — only the plate and its overlays change.

---

## Production Order

```
1.  Set the CapCut project: 9:16, 2160×3840, 24 fps.
2.  Import the narration audio and LOCK it. Mark the onset frames of
    "good" (w3), "bad" (w7), "Rehan" (w11), "wrong" (w16) and "People" (w18).
3.  Create E01, the off-white field, spanning the whole timeline.
4.  Generate IMG01. Check the bottom 56% is genuinely empty, the handle is on
    the right, there is no text and no red. Sample its off-white and line
    weight — every later plate must match.
5.  Generate C01 Dr. Rehan. Keep the file: Visuals 03 and 05 reuse this design.
6.  Generate G02a and G02b in the same session. Compare the two plates
    side by side — identical size, corner radius, stroke weight.
7.  Generate G03, the red strike.
8.  Import all four as layers 2, 3, 5, 7, 8 at 100% scale, no repositioning.
9.  Type T01 GOOD? and T02 BAD? as native text on layers 4 and 6. Same style.
10. Place M01 and M02: trim tracks 3+4 to the "good" frame, tracks 5+6 to the
    "bad" frame. Step one frame back to verify each pair appears together.
11. Place M03: trim track 7 to the "Rehan" frame.
12. Place M04: trim track 8 to the "wrong" frame, add the linear wipe mask at
    the stroke's angle, keyframe it across exactly 4 frames, interpolation
    LINEAR. Step through frame by frame to confirm it is 4 and not more.
13. Hold the finished frame to w18, then hard cut. No transition effect.
14. Watch it once on a phone. Check: both labels readable under the strike,
    the strike reads as a flick not a slide, nothing drifts or eases.
```

---

## OPEN PRODUCTION QUESTIONS

Three genuine unresolved items. None of them blocks generating the assets —
all three are resolved by looking at the generated files.

**1. Is IMG01 generated whole, or assembled from the reusable mug and heart?**
The asset list says draw the mug once and the heart once and reuse them at
other scales; the base-image list gives IMG01 as a single generated plate
containing both. Both readings are consistent with Revision 1 and it does not
change a single pixel of the specified composition. Recommendation: **generate
IMG01 whole**, then cut the mug and heart out of it as the reusable reference
for Visuals 02–05 — that way the reused pieces are guaranteed to match the
first plate the viewer sees. Confirm before generating the later plates.

**2. Red strike thickness is not specified numerically.**
Revision 1 fixes the stroke's path (x14%,y68% → x86%,y52%) but not its weight.
It must read as decisive at phone size while leaving `GOOD?` and `BAD?`
readable underneath. This is settled by generating it and checking on a phone
with the text layers on, not by a number in a file.

**3. Text size for GOOD? / BAD? is not specified numerically.**
Style, colour, weight and position are fixed; point size is not. Set it large
enough to fill most of the plate width, identical for both words, then verify
on a phone. Same size for both is the binding constraint, not the size itself.

---

## Note on file paths in the request

The task named four Revision 1 files that do not exist under those names —
`REVISION_1_FINAL_VISUAL_PRODUCTION_PLAN.md`, `REVISION_1_VISUAL_STATES.csv`,
`REVISION_1_BASE_IMAGES.csv`, `REVISION_1_ANIMATION_PROMPTS.md`. The actual
files are `REVISED_FINAL_VISUAL_PRODUCTION_PLAN.md`,
`REVISED_VISUAL_STATES.csv`, `REVISED_BASE_IMAGES.csv` and
`REVISED_ANIMATION_PROMPTS.md`. Those were read as the authority. A naming
difference only — the content matched the approved production pack with no
contradiction.
