# Revised Image Prompts — Revision 1

One complete, standalone, production-ready prompt per BASE_IMAGE_ID, plus one
per transparent overlay element. Every prompt can be pasted into an image
generator on its own — none of them refers to another image. Reuse
relationships live in `REVISED_BASE_IMAGES.csv`, never inside a prompt.

## What changed from the first pass

| Prompt | Change |
|---|---|
| IMG01 | Unchanged |
| IMG02 | Unchanged |
| IMG03 | Unchanged prompt. Its reserved-area note drops the red strike, which no longer exists in SH03. |
| IMG04 | **Changed.** The two stick figures are removed from the base plate. The plate is now mug + baseline only, and the figures are composited as one transparent PNG placed twice. |
| IMG05 | Unchanged prompt. Its reserved-area note drops the gauge icon. |
| Overlays | **C03 added** (the single duplicated figure). **G10 deleted** (blood-pressure gauge). G07 note simplified — no segmented variants are needed now that the arrows pop rather than draw. |

**Shared canvas spec** (written into every prompt below, repeated here for
reference): 2160 × 3840 pixels, 9:16 vertical, flat off-white background, flat
2D, no perspective, no shading, no lighting, no texture, no gradient, no drop
shadow, no border, no frame.

**Shared style spec:** simple thin black hand-drawn linework with slightly
imperfect, naturally uneven strokes, as if drawn quickly by hand with a fine
marker; uniform line weight throughout; flat 2D composition; large areas of
empty off-white; every form has a strong readable silhouette at phone size.

**Accent colour discipline:** flat coffee brown appears only as the liquid
inside a cup. Muted medical red appears only on elements composited in the
editor (the strike stroke, the caution mark, the response arcs) — **no red is
generated into any base image.** No other colours anywhere.

---

## IMG01 — The binary question (SH01, states R01.0–R01.4)

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

**Reserved for later compositing:** the whole field below y44% — the fork
lines, both label plates, the GOOD?/BAD? editor text, the Dr. Rehan figure and
the red strike stroke are all added in the editor.

---

## IMG02 — Coffee alone on a baseline (SH02, states R02.0–R02.3)

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

**Reserved for later compositing:** the bare right half of the baseline (the
energy-drink can), the empty field above y42% (the can's four strokes and the
red caution triangle).

---

## IMG03 — The consultation (SH03, states R03.0–R03.2)

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

**Reserved for later compositing:** the empty right field (the patient figure)
and the blank plate interiors (GOOD?/BAD? editor text). **No red strike is
composited into this shot in Revision 1** — the diagram group is deleted
outright instead.

---

## IMG04 — Coffee above an empty stage (SH04, states R04.0–R04.2) — REVISED

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

**Reserved for later compositing:** the ground line receives the same
single-figure PNG (C03) placed twice, at x14–36% and x64–86%; the empty band
between mug and figures receives both connector arrows; the chest areas of both
figures receive the red response arcs.

**Why this prompt changed.** The first pass asked the image model for "two
stick figures that are completely identical to each other". No image model
reliably delivers pixel-identical repeated figures, and this shot's entire
argument — *same coffee, same arrows, only the number of arcs differs* —
collapses if the two figures differ at all. Generating one figure and
duplicating the layer makes identity a guarantee rather than a hope.

---

## IMG05 — Three empty factors and the doctor (SH05, states R05.0–R05.4)

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

**Reserved for later compositing:** the top plate receives the BLOOD PRESSURE
text **only, with no icon**; the middle plate receives the heart icon plus its
text; the bottom plate receives the three-cup icon plus its text; the plate
column as a whole is replaced by the video card and play mark at R05.4.

---

## Transparent overlay elements

Not base images. Each is generated or drawn once as a transparent PNG and
composited in the editor. Each prompt below is standalone.

| Asset | Prompt |
|---|---|
| **C01** Dr. Rehan, arm-raised pose (SH01) | Minimal stick figure of a male doctor on a fully transparent background, thin black hand-drawn linework with slightly uneven strokes, flat 2D, no shading. Plain round circle head, two small rectangular spectacle lenses joined by a bridge, short solid black beard as a filled arc under the chin, one short curved side-swept hair stroke on top. No mouth, eyes, nose or other facial detail. Single-stroke body, simple straight legs; the near arm is raised at about 45 degrees pointing up and to the right, the far arm hangs down. Facing right. No coat, no stethoscope, no clipboard, no text, no colour, no background, no shadow. |
| **C02** Patient (SH03) | Minimal stick figure of a person on a fully transparent background, thin black hand-drawn linework with slightly uneven strokes, flat 2D, no shading. Plain round circle head with no face at all — no glasses, no beard, no hair, no features. Single-stroke body, simple straight legs; the near arm is slightly raised as if asking a question. Facing left. No clothing detail, no text, no colour, no background, no shadow. |
| **C03** Plain figure, generated ONCE and duplicated (SH04) — **NEW** | One minimal stick figure of a person on a fully transparent background, thin black hand-drawn linework with slightly uneven strokes, flat 2D, no shading. A plain round circle head with no face at all — no glasses, no beard, no hair, no eyes, no mouth, no features of any kind. A single-stroke straight body line, two simple straight arms hanging at the sides, two simple straight legs, standing upright and facing forward in a neutral posture. Exactly one figure. No text, no colour, no background, no shadow, no ground line, no second figure. |
| **O02** Energy-drink can (SH02) | A tall plain beverage can on a fully transparent background, thin black hand-drawn linework with slightly uneven strokes, flat 2D, no shading. Straight cylindrical body, rounded top rim with a small oval pull-tab, one plain horizontal band across the middle of the can, and completely blank sides. No logo, no brand name, no lettering, no numbers, no graphics, no colour fill, no background, no shadow. It must not resemble any real product. |
| **G03** Strike stroke (SH01 only) | One single thick hand-drawn diagonal stroke in muted medical red on a fully transparent background, rising slightly from lower-left to upper-right, with slightly uneven weight and a natural tapered end. It is one stroke only — not a cross, not an X, not a line with an arrowhead. No text, no second colour, no background, no shadow. |
| **G05** Caution mark (SH02) | A simple warning triangle on a fully transparent background, drawn as a muted medical red outline only with no fill, thin hand-drawn linework with slightly uneven strokes, flat 2D. Inside it, one short vertical stroke with a dot below it. Nothing else. No text, no second colour, no black outline, no background, no shadow, no glow. |
| **G07** Connector arrow (SH04) | One thin hand-drawn curved arrow in black on a fully transparent background, a single smooth curve with slightly uneven weight, ending in a small open V arrowhead. Flat 2D, no shading. No text, no colour, no double line, no background, no shadow. Produce one complete stroke — no partial or segmented versions are needed. |
| **G08** Response arcs (SH04) | Short concentric arc strokes in muted medical red on a fully transparent background, drawn in the style of a single hand-drawn sound-wave mark, thin and slightly uneven. Produce two versions: one containing a single arc, and one containing three arcs stacked at increasing radius. No text, no numbers, no waveform trace, no heartbeat line, no background, no shadow. |
| **G11** Heart icon (SH05) | Not a new generation. Rescale the G01 heart from IMG01's overlay set to fit the middle list plate. |
| **G12** Quantity icon (SH05) | Three simple coffee mugs in a row on a fully transparent background, thin black hand-drawn linework with slightly uneven strokes, flat 2D. Each mug is seen from the side with a round handle on its right and a flat coffee-brown horizontal band inside its top rim. They decrease in size from left to right. No text, no numbers, no plus or minus signs, no arrows, no background, no shadow. |
| **G13** Video card and play mark (SH05) | One plain rounded-rectangle panel on a fully transparent background, thin black hand-drawn outline with slightly uneven strokes, flat 2D, completely empty inside except for one hollow black triangle pointing right, centred in the panel, drawn as a simple outline. No text, no thumbnail image, no logo, no channel art, no subscribe button, no colour, no background, no shadow. |

### Deleted from the first pass

**G10 blood-pressure gauge icon — removed.** The first-pass prompt asked for
"a plain circle dial with one short straight needle from its centre and a
single small tick mark on the rim". Two problems. Nothing resembling an
instrument dial exists among the brain's 448 catalogued assets, so it is not a
grammar transfer but an import from generic infographic design. And a needle
resting somewhere on a dial reads as a *reading*, while a tick mark reads as a
*threshold* — the narration supplies neither, and an image that implies both
overclaims. Directional replacements were considered and rejected for the same
reason: an up-arrow beside BLOOD PRESSURE would assert that coffee raises it,
which this script never says. The top plate carries its text alone.

**No image prompt anywhere above asks for text.** Every word that appears in
the finished video is a CapCut native text layer — see
`REVISED_TEXT_OVERLAYS.csv`.
