# VISUAL 01 — LAYER STACK

Bottom to top. Eight layers. This is the stack Revision 1 specifies; do not
reorder it.

```
Layer 8 — G03   red strike stroke        + linear wipe mask   hidden at start
Layer 7 — C01   Dr. Rehan, arm raised                         hidden at start
Layer 6 — T02   text  BAD?               CapCut text          hidden at start
Layer 5 — G02b  fork right half (line + empty plate)          hidden at start
Layer 4 — T01   text  GOOD?              CapCut text          hidden at start
Layer 3 — G02a  fork left half (line + empty plate)           hidden at start
Layer 2 — IMG01 base plate (mug + heart)                      VISIBLE at start
Layer 1 — E01   flat off-white field                          VISIBLE at start
```

**At the first frame of the video, only layers 1 and 2 are on.** Everything
else is off and switches on later, each on its own spoken word.

## Why this order

| Position | Reason |
|---|---|
| E01 below everything | The one opaque asset in the project. Everything composites over it. It spans the entire timeline, not just this visual |
| IMG01 above E01 | The plate carries mug and heart only. If the plate's off-white does not match E01, the seam shows — sample and match |
| Text above its own plate | `GOOD?` sits on layer 4, directly above G02a on layer 3; `BAD?` on layer 6 above G02b on layer 5. Each label is locked to its plate as a pair |
| C01 above the diagram | He occupies empty lower-left field and overlaps nothing, but sitting above keeps him intact if the fork is nudged |
| G03 on top of all of it | The strike must cross the branch lines and clip the plates visibly. Underneath the diagram it would look like a stray mark behind the drawing |

## Separate exports

**No split export is needed in Visual 01.** Nothing in this shot is ever
removed — every element appears and holds to the cut. IMG01 can be one flat
plate.

The split-export requirement applies to IMG03 and IMG05 in later visuals, where
a group vanishes while the doctor stays. Do not apply it here.

## The one thing that must not be baked

If IMG01 comes back from the generator with fork lines, label plates, text, a
figure or any red in it, **regenerate it.** Compositing the fork into the plate
destroys M01 and M02 — both word-anchored reveals become impossible and the
whole binary would have to be on screen from frame one, which reverses the
argument of the shot.
