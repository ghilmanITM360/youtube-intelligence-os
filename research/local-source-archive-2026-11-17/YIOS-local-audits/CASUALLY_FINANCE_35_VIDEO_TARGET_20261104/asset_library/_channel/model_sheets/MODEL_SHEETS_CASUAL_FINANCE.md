# Casual Finance — model sheets v0.1 (2026-11-08, LOCAL ONLY)

Built from 19 verified videos (4,667 state frames; gG239LrksH4 pending). Labels: **MEASURED** (pixels/ledger numbers), **OBSERVED** (I looked at the image), **ESTIMATED** (rough pixel measurement), **INFERRED** (my interpretation), **UNAVAILABLE**.
Images to open: `characters_core_stickman.jpg`, `characters_variant_kit.jpg` (+ `.ids.txt`), `characters_anthropomorphic.jpg`, `props_graphics_core.jpg` (+ ids), `typography_txt_assets.jpg` (+ ids), `environments_full_bleed.jpg`, `../review_sheets/*.jpg`. Tile label = video/state, so every tile maps to `<video>/states/<state>_f*.jpg` at full resolution.
Originality line: this is the style SYSTEM to reproduce with ORIGINAL characters, logo and name. The named channel characters below are references for structure, not assets to copy.

## 0. Two coexisting visual layers (OBSERVED, the most important finding)
- **Layer A, "white canvas":** pure white background, flat black-outline stick figures and hand-drawn cut-out props placed sparsely with a lot of empty space; text is hand-lettered or plain sans/serif. Dominant by far (about 3,075 of 3,945 clusters have white_frac > 0.6; MEASURED).
- **Layer B, "full-bleed scene":** a coloured flat-fill illustration fills the frame (beige/cream, sky-blue, green, grey rooms; casino, boardroom, school hall, underwater, forest, supermarket, gym). Same black-outline cartoon language but richer, denser scenes, more like an illustrated panel than a cut-out. 376 clusters (about 9.5%; MEASURED by pixel rule).
- Inserted real-world material: screenshots, charts, articles, logos, photos, meme images, map crops on grey or white or dark pages (OBSERVED, about a third of clusters carry a graphics_ui tag, rule-based).
- Counterexamples to a single style: the black-and-white line-art scenes (Wall St street, "WALL ST" building sketch, naked-man outline figure), the greyscale ghost figure, the dark night-sky "WE ARE IN TROUBLE" neon text, the astronaut-on-moon black scene (OBSERVED).

## 1. Canvas and format (MEASURED from the saved frames)
- Long-form: 1920x1080 (12 videos) and 1280x720 (3 videos: Uumnx2Fo6cE, kwMHrTFCWUE, o3FQcd91MIs). Shorts: 1080x1920 (4 videos: 10nEByVLya0, CFrVTZBYa3Q, SYSUh-oow6M, turJ6VMfUjI). Full list `resolution_by_video.csv`.
- Shorts keep the same white-canvas language, the figure and props are small and centred, with a tiny caption line below (OBSERVED, `characters_core_stickman.jpg` tiles 1-3, 7-9, 22-24).

## 2. Character model sheet
**2a. Base stick figure rig (the workhorse, CH_STICKMAN: 219 states across 8 videos in the ledger ids; MEASURED).**
- OBSERVED: round, slightly lumpy, hand-drawn head disc filled peach (#FCD4B4 is the top chromatic colour in character/prop frames, 18% of chromatic pixels; MEASURED), thick black outline, two dot eyes, a short mouth line (smile, flat, frown, open-laugh, panic), a tuft of spiky black hair on top. A single-line neck and torso, single-line limbs (no hands/feet detail, a small hook for a hand when gripping), a body that stays thin and a head that is big.
- ESTIMATED (n=71 solo-figure 1920x1080 frames, `head_ratio_samples.csv`): head width is about 0.41 of full figure height (p25-p75 0.34-0.41), outline stroke about 11 px at 1920 wide. Rough, treat as +-15%.
- Pose set seen (OBSERVED, `characters_core_stickman.jpg`): neutral arms-out, smile, thinking-hand-on-chin, hands-on-hips, pointing with a long stick (teacher with pointer, CH_STICKMAN_POINTER, usually beside a green chalkboard), kneeling, hands-on-head panic with sweat marks and shake lines, laughing with eyes shut, reading paper, holding phone/mug/money, thought bubble with an inserted photo.
- Views: front only for the base rig. Side/back/3-4: UNAVAILABLE (kneeling, walking, and sitting-at-desk side poses exist but no turnaround).
- Pose changes are swaps of a whole drawing on the ledger (POSE entering class: 230 states, 4.9%; MEASURED), not smooth interpolation. INFERRED: stick figures are limited-animation cut-outs that are re-posed, a pivot rig is feasible.

**2b. Variant kit on top of the base rig (OBSERVED, `characters_variant_kit.jpg`, `.ids.txt`).** 237 distinct CH_/CHAR_ ids exist (MEASURED), most appearing in one video. They are the same body with modifiers: hair (spiky, curly brown, red, grey bob, ponytail, bald), face (glasses, sunglasses, pixel "deal with it" sunglasses, headband, beard), headgear (orange cap with logo, fedora/detective, hood/monk, soldier helmet, top hat, uncle-sam hat), clothes (green tie/scarf, suit and tie, apron, camouflage, striped sailor shirt), skin tone, and a held prop (magnifier, megaphone, laptop, clipboard, phone, lasso). INFERRED: one parameterised rig + modifier layers reproduces the channel better than designing 237 characters.
- Recurring named cast (ledger ids, MEASURED): CH_STICKMAN, CH_USA_MAP (67 states, 2 videos), CHAR_DAVE (38, 1 video, text label "Dave" with an arrow), CH_CHINA_MAP, CH_FOUR_NATION_FIGURES (4 costume figures), CH_RICH_MAN, CH_HOODED_FIGURE, CH_ROBOT_GREY (grey robot, red eyes, apron), CH_TEACHER, CH_DETECTIVE (fedora, magnifier), CH_BALD_MAN, CH_WOMAN_GREY.
- **2c. Anthropomorphic objects (OBSERVED, `characters_anthropomorphic.jpg`):** a green USA map with big white eyes and thin black stick legs/arms (expressions: calm, sunglasses, angry brows, "oh no"), a China map version, Earth with eyes, Bitcoin coin with limbs, bar-chart characters. They act as emotional "characters" in explainer beats.
- **2d. Layer B people (OBSERVED, `environments_full_bleed.jpg`):** crowds, businessmen at a boardroom table, a cashier and a customer, school kids: same peach round head and dot eyes but a thicker/darker outline, clothes, scene-integrated perspective. UNAVAILABLE: a turnaround for these; many look like individually illustrated panels.
- Expression set: neutral, smile, grin/laugh, worried, panic, angry (v-brows), sleeping (z z), shock (open mouth). Eye is always dots on stick figures; big white eyes with black pupils on maps/coins. No lip-sync (OBSERVED; mouth is one static shape per drawing).

## 3. Environment sheet
- Layer A has no environment: floor is a thin grey ground line or nothing (OBSERVED, `characters_core_stickman.jpg` tiles 4/6/24). Props and text float on white.
- Layer B scenes (OBSERVED, `environments_full_bleed.jpg`): 2D flat-fill panels, no real perspective camera. Typical backdrops: cream/beige room with one desk + black monitor + peach-head businessman; sky-blue with green grass and road; underwater blue gradient with anchors; grey school hall with lockers; boardroom with brown table; dark casino with neon text; supermarket interior. Vignette/gradient only rarely (one dark-to-white gradient frame).
- Recurring location: the desk with black monitor and a tie-wearing bald/peach-head man on a beige/grey wall, across several videos (OBSERVED, `audit1_environments.jpg` tiles 4, 20, 24).
- Lighting direction/shadows: UNAVAILABLE as a 3D property (flat fills; a faint contact shadow is only seen on the teacher/ground-line shots).
- Camera: static framing with cuts (CUT = 38.7% of state entries, MEASURED); push-ins are labelled CUT+ZOOM_IN 2.8% and POP_IN+ZOOM_IN 0.5% (MEASURED). A virtual orbit/parallax is not seen (INFERRED from the ledger classes and the sheets).
- Palette of scenes (MEASURED, `palette_full_bleed_scenes_chromatic.csv`): cream #F4E4C4 (10.7% of chromatic pixels), grass/map green #4CA44C (10.6%), sky blue #C4ECFC (9.4%), teal #64B4CC, sand #ECD4AC, brown #846444.

## 4. Graphics / typography sheet
- Hand-lettered black type for captions and bubbles (a rounded, slightly wobbly marker/hand font; family not identified: UNAVAILABLE, nearest guess a casual handwriting font, INFERRED); formal text cards in clean serif ("Chapter 1 / Blinded By Optimism" with an ornament rule) and a black sans for stats; bold red hand-drawn accents (arrows, circles, underline, X-outs, down-arrow zigzag) (OBSERVED, `audit1_props.jpg`).
- Chalkboard: green board (#4CA44C-family green with a brown wooden frame #846444) used for key terms in white chalk-style handwriting, with the pointer-holding stick man at its side (OBSERVED; OBJ_CHALKBOARD / OBJ_GREEN_CHALKBOARD ids in 3+ videos, MEASURED).
- Speech bubbles: white ellipse with a thick black outline and a tail, hand-lettered text, sometimes in red for emphasis (OBSERVED).
- Real-world inserts: screenshot/chart/article/logo/photo/meme (OBSERVED). Charts mostly supplied pictures, some redrawn on cream with beige bars.
- Entry behaviour (MEASURED, `entering_class_counts.csv`): POP_IN 27.2% of states, TEXT_SWAP 2.1%, TEXT_TYPE <0.2%, DRAWON <0.1%, SLIDE_IN/RISE_IN rare. Most words are placed as part of a whole new frame or popped in.
- Text timing against audio: UNAVAILABLE (audio unverified).
- Safe margins: sparse centred layouts, text kept well inside the frame on both 16:9 and 9:16 (OBSERVED, no measurement).

## 5. Rhythm (MEASURED from state ledgers, `rhythm_by_video.csv`)
- Median gap between consecutive visual states per video: Shorts 0.67-1.00 s (60-86 states/min); busiest long-form 1.04-1.4 s (about 40-55 states/min: Xkk9GnnJHBg 1.04, dPoDyl9Ys38 1.25, WCS1bK3KB3U 1.33, KTnp2OlQJHA 1.23); calmer long-form 2.2-3.3 s (17-25 states/min: 7K991LgY3tc, DKyJABtbF2o, Im-N3K9Pnf0, dlBhLhn8lL0, o3FQcd91MIs).
- State = a verified visual change (new cut, pop-in, pose, text swap). It is not a "shot length" in an editor sense.
- Entering mix across all 4,667 states: CUT 38.7%, POP_IN 27.2%, POSE 4.9%, CUT+ZOOM_IN 2.8%, CUT+MICRO 2.6%, CUT+ANIM 2.2%, TEXT_SWAP 2.1%.

## 6. Palette (MEASURED, sampled frames)
- Flat colours that identify the channel (chromatic share in white-canvas character/prop frames): peach skin #FCD4B4 18.1%, Bitcoin orange #EC9424 8.2%, money/map greens #7CB474, #3C843C, #4CA44C, parchment #E4DCBC; neutrals: pure black outline ~#040404 (about 10% of non-white pixels), greys for shadows/desk.
- Background: white (#FFFFFF family) in Layer A; cream #ECE4D4/#F4E4C4, sky #C4ECFC in Layer B.
- Files: `palette_*.csv` (hex + share), `palette_*.png` swatches. Sampling: 260 random frames per palette, 5-bit colour bins merged within 36 RGB units. Not calibrated against a colour chart.

## 7. Style bible, one page (rules that held in the frames I opened; each has counterexamples above)
1. White canvas is the default; add color only on the subject. 2. One black outline weight, hand-drawn wobble, flat fills, no gradients (exceptions: night/dark scenes, one vignette). 3. Peach round head + dot eyes + one-line limbs for all people, modifiers carry identity. 4. Anthropomorphic icons (maps, coins, Earth) are the emotional foil. 5. Evidence goes in as real screenshots/charts at native crispness, usually on white or a grey/cream plate. 6. Red marker marks (arrow/circle/X/underline) are the highlight system. 7. Sparse composition: 1-4 elements, lots of empty space. 8. Fast change: a new state every 1-3 s, mostly cuts and pop-ins, few camera moves.
