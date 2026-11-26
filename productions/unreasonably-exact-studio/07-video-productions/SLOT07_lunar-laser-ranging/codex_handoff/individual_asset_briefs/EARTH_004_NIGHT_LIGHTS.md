# Brief: EARTH_004_NIGHT_LIGHTS

Priority P1 | kind texture | batch Batch 1 | status PLANNED | first appears 86.31s in beats B37 | construction method: **procedural sphere mapping; masked by the terminator in code**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
City-light emissive layer for the night side (points of light, denser in coastal and populated regions). Qualitative; not a data layer.

Manifest description: City-lights layer visible only on the night side (masked by the terminator). Used in the final pull-back.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-EARTH-004** `references/earth/earth_nightlights_globalmap_nasa_blackmarble2012_e001593.jpg` [night hemisphere, Americas/Atlantic/Europe, with the thin sunlit crescent on the left limb]: Night lights layer: warm orange-gold points on transparent black, clustered (eastern USA, Europe, India, east Asia, Brazil coast), masked by the terminator; terminator is a soft gradient (not a hard line) roughly 5-8 percent of the diameter wide. Keep the dark side navy rather than pure black for readability, a deliberate stylisation.
- **REF-EARTH-014** `references/earth/earth_layers_cloud_atmos_nightlight_svs_nasa_5570.jpg` [3D render, full lit globe viewed from slightly north of the equator, Asia/Australia, with a star field]: Look-development target for the globe: soft atmosphere rim (brighter near the sun, weak elsewhere), no hard terminator, night lights hugging the dark side, cloud highlights. Supports the 5-layer split as the industry approach.
- **REF-EARTH-015** `references/earth/earth_lighting_equinox_diagram_wikimedia_blueshade.png` [orthographic diagram: Eastern hemisphere with the Sun from the left, equinox]: Clear visual for day side vs night side with city lights. Fully consistent with the manifest's day/night layering. Caution: this is an equinox picture; at other times of year the axis leans toward or away from the Sun (23.44 deg).
- **REF-EARTH-022** `references/earth/earth_limb_night_airglow_cloud_deck_city_lights_iss_nasa_iss040e062704.jpg` [oblique limb view at night from the ISS with robot arm and solar array in the frame]: Shows the nightside look for B37-style shots: clouds are blue-white from moonlight, the rim is a thin blue edge capped by an olive-green airglow band, city lights are tiny orange dots (not a continuous glow); includes ISS hardware that must be left out.
- **REF-EARTH-023** `references/earth/earth_nightlights_nadir_urban_road_network_iss_nasa_iss035e017286.jpg` [near-nadir night view of a dense urban region from the ISS]: Texture reference for the night-lights layer close-up: light is mostly thin orange lines and patches with sharp black gaps, not blobs; cores are small and white; maintain the colour split orange vs white.
- **REF-EARTH-024** `references/earth/earth_nightlights_oblique_city_grid_haze_iss_nasa_iss040e091208.jpg` [oblique night view of a large grid city between dark mountains]: Shows the glow-above-city haze and the grid structure; useful to set a modest bloom radius for the night-lights layer.
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
wide space view (B37)

## 4. Required geometry and proportions
4096x2048 equirectangular on black alpha; points 1-3 px, warm white #FFD9A0 (not the reserved warm/cool pair as areas); no oceans lit; wrap-safe.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Ocean #0A1A3E (night) to #2C6CC4 (lit); land muted greens/ochres, never saturated; clouds #F0F4FA at 85% value; atmosphere rim #60C8FF at low opacity, thin.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA emissive points only. No glow halos baked (glow is added in code, only on the unlit side).

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `earth_night_lights_4096x2048` | emissive points | `EARTH_000_SYSTEM` | same spin axis | 15 |

Parent group: `EARTH_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: EARTH_001_SURFACE.

## 9. Hidden overlap requirements
Wrap-safe.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `EARTH_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x2048 equirectangular**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): same spin axis as EARTH_001. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
rotates with the surface
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P01**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5 (light), B6 (reference), B8 (no baked graphics), plus P01 (rotation, seam) when used on a globe.
A-tests pass numerically: RGBA; canvas exactly 4096x2048 equirectangular; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Decorative realism only; no light pollution claim.

Must not change: Sun from the left about 30 degrees up (lit side left, night side right); cloud layer separate from surface; no light, shadow or atmosphere baked into the surface texture; same texture registration (wrap seam at the antimeridian, clean poles).

Known failure modes: baked clouds or lighting in the surface map; seam or pole pinching; oversaturated land; atmosphere drawn as a thick halo; clouds with hard cut-out edges.

## 16. Expected deliverable filenames
`earth_night_lights_4096x2048.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
