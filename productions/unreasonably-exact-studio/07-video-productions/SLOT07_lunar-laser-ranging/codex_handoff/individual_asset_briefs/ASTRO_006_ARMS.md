# Brief: ASTRO_006_ARMS

Priority P0 | kind illustration | batch Batch 5 (Batch 0 = calibration asset) | status PLANNED | first appears 38.65s in beats B18 | construction method: **pose replacement for large changes (stand -> kneel -> step-back) + hierarchical rigid FK for small limb offsets (<= +-8 degrees) with deliberately drawn suit joint rings (hard-shell suit: UE 7.2 step 3)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Upper arm + forearm, left and right, white fabric suit with elbow convolute rings.

Manifest description: Upper arm and forearm, left and right, with hidden overlap at shoulder and elbow.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-001** `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg` [front, eye-level, mid-step, full body head to boots, A7L suit]: Front reference for ASTRO_001..009: proportions (head ~ 1/8 of height with PLSS making the back bulky), RCU box on the chest, creases at elbows/knees, visor as a near-opaque gold mirror with an inverted reflection plate (ASTRO_003).
- **REF-ASTRO-006** `references/astronaut/astronaut_apollo11_rear34_striding_tool_nasa_as11-40-5964.jpg` [rear three-quarter from the astronaut's right-back, striding forward with a tool]: Rear-3/4 walking and tool-use pose; hose is a loop, not a straight tube; PLSS stays rigid while limbs swing.
- **REF-ASTRO-009** `references/astronaut/astronaut_apollo12_front34_striding_tool_visor_nasa_as12-47-6919.jpg` [front three-quarter, eye-level, striding with a tool, about 6-8 m away]: Equipment-interaction pose reference: rod/handle held at chest height, torso tilted forward (about 10-15 degrees, estimated by eye).
- **REF-ASTRO-011** `references/astronaut/astronaut_apollo12_side_bending_lean_core_tube_nasa_as12-49-7286.jpg` [side three-quarter, slightly low, bending forward at the waist, toward the left]: Bend/lean pose for the film's 'aligning the array' action: lean from the waist rather than kneeling (the A7L did not kneel easily).
- **REF-ASTRO-016** `references/astronaut/astronaut_apollo11_training_side34_bend_tool_to_ground_nasa_s69-32233.jpg` [side/3-4 profile (left figure) and front 3/4 (right figure), low wide-angle, both stooping to ground-level equipment]: Reference for the side/3-4 BEND pose in ASTRO_010: torso pitch about 30-45 degrees, knees flexed, arm reaching to the ground with an extension tool; PLSS tilts with the torso and hoses loop from the chest to the pack. Closest real evidence for the kneel/align beat (still not a kneel).
- **REF-ASTRO-017** `references/astronaut/astronaut_apollo11_training_front34_and_rear34_reach_equipment_nasa_s69-32243.jpg` [front 3/4 eye-level (left figure) and rear 3/4 bending to equipment (right figure), low wide angle]: Gives BOTH a front-3/4 gold-visor view with the face visible inside and a rear-3/4 bend with PLSS back plate; use for glove-on-equipment contact and for hose routing behind the torso.
- **REF-ASTRO-018** `references/astronaut/astronaut_apollo11_training_low34_double_bend_scoop_tongs_nasa_s69-32245.jpg` [low-angle 3/4, two figures stooped forward, portrait frame]: Reference for the deepest realistic bend (closest to a crouch) with both arms in front; shows knee flexion and the way the PLSS rides high behind the head.
- **REF-ASTRO-022** `references/astronaut/astronaut_apollo15_training_pure_side_bend_carry_instrument_nasa_71pc-0470.jpg` [pure side view, eye-level to slightly low, medium shot, bending forward carrying an instrument box]: Side-profile bend reference with the A7LB-type suit: shows PLSS tilting with the spine, belt/strap detail and boot shape; pairs with S69-32233 for the bend range.
- **REF-ASTRO-023** `references/astronaut/astronaut_apollo11_surface_front34_stoop_leveling_handle_nasa_as11-40-5951.jpg` [front 3/4 from the astronaut's left, eye-level, mid-distance, on the real lunar surface]: Only real-surface photo of an astronaut interacting with a deployed package by tool: slight stoop, handle at 45 degrees to the ground, both gloves on equipment. Use it for the arm/handle geometry of the align beat; the kneel itself is still stylised.
- **REF-ASTRO-027** `references/astronaut/astronaut_apollo15_rear34_turned_camera_dusty_plss_nasa_as15-85-11514.jpg` [rear-right 3/4, eye-level, large in frame; torso turned, helmet in near profile, holding a camera]: Best REAL rear-3/4 reference with the helmet turned to near-profile: PLSS+OPS pack mass dominates the back, helmet sits forward of the pack, and the whole suit is dust-grey below the waist.
- (family context) **REF-ASTRO-002** `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg` [front, eye-level, full body but small in frame (about 8-10 m away), standing next to the LM]
- (family context) **REF-ASTRO-003** `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg` [pure side profile of his left side, eye-level, standing, ~6 m away, full body, facing left toward the flag]
- (family context) **REF-ASTRO-004** `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg` [pure rear view, eye-level, walking away, full body, carrying two packages]
- (family context) **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]
- (family context) **REF-ASTRO-007** `references/astronaut/astronaut_apollo11_rear_lowangle_ladder_boot_sole_nasa_as11-40-5866.jpg` [rear, camera below, on the ground; astronaut at the LM porch with the right leg raised behind him]
- (family context) **REF-ASTRO-008** `references/astronaut/astronaut_apollo12_lowerbody_glove_boot_dust_closeup_nasa_as12-48-7149.jpg` [front close-up, waist down, standing on boulder-strewn regolith]
- (family context) **REF-ASTRO-010** `references/astronaut/astronaut_apollo12_front_walking_carrying_dust_spray_nasa_as12-46-6807.jpg` [front, slightly low, walking toward the camera, about 10 m away]
- (family context) **REF-ASTRO-012** `references/astronaut/astronaut_apollo14_side_walking_lean_nasa_as14-64-9089.jpg` [side/three-quarter from his left-front, walking left with a lean, full body, eye-level]

Web pointers (verify independently): https://www.nasa.gov/wp-content/uploads/static/history/alsj/tnD8093EMUDevelop.pdf (SNIPPET); NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22)

## 3. Intended camera angles
3/4 view (all poses); side view (step-back)

## 4. Required geometry and proportions
Upper arm 0.17 of figure height, forearm 0.15; elbow ring Ø 0.045 of height; shoulder ring Ø 0.06 of height; arms bagged, loose folds at the elbow; both arms present in every pose (near and far).

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Suit white #ECEEF4 (never pure white), gold visor #D6AA46, grey overshoes/gloves #8E929C, connector rings blue/red/silver; hard lunar sunlight from the left, long shadows to the right.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Stand: arms relaxed, elbows 20 degrees flexed. Kneel: near arm reaches forward-down to the reflector; far arm braces on the knee. Side step: arms slightly out.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `astro_upper_arm_near_stand34` | upper arm near | `astro_torso_stand34` | shoulder | 48 |
| `astro_upper_arm_near_kneel34` | upper arm near | `astro_torso_kneel34` | shoulder | 48 |
| `astro_upper_arm_near_side_step` | upper arm near | `astro_torso_side_step` | shoulder | 48 |
| `astro_forearm_near_stand34` | forearm near | `astro_upper_arm_near_stand34` | elbow | 49 |
| `astro_forearm_near_kneel34` | forearm near | `astro_upper_arm_near_kneel34` | elbow | 49 |
| `astro_forearm_near_side_step` | forearm near | `astro_upper_arm_near_side_step` | elbow | 49 |
| `astro_upper_arm_far_stand34` | upper arm far (behind torso) | `astro_torso_stand34` | shoulder | 40 |
| `astro_upper_arm_far_kneel34` | upper arm far (behind torso) | `astro_torso_kneel34` | shoulder | 40 |
| `astro_upper_arm_far_side_step` | upper arm far (behind torso) | `astro_torso_side_step` | shoulder | 40 |
| `astro_forearm_far_stand34` | forearm far | `astro_upper_arm_far_stand34` | elbow | 41 |
| `astro_forearm_far_kneel34` | forearm far | `astro_upper_arm_far_kneel34` | elbow | 41 |
| `astro_forearm_far_side_step` | forearm far | `astro_upper_arm_far_side_step` | elbow | 41 |

Parent group: `ASTRO_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Each child extends 1.5% of canvas width under its parent as bagged fabric with a drawn joint ring, never a generic round cap.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `ASTRO_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **delivered per pose, 3000x3000 each, same scale and registration across poses**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): shoulder, elbow. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
shoulder +-30, elbow 0-100 degrees (extremes tested in P05)
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
`astro_{upper_arm,forearm}_{near,far}_{stand34,kneel34,side_step}_3000x3000.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
