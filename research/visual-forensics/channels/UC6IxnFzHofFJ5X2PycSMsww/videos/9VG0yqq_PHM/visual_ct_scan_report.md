# Visual CT scan — 9VG0yqq_PHM "If you put a toaster in a freezer, which wins?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2026-09-15T11:23:56-07:00; public views at census 1521083 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4` sha256 `1a5c6363860a5c2c90c608602c8c9a9e3a8241238c8d75d0d4c94a16ac6016ac`, 1920x1080 h264, 24/1 (CHECK: 3893 distinct packet durations), time_base 1/12288, 3893 decoded frames, 162.261 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_9VG0yqq_PHM` (Claude Code sonnet subagent; transcript audit: 16/16 sheets opened, 17 image results, validator errors 0); primary spot-check: 1 of 16 sheets re-viewed by primary (0.6 scale), 9 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 3893 frames measured. 145 segments = 73 HOLD states (3678 frames, measured static; settled frame viewed) + 72 ACTIVITY events (215 frames; 111 viewed in tiles; 55 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 431. Unresolved segments: G0018, G0026, G0028, G0030, G0036, G0136.

## 2. Structure (OBSERVED, from ledgers)
- 10 shots (composition replacements incl. cuts back), 72 activity events: GRAPHIC/TEXT 50, CAMERA 2, CHARACTER 13, LIGHT/COLOR/EFFECT 8, SHOT_CUT 9, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_9VG0yqq_PHM/observations.md`)


All 16 sheets opened. Facts are OBSERVED from tiles; reasons are marked INFERRED. ASR is machine text, not audio.

## 1. Premise introduction (first ~10 s)
- G0001 (0.0s): empty white canvas, headphone stick figure lower-left, blank rectangular frame. G0002 (0.375s): grey box with "Q." pops on. G0004 (1.125-1.33s): attribution "— My Brother, My Brother and Me (podcast)" typed. G0006 (3.54-3.75s): question "Would a toaster still work in a freezer?" typed.
- Question text is complete by 3.75s while ASR places "still work in a freezer?" at 4.26-5.34s. INFERRED: captions lead speech, or ASR offset.
- G0008 (5.75s): frame fills with freezer cutaway and ponytail figure (ASR "Here's how they summed up", 5.78s). G0010 toaster (7.33s), G0012 bread (8.875s), G0014 bread pushed down (9.83s) track ASR "put a toaster... bread... click it down" (7.52-10.6s).
- Bounding: the Q box plus the headphone listener frame the question as a podcast quote; the blank frame is the stage for the demo.

## 2. Reasoning steps and anchors
- Anchor A: freezer/toaster tableau (G0008-G0035, 5.75-30.4s). Cutaway, toaster and ponytail figure persist; states change: heat lines (G0021), frost (G0022), charred toast (G0024), water damage (G0026), sparks and electrocution (G0032). INFERRED: this visualises the ASR dilemma "hot / cold / toaster wins / water damage / breaker".
- Anchor B: "FOR COOLING / FOR HEATING" pair (G0037-G0051, 33.5-45.4s), toaster escalates plain, steam, coils, glow, "600°C".
- Anchor C: temperature axis (G0052-G0061, 45.4-56.9s) built label by label: TOASTER COILS, ROOM TEMPERATURE, FRIDGE, FREEZER, bracket "COLD (FOR TOASTER)".
- Anchor D: fridge cutaway (G0078-G0103, 75.0-105.5s): red energy arrows, "COP ≈ 3", "E_IN", then toaster "COP ≈ 1", arrow counts grow, "~100W" and "~1000W", red glow.
- Closing arguments are new set pieces: ice cream room (G0104), Winnipeg (G0110), podcast table (G0138).

## 3. Label timing
- Labels arrive after the object they label, usually in the next ACTIVITY segment: "FOR COOLING" G0040 (34.79s) after the freezer holds from 33.5s; "FOR HEATING" G0042 (35.67s); "600°C" G0050 (43.1s) after the glow G0048; "COP ≈ 1" G0094 (91.08s) after the toaster G0088 (86.9s); "~1000W" G0100 (99.2-99.5s).
- Axis: the first label (TOASTER COILS) is already on the cut frame G0052 (45.4s); others follow at 49.4, 50.3, 51.2s (G0054, G0056, G0058), roughly in step with ASR 48.6-52.8s.
- Hold lengths between steps are short (about 1-2s), many single-frame events.

## 4. Reveal types
- POP_ON (single frame): most labels and objects, e.g. G0010, G0012, G0038, G0054, G0064, G0140.
- WRITE_ON (multi-frame): G0004, G0006 (typed text), G0050, G0060 (bracket), G0076, G0080, G0096, G0100.
- DISSOLVE / FADE: G0022 (red lines to frost), G0074, G0102, G0106 (red glow), G0112 (white to grey night).
- CAMERA: G0016 only strong move (blurred zoom, 10.9-11.25s); G0018 small drift (LOW).
- Hard cuts (SHOT_CUT): G0036 (in and out of title card), G0052, G0062, G0066, G0078, G0104, G0110, G0138, G0144; about 10 total.
- Pose swaps: G0012-G0014, G0116-G0120, G0132-G0136.

## 5. Visual jokes and callbacks
- G0032-G0034 (28.0-29.0s): ponytail figure electrocuted, grey background, caption about one circuit. ASR "circuit breaker might trip" (24.3-30.3s).
- G0062-G0064 (56.96-58.8s): figure holding smoking toaster says "IF I WANTED A BURNER I WOULD HAVE USED THE STOVE." ASR nearby: "burned a piece of toast... well above the ideal temperature" (57.1-62.8s).
- G0104-G0108 (105.5-111.3s): "THAT'S NOT HOW YOU MAKE AN ICE CREAM SANDWICH" with 600°C toaster in a -18°C room. ASR "even if the freezer were as powerful... toasting bread" (105.6-111s).
- G0122-G0132 (134.8-135.7s): eye pairs accumulate in trees, then G0134 "AWOO..." (136.7s). ASR "you'd quickly be eaten by wolves" (134.4-136.1s).
- G0140-G0142 (148.2-150.2s): "TOASTERS BEAT FREEZERS." then "BUT WOLVES BEAT TOASTERS." at the podcast table. ASR "to a toaster, all weather is cold" (147.6-150.2s); the wolves line is not in the ASR text near that point, UNRESOLVED.
- Callback: toast-holding figure reappears G0066, G0110, G0138; podcast trio (G0066, G0138) echoes the podcast premise.

## 6. Camera vs drawing animation vs cuts
- True camera: 1 clear (G0016), 1 doubtful (G0018). Hard cuts about 10. Drawing animation (write-on, pop-on, fades): remaining ~60 activity events. Many ACTIVITY segments are single frames.

## 7. Characters and objects
- Stick figures with round heads, minimal limbs; variants: headphones, ponytail, glasses/beard, chef hat, knit hat. Objects are detailed line art (fan units, ice tray, coil panel, outlet).
- Colour: red for heat, arrows, glow, title/credits card (red background); grey for frost, stains, night backgrounds (G0032 and G0112); black silhouette trees (G0110).

## 8. Unusual vs typical patterns
- Not a single persistent diagram: four anchors and several one-off scenes.
- Red is not only for marks: it is also glow/fill (G0048, G0074, G0102, G0106) and the title/credits background.
- Stick figures appear outside jokes: the listener (G0001) and ponytail figure (G0008-G0035) are explanatory.
- Whole-canvas grey tint (G0032, G0112) and a branded title card (G0036, 30.4s) are atypical.
- Intra-segment motion in G0036 and G0145 is UNRESOLVED.

## 9. Unresolved segments
G0018, G0026 (wedge identity), G0028, G0030, G0036 (also LOW-confidence G0136).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.7008, #707070 0.1459, #101010 0.0792, #B0B0B0 0.0272, #D0D0D0 0.0168; mean settled dark-ink coverage 25.1% (max 100.0%); red accent present in 35/73 holds; any saturated colour in 34/73 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio None (None/None caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
