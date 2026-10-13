// Beat 6 (coral path, clearly an ALTERNATIVE). S06A "Leave some unpaid,"
// S06B "and the accumulated interest can land on your bill."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, pop, poseTrack, prog, track } from "../lib/anim";
import { B, C, assetMarkup, charTf, pose, word } from "../lib/bundle";
import { scaleAbout } from "../lib/markup";
import { BalanceCard } from "./S05";

const REMY = { x: 870, y: 1990, s: 0.74 };
const CARD_TF = "translate(560 1010) scale(1.25)";
const concerned = pose("remy", "stand_neutral", { expr: { preset: "concerned", gaze: [3, 2] } });
const markupOf = (scene: string, id: string) => B.markup[B.scenes[scene].world.find((i) => i.id === id)!.m!];

/** Rewind wipe: a coral panel with ◀◀ that slides off to the left, marking an alternative path. */
const RewindWipe: React.FC<{ f: number }> = ({ f }) => {
  const x = track(f, [[0, 0], [9, -1180, E.in]]);
  if (x <= -1180) return null;
  return (
    <g transform={`translate(${x} 0)`}>
      <rect x={0} y={0} width={1180} height={1920} fill={C.coral} />
      <path d="M640 900 L540 960 L640 1020 Z M540 900 L440 960 L540 1020 Z" fill={C.ink} />
    </g>
  );
};

export const S06A: React.FC = () => {
  const f = useCurrentFrame();
  const unpaid = word("S06A", "unpaid");
  const title = pop(f, 9, 8), cal = prog(f, 16, 26, E.out);
  // the paid-off bar rewinds to a remainder while the wipe clears
  const level = 0.3 * prog(f, 4, 14, E.inOut);
  const pulse = 1 + 0.05 * Math.sin(Math.PI * prog(f, unpaid, unpaid + 12, E.linear));
  const ring = prog(f, unpaid - 2, unpaid + 2) * (1 - 0.5 * prog(f, unpaid + 14, unpaid + 22));
  const ov: Record<string, Override> = {
    title: { pre: scaleAbout(540, 300, Math.max(0.001, title)), opacity: Math.min(1, title * 2) },
    calendar: { pre: scaleAbout(250, 464, 1, Math.max(0.001, cal)), opacity: cal > 0 ? 1 : 0 },
    balance_card: {
      node: <>
        <BalanceCard level={level} remainder tf={CARD_TF} />
        <g transform={`${CARD_TF} ${scaleAbout(0, 38, pulse)}`} opacity={ring}>
          <rect x={-156} y={4} width={312} height={68} rx={16} fill="none" stroke={C.coral} strokeWidth={7} />
        </g>
      </>,
    },
    remy: { pose: poseTrack(f, [{ f: unpaid - 4, pose: { ...concerned, expr: { preset: "neutral", gaze: [3, 2] } } }, { f: unpaid + 2, pose: concerned }]), tf: charTf(REMY.x, REMY.y, REMY.s, true) },
  };
  return (
    <>
      <SceneWorld id="SCN_C07A_BALANCE_LEFT" ov={ov} />
      <svg viewBox="0 0 1080 1920" width={1080} height={1920} style={{ position: "absolute" }}><RewindWipe f={f} /></svg>
    </>
  );
};

// receipt flight: from its C07A spot to resting on the statement header, constant gravity
const FROM = { x: 800, y: 410, r: 0 }, TO = { x: 470, y: 300, r: -6 };
const APEX = 140;

export const S06B: React.FC = () => {
  const f = useCurrentFrame();
  const acc = word("S06B", "accumulated"), bill = word("S06B", "bill");
  const land = acc + 19;
  const u = prog(f, acc, land, E.linear);
  const H = Math.max(FROM.y, TO.y) - APEX; // parabola peak height above the higher end point
  const rx = FROM.x + (TO.x - FROM.x) * u;
  const ry = FROM.y + (TO.y - FROM.y) * u - 4 * (H - (FROM.y - TO.y) / 2) * u * (1 - u) * 1;
  const rr = FROM.r + (TO.r - FROM.r) * prog(f, land - 6, land, E.out);
  const charged = f >= land;
  const flash = charged ? 1 - prog(f, land, land + 10) : 0;
  // C07A pieces clear as the statement rises in
  const out = 1 - fade(f, 0, 6), stmt = track(f, [[3, 700], [15, 0, E.out]]);
  const st = f < bill ? 0 : track(f, [[bill, 1.6], [bill + 5, 0.98, E.in], [bill + 7, 1, E.out]]);
  const remy = poseTrack(f, [
    { f: land, pose: concerned },
    { f: land + 2, pose: pose("remy", "stand_neutral", { lean: 2, expr: { preset: "concerned", gaze: [3, 0] } }) },
    { f: land + 7, pose: pose("remy", "shocked"), ease: E.out, switchAt: 0.2 },
  ]);
  const ov: Record<string, Override> = {
    statement: {
      node: <g transform={`translate(0 ${stmt})`}>
        <Raw m={assetMarkup(charged ? "PRP_STATEMENT_CHARGED" : "PRP_STATEMENT_EMPTY")} tf="translate(470 900) scale(1.45)" />
        {flash > 0 && <g transform="translate(470 900) scale(1.45)" opacity={flash}><rect x={-150} y={56} width={300} height={70} rx={14} fill="none" stroke={C.coral} strokeWidth={8} /></g>}
      </g>,
      after: <g opacity={out}>
        <Raw m={markupOf("SCN_C07A_BALANCE_LEFT", "title")} tf="translate(540 300)" />
        <g transform={`translate(${-400 * (1 - out)} 0)`}>
          <Raw m={assetMarkup("PRP_CALENDAR_PAGE_PROMO_ENDS")} tf="translate(250 620) rotate(-4) scale(1.2)" />
          <BalanceCard level={0.3} remainder tf={CARD_TF} />
        </g>
      </g>,
    },
    receipt: { tf: `translate(${rx} ${ry}) rotate(${rr}) scale(0.8)` },
    stamp: { pre: scaleAbout(470, 1250, Math.max(0.001, st)), opacity: st > 0 ? 1 : 0 },
    remy: { pose: remy, tf: charTf(REMY.x, REMY.y, REMY.s, true) },
  };
  return <SceneWorld id="SCN_C07B_INTEREST_LANDS" ov={ov} />;
};
