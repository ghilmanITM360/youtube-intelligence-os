# Revised Final Visual Production Plan — Test A, Revision 1

**Script:** unchanged, verbatim, 130 words. `SCRIPT_CANONICAL.txt` in the
parent directory, SHA-256 `28893099c3e4cc997580c7fc78dc7f029abadadd3aa68dce9eeb2eee5289fe2b`.
Not one word was altered in the first pass and not one word is altered here.

**Production grammar authority:** frozen Production Intelligence Brain v1.0.0,
read-only, unmodified. Validator re-run after this revision: PASS.

**Status:** REVISION_1_COMPLETE — AWAITING HUMAN REVIEW. The blind first pass
is preserved untouched in the parent directory and its 18 locked hashes were
verified before this review began.

---

## Counts

| | First pass | Revision 1 |
|---|---|---|
| Shots | 5 | **5** |
| Base images | 5 | **5** |
| Visual states | 22 | **20** |
| Motions | 17 | **15** |
| Assets | 26 | **25** |
| Text overlays | 6 | **6** |
| Static (no-motion) states | 5 | **5** |
| CapCut motions | 17 | **15** |
| I2V motions | 0 | **0** |
| Camera moves | 0 | **0** |
| Fades / dissolves | 0 | **0** |
| Curved path-following draws | 2 | **0** |
| Operations with no deterministic build | 2 | **0** |
| Est. duration | 33.1s ESTIMATED | **33.1s ESTIMATED** |

Counts are an output of the state-by-state and motion-by-motion audits, not a
target. No reduction goal was set. Of 22 original states, 16 were kept
untouched, 3 modified, 2 merged into 1, and 1 removed. Of 17 motions, 10 were
kept untouched, 4 modified, 2 merged into 1, and 1 removed.

## Density against the recomputed corpus baseline

| Metric | Rev 1 | Portrait median | p75 | p90 | Verdict |
|---|---|---|---|---|---|
| words/shot | 26.0 | 25.5 | 45 | — | at median |
| shot duration | 6.6s est. median | 6.45s | 11.5s | — | at median |
| states/sec | 0.604 | 0.38 | 0.50 | 0.67 | inside p90 |
| motions/sec | 0.453 | 0.27 | 0.35 | 0.45 | at p90 |

The first-pass figures were 0.665 and 0.514. Both now sit inside the portrait
distribution. This was a consequence of the audit, not its purpose — see
`CORPUS_DENSITY_BASELINE.md`, which also corrects the first pass's claim that
its density ran 1.6–1.7x the corpus. Measured against the per-shot
*distribution* rather than the aggregate mean, the first pass sat at the
portrait 90th percentile: high-normal, not anomalous.

Per-shot, the picture is uneven and two shots remain above p90:

| Shot | States | Motions | Est. s | states/sec | motions/sec |
|---|---|---|---|---|---|
| SH01 | 5 | 4 | 4.33 | 1.155 | 0.924 |
| SH02 | 4 | 3 | 7.89 | 0.507 | 0.380 |
| SH03 | 3 | 2 | 8.14 | 0.369 | 0.246 |
| SH04 | 3 | 2 | 6.62 | 0.453 | 0.302 |
| SH05 | 5 | 4 | 6.11 | 0.818 | 0.655 |

SH01 (1.16 states/sec) and SH05 (0.82) exceed the portrait p90 of 0.67. Both
are driven by the script's own word density — SH01 names four concepts in 17
words, SH05 names three in six — and every state in both fires on a distinct
concept word. No cut was made for density alone. This is the most likely point
of reasonable disagreement in the plan and it is flagged rather than fixed.

---

## The visual language, stated once

Everything below is written in one language, derived from the frozen brain and
stated here so that no individual prompt has to restate it.

- **Canvas.** 9:16 vertical, 2160 x 3840. Every form must read on a phone held
  at arm's length.
- **Field.** Flat off-white, full frame, opaque. No texture, gradient, vignette
  or border. It is the only opaque asset; everything else composites over it.
- **Line.** Thin black hand-drawn strokes with slightly uneven weight, as if
  drawn quickly with a fine marker. Uniform weight across all five plates.
- **Flatness.** No perspective, no shading, no lighting, no drop shadow, no 3D.
- **One idea per frame.** Large readable forms, generous negative space, the
  fewest simultaneous objects that still carry the point.
- **Colour.** Three restrained accents only. Coffee brown appears solely as the
  liquid inside a cup. Muted medical red appears solely on the strike stroke,
  the caution mark and the response arcs — and is never generated into a base
  image, always composited. Light neutral grey is available and in the event
  unused. Nothing else is coloured.
- **Camera.** Locked. Zero moves of any kind, in any shot. Every well-formed
  CAMERA_STATE row across the brain's 581 states is LOCKED or STATIC.
- **Editing.** Hard cuts only, four of them. No dissolve, fade, wipe or
  swipe at any shot boundary. The corpus has zero fades across 186 measured
  boundaries.
- **Change.** A visual change is normally one frame. In the brain's 230
  portrait motions the most common SPEED value is literally ONE-FRAME CHANGE,
  and 30 further rows specify 3–15 frames. Fourteen of this plan's fifteen
  motions are one-frame; the fifteenth is four frames.
- **Sync.** Every change fires on the onset of the word that carries its
  concept. Measured STATE_CHANGE offset in the corpus is a median 37 ms, which
  is within one frame, so no offset padding is added.
- **Text.** Never generated inside an image. All six text strings are native
  editor layers.
- **Timing.** No absolute timestamps anywhere. Every anchor is a word onset.
  Durations are ESTIMATED from 3.93 words/sec and are never mixed with
  measured values, because no measured values exist yet.

## The medical guardrails, stated once

These are **web-verified medical constraints, not brain-derived production
decisions**, and they are labelled as such wherever they influence a choice.
They constrained what may be depicted; they never supplied a visual grammar.

- The attributed energy-drink comparison is carried by one restrained caution
  mark over one object. No skull, no death icon, no exploding or bleeding
  heart, no heart attack, no flatline, no poison symbol, no red emergency
  field, no colour wash.
- Coffee is depicted as neither universally healthy nor universally harmful.
  The plan's whole argument is that body response and context outrank a simple
  good/bad label.
- No numbers of any kind appear anywhere: no blood-pressure values, no
  caffeine milligrams, no safe-dose thresholds, no cup counts, no millilitres.
- No diagnoses, disease labels, arrhythmia tracings or ECG lines.
- No prescriptive recommendation is depicted.
- The response arcs are unlabelled and uncalibrated. They count; they do not
  measure.
- **Revision 1 removed the blood-pressure gauge icon** partly on this basis: a
  needle resting on a dial reads as a reading, and a tick mark reads as a
  threshold, neither of which the narration supplies.
- Dr. Rehan is a simplified corpus-compatible stick figure with three
  identifying cues — rectangular glasses, a short beard, a side-swept hair
  stroke. Not a portrait, not a likeness, no attempt at facial identity.
- The energy-drink can is unbranded and must not resemble any real product.

---

# SH01 — Install the good/bad binary model and have the named doctor strike it out

**Narration (verbatim):** Is coffee good for your heart-or bad for it? Dr. Rehan says that's actually the wrong question.

**Words** w1-w17 (17) · **Est. duration** 4.33 ESTIMATED ·
**Beats** B01,B02 · **Base image** IMG01 · **States** 5 ·
**Motions** 4 · **In** START · **Out** Red strike completes across the fork (4 frames)

**Revision 1 change:** No states or motions changed. M04 strike duration shortened from a spoken phrase to 4 frames.

**Brain evidence:** MASTER_SHOTS: 2/200 shots carry TRANSITION_IN=START. MASTER_MOTIONS red-strike duration 0.125-0.208s.

## IMG01 — base image

**In the plate:** Off-white field, coffee mug with brown liquid band, outline heart below it. Nothing else.

**Composited over it:** Fork lines + plates (G02, 2 layers), Dr. Rehan (C01), strike stroke (G03), text T01/T02

**Supports 5 states:** R01.0, R01.1, R01.2, R01.3, R01.4

**Standalone image prompt:**

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

## States

### R01.0 (was F01.0) — START of narration ("Is", w1)

**Script:** "Is coffee"

**Exact frame.** Off-white portrait field, 9:16. A flat black line-drawn coffee mug with a side handle on the right sits centred at x36-64%, y18-30%; the liquid inside the rim is a flat coffee-brown band across x39-61%, y19-22%. Directly below it, a single-stroke black outline heart, x42-58%, y34-43%. Everything below y44% is empty off-white field. No text, no arrows, no other objects.

**Changes on entry.** (nothing - opening state)

**Static throughout.** Off-white field; coffee mug; heart; camera

**Purpose.** Put the two subjects of the question on screen before the question is finished being asked

**Arrives by.** Hard cut in — no motion

**Hold.** ~0.5s ESTIMATED (2 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G01  ·  **Base image reuse.** NO

**Revision change.** UNCHANGED

**Brain pattern.** VISUAL_DNA: all 581 CAMERA_STATE rows are LOCKED/STATIC family; portrait opening states are a bare plate with large negative space

### R01.1 (was F01.1) — ON_WORD_START ("good", w3)

**Script:** "good for your heart-or"

**Exact frame.** Same off-white field, mug at x36-64% y18-30% and heart at x42-58% y34-43% unchanged. Two straight thin black lines now descend from the bottom point of the heart at x50%,y44%, one to x18%,y56% and one to x82%,y56%, forming a wide inverted V. A blank rounded-rectangle label plate, thin black outline, sits at x10-40%, y56-66% at the end of the left line. Editor text GOOD? is centred inside that left plate. The right line ends in empty field - no plate there yet.

**Changes on entry.** Fork lines; left label plate; GOOD? text

**Static throughout.** Off-white field; mug; heart; camera

**Purpose.** Draw the first half of the binary model on the word that names it

**Arrives by.** M01 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~1.0s ESTIMATED (4 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G01,G02,T01  ·  **Base image reuse.** YES (same base plate as R01.0)

**Revision change.** UNCHANGED

**Brain pattern.** AUDIO_VISUAL_SYNC_DNA: STATE_CHANGE median offset 37ms from the anchor word

### R01.2 (was F01.2) — ON_WORD_START ("bad", w7)

**Script:** "bad for it? Dr."

**Exact frame.** Same field, mug, heart and both fork lines. A second blank rounded-rectangle label plate, identical in size and stroke to the left one, now sits at x60-90%, y56-66% at the end of the right line. Editor text BAD? is centred inside it. The model is now symmetrical: one mug, one heart, two branches, two labels. Lower field below y68% still empty.

**Changes on entry.** Right label plate; BAD? text

**Static throughout.** Off-white field; mug; heart; fork lines; left plate and GOOD? text; camera

**Purpose.** Complete the binary so the viewer owns the model that is about to be rejected

**Arrives by.** M02 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~1.0s ESTIMATED (4 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G01,G02,T01,T02  ·  **Base image reuse.** YES

**Revision change.** KEPT AGAINST the first pass's own cut suggestion - merging would fire a named concept off its word onset

**Brain pattern.** AUDIO_VISUAL_SYNC_DNA word-onset anchoring (581 STATE_CHANGE events); VISUAL_CHANGE_PATTERNS one concept per reveal

### R01.3 (was F01.3) — ON_WORD_START ("Rehan", w11)

**Script:** "Rehan says that's actually the"

**Exact frame.** Same field and complete binary model. A stick figure now stands in the previously empty lower-left field at x8-30%, y70-95%: round head with two small rectangular glasses lenses joined by a bridge, a short filled black beard arc under the chin, a short side-swept hair stroke on top, plain single-stroke body, and the near arm raised at roughly 45 degrees toward the fork above. Faces frame-right. Lower-right field remains empty.

**Changes on entry.** Dr. Rehan figure

**Static throughout.** Off-white field; mug; heart; fork; both plates and their text; camera

**Purpose.** Put the named speaker in frame on his name, so the rejection that follows has an author

**Arrives by.** M03 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~1.3s ESTIMATED (5 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G01,G02,C01,T01,T02  ·  **Base image reuse.** YES

**Revision change.** UNCHANGED

**Brain pattern.** ASSET_CREATION_SYSTEM: CHARACTER assets are transparent PNG overlays (TRANSPARENT_BG=YES in 252/448 rows); entries are one-frame appearances

### R01.4 (was F01.4) — ON_WORD_START ("wrong", w16)

**Script:** "wrong question."

**Exact frame.** Same field, model and doctor figure. One thick muted-red hand-drawn stroke, slightly uneven, now crosses the entire fork diagonally from x14%,y68% up to x86%,y52%, cutting through both branch lines and clipping the top edge of both label plates. The plates and their text remain legible under the stroke. Nothing else changes.

**Changes on entry.** Muted-red strike stroke

**Static throughout.** Off-white field; mug; heart; fork; both plates and text; Dr. Rehan; camera

**Purpose.** Reject the model on the word that rejects it, and teach the viewer that a red strike means wrong

**Arrives by.** M04 — Draw on progressively, 4 frames (0.167s ESTIMATED)

**Hold.** ~0.5s ESTIMATED (2 words), held to the cut  ·  **Exit.** HOLD_TO_HARD_CUT

**Assets.** E01,O01,G01,G02,C01,G03,T01,T02  ·  **Base image reuse.** YES

**Revision change.** FRAME UNCHANGED; the strike now draws in 4 frames instead of across a spoken phrase (see M04)

**Brain pattern.** MASTER_MOTIONS: ten 'Draw red strike for line N' rows, left to right along a fixed stroke, DURATION 0.125-0.208s

## Motions

| ID | On word | Moving element | Action | Duration | Static anchors | Build |
|---|---|---|---|---|---|---|
| M01 (was A01) | ON_WORD_START ("good", w3) | Fork lines + left label plate + GOOD? text (G02a, T01) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; coffee mug; heart; camera | CAPCUT |
| M02 (was A02) | ON_WORD_START ("bad", w7) | Right label plate + BAD? text (G02b, T02) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; mug; heart; fork lines; left plate and GOOD? text; camera | CAPCUT |
| M03 (was A03) | ON_WORD_START ("Rehan", w11) | Dr. Rehan figure (C01) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; mug; heart; fork; both plates and text; camera | CAPCUT |
| M04 (was A04) | ON_WORD_START ("wrong", w16) | Muted-red strike stroke (G03) | Draw on progressively | 4 frames (0.167s ESTIMATED) | Off-white field; mug; heart; fork; both plates; both text labels; Dr. Rehan; camera | CAPCUT |

**M01** — A discrete element appearing is an opacity switch on a layer group - deterministic, exact geometry required, no generation needed  *Revision:* UNCHANGED

**M02** — The word 'bad' is spoken here and nowhere else; merging would fire a named concept off its word onset, breaking the brain's primary sync rule  *Revision:* KEPT against the first pass's own density-cut suggestion

**M03** — A character entering is a transparent PNG becoming visible. No walk-in, no slide, no scale - the corpus never travels a character into frame  *Revision:* UNCHANGED

**M04** — The mechanism was right and the pacing was wrong. Every one of the corpus's ten drawn red strikes completes in 3-5 frames. A 4-frame draw reads as a decisive slash; a half-second draw reads as an animated flourish. Built as a linear left-to-right wipe mask over a static PNG - the stroke is straight, so the mask is straight  *Revision:* DURATION SHORTENED from spanning "wrong"-to-"question." (~0.5s+) to 4 frames

---

# SH02 — Compare coffee and an unbranded energy drink as two physical objects on one baseline - strength first, then caution

**Narration (verbatim):** People usually ask me, then what about the energy drinks? So, energy drinks for me are much stronger than coffee and they are a bit more dangerous than coffee as well.

**Words** w18-w48 (31) · **Est. duration** 7.89 ESTIMATED ·
**Beats** B03,B04,B05 · **Base image** IMG02 · **States** 4 ·
**Motions** 3 · **In** HARD CUT · **Out** Caution mark appears above the can

**Revision 1 change:** Unchanged. The caution triangle was the strongest merge candidate and survives on newly located corpus precedent.

**Brain evidence:** MASTER_SHOTS hard-cut family 131/200. MASTER_STATES F06.1 (if_all_humans_died) warning triangles.

## IMG02 — base image

**In the plate:** Off-white field, horizontal baseline at y70%, coffee mug standing on it with brown liquid band, the mug's two stimulation strokes.

**Composited over it:** Can (O02), the can's four strokes (G04b), caution triangle (G05)

**Supports 4 states:** R02.0, R02.1, R02.2, R02.3

**Standalone image prompt:**

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
> They read as a small "activity" mark above the cup.
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

## States

### R02.0 (was F02.0) — HARD CUT on "People" (w18)

**Script:** "People usually ask me, then what about the"

**Exact frame.** Off-white portrait field. A thin horizontal black baseline runs across x8-92% at y70%. A flat black line-drawn coffee mug with a side handle stands on it at x14-40%, y52-70%, coffee-brown liquid band across x17-34%, y53-56%. Two short black radiating strokes sit above the mug at x20-34%, y42-50%. The right half of the baseline is bare and the whole field above y42% is empty. No text.

**Changes on entry.** (nothing - opening state of the shot)

**Static throughout.** Off-white field; baseline; coffee mug; the mug's two stimulation strokes; camera

**Purpose.** Establish coffee alone, with its stimulation reading already visible as the unit of measure the can will be compared against

**Arrives by.** Hard cut in — no motion

**Hold.** ~2.0s ESTIMATED (8 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G04  ·  **Base image reuse.** NO

**Revision change.** UNCHANGED

**Brain pattern.** DECISION_RULES 1: hard-cut family in 131/200 TRANSITION_IN rows; concept change triggers the cut

### R02.1 (was F02.1) — ON_WORD_START ("energy", w26)

**Script:** "energy drinks? So, energy drinks for me are much"

**Exact frame.** Same field, baseline, mug and its two strokes. A tall plain cylindrical can now stands on the same baseline at x60-86%, y44-70%: flat black outline, rounded top rim with a small pull-tab ellipse, one plain horizontal band across its middle, and completely blank sides - no logo, no brand, no lettering, no colour fill. It is visibly taller than the mug. The field above y42% remains empty.

**Changes on entry.** Energy-drink can

**Static throughout.** Off-white field; baseline; mug; mug strokes; camera

**Purpose.** Introduce the second container as a physical object, unbranded, on the word that names it

**Arrives by.** M05 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~2.3s ESTIMATED (9 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G04,O02  ·  **Base image reuse.** YES

**Revision change.** UNCHANGED

**Brain pattern.** ASSET_CREATION_SYSTEM: OBJECT assets are transparent PNG overlays; portrait SPEED ONE-FRAME CHANGE is the most common value

### R02.2 (was F02.2) — ON_WORD_START ("stronger", w35)

**Script:** "stronger than coffee and they are a bit more"

**Exact frame.** Same field, baseline, mug, mug strokes and can. Four black radiating strokes, in the same hand-drawn style as the mug's two, now sit above the can at x62-84%, y28-42%. They are the same stroke length as the mug's but there are four of them and the group sits higher in frame, so the two groups read as the same unit counted twice over. Nothing else changes.

**Changes on entry.** The can's four stimulation strokes

**Static throughout.** Off-white field; baseline; mug; mug strokes; can; camera

**Purpose.** State the comparison as a countable difference rather than a label

**Arrives by.** M06 — Pop on together in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~2.3s ESTIMATED (9 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,G04,O02  ·  **Base image reuse.** YES

**Revision change.** UNCHANGED

**Brain pattern.** MASTER_MOTIONS: grouped one-frame reveals ('Show the red letter-key TAP, 1.5 mJ and A S D key icons together')

### R02.3 (was F02.3) — ON_WORD_START ("dangerous", w44)

**Script:** "dangerous than coffee as well."

**Exact frame.** Same field with both containers and both stroke groups. A single muted-red outlined triangle with a short vertical exclamation stroke and dot inside now sits above the can's strokes at x66-80%, y14-25%. It sits over the can only; the space above the mug stays empty. No other marks, no colour wash, no background change.

**Changes on entry.** Muted-red caution triangle

**Static throughout.** Off-white field; baseline; mug; mug strokes; can; can strokes; camera

**Purpose.** Carry the narration's caution without overstating it - one restrained mark over one object

**Arrives by.** M07 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~1.3s ESTIMATED (5 words), held to the cut  ·  **Exit.** HOLD_TO_HARD_CUT

**Assets.** E01,O01,G04,O02,G05  ·  **Base image reuse.** YES

**Revision change.** KEPT, and its precedent status upgraded: warning triangles are directly precedented in three corpus videos, contrary to the first pass's claim

**Brain pattern.** MASTER_STATES F06.1 (if_all_humans_died) 'Multiple black warning triangles appear over wall map'; MASTER_ASSETS G03/G08/G10/O13. Muted red instead of black is a stated MEDICAL GUARDRAIL departure

## Motions

| ID | On word | Moving element | Action | Duration | Static anchors | Build |
|---|---|---|---|---|---|---|
| M05 (was A05) | ON_WORD_START ("energy", w26) | Energy-drink can (O02) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; baseline; coffee mug; the mug's two strokes; camera | CAPCUT |
| M06 (was A06) | ON_WORD_START ("stronger", w35) | The can's four stimulation strokes (G04b) | Pop on together in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; baseline; mug; mug strokes; can; camera | CAPCUT |
| M07 (was A07) | ON_WORD_START ("dangerous", w44) | Muted-red caution triangle (G05) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; baseline; mug; mug strokes; can; can strokes; camera | CAPCUT |

**M05** — Discrete object reveal at an exact position on a shared baseline. No drop-in, no bounce, no scale  *Revision:* UNCHANGED

**M06** — The four strokes must appear as one countable group, not stagger. Staggering would read as escalation over time; the narration says 'stronger', not 'getting stronger'  *Revision:* UNCHANGED

**M07** — One mark, one frame. Any animation here - pulse, flash, shake, colour wash - would overstate a claim the narration explicitly hedges. NO MOTION beyond the appearance is both the grammar answer and the guardrail answer  *Revision:* UNCHANGED, precedent status upgraded

---

# SH03 — Re-stage the binary as a real consultation, then delete it outright in front of the person who asked

**Narration (verbatim):** So now, if the patients ask me, so is coffee good or bad for your health? I tell them that should not be the question to be asked. That's a wrong question.

**Words** w49-w80 (32) · **Est. duration** 8.14 ESTIMATED ·
**Beats** B06,B07,B08 · **Base image** IMG03 · **States** 3 ·
**Motions** 2 · **In** HARD CUT · **Out** Diagram and its text removed in one frame

**Revision 1 change:** One state and one motion removed (F03.2 / A09, the second red strike). The deletion re-anchored from 'That's' (w77) to 'not' (w70), giving the emptied frame a 2.6s payoff hold.

**Brain evidence:** DECISION_RULES 3: STATE_REPLACEMENT 230/438. The corpus's repeated strikes enumerate different lines, they do not repeat one mark.

## IMG03 — base image

**In the plate:** Off-white field, Dr. Rehan lower-left facing right, compact binary diagram upper-centre as one removable group.

**Composited over it:** Patient (C02), text T01/T02

**Supports 3 states:** R03.0, R03.1, R03.2

**Standalone image prompt:**

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
> descend outward, one to the left and one to the right, each ending at the top
> edge of a rounded-rectangle plate. The left plate spans 24–46% of the width
> and 34–44% of the height; the right plate spans 54–76% of the width and the
> same height band. Both plates are thin black outlines with completely empty
> interiors.
>
> The entire right-hand side of the frame below 50% of the height is completely
> empty off-white. Leave it empty.
>
> Do NOT include: any text, letters, numbers, words, labels, check marks or
> crosses inside or near the plates — the plate interiors must be completely
> blank; any second person or patient figure; any speech bubbles; any strike,
> slash or cross-out stroke; any hearts, cans or warning signs; any border or
> panel; any red; any colour other than the single brown coffee band.

## States

### R03.0 (was F03.0) — HARD CUT on "So" (w49)

**Script:** "So now, if the"

**Exact frame.** Off-white portrait field. Dr. Rehan stands at x6-28%, y58-92% facing frame-right: round head, rectangular glasses, short filled beard, side-swept hair stroke, plain single-stroke body, near arm lowered. Upper-centre holds a compact binary diagram: a small coffee mug at x44-56%, y14-23% with a coffee-brown liquid band, two thin black lines descending from it to two blank rounded label plates at x24-46% and x54-76%, y34-44%, carrying editor text GOOD? and BAD?. The entire right-hand lower field below y50% is empty.

**Changes on entry.** (nothing - opening state of the shot)

**Static throughout.** Off-white field; Dr. Rehan; compact fork; both plates; GOOD?/BAD? text; camera

**Purpose.** Re-state the binary as something asked inside a consultation, not as a slide

**Arrives by.** Hard cut in — no motion

**Hold.** ~1.0s ESTIMATED (4 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,C01,O01,G06,T01,T02  ·  **Base image reuse.** NO

**Revision change.** UNCHANGED

**Brain pattern.** DECISION_RULES 1: hard cut on concept change. Labels are baked into the plate because this is a recall of a model already taught in SH01

### R03.1 (was F03.1) — ON_WORD_START ("patients", w53)

**Script:** "patients ask me, so is coffee good or bad for your health? I tell them that should"

**Exact frame.** Same field, doctor and binary diagram. A second stick figure now stands in the empty right field at x72-94%, y60-92%, facing frame-left toward the doctor: plain round head, no glasses, no beard, no hair marks, plain single-stroke body, near arm slightly raised as if asking. The two figures face each other across the diagram above them.

**Changes on entry.** Patient figure

**Static throughout.** Off-white field; Dr. Rehan; fork; plates; text; camera

**Purpose.** Make the question belong to a patient, and hold that frame while the whole question is spoken

**Arrives by.** M08 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~4.3s ESTIMATED (17 words) - a long deliberate hold while the question and its setup are delivered  ·  **Exit.** STATE_REPLACEMENT

**Assets.** E01,C01,O01,G06,T01,T02,C02  ·  **Base image reuse.** YES

**Revision change.** Exit method changed from ADDITIVE_REVEAL to STATE_REPLACEMENT: the second strike no longer intervenes, so this state now exits straight into the deletion

**Brain pattern.** MASTER_STATES portrait state duration median 2.00s, p90 4.79s, max 19.90s - long locked holds under continuous narration are normal

### R03.2 (was F03.3) — ON_WORD_START ("not", w70)

**Script:** "not be the question to be asked. That's a wrong question."

**Exact frame.** Same off-white field with Dr. Rehan at x6-28%, y58-92% and the patient at x72-94%, y60-92%, both unchanged and still facing each other. The entire upper-centre area is now empty off-white: the mug, both branch lines, both label plates and both text labels are all gone in one frame. Two figures, a large blank field between and above them, nothing else.

**Changes on entry.** Whole binary diagram and its text - all removed

**Static throughout.** Off-white field; Dr. Rehan; patient; camera

**Purpose.** Delete the model before the replacement arrives - the empty space is the argument

**Arrives by.** M09 — Remove in one frame (state replacement), 1 frame (0.042s ESTIMATED)

**Hold.** ~2.6s ESTIMATED (11 words), held to the cut  ·  **Exit.** HOLD_TO_HARD_CUT

**Assets.** E01,C01,C02  ·  **Base image reuse.** YES

**Revision change.** RE-ANCHORED from 'That's' (w77) to 'not' (w70) and its hold extended from ~1.0s to ~2.6s, because the intervening strike state was removed. The removed group no longer includes a strike stroke.

**Brain pattern.** DECISION_RULES 3: STATE_REPLACEMENT is 230/438 motions (53%). EDITING_DNA: zero fades across 186 measured shot boundaries

## Motions

| ID | On word | Moving element | Action | Duration | Static anchors | Build |
|---|---|---|---|---|---|---|
| M08 (was A08) | ON_WORD_START ("patients", w53) | Patient figure (C02) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; Dr. Rehan; compact fork; both plates; GOOD?/BAD? text; camera | CAPCUT |
| M09 (was A10) | ON_WORD_START ("not", w70) | The entire binary diagram group (G06) plus T01 and T02 | Remove in one frame (state replacement) | 1 frame (0.042s ESTIMATED) | Off-white field; Dr. Rehan; patient; camera | CAPCUT |

**M08** — Character entry as a visibility change, matching M03. The 4.3s static hold that follows it is the best pacing decision in the plan and is left completely alone  *Revision:* UNCHANGED

**M09** — The deletion must be instantaneous. A fade-out would soften exactly the beat that has to be blunt, and the corpus contains zero fades across 186 measured shot boundaries. Moving it to 'not' puts it on the word that performs the rejection and buys the emptied frame a 2.6s payoff hold  *Revision:* RE-ANCHORED from "That's" (w77) to "not" (w70). The removed group no longer contains a strike stroke, because the second strike no longer exists

---

# SH04 — Replace the deleted model with coffee - person - response, then show two identical people reading differently

**Narration (verbatim):** The real question is, how does your body respond to caffeine or coffee? And that's the main message: don't judge coffee only as "good" or "bad."

**Words** w81-w106 (26) · **Est. duration** 6.62 ESTIMATED ·
**Beats** B09,B10 · **Base image** IMG04 · **States** 3 ·
**Motions** 2 · **In** HARD CUT · **Out** Second reading completes at the right-hand figure

**Revision 1 change:** Two states merged into one (F04.1+F04.2). Both curved-arrow draws converted to one-frame coupled pops, which also removes the plan's only unbuildable operation.

**Brain evidence:** MASTER_MOTIONS: 'Reveal the six red curved arrow strokes toward the book pages' 0.292s / 7 frames - curved arrows are group reveals, not traced paths.

## IMG04 — base image

**In the plate:** Off-white field, coffee mug top-centre with brown liquid band, and one thin horizontal baseline at y80%. NO figures in the plate.

**Composited over it:** The single stick-figure PNG (C03) placed twice, at x14-36% and x64-86%; left arrow + left arc (G07a, G08a); right arrow + three arcs (G07b, G08b)

**Supports 3 states:** R04.0, R04.1, R04.2

**Standalone image prompt:**

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
> The mug and that one ground line are the only two things in the picture.
> Everything between 24% and 80% of the image height is completely empty
> off-white, across the full width. Nothing stands on the ground line. Leave it
> all empty.
>
> Do NOT include: any people, figures, stick figures, silhouettes or
> characters; any text, letters, numbers or labels; any arrows, curves, lines
> or connectors other than the single ground line; any marks, arcs, waves or
> symbols; any hearts, cans, plates or icons; any border or panel; any red;
> any colour other than the single brown coffee band.

## States

### R04.0 (was F04.0) — HARD CUT on "The" (w81)

**Script:** "The real question is, how does your body"

**Exact frame.** Off-white portrait field. A flat black line-drawn coffee mug with a coffee-brown liquid band sits centred at the top, x42-58%, y12-22%. A thin horizontal baseline runs across x10-90% at y80%. Two identical plain stick figures stand on it, facing forward: left figure x14-36%, y52-80%, right figure x64-86%, y52-80%. Both have plain round heads, no glasses, no beards, no distinguishing marks, and identical posture. The whole band between y24% and y50% is empty off-white.

**Changes on entry.** (nothing - opening state of the shot)

**Static throughout.** Off-white field; baseline; mug; both figures; camera

**Purpose.** Replace the deleted model with a new one: one coffee, two people, nothing decided yet

**Arrives by.** Hard cut in — no motion

**Hold.** ~2.0s ESTIMATED (8 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,C03  ·  **Base image reuse.** NO

**Revision change.** Frame unchanged. Asset build instruction tightened: the two figures must be one PNG duplicated in the editor, not two generated figures (see EXECUTABILITY_CHECK)

**Brain pattern.** IMAGE_TO_VIDEO_SYSTEM 2: deterministic diagram states stay deterministic - this is a static plate, not generated motion

### R04.1 (was F04.1 + F04.2 (MERGED)) — ON_WORD_START ("respond", w89)

**Script:** "respond to caffeine or coffee? And that's the main message: don't"

**Exact frame.** Same field, mug and both figures. A thin black hand-drawn arrow now curves from the bottom-left of the mug at x44%,y23% down and left to the left figure's chest at x28%,y58%, ending in a small open arrowhead; the curve is a single smooth stroke with slightly uneven weight. At the same moment one small muted-red arc, like a single sound-wave stroke, appears at the left figure's chest at x22-30%, y58-63%. It is a single arc only. The right figure and the right half of the frame are unchanged and still empty of marks.

**Changes on entry.** Left connector arrow and the left figure's single response arc (appear together)

**Static throughout.** Off-white field; baseline; mug; both figures; camera

**Purpose.** Show the direction of the new question and the reading it produces as one idea: from the drink, to the person, to a response at the body

**Arrives by.** M10 — Pop on together in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~4.3s ESTIMATED (17 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,O01,C03,G07,G08  ·  **Base image reuse.** YES

**Revision change.** MERGED from two states two words apart. Arrow and arc are one coupled idea; the corpus reveals coupled elements together rather than staggering them

**Brain pattern.** DECISION_RULES 3 SIMULTANEOUS_COUPLED (36 motions); MASTER_MOTIONS 'Show the first energy label and curved arrow' (0.042s, one-frame change). MEDICAL GUARDRAIL: the arc is unlabelled - no numbers, no diagnosis, no ECG trace

### R04.2 (was F04.3) — ON_WORD_START ("judge", w100)

**Script:** "judge coffee only as "good" or "bad.""

**Exact frame.** Same field, mug, both figures, left arrow and the left figure's single arc. A second thin black hand-drawn arrow now curves from the bottom-right of the mug at x56%,y23% down and right to the right figure's chest at x72%,y58%, and three stacked muted-red arcs - same stroke style as the left figure's single arc, but three of them - sit at the right figure's chest at x70-80%, y55-65%. All four elements appear in the same frame. The two figures are now identical in every way except the number of arcs. Same coffee, same arrows, different reading.

**Changes on entry.** Right connector arrow and the right figure's three response arcs (appear together)

**Static throughout.** Off-white field; baseline; mug; both figures; left arrow; left arc; camera

**Purpose.** State the main message as a picture: one coffee cannot carry one label because the reading is at the person

**Arrives by.** M11 — Pop on together in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~1.8s ESTIMATED (7 words), held to the cut  ·  **Exit.** HOLD_TO_HARD_CUT

**Assets.** E01,O01,C03,G07,G08  ·  **Base image reuse.** YES

**Revision change.** Frame unchanged. Motion changed from draw-then-pop to a single one-frame coupled pop, matching the corpus's curved-arrow treatment and making the left and right readings mechanically identical

**Brain pattern.** MASTER_MOTIONS: 'Reveal the six red curved arrow strokes toward the book pages' 0.292s / 7 frames - a group reveal, not a traced path

## Motions

| ID | On word | Moving element | Action | Duration | Static anchors | Build |
|---|---|---|---|---|---|---|
| M10 (was A11 + A12 (MERGED)) | ON_WORD_START ("respond", w89) | Left connector arrow (G07a) and the left figure's single response arc (G08a) | Pop on together in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; baseline; coffee mug; both stick figures; camera | CAPCUT |
| M11 (was A13) | ON_WORD_START ("judge", w100) | Right connector arrow (G07b) and the right figure's three response arcs (G08b) | Pop on together in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; baseline; mug; both figures; left arrow; left arc; camera | CAPCUT |

**M10** — Three findings converge. Grammar: the corpus reveals curved arrows as groups in a handful of frames, it does not trace them. Coupling: the arrow and the arc are one idea and the corpus reveals coupled elements together. Executability: CapCut masks are linear and shape-based, so a path-following curve had no deterministic implementation - the first pass flagged this and offered fallbacks; the one-frame pop was among them and should have been the primary choice  *Revision:* MERGED from two motions two words apart, and the curved draw converted to a one-frame pop

**M11** — Same evidence as M10, plus an internal-consistency gain: with M10 and M11 both one-frame coupled pops, the left and right readings are produced by identical mechanisms, which is what makes 'identical in every way except the number of arcs' true of the finished edit and not only of the storyboard. Confidence rises from MEDIUM to HIGH because the editor can now execute it exactly  *Revision:* CHANGED from draw-along-curve-then-pop to a single one-frame coupled pop

---

# SH05 — Name the three factors one at a time into a pre-visible scaffold, then hand off to the full video

**Narration (verbatim):** Dr. Rehan explains what blood pressure, heart response and quantity have to do with it in the full video. Watch it on the channel.

**Words** w107-w130 (24) · **Est. duration** 6.11 ESTIMATED ·
**Beats** B11,B12 · **Base image** IMG05 · **States** 5 ·
**Motions** 4 · **In** HARD CUT · **Out** (none - final shot of the video)

**Revision 1 change:** Gauge icon G10 deleted from the top plate (no corpus analogue, and a needle-on-dial implies a reading the narration never gives). Heart and three-cup icons kept - both reuse established shapes.

**Brain evidence:** MASTER_ASSETS: no dial/gauge asset in 448 rows. MASTER_SHOTS: 15/200 shots have empty TRANSITION_OUT.

## IMG05 — base image

**In the plate:** Off-white field, Dr. Rehan right facing left, three blank stacked plates and their vertical connector line on the left, all plates empty.

**Composited over it:** Heart icon (G11), three-cup icon (G12), video card + play mark (G13), text T03/T04/T05/T06

**Supports 5 states:** R05.0, R05.1, R05.2, R05.3, R05.4

**Standalone image prompt:**

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
> On the left, draw three identical rounded-rectangle plates stacked vertically,
> each spanning 8–58% of the width: the top plate occupies 20–30% of the height,
> the middle plate 36–46%, and the bottom plate 52–62%. All three are thin black
> outlines with completely empty interiors, evenly spaced, identical in size and
> corner radius.
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
> completely blank; any icons, symbols, hearts, gauges, dials, cups, play
> buttons or triangles; any second figure; any arrows; any border or panel;
> any colour of any kind — this image is pure black line on off-white.

## States

### R05.0 (was F05.0) — HARD CUT on "Dr." (w107)

**Script:** "Dr. Rehan explains what"

**Exact frame.** Off-white portrait field. Dr. Rehan stands at x66-92%, y58-92% facing frame-left: round head, rectangular glasses, short filled beard, side-swept hair stroke, plain single-stroke body. On the left, three identical blank rounded-rectangle plates, thin black outline, are stacked vertically at x8-58%, occupying y20-30%, y36-46% and y52-62%. A thin vertical black connector line runs down their left edges at x12% from y25% to y57%. All three plates are completely empty. The lower-left field below y64% is blank.

**Changes on entry.** (nothing - opening state of the shot)

**Static throughout.** Off-white field; Dr. Rehan; three blank plates; connector line; camera

**Purpose.** Show that three things are coming before naming any of them

**Arrives by.** Hard cut in — no motion

**Hold.** ~1.0s ESTIMATED (4 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,C01,G09  ·  **Base image reuse.** NO

**Revision change.** UNCHANGED

**Brain pattern.** VISUAL_DNA: corpus list layouts open with the empty scaffold visible and fill it on the words

### R05.1 (was F05.1) — ON_WORD_START ("blood", w111)

**Script:** "blood pressure,"

**Exact frame.** Same field, doctor, three plates and connector. The top plate is now filled with editor text BLOOD PRESSURE, left-aligned inside the plate at x12-56%, y22-28%. There is no icon in the plate - the text sits alone. The middle and bottom plates remain completely blank.

**Changes on entry.** Top plate contents: BLOOD PRESSURE text

**Static throughout.** Off-white field; Dr. Rehan; all three plates; connector; camera

**Purpose.** Name the first factor on the word that names it, without implying a value, a direction or a threshold

**Arrives by.** M12 — Pop on in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~0.5s ESTIMATED (2 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,C01,G09,T03  ·  **Base image reuse.** YES

**Revision change.** GAUGE ICON REMOVED. A needle-on-dial has no analogue in 448 corpus assets and reads as a measured value with a threshold, which the narration never supplies

**Brain pattern.** MASTER_ASSETS: no dial/gauge/instrument-face asset exists in the corpus. MEDICAL GUARDRAIL (web-verified, not brain-derived): no BP numbers, thresholds or directional claims

### R05.2 (was F05.2) — ON_WORD_START ("heart", w113)

**Script:** "heart response and"

**Exact frame.** Same field, doctor, plates and connector, with the top plate carrying its text. The middle plate is now filled: a small single-stroke black outline heart at x12-22%, y38-44%, with editor text HEART RESPONSE to its right inside the same plate. The bottom plate remains blank.

**Changes on entry.** Middle plate contents: heart icon and its text

**Static throughout.** Off-white field; Dr. Rehan; all three plates; connector; top plate text; camera

**Purpose.** Name the second factor on its word, reusing the same heart shape drawn in SH01

**Arrives by.** M13 — Pop on together in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~0.8s ESTIMATED (3 words)  ·  **Exit.** ADDITIVE_REVEAL

**Assets.** E01,C01,G09,G11,T03,T04  ·  **Base image reuse.** YES

**Revision change.** Icon KEPT - it is the IMG01 heart returning at reduced scale, which is the corpus's reuse behaviour, not a new pictogram

**Brain pattern.** MASTER_ASSETS REUSE_STATUS: ~150/448 rows carry REUSE/RECURRING. ASSET_DNA within-video reuse

### R05.3 (was F05.3) — ON_WORD_START ("quantity", w116)

**Script:** "quantity have to do with it in the"

**Exact frame.** Same field with the top plate carrying its text and the middle plate carrying its heart and text. The bottom plate is now filled: three small coffee cups drawn in a row in decreasing size at x12-26%, y54-60%, each with a coffee-brown liquid band, and editor text QUANTITY to their right inside the same plate. All three plates are now filled and the list is complete.

**Changes on entry.** Bottom plate contents: three-cup icon and its text

**Static throughout.** Off-white field; Dr. Rehan; all three plates; connector; top and middle plate contents; camera

**Purpose.** Complete the list - and make quantity a picture of cups, not a number

**Arrives by.** M14 — Pop on together in one frame, 1 frame (0.042s ESTIMATED)

**Hold.** ~2.0s ESTIMATED (8 words)  ·  **Exit.** STATE_REPLACEMENT

**Assets.** E01,C01,G09,G11,G12,T03,T04,T05  ·  **Base image reuse.** YES

**Revision change.** Icon KEPT - it repeats the already-established mug rather than introducing a new shape

**Brain pattern.** MASTER_MOTIONS countable-group reveals. MEDICAL GUARDRAIL: no count label, no millilitres, no dose figure

### R05.4 (was F05.4) — ON_WORD_START ("full", w124)

**Script:** "full video. Watch it on the channel."

**Exact frame.** Same off-white field with Dr. Rehan unchanged at x66-92%, y58-92%. The three plates, all their contents and the connector line are gone. In their place a single blank rounded rectangle, thin black outline, sits at x8-58%, y28-54%, with a hollow black triangular play mark centred inside it pointing right. Editor text WATCH THE FULL VIDEO sits below the rectangle at x8-58%, y58-63%. Same off-white field, same line weight, same doctor. No logo, no channel art, no colour panel.

**Changes on entry.** Three plates, contents and connector removed; video card, play mark and CTA text added in their place

**Static throughout.** Off-white field; Dr. Rehan; camera

**Purpose.** Hand off to the full video without leaving the visual language the rest of the Short is written in

**Arrives by.** M15 — Replace in one frame (state replacement), 1 frame (0.042s ESTIMATED)

**Hold.** ~1.8s ESTIMATED (7 words), held to the end  ·  **Exit.** END_OF_VIDEO

**Assets.** E01,C01,G13,T06  ·  **Base image reuse.** YES

**Revision change.** UNCHANGED, with its weakness restated: the swap mechanism is precedented but no corpus video ends on a CTA, so the content of this state is grammar-transferred rather than evidenced

**Brain pattern.** DECISION_RULES 3 STATE_REPLACEMENT 230/438; MASTER_SHOTS 15/200 shots have an empty TRANSITION_OUT

## Motions

| ID | On word | Moving element | Action | Duration | Static anchors | Build |
|---|---|---|---|---|---|---|
| M12 (was A14) | ON_WORD_START ("blood", w111) | BLOOD PRESSURE text (T03) | Pop on in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; Dr. Rehan; all three plates; connector line; camera | CAPCUT |
| M13 (was A15) | ON_WORD_START ("heart", w113) | Heart icon (G11) and HEART RESPONSE text (T04) | Pop on together in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; Dr. Rehan; all three plates; connector; top plate text; camera | CAPCUT |
| M14 (was A16) | ON_WORD_START ("quantity", w116) | Three-cup icon (G12) and QUANTITY text (T05) | Pop on together in one frame | 1 frame (0.042s ESTIMATED) | Off-white field; Dr. Rehan; all three plates; connector; top and middle plate contents; camera | CAPCUT |
| M15 (was A17) | ON_WORD_START ("full", w124) | The three list plates, all their contents and the connector line are removed; the video card, play mark (G13) and WATCH THE FULL VIDEO text (T06) appear in their place | Replace in one frame (state replacement) | 1 frame (0.042s ESTIMATED) | Off-white field; Dr. Rehan; camera | CAPCUT |

**M12** — Mechanism unchanged; what it reveals is reduced. A dial with a needle and a tick has no analogue in 448 corpus assets and reads as a measured value against a threshold, neither of which the narration supplies. At a 0.5s hold, text alone is also the more legible option on a phone  *Revision:* GAUGE ICON G10 REMOVED from this reveal - text only now

**M13** — Icon and its label are one unit and must not stagger. The icon survives review because it is the SH01 heart returning at reduced scale - the corpus's own reuse behaviour, not a new pictogram  *Revision:* UNCHANGED

**M14** — Same coupling rule as M13. The icon survives because it repeats the already-established mug, and three cups in decreasing size carries how-much with no dose figure  *Revision:* UNCHANGED

**M15** — A whole-column swap with the doctor held static is the clearest possible signal that the same person is still talking, now pointing at a video. The mechanism is the corpus's dominant one; the thing revealed has no corpus precedent, which stays flagged rather than resolved  *Revision:* UNCHANGED

---

# Asset build list

25 assets. 1 opaque environment, 3 characters, 2 objects, 12 graphics, 6 text
layers, 1 audio track.

| ID | Type | Format | Transparent | Build | Revision change |
|---|---|---|---|---|---|
| E01 | ENVIRONMENT | PNG or solid colour layer | NO (full-frame) | Solid fill in the editor, or one flat PNG | TYPE renamed BACKGROUND -> ENVIRONMENT to match the corpus TYPE vocabulary (ENVIRONMENT 91 rows; BACKGROUND does not exist) |
| C01 | CHARACTER | Transparent PNG, 3 pose variants | YES | Draw transparent line art | UNCHANGED |
| C02 | CHARACTER | Transparent PNG | YES | Draw transparent line art | UNCHANGED |
| C03 | CHARACTER | Transparent PNG, ONE instance | YES | Draw transparent line art once, duplicate the layer in the editor | BUILD METHOD TIGHTENED: the first pass described 'two identical figures' as one asset, which invited generating them as a pair. Image models cannot reliably produce two pixel-identical figures. Generate one, duplicate it. |
| O01 | OBJECT | Transparent PNG | YES | Draw transparent line art | UNCHANGED |
| O02 | OBJECT | Transparent PNG | YES | Draw transparent line art | UNCHANGED |
| G01 | GRAPHIC | Transparent PNG | YES | Draw transparent line art | UNCHANGED |
| G02 | GRAPHIC | Transparent PNG, 2 layers | YES | Draw transparent line art | UNCHANGED |
| G03 | GRAPHIC | Transparent PNG | YES | Draw transparent line art | REUSE COUNT REDUCED from 2 to 1 - the SH03 strike (F03.2 / A09) was removed as redundant |
| G04 | GRAPHIC | Transparent PNG, 2 groups | YES | Draw transparent line art | UNCHANGED |
| G05 | GRAPHIC | Transparent PNG | YES | Draw transparent line art | PRECEDENT STATUS UPGRADED - warning triangles are directly precedented in three corpus videos; the corpus draws them in black, and muted red here is a stated guardrail departure |
| G06 | GRAPHIC | Transparent PNG, one group | YES | Draw transparent line art | UNCHANGED - but note it is now removed one word-onset earlier (M09 on 'not', w70) |
| G07 | GRAPHIC | Transparent PNG, 2 mirrored | YES | Draw transparent line art | BUILD SIMPLIFIED: the first pass's fallback plan required per-segment PNGs to fake a curved draw. With M10/M11 now one-frame pops, one complete stroke per arrow is all that is needed. |
| G08 | GRAPHIC | Transparent PNG, 2 versions | YES | Draw transparent line art | UNCHANGED |
| G09 | GRAPHIC | Transparent PNG, one group | YES | Draw transparent line art | UNCHANGED |
| G11 | GRAPHIC | Transparent PNG (rescaled G01) | YES | Rescale G01 | TYPE renamed MEDICAL_SYMBOL -> GRAPHIC (no MEDICAL_SYMBOL type exists in the corpus's 448 assets). Asset itself unchanged. |
| G12 | GRAPHIC | Transparent PNG | YES | Rescale and repeat O01 | TYPE renamed CAFFEINE_SYMBOL -> GRAPHIC (no such type exists in the corpus). Asset itself unchanged. |
| G13 | GRAPHIC | Transparent PNG | YES | Draw transparent line art | TYPE renamed CTA_ELEMENT -> GRAPHIC (no such type exists in the corpus). Asset itself unchanged. |
| T01 | TEXT_SYSTEM | Native editor text layer | N/A | CapCut native text | TYPE renamed TEXT_OVERLAY -> TEXT_SYSTEM to match the corpus vocabulary (TEXT_SYSTEM 21 rows) |
| T02 | TEXT_SYSTEM | Native editor text layer | N/A | CapCut native text | TYPE renamed TEXT_OVERLAY -> TEXT_SYSTEM |
| T03 | TEXT_SYSTEM | Native editor text layer | N/A | CapCut native text | TYPE renamed; now the ONLY content of the top plate since the gauge icon was removed |
| T04 | TEXT_SYSTEM | Native editor text layer | N/A | CapCut native text | TYPE renamed TEXT_OVERLAY -> TEXT_SYSTEM |
| T05 | TEXT_SYSTEM | Native editor text layer | N/A | CapCut native text | TYPE renamed TEXT_OVERLAY -> TEXT_SYSTEM |
| T06 | TEXT_SYSTEM | Native editor text layer | N/A | CapCut native text | TYPE renamed TEXT_OVERLAY -> TEXT_SYSTEM |
| AU01 | AUDIO | Audio file | N/A | Supplied recording | UNCHANGED |

**Deleted from the first pass:** G10, the blood-pressure gauge icon.

**Asset TYPE values were renamed** to the corpus's own vocabulary. The first
pass invented `BACKGROUND`, `MEDICAL_SYMBOL`, `CAFFEINE_SYMBOL`, `CTA_ELEMENT`
and `TEXT_OVERLAY`; none of the five exists among the brain's 448 catalogued
assets, whose TYPE column runs GRAPHIC (146), ENVIRONMENT (91), OBJECT (91),
CHARACTER (50), TEXT_SYSTEM (31 across three spellings) and AUDIO (14). The
assets themselves did not change — only their classification, so that the plan
is legible to anyone reading it alongside the brain.

# Text layers

Six strings. Every one is a native editor text layer; none is generated in an
image.

| ID | Text | Appears on | Position | Removed on |
|---|---|---|---|---|
| T01 | `GOOD?` | ON_WORD_START ("good", w3) | Centred inside the left label plate (SH01 x10-40%, y56-66%; SH03 x24-46%, y34-44%) | R03.2 (removed with the whole diagram, on "not" w70) |
| T02 | `BAD?` | ON_WORD_START ("bad", w7) | Centred inside the right label plate (SH01 x60-90%, y56-66%; SH03 x54-76%, y34-44%) | R03.2 (removed with the whole diagram, on "not" w70) |
| T03 | `BLOOD PRESSURE` | ON_WORD_START ("blood", w111) | Left-aligned inside the top list plate at x12-56%, y22-28% - the plate's only content | R05.4 (removed with the list, on "full" w124) |
| T04 | `HEART RESPONSE` | ON_WORD_START ("heart", w113) | Inside the middle list plate, right of the heart icon (x26-56%, y39-43%) | R05.4 (removed with the list, on "full" w124) |
| T05 | `QUANTITY` | ON_WORD_START ("quantity", w116) | Inside the bottom list plate, right of the cup icons (x30-56%, y55-59%) | R05.4 (removed with the list, on "full" w124) |
| T06 | `WATCH THE FULL VIDEO` | ON_WORD_START ("full", w124) - appears in the same frame as the video card and play mark, one coupled reveal | Below the video card (x8-58%, y58-63%) | (end of video) |

# Anchor words

Nineteen word onsets carry every change in the video:

`good` · `bad` · `Rehan` · `wrong` · `People` · `energy` · `stronger` ·
`dangerous` · `So` · `patients` · `not` · `The` · `respond` · `judge` ·
`Dr.` · `blood` · `heart` · `quantity` · `full`

Two first-pass anchors are gone: `That's` (w77), because the deletion moved
earlier to `not`, and `caffeine` (w91), because that reveal merged into
`respond`.

# What this plan deliberately does not do

- It does not move the camera, anywhere, ever.
- It does not fade, dissolve or cross-cut. Four hard cuts, nothing else.
- It does not animate because animation is available. Five states have no
  motion at all, and the longest single moment in the video is a 4.3-second
  ESTIMATED locked hold on two figures facing each other while a patient's
  question is spoken.
- It does not draw anything along a curved path, because the corpus does not.
- It does not generate a single frame of video.
- It does not copy a scene from any training video. No composition here
  reproduces a corpus shot; the transfer is of grammar — word-onset anchoring,
  one-frame change, locked camera, hard cut, additive reveal into reserved
  negative space, group removal — not of remembered images.
- It does not put a number, a threshold, a diagnosis or a recommendation on
  screen.
- It does not claim the brain generalises. That is the human reviewer's call,
  on this evidence.
