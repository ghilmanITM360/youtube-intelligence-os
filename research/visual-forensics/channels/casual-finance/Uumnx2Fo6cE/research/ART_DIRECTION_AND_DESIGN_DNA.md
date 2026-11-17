# ART DIRECTION AND DESIGN DNA — Uumnx2Fo6cE

Scope: visual-only forensic reading of 507 verified-by-review states, 715 detected change episodes and 42 sub-threshold micro-events (see VISUAL_STATES.csv, BOUNDARY_VERIFICATION.csv, INTRA_STATE_EVENTS.csv). Labels: MEASURED (numbers from decoded frames), OBSERVED (seen in frames/tiles), INFERRED (interpretation). Evaluations are subjective professional judgement, not viewer data. No claim is made about software, AI generation, camera gear or retention.

## 1. System in one paragraph
A flat 2D "whiteboard explainer": an almost-white canvas (#FCFCFC is the dominant colour in 410 of 507 representative frames; MEASURED), hand-drawn stick-figure presenters with oversized round heads and minimal faces, small flat-coloured doodle props (houses, towers, money, tags, papers), and large rectangular third-party captures (articles, filings, charts, dark-mode transcripts, news-feed pages) cut onto the canvas. Information density is carried by the captures; emotion and comedy are carried by the doodle figures. About 87% of the average character/prop frame is canvas white (MEASURED mean share of the largest colour cluster, 0.867).

## 2. Composition and focal hierarchy (OBSERVED)
- Character/prop states (F1 character-only 50, F2 character+prop 130, F3 object cluster 72 states): a single dominant subject, 15–40% of frame height for props, a presenter often 60–95% of frame height anchored at the bottom edge; large negative space (>85% empty). Focal order is subject → label/number → secondary prop.
- Screenshot states (F4 full-bleed capture 47, F5 capture + presenter 144, F8 dark-UI capture 15, F6 chart/graph 20): the capture fills 55–100% of the frame; a presenter is typically pushed to a lower/side edge (often right, partially cropped) holding a thin brown pointer stick aimed at the highlighted part of the capture (pointer appears in ~60 state descriptions). The pointer is a recurring directional device.
- Rare full-bleed drawn scenes (F9, 6 states) and text/title cards (F7 4, F10 7) are used as pacing breaks and at the end-card.
- Balance is asymmetric: capture on one side, figure on the other; the thumbnail-style layouts (house + figure + doodles) are centred and symmetrical.

## 3. Illustration language (OBSERVED)
- Presenters: black marker-weight outline, flat skin fill (measured warm tones ≈ #E0C0A0), dot eyes, one-line mouth and brows; expression is carried by 3–6 stroke changes (smile, frown, worry, shout, shrug). Distinct presenter variants appear (spiky-haired lead; brown-haired; red-headband figure; hooded figure with sunglasses; elderly figure with cane; detective in a checked cap; green-tie figure; dark-haired worried figure). These are specific to the source and must not be copied.
- Props: slightly rougher fills with visible outline wobble (houses in red/tan/blue, grey towers with window grids, green dollar bills, yellow price tags, document icons labelled DEBT/TAX), a consistent "marker doodle" geometry: thick dark outline, 2–3 flat colours, no gradients or shading.
- Visual metaphors (INFERRED): house in chains/ice, torn price tag, bank building with speech bubble, detective with magnifier for "investigating a claim", news-paper reader for "the press".
- Humour: deadpan expression swaps and small gag props (INFERRED function: pacing relief between data-heavy captures).

## 4. Typography and numbers (OBSERVED)
- Handwritten red numerals/words ("58%", "$3.1…", "ever!", "4 in 10") in a brush-marker hand, large (8–15% frame height), often revealed one character per few frames (SUB036: "$3" gains ".", then "1").
- Third-party text in captures is small (body ≈ 1–2% frame height): often unreadable in a normal viewing size (flagged per state; 219 states carry unreadable_text notes). Headline text inside captures is readable at ~3–5% height.
- Handwritten green offer text ("40% off the Vantage Plan!") and a typed URL are used for the sponsor block; end card uses a clean sans plus handwritten lines.
- Highlighting is the dominant typographic emphasis: yellow marker highlight, red underline/box strokes, purple selection highlight, with cursor arrows in screen-recording-style captures.

## 5. Colour (MEASURED + OBSERVED)
Canvas #FCFCFC; line/ink near #202020; skin ≈ #E0C0A0; greys (#A0A0A0–#606060) for buildings and cards; accent set: marker red, highlighter yellow, money green (≈ #40A040), plus brown wood/pointer. Dark-mode captures introduce a second regime (near #202020 backgrounds). Colour is used as a pointer for attention (red/yellow strokes on the capture), not decoratively.

## 6. Graphic and information design
- Charts are always third-party captures; emphasis is added by drawing on them (blue stroke draw-on along a series, 5 sequential micro-events SUB031–035; magenta/red stroke segments; boxes drawn around table cells).
- Information is revealed progressively: element-by-element additive entries (233 additive episodes) rather than whole slides; counts of repeated icons grow (DEBT icons 2→3→4 in S0051–S0054 type sequences).
- A yellow progress bar of 8 px runs along the bottom edge from f10565 to f12437 (440.25–518.25 s; MEASURED roughly linear, ≈16.3 px/s) across a sponsor segment (INFERRED link to the Ground-style sponsor read: ASR mentions the sponsor in this span). A QR code sits lower right during that span (OBSERVED).

## 7. Motion design grammar (MEASURED + OBSERVED)
- 370 single-frame state changes (73% of state-changing events) are instantaneous hard replacements or additive entries; no easing exists on them.
- 136 state-transition motions (12.5% of all frames, median 0.63 s, max 2.67 s) use zoom/scale (31 intervals), pan/scroll (30), object motion (22) and wipes/entries; reviewers label easing: ease-out 63, ease-in-out 21, linear 17, stepped 30, overshoot 2, unknown 29 (easing labels are INFERRED from 4 sampled frames per interval, low precision).
- Draw-on animations (highlight/underline/box/line-stroke) and screen-recording cursor motion exist at sub-threshold scale (42 clusters + 176 small events).
- Camera: no 3D camera; "camera" moves are 2D scale/pan of the capture layer (INFERRED). No lens or depth cues exist.

## 8. Difference from the first gold-standard video (o3FQcd91MIs; facts about that video are from its accepted record)
| Aspect | o3FQcd91MIs | Uumnx2Fo6cE |
|---|---|---|
| Length / states | 278 s / 76 states (+3 micro) | 920.7 s / 507 states (+218 intra-state events) |
| Frame rate | 30 fps CFR | 24 fps CFR |
| State rate | 0.27 / s | 0.55 / s (median state 1.25 s) |
| Motion | zero tweened animation, zero camera motion | 169 motion intervals (zoom/pan/scroll/object), 12.5% of frames in transitions |
| Black frames | 2 pure-black frames + black holds | no black frames (min mean luma 67) |
| Content | cartoon explainer with doodles and cards | data-capture-heavy: articles, filings, transcripts, dark UI, sponsor block with QR and progress bar |
Same family: same canvas colour (#FCFCFC), same marker-doodle presenter language, same hard-replace default, same additive reveal habit. Style is therefore a consistent channel system with a heavier information layer, not a different style.

## 9. Production-quality read (subjective)
Layouts are precise but quickly assembled: capture scale and crop vary; many captures are shown at sizes where body text cannot be read, making the capture function as an "evidence texture" (INFERRED) with the highlighter/underline as the actual reading cue. Asset consistency of the doodle layer is high; capture layer consistency is mixed by nature.
