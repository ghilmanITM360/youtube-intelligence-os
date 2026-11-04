# Visual CT scan — oLoxdLfB6Gs "Why is the sky blue?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2026-04-14T10:44:48-07:00; public views at census 839948 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Why is the sky blue？ [oLoxdLfB6Gs].mp4` sha256 `ff89c7c7ea4b991d86203950df31f49a49dd9f6a3ee9c09d51b4f63ba2187079`, 1080x1920 h264, 24/1 (CHECK: 1096 distinct packet durations), time_base 1/12288, 1096 decoded frames, 45.720 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_oLoxdLfB6Gs` (Claude Code sonnet subagent; transcript audit: 8/8 sheets opened, 8 image results, validator errors 0); primary spot-check: NO primary image spot-check (validator + transcript audit only).

## 1. Coverage (MEASURED)
All 1096 frames measured. 43 segments = 22 HOLD states (988 frames, measured static; settled frame viewed) + 21 ACTIVITY events (108 frames; 50 viewed in tiles; 11 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 16. Unresolved segments: G0026.

## 2. Structure (OBSERVED, from ledgers)
- 5 shots (composition replacements incl. cuts back), 21 activity events: GRAPHIC/TEXT 14, CAMERA 0, CHARACTER 3, LIGHT/COLOR/EFFECT 7, SHOT_CUT 4, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_oLoxdLfB6Gs/observations.md`)


1. Premise. The video opens (G0001, 0.0-0.125 s) on a bare canvas with sun and stick figure only. ASR 0.0-3.7: "why is the sky blue?" A Rayleigh chart is written on at G0002 (0.17-0.96 s) titled RAYLEIGH SCATTERING, then G0004 (2.67-2.88 s) fades in a blue sky gradient, yellow sun and the text "WHY IS THE SKY BLUE?" beside the sun. The question text is therefore on screen from ~2.9 s, after the chart. ASR 4.18 "This is sort of true" coincides with a figure arm pose swap (G0006, 4.08 s) (INFERRED link).

2. Steps as visuals. Sun (upper-left), title and figure (lower-right) persist through G0001-G0017 (0-13.8 s) as anchors. The chart is replaced by a beam diagram at a hard cut (G0008, 5.33 s; ASR "Bluer light scatters more..."). The diagram then escalates by pop-ons: red arrows (G0010, 6.96 s), yellow glow (G0012, 7.71 s), a dense multi-ray set (G0014, 9.42 s). Each step is one frame; no gradual build. Scene 2 (G0018-G0023, 13.8-21.3 s) is black space with Earth and a helmeted figure; labels accumulate (G0020, 16.75-17.54 s). Scene 3 (G0024-G0037, 21.3-39.3 s) is the statue: line art, green fill, COPPER label, brown statue, Cu to Cu2CO3(OH)2 reaction, footnote, then an absorption chart replacing the reaction (G0036, 34.9 s). Scene 4 (G0038-G0043) returns to figure plus text. Persistent anchors: the title text and cropped figure in scene 3; the two statues in scene 3; the sun/figure in scene 1.

3. Labels vs objects. Labels follow or accompany their object: chart title typed after axes and curve (G0002); COPPER label typed after the statue is complete (G0028, 25.9-26.1 s; ASR 25.16 "outside of the statue is copper"); Cu circle with the brown statue (G0030); product circle and reagents after (G0032, 27.8-28.0). Space labels (G0020) come after Earth is shown for ~2.7 s; the AIR label (G0018-G0019) is on the cut frame itself, i.e. simultaneous with the object, and is removed at G0020.

4. Reveal types. Write-on/typed: chart axes and curve (G0002), title letters (G0002, G0028 'COPI'), space labels (G0020 'RAYL','REL'). Pop-on in one frame: beam diagram elements (G0010, G0012, G0014), absorption chart (G0036). Fade/dissolve: sky gradient (G0004, G0040, G0042), Cu statue/circle (G0030), reaction (G0032), footnote (G0034), end text (G0040, G0042). Colour fill spread: statue green (G0026). No camera moves seen.

5. Jokes/callbacks. (a) G0006/G0016/G0022 arm and shrug pose swaps on the figure, deadpan, at 4.08 s, 11.29 s, 18.33 s; nearby ASR "This is sort of true.", "because air is blue", "everything appears the color it is" (INFERRED link only for timing). (b) Space scene G0018-G0023: helmeted figure floating beside Earth with label AIR, ASR 11.02-15.12 "a better answer ... because air is blue". (c) Closing callback G0038-G0043: same bare-figure layout as G0001 with the answer text, ASR 37.5-44.2 "the sky is blue because the sky is made of air, and air is blue" - the text restates the premise as a deadpan tautology.

6. Counts. True shot cuts (whole composition replaced): G0008, G0018, G0024, G0038 = 4 (peak_cf 0.58, 0.98, 0.99, 0.20). Camera moves: 0 observed. Drawing/animation events: write-on G0002, G0020, G0028; pop-on G0010, G0012, G0014, G0036; fades G0004, G0030, G0032, G0034, G0040, G0042; pose swaps G0006, G0016, G0022. G0026 statue growth is partly UNRESOLVED (appears to scale/rise, could be a camera-like zoom of the statue only).

7. Characters/objects. Stick figure: round head, single-line body, black ink; in space the figure is white ink with a double-ring helmet. Detailed objects: sun with rays, Earth globe with continents (green/blue/dark rim), Statue of Liberty line art with shading, filled mint green then brown-red copy. Colour is used widely: purple scatter arrows and curve, red arrows, yellow glow, blue sky, green and brown-red statues and curves.

8. Unusual. Red is not only for marks here: red arrows are rays (G0010) but also the brown-red copper fill. Stick figure is a narrator/bystander, not only in jokes. Backgrounds change (white, blue gradient, black space), so there is not one persistent diagram; four distinct scenes. Statue is a rich illustration rather than stick-figure style. Heavy speckle texture on sky background.

9. Unresolved: G0020 (exact order of the last two labels and when AIR disappears; sampled sparsely), G0026 (mechanism of statue appearance), G0006/G0016/G0022 (pose differences read only from hold neighbours; single frame onset), G0034 (footnote text small).


## 4. Art direction (MEASURED palette)
Background exact #FDFDFD; top quantised bins #F0F0F0 0.7328, #101010 0.1419, #B0D0F0 0.0203, #D0F0F0 0.02, #D0D0F0 0.0146; mean settled dark-ink coverage 15.9% (max 90.3%); red accent present in 8/22 holds; any saturated colour in 18/22 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9854 (169/170 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
