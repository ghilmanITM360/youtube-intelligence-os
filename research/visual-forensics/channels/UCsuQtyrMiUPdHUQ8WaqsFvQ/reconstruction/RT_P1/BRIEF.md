# Reconstruction test RT_P1 - brief for a fresh worker (spec-only)
You are an animator-programmer. Build a 20-second ORIGINAL silent explainer animatic. Read ONLY /Users/ghilmankhan/YIOS-local-audits/primitive-education/reconstruction/SPEC.md and this brief. Open no other file outside reconstruction/RT_P1, and no image or video other than your own output if you choose to check it.
Topic: "Why do alarm clocks exist?" - you write the beat list (original jokes, original drawings).
Hard constraints (prove them in your timeline CSV):
- exactly 1000 frames, 1080x1920, 50 fps CFR, H.264 yuv420p (ffmpeg from PNG frames). Frame 0 must already be the #FDFDFD canvas.
- 12-16 intended visual events (each = one change of the picture). Single-frame replacement for all except one dip-to-white (count the dip-out and dip-in as two events, each spanning its frames).
- at least: 1 word-by-word text build (>=3 words), 1 red X negation, 1 literal picture of a key word, 1 dip-to-white, final joke state with no end card.
- No holds shorter than 0.6 s and none longer than 2.4 s except the final hold (<=3 s).
Technical: Python /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python (cv2, numpy, PIL if present). Draw with thick antialiased polylines with small random wobble. Script -> RT_P1/make_rt.py (editable source, deterministic seed); frames -> RT_P1/frames_tmp/ (delete after encoding).
Outputs: RT_P1/render.mp4 and RT_P1/intended_timeline.csv with columns start_frame,end_frame,device,description (start_frame = first frame showing the new state).
Write only inside /Users/ghilmankhan/YIOS-local-audits/primitive-education/reconstruction/RT_P1/. Reply with 3 lines: output path, ffprobe frames/duration, number of intended events.
