// Rig core: a TypeScript port of PHASE_2_ASSETS/build/rig_remy.py (evaluate, ik, eye) plus
// pose blending and a contact-constrained leg solver. Pure functions, no imports, so the
// parity test (scripts/test_rig.ts) can run under plain Node against Python reference output.

export type Mat = [number, number, number, number, number, number];
export type Pt = [number, number];

export const mul = (m: Mat, n: Mat): Mat => [
  m[0] * n[0] + m[2] * n[1], m[1] * n[0] + m[3] * n[1],
  m[0] * n[2] + m[2] * n[3], m[1] * n[2] + m[3] * n[3],
  m[0] * n[4] + m[2] * n[5] + m[4], m[1] * n[4] + m[3] * n[5] + m[5],
];
export const T = (x: number, y: number): Mat => [1, 0, 0, 1, x, y];
export const S = (sx: number, sy = sx): Mat => [sx, 0, 0, sy, 0, 0];
export const R = (deg: number, cx = 0, cy = 0): Mat => {
  const r = (deg * Math.PI) / 180;
  const co = Math.cos(r), si = Math.sin(r);
  return mul(T(cx, cy), mul([co, si, -si, co, 0, 0], T(-cx, -cy)));
};
export const apply = (m: Mat, p: Pt): Pt => [m[0] * p[0] + m[2] * p[1] + m[4], m[1] * p[0] + m[3] * p[1] + m[5]];
export const svgMatrix = (m: Mat) => `matrix(${m.map((v) => +v.toFixed(5)).join(" ")})`;
export const wrap = (a: number) => ((((a + 180) % 360) + 360) % 360) - 180;

export type IKSpec = { ik: Pt; hand_dir?: number; elbow?: "down" | "up" };
export type Triple = [number, number, number];
export type PropSpec = { id: string; hand: "n" | "f" | null; at: [number, number, number, number]; slot: string; m: string; asset: string | null };
export type Expr = { preset?: string; eyes?: string; brows?: string; mouth?: string; blush?: boolean; gaze?: Pt };
export type Pose = {
  body_dy: number; lean: number; neck: number; head_flip: boolean;
  arm_n: Triple | IKSpec; arm_f: Triple | IKSpec; leg_n: Triple; leg_f: Triple;
  hand_n: string; hand_f: string; flip_n: boolean; flip_f: boolean;
  expr: Expr; slots: Record<string, string>; props: PropSpec[];
};
export type Joints = Record<string, Pt>;

// 2-bone IK in the upper-body rest frame (port of rig_remy.ik).
export function ik(J: Joints, side: "n" | "f", spec: IKSpec): Triple {
  const [sx, sy] = J[`sho_${side}`], [ex, ey] = J[`elb_${side}`], [wx, wy] = J[`wri_${side}`];
  const l1 = Math.hypot(ex - sx, ey - sy), l2 = Math.hypot(wx - ex, wy - ey);
  const uRest = (Math.atan2(ey - sy, ex - sx) * 180) / Math.PI;
  const fRest = (Math.atan2(wy - ey, wx - ex) * 180) / Math.PI;
  const [tx, ty] = spec.ik;
  const dist = Math.min(Math.max(Math.hypot(tx - sx, ty - sy), Math.abs(l1 - l2) + 1), l1 + l2 - 0.5);
  const td = Math.atan2(ty - sy, tx - sx);
  const a = Math.acos((l1 * l1 + dist * dist - l2 * l2) / (2 * l1 * dist));
  const sols = [1, -1].map((b) => {
    const t1 = td + b * a;
    return { ely: sy + l1 * Math.sin(t1), t1, elx: sx + l1 * Math.cos(t1) };
  });
  // Python sorts tuples (ely, t1, elx); "down" = reverse (largest ely first)
  sols.sort((p, q) => p.ely - q.ely || p.t1 - q.t1 || p.elx - q.elx);
  if ((spec.elbow ?? "down") === "down") sols.reverse();
  const { t1, ely, elx } = sols[0];
  const t2 = (Math.atan2(ty - ely, tx - elx) * 180) / Math.PI;
  const sho = (t1 * 180) / Math.PI - uRest;
  const elb = t2 - fRest - sho;
  const wri = (spec.hand_dir ?? t2) - 90 - sho - elb;
  return [wrap(sho), wrap(elb), wrap(wri)];
}

export type RigData = {
  parts: Record<string, string>; // part id -> markup key
  hands: Record<string, string>;
  head: { plain: string; blush: string };
};
export type Part = { id: string; slot: string; m: Mat; key: string; kind: "markup" | "head" };

const isIK = (a: Triple | IKSpec): a is IKSpec => !Array.isArray(a);

// Forward kinematics (port of rig_remy.evaluate). Returns parts sorted back-to-front.
export function evaluate(J: Joints, slots: string[], handFront: Record<string, string>, rig: RigData, p: Pose): Part[] {
  const base = T(0, p.body_dy);
  const upper = mul(base, R(p.lean, ...J.hip_c));
  const parts: Part[] = [];
  const add = (id: string, slot: string, m: Mat, key: string, kind: Part["kind"] = "markup") =>
    parts.push({ id, slot: p.slots[id] ?? slot, m, key, kind });
  for (const [side, slot] of [["f", "legF"], ["n", "legN"]] as const) {
    const [hip, knee, ank] = side === "f" ? p.leg_f : p.leg_n;
    const mTh = mul(base, R(hip, ...J[`hip_${side}`]));
    const mSh = mul(mTh, R(knee, ...J[`knee_${side}`]));
    const mFt = mul(mSh, R(ank, ...J[`ankle_${side}`]));
    add(`shin_${side}`, slot, mSh, rig.parts[`shin_${side}`]);
    add(`thigh_${side}`, slot, mTh, rig.parts[`thigh_${side}`]);
    add(`shoe_${side}`, slot, mFt, rig.parts[`shoe_${side}`]);
  }
  add("neck", "neck", upper, rig.parts.neck);
  add("torso", "torso", upper, rig.parts.torso);
  let mHead = mul(upper, R(p.neck, ...J.neck));
  if (p.head_flip) mHead = mul(mHead, mul(T(314, 0), mul(S(-1, 1), T(-314, 0))));
  add("head", "head", mHead, "", "head");
  const handMats: Record<string, Mat> = {};
  for (const [side, slot] of [["f", "armF"], ["n", "armN"]] as const) {
    const arm = side === "f" ? p.arm_f : p.arm_n;
    const [sho, elb, wri] = isIK(arm) ? ik(J, side, arm) : arm;
    const mUp = mul(upper, R(sho, ...J[`sho_${side}`]));
    const mFo = mul(mUp, R(elb, ...J[`elb_${side}`]));
    const w = J[`wri_${side}`];
    let mHa = mul(mFo, mul(R(wri, ...w), mul(T(...w), R(90))));
    if (side === "f" ? p.flip_f : p.flip_n) mHa = mul(mHa, S(1, -1));
    handMats[side] = mHa;
    const shape = side === "f" ? p.hand_f : p.hand_n;
    add(`upper_arm_${side}`, slot, mUp, rig.parts[`upper_arm_${side}`]);
    add(`forearm_${side}`, slot, mFo, rig.parts[`forearm_${side}`]);
    add(`hand_${side}`, slot, mHa, rig.hands[shape]);
    if (handFront[shape]) add(`hand_${side}_front`, "top", mHa, rig.hands[handFront[shape]]);
    add(`cuff_${side}`, slot, mFo, rig.parts[`cuff_${side}`]);
  }
  p.props.forEach((pr, i) => {
    const [x, y, rot, sc] = pr.at;
    const anchor = pr.hand ? handMats[pr.hand] : upper;
    add(pr.id ?? `prop_${i}`, pr.slot ?? "prop", mul(anchor, mul(T(x, y), mul(R(rot), S(sc)))), pr.m);
  });
  const order = Object.fromEntries(slots.map((s, i) => [s, i]));
  return parts.map((q, i) => ({ q, i })).sort((a, b) => order[a.q.slot] - order[b.q.slot] || a.i - b.i).map((x) => x.q);
}

// ---- face (port of rig_remy.eye / features via exported head templates) ---------------------
const num = (v: number) => (Number.isInteger(v) ? String(v) : String(+v.toFixed(6)));
const pathEl = (d: string, ink: string, sw: number, fill = "none") =>
  `<path d="${d}" fill="${fill}" stroke="${ink}" stroke-width="${sw}" stroke-linejoin="round" stroke-linecap="round"/>`;

export function eye(c: Pt, kind: string, gx: number, gy: number, col: { ink: string; white: string; skin: string }): string {
  const x = c[0] + gx, y = c[1] + gy;
  if (kind === "open" || kind === "wide" || kind === "squint") {
    const [rx, ry] = ({ open: [7.5, 12.5], wide: [9, 15.5], squint: [8, 6] } as Record<string, Pt>)[kind];
    let out = `<ellipse cx="${num(x)}" cy="${num(y)}" rx="${num(rx)}" ry="${num(ry)}" fill="${col.ink}"/>`;
    if (kind !== "squint") out += `<circle cx="${num(x + 2.6)}" cy="${num(y - ry * 0.36)}" r="2.7" fill="${col.white}"/>`;
    return out;
  }
  const [cx, cy] = c;
  if (kind === "half") {
    let out = `<ellipse cx="${num(x)}" cy="${num(y + 3)}" rx="7.5" ry="9.5" fill="${col.ink}"/>`;
    out += `<path d="M${cx - 13} ${cy - 18}H${cx + 13}V${cy + 1}Q${cx} ${cy + 4} ${cx - 13} ${cy + 1}Z" fill="${col.skin}"/>`;
    return out + pathEl(`M${cx - 11} ${cy + 1}Q${cx} ${cy + 4} ${cx + 11} ${cy + 1}`, col.ink, 5);
  }
  if (kind === "happy") return pathEl(`M${cx - 10} ${cy + 5}Q${cx} ${cy - 10} ${cx + 10} ${cy + 5}`, col.ink, 6);
  if (kind === "closed") return pathEl(`M${cx - 10} ${cy - 1}Q${cx} ${cy + 9} ${cx + 10} ${cy - 1}`, col.ink, 6);
  throw new Error(`eye kind ${kind}`);
}

export type FaceData = {
  brows: Record<string, [string, string]>;
  mouths: Record<string, string>;
  eye_colors: { ink: string; white: string; skin: string };
  expressions: Record<string, { eyes: string; brows: string; mouth: string; blush: boolean }>;
};

export function headMarkup(rig: RigData, face: FaceData, markup: Record<string, string>, expr: Expr, fallbackPreset = "neutral"): string {
  const pre = face.expressions[expr.preset ?? fallbackPreset];
  const eyes = expr.eyes ?? pre.eyes, brows = expr.brows ?? pre.brows, mouth = expr.mouth ?? pre.mouth;
  const blush = expr.blush ?? pre.blush;
  const [gx, gy] = expr.gaze ?? [0, 0];
  const tpl = markup[blush ? rig.head.blush : rig.head.plain];
  return tpl
    .replace(/\{\{EYE:(-?[\d.]+):(-?[\d.]+)\}\}/g, (_, x, y) => eye([+x, +y], eyes, gx, gy, face.eye_colors))
    .replace("{{BROW_L}}", face.brows[brows][0])
    .replace("{{BROW_R}}", face.brows[brows][1])
    .replace("{{MOUTH}}", markup[face.mouths[mouth]]);
}

// ---- pose resolution and blending --------------------------------------------------------------
export type NumPose = Omit<Pose, "arm_n" | "arm_f"> & { arm_n: Triple; arm_f: Triple };

export const resolve = (J: Joints, p: Pose): NumPose => ({
  ...p,
  arm_n: isIK(p.arm_n) ? ik(J, "n", p.arm_n) : p.arm_n,
  arm_f: isIK(p.arm_f) ? ik(J, "f", p.arm_f) : p.arm_f,
});

const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
const lerpAng = (a: number, b: number, t: number) => a + wrap(b - a) * t;
const lerp3 = (a: Triple, b: Triple, t: number): Triple => [lerpAng(a[0], b[0], t), lerpAng(a[1], b[1], t), lerpAng(a[2], b[2], t)];

/** Blend two resolved poses. Continuous channels interpolate (shortest-path angles); discrete
 *  channels (hand shapes, flips, expression, slots, props) switch when t >= switchAt. */
export function blend(a: NumPose, b: NumPose, t: number, switchAt = 1): NumPose {
  const d = t >= switchAt ? b : a;
  const ga = a.expr.gaze ?? [0, 0], gb = b.expr.gaze ?? [0, 0];
  return {
    ...d,
    body_dy: lerp(a.body_dy, b.body_dy, t), lean: lerp(a.lean, b.lean, t), neck: lerp(a.neck, b.neck, t),
    arm_n: lerp3(a.arm_n, b.arm_n, t), arm_f: lerp3(a.arm_f, b.arm_f, t),
    leg_n: lerp3(a.leg_n, b.leg_n, t), leg_f: lerp3(a.leg_f, b.leg_f, t),
    expr: { ...d.expr, gaze: [lerp(ga[0], gb[0], t), lerp(ga[1], gb[1], t)] },
  };
}

// ---- legs: contact-constrained 2-bone solver -----------------------------------------------
/** Leg angles that put the ankle at `target` (base frame, i.e. before body_dy) with the knee
 *  bending forward (+x) and the shoe at world pitch `pitch` (0 = flat on the ground). */
export function legIK(J: Joints, side: "n" | "f", target: Pt, pitch = 0): Triple {
  const [hx, hy] = J[`hip_${side}`], [kx, ky] = J[`knee_${side}`], [ax, ay] = J[`ankle_${side}`];
  const l1 = Math.hypot(kx - hx, ky - hy), l2 = Math.hypot(ax - kx, ay - ky);
  const tRest = Math.atan2(ky - hy, kx - hx), sRest = Math.atan2(ay - ky, ax - kx);
  const [tx, ty] = target;
  const dist = Math.min(Math.max(Math.hypot(tx - hx, ty - hy), Math.abs(l1 - l2) + 1), l1 + l2 - 0.01);
  const td = Math.atan2(ty - hy, tx - hx);
  const a = Math.acos((l1 * l1 + dist * dist - l2 * l2) / (2 * l1 * dist));
  // knee forward = the solution whose knee has the larger x
  const cands = [td + a, td - a].map((t1) => ({ t1, kx: hx + l1 * Math.cos(t1), ky: hy + l1 * Math.sin(t1) }));
  const { t1, kx: kx2, ky: ky2 } = cands[0].kx >= cands[1].kx ? cands[0] : cands[1];
  const deg = 180 / Math.PI;
  const hip = (t1 - tRest) * deg;
  const knee = (Math.atan2(ty - ky2, tx - kx2) - sRest) * deg - hip;
  return [wrap(hip), wrap(knee), wrap(pitch - hip - knee)];
}

export const legLengths = (J: Joints, side: "n" | "f") => [
  Math.hypot(J[`knee_${side}`][0] - J[`hip_${side}`][0], J[`knee_${side}`][1] - J[`hip_${side}`][1]),
  Math.hypot(J[`ankle_${side}`][0] - J[`knee_${side}`][0], J[`ankle_${side}`][1] - J[`knee_${side}`][1]),
];
