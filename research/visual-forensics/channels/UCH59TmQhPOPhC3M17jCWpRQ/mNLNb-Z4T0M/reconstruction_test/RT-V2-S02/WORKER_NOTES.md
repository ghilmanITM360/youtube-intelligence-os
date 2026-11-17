# RT-V2-S02 worker notes
- Static background drawn once in render.py (cv2, seeded): pale sky + clouds, distant hills, two olive hills with ink outlines, ~2600 grass tufts, 650 ripple marks, S-curve river narrowing to horizon, 3 trees, tiny 8-roof village on horizon.
- Camera never moves; background pixels reused identically every frame (copy of one array).
- Labels "bugs", "mud", "rotten fish": Bradley Hand Bold, per-letter rotation/baseline jitter, white fill + dark outline; each group = label + dotted arrow + item (dot-bug, brown blob, grey fish), one rigid 3x-supersampled sprite.
- Appear f55/f85/f115 with 6-frame left-to-right write-on; drift up and shrink f70(or appear)-f195, smoothstep, following river centreline.
- Figure: sad chest-up person, closed eyes + tear, enters from bottom f140, floats up/shrinks, ends small right of centre at f207.
- Bounding-box overlap check across all frames: no overlaps reported.
- Unmet/caveats: hills are largely hidden under dense grass texture (hills read mainly via outlines); item sizes are tiny at end; labels are font-based (not stroke-built).
- Event frames in timeline.json. Output verified: 208 frames, 1920x1080, 30000/1001, h264 yuv420p.
