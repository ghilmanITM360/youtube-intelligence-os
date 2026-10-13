// Typed access to the generated asset bundle (src/data/bundle.json, from scripts/export_bundle.py).
import raw from "../data/bundle.json";
import { apply, evaluate, resolve, type FaceData, type Joints, type NumPose, type Pose, type RigData } from "../rig/rig";

export type CharMeta = { rig: "remy" | "assoc"; pose: Pose; feet?: [number, number] | null; scale?: number; flip?: boolean | null };
export type Inst = { id: string; asset: string; tf: string | null; m?: string | null; char?: CharMeta };
export type Scene = { shots: string[]; camera: string | null; world: Inst[]; ui: Inst[] };
export type Shot = { id: string; beat: number; scene: string; phrase: number; from: number; to: number; narration: string; qualifier: string; transition: string };
export type Word = { i: number; text: string; norm: string; phrase: number; from: number; to: number };

type Bundle = {
  palette: Record<string, string>; font: string;
  joints: Joints; slots: string[]; hand_front: Record<string, string>;
  rigs: Record<"remy" | "assoc", RigData>; face: FaceData;
  poses: Record<"remy" | "assoc", Record<string, Pose>>;
  assets: Record<string, { vb: number[]; m: string; category: string }>;
  scenes: Record<string, Scene>;
  markup: Record<string, string>;
  timeline: {
    fps: number; frames_total: number; timing_status: string;
    audio: { file: string; sha256: string; duration_s: number };
    gate: { result: string; final_sync_allowed: boolean };
    shots: Shot[]; phrases: { i: number; text: string; from: number; to: number }[]; words: Word[];
    captions: { shot: string; text: string; from: number; to: number }[];
  };
};

export const B = raw as unknown as Bundle;
export const C = B.palette;
export const TL = B.timeline;

export const assetMarkup = (id: string) => {
  const a = B.assets[id];
  if (!a) throw new Error(`asset ${id} is not in the bundle`);
  return B.markup[a.m];
};
export const instMarkup = (i: Inst) => (i.m ? B.markup[i.m] : assetMarkup(i.asset));

/** Library pose (resolved to joint angles), with optional overrides. */
export const pose = (rig: "remy" | "assoc", name: string, over: Partial<Pose> = {}): NumPose => {
  const p = B.poses[rig][name];
  if (!p) throw new Error(`pose ${rig}:${name} missing`);
  return resolve(B.joints, { ...p, ...over, expr: { ...p.expr, ...(over.expr ?? {}) } });
};

export const shot = (id: string) => {
  const s = TL.shots.find((x) => x.id === id);
  if (!s) throw new Error(`shot ${id}`);
  return s;
};

/** Frame (relative to the shot start) where a narration word starts. Words are looked up by their
 *  normalized text inside the shot's phrase, so keyframes follow the audio when it is re-aligned. */
export const word = (shotId: string, norm: string, nth = 0, edge: "from" | "to" = "from") => {
  const s = shot(shotId);
  const ws = TL.words.filter((w) => w.phrase === s.phrase && w.norm === norm);
  if (!ws[nth]) throw new Error(`word "${norm}" #${nth} not in ${shotId} (${s.narration})`);
  return ws[nth][edge] - s.from;
};
export const shotLen = (id: string) => shot(id).to - shot(id).from;

/** Port of scenes.char_tf: put the rig ground point (314, 1030) at scene (fx, fy) with scale s. */
export const charTf = (fx: number, fy: number, s: number, flip = false) =>
  flip ? `translate(${fx + 314 * s} ${fy - 1030 * s}) scale(${-s} ${s})` : `translate(${fx - 314 * s} ${fy - 1030 * s}) scale(${s})`;

/** Port of scenes.char_point: scene position of a local point on a character part. */
export const charPoint = (p: NumPose, part: string, local: [number, number], fx: number, fy: number, s: number, flip = false, rig: "remy" | "assoc" = "remy"): [number, number] => {
  const m = evaluate(B.joints, B.slots, B.hand_front, B.rigs[rig], p).find((q) => q.id === part)!.m;
  const [x, y] = apply(m, local);
  return [fx + (flip ? -1 : 1) * (x - 314) * s, fy + (y - 1030) * s];
};
