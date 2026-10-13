import React from "react";
import { AbsoluteFill } from "remotion";
import { evaluate, headMarkup, resolve, svgMatrix, type NumPose } from "../rig/rig";
import { captionLayout, CAPTION_METRICS } from "../lib/captions";
import { B, C, assetMarkup, instMarkup, type Inst } from "../lib/bundle";

/** Raw library markup inside a group. Markup is generator output from build/ (trusted, offline). */
export const Raw: React.FC<{ m: string; tf?: string | null; opacity?: number; style?: React.CSSProperties }> = ({ m, tf, opacity, style }) => (
  <g transform={tf ?? undefined} opacity={opacity} style={style} dangerouslySetInnerHTML={{ __html: m }} />
);

export const Asset: React.FC<{ id: string; tf?: string | null; opacity?: number }> = ({ id, tf, opacity }) =>
  opacity === 0 ? null : <Raw m={assetMarkup(id)} tf={tf} opacity={opacity} />;

/** A rigged character evaluated for this frame. `only` limits drawing to some part ids (macro crops). */
// Joint envelope = rig suggested limits ∪ the angles the approved library poses already use
// (several approved 3/4-view poses fold the near arm with the elbow out, beyond the side-view
// suggestion). Frames that leave this envelope are logged as [JOINT] for the QA report.
const LIMITS: Record<string, [number, number]> = { lean: [-10, 12], neck: [-12, 12], shoulder: [-170, 120], elbow: [-150, 20], wrist: [-60, 60], hip: [-95, 30], knee: [0, 100] };
type Env = Record<string, [number, number]>;
const ENVELOPE: Record<string, Env> = {};
for (const rig of ["remy", "assoc"] as const) {
  const env: Env = {};
  const widen = (k: string, v: number) => { const [lo, hi] = env[k] ?? LIMITS[k.split("_")[0]]; env[k] = [Math.min(lo, v), Math.max(hi, v)]; };
  for (const p of Object.values(B.poses[rig])) {
    const r = resolve(B.joints, p);
    widen("lean", r.lean); widen("neck", r.neck);
    for (const [side, a] of [["n", r.arm_n], ["f", r.arm_f]] as const) { widen(`shoulder_${side}`, a[0]); widen(`elbow_${side}`, a[1]); widen(`wrist_${side}`, a[2]); }
    for (const [side, l] of [["n", r.leg_n], ["f", r.leg_f]] as const) { widen(`hip_${side}`, l[0]); widen(`knee_${side}`, l[1]); }
  }
  ENVELOPE[rig] = env;
}
const checkJoints = (rig: "remy" | "assoc", p: NumPose) => {
  const env = ENVELOPE[rig], out: string[] = [];
  const t = (k: string, v: number) => { const [lo, hi] = env[k] ?? LIMITS[k.split("_")[0]]; if (v < lo - 2 || v > hi + 2) out.push(`${k}=${v.toFixed(1)}`); };
  t("lean", p.lean); t("neck", p.neck);
  for (const [side, a] of [["n", p.arm_n], ["f", p.arm_f]] as const) { t(`shoulder_${side}`, a[0]); t(`elbow_${side}`, a[1]); t(`wrist_${side}`, a[2]); }
  for (const [side, l] of [["n", p.leg_n], ["f", p.leg_f]] as const) { t(`hip_${side}`, l[0]); t(`knee_${side}`, l[1]); }
  if (out.length) console.warn(`[JOINT] ${rig} ${out.join(" ")}`);
};

export const Character: React.FC<{ rig: "remy" | "assoc"; pose: NumPose; tf?: string | null; only?: (id: string) => boolean; opacity?: number }> = ({ rig, pose, tf, only, opacity }) => {
  checkJoints(rig, pose);
  const parts = evaluate(B.joints, B.slots, B.hand_front, B.rigs[rig], pose);
  return (
    <g transform={tf ?? undefined} opacity={opacity}>
      {parts.filter((p) => !only || only(p.id)).map((p) => (
        <g key={p.id} transform={svgMatrix(p.m)} dangerouslySetInnerHTML={{
          __html: p.kind === "head" ? headMarkup(B.rigs[rig], B.face, B.markup, pose.expr, rig === "assoc" ? "content" : "neutral") : p.key.startsWith("<") ? p.key : B.markup[p.key],
        }} />
      ))}
    </g>
  );
};

export type Override = {
  hide?: boolean; tf?: string | null; opacity?: number;
  /** extra transform applied around the instance's own transform (e.g. a slide offset) */
  pre?: string;
  pose?: NumPose; only?: (id: string) => boolean;
  node?: React.ReactNode; // replaces the instance entirely
  after?: React.ReactNode; // drawn right above the instance (z-order insert)
};

const renderInst = (i: Inst, o: Override = {}) => {
  if (o.hide) return o.after ?? null;
  const tf = o.tf !== undefined ? o.tf : i.tf;
  let el: React.ReactNode = o.node ?? (i.char
    ? <Character rig={i.char.rig} pose={o.pose ?? (null as never)} tf={tf} only={o.only} opacity={o.opacity} />
    : <Raw m={instMarkup(i)} tf={tf} opacity={o.opacity} />);
  if (o.pre) el = <g transform={o.pre}>{el}</g>;
  return <>{el}{o.after}</>;
};

/** One approved composition (SCN_*), with per-instance overrides for animation. */
export const SceneWorld: React.FC<{ id: string; ov?: Record<string, Override>; camera?: string | null; ui?: boolean; children?: React.ReactNode }> = ({ id, ov = {}, camera, ui = true, children }) => {
  const sc = B.scenes[id];
  if (!sc) throw new Error(`scene ${id}`);
  for (const i of sc.world) if (i.char && !ov[i.id]?.pose && !ov[i.id]?.hide && !ov[i.id]?.node) throw new Error(`${id}:${i.id} needs an animated pose`);
  const cam = camera !== undefined ? camera : sc.camera;
  return (
    <AbsoluteFill>
      <svg viewBox="0 0 1080 1920" width={1080} height={1920} style={{ position: "absolute", fontFamily: B.font }}>
        <g transform={cam ?? undefined}>
          {sc.world.map((i) => <React.Fragment key={i.id}>{renderInst(i, ov[i.id])}</React.Fragment>)}
          {children}
        </g>
        {ui && sc.ui.map((i) => <React.Fragment key={i.id}>{renderInst(i, ov[`ui:${i.id}`])}</React.Fragment>)}
      </svg>
    </AbsoluteFill>
  );
};

/** Caption plate (port of typography.caption_plate; live text, Avenir Next 800). */
export const captionSize = (text: string, max = 56) => captionLayout(text, 0, max).size;
export const CaptionPlate: React.FC<{ text: string; opacity?: number; cy?: number }> = ({ text, opacity = 1, cy = 1430 }) => {
  const {size, width, height, x, y} = captionLayout(text, cy);
  return (
    <g opacity={opacity}>
      <rect x={Math.round(x)} y={Math.round(y)} width={Math.round(width)} height={Math.round(height)} rx={24} fill={C.ink} fillOpacity={0.88} />
      <text x={CAPTION_METRICS.centerX} y={Math.round(y + 17 + size * 0.95)} fontFamily={B.font} fontSize={size} fontWeight={800} textAnchor="middle" fill={C.paper}>{text}</text>
    </g>
  );
};

/** Rectangular clip (masks for wipes and paper growing out of a holder). */
export const Clip: React.FC<{ id: string; x: number; y: number; w: number; h: number; children: React.ReactNode }> = ({ id, x, y, w, h, children }) => (
  <>
    <defs><clipPath id={id}><rect x={x} y={y} width={Math.max(0, w)} height={Math.max(0, h)} /></clipPath></defs>
    <g clipPath={`url(#${id})`}>{children}</g>
  </>
);
