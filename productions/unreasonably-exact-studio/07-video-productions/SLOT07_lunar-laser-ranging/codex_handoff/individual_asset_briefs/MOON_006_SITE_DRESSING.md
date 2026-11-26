# Brief: MOON_006_SITE_DRESSING

Priority P2 | kind illustration | batch Batches 1 and 3 | status PLANNED | first appears 38.65s in beats B18 | construction method: **sprite (static)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
OPTIONAL distant Apollo 11 site details: a flag silhouette, TV camera on a tripod, seismometer package, foil-covered descent stage fragment. Generic silhouettes.

Manifest description: OPTIONAL distant Apollo 11 site details seen in AS11-40-5948: flag, TV camera, seismometer silhouettes. Flag does NOT flutter (vacuum).

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-ASTRO-005** `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg` [rear three-quarter from behind-right, walking away, left of frame; LRRR small in the mid-distance]: Shows the true relative scale and low height of the array against the astronaut (array roughly knee height or below), and the rear 3/4 walking gait.
- (family context) **REF-MOON-018** `references/moon/moon_limb_large_clean_edge_earth_behind_artemis2_nasa_art002e009287.jpg` [large Moon limb with a razor-sharp edge against black, half-lit; tiny Earth crescent behind the limb]
- (family context) **REF-MOON-019** `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg` [very low oblique view of the lunar horizon, Earth crescent dipping behind the limb]
- (family context) **REF-MOON-020** `references/moon/moon_through_atmosphere_flattened_refraction_airglow_iss_nasa_iss039e001440.jpg` [telephoto view of the Moon at the moment of setting behind the limb, from the ISS]
- (family context) **REF-MOON-021** `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg` [ground-level wide view over sunlit dust to a shadowed slope and a far ridge, rover at left]
- (family context) **REF-MOON-001** `references/moon/moon_nearside_fullmoon_lro_svs_nasa_e001861.jpg` [near-side full disc, north up, full phase; computer visualization from LRO data, not a photograph]
- (family context) **REF-MOON-002** `references/moon/moon_phase_firstquarter_lro_svs_nasa_e001863.jpg` [near-side disc, first quarter: right half lit, terminator running diagonally from upper centre to lower left]
- (family context) **REF-MOON-003** `references/moon/moon_phase_waxingcrescent_lro_svs_nasa_e001864.jpg` [near-side disc, waxing crescent; only a right-hand crescent lit]
- (family context) **REF-MOON-004** `references/moon/moon_terminator_artemis2_nasa_art002e014045.jpg` [oblique photo of the Moon's limb and terminator from the Orion window during the lunar flyby]

Web pointers (verify independently): NASA photo AS11-40-5948 (cited on https://lroc.im-ldi.com/images/22)

## 3. Intended camera angles
surface view, far midground

## 4. Required geometry and proportions
2048x1024 strip, items at 2-5% of image height (far midground), flag static and unfurled-by-wire (horizontal rod), TV camera tripod 3 legs.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Highlights #ACACB0, mid #7E7E84, shadow #3A3A42; maria #55555D to #6A6A72 (cooler, darker); sky black #000000-#05070D.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA. Flag hangs in a fixed folded shape (vacuum, no flutter).

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `moon_site_flag` | flag + pole | `MOON_006_SITE_DRESSING` | pole base | 30 |
| `moon_site_tv` | TV camera tripod | `MOON_006_SITE_DRESSING` | tripod base | 31 |
| `moon_site_seismo` | seismometer silhouette | `MOON_006_SITE_DRESSING` | base | 32 |

Parent group: `MOON_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: MOON_003_HORIZON.

## 9. Hidden overlap requirements
n/a (static silhouettes)
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `MOON_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2048x1024**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): base-centre. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
static
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **none**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2048x1024; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
No named patch or insignia; the flag has no readable stripes at this size; optional asset.

Must not change: Near side only; same maria/highlands layout in every Moon asset; sun from the left; black sky, hard shadows, sharp horizon, no atmosphere haze; no flag or hardware unless the brief names it.

Known failure modes: Earth-like colours; craters repeating visibly; atmosphere haze; shadows pointing the wrong way; horizon too close or too curved for the camera height.

## 16. Expected deliverable filenames
`moon_site_{flag,tv,seismo}.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
