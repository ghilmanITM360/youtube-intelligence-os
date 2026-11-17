// Beat 1 hook. S01A: "No interest?"  S01B: "Then why the interest bill?"
import React from "react";
import { useCurrentFrame } from "remotion";
import { SceneWorld } from "../components/Svg";
import { E, poseTrack, prog, track } from "../lib/anim";
import { C, charTf, pose, word } from "../lib/bundle";
import type { PropSpec } from "../rig/rig";

const signTf = (dy: number, rot: number) => `translate(540 ${170 + dy}) rotate(${rot}) scale(1.4)`;

// S01A end state, reused as the S01B start so the cut is continuous
const shrugHold = pose("remy", "shrug", { neck: -7 });

export const S01A: React.FC = () => {
  const f = useCurrentFrame();
  // hanging sign drops in and swings about its string tops (damped, max 2.5° overshoot)
  const dy = track(f, [[0, -560], [12, 0, E.out]]);
  const rot = track(f, [[0, -8], [12, 2.5, E.out], [18, -1], [24, 0]]);
  // Remy rises into frame (feet are below the crop), then shrugs with a small anticipation dip
  const rise = track(f, [[2, 520], [15, 0, E.out]]);
  const stand = pose("remy", "stand_neutral", { expr: { preset: "neutral", gaze: [2, -2] } });
  const dip = pose("remy", "stand_neutral", { neck: 3, arm_n: [10, -8, 0], arm_f: [-10, 8, 0], expr: { preset: "neutral", gaze: [2, -2] } });
  const shrug = pose("remy", "shrug");
  const p = poseTrack(f, [
    { f: 8, pose: stand }, { f: 11, pose: dip }, { f: 20, pose: shrug, ease: E.out },
    { f: 30, pose: shrugHold },
  ]);
  const blink = f >= 31 && f < 34;
  return (
    <SceneWorld id="SCN_C01A_HOOK_SIGN" ov={{
      promo_sign: { tf: signTf(dy, rot) },
      remy: { pose: blink ? { ...p, expr: { ...p.expr, eyes: "closed" } } : p, tf: charTf(540, 2040 + rise, 1.2) },
    }} />
  );
};

// Statement prop exactly as hold_bill holds it, so the hand-off from free motion to grip has no pop.
const billPose = pose("remy", "hold_bill");
const statement = billPose.props[0];
const ROW_RING = `<rect x="-150" y="56" width="300" height="70" rx="14" fill="none" stroke="${C.coral}" stroke-width="7"/>`;

export const S01B: React.FC = () => {
  const f = useCurrentFrame();
  const contact = 13, grip = 15, bill = word("S01B", "bill");
  // push in: Remy's placement moves from the S01A framing to the C01B framing
  const u = prog(f, 0, 14);
  const fx = 540 + (520 - 540) * u, fy = 2040 + (2090 - 2040) * u, s = 1.2 + (1.38 - 1.2) * u;
  // statement rises into the hands, decelerating to rest exactly at contact
  const rise = track(f, [[1, 620], [contact, 0, E.out]]);
  const reach = { ...billPose, hand_n: "open", hand_f: "open", flip_f: true, props: [], expr: shrugHold.expr };
  const body = poseTrack(f, [
    { f: 0, pose: { ...shrugHold, props: [] } },
    { f: contact, pose: reach, switchAt: 0.4 },
    { f: grip, pose: { ...billPose, expr: { preset: "concerned", gaze: [0, 5] } } },
  ]);
  const look = f >= bill + 1 ? { preset: "concerned", gaze: [1, -1] as [number, number] } : body.expr;
  // interest row pulse on "bill": ring scales 1 → 1.04 → 1 around the row, in the prop sandwich
  const pulse = 1 + 0.04 * Math.sin(Math.PI * prog(f, bill, bill + 10, E.linear));
  const ringOpacity = prog(f, bill - 2, bill + 2) * (1 - 0.4 * prog(f, bill + 12, bill + 18));
  const props: PropSpec[] = [{ ...statement, at: [statement.at[0], statement.at[1] + rise, statement.at[2], statement.at[3]] }];
  if (ringOpacity > 0) {
    const ring = `<g opacity="${ringOpacity.toFixed(3)}" transform="translate(0 91) scale(${pulse.toFixed(4)}) translate(0 -91)">${ROW_RING}</g>`;
    props.push({ ...statement, id: "row_ring", m: ring, asset: null }); // inline markup (procedural highlight)
  }
  return (
    <SceneWorld id="SCN_C01B_HOOK_BILL" ov={{
      remy: { pose: { ...body, expr: look, props }, tf: charTf(fx, fy, s) },
    }} />
  );
};
