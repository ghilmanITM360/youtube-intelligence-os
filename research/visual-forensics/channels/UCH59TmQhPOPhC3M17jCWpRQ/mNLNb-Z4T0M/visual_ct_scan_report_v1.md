# Visual CT-scan report v1 — Barely Evolved mNLNb-Z4T0M
Title: The Most Miserable Time to Be Alive in Human History  
Source sha256: e6799e8f16ad31772020d98404f2c9cf90536a255c6169d29e838c55bd1dd061 (matches registry: True)  
Status: **VISUAL_ANALYSIS_PARTIAL**. CT_SCAN_COMPLETE not awarded: audible synchronization is BLOCKED_CAPABILITY (no listener), and visual coverage is sampled (native representatives + 8-frame strips), not all-frame inspection.

## Evidence classes
- MEASURED: FULL_FRAME_MEASUREMENTS.csv (every frame), detector candidates, PTS.
- OBSERVED: bounded sonnet reviewer reads (one image per Read call; transcript-verified via be_validate_batch.py), plus orchestrator native-frame checks in primary_corrections.csv.
- INFERRED: interpretation of intent / narration relation. ASR is machine transcription, not listening.

## Coverage
- States: 136 (tables/states_v1.csv). Art audit 136/136, prompts 136/136.
- Motion events (strip-observed): 192; types {"CHARACTER_MOTION": 37, "CAMERA_SCALE": 19, "ELEMENT_EXIT": 14, "NO_VISIBLE_CHANGE": 31, "ELEMENT_ENTER": 37, "TEXT_REVEAL": 12, "OTHER": 21, "FADE": 7, "CUT_WITHIN_STRIP": 5, "CAMERA_PAN": 9}.
- ASR segments related to visuals (PARTIAL, sampled frames only): 101/101; relations {"LITERAL": 70, "ILLUSTRATIVE": 22, "MIXED": 12, "CONTRADICTORY_JOKE": 1, "UNCERTAIN": 3}.
- Reviewer batches: b01, b02, b03, b04, b05, b06, b07, b08, b09; not validated: none.

## Primary corrections (orchestrator, separate from reviewer claims)
- PC-001 S053: CONFIRMED_WITH_ADDITION — OBSERVED at native resolution by orchestrator: confirmed; additionally the bread sits higher at f4936 and lower/landed at f4937 with the crack appearing the same frame (1-frame drop-impact gag). Diff pixels >60: 41090.
- PC-002 S080/S088 (also S082/S089 by same pattern): REVIEWER_INFERENCE_REJECTED_FOR_S080_S088 — MEASURED: every consecutive frame differs (f8181-8193 mean_abs_diff 7.2->10.2 peak f8185 ->1.5, then ~0 from f8194; f9138-9150 steady ~3.1-3.5). Continuous per-frame camera move (f8180s: accelerate then decelerate to res

## Motion grammar (from production_specs/specifications_v1.json)
- M_ELEMENT_ENTER_EXIT: 51 events in 39 states; median observed span 5 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 4, "drop_from_top": 3, "slide_from_side": 12, "typing": 1}
- M_CAMERA_SCALE_PAN: 28 events in 22 states; median observed span 8 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 1, "slide_from_side": 4}
- M_FADES: 7 events in 7 states; median observed span 8 frames (strip-bounded); keyword counts {}
- M_CHARACTER_MOTION_POSE: 37 events in 27 states; median observed span 8 frames (strip-bounded); keyword counts {}
- M_TEXT_REVEAL_SWAP: 17 events in 16 states; median observed span 4 frames (strip-bounded); keyword counts {"typing": 2, "word_swap": 4}
- M_HOLDS: 31 events in 28 states; median observed span 3 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 1}
- M_OTHER: 21 events in 20 states; median observed span 6 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 1, "slide_from_side": 2, "word_swap": 4}

## Narration relation (INFERRED, ASR-based, not listened)
Counts: {"LITERAL": 70, "ILLUSTRATIVE": 22, "MIXED": 12, "CONTRADICTORY_JOKE": 1, "UNCERTAIN": 3}. Literal illustration dominates in this sample; this is not a claim about audience response, CTR or retention.

## State ledger (abridged; full fields in tables/consolidated_art_audit.csv)
| state | frames | t (s) | characters/assets | camera | label |
|---|---|---|---|---|---|
| S001 | 0-1 | 0.00 | Bearded long-haired male protagonist (recurring), face only, fuzzy hair/beard texture, ear | Static extreme close-up in the single viewed frame; motion U | OBSERVED;MEASURED;INFERRED(eyes closed) |
| S002 | 2-14 | 0.07 | Same bearded protagonist, same face crop. | Locked-off close-up; background brightness appears different | OBSERVED;MEASURED;INFERRED(fade) |
| S003 | 15-58 | 0.50 | Bearded protagonist as a bust: large head, flat neck, hairy chest with two dot nipples, tw | Camera appears pulled back from S002's close-up between f4 a | OBSERVED;MEASURED |
| S004 | 59-63 | 1.97 | Bearded protagonist bust (recurring) plus a title word. | The scene shifts horizontally (character moves right, text e | OBSERVED;MEASURED;INFERRED(slide) |
| S005 | 64-100 | 2.14 | No character; only the title text. | f98 title spans x ~495-1465 and sits marginally higher than  | OBSERVED;MEASURED;INFERRED(slow scale) |
| S006 | 101-344 | 3.37 | Protagonist (bust on rectangular beige/red tunic, crown with gems, stick arms) on a gothic | f105 wide shot; f222 and f341 are closer and show the throne | OBSERVED;MEASURED;INFERRED(push-in) |
| S007 | 345-349 | 11.51 | Empty throne, partially visible hand at right edge, the word 'peasant'. | Cross-dissolve between the throne scene and the white text c | OBSERVED;MEASURED;INFERRED(dissolve) |
| S008 | 350-374 | 11.68 | None; 'peasant' text card. | Word is slightly larger at f372 (width ~755 vs ~720), sugges | OBSERVED;MEASURED |
| S009 | 375-489 | 12.51 | Protagonist (head and tunic in brown) appears at f487 and is lying sideways in the strip t | From f379 to f487 the house shifts left and gets slightly sm | OBSERVED;MEASURED;INFERRED(pull-out) |
| S010 | 490-750 | 16.35 | Interior props: sack bed, table with pots, barrel with bowl, shelves with jars, hanging he | Slight camera shifts between f494/f620/f747; strips show roo | OBSERVED;MEASURED |
| S011 | 751-824 | 25.06 | Isolated cutout animals on white: rooster, goat, pig; handwritten word 'maybe'. | Static white backdrop; animals move within frame. | OBSERVED;MEASURED |
| S012 | 825-877 | 27.53 | Protagonist, goat with bulging eye, roosters, shelves, stone ring, handwritten word 'dirt' | Tighter crop than S010; the camera appears to drift slightly | OBSERVED;MEASURED |
| S013 | 878-915 | 29.30 | Worm (pink with orange band), pebbles, cracks; no recurring characters. | Slight position/scale shift between frames (pebbles and crac | OBSERVED;MEASURED;INFERRED(slow pan) |
| S014 | 916-1054 | 30.56 | Protagonist, goat, roosters, table with pots, shelves, stone ring, barrel; window at far l | The room shifts horizontally between f920, f985 and f1051, s | OBSERVED;MEASURED;INFERRED(pan, haze) |
| S015 | 1055-1132 | 35.20 | Wooden window shutters, stone wall, tiny castle and cottage visible through gaps. | f1130 window slightly larger and higher than f1059, suggesti | OBSERVED;MEASURED;INFERRED(push-in) |
| S016 | 1133-1137 | 37.80 | Window with two shutter panels (recurring window motif) | Static centred front view (one frame only) | OBSERVED/MEASURED/INFERRED |
| S017 | 1138-1185 | 37.97 | Single dark shutter panel on white card; hand-drawn arrow | Static framing | OBSERVED/MEASURED/INFERRED |
| S018 | 1186-1189 | 39.57 | Window with shutters; right shutter semi-transparent | Static | OBSERVED/MEASURED/INFERRED |
| S019 | 1190-1354 | 39.71 | Window, two slatted shutters, tiny flies, distant cottage roof and castle visible through  | Locked-off front view with slight scale change (window large | OBSERVED/MEASURED |
| S020 | 1355-1428 | 45.21 | Thatched stone cottage, second cottage, castle with flag, moon | Locked-off wide shot; mild framing shift between f1359 and f | OBSERVED/MEASURED |
| S021 | 1429-1532 | 47.68 | Bearded man lying on straw sack bed (recurring protagonist-style peasant with stick limbs  | Locked-off side view; slight zoom or position difference f14 | OBSERVED/MEASURED |
| S022 | 1533-1598 | 51.15 | Straw pile; open sack | Static; scale of straw pile slightly changes | OBSERVED/MEASURED |
| S023 | 1599-1610 | 53.35 | Open burlap sack close crop | Extreme scale-up of sack from S022 (INFERRED zoom, not viewe | OBSERVED/MEASURED/INFERRED |
| S024 | 1611-1809 | 53.75 | Straw macro, ticks, fleas | Locked macro; apparent scale change at f1657 (strip) | OBSERVED/MEASURED |
| S025 | 1810-2093 | 60.39 | Bearded man on bed, then standing; sack bed with straw | Locked-off; push-in toward man by f2090 | OBSERVED/MEASURED |
| S026 | 2094-2166 | 69.87 | Family room cast: old woman, two boys, bearded man, black-bearded man; props (shelves, wel | Wide locked-off; slight zoom out f2098 to f2164 | OBSERVED/MEASURED |
| S027 | 2167-2192 | 72.31 | Word card | Static; text shrinks slightly | OBSERVED/MEASURED |
| S028 | 2193-2440 | 73.17 | Same cast; adds bald grey-bearded man | Pan then push-in with defocus | OBSERVED/MEASURED |
| S029 | 2441-2498 | 81.45 | Word card | Static | OBSERVED/MEASURED |
| S030 | 2499-2662 | 83.38 | Bearded man with slime splat; bald man | Close-up locked then pan right | OBSERVED/MEASURED |
| S031 | 2663-2815 | 88.86 | Recurring bearded narrator with round glasses, leaf skirt and stick arms/pointer stick (OB | Static-looking framing; board/frame position drifts slightly | OBSERVED (frames) / INFERRED (slow drift) |
| S032 | 2816-2856 | 93.96 | Thatched roof with grey brick chimney (cartoon, tight dark outline); red X; handwritten ca | Fixed camera; no zoom visible in strip. | OBSERVED |
| S033 | 2857-2939 | 95.33 | Roof close-up with bent pink pipe and grey smoke puff, then full cottage with shuttered wi | Zoom-out from close roof (f2861/f2881) to cottage (f2888, f2 | OBSERVED |
| S034 | 2940-3085 | 98.10 | Recurring bearded narrator with round glasses, leaf skirt and stick arms/pointer stick (OB | Frame/board scale changes across the three samples (board le | OBSERVED / INFERRED |
| S035 | 3086-3158 | 102.97 | Bald grey-bearded older villager in brown vest, stone/timber wall, straw sack at lower-lef | Slight zoom/pan: posts move apart (x~320 vs ~295) between f3 | OBSERVED |
| S036 | 3159-3349 | 105.41 | Clip-art set on white: shaggy dog on blue puddle, hairy armpit with sweat/bug, burnt log,  | Fixed camera; items scale down toward centre f3289-3296. | OBSERVED / INFERRED (sequence) |
| S037 | 3350-3497 | 111.78 | Brown-bearded villager (same design as later S038-S040), stone wall, timber posts, straw s | Near static; character head moves slightly (x~690->725->725) | OBSERVED |
| S038 | 3498-3665 | 116.72 | Green thumbs-up and red thumbs-down badges, handwritten headings, photo-style plate of ste | Fixed camera; layout rearranges between f3581 and f3631. | OBSERVED |
| S039 | 3666-3803 | 122.32 | Bearded villager (full body, red vest) and a second smaller smooth-faced character partly  | Camera pans/moves: shelves move left (x~1500 f3670 -> ~1180  | OBSERVED |
| S040 | 3804-3868 | 126.93 | Bearded villager; round wooden table with bowl of speckled stew (colour flecks). | Slight zoom-out/pan: table edges shift (table left x~265->25 | OBSERVED |
| S041 | 3869-3899 | 129.10 | Handwritten word on white. | Fixed. | OBSERVED |
| S042 | 3900-3944 | 130.13 | Recurring bearded narrator with round glasses, leaf skirt and stick arms/pointer stick (OB | Zoom out between f3904 and f3942 (board left edge x~370->360 | OBSERVED |
| S043 | 3945-4060 | 131.63 | Black iron cauldron with stew on wooden tripod over stone ring with fire, white bowl on st | Slow zoom-out: stump and ring shrink/shift (stump left x 90- | OBSERVED |
| S044 | 4061-4217 | 135.50 | Bearded villager as scale: two wooden plates on stick arms with captions. | Fixed. | OBSERVED |
| S045 | 4218-4221 | 140.74 | Villager at right edge, yellow grain bits at left edge. | Possible slide transition (states table lists entry K073 SLI | OBSERVED |
| S046 | 4222-4239 | 140.87 | v2_rev_b04:grain_pile: pile of small yellow-tan oval seeds plus ~25 loose seeds around it. | Flat 2D, no visible depth. On a blank background camera moti | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S047 | 4240-4243 | 141.47 | v2_rev_b04:roots_mound: pile of pale tan tapered roots on a dark brown soil ellipse with s | Single frame. Compared with S048 f4248 (cross-state, OBSERVE | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S048 | 4244-4306 | 141.61 | v2_rev_b04:roots_mound (as S047); v2_rev_b04:mouse: grey-brown cartoon mouse with pink ear | Locked frame, 2D; assets move across it. Strip f4257-f4264 ( | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S049 | 4307-4489 | 143.71 | v2_rev_b04:hut_set: interior with stone-block wall, two dark wooden posts, shelf of terrac | Hard cut in (K077). Scene shifts left ~65-70 px and the pot  | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S050 | 4490-4662 | 149.82 | v2_rev_b04:classroom_set: ochre wall, green board in thick brown frame holding a photo-lik | Frame appears to scale up slowly: board inset width ~930/946 | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S051 | 4663-4826 | 155.59 | v2_rev_b04:narrator_table: curly auburn-haired bearded man (no glasses here) in brown vest | Hard cut (K080). Slow scale-up: table left edge 305/290/280  | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S052 | 4827-4886 | 161.06 | No characters. Recurring asset: black hand-lettered word card on off-white background. | Locked 2D frame; no camera motion visible. | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S053 | 4887-5042 | 163.06 | v2_rev_b04:narrator_table and v2_rev_b04:stew_bowl and v2_rev_b04:spoon (as S051); v2_rev_ | Locked-ish frame; table left edge ~270 at all viewed frames; | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S054 | 5043-5161 | 168.27 | v2_rev_b04:weapon_rack: wooden horizontal rack holding two swords with wrapped grips and a | Locked 2D frame. Slight enlargement between f5047 and f5159: | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S055 | 5162-5251 | 172.24 | v2_rev_b04:narrator_table, v2_rev_b04:stew_bowl, v2_rev_b04:spoon, v2_rev_b04:bread_loaf,  | Locked; bowl left edge ~570 and pillars unchanged between f5 | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S056 | 5252-5406 | 175.24 | No characters. Recurring assets: title text MEDIEVAL BREAD RECIPE; plus sign; four ingredi | Locked 2D frame; mounds unchanged in position across strip f | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S057 | 5407-5547 | 180.41 | v2_rev_b04:narrator_table, v2_rev_b04:stew_bowl, v2_rev_b04:spoon, v2_rev_b04:bread_loaf,  | Hard cut (K089). Slight scale-up: left pillar 400-555 / 390- | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S058 | 5548-5643 | 185.12 | v2_rev_b04:flour_mound (as S056) with a v2_rev_b04:skull_sign (rough wooden plank with a w | Locked 2D frame; sign translates down ~140 px per frame (pol | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S059 | 5644-5667 | 188.32 | v2_rev_b04:wheat_field_landscape: flat-vector wheat field with rolling green/tan hills, sm | Locked frame; the two viewed frames are pixel-similar except | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S060 | 5668-5674 | 189.12 | v2_rev_b04:wheat_field_landscape (washed out) with v2_rev_b04:single_ear: one tall saturat | Single frame. Landscape appears shifted down ~45-60 px and w | OBSERVED (viewed frames); MEASURED (kmeans palette shares); INFERRED (marked in text) |
| S061 | 5675-5753 | 189.36 | v2_rev_b05:WHEAT_EAR (yellow wheat ear, later with purple ergot kernels) | Static locked-off full frame on white; no camera move infera | OBSERVED |
| S062 | 5754-5926 | 191.99 | v2_rev_b05:NARRATOR_CLASSROOM (bearded, glasses, shirtless hairy torso, pointer stick); v2 | Fixed medium-wide frame; slight push/scale on whole frame be | OBSERVED |
| S063 | 5927-5964 | 197.76 | none recurring; text-only card | Locked-off. | OBSERVED |
| S064 | 5965-6049 | 199.03 | v2_rev_b05:PEASANT_BEARD (bearded man, brown vest, laced shirt, stick arms); stew bowl, sp | Close-up fixed frame; no camera move. | OBSERVED |
| S065 | 6050-6119 | 201.87 | v2_rev_b05:TWO_TAVERN_MEN (blue-clothed and brown-vested short-haired men, identical face) | Slight frame scale/shift between the two frames (window and  | OBSERVED |
| S066 | 6120-6208 | 204.20 | v2_rev_b05:PEASANT_BEARD on white; water glass; speech bubble | Static locked-off frame; man stays near centre in native fra | OBSERVED |
| S067 | 6209-6416 | 207.17 | v2_rev_b05:RIVER_TOWN_SCENE (river, hills, town, trees); labels 'parasites','animal waste' | Fixed frame with slight slow scale/drift in strip (backgroun | OBSERVED |
| S068 | 6417-6454 | 214.11 | none; text-only cards | Locked-off. | OBSERVED |
| S069 | 6455-6618 | 215.38 | v2_rev_b05:NARRATOR_CLASSROOM; board pictures (brewing manuscript-style picture, parchment | Frame slowly scales/shifts (poster crops differently across  | OBSERVED |
| S070 | 6619-6902 | 220.85 | v2_rev_b05:WOODEN_MUG_PHOTO (photo-like mug); glass beer mug photo; 'middle ages' sign; 's | Locked-off; objects slide (strip). | OBSERVED |
| S071 | 6903-7167 | 230.33 | v2_rev_b05:PEASANT_BEARD; wooden banded mug; round table | Close-up; slow scale/shift of frame (post positions drift) b | OBSERVED |
| S072 | 7168-7176 | 239.17 | v2_rev_b05:PEASANT_BEARD; table | Frame zoomed in closer than S071. | OBSERVED |
| S073 | 7177-7414 | 239.47 | v2_rev_b05:PEASANT_BEARD (large); spear; thought bubble with stew bowl; words 'deep','twis | Camera zoom/crop changes between f7295 and f7411 (man smalle | OBSERVED |
| S074 | 7415-7421 | 247.41 | v2_rev_b05:PEASANT_BEARD; spear; ghosted bowl | Interior zoomed closer than S075. | OBSERVED |
| S075 | 7422-7557 | 247.65 | v2_rev_b05:PEASANT_BEARD; round table; 'Medieval Problem #931' wooden sign | Camera static; scene scales slightly across frames. | OBSERVED |
| S076 | 7558-7624 | 252.19 | v2_rev_b06:A01 bearded long-haired man with round glasses and bare hairy chest (lecturer v | Static framing in both frames; between frames board/poster s | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S077 | 7625-7689 | 254.42 | None; text-only card. | Locked frame; text moves only. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S078 | 7690-8021 | 256.59 | v2_rev_b06:A06 bearded curly-haired man in brown laced tunic (tall rectangular torso, stic | Camera pans laterally across the room between the three nati | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S079 | 8022-8060 | 267.67 | None; text-only card. | Locked frame. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S080 | 8061-8405 | 268.97 | A13 muddy medieval street with thatched houses, arched door, castle on green hill (recurs  | Camera moves between frames (houses closer/shifted from f806 | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S081 | 8406-8468 | 280.48 | v2_rev_b06:A15 green-brown puddle icon with grass and red bug dots; A16 cartoon skull; bla | Locked frame. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S082 | 8469-8628 | 282.58 | A13 street; A06 bearded man; A14 grey-haired elder in green leaning from upper window hold | Camera lowered and tilted; f8473 to f8548 to f8625 successiv | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S083 | 8629-8688 | 287.92 | A14 elder in window holding bucket, castle, thatch roofs. | Close crop, slight push between f8633 and f8686 (window move | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S084 | 8689-8735 | 289.92 | None; text-only card. | Locked frame. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S085 | 8736-8793 | 291.49 | A06 bearded man; A13 street with doorway; mouse on street and in his hand. | Slow push-in/pan between f8740 and f8791 (man larger, castle | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S086 | 8794-8917 | 293.43 | A01 lecturer man; A02 chalkboard; A03 pointer; A04 projector; A05 poster; v2_rev_b06:A22 f | Static camera. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S087 | 8918-9107 | 297.56 | v2_rev_b06:A18 village square with sludge pool, dead rats, bones, skulls, rubbish; A06 bea | Camera slight push and pan between samples; strips show stab | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S088 | 9108-9173 | 303.90 | v2_rev_b06:A19 rainy village street with houses, trees, puddles, rats, bones, skulls, rubb | Slow push-in; strip shows step at f9143. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S089 | 9174-9229 | 306.11 | v2_rev_b06:A20 same street as S088 recolored warm yellow with steam wisps; rats, bones, pu | Slow push toward right; strip shows small shift at f9202. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S090 | 9230-9324 | 307.97 | A13 street with castle; v2_rev_b06:A21 two young figures (boy in blue collar tunic, man in | Camera moves between frames; strip frames closer. | OBSERVED (images); MEASURED (palette shares from rep_frames_b06.csv) |
| S091 | 9325-9430 | 311.14 | Grey-curly-haired elderly figure with bucket (rectangular green-brown tunic body, stick ar | Fixed wide shot; between f9329 and f9428 hills, town and fig | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S092 | 9431-9528 | 314.68 | Walled medieval town (tower with flag, crosses, red roofs) isolated on white; two green mi | Fixed framing; horizontal content slide leftwards during str | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S093 | 9529-9662 | 317.95 | Three green microbe drawings (blobby with nubs; rod with spikes; curved comma with flagell | Fixed framing. | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S094 | 9663-9843 | 322.42 | Bearded glasses figure with hairy torso (rectangular body, stick arms, green leaf-like gar | Camera drifts closer between f9667, f9753, f9840 (board and  | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S095 | 9844-10016 | 328.46 | Grey-curly-haired figure in green tunic; second identical small figure at distance in f984 | Camera appears to push in progressively: figure larger and m | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S096 | 10017-10197 | 334.23 | Map of Europe on parchment, hanging wooden sign, skull icons (emoji-like). | Fixed framing at native-frame level; sign drops in strip fra | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S097 | 10198-10312 | 340.27 | Bearded glasses figure, evolution poster, chalkboard, projector, pointer stick. | Camera shifted slightly between f10202 and f10310 (board lef | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S098 | 10313-10629 | 344.11 | Wooden bucket with dark sludge, burlap hay sack, tiny yellow marks; bearded figure lying o | Frame changes between f10317 (empty barn) and f10471 (figure | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S099 | 10630-10656 | 354.69 | No characters; single word. | Fixed. | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S100 | 10657-10831 | 355.59 | Bearded man-bun figure in dark robe at desk; hanging banner 'Barely Evolved Infirmarium';  | Camera appears to push in across f10661 to f10828 and in the | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S101 | 10832-10950 | 361.43 | Black-robed bearded figure with bun and belt; label; crown; bishop's mitre; arrows; text. | Fixed framing; objects slide off rightwards. | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S102 | 10951-11028 | 365.40 | Dark-haired figure in brown vest behind table; workshop; shelves with bottles; arched door | Frame scale and crop change between the two frames (more cei | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S103 | 11029-11032 | 368.00 | Same dark-haired figure now full-body (red spots on vest); faded workshop. | Fade to white. | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S104 | 11033-11151 | 368.13 | Dark-haired figure; scissors, tooth, bowl of dark red liquid, knife. | Fixed. | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S105 | 11152-11158 | 372.11 | Same figure over low-opacity workshop. | Dissolve between white and workshop. | OBSERVED (image content); MEASURED (palette); INFERRED (camera/transition mechanism) |
| S106 | 11159-11254 | 372.34 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | f11163 wide; f11252 tighter with room scaled up; strip shows | OBSERVED (arrow, push-in); INFERRED (arrow emphasises bucket). |
| S107 | 11255-11528 | 375.54 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | Static tight close-up across f11259-11525 with slight scale  | OBSERVED; INFERRED (gag about soap). |
| S108 | 11529-11766 | 384.68 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | Wide at f11533/f11647, push-in/zoom with slight table enlarg | OBSERVED; INFERRED (wipe start). |
| S109 | 11767-11769 | 392.63 | Parchment scroll graphic; no characters. | Static in single sampled frame; 3-frame state (f11767-11769) | OBSERVED |
| S110 | 11770-12093 | 392.73 | Parchment scroll; four coloured fluid blobs (red, green, yellow, dark brown) as recurring  | Parchment crops/pans: border visible at f11774, cropped tigh | OBSERVED; INFERRED (sequential reveal). |
| S111 | 12094-12125 | 403.54 | White card with text only. | Static (strip peak diff 1.06 = near zero). | OBSERVED |
| S112 | 12126-12449 | 404.60 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | Static framing across f12130-12287, slight shift by f12446;  | OBSERVED; INFERRED (censor hides cutting). |
| S113 | 12450-12687 | 415.42 | bearded curly-haired character in brown-red robe (recurring "patient") and the same figure | Layout slide left across f12514-12518; gauge enters. | OBSERVED; INFERRED (infographic of blood loss). |
| S114 | 12688-13002 | 423.36 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | Static to slightly wider/closer shifts between f12692, f1284 | OBSERVED; INFERRED (tasting urine gag). |
| S115 | 13003-13041 | 433.87 | No characters; TV colour-bar test pattern stock-like graphic. | Glitch tearing and roll in strip f13028-13030 then stable ba | OBSERVED |
| S116 | 13042-13154 | 435.17 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | Strip f13133-13140 shows small drift; f13152 doctor position | OBSERVED; INFERRED (doctor repositioning). |
| S117 | 13155-13306 | 438.94 | Shelf background; leech jar; doctor entering from left. | Static shelf background across f13159-13303; no camera move  | OBSERVED |
| S118 | 13307-13429 | 444.01 | Torso of patient with bandage; olive-green leeches as recurring prop. | Extreme close-up; slight scale/crop differences between f133 | OBSERVED; INFERRED (leeches slowly move). |
| S119 | 13430-13523 | 448.11 | Classroom set: chalkboard, desks, projector, poster; bearded glasses character with leaf l | Slight shift of board/desk positions between f13434 and f135 | OBSERVED |
| S120 | 13524-13961 | 451.25 | dark-haired receding-hairline character with oversized head on a rectangular beige jacket  | Framing pushes in toward f13958; strips show small shifts an | OBSERVED; INFERRED (word reading from tiny low-res tiles). |
| S121 | 13962-14173 | 465.87 | Dark-haired man (left, leaning over), bearded reclining figure (head plus bare torso lying | Locked frame: shelf, table, bucket at same positions in f140 | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S122 | 14174-14403 | 472.94 | Bearded teacher with round glasses and hairy bare torso with green leaf skirt (right), bla | Slow push-in suggested: board frame left edge x~240->225->21 | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S123 | 14404-14465 | 480.61 | Bearded man in brown vest, bald man in olive tunic with orange stain (enters from right),  | Framing widens between f14432 and f14433 (strip): huts appea | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S124 | 14466-14551 | 482.68 | Bearded man (right edge, head cropped at top), iron cauldron of stew on tripod over small  | Slight push-in: tripod legs 405-1610 -> 380-1630 (f14470->f1 | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S125 | 14552-14581 | 485.55 | No characters; hand-written text and green check mark; a soil mound with sprouts appears a | No camera motion; layout shift by element slide between f145 | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S126 | 14582-14713 | 486.55 | Brown soil mound with withered golden sprouts, dead cow (X eyes) lying, scowling bald man  | Upward scroll/move of entire group beginning f14707, almost  | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S127 | 14714-14793 | 490.96 | Bearded man in brown vest with ground shadow on white; hand-lettered word 'witch' and blac | No camera motion identified; character slides left (OBSERVED | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S128 | 14794-14970 | 493.63 | Bearded man (brown vest), grey-haired old villager and bald villager in olive tunics with  | Framing changes: f14798 and f14967 closer/shifted vs f14882  | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S129 | 14971-15128 | 499.53 | Bearded man tied by raised stick arms to a wooden post with crossbar; moustached villager  | Slow push-in across f14975, f15049, f15125: bell tower y 85- | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S130 | 15129-15172 | 504.80 | No characters; word 'Wrong' then 'answer'. | None. | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S131 | 15173-15395 | 506.27 | Same town-square set and five villagers around the tied man. | Push-in/reframe with stepped jumps (strips f15232->f15233 an | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S132 | 15396-15763 | 513.71 | Bearded man (brown vest) and moustached villager (olive tunic) by a rainy pond; trees, bus | Slow reframing: right tree trunk x~1715->1780->1815 across f | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S133 | 15764-16040 | 525.99 | Teacher in glasses at right with leaf skirt; board with picture of bridge, crowd, clergy a | Slow push-in: picture width 943->948->955 px (f15768,f15902, | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S134 | 16041-16104 | 535.23 | No characters; thatched stone cottage with double wooden door, windows, moon, second cotta | Slow push: moon x 1665->1685 and cottage edge enlarges f1604 | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S135 | 16105-16478 | 537.37 | Bearded man lying on straw-filled sack bed, small white tuft at neck, shuttered window wit | Slow push-in: shutter span 1020->1080 px f16109->f16475 (OBS | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |
| S136 | 16479-16688 | 549.85 | Teacher half behind stone block table with bowl; board with chalk 'subscribe'; parchment s | Slow push-in/drift: sign left edge 1490->1500->1510 and sign | OBSERVED (listed images); MEASURED (palette, state ranges); INFERRED (only where stated) |

## Not established
- Fonts, software, layer stacks, easing curves, sound design: UNAVAILABLE.
- Audio sync, SFX placement, music: BLOCKED_CAPABILITY.
- Interiors of long states between sampled frames: not inspected.
- Any retention/CTR explanation: not inferred.
