# Brief: OBS_004_MOUNTAINS

Priority P0 | kind illustration | batch Batch 4 | status PLANNED | first appears 0.00s in beats B01 B02 B03 B22 | construction method: **2.5D rigid layers (parallax factors far 0.15, mid 0.35, near 0.6)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Three parallax ridge layers of a dry mountain-top site seen from the observatory at night.

Manifest description: Three parallax ridge layers (far, mid, near) of a dry mountain-top site; distant landscape merges into the far layer.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-OBS-023** `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg` [telephoto ground view of a hilltop with four closed enclosures in front of the setting Moon]: Composition reference for the Moon-over-observatory ground shot: the Moon is placed directly behind the buildings, orange near the horizon; buildings are small white boxes. Moon colour should be neutral when high.
- **REF-OBS-005** `references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg` [very wide, ground level, mountain-top setting at dusk]: OBS_004_MOUNTAINS: three ridge layers with haze increasing to the far layer. At true scale the real enclosure is only about 5 percent of frame width here; the storyboard's dome lower-centre framing is a deliberate enlargement, so keep the ridge haze and layering but not the scale. Clouds can be the only sky texture at dusk; at night use the star field only.
- **REF-OBS-006** `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg` [high oblique day view, three-quarter from above]: Roof, drum and base are separate rotation levels: if a rotating shell is ever drawn, the roof+drum rotate relative to the base ring. Boulders and a squat annex are good OBS_007_PROPS (rocks, utility shed).
- **REF-OBS-008** `references/observatory/observatory_la-silla-ntt-36m_twilight-exterior_eso_img5380.jpg` [telephoto ground view of a barren summit at dusk]: Compare silhouettes: dome-on-cylinder reads at a glance from far away, the box does not. Supports choosing the hemispherical dome-on-drum for a 9:16 wide shot.
- (family context) **REF-OBS-021** `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg` [daytime 3/4-front exterior at ground level, enclosure shutter leaves slid apart, three people for scale]
- (family context) **REF-OBS-022** `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg` [low-angle FRONT view at night looking up through an open slit; star field between the leaves]
- (family context) **REF-OBS-002** `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg` [ground level, wide, low three-quarter on a small dome-on-box observatory at twilight]
- (family context) **REF-OBS-004** `references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg` [ground level, portrait, night, three-quarter on the corner of the tall enclosure]
- (family context) **REF-OBS-007** `references/observatory/observatory_ntt-box-enclosure_slit-open-twilight-exterior_eso_eso9704a.jpg` [ground level, three-quarter, twilight, portrait]
- (family context) **REF-OBS-009** `references/observatory/observatory_vlt-ut1-enclosure_open-doors-day_eso_ut1-at1-open-2007.jpg` [front-on, ground level, golden light]
- (family context) **REF-OBS-010** `references/observatory/observatory_vlt-ut-enclosure_slit-opening-tilted_eso_img7670-cc.jpg` [inside the enclosure, looking up and across from the floor]
- (family context) **REF-OBS-011** `references/observatory/observatory_vlt-ut-enclosure_interior-fisheye_eso_vlt1-brunier.jpg` [high interior fisheye, full circle with black corners]

Web pointers (verify independently): https://apo.nmsu.edu/ (site overview)

## 3. Intended camera angles
ground wide

## 4. Required geometry and proportions
Each 4320x1400 (2x width): far ridge value #1B2744 (lightest, near the horizon sky glow), mid #12203C, near #0B1530 (darkest); silhouette edges slightly different in each layer; no snow.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Night palette: sky #070B1A to #16223F, building/ridges #0B1530-#2A3558, instrument white/grey #E6E9F0 / #AEB4C2 / #6A7080; lit windows warm-dim #C9A877 at ~30% value; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA, three separate files.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `obs_ridge_far` | far ridge | `OBS_004_MOUNTAINS` | none | 15 |
| `obs_ridge_mid` | mid ridge | `OBS_004_MOUNTAINS` | none | 17 |
| `obs_ridge_near` | near ridge | `OBS_004_MOUNTAINS` | none | 19 |

Parent group: `OBS_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Each ridge extends 8% of canvas height below its visible base.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `OBS_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4320x1400 per layer (x3)**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): none. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
tiny parallax with camera push
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P03**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 4320x1400 per layer (x3); alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Generic dry-mountain silhouette; no real range.

Must not change: Generic illustrated station, never a named real site; no signage or logos; the dome receives no sunlight; one consistent dome radius and slit width across all OBS and TEL assets; night palette.

Known failure modes: fused dome and slit (cannot open); telescope floating; real-site signage; mountains as one flat layer; a sunlit dome at night.

## 16. Expected deliverable filenames
`obs_ridge_{far,mid,near}_4320x1400.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
