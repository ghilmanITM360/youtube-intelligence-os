# PRODUCTION-READY VISUAL PACK — Coffee / Heart Short

**Single document. Follow it top to bottom to make the whole Short.**
No CSV needs to be opened to produce this video.

- **Authority:** `../revision_1/` (Revision 1, frozen). This pack reformats it
  for production. It adds no states, no motions and no design decisions.
- **Grammar reference, read-only:** `releases/production_intelligence_brain-v1.0.0/`
- **Format:** 9:16 vertical, 2160 × 3840
- **Counts:** 5 visuals · 20 states · 5 base images · 15 animations · 0 I2V · 0 camera moves · 0 fades
- **Verified against Revision 1 files:** shots 5, states 20, base images 5, motions 15, assets 25, text overlays 6, anchor words 19. No discrepancy.

### What this pack adds (format only, no design change)

Revision 1 specified five overlay elements by exact coordinates but never wrote
generation prompts for them, because they were described as parts of base
plates. They are listed in Revision 1 as independently switchable layers, so
they need prompts. Written here, geometry copied verbatim:

`G02a` · `G02b` (the two fork halves) · `G04b` (the can's four strokes) ·
`IMG03_diagram` · `IMG05_plates` (the two split exports Revision 1's
executability check already requires).

Marked **[PROMPT ADDED]** where they appear. Nothing else is new.

---

## THE SCRIPT — DO NOT CHANGE

> Is coffee good for your heart—or bad for it? Dr. Rehan says that's actually the wrong question.
>
> People usually ask me, then what about the energy drinks? So, energy drinks for me are much stronger than coffee and they are a bit more dangerous than coffee as well.
>
> So now, if the patients ask me, so is coffee good or bad for your health? I tell them that should not be the question to be asked. That's a wrong question. The real question is, how does your body respond to caffeine or coffee?
>
> And that's the main message: don't judge coffee only as "good" or "bad." Dr. Rehan explains what blood pressure, heart response and quantity have to do with it in the full video. Watch it on the channel.

130 words. Not one word is rewritten, shortened or expanded anywhere in this
pack.

---

## GLOBAL SPECIFICATIONS

**Canvas:** 2160 × 3840 px, 9:16 vertical.

**Background:** flat warm off-white, full frame, no texture, gradient,
vignette or border. One value everywhere, all five images.

**Style — written into every image prompt in this document:**
thin black hand-drawn linework, slightly imperfect naturally uneven strokes as
if drawn quickly with a fine marker; uniform line weight throughout; flat 2D;
no perspective, no shading, no lighting, no shadows, no glow, no 3D;
large areas of empty off-white; strong readable silhouettes at phone size.

**Colour — the only two colours in the project:**

| Colour | Used for | Never used for |
|---|---|---|
| Flat coffee brown | The liquid band inside a cup. Nothing else | Anything else |
| Muted medical red | Strike stroke, caution triangle, response arcs. All three are editor overlays | Any base image. **No red is generated into any plate** |

**Text:** never generated in an image. All six text elements are CapCut native
text layers. One text style for all six.

**Camera:** locked and static in all five visuals. Zero pans, zooms, pushes,
tilts, parallax or shake.

**Transitions:** hard cuts only, four of them. No transition effect is applied
anywhere. No fades.

**Timing:** all durations are ESTIMATED from 3.93 words/sec and are labelled as
such. **Every operation is anchored to a spoken word, never to a timestamp.**
Scrub the narration, find the onset frame of the anchor word, place the
operation on that frame — no offset padding.

---

# VISUAL 01 — The binary question

```
Shot: SH01      Base image: IMG01 (NEW)
States: R01.0 → R01.1 → R01.2 → R01.3 → R01.4   (5)
Animations: M01 M02 M03 M04   (4)
Words: w1–w17     Est. duration 4.33s ESTIMATED
```

### NARRATION

> "Is coffee good for your heart—or bad for it? Dr. Rehan says that's actually the wrong question."

### PURPOSE

Build the good-or-bad model in the viewer's head, then have the named doctor
strike it out.

### STARTING FRAME

Flat off-white portrait field. A coffee mug seen from the side, black outline,
handle on its right, sits centred in the upper third at **x36–64%, y18–30%**;
inside its top rim a flat coffee-brown horizontal band at x39–61%, y19–22% —
the only colour in frame. Directly below it, a single-stroke symmetrical
outline heart, not filled, at **x42–58%, y34–43%**. The mug is roughly twice
the heart's width.

**Everything below y44% is empty off-white — the bottom 56% of the frame is
blank.** No text. No arrows. No lines. No figures. No other objects.

### BASE IMAGE TO CREATE

```
NEW BASE IMAGE — IMG01
```

### BASE IMAGE PROMPT

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

### SEPARATE ASSETS / OVERLAYS

```
Overlay A — G02a  fork left half   (left branch line + blank left label plate)
Overlay B — T01   text  GOOD?      (CapCut text, not an image)
Overlay C — G02b  fork right half  (right branch line + blank right label plate)
Overlay D — T02   text  BAD?       (CapCut text, not an image)
Overlay E — C01   Dr. Rehan, arm-raised pose
Overlay F — G03   muted-red strike stroke
```

**Must NOT be in IMG01:** the fork lines, either label plate, any text, the
doctor, the red strike.

**Overlay A — G02a fork left half** — [PROMPT ADDED]

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven strokes, flat 2D, no shading. Draw one thin straight line
> descending diagonally from a point at 50% width / 44% height down to the left,
> ending at 18% width / 56% height. At its lower end, draw one rounded-rectangle
> plate spanning 10–40% of the width and 56–66% of the height, as a thin black
> outline with a completely empty interior. Exactly one line and one empty
> plate. No text, no letters, no second line, no second plate, no arrowheads,
> no colour, no background, no shadow.

**Overlay C — G02b fork right half** — [PROMPT ADDED]

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven strokes, flat 2D, no shading. Draw one thin straight line
> descending diagonally from a point at 50% width / 44% height down to the
> right, ending at 82% width / 56% height. At its lower end, draw one
> rounded-rectangle plate spanning 60–90% of the width and 56–66% of the
> height, as a thin black outline with a completely empty interior. It must be
> identical in size, corner radius and stroke weight to a plate spanning
> 10–40% of the width at the same height. Exactly one line and one empty plate.
> No text, no letters, no second line, no second plate, no arrowheads, no
> colour, no background, no shadow.

**Overlay E — C01 Dr. Rehan, arm-raised**

> Minimal stick figure of a male doctor on a fully transparent background, thin
> black hand-drawn linework with slightly uneven strokes, flat 2D, no shading.
> Plain round circle head, two small rectangular spectacle lenses joined by a
> bridge, short solid black beard as a filled arc under the chin, one short
> curved side-swept hair stroke on top. No mouth, eyes, nose or other facial
> detail. Single-stroke body, simple straight legs; the near arm is raised at
> about 45 degrees pointing up and to the right, the far arm hangs down. Facing
> right. No coat, no stethoscope, no clipboard, no text, no colour, no
> background, no shadow.

**Overlay F — G03 strike stroke**

> One single thick hand-drawn diagonal stroke in muted medical red on a fully
> transparent background, rising slightly from lower-left to upper-right, with
> slightly uneven weight and a natural tapered end. It is one stroke only — not
> a cross, not an X, not a line with an arrowhead. No text, no second colour,
> no background, no shadow.

### STATE SEQUENCE

**R01.0 — opening frame**
```
Visible:    off-white field, mug, heart
Added:      —
Removed:    —
Moved:      —
Unchanged:  (first frame of the video)
```

**R01.1 — on "good"**
```
Visible:    field, mug, heart, left fork line, left plate, GOOD?
Added:      G02a left branch + left plate; T01 text GOOD? inside it
Removed:    —
Moved:      nothing
Unchanged:  mug, heart, field, camera
```
Two straight thin lines now descend from the heart's bottom point at x50%,y44%
— one to x18%,y56%, one to x82%,y56% — forming a wide inverted V. Only the
left one ends in a plate. The right line ends in empty field.

**R01.2 — on "bad"**
```
Visible:    field, mug, heart, both fork lines, both plates, GOOD?, BAD?
Added:      G02b right plate; T02 text BAD? inside it
Removed:    —
Moved:      nothing
Unchanged:  mug, heart, left plate, GOOD?, field, camera
```
The model is now symmetrical: one mug, one heart, two branches, two labels.
Below y68% still empty.

**R01.3 — on "Rehan"**
```
Visible:    everything above, plus Dr. Rehan lower-left
Added:      C01 at x8–30%, y70–95%, facing right, near arm raised toward the fork
Removed:    —
Moved:      nothing
Unchanged:  entire model, field, camera
```
Lower-right field stays empty.

**R01.4 — on "wrong"**
```
Visible:    everything above, plus the red strike
Added:      G03 — one thick muted-red stroke from x14%,y68% up to x86%,y52%,
            crossing both branch lines and clipping the top edge of both plates
Removed:    —
Moved:      nothing
Unchanged:  mug, heart, fork, both plates, both text labels, Dr. Rehan, camera
```
Both labels stay legible under the stroke. Held to the cut.

### ANIMATION

```
Animation ID:      M01
Trigger:           ON "good" (w3)
Moving element:    G02a fork-left group + T01 GOOD?
Action:            Appear — both in the same frame
Duration behavior: 1 frame. Instant
Static elements:   Off-white field, mug, heart
Camera:            Locked
Tool:              CAPCUT — visibility switch on two layers, same frame
```
```
Animation ID:      M02
Trigger:           ON "bad" (w7)
Moving element:    G02b fork-right group + T02 BAD?
Action:            Appear — both in the same frame
Duration behavior: 1 frame. Instant
Static elements:   Field, mug, heart, fork lines, left plate, GOOD?
Camera:            Locked
Tool:              CAPCUT — visibility switch on two layers, same frame
```
```
Animation ID:      M03
Trigger:           ON "Rehan" (w11)
Moving element:    C01 Dr. Rehan
Action:            Appear. No walk-in, no slide, no scale-up
Duration behavior: 1 frame. Instant
Static elements:   Field, mug, heart, fork, both plates, both labels
Camera:            Locked
Tool:              CAPCUT — visibility switch
```
```
Animation ID:      M04
Trigger:           ON "wrong" (w16)
Moving element:    G03 red strike stroke
Action:            Draws on left → right along its own straight path
Duration behavior: 4 frames (0.167s ESTIMATED), then holds. Completes before
                   the next word. NOT spread across the phrase
Static elements:   Everything else in frame, including Dr. Rehan
Camera:            Locked
Tool:              CAPCUT — linear left-to-right wipe mask over the static PNG,
                   animated across 4 frames only
```

### SHORT ANIMATION PROMPT

*M01–M03:* The fork half, then the second label, then the doctor each appear
instantly in a single frame, one per spoken word. Nothing else in the frame
changes and nothing moves. No camera motion.

*M04:* The red strike draws left to right across both answer branches in four
frames, then stops. Mug, heart, labels, doctor and background stay completely
static. No camera motion.

### NARRATION TRIGGERS

```
ON "good"    (w3)   → fork left half + GOOD?
ON "bad"     (w7)   → fork right half + BAD?
ON "Rehan"   (w11)  → Dr. Rehan appears
ON "wrong"   (w16)  → red strike draws (4 frames)
```

### TRANSITION TO NEXT VISUAL

```
HARD CUT on "People" (w18)
```
No transition effect. Butt cut.

### BUILD METHOD

```
CAPCUT
```

---

# VISUAL 02 — Coffee versus the can

```
Shot: SH02      Base image: IMG02 (NEW)
States: R02.0 → R02.1 → R02.2 → R02.3   (4)
Animations: M05 M06 M07   (3)
Words: w18–w48     Est. duration 7.89s ESTIMATED
```

### NARRATION

> "People usually ask me, then what about the energy drinks? So, energy drinks for me are much stronger than coffee and they are a bit more dangerous than coffee as well."

### PURPOSE

Compare coffee and an unbranded energy drink as two physical objects on one
shared baseline — strength first, then a single restrained caution.

### STARTING FRAME

Flat off-white portrait field. A thin horizontal black ground line runs across
**x8–92% at y70%** — no ticks, no arrowheads, no labels. Standing on its left
portion, a coffee mug seen from the side, handle on its right, at **x14–40%,
y52–70%**, with a flat coffee-brown liquid band at x17–34%, y53–56%. Above the
mug, **exactly two** short straight black strokes radiating upward and slightly
outward, evenly spaced, equal length, at **x20–34%, y42–50%** — a small
activity mark.

**The right half of the ground line, from x50% to x92%, is completely bare.
The whole field above y42% is empty off-white.** No text. No second container.

### BASE IMAGE TO CREATE

```
NEW BASE IMAGE — IMG02
```

### BASE IMAGE PROMPT

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

### SEPARATE ASSETS / OVERLAYS

```
Overlay A — O02   energy-drink can, unbranded
Overlay B — G04b  the can's four stimulation strokes (one group)
Overlay C — G05   muted-red caution triangle
```

**Must NOT be in IMG02:** the can, the can's four strokes, the caution
triangle. **No text at all in this visual.**

**Overlay A — O02 energy-drink can**

> A tall plain beverage can on a fully transparent background, thin black
> hand-drawn linework with slightly uneven strokes, flat 2D, no shading.
> Straight cylindrical body, rounded top rim with a small oval pull-tab, one
> plain horizontal band across the middle of the can, and completely blank
> sides. No logo, no brand name, no lettering, no numbers, no graphics, no
> colour fill, no background, no shadow. It must not resemble any real product.

Place at x60–86%, y44–70% — standing on the same baseline, visibly taller than
the mug.

**Overlay B — G04b the can's four strokes** — [PROMPT ADDED]

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven strokes, flat 2D, no shading. Draw exactly four short
> straight strokes radiating upward and slightly outward, evenly spaced in a
> row, all four exactly the same length as each other. Nothing else. No can, no
> cup, no object beneath them, no text, no numbers, no arrows, no colour, no
> background, no shadow.

Place at x62–84%, y28–42%. **The individual stroke length must match the two
strokes above the mug in IMG02** — the comparison is *four instead of two*,
not *bigger*. Draw the mug's two and the can's four in one sitting so the
weight and length match, then export the four as this overlay.

**Overlay C — G05 caution triangle**

> A simple warning triangle on a fully transparent background, drawn as a muted
> medical red outline only with no fill, thin hand-drawn linework with slightly
> uneven strokes, flat 2D. Inside it, one short vertical stroke with a dot
> below it. Nothing else. No text, no second colour, no black outline, no
> background, no shadow, no glow.

Place at x66–80%, y14–25% — above the can's strokes, over the can only.

### STATE SEQUENCE

**R02.0 — opening frame of the shot**
```
Visible:    field, baseline, mug, the mug's two strokes
Added:      —
Removed:    —
Moved:      —
Unchanged:  (hard cut in)
```

**R02.1 — on "energy"**
```
Visible:    above, plus the can
Added:      O02 at x60–86%, y44–70%, on the same baseline, taller than the mug
Removed:    —
Moved:      nothing
Unchanged:  field, baseline, mug, mug strokes, camera
```
Field above y42% still empty.

**R02.2 — on "stronger"**
```
Visible:    above, plus four strokes over the can
Added:      G04b — four strokes at x62–84%, y28–42%
Removed:    —
Moved:      nothing
Unchanged:  field, baseline, mug, mug strokes, can, camera
```
Same stroke length as the mug's, four of them, group sitting higher in frame.
The two groups read as the same unit counted twice over.

**R02.3 — on "dangerous"**
```
Visible:    above, plus the caution triangle
Added:      G05 at x66–80%, y14–25%
Removed:    —
Moved:      nothing
Unchanged:  everything else, camera
```
The space above the mug stays empty. No colour wash, no background change.
Held to the cut.

### ANIMATION

```
Animation ID:      M05
Trigger:           ON "energy" (w26)
Moving element:    O02 can
Action:            Appear at its exact position. No drop-in, no bounce, no scale
Duration behavior: 1 frame. Instant
Static elements:   Field, baseline, mug, the mug's two strokes
Camera:            Locked
Tool:              CAPCUT — visibility switch
```
```
Animation ID:      M06
Trigger:           ON "stronger" (w35)
Moving element:    G04b — all four strokes as one group
Action:            Appear together. They must NOT stagger one by one
Duration behavior: 1 frame. Instant
Static elements:   Field, baseline, mug, mug strokes, can
Camera:            Locked
Tool:              CAPCUT — one visibility switch on one grouped layer
```
```
Animation ID:      M07
Trigger:           ON "dangerous" (w44)
Moving element:    G05 caution triangle
Action:            Appear. No pulse, no flash, no shake, no scale, no glow
Duration behavior: 1 frame. Instant, then static
Static elements:   Everything else in frame
Camera:            Locked
Tool:              CAPCUT — visibility switch, no effects
```

### SHORT ANIMATION PROMPT

The can appears on the baseline in one frame; later its four strength strokes
appear together in one frame; later one small red caution triangle appears
above it in one frame. The coffee mug, its two strokes, the baseline and the
background never change. No camera motion, no pulsing, no effects.

### NARRATION TRIGGERS

```
ON "People"    (w18)  → hard cut into this visual
ON "energy"    (w26)  → can appears
ON "stronger"  (w35)  → the can's four strokes appear together
ON "dangerous" (w44)  → caution triangle appears
```

### TRANSITION TO NEXT VISUAL

```
HARD CUT on "So" (w49)
```

### BUILD METHOD

```
CAPCUT
```

---

# VISUAL 03 — The consultation, and the deletion

```
Shot: SH03      Base image: IMG03 (NEW — export as TWO files)
States: R03.0 → R03.1 → R03.2   (3)
Animations: M08 M09   (2)
Words: w49–w80     Est. duration 8.14s ESTIMATED
```

### NARRATION

> "So now, if the patients ask me, so is coffee good or bad for your health? I tell them that should not be the question to be asked. That's a wrong question."

### PURPOSE

Re-stage the good-or-bad model as a real consultation, then delete it outright
in front of the person who asked.

### STARTING FRAME

Flat off-white portrait field. Dr. Rehan stands at **x6–28%, y58–92%** facing
frame-right, arms at his sides — round head, rectangular glasses, short filled
beard, side-swept hair stroke, single-stroke body.

Upper-centre holds a **compact** version of the binary diagram: a small coffee
mug at **x44–56%, y14–23%** with a coffee-brown band, two thin black lines
descending from its base outward to two blank rounded label plates at
**x24–46%** and **x54–76%**, both at **y34–44%**, carrying the text **GOOD?**
and **BAD?**.

**The entire right-hand lower field below y50% is empty off-white** — that is
where the patient will stand.

Note: unlike VISUAL 01, both labels are already visible at the first frame.
This is a recall of a model the viewer already owns, not a fresh build.

### BASE IMAGE TO CREATE

```
NEW BASE IMAGE — IMG03
```
**Generate once, then export as two files at the same 2160 × 3840 canvas:**

```
IMG03_base     off-white field + Dr. Rehan only
IMG03_diagram  the mug + two lines + two empty plates, on transparency
```

This is mandatory, not optional. The doctor and the diagram sit in one
composition but only the diagram is deleted at "not" — a single opacity switch
on a combined plate would take the doctor with it.

### BASE IMAGE PROMPT

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

**If the split export is not possible from the generated file**, generate the
diagram separately with this prompt — [PROMPT ADDED]:

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven strokes, flat 2D, no shading. At the top, spanning 44–56% of
> the width and 14–23% of the height of a 2160 × 3840 vertical canvas, draw a
> small coffee mug seen from the side with a round handle on its right and a
> flat coffee-brown horizontal band inside its top rim. From the bottom of the
> mug, two thin straight black lines descend outward, one to the left and one
> to the right, each ending at the top edge of a rounded-rectangle plate. The
> left plate spans 24–46% of the width, the right plate 54–76%, both at 34–44%
> of the height, both thin black outlines with completely empty interiors,
> identical in size and corner radius. Nothing else on the canvas. No text, no
> letters, no figures, no strike stroke, no background, no shadow.

### SEPARATE ASSETS / OVERLAYS

```
Overlay A — C02  patient figure
Overlay B — T01  text  GOOD?   (repositioned for this shot)
Overlay C — T02  text  BAD?    (repositioned for this shot)
Overlay D — IMG03_diagram      the removable diagram group
```

**Must NOT be in IMG03_base:** the diagram, any text, the patient.
**Must NOT be anywhere in this visual: a red strike.** VISUAL 01 taught the
strike; this visual escalates to deletion instead of repeating the mark.

**Overlay A — C02 patient**

> Minimal stick figure of a person on a fully transparent background, thin
> black hand-drawn linework with slightly uneven strokes, flat 2D, no shading.
> Plain round circle head with no face at all — no glasses, no beard, no hair,
> no features. Single-stroke body, simple straight legs; the near arm is
> slightly raised as if asking a question. Facing left. No clothing detail, no
> text, no colour, no background, no shadow.

Place at x72–94%, y60–92%, facing the doctor.

### STATE SEQUENCE

**R03.0 — opening frame of the shot**
```
Visible:    field, Dr. Rehan, compact diagram, both plates, GOOD?, BAD?
Added:      —
Removed:    —
Moved:      —
Unchanged:  (hard cut in)
```

**R03.1 — on "patients"**
```
Visible:    above, plus the patient
Added:      C02 at x72–94%, y60–92%, facing left toward the doctor
Removed:    —
Moved:      nothing
Unchanged:  field, Dr. Rehan, diagram, plates, text, camera
```
The two figures now face each other across the diagram above them.
**Then nothing happens for roughly 4.3 seconds ESTIMATED** while the whole
question is spoken. This is the longest hold in the video. Do not fill it.

**R03.2 — on "not"**
```
Visible:    field, Dr. Rehan, the patient. Nothing else
Added:      —
Removed:    the mug, both branch lines, both plates, GOOD?, BAD? — all of it,
            in ONE frame
Moved:      nothing
Unchanged:  Dr. Rehan and the patient, both exactly where they were, still
            facing each other; field; camera
```
Two figures and a large empty field between and above them. The empty space is
the argument. Held ~2.6s ESTIMATED through "That's a wrong question."

### ANIMATION

```
Animation ID:      M08
Trigger:           ON "patients" (w53)
Moving element:    C02 patient
Action:            Appear. No walk-in
Duration behavior: 1 frame. Instant
Static elements:   Field, Dr. Rehan, diagram, plates, both text labels
Camera:            Locked
Tool:              CAPCUT — visibility switch
```
```
Animation ID:      M09
Trigger:           ON "not" (w70)
Moving element:    IMG03_diagram group + T01 + T02
Action:            Disappear — the whole group at once
Duration behavior: 1 frame. Instant. NO fade-out. NO shrink. NO wipe
Static elements:   Field, Dr. Rehan, the patient
Camera:            Locked
Tool:              CAPCUT — switch off three layers on the same frame
```

### SHORT ANIMATION PROMPT

The patient appears in one frame, then the frame holds still for several
seconds. Later the entire good/bad diagram and both its labels vanish in a
single frame, leaving the two figures untouched and the space between them
empty. No fade, no camera motion.

### NARRATION TRIGGERS

```
ON "So"       (w49)  → hard cut into this visual
ON "patients" (w53)  → patient appears
ON "not"      (w70)  → the whole diagram and both labels are deleted
```

### TRANSITION TO NEXT VISUAL

```
HARD CUT on "The" (w81)
```

### BUILD METHOD

```
CAPCUT
```

---

# VISUAL 04 — Two people, one coffee, different readings

```
Shot: SH04      Base image: IMG04 (NEW)
States: R04.0 → R04.1 → R04.2   (3)
Animations: M10 M11   (2)
Words: w81–w106     Est. duration 6.62s ESTIMATED
```

### NARRATION

> "The real question is, how does your body respond to caffeine or coffee? And that's the main message: don't judge coffee only as \"good\" or \"bad.\""

### PURPOSE

Replace the deleted model with a new one — coffee, person, response — and show
two identical people reading the same coffee differently.

### STARTING FRAME

Flat off-white portrait field. A coffee mug, black outline, handle on its
right, with a coffee-brown band, sits centred at the **top** of the frame at
**x42–58%, y12–22%**. A thin horizontal black ground line runs across
**x10–90% at y80%**.

Two **identical** plain stick figures stand on that line, facing forward:
left at **x14–36%, y52–80%**, right at **x64–86%, y52–80%**. Both have plain
round heads with no faces, no glasses, no beards, no distinguishing marks, and
identical posture and size.

**The whole band between y24% and y50% is empty off-white.** No arrows. No
marks. No text.

### BASE IMAGE TO CREATE

```
NEW BASE IMAGE — IMG04   (mug + ground line ONLY — no figures in the plate)
```

### BASE IMAGE PROMPT

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

### SEPARATE ASSETS / OVERLAYS

```
Overlay A — C03   plain stick figure — GENERATE ONE, DUPLICATE IN CAPCUT
Overlay B — G07a  left connector arrow
Overlay C — G08a  single response arc
Overlay D — G07b  right connector arrow (mirrored)
Overlay E — G08b  three stacked response arcs
```

**Must NOT be in IMG04:** the figures, either arrow, any arc.

**Overlay A — C03 the figure — generated once**

> One minimal stick figure of a person on a fully transparent background, thin
> black hand-drawn linework with slightly uneven strokes, flat 2D, no shading.
> A plain round circle head with no face at all — no glasses, no beard, no
> hair, no eyes, no mouth, no features of any kind. A single-stroke straight
> body line, two simple straight arms hanging at the sides, two simple straight
> legs, standing upright and facing forward in a neutral posture. Exactly one
> figure. No text, no colour, no background, no shadow, no ground line, no
> second figure.

**Then in CapCut: copy the layer and change only its X position.** Place
instance A at x14–36% and instance B at x64–86%. Do not import a second file.
Do not generate a second figure.

**Overlays B & D — G07 connector arrows**

> One thin hand-drawn curved arrow in black on a fully transparent background,
> a single smooth curve with slightly uneven weight, ending in a small open V
> arrowhead. Flat 2D, no shading. No text, no colour, no double line, no
> background, no shadow. Produce one complete stroke — no partial or segmented
> versions are needed.

Generate once, mirror horizontally for the second. Left arrow curves from
x44%,y23% down-left to x28%,y58%. Right arrow curves from x56%,y23%
down-right to x72%,y58%.

**Overlays C & E — G08 response arcs**

> Short concentric arc strokes in muted medical red on a fully transparent
> background, drawn in the style of a single hand-drawn sound-wave mark, thin
> and slightly uneven. Produce two versions: one containing a single arc, and
> one containing three arcs stacked at increasing radius. No text, no numbers,
> no waveform trace, no heartbeat line, no background, no shadow.

Single arc at x22–30%, y58–63%. Three arcs at x70–80%, y55–65%. Same stroke
weight and spacing in both versions — the only difference the viewer may see
between the two people is **how many arcs**.

### STATE SEQUENCE

**R04.0 — opening frame of the shot**
```
Visible:    field, mug top-centre, ground line, both identical figures
Added:      —
Removed:    —
Moved:      —
Unchanged:  (hard cut in)
```
Nothing is decided yet. No arrows, no arcs.

**R04.1 — on "respond"**
```
Visible:    above, plus left arrow and one arc at the left figure's chest
Added:      G07a arrow from x44%,y23% curving down-left to x28%,y58%, ending in
            a small open arrowhead; AND G08a one muted-red arc at x22–30%,
            y58–63%. Both in the same frame
Removed:    —
Moved:      nothing
Unchanged:  field, ground line, mug, BOTH figures, camera
```
The right figure and the right half of the frame stay completely unmarked.
Held ~4.3s ESTIMATED.

**R04.2 — on "judge"**
```
Visible:    above, plus right arrow and three arcs at the right figure's chest
Added:      G07b mirrored arrow from x56%,y23% to x72%,y58%; AND G08b three
            stacked arcs at x70–80%, y55–65%. All four elements in the same
            frame
Removed:    —
Moved:      nothing
Unchanged:  field, ground line, mug, both figures, left arrow, left arc, camera
```
The two figures are now identical in every way except the number of arcs.
Same coffee, same arrows, different reading. Held ~1.8s ESTIMATED to the cut.

### ANIMATION

```
Animation ID:      M10
Trigger:           ON "respond" (w89)
Moving element:    G07a left arrow + G08a single arc
Action:            Appear together, complete, in one frame
Duration behavior: 1 frame. Instant. The arrow does NOT draw along its curve
Static elements:   Field, ground line, mug, both figures
Camera:            Locked
Tool:              CAPCUT — one visibility switch on a group of two layers.
                   No mask, no keyframes
```
```
Animation ID:      M11
Trigger:           ON "judge" (w100)
Moving element:    G07b right arrow + G08b three arcs
Action:            Appear together, complete, in one frame
Duration behavior: 1 frame. Instant. The arrow does NOT draw along its curve
Static elements:   Field, ground line, mug, both figures, left arrow, left arc
Camera:            Locked
Tool:              CAPCUT — one visibility switch on a group of two layers.
                   No mask, no keyframes
```

**Why no draw-on here.** CapCut masks are linear and shape-based; they cannot
follow an arbitrary curve. And the corpus reveals curved arrows as completed
groups in a few frames rather than tracing them. The corpus-faithful answer
and the buildable answer are the same answer. Both sides use the identical
mechanism, which is what makes the two readings genuinely comparable in the
finished edit.

### SHORT ANIMATION PROMPT

The left arrow and one red arc appear together, already complete, in a single
frame. Later the mirrored right arrow and three red arcs appear together in a
single frame. The mug, the ground line, both stick figures and the background
never move or change. No stroke animation, no camera motion.

### NARRATION TRIGGERS

```
ON "The"     (w81)   → hard cut into this visual
ON "respond" (w89)   → left arrow + one arc appear together
ON "judge"   (w100)  → right arrow + three arcs appear together
```

### TRANSITION TO NEXT VISUAL

```
HARD CUT on "Dr." (w107)
```

### BUILD METHOD

```
CAPCUT
```

---

# VISUAL 05 — The three factors, and the handoff

```
Shot: SH05      Base image: IMG05 (NEW — export as TWO files)
States: R05.0 → R05.1 → R05.2 → R05.3 → R05.4   (5)
Animations: M12 M13 M14 M15   (4)
Words: w107–w130     Est. duration 6.11s ESTIMATED
```

### NARRATION

> "Dr. Rehan explains what blood pressure, heart response and quantity have to do with it in the full video. Watch it on the channel."

### PURPOSE

Name the three factors one at a time into a scaffold the viewer can already
see, then hand off to the full video.

### STARTING FRAME

Flat off-white portrait field, **no colour anywhere in this plate**. Dr. Rehan
stands at **x66–92%, y58–92%** facing frame-left, arms at his sides — same
design as VISUAL 01 and VISUAL 03, mirrored.

On the left, three identical blank rounded-rectangle plates stacked vertically,
all spanning **x8–58%**: top at **y20–30%**, middle at **y36–46%**, bottom at
**y52–62%**. Evenly spaced, identical size and corner radius, thin black
outlines, **all three completely empty**. A thin vertical black connector line
runs down their left edges at **x12%, from y25% to y57%**, linking them as a
list spine.

**The lower-left field below y64% is blank.** No text. No icons.

### BASE IMAGE TO CREATE

```
NEW BASE IMAGE — IMG05
```
**Generate once, then export as two files at the same 2160 × 3840 canvas:**

```
IMG05_base     off-white field + Dr. Rehan only
IMG05_plates   the three empty plates + connector line, on transparency
```

Same reason as VISUAL 03: at "full" the whole plate column is removed and the
doctor must stay.

### BASE IMAGE PROMPT

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

**If the split export is not possible**, generate the plate column separately —
[PROMPT ADDED]:

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven strokes, flat 2D, no shading. On a 2160 × 3840 vertical
> canvas, draw three identical rounded-rectangle plates stacked vertically,
> each spanning 8–58% of the width: the top plate at 20–30% of the height, the
> middle at 36–46%, the bottom at 52–62%. All three are thin black outlines
> with completely empty interiors, evenly spaced, identical in size and corner
> radius. Draw one thin vertical black line at 12% of the width running from
> 25% to 57% of the height down their left edges. Nothing else on the canvas.
> No text, no numerals, no icons, no figure, no colour, no background, no
> shadow.

### SEPARATE ASSETS / OVERLAYS

```
Overlay A — T03   text  BLOOD PRESSURE      (CapCut text)
Overlay B — G11   heart icon                (rescaled from the VISUAL 01 heart)
Overlay C — T04   text  HEART RESPONSE      (CapCut text)
Overlay D — G12   three-cup quantity icon
Overlay E — T05   text  QUANTITY            (CapCut text)
Overlay F — G13   video card + play mark
Overlay G — T06   text  WATCH THE FULL VIDEO (CapCut text)
Overlay H — IMG05_plates  the removable plate column
```

**Must NOT be in IMG05_base:** any text, any icon, the video card, the plate
column. **Must NOT exist at all: a gauge, a dial, a needle, a meter.**

**Overlay B — G11 heart icon.** Not a new generation. Take the heart drawn for
IMG01 and rescale it to x12–22%, y38–44%.

**Overlay D — G12 quantity icon**

> Three simple coffee mugs in a row on a fully transparent background, thin
> black hand-drawn linework with slightly uneven strokes, flat 2D. Each mug is
> seen from the side with a round handle on its right and a flat coffee-brown
> horizontal band inside its top rim. They decrease in size from left to right.
> No text, no numbers, no plus or minus signs, no arrows, no background, no
> shadow.

Place at x12–26%, y54–60%. Build from the same mug drawing used everywhere
else, rescaled and repeated.

**Overlay F — G13 video card**

> One plain rounded-rectangle panel on a fully transparent background, thin
> black hand-drawn outline with slightly uneven strokes, flat 2D, completely
> empty inside except for one hollow black triangle pointing right, centred in
> the panel, drawn as a simple outline. No text, no thumbnail image, no logo,
> no channel art, no subscribe button, no colour, no background, no shadow.

Place at x8–58%, y28–54%.

### STATE SEQUENCE

**R05.0 — opening frame of the shot**
```
Visible:    field, Dr. Rehan right-facing-left, three empty plates, connector
Added:      —
Removed:    —
Moved:      —
Unchanged:  (hard cut in)
```
Three things are coming and none is named yet.

**R05.1 — on "blood"**
```
Visible:    above, plus BLOOD PRESSURE in the top plate
Added:      T03 text, left-aligned inside the top plate at x12–56%, y22–28%
Removed:    —
Moved:      nothing
Unchanged:  field, Dr. Rehan, all three plates, connector, camera
```
**No icon in this plate.** The text occupies the plate alone, so set it large.
Middle and bottom plates stay completely blank.

**R05.2 — on "heart"**
```
Visible:    above, plus the heart icon and HEART RESPONSE in the middle plate
Added:      G11 heart at x12–22%, y38–44%; T04 text to its right inside the
            same plate. Both in the same frame
Removed:    —
Moved:      nothing
Unchanged:  field, Dr. Rehan, plates, connector, top plate text, camera
```
Bottom plate still blank.

**R05.3 — on "quantity"**
```
Visible:    above, plus the three-cup icon and QUANTITY in the bottom plate
Added:      G12 three cups at x12–26%, y54–60%; T05 text to their right. Both
            in the same frame
Removed:    —
Moved:      nothing
Unchanged:  everything above, camera
```
All three plates are now filled. The list is complete.

**R05.4 — on "full"**
```
Visible:    field, Dr. Rehan, video card with play mark, CTA text
Added:      G13 card at x8–58%, y28–54% with a hollow right-pointing play
            triangle centred inside; T06 WATCH THE FULL VIDEO at x8–58%, y58–63%
Removed:    all three plates, all their icons and text, the connector line —
            the whole left column, in ONE frame
Moved:      nothing
Unchanged:  Dr. Rehan, exactly where he was; field; camera
```
Same off-white field, same line weight, same doctor. No logo, no channel art,
no colour panel. Held to the end of the narration.

### ANIMATION

```
Animation ID:      M12
Trigger:           ON "blood" (w111)
Moving element:    T03 text BLOOD PRESSURE
Action:            Appear
Duration behavior: 1 frame. Instant
Static elements:   Field, Dr. Rehan, all three plates, connector line
Camera:            Locked
Tool:              CAPCUT — visibility switch on one text layer. Nothing else
                   appears. There is no gauge icon in this plan
```
```
Animation ID:      M13
Trigger:           ON "heart" (w113)
Moving element:    G11 heart icon + T04 text HEART RESPONSE
Action:            Appear together, in the same frame. Must NOT stagger
Duration behavior: 1 frame. Instant
Static elements:   Field, Dr. Rehan, plates, connector, top plate text
Camera:            Locked
Tool:              CAPCUT — one visibility switch on a group of two layers
```
```
Animation ID:      M14
Trigger:           ON "quantity" (w116)
Moving element:    G12 three-cup icon + T05 text QUANTITY
Action:            Appear together, in the same frame. Must NOT stagger
Duration behavior: 1 frame. Instant
Static elements:   Field, Dr. Rehan, plates, connector, top and middle contents
Camera:            Locked
Tool:              CAPCUT — one visibility switch on a group of two layers
```
```
Animation ID:      M15
Trigger:           ON "full" (w124)
Moving element:    OUT: plate column, all icons, all three list texts,
                   connector. IN: video card + play mark + CTA text
Action:            Replace — everything out and everything in on the SAME frame
Duration behavior: 1 frame. Instant. No fade, no crossfade, no slide
Static elements:   Field, Dr. Rehan
Camera:            Locked
Tool:              CAPCUT — switch off layers 3–7 and the plates group, switch
                   on layers 8–9, all on one frame
```

### SHORT ANIMATION PROMPT

Each factor's text — and for the second and third, its small icon — appears
instantly in its plate on the word that names it, one plate at a time. Then in
one frame the whole three-item column vanishes and a video card with a play
mark and a caption appears in its place. The doctor and the background never
move. No fades, no camera motion.

### NARRATION TRIGGERS

```
ON "Dr."      (w107)  → hard cut into this visual
ON "blood"    (w111)  → BLOOD PRESSURE text (text only, no icon)
ON "heart"    (w113)  → heart icon + HEART RESPONSE together
ON "quantity" (w116)  → three-cup icon + QUANTITY together
ON "full"     (w124)  → column out, video card + CTA in, same frame
```

### TRANSITION TO NEXT VISUAL

```
(none — final visual. Hold to the end of the narration, then end the video)
```

### BUILD METHOD

```
CAPCUT
```

---

# BLOOD PRESSURE — the visual cue, as Revision 1 settled it

**Not a production gap.** Revision 1 has a definite solution and it is built
above.

```
The cue for "blood pressure" is the word BLOOD PRESSURE itself,
appearing in the top list plate on the onset of "blood" (w111),
with no icon beside it.
```

The first pass had a gauge icon here — a circle dial with a needle and a tick
mark. Revision 1 deleted it on two independent grounds:

1. **Grammar.** Nothing resembling an instrument dial exists among the 448
   catalogued corpus assets. It is not a transfer from the learned style; it is
   an import from generic infographic design.
2. **Medical accuracy.** A needle resting somewhere on a dial reads as a
   *reading*. A tick mark on the rim reads as a *threshold*. The narration
   supplies neither. Directional replacements were considered and rejected for
   the same reason — an up-arrow next to BLOOD PRESSURE would assert that
   coffee raises it, which this script never says.

The text is not a weak cue here: it lands on the word, inside a plate the
viewer has already been shown, alongside two plates that do carry icons, so
the list structure does the work an icon would otherwise do. Because the text
now owns the whole plate, **set it larger than it would have been** beside an
icon.

**One thing to verify on a real phone, not a desktop preview:** the estimated
hold for `BLOOD PRESSURE` is ~0.5s before the next plate fills. That is the
tightest reading demand in the plan. If the recorded narration is faster than
estimated and 14 characters cannot be read in time, the fix is a type-size or
hold change — **not** a new icon.

---

# MEDICAL GUARDRAILS — fixed, do not relax during production

The video's whole visual argument is:

```
GOOD / BAD BINARY   →   REJECTED   →   BODY RESPONSE MATTERS
```

Nothing in the visuals may strengthen a claim the narration does not make.

| Allowed | Never |
|---|---|
| Stimulation strokes (2 for coffee, 4 for the can) | Exploding heart, skull, death imagery |
| One small muted-red caution triangle over the can | Flatlines, ECG tracings, hospital or emergency imagery |
| Unlabelled red response arcs, counted not measured | Numbers, scales, units, mmHg, milligrams, millilitres |
| Three cups in decreasing size for "quantity" | Dose figures, safe-limit marks, thresholds |
| The text BLOOD PRESSURE, alone | Gauges, dials, needles, meters, up/down arrows |

Coffee is never drawn as universally healthy and never as universally
dangerous. The energy drink is never a real product — no logo, no brand name,
no lettering, no brand colours.

---

# FINAL SANITY CHECK

| Check | Result |
|---|---|
| Every line of narration covered | **YES** — w1–w130 across 5 visuals, no gap, no overlap |
| Every visual has a base image | **YES** — IMG01–IMG05, one per visual |
| Every state represented | **YES** — all 20 (5 + 4 + 3 + 3 + 5) |
| Every surviving motion has an animation instruction | **YES** — all 15 (M01–M15) |
| Overlays that appear later separated from the base image | **YES** — no red is in any plate; no text is in any plate; no figure is in IMG04; the SH03 diagram and the SH05 plate column are separate removable files |
| Every reused asset identified | **YES** — mug (4 visuals), Dr. Rehan (3), heart (2, rescaled), C03 duplicated in-editor |
| I2V added | **NO** — 0, unchanged from Revision 1 |
| Camera movement added | **NO** — 0 |
| Fades added | **NO** — 0. Four butt cuts |
| Script wording changed | **NO** — 130 words verbatim |
| States or motions added or removed vs Revision 1 | **NO** — 20 and 15, identical |

**Known risks carried over from Revision 1, unresolved by design:**

1. All durations are ESTIMATED from 3.93 words/sec. Every operation anchors to
   a word, so nothing breaks — but recompute pacing against the real audio
   before judging it.
2. VISUAL 01 and VISUAL 05 reveal faster than the corpus's 90th percentile.
   This comes from the script's own word density, not from decoration. It is
   the most likely thing a reviewer will want to change.
3. Five plates generated separately may drift in line weight and off-white
   value. Generate all five in one session, fixed seed where available, and
   regenerate the whole set rather than one plate if any drifts.
4. The mug appears at four scales plus the three-cup icon. Draw it **once** and
   rescale.
5. The video card / CTA ending has no precedent anywhere in the corpus. It is
   drawn in the project's own line language, but it is an invention.

---

# PRODUCTION ORDER

```
STEP 1   Draw the reusable pieces first, once each:
         - the coffee mug (used at 4 scales + the 3-cup icon)
         - the heart (used in VISUAL 01 and rescaled for VISUAL 05)
         - Dr. Rehan, per DR_REHAN_CHARACTER_MASTER.md
         Keep the source files. Never redraw these.

STEP 2   Generate the five base plates in ONE session, same settings:
         IMG01, IMG02, IMG03, IMG04, IMG05.
         Compare side by side. If line weight or off-white value drifts,
         regenerate the whole set.

STEP 3   Split-export the two shared plates:
         IMG03 → IMG03_base + IMG03_diagram
         IMG05 → IMG05_base + IMG05_plates

STEP 4   Generate the transparent overlays:
         C01, C02, C03 (ONE figure), O02,
         G02a, G02b, G03, G04b, G05, G07 (one + mirror), G08 (1-arc + 3-arc),
         G11 (rescale the heart), G12, G13

STEP 5   Check every overlay: transparent background, no text baked in,
         no red in any plate, C03 is a single figure.

STEP 6   Open CapCut. Canvas 2160 × 3840. Import the narration and LOCK it.
         Mark the onset frame of all 19 anchor words.

STEP 7   Place the off-white background across the whole timeline.

STEP 8   Lay out the five visuals as butt cuts at "People", "So", "The", "Dr."
         No transition effect anywhere.

STEP 9   Per visual, build the layer stack bottom-up and set the opening
         visibility (see each visual's STATE SEQUENCE).
         VISUAL 04: duplicate the C03 layer — do not import twice.

STEP 10  Create the six text layers. One style for all six.
         BLOOD PRESSURE gets the largest size — it has a plate to itself.

STEP 11  Place every visibility switch on its marked anchor frame. No offset.

STEP 12  Build the ONE mask in the project: M04's linear left-to-right wipe on
         the red strike, 4 frames.

STEP 13  Review once at phone size with sound. Check two things only:
         does each change land on its word, and does anything move that is not
         listed as moving?
```

**Layer stacks per visual** are in `FINAL_ANIMATION_LIST.md`.
**Asset build order** is in `ASSET_CREATION_LIST.md`.
**One-page scan** is in `STORYBOARD_AT_A_GLANCE.md`.

---

**This pack generates no image files.** It is prompts, storyboard, asset plan
and animation instructions. Next step: human visual review, then image
generation.
