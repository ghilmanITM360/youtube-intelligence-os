// Beat 4 (C05 ledger, one held set-up over three phrases).
// S04A "With deferred interest,"  S04B "interest builds from purchase day,"  S04C "it just hasn't been charged yet."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Clip, Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, pop, poseTrack, prog, track } from "../lib/anim";
import { assetMarkup, charTf, pose, shot, word } from "../lib/bundle";
import { scaleAbout, setGroups } from "../lib/markup";

const L = (k: string) => `diagram_ledger__ledger_${k}`;
const RECEIPT = { x: 790, y: 500, s: 1.15 };
const receiptH = (rows: number) => (64 + rows * 34 + 24 + 16) * RECEIPT.s; // body + torn foot
const REMY = { x: 190, y: 1930, s: 0.62 };

const stand = pose("remy", "stand_neutral", { expr: { preset: "neutral", gaze: [4, -3] } });
const think = pose("remy", "think_chin");
const pointUp = pose("remy", "point_up", { expr: { preset: "determined", gaze: [5, -5] } });

/** Ledger state as a function of time since the start of S04A (all three shots share it). */
function Ledger({ t }: { t: number }) {
  const A = shot("S04A").from, b = (id: string, w: string) => word(id, w) + shot(id).from - A;
  const withW = b("S04A", "with"), deferred = b("S04A", "deferred");
  const builds = b("S04B", "builds"), purchase = b("S04B", "purchase"), b0 = shot("S04B").from - A;
  const charged = b("S04C", "charged"), c0 = shot("S04C").from - A;
  // title pop, balance card slides in from the left (no bounce)
  const title = pop(t, withW + 1, 8);
  const cardX = track(t, [[deferred, -520], [deferred + 14, 0, E.out]]);
  // month strip: months appear one after another (2 f stagger), each rising 12 px
  const months: Record<string, Record<string, string>> = {};
  for (let i = 1; i <= 12; i++) {
    const u = fade(t, b0 + 4 + 2 * i, 6);
    months[`month_${String(i).padStart(2, "0")}`] = { opacity: u.toFixed(3), transform: `translate(0 ${(12 * (1 - u)).toFixed(2)})` };
  }
  const timeline = setGroups(assetMarkup("DIAGRAM_LEDGER_L_LEDGER_TIMELINE"), months);
  // receipt prints out of the NOT CHARGED YET clip and grows 1 → 3 → 6 rows
  const clip = pop(t, b0 + 3, 7);
  const rows = t < builds + 6 ? 1 : t < purchase + 6 ? 3 : 6;
  const grow = (from: number, to: number, f0: number) => receiptH(from) + (receiptH(to) - receiptH(from)) * prog(t, f0, f0 + 8);
  const h = t < builds + 6 ? receiptH(1) * prog(t, b0 + 6, b0 + 14, E.out) : t < purchase + 6 ? grow(1, 3, builds + 6) : grow(3, 6, purchase + 6);
  const day = pop(t, purchase, 8), link = prog(t, purchase + 2, purchase + 12);
  const nc = pop(t, charged, 8);
  const ov: Record<string, Override> = {
    [L("title")]: { pre: scaleAbout(540, 300, Math.max(0.001, title)), opacity: Math.min(1, title * 2) },
    [L("balance")]: { pre: `translate(${cardX} 0)` },
    [L("timeline")]: { node: <Raw m={timeline} /> },
    [L("receipt_clip")]: { pre: scaleAbout(RECEIPT.x, 470, Math.max(0.001, clip)), opacity: Math.min(1, clip * 2) },
    [L("receipt_rows_01")]: { hide: true },
    [L("receipt_rows_03")]: { hide: true },
    [L("receipt_rows_06")]: {
      // drawn under the clip: render the current row state inside a growing clip rectangle
      node: <Clip id="s04-receipt" x={RECEIPT.x - 190} y={RECEIPT.y} w={380} h={h}><Raw m={assetMarkup(`DIAGRAM_LEDGER_L_LEDGER_RECEIPT_ROWS_0${rows}`)} /></Clip>,
    },
    [L("purchase_day")]: { pre: scaleAbout(214, 962, Math.max(0.001, day)), opacity: Math.min(1, day * 2) },
    [L("link")]: { node: <Clip id="s04-link" x={150} y={740} w={200} h={290 * link}><Raw m={assetMarkup("DIAGRAM_LEDGER_L_LEDGER_LINK")} /></Clip> },
    [L("not_charged")]: { pre: scaleAbout(540, 1210, Math.max(0.001, nc)), opacity: Math.min(1, nc * 2) },
  };
  // Remy: hand to chin while the idea forms; points up at the receipt on "charged"
  const p = poseTrack(t, [
    { f: deferred + 2, pose: stand }, { f: deferred + 12, pose: think, switchAt: 0.6 },
    { f: c0 + 4, pose: think }, { f: c0 + 14, pose: pointUp, switchAt: 0.6 },
    { f: charged + 2, pose: pointUp }, { f: charged + 8, pose: { ...pointUp, expr: { preset: "curious", gaze: [5, -5] } } },
  ]);
  const blink = (t >= b0 + 30 && t < b0 + 33);
  ov.remy = { pose: blink ? { ...p, expr: { ...p.expr, eyes: "closed" } } : p, tf: charTf(REMY.x, REMY.y, REMY.s) };
  return <SceneWorld id="SCN_C05_LEDGER" ov={ov} />;
}

const at = (id: string) => () => <Ledger t={useCurrentFrame() + shot(id).from - shot("S04A").from} />;
export const S04A = at("S04A");
export const S04B = at("S04B");
export const S04C = at("S04C");
