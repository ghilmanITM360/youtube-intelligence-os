# Visual CT scan — -1-ldW4kpLM "What if Earth grew 1cm every second?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2024-10-15T09:00:00-07:00; public views at census 6218558 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4` sha256 `dce7aed164da0da8979608392520c88e295185550c0d8b18950e58666a3c26b3`, 1920x1080 h264, 24/1 (CHECK: 7575 distinct packet durations), time_base 1/12288, 7575 decoded frames, 315.675 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_-1-ldW4kpLM` (Claude Code sonnet subagent; transcript audit: 23/23 sheets opened, 23 image results, validator errors 0); primary spot-check: 1 of 23 sheets re-viewed by primary (0.6 scale), 10 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 7575 frames measured. 209 segments = 105 HOLD states (6659 frames, measured static; settled frame viewed) + 104 ACTIVITY events (916 frames; 160 viewed in tiles; 87 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 235. Unresolved segments: G0006, G0012, G0018, G0080, G0176.

## 2. Structure (OBSERVED, from ledgers)
- 36 shots (composition replacements incl. cuts back), 104 activity events: GRAPHIC/TEXT 56, CAMERA 1, CHARACTER 21, LIGHT/COLOR/EFFECT 1, SHOT_CUT 35, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_-1-ldW4kpLM/observations.md`)



## 1. Premise introduction (first ~10 s)
G0001 (0-2.1s): a grey box states the question "Q. How long would it take for people to notice their weight gain..." with "Dennis O'Donnell", a large stick figure holding paper at left, and a whiteboard with a grey globe. ASR 0-10.5s reads the same question. G0002 (2.17s) pops a tiny figure on the globe; G0004 (5.92s) pops outward arrows around the globe (ASR ~4.5-8s "radius ... increased by one centimeter every second"). Premise is bounded by one fixed tableau; nothing else is added before the title card G0006 (10.67-12.67s, red "xkcd's what if? THE VIDEO SERIES"). G0007-G0011 (12.7-17.6s) redraw the board with a cutaway globe (G0008 13.79s) and arrows (G0010 14.79s) at ASR "from crust to core, starts expanding uniformly".

## 2. Reasoning steps, anchors
Escalation is a time ladder in the top banner: T = 1 SECOND (G0016, 22.75s), 2 SECONDS (inside G0018, by 25.9s), 1 DAY (by 33.5s), 1 MONTH (G0078, 107.7s), 1 YEAR (G0116, 150.0s), 5 YEARS (G0132, 165.2s), 10 YEARS (G0150, 186.1s), 40 YEARS (G0158, 202.7s), 100 YEARS (G0166, 214.9s), 300 YEARS (G0190, 277.1s). Persistent anchors: (a) the globe with a vertical divider whose right half swells with each epoch (G0116, G0132, G0150, G0158; G0134/G0152/G0158 show the grow animation) with a growing list "GRAVITY: +x%" / "RADIUS" / "MASS"; (b) the clock room (G0072, G0128) revisited with "+3 SECONDS" (G0076) then "+5 DAYS" (G0130); (c) the figure on a scale (G0022 70kg; G0096 70.28; G0122 73.6; G0136 88; G0162 210kg); (d) the black-silhouette ruin scenes (G0026, G0124, G0142, G0148). Each recurring anchor is progressively damaged by state swaps.

## 3. Labels, numbers vs objects
Labels follow their object by a beat: object cuts in, label pops in later as a separate segment: LOS ANGELES G0066 (87.67s) after car G0064; ROCHE LIMIT G0200 (296.5s) after moon/Earth; city names G0102 (135.75s) after three scales G0100; "6.28m" G0040 (63.25s) after rope scene G0036. Equations write on line by line (G0044-G0050, G0056-G0060, 66-79s) at ASR "circumference is proportional to radius ... two pi". Scale-comparison frames: landmark row vs grey ghost row G0019 (34.7s) with "+ 864 m" G0020.

## 4. Reveal types
- Pop-on: nearly all labels and objects (G0002, G0004, G0010, G0066, G0074, G0126, G0174, G0178).
- Write-on text: G0118 (21 frames), G0134, G0152 and equation lines; red strike-then-write: G0024 (42.08-42.17s), G0182, G0188.
- Cross-fade: G0052 (71.67-71.92s) fades equation out.
- Inset slide-in: G0014 (18.9-19.3s) rift clip from the right.
- State swap damage on drawn objects: G0108 viaduct, G0114 house, G0148 tower, G0164 logs.
- Camera: no clear whole-canvas pan found; see 6.

## 5. Jokes, cutaways, callbacks
- G0002/G0003 tiny person on globe (2.2s; ASR "question... weight gain").
- G0014 inset clip with red "what if?" logo, 18.9s; ASR 18.92 "avoid another drain-the-ocean scenario" (callback to another episode, INFERRED).
- G0018 dog-walker vignette (~31.5s; ASR "For the rest of the day, you wouldn't notice much of anything").
- G0064 desert car with tumbleweed, G0066 "LOS ANGELES" pin (86.2-87.7s; ASR "One of the first real effects").
- G0128 "YUP, THE EARTH IS DEFINITELY EXPANDING" (162.1s; ASR "pendulum clock now ahead by five days" nearby).
- G0136 "IT'S DEFINITELY BECAUSE THE EARTH IS EXPANDING..." with 88kg (168.1s; ASR "you'd weigh 88 now") — a repeated deadpan line.
- G0168 insect says "HI!" beside prone figure (223.58s; ASR "only small insects ... would be able to move around").
- G0174 robot with tray (236.25s; ASR "tended to by robots").
- G0206 stick figure arms raised beside ringed Earth (303.1s; ASR "the earth would ... have rings").

## 6. Camera vs animation vs cuts
Hard-cut onsets: about 42 (G0006 twice, G0016, G0018 twice, G0022, G0026, G0032, G0036, G0042, G0064, G0068, G0072, G0078, G0088, G0096, G0098, G0100, G0104, G0110, G0116, G0124, G0128, G0132, G0136, G0138, G0142, G0150, G0156, G0158, G0162, G0166, G0170, G0172, G0176 twice, G0190, G0208). Drawing animation: G0020 line grow, G0118 write-on, G0134/G0152/G0158 globe grow, G0176 long circle growth. Camera-like motion: G0070 (92.5-97.8s, ground line and tower rise while satellites stay, INFERRED to show ground expansion) and G0192 (283.5-284.9s slow drift, INFERRED). No clean pan or zoom of the whole canvas observed.

## 7. Characters, detail, colour
Stick figure: round head, line limbs, in black ink; bald main figure, black-haired second figure (G0036), tiny figures on globes. Colour: red is used for corrections, results and warnings ("70.01 kg" G0024, "~6.28" G0050, "0.01%" G0060, "+3 SECONDS" G0076, "CHANDRASEKHAR LIMIT" G0186, signal rings G0068, tidal arrows G0198, "210kg" G0162). Grey fill for globes and chart zones; black fills for silhouette scenes; white-on-black space scene (G0190-G0207); red full-frame title/end cards (G0006, G0208-G0209).

## 8. Unusual or contradicting patterns
- Not a single persistent diagram: cut roughly every 7 s.
- Red is not only for marks: red title/end cards and a red-dotted moon.
- Stick figures also serve in non-joke roles (narrator at whiteboard G0001, G0177-G0189 teacher gesturing).
- Split-screen layouts (G0098, G0100, G0156, G0166) and a technical chart G0170 break the sketch style.
- Full-frame black silhouette and space scenes show inverted palettes (G0026, G0124, G0190).

## 9. Unresolved segments
G0006 (title graphic internal frames), G0012 (board redraw: camera vs redraw), G0018 (onsets of 2 SECONDS banner and two cuts), G0080 (subtle globe/divider change), G0176 (cut and label onsets). MEDIUM: G0028, G0044, G0054, G0092, G0106, G0144, G0154, G0184, G0192, G0198, G0204.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.7792, #101010 0.1741, #D0D0D0 0.0241, #D03030 0.0077, #707070 0.0039; mean settled dark-ink coverage 19.2% (max 98.0%); red accent present in 23/105 holds; any saturated colour in 23/105 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9651 (1066/1103 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
