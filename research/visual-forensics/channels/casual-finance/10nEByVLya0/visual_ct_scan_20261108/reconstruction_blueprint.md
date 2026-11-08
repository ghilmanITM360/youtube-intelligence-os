# Reconstruction blueprint - original asset system derived from 10nEByVLya0
New ORIGINAL assets and motion only. No source screenshot, footage, logo or character drawing is copied; third-party items (`IMG_*`, `ICON_*`) are replaced with licensed or self-made equivalents and your own data. Timings at 30 fps, 1080x1920.

## Global system
- Canvas `#fcfcfc`; small centred content cluster in the middle band of a 9:16 frame (content rows ~640-1250 px of 1920); one burned-in caption line below it (rows ~1250-1440 px); everything outside is empty white.
- Style: flat 2D hand-drawn icons and one-colour stick figures, mixed with small embedded screenshots and short video clips; red hand-drawn arrows/ellipses/percent label as the single accent.
- Layers: canvas, plate (screenshot/icon cluster), characters, annotations (arrow, ellipse, check, highlight), caption (top).

## Reusable modules
1. **Caption track:** a separate text layer that changes about every 0.29 s (190 measured changes in 55.3 s), growing word by word and resetting per phrase; lead/lag vs speech is about zero (see report). Build as its own sequence, not baked into scenes.
2. **Pop-in annotation:** single-frame appearance (portrait, logo, bubble, check, "90%", question-mark circles), no easing visible.
3. **Hard-cut scene swap:** about one cut per 2.6 s; scenes are 1.5-4.5 s.
4. **Embedded clip scenes:** a small looping clip inside a static plate (Wall Street traders, fire-puppet, yacht, red news tiles, crowd in bubble); in the last scene the clip changes in 12-frame bursts every 15 frames.
5. **Draw-on annotations:** red arrow travelling to a point (about 25 frames), red ellipse drawn around a headline (about 3 frames), yellow highlight sweeping a table column (about 27 frames).
6. **Timeline scroller:** year numbers separated by red arrows scrolling horizontally and settling on "2007 <- 2008".
7. **Gag objects:** soap bubble inflating around a dollar sign then bursting into droplets; flame sprites that change shape every 10 frames; logo block tilting off screen with a "bye-bye" label.


## Editor timeline (frames)
- S001 f0-f3 (4 fr): START - Blank canvas
- S002 f4-f69 (66 fr): SLIDE_IN - Question-mark circles scroll in
- S003 f70-f98 (29 fr): POP_IN - Chart icon appears between circles
- S004 f99-f109 (11 fr): CUT - Chart shrinks left, money bag right
- S005 f110-f118 (9 fr): POP_IN - First "?" circle
- S006 f119-f124 (6 fr): POP_IN - Second "?" circle
- S007 f125-f133 (9 fr): POP_IN - Third "?" circle
- S008 f134-f153 (20 fr): POP_IN - Large "?" circle
- S009 f154-f154 (1 fr): CUT - Dollar sign alone
- S010 f155-f229 (75 fr): BUBBLE_GROW - Soap bubble inflates around the dollar sign
- S011 f230-f242 (13 fr): POP_IN - Bubble pops into particles
- S012 f243-f253 (11 fr): POP_IN - Particles gone
- S013 f254-f302 (49 fr): CUT - Stick man
- S014 f303-f319 (17 fr): SLIDE_IN - Cartoon Earth slides in
- S015 f320-f338 (19 fr): HOLD - Man and Earth held
- S016 f339-f365 (27 fr): POSE - Earth sweats
- S017 f366-f399 (34 fr): CUT+SCROLL - Timeline of years scrolls
- S018 f400-f404 (5 fr): HOLD - "2007 <- 2008" at rest
- S019 f405-f439 (35 fr): POP_IN - Calendar icon "June"
- S020 f440-f476 (37 fr): CUT+CLIP - Wall Street sign with two clips
- S021 f477-f510 (34 fr): CUT+CLIP - "The market:" fire clip
- S022 f511-f540 (30 fr): CUT - Stick man
- S023 f541-f565 (25 fr): CUT - Blackstone logo
- S024 f566-f595 (30 fr): POP_IN - First founder portrait
- S025 f596-f630 (35 fr): POP_IN - Second founder portrait
- S026 f631-f663 (33 fr): CUT - Stick man
- S027 f664-f706 (43 fr): CUT+CLIP - Yacht clip with money bags
- S028 f707-f729 (23 fr): CUT - Stick man (neutral face)
- S029 f730-f746 (17 fr): CUT - Baby in hospital bed
- S030 f747-f779 (33 fr): POP_IN - Speech bubble: baby name line
- S031 f780-f811 (32 fr): CUT - Newborn close-up with Peterson face
- S032 f812-f812 (1 fr): POP_IN - One-frame faint text flash
- S033 f813-f824 (12 fr): HOLD - Newborn close-up held
- S034 f825-f849 (25 fr): CUT - Stick man
- S035 f850-f858 (9 fr): CUT - News article page
- S036 f859-f891 (33 fr): POP_IN - Blackstone logo on article
- S037 f892-f898 (7 fr): POP_IN - First portrait on article
- S038 f899-f965 (67 fr): POP_IN - Second portrait on article
- S039 f966-f1046 (81 fr): ANIM_LOOP - Banknotes fall; text highlighted
- S040 f1047-f1064 (18 fr): CUT - Timeline with calendar
- S041 f1065-f1086 (22 fr): SCROLL - Timeline scrolls left
- S042 f1087-f1104 (18 fr): HOLD - Timeline at rest
- S043 f1105-f1159 (55 fr): CUT+LOOP - Burning Earth with spiral eyes
- S044 f1160-f1160 (1 fr): CUT - First red clip tile
- S045 f1161-f1173 (13 fr): POP_IN - Red clip tiles accumulate
- S046 f1174-f1191 (18 fr): POP_IN - Full cluster of red tiles
- S047 f1192-f1225 (34 fr): CUT - Candlestick price chart
- S048 f1226-f1250 (25 fr): DRAWON - Red arrow moves down the trough
- S049 f1251-f1263 (13 fr): POP_IN - "90%" label
- S050 f1264-f1288 (25 fr): POP_IN - Worried face
- S051 f1289-f1320 (32 fr): CUT - Dark search-result card
- S052 f1321-f1390 (70 fr): DRAWON - Red ellipse circles the headline
- S053 f1391-f1437 (47 fr): SLIDE_OUT - Logo tilts and slides out with "bye-bye"
- S054 f1438-f1460 (23 fr): HOLD - Search-result card alone
- S055 f1461-f1469 (9 fr): CUT - Data table page
- S056 f1470-f1533 (64 fr): SLIDE_IN - Stick man leans in from left
- S057 f1534-f1561 (28 fr): SWEEP - Yellow highlight sweeps down first column
- S058 f1562-f1569 (8 fr): HOLD - Highlighted table held
- S059 f1570-f1582 (13 fr): POP_IN - Green check mark
- S060 f1583-f1587 (5 fr): POP_IN - Skyscrapers and speech bubble
- S061 f1588-f1659 (72 fr): ANIM_LOOP - Crowd clip plays in bubble

## Per-state prompts
All 61 image and animation prompts with static anchors and nearest-frame QA: `PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json`.

## Acceptance tests
1. Cut frames equal the ledger exactly (99, 154, 254, 366, 440, 477, 511, 541, 631, 664, 707, 730, 780, 825, 850, 1047, 1105, 1160, 1192, 1289, 1461).
2. EXACT onsets match to the frame; BOUND onsets fall inside their window.
3. Static anchors are pixel-still between events.
4. Total length 1660 frames.
5. Sound unspecified (nobody listened); ASR lines are timing reference only.
