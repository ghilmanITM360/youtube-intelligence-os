# RT-V1-S01 worker notes
- render.py draws one 4550x2600 world canvas with jittered thick ink strokes + flat fills (cv2), text via PIL MarkerFelt (marker handwriting font).
- Villager: oval head, dot eyes, brown hair tuft, olive leaf skirt, stick limbs (x=760, height 810px = 75%).
- Creature: brown furry upright sloth-like beast, grey claws, hatch-shading; ~85% frame height at the end. Reads somewhat bear-like (short snout).
- Camera: smootherstep zoom f24-37, scale 1 -> 0.43, +120px drift; creature is off-screen until revealed. Warp = blur + warpAffine (bilinear).
- Events (timeline.json): bracket1 f13, label1 f14; bracket2 f38, label2 f39; villager blink f80,81,121; arm-raise swap f100,101; creature blink f140; no camera motion f52-157.
- Output verified: 158 frames, 1920x1080, 30000/1001, h264 yuv420p.
- Unmet/caveats: leaf skirt is olive green (not in palette); villager outline at final scale is ~2.5px (thinner than 4-7px); no gradients/shadows used.
