// Deterministic keyframe helpers. Every value is a pure function of the frame number, so
// seeking backward or at random gives the same picture (no state, no springs, no randomness).
import { blend, type NumPose } from "../rig/rig.ts";

export type Ease = (t: number) => number;
export const clamp01 = (t: number) => Math.min(1, Math.max(0, t));
export const E = {
  linear: (t: number) => t,
  in: (t: number) => t * t * t,
  out: (t: number) => 1 - (1 - t) ** 3,
  inOut: (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - (-2 * t + 2) ** 3 / 2),
  /** Cubic out with a small overshoot; `s` = peak overshoot as a fraction (0.03 = 3 %). Use only
   *  for light graphics (labels, stamps, signs) — never for charts, money values or people. */
  outBack: (s = 0.03): Ease => {
    // peak overshoot of 1 + (k+1)u³ + ku² (u = t-1) is 4k³ / (27(k+1)²); solve for k by bisection
    let lo = 0, hi = 5;
    for (let i = 0; i < 40; i++) {
      const k = (lo + hi) / 2;
      if ((4 * k ** 3) / (27 * (k + 1) ** 2) < s) lo = k; else hi = k;
    }
    const k = lo;
    return (t) => 1 + (k + 1) * (t - 1) ** 3 + k * (t - 1) ** 2;
  },
  /** Gravity: accelerates into contact (falling objects). */
  fall: (t: number) => t * t,
};

/** Normalized progress of f inside [f0, f1], eased. */
export const prog = (f: number, f0: number, f1: number, ease: Ease = E.inOut) =>
  f1 <= f0 ? (f >= f1 ? 1 : 0) : ease(clamp01((f - f0) / (f1 - f0)));

export type Key = [frame: number, value: number, ease?: Ease];
/** Piecewise track: holds the first value before the first key and the last value after the last.
 *  Each key's ease shapes the segment arriving at it (default inOut). */
export function track(f: number, keys: Key[]): number {
  if (f <= keys[0][0]) return keys[0][1];
  for (let i = 1; i < keys.length; i++) {
    const [f1, v1, ease] = keys[i];
    if (f <= f1) {
      const [f0, v0] = keys[i - 1];
      return v0 + (v1 - v0) * prog(f, f0, f1, ease ?? E.inOut);
    }
  }
  return keys[keys.length - 1][1];
}

export type PoseKey = { f: number; pose: NumPose; ease?: Ease; switchAt?: number };
/** Pose track: blends consecutive keyed poses (linear normalized joint angles). Discrete channels (hand
 *  shape, expression, props) switch at `switchAt` of each segment (default: at the key, i.e. the
 *  extreme of the move, per the handoff). */
export function poseTrack(f: number, keys: PoseKey[]): NumPose {
  if (f <= keys[0].f) return keys[0].pose;
  for (let i = 1; i < keys.length; i++) {
    const k = keys[i];
    if (f < k.f) {
      const a = keys[i - 1];
      return blend(a.pose, k.pose, prog(f, a.f, k.f, k.ease ?? E.inOut), k.switchAt ?? 1);
    }
  }
  return keys[keys.length - 1].pose;
}

/** Visibility step (1 from f0 on). */
export const on = (f: number, f0: number) => (f >= f0 ? 1 : 0);
/** Pop-in scale for light graphics: 0 → 1 with ≤ 3 % overshoot over `dur` frames. */
export const pop = (f: number, f0: number, dur = 8, s = 0.03) => (f < f0 ? 0 : prog(f, f0, f0 + dur, E.outBack(s)));
/** Fade 0→1. */
export const fade = (f: number, f0: number, dur = 8) => prog(f, f0, f0 + dur, E.inOut);
