# Visual CT scan — _efsqO-4OoQ "Could We Harvest Power From Lightning?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2025-07-15T10:00:58-07:00; public views at census 1629644 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Could We Harvest Power From Lightning？ [_efsqO-4OoQ].mp4` sha256 `3f3f2e4ef121b0ce610fc7978c1121636197e267cf74218c2e009af562b1c996`, 1080x1920 h264, 24/1 (CHECK: 1164 distinct packet durations), time_base 1/12288, 1164 decoded frames, 48.553 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1__efsqO-4OoQ` (Claude Code sonnet subagent; transcript audit: 6/6 sheets opened, 6 image results, validator errors 0); primary spot-check: 1 of 6 sheets re-viewed by primary, 9 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 1164 frames measured. 45 segments = 23 HOLD states (1120 frames, measured static; settled frame viewed) + 22 ACTIVITY events (44 frames; 30 viewed in tiles; 17 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 5. Unresolved segments: G0035.

## 2. Structure (OBSERVED, from ledgers)
- 8 shots (composition replacements incl. cuts back), 22 activity events: GRAPHIC/TEXT 8, CAMERA 0, CHARACTER 0, LIGHT/COLOR/EFFECT 8, SHOT_CUT 7, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1__efsqO-4OoQ/observations.md`)


Total duration about 48.5 s; portrait frame. ASR is provisional text, not audio.

## 1. Premise (first ~10 s)
OBSERVED: G0001 (0-4.9 s) opens on a grey canvas: stick figure holding a tall rod, cable to a lightning-symbol box and a monitor. G0002 (4.92 s) pops on a thought bubble: bolt sketch = three bolt symbols (ASR 0.0-8.3 s: "People often wonder whether we could harvest electrical power from lightning... After all, lightning is electricity"). G0004 (11.125 s) adds red scribble over the bolt symbols (ASR "The problem is, a lightning strike is over so fast"). G0006 (14.58 s) a big white bolt hits the monitor box. INFERRED: the figure is the "harvester" and the red scribble is the first bound on the premise.

## 2. Reasoning steps as visual steps
Each step is a separate scene: setup figure (G0001-G0007), house energy scale (G0008-G0013), Empire State Building (G0014-G0017), house again at x100 (G0018-G0027), world map (G0028-G0031), sun vs lightning (G0032-G0035), landscape (G0036-G0041), turbine punchline (G0042-G0045). Persistent anchors: the house scene recurs (G0008 17.08 s, G0018 25.67 s) as the unit of comparison; the sun symbol recurs (G0032 to G0041). There is no single persistent diagram, axis or ruler. Escalation x1 -> x100 is done by label change "1 -> 2 DAYS" to "100 -> 200 DAYS" plus cutaway to the building (INFERRED).

## 3. Labels relative to objects
Text lands after the object is on canvas: "1⚡ → 2 DAYS" pops at G0012 (20.42 s) after the lit house is held (G0011); ASR "enough energy to power a residential house for about two days". "100⚡ → 200 DAYS" arrives with the house cut-in at G0018 (25.67 s), the only label arriving with its scene. Red circles on the map at G0030 (30.46 s) after the map is held 28.5-30.4 s (ASR names Florida and Eastern Congo at ~28.7-31.7 s). "1,000,000 : 1" appears at G0034 (36.04 s) at the end of ASR "by a factor of a million". "TORNADO FOOD" arrives G0044 (45.42 s) after turbine hold, ASR "kinda like building a wind turbine powered by tornadoes" at 41-45 s. "TURBINE" label is present from the turbine cut (G0042).

## 4. Reveal types
- Hard cuts / scene swaps: G0008, G0014, G0018, G0028, G0032, G0042 (6 hard cuts, each a single frame).
- Pop-on single-frame: thought bubble G0002, red scribble G0004, bolt G0006, bolt G0016, labels G0012/G0034/G0044, red circles G0030, small bolt G0038, arrows G0040 (MEDIUM: pop vs short fade not resolvable from sampled tiles).
- Multi-frame light flicker: G0020, G0022, G0024, G0026 (lights and BZZZ/WHIRR labels fade on/off, 26.25-27.96 s).
- Dissolve/scene transition: G0036 (38.46-38.67 s, 6 frames; split panels dissolve into landscape).
- Write-on: none confirmed; red scribble G0004 appears in one frame.

## 5. Jokes, cutaways, callbacks
- G0006 14.58 s: the lightning destroys the figure's monitor (ASR "very hard to get lightning to strike where you want it").
- G0020-G0027 26.25-28.46 s: house lights flicker and die (ASR "wouldn't be able to keep a house running on lightning power alone") - callback to G0010 BZZZ/WHIRR house.
- G0014-G0017 22.1-25.6 s: Empire State Building struck (ASR "even the Empire State Building, ... struck by lightning about 100 times").
- G0042-G0045 42.7-48.5 s: turbine and stick figure scattering "TORNADO FOOD" (ASR "building a wind turbine powered by tornadoes"; "Impractical" at 45.6 s). Closing deadpun, sole use of xkcd-style label-and-arrow text.
- G0012 footnote in grey on ground band (unreadable at tile scale).

## 6. Camera vs animation vs cuts
True cuts: 6 (G0008, G0014, G0018, G0028, G0032, G0042); plus G0036 dissolve. Camera motion: none confirmed. G0035 shows the sun/lightning split shifted up relative to G0034, and the ground band changes in G0036 (hill and sea, dissolving) - UNRESOLVED whether this is a camera scroll or a re-layout; no mid-frames sampled. Drawing/state animation: G0010, G0020-G0026 lights, G0030 circles, G0038 bolt.

## 7. Characters/objects
Stick figure only in G0001-G0007 and G0042-G0045 (circle head, line body, thin limbs, black ink; matches xkcd style). House, building, sun, clouds and map are more detailed line art with grey shading, soft blur and glow (white glow on lit windows). Colour: red only in G0004 scribble and G0030 map circles (marks); otherwise greyscale. Backgrounds vary: grey gradient (setup), dark grey (house), mid grey (building), off-white (map, sun, turbine).

## 8. Unusual vs typical patterns
- Not a single persistent diagram: the video is a chain of distinct full-canvas scenes.
- Red is used for marks only (confirmed).
- Stick figures appear in the intro and the final joke only (not only in jokes).
- Dark-mode scenes with photoreal glow and blur (house, lightning, clouds) deviate from flat xkcd line art.
- Lightning is rendered as a bright white photographic-style bolt, not line art.

## 9. UNRESOLVED
G0004 (scribble text unreadable), G0020, G0022, G0024, G0026 (flicker onset between sampled frames), G0035 (camera or re-layout shift), G0036 (cut vs dissolve vs camera), G0040 (arrow reveal mode), G0012 footnote text.


## 4. Art direction (MEASURED palette)
Background exact #C6C6C6; top quantised bins #F0F0F0 0.2562, #505050 0.2077, #303030 0.147, #101010 0.0943, #707070 0.0896; mean settled dark-ink coverage 53.9% (max 99.6%); red accent present in 3/23 holds; any saturated colour in 2/23 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9838 (182/184 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
