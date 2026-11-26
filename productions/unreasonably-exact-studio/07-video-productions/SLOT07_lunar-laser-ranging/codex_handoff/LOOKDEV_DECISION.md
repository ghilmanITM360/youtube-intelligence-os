# LOOKDEV_DECISION: three treatments, one language

Written 2026-11-26 from STILLS ONLY. I rendered 18 panels (540x960) with `tools/lookdev.py panels`, viewed the contact sheets, the comparison sheet (which includes a 90x160 thumbnail row) and several panels at full size. No moving look-dev was watched. The owner has not approved anything here (G5 approval = owner).

Files: `look_dev/panels/treatment_{A,B,C}_{B01,B07,B17,B19_20,B26_27,B34_35}.png`, `contact_sheet_{A,B,C}.png`, `comparison_sheet.png`. Reference photographs used (all NASA public domain, TEMPORARY art): `look_dev/REFERENCE_USE.csv`. Source: `tools/lookdev.py`.

## What each treatment is (all drawn as layered composites, not boxes with labels)
| | World (real objects) | Scientific graphics | Built from |
|---|---|---|---|
| **A Illustrated documentary** | the C world after a mean-shift "gouache" simplification, warm/cool tonal glaze, no grain, no outlines | 3 px hairlines, Georgia italic labels | the same layers as C, filtered |
| **B Premium motion graphics** | flat polygons: dome, flat gibbous Moon, flat astronaut/reflector icons, flat Earth disc | 14 px strokes, Avenir Heavy, big numerals | separate flat builders (no photos) |
| **C Hybrid cinematic** | sky / stars / Moon (LROC map on a lit sphere, waning gibbous) / two ridges / dome + slit + tube / foreground; Earth cap (NASA map on a sphere, thin atmosphere rim); lunar plate in far and near slices + reflector + astronaut cutouts + hard shadows | 7 px crisp vector, warm out / cool back | photographs and maps colour-matched under one Sun |

## Scores. HC categories I can judge from stills (0-5, "stills only"); the rest are NOT SCORED
| HC category | A | B | C | note |
|---|---|---|---|---|
| Composition & focus (stills) | 4 | 4 | 4 | all keep one focal point and quiet negative space; B is the clearest |
| Pose & drawing / object coherence (stills) | 3 | 2 | 4 | B's astronaut icon is generic and childlike; A's filter smears the Moon and the astronaut's suit into patches |
| Compositing (stills) | 3 | 4 | 4 | C has visible plate seams (see weaknesses); A inherits them and adds filter noise; B has none because nothing is composited |
| Type & accessibility (stills) | 2 | 5 | 4 | A's 3 px hairlines and small italics fail at thumbnail size |
| Originality & reference ethics | 4 | 3 | 4 | B is the most generic "explainer" look; A and C learn from NASA photography without copying a frame |
| Technical & editability | 3 | 5 | 4 | see UE table |
| Story clarity (stills) | 4 | 5 | 4 | B states the idea fastest; C needs the caption for the astronaut beat |
| Timing & spacing, rig/character craft, camera & space, editorial rhythm, sound & narration | not scorable from stills | | | |

## UE criteria
| Criterion | A | B | C |
|---|---|---|---|
| **One visual language through the film** | breaks: sharp code overlays sit on a filtered world | strongest (everything is flat) but contradicts the art direction: no real hardware, no Apollo credibility | holds: real-object layers + one graphics layer, exactly the "two languages that never mix" rule in `PRODUCTION_ART_DIRECTION.md` |
| **Codex-producibility** | needs painterly illustrated masters (the brief's target) but a post filter is not a substitute | needs no Codex art at all | needs Codex illustrations of the same layers; the photo stand-ins are already cut to the layer list, so Codex art drops into the same rig |
| **Edit-ability in code** | filter is slow (about 1 s/frame), parameters interact | fully parametric | layers + sprites + parametric graphics; spheres re-lit by changing one vector |
| **Phone readability at 540x960** | hairlines thin out | excellent | good; diagram strokes were raised from 6 to 7 px after this review |
| **Thumbnail (90x160) readability** | weakest (Moon, dome and hairline path nearly vanish) | best (diagram shapes survive) | middle: Moon / Earth / astronaut identify at once, thin diagram strokes are the weak part |

## Decision: C, with B's diagram discipline and A as the target rendering of the real-object layers
**Selected language: C (hybrid cinematic science explainer)**, applied to every shot with no per-shot style changes. Justified hybrid, not three styles:
1. Real-object layers (Earth, Moon, dome, surface, astronaut, reflector) keep C's layered construction. The final rendering of those layers is the brief's "painterly-clean illustration" (what A tried to approximate); the animatic uses reference-based stand-ins so the timing, depth and light are proven first. A as a post filter is rejected: it hurt readability and cannot be edited deterministically.
2. Scientific graphics follow B's discipline (few elements, bold enough to read at 540 px, one idea per frame) but keep C's colour grammar and 7 px stroke. B as a whole is rejected because it removes the real-world credibility that carries H1 and H2 and conflicts with the art direction.
3. One Sun upper left, shadows to the right, in the sphere shader and in the contact shadows. The only deviation that I could not remove: the photographic regolith plate carries its own baked shadows.

## What is weak (honest list)
- **Photographic plate seams.** The ground plate is one photograph with the reflector cloned out and a right-hand extension cloned from the left of the plate; a faint horizontal band and an abrupt horizon step on the right remain. Reseau crosses from the original camera are visible near the horizon.
- **The astronaut and reflector are photographs of real hardware and a real, named person (face hidden).** Allowed here as TEMPORARY animatic art; they must not ship. The photographed astronaut faces left and walks only by translation and bob, no leg cycle.
- **Observatory is plain.** The dome has panel seams and a slit but no texture or work-light detail; the foreground is a dark mass that exists mostly to hold the caption band.
- **Earth is magnified about 2x** from a 2048 px equirectangular map; soft but acceptable at 540 px.
- **Array macro** in P4 uses the Apollo 14 photograph as a window; the cutout from the surface shot to this macro is not a physical push in the stills.
- **A's Moon turns to patches** and B's astronaut reads as a toy: both are recorded as reasons, not hidden.
- **Stills only.** Motion, pacing, and the transitions that the chosen language depends on were not evaluated here; see `storyboard/ANIMATIC_V1_NOTES.md`.
