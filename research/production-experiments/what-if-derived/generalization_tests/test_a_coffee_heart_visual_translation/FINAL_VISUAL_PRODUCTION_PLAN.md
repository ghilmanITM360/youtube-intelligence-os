# Final Visual Production Plan — Coffee / Heart Short

**Everything needed to build this Short is in this one document.**

| | |
|---|---|
| Format | 9:16 vertical, 2160 × 3840 |
| Script | unchanged, verbatim, 130 words |
| Estimated runtime | 33.1s ESTIMATED (130 ÷ 3.93 words/sec, the measured rate of the frozen corpus's 8 portrait videos). No measured timings exist — nothing here is a real timestamp. |
| Shots | 5 |
| Base images to generate | 5 |
| Visual states | 22 |
| Motions | 17, all CapCut |
| Image-to-video generations | 0 |
| Transitions | 5 hard cuts, no fades anywhere |
| Camera | locked for the entire video |
| Visual grammar source | frozen Production Intelligence Brain v1.0.0 only |

---

## Before you start: the visual language, once

Written out here so no prompt below has to say "xkcd style".

**Canvas.** Flat off-white full-frame field. No texture, gradient, vignette,
border or panel. One visual idea per frame, large forms, generous empty space.

**Line.** Simple thin black hand-drawn linework, slightly imperfect and
naturally uneven, uniform weight throughout, flat 2D, no perspective, no
shading, no lighting, no drop shadows.

**Figures.** Minimal stick figures. Plain round circle heads. No faces at all,
except Dr. Rehan, who is identified by exactly three cues: two small
rectangular spectacle lenses joined by a bridge, a short solid beard arc under
the chin, and one short side-swept hair stroke on top. He reads as "a doctor",
not as a likeness of anyone.

**Colour, strictly rationed.**
- **Coffee brown** — only ever the liquid band inside a cup.
- **Muted medical red** — only on the two strike strokes, the one caution
  triangle, and the response arcs. Nothing else is red, ever.
- **Light neutral grey** — available but not used in this plan; nothing needed it.
- No red is generated into any base image. All red arrives as an editor overlay.

**Motion.** Elements pop on in a single frame, or a stroke draws itself along
its own path. Nothing fades, scales, slides, rotates, pulses or glows. The
camera never moves.

**Text.** No image prompt asks for a single letter. Every word in the finished
video is a CapCut native text layer.

*Brain basis: `VISUAL_DNA.md` (89.8% LOCKED/STATIC camera), `MOTION_DNA.md`
(instant/<0.5s is the largest motion bucket), `DECISION_RULES.md` §7 (zero
fades across 186 corpus shot boundaries), `ASSET_CREATION_SYSTEM.md`
(CHARACTER 96% transparent PNG; TEXT_SYSTEM = native editor text layers).*

**Medical guardrails applied throughout (web-verified, not brain-derived).**
No blood-pressure numbers, no caffeine milligrams, no dose thresholds, no
diagnoses, no ECG or arrhythmia traces, no disease labels, no skull, death
icon, flatline, exploding heart or emergency-red frame. The energy-drink
section gets exactly one outline caution triangle over one object, because the
narration says "a bit more dangerous", not "dangerous". Coffee is never shown
as universally good or universally bad. Independently consistent with
[AHA: Caffeine and Heart Disease](https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/nutrition-basics/caffeine-and-heart-disease)
and [AHA: energy drinks and blood pressure](https://www.heart.org/en/news/2019/05/29/energy-drinks-may-provide-jolt-to-heart-function-blood-pressure),
which describe higher-caffeine products as raising risk of high blood pressure
or irregular rhythm, and describe caffeine response as varying by genetics,
metabolism, age and prior use — i.e. the script's own central claim.

---

# VISUAL 01 — The binary question

**Narration.** "Is coffee good for your heart—or bad for it? Dr. Rehan says
that's actually the wrong question." (words 1–17, ~4.3s ESTIMATED)

**Purpose.** Draw the good/bad model completely, so that the doctor has
something real to reject. The rejection only lands if the viewer owns the
model first.

**Base image.** IMG01 — new. Supports all 5 states of this shot.

**Exact frame description (the plate).** Flat off-white 9:16 field. A
line-drawn coffee mug, side view, handle on the right, at x36–64%, y18–30%,
with a flat coffee-brown band inside its top rim. Directly beneath it a
single-stroke outline heart at x42–58%, y34–43%. Everything below y44% empty.

**Assets.** E01 background · O01 mug · G01 heart · G02a fork+left plate ·
G02b right plate · C01 Dr. Rehan (arm raised) · G03 red strike stroke ·
T01 `GOOD?` · T02 `BAD?`

**Image prompt (IMG01).**

> A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat
> off-white background. Simple thin black hand-drawn linework with slightly
> imperfect, naturally uneven strokes. Flat 2D, no perspective, no shading,
> no texture, no gradient, no shadow.
>
> Centred in the upper third of the frame, spanning 36–64% of the image width
> and 18–30% of the image height, draw a simple coffee mug seen from the side:
> a plain tapered cup body with a single round handle on its right side. Inside
> the top of the mug, fill a flat coffee-brown horizontal band representing the
> coffee surface — this brown band is the only colour in the entire image.
>
> Directly below the mug, spanning 42–58% of the width and 34–43% of the height,
> draw a single-stroke symmetrical outline heart in the same thin black line.
> The heart is a plain outline only, not filled, not anatomical, no highlights.
>
> Everything below 44% of the image height is completely empty off-white. Leave
> it empty. The mug and the heart are the only two objects in the picture.
>
> Do NOT include: any text, letters, numbers, words or labels; any arrows,
> lines, branches or connectors; any people or figures; any additional cups,
> cans, hearts or icons; any speech bubbles; any question marks; any border,
> panel or background shape; any red; any colour other than the single brown
> coffee band.

**Initial state (F01.0).** Plate only — mug and heart, lower two-thirds empty.
Hold ~0.5s.

**State changes.**
| State | On | What appears |
|---|---|---|
| F01.1 | onset of "good" (w3) | Two thin fork lines descend from the heart's point at x50%,y44% to x18%,y56% and x82%,y56%. A blank rounded label plate at x10–40%, y56–66%, with `GOOD?` text inside it. |
| F01.2 | onset of "bad" (w7) | An identical blank plate at x60–90%, y56–66%, with `BAD?` text inside it. Model now symmetrical. |
| F01.3 | onset of "Rehan" (w11) | Dr. Rehan stick figure at x8–30%, y70–95%, facing right, near arm raised toward the fork. |
| F01.4 | onset of "wrong" (w16) | One thick muted-red hand-drawn stroke crosses the whole fork from x14%,y68% to x86%,y52%, cutting both branches and clipping both plate tops. |

**Animation 1 (A01).** The fork lines, the left label plate and the GOOD? text become visible together in a single frame. Everything else — coffee mug, heart, background, camera — stays completely static.

**Animation 2 (A02).** The right label plate and the BAD? text become visible together in a single frame. The mug, heart, fork lines, left plate and its text stay completely static. No camera movement.

**Animation 3 (A03).** The doctor figure becomes visible in the lower-left field in a single frame, already in final position — no walk-in, no slide, no scale-up. The entire binary diagram above him stays completely static. No camera movement.

**Animation 4 (A04).** The red stroke draws itself on progressively from its lower-left end to its upper-right end, revealed by a wipe along its own path, over roughly 0.5 seconds. The mug, heart, fork, both plates, both text labels and Dr. Rehan stay completely static. No camera movement.

**Static elements (every state).** Off-white field, coffee mug, heart, camera.
From F01.1 also the fork and left plate; from F01.2 also the right plate; from
F01.3 also Dr. Rehan.

**Narration triggers.** w3 "good" · w7 "bad" · w11 "Rehan" · w16 "wrong".
All on word onset.

**Transition out.** Hard cut after "question." (w17). No transition effect.

**Reuse instructions.** O01 (mug) is reused in VISUAL 02, 03 and 04 — draw it
once. G01 (heart) returns in VISUAL 05's middle list plate — draw it once.
G03 (red strike) is reused verbatim in VISUAL 03; that repetition is
deliberate, so use the same file. T01/T02 return in VISUAL 03.

**CapCut / I2V.** All four motions CapCut. I2V: none — every change is a
discrete visibility switch or a masked stroke reveal, and the fork geometry
must be exact.

**Notes.** The plates are blank in the generated image on purpose. Do not let
an image model write GOOD? or BAD?.
*Brain basis: `MOTION_DNA.md` instant-reveal dominance; `MASTER_MOTIONS`
"Draw red strike for line 1/2" is a real corpus motion using red
strike-through as a rejection mark; `AUDIO_VISUAL_SYNC_DNA.md` STATE_CHANGE
median offset 37ms.*

---

# VISUAL 02 — Coffee versus energy drink

**Narration.** "People usually ask me, then what about the energy drinks? So,
energy drinks for me are much stronger than coffee and they are a bit more
dangerous than coffee as well." (words 18–48, ~7.9s ESTIMATED)

**Purpose.** Compare two physical containers on one shared measure, then add
caution to one of them. This is the only side-by-side object comparison in the
video, and it never touches the heart, the doctor or the fork.

**Base image.** IMG02 — new. Supports all 4 states of this shot.

**Exact frame description (the plate).** Flat off-white 9:16 field. A thin
horizontal baseline across x8–92% at y70%. A coffee mug standing on its left
portion at x14–40%, y52–70%, brown band inside the rim. Two short black
radiating strokes above the mug at x20–34%, y42–50%, equal length, evenly
spaced. The right half of the baseline bare; everything above y42% empty.

**Assets.** E01 background · O01 mug · G04 stimulation strokes (2-group baked
into the plate, 4-group as an overlay) · O02 energy-drink can · G05 caution
triangle.

**Image prompt (IMG02).**

> A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat
> off-white background. Simple thin black hand-drawn linework with slightly
> imperfect, naturally uneven strokes. Flat 2D, no perspective, no shading,
> no texture, no gradient, no shadow.
>
> Draw one thin horizontal black line across the frame from 8% to 92% of the
> width, positioned at 70% of the image height. This is a plain ground line —
> no ticks, no arrowheads, no labels.
>
> Standing on the left portion of that line, spanning 14–40% of the width and
> 52–70% of the height, draw a simple coffee mug seen from the side: a plain
> tapered cup body with a single round handle on its right. Inside the top of
> the mug, fill a flat coffee-brown horizontal band representing the coffee
> surface — this brown band is the only colour in the entire image.
>
> Above the mug, spanning 20–34% of the width and 42–50% of the height, draw
> exactly two short straight black strokes radiating upward and slightly
> outward, evenly spaced, both the same length, in the same hand-drawn weight.
>
> The right half of the ground line, from about 50% to 92% of the width, is
> completely bare — nothing stands on it. The entire field above 42% of the
> height is completely empty off-white. Leave both empty.
>
> Do NOT include: any text, letters, numbers or labels; any can, bottle,
> tin or second container; any people or figures; any hearts, arrows,
> warning signs or exclamation marks; any additional strokes beyond the two
> specified; any border or panel; any red; any colour other than the single
> brown coffee band.

**Separate overlay prompt (O02, the can).**

> A tall plain beverage can on a fully transparent background, thin black
> hand-drawn linework with slightly uneven strokes, flat 2D, no shading.
> Straight cylindrical body, rounded top rim with a small oval pull-tab, one
> plain horizontal band across the middle, completely blank sides. No logo, no
> brand name, no lettering, no numbers, no graphics, no colour fill, no
> background, no shadow. It must not resemble any real product.

**Initial state (F02.0).** Coffee alone on the baseline with its two strokes
already visible — they are the unit of measure the can will be counted
against. Hold ~2.0s.

**State changes.**
| State | On | What appears |
|---|---|---|
| F02.1 | onset of "energy" (w26) | The tall unbranded can stands on the same baseline at x60–86%, y44–70%. Visibly taller than the mug. |
| F02.2 | onset of "stronger" (w35) | Four black radiating strokes above the can at x62–84%, y28–42% — same stroke length as the mug's two, four of them, sitting higher. |
| F02.3 | onset of "dangerous" (w44) | One muted-red outlined caution triangle with an exclamation stroke at x66–80%, y14–25%, above the can only. |

**Animation 1 (A05).** The can becomes visible standing on the right of the baseline in a single frame, already in final position and scale. The mug, its two strokes and the baseline stay completely static. No camera movement.

**Animation 2 (A06).** All four strokes above the can become visible together in a single frame — they do not appear one by one and they do not grow. The can, the mug and the mug's two strokes stay completely static. No camera movement.

**Animation 3 (A07).** The red caution triangle becomes visible above the can in a single frame. It does not pulse, flash, shake or scale. The can, mug and both stroke groups stay completely static. No camera movement.

**Static elements.** Off-white field, baseline, coffee mug, the mug's two
strokes, camera — in every state. From F02.1 also the can; from F02.2 also the
can's strokes.

**Narration triggers.** w26 "energy" · w35 "stronger" · w44 "dangerous".

**Transition out.** Hard cut after "as well." (w48).

**Reuse instructions.** O01 is the same mug file as VISUAL 01, re-scaled. G04's
single stroke must be the same drawing duplicated into the 2-group and the
4-group — identical stroke length is what makes the comparison countable
rather than decorative.

**CapCut / I2V.** All three motions CapCut. I2V: none.

**Notes.** The can must stay generic. The caution mark is outline-only, appears
once, over one object, with nothing above the mug — that asymmetry is the whole
claim, and it is as far as the narration goes.
*Brain basis: `MASTER_MOTIONS` reveals coupled elements together in one frame
("Droplet and temperature text appear together"); `VISUAL_DNA.md` compares by
revealing a second annotated group beside an existing one.*

---

# VISUAL 03 — The consultation, the rejection, the deletion

**Narration.** "So now, if the patients ask me, so is coffee good or bad for
your health? I tell them that should not be the question to be asked. That's a
wrong question." (words 49–80, ~8.1s ESTIMATED)

**Purpose.** Bring the binary back inside a real consultation, strike it out in
front of the person who asked, then delete it entirely. The empty space this
leaves is the argument.

**Base image.** IMG03 — new. Supports all 4 states of this shot.

**Exact frame description (the plate).** Flat off-white 9:16 field. Dr. Rehan
standing at x6–28%, y58–92%, facing right, arms down. Upper centre: a small
coffee mug at x44–56%, y14–23% with a brown band; two thin lines descending
from it to two blank rounded plates at x24–46% and x54–76%, y34–44%. Plate
interiors blank. The whole right side below y50% empty.

**Assets.** E01 background · C01 Dr. Rehan (arms-down pose) · O01 small mug ·
G06 compact fork group · T01 `GOOD?` · T02 `BAD?` · C02 patient · G03 red
strike stroke.

**Image prompt (IMG03).**

> A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat
> off-white background. Simple thin black hand-drawn linework with slightly
> imperfect, naturally uneven strokes. Flat 2D, no perspective, no shading,
> no texture, no gradient, no shadow.
>
> On the left, spanning 6–28% of the width and 58–92% of the height, draw a
> minimal stick figure of a male doctor standing and facing to the right: a
> plain round head drawn as a simple circle outline, two small rectangular
> spectacle lenses joined by a short bridge across the middle of the head, a
> short solid black beard drawn as a small filled arc under the chin, one short
> curved side-swept hair stroke across the top of the head, a single-stroke
> straight body line, two simple straight arms hanging at his sides and two
> simple straight legs. No mouth, no eyes, no nose, no ears, no facial detail
> beyond the glasses and beard. No coat, no stethoscope, no clipboard.
>
> In the upper centre of the frame, draw a small simple diagram. At the top,
> spanning 44–56% of the width and 14–23% of the height, a small coffee mug
> seen from the side with a handle on its right and a flat coffee-brown
> horizontal band inside its top rim — this brown band is the only colour in
> the entire image. From the bottom of that mug, two thin straight black lines
> descend outward, one left and one right, each ending at the top edge of a
> rounded-rectangle plate. The left plate spans 24–46% of the width and 34–44%
> of the height; the right plate spans 54–76% of the width and the same height
> band. Both plates are thin black outlines with completely empty interiors.
>
> The entire right-hand side of the frame below 50% of the height is completely
> empty off-white. Leave it empty.
>
> Do NOT include: any text, letters, numbers, words, labels, check marks or
> crosses inside or near the plates — the plate interiors must be completely
> blank; any second person or patient figure; any speech bubbles; any strike,
> slash or cross-out stroke; any hearts, cans or warning signs; any border or
> panel; any red; any colour other than the single brown coffee band.

**Separate overlay prompt (C02, the patient).**

> Minimal stick figure of a person on a fully transparent background, thin
> black hand-drawn linework with slightly uneven strokes, flat 2D, no shading.
> Plain round circle head with no face at all — no glasses, no beard, no hair,
> no features. Single-stroke body, simple straight legs; the near arm is
> slightly raised as if asking a question. Facing left. No clothing detail, no
> text, no colour, no background, no shadow.

**Initial state (F03.0).** Doctor left, labelled fork upper-centre (the
`GOOD?`/`BAD?` text is already on the plates here — this is a recall of a model
already taught in VISUAL 01, not a new reveal), right field empty. Hold ~1.0s.

**State changes.**
| State | On | What appears / disappears |
|---|---|---|
| F03.1 | onset of "patients" (w53) | Patient stick figure at x72–94%, y60–92%, facing left. Then **hold with no change for ~4.3s** while the whole question is spoken. |
| F03.2 | onset of "not" (w70) | One thick muted-red stroke crosses the compact fork from x20%,y46% to x80%,y30%. Neither figure is touched by it. |
| F03.3 | onset of "That's" (w77) | The mug, both branch lines, both plates, both text labels **and the red stroke** all disappear in one frame. Upper centre goes to bare off-white. Two figures, a large empty field between them. |

**Animation 1 (A08).** The patient figure becomes visible in the right field in a single frame, already in final position — no entrance movement. Dr. Rehan and the binary diagram stay completely static. No camera movement.

**Animation 2 (A09).** The red stroke draws itself on progressively from its lower-left end to its upper-right end, revealed by a wipe along its own path, over roughly 1.0 second. Both figures, the diagram, the plates and their text stay completely static. No camera movement.

**Animation 3 (A10).** The mug, both branch lines, both plates, both text labels and the red stroke all disappear together in a single frame, leaving empty off-white. No fade, no shrink, no slide-off. Dr. Rehan and the patient stay completely static. No camera movement.

**Static elements.** Off-white field, Dr. Rehan, camera — in every state. From
F03.1 also the patient.

**Narration triggers.** w53 "patients" · w70 "not" · w77 "That's".

**Transition out.** Hard cut after "question." (w80), from the emptied frame.

**Reuse instructions.** C01 is the same Dr. Rehan figure as VISUAL 01 in a
different pose. G03 is the *same* red stroke file as A04 — reuse it so the
second rejection reads as the same gesture. T01/T02 are the same text layers.
The whole fork must be one grouped layer so A10 can delete it in one frame;
if it is baked into the plate instead, prepare a second plate with the diagram
erased and cut to it.

**CapCut / I2V.** All three motions CapCut. I2V: none — A10 in particular must
be an instantaneous deletion; the corpus contains zero fades and a dissolve
would soften the one beat that has to be blunt.

**Notes.** The 4.3s static hold at F03.1 is deliberate, not an oversight. The
corpus's longest-held recurring state class averages 7.25s, and long static
holds under continuous narration are normal in this grammar.
*Brain basis: `DECISION_RULES.md` §3 (STATE_REPLACEMENT 230/438, 53%) and §7
(zero fades); `VISUAL_DNA.md` (Locked states avg 7.25s).*

---

# VISUAL 04 — Coffee to two people

**Narration.** "The real question is, how does your body respond to caffeine or
coffee? And that's the main message: don't judge coffee only as “good” or
“bad.”" (words 81–106, ~6.6s ESTIMATED)

**Purpose.** The pivot. The reading moves off the cup and onto the person —
then a second, identical person gets a different reading from the same cup.
That picture *is* the main message.

**Base image.** IMG04 — new. Supports all 4 states of this shot.

**Exact frame description (the plate).** Flat off-white 9:16 field. One coffee
mug centred at the top, x42–58%, y12–22%, brown band inside the rim. A thin
baseline across x10–90% at y80%. Two completely identical faceless stick
figures standing on it: left at x14–36%, y52–80%, right at x64–86%, y52–80%,
both facing forward, indistinguishable in height, build and posture. The band
between y24% and y50% entirely empty.

**Assets.** E01 background · O01 mug · C03 the two identical figures (drawn
into the plate so they are guaranteed identical) · G07a/G07b connector arrows ·
G08a single response arc · G08b three stacked response arcs.

**Image prompt (IMG04).**

> A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat
> off-white background. Simple thin black hand-drawn linework with slightly
> imperfect, naturally uneven strokes. Flat 2D, no perspective, no shading,
> no texture, no gradient, no shadow.
>
> Centred at the top of the frame, spanning 42–58% of the width and 12–22% of
> the height, draw a simple coffee mug seen from the side with a single round
> handle on its right, and a flat coffee-brown horizontal band inside its top
> rim — this brown band is the only colour in the entire image.
>
> Draw one thin horizontal black line across the frame from 10% to 90% of the
> width, positioned at 80% of the image height, as a plain ground line with no
> ticks and no labels.
>
> Standing on that line, draw two stick figures that are completely identical
> to each other in size, proportion, posture and line weight. The left figure
> spans 14–36% of the width and 52–80% of the height; the right figure spans
> 64–86% of the width and the same height band. Each is a plain round head
> drawn as a simple circle outline with no face at all, a single-stroke
> straight body line, two simple straight arms hanging at the sides and two
> simple straight legs. Both face forward. They must be indistinguishable from
> one another — no difference in height, build, hair, clothing or expression.
>
> The entire horizontal band between 24% and 50% of the image height, across
> the full width, is completely empty off-white. Leave it empty.
>
> Do NOT include: any text, letters, numbers or labels; any arrows, curves,
> lines or connectors between the mug and the figures; any marks, arcs, waves
> or symbols on or near either figure's chest; any hearts, cans, plates or
> icons; any third figure; any difference between the two figures; any border
> or panel; any red; any colour other than the single brown coffee band.

**Separate overlay prompts.**

> **G07 arrow —** One thin hand-drawn curved arrow in black on a fully
> transparent background, a single smooth curve with slightly uneven weight,
> ending in a small open V arrowhead. Flat 2D, no shading. No text, no colour,
> no double line, no background, no shadow.

> **G08 response arcs —** Short concentric arc strokes in muted medical red on
> a fully transparent background, drawn in the style of a single hand-drawn
> sound-wave mark, thin and slightly uneven. Produce two versions: one
> containing a single arc, and one containing three arcs stacked at increasing
> radius. No text, no numbers, no waveform trace, no heartbeat line, no
> background, no shadow.

**Initial state (F04.0).** One mug, two identical people, nothing decided.
Hold ~2.0s.

**State changes.**
| State | On | What appears |
|---|---|---|
| F04.1 | onset of "respond" (w89) | A thin curved arrow from the mug at x44%,y23% down-left to the left figure's chest at x28%,y58%, small open arrowhead. |
| F04.2 | onset of "caffeine" (w91) | One small muted-red arc at the left figure's chest, x22–30%, y58–63%. One arc only. |
| F04.3 | onset of "judge" (w100), arcs landing on "“good”" (w104) | A second arrow from the mug at x56%,y23% down-right to the right figure's chest at x72%,y58%, **and** three stacked red arcs at x70–80%, y55–65%. The figures now differ in exactly one respect: arc count. |

**Animation 1 (A11).** The arrow draws itself on progressively along its curve, from the mug down and to the left, arriving at the left figure's chest, over roughly 0.4 seconds. The mug, both figures and the baseline stay completely static. No camera movement.

**Animation 2 (A12).** The single red arc becomes visible at the left figure's chest in a single frame. It does not pulse or repeat. The mug, both figures and the left arrow stay completely static. No camera movement.

**Animation 3 (A13).** The right arrow draws itself on progressively along its curve from the mug down and to the right over roughly 0.4 seconds; the moment it lands, all three red arcs become visible together at the right figure's chest in a single frame. The mug, both figures, the left arrow and the left figure's single arc stay completely static. No camera movement.

**Static elements.** Off-white field, baseline, mug, both figures, camera — in
every state. From F04.1 also the left arrow; from F04.2 also the left arc.

**Narration triggers.** w89 "respond" · w91 "caffeine" · w100 "judge" →
w104 "“good”".

**Transition out.** Hard cut after "“bad.”" (w106).

**Reuse instructions.** O01 is the same mug again. G07 is one arrow drawing,
mirrored for the right side. G08's single arc must be the exact same stroke
used three times in the 3-arc version.

**CapCut / I2V.** All three motions CapCut. I2V: none. A13 is the closest thing
to an I2V candidate in the whole video — a genuinely coupled two-part
progression — and it is still CapCut, because the arrow endpoints must land
exactly and the three arcs must be stylistically identical to the left
figure's one. The entire argument rests on the two figures differing *only* in
arc count, which generation cannot guarantee.

**Notes.** The arcs are unlabelled response markers. No numbers, no units, no
ECG trace, no heartbeat line, no diagnosis on either figure. Neither figure is
"the healthy one" or "the sick one" — one simply reads higher than the other.
*Brain basis: `MASTER_MOTIONS` ACTION="ADD/DRAW"; `IMAGE_TO_VIDEO_SYSTEM.md` §2
(exact diagram geometry stays deterministic); `DECISION_RULES.md` §3
(SIMULTANEOUS_COUPLED, 36 motions).*

---

# VISUAL 05 — Three factors, then the CTA

**Narration.** "Dr. Rehan explains what blood pressure, heart response and
quantity have to do with it in the full video. Watch it on the channel."
(words 107–130, ~6.1s ESTIMATED)

**Purpose.** Name the three factors one at a time, then hand off to the full
video without leaving the visual language.

**Base image.** IMG05 — new. Supports all 5 states of this shot, including the
CTA.

**Exact frame description (the plate).** Flat off-white 9:16 field, no colour
at all. Dr. Rehan standing at x66–92%, y58–92%, facing left, arms down. Three
identical blank rounded plates stacked on the left, all x8–58%, at y20–30%,
y36–46% and y52–62%, interiors completely empty. A thin vertical connector
line at x12% from y25% to y57% linking their left edges. Lower left empty.

**Assets.** E01 background · C01 Dr. Rehan (arms-down, facing left) · G09
three blank plates + connector · G10 gauge icon · G11 heart icon (reused G01) ·
G12 three-cup icon · G13 video card + play mark · T03 `BLOOD PRESSURE` ·
T04 `HEART RESPONSE` · T05 `QUANTITY` · T06 `WATCH THE FULL VIDEO`.

**Image prompt (IMG05).**

> A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat
> off-white background. Simple thin black hand-drawn linework with slightly
> imperfect, naturally uneven strokes. Flat 2D, no perspective, no shading,
> no texture, no gradient, no shadow. This image contains no colour at all.
>
> On the right, spanning 66–92% of the width and 58–92% of the height, draw a
> minimal stick figure of a male doctor standing and facing to the left: a
> plain round head drawn as a simple circle outline, two small rectangular
> spectacle lenses joined by a short bridge across the middle of the head, a
> short solid black beard drawn as a small filled arc under the chin, one short
> curved side-swept hair stroke across the top of the head, a single-stroke
> straight body line, two simple straight arms hanging at his sides and two
> simple straight legs. No mouth, no eyes, no nose, no ears, no facial detail
> beyond the glasses and beard. No coat, no stethoscope, no clipboard.
>
> On the left, draw three identical rounded-rectangle plates stacked
> vertically, each spanning 8–58% of the width: the top plate occupies 20–30%
> of the height, the middle plate 36–46%, and the bottom plate 52–62%. All
> three are thin black outlines with completely empty interiors, evenly spaced,
> identical in size and corner radius.
>
> Draw one thin vertical black line at 12% of the width running from 25% to 57%
> of the height, passing down the left edges of the three plates and linking
> them as a simple list spine.
>
> The area below 64% of the height on the left side of the frame is completely
> empty off-white. Leave it empty.
>
> Do NOT include: any text, letters, numbers, words, labels, bullets or
> numerals inside or near the plates — all three plate interiors must be
> completely blank; any icons, symbols, hearts, gauges, cups, play buttons or
> triangles; any second figure; any arrows; any border or panel; any colour of
> any kind — this image is pure black line on off-white.

**Separate overlay prompts.**

> **G10 gauge —** A small simple pressure gauge on a fully transparent
> background, thin black hand-drawn linework with slightly uneven strokes,
> flat 2D. A plain circle dial with one short straight needle from its centre
> and a single small tick mark on the rim. No numbers, no scale markings, no
> text, no cuff, no tube, no colour, no background, no shadow.

> **G12 quantity —** Three simple coffee mugs in a row on a fully transparent
> background, thin black hand-drawn linework with slightly uneven strokes,
> flat 2D. Each mug is seen from the side with a round handle on its right and
> a flat coffee-brown horizontal band inside its top rim. They decrease in size
> from left to right. No text, no numbers, no plus or minus signs, no arrows,
> no background, no shadow.

> **G13 video card —** One plain rounded-rectangle panel on a fully transparent
> background, thin black hand-drawn outline with slightly uneven strokes,
> flat 2D, completely empty inside except for one hollow black triangle
> pointing right, centred in the panel, drawn as a simple outline. No text, no
> thumbnail image, no logo, no channel art, no subscribe button, no colour, no
> background, no shadow.

**Initial state (F05.0).** Three empty plates and the doctor. The viewer can
see that three things are coming before any is named. Hold ~1.0s.

**State changes.**
| State | On | What appears / disappears |
|---|---|---|
| F05.1 | onset of "blood" (w111) | Top plate fills: gauge icon at x12–22%, y22–28%, `BLOOD PRESSURE` to its right. Other two plates still blank. |
| F05.2 | onset of "heart" (w113) | Middle plate fills: the same heart drawn in VISUAL 01 at reduced scale, x12–22%, y38–44%, `HEART RESPONSE` to its right. |
| F05.3 | onset of "quantity" (w116) | Bottom plate fills: three cups in decreasing size at x12–26%, y54–60%, `QUANTITY` to their right. List complete. |
| F05.4 | onset of "full" (w124) | All three plates, all contents and the connector line disappear in the same frame that a blank video card at x8–58%, y28–54% with a hollow play triangle, plus `WATCH THE FULL VIDEO` at y58–63%, appear. Dr. Rehan unchanged. |

**Animation 1 (A14).** The gauge icon and the BLOOD PRESSURE text become visible together inside the top plate in a single frame. All three plates, the connector line and Dr. Rehan stay completely static. No camera movement.

**Animation 2 (A15).** The heart icon and the HEART RESPONSE text become visible together inside the middle plate in a single frame. All three plates, the connector line, the top plate's contents and Dr. Rehan stay completely static. No camera movement.

**Animation 3 (A16).** The three-cup icon and the QUANTITY text become visible together inside the bottom plate in a single frame. All three plates, the connector line, the top and middle plate contents and Dr. Rehan stay completely static. No camera movement.

**Animation 4 (A17).** The three plates, all their icons and text, and the connector line all disappear in the same single frame that the video card, its play mark and the WATCH THE FULL VIDEO text become visible. One instantaneous swap, no fade, no crossfade, no slide. Dr. Rehan and the background stay completely static. No camera movement.

**Static elements.** Off-white field, Dr. Rehan, camera — in every state
including the CTA. That constancy is the point: the same person is still
talking, now pointing at a video.

**Narration triggers.** w111 "blood" · w113 "heart" · w116 "quantity" ·
w124 "full".

**Transition out.** None — final shot of the video. Hold F05.4 through
"channel." (w130).

**Reuse instructions.** C01 is the same Dr. Rehan file as VISUAL 03. G11 is
literally G01, the heart from VISUAL 01, re-scaled — reuse, do not redraw;
that reuse ties the payoff back to the opening question. G12 is built from the
O01 mug silhouette at three scales. For A17, either group the plates +
connector into one removable clip, or prepare a second plate (IMG05b) with the
plate column erased and hard-cut the base to it.

**CapCut / I2V.** All four motions CapCut. I2V: none.

**Notes.** The gauge has no numbers. The cups have no count. There is no dose,
no threshold, no millilitre figure, and no safe-amount claim anywhere in this
frame — the narration gives none, so the visuals give none. The CTA stays in
the same off-white field, the same line weight and the same doctor; there is
no end-screen, no subscribe graphic and no colour panel.
*Brain basis: `MASTER_MOTIONS` "icon + label revealed together"; `ASSET_DNA.md`
within-video reuse (~150/448 rows REUSE/RECURRING); `MASTER_SHOTS` 15/200
final shots have no exit transition.*

---

## Asset build list — draw or generate these, in this order

| # | Asset | Format | Used in |
|---|---|---|---|
| 1 | O01 coffee mug | transparent PNG | VISUAL 01, 02, 03, 04 (+ basis for G12) |
| 2 | G01 heart outline | transparent PNG / SVG | VISUAL 01, 05 |
| 3 | C01 Dr. Rehan — two poses (arm raised; arms down) | transparent PNG | VISUAL 01, 03, 05 |
| 4 | C02 patient | transparent PNG | VISUAL 03 |
| 5 | O02 energy-drink can | transparent PNG | VISUAL 02 |
| 6 | G03 red strike stroke | transparent PNG / SVG | VISUAL 01, 03 |
| 7 | G04 stimulation stroke → 2-group + 4-group | transparent PNG / SVG | VISUAL 02 |
| 8 | G05 red caution triangle | transparent PNG / SVG | VISUAL 02 |
| 9 | G07 connector arrow (+ mirrored copy) | transparent PNG / SVG | VISUAL 04 |
| 10 | G08 response arc → 1-arc + 3-arc | transparent PNG / SVG | VISUAL 04 |
| 11 | G10 gauge icon | transparent PNG / SVG | VISUAL 05 |
| 12 | G12 three-cup icon | transparent PNG / SVG | VISUAL 05 |
| 13 | G13 video card + play mark | transparent PNG / SVG | VISUAL 05 |
| 14 | IMG01–IMG05 base plates (+ optional IMG05b) | full-frame JPG/PNG | one per shot |

## Text to type into the editor — nothing else

`GOOD?` · `BAD?` · `BLOOD PRESSURE` · `HEART RESPONSE` · `QUANTITY` ·
`WATCH THE FULL VIDEO`

Six text layers. No image prompt in this document asks for a single letter.

## The 21 anchor words to mark on the waveform

good · bad · Rehan · wrong · People · energy · stronger · dangerous · So ·
patients · not · That's · The · respond · caffeine · judge · Dr. · blood ·
heart · quantity · full

Every visual change in the video fires on the onset of one of these.

## Companion files

`CAPCUT_BUILD.md` (track stacks and operation order) · `STORYBOARD.md`
(state-by-state) · `VISUAL_STATES.csv` · `SHOT_PLAN.csv` · `MOTIONS.csv` ·
`ASSETS.csv` · `BASE_IMAGES.csv` · `TEXT_OVERLAYS.csv` ·
`NARRATION_BEATS.csv` · `IMAGE_PROMPTS.md` · `ANIMATION_PROMPTS.md` ·
`I2V_DECISIONS.md` · `VISUAL_STORY.md` · `TEST_A_SELF_AUDIT.md`
