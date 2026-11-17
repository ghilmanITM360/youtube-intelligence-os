# Revised CapCut Build — Revision 1

Every operation below is deterministic: a layer becomes visible or invisible at
a named frame, or a linear wipe mask travels across a static layer. There are
no keyframed transforms, no camera moves, no transitions between shots other
than plain cuts, and no generated video.

**Global project settings**

- Canvas 2160 × 3840, 9:16.
- Import the narration (AU01) first and lock it. Every visual operation is
  placed against a word onset in that waveform, never against a clock time.
- No transition effect is applied at any shot boundary. Shots butt-cut.
- Background layer E01 (off-white) spans the whole timeline.

**Anchor-word workflow.** Scrub the narration, find the onset frame of the
anchor word, and place the operation on that frame. The brain's measured
STATE_CHANGE offset from the anchor word is a median of 37 ms, which at 24 fps
is within one frame — so "on the onset frame" is the correct instruction and no
offset padding should be added.

## What changed from the first pass

1. **The SH03 red strike is gone.** Delete that layer and its wipe mask from
   the SH03 stack entirely.
2. **The SH03 deletion moves earlier**, from the onset of "That's" to the onset
   of "not".
3. **Both SH04 arrow wipe masks are gone.** The arrows are now plain visibility
   switches. This removes the only two operations in the first pass that CapCut
   could not execute as specified.
4. **SH04's two figures are now a duplicated layer**, not part of the base
   plate.
5. **The SH05 gauge layer is gone.** The top plate is a text layer only.
6. **M04's wipe mask is retimed** from roughly half a second to 4 frames.

---

## SH01 — IMG01 — 5 states, 4 motions

Track stack, bottom to top:

1. E01 off-white field
2. IMG01 base plate (mug + heart)
3. G02a fork-left group (left branch + left plate)
4. T01 text `GOOD?`
5. G02b fork-right group (right branch + right plate)
6. T02 text `BAD?`
7. C01 Dr. Rehan, arm-raised pose
8. G03 strike stroke + linear wipe mask

Initial composition at the first frame: layers 1–2 visible, layers 3–8 hidden.

| On word onset | Operation |
|---|---|
| "good" (w3) | Layers 3 and 4 visible in the same frame |
| "bad" (w7) | Layers 5 and 6 visible in the same frame |
| "Rehan" (w11) | Layer 7 visible |
| "wrong" (w16) | Layer 8 visible, and its wipe mask animates left → right over **4 frames only**, then holds |

Hold the finished frame to the cut.

---

## SH02 — IMG02 — 4 states, 3 motions

1. E01 off-white field
2. IMG02 base plate (baseline + mug + the mug's two strokes)
3. O02 can
4. G04b the can's four-stroke group
5. G05 caution triangle

Initial composition: layers 1–2 visible, 3–5 hidden.

| On word onset | Operation |
|---|---|
| "energy" (w26) | Layer 3 visible |
| "stronger" (w35) | Layer 4 visible — one grouped layer, so the four strokes cannot stagger |
| "dangerous" (w44) | Layer 5 visible. No effects, no keyframes, no pulse |

Hold to the cut.

---

## SH03 — IMG03 — 3 states, 2 motions

1. E01 off-white field
2. IMG03 base plate (doctor + compact binary diagram)
3. T01 text `GOOD?` (repositioned for this shot)
4. T02 text `BAD?` (repositioned for this shot)
5. C02 patient

Initial composition: layers 1–4 visible, layer 5 hidden.

| On word onset | Operation |
|---|---|
| "patients" (w53) | Layer 5 visible. Then **nothing happens for roughly 4.3 seconds ESTIMATED** — do not add anything to fill this hold |
| "not" (w70) | The diagram must vanish while the doctor stays. See the note below |

**How to delete the diagram while keeping the doctor.** The doctor and the
diagram arrive in the same base plate, so a plain opacity switch on layer 2
would remove him too. Two acceptable builds, in order of preference:

- *Preferred.* Export IMG03 as two files at the same canvas size: `IMG03_base`
  (off-white + doctor only) and `IMG03_diagram` (the diagram group on
  transparency). Stack the diagram above the base and switch only the diagram
  off at "not". This is also what makes the diagram group a single removable
  object, which the asset spec already calls for.
- *Fallback.* Keep the single plate and place a second, doctor-only PNG above
  it; switch the full plate off and the doctor-only PNG on in the same frame.
  Mechanically identical result, one more layer.

Hold the emptied frame to the cut, through "That's a wrong question."

---

## SH04 — IMG04 — 3 states, 2 motions

1. E01 off-white field
2. IMG04 base plate (mug + baseline, no figures)
3. C03 figure — instance A, positioned x14–36%
4. C03 figure — instance B, the **same layer duplicated**, positioned x64–86%
5. G07a left arrow
6. G08a single arc
7. G07b right arrow
8. G08b three-arc group

Initial composition: layers 1–4 visible, 5–8 hidden.

| On word onset | Operation |
|---|---|
| "respond" (w89) | Layers 5 and 6 visible in the same frame |
| "judge" (w100) | Layers 7 and 8 visible in the same frame |

No masks. No keyframes. Hold to the cut through "or 'bad.'"

**Duplicate, do not re-import.** Copy the layer in the timeline and change only
its X position. If the two figures come from two files they will not match, and
the shot's whole argument depends on them matching.

---

## SH05 — IMG05 — 5 states, 4 motions

1. E01 off-white field
2. IMG05 base plate (doctor + three empty plates + connector line)
3. T03 text `BLOOD PRESSURE`
4. G11 heart icon
5. T04 text `HEART RESPONSE`
6. G12 three-cup icon
7. T05 text `QUANTITY`
8. G13 video card + play mark
9. T06 text `WATCH THE FULL VIDEO`

Initial composition: layers 1–2 visible, 3–9 hidden.

| On word onset | Operation |
|---|---|
| "blood" (w111) | Layer 3 visible. **Nothing else** — there is no gauge icon in Revision 1 |
| "heart" (w113) | Layers 4 and 5 visible in the same frame |
| "quantity" (w116) | Layers 6 and 7 visible in the same frame |
| "full" (w124) | In one frame: the plate column and everything in it goes invisible, and layers 8 and 9 become visible |

**The same split-plate problem as SH03 applies here**, for the same reason: the
doctor and the plate column arrive in one base image and only the column is
removed. Export IMG05 as `IMG05_base` (off-white + doctor) plus
`IMG05_plates` (the three plates and connector on transparency), and switch off
only the plates group at "full", together with layers 3–7.

Hold to the end of the narration.

---

## Build order

1. Import and lock the narration. Mark the onset frame of all 19 anchor words.
2. Place E01 across the whole timeline.
3. Generate and import the five base plates, splitting IMG03 and IMG05 into
   base + removable-group files as described above.
4. Generate and import the ten transparent overlays.
5. Create the six native text layers. Use one text style for all six.
6. Lay out the five shots as butt cuts with no transition effects.
7. Per shot, build the layer stack bottom-up and set the initial visibility.
8. Place every visibility switch on its marked anchor frame.
9. Build the single wipe mask (M04) and set it to 4 frames.
10. Review once at phone size with sound, checking only that each change lands
    on its word and that nothing moves that was not listed as moving.

## Nineteen anchor words

`good` · `bad` · `Rehan` · `wrong` · `People` · `energy` · `stronger` ·
`dangerous` · `So` · `patients` · `not` · `The` · `respond` · `judge` ·
`Dr.` · `blood` · `heart` · `quantity` · `full`

That is 19 reveal/cut anchors plus the video's first frame. The first pass
listed 21; `That's` (w77) is no longer an anchor because the deletion moved to
`not`, and `caffeine` (w91) is no longer an anchor because that reveal merged
into `respond`.
