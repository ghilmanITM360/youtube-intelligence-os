# V13 artwork QA — candidate delivery, not approved

## Summary
The P0 acceptance criteria are **not met**. Do not integrate the elbow or neck candidates as finished repairs. All images in the manifest are candidate. The V1–V12 originals were not edited.

## Elbow
Three individual 1920×819 RGBA pose candidates combine the V12 forearm and hand rotated about (1335, 668) with locally registered image-generated sleeve fold art. They are already posed; do not rotate them again to their nominal angle. `previews/fold_pose_sheet.png`, the individual 2× elbow crops, and `previews/fold_sequence.gif` show them with the existing upper arm on top. The GIF is a four-frame diagnostic (0, 10, 15, 22 degrees over 0.4 seconds), not a smooth in-between animation proof.

**FAIL:** Each crop still has a small upper cut/notch and lower stray/doubled outlines; 22° also shows stray marks near the device. Continuity and 25 px useful cloth overlap are not established. No two-frame dissolve comparison to raised_generation.png was completed; the hand/device are inherited from the rotated V12 partition, not proven aligned to the raised art. These files need an artist's targeted repaint and proper animation test before use.

## Neck and collar
`side_neck_collar_underlay.png` is generated art masked and registered from a crop; the head and glance files are **unaltered copies of the V12 rig**, not newly recut heads. `previews/neck_range_sheet.png` and six full and 2× collar frames show -4/0/+4 degrees for both head states.

**FAIL:** head rotation exposes seams/notches; glance has visibly mismatched overlap. At rest, compositing V12 body, limbs, this underlay and V12 head differs from the supplied master in **11,936 RGBA pixels**; this is not pixel-identical. The head cut and underlay require further painted reconstruction. Pivot locations match the reference markings and V12 rig, but seam-free articulation at these coordinates has not been established.

## Hands
Three-quarter and back outputs were assembled using local generated edits on the exact current-source canvases, with no whole-image resampling. Generator's back output was one pixel narrower; it was padded at the right edge, and only local hand/cuff regions were copied. The three-quarter mouth is made neutral. RGBA difference tests show **0 changed pixels outside** documented local hand/cuff/mouth bounding regions (including 5-pixel mask allowance). Before/after sheets and 2× cuff comparisons are in previews. Cuffs appear joined in these views; fine skin colour, hand anatomy and line-weight consistency remain subject to Claude's review, especially the more detailed nails on the back hands. Candidate, not approved.

## Other
All side parts are 1920×819 RGBA. Three-quarter is 1774×887, back is 1586×992. Bounds in the CSV use left/top inclusive and right/bottom exclusive. Alpha and canvases were checked; alpha edge cleanliness throughout has not been certified. P1 layered wrists were not attempted. Final video was not edited.
