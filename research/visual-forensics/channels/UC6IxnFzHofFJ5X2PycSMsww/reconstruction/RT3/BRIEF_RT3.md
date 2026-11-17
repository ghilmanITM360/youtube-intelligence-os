# Reconstruction test RT3 — LONG-FORM STRUCTURE (fresh worker, spec-only, manual v0.4)
Read ONLY: /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT3/spec_s6.md and spec_s9.md. Open nothing else outside reconstruction/RT3; no images, no videos.
Identity (original, required): pebble narrator with dot eyes; teal accent #1F8A8A; ALL-CAPS cv2 Hershey labels; ORIGINAL series card: full-frame teal card with a simple pebble-and-question-mark emblem and the text "PEBBLE PONDERS" — no red, no stick figures, no dinosaur/satellite, no 'what if'.
Topic: "What if your shadow stayed where you left it?" — you write the beats.
Required structure (frame-exact, 24 fps, total 1440 frames = 60 s, 1920x1080):
1. Lecture frame: question card with attribution line "—A. READER" (choose typed, scaled-up, or present at frame 0) + narrator + empty board; 1-frame object pop on board.
2. Cold-open gag (1–3 events) then the series card as a hard cut, held ≈2 s (44–52 frames), starting between frame 144 and 744 (6–31 s).
3. At least 3 reasoning-step canvases after the card (hard cuts), with one persistent anchor, one write-on, one slide/pan-with-blur or dissolve, one deadpan aside, one continuous drawn growth animation (100–200 frames).
4. Final segment: full-frame teal end card with "THANKS FOR PONDERING" + three placeholder book rectangles, held exactly 240 frames to the end with no change.
Event budget per §9 (≈20–30 events/min overall; median hold 1.3–2.4 s). Objects more detailed than narrator.
Technical: Python /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python (cv2, numpy); script RT3/make_rt3.py; frames RT3/frames_tmp/ (delete after); ffmpeg libx264 yuv420p -r 24.
Outputs: RT3/RT3_animatic.mp4 and RT3/RT1_intended_timeline.csv (exact filename) columns start_frame,end_frame,device,description. Write only inside RT3. Reply 3 lines: path, ffprobe frames/duration, number of intended events.
