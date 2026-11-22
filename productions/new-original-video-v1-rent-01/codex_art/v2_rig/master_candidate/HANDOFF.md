# V1 Rent long-form master candidate — independent review

Status: PENDING independent visual review. This is a single composite design candidate, not a production rig, and has not been registered. Existing generated masters remain untouched in `../originals/`.

- `master_candidate.png`: RGBA 1300 × 1900, rendered at 2600 × 3800 then downsampled; SHA-256 `ecabb8c4425e9da228d3b52e9719ea114b8fede0505d514f1130a94c2c82169f`.
- `master.svg`: editable original paths, flat fills, no filters or gradients.
- `master_playback_comparison.jpg`: earlier candidate and this master at equal displayed figure height, white and dark backgrounds.
- `validation.json`: dimensions, alpha bounds, method and limitations.

The candidate retains the earlier V1 original renter's warm skin, dark side-parted curls, olive overshirt hint and white shoes, redrawn as paths; it does not trace reference frames. Head height is approximately 610 pixels, figure height approximately 1790 pixels, ratio approximately 0.34; arm and leg paths are 45 pixels. Antialiased alpha is preserved. The dark test demonstrates low contrast between the required dark outline/limbs and the dark background; white or light scenes are the intended use.

Self-review: flat color and edges look cleaner than the generated candidate in the supplied side-by-side. Geometric regularity and round hands may require artistic review; no claim of independent approval. Hair, face and outline should be judged at video and phone scale. Compare geometry with `productions/new-original-video-v1-rent-01/V1_RENT_STYLE_FIDELITY_AUDIT.md` and `CHANNEL_VISUAL_AUDIT/CHANNEL_001/22_LONGFORM_VISUAL_DNA.md` (repository-relative paths).

Next gate: independently review the master SHA above. Only after approval, derive five aligned facial variants and three body variants from the approved geometry, export required canvases and anchors, and test layer switching in a 1080p preview. No lip-sync or registration requested. No production renderer, storyboard or registry changed.

## Independent review and targeted correction

- Initial master `ecabb8c4425e9da228d3b52e9719ea114b8fede0505d514f1130a94c2c82169f`: **PARTIAL**. Reviewer accepted the approximate proportions, originality, flat palette and light-background edges, but found the paths too mechanically regular.
- Targeted correction: `master_refined.png`, 1300 × 1900, SHA-256 `55e295e4cd8aee771f4167a37ab23e18c76eb606e9e9a4263a2c24378d2189eb`; editable source `master_refined.svg`; playback comparison `master_refined_comparison.jpg`; format results `validation_refined.json`.
- Independent re-review: **PARTIAL**. Contour corrections remain too subtle to meet the hand-drawn criterion at playback scale. Dark outlines and limbs also lack contrast on a dark plate; light backgrounds are the intended use.
- Approval gate remains unmet. Do not expand or register the character family. No pose layers, expression layers, anchor map or motion preview have been generated. The V2 handoff allows one correction round per failed asset; an owner creative decision or a new instruction on how to proceed is needed for any exception or further revision.
