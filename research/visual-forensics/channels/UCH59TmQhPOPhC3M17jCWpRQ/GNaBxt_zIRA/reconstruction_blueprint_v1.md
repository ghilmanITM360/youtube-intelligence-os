# Reconstruction blueprint v1 — original equivalent of Barely Evolved GNaBxt_zIRA techniques
Label: PROPOSAL built on OBSERVED technique families. Copy no character, drawing or wording from the source.

## Canvas
1920x1080, 30000/1001 fps CFR (MEASURED for the source; adopted as a production choice).

## Pipeline (proposed)
1. Script new original narration; segment into beats roughly matching the observed state density (113 states over 545 s, mean 4.8 s/state, MEASURED for source).
2. Per beat, choose one illustration per tables/consolidated_state_prompts.csv (prompts already rewritten as original equivalents with placeholders).
3. Animate with the module set below; timing taken from observed frame spans, easing left to the animator (unverified in source).
4. Audio: write and mix independently; no sync rule can be derived because the source audio was not listened to.

## Modules
### M_ELEMENT_ENTER_EXIT
- Observed: 41 events; span min/median/max 1/5/8 frames (strip-bounded)
- Examples: S010 f1155-1162 [b01]: Lecturer figure enters from the right edge and drifts slightly leftward, still cropped by the edg; S052 f6767-6770 [b04]: Backpack slides left out of frame between f6767 and f6770.; S052 f6770-6774 [b04]: Headband villager slides in from the right edge at f6770 and decelerates to rest left of centre b
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_CAMERA_SCALE_PAN
- Observed: 33 events; span min/median/max 6/8/8 frames (strip-bounded)
- Examples: S011 f1384-1391 [b01]: Pull-back: giant sloth goes from partial claws at top right to nearly full body with tail by f139; S012 f1580-1587 [b01]: Scene content shifts rightward and down: chalk text, sign and lectern move right, projector enter; S022 f3315-3320 [b02]: Wide classroom view becomes a tighter view on the man across f3315-f3320 (man grows, board shrink
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_FADES
- Observed: 4 events; span min/median/max 4/6/6 frames (strip-bounded)
- Examples: S011 f1384-1389 [b01]: "modern sloth" arrow label and "2 feet" bracket shrink and fade from legible (f1384) to near invi; S016 f2472-2475 [b02]: Focus blur and corner darkening ramp up across f2472-f2475 (f2472 slightly soft, f2473 softer, f2; S049 f6428-6431 [b04]: Background blurs and darkens at the edges while the figure stays crisp, onset f6428-6431.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_CHARACTER_MOTION_POSE
- Observed: 49 events; span min/median/max 2/8/8 frames (strip-bounded)
- Examples: S001 f28-35 [b01]: Grey long-necked bird moves leftward into the frame from the right edge, neck and head lowering acros; S001 f28-30 [b01]: Hunter stick arms absent at f28, a left arm line appears at f29 and both by f30 (arm pose swap or swi; S051 f6661-6668 [b04]: Figure tips from upright to horizontal and slides left-down across the grass in about 8 frames (f
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_TEXT_REVEAL_SWAP
- Observed: 16 events; span min/median/max 1/3/8 frames (strip-bounded)
- Examples: S005 f466-467 [b01]: Small "5" glyph shows partial at f466 and complete from f467.; S016 f2475-2475 [b02]: Title text "step 1 : attack first!" first present at f2475, fully formed in that tile; no partial; S041 f5288-5293 [b03]: '440 lbs (200 kg)' label enters from top (partly cropped f5288), moves down and settles about f52
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_HOLDS
- Observed: 16 events; span min/median/max 2/8/8 frames (strip-bounded)
- Examples: S009 f944-951 [b01]: Room and lecturer look unchanged at tile resolution; detector peak value is low (1.43).; S009 f963-970 [b01]: Room and lecturer look unchanged at tile resolution; detector peak value is low (1.63).; S016 f2470-2471 [b02]: Scene sharp and nearly unchanged between f2470 and f2471.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.
### M_OTHER
- Observed: 14 events; span min/median/max 1/7/8 frames (strip-bounded)
- Examples: S047 f6209-6212 [b04]: Wooden basket drops from the figure and falls into the water, tilting as it goes.; S007 f754-761 [b01]: Frame-to-frame brightness flicker (lamp glow and wall tone vary) with soft blur; door and green lig; S013 f1690-1690 [b01]: Black jagged crack line appears between V and S at f1690, absent in f1688-f1689.
- Production choice: PROPOSAL: reproduce only the abstract technique (motion type, frame span, direction) with new original art and wording; easing, software and layer structure are UNAVAILABLE.

## Acceptance tests (proposed, not yet run for this video)
- Frame-span check: each animated move measured with the same per-frame mean-abs-diff script used on the source; spans within the observed min-max range.
- Originality check: no source character silhouette, text or layout copied 1:1.
- Coverage check: every beat has a prompt and a module assignment.

Reconstruction test: NOT_RUN for this video (video 1 RT-01 covers shared timing modules).
