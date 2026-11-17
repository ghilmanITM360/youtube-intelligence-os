# Visual CT scan — d5TD3r1nLqM "Which path would the three wise men have walked?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2026-03-17T11:00:27-07:00; public views at census 361761 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Which path would the three wise men have walked？ [d5TD3r1nLqM].mp4` sha256 `4d52a0271889920ca0024330c7485d8b19789a19f891cd51988e5cb31b5f8352`, 1080x1920 h264, 24/1 (CHECK: 2045 distinct packet durations), time_base 1/12288, 2045 decoded frames, 85.264 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_d5TD3r1nLqM` (Claude Code sonnet subagent; transcript audit: 10/10 sheets opened, 10 image results, validator errors 0); primary spot-check: 1 of 10 sheets re-viewed by primary (0.6 scale), 6 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 2045 frames measured. 63 segments = 32 HOLD states (1642 frames, measured static; settled frame viewed) + 31 ACTIVITY events (403 frames; 60 viewed in tiles; 21 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 3. Unresolved segments: G0010, G0018, G0034.

## 2. Structure (OBSERVED, from ledgers)
- 11 shots (composition replacements incl. cuts back), 31 activity events: GRAPHIC/TEXT 24, CAMERA 1, CHARACTER 0, LIGHT/COLOR/EFFECT 3, SHOT_CUT 10, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_d5TD3r1nLqM/observations.md`)


**1. Premise (0-12.8s).** G0001 (0-2.5s) opens on an empty blackboard with a stick figure holding paper. G0002 (2.58s) pops on horizon arc, three tiny wise men and star dots; G0004 (5.67s) a small object on the arc; G0006 (8.08s) red solid arrow wise men -> object; G0008 (11.17s) red dashed meandering path. ASR: "followed a star to Bethlehem" (3.8-6.9s), "walk toward a known star" (7.4-10.8s), "What path would you trace" (11.3-12.6s). INFERRED: red solid = the naive path, red dashed = the question's actual path; the board bounds the question before the cut at 12.79s (G0010).

**2. Steps and anchors.** The persistent anchors are the wise men trio (G0002, G0010, G0014, G0018, G0020, G0044, G0046) and the JERUSALEM/BETHLEHEM labelled dots (G0028-G0033, G0056-G0063). Escalation: sky view (G0010) -> spiral map with scale label (G0012) -> "500 MILES" joke (G0014) -> globe with growing spiral (G0018) -> board diagram of Earth, sun and Sirius (G0020) -> conditions list (G0024) -> abstract two-dot map (G0028) -> zoomed map (G0032) -> globe (G0034). The route is drawn progressively in red across four canvases. Stick-figure host appears only in board and desk scenes (G0001-G0009, G0019-G0027, G0036-G0045).

**3. Labels vs object.** Labels mostly appear in the same frame as the object (SIRIUS G0010; HALLEY'S COMET/SUPERNOVA/METEOR G0048; date labels G0054; the Earth diagram G0020). Labels after the object: "WALKING/HALF A DAY" bracket (G0012, 23.6s), "#CAN WALK ON WATER" (G0026, 44.3s), "DEC 25" (G0058, 78.9s), "DEC X" (G0060, G0062; 81-82.4s). Red verdicts "WRONG TIME"/"TOO FAST" typed after scribbles (G0052, 67.8-68.4s).

**4. Reveal types.** Pop-on (single-frame): G0002, G0004, G0006, G0008, G0012, G0020, G0024, G0026, G0048, G0058. Write-on: red zigzag strike G0022, G0050, G0052; red path lines G0030, G0032, G0034, G0060, G0062; typed text G0052; spiral growth G0018. Scroll/camera-like: sky slide G0010. No dissolve was resolved in the tiles; fade-like changes were not seen (INFERRED: transitions are hard cuts). Text updates on PyEphem screen G0038-G0044 are swaps.

**5. Jokes and callbacks.**
- Wise men with speech bubbles "AND I WOULD WALK 500 MILES / 500 MORE", G0014 (27.2s), ASR near: "determined by how far a person can walk in half a day" (23.7-26.8s). INFERRED: song reference.
- "#CAN WALK ON WATER" red text, G0026 (44.3s); ASR: "but they can still walk on water" (43.6-45.8s).
- Red scribble strike of the Earth-crossing line, G0022 (37.75s), ASR "walk toward the star while it's behind the earth" (37.2-40.2s).
- Tight red loops over southern Africa, G0034-G0035 (50.8-52.6s); ASR "wind up circling Botswana".
- Stick figure at laptop, PyEphem rewind icon with year counter 2025 -> 250 -> ~4BC, G0036-G0045 (52.6-59.5s); ASR "PIE-FM... historical positions".
- Black-sky candidates each struck red with "WRONG TIME"/"TOO FAST", G0048-G0053 (60.7-70.1s); ASR "none of the other obvious candidates really check out".
- Four stick figures with different dates, G0054 (70.1s); ASR "debate over Jesus' date, and even year of birth".

**6. Counts (63 segments, 31 ACTIVITY).** True cuts/scene replacements: 12 (G0010 start, G0010 internal swap to spiral map [onset UNRESOLVED], G0014, G0018, G0018 internal cut to board [onset UNRESOLVED], G0028, G0032, G0034, G0036, G0046, G0054, G0056). Board content swap without cut: G0024. Camera-like motion: 1 clear (sky slide G0010, 12.8-19.5s); G0034 may be zoom-out but unresolved. Drawing animation (write-on/typing): about 11 segments. Pop-ons: about 14 segments. Many ACTIVITY segments are single frames (pop-ons or hard cuts).

**7. Characters/objects.** Stick figures: round head, line body, black ink; host with paper (G0001) and raised arm (G0019); desk figure with laptop (G0036). Wise men: tiny robed trio with crown/hats and staffs, black ink on white, white line on black (G0046-G0053). Colour: red for paths, scribbles, verdicts, SIRIUS (G0010), "#CAN WALK ON WATER", DEC labels; grey fill for Earth/landmass (G0018, G0032, G0034), Dead Sea (G0011), PyEphem dish logo (G0036); white/glow on black for the night sky (G0046-G0053). Comet has grey gradient tail, supernova has glare (more detailed than elsewhere).

**8. Unusual vs typical patterns.** No single persistent diagram; the video uses many canvases (board, sky, spiral map, globe, desk, night, figures, two-dot map). Red is used for paths, strikes and labels, not just marks. Stick figures appear in explanatory frames, not only jokes. A dark inverted-colour night scene (G0046-G0053) and a software-screen scene (G0036-G0045) appear. Black-on-grey globe uses grey fill not seen in simple diagrams. The end repeats the Jerusalem/Bethlehem map G0056-G0063 with three dashed paths, a callback to G0030.

**9. Unresolved.** G0010 onset of map swap (19.5-21.1s), G0018 onset of cut to board (34.6-35.5s), G0034 zoom vs cut (50.8s), G0004 object identity. G0002 individual element order cannot be determined (single frame); G0032/G0034 first frames show cut already complete.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.8397, #101010 0.1364, #D0D0D0 0.0094, #303030 0.0035, #505050 0.0025; mean settled dark-ink coverage 14.7% (max 99.2%); red accent present in 15/32 holds; any saturated colour in 15/32 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9666 (347/358 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
