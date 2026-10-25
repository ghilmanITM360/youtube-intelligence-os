# Image-to-Video Decisions

Every candidate movement in this Short was evaluated individually. Result:

```
I2V_REQUIRED = 0
CAPCUT_MOTIONS = 17
I2V_MOTIONS = 0
STATIC (cut-entry states with no motion) = 5
```

Per the test protocol §31 this is an acceptable outcome, and it is the outcome
the frozen brain actually points to. It was not forced in either direction.

## The rule applied

`IMAGE_TO_VIDEO_SYSTEM.md` §2 is explicit about which motions have a case for
I2V: only `SEQUENTIAL`, `SIMULTANEOUS_COUPLED`, `SIMULTANEOUS_INDEPENDENT` and
`PERSISTENT_LOOP` motions (203/438, 46% of the corpus) describe a genuine
multi-frame organic progression. `STATE_REPLACEMENT` (230/438, 53%) is by
definition one static illustration discretely swapped for another and
"should remain deterministic image swaps, not I2V-generated."

`DECISION_RULES.md` §7 adds the hard constraint: every one of the corpus's
186 shot boundaries measures a 0.0s gap, and no fade, dissolve or wipe exists
anywhere. I2V generation cannot guarantee an exact frame-accurate end state
or an untouched static anchor — it interpolates. In a video whose entire
grammar is "exact geometry held in a locked frame, changed on a word," that
interpolation is a defect, not a feature.

## Per-motion decision

| Motion | Movement | USE_I2V | Why |
|---|---|---|---|
| A01 | Fork + plate + text appear | NO | Discrete visibility change. Exact line geometry and exact text position required. |
| A02 | Second plate + text appear | NO | Same. Must be pixel-identical in size and stroke to A01's plate — generation would not hold that. |
| A03 | Dr. Rehan appears | NO | Character entry is a one-frame opacity change in the corpus, not a travelled entrance. Nothing moves. |
| A04 | Red strike draws left to right | NO | A wipe mask along a static stroke is exact and repeatable. An I2V "draw" would invent stroke wobble and could not guarantee the final stroke matches the asset. |
| A05 | Can appears on baseline | NO | Discrete object reveal at an exact baseline position. |
| A06 | Four can strokes appear together | NO | They must appear as one countable group with stroke lengths identical to the mug's. Any interpolation would stagger or distort them and break the comparison. |
| A07 | Caution mark appears | NO | One frame, no animation at all. Any I2V treatment (pulse, glow, shake) would overstate a claim the narration hedges. |
| A08 | Patient appears | NO | Same as A03. |
| A09 | Red strike draws left to right | NO | Same as A04, and it must be visibly the *same gesture* as A04 — only a reused asset guarantees that. |
| A10 | Whole binary model removed | NO | An instantaneous deletion. This is the clearest `STATE_REPLACEMENT` in the video and the corpus rule is explicit: deterministic swap. An I2V dissolve would soften the exact beat that must be blunt. |
| A11 | Left arrow draws along its curve | NO | The arrow's endpoints must land exactly on the mug and exactly on the figure's chest. I2V drift at either endpoint breaks the diagram. |
| A12 | Single response arc appears | NO | One frame. |
| A13 | Right arrow draws, three arcs appear | NO | The only motion in the video with a genuinely coupled two-part progression, so the closest thing to an I2V candidate. Still NO: both parts are exact-geometry diagram elements, and the three arcs must be identical in style to the left figure's single arc — the whole argument of the shot rests on the two figures differing *only* in arc count. Generation cannot guarantee that. |
| A14 | Gauge icon + text appear | NO | One frame; text must be exact. |
| A15 | Heart icon + text appear | NO | One frame; the heart must be the same asset drawn in SH01. |
| A16 | Cup icon + text appear | NO | One frame; text must be exact. |
| A17 | Factor list swaps to video card | NO | Instantaneous replacement, `STATE_REPLACEMENT` class, with Dr. Rehan required to stay bit-identical across the swap. |

## Where an I2V case would have existed

If this script had asked for something that plays out continuously — liquid
pouring, a needle sweeping across a dial over time, a figure's posture
changing — `IMAGE_TO_VIDEO_SYSTEM.md` §2 would put those in the `SEQUENTIAL`
or `PERSISTENT_LOOP` bracket and they would be worth generating. The script
contains no such moment. It is a sequence of statements, comparisons and
rejections, and in this corpus's grammar those are drawn, revealed, struck out
and replaced — not simulated.
