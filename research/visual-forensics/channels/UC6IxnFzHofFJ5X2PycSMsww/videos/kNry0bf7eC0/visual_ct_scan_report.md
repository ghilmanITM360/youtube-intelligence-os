# Visual CT scan — kNry0bf7eC0 "Could this be the last surviving human light source?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2025-07-29T10:01:02-07:00; public views at census 2363632 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Could this be the last surviving human light source？ [kNry0bf7eC0].mp4` sha256 `cb6eb61dd038a1130dc353658dcd6752f2ed171dca1051925cf635e078ca221f`, 1080x1920 h264, 24/1 (CHECK: 606 distinct packet durations), time_base 1/12288, 606 decoded frames, 25.310 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_kNry0bf7eC0` (Claude Code sonnet subagent; transcript audit: 2/2 sheets opened, 2 image results, validator errors 0); primary spot-check: 1 of 2 sheets re-viewed by primary, 7 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 606 frames measured. 17 segments = 9 HOLD states (598 frames, measured static; settled frame viewed) + 8 ACTIVITY events (8 frames; 8 viewed in tiles; 8 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 2. Unresolved segments: G0002.

## 2. Structure (OBSERVED, from ledgers)
- 3 shots (composition replacements incl. cuts back), 8 activity events: GRAPHIC/TEXT 2, CAMERA 0, CHARACTER 2, LIGHT/COLOR/EFFECT 3, SHOT_CUT 2, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_kNry0bf7eC0/observations.md`)


1. Premise (first ~10 s): G0001 (0-1.58s) opens on a grey canvas with a single solar-panel lamp post, no text, no character. ASR 0-3.3s: "Solar panels will generally last as long as the electronics are connected". Bounded by the object alone; no title or label (OBSERVED). The question is not shown visually in these tiles.
2. Reasoning steps as visuals: Degradation is shown as successive states of one anchor (the pole): clean G0003 (to 3.2s), dirt/cobweb marks G0004-G0005 (3.25s), heavy grime and pole corrosion G0006-G0007 (6.33s). ASR near 6.4s: "wires and circuits will eventually succumb to corrosion". Then a cut to a wide roadside scene G0008 (9.0s). Final anchor is the same pole in G0017 (25.2s). Escalation is by state swap, not by graph.
3. Labels: only one label, '~100 YEARS' pops on at G0010 (11.875s), after the wide scene settled (G0009) and near the ASR "continue providing power for a century" (10.66-14.4s). The label sits near the panel (INFERRED label of panel lifespan). No numbers, axes or graphs elsewhere.
4. Reveal types: pop-on label (G0010); single-frame state swaps (G0004, G0006); rain overlay appears in one frame (G0012, 15.33s); hard cuts (G0008, G0014); light/background change (G0016). No write-on observed at tile scale (sampled frames only, so a write-on within one frame is not possible given 1-frame activities).
5. Visual jokes/callbacks: A "HELP" call box on the pole (G0008 onward) and a sign at left edge with sun burst and partial text 'MAS!' (G0008-G0013) are deadpan background details (INFERRED joke; text partly cropped). Spiky round plant near road (G0008). ASR near G0014-G0016: "last surviving human light source" while a hanging lamp is shown dark in G0016/G0017 and the pole lamp lit (INFERRED callback: the solar lamp outlasts the conventional lamp). Hanging lamp has rays at G0014-G0015 and none in G0016 (OBSERVED).
6. Camera vs drawing vs cuts: 2 true cuts (G0008 9.0s, G0014 18.46s). 0 clear camera moves (G0011 framing differs from G0009/G0010 tiles; INFERRED reframing between G0010 and G0011, UNRESOLVED whether move or crop). Drawing/state changes: 3 (G0004, G0006, G0002 weak). Effects: rain (G0012) and lighting change (G0016).
7. Characters/objects: no stick figures or characters in any tile. Objects drawn in black ink with moderate detail (panel grid cells, HELP box with grille, lamp shade). Colour: greyscale only; white used for light glows, rain and the label. No red.
8. Unusual: no stick figures, no red marks, single persistent object rather than diagram; the video is a mood/time-lapse of one object. Rain, glow and vignette lighting are atmospheric effects beyond typical line-art reveals. Bright background in G0014-G0015 then dark in G0016-G0017 changes ambient light within one scene (INFERRED day to night).
9. Unresolved: G0002 (nothing visible changed; LOW). G0011 framing relative to G0010 (MEDIUM). G0016 exact onset of light cone vs background change (single frame sampled).


## 4. Art direction (MEASURED palette)
Background exact #4C4C4C; top quantised bins #505050 0.6499, #707070 0.1235, #909090 0.0504, #D0D0D0 0.049, #B0B0B0 0.0396; mean settled dark-ink coverage 83.2% (max 98.4%); red accent present in 0/9 holds; any saturated colour in 0/9 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9947 (93/93 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
