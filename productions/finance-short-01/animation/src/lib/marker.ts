import { E, prog } from "./anim.ts";
export type Point = [number, number];
export const markerTipAt = (t: number, check: number, deadline: number, home: Point, pointOnCircle: (angle: number) => Point, turn: number): Point => {
  const d0 = deadline, d1 = deadline + 20;
  const th = turn * prog(t, d0, d1, E.inOut);
  const approach = prog(t, check, d0, E.inOut);
  const start = pointOnCircle(0), end = pointOnCircle(turn);
  return t < d0 ? [home[0] + (start[0] - home[0]) * approach, home[1] + (start[1] - home[1]) * approach]
    : t <= d1 + 4 ? pointOnCircle(th) : [end[0] + (home[0] - end[0]) * prog(t, d1 + 4, d1 + 14), end[1] + (home[1] - end[1]) * prog(t, d1 + 4, d1 + 14)];
};
