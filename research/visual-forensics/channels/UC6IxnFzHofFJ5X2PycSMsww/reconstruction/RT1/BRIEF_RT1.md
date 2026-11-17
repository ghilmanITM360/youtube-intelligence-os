# Reconstruction test RT1 — brief for a fresh worker (spec-only)

You are an animator-programmer. Build a 24-second ORIGINAL silent explainer animatic from a written production spec. You have NOT seen the reference channel and must not look for it: read ONLY these files:
- /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT1/spec_s6.md (motion vocabulary with frame counts)
- /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT1/spec_s9.md (original-production spec)
Do not open any other file outside reconstruction/RT1, any image, or any video. Do not use stick figures, red accent, or the series title-card look — §9 requires a NEW identity: pebble-shaped narrator with dot eyes, teal accent #1F8A8A, rounded monoline lettering (use cv2.FONT_HERSHEY_SIMPLEX or DUPLEX, thick ≈2–3 px, ALL CAPS for labels).

## Beat list (original topic: "What if your coffee never cooled down?")
1. 0–3 s: Question card (grey rounded box, top) "Q. WHAT IF YOUR COFFEE NEVER COOLED DOWN?" — write-on letter group by group over ~10 frames; pebble narrator left beside an empty framed board.
2. 3–6 s: Mug pops onto the board in 1 frame; steam lines write on (≈8 frames); label "85°C" pops 1 frame after.
3. 6–10 s: Hard cut to new canvas: a timeline anchor bar at top "T = 0 MIN" that persists; mug at centre; label swaps "T = 10 MIN" then "T = 1 HOUR" as 1-frame state swaps; teal strike-through write-on over "COOLS TO 40°C" (≈8 frames).
4. 10–14 s: Escalation: hard cut to dark canvas (near-black background, white line art): mug glowing (teal radial glow); label "STILL 85°C" pops; pebble narrator aside text "NICE." pops.
5. 14–18 s: Slide/pan with motion blur (≈8 frames) to the right revealing a desk with many mugs (pop on in 3 groups, 1 frame each); persistent anchor bar now "T = 1 YEAR".
6. 18–21 s: Cross-dissolve (≈6 frames) to a zoom-out world view: Earth outline with tiny mug, label "THE WARMEST MUG IN THE SOLAR SYSTEM".
7. 21–24 s: Payoff: hard cut to pebble narrator holding mug, aside "I'LL JUST WAIT." pops; hold to the end.
Holds between events: mostly 1.5–2.5 s. Most changes must be 1-frame pops/swaps; multi-frame devices only where the beat says.

## Technical
- 1920x1080, 24 fps CFR, exactly 576 frames, H.264 (write frames with cv2 then encode with `ffmpeg -framerate 24 -i ... -c:v libx264 -pix_fmt yuv420p -r 24`), off-white canvas #F7F7F7 except beat 4.
- Python: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python (has cv2 5.0 and numpy). Write your script to reconstruction/RT1/make_rt1.py and frames to reconstruction/RT1/frames_tmp/ (delete frames_tmp after encoding).
- Output: reconstruction/RT1/RT1_animatic.mp4 and reconstruction/RT1/RT1_intended_timeline.csv with columns `start_frame,end_frame,device,description` listing every intended event (the evaluator will compare measured events to this).
- Write only inside /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT1/. Reply with 3 lines: output path, frame count/duration from ffprobe, number of intended events.
