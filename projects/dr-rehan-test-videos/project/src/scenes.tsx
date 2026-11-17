import React from 'react';
import {Easing} from 'remotion';
import {INK, P, SW, W, H, FONT, CAP_FONT, Vec, add, clamp, k, lerp, pop, speech, out} from './lib';
import {Character, PATIENT, DOCTOR, Pose, STAND, FRONT, SIT, walk, mix, pose, calfPoint, FACES, Face, Magnifier} from './rig';
import {Cam, Park, Clinic, BOARD, BENCH_X, Bench} from './env';
import {LegCutaway, ArteryTree, FlowPanel, narrowPoint, muscleCenter} from './anatomy';
import {Label, Arrow, Circle, Bolt, Check, Warn, Clock, Paper, HeartIcon, BrainIcon, UpArrow, Foot} from './ui';

type SceneP = {t: number; f: number};
type CamT = {x: number; y: number; z: number};
const lin = Easing.linear;
const outQ = Easing.out(Easing.quad);
const outC = Easing.out(Easing.cubic);
const face = (name: keyof typeof FACES, o: Partial<Face> = {}): Face => ({...FACES[name], ...o});
const toScreen = (p: Vec, c: CamT): Vec => ({x: W / 2 + c.z * (p.x - c.x), y: H / 2 + c.z * (p.y - c.y)});
const frac = (x: number) => ((x % 1) + 1) % 1;

// Layout grammar (V2): labels live in the top band (y 250-560), the stage in y 560-1230, and narration
// captions in the low band (y 1265-1440) above the Shorts description area. Wide shots put the ground at GY.
const GY = 1225;
const gcam = (x: number, z: number, gy = GY): CamT => ({x, y: (H / 2 - gy) / z, z});
const lerpCam = (a: CamT, b: CamT, u: number): CamT => ({x: lerp(a.x, b.x, u), y: lerp(a.y, b.y, u), z: lerp(a.z, b.z, u)});
// Captions move to the top only on the clinic board, where the doctor and board fill the lower frame.
export const captionZone = (t: number): 'low' | 'high' => (t >= 25.52 && t < 35.92 ? 'high' : 'low');
// Pain pulse when the painful (front) leg is bearing weight.
const stance = (d: number, L: number) => {
  const f = frac(d / L);
  return f < 0.5 ? Math.sin((Math.PI * f) / 0.5) : 0;
};

// Two-colour "A → B" sticker label.
const Duo: React.FC<{t: number; at: number; until?: number; y: number; a: string; b: string; cb: string; size?: number}> = ({t, at, until = 1e9, y, a, b, cb, size = 92}) => {
  if (t < at || t > until) return null;
  const s = pop(t, at), o = clamp((until - t) / 0.2);
  return (
    <g opacity={o} transform={`translate(540 ${y}) scale(${s}) translate(-540 ${-y})`}>
      <text x={540} y={y} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={size} stroke={INK} strokeWidth={size * 0.16}
        strokeLinejoin="round" paintOrder="stroke" style={{whiteSpace: 'pre'}}>
        <tspan fill="#fff">{a}</tspan><tspan fill="#fff">{'  →  '}</tspan><tspan fill={cb}>{b}</tspan>
      </text>
    </g>
  );
};

// ---------- shared poses ----------
const CLUTCH0 = pose(STAND, {lean: 44, head: 14, thighF: 88, kneeF: 124, thighB: -4, kneeB: 6, armB: 30, elbowB: 40});
const CLUTCH = pose(CLUTCH0, {reachF: add(calfPoint(PATIENT, CLUTCH0), {x: -6, y: 0}), reachFW: 1, reachB: {x: 150, y: -322}, reachBW: 1});
const SITRUB0 = pose(SIT, {lean: 50, head: 14});
const SIT_CALF = calfPoint(PATIENT, SITRUB0);
const SEAT_X = BENCH_X - 30;
const CALF_SIT_W = add(calfPoint(PATIENT, SIT), {x: SEAT_X, y: 0});

// Doctor-local target (scale s, at world x) for a world point.
const docLocal = (w: Vec, dx: number, s: number, flip = false): Vec => ({x: ((w.x - dx) / s) * (flip ? -1 : 1), y: w.y / s});

// ===================== S1 HOOK + DR. REHAN OMAR (0 – 5.90), one continuous park shot =====================
const S1X = (t: number) => (t < 0.95 ? 980 + 360 * t : t < 1.45 ? k(t, [0.95, 1.4], [1322, 1346], outQ) : k(t, [1.45, 1.98], [1346, SEAT_X], lin));
const CALF_CAM: CamT = (() => {
  const c = add(calfPoint(PATIENT, CLUTCH), {x: 1340, y: 0});
  return {x: c.x + 30, y: c.y + 40, z: 1.85};
})();
const DOC_STOP = 2070;
const s1 = (t: number) => {
  const x = S1X(t);
  const limp = k(t, [0.15, 0.8], [0.35, 1]);
  const W0 = walk(x - 980, {L: 330, limp});
  const clutchW = k(t, [0.92, 1.1], [0, 1]) * (1 - k(t, [1.36, 1.5], [0, 1]));
  const clutch = pose(CLUTCH, {dy: -10 * Math.abs(Math.sin((t - 0.92) * 9))});
  const po = mix(mix(W0, clutch, clutchW), SIT, k(t, [1.95, 2.3], [0, 1]));
  let cam = gcam(x + 40, 1.15);
  cam = lerpCam(cam, CALF_CAM, k(t, [0.6, 1.25], [0, 1]));
  cam = lerpCam(cam, gcam(SEAT_X + 120, 1.0), k(t, [1.45, 2.2], [0, 1]));
  cam = lerpCam(cam, gcam(1800, 0.95), k(t, [2.4, 3.3], [0, 1]));
  if (t >= 4.27) cam = gcam(lerp(1850, 1880, k(t, [4.27, 5.9], [0, 1], lin)), k(t, [4.27, 5.9], [1.06, 1.13], lin));
  return {x, po, cam, limp};
};
const S1: React.FC<SceneP> = ({t, f}) => {
  const {x, po, cam} = s1(t);
  const pain = (t < 1.95 ? k(t, [0, 0.35, 0.9], [0.35, 0.65, 1]) * (0.8 + 0.2 * stance(x - 980, 330)) : k(t, [1.95, 2.5], [1, 0])) * (0.88 + 0.12 * Math.sin(t * 16));
  const relief = k(t, [2.2, 2.5, 3.2, 3.6], [0, 1, 1, 0]);
  const pf = t < 0.85 ? face('discomfort') : t < 2.15 ? face('pain') : t < 3.1 ? face('relief') : t < 4.27 ? face('concern', {look: 1}) : t < 4.9 ? face('surprised') : face('neutral', {look: 1});
  // doctor: walks in (side view) -> points at the calf -> cut -> front view, waves, badge
  const dx = k(t, [2.45, 3.3], [2420, DOC_STOP], Easing.out(Easing.sin));
  const dWalk = walk(2420 - dx, {look: DOCTOR, L: 380, arms: 12});
  const point = pose(STAND, {lean: 6, reachF: docLocal(add(CALF_SIT_W, {x: 30, y: -40}), DOC_STOP, 1, true), reachFW: 1, handF: 'point'});
  const dSide = mix(mix(dWalk, STAND, k(t, [3.2, 3.42], [0, 1])), point, k(t, [3.44, 3.7], [0, 1]) * (1 - k(t, [4.05, 4.25], [0, 1])));
  const wave = pose(FRONT, {armF: 150, elbowF: 18 + 26 * Math.sin(t * 15), handF: 'open', armB: 10});
  const gesture = pose(FRONT, {armB: 72, elbowB: 14, handB: 'open', armF: 12, elbowF: 10, head: -6});
  const front = t >= 4.27;
  const dpo = front ? mix(wave, gesture, k(t, [5.15, 5.45], [0, 1])) : dSide;
  const tag = pop(t, 4.74);
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} />
        <Character look={PATIENT} x={x} y={0} pose={po} face={pf} t={t} pain={pain} relief={relief} />
        {t > 2.45 && (
          <Character look={DOCTOR} x={dx} y={0} side={!front} flip={!front} pose={dpo}
            face={front ? face(t < 5.45 ? 'happy' : 'talk', {look: -0.6}) : face('concern', {look: 0.9})} talk={front && t > 5.45 ? speech(f) : 0} t={t} />
        )}
        {!front && <Circle t={t} t0={3.5} cx={CALF_SIT_W.x} cy={CALF_SIT_W.y} rx={92} ry={118} />}
      </Cam>
      <Label t={t} at={0.04} until={1.45} x={540} y={340} size={132} color={P.warning}>CALF PAIN</Label>
      <Label t={t} at={0.28} until={1.45} x={540} y={462} size={94} mode="write">WHEN WALKING?</Label>
      <Duo t={t} at={1.5} until={2.42} y={345} a="WALKING" b="PAIN" cb={P.warning} />
      <Duo t={t} at={1.98} until={2.42} y={460} a="REST" b="RELIEF" cb={P.relief} />
      <Label t={t} at={2.48} until={4.22} x={540} y={345} size={78}>WHY DO DOCTORS</Label>
      <Label t={t} at={2.64} until={4.22} x={540} y={445} size={84} color={P.caution}>NOTICE THIS?</Label>
      {tag > 0 && (
        <g transform={`translate(600 330) scale(${tag * k(t, [5.0, 5.9], [1, 1.05])}) rotate(-3)`}>
          <rect x={-300} y={-66} width={600} height={120} rx={60} fill={P.doctorScrubs} stroke={INK} strokeWidth={SW + 2} />
          <text y={22} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={76} fill="#fff">Dr. Rehan Omar</text>
        </g>
      )}
    </g>
  );
};

// ===================== S3 CALF CLOSE-UP → LENS (5.90 – 10.30) =====================
const s3 = (t: number) => {
  const x = t < 8.75 ? 2400 + 300 * (t - 5.9) : k(t, [8.75, 9.3], [3255, 3337], outQ);
  const po = mix(walk(x - 2400, {L: 300, limp: 0.55}), STAND, k(t, [9.0, 9.4], [0, 1]));
  const z = k(t, [5.9, 8.4], [2.9, 3.25], lin);
  return {x, po, cam: gcam(x - 30, z, 1190)};
};
const S3: React.FC<SceneP> = ({t}) => {
  const {x, po, cam} = s3(t);
  const cramp = t > 6.56 && t < 7.5 ? 1 : 0;
  const pain = t < 9.15 ? 0.45 + 0.55 * stance(x - 2400, 300) * (cramp ? 1 : 0.8) : k(t, [9.15, 9.6], [0.75, 0]);
  const shake = cramp * Math.sin(t * 95) * 4;
  const calfS = toScreen(add(calfPoint(PATIENT, po), {x, y: 0}), cam);
  const slide = 1 - k(t, [7.35, 7.8], [0, 1]);
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
      {slide < 1 && <PointingHand x={calfS.x + 105 + slide * 800} y={calfS.y - 20} />}
      <g opacity={1 - expand}>
        <Label t={t} at={8.06} x={540} y={450} size={114} mode="write">CLAUDICATION</Label>
        <Label t={t} at={8.72} x={540} y={335} size={86} color={P.caution} mode="slide">INTERMITTENT</Label>
        <Label t={t} at={9.2} x={540} y={545} size={60} mode="write">= pain that comes &amp; goes</Label>
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

// Dr. Rehan Omar's pointing hand (same white coat sleeve + skin tone as the rig), tip at (x, y).
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

// ===================== S4 MECHANISM: NORMAL vs NARROWED, then OXYGEN DEMAND (10.30 – 15.68) =====================
const CHIPS: [string, number, string][] = [['ARTERY', 10.42, P.arteryWall], ['NARROWING', 10.8, P.plaque], ['LESS FLOW', 11.68, '#F7A9A9'], ['LOW O₂', 14.78, '#A9D2F5']];
// The mechanism as one readable path, two rows: ARTERY → NARROWING / → LESS FLOW → LOW O₂.
const FlowPath: React.FC<{t: number}> = ({t}) => {
  const size = 54, wOf = (s: string) => s.length * size * 0.58 + 44, gap = 64;
  const on = CHIPS.filter((c) => t >= c[1]).length - 1;
  const rows = [CHIPS.slice(0, 2), CHIPS.slice(2)];
  return (
    <g>
      {rows.map((row, r) => {
        const y = 300 + r * 108;
        const total = row.reduce((n, c) => n + wOf(c[0]), 0) + gap * (row.length - 1) + (r ? gap : 0);
        let x = 540 - total / 2 + (r ? gap : 0);
        return row.map(([label, at, col], j) => {
          const i = r * 2 + j, w = wOf(label), cx = x + w / 2;
          x += w + gap;
          const s = pop(t, at);
          if (s <= 0) return null;
          const active = i === on;
          const ax = cx - w / 2 - 14;
          return (
            <g key={label}>
              {i > 0 && <path d={`M ${ax - gap + 26} ${y} L ${ax} ${y} M ${ax - 14} ${y - 13} L ${ax} ${y} L ${ax - 14} ${y + 13}`} stroke={INK} strokeWidth={8} fill="none" strokeLinecap="round" strokeLinejoin="round" opacity={s} />}
              <g transform={`translate(${cx} ${y}) scale(${s * (active ? 1.06 : 1)})`}>
                <rect x={-w / 2} y={-44} width={w} height={88} rx={44} fill={active ? col : '#fff'} stroke={INK} strokeWidth={active ? 8 : 5} />
                <text y={18} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={size} fill={INK}>{label}</text>
              </g>
            </g>
          );
        });
      })}
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
const StatusPill: React.FC<{t: number; at: number; until?: number; y?: number; label: string; color: string; children: React.ReactNode}> = ({t, at, until = 1e9, y = 535, label, color, children}) => {
  if (t < at || t > until) return null;
  const s = pop(t, at) * clamp((until - t) / 0.15);
  const w = Math.max(440, label.length * 28 + 190);
  return (
    <g transform={`translate(540 ${y}) scale(${s})`}>
      <rect x={-w / 2} y={-46} width={w} height={92} rx={46} fill="#fff" stroke={color} strokeWidth={8} />
      <g transform={`translate(${-w / 2 + 70} 6) scale(0.8)`}>{children}</g>
      <text x={50} y={18} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={50} fill={color} stroke={INK} strokeWidth={0}>{label}</text>
    </g>
  );
};
const PANEL_N = {x: 540, y: 750}, PANEL_X = {x: 540, y: 1068};
const DEMAND = [[-95, -70], [0, -88], [95, -66], [-105, 52], [5, 74], [105, 50]];
const S4: React.FC<SceneP> = ({t}) => {
  const n = narrowPoint();
  // A: inside the leg (continuity from the lens), find the artery and the plaque in its wall
  const leg = t < 11.42;
  const camA = {
    x: k(t, [10.3, 10.45, 10.95], [muscleCenter.x, muscleCenter.x, n.x]),
    y: k(t, [10.3, 10.45, 10.95], [muscleCenter.y, muscleCenter.y, n.y - 30]),
    z: k(t, [10.3, 10.45, 10.95, 11.2, 11.42], [0.75, 0.75, 1.55, 1.6, 2.6], Easing.inOut(Easing.quad)),
  };
  const plaqueS = toScreen(n, camA);
  // B/C: normal vs narrowed panels, then a selective zoom on the starving muscle
  const act = k(t, [12.8, 13.1], [0, 1]);
  const panelsIn = k(t, [11.25, 11.45], [0, 1]);
  const normalY = lerp(-720, 0, k(t, [11.62, 11.98], [0, 1], outC));
  const zu = k(t, [13.66, 14.2], [0, 1]);
  const mus = {x: PANEL_X.x + 330, y: PANEL_X.y + 28};
  const camB = {x: lerp(540, mus.x, zu), y: lerp(960, mus.y - 20, zu), z: lerp(1, 1.75, zu) * lerp(1.12, 1, panelsIn)};
  const starve = k(t, [15.2, 15.45], [0, 1]);
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      {leg && (
        <g opacity={1 - k(t, [11.28, 11.42], [0, 1])}>
          <Cam {...camA}><LegCutaway t={t} narrow={k(t, [10.5, 11.1], [0.2, 0.85])} flow={k(t, [10.9, 11.3], [1, 0.45])} o2={0.5} /></Cam>
          {t > 10.95 && t < 11.3 && <Arrow t={t} t0={10.95} t1={11.15} a={{x: 860, y: 1120}} b={{x: plaqueS.x + 70, y: plaqueS.y + 30}} bend={0.12} color={INK} w={8} />}
          <Label t={t} at={10.95} until={11.3} x={880} y={1190} size={62} color={P.plaque}>plaque</Label>
        </g>
      )}
      {panelsIn > 0 && (
        <g opacity={panelsIn}>
          <Cam {...camB}>
            <g transform={`translate(${PANEL_N.x} ${PANEL_N.y + normalY})`} opacity={1 - zu}>
              <FlowPanel t={t} narrow={0} activity={act} title="NORMAL ARTERY" titleColor={P.relief} h={306} o2={4 + Math.round(3 * act)} mood="ok" />
            </g>
            <g transform={`translate(${PANEL_X.x} ${PANEL_X.y})`}>
              <FlowPanel t={t} narrow={0.85} activity={act} title="NARROWED ARTERY" titleColor={P.warning} h={306} o2={2}
                mood={act > 0.5 ? 'strain' : 'ok'} pain={act * 0.45 + starve * 0.5} arrows={1 - zu} />
              {/* oxygen the working muscle NEEDS (dashed) vs what actually arrives (filled bubbles) */}
              {t > 13.95 && DEMAND.map(([dx, dy], i) => (
                <circle key={i} cx={330 + dx} cy={28 + dy} r={20 * pop(t, 14.0 + i * 0.07)} fill="none" stroke={P.oxygen} strokeWidth={5} strokeDasharray="8 7" />
              ))}
            </g>
            {t > 12.38 && t < 12.85 && <Circle t={t} t0={12.38} cx={mus.x} cy={mus.y} rx={200} ry={150} color={P.caution} w={8} />}
            {t > 12.38 && t < 12.85 && <Circle t={t} t0={12.45} cx={mus.x} cy={PANEL_N.y + 28} rx={200} ry={150} color={P.caution} w={8} />}
          </Cam>
          <StatusPill t={t} at={11.5} until={12.78} label="AT REST" color={P.relief}><MiniBench /></StatusPill>
          <StatusPill t={t} at={12.8} label="DURING ACTIVITY" color={P.caution}>
            <Character look={PATIENT} x={0} y={52} s={0.15} pose={walk(t * 330)} face="discomfort" t={t} />
          </StatusPill>
          <Label t={t} at={14.05} x={540} y={640} size={60} color={P.oxygen} mode="write">needs more O₂ than it gets</Label>
          {starve > 0 && <g transform={`translate(830 760) scale(${pop(t, 15.2)})`}><Bolt s={1.1} /></g>}
          <Label t={t} at={15.22} x={700} y={1185} size={70} color={P.warning}>→ PAIN</Label>
        </g>
      )}
      <FlowPath t={t} />
    </g>
  );
};

// ===================== S6 WALK → PAIN → REST → RELIEF loop (15.68 – 18.98) =====================
const CycleNode: React.FC<{t: number; at: number; x: number; label: string; color: string; active: boolean; children: React.ReactNode}> = ({t, at, x, label, color, active, children}) => {
  const s = pop(t, at);
  if (s <= 0) return null;
  return (
    <g transform={`translate(${x} 320) scale(${s * (active ? 1.08 : 1)})`}>
      <circle r={72} fill="#fff" stroke={active ? color : INK} strokeWidth={active ? 14 : SW} />
      {children}
      <text y={130} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={52} fill={active ? color : '#fff'} stroke={INK} strokeWidth={10} paintOrder="stroke">{label}</text>
    </g>
  );
};
const s6 = (t: number) => {
  const u1 = k(t, [16.42, 16.8], [0, 1]);
  const x = t < 17.55 ? lerp(1440, SEAT_X, u1) : SEAT_X + 360 * (t - 17.55);
  const limp = k(t, [18.05, 18.5], [0, 1]);
  const W0 = walk(x - SEAT_X, {L: 330, limp});
  const clutch = pose(CLUTCH, {dy: -10 * Math.abs(Math.sin(t * 9))});
  const po: Pose = t < 17.3 ? mix(clutch, SIT, u1) : mix(SIT, W0, k(t, [17.34, 17.62], [0, 1]));
  return {x, po, cam: gcam(lerp(1640, x + 140, k(t, [17.5, 18.3], [0, 1])), 1.0)};
};
const S6: React.FC<SceneP> = ({t}) => {
  const {x, po, cam} = s6(t);
  const pain = Math.max(k(t, [15.68, 16.5, 16.85], [1, 1, 0]), k(t, [18.05, 18.45], [0, 1])) * (0.85 + 0.15 * Math.sin(t * 16));
  const relief = k(t, [16.8, 17.0, 17.4, 17.62], [0, 1, 1, 0]);
  const fc = t < 16.8 ? 'pain' : t < 17.45 ? 'relief' : t < 18.1 ? 'neutral' : t < 18.4 ? 'discomfort' : 'pain';
  const state = t < 16.92 ? 0 : t < 17.05 ? 1 : t < 18.2 ? 2 : t < 18.5 ? 3 : 0;
  return (
    <g>
      <Cam {...cam}>
        <Park camX={cam.x} />
        <Character look={PATIENT} x={x} y={0} pose={po} face={fc as keyof typeof FACES} t={t} pain={pain} relief={relief} />
      </Cam>
      {[[170, 400], [400, 630], [630, 860]].map(([a, b], i) => (
        <Arrow key={i} t={t} t0={[16.92, 17.05, 18.2][i]} t1={[16.92, 17.05, 18.2][i] + 0.2} a={{x: a + 80, y: 320}} b={{x: b - 80, y: 320}} w={7} />
      ))}
      <Arrow t={t} t0={18.4} t1={18.75} a={{x: 860, y: 490}} b={{x: 170, y: 490}} bend={-0.18} color={P.warning} w={8} />
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
const s7cam = (t: number): CamT => ({x: -40, y: -40, z: k(t, [18.98, 22.9], [0.62, 0.7], lin)});
const S7: React.FC<SceneP> = ({t}) => {
  if (t < 22.9) {
    return (
      <g>
        <rect width={W} height={H} fill="#fff" />
        <Cam {...s7cam(t)}>
          <LegCutaway t={t} narrow={0.85} flow={0.4} o2={0.35} spots={pop(t, 21.6)} muscleGlow={0.35 + 0.25 * Math.sin(t * 8)} pump={0.6} />
          {t > 20.0 && [0, 1, 2].map((i) => {
            const r = ((t - 20) * 420 + i * 140) % 420;
            return <circle key={i} cx={muscleCenter.x} cy={muscleCenter.y} r={120 + r} fill="none" stroke={P.caution} strokeWidth={12} opacity={(1 - r / 420) * 0.9} />;
          })}
        </Cam>
        <Label t={t} at={20.0} until={21.3} x={540} y={340} size={84} color={P.caution}>KNOWN EARLY SIGNAL</Label>
        <Label t={t} at={21.4} x={540} y={330} size={80} mode="write">PERIPHERAL ARTERIAL</Label>
        <Label t={t} at={22.1} x={540} y={445} size={104} color={P.warning}>DISEASE (PAD)</Label>
      </g>
    );
  }
  const u = k(t, [22.9, 23.6], [0, 1], outC);
  const cam = {x: lerp(25, 0, u), y: lerp(-190, -270, u), z: lerp(2.6, 1.0, u)};
  const beat = t > 24.3 ? 0.5 + 0.5 * Math.sin(t * 13) : 0;
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      <Cam {...cam}>
        <BodyMap t={t} draw={k(t, [22.95, 23.7], [0.25, 1])} legPlaque={1} bodyPlaque={pop(t, 24.4)} pulse={k(t, [23.5, 24.3], [0, 1], lin)} beat={beat} />
        {t > 24.44 && (
          <g>
            <path d="M 70 -610 Q 140 -650 160 -660" stroke={INK} strokeWidth={5} strokeDasharray="12 10" fill="none" opacity={pop(t, 24.6)} />
            <g transform={`translate(225 -660) scale(${0.62 * pop(t, 24.6)})`}><BrainIcon /></g>
            <g transform={`translate(215 -420) scale(${0.7 * pop(t, 24.5)})`}><UpArrow /></g>
          </g>
        )}
      </Cam>
      <Label t={t} at={23.1} until={24.3} x={540} y={340} size={90} mode="write">DIRECTLY CONNECTED</Label>
      <Label t={t} at={24.4} x={540} y={335} size={88} color={P.warning}>CARDIOVASCULAR RISK</Label>
      <Label t={t} at={24.6} x={540} y={440} size={56} mode="write">same artery disease → heart &amp; brain</Label>
    </g>
  );
};

// ===================== CLINIC BOARD (shared by S8, S9, S13) =====================
const LEFT_PANEL = {x: 25, y: 170, w: 365, h: 410};
const RIGHT_PANEL = {x: 410, y: 170, w: 365, h: 410};
const GROUND = 282;
const panelCenter = (p: typeof LEFT_PANEL): Vec => ({x: BOARD.x + p.x + p.w / 2, y: BOARD.y + p.y + p.h / 2});
const BenchLite: React.FC = () => <Bench x={1560} />;
const BoardContent: React.FC<{t: number; titles?: boolean}> = ({t, titles = true}) => {
  const lp = pop(t, 28.7), rp = pop(t, 31.7);
  const mini = (p: typeof LEFT_PANEL, s: number, child: React.ReactNode) => (
    <g transform={`translate(${p.x + p.w / 2} ${p.y + p.h / 2}) scale(${s}) translate(${-p.w / 2} ${-p.h / 2})`}>
      <rect x={0} y={0} width={p.w} height={p.h} rx={14} fill="#fff" stroke={INK} strokeWidth={SW} />
      <clipPath id={`pc${p.x}`}><rect x={4} y={4} width={p.w - 8} height={p.h - 8} rx={12} /></clipPath>
      <g clipPath={`url(#pc${p.x})`}>{child}</g>
    </g>
  );
  const d = t * 330; // treadmill: ground scrolls at exactly the walk speed (s 0.3)
  return (
    <g>
      {titles && <Label t={t} at={27.6} x={400} y={128} size={104} color={P.warning} mode="write">CLAUDICATION</Label>}
      {lp > 0 && mini(LEFT_PANEL, lp, (
        <g>
          <path d={`M 0 ${GROUND} L 380 ${GROUND}`} stroke={INK} strokeWidth={5} />
          {[0, 1, 2, 3, 4, 5, 6, 7].map((i) => <path key={i} d={`M ${i * 60 - ((d * 0.3) % 60)} ${GROUND + 16} l 30 0`} stroke="#BDBDB6" strokeWidth={5} strokeLinecap="round" />)}
          <Character look={PATIENT} x={182} y={GROUND} s={0.3} pose={walk(d, {limp: 0.6})} face={t > 29.3 ? 'pain' : 'neutral'} t={t} pain={t > 29.3 ? 0.75 + 0.25 * Math.sin(t * 14) : 0} />
          <g transform="translate(312 64)"><Bolt s={0.8} /></g>
          <text x={182} y={342} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={54} fill={INK}>WALKING</text>
          <g opacity={k(t, [29.94, 30.1], [0, 1])}><text x={182} y={394} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={56} fill={P.warning}>= PAIN</text></g>
        </g>
      ))}
      {rp > 0 && mini(RIGHT_PANEL, rp, (
        <g>
          <path d={`M 0 ${GROUND} L 380 ${GROUND}`} stroke={INK} strokeWidth={5} />
          <g transform={`translate(168 ${GROUND}) scale(0.3)`}><g transform="translate(-1560 0)"><BenchLite /></g></g>
          <Character look={PATIENT} x={158} y={GROUND} s={0.3} pose={SIT} face="relief" t={t} relief={0.9} />
          <g transform="translate(312 64)"><Check s={0.8} /></g>
          <text x={182} y={342} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={54} fill={INK}>RESTING</text>
          <g opacity={k(t, [32.0, 32.15], [0, 1])}><text x={182} y={394} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={56} fill={P.relief}>= RELIEF</text></g>
        </g>
      ))}
    </g>
  );
};

const DOC_X = 410, DOC_S = 0.92;
const S8: React.FC<SceneP> = ({t, f}) => {
  const up = pose(FRONT, {armF: 38, elbowF: 112, handF: 'up', armB: 10});
  const explain = pose(FRONT, {armF: 30, elbowF: 76 + 10 * Math.sin(t * 6), handF: 'open', armB: 30, elbowB: 76 + 10 * Math.sin(t * 6 + 1), handB: 'open'});
  const pointL = pose(FRONT, {reachB: docLocal(panelCenter(LEFT_PANEL), DOC_X, DOC_S), reachBW: 1, handB: 'point', armF: 14, head: -5});
  const pointR = pose(FRONT, {reachB: docLocal(panelCenter(RIGHT_PANEL), DOC_X, DOC_S), reachBW: 1, handB: 'point', armF: 14, head: -5});
  let po = mix(up, explain, k(t, [27.4, 27.8], [0, 1]));
  po = mix(po, pointL, k(t, [28.65, 29.0], [0, 1]));
  po = mix(po, pointR, k(t, [31.6, 31.95], [0, 1]));
  // cut-then-zoom: medium on the doctor, then the whole board WITH the doctor in frame (never cropped)
  const cam = t < 27.55 ? {x: DOC_X - 30, y: -560, z: k(t, [25.52, 27.55], [1.42, 1.52], lin)} : {x: -30, y: -640, z: k(t, [27.55, 32.92], [0.96, 0.99], lin)};
  return (
    <Cam {...cam}>
      <Clinic><BoardContent t={t} /></Clinic>
      <Character look={DOCTOR} x={DOC_X} y={0} s={DOC_S} side={false} pose={po} face={face('talk', {look: t > 28.65 ? -0.8 : 0.2})} talk={speech(f)} t={t} />
    </Cam>
  );
};

// ===================== S9 CLINICALLY SIGNIFICANT (32.92 – 35.92) =====================
const S9: React.FC<SceneP> = ({t, f}) => {
  if (t < 35.18) {
    const po = pose(FRONT, {armF: 38, elbowF: 112 + 6 * Math.sin(t * 7), handF: 'up', armB: 22, elbowB: 70, handB: 'open', head: 4 * Math.sin(t * 5)});
    const cam = {x: DOC_X, y: -560, z: k(t, [32.92, 35.18], [1.62, 1.8], lin)};
    return (
      <g>
        <Cam {...cam}><Clinic><BoardContent t={t} /></Clinic></Cam>
        <rect width={W} height={H} fill="#fff" opacity={0.6} />
        <Cam {...cam}>
          <Character look={DOCTOR} x={DOC_X} y={0} s={DOC_S} side={false} pose={po} face={face('serious', {look: 0})} talk={speech(f)} t={t} />
        </Cam>
        <Label t={t} at={34.28} x={540} y={1300} size={96} color={P.caution}>CLINICALLY</Label>
        <Label t={t} at={34.6} x={540} y={1410} size={96} color={P.caution}>SIGNIFICANT</Label>
      </g>
    );
  }
  const lpW = panelCenter(LEFT_PANEL);
  const cam = {x: lpW.x, y: lpW.y + 10, z: k(t, [35.18, 35.92], [1.8, 1.9], lin)};
  const calf = calfPoint(PATIENT, walk(t * 330, {limp: 0.6}));
  const cw = {x: lpW.x - LEFT_PANEL.w / 2 + 182 + calf.x * 0.3, y: lpW.y - LEFT_PANEL.h / 2 + GROUND + calf.y * 0.3};
  const st = pop(t, 35.22, {damping: 9, stiffness: 220, mass: 0.6});
  return (
    <g>
      <Cam {...cam}>
        <Clinic><BoardContent t={t} titles={false} /></Clinic>
        <Circle t={t} t0={35.25} cx={cw.x} cy={cw.y} rx={46} ry={60} w={7} />
      </Cam>
      {st > 0 && (
        <g transform={`translate(540 1330) rotate(-6) scale(${lerp(1.35, 1, Math.min(1, st))})`} opacity={Math.min(1, st * 2)}>
          <rect x={-450} y={-78} width={900} height={140} rx={18} fill="#fff" stroke={P.warning} strokeWidth={12} />
          <text y={28} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={76} fill={P.warning}>EARLY WARNING SIGN</text>
        </g>
      )}
    </g>
  );
};

// ===================== S10 PAIN DURING WALKING vs PAIN EVEN AT REST (35.92 – 42.55) =====================
type Rect = {x: number; y: number; w: number; h: number};
const Panel: React.FC<{r: Rect; cam: CamT; id: string; rx?: number; border?: string; bw?: number; dim?: number; children: React.ReactNode}> = ({r, cam, id, rx = 24, border = INK, bw = SW, dim = 0, children}) => (
  <g>
    <clipPath id={id}><rect x={r.x} y={r.y} width={r.w} height={r.h} rx={rx} /></clipPath>
    <g clipPath={`url(#${id})`}>
      <rect x={r.x} y={r.y} width={r.w} height={r.h} fill="#fff" />
      <g filter="url(#boil)"><g transform={`translate(${r.x + r.w / 2} ${r.y + r.h / 2}) scale(${cam.z}) translate(${-cam.x} ${-cam.y})`}>{children}</g></g>
      {dim > 0 && <rect x={r.x} y={r.y} width={r.w} height={r.h} fill="#fff" opacity={dim} />}
    </g>
    {bw > 0 && <rect x={r.x} y={r.y} width={r.w} height={r.h} rx={rx} fill="none" stroke={border} strokeWidth={bw} />}
  </g>
);
const PZ = 0.68;
const panelCam = (x: number, r: Rect, z = PZ): CamT => ({x, y: -(r.h / 2 - 100) / z, z});
const L_R: Rect = {x: 18, y: 545, w: 510, h: 690}, R_R: Rect = {x: 552, y: 545, w: 510, h: 690};
const DOC_REST = 1990;
const s10 = (t: number) => {
  const ex = k(t, [39.98, 40.45], [0, 1], Easing.inOut(Easing.cubic));
  const r: Rect = {x: lerp(lerp(1100, R_R.x, k(t, [37.3, 37.65], [0, 1], outC)), 0, ex), y: lerp(R_R.y, 0, ex), w: lerp(R_R.w, W, ex), h: lerp(R_R.h, H, ex)};
  const full = lerpCam(gcam(1700, 0.95), gcam(1770, 0.9), k(t, [40.45, 41.2], [0, 1]));
  const cam = lerpCam(panelCam(SEAT_X + 60, r), full, ex);
  const rub = add(SIT_CALF, {x: -8 + 10 * Math.sin(t * 9), y: 14 * Math.sin(t * 9)});
  const sitRub = pose(SITRUB0, {reachF: rub, reachFW: 1, reachB: add(SIT_CALF, {x: 6, y: -60}), reachBW: 1});
  const po = mix(sitRub, pose(SIT, {head: -4}), k(t, [39.0, 39.4], [0, 1]));
  return {r, cam, ex, po};
};
const S10: React.FC<SceneP> = ({t, f}) => {
  const {r, cam, ex, po} = s10(t);
  const lx = 1000 + 300 * (t - 35.92);
  const lpain = 0.45 + 0.55 * stance(lx - 1000, 330);
  const pfc = t < 39.0 ? face('pain') : t < 40.6 ? face('worried', {look: 0.2}) : face('concern', {look: 1});
  const dx = k(t, [40.1, 40.8], [2330, DOC_REST], Easing.out(Easing.sin));
  const dWalk = walk(2330 - dx, {look: DOCTOR, L: 380, arms: 12});
  const explain = pose(STAND, {lean: 4, reachF: docLocal(add(CALF_SIT_W, {x: 40, y: -150}), DOC_REST, 1, true), reachFW: 0.85, handF: 'open'});
  const dpo = mix(mix(dWalk, STAND, k(t, [40.7, 40.9], [0, 1])), explain, k(t, [41.4, 41.75], [0, 1]));
  const hdr = 1 - k(t, [39.98, 40.2], [0, 1]);
  const restBorder = t > 38.34 ? P.warning : INK;
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      {ex < 1 && (
        <g opacity={hdr}>
          <Panel r={L_R} cam={panelCam(lx + 30, L_R)} id="pWalk" dim={k(t, [38.34, 38.6], [0, 0.45])} border={P.caution} bw={10}>
            <Park camX={lx} />
            <Character look={PATIENT} x={lx} y={0} pose={walk(lx - 1000, {L: 330, limp: 0.6})} face="discomfort" t={t} pain={lpain} />
          </Panel>
          <Label t={t} at={35.98} x={273} y={400} size={62} color={P.caution}>PAIN DURING</Label>
          <Label t={t} at={36.1} x={273} y={478} size={62} color={P.caution}>WALKING</Label>
          <Label t={t} at={36.5} x={273} y={622} size={40} color={P.relief} stroke={7}>eases with rest ✓</Label>
          <Label t={t} at={37.35} x={807} y={400} size={62} color={P.warning}>PAIN EVEN</Label>
          <Label t={t} at={37.45} x={807} y={478} size={62} color={P.warning}>AT REST</Label>
        </g>
      )}
      {t > 37.3 && (
        <Panel r={r} cam={cam} id="pRest" rx={lerp(24, 0, ex)} border={restBorder} bw={lerp(t > 38.34 ? 14 : SW, 0, ex)}>
          <Park camX={cam.x} dusk={1} />
          <g transform={`translate(${BENCH_X + 250} -620) scale(${0.95 * pop(t, 37.6)})`}><Clock t={t} /></g>
          <Character look={PATIENT} x={SEAT_X} y={0} pose={po} face={pfc} t={t} pain={0.85 + 0.12 * Math.sin(t * 2.6)} />
          {t > 40.1 && <Character look={DOCTOR} x={dx} y={0} flip pose={dpo} face={face('doctorConcern', {look: 0.9})} talk={speech(f)} t={t} />}
          <rect x={-3000} y={-4000} width={12000} height={8000} fill={P.duskTint} opacity={0.16} style={{mixBlendMode: 'multiply'}} />
        </Panel>
      )}
      {t > 41.45 && <g transform={`translate(120 312) scale(${0.85 * pop(t, 41.45)})`}><Warn /></g>}
      <Label t={t} at={41.5} x={570} y={335} size={66} color={P.caution} mode="write">may signal severe</Label>
      <Label t={t} at={41.8} x={540} y={445} size={88}>BLOOD-FLOW LOSS</Label>
    </g>
  );
};

// ===================== S11 SERIOUS: REDUCED FLOW EVEN AT REST (42.55 – 50.62) =====================
const S11: React.FC<SceneP> = ({t}) => {
  const n = narrowPoint();
  const leg = t < 45.95;
  const camA = {x: n.x, y: n.y + 40, z: k(t, [42.55, 45.5, 45.95], [1.5, 1.65, 0.9], Easing.inOut(Easing.quad))};
  const pIn = k(t, [45.6, 45.95], [0, 1]);
  const PC = {x: 540, y: 880};
  const zA = k(t, [46.0, 46.6], [0, 1]), zB = k(t, [47.9, 48.4], [0, 1]), zC = k(t, [49.4, 49.9], [0, 1]);
  let camB: CamT = {x: 540, y: 960, z: 1};
  camB = lerpCam(camB, {x: PC.x - 150, y: PC.y + 34, z: 1.3}, zA);
  camB = lerpCam(camB, {x: PC.x + 30, y: PC.y + 20, z: 1.3}, zB);
  camB = lerpCam(camB, {x: PC.x + 300, y: PC.y + 30, z: 1.45}, zC);
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      {leg && (
        <g opacity={1 - pIn}>
          <Cam {...camA}><LegCutaway t={t} narrow={1} flow={0.12} o2={0.12} spots={1} muscleGlow={0.35 + 0.2 * Math.sin(t * 3)} /></Cam>
          {t > 42.95 && <rect x={60} y={232} width={960} height={350} rx={30} fill="#fff" stroke={INK} strokeWidth={5} opacity={0.94 * pop(t, 42.97)} />}
          {t > 42.95 && <g transform={`translate(205 305) scale(${0.85 * pop(t, 43.0)})`}><Warn color={P.warning} /></g>}
          <Label t={t} at={43.02} x={590} y={345} size={114} color={P.warning}>SERIOUS</Label>
          <Label t={t} at={43.5} x={540} y={460} size={68} mode="write">PERSISTENT PAIN AT REST</Label>
          <Label t={t} at={44.0} x={540} y={548} size={54} color={P.caution} mode="write">→ seek prompt medical assessment</Label>
        </g>
      )}
      {pIn > 0 && (
        <g opacity={pIn}>
          <Cam {...camB}>
            <g transform={`translate(${PC.x} ${PC.y})`}>
              <FlowPanel t={t} narrow={1} activity={0} title="EVEN AT REST" titleColor={P.warning} h={380} o2={1}
                mood={t > 49.45 ? 'tired' : 'strain'} pain={0.55 + 0.15 * Math.sin(t * 3)} />
            </g>
          </Cam>
          <Label t={t} at={46.0} x={540} y={335} size={78} mode="write">ARTERIAL BLOOD FLOW</Label>
          <Label t={t} at={47.9} x={540} y={445} size={92} color={P.warning}>ALREADY REDUCED</Label>
          <Label t={t} at={49.45} x={540} y={548} size={64} mode="slide">→ muscle function affected</Label>
        </g>
      )}
    </g>
  );
};

// ===================== S12 RESEARCH → ELEVATED CARDIOVASCULAR RISK (50.62 – 55.30) =====================
const RiskIcon: React.FC<{t: number; at: number; x: number; y: number; label: string; children: React.ReactNode}> = ({t, at, x, y, label, children}) => {
  const s = pop(t, at);
  if (s <= 0) return null;
  return (
    <g transform={`translate(${x} ${y}) scale(${s})`}>
      {children}
      <g transform="translate(140 -10) scale(0.5)"><UpArrow /></g>
      <text y={128} textAnchor="middle" fontFamily={FONT} fontWeight={700} fontSize={48} fill="#fff" stroke={INK} strokeWidth={9} paintOrder="stroke">{label}</text>
    </g>
  );
};
const S12: React.FC<SceneP> = ({t}) => {
  const up = k(t, [52.25, 52.6], [0, 1], Easing.in(Easing.cubic));
  const bm = pop(t, 50.62);
  const bmO = lerp(0.28, 1, k(t, [52.3, 52.6], [0, 1]));
  const beat = t > 53.98 ? 0.6 + 0.4 * Math.sin(t * 15) : 0.3 + 0.3 * Math.sin(t * 9);
  const link = (a: Vec, b: Vec, at: number) => {
    const u = k(t, [at, at + 0.35], [0, 1]);
    return u > 0 ? <path d={`M ${a.x} ${a.y} L ${lerp(a.x, b.x, u)} ${lerp(a.y, b.y, u)}`} stroke={INK} strokeWidth={6} strokeDasharray="14 10" strokeLinecap="round" /> : null;
  };
  return (
    <g>
      <rect width={W} height={H} fill="#fff" />
      {bm > 0 && (
        <g opacity={Math.min(1, bm * 1.5) * bmO}>
          <Cam {...gcam(210, 1.0)}>
            <g transform={`translate(0 0) scale(${lerp(0.9, 1, bm)})`}>
              <BodyMap t={t} draw={1} legPlaque={1} bodyPlaque={pop(t, 53.72)} pulse={k(t, [53.72, 54.3], [0, 1], lin)} beat={beat} pain={k(t, [52.5, 52.9], [0, 0.9])}
                fc={t < 53.9 ? face('concern', {look: 0}) : face('worried', {look: 0})} />
            </g>
          </Cam>
          {link({x: 400, y: 630}, {x: 690, y: 600}, 54.38)}
          {link({x: 380, y: 800}, {x: 690, y: 860}, 53.98)}
          <RiskIcon t={t} at={54.38} x={780} y={600} label="STROKE"><g transform="scale(0.72)"><BrainIcon /></g></RiskIcon>
          <RiskIcon t={t} at={53.98} x={780} y={860} label="HEART ATTACK"><HeartIcon s={0.9} beat={beat} /></RiskIcon>
          <Label t={t} at={52.6} x={600} y={1150} size={64} color={P.caution}>PAD ←</Label>
        </g>
      )}
      {[50.76, 51.22, 51.6].map((at, i) => {
        const s = pop(t, at);
        if (s <= 0 || up >= 1) return null;
        return (
          <g key={i} transform={`translate(${lerp(270 + i * 270, 140 + i * 30, up)} ${lerp(880 + (i - 1) * 30, 560, up)}) rotate(${-6 + i * 6}) scale(${s * lerp(1.3, 0.4, up)})`} opacity={1 - up}>
            <Paper checked={pop(t, 51.88 + i * 0.12)} />
          </g>
        );
      })}
      <Label t={t} at={50.76} until={52.3} x={540} y={340} size={100}>RESEARCH</Label>
      <Label t={t} at={51.88} until={52.3} x={540} y={450} size={64} color={P.relief} mode="write">consistently shows</Label>
      <Label t={t} at={52.36} until={53.95} x={540} y={340} size={68} mode="write">PEOPLE WITH CLAUDICATION</Label>
      <Label t={t} at={53.98} x={540} y={335} size={104} color={P.warning}>ELEVATED</Label>
      <Label t={t} at={54.38} x={540} y={445} size={72}>CARDIOVASCULAR RISK</Label>
    </g>
  );
};

// ===================== S13 ALWAYS INVESTIGATE (55.30 – 60.60) =====================
const PX_STOP = -260, DXF = 60, DS = 0.95;
const S13: React.FC<SceneP> = ({t, f}) => {
  const x = t < 56.6 ? -820 + 420 * (t - 55.3) : k(t, [56.6, 56.9], [-274, PX_STOP], outQ);
  const W0 = walk(x + 820, {L: 330, limp: 0.7});
  const calfL = calfPoint(PATIENT, STAND);
  const pointCalf = pose(STAND, {lean: 10, head: 10, reachF: add(calfL, {x: 40, y: -40}), reachFW: 0.85, handF: 'point'});
  let ppo = mix(W0, STAND, k(t, [56.6, 56.95], [0, 1]));
  ppo = mix(ppo, pointCalf, k(t, [57.5, 57.85], [0, 1]) * (1 - k(t, [58.9, 59.2], [0, 1])));
  const nod = t > 59.85 ? 6 * Math.sin((t - 59.85) * 14) : 0;
  ppo = pose(ppo, {head: ppo.head + nod});
  const pfc = t < 56.9 ? face('discomfort') : t < 59.8 ? face('concern', {look: 1}) : face('understanding', {look: 0.6});
  // doctor kneels (side view, facing the patient); the magnifier is IK-aimed so the LENS sits on the calf
  const aim = docLocal(add(calfL, {x: PX_STOP, y: 0}), DXF, DS, true);
  const kneel = pose(STAND, {lean: 26, head: 10, thighF: 95, kneeF: 120, thighB: -35, kneeB: 60});
  const raise = pose(STAND, {armF: 40, elbowF: 112, handF: 'up', head: 6 * Math.sin(t * 16) * k(t, [56.8, 57.0, 57.4, 57.6], [0, 1, 1, 0])});
  let dpo = mix(STAND, raise, k(t, [56.7, 57.0], [0, 1]));
  dpo = mix(dpo, kneel, k(t, [58.88, 59.35], [0, 1]));
  const mag = pop(t, 58.95);
  const n = narrowPoint();
  const u = k(t, [58.85, 59.5], [0, 1]);
  const cam = gcam(lerp(-60, -110, u), lerp(0.92, 0.96, u));
  const bump = t > 59.82 ? 1 + 0.12 * Math.max(0, 1 - (t - 59.82) / 0.25) : 1;
  return (
    <g>
      <Cam {...cam}><Clinic><BoardContent t={t} titles={false} /></Clinic></Cam>
      <rect width={W} height={H} fill="#fff" opacity={k(t, [55.3, 58.85, 59.25], [0.6, 0.6, 0.75])} />
      <Cam {...cam}>
        <Character look={PATIENT} x={x} y={0} pose={ppo} face={pfc} t={t} pain={t < 58.9 ? 0.55 + 0.25 * Math.sin(t * 14) : 0.4} />
        <Character look={DOCTOR} x={DXF} y={0} s={DS} flip pose={dpo} face={face(t < 56.7 ? 'happy' : 'talk', {look: 0.9})} talk={t < 56.7 ? 0 : speech(f)} t={t}
          aim={mag > 0 ? aim : undefined} aimLen={140 * Math.max(0.05, mag)}
          prop={mag > 0 ? (ang: number) => (
            <g transform={`scale(${mag})`}>
              <Magnifier rot={ang} lens={<g transform={`scale(-0.32 0.32) translate(${-n.x} ${-n.y})`}><LegCutaway t={t} narrow={0.9} flow={0.35} /></g>} />
            </g>
          ) : undefined} />
      </Cam>
      <Label t={t} at={56.76} until={58.85} x={540} y={430} size={104} color={P.warning}>DON'T DISMISS</Label>
      <g transform={`translate(540 436) scale(${bump}) translate(-540 -436)`}>
        <Label t={t} at={59.0} x={540} y={436} size={80}>ALWAYS, ALWAYS</Label>
      </g>
      <Label t={t} at={59.82} x={540} y={540} size={104} color={P.warning}>INVESTIGATE</Label>
      {t > 57.6 && (
        <g opacity={k(t, [57.6, 57.85], [0, 1])}>
          <rect x={200} y={232} width={680} height={112} rx={28} fill="#fff" stroke={INK} strokeWidth={5} />
          <text x={540} y={279} textAnchor="middle" fontFamily={CAP_FONT} fontWeight={900} fontSize={40} fill={INK}>Not every cramp is PAD.</text>
          <text x={540} y={328} textAnchor="middle" fontFamily={CAP_FONT} fontWeight={900} fontSize={40} fill={P.doctorScrubs}>A clinician can tell.</text>
        </g>
      )}
    </g>
  );
};

export const SCENES: [number, React.FC<SceneP>][] = [
  [0, S1], [5.9, S3], [10.3, S4], [15.68, S6], [18.98, S7],
  [25.52, S8], [32.92, S9], [35.92, S10], [42.55, S11], [50.62, S12], [55.3, S13],
];

// ---------- narrative match transitions (screen-space anchors computed from the shots themselves) ----------
export type Transition = {at: number; a: number; c: number; type: 'zoom' | 'iris' | 'slide' | 'pullout'; from: [number, number]; to?: [number, number]; dir?: number};
const v = (p: Vec): [number, number] => [Math.round(p.x), Math.round(p.y)];
const calfOf = (st: {x: number; po: Pose; cam: CamT}) => v(toScreen(add(calfPoint(PATIENT, st.po), {x: st.x, y: 0}), st.cam));
export const TRANSITIONS: Transition[] = [
  // seated patient's calf -> close-up of the SAME calf walking
  {at: 5.9, a: 0.22, c: 0.2, type: 'zoom', from: v(toScreen(CALF_SIT_W, s1(5.9).cam)), to: calfOf(s3(5.9))},
  // oxygen-starved muscle -> opens out of the patient's calf in the park
  {at: 15.68, a: 0.08, c: 0.36, type: 'iris', from: calfOf(s6(15.68))},
  // walking with pain -> into the leg anatomy (early signal)
  {at: 18.98, a: 0.22, c: 0.2, type: 'zoom', from: calfOf(s6(18.98)), to: v(toScreen(muscleCenter, s7cam(18.98)))},
  // risk map -> the doctor's board
  {at: 25.52, a: 0.14, c: 0.22, type: 'slide', from: [540, 960], dir: -1},
  // board panel "walking = pain" -> the same pattern, side by side with rest pain
  {at: 35.92, a: 0.2, c: 0.22, type: 'zoom', from: [540, 1000], to: [273, 890]},
  // rest-pain calf -> inside that calf
  {at: 42.55, a: 0.08, c: 0.36, type: 'iris', from: v(toScreen(add(SIT_CALF, {x: SEAT_X, y: 0}), s10(42.55).cam))},
  // anatomy -> shrinks back into the body on the risk map
  {at: 50.62, a: 0.15, c: 0.32, type: 'pullout', from: [330, 1110]},
  // risk map -> final clinic evaluation
  {at: 55.3, a: 0.14, c: 0.22, type: 'slide', from: [540, 960], dir: 1},
];
