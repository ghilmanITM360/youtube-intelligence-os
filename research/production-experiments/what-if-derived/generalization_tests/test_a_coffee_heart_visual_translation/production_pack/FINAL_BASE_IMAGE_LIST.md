# Final Base Image List

Five base images. Generate all five in one session with the same settings so
line weight and off-white value match. Full prompts are repeated here so this
file stands alone.

**Every prompt below shares:** 2160 × 3840, 9:16 vertical, flat off-white
background, thin black hand-drawn linework with slightly uneven natural
strokes, flat 2D, no perspective, no shading, no texture, no gradient, no
shadow. **No text in any plate. No red in any plate.**

---

## IMG01

```
Name:            The binary question
Purpose:         Put coffee and the heart on screen, then leave the bottom
                 half of the frame empty to receive the good/bad model
Used in states:  R01.0  R01.1  R01.2  R01.3  R01.4   (VISUAL 01)
Must NOT be baked in:
                 fork lines, either label plate, GOOD?, BAD?, Dr. Rehan,
                 the red strike, any text, any red
Overlays added later:
                 G02a fork-left, T01 GOOD?, G02b fork-right, T02 BAD?,
                 C01 Dr. Rehan, G03 red strike
```

**Prompt**

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

---

## IMG02

```
Name:            Coffee alone on a baseline
Purpose:         Establish coffee with its stimulation reading already visible,
                 as the unit the can will be measured against
Used in states:  R02.0  R02.1  R02.2  R02.3   (VISUAL 02)
Must NOT be baked in:
                 the energy-drink can, the can's four strokes, the caution
                 triangle, any text, any red
Overlays added later:
                 O02 can, G04b four strokes, G05 caution triangle
```

**Prompt**

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

---

## IMG03 — split into two files

```
Name:            The consultation
Purpose:         Re-stage the binary as something a patient asks a doctor,
                 so it can be deleted in front of them
Used in states:  R03.0  R03.1  R03.2   (VISUAL 03)
EXPORT AS:       IMG03_base     off-white + Dr. Rehan only
                 IMG03_diagram  mug + two lines + two empty plates, transparent
Why split:       at "not" the diagram is deleted and the doctor stays. One
                 opacity switch on a combined plate would remove him too
Must NOT be baked in:
                 the patient, GOOD?, BAD?, any text, ANY RED STRIKE
                 (Revision 1 removed the second strike entirely)
Overlays added later:
                 C02 patient, T01 GOOD?, T02 BAD?
```

**Prompt**

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

---

## IMG04

```
Name:            Coffee above an empty stage
Purpose:         Hold the new model — one coffee, a ground line, and nothing
                 decided yet
Used in states:  R04.0  R04.1  R04.2   (VISUAL 04)
Must NOT be baked in:
                 THE TWO FIGURES (they are one PNG duplicated in the editor),
                 both arrows, all arcs, any text, any red
Overlays added later:
                 C03 figure ×2 (same layer duplicated), G07a left arrow,
                 G08a single arc, G07b right arrow, G08b three arcs
```

**Prompt**

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

**Note.** This is the one prompt Revision 1 rewrote. The first pass asked the
model for "two stick figures completely identical to each other" — no
generator delivers that reliably, and the shot's whole argument collapses if
the figures differ at all. One figure, duplicated in the editor, makes identity
structural.

---

## IMG05 — split into two files

```
Name:            Three empty factors and the doctor
Purpose:         Show that three things are coming before naming any of them
Used in states:  R05.0  R05.1  R05.2  R05.3  R05.4   (VISUAL 05)
EXPORT AS:       IMG05_base    off-white + Dr. Rehan only
                 IMG05_plates  three empty plates + connector, transparent
Why split:       at "full" the whole plate column is removed and the doctor
                 stays
Must NOT be baked in:
                 all text, the heart icon, the cup icon, the video card,
                 ANY GAUGE OR DIAL (deleted in Revision 1), any colour at all
Overlays added later:
                 T03 BLOOD PRESSURE, G11 heart + T04 HEART RESPONSE,
                 G12 three cups + T05 QUANTITY, G13 video card + T06 CTA
```

**Prompt**

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

---

## Cross-check

| | IMG01 | IMG02 | IMG03 | IMG04 | IMG05 |
|---|---|---|---|---|---|
| States served | 5 | 4 | 3 | 3 | 5 |
| Text baked in | none | none | none | none | none |
| Red baked in | none | none | none | none | none |
| Figures baked in | none | none | doctor | **none** | doctor |
| Brown band | yes | yes | yes | yes | **no colour at all** |
| Split export needed | no | no | **yes** | no | **yes** |

20 states, 5 plates, 7 exported plate files.

**Consistency warning.** These five are generated independently and must share
line weight, stroke character and off-white value. Generate them in one
session with a fixed seed where the tool allows. If one drifts, regenerate the
whole set rather than patching one plate. The mug in particular appears in all
five — draw it once and rescale rather than letting the generator re-invent it
each time.
