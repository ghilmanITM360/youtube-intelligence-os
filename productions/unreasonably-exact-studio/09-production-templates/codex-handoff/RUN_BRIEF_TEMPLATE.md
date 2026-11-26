RUN <ID> (<one-line purpose: master | layer cut | one-defect correction>).
Deliverable: runs/<ID>/<file>.png, <transparent|opaque>, <1254x1254 | 1536x1024 | 1024x1536>, <SAME canvas/position as <candidate>.png | new master>.
Attached (-i): <master or 2-3 decisive references>. Look at each with view_image first. In NOTES.md say in one line what you saw in each.
<For a correction> Defect (Claude, measured on <evidence file>): <the single defect, with the measured number>.
Do: <the single change>. Keep: <everything else, pixel-for-pixel where possible>.
Do not: add text, insets, a second view or a background; resample.
Acceptance (Claude measures): <IoU >= 0.97 vs X | angle within +-3 deg of Y | corners alpha 0 | one large component | count = N>.
