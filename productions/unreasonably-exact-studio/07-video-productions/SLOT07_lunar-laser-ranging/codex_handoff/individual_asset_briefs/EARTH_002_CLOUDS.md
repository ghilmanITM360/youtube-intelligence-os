# Brief: EARTH_002_CLOUDS

Priority P0 | kind texture | batch Batch 1 | status PLANNED | first appears 8.04s in beats B05 B06 B07 B08 B09 B10 B11 B12 B13 B25 B31 B32 B33 B34 B35 B36 B37 B39 | construction method: **Codex generates cloud tiles at native size (<= ~1500 px, flat-lit, alpha); Claude tiles/blends them into the 4096x2048 wrap-safe layer; clouds drift at ~0.1-0.3 deg/s in code**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Independent cloud layer for Earth (alpha-only formations: frontal bands, a tropical convective belt, cyclonic swirls). Authored from the cloud references; NOT cut from a satellite composite.

Manifest description: Independent cloud layer: white cloud formations with soft alpha, no shadow, drifts slower than the surface. No transparent public cloud layer exists: it is authored from the cloud references.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-EARTH-001** `references/earth/earth_fullglobe_translunar_nasa_as17-148-22727.jpg` [full sunlit disc, south at bottom, translunar coast (tens of thousands of km)]: Colour target for the Earth globe: ocean deep blue (not cyan), land ochre/brown/green, clouds pure white with soft alpha, limb rim thin and pale blue. Clouds cover roughly half the disc, so cloud alpha should be dense, not sprinkled.
- **REF-EARTH-002** `references/earth/earth_fullglobe_composite_nasa_bluemarble2012_e001788.jpg` [full disc, Africa/Middle East/India, composite from low Earth orbit data rendered as if from far away]: Atmosphere ring in code: thin, dim, cool-blue halo outside the limb, fading to black within about 1-2 percent of the radius. Do NOT copy the vertical swath streaks (artefacts).
- **REF-EARTH-003** `references/earth/earth_moon_transit_dscovr_epic_nasa_e000670.png` [full disc seen from the Sun-Earth L1 point (about a million miles per caption); Moon lies between camera and Earth]: Shows that Earth is much brighter than the Moon (Earth geometric albedo 0.434 vs Moon 0.12 in the NASA fact sheets): when both appear in one frame keep the Earth visibly brighter and bluer. Warns that any perspective frame with the Moon nearer to the camera must not use the 0.2727 ratio.
- **REF-EARTH-013** `references/earth/earth_clouds_equirect_svs_nasa_3615.jpg` [equirectangular 2:1 map with clouds baked in]: Cloud layer design: swirled mid-latitude bands and an equatorial belt, clear subtropical deserts (Sahara, Australia), clean poles. Authoring an RGBA cloud PNG from scratch should follow this distribution, and alpha must be soft.
- **REF-EARTH-014** `references/earth/earth_layers_cloud_atmos_nightlight_svs_nasa_5570.jpg` [3D render, full lit globe viewed from slightly north of the equator, Asia/Australia, with a star field]: Look-development target for the globe: soft atmosphere rim (brighter near the sun, weak elsewhere), no hard terminator, night lights hugging the dark side, cloud highlights. Supports the 5-layer split as the industry approach.
- **REF-EARTH-021** `references/earth/earth_limb_edge_on_sunrise_cloud_silhouette_shuttle_nasa_sts047-54-018.jpg` [edge-on limb, tilted, with silhouetted cumulus in the foreground and a sun glint]: Shows clouds as a thin textured layer on the globe edge: dark silhouettes with bright rim light against the orange band; use for the cloud edge and limb silhouette.
- **REF-EARTH-022** `references/earth/earth_limb_night_airglow_cloud_deck_city_lights_iss_nasa_iss040e062704.jpg` [oblique limb view at night from the ISS with robot arm and solar array in the frame]: Shows the nightside look for B37-style shots: clouds are blue-white from moonlight, the rim is a thin blue edge capped by an olive-green airglow band, city lights are tiny orange dots (not a continuous glow); includes ISS hardware that must be left out.
- **REF-EARTH-026** `references/earth/earth_cloud_layer_oblique_cumulonimbus_shadows_limb_shuttle_nasa_sts064-83-099.jpg` [oblique daytime view toward the limb at high altitude, square 70 mm frame]: Cloud-layer reference with height cues: cloud tops are bright white, shadows are dark blue; clouds shrink to thin textured bands near the limb; use for the separate cloud layer (EARTH_002) with soft alpha and cast shadows only when the camera is oblique.
- **REF-EARTH-028** `references/earth/earth_south_polar_projection_composite_nasa_pia00729.jpg` [south-polar-up globe disc with no night side (composite)]: Low-resolution (452x439) but the only globe-with-the-pole-in-view example: shows polar cloud spirals around Antarctica; use as a layout reference, not as a texture.
- (family context) **REF-DIAG-001** `references/earth/diagrams_time_of_flight_range_diagram_wikimedia_20200501-time-of-flight.svg` [2-D schematic, emitter at left, target at right]
- (family context) **REF-DIAG-002** `references/earth/diagrams_moon_distance_range_to_scale_wikimedia_moon-distance-range-to-scale.svg` [strip diagram, Earth at left, scale in km, rendered to a 1600 px PNG by me]
- (family context) **REF-DIAG-003** `references/earth/diagrams_perigee_apogee_size_comparison_wikimedia_lunar-perigee-apogee.png` [two full-Moon photographs side by side at the same scale]
- (family context) **REF-DIAG-004** `references/earth/diagrams_moon_orbit_distance_variation_wikimedia_moons-orbit-variation-of-distance.png` [line chart, white background, grey gridlines]
- (family context) **REF-DIAG-005** `references/earth/diagrams_moon_distance_phase_animation_wikimedia_moon-earth-distance-moon-phases.gif` [chart on white, then black padding]
- (family context) **REF-DIAG-006** `references/earth/diagrams_light_crossing_earth_moon_animation_wikimedia_odonoghue-speed-of-light.gif` [animated strip, Earth left, Moon right, black ground]
- (family context) **REF-DIAG-007** `references/earth/diagrams_orbit_schematic_nasa_wikimedia_orbits-schematic-edit.png` [2-D schematic, Earth at left, 720x240]
- (family context) **REF-DIAG-008** `references/earth/diagrams_earth_moon_scale_strip_wikimedia_earth-moon-to-scale.svg` [strip diagram, Earth at the left; Moon off-screen in my renders]

Web pointers (verify independently): https://svs.gsfc.nasa.gov/5570

## 3. Intended camera angles
globe; limb

## 4. Required geometry and proportions
4096x2048 equirectangular; same wrap-safe seam rule; ~55-65% of pixels fully transparent; cloud alpha 0.35-0.95 with soft edges; polar regions thinner.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Ocean #0A1A3E (night) to #2C6CC4 (lit); land muted greens/ochres, never saturated; clouds #F0F4FA at 85% value; atmosphere rim #60C8FF at low opacity, thin.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA. Cloud colour #F0F4FA (bright side) - shading is added in code from the sun direction, so paint clouds flat-lit with only internal density variation.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `earth_clouds_4096x2048` | cloud density as alpha | `EARTH_000_SYSTEM` | same spin axis as surface | 20 |

Parent group: `EARTH_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: EARTH_001_SURFACE.

## 9. Hidden overlap requirements
Wrap-safe seam (as the surface).
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `EARTH_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x2048 equirectangular**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): same spin axis as EARTH_001. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
drifts independently of the surface
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P01**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5 (light), B6 (reference), B8 (no baked graphics), plus P01 (rotation, seam) when used on a globe.
A-tests pass numerically: RGBA; canvas exactly 4096x2048 equirectangular; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Not weather; must not create a recognisable single storm that would date the picture.

Must not change: Sun from the left about 30 degrees up (lit side left, night side right); cloud layer separate from surface; no light, shadow or atmosphere baked into the surface texture; same texture registration (wrap seam at the antimeridian, clean poles).

Known failure modes: baked clouds or lighting in the surface map; seam or pole pinching; oversaturated land; atmosphere drawn as a thick halo; clouds with hard cut-out edges.

## 16. Expected deliverable filenames
`earth_clouds_4096x2048.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
