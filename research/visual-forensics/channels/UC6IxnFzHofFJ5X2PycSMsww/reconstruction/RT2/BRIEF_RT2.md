# Reconstruction test RT2 — brief for a fresh worker (spec-only, manual v0.3)

You are an animator-programmer. Build a 24-second ORIGINAL silent explainer animatic from a written spec. Read ONLY:
- /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT2/spec_s6.md
- /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT2/spec_s9.md (note its v0.3 hard constraints: event budget, detail contrast)
Open no other file outside reconstruction/RT2, no image, no video. Identity (original, required): pebble-shaped narrator with dot eyes, teal accent #1F8A8A, ALL-CAPS labels in cv2 Hershey fonts. No stick figures, no red, no series title card.

## Topic: "What if every elevator in a city stopped at once?" — YOU write the beat list
Constraints you must satisfy and prove in your timeline CSV:
- 8–12 intended visual events total in 576 frames; median gap between consecutive events 1.5–2.4 s.
- At least: 1 question card, 1 persistent anchor (e.g., counter banner), ≥2 hard cuts to new canvases, 1 write-on (6–10 f), 1 slide/pan with blur (≈8 f) OR cross-dissolve (≈6 f), 1 deadpan narrator aside, everything else 1-frame pops/swaps.
- Objects (elevator cars, buildings, cables) drawn with visibly more internal detail (panels, hatching, buttons, cables) than the minimal narrator.

## Technical
1920x1080, 24 fps CFR, exactly 576 frames, H.264 yuv420p via ffmpeg from frames; off-white #F7F7F7 canvas.
Python: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python (cv2, numpy). Script → RT2/make_rt2.py; frames → RT2/frames_tmp/ (delete after encoding).
Outputs: RT2/RT2_animatic.mp4 and RT2/RT1_intended_timeline.csv (keep this exact filename) with columns `start_frame,end_frame,device,description`.
Write only inside /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT2/. Reply with 3 lines: output path, ffprobe frames/duration, number of intended events.
