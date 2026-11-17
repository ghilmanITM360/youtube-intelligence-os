# Revised Image-to-Video Decisions — Revision 1

```
I2V_REQUIRED = 0
CAPCUT_MOTIONS = 15
I2V_MOTIONS = 0
```

Unchanged from the first pass in its conclusion, and now better supported: the
three motions that came closest to needing generation — the two curved arrow
draws and, to a lesser extent, the multi-second strike draws — have been
converted to one-frame or few-frame editor operations on direct corpus
evidence, so the closest candidate is now further from the line than it was.

Zero is an acceptable and, for this script, the correct answer. `IMAGE_TO_VIDEO_SYSTEM`
§2 reserves generation for states whose motion cannot be specified as exact
geometry. Every state in this plan can.

## Per-motion determination

| Motion | Operation | Needs generation? | Why not |
|---|---|---|---|
| M01 | Layer group visibility on at a frame | NO | Exact geometry; a generator would redraw the plates and the text |
| M02 | Layer group visibility on | NO | Same |
| M03 | Transparent PNG visibility on | NO | A character appearing is not a character moving |
| M04 | Linear left-to-right wipe mask over a static PNG, 4 frames | NO | The stroke is straight, so the mask is straight. Fully deterministic |
| M05 | Transparent PNG visibility on | NO | Exact position on a shared baseline |
| M06 | Grouped PNG visibility on | NO | The four strokes must be pixel-stable; generation would re-draw them |
| M07 | Transparent PNG visibility on | NO | One mark, one frame, no motion at all |
| M08 | Transparent PNG visibility on | NO | Same as M03 |
| M09 | Grouped visibility off at a frame | NO | A removal is the simplest editor operation that exists |
| M10 | Two-layer grouped visibility on | NO | **Previously the closest I2V candidate.** As a path-following curved draw it had no deterministic editor implementation, which is exactly the condition that would have pushed it toward generation. As a one-frame group reveal — which is what the corpus does with curved arrows — it is trivially deterministic |
| M11 | Four-element grouped visibility on | NO | Same reasoning as M10 |
| M12 | Native text layer visibility on | NO | Text is never generated |
| M13 | Grouped PNG + text visibility on | NO | Exact plate geometry |
| M14 | Grouped PNG + text visibility on | NO | Exact plate geometry |
| M15 | Grouped visibility off + grouped visibility on, same frame | NO | A swap is two opacity switches |

## The closest candidate, and why it still fails the test

In the first pass, the closest candidate was A13 — a curved arrow tracing its
own path while three arcs landed at its head. It was rejected then on
determinism grounds and offered three fallbacks.

In Revision 1 that motion no longer exists in that form. Looking up the brain's
34 arrow motions showed that the corpus does not trace curved arrows at all: the
one directly analogous row is *"Reveal the six red curved arrow strokes toward
the book pages"* at 0.292s / 7 frames — a group reveal. Two more curved-arrow
rows are one-frame changes at 0.042s. So the corpus-faithful treatment and the
deterministic treatment turned out to be the same treatment.

The new closest candidate is **M04**, the 4-frame strike draw, and it is not
close: a straight stroke revealed by a straight wipe is the textbook case for a
mask, not for generation.

## What would have changed this answer

Generation would be the right call if any state required a form to deform,
liquid to behave like liquid, a figure to change pose mid-shot, or a texture to
evolve. Nothing in this script's visual translation requires any of those. If a
future revision introduces, say, coffee actually pouring, that state — and only
that state — would become an I2V candidate.
