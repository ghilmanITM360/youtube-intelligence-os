# V10 screenshot defect audit

## Sources

- **Owner screenshots:** the nine `Screenshot 2026-11-25 at 12.50.36–12.52.27 PM.png` files from the Desktop. Copies are in `qa/owner/`, with a contact sheet at `qa/owner_sheet.png`. Each was viewed.
- **V10 frames:** extracted from `../v10/SKYDIVER_SLOWDOWN_V10.mp4` at the same seconds into `qa/before_after/v10/`.
- **Full sequences:** each frame was mapped to its V10 shot in `../v10/tools/v10_shots.py` and the whole shot was reviewed, not only the still.
- **Timestamps:** playback-bar times are rounded to the second. The 0:16 screenshot shows the E1 three-quarter shot, which starts at 16.80 s.

## Findings

**Origin codes:**
- **ART:** artwork
- **REG:** rig registration
- **ORD:** layer order
- **ROT:** rotation
- **MOT:** motion curves
- **CAM:** camera framing
- **INS:** instrument composition
- **SCI:** scientific diagram design

| Time | V10 shot | What is wrong | Origin | V11 fix |
|---|---|---|---|---|
| 0:13 | D1 questions (side rig) | The pack reads as a separate tan lump sitting on the back. The harness does not visibly hold it. Beige knee/elbow discs and oval boot tops show. | ART (separately drawn pack and limb parts with round caps), REG/ORD (pack layer floats over the torso layer) | Whole-pose Codex V11 side drawing: harness straps wrap the pack and torso in one drawing. Boot-top ovals painted out (`tools/fix_boots.py`). No joints to open. |
| 0:16 | E1 (three-quarter rig) | Large circular shoulder/elbow/knee discs, disconnected boot tops and a smiling face, so the figure reads as a different person. | ART (caps baked into parts), ROT (flat parts rotated in-plane show the discs) | Codex V11 three-quarter pose with continuous bends and a neutral expression. Far sleeve recoloured to the cream jacket (`tools/recolour.py`). Gloves still differ from the bare-handed side pose (open). |
| 0:20 | E1 airflow | Uniform dashed vertical lines across the whole frame read as rain or background texture. Most lines are far from the body. | SCI (no flow source, no relation to the body, no direction marks in a still) | New `flow_lines()`: a "you: moving down" arrow first, then lines grow from below, part around the body and carry up-pointing chevrons. Lines exist only near the body, fade at their ends, and are labelled "relative airflow · simplified sketch". |
| 0:22 | F1 reset (side rig) | Knee and elbow caps, and oval boot ends. Limbs look bolted on. | ART, REG | Whole-pose side drawing (as 0:13). |
| 0:32 | I2 drag grows | Stiff pose (fixed rig), dashed streamlines fill the frame behind the arrows, and the clock card stays in the corner. | MOT (flutter only on rigid parts), SCI (streamlines too wide and decorative) | Whole-pose figure with calm whole-body motion. Flow lines are limited to the body. The wrist inset replaces the clock card. |
| 0:41 | K1 cross | A "weight length" tick and label, "body position held fixed", the STATE label, the clock card, both arrows and the caption all compete. | SCI (all overlays at once) | K1 is split into three steps, one idea each: forces on one scale; a ring on the tips ("tiny difference here"); a circular reveal into the full-frame ZOOM ×30 card. |
| 0:55 | N1 dial | The instrument fills the screen. It is a 4-mark clock face with a long empty strap and no wrist, and the gridded farmland shows behind it. | INS (standalone device), CAM (framed without the wearer), ART (blank 4-mark dial; procedural grid ground) | Gaze shot (M2) → first-person forearm with the device on the wrist (N1) → push-in to a readable SLOW…FAST "DOWN SPEED" face, needle falling → tilt to the ground (O1). Irregular terrain. |
| 0:56 | N1 dial | Same as 0:55. The needle is the only cue, and a 4-mark face reads as a clock. | INS, ART | Same as 0:55. The dial has a graduated band, SLOW/FAST labels and "DOWN SPEED" with a down arrow. |
| 1:08 | Q2 recap | Speed card, character, drag, weight, velocity, lens inset, "extra push" label, "zoomed in 10x", "weight length", "still moving down", the subtitle and gridded ground all at once. | SCI (everything on screen at once), ORD | Three steps that replace each other: forces on one scale with a ring → a full-frame ZOOM card where the net force points UP → back to the body with only the DOWN velocity arrow. No speed card in this shot. |

## Cross-cutting causes

1. **Artwork.** V9/V10 limbs were separate parts with round overlap caps, and the boots were drawn as open tubes. No rig setting could hide them. V11 uses whole-pose drawings instead, so the rig no longer animates individual limbs.
2. **Diagram design.** V10 added explanatory overlays without removing earlier ones. V11 enforces one idea per beat and uses dedicated cards for anything that needs magnifying.
3. **Instrument.** The device was enlarged without its wearer. In V11 it is always shown on a wrist (inset, arm shot or POV), and only the camera changes its apparent size.
4. **Terrain.** The 450 m square parcels on a regular grid read as a checkerboard from altitude. V11 uses a jittered irregular field mesh in the Codex landscape palette, with merged fields, rounded forest clumps, winding roads and crop rows at low altitude.

Before/after images: `qa/before_after/*.png`, with V10 on the left and V11 on the right.
