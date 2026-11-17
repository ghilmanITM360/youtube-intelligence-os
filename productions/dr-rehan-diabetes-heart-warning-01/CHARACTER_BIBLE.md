# Character bible

Five original fictional identities; none depicts a real patient or Dr. Rehan. Character sources use a shared 600×900 canvas and foot anchor [285,802]. Head shell, torso clothing and hair silhouettes remain stable within identity. Neutral/explaining/concerned expressions are authored variants, not inferred emotion from real footage.

| Identity | Fixed identity cues | Delivered poses / expressions |
|---|---|---|
| CH-doctor | short slate hair, warm skin, ivory clinical coat, teal stethoscope, blank ID badge | front neutral; open hand explaining; open hand concerned; pointing explaining with shallow three-quarter facial turn |
| CH-diabetes | curly dark hair, ochre shirt with thin light seam, dark trousers | standing neutral; hand-to-chest concerned/breathless; holding glucose kit neutral; sitting concerned |
| CH-older-man | silver side hair, rounded glasses, muted teal shirt | standing neutral; hand-to-chest concerned alternative |
| CH-older-woman | silver bob, terracotta blouse, fine cheek creases | standing neutral; open hand concerned alternative |
| CH-risk-adult | dark swept hair, deeper skin tone, muted blue shirt | standing neutral; open-hand neutral |

14 pose/expression/view composites; five authored character designs. This is not 14 independent character identities. No walk cycle or full turnaround needed for the current scenes. The three-quarter option is a shallow illustrative face turn, not a 3D rotation.

Each composite has seven named groups: legs, torso, arm-left, arm-right, head, eyes-brows, mouth. Independently editable SVG and transparent PNG parts share the full parent canvas, so no trim-origin compensation is necessary. Swap whole poses at one frame; for expression-only changes swap eyes-brows and mouth together, preserving head/hair/clothing. Never animate a hand independently away from its sleeve. Eyebrows and eyes are kept together to avoid drift.

Parts are derivatives, not new authored designs. PART_REGISTER.csv records IDs, parents, local anchors, dependencies and hashes. Arm/hand artwork is one part to preserve wrist contact. Head/hair/ears are one part; eyes, brows and nose share a facial part. No phoneme or lip-sync variants supplied.

Contact rules: S04-B kit is above the character in z-order and attached to left-hand contact; parent them for any movement. S03-B seated character and chair move as one interaction unit. S07-C clipboard/stethoscope is a diagram overlay near pointing hand, not a held prop; do not move it as if attached. Other medical objects are explanatory overlays. No unsupported hand-held object in other scenes.

Do not recolor outfits mid-video. Do not use the concerned older-adult alternatives to suggest all older people have the same symptoms. No stigma signifiers or exaggerated frailty. Owner approval of the generic presenter remains required before use beside a real doctor's voice.
