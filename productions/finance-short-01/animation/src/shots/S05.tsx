// Beat 5 (teal path). S05A "Meet the terms and clear the promotional balance before the deadline,"
// S05B "and that interest is waived."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, pop, poseTrack, prog, track } from "../lib/anim";
import { B, C, assetMarkup, charPoint, charTf, pose, word } from "../lib/bundle";
import { scaleAbout } from "../lib/markup";
import type { NumPose } from "../rig/rig";

const REMY = { x: 200, y: 1960, s: 0.72 };
const CARD = { x: 560, y: 1010, s: 1.25 };
const SLOT: [number, number] = [CARD.x, CARD.y - 110 * CARD.s]; // top edge of the balance card
const TIP: [number, number] = [60, 10]; // release-hand fingertip (scenes.py coin_from)

/** Balance card with a live fill bar. Geometry and colours are the props.balance_card generator's
 *  (bar x −146, y 14, h 48, full width 292), drawn over the registered empty card. */
export const BalanceCard: React.FC<{ level: number; tf: string; remainder?: boolean }> = ({ level, tf, remainder }) => (
  <g transform={tf}>
    <Raw m={assetMarkup("PRP_BALANCE_CARD_000")} />
    {level > 0.001 && <rect x={-146} y={14} width={292 * level} height={48} rx={11} fill={remainder ? C.coral : C.teal_lt} />}
  </g>
);

// four payments: coin leaves the hand at r, lands in the card slot 14 frames later
const releases = (meet: number) => [0, 1, 2, 3].map((i) => meet + 4 + i * 20);
const FLIGHT = 14;
const base = pose("remy", "drop_coin");
const cocked = pose("remy", "drop_coin", { arm_f: { ik: [560, 600], hand_dir: 20 }, hand_f: "fist", lean: 3 });
const tossed = pose("remy", "drop_coin", { arm_f: { ik: [600, 470], hand_dir: 40 }, lean: 7 });

function tossPose(f: number, rs: number[]): NumPose {
  const keys = rs.flatMap((r) => [
    { f: r - 7, pose: base }, { f: r - 2, pose: cocked, switchAt: 0.3 }, { f: r, pose: tossed, ease: E.out }, { f: r + 8, pose: base },
  ]);
  return poseTrack(f, keys);
}

const coinAt = (from: [number, number], u: number): [number, number] => {
  // projectile with constant gravity: apex ~110 px above the slot, then falls into it
  const [x0, y0] = from, [x1, y1] = SLOT;
  const H = (y0 - y1) * 0.55 + 110;
  return [x0 + (x1 - x0) * u, y0 + (y1 - y0) * u - 4 * H * u * (1 - u)];
};

export const S05A: React.FC = () => {
  const f = useCurrentFrame();
  const meet = word("S05A", "meet"), deadline = word("S05A", "deadline");
  const rs = releases(meet);
  const p = tossPose(f, rs);
  const expr = { preset: "determined", gaze: [4, -6] as [number, number] };
  const remy = { ...p, expr };
  const hand = charPoint(remy, "hand_f", TIP, REMY.x, REMY.y, REMY.s);
  // fill steps down at each landing (no overshoot): 1 → .75 → .5 → .25 → 0
  const level = 1 - rs.reduce((acc, r) => acc + 0.25 * prog(f, r + FLIGHT, r + FLIGHT + 5), 0);
  const coins = rs.map((r, i) => {
    if (f < r - 7 || f > r + FLIGHT) return null;
    const [x, y] = f <= r ? hand : coinAt(hand0(r), prog(f, r, r + FLIGHT, E.linear));
    const behind = f > r + FLIGHT - 3; // last frames: slipping into the card, drawn under it
    return { key: i, behind, node: <g key={i} transform={`translate(${x} ${y}) rotate(${(f - r) * 9}) scale(0.62)`}><Raw m={assetMarkup("PRP_COIN")} /></g> };
  }).filter(Boolean) as { key: number; behind: boolean; node: React.ReactNode }[];
  function hand0(r: number) { return charPoint(tossPose(r, rs), "hand_f", TIP, REMY.x, REMY.y, REMY.s); }
  // months light up as time passes (procedural progress bar under the strip)
  const months = Math.min(12, 12 * prog(f, rs[0], rs[3] + FLIGHT, E.linear));
  const title = pop(f, meet, 8), flag = pop(f, deadline, 8, 0.03);
  const ov: Record<string, Override> = {
    title: { pre: scaleAbout(540, 300, Math.max(0.001, title)), opacity: Math.min(1, title * 2) },
    balance_card: {
      node: <>
        {coins.filter((c) => c.behind).map((c) => c.node)}
        <BalanceCard level={level} tf={`translate(${CARD.x} ${CARD.y}) scale(${CARD.s})`} />
      </>,
    },
    coin_1: { hide: true }, coin_2: { hide: true },
    month_strip: { after: <rect x={156} y={1226} width={Math.max(0, months * 64 - 6)} height={10} rx={5} fill={C.gold} /> },
    deadline_flag: { pre: scaleAbout(890, 1150, Math.max(0.001, flag)), opacity: Math.min(1, flag * 2) },
    remy: { pose: remy, tf: charTf(REMY.x, REMY.y, REMY.s), after: coins.filter((c) => !c.behind).map((c) => c.node) },
  };
  return <SceneWorld id="SCN_C06A_PAID_IN_FULL" ov={ov} />;
};

export const S05B: React.FC = () => {
  const f = useCurrentFrame();
  const waived = word("S05B", "waived");
  // the C06A title and flag clear before the outcome lands
  const oldTitle = 1 - fade(f, waived - 6, 5);
  const flag = 1 - fade(f, 0, 8);
  const title = pop(f, waived, 8);
  // stamp hits: 1.6 → 1 in 5 frames, then a 2-frame settle
  const st = f < waived ? 0 : track(f, [[waived, 1.6], [waived + 5, 0.98, E.in], [waived + 7, 1, E.out]]);
  const receipt = 1 - fade(f, waived + 10, 12);
  const remy = poseTrack(f, [
    { f: 0, pose: { ...base, expr: { preset: "determined", gaze: [4, -6] } } },
    { f: 12, pose: pose("remy", "stand_neutral", { expr: { preset: "content", gaze: [4, -4] } }), switchAt: 0.5 },
    { f: waived + 1, pose: pose("remy", "stand_neutral", { expr: { preset: "content", gaze: [4, -4] } }) },
    { f: waived + 9, pose: pose("remy", "relieved"), switchAt: 0.3 },
  ]);
  const ov: Record<string, Override> = {
    title: {
      node: <>
        <g opacity={oldTitle}><Raw m={B.markup[B.scenes.SCN_C06A_PAID_IN_FULL.world.find((i) => i.id === "title")!.m!]} tf="translate(540 300)" /></g>
        <g opacity={Math.min(1, title * 2)} transform={scaleAbout(540, 300, Math.max(0.001, title))}><Raw m={B.markup[B.scenes.SCN_C06B_WAIVED.world.find((i) => i.id === "title")!.m!]} tf="translate(540 300)" /></g>
      </>,
    },
    balance_card: { node: <BalanceCard level={0} tf={`translate(${CARD.x} ${CARD.y}) scale(${CARD.s})`} /> },
    receipt: { opacity: receipt, pre: `translate(0 ${-30 * (1 - receipt)})` },
    stamp: { pre: scaleAbout(800, 620, Math.max(0.001, st)), opacity: st > 0 ? 1 : 0 },
    month_strip: {
      after: <>
        <rect x={156} y={1226} width={12 * 64 - 6} height={10} rx={5} fill={C.gold} />
        <g opacity={flag} transform={`translate(890 1150) scale(.75)`}><Raw m={assetMarkup("PRP_DEADLINE_FLAG")} /></g>
      </>,
    },
    remy: { pose: remy, tf: charTf(REMY.x, REMY.y, REMY.s) },
  };
  return <SceneWorld id="SCN_C06B_WAIVED" ov={ov} />;
};
