# Brief: RETRO_005_CUBE_3FACE

Priority P1 | kind illustration | batch Batch 2 | status PLANNED | first appears 42.71s in beats B19 B20 B21 | construction method: **rigid sprite (bridge/inset)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
One corner cube seen looking into its corner: three mutually perpendicular faces meeting at the apex, same glass look as RETRO_002.

Manifest description: One cube seen looking into its corner: three mutually perpendicular faces meeting at the apex; same glass look as RETRO_002.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-OPT-003** `references/retroreflector/optical_corner_cube_photo_gold_wikimedia_corner-cube.jpg` [3/4 high angle looking into a black cylindrical mount, white background]: B19: the macro push into one cube should end on the apex with three seams meeting, not on a plain glass disc. Solid fused-silica Apollo cubes are glass (C05); this hollow gold one is a different construction, so use it for the seam geometry only.
- **REF-RETRO-005** `references/retroreflector/reflector_apollo11_cube_mount_section_figure_nasa_sp214_fig7-1.png` [cross-section drawing, side view, cube apex pointing down]: RETRO_003: draw the cutaway with these five labelled parts, apex down, and the glass front set back from the panel surface.
- **REF-RETRO-011** `references/retroreflector/reflector_corner_cube_ray_path_3d_diagram_wikimedia_corner-reflector.png` [3-D isometric of the open corner, rays entering from the upper right]: RETRO_003/RETRO_005: use as the structural template (redrawn): three planes, three bounces, parallel but offset return; exit ray is not collinear with the entry ray.
- (family context) **REF-OPT-024** `references/retroreflector/optical_diffuse_scatter_reflection_wikimedia_diffuse-reflection1_render.png` [2-D schematic: incident ray from the upper left onto a grainy surface, rays scatter in all directions]
- (family context) **REF-RETRO-014** `references/retroreflector/reflector_nglr1_modern_retroreflector_housing_red_cap_pivot_bracket_side34_nasa_nglr-payload.jpg` [close side/3-4 view at eye level, hardware on a bench or spacecraft deck, shallow depth of field]
- (family context) **REF-OPT-004** `references/retroreflector/optical_corner_cube_three_reflections_animation_wikimedia_reflection-coin-cube-rot.gif` [animated, camera orbits a transparent cube while a red marker travels along a ray]
- (family context) **REF-OPT-005** `references/retroreflector/optical_apollo_photon_histogram_apollo-collab_lunarphotons.png` [2-D data plot: x = time (minutes), y = time into the detector gate (ns)]
- (family context) **REF-OPT-006** `references/retroreflector/optical_beam_divergence_gaussian_wikimedia_divergenz-gauss-strahl.png` [side view, beam axis horizontal (z), radius vertical (w)]
- (family context) **REF-OPT-007** `references/retroreflector/optical_beam_waist_divergence_wikimedia_gaussianbeamwaist.svg` [side view, beam axis horizontal]
- (family context) **REF-OPT-008** `references/retroreflector/optical_seeing_star_image_d2r0_wikimedia_ast-seeing-2r0.png` [negative (dark-on-white) image of a point source]
- (family context) **REF-OPT-009** `references/retroreflector/optical_seeing_star_image_d20r0_wikimedia_ast-seeing-20r0.png` [negative image of a point source]

Web pointers (verify independently): https://tmurphy.physics.ucsd.edu/apollo/lrrr.html

## 3. Intended camera angles
perspective into the corner

## 4. Required geometry and proportions
2160x2160; apex at the exact canvas centre pixel (1080,1080), three faces as 120-degree-apart rhombi in perspective; circular front aperture Ø 86% of canvas.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Silver aluminium frame #AEB4C2-#E6E9F0, bright white base, dark glossy glass faces #1A2030-#2C3550 with faint blue-grey sheen; hard sunlight from the left.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA, clear glass with faint edge lines; no rays.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `retro_cube_3face` | cube interior view | `RETRO_000_SYSTEM` | apex = (1080,1080) | 58 |

Parent group: `RETRO_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: RETRO_002_CUBE_ARRAY.

## 9. Hidden overlap requirements
n/a
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `RETRO_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2160x2160**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): apex. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
static
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P07**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2160x2160; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
C06: three faces mutually perpendicular; return travels back along the incoming direction.

Must not change: Exactly 100 round cube faces in a 10x10 grid on a 46 cm panel (Apollo 11 style); cube diameter 3.8 cm = 1/12 of the panel width; same panel colour, frame and tilt toward Earth in every view; sun from the left.

Known failure modes: wrong cube count; cubes fused into a texture; panel too large relative to the astronaut; perspective that differs between array and cutaway so the match cut cannot line up; baked glow standing for light.

## 16. Expected deliverable filenames
`retro_cube_3face_2160x2160.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
