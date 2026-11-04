# Reconstruction blueprint v1 — original equivalent of Barely Evolved mNLNb-Z4T0M techniques
Label: PROPOSAL built on OBSERVED technique families. Copy no character, drawing or wording from the source.

## Canvas
1920x1080, 30000/1001 fps CFR (MEASURED for the source; adopted as a production choice).

## Pipeline (proposed)
1. Script new original narration; segment into beats roughly matching the observed state density (136 states over 557 s, mean 4.1 s/state, MEASURED for source).
2. Per beat, choose one illustration per tables/consolidated_state_prompts.csv (prompts already rewritten as original equivalents with placeholders).
3. Animate with the module set below; timing taken from observed frame spans, easing left to the animator (unverified in source).
4. Audio: write and mix independently; no sync rule can be derived because the source audio was not listened to.

## Modules
### M_ELEMENT_ENTER_EXIT
- Observed: 51 events; span min/median/max 1/5/8 frames (strip-bounded)
- Examples: S010 f530-535 [b01]: Sack bed enters from the top edge at f530, moves down and left through f531-f532, then back right t; S010 f555-562 [b01]: Barrel with a bowl and the shelf unit drop in from the top at f555, move down and settle to the rig; S022 f1564-1568 [b02]: Burlap sack slides in from right edge over the arrow label by f1568.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_CAMERA_SCALE_PAN
- Observed: 28 events; span min/median/max 1/8/8 frames (strip-bounded)
- Examples: S028 f2260-2267 [b02]: Camera moves right; old woman exits left, arched doorway enters from right.; S030 f2597-2604 [b02]: Camera moves right; bald man enters from right edge and slime-faced man exits left.; S078 f7950-7957 [b06]: Room shifts left across strip, shelves enter from right.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_FADES
- Observed: 7 events; span min/median/max 3/8/8 frames (strip-bounded)
- Examples: S019 f1248-1255 [b02]: Wall tone and sky-through-gap tint brighten from pale cyan to near white across the 8 tiles; wind; S020 f1370-1377 [b02]: Day sky blends to dark blue night across the 8 tiles; grass dims.; S022 f1564-1568 [b02]: Label Straw and arrow turn grey and disappear as sack covers them.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_CHARACTER_MOTION_POSE
- Observed: 37 events; span min/median/max 3/8/8 frames (strip-bounded)
- Examples: S003 f18-25 [b01]: Head and torso hold position; only the mouth shape and eye pupils change tile to tile (mouth open ell; S006 f324-326 [b01]: Seated character tilted while the hand with extended finger sits at right; little change among thes; S006 f328-330 [b01]: Character is flicked off the throne: tilted off the seat at f328, rotated and moving left at f329, 
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_TEXT_REVEAL_SWAP
- Observed: 17 events; span min/median/max 2/4/8 frames (strip-bounded)
- Examples: S011 f790-792 [b01]: Hand-lettered word 'maybe' is already fully formed at f790 with no visible partial letters in the s; S029 f2461-2462 [b02]: Word privacy replaced by word is.; S052 f4871-4872 [b04]: Hard swap from "invented" (about 470 px wide) to the smaller word "yet" (about 185 px wide) betwe
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_HOLDS
- Observed: 31 events; span min/median/max 1/3/8 frames (strip-bounded)
- Examples: S058 f5600-5603 [b04]: Sign stays planted; no visible bounce, differences of about 2 tile px (about 8 px) or less.; S009 f412-419 [b01]: The peasant lies sideways near the path and the cottage and castle remain; only very small shifts (; S010 f528-529 [b01]: Empty room with window and posts; no bed yet.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_OTHER
- Observed: 21 events; span min/median/max 2/6/8 frames (strip-bounded)
- Examples: S062 f5862-5869 [b05]: Board picture squashes vertically to a thin sliver (f5865-f5867) and re-expands (f5868-f5869) as ; S069 f6569-6576 [b05]: Board picture squash-and-expand: thin sliver at f6569-f6570, expands to parchment panel with pot ; S077 f7667-7669 [b06]: Two labels "option 1" and "option 2" visible; both slide rightward each frame.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.

## Acceptance tests (proposed, not yet run for this video)
- Frame-span check: each animated move measured with the same per-frame mean-abs-diff script used on the source; spans within the observed min-max range.
- Originality check: no source character silhouette, text or layout copied 1:1.
- Coverage check: every beat has a prompt and a module assignment.

Reconstruction test: NOT_RUN for this video (video 1 RT-01 covers shared timing modules).
