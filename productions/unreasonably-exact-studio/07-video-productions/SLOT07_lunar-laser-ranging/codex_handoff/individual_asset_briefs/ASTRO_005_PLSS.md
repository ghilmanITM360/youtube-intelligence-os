# Brief: ASTRO_005_PLSS

Priority P0 | kind illustration | batch Batch 5 (Batch 0 = calibration asset) | status PLANNED | first appears 38.65s in beats B18 | construction method: **pose replacement for large changes (stand -> kneel -> step-back) + hierarchical rigid FK for small limb offsets (<= +-8 degrees) with deliberately drawn suit joint rings (hard-shell suit: UE 7.2 step 3)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Portable life-support backpack: rigid white box with a flat antenna stowed on top, two small connectors, grey strap hardware.

Manifest description: Backpack life-support system, rigid.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-001** `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg` [front, eye-level, mid-step, full body head to boots, A7L suit]: Front reference for ASTRO_001..009: proportions (head ~ 1/8 of height with PLSS making the back bulky), RCU box on the chest, creases at elbows/knees, visor as a near-opaque gold mirror with an inverted reflection plate (ASTRO_003).
- **REF-ASTRO-002** `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg` [front, eye-level, full body but small in frame (about 8-10 m away), standing next to the LM]: Basis for the 3/4 standing-rest pose (ASTRO_010) and for registration of the PLSS behind the helmet.
- **REF-ASTRO-003** `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg` [pure side profile of his left side, eye-level, standing, ~6 m away, full body, facing left toward the flag]: Side step-back pose (ASTRO_010) and PLSS depth: draw the backpack roughly as deep as the chest, antenna thin and short.
- **REF-ASTRO-004** `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg` [pure rear view, eye-level, walking away, full body, carrying two packages]: Rear view reference (the film has no rear shot planned; keep it in the pose library as a hidden-overlap check). Shows the PLSS back detail needed if the camera ever sees him walk away.
- **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]: Shows the true relative scale and low height of the array against the astronaut (array roughly knee height or below), and the rear 3/4 walking gait.
- **REF-ASTRO-006** `references/astronaut/astronaut_apollo11_rear34_striding_tool_nasa_as11-40-5964.jpg` [rear three-quarter from the astronaut's right-back, striding forward with a tool]: Rear-3/4 walking and tool-use pose; hose is a loop, not a straight tube; PLSS stays rigid while limbs swing.
- **REF-ASTRO-007** `references/astronaut/astronaut_apollo11_rear_lowangle_ladder_boot_sole_nasa_as11-40-5866.jpg` [rear, camera below, on the ground; astronaut at the LM porch with the right leg raised behind him]: Boot sole is a smooth flat slab with a raised rim in this frame (the chevron tread appears only as prints on the ground in other frames); the leg shows only soft creases, not strong accordion folds.
- **REF-ASTRO-011** `references/astronaut/astronaut_apollo12_side_bending_lean_core_tube_nasa_as12-49-7286.jpg` [side three-quarter, slightly low, bending forward at the waist, toward the left]: Bend/lean pose for the film's 'aligning the array' action: lean from the waist rather than kneeling (the A7L did not kneel easily).
- **REF-ASTRO-012** `references/astronaut/astronaut_apollo14_side_walking_lean_nasa_as14-64-9089.jpg` [side/three-quarter from his left-front, walking left with a lean, full body, eye-level]: Walking pose with forward lean and trailing foot; dust-darkening from the knee down.
- **REF-ASTRO-016** `references/astronaut/astronaut_apollo11_training_side34_bend_tool_to_ground_nasa_s69-32233.jpg` [side/3-4 profile (left figure) and front 3/4 (right figure), low wide-angle, both stooping to ground-level equipment]: Reference for the side/3-4 BEND pose in ASTRO_010: torso pitch about 30-45 degrees, knees flexed, arm reaching to the ground with an extension tool; PLSS tilts with the torso and hoses loop from the chest to the pack. Closest real evidence for the kneel/align beat (still not a kneel).
- (family context) **REF-ASTRO-008** `references/astronaut/astronaut_apollo12_lowerbody_glove_boot_dust_closeup_nasa_as12-48-7149.jpg` [front close-up, waist down, standing on boulder-strewn regolith]
- (family context) **REF-ASTRO-009** `references/astronaut/astronaut_apollo12_front34_striding_tool_visor_nasa_as12-47-6919.jpg` [front three-quarter, eye-level, striding with a tool, about 6-8 m away]
- (family context) **REF-ASTRO-010** `references/astronaut/astronaut_apollo12_front_walking_carrying_dust_spray_nasa_as12-46-6807.jpg` [front, slightly low, walking toward the camera, about 10 m away]
- (family context) **REF-ASTRO-013** `references/astronaut/astronaut_apollo16_front_airborne_jump_a7lb_nasa_as16-113-18339.jpg` [front, eye-level, airborne mid-jump, full body (A7LB suit, Apollo 16)]
- (family context) **REF-ASTRO-014** `references/astronaut/astronaut_apollo16_front_crouch_dusty_a7lb_nasa_as16-114-18423.jpg` [front, eye-level, standing on a slope with slightly flexed knees (A7LB suit, Apollo 16)]
- (family context) **REF-ASTRO-015** `references/astronaut/astronaut_apollo17_front34_stooping_dusty_a7lb_nasa_as17-145-22157.jpg` [front three-quarter, slightly low, stooping with wide stance (A7LB suit, Apollo 17)]
- (family context) **REF-ASTRO-018** `references/astronaut/astronaut_apollo11_training_low34_double_bend_scoop_tongs_nasa_s69-32245.jpg` [low-angle 3/4, two figures stooped forward, portrait frame]
- (family context) **REF-ASTRO-023** `references/astronaut/astronaut_apollo11_surface_front34_stoop_leveling_handle_nasa_as11-40-5951.jpg` [front 3/4 from the astronaut's left, eye-level, mid-distance, on the real lunar surface]

Web pointers (verify independently): https://www.nasa.gov/wp-content/uploads/static/history/alsj/tnD8093EMUDevelop.pdf (SNIPPET); NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22)

## 3. Intended camera angles
3/4 view (all poses); side view (step-back)

## 4. Required geometry and proportions
PLSS width 0.78 of torso width, height 0.9 of torso height; rigid rectangle with rounded edges; in the side view it extends 0.2 of figure height behind the torso; antenna folded.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Suit white #ECEEF4 (never pure white), gold visor #D6AA46, grey overshoes/gloves #8E929C, connector rings blue/red/silver; hard lunar sunlight from the left, long shadows to the right.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Rigid, same in all poses; visible edge behind the helmet in the 3/4 views.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `astro_plss_stand34` | backpack | `astro_torso_stand34` | mount on torso upper-back | 43 |
| `astro_plss_stand34` | backpack | `astro_torso_kneel34` | mount on torso upper-back | 43 |
| `astro_plss_stand34` | backpack | `astro_torso_side_step` | mount on torso upper-back | 43 |
| `astro_plss_kneel34` | backpack | `astro_torso_stand34` | mount on torso upper-back | 43 |
| `astro_plss_kneel34` | backpack | `astro_torso_kneel34` | mount on torso upper-back | 43 |
| `astro_plss_kneel34` | backpack | `astro_torso_side_step` | mount on torso upper-back | 43 |
| `astro_plss_side_step` | backpack | `astro_torso_stand34` | mount on torso upper-back | 43 |
| `astro_plss_side_step` | backpack | `astro_torso_kneel34` | mount on torso upper-back | 43 |
| `astro_plss_side_step` | backpack | `astro_torso_side_step` | mount on torso upper-back | 43 |

Parent group: `ASTRO_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Backpack extends 2% of canvas width into the torso silhouette (hidden).
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `ASTRO_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **delivered per pose, 3000x3000 each, same scale and registration across poses**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): mount on torso. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
rigid (moves with the torso)
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P05, P06**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly delivered per pose, 3000x3000 each, same scale and registration across poses; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Apollo 11 A7L suit; no face, no name, no patch text; kneel is STYLISED (no photograph shows it); rear view, walking, top view are not planned; no cloth flutter in vacuum.

Must not change: Costume, helmet, gold visor, PLSS, gloved hands and boots identical in every pose; no face visible; no named patch; sun from the left; height ratio to the 46 cm reflector panel fixed.

Known failure modes: face visible in the visor; bare hands; extra or fused fingers; detached equipment; cloth billowing; joint caps that are round discs; different boots left/right; proportions drifting between poses.

## 16. Expected deliverable filenames
`astro_plss_{stand34,kneel34,side_step}_3000x3000.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
