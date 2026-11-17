import {Easing, interpolate, spring} from 'remotion';
import tokens from '../STYLE_TOKENS.json';
import envelope from './envelope.json';

export const FPS = tokens.canvas.fps;
export const W = tokens.canvas.width;
export const H = tokens.canvas.height;
export const P = tokens.palette;
export const INK = P.ink;
export const SW = tokens.stroke.ink;
export const FONT = `${tokens.type.family}, 'Chalkboard SE', 'Comic Sans MS', sans-serif`;
// Narration captions: bundled Nunito Black (OFL) for maximum legibility on phones.
export const CAP_FONT = "Nunito, 'Avenir Next', sans-serif";

export type Vec = {x: number; y: number};

export const smooth = Easing.bezier(0.45, 0, 0.2, 1);
export const clamp = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
export const lerp = (a: number, b: number, u: number) => a + (b - a) * u;

// Keyframe a value against absolute narration time (seconds).
export const k = (t: number, ts: number[], vs: number[], easing = smooth) =>
  interpolate(t, ts, vs, {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing});

// Springy 0 -> 1 pop that starts at t0 (POP_IN grammar).
export const pop = (t: number, t0: number, cfg = tokens.motion.popIn.spring) =>
  t < t0 ? 0 : spring({frame: (t - t0) * FPS, fps: FPS, config: cfg});

// Fade-out multiplier helper: 1 until t1, then 0 by t1+d.
export const out = (t: number, t1: number, d = 0.25) => 1 - clamp((t - t1) / d);

// Mouth openness from the real narration loudness (frame-accurate).
export const speech = (frame: number) => {
  const db = (i: number) => envelope[Math.max(0, Math.min(envelope.length - 1, i))];
  const v = (db(frame - 1) + 2 * db(frame) + db(frame + 1)) / 4;
  return clamp((v + 38) / 22);
};

// Deterministic pseudo-random in [0,1).
export const rnd = (i: number) => {
  const x = Math.sin(i * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

export const add = (p: Vec, v: Vec, s = 1): Vec => ({x: p.x + v.x * s, y: p.y + v.y * s});
