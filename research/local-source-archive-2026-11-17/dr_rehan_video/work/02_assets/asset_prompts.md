# Asset prompts v3: Dr. Rehan explainer ("BP after 65"), story "Two Mornings"

The story is in `01_script/STORYLINES.md` (A). One woman, Margaret (72), is followed through the film:
- **H01:** a dizzy blue dawn in her bedroom.
- **I01:** the check-up with her daughter.
- **J01/J02/U01:** explainers drawn in her own notebook.
- **B02:** the night hallway where a fall could happen.
- **DR5:** the consultation.
- **O01:** the payoff. The **same bedroom, same camera angle**, a warm morning, and she stands up steady. Then she is in the garden with her granddaughter.

Every image below is a piece of that one story.

**Audience:** 50+ in the USA, UK, New Zealand and Australia.

v2 (60 unrelated plates, South-Asian setting) is replaced. Its backup is kept outside the project, and the 50 images Codex already made stay in Codex's own folder, untouched.

## Instructions for Codex

1. **Generate in this order:**
   - first the CAST sheets (CH);
   - then the LOCATION masters (L);
   - then the STORY shots (S);
   - then the FX plates (T).
2. **Consistency rule** (from the AI Character Sheet method):
   - Every S block lists `Refs:`. Attach those finished files as **reference images** to that generation, and start the prompt with: *"Using the attached reference images, keep the exact same person (hair, build, hands, ring, watch, clothes) and the exact same room. Change only what this prompt describes."*
   - Never re-roll a character from words alone once their sheet exists.
   - Keep one master per character and per location (the `a` file unless the user picks `b`).
3. Prepend the STYLE LOCK the block names (CC, MC, NB or FX) and the WORLD LOCK to every prompt.
4. **Save into `generated/v3/`** with the exact file name given (the ID is the prefix). Write `generated/v3/_index.md` (ID → file → refs used). Do not touch the older files in `generated/`.
5. **Size and failures:**
   - Use the size given (16:9 = 2048×1152 or the nearest the tool allows; say the actual size in the index).
   - "transparent" means a PNG with alpha.
   - If a generation fails, retry once, then log it in `generated/v3/_failed.txt`.
6. No text, letters or numbers in any image. Every screen (BP monitor, phone) is **blank**; the numbers are drawn in the edit.

## WORLD LOCK (every image)

The setting has to feel like home to a viewer in the USA, the UK, Australia **and** New Zealand at once. It is a modest, lived-in suburban home of a retired woman, built around 1970–1990, kept tidy, not wealthy and not poor. The palette is soft sage, cream, oak and dusty rose.

**NEVER show:**
- power plugs or wall sockets (they differ between countries);
- car interiors or steering wheels (left- vs right-hand drive);
- road markings, number plates, currency, flags or mailboxes;
- seasonal holiday decorations;
- brand names, or any readable text on paper, screens, packaging or signs.

## STYLE LOCK: CC (Clinical Calm, the daytime world)

Editorial documentary photography, natural soft window light, muted warm-neutral palette (off-white, warm grey, sage, oak, deep navy, one accent of clinical red #D64545 only where noted). Shallow depth of field, a 50mm lens feel, subtle film grain, realistic skin and fabric textures, an uncluttered composition with generous negative space for typography.

NO text, NO logos, NO glossy CGI, NO plastic skin, NO oversaturated colours, NO medical gore, NO holograms.

People: **never a visible face.** Show backs, over-the-shoulder, hands, silhouettes, or a face turned away or cropped above the frame. The people are recognised by their hair, clothes, ring and watch, never by a face.

## STYLE LOCK: MC (Midnight Clinic, dawn and night only)

The same rules as CC, but low-key: pre-dawn blue hour, deep navy shadows (#0B1430), a cool cobalt rim light, one small warm practical light (a bedside lamp or a night light). Quiet and intimate, never horror or sci-fi. Keep the left 40% of the frame dark and simple for typography unless the block says otherwise.

## STYLE LOCK: NB (Margaret's notebook)

Hand-drawn editorial illustration: fine graphite pencil and dark-grey ink line art (#3A3A3A) on warm cream paper (#FAF6EE), slightly wobbly human lines, light cross-hatching, at most one accent of red pencil (#D64545) where noted. It looks drawn by hand in a notebook, not vector, not 3D. NO text, labels, numbers or arrows with words. Faces are drawn as simple shapes without features.

"transparent" means line art only, with no paper behind it.

**Never draw hearts, arteries, kidneys or any organ:** anatomy is drawn in code so it stays medically correct.

## STYLE LOCK: FX (overlay plates)

Pure photographic overlay plates for compositing: shot on black (or mid-grey where noted), no objects, no text, no borders. They tile without seams where noted.

---

## CAST (generate first). One master per person

### CH1: Margaret, 72 (the viewer). Identity sheet
- File: `CH1_margaret_identity_a.png` / `_b.png` | Style: CC | 2048×1152 | plain warm-grey studio wall
- **Who:**
  - a 72-year-old retired woman of European descent, about 165 cm, slim-average build, slightly rounded shoulders;
  - silver-white hair in a soft chin-length bob with a side part on the left;
  - fair skin with light age spots on the backs of her hands, short unpolished nails;
  - **signature details, in every shot where her hands show:** a thin gold wedding band on the left ring finger and a small round silver watch on a brown leather strap on the left wrist;
  - tortoiseshell reading glasses on a thin gold chain around her neck.
- **Prompt:** Create a photographic identity contact sheet of this woman, in two rows, with natural relaxed posture, as if photographed on the same day:
  - **top row:** (1) full body from directly behind, (2) full body three-quarter from behind on the left, (3) full body in left profile as a soft silhouette against a bright window, so no facial features show, (4) full body walking away;
  - **bottom row:** (5) the back of her head and hair close up, (6) her left hand resting on a table, showing the ring and watch, (7) her shoulders and glasses chain, seen from behind and above.
- Wardrobe for this sheet: W1 (below). Soft neutral light, documentary, not stylised.
- **b:** the same sheet, with a slightly warmer light.
- Avoid: any frame where her face is visible, jewellery other than the ring, watch and glasses chain.

### CH1-W: Margaret wardrobe sheet
- File: `CH1W_margaret_wardrobe_a.png` | Style: CC | 2048×1152 | Refs: CH1
- **Prompt** (from the guide's wardrobe method): Using the attached identity sheet, keep the exact same woman, body, hair, ring, watch and glasses chain. Show her four times from behind / three-quarter behind, side by side, changing ONLY the clothing:
  - **W1 morning:** a dusty-rose knitted cardigan over a cream cotton nightdress, grey sheepskin-lined slippers;
  - **W2 going out:** a navy wool coat to the knee, a grey knitted scarf, a tan leather handbag;
  - **W3 at home:** an oatmeal cable-knit jumper, charcoal trousers, soft brown shoes;
  - **W4 garden:** the same dusty-rose cardigan over a white blouse, light trousers, white canvas shoes.
- Real fabric on a real body.
- **b:** not needed.

### CH1-NB: Margaret as a notebook sketch (model sheet)
- File: `CH1NB_margaret_sketch_a.png` | Style: NB | 2048×1152 | transparent | Refs: CH1, CH1-W
- **Prompt:** Draw the woman from the reference as a simple hand-drawn ink character in the notebook style: the chin-length bob and the cardigan clearly recognisable, the face as a plain shape with no features. Five poses side by side: (1) sitting on a chair, (2) pushing up to stand, (3) standing with one hand on her head and small wobble lines, (4) standing steady and upright, (5) walking.
- **b:** the same five poses, with the cardigan in a red pencil accent.

### CH2: Claire, 50 (Margaret's daughter)
- File: `CH2_claire_identity_a.png` | Style: CC | 2048×1152 | Refs: CH1 (for family resemblance in build and hair texture)
- **Who:**
  - a 50-year-old woman, auburn shoulder-length hair in a low ponytail;
  - an olive-green waxed jacket over a grey jumper;
  - a plain silver bangle on her right wrist.
- **Prompt:** Identity sheet like CH1: from behind, three-quarter behind, her hands (bangle visible), and her walking away. Face never visible.

### CH3: Lily, 7 (granddaughter)
- File: `CH3_lily_identity_a.png` | Style: CC | 2048×1152
- **Who:**
  - a 7-year-old girl with a long blonde plait;
  - a red-and-white striped long-sleeve top, denim pinafore, yellow wellington boots.
- **Prompt:** Sheet: from behind, three-quarter behind, her small hand, and skipping away. Face never visible.

### CH4: The nurse / GP (never Dr. Rehan)
- File: `CH4_clinician_hands_a.png` | Style: CC | 2048×1152
- **Who:**
  - hands and forearms only;
  - a light-blue shirt sleeve rolled to the forearm, a navy lanyard with a blank card;
  - short clean nails, no rings;
  - a plain black stethoscope.
- **Prompt:** Sheet of these hands: holding a stethoscope, writing with a pen, gesturing calmly with an open palm, and wrapping a BP cuff.
- Avoid: a face, a white coat (so this person is never mistaken for Dr. Rehan).

---

## LOCATIONS (generate second). One empty master per place; every S shot in that place uses it

### L1: Margaret's bedroom
- File: `L1_bedroom_master_a.png` / `_b.png` | Style: CC | 2048×1152
- **Prompt:** A modest suburban bedroom, pale sage walls, a white-painted wooden double bed with a cream knitted throw, an oak bedside table on the RIGHT of the bed with a small brass lamp, a home blood pressure monitor (blank screen) and a framed photo turned slightly away. A window with thin linen curtains on the right wall. A pale rug on oak floorboards. Daylight, empty, wide.
- **b:** the same room at blue pre-dawn, lamp off (MC).
- This room appears twice in the film (the hook and the payoff). **Keep the same furniture and layout.**

### L2: Margaret's kitchen-diner
- File: `L2_kitchen_master_a.png` | Style: CC | 2048×1152
- **Prompt:** A small kitchen-diner, a round pine table with two chairs by a window, a white kettle and a green potted herb on the counter, a fridge door covered in children's crayon drawings and a few photos (faces too small or blurred to read), soft morning light. Empty.

### L3: Hallway and stairs
- File: `L3_hallway_master_a.png` / `_b.png` | Style: MC | 2048×1152
- **Prompt:** A narrow hallway at night, a wooden staircase with white balusters and a polished wooden handrail, a patterned runner rug whose near corner is slightly curled up, a small warm night light glowing low on the skirting board (no plug visible), cobalt moonlight from a door glass panel. Empty.
- **b:** the same in daylight (CC).

### L4: The GP consulting room
- File: `L4_consult_master_a.png` | Style: CC | 2048×1152
- **Prompt:** A calm, light GP consulting room, a light-wood desk with a computer monitor turned away from camera, an upper-arm blood pressure machine on a wheeled stand, two chairs on the patient side, a window with white blinds, a pot plant. Empty. No posters, no signs.

### L5: The garden and park path
- File: `L5_garden_master_a.png` / `_b.png` | Style: CC | 2048×1152
- **Prompt:** A small back garden in early morning sun: a lawn, a timber bench, roses along a fence, a gravel path, lots of soft sky.
- **b:** a tree-lined park path nearby in the same light.

---

## STORY SHOTS (★ = needed for draft v3, ○ = nice to have)

Format: ID · file · style · size · refs · where it plays (with the narrator's words) · what the shot does in the story.

### ACT 1: H01 "You're 72…" (the dizzy dawn). The viewer must think "that's me / that's Mum"

#### S01 ★ The first frame (visual hook)
- `S01_cuff_dawn_a.png` / `_b.png` · MC · 2048×1152 · Refs: CH1, CH1-W (W1), L1b
- **Plays:** 0:00, "You're 72. Your blood pressure is finally coming down." The code draws the digits on the blank screen, ticking down.
- **Prompt:** Blue pre-dawn in her bedroom. An over-the-shoulder close shot: Margaret sits on the edge of the bed in the dusty-rose cardigan, a grey upper-arm BP cuff on her LEFT arm (the ring and watch clearly visible), her right finger on the button of the home monitor on the bedside table, its screen blank and softly glowing, the brass lamp warm and low.
- **b:** tighter, only the cuffed arm, the hand and the glowing blank screen.
- Avoid: digits on the screen, her face.

#### S02 ★ The screen
- `S02_monitor_macro_a.png` · MC · 2048×1152 · Refs: S01a
- **Plays:** "That sounds like good news." A slow push; the code numbers sit on the screen.
- **Prompt:** Macro of the same home monitor's blank glowing screen, the edge of her cuffed arm and watch soft in the foreground, cobalt shadows.

#### S03 ★ Standing up
- `S03_rise_from_bed_a.png` / `_b.png` · MC · 2048×1152 · Refs: CH1, L1b, S01a
- **Plays:** "BUT now, every time you stand up…"
- **Prompt:** Low side angle. Margaret's hand with the ring pushes on the mattress edge as she rises, her slippered feet on the floorboards, the cardigan hem moving, her face out of frame.
- **b:** from behind, her silhouette half-risen against the curtained window.
- **This exact framing returns in S34** (the payoff).

#### S04 ★ The room spins (her eyes)
- `S04_dizzy_pov_a.png` · MC · 2048×1152 · Refs: L1b
- **Plays:** "…the room spins." Rotated and rack-blurred in code.
- **Prompt:** Her point of view, standing beside the bed looking toward the bedroom door, the frame tilted about 8°, edge blur, a doubled doorframe, blue light.
- Avoid: horror.

#### S05 ★ Steadying herself
- `S05_hand_on_bedside_a.png` · MC · 2048×1152 · Refs: CH1, L1b
- **Plays:** after "the room spins": the hit and the hold.
- **Prompt:** Close-up of her left hand (ring, watch) gripping the edge of the oak bedside table, the brass lamp rocking slightly, the BP monitor beside her hand.
- **b:** her hand flat against the sage wall.

#### S06 ★ The question
- `S06_sitting_back_down_a.png` · MC · 2048×1152 · Refs: CH1, L1b
- **Plays:** "So should it go even LOWER? Or does your treatment need a second look?"
- **Prompt:** From behind, Margaret sitting back down on the bed edge, the monitor in her lap, head slightly bowed toward it, first pale light on the curtains. Quiet, thinking.

#### S07 ○ Establishing window
- `S07_curtain_dawn_a.png` · MC · 2048×1152 · Refs: L1b
- **Plays:** the hook's split card "Protect the heart / Avoid falls" (background, blurred).
- **Prompt:** The bedroom window, linen curtain glowing blue, the first warm line on the horizon.

### ACT 2: I01 "Here's Dr. Rehan Omer…" (she goes for a check-up)

#### S08 ★ Leaving for the appointment
- `S08_front_door_a.png` · CC · 2048×1152 · Refs: CH1-W (W2), CH2
- **Plays:** the I01 start (before the name). The narrator's sweep reveals it.
- **Prompt:** Inside her front door. Margaret in the navy coat and grey scarf, from behind, slips a small BP diary into her tan handbag. Claire's hand (silver bangle, olive jacket sleeve) holds the door open to soft daylight.

#### S09 ★ The waiting room
- `S09_waiting_room_a.png` · CC · 2048×1152 · Refs: CH1-W (W2), CH2
- **Plays:** "…he opens blocked heart arteries without open surgery…" (behind the title card, blurred).
- **Prompt:** A calm clinic waiting area. Margaret and Claire from behind, sitting side by side on simple chairs, her handbag on her lap, Claire's hand resting on her mother's forearm. No signs.

#### S10 ★ The door to the doctor
- `S10_consult_door_a.png` · CC · 2048×1152 · Refs: L4
- **Plays:** the I01 → DR1 transition. The iris opens out of the bright doorway into Dr. Rehan.
- **Prompt:** The consulting-room door half open from the corridor, warm daylight spilling out, the room soft behind.

### ACT 3: DR1 / J01 "why treat it?" (what's at stake)

#### S11 ★ What's at stake
- `S11_fridge_drawings_a.png` · CC · 2048×1152 · Refs: L2
- **Plays:** J01 "That's why it should be treated."
- **Prompt:** Close on her fridge door: children's crayon drawings (a house, a sun, stick figures, no words), a holiday photo of a family on a beach (faces too small to read), a magnet. Morning light.
- **b:** Margaret's ringed hand straightening one drawing.

#### S12 ○ The world study
- `S12_world_map_a.png` · CC · 2048×1152
- **Plays:** the DR1 "INTERHEART" label (the code draws dots).
- **Prompt:** A muted vintage paper world map on a desk, no labels or text, soft light.

#### S13 ★ Her notebook (home of every notebook scene)
- `S13_notebook_table_a.png` / `_b.png` · CC · 2048×1152 · Refs: CH1, L2
- **Plays:** J01, J02 and U01. The camera dives into the blank page and the code draws on it.
- **Prompt:** Top-down on her pine kitchen table: an open cream notebook with blank pages, a pencil, her tortoiseshell glasses on their gold chain lying beside it, a cup of tea, her ringed hand at the edge of the page.
- **b:** the same, the camera lower and closer to the page.

### ACT 4: J02 "orthostatic HYPOtension" (her morning, redrawn)

#### S14 ★ The morning as a sketch
- `S14_sketch_bed_rise_a.png` / `_b.png` · NB · 2048×1152 · transparent · Refs: CH1-NB, S03a
- **Plays:** J02 "You get up, / your pressure falls, / and you may feel dizzy." A match cut from photo S03 to this.
- **Prompt:** Margaret drawn in the notebook style, rising from the edge of the bed in exactly the pose of S03.
- **b:** standing with a hand on her head and small wobble lines beside the bed.

#### S15 ○ Sitting AND standing ⚠️ (only if Dr. Rehan approves that line)
- `S15_sketch_cuff_two_a.png` · NB · 2048×1152 · transparent · Refs: CH1-NB
- **Prompt:** Two small sketches of Margaret wearing a BP cuff: one sitting in a chair, one standing beside it. Blank monitor.

#### S16 ★ "Should older people be treated at all?"
- `S16_armchair_window_a.png` · CC · 2048×1152 · Refs: CH1-W (W3)
- **Plays:** the last J02 line, which opens into the doctor's answer.
- **Prompt:** From behind, Margaret in an armchair by a living-room window in her oatmeal jumper, looking out, the pill organiser on the side table. Still, thoughtful.

### ACT 5: DR3 / B01 / DR4 "the old belief, the line that moved"

#### S17 ★ The old belief
- `S17_old_files_a.png` · CC · 2048×1152
- **Plays:** the DR3 "OLD BELIEF" stamp beat (sepia push and dust T05).
- **Prompt:** Old cardboard file folders and yellowed papers tied with string on a dusty shelf, no readable writing.

#### S18 ○ The stamp
- `S18_rubber_stamp_a.png` · CC · 2048×2048 · transparent
- **Prompt:** A wooden-handled rubber stamp, isolated, blank face.

#### S19 ★ The trial helped people like her
- `S19_walking_group_a.png` · CC · 2048×1152 · Refs: CH1-W (W2), L5b
- **Plays:** DR3 "a big trial showed treatment helps."
- **Prompt:** A small walking group of six people in their 70s and 80s on the park path, from behind, morning light. Margaret in the navy coat is among them, second from the left.

#### S20 ★ The line moved
- `S20_pencil_ruler_a.png` / `_b.png` · CC · 2048×1152 · Refs: S13a
- **Plays:** B01 "That line has MOVED."
- **Prompt:** Top-down on her notebook (from S13): her ringed hand drawing a straight pencil line along a wooden ruler.
- **b:** an eraser rubbing out an earlier line, crumbs on the page.

#### S21 ★ 140/90 at home
- `S21_monitor_kitchen_a.png` · CC · 2048×1152 · Refs: L2, S01a
- **Plays:** DR4 "140/90 or more" (the numbers are typeset in code).
- **Prompt:** The same home monitor (blank screen) on her pine kitchen table, the cuff beside it, a cup of tea, her BP diary closed, morning light.

### ACT 6: B02 "Here's the challenge" (the night hallway, where a fall could happen)

#### S22 ★ The night walk
- `S22_banister_night_a.png` · MC · 2048×1152 · Refs: CH1-W (W1), L3
- **Plays:** "Lower it carelessly, and dizziness and FALLS become the risk."
- **Prompt:** Night. Margaret in the cardigan, from behind, at the top of the stairs, her ringed hand gripping the handrail, the warm night light far below.

#### S23 ★ The curled rug
- `S23_rug_slipper_a.png` · MC · 2048×1152 · Refs: CH1-W (W1), L3
- **Plays:** a tension insert on "FALLS". It holds for 0.6 s; no fall is ever shown.
- **Prompt:** Floor level: her slippered foot about to step near the curled-up corner of the hallway runner rug, the night light glowing.

#### S24 ★ What she's protecting
- `S24_family_photo_a.png` · MC · 2048×1152 · Refs: L1b
- **Plays:** "your HEART is at risk" (opposite the rug, so the two sides of the balance are both her life).
- **Prompt:** On the bedside table at night, a framed family photo seen at an angle with faces too soft to read, the brass lamp warm beside it.

#### S25 ★ Fit the PERSON
- `S25_organiser_hands_a.png` / `_b.png` · CC · 2048×1152 · Refs: CH1, L2
- **Plays:** "By choosing the medicine to fit the PERSON." The light warms, from MC to CC.
- **Prompt:** Close-up of her hands (ring, watch) holding a plain weekly pill organiser with seven closed lids at the kitchen table, warm lamp light.
- **b:** one lid open, two plain white tablets.

### ACT 7: DR5 "the medicine depends on the person"

#### S26 ★ The consultation
- `S26_consult_ots_a.png` / `_b.png` · CC · 2048×1152 · Refs: CH1-W (W3), CH4, L4
- **Plays:** DR5 split-card top strip, "depends on the person".
- **Prompt:** Over Margaret's shoulder (silver bob, oatmeal jumper) across the desk. Only the clinician's hands (light-blue sleeve) are visible, gesturing calmly over her open BP diary. Warm daylight.
- **b:** the clinician's hands wrapping the cuff on her arm.

#### S27 ★ Tablets
- `S27_plain_tablets_a.png` / `_b.png` · CC · 2048×1152
- **Prompt:** Plain white and off-white tablets on a linen cloth, no markings.
- **b:** the tablets in four separate small groups (lined up with the four map rows).

#### S28 ○ Blister pack
- `S28_blister_pack_a.png` · CC · 2048×2048 · transparent
- **Prompt:** A plain silver blister pack of white tablets, no print.

### ACT 8: U01 ⚠️ "no single target" (used only if U01 is approved)

#### S29 ○ Water tablet
- `S29_water_tablet_a.png` · CC · 2048×1152 · Refs: L2, CH1
- **Prompt:** A glass of water and one plain white tablet on her kitchen counter, her ringed hand reaching in.

#### S30 ★ Not one number for everyone
- `S30_sketch_three_people_a.png` / `_b.png` · NB · 2048×1152 · transparent · Refs: CH1-NB
- **Plays:** "Today, there's no SINGLE target for everyone."
- **Prompt:** Three hand-drawn older people standing side by side, in the notebook style: (1) Margaret as in her sketch, (2) a frail man of about 85 with a walking frame, (3) a fit woman of about 68 in walking shoes. Clearly different people.
- **b:** the three on three separate paths that split from one road.

#### S31 ○ Frailty
- `S31_sketch_hands_stick_a.png` · NB · 2048×1152 · transparent
- **Plays:** "frailty".
- **Prompt:** Hand-drawn elderly hands resting on top of a walking stick.

### ACT 9: DR6 "bottom line"

#### S32 ★ The check
- `S32_stethoscope_back_a.png` · CC · 2048×1152 · Refs: CH1-W (W3), CH4, L4
- **Plays:** DR6 "see a trained specialist."
- **Prompt:** From behind, the clinician's hand holds a stethoscope to Margaret's back over her oatmeal jumper, both faces out of frame, soft light.

#### S33 ○ The clipboard
- `S33_clipboard_a.png` · CC · 2048×2048 · transparent
- **Plays:** the DR6 ticks (drawn in code).
- **Prompt:** A plain wooden clipboard with a blank sheet and a pen, top-down.

### ACT 10: O01 "So what should it be?" (the payoff: the second morning)

#### S34 ★ THE MIRROR
- `S34_mirror_morning_a.png` / `_b.png` · CC · 2048×1152 · Refs: CH1, CH1-W (W1), L1, S03a
- **Plays:** "The real question is: is it being controlled SAFELY?"
- **Prompt:** EXACTLY the framing of S03 (same low side angle, same bed, same bedside table and monitor), but warm golden morning sun through the open linen curtains. Margaret stands up fully and steadily, one hand lightly on the bedside table out of habit, her posture upright.
- **b:** from behind, standing tall at the window in the sun.

#### S35 ★ Sign 1: dizzy when you stand
- `S35_sign_dizzy_a.png` · CC · 2048×1152 · Refs: CH1, L1
- **Plays:** "If you feel dizzy when you stand." A small inset; it calls back S05.
- **Prompt:** Daylight version of S05: her hand on the bedside table, steadying.

#### S36 ★ Sign 3: unwell after the medicine
- `S36_sign_unwell_a.png` · CC · 2048×1152 · Refs: CH1-W (W3), L2
- **Plays:** "…or feel unwell after your medicine." (Sign 2, falls, reuses S23.)
- **Prompt:** At the kitchen table, Margaret from behind and to the side, one hand at her temple, the pill organiser open beside a glass of water. Calm, not dramatic.

#### S37 ★ Talk to your doctor
- `S37_phone_call_a.png` / `_b.png` · CC · 2048×1152 · Refs: CH1, CH2, L2
- **Plays:** "talk to your doctor."
- **Prompt:** Her ringed hand holding a simple phone to her ear (face out of frame), her BP diary open on the table, a cup of tea.
- **b:** Claire's hand (bangle) resting on Margaret's hand on the table.

#### S38 ★ PROTECTION (the biggest picture of the film)
- `S38_garden_lily_a.png` / `_b.png` · CC · 2048×1152 · Refs: CH1-W (W4), CH3, L5
- **Plays:** "It's better PROTECTION." It holds 2–3 s at full screen.
- **Prompt:** Morning sun in the garden. From behind, Margaret walks steadily along the gravel path holding Lily's small hand, Lily's plait and yellow wellies, roses, lots of soft sky.
- **b:** the two of them sitting together on the timber bench.

#### S39 ★ Never on your own
- `S39_organiser_rest_a.png` · CC · 2048×1152 · Refs: CH1, S25a
- **Plays:** "And never change your blood pressure medicine on your own." This is the quiet 0.5 s pause frame.
- **Prompt:** Her ringed hand resting flat and still on the closed weekly pill organiser on the kitchen table, soft morning light.

#### S40 ○ Bridge to the doctor
- `S40_sunrise_rooftops_a.png` · CC · 2048×1152
- **Plays:** O01 → DR7 (light leak T04 into the doctor).
- **Prompt:** Sunrise over the pitched tiled rooftops of a quiet suburb, chimneys, a few trees, soft haze, lots of sky. No signs or vehicles.

### END

#### S41 ★ End card ground
- `S41_warm_bokeh_a.png` / `_b.png` · CC · 4096×2304 · Refs (b only): L5
- **Prompt:** Soft out-of-focus warm bokeh on off-white (#F4F1EC), no objects.
- **b:** the empty garden bench from S38b at golden hour, very soft focus.

---

## FX + TEXTURES (generate last)

- **T01** `T01_paper_a.png` / `_b.png`
  - NB, 4096×2304.
  - Cream notebook paper, very faint fibres (a); faint pale-blue ruled lines (b).
- **T02** `T02_navy_a.png`
  - MC, 4096×2304.
  - A deep navy matte texture with a gentle cobalt falloff from the top right.
- **T03 ★** `T03_grain_a.png` / `_b.png`
  - FX, 2048×1152, mid-grey (#808080), tiling.
  - Fine 35mm grain (a), coarser 16mm grain (b).
- **T04 ★** `T04_light_leak_a.png` / `_b.png`
  - FX, on black.
  - A warm orange-gold leak from the right (a), a soft rose leak from the top-left (b).
  - Used for the doctor ↔ narrator transitions and the mirror morning.
- **T05** `T05_dust_a.png`
  - FX, on black.
  - Sparse dust specks and thin film scratches (DR3 "old belief" only).
- **T06 ★** `T06_paper_torn_a.png`
  - NB, 4096×2304, transparent.
  - A sheet of cream notebook paper with a torn fibrous left edge; it slides in for every notebook scene.
- **T07 ★** `T07_ink_brush_a.png` / `_b.png`
  - FX, on white.
  - One bold dry-brush ink stroke across the frame (a); three strokes covering the frame (b).
  - A luma matte for the photo ↔ notebook cuts.
- **T08** `T08_highlighter_a.png` / `_b.png`
  - NB, 2048×512, transparent.
  - A yellow highlighter swipe (#F5D547) (a); a red pencil underline (b).
- **T09 ★** `T09_cobalt_streak_a.png`
  - FX, on black.
  - A soft horizontal cobalt anamorphic streak, used into and out of the dawn and night scenes.
- **T10** `T10_lens_dirt_a.png`
  - FX, on black.
  - Subtle lens smudges lit from one side (S01–S06, S22–S24 at 15%).

---

**Totals:**
- 4 cast sheets + 2 cast extensions (wardrobe, sketch)
- 5 location masters
- 41 story shots
- 10 FX/textures

That makes **62 prompts** (about 95 images with the a/b variants).

**Return:** put everything in `work/02_assets/generated/v3/`. Do the cast and locations first and send them for approval before the story shots, because every other image copies them.
