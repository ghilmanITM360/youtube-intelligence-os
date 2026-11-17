# RT-V2-S04 worker notes
- render.py draws one static background (seeded; sky, 2 hills, S-curve river, 3 trees, village, texture) once; every frame reuses identical pixels.
- No camera motion. Labels (Bradley Hand Bold, white + 3px dark outline) are rigid groups (word, dotted arrow, item).
- Onsets f55 "bugs", f85 "mud", f115 "rotten fish"; 5-frame left-to-right write-on.
- Drift/shrink to 0.5 scale: g1 f70-195, g2 f85-195, g3 f115-195 (smoothstep).
- Person (chest-up, eyes closed, sad) enters bottom at f140, floats up to centre, ends scale ~0.28 at f207.
- 208 frames, 1920x1080, 30000/1001, h264 yuv420p (verified with ffprobe).
- Frame 104 fraction within L1<=60 of #789838: see reply (approx 0.25).
- Item colours: mud blob #7a5230, fish grey, bugs dark dot.
