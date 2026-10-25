# ANIMATION PROMPTS — earthquake-magnitude-shorts-wBLVmEZV2Oc

Each prompt ≤500 characters, focused on change-through-time only (appearance already established by the source image). Static holds are NOT animated — see I2V_REBUILD.md for which states use ANIMATION REQUIRED: NO.

## A02 (uses IMG01)
SHOT: S01 | SOURCE STATE: F01.1 | TARGET STATE: F01.2 | CLIP DURATION: ~3.0s
MOVING ELEMENT: seismograph pen arm and ink line
STATIC ANCHORS: drum, stand, canvas, white background
PROMPT: "Locked camera. The seismograph's pen arm trembles and shakes rapidly, and the thin ink line on the paper becomes an erratic, jagged red scribble that grows and extends off the right edge of the page. Keep the drum, stand, and page fixed in place. Preserve identity, linework style, and scale. End with the red scribble fully extended off-frame."

## A06+A07 (uses IMG03)
SHOT: S01 | SOURCE STATE: F01.5 | TARGET STATE: F01.7 | CLIP DURATION: ~5.0s
MOVING ELEMENT: the ruler itself (height/scale)
STATIC ANCHORS: canvas center-line, tick style, white background
PROMPT: "Locked camera. The vertical ruler smoothly grows taller from the bottom, extending upward, gaining more numbered tick marks as it grows, until it reaches its full height. Keep the ruler horizontally centered and its tick style fixed. Preserve linework style. End with the ruler at full height, numbered 0 to 30."

## A09 (uses IMG03, ruler at full height)
SHOT: S01 | SOURCE STATE: F01.8 | TARGET STATE: F01.9 | CLIP DURATION: ~1.5s
MOVING ELEMENT: red scribble overlay on the ruler
STATIC ANCHORS: ruler, canvas
PROMPT: "Locked camera. A dense red scribbled line appears over the middle-upper section of the ruler and vibrates rapidly in place, like a shaking seismograph trace. Keep the ruler itself completely fixed. Preserve linework style and scale. End with the scribble still vibrating, ready to disappear on the next cut."

## A16 (uses IMG05, crack-only stage → full-spiky stage)
SHOT: S01 | SOURCE STATE: F01.15 | TARGET STATE: F01.16 | CLIP DURATION: ~3.0s
MOVING ELEMENT: crack line and outer border of the globe
STATIC ANCHORS: globe body, continent shape, canvas position
PROMPT: "Locked camera. A jagged crack line splits across the globe's continent, then the globe's outer circular edge progressively breaks apart into a dense jagged spiky silhouette spreading all the way around it. Keep the globe centered and its size fixed. Preserve linework style. End with the border fully jagged and spiky all the way around."

## A23 (uses IMG07 + IMG07B overlay)
SHOT: S01 | SOURCE STATE: F01.20/F01.22 (reused) | TARGET STATE: F01.22 (final) | CLIP DURATION: ~2.5s
MOVING ELEMENT: debris fragments and streak lines
STATIC ANCHORS: central cluster position, canvas
PROMPT: "Locked camera. Additional jagged fragments burst outward from the central debris cluster along radiating streak lines, increasing the density and spread of scattered pieces. Keep the central cluster's position and overall scale fixed. Preserve linework style. End with visibly more scattered fragments than at the start."

## A25 (uses IMG04 or IMG06, subtle background loop — OPTIONAL)
SHOT: S01 | SOURCE STATE: any single-globe/slab hold (F01.10-F01.17) | TARGET STATE: same (loop) | CLIP DURATION: 3-4s loop
MOVING ELEMENT: globe/slab illustration only
STATIC ANCHORS: everything else, canvas, ruler
PROMPT: "Locked camera. The globe rotates very slowly and subtly in place, as if spinning on its axis, barely perceptible. Keep its size, position, and all markings fixed relative to its surface. Preserve linework style. End back at a near-identical rotation angle to loop cleanly."
FIDELITY RISK: rotation amplitude is POSSIBLE/unverified from source footage (see MOTION_EVENTS.csv A25) — treat this pass as optional embellishment, not a confirmed requirement.

## Draw-on / fade annotations (A01, A04, A08, A10-A15, A17-A22) — NOT separate I2V passes
These are simple opacity fades, straight cuts, or small draw-on shapes (strike-through, red circle, epicenter marks, labels). Per the STATIC SCENES rule, do not spend an I2V generation on these — implement them as overlay elements added during FINAL ASSEMBLY (see I2V_REBUILD.md COMPOSITE / TEXT-GRAPHICS OVERLAY sections) directly on top of the held source image.
