# RT-V1-P01 worker notes
- Read only SPEC_GIVEN_TO_WORKER.json; no other files opened.
- Art drawn once on 3840x2160 canvas (stick figure, clay pot, grass tufts, grain baked in).
- Wide = INTER_AREA 2x downscale. Punch = affine on 2x canvas (scale 2.14, fixed point 627,818, cubic) then INTER_AREA to 1920x1080.
- f0-44 wide, f45-89 punch; hard cut, identical frames within each segment.
- ffprobe: h264 yuv420p 1920x1080 30000/1001, 90 frames. Viewed f44/f45: OK.
- Encoded crf 12; seed fixed (7), so render.py is reproducible.
