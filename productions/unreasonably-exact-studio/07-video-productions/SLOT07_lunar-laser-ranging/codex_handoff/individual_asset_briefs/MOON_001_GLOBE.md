# Brief: MOON_001_GLOBE

Priority P0 | kind texture | batch Batches 1 and 3 | status PLANNED | first appears 0.00s in beats B01 B02 B03 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14 B15 B25 B31 B32 B33 B34 B35 B36 B37 B39 | construction method: **BASE = public-domain LRO/SVS Moon map (licence verified by Claude); Codex repaints/cleans only if needed at native size; Claude upscales (labelled resampled); sphere mapping in code**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Full-disc Moon near-side-first texture map (equirectangular) showing maria and highlands; the Mare Tranquillitatis region (Apollo 11 site) must be locatable.

Manifest description: Near-side-first Moon map: maria (incl. Tranquillitatis), highlands, major craters. The Apollo 11 site region must be locatable on it.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-EARTH-003** `references/earth/earth_moon_transit_dscovr_epic_nasa_e000670.png` [full disc seen from the Sun-Earth L1 point (about a million miles per caption); Moon lies between camera and Earth]: Shows that Earth is much brighter than the Moon (Earth geometric albedo 0.434 vs Moon 0.12 in the NASA fact sheets): when both appear in one frame keep the Earth visibly brighter and bluer. Warns that any perspective frame with the Moon nearer to the camera must not use the 0.2727 ratio.
- **REF-EARTH-008** `references/earth/earth_crescent_withmoon_nasa_art002e014211.jpg` [Moon (left) and Earth crescent (far right) in one wide frame, from the approach to the Moon's far side]: Supports drawing Earth and Moon far apart with a big black gap. Phases are complementary: a crescent Earth is seen when the Moon is near full as seen from Earth. A single light source fixes both phases.
- **REF-EARTH-011** `references/earth/earth_moon_scale_galileo_nasa_pia00342.jpg` [Earth limb (left) and Moon (lower right) in one composite frame; separate images combined]: Use only for colour relationship (Earth strongly blue and white, Moon grey-brown); the image's relative size and spacing are NOT physical.
- **REF-MOON-018** `references/moon/moon_limb_large_clean_edge_earth_behind_artemis2_nasa_art002e009287.jpg` [large Moon limb with a razor-sharp edge against black, half-lit; tiny Earth crescent behind the limb]: Settles the Moon limb treatment for MOON_001/004: clean antialiased edge, NO rim glow, terminator follows terrain (jagged), shadowed side almost black; Earth is only a few percent of the Moon diameter here.
- **REF-MOON-019** `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg` [very low oblique view of the lunar horizon, Earth crescent dipping behind the limb]: Reference for MOON_003 horizon (black sky, sharp line, no haze) and for placing Earth on the horizon in a wide view.
- **REF-MOON-020** `references/moon/moon_through_atmosphere_flattened_refraction_airglow_iss_nasa_iss039e001440.jpg` [telephoto view of the Moon at the moment of setting behind the limb, from the ISS]: Useful ONLY for the lunar-sky-through-air idea (B01): the Moon shape flattens near the horizon; the film Moon should be round when high in the sky.
- **REF-MOON-001** `references/moon/moon_nearside_fullmoon_lro_svs_nasa_e001861.jpg` [near-side full disc, north up, full phase; computer visualization from LRO data, not a photograph]: Texture target for MOON_001: two-tone maria/highlands, strong ray systems, craters get denser toward the south. For the big full-disc beats, keep the shading subtle at full phase (flat), and use a strong terminator for any phase other than full.
- **REF-MOON-002** `references/moon/moon_phase_firstquarter_lro_svs_nasa_e001863.jpg` [near-side disc, first quarter: right half lit, terminator running diagonally from upper centre to lower left]: MOON_004 mask: hard-edged terminator, only a few pixels of softness (no atmosphere), slightly irregular because of relief; the terminator tilts as seen from Earth (here about 20-30 degrees from vertical). Unlit disc may carry a very faint dark-grey earthshine fill, not pure black, if the dark half should be seen.
- **REF-MOON-004** `references/moon/moon_terminator_artemis2_nasa_art002e014045.jpg` [oblique photo of the Moon's limb and terminator from the Orion window during the lunar flyby]: Terminator rendered in code should show the 'islands of lit rims' pattern if the texture has height data; with a plain colour texture, keep the terminator crisp, with a faint warm tint.
- **REF-MOON-005** `references/moon/moon_terminator_craters_artemis2_nasa_art002e014055.jpg` [oblique close-up of cratered terrain at the terminator; the limb curves across the top]: Crater look for the globe: circular, overlapping, with floors in shadow under side light; helps match texture appearance for the highland areas.
- (family context) **REF-MOON-021** `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg` [ground-level wide view over sunlit dust to a shadowed slope and a far ridge, rover at left]
- (family context) **REF-MOON-003** `references/moon/moon_phase_waxingcrescent_lro_svs_nasa_e001864.jpg` [near-side disc, waxing crescent; only a right-hand crescent lit]
- (family context) **REF-MOON-007** `references/moon/moon_copernicus_crater_lroc_nasa_pia13524.jpg` [close-up (metres per pixel scale) of the rugged interior of Copernicus, high-resolution LROC NAC style]
- (family context) **REF-MOON-010** `references/moon/moon_regolith_bootprint_apollo11_nasa_as11-40-5878.jpg` [close-up oblique macro of the soil (70 mm lunar surface camera per the caption)]
- (family context) **REF-MOON-011** `references/moon/moon_surface_longshadow_apollo12_nasa_as12-46-6813.jpg` [ground-level wide view across the site; low horizon about 40 percent down from the top, lunar module in the left background]

Web pointers (verify independently): GAP: LROC/SVS global Moon map not opened yet; https://lroc.im-ldi.com/images/22 for the site

## 3. Intended camera angles
globe (ground sky, schematic, top-down orbit view, closing pull-back)

## 4. Required geometry and proportions
4096x2048. Near side centred at u=0.5 (lon 0), Mare Imbrium upper-left, Mare Serenitatis/Tranquillitatis centre-right, Oceanus Procellarum left, Tycho (south) bright rayed crater. Maria #55555D-#6A6A72, highlands #8A8A90-#ACACB0.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Highlights #ACACB0, mid #7E7E84, shadow #3A3A42; maria #55555D to #6A6A72 (cooler, darker); sky black #000000-#05070D.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
Opaque, no baked phase or terminator, no baked limb darkening (code adds both). No labels.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `moon_globe_4096x2048` | surface albedo map | `MOON_000_SYSTEM` | globe centre; no spin in the film | 10 |

Parent group: `MOON_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Wrap-safe seam (far-side edge columns continue).
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `MOON_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x2048 equirectangular**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): globe centre; no spin in film. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
none (fixed near side)
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P02**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5 (light), B6 (reference), B8 (no baked graphics), plus P01 (rotation, seam) when used on a globe.
A-tests pass numerically: RGBA; canvas exactly 4096x2048 equirectangular; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Apollo 11 site position is approximate on the map (C05); libration not modelled; far side is a plausible fill and is never shown.

Must not change: Near side only; same maria/highlands layout in every Moon asset; sun from the left; black sky, hard shadows, sharp horizon, no atmosphere haze; no flag or hardware unless the brief names it.

Known failure modes: Earth-like colours; craters repeating visibly; atmosphere haze; shadows pointing the wrong way; horizon too close or too curved for the camera height.

## 16. Expected deliverable filenames
`moon_globe_4096x2048.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
