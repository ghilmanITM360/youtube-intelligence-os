# RT-V2-02 worker brief
You are a fresh worker. Read only SPEC_GIVEN_TO_WORKER.json in this folder.
1. Write render.py (Python 3; numpy + opencv available in the given interpreter) that renders rt.mp4 in this folder exactly per the spec (1920x1080, 30000/1001 fps, 60 frames, h264 yuv420p via ffmpeg pipe or cv2 + ffmpeg re-encode).
2. Draw an ORIGINAL procedural textured scene (seeded) as the spec requires. Implement the pan by sampling the measured cumulative progress table per frame (sub-pixel shift allowed, e.g. cv2.warpAffine with bilinear interpolation).
3. Write timeline.json with keys PAN_start, PAN_end (last moving frame), total_shift_px, method (one sentence).
4. Do not read or modify anything outside this folder. Report in under 120 words what you rendered.
Interpreter: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3
