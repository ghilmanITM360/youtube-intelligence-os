// Rig parity + invariants. Run: node scripts/test_rig.ts (Node >= 22.18 strips types natively).
// Python (PHASE_2_ASSETS/build/rig_remy.py) is the reference implementation.
import { readFileSync } from "node:fs";
import { evaluate, eye, ik, headMarkup, legIK, resolve, apply, type Pose, type Pt } from "../src/rig/rig.ts";
import { planWalk, walkAt, footAt } from "../src/rig/walk.ts";

const B = JSON.parse(readFileSync(new URL("../src/data/bundle.json", import.meta.url), "utf8"));
const REF = JSON.parse(readFileSync(new URL("../src/data/rig_reference.json", import.meta.url), "utf8"));
let fails = 0;
const check = (ok: boolean, msg: string) => { if (!ok) { fails++; console.error("FAIL", msg); } };
const close = (a: number[], b: number[], tol = 1e-6) => a.length === b.length && a.every((v, i) => Math.abs(v - b[i]) <= tol);

// 1. FK parity for every library pose of both characters
for (const [k, ref] of Object.entries(REF.poses) as [string, [string, string, number[]][]][]) {
  const [rig, name] = k.split(":");
  const parts = evaluate(B.joints, B.slots, B.hand_front, B.rigs[rig], B.poses[rig][name] as Pose);
  check(parts.length === ref.length, `${k}: part count ${parts.length} vs ${ref.length}`);
  ref.forEach(([pid, slot, m], i) => {
    const p = parts[i];
    check(p?.id === pid && p.slot === slot && close(p.m, m), `${k}: part ${i} ${p?.id}/${p?.slot} vs ${pid}/${slot}`);
  });
}
// 2. eye and IK parity
for (const e of REF.eyes) check(eye(e.c, e.kind, e.g[0], e.g[1], B.face.eye_colors) === e.out, `eye ${e.kind} ${e.g}`);
for (const s of REF.ik) check(close(ik(B.joints, s.side, s.spec), s.out, 1e-6), `ik ${s.side} ${JSON.stringify(s.spec)}`);
// 3. every expression renders without leftover placeholders, for both heads
for (const rig of ["remy", "assoc"]) for (const preset of Object.keys(B.face.expressions)) {
  const h = headMarkup(B.rigs[rig], B.face, B.markup, { preset, gaze: [3, -2] });
  check(!h.includes("{{") && h.length > 200, `${rig} head ${preset}`);
}
// 4. rigid limbs: every non-prop part matrix has |det| = 1 (no stretch, bone lengths preserved)
for (const [rig, lib] of Object.entries(B.poses) as [string, Record<string, Pose>][]) for (const [name, pose] of Object.entries(lib)) {
  for (const p of evaluate(B.joints, B.slots, B.hand_front, B.rigs[rig], pose)) {
    if (p.id.startsWith("held_") || p.id.startsWith("prop_")) continue;
    check(Math.abs(Math.abs(p.m[0] * p.m[3] - p.m[1] * p.m[2]) - 1) < 1e-9, `${rig}:${name} ${p.id} not rigid`);
  }
}
// 5. leg IK round trip: ankle lands exactly on the target, shoe flat
const base = B.poses.remy.stand_neutral as Pose;
for (const side of ["n", "f"] as const) for (const [dx, lift, dy] of [[-120, 0, 30], [0, 0, 4], [130, 0, 36], [60, 40, 8]]) {
  const rest: Pt = B.joints[`ankle_${side}`];
  const target: Pt = [rest[0] + dx, rest[1] - lift - dy];
  const leg = legIK(B.joints, side, target, 0);
  const pose = { ...resolve(B.joints, base), body_dy: dy, [`leg_${side}`]: leg } as unknown as Pose;
  const shoe = evaluate(B.joints, B.slots, B.hand_front, B.rigs.remy, pose).find((p) => p.id === `shoe_${side}`)!;
  const w = apply(shoe.m, rest);
  check(close(w, [target[0], target[1] + dy], 1e-6), `legIK ${side} ${dx},${lift}: ankle ${w}`);
  check(Math.abs(Math.atan2(shoe.m[1], shoe.m[0])) < 1e-9, `legIK ${side}: shoe not flat`);
  check(leg[1] >= -1e-9 && leg[1] <= 100, `legIK ${side} ${dx}: knee ${leg[1].toFixed(1)} outside [0,100]`);
}
// 6. walk: planted feet do not slide, stay on the ground, joints stay in range
for (const [dist, frames, lead] of [[645, 50, "n"], [900, 70, "f"], [300, 30, "n"]] as const) {
  const plan = planWalk({ f0: 0, f1: frames, dist, lead, upper: resolve(B.joints, B.poses.remy.walk_a) });
  const plantedAt: Record<string, number | null> = { n: null, f: null };
  let maxSlide = 0, maxGround = 0, minKnee = 1e9, maxKnee = -1e9, minHip = 1e9, maxHip = -1e9, maxDy = 0;
  for (let f = -2; f <= plan.fEnd + 2; f += 0.25) {
    const { pose, dx } = walkAt(B.joints, plan, f);
    const parts = evaluate(B.joints, B.slots, B.hand_front, B.rigs.remy, pose as unknown as Pose);
    maxDy = Math.max(maxDy, pose.body_dy);
    for (const side of ["n", "f"] as const) {
      const shoe = parts.find((p) => p.id === `shoe_${side}`)!;
      const [wx, wy] = apply(shoe.m, B.joints[`ankle_${side}`]);
      const foot = footAt(plan, side, f);
      const leg = side === "n" ? pose.leg_n : pose.leg_f;
      minKnee = Math.min(minKnee, leg[1]); maxKnee = Math.max(maxKnee, leg[1]);
      minHip = Math.min(minHip, leg[0]); maxHip = Math.max(maxHip, leg[0]);
      // world x = rig x + body travel; the ankle must sit exactly where the plan put it
      check(Math.abs(wx + dx - (B.joints[`ankle_${side}`][0] + foot.x)) < 1e-6 && Math.abs(wy - (B.joints[`ankle_${side}`][1] - foot.lift)) < 1e-6,
        `walk ${dist}: ${side} ankle off target at f=${f}`);
      if (foot.planted) {
        if (plantedAt[side] === null) plantedAt[side] = wx + dx;
        maxSlide = Math.max(maxSlide, Math.abs(wx + dx - plantedAt[side]!));
        maxGround = Math.max(maxGround, Math.abs(wy - B.joints[`ankle_${side}`][1]));
      } else plantedAt[side] = null;
    }
  }
  check(maxSlide < 1e-6 && maxGround < 1e-6, `walk ${dist}: slide ${maxSlide} ground ${maxGround}`);
  check(minKnee >= -0.5 && maxKnee <= 100 && minHip >= -95 && maxHip <= 30, `walk ${dist}: knee ${minKnee.toFixed(1)}..${maxKnee.toFixed(1)} hip ${minHip.toFixed(1)}..${maxHip.toFixed(1)}`);
  console.log(`  walk dist=${dist} over ${frames}f: steps=${plan.steps.length} slide=${maxSlide.toExponential(1)} knee ${minKnee.toFixed(1)}..${maxKnee.toFixed(1)} hip ${minHip.toFixed(1)}..${maxHip.toFixed(1)} max body_dy ${maxDy.toFixed(1)}`);
}
console.log(fails ? `rig tests: ${fails} FAILED` : `rig tests: PASS (${Object.keys(REF.poses).length} poses, ${REF.eyes.length} eyes, ${REF.ik.length} IK, legIK, rigidity)`);
process.exit(fails ? 1 : 0);
