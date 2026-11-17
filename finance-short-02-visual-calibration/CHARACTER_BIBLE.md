# Original host and practical attachment rules

Retain the V2 host identity: warm tan face(#e8b780), deep brown swept hair and side bun(#433126), wide head with small readable expression, black single-line body. No hair/identity redesign. Head/torso/feet proportions stay fixed across production poses; no independent limb stretching. Character source canvas290×400; standing pelvis139,269; feet pivot139,377. Upper-body crops are only used if actually authored in ASSET_REGISTER.csv.

Neutral, explaining, surprised, worried, thinking and resolved expressions have six optional standalone FACE_* overlays. Their top-left attaches to host-local100,65; hide the existing face-feature paths before applying one. These are additional editor assets, not stacked expressions. Expression metadata and full-body child IDs remain addressable. Hands POINT/GRIP/OPEN are standalone with wrist17,40; use contact anchors from the register rather than guessing a new wrist position.

HOST_BILL contains paper behind thumb and in front of the near arm. Paper/hand must move as one parent attachment. World contact = placement + uniform_scale×local_anchor. Thumb at207,196 is visibly on the held paper. Do not animate the large separate interest-bill illustration as if it is the small held sheet.

HOST_UP,POINT,THINK,SHIELD,REPAIR and concerned variants keep head/torso geometry. Thinking hand touches chin deliberately; raised pointing hand sits beside the face. For a static shield grip, hand contacts the near edge with a separate shield layer; repair hand grips the wrench handle. Actual motion requires step switches or explicit attached-parent transforms, with final contact retested. These sources contain no IK engine or walking promises.

SUPPORT_BANKER uses separate greying hair, glasses and green tie. It is a generic institutional representative, not an identified real official. No approved narrator impersonation or real-person portrait is implied. All current poses/variants and exact pivots must be read from ASSET_REGISTER.csv; filenames in the generator that have no registered file are not claimed completed assets.
