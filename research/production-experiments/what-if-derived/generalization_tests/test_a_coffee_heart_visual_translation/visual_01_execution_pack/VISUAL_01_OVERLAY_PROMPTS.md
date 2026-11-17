# VISUAL 01 — OVERLAY PROMPTS

Four generated overlays. All four are **transparent-background PNGs**. None of
them may be baked into IMG01 — each one appears on its own spoken word and must
be switchable on its own layer.

The two text labels (`GOOD?`, `BAD?`) are **not** generated. They are CapCut
native text — see `VISUAL_01_TEXT_OVERLAYS.md`.

```
G02a   fork left half    transparent PNG   no text   single shot
G02b   fork right half   transparent PNG   no text   single shot
C01    Dr. Rehan         transparent PNG   no text   REUSED (3 visuals)
G03    red strike        transparent PNG   no text   SINGLE USE in whole video
```

---

## G02a — fork left half

```
Purpose:            The first branch of the good/bad model. Appears on "good"
                    carrying the empty plate that T01 sits inside
Transparent BG:     YES
Contains text:      NO — the word GOOD? is a CapCut text layer placed on top
Reused later:       No. Visual 01 only
Canvas:             2160 × 3840 so it drops straight onto the timeline at 100%
```

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven natural strokes, uniform line weight, flat 2D, no shading,
> no shadow. Draw one thin straight line descending diagonally from a point at
> 50% width / 44% height down to the left, ending at 18% width / 56% height.
> At its lower end, draw one rounded-rectangle plate spanning 10–40% of the
> width and 56–66% of the height, as a thin black outline with a completely
> empty interior. Exactly one line and one empty plate. No text, no letters,
> no second line, no second plate, no arrowheads, no colour, no background,
> no shadow.

---

## G02b — fork right half

```
Purpose:            The second branch. Appears on "bad", completing the binary
Transparent BG:     YES
Contains text:      NO — BAD? is a CapCut text layer
Reused later:       No. Visual 01 only
Canvas:             2160 × 3840
```

> On a fully transparent background, thin black hand-drawn linework with
> slightly uneven natural strokes, uniform line weight, flat 2D, no shading,
> no shadow. Draw one thin straight line descending diagonally from a point at
> 50% width / 44% height down to the right, ending at 82% width / 56% height.
> At its lower end, draw one rounded-rectangle plate spanning 60–90% of the
> width and 56–66% of the height, as a thin black outline with a completely
> empty interior. It must be identical in size, corner radius and stroke weight
> to a plate spanning 10–40% of the width at the same height. Exactly one line
> and one empty plate. No text, no letters, no second line, no second plate,
> no arrowheads, no colour, no background, no shadow.

**Generate G02a and G02b in the same session.** The two plates must look like
one pair. If they differ in size or corner radius, the fork reads as lopsided
and the viewer sees a preference between the two answers.

---

## C01 — Dr. Rehan, arm-raised pose

```
Purpose:            The named doctor enters and points at the model he is
                    about to reject
Transparent BG:     YES
Contains text:      NO
Reused later:       YES — the same character design returns in VISUAL 03 and
                    VISUAL 05 in two other poses. This file is pose A.
                    Keep it. See DR_REHAN_CHARACTER_MASTER.md
Placement:          x8–30%, y70–95%, facing right
```

> Minimal stick figure of a male doctor on a fully transparent background, thin
> black hand-drawn linework with slightly uneven strokes, uniform line weight,
> flat 2D, no shading, no shadow. Plain round circle head, two small
> rectangular spectacle lenses joined by a bridge across the middle of the
> head, short solid black beard as a small filled arc under the chin, one short
> curved side-swept hair stroke on top. No mouth, no eyes, no nose, no ears, no
> other facial detail. Single-stroke body, two simple straight arms, two simple
> straight legs. The near arm is raised at about 45 degrees pointing up and to
> the right; the far arm hangs down. Facing right. No coat, no stethoscope, no
> clipboard, no badge, no text, no colour, no background, no shadow.

**Not a likeness.** Rectangular glasses plus the short beard are the whole
identity cue. Do not attempt the real person's face.

---

## G03 — red strike stroke

```
Purpose:            Rejects the good/bad binary on the word "wrong".
                    This is the moment the video turns
Transparent BG:     YES
Contains text:      NO
Reused later:       NO — Revision 1 removed the second strike.
                    This mark appears exactly ONCE in the entire video
Placement:          drawn from x14%,y68% up to x86%,y52%
```

> One single thick hand-drawn diagonal stroke in muted medical red on a fully
> transparent background, rising slightly from lower-left to upper-right, with
> slightly uneven weight and a natural tapered end. It is one stroke only — not
> a cross, not an X, not a line with an arrowhead, not a circle, not a scribble.
> No text, no second colour, no background, no shadow.

**Thickness note.** It must read at phone size as a decisive strike, and the
words `GOOD?` and `BAD?` must still be readable underneath it. Generate it
thick enough to be unmistakable, thin enough that both labels survive. Check
this on a phone with the text layers on, not in the generator preview.

---

## Not generated for Visual 01

| Item | Why |
|---|---|
| `GOOD?` / `BAD?` | CapCut text layers. Generators misrender short words, and each label must switch on its own frame |
| The mug, the heart | Already inside IMG01 |
| A second red strike | Deleted in Revision 1 |
| A cross or X shape | The mark is one stroke. A cross is a different, stronger symbol |
