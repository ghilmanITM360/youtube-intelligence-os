# Brief: OBS_003_INTERIOR

Priority P0 | kind illustration | batch Batch 4 | status PLANNED | first appears 50.10s in beats B23 B24 | construction method: **rigid layers**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Dome interior seen as a cutaway: ribs, catwalk, shutter rails; separate foreground occlusion layer that passes in front of the telescope.

Manifest description: Dome interior: ribs, floor, catwalk, shutter rails; separate foreground occlusion layer (structure that passes in front of the telescope).

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-TEL-014** `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg` [wide interior 3/4 from the platform, telescope pointing steeply upward toward the open slit]: Telescope-pointing-up reference for the B01 slit view: tube is a lattice of struts, altitude ring is a big pale-grey torus on a blue azimuth bearing, platforms ring the structure; slit lets sky light in from one side.
- **REF-OBS-010** `references/observatory/observatory_vlt-ut-enclosure_slit-opening-tilted_eso_img7670-cc.jpg` [inside the enclosure, looking up and across from the floor]: B01: telescope should sit tilted (not flat) while the slit opens; then tilt up on 'ask' (B03). Structure in the foreground gives the occlusion layer for OBS_003_INTERIOR.
- **REF-OBS-011** `references/observatory/observatory_vlt-ut-enclosure_interior-fisheye_eso_vlt1-brunier.jpg` [high interior fisheye, full circle with black corners]: OBS_003_INTERIOR: floor ring + railed platform + overhead trusses; the control room is NOT here (it is a separate room), confirming the film can omit workstations. One tiny human figure gives scale; the film should leave the interior unpeopled.
- **REF-OBS-014** `references/observatory/observatory_paranal-ut-laser-guide-star_beam-night-vertical_eso_ann15034b.jpg` [from inside the enclosure, looking up through the slit, portrait]: B22/B24 option: a view from inside the slit with dark structural silhouettes framing a sky strip is a strong occlusion-mask composition (OBS_003_INTERIOR foreground layer).
- **REF-OBS-015** `references/observatory/observatory_mayall-4m-dome_interior-floor-and-slit_noirlab_mayallinterior-5000.jpg` [wide-angle interior from the floor, looking up]: OBS_003_INTERIOR background layer: ribbed hemisphere with a central slit; pier platform with a railed stair. Foreground occlusion: stair railings and platform edge in front of the telescope base.
- **REF-OBS-016** `references/observatory/observatory_mayall-4m-dome_slit-view-from-inside-sunset-silhouette_noirlab_noirlab-05025.jpg` [inside the dome, portrait, tube pointing to the slit]: B03/B24 silhouette test: the telescope reads mainly as a ring + thin diagonal struts + a dark secondary hub; the mount disappears in darkness. Occlusion: the slit edge crosses in front of the tube top.
- **REF-TEL-007** `references/telescope/telescope_vlt-ut-82m_secondary-mirror-unit-lifted-on-floor_eso_eso9812a.jpg` [ground level on the enclosure floor, portrait]: TEL_001/TEL_003: secondary mirror housing is a short cylinder hung on the spider; floor in OBS_003 has painted rings and tracks.
- (family context) **REF-OBS-021** `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg` [daytime 3/4-front exterior at ground level, enclosure shutter leaves slid apart, three people for scale]
- (family context) **REF-OBS-022** `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg` [low-angle FRONT view at night looking up through an open slit; star field between the leaves]
- (family context) **REF-OBS-023** `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg` [telephoto ground view of a hilltop with four closed enclosures in front of the setting Moon]
- (family context) **REF-OBS-002** `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg` [ground level, wide, low three-quarter on a small dome-on-box observatory at twilight]
- (family context) **REF-OBS-004** `references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg` [ground level, portrait, night, three-quarter on the corner of the tall enclosure]
- (family context) **REF-OBS-005** `references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg` [very wide, ground level, mountain-top setting at dusk]
- (family context) **REF-OBS-006** `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg` [high oblique day view, three-quarter from above]
- (family context) **REF-OBS-007** `references/observatory/observatory_ntt-box-enclosure_slit-open-twilight-exterior_eso_eso9704a.jpg` [ground level, three-quarter, twilight, portrait]

Web pointers (verify independently): 

## 3. Intended camera angles
cutaway interior, 3/4 view

## 4. Required geometry and proportions
2160x3840; interior ribs converge to the slit; floor ellipse; catwalk as horizontal band at 62% height; occlusion layer = 3 ribs + a rail running in front of the telescope tube.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Night palette: sky #070B1A to #16223F, building/ridges #0B1530-#2A3558, instrument white/grey #E6E9F0 / #AEB4C2 / #6A7080; lit windows warm-dim #C9A877 at ~30% value; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA two files: back (opaque interior) and front occlusion (partial).

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `obs_interior_back` | ribs, floor, catwalk | `OBS_000_SYSTEM` | none | 10 |
| `obs_interior_occluder` | ribs/rail in front of telescope | `OBS_000_SYSTEM` | none | 90 |

Parent group: `OBS_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Occluder extends 2% of canvas width onto the back plate at every join.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `OBS_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2160x3840 px (2x of 1080x1920)**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): none. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
static
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P04**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2160x3840 px (2x of 1080x1920); alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Illustrative interior; no real instrument layout.

Must not change: Generic illustrated station, never a named real site; no signage or logos; the dome receives no sunlight; one consistent dome radius and slit width across all OBS and TEL assets; night palette.

Known failure modes: fused dome and slit (cannot open); telescope floating; real-site signage; mountains as one flat layer; a sunlit dome at night.

## 16. Expected deliverable filenames
`obs_interior_{back,occluder}_2160x3840.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
