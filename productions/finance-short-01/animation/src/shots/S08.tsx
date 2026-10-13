// Beat 8. S08 "Even making every minimum payment might not clear it in time."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, pop, poseTrack, prog, track } from "../lib/anim";
import { C, assetMarkup, charTf, pose, word } from "../lib/bundle";
import { scaleAbout, setGroup } from "../lib/markup";
import type { NumPose } from "../rig/rig";

const M = (k: string) => `diagram_min_payments__min_${k}`;
const box = (i: number) => ({ x: 210 + (i % 4) * 220, y: 470 + Math.floor(i / 4) * 190 });
const tick = pose("remy", "tick_pen");

export const S08: React.FC = () => {
  const f = useCurrentFrame();
  const even = word("S08", "even"), might = word("S08", "might"), not = word("S08", "not"), time = word("S08", "time");
  const t0 = even, step = 3;
  const ov: Record<string, Override> = {};
  for (let i = 0; i < 12; i++) {
    const n = String(i + 1).padStart(2, "0"), { x, y } = box(i);
    const b = pop(f, t0 + step * i, 6, 0.02);
    const c = prog(f, t0 + step * i + 3, t0 + step * i + 7, E.out); // tick lands just after the box
    const m = setGroup(assetMarkup(`DIAGRAM_MIN_PAYMENTS_L_MIN_BOX_${n}`), "check_mark", {
      transform: scaleAbout(2, 0, Math.max(0.001, c)), opacity: c > 0 ? 1 : 0,
    });
    ov[M(`box_${n}`)] = { node: <g transform={scaleAbout(x, y, Math.max(0.001, b))} opacity={Math.min(1, b * 2)}><Raw m={m} /></g> };
  }
  // the conclusion appears with "might not": the remainder card rises, then the deadline flag
  const title = pop(f, might, 8);
  const card = track(f, [[not, 260], [not + 12, 0, E.out]]);
  const flag = pop(f, time - 2, 8);
  const ring = prog(f, time, time + 4) * (1 - 0.5 * prog(f, time + 14, time + 20));
  ov[M("title")] = { pre: scaleAbout(540, 300, Math.max(0.001, title)), opacity: Math.min(1, title * 2) };
  ov[M("balance_left")] = {
    pre: `translate(0 ${card})`, opacity: fade(f, not, 8),
    after: <g transform="translate(470 1130)" opacity={ring}><rect x={-156} y={4} width={312} height={68} rx={16} fill="none" stroke={C.coral} strokeWidth={7} /></g>,
  };
  ov[M("deadline_flag")] = { pre: scaleAbout(720, 1240, Math.max(0.001, flag)), opacity: Math.min(1, flag * 2) };
  // Remy ticks in rhythm with the boxes: small wrist strokes, never leaving the pen grip
  const tEnd = t0 + step * 12 + 4;
  const wob = f > t0 && f < tEnd ? Math.sin(((f - t0) / step) * Math.PI) : 0;
  const writing: NumPose = { ...tick, arm_f: [tick.arm_f[0] + 3 * wob, tick.arm_f[1] - 4 * Math.abs(wob), tick.arm_f[2] + 8 * wob] };
  const remy = poseTrack(f, [
    { f: 0, pose: { ...tick, expr: { preset: "focused", gaze: [5, -6] } } },
    { f: time, pose: { ...tick, expr: { preset: "focused", gaze: [5, -6] } } },
    { f: time + 6, pose: pose("remy", "tick_pen", { lean: 1, expr: { preset: "concerned", gaze: [6, -2] } }), switchAt: 0.3 },
  ]);
  ov.remy = { pose: f < tEnd ? { ...writing, expr: { preset: "focused", gaze: [5, -6] } } : remy, tf: charTf(150, 1960, 0.62) };
  return <SceneWorld id="SCN_C10_MIN_PAYMENTS" ov={ov} />;
};
