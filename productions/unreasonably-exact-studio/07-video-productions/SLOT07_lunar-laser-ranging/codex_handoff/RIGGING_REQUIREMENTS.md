# Rigging requirements: what the art must make possible

Goal: do not discover missing layers after art generation (the V15 lesson). Every asset below says *what must move*, so the layers exist before animation starts. Claude implements the rigs; Codex delivers art that supports them. Unknown values are `null` and block integration (never guess pivots).

## 1. Delivery rules for layered assets
- RGBA PNG, straight alpha, every layer of one pose/view on the **same canvas, same pixel positions** as the master (no cropping, no trimming).
- Hidden overlap under each child: **at least 1.2% of the canvas width at 2x authoring size (about 36 px on 3000 px canvases), drawn as the parent's own material** (suit fabric, structure), never a generic round cap. State the unit in `PIVOTS.json`.
- Fill behind anything that moves: the layer underneath must contain what the mover uncovers.
- `RGB == 0` where `alpha == 0`; body alpha >= 245 counts as opaque; no stray components; nothing touches the canvas edge unless the master does.
- `PIVOTS.json` per asset family: `{layer: {pivot:[x,y], parent, draw_order, limits:[min,max]}}`. Certify each pivot by test (render at both limits on a flat background).

## 2. Per-system requirements
| Rig (manifest ID) | Must move | Art it needs | Limits / notes |
|---|---|---|---|
| RIG_001 Globe lighting (Earth, Moon) | globe rotation under fixed light; cloud layer drifts independently; terminator fixed in screen space | equirectangular surface, clouds (separate), night lights (separate), atmosphere rim (separate, radial) | Light never rotates with the globe. Atmosphere is drawn above the globe and slightly larger |
| RIG_002 Telescope + dome | dome slit opens; telescope tilts up inside the slit; slow dome rotation optional | dome, dome slit (separate door/opening layer), telescope housing, mount, aperture (front view), interior behind slit | Telescope tilt 0-75 degrees; telescope must be occluded by dome wall at its base: needs separate **foreground occlusion mask** layer (dome rim in front) |
| RIG_003 Astronaut pose | whole-pose blends; kneel-to-reach; limb offsets small (+-12 degrees) | ASTRO_010 pose set with component layers per pose | Rigid FK with deliberate suit joint rings; NO mesh cloth; dust is code (ballistic) |
| RIG_004 Camera + multiplane | parallax pushes of 3-10% and a macro push (about 8-10x) into one reflector cube | every environment split into >= 3 depth layers with bleed; reflector assembly authored at **>= 4096 px** so a macro push stays sharp | Macro push needs native detail in RETRO_002; if native generation is smaller, label `resampled` and ask Claude before use |
| Retroreflector transition | match-cut from real array to optical cross-section, same position and scale | RETRO_001 (assembly), RETRO_002 (cube array), RETRO_003 (cutaway, Claude code), RETRO_005 (3-face inset) | Registration marker: the same cube centre pixel in RETRO_002 and RETRO_003 |

## 3. Astronaut layer tree (back to front)
```
master (no art)
 pelvis: far_thigh -> far_shin -> far_boot
  torso (PLSS child; far_upper_arm -> far_forearm -> far_glove behind torso)
   neck -> helmet -> visor -> visor_reflection
   near_upper_arm -> near_forearm -> near_glove
  near_thigh -> near_shin -> near_boot
contact_shadow (child of master)
```
Joint extremes Claude will render for the seam test: shoulders +-30, elbows 0-100, hips 0-80, knees 0-120, ankles +-20 degrees (kneel_ and reach_ poses use the real range only).

## 4. Telescope and dome layers
Dome shell (front), dome slit opening (back, shows sky), dome rim occluder (front), building base, telescope tube/housing, mount/fork, aperture ring (front view), primary-mirror cutaway (separate cutaway asset). Each carries a pivot: telescope pivot = altitude axis; dome rotation pivot = dome centre.

## 5. Things that must NOT be baked into any art
Light rays, stopwatch numerals, text of any kind, arrows, lens flares standing for laser light, motion blur, depth-of-field blur (Claude adds those), drop shadows that move with the camera.

## 6. Proof clips these rigs must pass
P01 Earth rotation, clouds, lighting; P02 Earth-Moon parallax; P03 observatory-to-Moon transition; P04 telescope and dome movement; P05 astronaut movement; P06 astronaut and reflector; P07 corner-cube cutaway; P13 narration-aligned sample. Table with test conditions: `ASSET_ACCEPTANCE_TESTS.md`.
