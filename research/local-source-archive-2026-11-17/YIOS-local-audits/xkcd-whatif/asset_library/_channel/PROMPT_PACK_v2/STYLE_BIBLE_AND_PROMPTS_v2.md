# Style bible + prompt pack v2 (deep-VF v2 corrections; TEXT ONLY, LOCAL ONLY)

This pack adds to `../PROMPT_PACK/` (P6, v1). Those files are not edited.
- Where the two differ, **this file wins**.
- Nothing has been generated. Image generation needs owner approval.
- Every brand element is **original**:
  - the NIB narrator, the TARDI mascot, the teal #1F6F78 brand colour, the Moon-proof card style;
  - the channel name is still the owner's choice.
- **Never copied from the source:** logo, title lockup, name, red cards, mascot, recurring characters, book covers, credits.

## A. Corrections to v1 (evidence in `../deep_vf/DEEP_VF_ADDENDUM_v2.md`)
| v1 said | v2 rule | Evidence |
|---|---|---|
| One 12 s title card (BRD-001 "title card plate") | **Two separate cards.** OPENING CARD 2.0 s (48 f) and END SCREEN 10.0 s (240 f, last frames). Separate assets, separate timeline slots. | MEASURED, `deep_vf/v2/title_card_durations.csv`: 43/44 and 40/44 longs |
| Red never a fill | Red fill is allowed **only** when the story object is red, hot or dangerous: fire, magma, laser, heat or danger zone, a red prop. Never decorative. | C2 v8: 17/18 |
| Dark/space scenes are exceptions | **DARK_FIELD is a core scene class**: 0–66% of states in longs, up to 78% in Shorts | `v2/colour_*.csv` |
| Maps as tint plates (ENV-004) | Two map classes: **TINT map** (pastel land/sea) and **MAP_FILL** (saturated flat fills). Both are content, not decoration. | v8 zJNm fail; rules v3 |
| Red marks write on at ~0.2 stroke/frame (GFX-002) | **The red circle POPS in 1 frame** and then holds. Write-on is not used for callout circles. | MEASURED in the proof: ROI red px 0→3576 in one frame |
| No photographs | Photographic material only as a degraded or blurred in-story camera or sensor image | `2LSyizrk8-0` G0038/G0070 |

## B. Scene classes (the class names match `deep_vf/v2/colour_classes.py`)
| Class | Look | When to use |
|---|---|---|
| LINE_ART (default) | Black monoline 8 px at 1080 on #F8F8F8, grey fills #E4E4E4/#C4C4C4/#848484 | Every lecture, board and diagram state |
| RED_MARK | Red #D7263D monoline: circle, arrow, strike, X, underline | Emphasis only, 1-frame pop |
| RED_SOLID | Flat red fill on the object | Fire, magma, laser, danger zone |
| TINT_REGION | Pastel flat regions (land #ECECB4, sea #BCECF4, terrain #C4B4A4) | Maps, climate zones, sky/ground |
| **MAP_FILL** | Saturated flat map fills (vegetation #6CBC6C, water #8CACAC, heat #CC2C3C), dashed latitude lines, hand-lettered caps place names as editable layers | A map *is* the subject (MAP_TOUR) |
| **DARK_FIELD** | #0C0C0C / #1C1C1C / #343434 fields, white line #FCFCFC, silhouettes in pure black | Space, night, underground, deep water, darkness |
| **GLOW** | A soft radial warm or white glow on DARK_FIELD; the only gradient allowed | Light sources: sun, explosion, reactor, heat bloom |
| PAINTED_PLATE | Saturated full-frame sky, sunset, fire or aurora plate | Sparing: big sky or energy moments only |
| OPENING CARD / END SCREEN | Brand teal #1F6F78 (never full-frame red) | See §D |

## C. Motion grammar (unchanged from the proof except where noted)
- **Pops:** every entering element appears in 1 frame and then holds dead still. This includes the **red circle**: on frame f it is absent, and on f+1 it is present at full stroke.
- **QA:** check the red circle with a **native-colour ROI** test, not greyscale. Its whole-frame luma change is only 0.24, so grey detectors miss it.
- **Cuts** change scene class (for example LINE_ART → DARK_FIELD).
- **The glow enters by a 6-frame linear dissolve**, and only into a GLOW plate.
- **A label must be backed by a state change.** A word label ("MELTING", "STEAM") pops on the same frame as the visual state it names (drips, wisps). Never pop a label over an unchanged picture (proof attempt 3).
- **Shorts (9:16):** the question or the subject visual is on screen inside the **first 24 frames** (1 s).
- **Camera budget** (whole-frame camera moves / all activity): ORDINARY ≤ 0.13, MAP_TOUR ≤ 0.20 (longs), and JOURNEY_LADDER uses a ruler/axis scroll rather than extra camera moves.
  - The JOURNEY_LADDER arm is **not validated**; see the addendum.
  - The Shorts film-strip scroll is under rules v3.

## D. New and replacement prompts
Repeat these **locks** verbatim in every image request. They are the same as v1:
> hand-drawn black monoline ink illustration, one uniform line weight (about 8 px on a 1080 px tall frame), slightly wobbly hand-drawn line with round line ends, flat fills only (light greys #E4E4E4, #C4C4C4, #848484 where a fill is needed), no gradients, no shading, no texture, no outline glow; people are faceless stick figures: head = unfilled circle with no eyes and no mouth, torso, arms and legs are single lines, no hands or feet drawn; objects carry the detail (parts, hatching), people stay minimal

Use this **negative** on every request:
> no text, no letters, no numbers, no logos, no watermark, no faces on stick figures, no hands or fingers, no 3D shading, no cel shading, no thick-thin calligraphic line variation, no sketchy double lines, no photo realism, no full-frame red, no resemblance to any existing comic, channel, mascot or title card, no real person

### BRD-002 — OPENING CARD (replaces the BRD-001 "title card plate"; 2.0 s = 48 f)
```
16:9 opening-card plate: flat deep-teal #1F6F78 full frame; TARDI the water bear (chubby tardigrade-like creature, black monoline, plump segmented body, eight stubby legs, two dot eyes, flat #E4E4E4 fill) drawn in white monoline, small, lower-left third, looking up at an empty hand-drawn rounded speech box in the upper centre (the question is typeset later as an editable layer). [locks]
```
- **Timeline:** the card pops in 1 frame, holds 48 f, then hard-cuts to the lecture frame.
- **Shorts:** no opening card. The question chip pops inside the first 24 f instead.

### BRD-003 — END SCREEN (separate asset; 10.0 s = 240 f, last frames)
```
16:9 end-screen plate: flat deep-teal #1F6F78 full frame; TARDI in white monoline at the left third, waving with one stubby leg; two empty hand-drawn rounded rectangles in the centre (for video/link tiles); an empty column on the right for an editable credits text layer. [locks]
```
- **Timeline:** the end screen pops in 1 frame and holds 240 f until the last frame. It is separate from BRD-002.
- **Shorts:** no end screen.

### ENV-005 — DARK_FIELD plates (supersedes ENV-002/003 where they differ)
```
Three 16:9 plates, one per request: (1) deep space: flat #0C0C0C field, sparse white dot stars, a flat grey #343434 planet limb along the bottom with white monoline outline; (2) night ground: flat #1C1C1C sky, pure black ground silhouette with a jagged tree line; (3) underground cross-section: flat #343434 rock with stipple dots, a black tunnel shape. White #FCFCFC monoline for any drawn object. [locks, but line colour white on dark]
```

### ENV-006 — MAP_FILL plate (new)
```
16:9 flat map plate of an invented coastline: saturated flat fills only — land #6CBC6C, deep water #8CACAC, shallow shelf #BCECF4, a heat/danger zone #CC2C3C as one flat blob; dashed thin black latitude lines; small black dots for places (names are added later as editable hand-lettered layers). [locks]
```
- Keep a separate TINT variant: land #ECECB4, sea #BCECF4.
- Red #CC2C3C appears only on a story danger or heat zone.

### GFX-003 — GLOW plate (new)
```
16:9 glow plate: #101010 field with one soft radial warm glow (centre near-white warm yellow, falling to amber then to the dark field), smooth, no rays, no lens flare, no texture. This plate is the only allowed gradient. [locks except the no-gradient clause]
```
- **Timeline:** it enters by a 6-frame linear dissolve, with no overshoot.
- **Optional:** it can be generated procedurally instead (the proof renderer does this).

### GFX-004 — RED CIRCLE pop (build spec, no image generation)
- A vector ellipse, red #D7263D, same weight as the ink (8 px at 1080), no fill, slightly wobbly path.
- Centre it on the referent (for example the crack on the moon in the proof).
- **Timing:**
  - frame f: 0 red pixels in the ROI;
  - frame f+1: full stroke;
  - then hold, and remove it on the next cut.
- **Acceptance:** native-HSV red pixel count in the ROI goes from 0 to >200 in one frame, and the pixel counts on the next 2 frames stay within ±5%.

### SHT-002 — 9:16 opening (replaces the SHT-001 opening guidance)
- A short question chip (≤ 18 characters, editable layer) **or** the subject visual pops at f ≤ 6.
- The narrator stays in the lower third, unsquashed, with no element overlapping a label.
- **Reference:** `deep_vf/proof_v1_attempt3/keyframes_9x16.png` f6.

## E. Acceptance (in addition to v1's per-prompt checks)
1. The opening card and end screen are separate files with lengths 48 f and 240 f.
2. No full-frame red anywhere.
3. Every DARK_FIELD, MAP_FILL, GLOW or RED_SOLID state names its story referent in the edit notes (rule C2).
4. The red circle passes GFX-004.
5. Labels are backed by state changes.
6. Originality: nothing in the result resembles the source's logo, title lockup, name, mascot, cards or recurring characters.

**Labels:**
- The class definitions and durations are MEASURED (see the evidence column).
- The designs are ORIGINAL proposals.
- The colour hexes for map and dark fields are MEASURED palette centres (`model_sheets/palette_*.csv`).
