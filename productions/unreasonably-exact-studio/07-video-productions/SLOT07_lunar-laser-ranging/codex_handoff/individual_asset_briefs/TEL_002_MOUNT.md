# Brief: TEL_002_MOUNT

Priority P0 | kind illustration | batch Batch 4 | status PLANNED | first appears 0.00s in beats B01 B02 B03 B04 B22 B23 | construction method: **hierarchical rig (azimuth rotation small)**

Read first: `../START_HERE.md`, `../PRODUCTION_ART_DIRECTION.md`, `../ASSET_ACCEPTANCE_TESTS.md`, `../ASSEMBLY_DIAGRAMS.md`. Research this asset yourself before generating (section 2), save extra references to `references_codex/` with source and licence.

## 1. Real-world object identification
Azimuth base with two pylons (yoke) carrying altitude bearings (NTT/VLT-class alt-az mount). Not a classic fork.

Manifest description: Azimuth base and two pylons (yoke) carrying the altitude bearings, 3/4 view; hidden overlap where the tube sits between them. Not a classic fork: follow the NTT/VLT-class references.

## 2. Exact local reference paths (relative to `codex_handoff/`; every path below is checked to exist)
- **REF-TEL-014** `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg` [wide interior 3/4 from the platform, telescope pointing steeply upward toward the open slit]: Telescope-pointing-up reference for the B01 slit view: tube is a lattice of struts, altitude ring is a big pale-grey torus on a blue azimuth bearing, platforms ring the structure; slit lets sky light in from one side.
- **REF-TEL-002** `references/telescope/telescope_ntt-358m_threequarter-drawing-altaz-structure_eso_eso8602a.jpg` [three-quarter, slightly from above, whole telescope]: TEL_002_MOUNT: azimuth drum + two pylons with a round port; altitude axis near the pylon tops, slightly above the tube's centre of mass; the tube is much shorter than the pylon height.
- **REF-TEL-004** `references/telescope/telescope_vlt-ut1-82m_altitude-bearing-threequarter_eso_eso9804c.jpg` [three-quarter from the floor beside the bearing, portrait]: TEL_002_MOUNT: bearing is a big disc, not a small pin; centrepiece box carries the tube; cabinets on the box side are optional detail but would be 'invented dials' so keep them as plain rectangles.
- **REF-TEL-005** `references/telescope/telescope_vlt-ut2-82m_centrepiece-and-bearing-threequarter_eso_eso9902g.jpg` [three-quarter, low, portrait]: TEL_001_HOUSING: tube = ring + four legs + box; the box is the big visual mass, the ring is small relative to it. Separate layers: ring+legs (rotate with tilt) and box (tilts with it).
- (family context) **REF-TEL-001** `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg` [near front-on, low, looking up along the tube from the floor (aperture seen almost face-on)]
- (family context) **REF-TEL-003** `references/telescope/telescope_ntt-358m_nasmyth-rotator-and-instrument-box_eso_agil1766-cc.jpg` [close side view of the Nasmyth port with an instrument attached, portrait]
- (family context) **REF-TEL-006** `references/telescope/telescope_vlt-ut4-82m_mirror-cell-on-transporter-side_eso_max-313677s.jpg` [side view in daylight, outdoors]
- (family context) **REF-TEL-007** `references/telescope/telescope_vlt-ut-82m_secondary-mirror-unit-lifted-on-floor_eso_eso9812a.jpg` [ground level on the enclosure floor, portrait]
- (family context) **REF-TEL-008** `references/telescope/telescope_wiyn-3p5m_new-mirror-cell-carried_noirlab_01073-cc.jpg` [high oblique from above, whole cell]
- (family context) **REF-TEL-009** `references/telescope/telescope_wiyn-3p5m_primary-mirror-lowered-onto-cell_noirlab_01074-cc.jpg` [eye level, close, side-on to the mirror edge]
- (family context) **REF-TEL-010** `references/telescope/telescope_mayall-4m_tube-truss-ring-mirror-cell-lowthreequarter_noirlab_noirlab-02052.jpg` [low three-quarter looking up the tube, portrait]

Web pointers (verify independently): https://apo.nmsu.edu/ (alt-azimuth fork photo, telescope identity unconfirmed)

## 3. Intended camera angles
side; 3/4

## 4. Required geometry and proportions
Base disc width 78% of canvas; pylon spacing = 1.3x tube width; bearing circles Ø 9% of canvas width; pylon height 1.1x tube; 3000x3000 for side and 3/4.

## 5. Illustration style
Painterly-clean cinematic illustration, per `../PRODUCTION_ART_DIRECTION.md` and `../VISION_CARD.md`: soft value shapes, no outline strokes, no photographic noise, no text/numbers/arrows/rays/lens flare, matte-clean edges. One visual language across the whole film; do not mix styles between assets.

## 6. Palette and lighting
Instrument white #E6E9F0, grey #AEB4C2, dark grey #6A7080, black glass; cool night light; no sunlit surfaces.
Sun from the left, about 30 degrees above the horizon (shadows fall right and slightly down). Reserved warm #FFAC40 / cool #60C8FF belong to code-drawn light only.

## 7. Pose or object-state requirements
RGBA. Bearing sockets open toward the tube, neutral grey/white #AEB4C2/#E6E9F0.

## 8. Layered asset decomposition (deliver one PNG per row; same canvas and pixel positions as the master)
| Layer file stem | Contents | Parent | Pivot | Draw order |
|---|---|---|---|---|
| `tel_base` | azimuth base | `TEL_000_SYSTEM` | azimuth axis through base centre | 35 |
| `tel_pylon_near` | near pylon | `tel_base` | rigid; bearing centre listed | 36 |
| `tel_pylon_far` | far pylon (behind tube) | `tel_base` | rigid | 34 |

Parent group: `TEL_000_SYSTEM`. Child layers named in the manifest: none (single asset). Depends on: none.

## 9. Hidden overlap requirements
Pylons extend 2% of canvas width into the base; the far pylon extends 2% behind the tube footprint.
Never a generic round cap; state the unit used in `PIVOTS.json`.

## 10. Parent-child relationships
Parent group `TEL_000_SYSTEM`; in the layer table above the *Parent* column gives the transform parent (a child inherits its parent's rotation and translation). Rotate children only about their own listed pivot.

## 11. Pivot registration
Canvas: **3000x3000**. Pivots (pixel coordinates on that canvas, certified by you with a test image, never guessed): azimuth axis through base centre; altitude axis through bearings. Unknown pivot = `null` in `PIVOTS.json` (blocks integration). **Canvas sizes are targets for the final assembled asset. Your generator is native at about 1254 px (Batch 0 calibration): deliver at native size, state it, label any larger export `resampled`; Claude assembles and upscales.**

## 12. Intended motion
azimuth rotation <= 6 degrees; supports tilt
This art is only the starting pose; Claude drives the motion in code.

## 13. Required animation proof (Claude renders; extremes are the shot's real range)
Proof clips: **P04**. Definitions and pass conditions: `../ASSET_ACCEPTANCE_TESTS.md` section C. A still PNG is never accepted as animation-ready.

## 14. Objective acceptance tests
A1-A8, B5, B6, B7 (counts), B8; layered assets also B1-B3 (rest, seam, occlusion); astronaut also B4 (identity); reflector also B9 (registration).
A-tests pass numerically: RGBA; canvas exactly 3000x3000; alpha >= 245 where solid; **0** px of RGB under zero alpha; **no detached component > 400 px**; semi-transparent share <= 25%; hashes recorded. B-tests are judged on a contact sheet. Run `python3 tools/validate_asset.py <file> --canvas <WxH>` and paste the output into `ARTWORK_QA.md` with whatever failed; a failed test you report yourself = batch BLOCKED.
Full definitions: `../ASSET_ACCEPTANCE_TESTS.md`.

## 15. Scientific or historical limitations (what the art must not claim)
Generic mount; no specific telescope identity; no text.

Must not change: One telescope design across exterior, aperture and cutaway; same proportions, same mount type; not any specific real telescope; no text or logos.

Known failure modes: invented hardware; mount that cannot rotate; aperture not a true circle; different design in cutaway vs exterior; text on the housing.

## 16. Expected deliverable filenames
`tel_{base,pylon_near,pylon_far}_{side,34}_3000x3000.png`
Plus in the package root: `ARTWORK_QA.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md`, `previews/`, `SHA256SUMS.txt`, `CODEX_PROGRESS.csv` (see `../CODEX_HANDOFF.md`).
