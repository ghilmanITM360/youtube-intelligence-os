# Brief: OBS_007_PROPS

Priority P1 | kind illustration | batch Batch 4 | status PLANNED | first appears 0.00s in beats B01 B02 B03 B22 | construction method: **sprite replacement (static)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Foreground ground props around an observatory: rocks, antenna mast, fence posts, utility box.

Manifest description: Foreground props: rocks, antenna mast, fence posts, utility box; sprite sheet.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-OBS-006** `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg` [high oblique day view, three-quarter from above]: Roof, drum and base are separate rotation levels: if a rotating shell is ever drawn, the roof+drum rotate relative to the base ring. Boulders and a squat annex are good OBS_007_PROPS (rocks, utility shed).
- (family context) **REF-OBS-021** `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg` [daytime 3/4-front exterior at ground level, enclosure shutter leaves slid apart, three people for scale]
- (family context) **REF-OBS-022** `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg` [low-angle FRONT view at night looking up through an open slit; star field between the leaves]
- (family context) **REF-OBS-023** `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg` [telephoto ground view of a hilltop with four closed enclosures in front of the setting Moon]
- (family context) **REF-OBS-002** `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg` [ground level, wide, low three-quarter on a small dome-on-box observatory at twilight]
- (family context) **REF-OBS-004** `references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg` [ground level, portrait, night, three-quarter on the corner of the tall enclosure]
- (family context) **REF-OBS-005** `references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg` [very wide, ground level, mountain-top setting at dusk]
- (family context) **REF-OBS-007** `references/observatory/observatory_ntt-box-enclosure_slit-open-twilight-exterior_eso_eso9704a.jpg` [ground level, three-quarter, twilight, portrait]
- (family context) **REF-OBS-008** `references/observatory/observatory_la-silla-ntt-36m_twilight-exterior_eso_img5380.jpg` [telephoto ground view of a barren summit at dusk]

Web pointers (verify independently): 

## 3. Intended camera angles
ground wide foreground

## 4. Required geometry and proportions
4096x4096 sheet, sprites <= 1024 px: 5 rocks, 1 lattice mast (tall, 1:8), 4 fence posts, 1 grey utility box, 2 shrubs (dry); base-centre registered; gutter 32 px.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Night palette: sky #070B1A to #16223F, building/ridges #0B1530-#2A3558, instrument white/grey #E6E9F0 / #AEB4C2 / #6A7080; lit windows warm-dim #C9A877 at ~30% value; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA, shadows not baked.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `obs_props_sheet` | sprite sheet | `OBS_007_PROPS` | base-centre per sprite (PIVOTS.json) | 50 |

Parent group: `OBS_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
n/a
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `OBS_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **4096x4096 sheet**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): base-centre. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
static (mast light blink by code optional)
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **none**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 4096x4096 sheet; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
No signs, text or logos; no real-site hardware.

Must not change: Generic illustrated station, never a named real site; no signage or logos; the dome receives no sunlight; one consistent dome radius and slit width across all OBS and TEL assets; night palette.

Known failure modes: fused dome and slit (cannot open); telescope floating; real-site signage; mountains as one flat layer; a sunlit dome at night.

## 16. Expected deliverable filenames
`obs_props_sheet_4096x4096.png + PIVOTS.json`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
