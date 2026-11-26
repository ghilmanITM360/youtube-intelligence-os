# Brief: RETRO_001_ASSEMBLY

Priority P0 | kind illustration | batch Batch 2 | status RESEARCHED | first appears 37.21s in beats B17 B18 | construction method: **rigid prop (frame + faces)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Apollo 11 Laser Ranging Retroreflector Array hero composite on regolith: silver aluminium frame, dark glossy glass faces in a 10x10 grid, support legs, shadow. Not the Apollo 14/15 array (those carry 100 and 300 cubes).

Manifest description: Hero composite on regolith, 3/4 view, tilted toward Earth: frame, support, 10x10 face grid and shadow. Assembled from RETRO_004, RETRO_002 and RETRO_006.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-004** `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg` [pure rear view, eye-level, walking away, full body, carrying two packages]: Rear view reference (the film has no rear shot planned; keep it in the pose library as a hidden-overlap check). Shows the PLSS back detail needed if the camera ever sees him walk away.
- **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]: Shows the true relative scale and low height of the array against the astronaut (array roughly knee height or below), and the rear 3/4 walking gait.
- **REF-ASTRO-023** `references/astronaut/astronaut_apollo11_surface_front34_stoop_leveling_handle_nasa_as11-40-5951.jpg` [front 3/4 from the astronaut's left, eye-level, mid-distance, on the real lunar surface]: Only real-surface photo of an astronaut interacting with a deployed package by tool: slight stoop, handle at 45 degrees to the ground, both gloves on equipment. Use it for the arm/handle geometry of the align beat; the kneel itself is still stylised.
- **REF-RETRO-001** `references/retroreflector/reflector_apollo11_lrrr_threequarter_deployed_nasa_as11-40-5952.jpg` [three-quarter view from the front, a few metres away (distance estimated by eye), array face tilted up toward the upper left]: RETRO_001/RETRO_004: draw a silver-grey aluminium box with a white-bright base plate and bail handle; the cube faces read as a dark glossy grid (not round glassy bubbles). Tilt the face upward toward the camera's upper left.
- **REF-RETRO-003** `references/retroreflector/reflector_apollo11_lrrr_elevated_from_lm_window_nasa_as11-37-5551_crop.jpg` [elevated, from the LM window, long distance, front-left]: Use only as layout reference (array in front of and closer than the PSEP from the window), not for detail.
- **REF-RETRO-004** `references/retroreflector/reflector_apollo11_lrrr_preflight_hardware_nasa_sp214_fig7-6.png` [three-quarter from above-front, on a test stand, face up]: RETRO_004: include a gnomon rod, alignment scale and bail handle on the base; the cavities are visibly round and recessed.
- **REF-RETRO-006** `references/retroreflector/reflector_apollo14_lrr_closeup_high_threequarter_tilt_support_nasa_as14-67-9385.jpg` [close three-quarter from above and in front, array face at lower left, support at right]: RETRO_004: the support stands behind the array like a hinged easel with a round level fixture on top; gnomon is a thin vertical rod.
- **REF-RETRO-007** `references/retroreflector/reflector_apollo14_lrr_medium_threequarter_sunlit_horizon_nasa_as14-67-9386.jpg` [medium distance (a few metres, estimated by eye), three-quarter from the front-right, low, with a long horizon behind]: RETRO_002: faces are bright round rims in silver aluminium on the Apollo 14 unit, so cube count and spacing can be drawn exactly; box depth is shallow relative to its width.
- (family context) **REF-OPT-024** `references/retroreflector/optical_diffuse_scatter_reflection_wikimedia_diffuse-reflection1_render.png` [2-D schematic: incident ray from the upper left onto a grainy surface, rays scatter in all directions]
- (family context) **REF-RETRO-014** `references/retroreflector/reflector_nglr1_modern_retroreflector_housing_red_cap_pivot_bracket_side34_nasa_nglr-payload.jpg` [close side/3-4 view at eye level, hardware on a bench or spacecraft deck, shallow depth of field]
- (family context) **REF-OPT-003** `references/retroreflector/optical_corner_cube_photo_gold_wikimedia_corner-cube.jpg` [3/4 high angle looking into a black cylindrical mount, white background]
- (family context) **REF-OPT-004** `references/retroreflector/optical_corner_cube_three_reflections_animation_wikimedia_reflection-coin-cube-rot.gif` [animated, camera orbits a transparent cube while a red marker travels along a ray]
- (family context) **REF-OPT-005** `references/retroreflector/optical_apollo_photon_histogram_apollo-collab_lunarphotons.png` [2-D data plot: x = time (minutes), y = time into the detector gate (ns)]
- (family context) **REF-OPT-006** `references/retroreflector/optical_beam_divergence_gaussian_wikimedia_divergenz-gauss-strahl.png` [side view, beam axis horizontal (z), radius vertical (w)]
- (family context) **REF-OPT-007** `references/retroreflector/optical_beam_waist_divergence_wikimedia_gaussianbeamwaist.svg` [side view, beam axis horizontal]
- (family context) **REF-OPT-008** `references/retroreflector/optical_seeing_star_image_d2r0_wikimedia_ast-seeing-2r0.png` [negative (dark-on-white) image of a point source]

Web pointers (verify independently): https://ilrs.gsfc.nasa.gov/missions/satellite_missions/current_missions/ap11_reflector.html; https://lroc.im-ldi.com/images/22; NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22)

## 3. Intended camera angles
3/4 hero; low surface

## 4. Required geometry and proportions
3000x2000; panel 46 cm square (0.45 m by UCSD, say about half a metre), tilted toward Earth about 30 degrees back from vertical; legs ~25 cm; 10x10 round cube faces, cube diameter 3.8 cm = 1/12 of panel width; boot-print scale cue 30 cm.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Silver aluminium frame #AEB4C2-#E6E9F0, bright white base, dark glossy glass faces #1A2030-#2C3550 with faint blue-grey sheen; hard sunlight from the left.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Hero state: panel tilted, resting on regolith; shadow added in code. Second state: ghost (code) - the astronaut aligns it at B18; art is the settled state only.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `retro_assembly_frame` | frame + support (from RETRO_004) | `RETRO_000_SYSTEM` | ground contact bottom-centre | 45 |
| `retro_assembly_faces` | 10x10 faces (from RETRO_002) | `retro_assembly_frame` | array centre | 55 |

Parent group: `RETRO_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: RETRO_002_CUBE_ARRAY RETRO_004_FRAME_MOUNT RETRO_006_SHADOW.

## 9. Hidden overlap requirements
Faces layer extends 1.2% of canvas width under the frame lip.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `RETRO_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **3000x2000**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): bottom-centre of the support (ground contact). Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
pops in at B17 (scale/alpha), tiny settle at B18
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P06**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 3000x2000; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
C05/C06: the array is a passive prop; its distance from the lander is tens of metres; which of array/PSEP appears nearer is viewpoint-dependent; do not name an astronaut.

Must not change: Exactly 100 round cube faces in a 10x10 grid on a 46 cm panel (Apollo 11 style); cube diameter 3.8 cm = 1/12 of the panel width; same panel colour, frame and tilt toward Earth in every view; sun from the left.

Known failure modes: wrong cube count; cubes fused into a texture; panel too large relative to the astronaut; perspective that differs between array and cutaway so the match cut cannot line up; baked glow standing for light.

## 16. Expected deliverable filenames
`retro_assembly_frame_3000x2000.png, retro_assembly_faces_3000x2000.png, retro_assembly_master_3000x2000.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
