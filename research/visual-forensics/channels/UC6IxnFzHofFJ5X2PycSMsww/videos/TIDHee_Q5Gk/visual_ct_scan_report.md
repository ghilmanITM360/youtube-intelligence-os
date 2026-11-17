# Visual CT scan — TIDHee_Q5Gk "What if all visible light was a single beam?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2026-09-01T10:00:04-07:00; public views at census 4305213 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if all visible light was a single beam？ [TIDHee_Q5Gk].mp4` sha256 `fca5fe3090b154140a411458d272fd9108e53519b7fe92f2a245b5eaddc0b09d`, 1080x1920 h264, 24/1 (CHECK: 2973 distinct packet durations), time_base 1/12288, 2973 decoded frames, 123.925 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_TIDHee_Q5Gk` (Claude Code sonnet subagent; transcript audit: 11/11 sheets opened, 11 image results, validator errors 0); primary spot-check: NO primary image spot-check (validator + transcript audit only).

## 1. Coverage (MEASURED)
All 2973 frames measured. 99 segments = 50 HOLD states (2908 frames, measured static; settled frame viewed) + 49 ACTIVITY events (65 frames; 55 viewed in tiles; 46 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 9. Unresolved segments: G0038, G0040.

## 2. Structure (OBSERVED, from ledgers)
- 12 shots (composition replacements incl. cuts back), 49 activity events: GRAPHIC/TEXT 33, CAMERA 2, CHARACTER 3, LIGHT/COLOR/EFFECT 12, SHOT_CUT 11, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_TIDHee_Q5Gk/observations.md`)


**1. Premise (first ~10 s).** OBSERVED: G0001 (0-1.8 s) opens on a grey canvas with a blackboard showing SUN and 'UN-SUN-SPECTING EARTH', and a stick figure with a paper below. ASR 0-6 s: "What if all the sun's output of visible light were bundled up into a laser-like beam ... diameter of around 1 meter". G0002 (1.83-2.04 s) turns the sun's rays into a lobed beam to Earth and the label cross-fades to 'UNINHABITABLE EARTH'; G0004 (3.5 s) pops on a '1m' marker at the beam tip (matches "1 meter"). G0006 (6.54 s) hard-cuts to a black canvas with a white figure labelled DNA/FATTY ACIDS/BLOOD/MITOSIS/CELLULOSE and a beam from the left (ASR 6.5-9.5 "you would obviously die"). G0008 (7.96 s) the figure disperses into particles and scattered letters. The premise is bounded by the board diagram plus the '1m' marker; the first cut moves straight to the consequence.

**2. Reasoning as visual steps.** OBSERVED: no single persistent diagram; instead a chain of scenes. Recurring anchors: the Earth (small blackboard Earth G0001; sun/Earth pair G0014 14.9 s; limb close-up G0020 20.9 s; full globe G0034 39.7 s; half-lit globe G0046 51.9 s; small globe G0072 90.75 s; damaged Earth G0096) and the vertical beam. Escalation is built by repeated progressive growth: the plasma bubble (G0026, 24.7 s) then X-RAYS/MORE PLASMA (G0028, 26.6 s), then IR (G0030, 32.3 s) and a red/white wash (G0032, 37.3 s); the red heat arc around the globe grows in steps G0052-G0064 (59.4-78.5 s) until a full ring; the same stepwise ring recurs G0080-G0086 (103.0-103.75 s). INFERRED: step growth mirrors ASR "heat the air to millions of degrees" and "A bubble of heat and light would wrap around the Earth".

**3. Labels relative to objects.** OBSERVED: labels arrive after the object they label or with it: '~1.5·10^22 J/day' appears (G0016, 15.67 s) about 0.8 s after the Earth is on screen (ASR 14.96-19.4 "Earth receives about .004% ..."); '~3.8·10^26 J/second' and the 'VISIBLE LIGHT ... 1/2' note appear together (G0018, 18.9 s); 'MILLIONS OF DEGREES' label with the red glow (G0024, 22.2 s); 'PLASMA' with the bubble (G0026, 24.7 s); 'RIP' present at the globe cut (G0034, 39.7 s) then 'SAFE?' (G0036, 40.7 s) then red 'NOT' (G0038, 44.6 s). The 'TWILIGHT' tombstone (G0042, 49.0 s) is on screen when ASR says "Turns out, twilight" (48.4-49.5).

**4. Reveal types.** OBSERVED: pop-on (single-frame): '1m' marker G0004, energy labels G0016/G0018, SAFE? G0036, NOT G0038, three small objects G0040, red marks on scattered letters G0010, particle diagrams G0012. Stepwise write-on (arcs/rings in 4-6 equal single-frame steps about 1 s or 0.25 s apart): G0052-G0064, G0080-G0086; INFERRED these are frame-by-frame progressive reveals, not continuous sweeps. Dissolve: G0002 label cross-fade; G0098 tombstone over Earth (120.29-120.54 s, 7 frames). Camera move: only one clear pan, G0044 (49.9-50.1 s, tombstone slide left, TWILIGHT to MOONLIGHT).

**5. Jokes and callbacks.** OBSERVED: (a) G0002 pun label 'UN-SUN-SPECTING EARTH' (0-2 s, ASR "What if all the sun's output"); (b) 'FATTY ACIDS ... CELLULOSE' body-label figure vaporised, G0006/G0008 6.5-8 s, ASR "you would obviously die pretty quickly", then "stop being biology and start being physics" at G0010/G0012 where particle diagrams replace the labels (12.25-13.46 s, ASR 9.8-14.4); (c) RIP / SAFE? / NOT SAFE! with three tiny objects, G0034-G0040 (39.7-45.9 s, ASR "Earth is big enough to protect people on the other side ... still not going to make it"); (d) tombstones 'TWILIGHT' / 'MOONLIGHT' G0042-G0045 (49-51.9 s, ASR "Turns out, twilight. Or moonlight") with callback in wreckage G0088 (105.5 s, ASR "bringing on one final sunrise"); (e) closing tombstone 'WE SHOULDN'T HAVE TURNED THE SUN INTO A LASER' G0098-G0099 (120.3-123.8 s, ASR "testament to humanity's horrible ideas"), with the Earth embedded in the RIP letters.

**6. Counts (INFERRED where noted).** True hard cuts (SHOT_CUT): G0006, G0014, G0020, G0034, G0042, G0046, G0066, G0072, G0088, G0090, G0096 = 11. Camera: 1 clear (G0044) plus zoom-out within G0034. Drawing animations (stepwise arcs/rings, label pop-ons, diagrams): about 35 activity segments. Dissolves/lighting effects: about 8 (e.g. G0002, G0032, G0050, G0074, G0098).

**7. Characters and objects.** OBSERVED: stick figure with big round head, thin black line limbs, holding a paper (G0001); a larger white outline figure with arrow labels (G0006); tiny white figures on globes in G0046-G0076. Objects are detailed illustrations: shaded planet with continents (Africa, Madagascar), clouds, tombstones with texture, glowing sun. Colour: grey canvas then mostly dark/black canvas with white ink; red is used both for marks (X-RAYS text G0028, NOT G0038, marks on letters G0010) and for fills/glows (red-tinted Earth G0032 and G0066, red arc and ring, dusk sky purple/pink G0042-G0045, red wreckage G0088).

**8. Departures from typical patterns.** OBSERVED: no single persistent diagram: about 11 distinct scenes; red is also used for large glows and tinted landscapes, not only marks; the stick figure appears as the narrator at the start (G0001) not only in jokes; there is a dusk-sky colour palette (purple/pink) and darkening beyond G0014; a pan exists only for tombstones.

**9. Unresolved items.** G0038 (globe appears to shift between G0037 and G0039 — rotation? unclear); G0040 (identity of three tiny objects); G0030 ('IR' label identity; small text); G0012 (diagram labels unreadable at tile scale); G0076/G0078 (small camera or composition shift, arrow identity); G0092/G0094 (Earth motion and beam shift only partly clear); G0068 (exact debris items). Intermediate states inside single-frame activities are not sampled (duration UNRESOLVED).


## 4. Art direction (MEASURED palette)
Background exact #C8C8C8; top quantised bins #101010 0.444, #303030 0.1866, #D0D0D0 0.0954, #505050 0.0532, #707070 0.0292; mean settled dark-ink coverage 79.8% (max 98.9%); red accent present in 35/50 holds; any saturated colour in 35/50 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio None (None/None caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
