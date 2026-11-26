# Brief: MOON_005_PROPS

Priority P0 | kind illustration | batch Batches 1 and 3 | status PLANNED | first appears 32.37s in beats B15 B16 B17 B18 | construction method: **sprite replacement (static)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Sprite sheet of regolith props: rocks, small oblique craters, boot prints, clumps. Boot prints give scale beside the reflector.

Manifest description: Sprite sheet: rocks (3 sizes), small craters (oblique), boot prints (4), regolith clumps. Footprints give scale next to the reflector.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]: Shows the true relative scale and low height of the array against the astronaut (array roughly knee height or below), and the rear 3/4 walking gait.
- **REF-MOON-007** `references/moon/moon_copernicus_crater_lroc_nasa_pia13524.jpg` [close-up (metres per pixel scale) of the rugged interior of Copernicus, high-resolution LROC NAC style]: Rock sprite distribution: boulders cluster rather than scatter uniformly; shadows are pure black and hard-edged; ground texture is fine-grained grey.
- **REF-MOON-010** `references/moon/moon_regolith_bootprint_apollo11_nasa_as11-40-5878.jpg` [close-up oblique macro of the soil (70 mm lunar surface camera per the caption)]: Boot-print sprites should have crisp, near-vertical walls and visible tread with a deep black shadow; the soil texture should be fine-grained speckle, not smooth sand. Dust in the film must be ballistic, since the soil is fine and dry (MOON_007).
- **REF-MOON-011** `references/moon/moon_surface_longshadow_apollo12_nasa_as12-46-6813.jpg` [ground-level wide view across the site; low horizon about 40 percent down from the top, lunar module in the left background]: Ground brightness varies strongly with sun angle: with the Sun behind the camera, the ground is lighter and shadows are hidden; dark soil from this site looks darker than at Apollo 11. Foot-track texture adds scale (about 30 cm boot length).
- **REF-MOON-012** `references/moon/moon_tranquility_base_lroc_nasa_pia12925.jpg` [orbital top-down view of the Apollo 11 site with the Sun almost overhead; the scale bar is 200 m]: Use as a locating reference: the Apollo 11 site is in a flat plain with small craters and a nearby bright crater (West) to the east. The reflector is a few metres across, sub-pixel here, so a ring marker in B05 should be drawn as a symbol, not a feature.
- (family context) **REF-MOON-018** `references/moon/moon_limb_large_clean_edge_earth_behind_artemis2_nasa_art002e009287.jpg` [large Moon limb with a razor-sharp edge against black, half-lit; tiny Earth crescent behind the limb]
- (family context) **REF-MOON-019** `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg` [very low oblique view of the lunar horizon, Earth crescent dipping behind the limb]
- (family context) **REF-MOON-020** `references/moon/moon_through_atmosphere_flattened_refraction_airglow_iss_nasa_iss039e001440.jpg` [telephoto view of the Moon at the moment of setting behind the limb, from the ISS]
- (family context) **REF-MOON-021** `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg` [ground-level wide view over sunlit dust to a shadowed slope and a far ridge, rover at left]
- (family context) **REF-MOON-001** `references/moon/moon_nearside_fullmoon_lro_svs_nasa_e001861.jpg` [near-side full disc, north up, full phase; computer visualization from LRO data, not a photograph]
- (family context) **REF-MOON-002** `references/moon/moon_phase_firstquarter_lro_svs_nasa_e001863.jpg` [near-side disc, first quarter: right half lit, terminator running diagonally from upper centre to lower left]
- (family context) **REF-MOON-003** `references/moon/moon_phase_waxingcrescent_lro_svs_nasa_e001864.jpg` [near-side disc, waxing crescent; only a right-hand crescent lit]
- (family context) **REF-MOON-004** `references/moon/moon_terminator_artemis2_nasa_art002e014045.jpg` [oblique photo of the Moon's limb and terminator from the Orion window during the lunar flyby]

Web pointers (verify independently): NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22); https://ilrs.gsfc.nasa.gov/missions/satellite_missions/current_missions/ap11_reflector.html (boot prints)

## 3. Intended camera angles
surface view

## 4. Required geometry and proportions
4096x4096 sheet, individual sprites <= 1024 px, 6 rocks (3 sizes x 2 shapes, angular not round), 4 boot prints (~30 cm long, chevron tread, left/right pairs), 4 small craters (oblique), 4 clump piles; gutter 32 px; sprite base-centre registered.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Highlights #ACACB0, mid #7E7E84, shadow #3A3A42; maria #55555D to #6A6A72 (cooler, darker); sky black #000000-#05070D.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA, shadows NOT baked (code adds them from the sun vector).

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `moon_props_sheet` | all sprites on one sheet | `MOON_005_PROPS` | base-centre of each sprite (listed in PIVOTS.json) | 50 |

Parent group: `MOON_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: MOON_002_TERRAIN_SURFACE.

## 9. Hidden overlap requirements
Not applicable (static); 8 px alpha padding around every sprite.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `MOON_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x4096 sheet, individual sprites <= 1024 px**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): base-centre of each sprite. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
static
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P05**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 4096x4096 sheet, individual sprites <= 1024 px; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Boot-print size ~30 cm is a design size (qualitative scale cue only).

Must not change: Near side only; same maria/highlands layout in every Moon asset; sun from the left; black sky, hard shadows, sharp horizon, no atmosphere haze; no flag or hardware unless the brief names it.

Known failure modes: Earth-like colours; craters repeating visibly; atmosphere haze; shadows pointing the wrong way; horizon too close or too curved for the camera height.

## 16. Expected deliverable filenames
`moon_props_sheet_4096x4096.png + PIVOTS.json`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
