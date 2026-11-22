# Independent QA: R7 (Codex targeted corrections, rig v2)

Reviewer: independent session, 2026-11-21. No project file was modified except this report. Scratch frames and sheets live in the session scratchpad (not in the project).

## Verdict

- R7 0-75 s: PASS WITH FIXES (P2/P3 only, no P1)
- R7 75-122.3 s: PASS WITH FIXES (P3 only; identical to R6 except host assets)
- TEST_corrected_faces_10s.mp4: PASS
- Character development may be frozen for this video as PROVISIONAL (not publication-approved). No further Codex redesign is required for this video; only the optional P2/P3 items below.

## 1. Per-asset verdicts

Method: installed v1r4_assets/rig/ compared to the staged targeted_correction files (md5 identical for all 5), to rig_r6_v1_backup and to the parent folder (backup == parent originals). Neutral, smile, surprised heads are byte-identical to the originals; rig_anchors.json identical to the backup. All 15 head x body pairings were composited myself (chin 350,651 onto neck 650,70 / 750,70) on #FDFDFD and on cream (240,230,205) and inspected zoomed.

| Asset | Verdict | Evidence |
|---|---|---|
| rig_head_worried.png | ACCEPT | Raised/angled inner brows + clear downturned mouth. Reads as worried/sad vs neutral (flat line mouth, level brows) at 200 px, at 110 px and at the on-screen 0.34 scale downscaled to 640x360. The R6 version (wavy mouth, arched brows) read as puzzled; this is clearly better. Only the face interior changed (pixel diff confined to x190-500, y313-523 of the 700 canvas); hair, skin, ears, outline weight identical. |
| rig_head_smirk.png | ACCEPT-PROVISIONAL | One brow raised higher/more arched, mouth asymmetric and slightly lower on one side. Distinct from smile at 200 px and at full 1920 on-screen size. At 110 px and at 640x360 phone scale the difference smile vs smirk is carried mainly by the raised brow and the tilt; still readable side by side, but subtle in isolation. Better than R6 (marginally). Not worse. Diff confined to face interior (x189-478, y309-507). |
| rig_body_down.png | ACCEPT | Torso fill #5b6b3a -> #72864a, outline 27 -> 17 units; the olive panel is now ~23 % larger in pixels (27,083 vs 21,966 olive px) and clearly visible as green at 0.34/0.46/0.5 scale in video. Changed pixels only in x593-706, y89-584 (torso panel). Alpha bbox identical to R6 (502,16,797,1236). Neck anchor unchanged; no gap or halo with any of the 5 heads on white or cream. |
| rig_body_shrug.png | ACCEPT | Same as down; arms/hands unchanged (diff only x593-706). Alpha bbox identical. Neck join clean with all 5 heads. |
| rig_body_point.png | ACCEPT | Same; diff only x693-806 (torso, shifted by the 100 px canvas offset). Straight arm unchanged (P3, accepted provisional). Neck join at (750,70) clean with all 5 heads. |

Cross-checks:
- Neck/chin alignment, 15 pairings x 2 backgrounds: no gaps, no halos, no clipping; chin outline sits directly on the neck stub exactly as in R6. The neck stays very short (accepted provisional).
- Stroke weight / thin-body consistency: head outline and limb strokes unchanged; the torso fill now has a thinner outline (17) than the limbs (27) but the dark arm strokes bound the panel so there is no visible inconsistency at video scale. Body stays thin.
- Identity unchanged: same hair, skin, line weight, ears; verified by pixel diff (heads) and visually.
- Worse than previous? No asset is worse. The only side effect: the lighter green (#72864a) is brighter than the chart olive (#5b6b3a used for the 2.8 % bar and "about 3%"); see D4.

## 2. Room beat 17.9-22.5 s (R7 0-75 file)

Measured on frames at 19.6 s (same on 18.5, 20.5, 21.5, 22.3): caption box left edge x=753, box y 46-200.
- R6: hair/outline reached x=751 inside the box band, a 2 px gap (touching). Confirmed defect.
- R7: rightmost hair/outline pixel in the box band (y100-200) is x=705, a 48 px horizontal gap to the box. The right ear (rightmost host pixel, x=726 at y=275) is 27 px left of the box line and 75 px below the box bottom (y=200). No collision, no near-tangent.
- Host still sits well in the room: feet at y~985 on the floor, body centred between window wall and plant, hands clear of props.
- Left side: ear/hair left edge x=393, right curtain edge ~x=375 (18 px gap), and the wall-corner line at x~410 now runs behind the head. Acceptable, see D3 (P3).

## 3. Regression

- Duration: R7 0-75 file 75.000 s (2250 frames), 75-122 file 47.300 s (1419 frames), 1920x1080/30. Test clip 10.600 s.
- Decode: `ffmpeg -v error -f null` printed nothing for all 3 files.
- Audio: md5 of decoded s16le audio of R7 0-75 = R6 = frozen R4 v4 = 9920006e9318376d664d441cc89deba7. R7 75-122 = R6 = frozen R5 v2 = efbcec5acbd6e4ddc25dfe8215a81511. Bit-identical.
- Frozen files untouched: sha256 of out_r4 v4, out_r5 v2, out_r6/*.mp4 match out_r6/CHECKPOINT_SHA256.txt; mtimes predate R7.
- Frame regression: 38 matched timestamps (27 in file 1, 11 in file 2) compared R7 vs R6 and vs frozen R4/R5, diff threshold 24/255, area outside the host box masked. R7 vs R6: 0 differing pixels outside the host box (max 12 px of compression noise at 17.95 s in the caption-box rect; 1 px elsewhere). R7 vs frozen: 0-7 stray pixels outside the host box (compression noise, 62 px at 17.95 s inside the animated caption box edge). Figures, numbers, labels, source tags, charts unchanged. The only differing areas are the host figure, and the room-beat host position (x shifted 60 px left).
- 75.0 s join (file 1 frame 2249 vs file 2 frame 0): same host state (down body, smile head, same position and scale 0.46 at 470,1010); the differences are the text that clears at the segment boundary, as in the frozen R4/R5 baseline. Continuity OK.
- Host head swaps verified in R7 at: 0.5 neutral, 3.5 point/neutral, 12.5 shrug/neutral, 13.9 shrug/smirk, 14.5 point/smirk, 16.8 shrug/neutral, 17.95-22.3 down/worried, 22.7 point/smirk, 25.2 point/smile, 27.8 down/neutral, 30.6 shrug/smirk, 31.7 and 32.5 shrug/worried, 33.2 point/neutral, 40.2 down/smile, 63.9 and 64.7 shrug/surprised, 70.5 point/smirk, 72.6 and 74.5 down/smile; file 2: 0.0/0.5 down/smile, 9.8 and 10.3 point/neutral, 29.5 and 30.5 shrug/smirk (abs 104.5 and 105.5), 44.5 and 47.2 down/smile. All render the correct state, no stale R6 head/body.
- No lip sync, no idle bob, hard cuts: unchanged from R6 (not re-derived; logic untouched).

## 4. TEST_corrected_faces_10s.mp4 (10.6 s = 17.0-24.6 s + 31.0-34.0 s)

Viewed 29 frames: every 0.5 s plus around the cuts (0.8/0.9 into the room, 5.4/5.5/5.6 out of the room, 7.5/7.7 splice, 9.8/9.9). Contents match the R7 0-75 file at the matching timestamps. Worried (clip 0.9-5.4 and 8.5-10.6) is clearly readable; room-beat host clear of the caption box in every frame; smirk at 5.5-7.5 and 7.7-8.4 reads as a smirk next to smile in the full-resolution frames; torso visibly green on every pose. Splice at 7.6 s is a hard cut (intended). Verdict: PASS. Note: I did not listen to the test clip; its audio md5 is not comparable to a full file.

## 5. Defects

| ID | Class | Where | Defect | Action |
|---|---|---|---|---|
| D1 | P3 | rig_head_smirk.png at 0.34 scale, R7 0-75: 14.5, 22.7-24.5, 30.4-31.4, 70.3-72.4 | Smirk vs smile is still subtle in isolation at phone scale (brow + mouth tilt only). Always paired with a different pose/context, and distinct at full size. | Accepted provisional. Optional for the final art: stronger mouth asymmetry or a cheek mark. |
| D2 | P3 | rig_head_worried at 0.34 scale, 31.5-32.9 | Reads clearly as worried/sad at phone scale; no defect, listed only because it was the P2 in the R6 QA: now closed. | None |
| D3 | P3 | Room beat 17.9-22.5 | Host head now sits 18 px from the right curtain edge and straddles the wall-corner line (line hidden behind the head). Mild tangents, not collisions. | Optional: nudge to x=575 for ~33 px curtain gap while keeping >=33 px to the caption box. Not required. |
| D4 | P3 | All bodies, all host scenes | Torso green #72864a is lighter than the chart olive #5b6b3a (e.g. 2.8 % bar 14.5-16 s, "about 3%" 16.9 s), so the host and chart olive are two different greens. | Accepted provisional; unify in final art. |
| D5 | P3 | Provisional-accepted, unchanged | Geometric contours, very short neck, tiny hands, straight pointing arm, host scales 0.34/0.46/0.5, room-beat length 4.6 s vs 1-3 s guide. | Accepted provisional; not re-litigated. |

R6 P2 items status: worried reads puzzled -> closed; smirk/smile merge -> improved, residual P3 (D1); thin olive stripe -> closed; hair touching the caption box -> closed (2 px -> 48 px).

There is no P1 and no P2 left that blocks use.

## 6. What I did not check

- Audio quality/sync by ear, and the audio of the test clip; only decoded-audio md5 of the three full files was compared.
- Every single frame: 38 matched frames across both files plus 29 test-clip frames plus join frames were examined; the remainder of the 122.3 s was covered by the frame-diff logic only at those timestamps, not exhaustively. A full per-frame diff vs R6 was not run.
- The frame at 74.97 s of file 1 by seek (failed); the join was checked with frame-number select (frames 2249 and 0) instead.
- Playback motion/pacing in a real player, YouTube re-encode, and real phone screens (phone scale was emulated by downscaling to 640x360).
- Font licences, claim/source accuracy, narration (out of scope; not changed by R7).
- Publication approval: none given or implied; this is provisional character acceptance only.
