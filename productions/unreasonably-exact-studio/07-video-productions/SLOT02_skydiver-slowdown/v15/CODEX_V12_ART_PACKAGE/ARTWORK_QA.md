# V12 artwork QA — CANDIDATE, NOT READY TO ANIMATE

## Side master and rest
Source `v11/codex_request/side_body_v11_repaired.png`, 1920×819. Original split into same-canvas RGBA components. Rest assembled over sky blue exactly matches the master over the same sky background: ImageMagick AE = 0 (see qa/rest_pixel_comparison.txt). Boots remain unchanged. The split is a disjoint partition, not a finished rig: portions of neighbouring clothing/straps can be present in a cutout.

## Motion FAIL
No painted or generated hidden torso, sleeve overlap or cloth joint coverage is integrated. Diagnostic tests rotate only individual layers, not a hierarchical chain, using approximate trial points; these trial points are not certified pivots. Visible gaps and cut edges occur, especially shoulder and elbow; hand is left behind because diagnostics isolate individual rotations. See qa/upper_plus20.png and qa/forearm_plus20.png, plus previews/side_diagnostic_extremes.png. Raised 0/+15 and lift proof are not validated. Do not animate this partition as delivered. Exact pivots are null.

## Bare hands and expression
Three-quarter and back candidates use image-generated hand edits constrained to local regions, with original pixels elsewhere. Three-quarter mouth edit was feathered to remove an initial hard rectangle; edge and colour consistency remain unverified. Hand/cuff seams, skin consistency and back resampling need review. Back source is 1586×992; the generated candidate was 1585×992 and was resampled before local patches. These are not approved.

## Wrist layers
Face, housing, strap and arm are same-canvas disjoint visual partitions; rest previews reconstruct the source. Housing retains small skin/sleeve fragments and strap hardware; no arm is reconstructed under the device. The separations have hard internal cuts and are not clean nudge-ready isolated components. Faces are blank, but their boundary and centre estimates are approximate and rotated shapes do not fit an axis-aligned ellipse perfectly. 12 o'clock is unknown. Do not use estimates as final registration without fitting.

## Generated variants and alpha
The glance and raised layers are rough masks cut from generated full-pose edits; include foreign fragments or hard cut edges and have not been registered. Some input artwork contains low-alpha coloured fringes, which remain; no clean-alpha certification. P1 and P2 not produced. V1–V11 sources are untouched.

## Additional generated experiments
`sources/torso_underlay_generation.png` depicts reconstructed jacket beneath the removed near arm; `character/side/side_torso_underlay_candidate.png` is an unregistered partial extraction. It is not integrated into the rest assembly or motion-tested. `sources/sleeve_overlap_generation.png` has a large haze and is not registered or suitable for use.
