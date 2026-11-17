# i6e4NnFnQi0: visual-only closure (contract v1; LOCAL ONLY)

## Evidence base
- **Source:** sha re-computed = manifest (checks.json V1, b06384dc…). 1708 frames. Every frame is measured and covered once (V2).
- **Reused:** the rv1 ledger (51 segments) and its measurements. rv1 had left 13 segments partly unviewed (274 frames).
- **New in closure_v1/:**
  - native frames;
  - holds_01..07.jpg: all 26 holds, viewed;
  - activity_grid.jpg: every frame of G0008, G0010, G0012, G0014, G0016, G0018, G0020, G0042 and G0044 at 1/8 scale, viewed;
  - strips of every frame of G0006, G0022, G0030, G0040 and G0050, viewed;
  - residue_crops.png and flash_581_584.jpg (half scale);
  - a per-frame change series for every activity;
  - checks.json.
- **Disclosure:** the grid frames are viewed at 1/8 scale.

## V4/V5 resolutions
| Seg | rv1 | Resolution |
|---|---|---|
| G0006 | — | `TOO SLOW` is typed (f113–115), then a curved arrow is drawn down to the telescope (f117–119). |
| G0008 f183–243 | MEDIUM | Hard cut to a white canvas with a tiny telescope and grey lines. Over ~60 f the black telescope drifts down and tilts, leaving a grey **ghost** copy at the old pose. The grey sight lines follow it. This is object motion, not camera. |
| G0010 f248–264 | PAN_LEFT_BLUR | Whole-canvas slide left with blur. The telescopes exit left and the stippled spiral galaxy slides in. This is a camera/canvas move. |
| G0012 f310–322 | PAN_RIGHT | The canvas slides back. The galaxy exits and the telescopes re-enter, with `MOON` and the disc now on the upper line. |
| G0014 f327–367 | MEDIUM, ZOOM_OUT_RED_FILL | The red ray and the wedge fill grow in (the ray swings out to the frame edge). The layout stays nearly fixed. f326 (in-hold residue, largest component 33 px) is the **1-frame-early onset** of this change. |
| G0016 | — | Dashed vertical line drawn top-down; `AUTOMATIC ON-BOARD TRACKING ALGORITHM LIMIT` typed. |
| **Hold G0017 f440–445** | not in ledger | **Un-ledgered event:** `(TOO CLOSE)` **fades in over 6 f** under `MOON` (grey to black, largest component ≈380 px). This is a ledger correction: a FADE_IN_LABEL inside VS009. |
| G0017 f467 / G0018 f468–475 | PAN_RIGHT_SLIDE_IN | f467 is the onset frame. The canvas slides right with motion blur and a divider plus the `MANUAL TRACKING` panel enter from the left. Hold shift ≈492 px = this slide. |
| G0019 f530 / G0020 f531–591 | MEDIUM, POSE_SWAP_ROTATION | f530 is the onset. The telescope rotates stepwise counter-clockwise and the red ray swings onto the Moon. A `CLICK` label appears at the hand-held controller (f581). **f582–583: the right panel flashes as a colour-inverted negative for 2 frames** (black field, teal ray and wedge; mean luma 242→121→242), a snapshot cue. Then it returns to normal. |
| G0022 f626–631 | — | Hard cut to a black plate with a grey **photograph** mosaic of a crater plus a full-Moon photo, with credit captions. The frames after the cut are static. |
| G0030 | — | 6-f cross-dissolve: `EXPECTATION` → `REALITY`, tilted ray → near-vertical ray, `~1°/second` → `6°/minute`. |
| G0040 | — | Speech bubble with a zigzag tail **scales up** from the telescope aperture over 9 f; inside is a blurred photo inset. |
| G0042 f1205–1220 | ZOOM_IN | Camera zoom into the bubble. The telescope and Earth blur out; the bubble border passes off-frame. |
| G0044 f1272–1348 | MEDIUM, 71 f unviewed | Inside the blurred photo, a blue top-down chair-like object rotates and swings down-left over ~65 f. Then a zoom-out (f1338–1348) returns the bubble border as a small bordered panel at right. |
| G0050 | LOW | **1-frame pop** of a small striped flag on the redacted silhouette (f1636; next frame 0 px). Resolved. |

**Other hold residue:**
- f272, f933, f1075, f1243 and f1579 have components ≤11 px: NOISE.
- f1411 (largest component 27 px, max diff 39) is a low-amplitude grain shimmer over the silhouette and the photo. By viewing it is NOISE: there is no drawn change.

## V6 creative (text read from native holds)
- **Text:**
  - `WIDE FIELD PLANETARY CAMERA 2 (WFPC2)`;
  - `TOO SLOW`;
  - `MOON`, `(TOO CLOSE)`;
  - `AUTOMATIC ON-BOARD TRACKING ALGORITHM LIMIT`;
  - `MANUAL TRACKING`, `CLICK`;
  - photo credits `Crater Copernicus on Earth's Moon / Credit: John Caldwell (York University, Ontario), Alex Storrs (STScI), and NASA` and `Moon / Credit: Lick Observatory`;
  - nebula photo caption `AG Carinae / Credit: NASA, ESA, STScI`;
  - `EXPECTATION` / `REALITY`, red `~1°/second` / `6°/minute`;
  - `REDACTED`.
- **Colour:** mostly off-white canvas with black line art, plus red for the ray, wedge and rate labels.
  - **DARK_FIELD** starfield with a white line-art telescope, a grey Earth and a Moon.
  - Two full-frame third-party **photographs**: a grey lunar mosaic and a colour nebula.
  - Blurred colour photo insets.
  - Tan/blue desk chairs with motion-blur trails.
  - A 2-frame teal negative flash.
  - No full-frame red.
- **Continuity:** the same telescope drawing is used at every scale, and the ghost copy shows the previous pose.
- **INFERRED rv1 claims tested:**
  - "ZOOM_OUT" at G0014 is **refuted**: it is a red-fill growth with a near-fixed layout.
  - G0044 "rotate then zoom-out" is confirmed.
- **Originality flags:** never reuse the agency logo, the third-party photographs, the flag or the software/instrument names as branding.

## V7
- `reconstruction_blueprint_v2.md`: per-state prompts, motion, continuity, QA and originality.
- **Format:** ORDINARY explainer Short with canvas slides and two camera zooms. This is a dev-library observation, not a scored test.
- **Ledger corrections:**
  - an un-ledgered `(TOO CLOSE)` 6-f fade-in at f440–445 inside G0017;
  - a 2-f negative flash at f582–583 inside G0020.
  These are recorded here; the rv1 ledger is not edited.

## Status
**VISUAL_ANALYSIS_COMPLETE** (visual-only contract v1). visual_script_mapping, audio and AV are out of scope and remain unsigned.
