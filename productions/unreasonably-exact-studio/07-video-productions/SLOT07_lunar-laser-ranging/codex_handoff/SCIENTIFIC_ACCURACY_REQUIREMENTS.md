# Scientific accuracy requirements for illustrated assets

Codex draws objects; Claude draws all explanatory graphics. These are the facts your art must respect. Sources: `SCIENTIFIC_CLAIMS_LEDGER.csv` (C01-C13, all closed) and `SCIENTIFIC_VISUAL_DESIGN.md`. Do not add numbers, labels or scales to artwork.

## Object facts
| Object | Facts to respect | Source |
|---|---|---|
| Earth | radius 6,371 km; axial tilt 23.4 degrees (do not paint a tilt unless the brief asks); atmosphere is a thin shell (about 1% of the radius visible as a rim); ocean/clouds/land proportions realistic | NASA fact sheets; saved references |
| Moon | radius 1,737.4 km; near side shows maria (dark, smooth) and highlands (bright); same face toward Earth, so the globe texture is the near side; no atmosphere, so black sky, hard shadows, a sharp horizon | NASA/LRO references |
| Earth-Moon | **not drawn to scale** in schematics (true spacing about 30 Earth diameters); declared once on screen by Claude | owner decision 2026-11-26 |
| Apollo 11 reflector (LRRR) | 100 fused-silica corner cubes, 10x10, 3.8 cm each, about 46 cm aluminium panel; round cube faces recessed in the panel; deployed tilted toward Earth; sits on the surface, small next to an astronaut | ILRS; C05 |
| Corner cube | three mutually perpendicular reflecting faces meeting at an apex; returns light back along its incoming direction. A 2-D slice shows two of the three reflections, so the third face is a separate inset | C06; SCI_005 |
| Observatory + telescope | generic lunar-ranging station: dome with a slit, an alt-azimuth telescope of order 1-3.5 m aperture; same telescope may send and receive; **not** any named real site | research notes; owner rule |
| Astronaut | Apollo EVA suit, gold visor, PLSS, gloved hands; vacuum: no cloth in wind, dust follows ballistic arcs under 1.62 m/s^2 | NASA photographs |

## Things artwork must never imply
1. A visible laser beam crossing space (real beams are invisible in vacuum; the real beam near the telescope is only a faint scattered line).
2. Light "bouncing" off the lunar surface as a mirror (the ordinary Moon scatters diffusely).
3. The reflector as a large mirror or a dish.
4. Sound, wind, fluttering cloth, or atmospheric haze on the Moon.
5. A bright, powerful return flash (the return is a few photons).
6. Earth and Moon at true relative separation, or at true relative size, without a declared model.
7. Different sun directions between assets.

## Perspective and model classes (what each asset is allowed to be)
| Class | Assets |
|---|---|
| Actual-object illustration (from photographs) | EARTH_*, MOON_*, ASTRO_*, RETRO_001/002/004, OBS_*, TEL_001/002/003 |
| Simplified scientific illustration | TEL_004 (primary cutaway), RETRO_005 (third face), EARTH_006 (atmosphere slice) |
| Educational symbols | all OPT_* and MG_* (Claude, code) |

Where an asset is a *simplified* illustration, mark that in `ARTWORK_QA.md` so the film can label it correctly.

## Disclosure
Write down anything you changed from the reference for readability (e.g. enlarged the atmosphere rim) in `ARTWORK_QA.md` under "Departures from reference". Claude will carry the departures into the QA ledger.
