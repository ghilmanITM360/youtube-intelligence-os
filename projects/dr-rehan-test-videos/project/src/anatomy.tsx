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
const bump = (u: number) => Math.exp(-(((u - NARROW_U) / 0.03) ** 2));
// Plaque crescent on one side (sd = +1/-1) of the vessel: from inside the wall (r 30) to r = 23 - depth.
const plaquePath = (narrow: number, sd: number) => {
  const outer: string[] = [], inner: string[] = [];
  for (let j = 0; j <= 24; j++) {
    const u = NARROW_U - 0.07 + (0.14 * j) / 24, p = ART.at(u), nx = -Math.sin(p.ang) * sd, ny = Math.cos(p.ang) * sd;
    const r = 23 - narrow * (sd > 0 ? 19 : 15) * bump(u);
    outer.push(`${(p.x + nx * 31).toFixed(1)} ${(p.y + ny * 31).toFixed(1)}`);
    inner.unshift(`${(p.x + nx * r).toFixed(1)} ${(p.y + ny * r).toFixed(1)}`);
  }
  return `M ${outer.join(' L ')} L ${inner.join(' L ')} Z`;
};

const LEG_OUT =
  'M -190 -980 C -230 -700 -310 -420 -275 -180 C -250 10 -150 230 -112 420 C -96 520 -90 584 -100 640 C -112 704 -62 742 0 742 L 300 742 C 362 742 372 690 322 670 C 222 640 152 600 112 540 C 92 400 100 0 118 -300 C 128 -520 150 -760 166 -980 Z';
const MUSCLE =
  'M -40 -700 C -258 -650 -290 -330 -226 -80 C -186 80 -126 200 -84 330 C -62 170 -24 -100 -14 -400 C -10 -560 -12 -660 -40 -700 Z';

type LegProps = {t: number; narrow: number; flow: number; muscleGlow?: number; pump?: number; o2?: number; xray?: number; spots?: number; tired?: number};
// 3. ANATOMY world: patient's lower leg (same side view/proportions as the rig, enlarged).
export const LegCutaway: React.FC<LegProps> = ({t, narrow, flow, muscleGlow = 0, pump = 0, o2 = 0, xray = 1, spots = 0, tired = 0}) => {
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
        {/* artery: ink edge, wall, lumen */}
        <path d={ART.d} stroke={INK} strokeWidth={84} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <path d={ART.d} stroke={P.arteryWall} strokeWidth={70} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <path d={ART.d} stroke="#B3202C" strokeWidth={46} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        {/* blood cells: always flow down the leg (u increasing); fewer get past the narrowing */}
        {Array.from({length: 40}, (_, i) => {
          const speed = 0.05 + 0.1 * flow;
          const u = (i / 40 + t * speed + rnd(i) * 0.01) % 1;
          if (u > NARROW_U + 0.02 && rnd(i + 40) > flow) return null;
          const p = ART.at(u);
          const lane = (rnd(i + 90) - 0.5) * 18 * (1 - narrow * bump(u));
          const near = bump(u) * narrow;
          return <ellipse key={i} cx={p.x - Math.sin(p.ang) * lane} cy={p.y + Math.cos(p.ang) * lane} rx={13 - 5 * near} ry={9 - 4 * near}
            transform={`rotate(${(p.ang * 180) / Math.PI} ${p.x - Math.sin(p.ang) * lane} ${p.y + Math.cos(p.ang) * lane})`} fill="#F04A55" stroke="#7E0F19" strokeWidth={3} />;
        })}
        {/* plaque built INTO the wall: yellow layer from the wall that bulges into the lumen (never fully closed) */}
        {narrow > 0.01 && [1, -1].map((sd) => <path key={sd} d={plaquePath(narrow, sd)} fill={P.plaque} stroke={INK} strokeWidth={4} strokeLinejoin="round" />)}
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

// Horizontal "artery -> muscle" panel used for NORMAL vs NARROWED comparisons (no numbers, only relative flow).
// Local frame: panel centre (0,0). Blood always flows left -> right into the calf muscle on the right.
const VY = 34, WALL = 44, LUMEN = 31, XC = -150, X0 = -560, X1 = 190;
const lumenAt = (x: number, narrow: number) => LUMEN - narrow * 24 * Math.exp(-(((x - XC) / 78) ** 2));
export const FlowPanel: React.FC<{
  t: number; narrow: number; activity: number; title: string; titleColor: string;
  w?: number; h?: number; o2?: number; mood?: 'ok' | 'strain' | 'tired'; pain?: number; arrows?: number;
}> = ({t, narrow, activity, title, titleColor, w = 1000, h = 330, o2 = 6, mood = 'ok', pain = 0, arrows = 1}) => {
  const id = `fp${Math.round(narrow * 100)}_${title.length}`;
  const pass = 1 - narrow * 0.72; // share of cells that make it past the narrowing
  const speed = 0.16 + 0.12 * activity;
  const pump = 1 + activity * 0.06 * Math.sin(t * 13);
  const plaque = (sd: number) => {
    const a: string[] = [], b: string[] = [];
    for (let j = 0; j <= 30; j++) {
      const x = XC - 190 + (380 * j) / 30;
      a.push(`${x.toFixed(1)} ${(VY + sd * (LUMEN + 4)).toFixed(1)}`);
      b.unshift(`${x.toFixed(1)} ${(VY + sd * lumenAt(x, narrow)).toFixed(1)}`);
    }
    return `M ${a.join(' L ')} L ${b.join(' L ')} Z`;
  };
  return (
    <g>
      <rect x={-w / 2} y={-h / 2} width={w} height={h} rx={26} fill="#fff" stroke={INK} strokeWidth={SW} />
      <clipPath id={id}><rect x={-w / 2 + 4} y={-h / 2 + 4} width={w - 8} height={h - 8} rx={22} /></clipPath>
      <g clipPath={`url(#${id})`}>
        {/* vessel */}
        <rect x={X0} y={VY - WALL} width={X1 - X0 + 40} height={WALL * 2} fill={P.arteryWall} stroke={INK} strokeWidth={6} />
        <rect x={X0} y={VY - LUMEN} width={X1 - X0 + 40} height={LUMEN * 2} fill="#B3202C" />
        {Array.from({length: 26}, (_, i) => {
          const u = (i / 26 + t * speed + rnd(i) * 0.02) % 1;
          const x = X0 + u * (X1 - X0 + 30);
          if (x > XC + 40 && rnd(i + 31) > pass) return null;
          const hl = lumenAt(x, narrow);
          const y = VY + (rnd(i + 7) - 0.5) * 1.2 * Math.max(0, hl - 10);
          const sq = clamp(hl / LUMEN, 0.45, 1);
          return <ellipse key={i} cx={x} cy={y} rx={13 * (1.25 - 0.25 * sq)} ry={10 * sq} fill="#F04A55" stroke="#7E0F19" strokeWidth={3} />;
        })}
        {narrow > 0.01 && [-1, 1].map((sd) => <path key={sd} d={plaque(sd)} fill={P.plaque} stroke={INK} strokeWidth={5} strokeLinejoin="round" />)}
        {/* flow arrows sit ABOVE the vessel, never on it */}
        {arrows > 0 && (
          <g opacity={arrows} fill="none" strokeLinecap="round" strokeLinejoin="round">
            <path d={`M ${X0 + 60} ${VY - 78} L ${X0 + 230} ${VY - 78} M ${X0 + 206} ${VY - 96} L ${X0 + 230} ${VY - 78} L ${X0 + 206} ${VY - 60}`} stroke={INK} strokeWidth={10} />
            <path d={`M ${XC + 110} ${VY - 78} L ${XC + 250} ${VY - 78} M ${XC + 230} ${VY - 92} L ${XC + 250} ${VY - 78} L ${XC + 230} ${VY - 64}`}
              stroke={narrow > 0.3 ? P.warning : INK} strokeWidth={narrow > 0.3 ? 5 : 10} strokeDasharray={narrow > 0.3 ? '12 12' : undefined} />
          </g>
        )}
        {/* calf muscle fed by the vessel */}
        <g transform={`translate(330 ${VY - 6}) scale(${1 / pump} ${pump})`}>
          <path d="M -150 0 C -150 -84 -60 -116 30 -110 C 120 -104 170 -50 168 6 C 166 64 110 112 20 110 C -70 108 -150 70 -150 0 Z" fill={P.muscle} stroke={INK} strokeWidth={SW} />
          {pain > 0 && <ellipse rx={170} ry={120} fill="url(#painGlow)" opacity={pain} />}
          {[-50, 0, 50].map((y, i) => <path key={i} d={`M -126 ${y * 0.7} Q 10 ${y * 1.15} 150 ${y * 0.8}`} stroke="#D46F6A" strokeWidth={5} fill="none" strokeLinecap="round" />)}
          {Array.from({length: o2}, (_, i) => {
            const life = (t * 0.55 + i / o2) % 1;
            return (
              <g key={i} transform={`translate(${-130 + life * 230} ${Math.sin(i * 2.3) * 58 + Math.sin(life * 5 + i) * 8})`} opacity={Math.sin(life * Math.PI)}>
                <circle r={20} fill={P.oxygen} stroke={INK} strokeWidth={3} />
                <text y={7} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={20} fill="#fff">O₂</text>
              </g>
            );
          })}
          <g transform="translate(40 -6)">
            {mood === 'ok' ? (
              <><circle cx={-26} cy={0} r={8} fill={INK} /><circle cx={26} cy={0} r={8} fill={INK} /><path d="M -18 26 Q 0 42 18 26" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" /></>
            ) : mood === 'strain' ? (
              <><path d="M -38 -10 L -18 0 L -38 10 M 38 -10 L 18 0 L 38 10" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" strokeLinejoin="round" />
                <rect x={-22} y={20} width={44} height={20} rx={7} fill="#fff" stroke={INK} strokeWidth={5} /></>
            ) : (
              <><path d="M -36 -2 L -16 -2 M 16 -2 L 36 -2" stroke={INK} strokeWidth={6} strokeLinecap="round" /><path d="M -18 36 Q 0 22 18 36" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" /></>
            )}
          </g>
        </g>
      </g>
      <text x={-w / 2 + 34} y={-h / 2 + 62} fontFamily={FONT} fontWeight={700} fontSize={52} fill={titleColor} stroke={INK} strokeWidth={9} paintOrder="stroke">{title}</text>
    </g>
  );
};
