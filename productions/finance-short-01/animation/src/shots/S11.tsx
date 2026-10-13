// Beat 11-12. S11 "The sofa came home on day one."  S12 "The interest was waiting there too."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, pop, prog, track } from "../lib/anim";
import { B, charTf, pose, word } from "../lib/bundle";
import { scaleAbout, setGroup } from "../lib/markup";
import { apply, blend, evaluate, legIK, type NumPose, type Pt } from "../rig/rig";

const REMY = { x: 420, y: 1650, s: 0.78 };
const sit = pose("remy", "sit_relaxed");
const standUp = pose("remy", "stand_neutral", { expr: { preset: "content", gaze: [4, 0] } });
// where the seated pose puts each ankle (rig frame, includes body_dy): these stay planted
const ankleOf = (p: NumPose, side: "n" | "f"): Pt =>
  apply(evaluate(B.joints, B.slots, B.hand_front, B.rigs.remy, p).find((q) => q.id === `shoe_${side}`)!.m, B.joints[`ankle_${side}`]);
const AN = ankleOf(sit, "n"), AF = ankleOf(sit, "f");
const BX0 = AN[0] - B.joints.ankle_n[0]; // standing body offset that puts the near foot on its seated spot

/** Stand-to-sit with both feet planted: the pelvis travels back and down onto the seat while leg IK
 *  keeps the ankles fixed. Torso leans forward to counterbalance, then settles back. */
function sitDown(f: number, f0: number, f1: number): { pose: NumPose; bx: number } {
  const u = prog(f, f0, f1, E.inOut);
  const bx = BX0 * (1 - u);
  const dy = 6 + (sit.body_dy - 6) * prog(f, f0 + 2, f1, E.inOut);
  const lean = track(f, [[f0 - 4, 0], [f0 + 4, 12], [f1 - 2, 6], [f1 + 6, sit.lean]]);
  const leg = (side: "n" | "f", a: Pt) => legIK(B.joints, side, [a[0] - bx, a[1] - dy], 0);
  const upper = blend(standUp, sit, u, 0.6);
  return {
    bx,
    pose: { ...upper, lean, body_dy: dy, leg_n: leg("n", AN), leg_f: leg("f", AF), slots: u > 0.55 ? sit.slots : {} },
  };
}

export const S11: React.FC = () => {
  const f = useCurrentFrame();
  const sofa = word("S11", "sofa"), day = word("S11", "day");
  const s0 = 2, s1 = sofa + 8;
  const { pose: p, bx } = sitDown(f, s0, s1);
  // cushion takes the weight: seat compresses 1.5 % and recovers, no bounce
  const squash = 1 - 0.015 * Math.sin(Math.PI * prog(f, s1 - 1, s1 + 8, E.linear));
  const tag = pop(f, day, 8);
  const expr = f >= s1 + 4 ? { preset: "content" } : { preset: "neutral", gaze: [4, 2] as [number, number] };
  const ov: Record<string, Override> = {
    sofa__seat: { pre: scaleAbout(560, 1614, 1, squash) },
    remy: { pose: { ...p, expr }, tf: charTf(REMY.x + bx * REMY.s, REMY.y, REMY.s) },
    day1_tag: { pre: scaleAbout(860, 1330, Math.max(0.001, tag)), opacity: Math.min(1, tag * 2) },
  };
  return <SceneWorld id="SCN_C13_SOFA_HOME" ov={ov} />;
};

const CLOCK_TF = "translate(742 1352) scale(0.2)";
const clockMarkup = B.markup[B.scenes.SCN_C14_INTEREST_WAITING.world.find((i) => i.id === "clock")!.m!];

export const S12: React.FC = () => {
  const f = useCurrentFrame();
  const waiting = word("S12", "waiting"), there = word("S12", "there"), too = word("S12", "too");
  // camera refits from the C13 framing to the approved C14 close-up
  const u = prog(f, 0, 30, E.inOut);
  const camera = `translate(${-210 * u} ${-560 * u}) scale(${1 + 0.35 * u})`;
  // receipt rises from behind the cushion edge, clock appears; the minute hand ticks back once
  const r = prog(f, waiting, waiting + 9, E.out);
  const clock = pop(f, waiting + 3, 8);
  const tick = -30 * prog(f, there, there + 4, E.inOut);
  const clockM = setGroup(clockMarkup, "clock_hand_minute", { transform: `rotate(${tick.toFixed(2)})` });
  const notice = prog(f, waiting + 3, waiting + 12, E.inOut);
  const remy = blend({ ...sit, expr: { preset: "content" } }, pose("remy", "sit_notice"), notice, 0.5);
  const ov: Record<string, Override> = {
    remy: { pose: remy, tf: charTf(REMY.x, REMY.y, REMY.s) },
    receipt: { opacity: r, pre: `translate(0 ${(50 * (1 - r)).toFixed(2)})` },
    clock: { node: <g transform={scaleAbout(742, 1352, Math.max(0.001, clock))} opacity={Math.min(1, clock * 2)}><Raw m={clockM} tf={CLOCK_TF} /></g> },
    "ui:qualifier": { opacity: fade(f, too, 8) },
  };
  return <SceneWorld id="SCN_C14_INTEREST_WAITING" camera={camera} ov={ov} />;
};

