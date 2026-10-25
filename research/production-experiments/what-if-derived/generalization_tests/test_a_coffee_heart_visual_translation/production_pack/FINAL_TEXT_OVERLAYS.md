# Final Text Overlays

Six text elements survive Revision 1. **All six are CapCut native text layers.
No image prompt anywhere in this pack asks a generator to render text**, because
image models render short words unreliably and every one of these must be
exact and independently switchable.

One text style for all six: same typeface, same colour (black), same weight.
Only the size differs where noted.

---

```
T01
Exact text:  GOOD?
Visual:      Black text centred inside the LEFT label plate
Trigger:     ON "good" (w3) — appears with the left fork half, same frame
Position:    VISUAL 01 — x10–40%, y56–66%
             VISUAL 03 — x24–46%, y34–44%  (repositioned, smaller plate)
Purpose:     Names the first half of the binary model on the word that says it
Removed:     ON "not" (w70), together with the whole diagram
```

```
T02
Exact text:  BAD?
Visual:      Black text centred inside the RIGHT label plate
Trigger:     ON "bad" (w7) — appears with the right label plate, same frame
Position:    VISUAL 01 — x60–90%, y56–66%
             VISUAL 03 — x54–76%, y34–44%  (repositioned, smaller plate)
Purpose:     Completes the binary, so the viewer owns the model about to be
             rejected
Removed:     ON "not" (w70), together with the whole diagram
```

Both labels reappear in VISUAL 03 already visible at the first frame of that
shot — it is a recall of a model the viewer has, not a fresh build. Set the
same style, smaller size to fit the compact plates.

```
T03
Exact text:  BLOOD PRESSURE
Visual:      Black text, left-aligned, ALONE in the top list plate. No icon
Trigger:     ON "blood" (w111)
Position:    x12–56%, y22–28%
Purpose:     Names the first of three factors without implying a value,
             a direction or a threshold
Removed:     ON "full" (w124), with the list
```
**Set this one largest.** The gauge icon was deleted in Revision 1, so the text
has the whole plate. Its estimated hold is ~0.5s before the next plate fills —
the tightest reading demand in the video. Verify on a phone, not a desktop
preview. If it cannot be read in time, change the size or the hold. **Do not
add an icon.**

```
T04
Exact text:  HEART RESPONSE
Visual:      Black text to the right of the small heart icon, inside the
             middle list plate
Trigger:     ON "heart" (w113) — appears in the same frame as the icon
Position:    x26–56%, y39–43%
Purpose:     Names the second factor, reusing the heart already drawn in
             VISUAL 01
Removed:     ON "full" (w124), with the list
```

```
T05
Exact text:  QUANTITY
Visual:      Black text to the right of the three-cup icon, inside the bottom
             list plate
Trigger:     ON "quantity" (w116) — appears in the same frame as the icon
Position:    x30–56%, y55–59%
Purpose:     Names the third factor. The cups carry how-much; no number appears
Removed:     ON "full" (w124), with the list
```

```
T06
Exact text:  WATCH THE FULL VIDEO
Visual:      Black text below the video card
Trigger:     ON "full" (w124) — same frame as the video card and play mark,
             one coupled reveal
Position:    x8–58%, y58–63%
Purpose:     Hands off to the full video
Removed:     (never — holds to the end)
```

---

## Rules

| Rule | Why |
|---|---|
| Never generated in an image | Generators misrender short words, and each of these must be removable as its own layer |
| Text matches the narration word for word | `BLOOD PRESSURE`, `HEART RESPONSE`, `QUANTITY` are spoken terms; a misrendered medical term is a factual error |
| No numbers anywhere | No mmHg, no milligrams, no millilitres, no cup counts, no thresholds. The narration supplies none |
| Appears on the word onset | Same rule as every other reveal: no offset padding |
| Icon and label never stagger | T04 and T05 appear in the same frame as their icons — they are one unit |

## Not in production

The first pass's blood-pressure gauge is deleted, so **no numeric readout, tick
mark, scale label or unit appears anywhere in the video.** No other text was
removed — all six first-pass text elements survive Revision 1 unchanged except
T03's position, which widened when the icon beside it was deleted.
