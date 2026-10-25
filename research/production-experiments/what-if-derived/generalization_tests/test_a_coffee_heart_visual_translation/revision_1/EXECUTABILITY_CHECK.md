# Executability Check — Revision 1

Every operation in the revised plan, tested against one question: **can the
named tool produce exactly this, repeatably, without a lucky generation?**

## Summary

| | First pass | Revision 1 |
|---|---|---|
| Operations with no deterministic implementation | 2 (A11, A13 curved draws) | **0** |
| Operations relying on a lucky generation | 1 (IMG04's two identical figures) | **0** |
| Operations needing a documented workaround | 2 (SH03 / SH05 partial plate removal, undocumented in the first pass) | 2, **now documented** |
| Motions requiring image-to-video generation | 0 | 0 |

## Resolved

**1. Curved arrow draws (was A11, A13).** CapCut's masks are linear and
shape-based; they do not follow an arbitrary path. A curved stroke revealing
itself along its own curve therefore had no exact implementation, and the first
pass named three fallbacks without choosing one. Resolved by looking up what
the corpus actually does with curved arrows — *"Reveal the six red curved arrow
strokes toward the book pages"*, 0.292s / 7 frames, a group reveal — and
adopting that. The arrows now appear whole in one frame (M10, M11). The
corpus-faithful answer and the buildable answer were the same answer.

**2. Two pixel-identical figures (IMG04).** The first-pass prompt asked an
image model for "two stick figures that are completely identical to each
other", and the entire shot's argument — same coffee, same arrows, only the
arc count differs — fails if they differ at all. Resolved by removing the
figures from the base plate: C03 is generated once as a transparent PNG and the
layer is duplicated in the editor with a changed X position. Identity is now
structural rather than hoped for.

**3. Strike stroke timing (was A04, A09).** Not an executability problem but a
pacing one: a wipe mask animated across half a second is trivially buildable
and wrong. Retimed to 4 frames on measured corpus durations (0.125–0.208s).

## Still requires a workaround — now written down

**Partial removal from a shared base plate (SH03 and SH05).** In both shots the
doctor and a removable group are drawn in the same base image, but only the
group is removed. A single opacity switch would take the doctor with it.

Fix, specified in `REVISED_CAPCUT_BUILD.md`: export each of those two base
images as two files at the same canvas size — a base carrying the off-white
field and the doctor, and a transparent-background file carrying just the
removable group. Switch off only the group.

This is not a compromise. It is what the asset spec already implies by calling
G06 and G09 single removable groups, and the first pass simply never said how
to build it. Cost: two extra exports and two extra layers.

## Verified buildable as specified

| Operation class | Count | Tool mechanism |
|---|---|---|
| Layer / group visibility on at a frame | 10 | Opacity or visibility switch |
| Group visibility off at a frame | 1 | Same |
| Simultaneous off + on at one frame | 1 | Two switches on the same frame |
| Coupled multi-layer reveal at one frame | 5 | Grouped layers, one switch |
| Linear wipe mask, 4 frames | 1 | Standard linear mask animation |
| Native text layers | 6 | Editor text |
| Butt cuts between shots | 4 | No transition effect applied |
| Camera moves | 0 | — |
| Generated video clips | 0 | — |

(Counts overlap because coupled reveals are also visibility switches.)

## Residual risks — no fix applied, stated for the reviewer

1. **All timings are ESTIMATED.** Every duration in this plan derives from
   3.93 words/sec, the measured portrait-subcorpus rate. Real narration will
   differ, and a slower hook in particular would relieve SH01's density.
   Nothing in the plan depends on the estimate being right — every operation is
   anchored to a word onset, not to a clock time — but the per-shot density
   figures in `REVISED_SHOT_PLAN.csv` will move once the audio exists. They
   must be recomputed against the real track before anyone judges pacing.

2. **SH01 and SH05 exceed the corpus's 90th-percentile reveal rate.** SH01 runs
   an estimated 1.16 states/sec and SH05 0.82, against a portrait p90 of 0.67.
   Both are driven by the script's own word density — SH01 names four concepts
   in 17 words, SH05 names three in six — not by added decoration. No cut was
   made for this, because every state in both shots fires on a distinct concept
   word. This is the single most likely thing a human reviewer will disagree
   with, and the disagreement would be reasonable.

3. **Hand-drawn consistency across five separately generated plates.** The five
   base images are generated independently and must share line weight, stroke
   character and off-white value. Generation variance is a real risk that no
   prompt wording fully removes. Mitigation, unapplied: generate all five in
   one session with a fixed seed where the tool allows, and re-generate the
   whole set rather than one plate if any drifts.

4. **The mug appears at four different scales** (IMG01 large, IMG02 standing,
   IMG03 small, IMG04 small, and repeated three times in G12). If generated
   independently each time, the handle side, taper and brown band height will
   drift. Mitigation, unapplied: draw the mug once and rescale it, treating it
   as the recurring asset the asset table already says it is.

5. **Text legibility at 0.5s.** `BLOOD PRESSURE` holds for an estimated half a
   second before the next plate fills. Removing the gauge icon helps — the text
   now has the whole plate — but a 14-character phrase at that duration is the
   plan's tightest reading demand. Verify on an actual phone, not on a desktop
   preview.
