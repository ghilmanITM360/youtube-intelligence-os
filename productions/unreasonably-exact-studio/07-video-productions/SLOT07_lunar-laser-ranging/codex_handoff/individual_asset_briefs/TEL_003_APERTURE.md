# Brief: TEL_003_APERTURE

Priority P0 | kind illustration | batch Batch 4 | status PLANNED | first appears 7.16s in beats B04 B24 | construction method: **rigid layers (push-in by camera)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Head-on simplified view of the open aperture: rim, secondary mirror with 4-vane spider, primary mirror visible around it. No photograph shows this exact view (centre box hides the primary), so it is built from the geometry.

Manifest description: Head-on view of the open aperture: rim, secondary-mirror spider, primary mirror visible; clean area for the laser flash. NOTE: no photograph shows this exact view (the only front views hide the primary behind the centre box): a simplified illustration from the geometry.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-OBS-022** `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg` [low-angle FRONT view at night looking up through an open slit; star field between the leaves]: Best view of the slit-open state with the telescope visible through it and the camera looking up: leaves lean outward like a V, ring of the telescope is cream-coloured, mirror not visible; use for B01/B04 composition of aperture and slit.
- **REF-TEL-001** `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg` [near front-on, low, looking up along the tube from the floor (aperture seen almost face-on)]: TEL_003_APERTURE: ring + X spider (4 vanes) + centred secondary housing; flash overlay goes at the primary's centre, not on the secondary. TEL_001 needs thin round truss legs.
- **REF-TEL-007** `references/telescope/telescope_vlt-ut-82m_secondary-mirror-unit-lifted-on-floor_eso_eso9812a.jpg` [ground level on the enclosure floor, portrait]: TEL_001/TEL_003: secondary mirror housing is a short cylinder hung on the spider; floor in OBS_003 has painted rings and tracks.
- (family context) **REF-TEL-014** `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg` [wide interior 3/4 from the platform, telescope pointing steeply upward toward the open slit]
- (family context) **REF-TEL-002** `references/telescope/telescope_ntt-358m_threequarter-drawing-altaz-structure_eso_eso8602a.jpg` [three-quarter, slightly from above, whole telescope]
- (family context) **REF-TEL-003** `references/telescope/telescope_ntt-358m_nasmyth-rotator-and-instrument-box_eso_agil1766-cc.jpg` [close side view of the Nasmyth port with an instrument attached, portrait]
- (family context) **REF-TEL-004** `references/telescope/telescope_vlt-ut1-82m_altitude-bearing-threequarter_eso_eso9804c.jpg` [three-quarter from the floor beside the bearing, portrait]
- (family context) **REF-TEL-005** `references/telescope/telescope_vlt-ut2-82m_centrepiece-and-bearing-threequarter_eso_eso9902g.jpg` [three-quarter, low, portrait]
- (family context) **REF-TEL-006** `references/telescope/telescope_vlt-ut4-82m_mirror-cell-on-transporter-side_eso_max-313677s.jpg` [side view in daylight, outdoors]
- (family context) **REF-TEL-008** `references/telescope/telescope_wiyn-3p5m_new-mirror-cell-carried_noirlab_01073-cc.jpg` [high oblique from above, whole cell]
- (family context) **REF-TEL-009** `references/telescope/telescope_wiyn-3p5m_primary-mirror-lowered-onto-cell_noirlab_01074-cc.jpg` [eye level, close, side-on to the mirror edge]

Web pointers (verify independently): https://tmurphy.physics.ucsd.edu/apollo/onscope.html

## 3. Intended camera angles
front-on (B04), slow push-in (B24)

## 4. Required geometry and proportions
2160x2160; outer rim circle Ø 92% of canvas; secondary mirror Ø 31% of aperture with 4 spider vanes at 45/135/225/315 degrees; primary mirror dark glass with a faint ring of mounting pads; perfect circles.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Instrument white #E6E9F0, grey #AEB4C2, dark grey #6A7080, black glass; cool night light; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA, black sky visible through the aperture is NOT painted (transparent where the sky shows); no flash drawn (code adds the pulse).

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `tel_aperture_rim` | rim + housing front face | `TEL_000_SYSTEM` | aperture centre | 50 |
| `tel_aperture_secondary` | secondary + spider | `tel_aperture_rim` | aperture centre | 51 |
| `tel_aperture_primary` | primary mirror face | `tel_aperture_rim` | aperture centre | 49 |

Parent group: `TEL_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Spider vanes extend 1% of canvas width into the rim; primary extends 1% under the rim.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `TEL_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **2160x2160**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): aperture centre. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
slow push-in on B24; background dims in code
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P03**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 2160x2160; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Simplified: the real optical path is folded (third mirror) - label as simplified in the shot.

Must not change: One telescope design across exterior, aperture and cutaway; same proportions, same mount type; not any specific real telescope; no text or logos.

Known failure modes: invented hardware; mount that cannot rotate; aperture not a true circle; different design in cutaway vs exterior; text on the housing.

## 16. Expected deliverable filenames
`tel_aperture_{rim,secondary,primary}_2160x2160.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
