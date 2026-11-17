# VISUAL DNA

Global, evidence-supported production characteristics. Scene-specific detail lives in TIMELINE.csv / ASSET_MANIFEST.csv — not repeated here.

## ENVIRONMENT DNA
- Flat solid white/off-white canvas for the entire video (OBSERVED). No background photography, no gradients, no depth layers.
- No camera moves, no parallax, no depth-of-field anywhere (OBSERVED — zero scene cuts detected, all "cuts" are 2D layer swaps on the same flat canvas).

## CHARACTER DNA
- One recurring minimalist stick-figure design (circle head, straight-line limbs, no facial detail beyond dot eyes) reused across 4 poses/props (interview duo, NASA-badge figure, distressed figure, headset figure). See C01.

## OBJECT / ILLUSTRATION DNA
- Uniform hand-drawn / sketch line-art style for every illustration (seismograph, newspaper, globe, fault-block slabs, debris) — black ink linework, thin uniform stroke weight, minimal or flat grey shading, no gradients or 3D rendering (OBSERVED).
- Central recurring visual metaphor: a grey globe/Earth icon that accumulates visible "damage" states as the fictional magnitude escalates (clean → epicenter marks → cracked → spiky border → exploded debris). This is the emotional/visual throughline of the whole piece (OBSERVED progression, LIKELY intentional escalation device).
- Red ink is reserved exclusively for "alert/annotation" marks: strike-throughs, circles, epicenter ripples, the climbing scribble — never used for the base illustrations (OBSERVED, consistent rule across the whole video).

## COLOR PALETTE
- Background: white/off-white (#FFFFFF-ish).
- Line art: black.
- Fills: flat light-to-mid grey (globe, slabs).
- Accent: red (annotations, alerts, epicenters, "danger" scribbles) — the only saturated color used anywhere in the video (OBSERVED).

## TYPOGRAPHY (T01/T02)
- T01 (titles): bold, all-caps, hand-drawn/marker-style sans-serif, large, centered top of canvas.
- T02 (captions/annotations): same type family, much smaller, regular weight, used for facts, dates, measurements, and punchlines.
- No other type styles appear anywhere in the video (OBSERVED).

## GRAPHICS / UI LANGUAGE
- E02 (the vertical ruler/number-line) is the single persistent HUD element from F01.5 onward — it never fully disappears once introduced, acting as a constant visual reminder of "where we are on the scale" (OBSERVED).
- G01 ("LIVE" broadcast box) is a reusable template appearing 3 times with different internal content — the video's go-to device for a punchline/reaction beat (OBSERVED reuse pattern).

## COMPOSITION
- Every state is centered, single-column, vertically stacked (title → illustration → optional caption/box), consistent with 9:16 short-form framing (OBSERVED).

## MOTION LANGUAGE
- No camera motion anywhere. All motion is 2D layer animation: fade-ins, one draw-on (strike-through, circle), one continuous scale-up (the ruler, once), and hard cuts between major "screens" (OBSERVED — see MOTION_EVENTS.csv).
- Hard cuts are used specifically at every full-topic change (new magnitude number); fades/draw-ons are used for additions *within* a topic. This is a consistent authorial rule (LIKELY intentional pacing device).

## TRANSITION LANGUAGE
- Two transition types only: (1) instant hard cut (STATE_REPLACEMENT, used ~11 times at major beats) and (2) opacity fade-in (used for additive annotations within a state). No wipes, no slides, no 3D transitions anywhere (OBSERVED).

## ASSET REUSE PATTERN
- High reuse of structural templates (G01 LIVE box x3, C01 stick figure x4 poses, E02 ruler throughout, E03 globe across 4 damage states) vs. single-use "punchline" illustrations (E01 seismograph, O01 newspaper, O02 phone, O03 fault-blocks) that appear exactly once each. This 80/20 pattern (few reusable structural assets + many disposable gag assets) is the core efficiency pattern of the production (OBSERVED).

## FIDELITY LIMITATION
- Sub-0.5-second easing curves (exact fade durations, exact scale-up curve of the ruler, exact rotation speed of the globe) cannot be measured precisely from 2fps sampling; all such values are marked APPROXIMATE or LIKELY in MOTION_EVENTS.csv rather than fabricated as exact numbers.
