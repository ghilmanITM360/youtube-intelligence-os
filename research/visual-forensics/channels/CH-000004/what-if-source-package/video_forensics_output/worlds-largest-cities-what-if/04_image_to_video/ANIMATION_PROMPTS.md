# Animation Prompts

## Compliance note (read first)
Every observed motion in this video is either (a) a camera crop moving across a static painted image (E01/IMG02), or (b) a static overlay/text popping on and holding. There is no observed independent motion of any drawn element — no character movement, no water/cloud animation, no object travel. Per rule 28 (static scenes) and rule 22 (I2V motion should be reserved for real change-through-time), generating genuine I2V clips for the map pans would manufacture motion detail (drift risk) the source never asked for. **ANIMATION REQUIRED: NO for every S02 camera move — reconstruct them as crop/position keyframes on the still IMG02 master plate during final assembly (identical technique to the CapCut build's E01 keyframes), not as generative I2V passes.** This is the correct lazy-and-faithful call, not a shortcut around a real requirement.

The only place a generative I2V pass is defensible is the single whip-zoom-blur cut into the map (A02), and even that is optional — a plain blur-transition effect in the assembly tool achieves the same observed result with zero drift risk.

## A02 (optional — transition effect, not required)
- SHOT ID: S01→S02
- SOURCE IMAGE: IMG01b (two-globe board state)
- SOURCE STATE: F01.1
- TARGET STATE: F02.0
- CLIP DURATION: ~0.6s
- MOVING ELEMENT: camera only (whole-frame push)
- STATIC ANCHORS: none (full-frame transition)
- ANIMATION PROMPT (≤500 chars): "Fast camera push forward into the scene with heavy directional motion blur, as if rushing toward the blackboard. Hold for the first 0.1s, then blur and accelerate for 0.4s, ending fully blurred. No new objects appear. Keep the illustration style and line weight identical throughout."
- FIDELITY RISK: If your I2V tool invents new geometry mid-blur (common drift), skip this and use a plain editor blur/zoom transition instead — it's the safer, equally faithful option.

## All S02 camera moves (A03–A10): NO ANIMATION PROMPT NEEDED
Build these as crop/position/scale keyframes on the static IMG02 plate in final assembly:
| ID | Behavior | Duration | Notes |
|---|---|---|---|
| A03 | fast blurred pan | ~0.5s | add a brief motion-blur/speed-ramp effect over the crop-move to sell the "fast burst" look |
| A04 | fast blurred pan | ~0.5s | same |
| A05 | fast blurred pan | ~0.5s | same |
| A06 | fast blurred pan | ~0.5s | same |
| A07 | fast blurred push-in | ~0.5s | same, tighter scale target |
| A08 | slow unblurred pan | ~17s | the one exception — animate as a smooth linear/eased crop move, no blur effect |
| A09 | fast blurred pan | ~0.5s | same as A03–A07 |
| A10 | fast blurred pan | ~0.5s | same |

## Reveals (R01, R02, R04, R05, R06): NO ANIMATION PROMPT NEEDED
G02 city pins, G03 red circle, G04 and G05 stickers are all static pop-ins/holds — add as overlay images/text with a simple opacity fade (or hard cut-in, per OBSERVED — the exact fade-vs-cut style could not be isolated at 1fps sampling) in final assembly. Generating these via I2V would be pure drift risk for zero benefit.
