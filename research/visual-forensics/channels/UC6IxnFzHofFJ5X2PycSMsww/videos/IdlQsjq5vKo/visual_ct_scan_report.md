# Visual CT scan — IdlQsjq5vKo "What if you made a jetpack using rifles?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2026-02-10T11:41:12-08:00; public views at census 1668698 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4` sha256 `3961fc65194672d670462cee63a3987e11f4b3f37432ac9115deeb4a457ebbba`, 1920x1080 h264, 24/1 (CHECK: 6666 distinct packet durations), time_base 1/12288, 6666 decoded frames, 277.804 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_IdlQsjq5vKo` (Claude Code sonnet subagent; transcript audit: 24/24 sheets opened, 25 image results, validator errors 0); primary spot-check: 1 sheet re-viewed by primary, 8 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 6666 frames measured. 209 segments = 105 HOLD states (5933 frames, measured static; settled frame viewed) + 104 ACTIVITY events (733 frames; 172 viewed in tiles; 86 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 194. Unresolved segments: G0008, G0022, G0078, G0132, G0143, G0144, G0146, G0172, G0202.

## 2. Structure (OBSERVED, from ledgers)
- 25 shots (composition replacements incl. cuts back), 104 activity events: GRAPHIC/TEXT 67, CAMERA 1, CHARACTER 26, LIGHT/COLOR/EFFECT 3, SHOT_CUT 24, FALSE_POSITIVE 2.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_IdlQsjq5vKo/observations.md`)


ASR is machine text, not audio. Facts are OBSERVED from tiles; reasons are INFERRED.

## 1. Premise (first ~10 s)
- G0001 (0.0 s): white canvas, left stick figure holding paper, empty outlined rectangle.
- G0002 (0.21-0.5 s): grey card scales up from a speck to "Q. Is it possible to build a jetpack using downward firing rifles? -Rob B" (ASR 0-4.8 s "This question comes from Rob...").
- G0004 (1.9 s): tiny rider strapped to a downward rifle pops into the rectangle (answer preview). G0006 (5.3 s): left figure tilts head to read (ASR "surprised to find that the answer was yes").
- G0008 (7.9-9.9 s): red "xkcd's what if? THE VIDEO SERIES" title card, then cut. INFERRED: the card bounds the premise.

## 2. Reasoning steps and anchors
- No single persistent diagram. Each step is a new white canvas (hard cut) built up by pop-ons, then cut.
- Numbered/titled steps: G0016 "1) CAN IT LIFT ITS OWN WEIGHT?" (16.9 s); "JETPACK PLANS" panel (G0082, 95.7 s); graph (G0102, 125.8 s); FUEL/AMMUNITION (G0116-G0118).
- Persistent anchor within a step: the lone vertical rifle, which recurs (G0016, G0058, G0084, G0114) and is re-annotated: red arrows 10 lbs / 8 lbs (G0018-G0020), 15 lbs thrust (G0066), +30% (G0068).
- Escalation by state swap: 1 rifle + squirrel (G0090), 2 rifles (G0092), 30/40/60 rifle platforms with relabelled equation and more tilt (G0096-G0100), then graph (G0104), then >300 rifle rig (G0134-G0142), then GAU-8 / A-10 / car / GSh-6-30 (G0145-G0208).

## 3. Labels relative to objects
Objects appear first, labels follow in later pops: Saturn V then THRUST (G0026), WEIGHT (G0028), fraction (G0030), <1 (G0032), ~1.5 (G0038). Rifle then 10 lbs, 8 lbs. Equations grow one factor at a time (G0060-G0066, 61-68 s; ASR 63.8-69.6 s). Graph axes are written before the curve (G0102, G0104). Exception: G0172 shows labels and speech in the first sample of the cut (onset unresolved).

## 4. Reveal types
- Pop-on (instant) for most labels, arrows, speech: majority of ~70 ACTIVITY rows.
- Write-on: axis text typing and ticks (G0102), S-curve with following label (G0104), grey dashed asymptote (G0106), "ALONE" typed (G0108), red underlines on quote (G0184-G0190, 246-255 s).
- Scale-up: Q card (G0002).
- Cross-dissolve/ghosting: small rocket (G0036, 36.0 s), Saturn V (G0040, 39.6 s), vibration ghost (G0180).
- Scroll/camera: only G0182 (245.9-246.25 s).

## 5. Jokes and callbacks (seg, PTS, nearby ASR)
- G0022 (23.3-26.1 s) "190 lbs" rewrite over "10 lbs" after rider attached ("lift itself plus a person").
- G0046 (47.0 s) red "DEFINITELY DO NOT TRY THIS AT HOME. OR ANYWHERE." with remote-holding figure ("remotely fired it").
- G0074-G0080 (85-91 s) "DEAD WEIGHT"/"MORE DEAD WEIGHT" and sign "DON'T TRY AT HOME!" ("complete lack of regard for the safety of anyone below"). G0078 lower-left head-with-triangle object UNRESOLVED.
- G0090 (103.6 s) squirrel with 5 lbs ("can't lift much more than a squirrel").
- G0094 (112.1 s) "YES, ALL OF THEM." ("At this point it's clear where we're headed").
- G0116-G0118 (140-141.6 s) "FUEL" then red "AMMUNITION" ("Fuel. I mean, ammunition.").
- G0164-G0168 (215-219 s) car on gun, police "DO YOU KNOW WHY I PULLED YOU OVER?" / "NO." (speed-limit ASR, 214-221 s).
- G0172 (225.8 s) "THIS BAD BOY HAS A THRUST-WEIGHT RATIO OF 30".
- G0192 (255.9 s) "AND BY 'OVERHEATING' THEY MEAN 'MELTING THE CANNON'".
- G0206 (265.2 s) "IT'S A BIRD! IT'S A PLANE! IT'S A GSh-6-30!" with BROAD PEAK sign (ASR "jump over mountains").

## 6. Camera vs drawing vs cuts
- True hard cuts: about 22 confirmed ACTIVITY rows with SHOT_CUT (G0008, 16, 24, 42, 50, 58, 72, 82, 96, 102, 114, 124, 130, 152, 162, 170, 172, 174, 178, 194, 204, 208), plus likely cuts inside G0008 (exit), G0132 (end) and G0144 (end).
- Camera move: one, G0182 SCROLL_UP with panel entering (~0.35 s).
- No long continuous camera moves or flight sequences. Object animation inside a static frame is limited to: G0132 rifle sliding off bottom (~2.4 s, 156.5-158.8 s), G0142 rig rising with fixed ground (173.75-175.9 s), G0144 rig lowering with spike marks (181-185 s), G0022 muzzle flash then rider (~2.9 s). Flight otherwise appears as separate static scenes (G0170, G0174, G0194, G0204) and pose/state swaps.

## 7. Characters and objects
Stick figures with round heads and thin limbs; riders strapped to rifles; goggled rider on platform (G0096); police officer cap; hatted rider (G0022). Rifles, rockets, cartridge, GAU-8, A-10, MiG, cars drawn in detailed black line art. Colour: red for arrows/measure labels and warnings (G0010, G0018, G0150, G0154, G0176, G0184-G0190); grey fill for planes (G0152, G0178), ammo pile (G0120), dashed asymptote and "ALONE" (G0106-G0108); red full-screen cards for title and credits (G0008, G0208). Mountain scene (G0204) uses grey shading. The quoted-text panel (G0182+) uses a different serif/sans small typeface than the hand lettering.

## 8. Unusual vs typical patterns
- Contradicts "single persistent diagram": 22+ distinct scenes.
- Red is not only for marks: also whole title/end cards and the word AMMUNITION.
- Stick figures are not only in jokes; rider figures are part of the argument (G0072, G0096).
- Graph (G0102-G0113) is the only chart; it is built by write-on, not pop-on.
- Large embedded real-text quote with red underline write-ons (G0182-G0190) is a distinct reveal mode.
- Grey is a semantic colour for secondary/"real world" things (aircraft).

## 9. Unresolved segments
G0008 (exit cut onset), G0022 (rider/strike onset), G0078 (object identity), G0092 (squirrel count), G0132 (transition to wide scene), G0143 (hold drift 6420 px cause), G0144 (cut onset), G0146 (possible false positive), G0172 (speech timing), G0202 (minor change).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.9271, #101010 0.0249, #D0D0D0 0.0184, #B0B0B0 0.0097, #D03030 0.0079; mean settled dark-ink coverage 4.1% (max 94.3%); red accent present in 42/105 holds; any saturated colour in 41/105 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9691 (1034/1063 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
