# Visual CT-scan report v1 — Barely Evolved GNaBxt_zIRA
Title: How to Survive a Fight Against Prehistoric Animals  
Source sha256: cbe7a3afac6c6b7b13db10b7ce2493715f5299208d6f3ebffb7fd74e2bf5c0f7 (matches registry: True)  
Status: **VISUAL_ANALYSIS_PARTIAL**. CT_SCAN_COMPLETE not awarded: audible synchronization is BLOCKED_CAPABILITY (no listener), and visual coverage is sampled (native representatives + 8-frame strips), not all-frame inspection.

## Evidence classes
- MEASURED: FULL_FRAME_MEASUREMENTS.csv (every frame), detector candidates, PTS.
- OBSERVED: bounded sonnet reviewer reads (one image per Read call; transcript-verified via be_validate_batch.py), plus orchestrator native-frame checks in primary_corrections.csv.
- INFERRED: interpretation of intent / narration relation. ASR is machine transcription, not listening.

## Coverage
- States: 113 (tables/states_v1.csv). Art audit 113/113, prompts 113/113.
- Motion events (strip-observed): 173; types {"CHARACTER_MOTION": 49, "TEXT_REVEAL": 15, "ELEMENT_ENTER": 23, "CAMERA_PAN": 20, "CAMERA_SCALE": 13, "OTHER": 14, "NO_VISIBLE_CHANGE": 16, "FADE": 4, "ELEMENT_EXIT": 18, "CUT_WITHIN_STRIP": 1}.
- ASR segments related to visuals (PARTIAL, sampled frames only): 172/172; relations {"ILLUSTRATIVE": 35, "LITERAL": 64, "UNCERTAIN": 58, "MIXED": 12, "LITERAL_TEXT_ECHO": 3, "ILLUSTRATIVE_SETTING": 1, "CONTRADICTORY_JOKE": 2, "LITERAL_ACTION": 1, "UNRELATED_HOLD": 2}.
- Reviewer batches: b01, b02, b03, b04, b05, b06, b07a, b07b; not validated: none.

## Primary corrections (orchestrator, separate from reviewer claims)
- PC-001 S015: CORRECTION_APPLIES — OBSERVED by orchestrator: f2076 inset is smaller; f2077-f2078 larger than f2079-f2080 (scale-up with overshoot then settle, same pop pattern as uPQ M3). Collapse-out f2073-f2075 agreed.
- PC-002 S016: REVIEWER_CLAIM_REJECTED — OBSERVED by orchestrator: f2803 shows the same meadow and trees with the sloth (head turned) plus man and rock; boundary review K039-K041 (man enters, throws rock, rock lands) and measurements show no D1 cut 2511-2806 (m

## Motion grammar (from production_specs/specifications_v1.json)
- M_ELEMENT_ENTER_EXIT: 41 events in 30 states; median observed span 5 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 1, "slide_from_side": 12, "typing": 2}
- M_CAMERA_SCALE_PAN: 33 events in 29 states; median observed span 8 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 1, "slide_from_side": 4, "typing": 1}
- M_FADES: 4 events in 4 states; median observed span 6 frames (strip-bounded); keyword counts {}
- M_CHARACTER_MOTION_POSE: 49 events in 40 states; median observed span 8 frames (strip-bounded); keyword counts {"slide_from_side": 3, "word_swap": 1}
- M_TEXT_REVEAL_SWAP: 16 events in 16 states; median observed span 3 frames (strip-bounded); keyword counts {"overshoot_or_bounce": 2, "drop_from_top": 1, "typing": 4}
- M_HOLDS: 16 events in 12 states; median observed span 8 frames (strip-bounded); keyword counts {}
- M_OTHER: 14 events in 14 states; median observed span 7 frames (strip-bounded); keyword counts {"drop_from_top": 1}

## Narration relation (INFERRED, ASR-based, not listened)
Counts: {"ILLUSTRATIVE": 35, "LITERAL": 64, "UNCERTAIN": 58, "MIXED": 12, "LITERAL_TEXT_ECHO": 3, "ILLUSTRATIVE_SETTING": 1, "CONTRADICTORY_JOKE": 2, "LITERAL_ACTION": 1, "UNRELATED_HOLD": 2}. Literal illustration dominates in this sample; this is not a claim about audience response, CTR or retention.

## State ledger (abridged; full fields in tables/consolidated_art_audit.csv)
| state | frames | t (s) | characters/assets | camera | label |
|---|---|---|---|---|---|
| S001 | 0-143 | 0.00 | Hunter figure (round head, rectangular torso, stick arms, leaf-fur loincloth); grey long-n | Static wide frame across f4-f140; bird scale differs from f7 | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S002 | 144-262 | 4.80 | Mammoth with spear(s) in its back; three or more spear-carrying hunters (same simple body  | Static framing at f148 and in strip; f260 same scene with bl | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S003 | 263-371 | 8.78 | Black silhouettes of ground sloth, eagle, bird, mammoth, bear on a five-tick timeline; han | Static frame; no camera move seen. | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S004 | 372-451 | 12.41 | Bearded, glasses-wearing lecturer behind stone lectern; chalkboard; wall posters (evolutio | Wide frame, slight scale difference between f376 and f449 (I | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S005 | 452-533 | 15.08 | Same silhouettes; later colour brown ground sloth; handwritten "5". | Pan and slight zoom across f466-f473 (strip). | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S006 | 534-592 | 17.82 | Lecturer, extreme close-up. | Tight close-up frame; f538 and f590 look identical in layout | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S007 | 593-827 | 19.79 | Lecturer in leaf skirt (f597 only), dim basement lab, machine with button light, shelves,  | Static f597/f710; strong radial blur and push toward machine | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S008 | 828-871 | 27.63 | Lecturer at right edge; blue circular logo with white "mnn" and grey "mother nature networ | Close crop, static between f832 and f869. | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S009 | 872-1062 | 29.10 | Lecturer in white coat with blue goggles, orange flask, lab bench with coloured glassware, | Slow gradual push-in across f876-f1059 (INFERRED from scale  | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S010 | 1063-1261 | 35.47 | Pod with pale blob creature and cables; circular platform; lecturer joins. | Slow push-in across f1067-f1258 (INFERRED). | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S011 | 1262-1515 | 42.11 | Cartoon sloth, giant realistic sloth. | Zoom-out reveal across f1384-f1391 and later. | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S012 | 1516-1660 | 50.58 | Lecturer, chalkboard text, projector, desk. | Pull-back/pan across f1580-f1657 (INFERRED). | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S013 | 1661-1708 | 55.42 | Giant sloth, lecturer, red "VS", crack line. | Static camera; VS slam via scale. | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S014 | 1709-1987 | 57.02 | Lecturer, giant sloth from behind, trees, bush. | Pan/shift left across f1766-f1773 and further in f1848. | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S015 | 1988-2148 | 66.33 | Lecturer with leaf skirt; two inset images on board. | Static camera. | OBSERVED (images opened); palette MEASURED (kmeans); interpretation INFERRED |
| S016 | 2149-2806 | 71.70 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Static wide frame, no camera movement seen in f2153; f2477 s | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S017 | 2807-2927 | 93.66 | Sloth head and shoulder only; blurred trees | Static extreme close-up; very slow drift of head position (< | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S018 | 2928-3007 | 97.70 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Static wide frame; rock and sloth shift by a few px between  | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S019 | 3008-3109 | 100.37 | Sloth forearms and claws cropped on white; measurement bracket | f3107 slightly more zoomed than f3012 (claw tips x ~810 vs ~ | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S020 | 3110-3229 | 103.77 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Static wide frame; no camera move observed (strip: only slot | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S021 | 3230-3276 | 107.77 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Tight side tracking-type framing; background trees shift hor | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S022 | 3277-3468 | 109.34 | bearded stick-limbed man: hairy-textured head on a plain cylinder torso with black line ar | Wide to zoomed view with pan toward man f3315-3320 (strip);  | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S023 | 3469-3564 | 115.75 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Tight profile with scrolling blur background; no zoom seen | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S024 | 3565-3630 | 118.95 | bearded stick-limbed man: hairy-textured head on a plain cylinder torso with black line ar | Static wide frame | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S025 | 3631-3724 | 121.15 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Static high wide camera | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S026 | 3725-3866 | 124.29 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Close two-shot static camera; strip shows no pan; blur backg | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S027 | 3867-3960 | 129.03 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Static high wide camera | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S028 | 3961-3979 | 132.17 | None | None | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S029 | 3980-4040 | 132.80 | sloth-like large brown furred creature with long pale claws (INFERRED: ground-sloth-type a | Static high wide camera | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S030 | 4041-4066 | 134.83 | None | None | OBSERVED for all visual descriptions in frames_viewed; INFERRED for species/role/intent |
| S031 | 4067-4145 | 135.70 | Giant sloth-like brown animal and tiny bearded loincloth figure (recurring narrator charac | Static high wide shot; characters move within it. | OBSERVED (layout/positions); INFERRED (chase) |
| S032 | 4146-4362 | 138.34 | Large brown furry ground sloth lying down; narrator character (bearded, long hair, leaf sk | Wide mid shot; at f4320-4327 lateral pan left-to-right scene | OBSERVED; MEASURED palette |
| S033 | 4363-4439 | 145.58 | Colour cartoon sloth, silhouetted eagle, silhouetted flightless bird, silhouetted mammoth, | Whole row pans leftward with decelerating displacement acros | OBSERVED |
| S034 | 4440-4548 | 148.15 | Single brown eagle (white tail patches, orange beak and feet, black talons); no narrator. | Slow scale increase over f4453-4460 and onward (eagle grows  | OBSERVED; MEASURED palette |
| S035 | 4549-4619 | 151.78 | Stylised map: Australia, Indonesian archipelago, Pacific islands, New Zealand; pink map pi | Pan toward NZ with zoom-in, continuous over f4569-4576 (OBSE | OBSERVED; MEASURED palette |
| S036 | 4620-4677 | 154.15 | Narrator character (bearded, round glasses, curly red-brown hair, chest hair), projector,  | Slow push-in (narrator and board grow between f4624 and f467 | OBSERVED; MEASURED palette |
| S037 | 4678-4882 | 156.09 | Warrior (long black hair, fur-trim cape, grass skirt) with spear; later eagle. | Gradual slow camera drift/zoom between f4682 and f4780 (hill | OBSERVED |
| S038 | 4883-5016 | 162.93 | Same brown eagle on white; '33 lbs (15 kg)' label. | Upward slide of entire eagle+label out of top by f5014 (OBSE | OBSERVED |
| S039 | 5017-5138 | 167.40 | Front-facing spread-wing eagle with white bellybutton patch; measure bar. | Eagle ascends and settles f5020-5024 then stays (OBSERVED). | OBSERVED |
| S040 | 5139-5269 | 171.47 | Narrator, projector, desk, stool, chalkboard bearing a framed painting (eagle attacking tw | Slow push-in: painting width 876->890->905 px across f5143/5 | OBSERVED; MEASURED sizes |
| S041 | 5270-5510 | 175.84 | Large long-necked brown flightless bird (moa-like); forest clearing; label '440 lbs (200 k | Slow camera drift/scale: background elements shift between f | OBSERVED |
| S042 | 5511-5637 | 183.88 | Eagle in flight, side view. | Locked eagle position, clouds scroll, giving parallax of mot | OBSERVED |
| S043 | 5638-5707 | 188.12 | Perched brown eagle; label '4-inch talons (11 cm)'. | Slow scale increase (f5645-5652) and drift. | OBSERVED |
| S044 | 5708-5811 | 190.46 | Narrator, chalkboard with moa-like bird plus semi-transparent bone overlay (spine, pelvis) | Strong push-in: poster exposes more letters as board enlarge | OBSERVED |
| S045 | 5812-5908 | 193.93 | Moa-like bird; eagle; rocks, ferns. | Scene position shifts between f5816 and f5906 and within str | OBSERVED |
| S046 | 5909-6051 | 197.16 | Four peg-bodied villagers with oversized heads and stick arms (headband man, bun-haired fi | Static eye-level wide shot; between f5913 and f5980/f6048 th | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S047 | 6052-6281 | 201.94 | Headband villager with wooden basket (reused character design from S046), large brown eagl | Daytime wide shot; scene shifts framing across f6056, f6166, | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S048 | 6282-6363 | 209.61 | Bearded spectacled teacher figure (peg body, hairy torso, leaf skirt), stone lectern with  | Close wide-medium shot; framing moves between f6286 and f636 | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S049 | 6364-6542 | 212.35 | Same bearded figure (without glasses, leaf skirt) alone in meadow; trees, mountain, rock p | Static wide shot; at f6429-6434 strip background gets blurre | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S050 | 6543-6615 | 218.32 | No characters; sky with cloud band, conifers, hills. | Frames show cloud band and trees at different positions (f65 | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S051 | 6616-6719 | 220.75 | Bearded figure in meadow, brown eagle entering from top. | Static wide shot with possible slight scale/translation of b | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S052 | 6720-6815 | 224.22 | Leafy branch, grey backpack, headband villager (same design as S047). | Locked-off white frame; items move horizontally (strip f6767 | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S053 | 6816-6974 | 227.43 | Teacher with glasses, stone lectern, bowl, wooden club, poster, pointer stick. | Continuous push-in: teacher head grows from f6820 to f6971;  | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S054 | 6975-7241 | 232.73 | Same bearded figure in meadow, brown eagle. | Static wide with small oscillations; strip frames at 7143 an | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S055 | 7242-7443 | 241.64 | Teacher (right), blackboard used as projection screen, three real-looking painted illustra | Static classroom shot with slight push; strips show image 'u | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S056 | 7444-7520 | 248.38 | Evolution-timeline graphic: numerals 5,4,3, tick bar, coloured sloth, eagle, grey bird, bl | Strip shows leftward decelerating slide of entire graphic (f | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S057 | 7521-7699 | 250.95 | Teacher, desks, stools, projector, evolution poster with three-stage figures, pointer. | Push-in from wide to close across f7525, f7610, f7696; strip | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S058 | 7700-7743 | 256.92 | Large grey terror-bird with yellowish hooked beak, tan chest, scaly legs. | Locked-off frame; the bird enters from right over about 8 fr | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S059 | 7744-7891 | 258.39 | Americas map in green on cyan, grey terror birds (1 then 8), 'LAKES' blob. | Map zoomed over frames; vignette darkens edges from f7801. | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S060 | 7892-7901 | 263.33 | Same map, birds and caption as S059 end. | Slide wipe type per states table (MEASURED); one frame viewe | OBSERVED (frames) + MEASURED (palette kmeans, frame numbers) |
| S061 | 7902-8124 | 263.66 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Static wide framing; left acacia canopy and hill lines diffe | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S062 | 8125-8172 | 271.10 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Slow scale difference: board frame left edge x~123 in f8129  | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S063 | 8173-8384 | 272.71 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | White cut-out layout; bird position and scale differ between | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S064 | 8385-8488 | 279.78 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | Backdrop trees shift rightward across strip f8399-8406 (INFE | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S065 | 8489-8494 | 283.25 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | Static. | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S066 | 8495-8667 | 283.45 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | Close crop of head versus S063 full body; head position simi | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S067 | 8668-8873 | 289.22 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | Static wide framing across samples. | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S068 | 8874-8951 | 296.10 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Static near-frontal framing; no scale change evident between | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S069 | 8952-9402 | 298.70 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Background composition changes between samples (INFERRED pan | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S070 | 9403-9448 | 313.75 | Brown soil mound with texture specks; grass backdrop; black limb silhouette (identity uncl | Static extreme close-up. | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S071 | 9449-9530 | 315.28 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Static wide; bird head moves rather than camera. | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S072 | 9531-9605 | 318.02 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | Close crop; between f9535 and f9603 head and tree shifts lef | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S073 | 9606-9716 | 320.52 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Camera and framing change between f9610 and f9714 (narrator  | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S074 | 9717-9807 | 324.22 | Large grey flightless bird with hooked tan/dark beak, cream neck panel, fine-line feather  | Bokeh-like blur INFERRED simulated depth of field; no camera | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S075 | 9808-9882 | 327.26 | Recurring bearded cartoon narrator: tall log-shaped hairy torso, leaf skirt, thin black li | Board larger at f9880 than f9812: INFERRED slow push-in. | OBSERVED (images opened); palette MEASURED (kmeans); in-state change inferences marked INFERRED |
| S076 | 9883-9989 | 329.76 | Large gray flightless bird with pale neck patch and olive beak shown twice (standing, and  | Static framing; no camera move visible | OBSERVED |
| S077 | 9990-10052 | 333.33 | Horizontal numbered timeline with five animals: ground sloth, eagle, gray flightless bird, | Horizontal pan left over f9994-10001 (strip) and continuing  | OBSERVED |
| S078 | 10053-10352 | 335.44 | Teacher character: bearded bespectacled long-haired shirtless head on a stick body behind  | Gradual zoom-in/crop drift between f10057 and f10202 (OBSERV | OBSERVED |
| S079 | 10353-10634 | 345.45 | Large woolly brown mammoth with ivory tusks; teacher character in leaf skirt with a spear  | Static background in viewed frames, no camera move seen | OBSERVED |
| S080 | 10635-10707 | 354.85 | Dead mammoth with red blood patch; five small tribal figures with spears | Static framing in both frames | OBSERVED |
| S081 | 10708-10801 | 357.29 | Teacher at right behind stone desk; projector; board projections (cave-art mammoth then ex | Camera slightly different between f10712 and f10799 (board a | OBSERVED |
| S082 | 10802-10895 | 360.43 | Photographed curved bone with scratch marks; arrow; handwritten label | Slow scale-in: bone larger at f10893 than f10806 | OBSERVED |
| S083 | 10896-11006 | 363.56 | Teacher and pointer; board illustration of bone-framed domed huts on steppe | Slow camera zoom-out visible (board border moves out) | OBSERVED |
| S084 | 11007-11138 | 367.27 | Dead mammoth with five tribal figures around it, one on its back | Camera drifts: mountain peak moves from about (290,130) to ( | OBSERVED |
| S085 | 11139-11393 | 371.67 | Teacher full length with leaf skirt, pointer, projector, evolution poster, laptop, sign, b | Camera pan right across f11266-11273, closer crop by f11390 | OBSERVED |
| S086 | 11394-12335 | 380.18 | Video-site UI with cartoon video of two tribal men; red subscribe button; cursor | Inner video pan (f11709-11716) and cut at f11795/f11796 | OBSERVED |
| S087 | 12336-12403 | 411.61 | Teacher, laptop, bowl, club | Slight zoom between f12340 and f12401 | OBSERVED |
| S088 | 12404-12590 | 413.88 | Hanging wooden sign; typed list lines | Sign shifts up about 10 px between f12408 and f12497 (OBSERV | OBSERVED |
| S089 | 12591-12779 | 420.12 | Gray boulder with etched bearded figure, shells and bones; rope posts; tourist in hat with | Slow zoom-in suggested by larger boulder at f12776 | OBSERVED |
| S090 | 12780-12939 | 426.43 | Teacher character on cliff, mammoth on plateau | Camera shifts slightly across three frames | OBSERVED |
| S091 | 12940-13000 | 431.76 | No character. Two isolated terrain props: grassy-topped grey rock block (left) and flat mu | Locked-off framing across viewed frames; no zoom seen. | OBSERVED;MEASURED;INFERRED(hard-cut entry from white) |
| S092 | 13001-13146 | 433.80 | Bearded long-haired head-and-torso figure with leaf skirt and stick arms (recurring narrat | Static framing seen; mammoth scale changes only by movement. | OBSERVED;MEASURED;INFERRED |
| S093 | 13147-13218 | 438.67 | Animal figures on a number line: bird of prey, flightless large bird, mammoth, bear; bear  | Line translates left across strip (approx 12 tile px/frame,  | OBSERVED;MEASURED;INFERRED |
| S094 | 13219-13298 | 441.07 | Map of the Americas and part of Greenland; later a white hand-drawn arrow. | Map slightly larger and shifted left between viewed frames ( | OBSERVED;MEASURED;INFERRED(push-in) |
| S095 | 13299-13543 | 443.74 | Dark-skinned round-headed bare-chested figure in fur loincloth with stick arms; wooden arr | Pan to the right between f13303 and f13421 (background moves | OBSERVED;MEASURED;INFERRED |
| S096 | 13544-13753 | 451.92 | Same plains figure and sign, then sign alone, then bear again. | Slow leftward drift in strip f13657-13664; bear enters from  | OBSERVED;MEASURED;INFERRED |
| S097 | 13754-13757 | 458.93 | Brown bear (same bear drawing). | Single frame; transition state of 4 frames (MEASURED). | OBSERVED;MEASURED;INFERRED(dissolve) |
| S098 | 13758-13816 | 459.06 | Bear in profile on white, shadow absent. | Bear moves right between f13762 and f13814 and decreases in  | OBSERVED;MEASURED;INFERRED |
| S099 | 13817-13820 | 461.03 | Bear (partial) and bear silhouette head. | Vertical slide up of previous layout (OBSERVED in a single f | OBSERVED;MEASURED;INFERRED |
| S100 | 13821-13870 | 461.16 | Standing bear silhouette; small caped pointed-eared human silhouette. | Static. | OBSERVED;MEASURED |
| S101 | 13871-13937 | 462.83 | Bearded glasses-wearing figure (similar to narrator-type figure with glasses) behind rock  | Slight camera push/pan between f13875 and f13935 (board larg | OBSERVED;MEASURED;INFERRED |
| S102 | 13938-14183 | 465.06 | Small brown grizzly-type bear and larger dark short-faced bear (same bear as earlier). | Group sinks lower in frame between f14060 and f14180 (OBSERV | OBSERVED;MEASURED |
| S103 | 14184-14297 | 473.27 | Recurring bearded lecturer figure (head and hairy torso, stick limbs, leaf garment) at rig | OBSERVED: framing differs between the two frames (board edge | OBSERVED (frames); MEASURED (palette); INFERRED (camera drift) |
| S104 | 14298-14427 | 477.08 | Large oak trunk; small sitting bear cub with claws and fur texture; (strip) a very large a | OBSERVED: tree base and horizon shift/enlarge across f14302, | OBSERVED; MEASURED (palette); INFERRED (camera, mother) |
| S105 | 14428-14586 | 481.41 | Wooden hanging sign on ropes; large side-profile bear (brown, then black silhouette with c | OBSERVED: bear shifts/enlarges between frames (head position | OBSERVED; MEASURED (palette); INFERRED (drift) |
| S106 | 14587-14734 | 486.72 | Recurring lecturer figure; stone podium with bowl and club-like stick; wall sign Barely Ev | OBSERVED/ strip: content shifts and enlarges over f14697-f14 | OBSERVED; MEASURED; INFERRED (push-in) |
| S107 | 14735-14754 | 491.66 | None; text card only. | OBSERVED: static in both frames; 20-frame state. | OBSERVED; MEASURED |
| S108 | 14755-15099 | 492.33 | Big oak tree, small seated lecturer figure with leaf garment at trunk, large brown bear wi | OBSERVED: framing changes between viewed frames (bear and tr | OBSERVED; MEASURED; INFERRED (shade) |
| S109 | 15100-15157 | 503.84 | None; text card only. | OBSERVED: static card; no scale or pan visible in strip. | OBSERVED; MEASURED |
| S110 | 15158-15620 | 505.77 | Lone lecturer figure (leaf garment, stick arms), large brown bear, shrubs, conifers, tufte | OBSERVED: wide shot in f15162, closer shots after; strip f15 | OBSERVED; MEASURED; INFERRED (camera) |
| S111 | 15621-15739 | 521.22 | Recurring lecturer, chalkboard, podium, projector, poster fragments, pointer stick. | OBSERVED: closer framing in f15737 than f15625; strip shows  | OBSERVED; MEASURED |
| S112 | 15740-16042 | 525.19 | Lecturer figure with leaf garment, large brown bear, conifers, bushes. | OBSERVED: bear larger across frames; strip f15831-f15838 nea | OBSERVED; MEASURED |
| S113 | 16043-16318 | 535.30 | Lecturer, chalkboard, podium with bowl, projector, poster edges. | OBSERVED: static camera across f16047 and f16315; strips sho | OBSERVED; MEASURED |

## Not established
- Fonts, software, layer stacks, easing curves, sound design: UNAVAILABLE.
- Audio sync, SFX placement, music: BLOCKED_CAPABILITY.
- Interiors of long states between sampled frames: not inspected.
- Any retention/CTR explanation: not inferred.
