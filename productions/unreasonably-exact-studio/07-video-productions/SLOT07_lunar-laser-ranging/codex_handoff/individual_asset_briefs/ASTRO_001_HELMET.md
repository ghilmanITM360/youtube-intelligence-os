# Brief: ASTRO_001_HELMET

Priority P0 | kind illustration | batch Batch 5 (Batch 0 = calibration asset) | status PLANNED | first appears 38.65s in beats B18 | construction method: **pose replacement for large changes (stand -> kneel -> step-back) + hierarchical rigid FK for small limb offsets (<= +-8 degrees) with deliberately drawn suit joint rings (hard-shell suit: UE 7.2 step 3)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Apollo A7L helmet: white outer shell with neck ring (blue/red/silver disc rings), communication cap hidden under the helmet cover; face hidden by the gold visor.

Manifest description: Polycarbonate helmet shell, neck ring, communication cap.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-001** `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg` [front, eye-level, mid-step, full body head to boots, A7L suit]: Front reference for ASTRO_001..009: proportions (head ~ 1/8 of height with PLSS making the back bulky), RCU box on the chest, creases at elbows/knees, visor as a near-opaque gold mirror with an inverted reflection plate (ASTRO_003).
- **REF-ASTRO-002** `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg` [front, eye-level, full body but small in frame (about 8-10 m away), standing next to the LM]: Basis for the 3/4 standing-rest pose (ASTRO_010) and for registration of the PLSS behind the helmet.
- **REF-ASTRO-017** `references/astronaut/astronaut_apollo11_training_front34_and_rear34_reach_equipment_nasa_s69-32243.jpg` [front 3/4 eye-level (left figure) and rear 3/4 bending to equipment (right figure), low wide angle]: Gives BOTH a front-3/4 gold-visor view with the face visible inside and a rear-3/4 bend with PLSS back plate; use for glove-on-equipment contact and for hose routing behind the torso.
- **REF-ASTRO-019** `references/astronaut/astronaut_apollo11_training_pure_side_profile_helmet_visor_pole_nasa_s69-32247.jpg` [pure side profile, eye-level, full body, single astronaut, plain black background]: Best SIDE reference for the step-back pose (ASTRO_010) and for registering the helmet/visor, hose and PLSS silhouette from the side; the helmet is a rounded dome with the visor assembly projecting forward and the PLSS about as deep as the torso.
- **REF-ASTRO-020** `references/astronaut/astronaut_apollo11_training_side34_helmet_visor_tool_lm_leg_nasa_s69-32248.jpg` [side/3-4 profile facing right, mid-body close, portrait frame]: Primary close helmet reference at medium scale (fills about 1/3 of the frame height): visor assembly sits proud of the shell, communications cap and neck ring are distinct pieces, hoses leave the chest to loop behind.
- **REF-ASTRO-024** `references/astronaut/astronaut_apollo11_helmet_visor_closeup_crop_nasa_as11-40-5903.jpg` [front, eye-level, tight head and shoulders crop (native pixels, 1150x1050) of AS11-40-5903]: CLOSE HELMET REFERENCE (fills the gap of ASTRO_001 having only full-body shots): quilted helmet cover with fasteners, visor opening with a dark seal ring, neck ring and collar; the visor reflection plate (ASTRO_003) is an inverted fisheye of a bright foreground, a long dark cast shadow, the LM with gold foil and a small standing figure.
- **REF-ASTRO-027** `references/astronaut/astronaut_apollo15_rear34_turned_camera_dusty_plss_nasa_as15-85-11514.jpg` [rear-right 3/4, eye-level, large in frame; torso turned, helmet in near profile, holding a camera]: Best REAL rear-3/4 reference with the helmet turned to near-profile: PLSS+OPS pack mass dominates the back, helmet sits forward of the pack, and the whole suit is dust-grey below the waist.
- (family context) **REF-ASTRO-003** `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg` [pure side profile of his left side, eye-level, standing, ~6 m away, full body, facing left toward the flag]
- (family context) **REF-ASTRO-004** `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg` [pure rear view, eye-level, walking away, full body, carrying two packages]
- (family context) **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]
- (family context) **REF-ASTRO-006** `references/astronaut/astronaut_apollo11_rear34_striding_tool_nasa_as11-40-5964.jpg` [rear three-quarter from the astronaut's right-back, striding forward with a tool]
- (family context) **REF-ASTRO-007** `references/astronaut/astronaut_apollo11_rear_lowangle_ladder_boot_sole_nasa_as11-40-5866.jpg` [rear, camera below, on the ground; astronaut at the LM porch with the right leg raised behind him]
- (family context) **REF-ASTRO-008** `references/astronaut/astronaut_apollo12_lowerbody_glove_boot_dust_closeup_nasa_as12-48-7149.jpg` [front close-up, waist down, standing on boulder-strewn regolith]
- (family context) **REF-ASTRO-009** `references/astronaut/astronaut_apollo12_front34_striding_tool_visor_nasa_as12-47-6919.jpg` [front three-quarter, eye-level, striding with a tool, about 6-8 m away]
- (family context) **REF-ASTRO-010** `references/astronaut/astronaut_apollo12_front_walking_carrying_dust_spray_nasa_as12-46-6807.jpg` [front, slightly low, walking toward the camera, about 10 m away]

Web pointers (verify independently): https://www.nasa.gov/wp-content/uploads/static/history/alsj/tnD8093EMUDevelop.pdf (SNIPPET); NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22)

## 3. Intended camera angles
3/4 view (all poses); side view (step-back)

## 4. Required geometry and proportions
Helmet height = 1/8 of figure height; neck ring Ø 0.7x helmet width; viewed 3/4: helmet width 1.0, depth 1.05 (slightly deeper); side view: helmet silhouette with the PLSS top directly behind.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Suit white #ECEEF4 (never pure white), gold visor #D6AA46, grey overshoes/gloves #8E929C, connector rings blue/red/silver; hard lunar sunlight from the left, long shadows to the right.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Same helmet in every pose; neck angle follows the torso (kneel: head down ~20 degrees).

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `astro_helmet_stand34` | helmet shell + neck ring | `astro_torso_stand34` | neck ring centre | 42 |
| `astro_helmet_stand34` | helmet shell + neck ring | `astro_torso_kneel34` | neck ring centre | 42 |
| `astro_helmet_stand34` | helmet shell + neck ring | `astro_torso_side_step` | neck ring centre | 42 |
| `astro_helmet_kneel34` | helmet shell + neck ring | `astro_torso_stand34` | neck ring centre | 42 |
| `astro_helmet_kneel34` | helmet shell + neck ring | `astro_torso_kneel34` | neck ring centre | 42 |
| `astro_helmet_kneel34` | helmet shell + neck ring | `astro_torso_side_step` | neck ring centre | 42 |
| `astro_helmet_side_step` | helmet shell + neck ring | `astro_torso_stand34` | neck ring centre | 42 |
| `astro_helmet_side_step` | helmet shell + neck ring | `astro_torso_kneel34` | neck ring centre | 42 |
| `astro_helmet_side_step` | helmet shell + neck ring | `astro_torso_side_step` | neck ring centre | 42 |

Parent group: `ASTRO_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Neck ring extends 1.2% of canvas width into the torso collar.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `ASTRO_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **delivered per pose, 3000x3000 each, same scale and registration across poses**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): neck ring. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
head rotation <= 4 degrees; no face motion
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
`astro_helmet_{stand34,kneel34,side_step}_3000x3000.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
