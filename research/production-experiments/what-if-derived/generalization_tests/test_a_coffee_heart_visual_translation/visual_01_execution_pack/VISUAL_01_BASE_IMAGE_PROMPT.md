# VISUAL 01 — BASE IMAGE PROMPT

```
Base image ID:   IMG01
Name:            The binary question
Canvas:          2160 × 3840 px, 9:16 vertical
Background:      flat warm off-white, opaque, full frame
Used in states:  R01.0  R01.1  R01.2  R01.3  R01.4  (all five)
Contains:        the coffee mug and the outline heart. Nothing else
Dr. Rehan:       NOT in the base image — he is a separate overlay (C01)
Fork lines:      NOT in the base image — separate overlays (G02a, G02b)
Labels:          NOT in the base image — CapCut text (T01, T02)
Red strike:      NOT in the base image — separate overlay (G03)
Colour:          one flat coffee-brown band inside the mug rim. No red anywhere
```

## THE PROMPT — copy from here

> A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat
> off-white background. Simple thin black hand-drawn linework with slightly
> imperfect, naturally uneven strokes, as if drawn quickly with a fine marker.
> Uniform line weight throughout. Flat 2D, no perspective, no shading, no
> lighting, no texture, no gradient, no shadow, no glow. Sparse hand-drawn
> scientific-explainer look with large areas of empty space.
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
> The mug is roughly twice the width of the heart.
>
> Everything below 44% of the image height is completely empty off-white. Leave
> it empty. The mug and the heart are the only two objects in the picture.
>
> Do NOT include: any text, letters, numbers, words or labels; any arrows,
> lines, branches or connectors; any people or figures; any additional cups,
> cans, hearts or icons; any speech bubbles; any question marks; any border,
> panel or background shape; any red; any colour other than the single brown
> coffee band.

## After generating — check before moving on

| Check | Why |
|---|---|
| Bottom 56% of the frame is genuinely empty | The whole good/bad model is built there. Anything drawn in it must be regenerated |
| Mug handle is on the RIGHT | The same mug is reused at four scales across the video |
| Heart is an outline, not filled, not anatomical | Filled or anatomical reads as a medical claim the narration does not make |
| Exactly one brown band, no other colour | Red must not exist in any plate |
| No text of any kind | All text is added in CapCut |
| Off-white value noted / sampled | The other four plates must match it exactly |
