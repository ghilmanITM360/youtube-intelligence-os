// Beat 2. S02A: "Imagine buying a sofa on a store card."  S02B: "No interest if paid in full within 12 months."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld } from "../components/Svg";
import { E, fade, pop, poseTrack, prog, track } from "../lib/anim";
import { B, assetMarkup, charTf, pose, word } from "../lib/bundle";
import { setGroups, scaleAbout } from "../lib/markup";
import { planWalk, walkAt } from "../rig/walk";
import { blend } from "../rig/rig";

// Walk-in: Remy is already walking when the shot opens and stops at the hero mark (250, 1800).
const S = 0.62, X0 = -300, X1 = 250;
const curious = pose("remy", "stand_neutral", { expr: { preset: "curious", gaze: [4, 0] } });
const WALK = planWalk({ f0: -14, f1: 50, dist: (X1 - X0) / S, stepLen: 170, lead: "n", upper: curious });

export const S02A: React.FC = () => {
  const f = useCurrentFrame();
  const sofa = word("S02A", "sofa"), card = word("S02A", "card");
  const w = walkAt(B.joints, WALK, f);
  // after stopping: legs stay pinned where the walk left them, upper body settles; looks at the associate on "store card"
  const lookAt = pose("remy", "stand_neutral", { expr: { preset: "curious", gaze: [5, -1] } });
  const settled = { ...lookAt, body_dy: w.pose.body_dy, leg_n: w.pose.leg_n, leg_f: w.pose.leg_f };
  const remy = f <= WALK.fEnd ? w.pose : blend({ ...w.pose, expr: curious.expr }, settled, prog(f, WALK.fEnd, WALK.fEnd + 8), 0.5);
  const glance = f >= card - 4 ? { ...remy, expr: { preset: "curious", gaze: [6, -2] as [number, number] } } : remy;
  // associate presents the sofa on "sofa"
  const assoc = poseTrack(f, [
    { f: sofa - 2, pose: pose("assoc", "assoc_stand") },
    { f: sofa + 8, pose: pose("assoc", "assoc_present"), switchAt: 0.5 },
  ]);
  return (
    <SceneWorld id="SCN_C02_STORE_WIDE" ov={{
      // the foreground plant is nearer the camera than Remy's path, so it is drawn over him
      env_store__store_fg_plant: { hide: true },
      remy: { pose: glance, tf: charTf(X0 + w.dx * S, 1800, S), after: <Raw m={assetMarkup("ENV_STORE_L_STORE_FG_PLANT")} /> },
      associate: { pose: assoc },
      "ui:qualifier": { opacity: fade(f, 5, 10) },
    }} />
  );
};

const sheetPose = pose("remy", "hold_sheet");
const sheet = sheetPose.props[0];
const sheetMarkup = B.markup[sheet.m];

export const S02B: React.FC = () => {
  const f = useCurrentFrame();
  const no = word("S02B", "no"), iff = word("S02B", "if"), paid = word("S02B", "paid");
  // the offer prints itself in the order it is read: headline, IF, condition
  const h = fade(f, no - 1, 6), i = pop(f, iff - 1, 8, 0.03), c = fade(f, paid - 1, 8);
  const m = setGroups(sheetMarkup, {
    offer_headline: { opacity: h.toFixed(3), transform: `translate(0 ${(8 * (1 - h)).toFixed(2)})` },
    offer_if: { opacity: Math.min(1, i * 1.6).toFixed(3), transform: scaleAbout(0, 8, Math.max(0.001, 0.6 + 0.4 * i)) },
    offer_condition: { opacity: c.toFixed(3), transform: `translate(0 ${(8 * (1 - c)).toFixed(2)})` },
  });
  const expr = f >= iff + 2 ? { preset: "intrigued", gaze: [2, 5] as [number, number] } : { preset: "neutral", gaze: [2, 5] as [number, number] };
  const blink = f >= 62 && f < 65;
  const remy = { ...sheetPose, expr: blink ? { ...expr, eyes: "closed" } : expr, props: [{ ...sheet, m }] };
  // associate eases back from handing over the sheet to an open-palm "here's the deal"
  const assoc = poseTrack(f, [
    { f: 2, pose: pose("assoc", "assoc_offer_sheet") },
    { f: 16, pose: pose("assoc", "assoc_present"), switchAt: 0.5 },
  ]);
  const push = track(f, [[no, 1], [80, 1.14, E.inOut]]);
  return (
    <SceneWorld id="SCN_C03_CHECKOUT_OFFER" camera={scaleAbout(330, 1010, push)} ov={{
      remy: { pose: remy },
      associate: { pose: assoc },
    }} />
  );
};
