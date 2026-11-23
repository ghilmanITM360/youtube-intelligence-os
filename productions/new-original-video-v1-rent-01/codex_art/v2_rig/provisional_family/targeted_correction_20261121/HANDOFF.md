# V1 Rent targeted character corrections

Status: staged candidates, pending independent review and production integration. No production files or registry were changed.

Changed files: `rig_head_worried.{svg,png}`, `rig_head_smirk.{svg,png}`, and `rig_body_{down,shrug,point}.{svg,png}`. PNGs are RGBA, 700×700 for heads, 1300×1300 for down/shrug, 1500×1300 for point. Editable SVGs retain original canvas and transforms. Original files remain in the parent folder; use the other three unchanged heads from there.

Worried: inner eyebrows raised with angled lines, and mouth downturned. Smirk: one eyebrow raised and an asymmetric mouth. Torso: same path and outer geometry, olive fill changed from #5b6b3a to #72864a and outline reduced from 27 to 17 SVG units so the fill remains visible at small scale; limbs and pose paths remain unchanged.

The existing attachment coordinates remain head chin (350,651), body neck (650,70) for down/shrug and (750,70) for point. `all_15_alignment_1080p.jpg` shows the five heads with all three bodies using those anchors. `expression_comparison_1080p.jpg` shows original and revised faces, plus revised whole figures at 180 pixels high as a phone-scale proxy. Visual inspection shows no obvious neck gaps or clipping in this static sheet; the smirk remains subtler than worried at phone scale. RGBA dimensions, alpha range and nonempty bounds were checked for each changed PNG. These are static staging checks, not a rerender in Claude's R4/R5 scenes or an independent approval. SHA-256 digests are in `SHA256SUMS.txt`.

Claude: compare against the active R4/R5 scenes, independently review the revised expressions and torso color, and integrate only through the established approval workflow.
