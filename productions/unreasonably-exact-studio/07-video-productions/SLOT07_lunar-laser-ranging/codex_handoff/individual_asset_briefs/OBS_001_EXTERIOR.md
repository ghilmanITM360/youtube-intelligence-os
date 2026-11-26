# Brief: OBS_001_EXTERIOR

Priority P0 | kind illustration | batch Batch 4 | status PLANNED | first appears 0.00s in beats B01 B02 B03 B22 | construction method: **rigid layers**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
A generic observatory building body at night (no dome): concrete base, lit windows, vents, doors. Never a real named site, no signage.

Manifest description: Observatory building body (no dome), doors, vents, a few lit windows; cool dim night light.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-OBS-023** `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg` [telephoto ground view of a hilltop with four closed enclosures in front of the setting Moon]: Composition reference for the Moon-over-observatory ground shot: the Moon is placed directly behind the buildings, orange near the horizon; buildings are small white boxes. Moon colour should be neutral when high.
- **REF-OBS-002** `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg` [ground level, wide, low three-quarter on a small dome-on-box observatory at twilight]: Pattern for OBS_001/OBS_002: low cuboid base, rail ring where the dome meets it, exterior stair, lit doorway as the only warm light. Use the dome-on-base proportion (dome diameter about equal to the base width).
- **REF-OBS-004** `references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg` [ground level, portrait, night, three-quarter on the corner of the tall enclosure]: Key evidence for the unresolved 3.5 m enclosure form (see note). Decision: the film's generic observatory must not copy this building; use a hemispherical dome-on-drum so no viewer can read it as Apache Point.
- **REF-OBS-005** `references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg` [very wide, ground level, mountain-top setting at dusk]: OBS_004_MOUNTAINS: three ridge layers with haze increasing to the far layer. At true scale the real enclosure is only about 5 percent of frame width here; the storyboard's dome lower-centre framing is a deliberate enlargement, so keep the ridge haze and layering but not the scale. Clouds can be the only sky texture at dusk; at night use the star field only.
- **REF-OBS-013** `references/observatory/observatory_paranal-ut-laser-guide-star_beam-night_eso_ann15034h.jpg` [low ground level, night, three-quarter on the enclosure]: OBS_001/OBS_002 night grading: building is a dim cool grey with a warm accent only where the beam spills. Confirms the film's beam must be an explicit symbol; B02 dashed cone is a different, imagined thing.
- **REF-OPT-012** `references/retroreflector/optical_laser_beams_in_dark_sky_nasa-gsfc_gsfc_20171208_archive_e001973.jpg` [ground-level, portrait; wide-angle looking up at a bright Moon]: B01-B04: the ground-view beam should be a thin straight green line with soft edges that fades with height; do not extend it visually past the atmosphere. Colour conflict with 'outbound warm' flagged in notes.
- (family context) **REF-OBS-021** `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg` [daytime 3/4-front exterior at ground level, enclosure shutter leaves slid apart, three people for scale]
- (family context) **REF-OBS-022** `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg` [low-angle FRONT view at night looking up through an open slit; star field between the leaves]
- (family context) **REF-OBS-006** `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg` [high oblique day view, three-quarter from above]
- (family context) **REF-OBS-007** `references/observatory/observatory_ntt-box-enclosure_slit-open-twilight-exterior_eso_eso9704a.jpg` [ground level, three-quarter, twilight, portrait]
- (family context) **REF-OBS-008** `references/observatory/observatory_la-silla-ntt-36m_twilight-exterior_eso_img5380.jpg` [telephoto ground view of a barren summit at dusk]
- (family context) **REF-OBS-009** `references/observatory/observatory_vlt-ut1-enclosure_open-doors-day_eso_ut1-at1-open-2007.jpg` [front-on, ground level, golden light]
- (family context) **REF-OBS-010** `references/observatory/observatory_vlt-ut-enclosure_slit-opening-tilted_eso_img7670-cc.jpg` [inside the enclosure, looking up and across from the floor]
- (family context) **REF-OBS-011** `references/observatory/observatory_vlt-ut-enclosure_interior-fisheye_eso_vlt1-brunier.jpg` [high interior fisheye, full circle with black corners]

Web pointers (verify independently): https://apo.nmsu.edu/ (context); generic by decision

## 3. Intended camera angles
ground-level wide, vertical frame

## 4. Required geometry and proportions
2160x3840 portrait; building width 62% of canvas, height 16%; dome ring (circle seen as ellipse, 0.7 ratio) at the roof centre; 3 lit windows (warm-dim #C9A877 at 30% value); door at left.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Night palette: sky #070B1A to #16223F, building/ridges #0B1530-#2A3558, instrument white/grey #E6E9F0 / #AEB4C2 / #6A7080; lit windows warm-dim #C9A877 at ~30% value; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA. Cool night light #16223F-#2A3558; the building is lit only by starlight, a small work-light and the windows.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `obs_exterior_body` | building without dome | `OBS_000_SYSTEM` | dome ring centre | 30 |
| `obs_exterior_window_light` | window glow as separate layer | `OBS_000_SYSTEM` | none | 31 |

Parent group: `OBS_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Roof ring extends 4% of canvas width under where the dome shell sits.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `OBS_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2160x3840 px (2x of 1080x1920)**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): ring where the dome sits. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
static; window glow may flicker once (code opacity)
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P03**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2160x3840 px (2x of 1080x1920); alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Generic: do not copy Apache Point or any building; unnamed.

Must not change: Generic illustrated station, never a named real site; no signage or logos; the dome receives no sunlight; one consistent dome radius and slit width across all OBS and TEL assets; night palette.

Known failure modes: fused dome and slit (cannot open); telescope floating; real-site signage; mountains as one flat layer; a sunlit dome at night.

## 16. Expected deliverable filenames
`obs_exterior_{body,window_light}_2160x3840.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
