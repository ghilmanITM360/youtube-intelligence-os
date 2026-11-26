# Brief: EARTH_006_ATMOS_SLICE

Priority P1 | kind illustration | batch Batch 1 | status PLANNED | first appears 65.52s in beats B29 | construction method: **rigid layers; band wobble driven in code (OPT_005)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Educational side cross-section of air above a ground limb (thin layered air with one turbulent band). Magnified in thickness and labelled magnified by Claude (not in the art).

Manifest description: Side cross-section of the air over a ground limb, in layers with one turbulent band, for the atmosphere beat. Thickness is exaggerated and labelled magnified.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-EARTH-010** `references/earth/earth_limb_glow_iss_nasa_iss074e0089803.jpg` [near-horizontal limb view from the ISS at about 271 miles altitude (caption)]: Atmosphere ring: saturated mid-blue at the horizon line, fading outward over a few pixels; the haze on the surface side is paler and warm. Thickness is a small fraction of the radius. Clouds seen edge-on appear as thin low layers. Sun-glint is golden.
- **REF-EARTH-019** `references/earth/earth_limb_edge_on_sunset_layers_iss_nasa_iss023e057948.jpg` [edge-on limb (horizon tangent) from low Earth orbit, tilted across the frame]: Defines the atmosphere limb slice (EARTH_003 limb ramp and EARTH_006 side cross-section): bands are soft-edged horizontal gradients; total visible thickness is a very thin fraction of the globe radius; no hard outline.
- **REF-EARTH-020** `references/earth/earth_limb_twilight_noctilucent_layer_iss_nasa_iss024e006136.jpg` [near-horizontal limb at orbital twilight, straight-on]: Shows the limb as a straight-on horizontal band structure: dark sky, a faint streaky electric-blue thin layer, a bright white/cyan band and a thin orange line at the horizon; no curved limb in this crop. Use for a dawn/dusk limb variant of EARTH_003 and the high thin layer.
- **REF-EARTH-021** `references/earth/earth_limb_edge_on_sunrise_cloud_silhouette_shuttle_nasa_sts047-54-018.jpg` [edge-on limb, tilted, with silhouetted cumulus in the foreground and a sun glint]: Shows clouds as a thin textured layer on the globe edge: dark silhouettes with bright rim light against the orange band; use for the cloud edge and limb silhouette.
- (family context) **REF-DIAG-001** `references/earth/diagrams_time_of_flight_range_diagram_wikimedia_20200501-time-of-flight.svg` [2-D schematic, emitter at left, target at right]
- (family context) **REF-DIAG-002** `references/earth/diagrams_moon_distance_range_to_scale_wikimedia_moon-distance-range-to-scale.svg` [strip diagram, Earth at left, scale in km, rendered to a 1600 px PNG by me]
- (family context) **REF-DIAG-003** `references/earth/diagrams_perigee_apogee_size_comparison_wikimedia_lunar-perigee-apogee.png` [two full-Moon photographs side by side at the same scale]
- (family context) **REF-DIAG-004** `references/earth/diagrams_moon_orbit_distance_variation_wikimedia_moons-orbit-variation-of-distance.png` [line chart, white background, grey gridlines]
- (family context) **REF-DIAG-005** `references/earth/diagrams_moon_distance_phase_animation_wikimedia_moon-earth-distance-moon-phases.gif` [chart on white, then black padding]
- (family context) **REF-DIAG-006** `references/earth/diagrams_light_crossing_earth_moon_animation_wikimedia_odonoghue-speed-of-light.gif` [animated strip, Earth left, Moon right, black ground]
- (family context) **REF-DIAG-007** `references/earth/diagrams_orbit_schematic_nasa_wikimedia_orbits-schematic-edit.png` [2-D schematic, Earth at left, 720x240]
- (family context) **REF-DIAG-008** `references/earth/diagrams_earth_moon_scale_strip_wikimedia_earth-moon-to-scale.svg` [strip diagram, Earth at the left; Moon off-screen in my renders]

Web pointers (verify independently): GAP (no source opened yet)

## 3. Intended camera angles
side view, beam passes through

## 4. Required geometry and proportions
2160x1200 landscape; ground at the bottom 12%, 5 horizontal air layers fading upward, one turbulent band at ~40% height with soft vertical eddies; no sun disc.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Ocean #0A1A3E (night) to #2C6CC4 (lit); land muted greens/ochres, never saturated; clouds #F0F4FA at 85% value; atmosphere rim #60C8FF at low opacity, thin.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA. Transparent above the last air layer; the beam never appears in the art.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `atmos_slice_ground` | ground strip | `EARTH_006_ATMOS_SLICE` | none | 4 |
| `atmos_slice_air_layers` | stacked translucent layers | `EARTH_006_ATMOS_SLICE` | none | 5 |
| `atmos_slice_turbulent_band` | separate turbulent band | `EARTH_006_ATMOS_SLICE` | band centre | 6 |

Parent group: `EARTH_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Band extends 4% of canvas width beyond both side edges of the air layers.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `EARTH_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2160x1200**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): none. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
turbulent band wobbles (code)
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **none (checked in the shot)**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2160x1200; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Qualitative only (C09): air bends and slightly delays light; thickness exaggerated; no refractive-index numbers.

Must not change: Sun from the left about 30 degrees up (lit side left, night side right); cloud layer separate from surface; no light, shadow or atmosphere baked into the surface texture; same texture registration (wrap seam at the antimeridian, clean poles).

Known failure modes: baked clouds or lighting in the surface map; seam or pole pinching; oversaturated land; atmosphere drawn as a thick halo; clouds with hard cut-out edges.

## 16. Expected deliverable filenames
`atmos_slice_{ground,air_layers,turbulent_band}_2160x1200.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
