// Contact-constrained walk: a footstep plan with planted feet solved by leg IK, replacing the
// two-key walk_a/walk_b flip-book (which slides feet). Pure function of the frame.
//
// Coordinates are rig units along the character's facing direction (+x in the rig frame; the
// scene mirror handles left-facing walkers). The body travels with a trapezoid speed profile;
// each step lands a foot ahead of the body, the stance foot stays fixed in the world while the
// body passes over it, and pelvis height comes from the leg reach (lower in double support,
// higher at mid-stance) so the bob is physical rather than a fixed sine.
import { legIK, legLengths, type Joints, type NumPose, type Triple } from "./rig.ts";

export type WalkSpec = {
  f0: number; f1: number; // body moves between these frames; a closing step follows f1
  dist: number;           // rig units to travel (> 0)
  stepLen?: number;       // target body advance per step (rig units)
  lead?: "n" | "f";       // which foot steps first
  lift?: number;          // swing foot clearance
  upper: NumPose;         // upper-body template (arms/hands/expr/lean); legs are replaced
  armSwing?: number;      // degrees at cruise speed
};

type Plant = { side: "n" | "f"; t0: number; t1: number; from: number; to: number };
export type WalkPlan = { spec: Required<WalkSpec>; steps: Plant[]; fEnd: number; tb: number[] };

const RAMP = 0.22; // fraction of the move spent accelerating / decelerating
function travel(u: number): number {
  // trapezoid velocity profile, normalized so travel(1) = 1
  const a = RAMP, vmax = 1 / (1 - a);
  if (u <= 0) return 0;
  if (u >= 1) return 1;
  if (u < a) return (vmax * u * u) / (2 * a);
  if (u > 1 - a) return 1 - (vmax * (1 - u) ** 2) / (2 * a);
  return vmax * (u - a / 2);
}
const speedEnv = (u: number) => (u <= 0 || u >= 1 ? 0 : u < RAMP ? u / RAMP : u > 1 - RAMP ? (1 - u) / RAMP : 1);

export function planWalk(s: WalkSpec): WalkPlan {
  const spec: Required<WalkSpec> = { stepLen: 150, lead: "n", lift: 34, armSwing: 15, ...s };
  // Half-length first and last body advances: the first step starts from feet together and the
  // last step lands alongside the stance foot, so no stance offset exceeds half a step.
  const n = Math.max(2, Math.round(spec.dist / spec.stepLen) + 1);
  const step = spec.dist / (n - 1), d = step / 2;
  const b = Array.from({ length: n + 1 }, (_, k) => (k === 0 ? 0 : k === n ? spec.dist : d + (k - 1) * step));
  const dur = spec.f1 - spec.f0;
  // frame at which the body reaches each boundary (invert the monotone travel curve)
  const tb = b.map((bk) => {
    let lo = 0, hi = 1;
    for (let i = 0; i < 40; i++) { const m = (lo + hi) / 2; if (travel(m) < bk / spec.dist) lo = m; else hi = m; }
    return spec.f0 + dur * ((lo + hi) / 2);
  });
  const other = (x: "n" | "f") => (x === "n" ? "f" : "n");
  const last: Record<"n" | "f", number> = { n: 0, f: 0 };
  const steps: Plant[] = [];
  for (let k = 1; k <= n; k++) {
    const side = k % 2 ? spec.lead : other(spec.lead);
    const to = k < n ? b[k] + d : spec.dist;
    const t0 = tb[k - 1] + 0.18 * (tb[k] - tb[k - 1]); // double support before lift-off
    steps.push({ side, t0, t1: tb[k], from: last[side], to });
    last[side] = to;
  }
  return { spec, steps, fEnd: spec.f1, tb };
}

const smooth = (t: number) => t * t * (3 - 2 * t);

/** Foot displacement (forward, lift) at frame f. */
export function footAt(plan: WalkPlan, side: "n" | "f", f: number): { x: number; lift: number; planted: boolean } {
  let x = 0;
  for (const st of plan.steps) {
    if (st.side !== side) continue;
    if (f < st.t0) return { x, lift: 0, planted: true };
    if (f < st.t1) {
      const u = (f - st.t0) / (st.t1 - st.t0);
      return { x: st.from + (st.to - st.from) * smooth(u), lift: plan.spec.lift * Math.sin(Math.PI * u), planted: false };
    }
    x = st.to;
  }
  return { x, lift: 0, planted: true };
}

export const bodyAt = (plan: WalkPlan, f: number) =>
  plan.spec.dist * travel((f - plan.spec.f0) / (plan.spec.f1 - plan.spec.f0));

/** Full pose plus body travel (rig units) at frame f. */
export function walkAt(J: Joints, plan: WalkPlan, f: number): { pose: NumPose; dx: number } {
  const { spec } = plan;
  const dx = bodyAt(plan, f);
  const u = (f - spec.f0) / (spec.f1 - spec.f0);
  const env = speedEnv(u);
  const feet = { n: footAt(plan, "n", f), f: footAt(plan, "f", f) };
  // pelvis height: lowest body_dy that keeps every foot reachable at 98.5 % leg length
  let dy = 3;
  for (const side of ["n", "f"] as const) {
    const [l1, l2] = legLengths(J, side);
    const reach = 0.985 * (l1 + l2);
    const ax = J[`ankle_${side}`][0] + feet[side].x - dx - J[`hip_${side}`][0];
    const need = J[`ankle_${side}`][1] - feet[side].lift - J[`hip_${side}`][1] - Math.sqrt(Math.max(0, reach * reach - ax * ax));
    dy = Math.max(dy, need);
  }
  const leg = (side: "n" | "f"): Triple => legIK(J, side,
    [J[`ankle_${side}`][0] + feet[side].x - dx, J[`ankle_${side}`][1] - feet[side].lift - dy], 0);
  // gait phase: step index + progress, used for counter-swinging arms
  const k = plan.tb.findIndex((t) => t > f);
  const phi = k <= 0 ? (f < spec.f0 ? 0 : plan.tb.length - 1) : k - 1 + (f - plan.tb[k - 1]) / (plan.tb[k] - plan.tb[k - 1]);
  const sw = spec.armSwing * env * -Math.cos(Math.PI * phi) * (spec.lead === "n" ? 1 : -1);
  const up = spec.upper;
  return {
    dx,
    pose: {
      ...up,
      body_dy: dy, lean: up.lean + 3 * env,
      leg_n: leg("n"), leg_f: leg("f"),
      arm_n: [up.arm_n[0] + sw, up.arm_n[1] - 6 * env, up.arm_n[2]],
      arm_f: [up.arm_f[0] - sw, up.arm_f[1] - 6 * env, up.arm_f[2]],
      slots: {},
    },
  };
}
