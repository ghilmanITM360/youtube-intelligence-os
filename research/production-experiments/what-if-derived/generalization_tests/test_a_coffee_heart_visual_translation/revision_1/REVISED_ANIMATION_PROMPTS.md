# Revised Animation Prompts — Revision 1

One prompt per motion, 1–3 lines each. Every prompt names what moves, what
stays static, and states that the camera does not move.

**15 motions. 14 are one-frame appearances or removals. 1 is a 4-frame draw.
All 15 are built in the editor. None requires image-to-video generation.**

That ratio is not a stylistic choice — it is what the portrait corpus does. In
the brain's 230 portrait motions, the single most common SPEED value is
`ONE-FRAME CHANGE` (28 rows), followed by `FAST` (27) and `INSTANT` (21), and a
further 30 rows give an explicit frame count between 3 and 15 frames.

## Changes from the first pass

| First pass | Revision 1 |
|---|---|
| A04 strike draws across "wrong … question." | **M04** draws in 4 frames on "wrong" |
| A09 second strike draws across "not … asked." | **Removed entirely** |
| A10 deletion on "That's" (w77) | **M09** deletion on "not" (w70) |
| A11 left arrow draws along a curve, then A12 pops the arc | **M10** — arrow and arc pop together in one frame |
| A13 right arrow draws along a curve, then arcs pop | **M11** — arrow and all three arcs pop together in one frame |
| A14 reveals gauge icon + text | **M12** reveals text only |

The three curved draws are gone. Every one of them was replaced by the
treatment the corpus actually uses for curved arrows — a group reveal in a
handful of frames — which happens to also be the only treatment CapCut can
execute exactly.

---

## SH01

**M01** — On the onset of the word "good", the two fork lines, the left label
plate and its GOOD? text appear together in a single frame. The off-white
field, the coffee mug and the heart do not change. No camera movement.

**M02** — On the onset of the word "bad", the right label plate and its BAD?
text appear together in a single frame. The mug, the heart, the fork lines and
the left plate with its text all stay exactly where they are. No camera
movement.

**M03** — On the onset of the word "Rehan", the doctor figure appears in the
lower-left field in a single frame. He does not walk in, slide in or scale up;
he is simply there on the next frame. The mug, heart, fork and both plates with
their text are unchanged. No camera movement.

**M04** — On the onset of the word "wrong", the muted-red strike stroke draws
itself left to right along its own fixed diagonal path, completing in 4 frames.
The mug, heart, fork lines, both plates, both text labels and the doctor are
all completely static throughout. No camera movement. The stroke must be
finished well before the word "question."

---

## SH02

**M05** — On the onset of the word "energy", the tall unbranded can appears
standing on the baseline to the right of the mug, in a single frame. It does
not drop in, bounce or scale. The baseline, the mug and the mug's two strokes
are unchanged. No camera movement.

**M06** — On the onset of the word "stronger", all four of the can's
stimulation strokes appear together in one frame as a single group. They must
not stagger or appear one by one. The baseline, mug, the mug's two strokes and
the can are unchanged. No camera movement.

**M07** — On the onset of the word "dangerous", the muted-red caution triangle
appears above the can's strokes in a single frame. It does not pulse, flash,
shake, glow or grow, and nothing else in the frame reacts to it. The baseline,
both containers and both stroke groups are unchanged. No camera movement.

---

## SH03

**M08** — On the onset of the word "patients", the patient figure appears in
the empty right field, facing the doctor, in a single frame. The doctor, the
compact binary diagram and both text labels are unchanged. No camera movement.
Hold this frame, completely still, for the whole of the patient's question —
roughly 4.3 seconds ESTIMATED. Nothing moves during that hold.

**M09** — On the onset of the word "not", the whole binary diagram group — the
small mug, both branch lines, both label plates and both text labels —
disappears in a single frame, leaving empty off-white. There is no fade, no
wipe and no shrink. The doctor and the patient do not move at all and remain
facing each other. No camera movement. Hold the emptied frame for the rest of
the sentence and through "That's a wrong question."

---

## SH04

**M10** — On the onset of the word "respond", the left connector arrow and the
left figure's single red arc appear together in one frame. The arrow is a
complete curved stroke that appears whole; it does not draw itself along its
path. The mug, the baseline and both figures are unchanged. No camera movement.

**M11** — On the onset of the word "judge", the right connector arrow and all
three of the right figure's red arcs appear together in one frame. The arrow
appears whole, and the three arcs appear as one group, not one at a time. The
mug, the baseline, both figures, the left arrow and the left arc are unchanged.
No camera movement. Hold through "or 'bad.'"

---

## SH05

**M12** — On the onset of the word "blood", the text BLOOD PRESSURE appears
inside the top list plate in a single frame. No icon appears with it. The
doctor, all three plates and the connector line are unchanged, and the middle
and bottom plates stay empty. No camera movement.

**M13** — On the onset of the word "heart", the small heart icon and the text
HEART RESPONSE appear together inside the middle plate in one frame. They must
not stagger. The doctor, all three plates, the connector line and the top
plate's text are unchanged, and the bottom plate stays empty. No camera
movement.

**M14** — On the onset of the word "quantity", the three-cup icon and the text
QUANTITY appear together inside the bottom plate in one frame. The doctor, all
three plates, the connector line and the contents of the top two plates are
unchanged. No camera movement.

**M15** — On the onset of the word "full", the three plates, all of their
contents and the connector line disappear, and in the same single frame the
video card, its hollow play triangle and the text WATCH THE FULL VIDEO appear
in their place. It is one simultaneous swap, not a removal followed by a
reveal. The off-white field and Dr. Rehan do not change at all. No camera
movement. Hold to the end of the narration.

---

## Motions that were considered and deliberately not written

- No camera move anywhere. Not a slow push, not a Ken Burns drift, not a
  parallax, not a settle. Every well-formed `CAMERA_STATE` row in the brain's
  581 states is in the LOCKED/STATIC family.
- No fade or dissolve anywhere, including on the deletion at M09, where the
  instinct to soften is strongest. The corpus has zero fades across 186
  measured shot boundaries.
- No pulse, beat or throb on the heart, and no motion at all on the response
  arcs. A beating heart would imply a physiological event the narration does
  not describe; animated arcs would imply a live measurement.
- No animation on the caution triangle. The narration hedges ("a bit more
  dangerous"), so the visual hedges too.
- No entrance movement for any character. The corpus never travels a character
  into frame.
