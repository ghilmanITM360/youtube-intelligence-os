// Beat 10. S10A "So check the promotion's deadline,"  S10B "not just your monthly payment date."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld, type Override } from "../components/Svg";
import { E, pop, prog } from "../lib/anim";
import { markerTipAt } from "../lib/marker";
import { C, assetMarkup, charPoint, charTf, pose, shot, word } from "../lib/bundle";
import { scaleAbout, without } from "../lib/markup";
import { apply, mul, R, S as Sc, T, type IKSpec, type NumPose } from "../rig/rig";

const REMY = { x: 330, y: 1760, s: 0.85 };
const base = pose("remy", "circle_marker");
const BASE_IK = { ik: [600, 290] as [number, number], hand_dir: -34 };
// calendar "PROMO ENDS" mark (props.calendar_page mark='circle'), placed at (800, 940) scale 1.45
const MARK = '<ellipse cx="47" cy="60" rx="34" ry="28" fill="none" stroke="#F16850" stroke-width="9"/>';
const CAL = { x: 800, y: 940, s: 1.45 };
const EL = { cx: CAL.x + 47 * CAL.s, cy: CAL.y + 60 * CAL.s, rx: 34 * CAL.s, ry: 28 * CAL.s };
const TURN = 2 * Math.PI * 1.08; // a hand-drawn circle overlaps its start a little

/** Marker tip in scene coordinates for a pose (marker prop: hand_f · T(26,-6) R(70) S(.8); tip ≈ (1, 76)). */
const tipOf = (p: NumPose) => {
  const [hx, hy] = charPoint(p, "hand_f", [0, 0], REMY.x, REMY.y, REMY.s);
  const [ax, ay] = charPoint(p, "hand_f", [1, 0], REMY.x, REMY.y, REMY.s);
  const [bx, by] = charPoint(p, "hand_f", [0, 1], REMY.x, REMY.y, REMY.s);
  const m = mul([ax - hx, ay - hy, bx - hx, by - hy, hx, hy], mul(T(26, -6), mul(R(70), Sc(0.8))));
  return apply(m, [1, 76]);
};
const TIP0 = tipOf(base);
const elPt = (th: number): [number, number] => [EL.cx + EL.rx * Math.cos(th), EL.cy + EL.ry * Math.sin(th)];
/** Pose whose marker tip sits at scene point q (wrist IK shifted; hand angle unchanged, so the tip offset is rigid). */
const poseForTip = (q: [number, number]): NumPose =>
  pose("remy", "circle_marker", {
    arm_f: { ...BASE_IK, ik: [BASE_IK.ik[0] + (q[0] - TIP0[0]) / REMY.s, BASE_IK.ik[1] + (q[1] - TIP0[1]) / REMY.s] } as IKSpec,
  });

function Dates({ t }: { t: number }) {
  const A = shot("S10A").from, w = (id: string, n: string) => word(id, n) + shot(id).from - A;
  const check = w("S10A", "check"), deadline = w("S10A", "deadline");
  const b0 = shot("S10B").from - A, monthly = w("S10B", "monthly"), date = w("S10B", "date");
  // approach: tip travels to the circle's start, then traces it in sync with "deadline"
  const d0 = deadline, d1 = deadline + 20;
  const th = TURN * prog(t, d0, d1, E.inOut);
  const tip = markerTipAt(t, check, deadline, TIP0, elPt, TURN);
  const nPts = Math.max(2, Math.ceil((th / TURN) * 70));
  const traced = t >= d0 ? Array.from({ length: nPts }, (_, i) => elPt((th * i) / (nPts - 1))) : [];
  const gazeUp = t >= monthly - 4;
  const remy = { ...poseForTip(tip), expr: { preset: "determined", gaze: (gazeUp ? [4, -6] : [5, -2]) as [number, number] } };
  const due = pop(t, b0 + 4, 8), every = pop(t, monthly, 8), one = pop(t, date, 8), cal = pop(t, 2, 8);
  const ov: Record<string, Override> = {
    cal_due: { pre: scaleAbout(720, 450, Math.max(0.001, due)), opacity: Math.min(1, due * 2) },
    cal_promo: {
      node: <g transform={scaleAbout(CAL.x, CAL.y, Math.max(0.001, cal))} opacity={Math.min(1, cal * 2)}>
        <Raw m={without(assetMarkup("PRP_CALENDAR_PAGE_PROMO_ENDS"), MARK)} tf={`translate(${CAL.x} ${CAL.y}) scale(${CAL.s})`} />
        {traced.length > 1 && <polyline points={traced.map((p) => p.map((v) => v.toFixed(1)).join(",")).join(" ")} fill="none" stroke={C.coral} strokeWidth={9 * CAL.s} strokeLinecap="round" strokeLinejoin="round" />}
      </g>,
    },
    remy: { pose: remy, tf: charTf(REMY.x, REMY.y, REMY.s) },
    "ui:label_due": { pre: scaleAbout(720, 630, Math.max(0.001, every)), opacity: Math.min(1, every * 2) },
    "ui:label_promo": { pre: scaleAbout(800, 1170, Math.max(0.001, one)), opacity: Math.min(1, one * 2) },
  };
  return <SceneWorld id="SCN_C12_TWO_DATES" ov={ov} />;
}

export const S10A: React.FC = () => <Dates t={useCurrentFrame()} />;
export const S10B: React.FC = () => <Dates t={useCurrentFrame() + shot("S10B").from - shot("S10A").from} />;
