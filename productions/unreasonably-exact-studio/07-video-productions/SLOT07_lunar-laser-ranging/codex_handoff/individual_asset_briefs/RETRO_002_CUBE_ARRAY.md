# Brief: RETRO_002_CUBE_ARRAY

Priority P0 | kind illustration | batch Batch 2 | status RESEARCHED | first appears 37.21s in beats B17 B18 B19 B20 B21 | construction method: **sprite instancing in code: Claude places 100 copies of the face disc on the measured recess grid (exact count and registration); macro is its own generation**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
The 10x10 grid of round glassy cube faces of the Apollo 11 retroreflector in its silver frame (exactly 100 faces). Built from TWO generated parts that Claude assembles in code: an empty frame plate with 100 recesses, and one face-disc sprite (plus variants).

Manifest description: Front and close-up view of the 10x10 grid of round glassy cube faces, dark glossy glass in a silver-aluminium frame (exactly 100 faces visible).

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-RETRO-001** `references/retroreflector/reflector_apollo11_lrrr_threequarter_deployed_nasa_as11-40-5952.jpg` [three-quarter view from the front, a few metres away (distance estimated by eye), array face tilted up toward the upper left]: RETRO_001/RETRO_004: draw a silver-grey aluminium box with a white-bright base plate and bail handle; the cube faces read as a dark glossy grid (not round glassy bubbles). Tilt the face upward toward the camera's upper left.
- **REF-RETRO-004** `references/retroreflector/reflector_apollo11_lrrr_preflight_hardware_nasa_sp214_fig7-6.png` [three-quarter from above-front, on a test stand, face up]: RETRO_004: include a gnomon rod, alignment scale and bail handle on the base; the cavities are visibly round and recessed.
- **REF-RETRO-005** `references/retroreflector/reflector_apollo11_cube_mount_section_figure_nasa_sp214_fig7-1.png` [cross-section drawing, side view, cube apex pointing down]: RETRO_003: draw the cutaway with these five labelled parts, apex down, and the glass front set back from the panel surface.
- **REF-RETRO-006** `references/retroreflector/reflector_apollo14_lrr_closeup_high_threequarter_tilt_support_nasa_as14-67-9385.jpg` [close three-quarter from above and in front, array face at lower left, support at right]: RETRO_004: the support stands behind the array like a hinged easel with a round level fixture on top; gnomon is a thin vertical rod.
- **REF-RETRO-007** `references/retroreflector/reflector_apollo14_lrr_medium_threequarter_sunlit_horizon_nasa_as14-67-9386.jpg` [medium distance (a few metres, estimated by eye), three-quarter from the front-right, low, with a long horizon behind]: RETRO_002: faces are bright round rims in silver aluminium on the Apollo 14 unit, so cube count and spacing can be drawn exactly; box depth is shallow relative to its width.
- **REF-RETRO-008** `references/retroreflector/reflector_apollo15_lrrr_topdown_hex_cubes_gnomon_nasa_as15-85-11468.jpg` [top-down looking over the array from the back, face toward the viewer's lower side]: The Apollo 15 array should only be shown as a comparison inset: far more cells in staggered rows, same cell size.
- (family context) **REF-OPT-024** `references/retroreflector/optical_diffuse_scatter_reflection_wikimedia_diffuse-reflection1_render.png` [2-D schematic: incident ray from the upper left onto a grainy surface, rays scatter in all directions]
- (family context) **REF-RETRO-014** `references/retroreflector/reflector_nglr1_modern_retroreflector_housing_red_cap_pivot_bracket_side34_nasa_nglr-payload.jpg` [close side/3-4 view at eye level, hardware on a bench or spacecraft deck, shallow depth of field]
- (family context) **REF-OPT-003** `references/retroreflector/optical_corner_cube_photo_gold_wikimedia_corner-cube.jpg` [3/4 high angle looking into a black cylindrical mount, white background]
- (family context) **REF-OPT-004** `references/retroreflector/optical_corner_cube_three_reflections_animation_wikimedia_reflection-coin-cube-rot.gif` [animated, camera orbits a transparent cube while a red marker travels along a ray]
- (family context) **REF-OPT-005** `references/retroreflector/optical_apollo_photon_histogram_apollo-collab_lunarphotons.png` [2-D data plot: x = time (minutes), y = time into the detector gate (ns)]
- (family context) **REF-OPT-006** `references/retroreflector/optical_beam_divergence_gaussian_wikimedia_divergenz-gauss-strahl.png` [side view, beam axis horizontal (z), radius vertical (w)]
- (family context) **REF-OPT-007** `references/retroreflector/optical_beam_waist_divergence_wikimedia_gaussianbeamwaist.svg` [side view, beam axis horizontal]
- (family context) **REF-OPT-008** `references/retroreflector/optical_seeing_star_image_d2r0_wikimedia_ast-seeing-2r0.png` [negative (dark-on-white) image of a point source]

Web pointers (verify independently): https://ilrs.gsfc.nasa.gov/missions/satellite_missions/current_missions/ap11_reflector.html (Apollo 11, 14, 15 photos)

## 3. Intended camera angles
front; close-up macro for the push-in

## 4. Required geometry and proportions
NATIVE generation (about 1254-1500 px per image; label anything larger resampled). Plate: square 1:1, panel fills 92% of the canvas with a transparent margin, 10x10 round recesses on a uniform pitch (recess diameter 0.083 of panel width = 3.8/46 cm, pitch 0.086), recesses EMPTY (flat dark floor). Face sprite: ONE round fused-silica face, square canvas, centred, transparent outside the disc, subtle 3-facet interior, no perfect sphere highlight, matte-clean. Variants: 3 faces with slightly different reflection (so the grid does not look stamped).

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Silver aluminium frame #AEB4C2-#E6E9F0, bright white base, dark glossy glass faces #1A2030-#2C3550 with faint blue-grey sheen; hard sunlight from the left.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Front orthographic view (inferred projection; no photograph is exactly front-on: the Apollo 11 photograph AS11-40-5952 shows the panel tilted, dark glass, matte silver box). Keep the surface MATTE aluminium, not mirror-polished. Light from the upper left, about 30 degrees up, hard.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `retro_array_plate_empty` | frame plate with 100 empty recesses | `RETRO_000_SYSTEM` | plate centre; recess (1,1) and (10,10) centres listed in PIVOTS.json | 54 |
| `retro_face_disc_a` | one face disc sprite | `retro_array_plate_empty` | disc centre | 55 |
| `retro_face_disc_b` | face variant b | `retro_array_plate_empty` | disc centre | 55 |
| `retro_face_disc_c` | face variant c | `retro_array_plate_empty` | disc centre | 55 |
| `retro_array_macro3x3_native` | independently generated 3x3 close-up at native size | `RETRO_000_SYSTEM` | centre face centre | 55 |

Parent group: `RETRO_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Face discs are placed 0.5% of canvas width inside the recess edge in code (hidden bezel overlap lives in the plate).
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `RETRO_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x4096**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): array centre. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
macro push-in B19; no motion inside the art
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P06, P07**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 4096x4096; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
100 faces exact (B7 is checked in code from the instance list, not by eye); registration point shared with RETRO_005 cube centre (B9); appearance of the glass varies with viewing angle in the photographs, so the dark-glass look is an illustration choice.

Must not change: Exactly 100 round cube faces in a 10x10 grid on a 46 cm panel (Apollo 11 style); cube diameter 3.8 cm = 1/12 of the panel width; same panel colour, frame and tilt toward Earth in every view; sun from the left.

Known failure modes: wrong cube count; cubes fused into a texture; panel too large relative to the astronaut; perspective that differs between array and cutaway so the match cut cannot line up; baked glow standing for light.

## 16. Expected deliverable filenames
`retro_array_plate_empty.png, retro_face_disc_{a,b,c}.png, retro_array_macro3x3_native.png (native sizes stated in ASSET_MANIFEST.csv)`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
