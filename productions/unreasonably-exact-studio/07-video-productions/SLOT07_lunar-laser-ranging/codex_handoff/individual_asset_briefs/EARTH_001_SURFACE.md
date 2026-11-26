# Brief: EARTH_001_SURFACE

Priority P0 | kind texture | batch Batch 1 | status PLANNED | first appears 8.04s in beats B05 B06 B07 B08 B09 B10 B11 B12 B13 B25 B29 B31 B32 B33 B34 B35 B36 B37 B38 B39 | construction method: **BASE = public-domain NASA map (SVS / Blue Marble class, licence verified by Claude); Codex repaints only what is wrong (poles, filler band) at native size; Claude assembles/upscales to 4096x2048 (labelled resampled); sphere mapping in code**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Cloud-free Earth surface map (equirectangular). Not a photograph of a particular day; not a political map.

Manifest description: Cloud-free Earth surface map: ocean, continents, polar ice. No light, shadow, atmosphere or clouds baked in. The only public cloud-free map (SVS 3615, 2048x1024) has a grey filler band at the north: the poles must be repainted clean.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-EARTH-001** `references/earth/earth_fullglobe_translunar_nasa_as17-148-22727.jpg` [full sunlit disc, south at bottom, translunar coast (tens of thousands of km)]: Colour target for the Earth globe: ocean deep blue (not cyan), land ochre/brown/green, clouds pure white with soft alpha, limb rim thin and pale blue. Clouds cover roughly half the disc, so cloud alpha should be dense, not sprinkled.
- **REF-EARTH-002** `references/earth/earth_fullglobe_composite_nasa_bluemarble2012_e001788.jpg` [full disc, Africa/Middle East/India, composite from low Earth orbit data rendered as if from far away]: Atmosphere ring in code: thin, dim, cool-blue halo outside the limb, fading to black within about 1-2 percent of the radius. Do NOT copy the vertical swath streaks (artefacts).
- **REF-EARTH-003** `references/earth/earth_moon_transit_dscovr_epic_nasa_e000670.png` [full disc seen from the Sun-Earth L1 point (about a million miles per caption); Moon lies between camera and Earth]: Shows that Earth is much brighter than the Moon (Earth geometric albedo 0.434 vs Moon 0.12 in the NASA fact sheets): when both appear in one frame keep the Earth visibly brighter and bluer. Warns that any perspective frame with the Moon nearer to the camera must not use the 0.2727 ratio.
- **REF-EARTH-007** `references/earth/earth_crescent_deepspace_nasa_art002e014225.jpg` [Earth as a tiny crescent far from Earth, near the lunar flyby]: A true-scale far view would make Earth a tiny dot-crescent in black space. This supports the manifest's schematic choice (not to scale spacing). No stars in the exposure is realistic for a bright subject; the film's star field is stylisation.
- **REF-EARTH-012** `references/earth/earth_surface_nocloud_equirect_svs_nasa_3615.jpg` [equirectangular 2:1 map (not a camera view)]: Possible EARTH_001 reference/source at 2048x1024; the 4096x2048 cloud-free file was NOT found on this page (see gaps). The flat grey-lavender band at the top is a defect for a top-down or north-pole-up view, so the pole must be repainted (manifest 'pole regions must be clean').
- **REF-EARTH-014** `references/earth/earth_layers_cloud_atmos_nightlight_svs_nasa_5570.jpg` [3D render, full lit globe viewed from slightly north of the equator, Asia/Australia, with a star field]: Look-development target for the globe: soft atmosphere rim (brighter near the sun, weak elsewhere), no hard terminator, night lights hugging the dark side, cloud highlights. Supports the 5-layer split as the industry approach.
- **REF-EARTH-027** `references/earth/earth_arctic_polar_cap_topdown_mosaic_terra_nasa_gsfc_e001802.jpg` [straight-down polar mosaic of the Arctic (satellite swaths stitched), north pole at centre]: Reference for repainting the grey filler band at the pole of the cloud-free map: ice is blue-white with fine crack lines and slightly darker coast margins, not flat white; Greenland sits as a bright wedge.
- **REF-EARTH-028** `references/earth/earth_south_polar_projection_composite_nasa_pia00729.jpg` [south-polar-up globe disc with no night side (composite)]: Low-resolution (452x439) but the only globe-with-the-pole-in-view example: shows polar cloud spirals around Antarctica; use as a layout reference, not as a texture.
- (family context) **REF-DIAG-001** `references/earth/diagrams_time_of_flight_range_diagram_wikimedia_20200501-time-of-flight.svg` [2-D schematic, emitter at left, target at right]
- (family context) **REF-DIAG-002** `references/earth/diagrams_moon_distance_range_to_scale_wikimedia_moon-distance-range-to-scale.svg` [strip diagram, Earth at left, scale in km, rendered to a 1600 px PNG by me]
- (family context) **REF-DIAG-003** `references/earth/diagrams_perigee_apogee_size_comparison_wikimedia_lunar-perigee-apogee.png` [two full-Moon photographs side by side at the same scale]
- (family context) **REF-DIAG-004** `references/earth/diagrams_moon_orbit_distance_variation_wikimedia_moons-orbit-variation-of-distance.png` [line chart, white background, grey gridlines]
- (family context) **REF-DIAG-005** `references/earth/diagrams_moon_distance_phase_animation_wikimedia_moon-earth-distance-moon-phases.gif` [chart on white, then black padding]
- (family context) **REF-DIAG-006** `references/earth/diagrams_light_crossing_earth_moon_animation_wikimedia_odonoghue-speed-of-light.gif` [animated strip, Earth left, Moon right, black ground]
- (family context) **REF-DIAG-007** `references/earth/diagrams_orbit_schematic_nasa_wikimedia_orbits-schematic-edit.png` [2-D schematic, Earth at left, 720x240]
- (family context) **REF-DIAG-008** `references/earth/diagrams_earth_moon_scale_strip_wikimedia_earth-moon-to-scale.svg` [strip diagram, Earth at the left; Moon off-screen in my renders]

Web pointers (verify independently): https://svs.gsfc.nasa.gov/5570 (layer split); Blue Marble class texture (SNIPPET)

## 3. Intended camera angles
globe; limb at bottom of frame; top-down orbit view (north pole up, pole regions must be clean)

## 4. Required geometry and proportions
4096x2048, 2:1. Equator at row 1024, antimeridian at the left/right edge: left and right columns must tile (wrap-safe). North/south 8% bands are polar ice, painted clean (no grey filler band, no pinching artefact).

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Ocean #0A1A3E (night) to #2C6CC4 (lit); land muted greens/ochres, never saturated; clouds #F0F4FA at 85% value; atmosphere rim #60C8FF at low opacity, thin.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Opaque. Daylight-neutral colour: ocean #1C5AA8-#2C6CC4 shallow-to-deep, land muted greens/ochres, ice #E9EEF5. NO clouds, light, shadow, terminator, atmosphere, graticule or labels.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `earth_surface_4096x2048` | surface colour map (Claude assembles from the public-domain base map) | `EARTH_000_SYSTEM` | spin axis = vertical centre line of the globe; texture u=0 at antimeridian | 10 |
| `earth_pole_north_native` | BATCH 1 CODEX DELIVERABLE: clean top-down north polar cap disc (ice, ocean edge), square canvas, transparent outside the disc, no clouds/light/atmosphere | `EARTH_001_SURFACE` | pole at canvas centre | 11 |
| `earth_pole_south_native` | BATCH 1 CODEX DELIVERABLE: clean top-down south polar cap (Antarctica) disc, same rules | `EARTH_001_SURFACE` | pole at canvas centre | 11 |

Parent group: `EARTH_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Wrap-safe: the leftmost 64 px column must continue the rightmost 64 px column (state the measured seam difference in ARTWORK_QA.md).
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `EARTH_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x2048 equirectangular**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): spin axis = north-south, tilt 0 in schematic. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
rotated by the Earth rig (spin) under a fixed sun direction; no baked motion
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P01**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5 (light), B6 (reference), B8 (no baked graphics), plus P01 (rotation, seam) when used on a globe.
A-tests pass numerically: RGBA; canvas exactly 4096x2048 equirectangular; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
The Pacific/Atlantic arrangement shown to the camera is a design choice, not a claim about which side faces the Moon at transmit time (C03). No Earth-Moon distance is implied by the map.

Must not change: Sun from the left about 30 degrees up (lit side left, night side right); cloud layer separate from surface; no light, shadow or atmosphere baked into the surface texture; same texture registration (wrap seam at the antimeridian, clean poles).

Known failure modes: baked clouds or lighting in the surface map; seam or pole pinching; oversaturated land; atmosphere drawn as a thick halo; clouds with hard cut-out edges.

## 16. Expected deliverable filenames
`earth_surface_4096x2048.png (+ earth_surface_preview_1024.png)`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
