# Character consistency guide: the Apollo astronaut (ASTRO_*)

One character, one costume, one body, many poses. Anything that changes between poses is a failure (V10-V13 history: a different face, gloves vs bare hands, round joint caps). Written 2026-11-26 from the owner brief and the playbook §7.2-7.5; to be tightened against `research/asset_research/ASTRONAUT_RESEARCH.md` when it lands.

## Decisions (one place, never revisited per shot)
| Item | Decision |
|---|---|
| Role in the film | B18 only (about 4 s): a kneeling astronaut beside the reflector, for scale and for "astronauts placed it" |
| Suit | Apollo 11 EVA configuration (A7L-class pressure suit, white outer layer), simplified; **hard-shell suit so visible joint rings are correct** (no soft-cloth wind folds) |
| Helmet | white shell with **gold visor down**; the face is never visible. Visor shows a distorted reflection of sky/surface (ASTRO_003 separate layer) |
| Backpack | Portable life-support system (PLSS) box, white, with the antenna stub omitted unless the references show it clearly |
| Hands | **Gloved in every view** (EVA gloves). Five-finger silhouette, bulky; never bare |
| Boots | lunar overshoes, grey-white, ridged soles |
| Identity | anonymous: no name, no patch that identifies a person, no flag unless the references show it on the suit |
| Movement | whole-pose blends with limb offsets (see RIGGING_REQUIREMENTS); **no wind-driven cloth, no billowing**; dust moves in ballistic arcs under 1.62 m/s2 |
| Scale | an adult in the suit is about 1.8-1.9 m standing; the reflector panel is 46 cm; keep that ratio exact in every shot |

## Pose set (ASTRO_010)
Minimum delivered poses, all on the same canvas, same scale, same ground contact point:
`kneel_side`, `stand_side`, `kneel_three_quarter`, `stand_three_quarter`, `reach_down_side` (equipment interaction), `stand_back`, `walk_contact_side`, `walk_passing_side`.
Only `kneel_*` and `reach_down_side` are used on screen in V1; the rest exist because the brief asks for a complete turnaround and because B18 may be re-blocked. Do not spend more than one iteration on poses the storyboard does not use.

## Layer parts per pose
Helmet, visor, visor reflection, torso, PLSS, near/far upper arms, near/far forearms, near/far gloves, near/far thighs, near/far shins, near/far boots, contact shadow (separate), plus hidden overlap under every child. Draw order and parent tree: RIGGING_REQUIREMENTS section 3.

## Identity test (run on every delivery)
Place all delivered views side by side. Pass only if: same helmet shape and visor tint, same backpack proportions, same glove style on both hands, same suit panel logic, same boot design, same overall height-to-width ratio. Write the result in `ARTWORK_QA.md`, including the views that failed.

## Known failure modes to design against
1. Fused backpack and torso (cannot rotate separately). 2. Gloves changing colour or becoming bare hands. 3. Extra or missing fingers. 4. Visor showing a face. 5. Boots that differ left/right. 6. Cloth folds that imply wind. 7. Detached equipment floating beside the body. 8. Proportions drifting (head size) between poses. 9. A visible round "cap" at a joint instead of a purposely drawn suit joint ring.
