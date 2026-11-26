# ANIMATIC V1 (reference informed): what changed, how it was checked, what is still weak

Generated 2026-11-26. `storyboard/animatic/ANIMATIC_V1_REFERENCE_INFORMED.mp4`, built by `tools/animatic_v1.py` (engine and assets in `tools/lookdev.py`). 540x960, 24 fps, h264 yuv420p, 94.0 s, the unmodified master `narration/raw/SLOT07_NARRATION_RAW.wav` muxed (AAC 192 kbps, silence-padded after 92.53 s). V0 is untouched.

**Not approved. Nothing in this animatic has been watched continuously by a human, by me or by anyone else.** I looked at still frames only. V0's technical checks (decode, durations) and mine are not artistic proof. Every statement about pacing, motion quality and edit rhythm below is UNVERIFIED until someone plays it at phone size with sound (G2 owner approval = NOT PERFORMED).

## Technical checks (these prove the file, not the film)
- `ffprobe`: video h264 540x960 yuv420p 24/1, 2256 frames, duration 94.000000 s; audio aac 24 kHz mono, duration 94.000000 s; container duration 94.000000 s.
- `ffmpeg -v error -i ... -f null -`: no output (decodes cleanly).
- Audio: the decoded AAC track correlates 0.9999 with the source WAV over its length, and the RMS after 92.6 s is 0.0 (silent tail). The narration samples were not edited; only AAC encoding and trailing silence were added.
- Tail: narration ends 92.53 s, last caption off at 92.6 s, the picture holds, fades to black 93.2 to 94.0 s (0.8 s). Last frame is black.
- Caption and key-subject audit runs on every one of the 2256 frames inside the video build (`ANIMATIC_V1_SAFE_AUDIT.json`, result: `[]`, 0 violating frames). Caption layout is asserted for all 41 caption chunks (widest box 941 px of the 960 px band, max 2 lines).

## Our provisional mask (NOT a platform specification)
Declared in `tools/lookdev.py` and used by the audit: **caption band x 60-1020, y 1480-1730** (1080x1920 space); **key-subject box y 150-1440, x 60-1020**; nothing is placed below y 1730. These numbers were chosen so key subjects clear a typical bottom UI strip; they are not verified against any real UI overlay. The audit asserts (a) every caption box lies inside the band, (b) no registered key subject intersects the band or extends below y 1440. Key subjects registered: Moon, dome, stopwatch, readouts, traces, reflector, astronaut, cube diagram, mirror, inset, telescope, histogram, dots, bar, ruler. The Earth limb is background and is allowed to enter the band (it does in every schematic; the caption pill sits over it). Transient exceptions (marked `~`, ignored by the audit): the pulse bead in flight, the dome while it falls away during the Earth-rise handoffs, the astronaut while walking in or while off-frame in the B19 push-in, the full-frame Moon during the B14-B15 push-in. Left/right and top margins are not asserted; the HUD (review aid, 21 px mono, top-left) and the top 150 px are outside the box by design.

## V0 defect by defect
| V0 defect | What changed | How it was verified (all frame times are from the final MP4 unless marked "engine") |
|---|---|---|
| **Incomplete ending / tail padding** | Timeline is 94.0 s: narration to 92.53 s, picture hold, 0.8 s fade to black 93.2-94.0 s; audio padded with silence to 94.0 s. B39 settles the ruler value on "is" (91.99 s), then holds. | ffprobe durations equal; frames 90.3, 92.4, 93.7 s viewed (value settled, fading, near-black). |
| **Caption safe area** | Captions are word-timed chunks (from `WORD_TIMESTAMPS.json`, word edges +-0.12 s), at most 2 balanced lines, in a translucent pill centred in the declared band; the audit asserts layout and key subjects (see above). | Assertion output plus a zero-violation audit of all frames. Frames at about 40 times viewed: pills sit in the lower band, key subjects above. |
| **Excess information at B20** | Cross-section only. Rays enter one at a time (3 rays, 0.62 s each from 44.95 s), earlier rays dimmed to 22 %. The magnified footprint inset enters on "tiny fraction" (45.55 s) and fades out at 47.0 s. The V0 third-face inset, the in/out arrows and the "cube/flat mirror" words are gone (words became a check mark and a cross at B21). A one-line "simplified 2-D cutaway" tag shows 44.25-45.4 s. | Frames 44.3 (engine), 45.2, 45.8 (MP4 and engine), 46.5 (engine), 47.7, 48.4 viewed. At 45.8 one ray is bright, one dimmed, inset present: legible. |
| **Link between the trajectory and the folded distance** | The traced path itself becomes the bar: the warm outbound trace (x 500) and cool return trace (x 580) peel off the Earth-Moon line (80.95-82.35 s), rotate and shrink to lie end to end as one bar (c x t), the cool half folds over the warm half about the midpoint with a short anticipation (82.95-83.6 s, "divide by two"), and the doubled bar rotates and grows back onto the Earth-Moon line (84.35-85.3 s), turning white and gaining ruler ticks as the distance. | Frames 81.4, 81.8, 82.0, 82.4, 82.5, 83.0, 83.3, 83.8, 84.6, 84.9, 85.0, 85.6 viewed. The sequence reads as one object moving. The bar is drawn at about half the line's length so it fits horizontally (a stated scale change; the object shown is the same). |
| **Placeholder planetary geography** | Earth and Moon are NASA SVS/LROC equirectangular maps on lit spheres (`sphere_region`): one Sun, upper left and slightly toward the viewer, soft terminator, thin cool atmosphere rim on Earth, Moon waning gibbous with a faint earthshine ambient. Earth shows Africa and the Atlantic. NOT TO SCALE appears once (9.0-11.8 s), plus "orbit exaggerated" at B12-B13. | Frames 9.9, 12.6, 29.5, 33.1, 56.9, 87.5 viewed. Earth is upsampled about 2x (soft). |
| **Simplified astronaut and observatory silhouettes** | Astronaut and reflector are cut out of NASA photographs (suit, PLSS, gold visor, true proportions: helmet about 1/8 of figure height, PLSS box visible). The observatory has a hemispherical dome with panel seams, shutter slit, telescope tube silhouette and catwalk, built to the proportions of the laser-ranging photographs but a generic site. | Frames 38.0, 40.4, 43.3 (astronaut, reflector); 1.9, 4.5, 7.75 (dome). The observatory is still plain (see weak list). |
| **Consistent light direction** | Sun upper left in the sphere shader, shadows to the right (`contact_shadow`, plate flipped so its baked shadows fall right), the dome lit only by a faint cool top light, never the Sun. | Frames 9.9, 33.1, 40.4 viewed. The plate's baked shadows are the photographer's, not ours. |
| **Real depth, parallax and overscan** | Independent layers with parallax factors p (sky/stars 0.97, Moon 0.96, far ridge 0.94, near ridge 0.97, dome 1.0, foreground 1.10; far/near ground slices 0.94/1.0; stars 0.1 vs Earth 1.0 in the pull-back) and overscan (plate 2070 px wide for a 1080 frame, sky 3400 px tall). Numeric differential from the engine: ground tilt 1.0->2.5 s shifts the foreground 619 px, dome 563 px, far ridge 529 px (about 90 px between nearest and farthest); surface ease-out 39->41.4 s shifts the far slice 237 px and the near slice 255 px horizontally; pull-back 87->89 s moves the Earth limb 2010 -> 1400 px and the stars 4 px. | Numbers from `Cam.map`; frames 1.9, 4.5, 6.3, 38.0, 40.4, 87.5 viewed. Honest label: the ground tilt is a tilt with small crane-like parallax, the ground slices differ by only 6 % (a subtle effect, a flat Ken Burns would look similar to a casual viewer), the strongest depth is the pull-back. |
| **Clearer optical explanation** | Cross-section is oriented with light entering from below (Earth at the bottom in the film grammar) and leaving downwards, so the B21 exit ray is travelling the same way as the B22 returning bead; B21 puts a flat mirror beside a smaller cube: the mirror throws the ray sideways (cross), the cube returns it anti-parallel (check). | Frames 47.7, 48.4 viewed; exit offset is visible because the replay ray enters off-axis. |
| **Motivated camera moves** | Table below (also printed by `python tools/animatic_v1.py camera`). | Not testable from stills. |
| **Meaningful transitions** | See list below. No flashes: every transition is a movement, wipe, iris or match. | Frames across each viewed; none played. |

### Transitions (each states its relationship)
| Cut | Relationship |
|---|---|
| B04 -> B05 (8.04-8.9 s) | movement handoff: the pulse leaves, the camera pulls out of the ground group as the Earth limb rises; the Moon is the same sprite and lands on (540, 430) |
| B11 -> B12 (26.46-27.0 s) | soft upward wipe (a change of model; upward because Earth is at the bottom) |
| B14 -> B15 -> B16 (31.75-33.6 s) | exponential push-in on the Moon, dissolve to the same Moon's surface |
| B16 -> B17 (37.62-38.05 s) | match cut: ghost mirror dissolves into the real reflector at the same spot and scale |
| B18 -> B19 (42.62-44.4 s) | push-in on the array face, magnifier-ring iris opens onto the cross-section |
| B21 -> B22 (49.58 s) | hard match cut on direction of travel (exit ray down, returning bead down) |
| B22 -> B23 (50.0-50.5 s) | push-in on the tube tip, dissolve to the cutaway |
| B23 -> B24 (53.1-53.5 s) | dissolve to the dimmed dome (hush) |
| B24 -> B25 (55.0-55.7 s) | same Earth-rise handoff as B04-B05 |
| B25 -> B26 (58.2-58.7 s) | fade through the page colour (a change of subject: statistics) |
| B29 -> B29b, B30 -> B31 | dissolve; upward wipe into the model view (75.5-76.2 s) |
| B36 -> B37 | the ruler stays glued to Earth and Moon through the pull-back |

## Frames actually looked at
From the final MP4 (extracted with ffmpeg, viewed as contact sheets): 1.9, 4.5, 6.3, 7.75, 8.45, 9.9, 12.6, 16.3, 18.9, 20.7, 22.5, 29.5, 31.2, 33.1, 35.5, 38.0, 40.4, 43.3, 43.8, 45.8, 47.7, 48.4, 50.3, 51.7, 54.4, 56.9, 60.7, 63.3, 64.5, 66.9, 71.0, 73.5, 81.8, 82.4, 83.3, 84.9, 87.5, 90.3, 92.4, 93.7 s.
From the engine during development (same renderer, earlier revisions, at 540x960): 0.2, 1.3, 1.8, 1.9, 2.9, 4.0, 4.5, 5.4, 6.3, 7.2, 7.75, 8.0, 8.3, 8.6, 9.2, 9.95, 10.3, 11.0, 12.5, 14, 15.6, 16.3, 18.2, 19.0, 20.5, 21.2, 22.5, 23.4, 25, 26.7, 28, 29.5, 30.5, 31.3, 32.2, 32.9, 33.3, 33.8, 34.4, 35.4, 36.5, 37.8, 38.3, 39.2, 40.0, 41.0, 42.5, 43.2, 43.8, 44.3, 45.2, 45.8, 46.5, 47.3, 48.4, 49.7, 50.1, 50.35, 51.0, 51.6, 52.5, 53.4, 54.0, 54.8, 55.3, 55.9, 56.8, 57.6, 58.5, 59.5, 60.7, 61.5, 62.3, 60.9, 63.3, 64.3, 65.0, 66.3, 66.8, 67.4, 68.2, 69.2, 70.8, 72.0, 73.2, 74.5, 75.6, 76.0, 76.8, 77.6, 78.5, 79.4, 80.3, 81.4, 82.0, 82.5, 83.0, 83.3, 83.8, 84.6, 85.0, 85.6, 86.6, 87.5, 88.5, 89.7, 90.2, 91.0, 93.6 s. Revisions made from those views: caption widow words, B21 ray offset, ground-slice seams, shadow bands, the plate right edge, readout overlap with ruler ticks.

## Temporary art used (public-domain NASA photographs and maps; also `look_dev/REFERENCE_USE.csv`)
REF-ASTRO-003 (astronaut cutout), REF-RETRO-001 (reflector cutout and ground plate, flipped), REF-RETRO-006 (array window in the look-dev panels only), REF-MOON-013 (Moon sphere map), REF-EARTH-013 (Earth sphere map). All are TEMPORARY animatic art and must be replaced by Codex illustrations of the same layers; a photograph of a named astronaut is not a shippable asset under `PRODUCTION_ART_DIRECTION.md` section 7.

## Animation craft notes (HC principles used, only where they change meaning)
Light travels at constant speed (no easing) and is slowed by 1.84x so the stopwatch and the bead agree (2.56 s of clock for 4.72 s of screen time). The bead has a short launch kick, then cruises. The telescope tube swings toward the Moon with a small overshoot (B03). The aperture charges for 0.43 s before the pulse leaves (anticipation, B04). The readout "2.56 s" pops with a short overshoot at B07. The fold at B35 has a 0.18 s anticipation in the opposite direction, then fast rotation with ease. The reflector settles with a damped bounce and dust follows parabolic arcs (B18). Counting readouts use a tabular mono face so digits do not jitter.

## What is still weak
1. **Astronaut animation is a placeholder**: one photographic pose translated with a vertical bob; feet slide; no leg cycle; "sets the array" is a damped drop of the reflector sprite plus dust, not a hand action. Needs the ASTRO rig from Codex.
2. **Ground plate seams**: a faint horizontal band and a stepped horizon on the right (cloned extension), reseau crosses, and the plate is slightly soft at the 2x B15-B17 zoom (deliberately like depth of field).
3. **Ground parallax is subtle** (6 % between slices); the observatory is plain, the foreground is a dark mass, and the sky has only a gradient and stars.
4. **B05 vs B06**: the first pulse (B05, to the ring) and the timed pulse (B06) are two launches; nothing on screen says "replay".
5. **B09** carries a bracket, a struck "2.5 s", then two "1.28 s" labels in 1.3 s: likely busy; unverified by a viewer.
6. **B20-B21 geometry** is a 2-D simplification (two reflections; third face omitted and disclosed in the tag). The exit ray and entry ray are drawn offset only when the ray enters off-axis.
7. **B14-B15**: the Moon texture is stretched to r 1500 before the dissolve to the surface; it is soft.
8. **Caption timing** uses estimated word edges (+-0.12 s). The caption pill is nearly invisible over very dark frames (by design); over bright ground it is grey.
9. **B25 cones** are qualitative (the return footprint is drawn wider than the beam, the array and the telescope are tiny markers). Not to scale and not captioned again.
10. **B29 atmosphere band** is exaggerated about 8x in thickness; the correction mark is a check glyph, not a measurement.
11. **B38 last return** is a 55 % size bead taking 0.7 s, faster than the leg timing used elsewhere (1.28 s physical); an editorial shortcut.
12. **Audio**: no sound design, no mix; only the narration.
13. **No EDITORIAL or ANIMATION review pass has been written for moving footage** because none was watched.

## Camera notes (every camera move has a stated reason)
| Beats | Time | Move | Reason |
|---|---|---|---|
| B01 | 0.6-2.7 s | tilt up 640 px (ease in-out), layers p 0.94-1.10 so the near ground shifts slightly more than the sky | reveals the target on the word "laser"; the Moon enters at the top as the word lands |
| B02 | 3.47-5.0 s | locked | the rejected floodlight idea is the only event; nothing else may move |
| B03-B04 | 5.05-8.04 s | push-in 1.0 -> 1.40 (+0.08 creep) toward the dome slit | moves from "a place" to "the instrument"; the question becomes one pulse leaving the aperture |
| B04-B05 | 8.04-8.90 s | pull back to 1.0 while the ground group drops 1100 px and the Earth limb rises from below | movement handoff: the pulse leaves Earth, we leave with it; the Moon lands exactly on its schematic spot (540, 430) |
| B05-B11 | 8.9-26.46 s | locked schematic | the stopwatch and the pulse are the only motion; a moving camera would corrupt the distance reading |
| B12-B13 | 26.46-31.06 s | soft upward wipe into the orbit diagram | a change of model (top-down), so a change of view; wipe runs upward (Earth is at the bottom) |
| B14-B15 | 31.75-33.6 s | exponential push-in on the Moon (r 56 -> 1500), then dissolve to the surface | scale change from "the Moon in space" to "the ground under the pulse"; exponential so the zoom feels constant |
| B15-B17 | 33.15-38.65 s | near-locked at z 2.0 (+0.02 drift) on the target spot | ghost mirror and real reflector must share spot and scale for the match cut |
| B18 | 38.65-41.5 s | ease out 2.0 -> 1.0 with a pan right (490 -> 600); far/near ground slices at p 0.90/1.00 | reveals the astronaut for scale as he walks in; differential ground slices give depth |
| B19 | 42.62-43.85 s | anticipation dip (-3%), then push-in 1.0 -> 2.6 to the array face, circular iris opens at 43.6 s | scale change into the optics; the iris is a magnifier ring, the same device as the B20 inset |
| B20-B21 | 44.8-48.5 s | locked; the diagram shrinks and slides left in B21 (by the diagram, not the camera) | one idea at a time; B21 needs room for the flat-mirror comparison |
| B22 | 49.58-50.45 s | hard cut from the exit ray (travelling down) to a bead travelling down; push-in 1.0 -> 1.7 on the tube tip in the last 0.4 s | match cut on direction of travel (Earth at the bottom in both); push-in hands over to the cutaway |
| B23 | 50.1-53.1 s | locked cutaway, quiet hold after the detector lights | restraint moment: the detector lighting is the event |
| B24 | 53.1-55.0 s | slow push-in 1.0 -> 1.05 while the frame dims | hush: the image narrows and darkens before the surprise |
| B25 | 55.0-55.7 s | the same Earth-rise handoff as B04-B05 | return to the schematic where the two widening cones can be read |
| B26-B30 | 58.7-75.3 s | locked | statistics are read as a static chart; only the data move |
| B31 | 75.5-76.2 s | upward wipe back to the model view | the details drop away: Earth-Moon line only |
| B32-B36 | 77-86 s | locked | the bar peeling off the path, folding, and returning is the whole event |
| B37 | 86.4-89.4 s | slow pull-back 1.5 -> 1.0 (ease out), layers p 0.1 / 0.9 / 1.0 (stars / Moon / Earth) | the wide shot for "not just hanging in the sky"; parallax proves it is a space, not a flat picture |
| B38-B39 | 89.4-94 s | locked, then fade to black 93.2-94.0 s | stillness for the conclusion |

The rest of the shots use a locked camera (listed above as "locked"). The per-layer parallax factors are in `tools/lookdev.py` (`ground_layers`, `surface_layers`) and `tools/animatic_v1.py` (`put_moon`, `sc_close`).
