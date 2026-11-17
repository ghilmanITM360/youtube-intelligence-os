import React from 'react';
import {INK, P, SW, FONT, Vec, clamp, lerp, rnd} from './lib';

// ---------- polyline sampling for the leg artery ----------
const catmull = (pts: Vec[], n = 18): Vec[] => {
  const out: Vec[] = [];
  for (let i = 0; i < pts.length - 1; i++) {
    const p0 = pts[Math.max(0, i - 1)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(pts.length - 1, i + 2)];
    for (let j = 0; j < n; j++) {
      const t = j / n, t2 = t * t, t3 = t2 * t;
      const f = (a: number, b: number, c: number, d: number) => 0.5 * (2 * b + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t2 + (-a + 3 * b - 3 * c + d) * t3);
      out.push({x: f(p0.x, p1.x, p2.x, p3.x), y: f(p0.y, p1.y, p2.y, p3.y)});
    }
  }
  out.push(pts[pts.length - 1]);
  return out;
};
const sampler = (pts: Vec[]) => {
  const cum = [0];
  for (let i = 1; i < pts.length; i++) cum.push(cum[i - 1] + Math.hypot(pts[i].x - pts[i - 1].x, pts[i].y - pts[i - 1].y));
  const total = cum[cum.length - 1];
  const d = 'M' + pts.map((p) => `${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' L');
  const at = (u: number) => {
    const s = clamp(u) * total;
    let i = 1;
    while (i < cum.length - 1 && cum[i] < s) i++;
    const a = pts[i - 1], b = pts[i], f = (s - cum[i - 1]) / (cum[i] - cum[i - 1] || 1);
    return {x: lerp(a.x, b.x, f), y: lerp(a.y, b.y, f), ang: Math.atan2(b.y - a.y, b.x - a.x)};
  };
  return {d, at, total};
};

const ART = sampler(catmull([{x: -20, y: -900}, {x: -40, y: -600}, {x: -58, y: -330}, {x: -44, y: -60}, {x: -6, y: 220}, {x: 36, y: 450}, {x: 90, y: 600}, {x: 210, y: 690}]));
export const NARROW_U = 0.3;
export const narrowPoint = () => ART.at(NARROW_U);
export const muscleCenter = {x: -150, y: -260};

const LEG_OUT =
  'M -190 -980 C -230 -700 -310 -420 -275 -180 C -250 10 -150 230 -112 420 C -96 520 -90 584 -100 640 C -112 704 -62 742 0 742 L 300 742 C 362 742 372 690 322 670 C 222 640 152 600 112 540 C 92 400 100 0 118 -300 C 128 -520 150 -760 166 -980 Z';
const MUSCLE =
  'M -40 -700 C -258 -650 -290 -330 -226 -80 C -186 80 -126 200 -84 330 C -62 170 -24 -100 -14 -400 C -10 -560 -12 -660 -40 -700 Z';

type LegProps = {t: number; narrow: number; flow: number; muscleGlow?: number; pump?: number; o2?: number; xray?: number; spots?: number; tired?: number};
// 3. ANATOMY world: patient's lower leg (same side view/proportions as the rig, enlarged).
export const LegCutaway: React.FC<LegProps> = ({t, narrow, flow, muscleGlow = 0, pump = 0, o2 = 0, xray = 1, spots = 0, tired = 0}) => {
  const n = narrowPoint();
  const nx = -Math.sin(n.ang), ny = Math.cos(n.ang);
  const plaq = 8 + narrow * 15;
  const sq = 1 + pump * 0.05 * Math.sin(t * 12);
  return (
    <g>
      <path d={LEG_OUT} fill="#F6DDC6" stroke={INK} strokeWidth={SW * 1.4} strokeLinejoin="round" />
      <g opacity={xray}>
        {/* tibia */}
        <path d="M 46 -980 L 92 -980 Q 100 -300 84 520 Q 70 560 52 520 Q 36 -300 46 -980 Z" fill="#FBF6EA" stroke={INK} strokeWidth={5} />
        {/* calf muscle */}
        <g transform={`translate(${muscleCenter.x} ${muscleCenter.y}) scale(${1 / sq} ${sq}) translate(${-muscleCenter.x} ${-muscleCenter.y})`}>
          <path d={MUSCLE} fill={P.muscle} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          {muscleGlow > 0 && <path d={MUSCLE} fill="url(#painGlow)" opacity={muscleGlow} />}
          {[0, 1, 2, 3, 4].map((i) => (
            <path key={i} d={`M ${-60 - i * 34} ${-560 + i * 30} Q ${-150 - i * 16} ${-260} ${-90 - i * 10} ${80 - i * 20}`} stroke="#D46F6A" strokeWidth={5} fill="none" strokeLinecap="round" />
          ))}
        </g>
        <path d="M -84 320 Q -84 500 -74 640" stroke={INK} strokeWidth={34} fill="none" strokeLinecap="round" />
        <path d="M -84 320 Q -84 500 -74 640" stroke="#F3EBDD" strokeWidth={22} fill="none" strokeLinecap="round" />
        {/* artery */}
        <path d={ART.d} stroke={INK} strokeWidth={68} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <path d={ART.d} stroke={P.arteryWall} strokeWidth={56} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <path d={ART.d} stroke="#B3202C" strokeWidth={34} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        {/* blood cells */}
        {Array.from({length: 34}, (_, i) => {
          const speed = 0.05 + 0.1 * flow;
          const u = (i / 34 + t * speed + rnd(i) * 0.01) % 1;
          if (u > NARROW_U + 0.02 && rnd(i + 40) > flow) return null;
          const p = ART.at(u);
          const near = Math.abs(u - NARROW_U) < 0.03;
          return <ellipse key={i} cx={p.x} cy={p.y} rx={near ? 7 : 11} ry={near ? 6 : 8} transform={`rotate(${(p.ang * 180) / Math.PI} ${p.x} ${p.y})`} fill="#F04A55" stroke="#7E0F19" strokeWidth={3} />;
        })}
        {/* plaque narrowing */}
        {narrow > 0.01 &&
          [1, -1].map((s) => (
            <ellipse key={s} cx={n.x + nx * s * (28 - plaq / 2)} cy={n.y + ny * s * (28 - plaq / 2)} rx={30 + narrow * 22} ry={plaq}
              transform={`rotate(${(n.ang * 180) / Math.PI} ${n.x + nx * s * (28 - plaq / 2)} ${n.y + ny * s * (28 - plaq / 2)})`}
              fill={P.plaque} stroke={INK} strokeWidth={4} opacity={clamp(narrow * 3)} />
          ))}
        {/* oxygen delivered into the muscle */}
        {Array.from({length: 10}, (_, i) => {
          if (rnd(i + 70) > o2) return null;
          const life = (t * 0.6 + rnd(i)) % 1;
          const src = ART.at(0.36 + rnd(i + 5) * 0.22);
          const x = src.x - life * 120, y = src.y + Math.sin(life * 6 + i) * 10;
          return (
            <g key={'o' + i} transform={`translate(${x} ${y})`} opacity={Math.sin(life * Math.PI)}>
              <circle r={22} fill={P.oxygen} stroke={INK} strokeWidth={3} />
              <text y={8} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={22} fill="#fff">O₂</text>
            </g>
          );
        })}
        {spots > 0 && [0.56, 0.74].map((u, i) => {
          const p = ART.at(u);
          return <ellipse key={'s' + i} cx={p.x + 18} cy={p.y} rx={16 * spots} ry={26 * spots} transform={`rotate(${(p.ang * 180) / Math.PI} ${p.x + 18} ${p.y})`} fill={P.plaque} stroke={INK} strokeWidth={4} />;
        })}
        {tired > 0 && (
          <g transform={`translate(${muscleCenter.x - 10} ${muscleCenter.y - 40}) scale(${tired})`}>
            <circle cx={-34} cy={4} r={10} fill={INK} /><circle cx={34} cy={4} r={10} fill={INK} />
            <path d="M -50 -12 L -20 -12 M 20 -12 L 50 -12" stroke={INK} strokeWidth={7} strokeLinecap="round" />
            <path d="M -24 52 Q 0 32 24 52" stroke={INK} strokeWidth={7} fill="none" strokeLinecap="round" />
            <path d="M 0 -20 Q 9 -6 0 2 Q -9 -6 0 -20 Z" transform="translate(70 -30) scale(1.6)" fill="#9AD2F7" stroke={INK} strokeWidth={3} />
          </g>
        )}
      </g>
    </g>
  );
};

// Round artery cross-section: plaque crescent closing the lumen.
export const CrossSection: React.FC<{narrow: number; t: number}> = ({narrow, t}) => (
  <g>
    <circle r={120} fill={P.arteryWall} stroke={INK} strokeWidth={SW} />
    <clipPath id="lumenClip"><circle r={80} /></clipPath>
    <circle r={80} fill="#B3202C" stroke={INK} strokeWidth={5} />
    <g clipPath="url(#lumenClip)">
      {[0, 1, 2, 3, 4].map((i) => (
        <circle key={i} cx={30 * Math.cos(i * 1.3 + t * 2)} cy={30 * Math.sin(i * 1.7 + t * 2)} r={12} fill="#F04A55" stroke="#7E0F19" strokeWidth={3} opacity={i < 2 + 3 * (1 - narrow) ? 1 : 0} />
      ))}
      <circle cx={-150 + 100 * narrow} cy={0} r={100} fill={P.plaque} stroke={INK} strokeWidth={5} />
    </g>
    <circle r={80} fill="none" stroke={INK} strokeWidth={5} />
  </g>
);

// Gauge: v in 0..1 (0 = low/red, 1 = full/green).
export const Gauge: React.FC<{v: number; label: string; low?: string}> = ({v, label, low}) => {
  const seg = (a0: number, a1: number, c: string) => {
    const r = 110, p = (a: number) => `${-Math.cos(a) * r} ${-Math.sin(a) * r}`;
    return <path d={`M ${p(a0)} A ${r} ${r} 0 0 1 ${p(a1)}`} stroke={c} strokeWidth={34} fill="none" />;
  };
  const a = Math.PI * clamp(v);
  return (
    <g>
      <path d="M -150 20 A 150 150 0 0 1 150 20 Z" fill="#fff" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      {seg(0.02, 1.0, P.warning)}{seg(1.0, 2.0, P.caution)}{seg(2.0, Math.PI - 0.02, P.relief)}
      <path d={`M 0 0 L ${-Math.cos(a) * 100} ${-Math.sin(a) * 100}`} stroke={INK} strokeWidth={10} strokeLinecap="round" />
      <circle r={14} fill={INK} />
      <text y={-34} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={40} fill={INK}>{label}</text>
      {low && <text x={-118} y={62} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={34} fill={P.warning} opacity={clamp((0.3 - v) * 6)}>{low}</text>}
    </g>
  );
};

// Personified calf muscle (explainer character, used in muscle close-ups).
export const MuscleBuddy: React.FC<{t: number; effort: number; mood: 'ok' | 'strain' | 'tired'; sweat?: number}> = ({t, effort, mood, sweat = 0}) => {
  const sq = 1 + effort * 0.07 * Math.sin(t * 13);
  const droop = mood === 'tired' ? 8 : 0;
  return (
    <g transform={`scale(${1 / sq} ${sq})`}>
      <path d="M 0 -300 C -190 -270 -210 -40 -150 120 C -110 220 -40 280 0 330 C 40 280 110 220 150 120 C 210 -40 190 -270 0 -300 Z" fill={P.muscle} stroke={INK} strokeWidth={SW * 1.3} strokeLinejoin="round" />
      {[-90, -45, 45, 90].map((x, i) => (
        <path key={i} d={`M ${x * 0.6} -250 Q ${x * 1.4} 0 ${x * 0.4} 260`} stroke="#D46F6A" strokeWidth={6} fill="none" strokeLinecap="round" />
      ))}
      <path d="M 0 320 L 0 420" stroke={INK} strokeWidth={40} strokeLinecap="round" />
      <path d="M 0 320 L 0 420" stroke="#F3EBDD" strokeWidth={26} strokeLinecap="round" />
      {/* face */}
      <g transform={`translate(0 ${-40 + droop})`}>
        {mood === 'ok' ? (
          <>
            <circle cx={-46} cy={0} r={13} fill={INK} /><circle cx={46} cy={0} r={13} fill={INK} />
            <path d="M -30 46 Q 0 72 30 46" stroke={INK} strokeWidth={8} fill="none" strokeLinecap="round" />
          </>
        ) : mood === 'strain' ? (
          <>
            <path d="M -62 -14 L -34 0 L -62 14 M 62 -14 L 34 0 L 62 14" stroke={INK} strokeWidth={8} fill="none" strokeLinecap="round" strokeLinejoin="round" />
            <rect x={-36} y={36} width={72} height={30} rx={10} fill="#fff" stroke={INK} strokeWidth={6} />
            <path d="M -34 51 L 34 51" stroke={INK} strokeWidth={4} />
          </>
        ) : (
          <>
            <circle cx={-46} cy={4} r={12} fill={INK} /><circle cx={46} cy={4} r={12} fill={INK} />
            <path d="M -64 -10 L -28 -10 M 28 -10 L 64 -10" stroke={INK} strokeWidth={8} strokeLinecap="round" />
            <path d="M -30 64 Q 0 40 30 64" stroke={INK} strokeWidth={8} fill="none" strokeLinecap="round" />
          </>
        )}
        <path d="M -70 -46 L -24 -30 M 70 -46 L 24 -30" stroke={INK} strokeWidth={8} strokeLinecap="round" opacity={mood === 'ok' ? 0 : 1} />
      </g>
      {sweat > 0 && [0, 1].map((i) => (
        <path key={i} d="M 0 -22 Q 13 0 0 11 Q -13 0 0 -22 Z" transform={`translate(${i ? 150 : -160} ${-150 + ((t * 60 + i * 20) % 50)}) scale(1.4)`} fill="#9AD2F7" stroke={INK} strokeWidth={3} opacity={sweat} />
      ))}
    </g>
  );
};

// Artery tree overlay for the front-view patient (character space, s = 1 rig units).
export const ArteryTree: React.FC<{draw: number; legPlaque: number; bodyPlaque: number; pulse: number}> = ({draw, legPlaque, bodyPlaque, pulse}) => {
  const legs = [1, -1].map((s) => `M 0 -330 Q ${s * 22} -312 ${s * 25} -250 L ${s * 26} -170 Q ${s * 24} -90 ${s * 24} -30`);
  const up = ['M 0 -330 L 0 -470 Q 14 -490 22 -470', 'M 0 -470 L -12 -512', 'M 0 -470 L 12 -512'];
  const len = 420;
  const stroke = (d: string, i: number) => (
    <g key={i}>
      <path d={d} stroke={INK} strokeWidth={16} fill="none" strokeLinecap="round" strokeDasharray={len} strokeDashoffset={len * (1 - draw)} />
      <path d={d} stroke={P.artery} strokeWidth={8} fill="none" strokeLinecap="round" strokeDasharray={len} strokeDashoffset={len * (1 - draw)} />
    </g>
  );
  const dot = (x: number, y: number, v: number, key: string) =>
    v > 0 ? <ellipse key={key} cx={x} cy={y} rx={10 * v} ry={13 * v} fill={P.plaque} stroke={INK} strokeWidth={3} /> : null;
  return (
    <g>
      {[...legs, ...up].map(stroke)}
      {dot(25, -200, legPlaque, 'a')}{dot(-26, -150, legPlaque, 'b')}{dot(24, -80, legPlaque, 'c')}
      {dot(-10, -500, bodyPlaque, 'd')}{dot(0, -400, bodyPlaque, 'e')}
      {pulse > 0 && pulse < 1 && <circle cx={pulse < 0.5 ? 25 : 0} cy={pulse < 0.5 ? lerp(-60, -330, pulse * 2) : lerp(-330, -450, (pulse - 0.5) * 2)} r={14} fill="#FFE38A" stroke={INK} strokeWidth={4} />}
    </g>
  );
};
