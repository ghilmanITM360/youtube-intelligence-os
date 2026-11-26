# Brief: TEL_005_DETECTOR_BOX

Priority P1 | kind illustration | batch Batch 4 | status PLANNED | first appears 50.10s in beats B23 | construction method: **rigid sprite**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Generic plain instrument housing on the telescope that receives the return light.

Manifest description: Plain instrument housing on the telescope that receives the return; generic, no brand, no invented dials.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-TEL-003** `references/telescope/telescope_ntt-358m_nasmyth-rotator-and-instrument-box_eso_agil1766-cc.jpg` [close side view of the Nasmyth port with an instrument attached, portrait]: TEL_005_DETECTOR_BOX: generic grey box on a round flange with a short cable run; no brand or dials; round rotator ring is the mount interface.
- (family context) **REF-TEL-014** `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg` [wide interior 3/4 from the platform, telescope pointing steeply upward toward the open slit]
- (family context) **REF-TEL-001** `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg` [near front-on, low, looking up along the tube from the floor (aperture seen almost face-on)]
- (family context) **REF-TEL-002** `references/telescope/telescope_ntt-358m_threequarter-drawing-altaz-structure_eso_eso8602a.jpg` [three-quarter, slightly from above, whole telescope]
- (family context) **REF-TEL-004** `references/telescope/telescope_vlt-ut1-82m_altitude-bearing-threequarter_eso_eso9804c.jpg` [three-quarter from the floor beside the bearing, portrait]
- (family context) **REF-TEL-005** `references/telescope/telescope_vlt-ut2-82m_centrepiece-and-bearing-threequarter_eso_eso9902g.jpg` [three-quarter, low, portrait]
- (family context) **REF-TEL-006** `references/telescope/telescope_vlt-ut4-82m_mirror-cell-on-transporter-side_eso_max-313677s.jpg` [side view in daylight, outdoors]
- (family context) **REF-TEL-007** `references/telescope/telescope_vlt-ut-82m_secondary-mirror-unit-lifted-on-floor_eso_eso9812a.jpg` [ground level on the enclosure floor, portrait]
- (family context) **REF-TEL-008** `references/telescope/telescope_wiyn-3p5m_new-mirror-cell-carried_noirlab_01073-cc.jpg` [high oblique from above, whole cell]

Web pointers (verify independently): 

## 3. Intended camera angles
interior 3/4; cutaway

## 4. Required geometry and proportions
1500x1500; a plain rectangular box 1:1.3 with rounded corners, one round port, two mounting flanges; no dials, brand marks or text.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Instrument white #E6E9F0, grey #AEB4C2, dark grey #6A7080, black glass; cool night light; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA; neutral grey/white.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `tel_detector_box` | box | `TEL_001_HOUSING` | port centre | 60 |

Parent group: `TEL_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: TEL_001_HOUSING.

## 9. Hidden overlap requirements
Flanges extend 1.5% of canvas width into the telescope body.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `TEL_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **1500x1500**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): none. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
highlight ring by code
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P09**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 1500x1500; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Illustrative box; no internal detail claimed.

Must not change: One telescope design across exterior, aperture and cutaway; same proportions, same mount type; not any specific real telescope; no text or logos.

Known failure modes: invented hardware; mount that cannot rotate; aperture not a true circle; different design in cutaway vs exterior; text on the housing.

## 16. Expected deliverable filenames
`tel_detector_box_1500x1500.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
