# Visual CT scan — 8fADp43wJwU "If all humans died, when would the last light go out?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2024-05-28T11:19:34-07:00; public views at census 10411552 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/If all humans died, when would the last light go out？ [8fADp43wJwU].mp4` sha256 `973bb97ae6717fa54d42fe3524fcc6921016a65fa23ccae4b569ea62e91f2b4b`, 1920x1080 h264, 24/1 (CHECK: 7291 distinct packet durations), time_base 1/12288, 7291 decoded frames, 303.856 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_8fADp43wJwU` (Claude Code sonnet subagent; transcript audit: 25/25 sheets opened, 25 image results, validator errors 0); primary spot-check: 1 of 25 sheets re-viewed by primary, 7 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 7291 frames measured. 223 segments = 112 HOLD states (6960 frames, measured static; settled frame viewed) + 111 ACTIVITY events (331 frames; 182 viewed in tiles; 79 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 237. Unresolved segments: G0008, G0054, G0160, G0200, G0206, G0218.

## 2. Structure (OBSERVED, from ledgers)
- 29 shots (composition replacements incl. cuts back), 111 activity events: GRAPHIC/TEXT 34, CAMERA 4, CHARACTER 5, LIGHT/COLOR/EFFECT 40, SHOT_CUT 28, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_8fADp43wJwU/observations.md`)


## 1. Premise (first ~10 s)
OBSERVED: G0001 (0-2.5 s) shows a grey box with black serif 'Q. If every human somehow simply disappeared ... last artificial light source would go out? - Alan' above a large stick figure holding paper and a small figure beside a lit lamp in a dark panel. ASR 0.0-8.7 s repeats this text. G0002-G0006 (2.5-6.5 s): ink turns red, figures dissolve to red particles, lamp glow fades off. G0008 (8.67 s) hard cut to the red 'xkcd's what if? THE VIDEO SERIES' card, then to a skyline by 10.7 s. INFERRED: question text plus a 'humans vanish, light goes out' enactment bounds the premise.

## 2. Reasoning steps as visual steps; persistent anchors
No single persistent diagram. Each candidate light source gets its own scene: coal plant (G0014, 20.7 s), control room (G0024, 30.8 s), nuclear plant (G0044, 40.9 s), 2x2 grid (G0062, 72.9 s), island hut (G0072, 78.9 s), geothermal (G0080, 92.2 s), pipe room (G0084, 99.3 s), wind (G0102, 110.1 s), dam (G0124, 138.7 s), batteries (G0132-G0148, 158-169 s), solar (G0150-G0170, 172-209 s), radioactive waste (G0186-G0221). Recurring anchors: the black silhouette plant + pylon (G0015, G0044, G0080); the five-icon strip G0172 (209.7 s) recaps survivors and eliminates them left to right (G0174-G0180, 211.3-211.8 s) until the solar panel remains; G0182 pans to add the radioactive barrel as a fifth panel. Escalation is shown by elapsed-time labels: '< 6 MONTHS' (G0076, 85.75 s), '< 3 YEARS' (G0100, 106.4 s), '11 YEARS' / '3 YEARS' / '>20 YEARS' (G0108-G0116, 121-128 s), '~4 YEARS' (G0130, 151.3 s), '~100 YEARS' (G0168, 203.1 s).

## 3. Labels and graphics relative to object
Object first, label after: pylon (G0016) and truck (G0018) before plant narration; 'SVARTSENGI ISLAND GEOTHERMAL PLANT' (G0082, 95.6 s) appears about 4 s after the plant cut (G0080); 'CHERENKOV RADIATION' (G0204, 251.96 s) after the glow (G0202, 249.5 s); 'CESIUM 137' text first (G0208) then box (G0210) then glass block (G0212). Exception: the fuel-energy chart (G0048, 49.6 s) arrives with bars and numbers already present; only '76,000,000' is typed on later (G0050, 51.0-51.4 s).

## 4. Reveal types
- Pop-on (single-frame): objects, labels, signs, warning triangles (G0032-G0040 add one triangle at a time, 36.75-37.9 s), speech labels (G0028, G0060, G0126), panels (G0110, G0114, G0152, G0154).
- Write-on: only '76,000,000' typed digit by digit (G0050).
- Dissolve/fade: figures turn red and break into particles (G0002-G0004, G0030, G0046, G0074, G0098, G0128), smoke fades (G0022, G0056), lights go out (G0010, G0064-G0070, G0174-G0180), fade to dark (G0042, G0134, G0214), label fade-ins (G0100, G0130), fill drains (G0138-G0148).
- Camera: only G0182, G0206, G0216, G0218.

## 5. Visual jokes / deadpan / callbacks (with nearby ASR)
- G0028 'UH OH...' (34.9 s), ASR 'cascading failures'.
- G0060 'MAYDAY!' from a pylon (70.5 s), ASR 'failure of the power grid'.
- G0084-G0097 worker 'OH, HAS IT BEEN 6 MONTHS ALREADY?' with blinking beacon (99.3-104 s), ASR 95-105 s 'every six months operators must change the gearbox oil'.
- G0104 video-call inset captioned 'Tom Scott' with helmeted figure (116.0 s), ASR 112-117 s 'a pain to climb'.
- G0118 status LED in a nacelle (129.67 s), ASR 129.4-132.6 s 'status LED'.
- G0126 'I DON'T ACTUALLY DO ANYTHING HERE' / G0128 'OOPS!' (142.2 s, 148.1 s), ASR 138-149 s Hoover Dam operator 'continue to run on autopilot'.
- G0132 'Eternal LIGHT Requires infinity AA Batteries (not included)' (158.1 s), ASR 157.8-162 s 'Battery powered lights'.
- G0156 sign 'RHODE ISLAND POPULATION: EVERYONE' with struck word (180.0 s), ASR 'Emergency call boxes'.
- G0166 billboard 'SPACE SUBMARINES in CINEMAS!' (200.2 s), ASR 197-205 s 'wires and circuits will eventually succumb to corrosion'.
Callbacks: red dissolving-people motif (G0004 to G0128); title-card dinosaur returns in credits (G0222).

## 6. Camera vs animation vs cuts
True hard cuts: 28 ACTIVITY segments tagged SHOT_CUT (G0008 contains two), plus G0012 half-frame panel pop. Camera motion: 4 segments (G0182 pan with blur 216.5-216.9 s; G0206 pan plus fuel-assembly reveal 253.6-254.0 s; G0216 tilt as graph enters 269.2-269.5 s; G0218 small settle, LOW). Drawing/effect animation: 40 LIGHT/COLOR/EFFECT and 34 GRAPHIC/TEXT segments; 5 CHARACTER.

## 7. Characters and objects
OBSERVED: stick figures have round head, single-line limbs, optionally helmet (G0084), hair bun (G0194), or tiny scale (G0020, G0124). Objects range from flat black silhouettes (plants, wind field, G0102) to detailed line drawings (pipe room motor, G0084; fuel assembly, G0206; watch, G0192). Colour: red is used for stick figures that disappear (G0002 onward), red battery fill (G0137, G0140), red alarm dots (G0058), and the decay curve (G0216). Other colour: cyan glow for Cherenkov light (G0202, G0214, G0220).

## 8. Unusual vs typical patterns
- Contradicts 'single persistent diagram': scene-per-source, with only the 5-panel strip recurring.
- Contradicts 'red only for marks': red also fills batteries, drawn figures, the title and credits card background (G0008, G0222), and the decay curve.
- Contradicts 'stick figures only in jokes': figures are the disintegration device across many scenes, appearing without a joke (G0030, G0046).
- Cyan glow, rain (G0170), particle dissolves and motion blur (G0182) go beyond line-drawing reveals.

## 9. Unresolved
G0008 (second cut onset between 10.25 and 10.67 s; no visible change inside the title card at tile scale), G0200 (zoom or redraw), G0206 (pan onset/duration), G0218 (extent of settle). Low confidence: G0054, G0160 (tiny details unreadable at tile scale).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.4599, #101010 0.1412, #303030 0.1075, #505050 0.0953, #D0D0D0 0.0818; mean settled dark-ink coverage 38.6% (max 100.0%); red accent present in 27/112 holds; any saturated colour in 33/112 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9797 (1109/1128 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
