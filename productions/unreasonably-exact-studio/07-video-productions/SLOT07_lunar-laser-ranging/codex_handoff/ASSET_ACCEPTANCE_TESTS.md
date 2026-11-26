# Asset acceptance tests

Claude runs these before using any file. **Any failure means the asset stays `CANDIDATE`.** A failed test that Codex reports itself means the batch is `BLOCKED` and is not integrated. Never label an asset `APPROVED`: only the owner approves art, and only after a passing proof clip. A PNG that exists is not a finished asset. Derived from playbook §7.5-7.7 and §8.6; run with `codex_handoff/tools/validate_asset.py` (needs numpy, Pillow, scipy).

## A. Automated (every PNG)
| # | Test | Pass condition |
|---|---|---|
| A1 | Mode, canvas | RGBA; canvas equals the manifest `canvas_size` for that asset |
| A2 | Alpha range | alpha reaches >= 245 where solid; no all-transparent file |
| A3 | RGB under zero alpha | **0 pixels** (otherwise crop by alpha; note it) |
| A4 | Stray components | none above 400 px detached from the main body |
| A5 | Haze | semi-transparent share <= 25% of non-empty pixels |
| A6 | Registration | alpha bbox lies inside the safe region stated in the brief; layers of one pose share the master's canvas |
| A7 | Hash | SHA-256 of every file recorded in `ASSET_MANIFEST.csv` |
| A8 | Native size | `generation_px` stated; any larger export labelled `resampled=yes` |

## B. Visual (a human or Claude looks; evidence = contact sheet, which is *prepared evidence, not review*)
| # | Test | Pass condition |
|---|---|---|
| B1 | **Rest test** | assembled layers at rest equal the master within anti-aliasing (report max diff and pixels > 8) |
| B2 | **Seam test** | at every listed joint extreme, on a flat background: no gap, disc, double outline |
| B3 | **Occlusion test** | moving a child reveals parent material, not empty background |
| B4 | **Identity test** | astronaut: same helmet, visor, gloves, PLSS, boots in every pose (see CHARACTER_CONSISTENCY_GUIDE) |
| B5 | **Light test** | sun from the left, about 30 degrees up; shadows to the right; same on every asset |
| B6 | **Reference test** | side by side with the saved reference photographs: silhouette, proportions, panel structure match; list departures |
| B7 | **Count test** | cube count (10x10), finger count, strut count correct where the brief gives a count |
| B8 | **No-baked-graphics test** | no text, numerals, arrows, rays, flares, motion blur anywhere in the art |
| B9 | **Registration test (reflector)** | the same cube centre pixel exists in the array and the cutaway, so the match cut lines up |

## C. Motion proofs (Claude renders; owner reviews on a phone)
Each proof is 5-12 s, uses the **shot's actual range of motion** (not 60% of it), and is saved with a note of what was tested.
| Proof | Demonstrates | Pass condition |
|---|---|---|
| P01 | Earth rotation, clouds, lighting | rotation under fixed light; clouds drift independently; no seam at the texture wrap; atmosphere rim steady |
| P02 | Earth-Moon parallax | layers separate with consistent depth; no popping |
| P03 | Observatory to Moon | slit opens, telescope tips, camera moves up to the Moon without inconsistent lighting |
| P04 | Telescope + dome | tilt and dome rotation with occlusion correct at the dome rim |
| P05 | Astronaut movement | kneel / reach blend without seams; dust ballistic; no cloth motion |
| P06 | Astronaut and reflector | scale ratio (46 cm panel vs human) and contact shadow correct |
| P07 | Retroreflection | exit rays antiparallel to entry rays (asserted in code); flat-mirror contrast variant |
| P08 | Light journey | pulse and stopwatch stay in step; colour grammar warm out / cool back |
| P09 | Faint detection | sparse markers, no bright flash |
| P10 | Pulse accumulation | peak emerges from background; counts labelled illustrative |
| P11 | Stopwatch sync | final reading is exactly 2.56 s |
| P12 | Distance calculation | the path bar folds in half; readout appears on the "distance" word |
| P13 | Narration-aligned sample (B17-B21 proposed) | reveal events land on the anchor words |

## D. Status ladder
`PLANNED` spec exists -> `RESEARCHED` references saved and viewed -> `CANDIDATE` art generated -> `REGISTERED` layers and pivots verified -> `RIGGED` controls implemented -> `MOTION_TESTED` required movement proven -> `APPROVED` all tests passed and the owner signed off. `BLOCKED` records the specific unresolved issue.

## E. Package contents (every Codex delivery)
`ARTWORK_QA.md` (what you checked and what FAILED), `ASSET_MANIFEST.csv`, `PIVOTS.json`, `IMAGE_GENERATION_PROMPTS.md` (exact prompts, rejected ones marked), `previews/`, `SHA256SUMS.txt`, and `CODEX_PROGRESS.csv` (see CODEX_HANDOFF.md).
