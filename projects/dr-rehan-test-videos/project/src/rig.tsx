import React from 'react';
import {INK, SW, P, Vec, clamp, lerp} from './lib';

// Limb angle convention: 0 = pointing straight down, + = rotated toward +x (the facing side).
const D2R = Math.PI / 180;
const dir = (a: number): Vec => ({x: Math.sin(a * D2R), y: Math.cos(a * D2R)});
const add = (p: Vec, v: Vec, s = 1): Vec => ({x: p.x + v.x * s, y: p.y + v.y * s});
const lerpV = (a: Vec, b: Vec, u: number): Vec => ({x: lerp(a.x, b.x, u), y: lerp(a.y, b.y, u)});
const angOf = (from: Vec, to: Vec) => Math.atan2(to.x - from.x, to.y - from.y) / D2R;
const pts = (...p: Vec[]) => 'M' + p.map((q) => `${q.x.toFixed(1)} ${q.y.toFixed(1)}`).join(' L');
// Torso-local point (hip origin, up = -y) rotated by lean.
const tl = (hip: Vec, lean: number, lx: number, ly: number): Vec => {
  const c = Math.cos(lean * D2R), s = Math.sin(lean * D2R);
  return {x: hip.x + lx * c - ly * s, y: hip.y + lx * s + ly * c};
};

export type Look = {
  id: 'patient' | 'doctor';
  skin: string; hair: string; top: string; bottom: string; shoe: string; sole: string;
  thigh: number; shin: number; upper: number; fore: number;
  legW: number; armW: number; headR: number; torso: number; halfW: number;
};

export const PATIENT: Look = {
  id: 'patient', skin: P.patientSkin, hair: P.patientHair, top: P.patientShirt, bottom: P.patientShorts,
  shoe: '#FFFFFF', sole: P.patientShorts, thigh: 140, shin: 150, upper: 104, fore: 98,
  legW: 42, armW: 28, headR: 96, torso: 222, halfW: 80,
};
export const DOCTOR: Look = {
  id: 'doctor', skin: P.doctorSkin, hair: P.doctorHair, top: P.doctorCoat, bottom: P.doctorPants,
  shoe: '#2B2B2B', sole: '#111111', thigh: 150, shin: 158, upper: 106, fore: 98,
  legW: 44, armW: 32, headR: 96, torso: 240, halfW: 94,
};

export type Hand = 'fist' | 'point' | 'open' | 'up' | 'thumb';
export type Pose = {
  lean: number; seat?: number; dy?: number; head: number;
  thighF: number; kneeF: number; thighB: number; kneeB: number;
  armF: number; elbowF: number; armB: number; elbowB: number;
  handF: Hand; handB: Hand;
  reachF?: Vec; reachFW?: number; reachB?: Vec; reachBW?: number;
};

export const STAND: Pose = {
  dy: 0, lean: 0, head: 0, thighF: 3, kneeF: 2, thighB: -3, kneeB: 2,
  armF: 4, elbowF: 12, armB: -4, elbowB: 12, handF: 'fist', handB: 'fist',
};
export const FRONT: Pose = {
  dy: 0, lean: 0, head: 0, thighF: 4, kneeF: 0, thighB: 4, kneeB: 0,
  armF: 10, elbowF: 6, armB: 10, elbowB: 6, handF: 'fist', handB: 'fist',
};
export const SIT: Pose = {
  dy: 0, lean: -3, seat: 168, head: 0, thighF: 86, kneeF: 86, thighB: 80, kneeB: 78,
  armF: 20, elbowF: 50, armB: 14, elbowB: 50, handF: 'fist', handB: 'fist',
};

export const pose = (base: Pose, o: Partial<Pose>): Pose => ({...base, ...o});

export function mix(a: Pose, b: Pose, u: number): Pose {
  u = clamp(u);
  const out: any = {...(u < 0.5 ? a : b)};
  for (const key of Object.keys(b) as (keyof Pose)[]) {
    const va = a[key], vb = b[key];
    if (typeof va === 'number' && typeof vb === 'number') out[key] = lerp(va, vb, u);
  }
  out.seat = a.seat !== undefined && b.seat !== undefined ? lerp(a.seat, b.seat, u) : undefined;
  out.sitW = lerp(a.seat !== undefined ? 1 : 0, b.seat !== undefined ? 1 : 0, u);
  out.seatA = a.seat ?? b.seat;
  out.seatB = b.seat ?? a.seat;
  for (const s of ['F', 'B'] as const) {
    const ra = a[`reach${s}`], rb = b[`reach${s}`];
    out[`reach${s}`] = ra && rb ? lerpV(ra, rb, u) : ra ?? rb;
    out[`reach${s}W`] = lerp(ra ? a[`reach${s}W`] ?? 1 : 0, rb ? b[`reach${s}W`] ?? 1 : 0, u);
  }
  return out as Pose;
}

// Ground-locked walk. d = distance walked in character units (world distance / scale).
// The stance foot is solved by 2-bone IK so it stays fixed on the ground (no foot sliding);
// the swing foot leaves and lands with zero ground speed; hip bob comes from leg geometry.
export function walk(d: number, o: {L?: number; limp?: number; arms?: number; look?: Look} = {}): Pose {
  const look = o.look ?? PATIENT, L = o.L ?? 340, limp = o.limp ?? 0, A = o.arms ?? 20;
  const T = look.thigh, S = look.shin, leg = T + S;
  const p = d / L, fr = (x: number) => ((x % 1) + 1) % 1;
  const fF = fr(p), fB = fr(p + 0.5);
  // antalgic dip: the painful (front) leg gives a little in its own mid-stance
  const dip = fF < 0.5 ? Math.sin((Math.PI * fF) / 0.5) ** 2 : 0;
  const k = 0.972 - 0.06 * limp * dip;
  const rel = (f: number) => (f < 0.5 ? (0.25 - f) * L : (() => {
    const u = (f - 0.5) / 0.5, e = 0.5 - 0.5 * Math.cos(Math.PI * u);
    return (-0.25 + e - 0.5 * u) * L;
  })());
  const lift = (f: number) => (f < 0.5 ? 0 : Math.sin((Math.PI * (f - 0.5)) / 0.5) * (44 - 14 * limp));
  const stanceRx = fF < 0.5 ? rel(fF) : rel(fB);
  const h = Math.sqrt(Math.max(1, (k * leg) ** 2 - stanceRx ** 2));
  const ik = (rx: number, ry: number) => {
    const dd = Math.min(Math.hypot(rx, ry), leg - 0.5);
    const a = Math.atan2(rx, ry) / D2R;
    const al = Math.acos(clamp((T * T + dd * dd - S * S) / (2 * T * dd), -1, 1)) / D2R;
    const be = Math.acos(clamp((T * T + S * S - dd * dd) / (2 * T * S), -1, 1)) / D2R;
    return [a + al, 180 - be];
  };
  const [thF, knF] = ik(rel(fF) - 4, h - lift(fF));
  const [thB, knB] = ik(rel(fB) + 4, h - lift(fB));
  const f = p * 2 * Math.PI;
  return {
    dy: 0, lean: 4 + limp * 7, head: limp * 7 + 1.5 * Math.sin(2 * f),
    thighF: thF, kneeF: knF, thighB: thB, kneeB: knB,
    armF: -A * Math.sin(f) + 4, elbowF: 24 + 8 * Math.sin(f),
    armB: A * Math.sin(f) + 4, elbowB: 24 - 8 * Math.sin(f),
    handF: 'fist', handB: 'fist',
  };
}

// ---------- faces ----------
export type Mouth = 'smile' | 'big' | 'line' | 'frown' | 'wavy' | 'grit' | 'o' | 'talk';
export type Eyes = 'dot' | 'wide' | 'closed' | 'squeeze' | 'half';
export type Face = {mouth: Mouth; eyes: Eyes; brow: number; raise: number; look: number; sweat: number; blush: number};

export const FACES = {
  neutral: {mouth: 'line', eyes: 'dot', brow: 0, raise: 0, look: 0.8, sweat: 0, blush: 0},
  happy: {mouth: 'smile', eyes: 'dot', brow: 0, raise: 0.2, look: 0.8, sweat: 0, blush: 0},
  discomfort: {mouth: 'wavy', eyes: 'dot', brow: -0.5, raise: 0, look: 0.6, sweat: 0.6, blush: 0},
  pain: {mouth: 'grit', eyes: 'squeeze', brow: 1, raise: 0, look: 0.5, sweat: 1, blush: 0},
  relief: {mouth: 'smile', eyes: 'closed', brow: -0.3, raise: 0.3, look: 0.6, sweat: 0, blush: 1},
  concern: {mouth: 'frown', eyes: 'dot', brow: -0.9, raise: 0.2, look: 0.6, sweat: 0.3, blush: 0},
  worried: {mouth: 'wavy', eyes: 'half', brow: -1, raise: 0, look: 0.4, sweat: 0.8, blush: 0},
  understanding: {mouth: 'smile', eyes: 'dot', brow: -0.1, raise: 0.5, look: 0.8, sweat: 0, blush: 0.4},
  surprised: {mouth: 'o', eyes: 'wide', brow: 0, raise: 1, look: 0.8, sweat: 0, blush: 0},
  talk: {mouth: 'talk', eyes: 'dot', brow: 0, raise: 0.2, look: 0.3, sweat: 0, blush: 0},
  serious: {mouth: 'talk', eyes: 'dot', brow: 0.5, raise: 0, look: 0.2, sweat: 0, blush: 0},
  doctorConcern: {mouth: 'talk', eyes: 'dot', brow: -0.8, raise: 0.3, look: 0.4, sweat: 0, blush: 0},
} satisfies Record<string, Face>;
export type FaceName = keyof typeof FACES;

const HAIR = {
  patient:
    'M -98 -12 C -104 -72 -60 -114 -4 -112 C 56 -114 102 -78 99 -16 C 90 -34 80 -46 64 -52 C 64 -40 58 -34 50 -32 C 44 -50 30 -60 12 -64 C 14 -52 8 -44 0 -42 C -6 -58 -26 -64 -46 -62 C -40 -50 -44 -40 -54 -36 C -64 -46 -80 -42 -98 -12 Z',
  patientTuft: 'M -30 -104 C -46 -136 -20 -152 2 -140 C -12 -134 -16 -122 -10 -108 Z',
  doctor:
    'M -96 -22 C -100 -80 -52 -114 4 -112 C 60 -112 100 -80 97 -24 C 86 -50 70 -62 42 -68 C 12 -74 -22 -64 -42 -80 C -58 -62 -78 -52 -96 -22 Z',
  beard:
    'M -90 14 C -86 66 -48 98 0 100 C 48 98 86 66 90 14 C 80 36 68 50 50 58 C 32 70 -32 70 -50 58 C -68 50 -80 36 -90 14 Z',
  mustache: 'M -30 30 C -16 16 16 16 30 30 C 14 24 -14 24 -30 30 Z',
};

export const Head: React.FC<{look: Look; face: Face; talk: number; t: number; side: boolean}> = ({look, face, talk, t, side}) => {
  const R = look.headR;
  const ox = face.look * (side ? 24 : 10);
  const ey = -2;
  const eyes = [ox - 28, ox + 28];
  const blink = face.eyes === 'dot' && (t * 10) % 37 < 1.2;
  const br = face.raise * 10;
  const bi = face.brow * 9, bo = -face.brow * 5;
  const doc = look.id === 'doctor';
  const my = doc ? 40 : 42;
  const mouth = () => {
    const m = face.mouth;
    if (m === 'talk') {
      if (talk < 0.12) return <path d="M -16 2 Q 0 10 16 2" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" />;
      return <ellipse cx={0} cy={4} rx={13 + talk * 3} ry={3 + talk * 13} fill="#7A2430" stroke={INK} strokeWidth={5} />;
    }
    if (m === 'smile') return <path d="M -22 -2 Q 0 18 22 -2" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" />;
    if (m === 'big') return <path d="M -26 -6 Q 0 36 26 -6 Z" fill="#7A2430" stroke={INK} strokeWidth={5} strokeLinejoin="round" />;
    if (m === 'line') return <path d="M -15 4 L 15 4" stroke={INK} strokeWidth={6} strokeLinecap="round" />;
    if (m === 'frown') return <path d="M -20 12 Q 0 -6 20 12" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" />;
    if (m === 'wavy') return <path d="M -22 6 Q -11 -3 0 6 Q 11 15 22 6" stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" />;
    if (m === 'o') return <ellipse cx={0} cy={6} rx={9} ry={12} fill="#7A2430" stroke={INK} strokeWidth={5} />;
    return (
      <g>
        <rect x={-26} y={-6} width={52} height={24} rx={9} fill="#fff" stroke={INK} strokeWidth={5} />
        <path d="M -24 6 L 24 6 M -9 -5 L -9 17 M 8 -5 L 8 17" stroke={INK} strokeWidth={3} />
      </g>
    );
  };
  const eye = (x: number, i: number) => {
    const e = blink ? 'blink' : face.eyes;
    if (e === 'blink') return <path key={i} d={`M ${x - 10} ${ey} L ${x + 10} ${ey}`} stroke={INK} strokeWidth={5} strokeLinecap="round" />;
    if (e === 'dot') return <circle key={i} cx={x} cy={ey} r={9.5} fill={INK} />;
    if (e === 'wide') return <g key={i}><circle cx={x} cy={ey} r={16} fill="#fff" stroke={INK} strokeWidth={4} /><circle cx={x + 3} cy={ey} r={8} fill={INK} /></g>;
    if (e === 'closed') return <path key={i} d={`M ${x - 13} ${ey + 4} Q ${x} ${ey - 10} ${x + 13} ${ey + 4}`} stroke={INK} strokeWidth={5.5} fill="none" strokeLinecap="round" />;
    if (e === 'half') return <g key={i}><circle cx={x} cy={ey + 2} r={9} fill={INK} /><path d={`M ${x - 14} ${ey - 4} L ${x + 14} ${ey - 4}`} stroke={INK} strokeWidth={5} strokeLinecap="round" /></g>;
    const s = i === 0 ? 1 : -1;
    return <path key={i} d={`M ${x - 11 * s} ${ey - 10} L ${x + 9 * s} ${ey} L ${x - 11 * s} ${ey + 10}`} stroke={INK} strokeWidth={5.5} fill="none" strokeLinecap="round" strokeLinejoin="round" />;
  };
  return (
    <g>
      {!doc && <path d={HAIR.patientTuft} fill={look.hair} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />}
      <circle r={R} fill={look.skin} stroke={INK} strokeWidth={SW} />
      {doc && <path d={HAIR.beard} transform={`translate(${ox * 0.6} 0)`} fill="#3B312B" stroke={INK} strokeWidth={5} strokeLinejoin="round" />}
      <path d={doc ? HAIR.doctor : HAIR.patient} fill={look.hair} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      {face.blush > 0 && eyes.map((x, i) => <ellipse key={i} cx={x + (i ? 10 : -10)} cy={24} rx={15} ry={9} fill="#F28C8C" opacity={0.55 * face.blush} />)}
      {eyes.map(eye)}
      {eyes.map((x, i) => {
        const s = i === 0 ? -1 : 1;
        const outer = {x: x + 16 * s, y: -36 + bo - br}, inner = {x: x - 14 * s, y: -36 + bi - br};
        return <path key={'b' + i} d={pts(outer, inner)} stroke={INK} strokeWidth={8} strokeLinecap="round" />;
      })}
      {doc && (
        <g fill="rgba(255,255,255,0.18)" stroke={INK} strokeWidth={5}>
          <circle cx={eyes[0]} cy={ey} r={24} /><circle cx={eyes[1]} cy={ey} r={24} />
          <path d={`M ${eyes[0] + 24} ${ey - 4} Q ${ox} ${ey - 12} ${eyes[1] - 24} ${ey - 4}`} fill="none" />
        </g>
      )}
      <g transform={`translate(${ox} ${my})`}>{mouth()}</g>
      {doc && <path d={HAIR.mustache} transform={`translate(${ox} ${my - 30})`} fill="#2A2421" stroke={INK} strokeWidth={3} />}
      {face.sweat > 0.05 && (
        <path
          d="M 0 -18 Q 11 0 0 9 Q -11 0 0 -18 Z"
          transform={`translate(${-ox * 0.5 + 76} ${-40 + ((t * 40) % 30)}) scale(${0.8 + 0.4 * face.sweat})`}
          fill="#9AD2F7" stroke={INK} strokeWidth={4} opacity={clamp(face.sweat * 1.5)}
        />
      )}
    </g>
  );
};

// ---------- hands & props ----------
const capsule = (a: Vec, b: Vec, w: number, fill: string) => (
  <g>
    <path d={pts(a, b)} stroke={INK} strokeWidth={w + 2 * 5} strokeLinecap="round" />
    <path d={pts(a, b)} stroke={fill} strokeWidth={w} strokeLinecap="round" />
  </g>
);
const HandG: React.FC<{p: Vec; ang: number; kind: Hand; skin: string; k?: number}> = ({p, ang, kind, skin, k: hk = 1}) => {
  const d = dir(ang);
  return (
    <g transform={`translate(${p.x} ${p.y}) scale(${hk}) translate(${-p.x} ${-p.y})`}>
      {kind === 'point' && capsule(p, add(p, d, 34), 11, skin)}
      {kind === 'up' && capsule(p, add(p, {x: 0, y: -1}, 34), 11, skin)}
      {kind === 'thumb' && capsule(add(p, {x: 4, y: -6}), add(p, {x: 4, y: -34}), 12, skin)}
      {kind === 'open' ? (
        <ellipse cx={p.x} cy={p.y} rx={17} ry={21} transform={`rotate(${-ang} ${p.x} ${p.y})`} fill={skin} stroke={INK} strokeWidth={5} />
      ) : (
        <circle cx={p.x} cy={p.y} r={kind === 'fist' ? 16 : 15} fill={skin} stroke={INK} strokeWidth={5} />
      )}
    </g>
  );
};

export const Magnifier: React.FC<{lens?: React.ReactNode; rot?: number}> = ({lens, rot = 0}) => (
  <g>
    <path d="M 0 0 L 0 -70" stroke={INK} strokeWidth={22} strokeLinecap="round" />
    <path d="M 0 0 L 0 -70" stroke="#8B5A2B" strokeWidth={12} strokeLinecap="round" />
    <g transform="translate(0 -140)">
      <clipPath id="lensClip"><circle r={66} /></clipPath>
      <circle r={66} fill="#EAF6FF" />
      <g clipPath="url(#lensClip)"><g transform={`rotate(${-rot})`}>{lens}</g></g>
      <circle r={66} fill="none" stroke={INK} strokeWidth={12} />
      <path d="M -40 -22 Q -34 -42 -14 -48" stroke="#fff" strokeWidth={8} fill="none" strokeLinecap="round" />
    </g>
  </g>
);

// ---------- the character ----------
type Props = {
  look: Look; x: number; y: number; s?: number; flip?: boolean; side?: boolean;
  pose: Pose; face: FaceName | Face; talk?: number; t: number;
  pain?: number; relief?: number; prop?: React.ReactNode | ((ang: number) => React.ReactNode); propAng?: number;
  aim?: Vec; aimLen?: number; // character-local point the prop tip (e.g. lens centre) should sit on
};

export const Character: React.FC<Props> = ({look, x, y, s = 1, flip, side = true, pose: po, face, talk = 0, t, pain = 0, relief = 0, prop, propAng, aim, aimLen = 140}) => {
  const L = look;
  const F: Face = typeof face === 'string' ? FACES[face] : face;
  const po2 = po as Pose & {sitW?: number; seatA?: number; seatB?: number};
  const sx = side ? 0 : L.legW * 0.8;
  const sgn = (i: number) => (side ? 1 : i === 0 ? 1 : -1);
  // legs relative to hip
  const legs = [
    {th: po.thighF, kn: po.kneeF},
    {th: po.thighB, kn: po.kneeB},
  ].map(({th, kn}, i) => {
    const g = sgn(i);
    const hip = {x: side ? (i === 0 ? 4 : -4) : g * sx, y: 0};
    const tw = g * th;
    const shinA = side ? th - kn : g * (th - kn * 0.15);
    const knee = add(hip, dir(tw), L.thigh * (side ? 1 : 1 - 0.55 * clamp(kn / 90)));
    const ankle = add(knee, dir(shinA), L.shin);
    return {hip, knee, ankle, shinA};
  });
  const standH = Math.max(legs[0].ankle.y, legs[1].ankle.y) + 18;
  const sitW = po2.sitW ?? (po.seat !== undefined ? 1 : 0);
  const seatVal = po.seat ?? po2.seatA;
  const hipY = -(seatVal !== undefined ? lerp(standH, seatVal, sitW) : standH) + (po.dy ?? 0);
  const off = {x: 0, y: hipY};
  const lg = legs.map((l) => ({hip: add(l.hip, off), knee: add(l.knee, off), ankle: add(l.ankle, off), shinA: l.shinA}));
  const hip = {x: 0, y: hipY};
  const groundY = Math.max(lg[0].ankle.y, lg[1].ankle.y);
  const lean = po.lean;
  let aimAng: number | undefined;
  const arms = [
    {a: po.armF, e: po.elbowF, hand: po.handF, reach: po.reachF, w: po.reachFW ?? 0},
    {a: po.armB, e: po.elbowB, hand: po.handB, reach: po.reachB, w: po.reachBW ?? 0},
  ].map(({a, e, hand, reach, w}, i) => {
    const g = sgn(i);
    const sh = side ? tl(hip, lean, i === 0 ? 6 : -6, -L.torso + 16) : tl(hip, lean, g * (L.halfW - 10), -L.torso + 26);
    if (i === 0 && aim) {
      const dd = Math.hypot(aim.x - sh.x, aim.y - sh.y) || 1;
      const u = {x: (aim.x - sh.x) / dd, y: (aim.y - sh.y) / dd};
      reach = add(sh, u, Math.min(dd - aimLen, (L.upper + L.fore) * 0.96));
      w = 1;
      aimAng = Math.atan2(u.x, -u.y) / D2R;
    }
    let el = add(sh, dir(g * a), L.upper);
    let ha = add(el, dir(g * (a + e)), L.fore);
    if (reach && w > 0) {
      // two-bone IK, elbow bends down/outward
      const dx = reach.x - sh.x, dy = reach.y - sh.y;
      const dist = Math.min(Math.hypot(dx, dy), L.upper + L.fore - 0.5);
      const base = Math.atan2(dy, dx);
      const cosA = (L.upper ** 2 + dist ** 2 - L.fore ** 2) / (2 * L.upper * dist);
      const A = Math.acos(clamp(cosA, -1, 1));
      const bend = side ? (reach.x > sh.x ? 1 : -1) : -g;
      const ang = base + bend * A;
      const el2 = {x: sh.x + L.upper * Math.cos(ang), y: sh.y + L.upper * Math.sin(ang)};
      const u = Math.hypot(reach.x - el2.x, reach.y - el2.y) || 1;
      const ha2 = {x: el2.x + ((reach.x - el2.x) / u) * L.fore, y: el2.y + ((reach.y - el2.y) / u) * L.fore};
      el = lerpV(el, el2, w);
      ha = lerpV(ha, ha2, w);
    }
    return {sh, el, ha, hand, ang: angOf(el, ha)};
  });

  const shade = (c: string) => (c === '#FFFFFF' ? '#E9ECEF' : c);
  const legG = (l: (typeof lg)[0], i: number) => {
    const back = side && i === 1;
    const d = dir(l.shinA);
    const n = {x: -d.y, y: d.x};
    const calf = add(add(l.knee, d, L.shin * 0.38), n, L.legW * 0.3);
    const skin = back ? '#DDAA80' : L.skin;
    const pantsLeg = L.id === 'doctor';
    const legColor = pantsLeg ? (back ? '#30343E' : L.bottom) : skin;
    const footRot = side ? clamp(-0.6 * l.shinA, -28, 28) * clamp((groundY - l.ankle.y) / 16) : 0;
    const shoe = side ? (
      <g transform={`translate(${l.ankle.x} ${l.ankle.y + 6}) rotate(${footRot}) scale(${1 + (L.legW - 32) / 80})`}>
        <path d="M -22 -12 Q -24 14 -10 14 L 44 14 Q 52 2 40 -8 Q 20 -14 6 -18 Z" fill={back ? shade(L.shoe) : L.shoe} stroke={INK} strokeWidth={5} strokeLinejoin="round" />
        <path d="M -16 10 L 44 10" stroke={L.sole} strokeWidth={5} strokeLinecap="round" />
      </g>
    ) : (
      <ellipse cx={l.ankle.x + (i === 0 ? 8 : -8)} cy={l.ankle.y + 10} rx={30} ry={15} fill={L.shoe} stroke={INK} strokeWidth={5} />
    );
    const legPath = pts(l.hip, l.knee, l.ankle);
    const calfE = (fill: string, stroke?: boolean) => (
      <ellipse cx={calf.x} cy={calf.y} rx={L.legW * 0.5} ry={L.shin * 0.31} transform={`rotate(${-l.shinA} ${calf.x} ${calf.y})`}
        fill={fill} stroke={stroke ? INK : 'none'} strokeWidth={stroke ? SW * 2 : 0} />
    );
    const thighEnd = add(l.hip, {x: l.knee.x - l.hip.x, y: l.knee.y - l.hip.y}, 0.62);
    const hipUp = add(l.hip, {x: 0, y: -26});
    const isFront = i === 0;
    return (
      <g key={'leg' + i}>
        <path d={legPath} stroke={INK} strokeWidth={L.legW + 2 * SW} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        {!pantsLeg && side && calfE(INK, true)}
        <path d={legPath} stroke={legColor} strokeWidth={L.legW} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        {!pantsLeg && side && calfE(skin)}
        {shoe}
        {isFront && pain > 0.01 && (
          <g>
            <ellipse cx={calf.x} cy={calf.y} rx={70} ry={100} transform={`rotate(${-l.shinA} ${calf.x} ${calf.y})`} fill="url(#painGlow)" opacity={clamp(pain)} />
            {[0, 1, 2, 3].map((j) => {
              const a = -150 + j * 34 + (side ? 0 : 0);
              const r0 = 34, r1 = 62 + 16 * pain * (0.6 + 0.4 * Math.sin(t * 22 + j * 1.7));
              const dd = {x: Math.cos(a * D2R), y: Math.sin(a * D2R)};
              const p0 = add(calf, dd, r0), p1 = add(calf, dd, r1);
              const mid = add(add(p0, dd, (r1 - r0) / 2), {x: -dd.y, y: dd.x}, 7);
              return <path key={j} d={pts(p0, mid, p1)} stroke={P.warning} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" fill="none" opacity={clamp(pain * 1.4 - 0.2)} />;
            })}
          </g>
        )}
        {isFront && relief > 0.01 && (
          <g opacity={clamp(relief)}>
            <ellipse cx={calf.x} cy={calf.y} rx={66} ry={96} transform={`rotate(${-l.shinA} ${calf.x} ${calf.y})`} fill="url(#reliefGlow)" />
            {[0, 1, 2].map((j) => {
              const a = (j * 120 + t * 90) * D2R;
              const c = add(calf, {x: Math.cos(a) * 64, y: Math.sin(a) * 84});
              const sz = 10 + 5 * Math.sin(t * 9 + j);
              return <path key={j} d={`M ${c.x} ${c.y - sz} Q ${c.x} ${c.y} ${c.x + sz} ${c.y} Q ${c.x} ${c.y} ${c.x} ${c.y + sz} Q ${c.x} ${c.y} ${c.x - sz} ${c.y} Q ${c.x} ${c.y} ${c.x} ${c.y - sz} Z`} fill={P.relief} stroke={INK} strokeWidth={2.5} />;
            })}
          </g>
        )}
        {!pantsLeg && (
          <g>
            <path d={pts(hipUp, thighEnd)} stroke={INK} strokeWidth={L.legW + 16 + 2 * SW} strokeLinecap="round" />
            <path d={pts(hipUp, thighEnd)} stroke={back ? '#283F68' : L.bottom} strokeWidth={L.legW + 16} strokeLinecap="round" />
          </g>
        )}
      </g>
    );
  };

  const armG = (a: (typeof arms)[0], i: number) => {
    const back = side && i === 1;
    const sleeve = L.id === 'doctor' ? 1 : 0.42;
    const sl = add(a.sh, {x: a.el.x - a.sh.x, y: a.el.y - a.sh.y}, sleeve);
    const sleevePath = L.id === 'doctor' ? pts(a.sh, a.el, add(a.el, {x: a.ha.x - a.el.x, y: a.ha.y - a.el.y}, 0.82)) : pts(a.sh, sl);
    const col = back ? shade(L.top) : L.top;
    const skin = back ? (L.id === 'doctor' ? '#A57250' : '#DDAA80') : L.skin;
    return (
      <g key={'arm' + i}>
        <path d={pts(a.sh, a.el, a.ha)} stroke={INK} strokeWidth={L.armW + 2 * SW} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        <path d={pts(a.sh, a.el, a.ha)} stroke={skin} strokeWidth={L.armW} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        <path d={sleevePath} stroke={INK} strokeWidth={L.armW + 12 + 2 * 5} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        <path d={sleevePath} stroke={col} strokeWidth={L.armW + 12} strokeLinecap="round" strokeLinejoin="round" fill="none" />
        <HandG p={a.ha} ang={a.ang} kind={a.hand} skin={skin} k={L.armW / 24} />
        {i === 0 && prop && <g transform={`translate(${a.ha.x} ${a.ha.y}) rotate(${aimAng ?? propAng ?? 0})`}>{typeof prop === 'function' ? prop(aimAng ?? propAng ?? 0) : prop}</g>}
      </g>
    );
  };

  const T = L.torso;
  const hw = side ? (L.id === 'doctor' ? 70 : 60) : L.halfW;
  const torso = (
    <g transform={`translate(${hip.x} ${hip.y}) rotate(${lean})`}>
      {L.id === 'doctor' ? (
        <g>
          <path d={`M ${-hw - 16} 136 L ${-hw + 2} ${-T + 40} Q ${-hw + 6} ${-T + 4} ${-hw + 34} ${-T + 2} Q 0 ${-T - 14} ${hw - 34} ${-T + 2} Q ${hw - 6} ${-T + 4} ${hw - 2} ${-T + 40} L ${hw + 16} 136 Z`} fill={L.top} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
          <path d={`M -30 ${-T + 8} L ${side ? 14 : 0} ${-T + 86} L 30 ${-T + 8} Z`} fill={P.doctorScrubs} stroke={INK} strokeWidth={5} strokeLinejoin="round" />
          <path d={`M -34 ${-T + 6} L ${side ? 8 : -6} ${-T + 120} M 34 ${-T + 6} L ${side ? 20 : 6} ${-T + 120} M ${side ? 14 : 0} ${-T + 92} L ${side ? 14 : 0} 128`} stroke={INK} strokeWidth={4} fill="none" strokeLinecap="round" />
          <path d={`M -40 ${-T + 12} C -50 ${-T + 80} -10 ${-T + 118} ${side ? 22 : 6} ${-T + 124} M 40 ${-T + 12} C 46 ${-T + 70} 30 ${-T + 104} ${side ? 22 : 6} ${-T + 124}`} stroke={INK} strokeWidth={10} fill="none" strokeLinecap="round" />
          <path d={`M -40 ${-T + 12} C -50 ${-T + 80} -10 ${-T + 118} ${side ? 22 : 6} ${-T + 124} M 40 ${-T + 12} C 46 ${-T + 70} 30 ${-T + 104} ${side ? 22 : 6} ${-T + 124}`} stroke="#5D6475" strokeWidth={5} fill="none" strokeLinecap="round" />
          <circle cx={side ? 22 : 6} cy={-T + 134} r={13} fill="#C9CFD8" stroke={INK} strokeWidth={5} />
          {!side && <rect x={34} y={-T + 116} width={36} height={24} rx={4} fill={P.doctorScrubs} stroke={INK} strokeWidth={4} />}
          {!side && <path d={`M -66 ${-T + 120} L -36 ${-T + 120} M -58 ${-T + 120} L -58 ${-T + 98}`} stroke={INK} strokeWidth={4} strokeLinecap="round" />}
          {!side && <path d={`M -58 ${-T + 120} L -58 ${-T + 98}`} stroke={P.oxygen} strokeWidth={3} />}
        </g>
      ) : (
        <path d={`M ${-hw} 16 C ${-hw - 8} -60 ${-hw - 10} -150 ${-hw + 14} ${-T + 22} Q 0 ${-T - 14} ${hw - 14} ${-T + 22} C ${hw + 10} -150 ${hw + 8} -60 ${hw} 16 Z`} fill={L.top} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      )}
    </g>
  );

  const neckBase = tl(hip, lean, 0, -T + 6);
  const headC = tl(hip, lean, 0, -T - L.headR + 18);
  const neck = pts(neckBase, headC);

  const order = side
    ? [armG(arms[1], 1), legG(lg[1], 1), legG(lg[0], 0)]
    : [legG(lg[1], 1), legG(lg[0], 0)];
  return (
    <g transform={`translate(${x} ${y}) scale(${flip ? -s : s} ${s})`}>
      {order}
      <path d={neck} stroke={INK} strokeWidth={32 + 2 * SW} strokeLinecap="round" />
      <path d={neck} stroke={L.skin} strokeWidth={32} strokeLinecap="round" />
      {torso}
      <g transform={`translate(${headC.x} ${headC.y}) rotate(${po.head + lean * 0.4})`}>
        <Head look={L} face={F} talk={talk} t={t} side={side} />
      </g>
      {side ? armG(arms[0], 0) : [armG(arms[1], 1), armG(arms[0], 0)]}
    </g>
  );
};

// Character-space helpers for scenes (calf point of the front leg in side view, at given pose).
export const calfPoint = (look: Look, po: Pose): Vec => {
  const tw = po.thighF, shinA = po.thighF - po.kneeF;
  const knee = add({x: 4, y: 0}, dir(tw), look.thigh);
  const ankle = add(knee, dir(shinA), look.shin);
  const ankB = add(add({x: -4, y: 0}, dir(po.thighB), look.thigh), dir(po.thighB - po.kneeB), look.shin);
  const standH = Math.max(ankle.y, ankB.y) + 18;
  // mirror Character's seat blending so the point is exact while poses are mixed
  const p2 = po as Pose & {sitW?: number; seatA?: number};
  const sitW = p2.sitW ?? (po.seat !== undefined ? 1 : 0), seatVal = po.seat ?? p2.seatA;
  const hipY = -(seatVal !== undefined ? lerp(standH, seatVal, sitW) : standH) + (po.dy ?? 0);
  const d = dir(shinA);
  return add(add({x: knee.x, y: knee.y + hipY}, d, look.shin * 0.38), {x: -d.y, y: d.x}, look.legW * 0.3);
};
