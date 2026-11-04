# Visual CT scan — EsUBRd1O2dU "Would a Submarine Work as a Spaceship?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2024-03-05T09:00:11-08:00; public views at census 5806311 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Would a Submarine Work as a Spaceship？ [EsUBRd1O2dU].mp4` sha256 `76aaaeff0b4862151d25ec1e0adcfa5818eb87c3a6f4a6847ee6f88c184f2d65`, 1920x1080 h264, 24/1 (CHECK: 6303 distinct packet durations), time_base 1/12288, 6303 decoded frames, 262.687 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_EsUBRd1O2dU` (Claude Code sonnet subagent; transcript audit: 20/20 sheets opened, 20 image results, validator errors 0); primary spot-check: 1 of 20 sheets re-viewed by primary, 12 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 6303 frames measured. 195 segments = 98 HOLD states (6077 frames, measured static; settled frame viewed) + 97 ACTIVITY events (226 frames; 131 viewed in tiles; 83 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 228. Unresolved segments: G0008, G0146, G0150, G0180, G0182.

## 2. Structure (OBSERVED, from ledgers)
- 25 shots (composition replacements incl. cuts back), 97 activity events: GRAPHIC/TEXT 50, CAMERA 10, CHARACTER 17, LIGHT/COLOR/EFFECT 7, SHOT_CUT 24, FALSE_POSITIVE 2.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_EsUBRd1O2dU/observations.md`)


All claims are from sheet tiles (20 sheets opened). ASR is provisional text, not audio.

## 1. Premise (first ~10 s)
- OBSERVED: G0001 (0.0 s): stick figure with paper beside a blackboard reading FUN VACATION IDEA with a submarine and Earth arc. G0002 (0.42-0.67 s): grey card scales up: "Q. How long could a nuclear submarine last in orbit? - Jason Lathbuy" (ASR 0-5 s reads the same question). G0004 (5.79-6.0 s): red scribble strikes FUN VACATION IDEA (ASR "not very long"). G0006 (7.42 s): figure's hand goes to head. G0008 (9.21 s): red xkcd's what if? title card, then G0009 (11.25 s) BOOM!!! cloud, G0010 red scribble over it, G0012 (12.5 s) cut to the underwater sub. Premise is bounded by a framed blackboard, a quoted question and an immediate joke (ASR 5.8-10.9 "not for the reason I expected"; "wouldn't burst").

## 2. Reasoning steps as visuals; persistent anchors
- Persistent anchors: the submarine (nearly every scene), a black/grey background that encodes environment (grey = water G0012-G0025; black starfield = space G0026+), the title box WHY SPACE IS WARM (G0066-G0107, 64.6-125 s) with PART 1 (G0078, 76.1 s) and PART 2 (G0102, 122.6 s) sub-labels, and the blackboard+figure frame (G0001-G0007, G0140-G0143 at 174.5-177.7 s, G0190-G0193 at 243.7-252.6 s).
- Steps: pressure (G0014 50-80 ATMOSPHERES then G0018 1 ATMOSPHERE, 16.7-17.6 s), WATER-FREE ZONE (G0022, 22.9 s), AIR-FREE ZONE (G0028, 30.4 s), CO2 clouds scribbled out (G0030-G0033), electrolysis equation struck in red (G0040-G0042), then escalation: balloons "EVEN BIGGER?!" (G0044-G0048), heat lines (G0050). Heat: WARM/COLD split (G0052-G0065), SPACE/EARTH split (G0070), equation (G0080), molecules (G0082), grinder cutaway (G0086-G0095), radiating sub (G0098-G0108), 200 MEGAWATT (G0116), reactor diagram, 100 MEGAWATTS (G0124), ~0.5C/min, +30C/hour (G0132-G0134). The sub is redrawn at several levels of detail: simple, big cutaway (G0020), full-length cutaway (G0114), magnified missile tubes (G0148).

## 3. Labels relative to objects
- OBSERVED: labels appear after the object is settled (G0014 label+arrows arrive in one frame after sub hold G0013; G0116 label after cutaway hold G0115; G0158 4 m/s after plume hold G0157). Exceptions where object and label arrive together: ELECTRICITY equation in the cut G0036; title box in G0066. Equations are written on (G0080). Numeric labels in red: DeltaV ~ 100 m/s (G0162, 208.3 s), 24-4 m/s ~ 100 m/s (G0164), 100 MEGAWATTS (G0124), +30C/hour (G0134).

## 4. Reveal types
- Pop-on (one frame): most labels, arrows, speech bubbles, balloons, fan, sparks (about 50 segments, e.g. G0014, G0072, G0090, G0124, G0132, G0142).
- Write-on: equation G0080 (typed in steps); red strike scribbles G0004, G0010, G0040, G0060, G0064, G0154 (G0032 progressive); red ellipse G0150 appears complete in the sampled frame, so onset UNRESOLVED.
- Dissolve/fade: question card scale-up G0002, WATER-FREE ZONE G0022, CO2 clouds G0030, sub hatching G0098, missile to plume G0156.
- Camera: G0016 scroll up, G0070 and G0164 pan-wipe split reveals, G0140 zoom-out.

## 5. Visual jokes and callbacks (seg, PTS, nearby ASR)
- G0001-G0006 FUN VACATION IDEA struck out, 0-7.4 s ("Jason, asks...").
- G0009-G0010 BOOM!!! scribbled out, 11.25-11.75 s ("The submarine wouldn't burst").
- G0058/G0062 PEDANTIC and MORE PEDANTIC figures, G0060/G0064 WARM -> ALSO COLD -> WARM!, 56-64.5 s ("If you're pedantic... even more pedantic").
- G0084 frostbite quote bubble, 85.75 s (ASR 85.74 "doesn't make space feel warm").
- G0086-G0095 Papa Munroe's skin, 88.7-109 s (ASR "my dad use a metal grinder").
- G0110-G0112 capsule in beanie and scarf then bare, 133.7-136.8 s (ASR "isn't staying warm, it's keeping cool").
- G0118 diagram with struck "CONFIDENTIAL/RESTRICTED DATA" and REDACTED, 143.3 s (ASR "hard to get good numbers").
- G0136 DEATH BY SUBMARINE-SAUNA, 167.6 s.
- G0140-G0143 zoom out to blackboard, second figure "WHO WOULD HAVE GUESSED?", 174.5-176.7 s (ASR "a bad idea").
- G0176 "I DIDN'T KNOW SUBMARINES HAD THESE", 232.5 s, G0186 "WOW, THERE WAS A PARACHUTE TOO!", 240.3 s, G0188 KABLAM!, 242.3 s (ASR 230-243).
- G0190-G0192 blackboard callback with explosion, 243.7-249 s (ASR "disable the detonators").

## 6. Camera vs drawing vs cuts (counts are my reading)
- Hard SHOT_CUT: 21 clear (G0008, 12, 36, 52, 66, 76, 86, 92, 96, 110, 114, 118, 130, 144, 160, 166, 174, 178, 190, 194 plus G0148 with zoom). Background-only swaps without scene change: G0026, G0038, G0126, G0128.
- Camera moves: 5 clear (G0016, G0070, G0140, G0164, plus G0184 partial). Ambiguous cut-vs-zoom: G0180, G0182 (UNRESOLVED).
- Drawing/pop-on events: the large majority (~85 of 100 activity segments).
- False positives: G0068, G0146.

## 7. Characters and objects
- OBSERVED: stick figures with round heads: teacher at blackboard, bushy-hair figure, ponytail figure, helmeted double-ring-head figure, grinder worker with goggles, tiny seated and parachuting figures. Submarines and tubes drawn in high detail (cutaways with hull ribs, missile tubes). Colours: black/white/grey dominant; grey fill for water and Earth; red for strikes, heat, and key numbers; red also used for the whole title and end cards.

## 8. Contradictions to typical patterns
- No single persistent diagram: scenes are swapped about every 5-6 s (21 hard cuts in 262 s).
- Red is not only for marks: red title card G0008 and end card G0194 (full red), red heat lines G0050 and G0122, red numeric labels G0134, G0162.
- Stick figures appear in explanatory scenes (grinder G0086, electrolysis G0036) and as running commentators (pedantic figures), not only in jokes.
- Several comedic cutaways are real explanatory analogies (G0086-G0095).
- Split-screen layouts (G0052, G0070, G0164) used as comparisons.
- Opening and closing frame the whole video in the same blackboard scene (G0001, G0190).

## 9. Unresolved segments
G0008 (second cut onset between f259 and f269), G0150 (draw-on onset), G0180 and G0182 (zoom vs cut), G0146 (tiny shift or none), plus low-confidence: G0126, G0128, G0172, G0192 (partly resolved, flagged MEDIUM).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #101010 0.5253, #F0F0F0 0.3252, #D0D0D0 0.0971, #707070 0.0198, #D03030 0.0083; mean settled dark-ink coverage 56.4% (max 98.0%); red accent present in 31/98 holds; any saturated colour in 31/98 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9806 (933/950 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
