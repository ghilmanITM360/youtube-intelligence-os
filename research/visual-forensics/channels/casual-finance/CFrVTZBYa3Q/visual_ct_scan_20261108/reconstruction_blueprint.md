# Reconstruction blueprint - original asset system derived from CFrVTZBYa3Q
New ORIGINAL assets and motion only. No source screenshot, footage, logo or character drawing is copied; third-party items (`IMG_*`, `ICON_*`) are replaced with licensed or self-made equivalents and your own data. Timings at 24 fps, 1080x1920.

## Global system
- Canvas `#fcfcfc`; black outline 6-8 px, uneven hand line; flat fills; one saturated accent (red `#b0202f`-family hand-lettered labels and arrows); chart scenes use one hue per country; blackboard `#37843e` with `#6a5046` frame.
- Layers (bottom to top): canvas, chart/screenshot plate (wider than frame for pans), characters (lower third, cropped by frame edge), arrows/circles/ellipses, hand-lettered labels.
- Fonts: hand-lettered display for labels, chalk font for blackboard, handwritten black for type-on. Pick licensed equivalents.

## Reusable modules
1. **Chart module (A):** plate width ~2.5-3x frame. Hard cut onto plate panned fully left. Pan right 51-83 frames, settle. Arrow slides in from the right edge 24-36 frames after cut; "since YEAR" label pops (1 frame) about 65 frames after cut; character rises from bottom over 10-18 frames; hold >= 20 frames. QA: label onset frame equals plan +/- 0.
2. **Row pop-in grid (B):** four rows (icon + thumbnail) popping at f0, f+4, f+8, f+10 frames; hold 62 frames.
3. **Blackboard (D/F):** board top, teacher lower left, pointer poses up/down; chalk bullet appears on the same frame the pointer rises; pointer drops 8 frames later.
4. **Type-on text (I):** one character per frame, 7 frames, then hold; character gesture on the hold.
5. **Gag props (E/G/L):** sleeping armchair pop-in, z marks added one per 10 frames, plug-pull pose swap in one frame, hard cut to black held 22 frames.
6. **Dark-screenshot module (J):** plate with two bottom characters hopping in over 12 frames, plate pans right 20 frames, hand-drawn ellipse pops on the high.



## Editor timeline (frames)
- S001 f0-f0 (1 fr): START - US chart pre-draw
- S002 f1-f49 (49 fr): PAN+DRAWON - US chart pan right with line draw-on
- S003 f50-f62 (13 fr): HOLD - US chart settled
- S004 f63-f68 (6 fr): POP_IN - Handwritten "since 2007" label
- S005 f69-f76 (8 fr): POP_IN - CNBC headline card with curved arrow
- S006 f77-f98 (22 fr): POP_IN - Shocked-face character
- S007 f99-f134 (36 fr): CUT+PAN - UK chart cut and pan
- S008 f135-f163 (29 fr): SLIDE_IN - Red arrow enters
- S009 f164-f164 (1 fr): POP_IN - "since 1998" label
- S010 f165-f181 (17 fr): RISE_IN - UK-map character rises
- S011 f182-f202 (21 fr): HOLD - UK chart settled
- S012 f203-f226 (24 fr): CUT+PAN - Germany chart cut and pan
- S013 f227-f267 (41 fr): SLIDE_IN - Red arrow enters
- S014 f268-f268 (1 fr): POP_IN - "since 2011" label
- S015 f269-f280 (12 fr): RISE_IN - Germany-map character rises
- S016 f281-f295 (15 fr): HOLD - Germany chart settled
- S017 f296-f325 (30 fr): CUT+PAN - Japan 10-year chart cut and pan
- S018 f326-f338 (13 fr): SLIDE_IN - Red arrow enters
- S019 f339-f374 (36 fr): POP_IN - Pink circle and 2.1 tag
- S020 f375-f385 (11 fr): POP_IN - "since 1999" label
- S021 f386-f398 (13 fr): SLIDE_IN - Japan-map character slides in
- S022 f399-f422 (24 fr): HOLD - Japan 10-year chart held
- S023 f423-f442 (20 fr): CUT+PAN - Japan 30-year chart cut and pan
- S024 f443-f466 (24 fr): SLIDE_IN - Red arrow enters
- S025 f467-f473 (7 fr): SLIDE_IN - Japan-map character and shocked face enter
- S026 f474-f483 (10 fr): HOLD - Japan 30-year chart settled
- S027 f484-f487 (4 fr): CUT - Flag grid: US row
- S028 f488-f491 (4 fr): POP_IN - UK row added
- S029 f492-f493 (2 fr): POP_IN - Germany row added
- S030 f494-f555 (62 fr): POP_IN - Japan row added (four-row grid)
- S031 f556-f584 (29 fr): FADE+RISE - Doge coins fade over flags; dancing Doge rises
- S032 f585-f611 (27 fr): CUT - Dogecoin vs Bitcoin chart
- S033 f612-f627 (16 fr): SCROLL+SLIDE - Chart rises; tweet screenshot and Musk head enter
- S034 f628-f643 (16 fr): HOLD - Chart + tweets settled
- S035 f644-f658 (15 fr): CUT - Blackboard, teacher smiling, empty board
- S036 f659-f703 (45 fr): POP_IN - "One VERY important question:" on board
- S037 f704-f733 (30 fr): CUT - Meme image (reaction GIF)
- S038 f734-f745 (12 fr): POP_IN - Second "???"
- S039 f746-f749 (4 fr): CUT - Blank white
- S040 f750-f765 (16 fr): SLIDE_IN - Treasury and Japan bonds slide in
- S041 f766-f776 (11 fr): HOLD - Two bonds held
- S042 f777-f800 (24 fr): POP_IN - Sleeping armchair character
- S043 f801-f815 (15 fr): CUT - Blackboard, teacher stern, empty board
- S044 f816-f823 (8 fr): POP_IN - "- Predictable" on board; pointer up
- S045 f824-f837 (14 fr): POSE - Pointer lowered
- S046 f838-f838 (1 fr): POSE - Pointer raised
- S047 f839-f844 (6 fr): POP_IN - "- Uneventful" added
- S048 f845-f861 (17 fr): POSE - Pointer lowered
- S049 f862-f872 (11 fr): CUT+ENTRY - Old man and bonds drop in
- S050 f873-f888 (16 fr): HOLD - Old man speaks
- S051 f889-f891 (3 fr): POSE - Old man dozes
- S052 f892-f901 (10 fr): POP_IN - First z
- S053 f902-f908 (7 fr): POP_IN - Second z
- S054 f909-f922 (14 fr): POP_IN - Third z
- S055 f923-f958 (36 fr): CUT - Party scene with confetti
- S056 f959-f1004 (46 fr): POP_IN - Thought bubble "These people are mad"
- S057 f1005-f1005 (1 fr): CUT - Stick man, no text yet
- S058 f1006-f1012 (7 fr): TEXT_TYPE - "But right now," typed on
- S059 f1013-f1019 (7 fr): HOLD - "But right now," held
- S060 f1020-f1021 (2 fr): CUT - S&P 500 screenshot
- S061 f1022-f1034 (13 fr): HOP_IN - Two characters hop in
- S062 f1035-f1047 (13 fr): HOLD - Screenshot and characters held
- S063 f1048-f1067 (20 fr): PAN - S&P chart pans right
- S064 f1068-f1088 (21 fr): POP_IN - Green ellipse circles the high
- S065 f1089-f1091 (3 fr): CUT - AI chatter chart grid
- S066 f1092-f1101 (10 fr): RISE_IN - Robot rises
- S067 f1102-f1116 (15 fr): HOLD - Robot thumbs-up held
- S068 f1117-f1156 (40 fr): CUT - Treasury character plugged into wall socket
- S069 f1157-f1166 (10 fr): POSE - Plug pulled out
- S070 f1167-f1188 (22 fr): CUT - Black

## Per-state prompts
All 70 image and animation prompts with static anchors and nearest-frame QA: `PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json`.

## Acceptance tests
1. Cut frames equal the ledger exactly (99, 203, 296, 423, 484, 585, 644, 704, 746, 801, 862, 923, 1005, 1020, 1089, 1117, 1167).
2. EXACT onsets match to the frame; BOUND onsets fall inside their window.
3. Static anchors are pixel-still between events.
4. Total length 1189 frames.
5. Sound unspecified (nobody listened); ASR lines are timing reference only.
