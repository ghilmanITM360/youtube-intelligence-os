// Beat 3. S03: "That "if" is the switch."  Macro: Remy's fingertip meets the IF lever and presses it.
import React from "react";
import { useCurrentFrame } from "remotion";
import { SceneWorld } from "../components/Svg";
import { E, pop, poseTrack, prog, track } from "../lib/anim";
import { B, assetMarkup, charTf, pose, word } from "../lib/bundle";
import { apply, evaluate } from "../rig/rig";
import { scaleAbout, setGroup } from "../lib/markup";

const point = pose("remy", "point_forward", { expr: { preset: "determined" } });
// arm drawn back before the reach: wrist nearer the shoulder, finger already extended
const ready = pose("remy", "point_forward", { arm_f: { ik: [560, 430], hand_dir: 8 }, expr: { preset: "determined" } });
const SW = 1.35; // switch scale in the layout
// Deviation from the C04 hero (documented): the hero put the fingertip on the switch plate edge at
// (610, 1010); for a physical press the fingertip must touch the IF lever face, so the arm is
// re-placed to land at (712, 742) — the lower-left of the lever (lever spans x 660–860, y 590–785).
const TIP_LOCAL: [number, number] = [88, -13];
const TARGET: [number, number] = [712, 742];
const tipRig = apply(evaluate(B.joints, B.slots, B.hand_front, B.rigs.remy, point).find((p) => p.id === "hand_f")!.m, TIP_LOCAL);
const ARM_TF = charTf(TARGET[0] - (tipRig[0] - 314) * 2.4, TARGET[1] - (tipRig[1] - 1030) * 2.4, 2.4);

export const S03: React.FC = () => {
  const f = useCurrentFrame();
  const iff = word("S03", "if"), sw = word("S03", "switch");
  const contact = iff;
  // arm slides in from the left and extends; fingertip arrives exactly at contact
  const slide = track(f, [[4, -320], [contact, 0, E.out]]);
  const lift = track(f, [[4, 140], [contact, 0, E.out]]); // arrives on a rising diagonal, landing on the lever
  const arm = poseTrack(f, [{ f: 6, pose: ready }, { f: contact, pose: point, ease: E.out }]);
  // press: lever and finger travel 4 px together, then hold (no rebound)
  const press = 4 * prog(f, contact, contact + 4, E.inOut);
  const lever = setGroup(assetMarkup("PRP_IF_SWITCH_UP"), "if_switch_lever_up", { transform: `translate(0 ${(press / SW).toFixed(3)})` });
  const label = pop(f, iff - 2, 8) * (1 + 0.04 * Math.sin(Math.PI * prog(f, sw, sw + 10, E.linear)));
  return (
    <SceneWorld id="SCN_C04_IF_SWITCH" ov={{
      if_switch: { node: <g transform="translate(760 820) scale(1.35)" dangerouslySetInnerHTML={{ __html: lever }} /> },
      remy_arm: { pose: arm, pre: `translate(${slide} ${lift + press})`, tf: ARM_TF },
      "ui:qualifier": { pre: scaleAbout(540, 300, Math.max(0.001, label)), opacity: Math.min(1, label * 2) },
    }} />
  );
};
