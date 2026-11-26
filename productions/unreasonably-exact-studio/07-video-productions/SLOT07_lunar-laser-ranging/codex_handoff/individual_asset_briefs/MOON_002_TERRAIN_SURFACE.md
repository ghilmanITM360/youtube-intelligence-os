# Brief: MOON_002_TERRAIN_SURFACE

Priority P0 | kind illustration | batch Batches 1 and 3 | status PLANNED | first appears 32.37s in beats B15 B16 B17 B18 | construction method: **2.5D rigid layers with real parallax factors (near 1.0, mid 0.6, far 0.3)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Lunar regolith ground plane in perspective as seen from a standing astronaut eye level (about 1.7 m). Low albedo, HARD-lit grey regolith, not sand.

Manifest description: Grey fine regolith ground plane in perspective; low albedo (dark grey) but HARD-LIT: crisp black shadows from the single sun direction, no fill light, no atmosphere haze, sharp horizon (reference: Apollo 11/12 surface photographs).

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]: Shows the true relative scale and low height of the array against the astronaut (array roughly knee height or below), and the rear 3/4 walking gait.
- **REF-EARTH-009** `references/earth/earth_rising_moonhorizon_apollo11_nasa_as11-44-6552.jpg` [from lunar orbit looking across the surface; partly lit (gibbous) Earth above the lunar horizon]: Earth is much brighter than the surface, with a clear blue/grey contrast; lunar horizon edge with zero haze. The caption places the terrain at about 85 deg E, 3 deg N on the near side (Smyth's Sea).
- **REF-ASTRO-026** `references/astronaut/astronaut_apollo15_rear34_stoop_reach_boulder_long_shadow_nasa_as15-85-11437.jpg` [rear 3/4, eye-level-ish, wide shot; astronaut small at upper left on a slope, rover at right]: Shows the full-body bend-and-reach silhouette from behind on the real surface, and that the cast shadow is a distorted long silhouette (about 3-4 body lengths) for ASTRO_011/RETRO_006; the horizon is a smooth hill line against pure black.
- **REF-MOON-021** `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg` [ground-level wide view over sunlit dust to a shadowed slope and a far ridge, rover at left]: Strong reference for MOON_002/003: shadowed slopes go to near-black with a sharp lit/unlit boundary, horizon is a clean ridge line, ground texture is fine crisp pocks not sand ripples; shadow lengths show a lowish Sun.
- **REF-MOON-005** `references/moon/moon_terminator_craters_artemis2_nasa_art002e014055.jpg` [oblique close-up of cratered terrain at the terminator; the limb curves across the top]: Crater look for the globe: circular, overlapping, with floors in shadow under side light; helps match texture appearance for the highland areas.
- **REF-MOON-007** `references/moon/moon_copernicus_crater_lroc_nasa_pia13524.jpg` [close-up (metres per pixel scale) of the rugged interior of Copernicus, high-resolution LROC NAC style]: Rock sprite distribution: boulders cluster rather than scatter uniformly; shadows are pure black and hard-edged; ground texture is fine-grained grey.
- **REF-MOON-010** `references/moon/moon_regolith_bootprint_apollo11_nasa_as11-40-5878.jpg` [close-up oblique macro of the soil (70 mm lunar surface camera per the caption)]: Boot-print sprites should have crisp, near-vertical walls and visible tread with a deep black shadow; the soil texture should be fine-grained speckle, not smooth sand. Dust in the film must be ballistic, since the soil is fine and dry (MOON_007).
- **REF-MOON-011** `references/moon/moon_surface_longshadow_apollo12_nasa_as12-46-6813.jpg` [ground-level wide view across the site; low horizon about 40 percent down from the top, lunar module in the left background]: Ground brightness varies strongly with sun angle: with the Sun behind the camera, the ground is lighter and shadows are hidden; dark soil from this site looks darker than at Apollo 11. Foot-track texture adds scale (about 30 cm boot length).
- (family context) **REF-MOON-018** `references/moon/moon_limb_large_clean_edge_earth_behind_artemis2_nasa_art002e009287.jpg` [large Moon limb with a razor-sharp edge against black, half-lit; tiny Earth crescent behind the limb]
- (family context) **REF-MOON-019** `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg` [very low oblique view of the lunar horizon, Earth crescent dipping behind the limb]
- (family context) **REF-MOON-020** `references/moon/moon_through_atmosphere_flattened_refraction_airglow_iss_nasa_iss039e001440.jpg` [telephoto view of the Moon at the moment of setting behind the limb, from the ISS]
- (family context) **REF-MOON-001** `references/moon/moon_nearside_fullmoon_lro_svs_nasa_e001861.jpg` [near-side full disc, north up, full phase; computer visualization from LRO data, not a photograph]
- (family context) **REF-MOON-002** `references/moon/moon_phase_firstquarter_lro_svs_nasa_e001863.jpg` [near-side disc, first quarter: right half lit, terminator running diagonally from upper centre to lower left]
- (family context) **REF-MOON-003** `references/moon/moon_phase_waxingcrescent_lro_svs_nasa_e001864.jpg` [near-side disc, waxing crescent; only a right-hand crescent lit]
- (family context) **REF-MOON-004** `references/moon/moon_terminator_artemis2_nasa_art002e014045.jpg` [oblique photo of the Moon's limb and terminator from the Orion window during the lunar flyby]
- (family context) **REF-MOON-006** `references/moon/moon_farside_lroc_wac_nasa_e001939.jpg` [far-side orthographic view centred at 180 deg longitude, 0 deg latitude; grayscale LROC mosaic]

Web pointers (verify independently): NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22)

## 3. Intended camera angles
low lunar-surface 3/4 view, slow parallax

## 4. Required geometry and proportions
2160x3840 portrait; camera 1.7 m high, looking slightly down; horizon at 36% from the top (its position is fixed by MOON_003); ground fills below with perspective foreshortening; fine texture scale 3 mm near to 3 cm far; a few shallow craters, oblique.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Highlights #ACACB0, mid #7E7E84, shadow #3A3A42; maria #55555D to #6A6A72 (cooler, darker); sky black #000000-#05070D.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA, top edge soft alpha (~64 px) to blend into the horizon layer. Crisp, long shadows from the left sun fall to the right; no fill light, no haze.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `moon_terrain_near` | near regolith strip with foot-scale texture | `MOON_000_SYSTEM` | none | 42 |
| `moon_terrain_mid` | mid plane with craters | `MOON_000_SYSTEM` | none | 41 |
| `moon_terrain_far` | far plane flattening to the horizon | `MOON_000_SYSTEM` | none | 40 |

Parent group: `MOON_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Each strip overlaps the next by 6% of canvas height with matched texture so parallax never exposes a gap.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `MOON_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2160x3840 px (2x of 1080x1920)**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): none. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
parallax layer only
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P05**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2160x3840 px (2x of 1080x1920); alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
No atmospheric perspective: distant ground stays sharp (vacuum). Terrain is generic, not the real Apollo 11 landscape.

Must not change: Near side only; same maria/highlands layout in every Moon asset; sun from the left; black sky, hard shadows, sharp horizon, no atmosphere haze; no flag or hardware unless the brief names it.

Known failure modes: Earth-like colours; craters repeating visibly; atmosphere haze; shadows pointing the wrong way; horizon too close or too curved for the camera height.

## 16. Expected deliverable filenames
`moon_terrain_{near,mid,far}_2160x3840.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
