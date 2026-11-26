# Production art direction: Slot 07 "Lunar Laser Ranging"

Binding for every illustrated and texture asset. Written by Claude 2026-11-26. If you (Codex) disagree with a rule, write the disagreement in `ARTWORK_QA.md` and ask; do not silently deviate.

## 1. What the film is
A 94-second vertical (1080x1920) science short. A narrator explains how a laser pulse sent to the Moon and back is timed. The picture has to *explain*, so objects are simple, readable on a phone, and consistent from the first frame to the last. Quality bar: a hand-directed motion-design piece, not a set of unrelated AI illustrations.

## 2. Two visual languages that never mix
| Language | Used for | Drawn by | Rules |
|---|---|---|---|
| **Illustrated real objects** | Earth, Moon, observatory, telescope, astronaut, reflector, terrain | **Codex** (you) | Painterly-clean cinematic illustration: soft value shapes, subtle grain-free gradients, **no outline strokes**, no photographic noise, no text, no numbers, no arrows, no diagrams |
| **Scientific graphics** | light pulse, rays, stopwatch, rulers, histograms, brackets, labels | **Claude, in code** | Flat vector, rounded caps, 6 px strokes at 1080 wide, warm/cool colour grammar |

You never draw rays, beams, glows that stand for light, photons, dials, digits, formulas or captions. If a master needs a light effect (visor sheen, sun glint), it is *surface lighting on the object*, not a beam.

## 3. One sun, one direction (film-wide)
The Sun is to the **left**, about **30 degrees above the horizon** in screen space (light vector from left, slightly above). Consequences for every asset:
- spheres (Earth, Moon): lit side on the left, terminator curving on the right, night side right;
- lunar surface, astronaut, reflector: shadows fall to the **right** and slightly down, hard-edged (no atmosphere, no soft penumbra beyond the sun's disc);
- observatory at night is lit only by faint starlight and a small cool work-light; **the dome never receives sunlight**;
- **phase rule (decided 2026-11-26 from the reference research):** the film shows Earth and Moon as mostly-lit discs (gibbous), lit from the upper left with the light slightly toward the viewer, so the single sun direction holds; the Moon in the observatory sky is a waning gibbous lit on its left. Phase shading is done in code (MOON_004/EARTH_005 masks) over full-disc textures, so textures carry no baked phase;
- never repaint lighting per shot. If an asset needs a different light direction for a proof, it is a different, labelled asset.

## 4. Palette (sRGB hex; stay within hue family, vary value)
| Role | Value |
|---|---|
| Night sky / deep space | #070B1A to #16223F (gradient up to the horizon only) |
| Moon surface, light | #ACACB0; mid #7E7E84; shadow #3A3A42 |
| Maria on Moon | #55555D to #6A6A72 (cooler, darker than highlands) |
| Earth ocean | #0A1A3E (night) to #2C6CC4 (lit) |
| Earth land | muted greens/ochres, never saturated |
| Clouds | #F0F4FA at 85% value, soft |
| Atmosphere rim | #60C8FF at low opacity, thin |
| Instrument white / grey | #E6E9F0, #AEB4C2, #6A7080 |
| Suit white | #ECEEF4 (never pure #FFF); gold visor #D6AA46 |
| **Reserved for code-drawn light** | warm #FFAC40 (outbound), cool #60C8FF (return) |

**Do not use the reserved warm/cool pair as large painted areas** in any asset; they mean "light going out / coming back". The Earth atmosphere rim is the one permitted use of a pale cool tone, kept thin and dim.

## 5. Camera, framing and depth
- Final frame is 9:16. Assets are authored at 2x (2160x3840) unless the manifest says otherwise. Keep key subjects inside the **safe box (y 150-1440 of 1920, x 60-1020)**; a **caption band sits at about y 1480-1730** (provisional).
- Earth is at the **bottom** and the Moon at the **top** in every schematic frame. Do not paint compositions that invert this.
- Environments are built as separate parallax layers (see manifest `draw_order`); each layer is a clean silhouette with generous bleed beyond the 9:16 crop so the camera can move 6-10%.

## 6. Realism target
Painterly but **photo-referenced**: proportions, panel structure, colours, material behaviour come from the saved photographs in `references/`. Simplify detail, do not invent hardware. Where the references disagree, follow the NASA/agency photograph; where nothing exists (the generic observatory), the brief says so and you design to the references' *geometry* without copying any specific site.

## 7. Honest-labelling rules (visual)
- The observatory is a **generic, illustrated** lunar-ranging station. Never reproduce signage, a real site name, a real logo or a specific building.
- The astronaut is **unnamed**; no mission patches that identify a person, no name tags, face never visible (visor reflects, gold).
- The reflector is the **Apollo 11-style 10x10 array** (100 cubes, 46 cm panel, 3.8 cm cubes); the Apollo 14 and 15 arrays are reference only.
- Nothing is photographic composite of a real person.

## 8. What "premium" means here (the checklist the owner will apply)
Consistent shape language across assets; same light on everything; no random line weights; no melted or fused geometry; correct count of fingers, cubes, struts; no detached floating pieces; no generic stock backgrounds; every asset registered so layers drop in with no re-fit.
