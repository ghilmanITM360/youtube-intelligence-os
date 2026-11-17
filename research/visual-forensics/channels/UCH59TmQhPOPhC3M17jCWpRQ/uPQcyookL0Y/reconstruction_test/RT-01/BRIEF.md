# Reconstruction test RT-01 (fresh worker)
You receive ONLY `SPEC_GIVEN_TO_WORKER.json` in this folder. Do not look at any other file outside this folder (no source video, no frames, no other tables).
Build a NEW ORIGINAL 4.0-second clip that implements modules M1, M3 and M5 exactly as specified:
- 1920x1080, 30000/1001 fps CFR, H.264 mp4, white-card background colour and ink colour from `canvas`.
- An original simple character of your own design (e.g. a round-headed figure drawn with PIL primitives) on the left third, with a mouth that swaps closed->open->closed per M5.
- Line 1 of original text (your own words, e.g. "Year 1350: bad news") revealed per M1 on the right two-thirds.
- Line 2 (your own words) appearing per M3 beneath line 1.
- Render with Python (PIL + numpy) and ffmpeg via: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 (has PIL, numpy, cv2). Font: any file in /System/Library/Fonts/Supplemental (e.g. Bradley Hand Bold.ttf).
Write in this folder: `render.py`, `rt01.mp4`, and `timeline.json` listing, for each module event, the exact first/last frame indices you intended (keys: M1_start,M1_end,M3_start,M3_peak,M3_settle_end,M5_swaps[list of frame indices where the new mouth first appears]) and `boxes`: {"line1":[x0,y0,x1,y1],"line2":[...],"mouth":[...],"character":[...]} as normalized 0-1 corner coordinates (each box must fully contain that element at its largest, and the mouth box must contain only the mouth).
Do not copy any existing channel's characters or wording. Final message: what you built, frames per event, any spec ambiguity you had to resolve and how.
