// Beat 7. S07A "Not just interest on what's left:"
// S07B "interest calculated across the balances you carried since buying the sofa."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Clip, Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, pop, poseTrack, prog, track } from "../lib/anim";
import { B, assetMarkup, charTf, pose, word } from "../lib/bundle";
import { scaleAbout, setGroups } from "../lib/markup";
import { blend } from "../rig/rig";
import { planWalk, walkAt } from "../rig/walk";
import { BalanceCard } from "./S05";

export const S07A: React.FC = () => {
  const f = useCurrentFrame();
  const not = word("S07A", "not"), left = word("S07A", "left");
  // magnifier glides in and settles over the remainder (no bounce)
  const mx = track(f, [[not, 760], [not + 21, 0, E.out]]);
  const my = track(f, [[not, -60], [not + 21, 0, E.out]]);
  const label = pop(f, left, 8);
  const remy = poseTrack(f, [
    { f: 2, pose: pose("remy", "stand_neutral", { expr: { preset: "neutral", gaze: [5, -4] } }) },
    { f: 12, pose: pose("remy", "think_chin"), switchAt: 0.6 },
  ]);
  const blink = f >= 36 && f < 39;
  const ov: Record<string, Override> = {
    balance_card: { node: <BalanceCard level={0.3} remainder tf="translate(560 760) scale(1.6)" /> },
    magnifier: { pre: `translate(${mx} ${my})` },
    label: { pre: scaleAbout(540, 300, Math.max(0.001, label)), opacity: Math.min(1, label * 2) },
    remy: { pose: blink ? { ...remy, expr: { ...remy.expr, eyes: "closed" } } : remy, tf: charTf(220, 1930, 0.62) },
  };
  return <SceneWorld id="SCN_C08_NOT_JUST_LEFTOVER" ov={ov} />;
};

// balance-history geometry from diagrams.balance_history()
const BASE = 1180, X0 = 150, STEP = 66;
const barH = (i: number) => 470 - i * 33;
const H = (k: string) => `diagram_balance_history__history_${k}`;
// Remy walks back along the timeline, right → left (mirrored rig walks "forward")
const RS = 0.5, RX0 = 900, RX1 = 520;
const lookLeft = pose("remy", "stand_neutral", { expr: { preset: "curious", gaze: [4, -3] } });

export const S07B: React.FC = () => {
  const f = useCurrentFrame();
  const balances = word("S07B", "balances");
  const since = word("S07B", "since"), sofa = word("S07B", "sofa");
  const walk = planWalk({ f0: since - 8, f1: since + 40, dist: (RX0 - RX1) / RS, stepLen: 170, lead: "n", upper: lookLeft });
  // bars grow up from the axis, left → right (3 f stagger, eased out, never past their height)
  const bars: Record<string, Record<string, string | number>> = {}, chips: Record<string, Record<string, string | number>> = {};
  for (let i = 0; i < 12; i++) {
    const n = String(i + 1).padStart(2, "0");
    const g = prog(f, 6 + 3 * i, 14 + 3 * i, E.out);
    bars[`history_bar_${n}`] = { transform: scaleAbout(0, BASE, 1, Math.max(0.0001, g)), opacity: g > 0 ? 1 : 0 };
    const c = prog(f, 14 + 3 * i, 20 + 3 * i, E.out);
    chips[`history_chip_${n}`] = { transform: scaleAbout(X0 + i * STEP + 24, BASE - barH(i) - 34, Math.max(0.0001, c)), opacity: c > 0 ? 1 : 0 };
  }
  const bracket = prog(f, balances, balances + 12, E.inOut);
  const collect = fade(f, balances + 8, 10);
  const arrow = prog(f, since, since + 18, E.inOut);
  const sinceLabel = fade(f, since + 2, 8), sofaIcon = pop(f, sofa, 8);
  const w = walkAt(B.joints, walk, f);
  const settled = { ...lookLeft, body_dy: w.pose.body_dy, leg_n: w.pose.leg_n, leg_f: w.pose.leg_f, expr: { preset: "intrigued", gaze: [5, 2] as [number, number] } };
  const remy = f <= walk.fEnd ? w.pose : blend(w.pose, settled, prog(f, walk.fEnd, walk.fEnd + 8), 0.5);
  const collectM = assetMarkup("DIAGRAM_BALANCE_HISTORY_L_HISTORY_COLLECT"), traceM = assetMarkup("DIAGRAM_BALANCE_HISTORY_L_HISTORY_TRACE_BACK");
  const ov: Record<string, Override> = {
    [H("axis")]: { opacity: fade(f, 0, 6) },
    [H("bars")]: { node: <Raw m={setGroups(assetMarkup("DIAGRAM_BALANCE_HISTORY_L_HISTORY_BARS"), bars)} /> },
    [H("chips")]: { node: <Raw m={setGroups(assetMarkup("DIAGRAM_BALANCE_HISTORY_L_HISTORY_CHIPS"), chips)} /> },
    [H("collect")]: {
      node: <>
        <Clip id="s07-bracket" x={120} y={505} w={830 * bracket} h={70}><Raw m={collectM} /></Clip>
        <g opacity={collect}><Clip id="s07-collect" x={0} y={0} w={1080} h={505}><Raw m={collectM} /></Clip></g>
      </>,
    },
    [H("trace_back")]: {
      node: <>
        {/* gold arrow draws right → left (back in time) */}
        <Clip id="s07-arrow" x={Math.max(212, 930 - 720 * arrow)} y={1250} w={930 - Math.max(212, 930 - 720 * arrow)} h={80}><Raw m={traceM} /></Clip>
        <g transform={scaleAbout(160, 1298, Math.max(0.001, sofaIcon))} opacity={Math.min(1, sofaIcon * 2)}><Clip id="s07-sofa" x={100} y={1250} w={112} h={80}><Raw m={traceM} /></Clip></g>
        <g opacity={sinceLabel}><Clip id="s07-label" x={0} y={1330} w={1080} h={90}><Raw m={traceM} /></Clip></g>
      </>,
    },
    // the SCHEMATIC qualifier must stay readable, so it is drawn over Remy as he walks past
    [H("note")]: { hide: true },
    // legs always come from the walk solver (pinned before and after), so no foot pops
    remy: {
      pose: remy, tf: charTf(RX0 - w.dx * RS, 1930, RS, true),
      after: <g opacity={fade(f, 2, 8)}><Raw m={assetMarkup("DIAGRAM_BALANCE_HISTORY_L_HISTORY_NOTE")} /></g>,
    },
  };
  return <SceneWorld id="SCN_C09_BALANCE_HISTORY" ov={ov} />;
};
