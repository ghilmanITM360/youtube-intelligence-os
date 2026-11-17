# Reconstruction blueprint - original asset system derived from eePIUX0Sd6c
New ORIGINAL assets and motion only. No source screenshot, footage, logo or character drawing is copied; third-party items (`IMG_*`, `ICON_*`) are replaced with licensed or self-made equivalents and your own data. Timings at 30 fps, 1920x1080.

## Modules (original rebuild; derived from measured patterns)
1. **Cast and set kit**: a small reusable cast (stick-man host with pointer, four national-costume figures, a star-banded top-hat figure, a detective, a lone suited boardroom figure, a turtle, a dragon) and a few reusable sets (green chalkboard, city boardroom with projector, fork-in-road, iceberg, burning Earth). Redraw originals; reuse the same assets across the video (the boardroom with the gold screen returns at f81, f1725, f4222, f12015, f14434).
2. **Hard-cut scene chain**: 119 hard cuts, median shot 3.2 s (0.6-17.9 s); the encoder places an I-frame on 116 of them, so cuts must be authored as true edits and the codec will follow.
3. **Slow push-in on held illustrations**: apply a continuous scale-up of about 0.8 percent per second (interquartile range 0.64-0.97, extremes 0.25-4.4 on very short shots, measured on 56 shots) starting at the cut; leave screen recordings and monitor sketches locked.
4. **24 fps motion on a 30 fps timeline**: character and background animation is drawn at 24 fps and conformed to 30 by repeating every fifth frame (4 of 5 frames change); reproduce the cadence for animated runs, not for held scenes.
5. **Text-card beat**: small black rounded-handwriting text centred on white, replaced in place by a single-frame swap for lists of short beats ('Cute.' / 'Respectable.'; 'Not Dumping.' / 'Diversifying.' / 'Slowly.' / 'Strategically.'; When/Then pairs built line by line).
6. **Annotation pop-ins**: red marker circles, arrows and labels (CPI, Gold, ~70%, 58%, -12%) appear in one frame on top of a chart screenshot, never drawn on; use your own chart and numbers.
7. **Sponsor block in house style**: sponsor card, host at a desk, mascot-cube character, hand-drawn monitor over screen recordings, a meme card; about 69 s; replace with your own sponsor assets and disclosure.
8. **Third-party insert slot**: photographs, news snippets, marketplace listing, meme, banknote images, forum posts and chart screenshots are replaced with licensed or self-made equivalents; never copy the source items.
9. **Eased zoom reveal**: one eased push-in (about 2.8x over 5 s, fastest in the middle) lands on faces before a hard cut (f8238-f8398); use for a punch-in beat.
10. **Callback structure**: open and close on the chalkboard host (f0, f11581, f13994) and repeat the iceberg, fork-in-road, burning Earth and central-bank-purchases visuals as motifs.
11. **Codec note**: do not reproduce the sub-2,000-px MICRO states; in zoom shots they are the quantization steps of the push-in, elsewhere their cause is unresolved.
12. **End card**: 'Subscribe for more Casual Finance', platform mark with social icons, button, waving stick man; hold about 5.0 s.


## Editor timeline (frames)
- S001 f0-f37 (38 fr): START - Stick man presenting gold chart on chalkboard
- S002 f38-f80 (43 fr): CUT - Chalkboard close-up with red arrow
- S003 f81-f223 (143 fr): CUT+ZOOM_IN - Boardroom of puzzled figures with gold chart screen
- S004 f224-f291 (68 fr): CUT - Bedroom stick man drinking FOUR can
- S005 f292-f393 (102 fr): POP_IN - Portrait photo pop-in at upper left
- S006 f394-f429 (36 fr): CUT+ZOOM_IN - Here's the thing text card
- S007 f430-f590 (161 fr): CUT+ZOOM_IN - Chalkboard table Average returns
- S008 f591-f609 (19 fr): CUT - Cute text card
- S009 f610-f636 (27 fr): TEXT_SWAP+ZOOM_IN - Respectable replaces Cute
- S010 f637-f699 (63 fr): CUT+ZOOM_IN - Turtle carrying gold bar by pond
- S011 f700-f864 (165 fr): CUT+ZOOM_IN - Chalkboard returns table again
- S012 f865-f1003 (139 fr): CUT+ZOOM_IN - Earth on fire with party hat
- S013 f1004-f1071 (68 fr): CUT - Fork in the road Option A Option B
- S014 f1072-f1089 (18 fr): POP_IN+MICRO - Red arrow beside Option A sign
- S015 f1090-f1173 (84 fr): CUT+ZOOM_IN - Earth on fire returns
- S016 f1174-f1191 (18 fr): CUT - Fork in road arrow at Option B
- S017 f1192-f1333 (142 fr): CUT+ZOOM_IN - Cave people around gold bar
- S018 f1334-f1355 (22 fr): CUT - Fork in road no arrow
- S019 f1356-f1478 (123 fr): CUT+ZOOM_IN - Caveman on snowy summit holding gold bar
- S020 f1479-f1511 (33 fr): CUT+ZOOM_IN - But don't worry text card
- S021 f1512-f1556 (45 fr): TEXT_SWAP+ZOOM_IN - It gets even weirder text
- S022 f1557-f1689 (133 fr): CUT+ZOOM_IN - Tunnel with truth about gold sign
- S023 f1690-f1724 (35 fr): CUT - Stock trader at six monitors
- S024 f1725-f1765 (41 fr): CUT - Boardroom with gold on screen
- S025 f1766-f1805 (40 fr): CUT - Tired analyst at spreadsheet
- S026 f1806-f2033 (228 fr): CUT+ZOOM_IN - Grey room desk with water jugs
- S027 f2034-f2138 (105 fr): CUT+ZOOM_IN - Whiteboard of equations with puzzled stick man
- S028 f2139-f2182 (44 fr): CUT - Stick man pointing at STOP sign
- S029 f2183-f2236 (54 fr): CUT - Stick man thumbs up on white
- S030 f2237-f2312 (76 fr): CUT+ZOOM_IN - Sponsored by Notion card
- S031 f2313-f2354 (42 fr): CUT - Stick man at desk with microphone
- S032 f2355-f2455 (101 fr): POP_IN+MICRO - Notion cube character joins desk
- S033 f2456-f2544 (89 fr): CUT+ZOOM_IN - Monitor showing Notion logo
- S034 f2545-f2621 (77 fr): CUT+ZOOM_IN - Tired man at paper-covered desk
- S035 f2622-f2663 (42 fr): CUT+ANIM - Monitor showing PDF report page
- S036 f2664-f2690 (27 fr): SCREEN_SWAP - Spreadsheet on monitor
- S037 f2691-f2717 (27 fr): SCREEN_SWAP - Central Bank Gold Reserves Survey 2025 page
- S038 f2718-f2749 (32 fr): SCREEN_SWAP+MICRO - Historical performance of the Gold spot price index page
- S039 f2750-f2781 (32 fr): SCREEN_SWAP+MICRO - Key takeaways gauge page with new address bar
- S040 f2782-f2806 (25 fr): SCREEN_SWAP - Dark PDF viewer with thumbnails
- S041 f2807-f2816 (10 fr): SCREEN_SWAP - Article Gold forecast to rise 6 percent
- S042 f2817-f2882 (66 fr): CUT+ZOOM_IN - Notion 3.0 agents card
- S043 f2883-f2969 (87 fr): CUT+ZOOM_IN - Lifter straining under barbell
- S044 f2970-f3034 (65 fr): POSE+ZOOM_IN - Notion cubes carry the barbell lifter smiles
- S045 f3035-f3152 (118 fr): CUT - Dark Notion AI start screen
- S046 f3153-f3183 (31 fr): TEXT_TYPE - Prompt text appears first burst
- S047 f3184-f3229 (46 fr): TEXT_TYPE - Prompt text second burst
- S048 f3230-f3285 (56 fr): TEXT_TYPE+MICRO - Prompt text third burst
- S049 f3286-f3286 (1 fr): POP_IN - Major Central Bank Gold Holdings table card
- S050 f3287-f3298 (12 fr): CUT - Monitor sketch showing table with AI panel
- S051 f3299-f3418 (120 fr): TEXT_STREAM+ANIM - AI answer text streams in right panel
- S052 f3419-f3447 (29 fr): CUT - And the best part text card
- S053 f3448-f3561 (114 fr): CUT - Dark table with Notion AI chat popup
- S054 f3562-f3589 (28 fr): TEXT_TYPE+MICRO - Chat prompt text appears
- S055 f3590-f3695 (106 fr): CUT - Full dark table view
- S056 f3696-f3790 (95 fr): CUT+ZOOM_IN - Overwhelmed stick man in paper piles
- S057 f3791-f3889 (99 fr): CUT+ZOOM_IN - The solution bin sign
- S058 f3890-f3931 (42 fr): POP_IN+ZOOM_IN - Notion logo on solution sign
- S059 f3932-f4080 (149 fr): CUT+ZOOM_IN - Meme with N logo Go on do tell
- S060 f4081-f4149 (69 fr): CUT - Stick man running under rainbow
- S061 f4150-f4221 (72 fr): CUT - Stick man beside Notion logo
- S062 f4222-f4326 (105 fr): CUT+MICRO - Boardroom with gold bar on screen
- S063 f4327-f4418 (92 fr): CUT - Iceberg with gold bar tip
- S064 f4419-f4498 (80 fr): POP_IN - Question marks under water
- S065 f4499-f4568 (70 fr): CUT+ZOOM_IN - Turtle with gold bar again
- S066 f4569-f4636 (68 fr): CUT - Photo of man holding gold card
- S067 f4637-f4750 (114 fr): CUT - Detective at corkboard with gold at centre
- S068 f4751-f4875 (125 fr): POP_OUT+ZOOM_IN - Gold bar removed from centre card
- S069 f4876-f4907 (32 fr): POP_IN - Inflation text appears on card
- S070 f4908-f4971 (64 fr): CUT - Spotlit figure with striped hat and book
- S071 f4972-f5002 (31 fr): CUT - Rent hike door
- S072 f5003-f5029 (27 fr): CUT - Grocery eggs price tag
- S073 f5030-f5087 (58 fr): CUT+MICRO - Drive-through menu price hikes
- S074 f5088-f5188 (101 fr): CUT+ZOOM_IN - Clown mascot presenting rising chart
- S075 f5189-f5222 (34 fr): CUT+ZOOM_IN - Here's the thing text card again
- S076 f5223-f5288 (66 fr): CUT - Detective corkboard with scribbled Inflation
- S077 f5289-f5351 (63 fr): POP_OUT - Inflation card cleared
- S078 f5352-f5443 (92 fr): CUT - Gold vs CPI line chart
- S079 f5444-f5630 (187 fr): POP_IN - CPI red annotation
- S080 f5631-f5684 (54 fr): POP_IN - Small face photo beside CPI label
- S081 f5685-f5751 (67 fr): POP_IN - Gold label and red oval
- S082 f5752-f5849 (98 fr): SCREEN_SWAP - Chart view changes with Gold arrow and bracket
- S083 f5850-f5993 (144 fr): CUT+ZOOM_IN - Pie chart with small Inflation slice
- S084 f5994-f6082 (89 fr): CUT - Iceberg with gold bar and three question marks
- S085 f6083-f6156 (74 fr): POP_IN+ZOOM_IN - Angry face in iceberg
- S086 f6157-f6270 (114 fr): CUT - Four costumed figures with banknotes
- S087 f6271-f6313 (43 fr): POSE - Figures hush with fingers to lips
- S088 f6314-f6369 (56 fr): CUT - Social profile grid left
- S089 f6370-f6587 (218 fr): POP_IN+MICRO - Second profile with empty grid
- S090 f6588-f6709 (122 fr): CUT+ZOOM_IN - Currency composition of foreign reserves line chart
- S091 f6710-f6949 (240 fr): CUT+ZOOM_IN - Key takeaways text card
- S092 f6950-f7081 (132 fr): CUT+ZOOM_IN - Declining dollar share line chart with red arrow
- S093 f7082-f7200 (119 fr): CUT+ANIM - Four costumed figures with DUMP USD button
- S094 f7201-f7234 (34 fr): POSE - Figures react alarmed at button
- S095 f7235-f7263 (29 fr): POSE - Figures lean away from button
- S096 f7264-f7367 (104 fr): POSE+ZOOM_IN - Button gone figures hush
- S097 f7368-f7392 (25 fr): POSE - Figures point up with empty thought cloud
- S098 f7393-f7465 (73 fr): POP_IN - Diversifying inside thought cloud
- S099 f7466-f7490 (25 fr): CUT - Not Dumping text card
- S100 f7491-f7530 (40 fr): TEXT_SWAP - Diversifying text
- S101 f7531-f7555 (25 fr): TEXT_SWAP - Slowly text
- S102 f7556-f7588 (33 fr): TEXT_SWAP - Strategically text
- S103 f7589-f7710 (122 fr): CUT - Sleeping dragon on money pile in vault
- S104 f7711-f7720 (10 fr): CUT - Foreign exchange reserves stacked bar chart
- S105 f7721-f7789 (69 fr): POP_IN - Red curved arrow on chart
- S106 f7790-f7899 (110 fr): POP_IN+MICRO - Red 70 percent label above chart
- S107 f7900-f7964 (65 fr): POP_IN - Second red arrow at right edge
- S108 f7965-f7998 (34 fr): POP_IN - 58 percent red label
- S109 f7999-f8048 (50 fr): POP_IN - Minus 12 percent red label with curve
- S110 f8049-f8237 (189 fr): CUT+ZOOM_IN - Official foreign exchange reserves area chart
- S111 f8238-f8401 (164 fr): CUT+ZOOM_IN - Five figures arm in arm with Uncle Sam figure
- S112 f8402-f8438 (37 fr): CUT - Euro banknotes fan
- S113 f8439-f8465 (27 fr): POP_IN - Red X over euro notes
- S114 f8466-f8503 (38 fr): POP_IN - Yen notes with red X
- S115 f8504-f8542 (39 fr): POP_IN - Pound notes with red X
- S116 f8543-f8577 (35 fr): CUT+ZOOM_IN - Four figures around dropped gold bar
- S117 f8578-f8620 (43 fr): CUT - Figures at bedside with gold bars
- S118 f8621-f8680 (60 fr): CUT - Meeting with gold bar on desk
- S119 f8681-f8762 (82 fr): CUT - Break glass in case of emergency gold
- S120 f8763-f8852 (90 fr): CUT - Central bank gold purchases infographic
- S121 f8853-f9008 (156 fr): POP_IN+MICRO - Red circle around highlight text
- S122 f9009-f9175 (167 fr): POP_IN+MICRO - Red arrows over lower bars
- S123 f9176-f9298 (123 fr): POSE - Circle replaced by arrow at highlight text
- S124 f9299-f9387 (89 fr): CUT+ZOOM_IN - Figures with dropped gold bar
- S125 f9388-f9563 (176 fr): CUT+ZOOM_IN - Reuters snippet on grey
- S126 f9564-f9743 (180 fr): SCREEN_SWAP+ZOOM_IN - Key highlights card
- S127 f9744-f9812 (69 fr): CUT+ZOOM_IN - Labubu doll marketplace listing
- S128 f9813-f9873 (61 fr): CUT+ZOOM_IN - Figures with DUMP USD button again
- S129 f9874-f9971 (98 fr): CUT - Classroom board Things to worry about
- S130 f9972-f10008 (37 fr): POP_IN - U.S. Debt written on board
- S131 f10009-f10056 (48 fr): POP_IN - Inflation written on board
- S132 f10057-f10151 (95 fr): POP_IN+MICRO - Over-Reliant on the US written on board
- S133 f10152-f10175 (24 fr): CUT - And Gold text card
- S134 f10176-f10338 (163 fr): CUT+ANIM - Boxing ring with star-hat boxer over huddled figures
- S135 f10339-f10373 (35 fr): CUT - Stick man pointing at STOP sign again
- S136 f10374-f10544 (171 fr): CUT+MICRO - Control room with star-hat figure and coffee
- S137 f10545-f10678 (134 fr): CUT - Dark forum posts
- S138 f10679-f10835 (157 fr): CUT+ZOOM_IN - Bunker computer with gold bars
- S139 f10836-f10928 (93 fr): CUT+ZOOM_IN - Official reserves area chart with 58 percent brace
- S140 f10929-f11079 (151 fr): CUT - Four blindfolded figures
- S141 f11080-f11132 (53 fr): CUT - Alarm bell in school hallway
- S142 f11133-f11222 (90 fr): CUT+ZOOM_IN - Central bank gold purchases infographic again
- S143 f11223-f11244 (22 fr): CUT - When Then text card
- S144 f11245-f11280 (36 fr): TEXT_TYPE - Trust is high text
- S145 f11281-f11310 (30 fr): TEXT_TYPE - Gold is boring text
- S146 f11311-f11352 (42 fr): TEXT_SWAP - Markets feel stable replaces trust text
- S147 f11353-f11386 (34 fr): TEXT_TYPE - Gold goes nowhere text
- S148 f11387-f11442 (56 fr): TEXT_SWAP - Institutions feel safe replaces markets line
- S149 f11443-f11485 (43 fr): TEXT_TYPE - Gold gets ignored text
- S150 f11486-f11580 (95 fr): CUT - Gold bar character amid collapsing city
- S151 f11581-f11680 (100 fr): CUT - Stick man with pointer at chalkboard
- S152 f11681-f11778 (98 fr): CUT+ZOOM_IN - Break glass in case of emergency box again
- S153 f11779-f11830 (52 fr): CUT - Preemptive positioning text card
- S154 f11831-f11938 (108 fr): CUT - Figures running from monster face
- S155 f11939-f12014 (76 fr): POSE - Figures arm with pitchforks and swords
- S156 f12015-f12073 (59 fr): CUT+ZOOM_IN - Boardroom with gold bar on screen again
- S157 f12074-f12145 (72 fr): CUT - E-mini S&P 500 futures chart
- S158 f12146-f12239 (94 fr): CUT - Nightclub with star-hat figure on cash
- S159 f12240-f12372 (133 fr): CUT+MICRO - The AI valuation premium chart
- S160 f12373-f12408 (36 fr): CUT - Stick man with blank green board
- S161 f12409-f12474 (66 fr): POP_IN - Gold chart appears on board
- S162 f12475-f12519 (45 fr): CUT+ZOOM_IN - Iceberg with gold and question marks again
- S163 f12520-f12589 (70 fr): CUT - Fork in road with blank signs
- S164 f12590-f12758 (169 fr): POP_IN - Risk-On Rally sign text
- S165 f12759-f12903 (145 fr): POP_IN - Risk-Off Rally sign text
- S166 f12904-f12968 (65 fr): POP_IN+ZOOM_IN - Confused stick man between signs
- S167 f12969-f13002 (34 fr): CUT+ZOOM_IN - Earth on fire again
- S168 f13003-f13068 (66 fr): CUT - S&P futures chart again
- S169 f13069-f13137 (69 fr): CUT - Gold price chart
- S170 f13138-f13198 (61 fr): CUT - US 10 Year Treasury chart
- S171 f13199-f13286 (88 fr): CUT+ZOOM_IN - Detective with asset class diagram
- S172 f13287-f13440 (154 fr): CUT+ZOOM_IN - Chaotic trading floor
- S173 f13441-f13514 (74 fr): CUT+MICRO - WTF is happening stressed stick man
- S174 f13515-f13592 (78 fr): CUT+MICRO - Bar scene two figures
- S175 f13593-f13668 (76 fr): POP_IN - Speech bubble not looking for anything serious
- S176 f13669-f13715 (47 fr): POSE - Woman smiles with love language bubble
- S177 f13716-f13872 (157 fr): CUT+ZOOM_IN - Stick man presenting COMMENTS board
- S178 f13873-f13912 (40 fr): CUT+ZOOM_IN - One thing for certain text card
- S179 f13913-f13993 (81 fr): CUT+ZOOM_IN - Crystal ball with question marks
- S180 f13994-f14053 (60 fr): CUT - Stick man at chalkboard gold chart closing
- S181 f14054-f14099 (46 fr): CUT - Figures with dropped gold bar closing
- S182 f14100-f14170 (71 fr): CUT - Gold price chart yellow
- S183 f14171-f14243 (73 fr): CUT - Five figures arm in arm closing
- S184 f14244-f14433 (190 fr): CUT+ZOOM_IN - Central bank gold purchases infographic with circle
- S185 f14434-f14510 (77 fr): CUT - Boardroom with gold on screen closing
- S186 f14511-f14660 (150 fr): CUT - Subscribe end card

## Per-state prompts
All 186 image and animation prompts with static anchors and nearest-frame QA: `PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json`.

## Acceptance tests
1. Cut frames equal the ledger exactly (38, 81, 224, 394, 430, 591, 637, 700, 865, 1004, 1090, 1174, 1192, 1334, 1356, 1479, 1557, 1690, 1725, 1766, 1806, 2034, 2139, 2183, 2237, 2313, 2456, 2545, 2622, 2817, 2883, 3035, 3287, 3419, 3448, 3590, 3696, 3791, 3932, 4081, 4150, 4222, 4327, 4499, 4569, 4637, 4908, 4972, 5003, 5030, 5088, 5189, 5223, 5352, 5850, 5994, 6157, 6314, 6588, 6710, 6950, 7082, 7466, 7589, 7711, 8049, 8238, 8402, 8543, 8578, 8621, 8681, 8763, 9299, 9388, 9744, 9813, 9874, 10152, 10176, 10339, 10374, 10545, 10679, 10836, 10929, 11080, 11133, 11223, 11486, 11581, 11681, 11779, 11831, 12015, 12074, 12146, 12240, 12373, 12475, 12520, 12969, 13003, 13069, 13138, 13199, 13287, 13441, 13515, 13716, 13873, 13913, 13994, 14054, 14100, 14171, 14244, 14434, 14511).
2. EXACT onsets match to the frame; BOUND onsets fall inside their window.
3. Static anchors are pixel-still between events.
4. Total length 14661 frames.
5. Sound unspecified (nobody listened); ASR lines are timing reference only.
