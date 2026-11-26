# Skydiver rig manifest

Four full-body rigs have 15 transparent vector layers each. The close-up has six. The path and pivot of every part are recorded in the corresponding JSON.

| View | Rig definition |
|---|---|
| Side | [Side rig](rigs/side/rig.json) |
| Three-quarter | [Three-quarter rig](rigs/three_quarter/rig.json) |
| Front | [Front rig](rigs/front/rig.json) |
| Back | [Back rig](rigs/back/rig.json) |
| Close-up | [Close-up rig](rigs/closeup/rig.json) |

All views use a 640 × 400 rest canvas. Positive x points right. Positive y points down. Positive angles rotate clockwise. Each SVG shares its view's full canvas, origin and rest pose. The manifest lists paint order from farthest to nearest. A parent can occur later in paint order, so resolve the complete ID map before composing transforms. For each part, apply the global placement followed by the ancestor rotations from root to parent, then the part's own rotation about its listed rest-space pivot. SVG transforms inside each asset belong to the drawing.

## Controls

| Root or chain | Rotation or drawing control |
|---|---|
| `torso` | Body root. Apply the shot's travel and scale outside this rig. |
| `torso → head` | Neck tilt. Helmet and goggles follow the face. |
| `torso → pack` | Pack stays closed. Restrict mounted motion to ±3°. |
| `torso → {near,far}_upper_arm → {near,far}_forearm → {near,far}_hand` | Shoulder, elbow and wrist pivots. A controller moves its descendants as a unit. |
| `torso → {near,far}_thigh → {near,far}_shin → {near,far}_foot` | Hip, knee and ankle pivots. Use modest changes around the already flexed rest drawings. |
| Close-up `head → eyes, brows, mouth, lids` | The eyes can take a small translation together. The mouth and brows each have their own resting pivot. The paired lids overlay the eyes at opacity 1, returning to the default opacity 0 after a blink. |

Each limit is expressed in degrees relative to rest. Limits are individual mechanical bounds. Stage interacting limbs by eye when combining rotations. Broad silhouette changes should use an angle-specific drawing.

## Editing and inspection

The distributed SVGs and JSON are directly editable. [build_rigs.py](assets/character/build_rigs.py) regenerates them from the Bézier drawing definitions and per-view joint coordinates. Make changes in the generator if they must survive regeneration. [preview_rigs.py](rigs/preview_rigs.py) uses CairoSVG and Pillow to render both rest and alternate hierarchical poses to the [turnaround sheet](rigs/turnaround.jpg). The sheet includes a head turn, a closed eye pose and counterposed limb angles. An initial side-profile inspection exposed weak neck-to-shoulder contact. The final profile and three-quarter drawings include a neck overlap, and the three-quarter face has an asymmetrical goggle bridge and repositioned features.
