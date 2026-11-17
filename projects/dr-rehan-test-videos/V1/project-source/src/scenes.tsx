import React from 'react';
import {Easing} from 'remotion';
import {INK, P, SW, W, H, FONT, Vec, add, clamp, k, lerp, pop, speech, out} from './lib';
import {Character, PATIENT, DOCTOR, Pose, STAND, FRONT, SIT, walk, mix, pose, calfPoint, STRIDE_PX, FACES, Face, Magnifier} from './rig';
import {Cam, Park, Clinic, BOARD, BENCH_X, Dusk} from './env';
import {LegCutaway, CrossSection, Gauge, MuscleBuddy, ArteryTree, narrowPoint, muscleCenter} from './anatomy';
import {Label, Arrow, Circle, Bolt, Check, Warn, Clock, Paper, HeartIcon, BrainIcon, UpArrow, Foot} from './ui';

type SceneP = {t: number; f: number};
const lin = Easing.linear;
const outQ = Easing.out(Easing.quad);
const face = (name: keyof typeof FACES, o: Partial<Face> = {}): Face => ({...FACES[name], ...o});
const toScreen = (p: Vec, c: {x: number; y: number; z: number}): Vec => ({x: W / 2 + c.z * (p.x - c.x), y: H / 2 + c.z * (p.y - c.y)});

// ---------- shared poses ----------
const CLUTCH0 = pose(STAND, {lean: 44, head: 14, thighF: 88, kneeF: 124, thighB: -4, kneeB: 6, armB: 30, elbowB: 40});
const CLUTCH = pose(CLUTCH0, {reachF: add(calfPoint(PATIENT, CLUTCH0), {x: -6, y: 0}), reachFW: 1, reachB: {x: 150, y: -322}, reachBW: 1});
const SITRUB0 = pose(SIT, {lean: 50, head: 14});
const SIT_CALF = calfPoint(PATIENT, SITRUB0);
const SEAT_X = BENCH_X - 30;

// Doctor-local target (front view, scale s, at world x) for a world point.
const docLocal = (w: Vec, dx: number, s: number, flip = false): Vec => ({x: ((w.x - dx) / s) * (flip ? -1 : 1), y: w.y / s});

// ===================== S1 HOOK (0 – 4.27) =====================
const S1: React.FC<SceneP> = ({t}) => {
  const x = t < 1.3 ? 880 + 385 * t : k(t, [1.3, 1.95], [1380.5, 1500], outQ);
  const limp = k(t, [0.45, 1.2], [0, 1]);
  const W0 = walk((x - 880) / STRIDE_PX + 0.3, {limp, stride: lerp(22, 15, limp)});
  const clutch = pose(CLUTCH, {dy: -12 * Math.abs(Math.sin(t * 9))});
  const po = mix(mix(W0, clutch, k(t, [1.45, 1.75], [0, 1])), SIT, k(t, [2.05, 2.45], [0, 1]));
  const px = x + k(t, [2.05, 2.45], [0, SEAT_X - 1500]);
  const fc = t < 0.5 ? 'neutral' : t < 1.0 ? 'discomfort' : t < 2.45 ? 'pain' : t < 3.2 ? 'relief' : 'concern';
  const pain = k(t, [0.22, 0.5, 1.3, 2.25, 2.65], [0, 0.6, 1, 1, 0]) * (0.85 + 0.15 * Math.sin(t * 16));
  const relief = k(t, [2.35, 2.65, 3.3, 3.7], [0, 1, 1, 0]);
  const follow = k(t, [2.4, 3.4], [0, 1]);
  const cam = {x: lerp(x + 150, 1610, follow), y: k(t, [2.7, 4.27], [-430, -340]), z: k(t, [0, 2.7, 4.27], [0.8, 0.84, 1.16])};
  const calf = add(calfPoint(PATIENT, SIT), {x: SEAT_X, y: 0});
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} />
        <Character look={PATIENT} x={px} y={0} pose={po} face={face(fc as any, fc === 'concern' ? {look: 0.3} : {})} t={t} pain={pain} relief={relief} />
        <Circle t={t} t0={3.44} cx={calf.x} cy={calf.y} rx={95} ry={125} />
        <g transform={`translate(${SEAT_X + 70} -930) scale(${pop(t, 3.6)})`}>
          <text textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={150} fill="#fff" stroke={INK} strokeWidth={14} paintOrder="stroke">?</text>
        </g>
        {t > 2.55 && t < 3.3 && (
          <g opacity={k(t, [2.55, 2.75, 3.1, 3.3], [0, 1, 1, 0])} transform={`translate(${SEAT_X + 120} ${-720 - (t - 2.55) * 60})`}>
            <path d="M 0 0 q 30 -20 60 0 M 10 30 q 30 -20 60 0" stroke="#9BB8D6" strokeWidth={8} fill="none" strokeLinecap="round" />
          </g>
        )}
      </Cam>
      <Label t={t} at={0.22} until={1.62} x={540} y={340} size={124} color={P.warning}>CALF PAIN</Label>
      <Label t={t} at={0.66} until={1.62} x={540} y={460} size={76} mode="write">when walking</Label>
      <Label t={t} at={1.72} until={2.76} x={540} y={370} size={98} color={P.relief}>EASES WITH REST</Label>
      <Label t={t} at={2.82} x={540} y={330} size={76}>A PATTERN DOCTORS</Label>
      <Label t={t} at={3.44} x={540} y={455} size={118} color={P.warning}>DON'T IGNORE</Label>
    </g>
  );
};

// ===================== S2 DR. RAHIM ENTERS (4.27 – 5.90) =====================
const S2: React.FC<SceneP> = ({t}) => {
  const dx = lerp(2400, 2000, pop(t, 4.3, {damping: 13, stiffness: 140, mass: 0.8}));
  const wave = pose(FRONT, {armF: 150, elbowF: 18 + 26 * Math.sin(t * 15), handF: 'open', armB: 10});
  const gesture = pose(FRONT, {armB: 72, elbowB: 14, handB: 'open', armF: 12, elbowF: 10, head: -6});
  const dpo = mix(wave, gesture, k(t, [5.15, 5.45], [0, 1]));
  const pf = t < 4.5 ? face('concern') : t < 5.05 ? face('surprised') : face('neutral', {look: 1});
  const cam = {x: k(t, [4.27, 5.9], [1700, 1760]), y: -440, z: k(t, [4.27, 5.9], [0.98, 0.9])};
  const tag = pop(t, 4.74);
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} />
        <Character look={PATIENT} x={SEAT_X} y={0} pose={SIT} face={pf} t={t} />
        <Character look={DOCTOR} x={dx} y={0} side={false} pose={dpo} face={face('happy', {look: -0.6})} t={t} />
        <g transform={`translate(${dx - 10} -1000) scale(${tag * k(t, [5.0, 5.9], [1, 1.08])}) rotate(-3)`}>
          <rect x={-200} y={-62} width={400} height={112} rx={56} fill={P.doctorScrubs} stroke={INK} strokeWidth={SW + 2} />
          <text y={22} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={72} fill="#fff">Dr. Rahim</text>
        </g>
      </Cam>
    </g>
  );
};

// ===================== S3 CALF CLOSE-UP → LENS (5.90 – 10.30) =====================
const S3: React.FC<SceneP> = ({t}) => {
  const x = t < 8.75 ? 2400 + 300 * (t - 5.9) : k(t, [8.75, 9.3], [3255, 3337], outQ);
  const phase = (x - 2400) / 336 + 0.1;
  const W0 = walk(phase, {limp: 0.55, stride: 16});
  const po = mix(W0, STAND, k(t, [9.0, 9.4], [0, 1]));
  const strike = Math.pow(Math.max(0, Math.sin(2 * Math.PI * phase)), 2);
  const cramp = t > 6.56 && t < 7.5 ? 1 : 0;
  const pain = t < 9.15 ? 0.45 + 0.55 * strike * (cramp ? 1 : 0.75) : k(t, [9.15, 9.6], [0.75, 0]);
  const shake = cramp * Math.sin(t * 95) * 4;
  const cam = {x: x - 30, y: -215, z: k(t, [5.9, 8.4], [2.9, 3.25], lin)};
  const calfS = toScreen(add(calfPoint(PATIENT, po), {x, y: 0}), cam);
  // doctor's pointing arm slides in from the right edge (REVEAL_MOVE)
  const slide = 1 - k(t, [7.35, 7.8], [0, 1]);
  const hx = calfS.x + 105 + slide * 800, hy = calfS.y - 20;
  // lens reveal into the anatomy world
  const lensIn = pop(t, 9.62);
  const expand = k(t, [9.95, 10.3], [0, 1], Easing.in(Easing.cubic));
  const lc = {x: lerp(calfS.x, W / 2, expand), y: lerp(calfS.y, H / 2, expand)};
  const lr = lerp(190 * lensIn, 1250, expand);
  const zl = lerp(0.55, 0.75, expand);
  const lensCam = {x: muscleCenter.x - (lc.x - W / 2) / zl, y: muscleCenter.y - (lc.y - H / 2) / zl, z: zl};
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} />
        <Character look={PATIENT} x={x + shake} y={0} pose={po} face="discomfort" t={t} pain={pain} />
      </Cam>
      {slide < 1 && <PointingHand x={hx} y={hy} />}
      <g opacity={1 - expand}>
        <Label t={t} at={8.72} x={540} y={300} size={88} color={P.caution} mode="slide">INTERMITTENT</Label>
        <Label t={t} at={8.06} x={540} y={420} size={112} mode="write">CLAUDICATION</Label>
        <Label t={t} at={9.2} x={540} y={525} size={60} mode="write">= pain that comes &amp; goes</Label>
      </g>
      {lensIn > 0 && (
        <g>
          <clipPath id="lens3"><circle cx={lc.x} cy={lc.y} r={Math.max(1, lr)} /></clipPath>
          <g clipPath="url(#lens3)">
            <rect x={0} y={0} width={W} height={H} fill="#fff" />
            <Cam {...lensCam}><LegCutaway t={t} narrow={0.15} flow={1} o2={0.6} /></Cam>
          </g>
          <path d={`M ${lc.x + lr * 0.7} ${lc.y + lr * 0.7} L ${lc.x + lr * 1.25} ${lc.y + lr * 1.25}`} stroke={INK} strokeWidth={34} strokeLinecap="round" opacity={1 - expand} />
          <path d={`M ${lc.x + lr * 0.7} ${lc.y + lr * 0.7} L ${lc.x + lr * 1.25} ${lc.y + lr * 1.25}`} stroke="#8B5A2B" strokeWidth={20} strokeLinecap="round" opacity={1 - expand} />
          <circle cx={lc.x} cy={lc.y} r={lr} fill="none" stroke={INK} strokeWidth={16} />
        </g>
      )}
    </g>
  );
};

// Dr. Rahim's pointing hand (same white coat sleeve + skin tone as the rig), tip at (x, y).
const PointingHand: React.FC<{x: number; y: number}> = ({x, y}) => {
  const cap = (a: Vec, b: Vec, w: number, c: string) => (
    <g>
      <path d={`M ${a.x} ${a.y} L ${b.x} ${b.y}`} stroke={INK} strokeWidth={w + 16} strokeLinecap="round" />
      <path d={`M ${a.x} ${a.y} L ${b.x} ${b.y}`} stroke={c} strokeWidth={w} strokeLinecap="round" />
    </g>
  );
  return (
    <g>
      {cap({x: x + 760, y: y + 300}, {x: x + 230, y: y + 52}, 150, '#FFFFFF')}
      <path d={`M ${x + 262} ${y - 22} L ${x + 196} ${y + 120}`} stroke={INK} strokeWidth={8} strokeLinecap="round" />
      {cap({x: x + 200, y: y + 40}, {x: x + 130, y: y + 16}, 76, P.doctorSkin)}
      <ellipse cx={x + 96} cy={y + 14} rx={64} ry={52} fill={P.doctorSkin} stroke={INK} strokeWidth={8} />
      {cap({x: x + 70, y: y}, {x: x + 4, y: y - 2}, 30, P.doctorSkin)}
      {cap({x: x + 100, y: y - 28}, {x: x + 66, y: y - 46}, 26, P.doctorSkin)}
      <path d={`M ${x + 70} ${y + 30} q -18 10 0 22 M ${x + 92} ${y + 44} q -18 10 0 22`} stroke={INK} strokeWidth={6} fill="none" strokeLinecap="round" />
    </g>
  );
};

// ===================== S4 INSIDE THE LEG (10.30 – 13.62) =====================
const S4: React.FC<SceneP> = ({t}) => {
  const n = narrowPoint();
  const narrow = k(t, [10.45, 11.2], [0.15, 0.85]);
  const flow = k(t, [11.3, 12.0], [1, 0.38]);
  const cam = {
    x: k(t, [10.3, 10.45, 11.0, 11.6, 12.25, 12.3, 12.7], [muscleCenter.x, muscleCenter.x, n.x, n.x, -20, -20, -120]),
    y: k(t, [10.3, 10.45, 11.0, 11.6, 12.25, 12.3, 12.7], [muscleCenter.y, muscleCenter.y, n.y, n.y, 40, 40, -190]),
    z: k(t, [10.3, 10.45, 11.0, 11.6, 12.25, 12.3, 12.7], [0.75, 0.75, 1.7, 1.7, 1.15, 1.15, 0.82]),
  };
  const plaqueS = toScreen(n, cam);
  const muscleS = toScreen({x: muscleCenter.x - 40, y: muscleCenter.y}, cam);
  const glow = k(t, [12.38, 12.6], [0, 0.65]) * (0.75 + 0.25 * Math.sin(t * 10));
  const badge = pop(t, 12.8);
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      <Cam {...cam}>
        <LegCutaway t={t} narrow={narrow} flow={flow} o2={k(t, [11.3, 12.0], [0.7, 0.3])} muscleGlow={glow} pump={k(t, [12.8, 13.0], [0, 1])} />
      </Cam>
      <Label t={t} at={10.8} until={11.62} x={540} y={330} size={86}>NARROWED ARTERY</Label>
      {t > 10.9 && t < 11.62 && <Arrow t={t} t0={10.9} a={{x: 540, y: 380}} b={{x: plaqueS.x + 10, y: plaqueS.y - 90}} bend={0.15} />}
      <Label t={t} at={11.0} until={11.62} x={plaqueS.x + 250} y={plaqueS.y + 150} size={60} color={P.plaque}>plaque</Label>
      {t > 10.95 && t < 12.35 && (
        <g transform={`translate(830 1300) scale(${0.85 * pop(t, 10.95) * out(t, 12.1)})`}>
          <CrossSection narrow={narrow} t={t} />
          <text y={175} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={40} fill={INK}>cross-section</text>
        </g>
      )}
      <Label t={t} at={11.68} until={12.32} x={540} y={330} size={94} color={P.warning}>LESS BLOOD FLOW</Label>
      <Label t={t} at={12.38} x={540} y={330} size={94}>LEG MUSCLES</Label>
      {t > 12.45 && <Arrow t={t} t0={12.45} a={{x: 470, y: 390}} b={{x: muscleS.x + 30, y: muscleS.y - 200}} bend={-0.12} />}
      {badge > 0 && (
        <g transform={`translate(860 1250) scale(${badge})`}>
          <circle r={130} fill="#FFF7E0" stroke={INK} strokeWidth={SW} />
          <clipPath id="badgeClip"><circle r={124} /></clipPath>
          <g clipPath="url(#badgeClip)">
            <path d="M -130 92 L 130 92" stroke={INK} strokeWidth={5} />
            <Character look={PATIENT} x={0} y={92} s={0.24} pose={walk(t * 1.15)} face="discomfort" t={t} pain={0.8} />
          </g>
          <text y={190} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={48} fill="#fff" stroke={INK} strokeWidth={10} paintOrder="stroke">DURING ACTIVITY</text>
        </g>
      )}
    </g>
  );
};

// ===================== S5 LOW OXYGEN (13.62 – 15.68) =====================
const S5: React.FC<SceneP> = ({t}) => {
  const z = k(t, [13.62, 15.68], [1, 1.06], lin);
  const need = k(t, [13.9, 14.4], [0, 360]);
  const get = k(t, [14.1, 14.5], [0, 105]);
  const mood = t < 14.54 ? 'ok' : 'strain';
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      <g transform={`translate(540 960) scale(${z}) translate(-540 -960)`} filter="url(#boil)">
        {/* sparse oxygen arriving through the narrowed supply */}
        <path d="M -60 640 Q 120 600 210 700" stroke={INK} strokeWidth={70} fill="none" strokeLinecap="round" />
        <path d="M -60 640 Q 120 600 210 700" stroke={P.arteryWall} strokeWidth={56} fill="none" strokeLinecap="round" />
        <path d="M -60 640 Q 120 600 210 700" stroke="#B3202C" strokeWidth={30} fill="none" strokeLinecap="round" />
        <ellipse cx={90} cy={610} rx={40} ry={16} fill={P.plaque} stroke={INK} strokeWidth={4} transform="rotate(-8 90 610)" />
        <ellipse cx={100} cy={652} rx={40} ry={14} fill={P.plaque} stroke={INK} strokeWidth={4} transform="rotate(-8 100 652)" />
        {[0, 1, 2].map((i) => {
          const life = (t * 0.7 + i * 0.37) % 1;
          return (
            <g key={i} transform={`translate(${lerp(210, 330, life)} ${lerp(720, 900, life) + Math.sin(life * 7) * 12})`} opacity={Math.sin(life * Math.PI)}>
              <circle r={26} fill={P.oxygen} stroke={INK} strokeWidth={4} />
              <text y={9} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={26} fill="#fff">O₂</text>
            </g>
          );
        })}
        <g transform="translate(390 1030) scale(0.95)">
          <MuscleBuddy t={t} effort={1} mood={mood} sweat={k(t, [14.8, 15.1], [0, 1])} />
        </g>
        {/* demand vs supply */}
        <g transform="translate(0 0)">
          <path d="M 660 880 L 980 880" stroke={INK} strokeWidth={SW} strokeLinecap="round" />
          <rect x={690} y={880 - need} width={110} height={need} fill={P.oxygen} stroke={INK} strokeWidth={SW} />
          <rect x={840} y={880 - get} width={110} height={get} fill="#A9D2F5" stroke={INK} strokeWidth={SW} />
          <text x={745} y={940} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={44} fill={INK} opacity={need > 0 ? 1 : 0}>NEEDS</text>
          <text x={895} y={940} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={44} fill={INK} opacity={get > 0 ? 1 : 0}>GETS</text>
          <text x={820} y={460} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={50} fill={P.oxygen} opacity={need > 0 ? 1 : 0}>oxygen</text>
        </g>
        <g transform={`translate(800 1290) scale(${0.82 * pop(t, 14.3)})`}>
          <Gauge v={k(t, [13.62, 14.54, 15.3], [0.75, 0.72, 0.07])} label="O₂ level" low="LOW" />
        </g>
      </g>
      <Label t={t} at={15.2} x={540} y={330} size={104} color={P.warning}>LOW ON OXYGEN</Label>
      <Label t={t} at={13.7} until={15.15} x={540} y={330} size={80} mode="write">MUSCLES AT WORK</Label>
    </g>
  );
};

// ===================== S6 WALK → PAIN → REST → RELIEF loop (15.68 – 18.98) =====================
const CycleNode: React.FC<{t: number; at: number; x: number; label: string; color: string; active: boolean; children: React.ReactNode}> = ({t, at, x, label, color, active, children}) => {
  const s = pop(t, at);
  if (s <= 0) return null;
  return (
    <g transform={`translate(${x} 320) scale(${s})`}>
      <circle r={72} fill="#fff" stroke={active ? color : INK} strokeWidth={active ? 14 : SW} />
      {children}
      <text y={125} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={46} fill={active ? color : '#fff'} stroke={INK} strokeWidth={9} paintOrder="stroke">{label}</text>
    </g>
  );
};
const MiniBench: React.FC = () => (
  <g stroke={INK} strokeWidth={5} strokeLinejoin="round">
    <rect x={-40} y={-30} width={80} height={14} fill="#C98A50" />
    <rect x={-40} y={-4} width={80} height={14} fill="#D99A5E" />
    <path d="M -32 10 L -32 34 M 32 10 L 32 34" strokeWidth={8} />
  </g>
);
const S6: React.FC<SceneP> = ({t}) => {
  const u1 = k(t, [16.42, 16.8], [0, 1]);
  const x = t < 17.55 ? lerp(1440, SEAT_X, u1) : SEAT_X + 420 * (t - 17.55);
  const limp = k(t, [18.1, 18.6], [0, 1]);
  const W0 = walk((x - SEAT_X) / STRIDE_PX, {limp, stride: lerp(22, 16, limp)});
  const clutch = pose(CLUTCH, {dy: -12 * Math.abs(Math.sin(t * 9))});
  const po: Pose = t < 17.3 ? mix(clutch, SIT, u1) : mix(SIT, W0, k(t, [17.34, 17.62], [0, 1]));
  const pain = Math.max(k(t, [15.68, 16.5, 16.85], [1, 1, 0]), k(t, [18.1, 18.5], [0, 1])) * (0.85 + 0.15 * Math.sin(t * 16));
  const relief = k(t, [16.8, 17.0, 17.4, 17.62], [0, 1, 1, 0]);
  const fc = t < 16.8 ? 'pain' : t < 17.45 ? 'relief' : t < 18.15 ? 'neutral' : t < 18.45 ? 'discomfort' : 'pain';
  const cam = {x: lerp(1660, x + 140, k(t, [17.5, 18.3], [0, 1])), y: -380, z: 0.8};
  const state = t < 16.92 ? 0 : t < 17.05 ? 1 : t < 18.2 ? 2 : t < 18.5 ? 3 : 0;
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} />
        <Character look={PATIENT} x={x} y={0} pose={po} face={fc as any} t={t} pain={pain} relief={relief} />
      </Cam>
      {[[170, 400], [400, 630], [630, 860]].map(([a, b], i) => (
        <Arrow key={i} t={t} t0={[16.92, 17.05, 18.2][i]} t1={[16.92, 17.05, 18.2][i] + 0.2} a={{x: a + 80, y: 320}} b={{x: b - 80, y: 320}} w={7} />
      ))}
      <Arrow t={t} t0={18.4} t1={18.75} a={{x: 860, y: 470}} b={{x: 170, y: 470}} bend={-0.22} color={P.warning} w={8} />
      <CycleNode t={t} at={15.82} x={170} label="PAIN" color={P.warning} active={state === 0}><Bolt s={1.05} /></CycleNode>
      <CycleNode t={t} at={16.92} x={400} label="REST" color={P.caution} active={state === 1}><MiniBench /></CycleNode>
      <CycleNode t={t} at={17.05} x={630} label="RELIEF" color={P.relief} active={state === 2}><Check s={1.1} /></CycleNode>
      <CycleNode t={t} at={18.2} x={860} label="WALK" color={P.oxygen} active={state === 3}><Foot s={1.05} /></CycleNode>
    </g>
  );
};

// ===================== S7 PAD → CARDIOVASCULAR RISK (18.98 – 25.52) =====================
const BodyMap: React.FC<{t: number; draw: number; legPlaque: number; bodyPlaque: number; pulse: number; beat: number; pain?: number; fc?: Face}> = ({t, draw, legPlaque, bodyPlaque, pulse, beat, pain = 0, fc}) => (
  <g>
    <ellipse cx={0} cy={6} rx={170} ry={22} fill="#E8ECEF" />
    <Character look={PATIENT} x={0} y={0} side={false} pose={FRONT} face={fc ?? face('concern', {look: 0})} t={t} pain={pain} />
    {beat > 0 && <circle cx={22} cy={-430} r={90 + 20 * beat} fill="url(#heartGlow)" />}
    <ArteryTree draw={draw} legPlaque={legPlaque} bodyPlaque={bodyPlaque} pulse={pulse} />
    <g transform="translate(22 -430)"><HeartIcon s={0.42} beat={beat} /></g>
  </g>
);
const S7: React.FC<SceneP> = ({t}) => {
  if (t < 22.9) {
    const cam = {x: -40, y: -110, z: k(t, [18.98, 22.9], [0.58, 0.68], lin)};
    return (
      <g>
        <rect width={W} height={H} fill="#fff" />
        <Cam {...cam}>
          <LegCutaway t={t} narrow={0.85} flow={0.4} o2={0.35} spots={pop(t, 21.6)} muscleGlow={0.35 + 0.25 * Math.sin(t * 8)} pump={0.6} />
          {t > 20.0 && [0, 1, 2].map((i) => {
            const r = ((t - 20) * 420 + i * 140) % 420;
            return <circle key={i} cx={muscleCenter.x} cy={muscleCenter.y} r={120 + r} fill="none" stroke={P.caution} strokeWidth={12} opacity={(1 - r / 420) * 0.9} />;
          })}
        </Cam>
        <Label t={t} at={19.1} until={19.95} x={540} y={330} size={84} mode="write">THIS PATTERN...</Label>
        <Label t={t} at={20.0} until={21.3} x={540} y={330} size={92} color={P.caution}>KNOWN EARLY SIGNAL</Label>
        <Label t={t} at={21.4} x={540} y={320} size={78} mode="write">PERIPHERAL ARTERIAL</Label>
        <Label t={t} at={22.1} x={540} y={430} size={100} color={P.warning}>DISEASE (PAD)</Label>
      </g>
    );
  }
  const cam = {x: k(t, [22.9, 23.6], [25, 0]), y: k(t, [22.9, 23.6], [-190, -520]), z: k(t, [22.9, 23.6], [2.6, 1.2], Easing.out(Easing.cubic))};
  const beat = t > 24.3 ? 0.5 + 0.5 * Math.sin(t * 13) : 0;
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      <Cam {...cam}>
        <BodyMap t={t} draw={k(t, [22.95, 23.7], [0.25, 1])} legPlaque={1} bodyPlaque={pop(t, 24.4)} pulse={k(t, [23.5, 24.3], [0, 1], lin)} beat={beat} />
        {t > 24.44 && (
          <g>
            <path d="M 60 -640 Q 130 -700 150 -740" stroke={INK} strokeWidth={5} strokeDasharray="12 10" fill="none" opacity={pop(t, 24.6)} />
            <g transform={`translate(190 -780) scale(${0.6 * pop(t, 24.6)})`}><BrainIcon /></g>
            <g transform={`translate(200 -420) scale(${0.75 * pop(t, 24.5)})`}><UpArrow /></g>
          </g>
        )}
      </Cam>
      <Label t={t} at={23.1} until={24.3} x={540} y={330} size={86} mode="write">DIRECTLY CONNECTED</Label>
      <Label t={t} at={24.4} x={540} y={330} size={84} color={P.warning}>CARDIOVASCULAR RISK</Label>
      <Label t={t} at={24.6} x={540} y={425} size={52} mode="write">same artery disease, heart &amp; brain</Label>
    </g>
  );
};

// ===================== CLINIC BOARD (shared by S8, S9, S13) =====================
const LEFT_PANEL = {x: 25, y: 195, w: 365, h: 380};
const RIGHT_PANEL = {x: 410, y: 195, w: 365, h: 380};
const GROUND = 262;
const panelCenter = (p: typeof LEFT_PANEL): Vec => ({x: BOARD.x + p.x + p.w / 2, y: BOARD.y + p.y + p.h / 2});
const BoardContent: React.FC<{t: number; titles?: boolean}> = ({t, titles = true}) => {
  const lp = pop(t, 28.7), rp = pop(t, 31.7);
  const mini = (p: typeof LEFT_PANEL, s: number, child: React.ReactNode) => (
    <g transform={`translate(${p.x + p.w / 2} ${p.y + p.h / 2}) scale(${s}) translate(${-p.w / 2} ${-p.h / 2})`}>
      <rect x={0} y={0} width={p.w} height={p.h} rx={14} fill="#fff" stroke={INK} strokeWidth={SW} />
      <clipPath id={`pc${p.x}`}><rect x={4} y={4} width={p.w - 8} height={p.h - 8} rx={12} /></clipPath>
      <g clipPath={`url(#pc${p.x})`}>{child}</g>
    </g>
  );
  const dash = (t * 160) % 60;
  return (
    <g>
      {titles && <Label t={t} at={25.68} x={400} y={72} size={48} color={INK} stroke={0.01} mode="write">THE SIGNAL DOCTORS WATCH:</Label>}
      {titles && <Label t={t} at={27.6} x={400} y={158} size={80} color={P.warning} mode="write">CLAUDICATION</Label>}
      {lp > 0 && mini(LEFT_PANEL, lp, (
        <g>
          <path d={`M 0 ${GROUND} L 380 ${GROUND}`} stroke={INK} strokeWidth={5} />
          {[0, 1, 2, 3, 4, 5, 6, 7].map((i) => <path key={i} d={`M ${i * 60 - dash} ${GROUND + 16} l 30 0`} stroke="#BDBDB6" strokeWidth={5} strokeLinecap="round" />)}
          <Character look={PATIENT} x={182} y={GROUND} s={0.3} pose={walk(t * 1.1, {limp: 0.6, stride: 18})} face={t > 29.3 ? 'pain' : 'neutral'} t={t} pain={t > 29.3 ? 0.75 + 0.25 * Math.sin(t * 14) : 0} />
          <g transform="translate(310 66)"><Bolt s={0.8} /></g>
          <text x={182} y={318} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={44} fill={INK}>WALKING</text>
          <g opacity={k(t, [29.94, 30.1], [0, 1])}><text x={182} y={366} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={46} fill={P.warning}>= PAIN</text></g>
        </g>
      ))}
      {rp > 0 && mini(RIGHT_PANEL, rp, (
        <g>
          <path d={`M 0 ${GROUND} L 380 ${GROUND}`} stroke={INK} strokeWidth={5} />
          <g transform={`translate(168 ${GROUND}) scale(0.3)`}><g transform="translate(-1560 0)"><BenchLite /></g></g>
          <Character look={PATIENT} x={158} y={GROUND} s={0.3} pose={SIT} face="relief" t={t} relief={0.9} />
          <g transform="translate(310 66)"><Check s={0.8} /></g>
          <text x={182} y={318} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={44} fill={INK}>RESTING</text>
          <g opacity={k(t, [32.0, 32.15], [0, 1])}><text x={182} y={366} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={46} fill={P.relief}>= RELIEF</text></g>
        </g>
      ))}
    </g>
  );
};
// Bench drawn in its own world frame (reuses the park bench geometry).
import {Bench} from './env';
const BenchLite: React.FC = () => <Bench x={1560} />;

const DOC_X = 330, DOC_S = 0.95;
const S8: React.FC<SceneP> = ({t, f}) => {
  const talk = speech(f);
  const up = pose(FRONT, {armF: 38, elbowF: 112, handF: 'up', armB: 10});
  const explain = pose(FRONT, {armF: 30, elbowF: 76 + 10 * Math.sin(t * 6), handF: 'open', armB: 30, elbowB: 76 + 10 * Math.sin(t * 6 + 1), handB: 'open'});
  const lpW = panelCenter(LEFT_PANEL), rpW = panelCenter(RIGHT_PANEL);
  const pointL = pose(FRONT, {reachB: docLocal(lpW, DOC_X, DOC_S), reachBW: 1, handB: 'point', armF: 14, head: -5});
  const pointR = pose(FRONT, {reachB: docLocal(rpW, DOC_X, DOC_S), reachBW: 1, handB: 'point', armF: 14, head: -5});
  let po = mix(up, explain, k(t, [27.4, 27.8], [0, 1]));
  po = mix(po, pointL, k(t, [28.65, 29.0], [0, 1]));
  po = mix(po, pointR, k(t, [31.6, 31.95], [0, 1]));
  const medium = t < 27.55;
  const cam = medium
    ? {x: DOC_X - 40, y: -560, z: k(t, [25.52, 27.55], [1.42, 1.55], lin)}
    : {x: k(t, [28.6, 29.2], [-35, 0]), y: k(t, [28.6, 29.2], [-760, -1040]), z: k(t, [27.55, 28.6, 29.2], [0.98, 1.0, 1.08])};
  return (
    <g>
      <Cam {...cam}>
        <Clinic><BoardContent t={t} /></Clinic>
        <Character look={DOCTOR} x={DOC_X} y={0} s={DOC_S} side={false} pose={po} face={face('talk', {look: t > 28.65 ? -0.8 : 0.2})} talk={talk} t={t} />
      </Cam>
      {medium && <Label t={t} at={25.68} x={540} y={330} size={78}>THE SIGNAL DOCTORS</Label>}
      {medium && <Label t={t} at={26.45} x={540} y={445} size={100} color={P.caution}>WATCH MOST</Label>}
    </g>
  );
};

// ===================== S9 CLINICALLY SIGNIFICANT (32.92 – 35.92) =====================
const S9: React.FC<SceneP> = ({t, f}) => {
  if (t < 35.18) {
    const po = pose(FRONT, {armF: 38, elbowF: 112 + 6 * Math.sin(t * 7), handF: 'up', armB: 22, elbowB: 70, handB: 'open', head: 4 * Math.sin(t * 5)});
    const cam = {x: DOC_X, y: -540, z: k(t, [32.92, 35.18], [1.62, 1.8], lin)};
    return (
      <g>
        <Cam {...cam}><Clinic><BoardContent t={t} /></Clinic></Cam>
        <rect width={W} height={H} fill="#fff" opacity={0.6} />
        <Cam {...cam}>
          <Character look={DOCTOR} x={DOC_X} y={0} s={DOC_S} side={false} pose={po} face={face('serious', {look: 0})} talk={speech(f)} t={t} />
        </Cam>
        <Label t={t} at={33.1} x={540} y={320} size={70} mode="write">ONE OF THE MOST</Label>
        <Label t={t} at={34.28} x={540} y={430} size={92} color={P.caution}>CLINICALLY</Label>
        <Label t={t} at={34.6} x={540} y={540} size={92} color={P.caution}>SIGNIFICANT</Label>
      </g>
    );
  }
  const lpW = panelCenter(LEFT_PANEL);
  const cam = {x: lpW.x, y: lpW.y + 10, z: k(t, [35.18, 35.92], [1.8, 1.9], lin)};
  const calf = calfPoint(PATIENT, walk(t * 1.1, {limp: 0.6, stride: 18}));
  const cw = {x: lpW.x - LEFT_PANEL.w / 2 + 182 + calf.x * 0.3, y: lpW.y - LEFT_PANEL.h / 2 + GROUND + calf.y * 0.3};
  const st = pop(t, 35.22, {damping: 9, stiffness: 220, mass: 0.6});
  return (
    <g>
      <Cam {...cam}>
        <Clinic><BoardContent t={t} titles={false} /></Clinic>
        <Circle t={t} t0={35.25} cx={cw.x} cy={cw.y} rx={46} ry={60} w={7} />
      </Cam>
      {st > 0 && (
        <g transform={`translate(540 380) rotate(-7) scale(${lerp(1.35, 1, Math.min(1, st))})`} opacity={Math.min(1, st * 2)}>
          <rect x={-450} y={-78} width={900} height={140} rx={18} fill="#fff" stroke={P.warning} strokeWidth={12} />
          <text y={28} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={76} fill={P.warning}>EARLY WARNING SIGN</text>
        </g>
      )}
    </g>
  );
};

// ===================== S10 PAIN EVEN AT REST (35.92 – 42.55) =====================
const S10: React.FC<SceneP> = ({t, f}) => {
  const rub = add(SIT_CALF, {x: -8 + 10 * Math.sin(t * 9), y: 14 * Math.sin(t * 9)});
  const sitRub = pose(SITRUB0, {reachF: rub, reachFW: 1, reachB: add(SIT_CALF, {x: 6, y: -60}), reachBW: 1});
  const po = mix(sitRub, pose(SIT, {head: -4}), k(t, [38.2, 38.6], [0, 1]));
  const pfc = t < 38.3 ? face('concern', {look: 0.4}) : t < 39.4 ? face('pain') : t < 40.6 ? face('worried', {look: 0.2}) : face('concern', {look: 1});
  const pain = 0.85 + 0.12 * Math.sin(t * 2.6);
  const dxW = lerp(2420, 1960, pop(t, 40.0, {damping: 13, stiffness: 140, mass: 0.8}));
  const chin = {x: 34, y: -548};
  const dpo = mix(
    pose(FRONT, {reachF: chin, reachFW: 1, handF: 'fist', reachB: {x: 30, y: -430}, reachBW: 1, head: 6}),
    pose(FRONT, {armB: 70, elbowB: 16, handB: 'open', armF: 12, head: -4}),
    k(t, [41.4, 41.75], [0, 1]),
  );
  const cam = {
    x: k(t, [35.92, 39.3, 39.45, 40.0, 40.6], [1600, 1620, 1620, SEAT_X + 70, 1770]),
    y: k(t, [35.92, 39.3, 39.45, 40.0, 40.6], [-420, -430, -430, -700, -470]),
    z: k(t, [35.92, 39.3, 39.45, 40.0, 40.6], [0.95, 1.06, 1.06, 1.5, 0.86]),
  };
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} dusk={1} />
        <g transform={`translate(${BENCH_X + 250} -620) scale(${0.95 * pop(t, 38.4)})`}><Clock t={t} /></g>
        <Character look={PATIENT} x={SEAT_X} y={0} pose={po} face={pfc} t={t} pain={pain} />
        {t > 39.9 && <Character look={DOCTOR} x={dxW} y={0} side={false} pose={dpo} face={face('doctorConcern', {look: -0.7})} talk={speech(f)} t={t} />}
      </Cam>
      <Dusk v={1} />
      <Label t={t} at={36.2} until={39.9} x={540} y={300} size={56} color={P.relief} mode="write">usually: eases with rest</Label>
      {t > 37.35 && t < 40.2 && <path d={`M 230 284 L ${lerp(230, 850, k(t, [37.35, 37.7], [0, 1]))} 290`} stroke={P.warning} strokeWidth={10} strokeLinecap="round" opacity={out(t, 39.9)} />}
      <Label t={t} at={38.34} until={39.9} x={540} y={430} size={100} color={P.warning}>CONTINUOUS PAIN</Label>
      <Label t={t} at={39.4} until={39.9} x={540} y={545} size={88}>EVEN AT REST</Label>
      {t > 41.45 && <g transform={`translate(130 300) scale(${0.9 * pop(t, 41.45)})`}><Warn /></g>}
      <Label t={t} at={41.5} x={560} y={325} size={64} color={P.caution} mode="write">may signal severe</Label>
      <Label t={t} at={41.8} x={540} y={430} size={82}>BLOOD-FLOW LOSS</Label>
    </g>
  );
};

// ===================== S11 LOW FLOW, EVEN AT REST (42.55 – 50.62) =====================
const S11: React.FC<SceneP> = ({t, f}) => {
  const n = narrowPoint();
  const cam = {
    x: k(t, [42.55, 44.6, 45.4], [n.x, n.x, -60]),
    y: k(t, [42.55, 44.6, 45.4], [n.y, n.y, -60]),
    z: k(t, [42.55, 44.6, 45.4], [1.55, 1.68, 0.6]),
  };
  const dx = lerp(1300, 900, pop(t, 45.92, {damping: 13, stiffness: 140, mass: 0.8}));
  const dpo = pose(FRONT, {armB: 66, elbowB: 12 + 6 * Math.sin(t * 5), handB: 'open', armF: 12});
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      <Cam {...cam}>
        <LegCutaway t={t} narrow={1} flow={0.12} o2={0.12} spots={1} muscleGlow={0.3 + 0.2 * Math.sin(t * 3)} tired={pop(t, 49.45)} />
      </Cam>
      {t > 45.9 && <Character look={DOCTOR} x={dx} y={1830} s={0.62} side={false} pose={dpo} face={face('talk', {look: -0.8})} talk={speech(f)} t={t} />}
      {t > 45.95 && (
        <g transform={`translate(845 700) scale(${0.72 * pop(t, 46.0)})`}>
          <Gauge v={k(t, [46.0, 47.9, 48.8], [0.45, 0.45, 0.07])} label="blood flow" low="LOW" />
        </g>
      )}
      {t > 42.95 && t < 45.9 && <g transform={`translate(240 300) scale(${0.85 * pop(t, 43.0)})`}><Warn color={P.warning} /></g>}
      <Label t={t} at={43.02} until={45.9} x={600} y={340} size={112} color={P.warning}>SERIOUS</Label>
      <Label t={t} at={43.5} until={45.9} x={540} y={455} size={68} mode="write">PERSISTENT PAIN AT REST</Label>
      <Label t={t} at={44.0} until={45.9} x={540} y={545} size={54} color={P.caution} mode="write">→ seek prompt medical assessment</Label>
      <Label t={t} at={46.0} x={540} y={330} size={74} mode="write">ARTERIAL BLOOD FLOW</Label>
      <Label t={t} at={47.9} x={540} y={440} size={88} color={P.warning}>ALREADY REDUCED</Label>
      <Label t={t} at={49.45} x={540} y={540} size={64} mode="slide">→ muscles affected</Label>
    </g>
  );
};

// ===================== S12 RESEARCH → ELEVATED RISK (50.62 – 55.30) =====================
const S12: React.FC<SceneP> = ({t}) => {
  const cam = {x: -150, y: -520, z: k(t, [50.62, 55.3], [1.08, 1.16], lin)};
  const papersOut = k(t, [52.3, 52.7], [0, 1]);
  const beat = t > 53.7 ? 0.6 + 0.4 * Math.sin(t * 15) : 0.3 + 0.3 * Math.sin(t * 9);
  const arrowGrow = k(t, [53.98, 54.8], [0.4, 1.25], Easing.out(Easing.back(1.6)));
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      <Cam {...cam}>
        <BodyMap t={t} draw={1} legPlaque={1} bodyPlaque={1} pulse={0} beat={beat} pain={k(t, [52.4, 52.8], [0, 0.9])}
          fc={t < 53.9 ? face('concern', {look: 0}) : face('worried', {look: 0})} />
        {t > 53.98 && <g transform={`translate(210 -430) scale(0.75 ${0.75 * arrowGrow})`}><UpArrow /></g>}
        {t > 54.38 && <g transform={`translate(200 -790) scale(${0.6 * pop(t, 54.38)})`}><BrainIcon /></g>}
      </Cam>
      {[50.76, 51.22, 51.6].map((at, i) => {
        const s = pop(t, at);
        if (s <= 0 || papersOut >= 1) return null;
        return (
          <g key={i} transform={`translate(${200 - papersOut * 500 + i * 26} ${660 + i * 250}) rotate(${-6 + i * 5}) scale(${s})`}>
            <Paper checked={pop(t, 51.88 + i * 0.12)} />
          </g>
        );
      })}
      <Label t={t} at={50.76} until={52.3} x={540} y={330} size={92}>RESEARCH</Label>
      <Label t={t} at={51.88} until={52.3} x={540} y={430} size={60} color={P.relief} mode="write">consistently shows</Label>
      <Label t={t} at={52.36} until={55.3} x={540} y={320} size={64} mode="write">PEOPLE WITH CLAUDICATION</Label>
      <Label t={t} at={53.98} x={540} y={430} size={96} color={P.warning}>ELEVATED</Label>
      <Label t={t} at={54.38} x={540} y={530} size={70}>CARDIOVASCULAR RISK</Label>
    </g>
  );
};

// ===================== S13 ALWAYS INVESTIGATE (55.30 – 60.60) =====================
const S13: React.FC<SceneP> = ({t, f}) => {
  const PX_STOP = -300, DXF = 300, DS = 0.95;
  const x = t < 56.5 ? -900 + 420 * (t - 55.3) : k(t, [56.5, 56.9], [-396, PX_STOP], outQ);
  const W0 = walk((x + 900) / STRIDE_PX, {limp: 0.7, stride: 17});
  const calfL = calfPoint(PATIENT, STAND);
  const pointCalf = pose(STAND, {lean: 10, head: 10, reachF: add(calfL, {x: 40, y: -40}), reachFW: 0.85, handF: 'point'});
  let ppo = mix(W0, STAND, k(t, [56.6, 56.95], [0, 1]));
  ppo = mix(ppo, pointCalf, k(t, [57.5, 57.85], [0, 1]) * (1 - k(t, [58.9, 59.2], [0, 1])));
  const nod = t > 59.85 ? 6 * Math.sin((t - 59.85) * 14) : 0;
  ppo = pose(ppo, {head: ppo.head + nod});
  const pfc = t < 56.9 ? face('discomfort') : t < 59.8 ? face('concern', {look: 1}) : face('understanding', {look: 0.6});
  // doctor (side view, facing the patient)
  const calfW = add(calfL, {x: PX_STOP, y: 0});
  const lensLocal = docLocal(calfW, DXF, DS, true);
  const crouch0 = pose(STAND, {lean: 30, head: 12, thighF: 72, kneeF: 118, thighB: -22, kneeB: 84});
  const crouch = pose(crouch0, {reachF: add(lensLocal, {x: -150, y: 40}), reachFW: 1, handF: 'fist'});
  const raise = pose(STAND, {armF: 40, elbowF: 112, handF: 'up', head: 6 * Math.sin(t * 16) * k(t, [56.8, 57.0, 57.4, 57.6], [0, 1, 1, 0])});
  let dpo = mix(STAND, raise, k(t, [56.7, 57.0], [0, 1]));
  dpo = mix(dpo, crouch, k(t, [58.88, 59.35], [0, 1]));
  const mag = pop(t, 58.95);
  const n = narrowPoint();
  const cam = {x: k(t, [58.85, 59.5], [0, -60]), y: k(t, [58.85, 59.5], [-560, -420]), z: k(t, [55.3, 58.85, 59.5], [0.92, 0.98, 1.32])};
  const bump = t > 59.7 ? 1 + 0.18 * Math.max(0, 1 - (t - 59.7) / 0.25) : 1;
  return (
    <g>
      <Cam {...cam}><Clinic><BoardContent t={t} titles={false} /></Clinic></Cam>
      <rect width={W} height={H} fill="#fff" opacity={k(t, [58.85, 59.25], [0, 0.72])} />
      <Cam {...cam}>
        <Character look={PATIENT} x={x} y={0} pose={ppo} face={pfc} t={t} pain={t < 58.9 ? 0.55 + 0.25 * Math.sin(t * 14) : 0.4} />
        <Character look={DOCTOR} x={DXF} y={0} s={DS} flip pose={dpo} face={face(t < 56.7 ? 'happy' : 'talk', {look: 0.9})} talk={t < 56.7 ? 0 : speech(f)} t={t}
          prop={mag > 0 ? (
            <g transform={`scale(${mag})`}>
              <Magnifier lens={<g transform={`scale(-0.32 0.32) translate(${-n.x} ${-n.y})`}><LegCutaway t={t} narrow={0.9} flow={0.35} /></g>} />
            </g>
          ) : undefined} propAng={116} />
      </Cam>
      <Label t={t} at={56.76} until={58.85} x={540} y={330} size={104} color={P.warning}>DON'T DISMISS</Label>
      <Label t={t} at={57.58} until={58.85} x={540} y={440} size={66} mode="write">leg pain when walking</Label>
      <g transform={`translate(540 330) scale(${bump}) translate(-540 -330)`}>
        <Label t={t} at={59.0} x={540} y={330} size={96}>ALWAYS, ALWAYS</Label>
      </g>
      <Label t={t} at={59.82} x={540} y={455} size={118} color={P.warning}>INVESTIGATE</Label>
      <Label t={t} at={57.6} x={540} y={1440} size={42} mode="write">Not every cramp is PAD. A clinician can tell.</Label>
    </g>
  );
};

export const SCENES: [number, React.FC<SceneP>][] = [
  [0, S1], [4.27, S2], [5.9, S3], [10.3, S4], [13.62, S5], [15.68, S6], [18.98, S7],
  [25.52, S8], [32.92, S9], [35.92, S10], [42.55, S11], [50.62, S12], [55.3, S13],
];
