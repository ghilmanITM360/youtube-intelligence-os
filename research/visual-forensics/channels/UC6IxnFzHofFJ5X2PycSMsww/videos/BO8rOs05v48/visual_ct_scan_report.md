# Visual CT scan — BO8rOs05v48 "What would a rainbow be like on Tatooine?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2026-07-07T10:03:59-07:00; public views at census 690339 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What would a rainbow be like on Tatooine？ [BO8rOs05v48].mp4` sha256 `dc2a7b1b84e8af857d040176c34ad23b8946f00810b7d195a72c48f35e1de462`, 1920x1080 h264, 24/1 (CHECK: 3981 distinct packet durations), time_base 1/12288, 3981 decoded frames, 165.930 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_BO8rOs05v48` (Claude Code sonnet subagent; transcript audit: 18/18 sheets opened, 33 image results, validator errors 0); primary spot-check: 1 of 18 sheets re-viewed by primary (0.6 scale), 9 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 3981 frames measured. 171 segments = 86 HOLD states (3717 frames, measured static; settled frame viewed) + 85 ACTIVITY events (264 frames; 120 viewed in tiles; 70 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 164. Unresolved segments: G0014, G0038, G0050, G0052, G0056, G0058, G0083, G0092.

## 2. Structure (OBSERVED, from ledgers)
- 12 shots (composition replacements incl. cuts back), 85 activity events: GRAPHIC/TEXT 73, CAMERA 1, CHARACTER 4, LIGHT/COLOR/EFFECT 6, SHOT_CUT 12, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_BO8rOs05v48/observations.md`)


1. Premise. G0001 (0-1.96s) shows grey quote box "Q. Since rainbows ... two suns like Tatooine? - Raga" (persists to G0013, 12.2s), large stick figure holding paper, empty board. ASR: "This question comes from Raga". G0002 (2.0s) pops on sun, ray, droplet, beam; G0004 (6.25s, ASR "two suns like Tatooine") adds second sun and beam; G0006 (7.17s) fills board tan with Tatooine silhouette; G0008 (8.4s) removes droplet; G0010 (9.2s) / G0012 (11.1s) add rainbow arcs and faint outer arcs (ASR "double rainbows ... quadruple"). The board frames the premise as a picture-in-picture.

2. Reasoning as visual steps. Sequence of sub-topics, each a new canvas: title card (G0014, 12.25s); Earth double-rainbow landscape with labels (G0014-G0027); numbered droplets 1-4 (G0028-G0035, 23-31s); ring labels FIRST..FIFTH (G0036-G0047, 31-38s); board scene with converging arcs (G0048-G0060); "DOUBLE STAR PLANETS" 1)/2) page (G0060-G0077); blue sky sun-path scene (G0078-G0085); Tatooine scene with thought bubbles (G0086-G0105); whiteboard with 84 degree cone and second sun swept 30, 60, 84 (G0106-G0113); orbit diagrams plus red IMPOSSIBLE (G0114-G0129); dark starfield R_CRITICAL (G0130-G0137); Lagrange points (G0138-G0143); closing Tatooine scene (G0144-G0151); Wizard-of-Oz-style label pile (G0152-G0169). Persistent anchors: stick figure and whiteboard frame (G0001-G0013, G0048-G0060, G0106-G0129); sun, clouds and figure in G0028-G0047; the two-sun Tatooine skyline recurs at 7s, 38s, 74s, 92s, 136s. Escalation INFERRED: label stack grows nine items in G0154-G0168 (148.9-153.2s).

3. Label timing. Labels almost always appear after the object they label, in a separate step: DOUBLE RAINBOW G0016 (15.0s) vs arc earlier; SECONDARY BOW G0018; ordinal labels FIRST..FIFTH one per segment (G0038-G0046); CIRCUMBINARY G0068 (51.0s) after its orbit G0066; THE OTHER KIND G0076; IMPOSSIBLE G0120 (109.9s) after the diagram G0118; R_CRITICAL G0132 before the 6d line G0134 and ~18 degree G0136. Exception: heading "DOUBLE STAR PLANETS", "1)" and "2)" exist before content (G0061); G0116 adds heading with orbit simultaneously. Numbers (84, 60, 30 degrees) appear with the second cone (G0108) and are updated in place (G0110, G0112).

4. Reveal types. Pop-on (single-frame) dominates for objects and labels (about 70 segments). Fade in/out only for thought bubbles (G0094, G0098, G0100, G0102, 81-90s) and the right-hand sun (G0083/G0084, 68-74s) and the footnote (G0022). Pixel slide of arcs inside a panel (G0048-G0060, 38-44s). One true camera move (G0152). No write-on lines or strikes seen; each tile pair shows full objects arriving in one step (INFERRED: frame rate sampling may hide short write-ons, e.g. G0066 ellipse).

5. Jokes and callbacks. G0022 footnote "*TECHNICALLY, EACH OF YOUR EYES SEES ITS OWN RAINBOW, TOO" (18.7s, ASR "The circumstances need to be just right"); G0024/G0026 figure raises arms with "DOUBLE RAINBOW ALL THE WAY!" (21-21.6s, ASR "people get excited when they see one"); G0054 thought bubble of Tatooine (41.5s); G0076 label "THE OTHER KIND" (58.2s, ASR "called the other kind of planet"); G0104 footnote "RAINBOWS REQUIRE RAIN ..." with figure arms up (92.4s); G0128 red ejection arrow (120.25s, ASR "ejected"); G0148/G0150 pots of gold appear (145.4s, 145.9s, ASR "pots of gold"); G0152 girl with dog and "SOMEWHERE, OVER THE RAINBOW..." (147.5s, ASR "rethink all kinds of rainbow references") followed by absurd labels such as "DEFINITELY OVER THE RAINBOW" (G0168, 153.2s).

6. Counts (from my annotations). True cuts about 13: G0014 (two), G0028, G0048, G0060 end, G0078, G0086, G0106, G0130, G0138, G0144, G0170. Camera moves 1 (G0152, 147.46-147.96s, with motion blur). Drawing/state changes: the remaining ACTIVITY segments, mainly pop-ons; pose swaps 4 (G0024, G0046, G0104, partly G0152). G0006 and G0114 are in-board background/diagram swaps, not whole-frame cuts.

7. Characters and colour. Main figure: large round-head stick figure with bent arm, holding paper (G0001) or at whiteboard (G0106); tiny stick figures in scenes; thought bubbles with Tatooine skyline; girl with pigtails, basket and small dog (G0152). Objects simple outline: suns with rays, clouds, tree with bird. Colour: rainbow bands (red-orange-yellow-green-blue) as content; tan Tatooine fill; pale blue sky G0078; dark grey starfield G0130-G0143; red title and end cards G0014, G0170; grey fills for bands and arcs; red used for marks only in G0120-G0128 (IMPOSSIBLE box and arrows).

8. Unusual. Not a single persistent diagram: about 14 canvases. Red also used as full-frame brand colour (title/end cards). Stick figures not only in jokes: figure is the narrator at board and persistent in the Tatooine scenes. Colour glows and photoreal-ish gradients (suns, starfield) appear, beyond line drawing. Four footnote/thought-bubble gags occur inside explanatory scenes, not as cutaways. Short ACTIVITY pairs G0049-G0059 are low-level arc drift split by thresholds.

9. Unresolved: G0014 (second cut timing between f332 and f342), G0020 (possible slight rescale), G0038 (ring change), G0050, G0052, G0056, G0058 (arc drift detail), G0083 (dimming onset), G0092 (tick marks), G0152 (exact pan onset). All annotated with LOW/MEDIUM confidence.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.5241, #B0B0B0 0.1961, #101010 0.078, #303030 0.0777, #B0D0F0 0.0375; mean settled dark-ink coverage 17.4% (max 99.2%); red accent present in 46/86 holds; any saturated colour in 66/86 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9947 (660/662 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
