import React from 'react';
import tokens from '../STYLE_TOKENS.json';
import {FONT, CAP_FONT, INK, P, SW, clamp, pop, k, Vec} from './lib';
import CUES from './captions.json';

// Shared SVG defs: glows + hand-drawn "line boil" (seed steps every few frames).
export const Defs: React.FC<{frame: number}> = ({frame}) => (
  <defs>
    <radialGradient id="painGlow">
      <stop offset="0" stopColor={P.warning} stopOpacity={0.85} />
      <stop offset="0.55" stopColor={P.warning} stopOpacity={0.35} />
      <stop offset="1" stopColor={P.warning} stopOpacity={0} />
    </radialGradient>
    <radialGradient id="reliefGlow">
      <stop offset="0" stopColor={P.relief} stopOpacity={0.55} />
      <stop offset="1" stopColor={P.relief} stopOpacity={0} />
    </radialGradient>
    <radialGradient id="heartGlow">
      <stop offset="0" stopColor={P.warning} stopOpacity={0.5} />
      <stop offset="1" stopColor={P.warning} stopOpacity={0} />
    </radialGradient>
    <filter id="boil" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency={tokens.stroke.boil.frequency} numOctaves={2}
        seed={Math.floor(frame / tokens.stroke.boil.everyFrames) % 4} result="n" />
      <feDisplacementMap in="SourceGraphic" in2="n" scale={tokens.stroke.boil.scale * 2} xChannelSelector="R" yChannelSelector="G" />
    </filter>
  </defs>
);

type LabelProps = {
  t: number; at: number; x: number; y: number; children: string;
  size?: number; color?: string; until?: number; anchor?: 'middle' | 'start' | 'end';
  mode?: 'pop' | 'write' | 'slide'; rot?: number; stroke?: number;
};
// Sticker caption: paper/colour fill over heavy ink outline (CF caption grammar).
export const Label: React.FC<LabelProps> = ({t, at, x, y, children, size = 72, color = '#FFFFFF', until = 1e9, anchor = 'middle', mode = 'pop', rot = 0, stroke}) => {
  // fade completes AT `until`, so the next caption never overlaps this one
  if (t < at || t > until) return null;
  const outA = clamp((until - t) / 0.2);
  const sc = mode === 'pop' ? pop(t, at) : 1;
  const slide = mode === 'slide' ? (1 - k(t, [at, at + 0.35], [0, 1])) * 120 : 0;
  const reveal = mode === 'write' ? k(t, [at, at + Math.min(0.7, 0.045 * children.length)], [0, 1]) : 1;
  const id = `clip${Math.round(x)}_${Math.round(y)}_${children.length}`;
  const wEst = children.length * size * 0.56;
  const x0 = anchor === 'middle' ? x - wEst / 2 : anchor === 'end' ? x - wEst : x;
  return (
    <g opacity={outA} transform={`translate(${x + slide} ${y}) rotate(${rot}) scale(${sc}) translate(${-x} ${-y})`}>
      {mode === 'write' && (
        <clipPath id={id}><rect x={x0 - 30} y={y - size * 1.2} width={(wEst + 60) * reveal} height={size * 1.8} /></clipPath>
      )}
      <text x={x} y={y} textAnchor={anchor} fontFamily={FONT} fontWeight={700} fontSize={size}
        fill={color} stroke={INK} strokeWidth={stroke ?? Math.max(8, size * 0.16)} strokeLinejoin="round" paintOrder="stroke"
        clipPath={mode === 'write' ? `url(#${id})` : undefined}>
        {children}
      </text>
    </g>
  );
};

// Plain handwritten text (no outline), for board/diagram annotations.
export const Note: React.FC<{x: number; y: number; size?: number; color?: string; anchor?: 'middle' | 'start' | 'end'; children: React.ReactNode; opacity?: number}> = ({x, y, size = 44, color = INK, anchor = 'middle', children, opacity = 1}) => (
  <text x={x} y={y} textAnchor={anchor} fontFamily={FONT} fontWeight={700} fontSize={size} fill={color} opacity={opacity}>{children}</text>
);

// Hand-drawn arrow that draws on between t0..t1.
export const Arrow: React.FC<{t: number; t0: number; t1?: number; a: Vec; b: Vec; bend?: number; color?: string; w?: number}> = ({t, t0, t1, a, b, bend = 0, color = INK, w = 9}) => {
  const u = k(t, [t0, t1 ?? t0 + 0.4], [0, 1]);
  if (u <= 0) return null;
  const mx = (a.x + b.x) / 2 - (b.y - a.y) * bend, my = (a.y + b.y) / 2 + (b.x - a.x) * bend;
  const len = Math.hypot(b.x - a.x, b.y - a.y) * (1 + Math.abs(bend));
  const ang = Math.atan2(b.y - my, b.x - mx);
  const head = (s: number) => `M ${b.x + Math.cos(ang + Math.PI - 0.5) * s} ${b.y + Math.sin(ang + Math.PI - 0.5) * s} L ${b.x} ${b.y} L ${b.x + Math.cos(ang + Math.PI + 0.5) * s} ${b.y + Math.sin(ang + Math.PI + 0.5) * s}`;
  return (
    <g fill="none" strokeLinecap="round" strokeLinejoin="round">
      <path d={`M ${a.x} ${a.y} Q ${mx} ${my} ${b.x} ${b.y}`} stroke={color} strokeWidth={w} strokeDasharray={len} strokeDashoffset={len * (1 - u)} />
      {u > 0.92 && <path d={head(32)} stroke={color} strokeWidth={w} />}
    </g>
  );
};

// Hand-drawn ellipse highlight that draws on (HIGHLIGHT grammar).
export const Circle: React.FC<{t: number; t0: number; cx: number; cy: number; rx: number; ry: number; color?: string; w?: number; dash?: boolean}> = ({t, t0, cx, cy, rx, ry, color = P.warning, w = 9, dash}) => {
  const u = k(t, [t0, t0 + 0.45], [0, 1]);
  if (u <= 0) return null;
  const len = 2 * Math.PI * Math.max(rx, ry) * 1.1;
  return (
    <path d={`M ${cx + rx} ${cy} A ${rx} ${ry} 0 1 1 ${cx + rx * 0.98} ${cy - ry * 0.18}`} fill="none" stroke={color} strokeWidth={w}
      strokeLinecap="round" strokeDasharray={dash ? '18 16' : len} strokeDashoffset={dash ? 0 : len * (1 - u)} opacity={dash ? u : 1} />
  );
};

// ---------- icons (all original, ink outline + flat fill) ----------
export const Bolt: React.FC<{s?: number}> = ({s = 1}) => (
  <path transform={`scale(${s})`} d="M 8 -46 L -22 6 L 0 6 L -10 46 L 24 -10 L 2 -10 Z" fill={P.warning} stroke={INK} strokeWidth={5} strokeLinejoin="round" />
);
export const Check: React.FC<{s?: number; color?: string}> = ({s = 1, color = P.relief}) => (
  <g transform={`scale(${s})`}>
    <circle r={40} fill={color} stroke={INK} strokeWidth={5} />
    <path d="M -18 0 L -4 15 L 20 -14" stroke="#fff" strokeWidth={10} fill="none" strokeLinecap="round" strokeLinejoin="round" />
  </g>
);
export const Warn: React.FC<{s?: number; color?: string}> = ({s = 1, color = P.caution}) => (
  <g transform={`scale(${s})`}>
    <path d="M 0 -44 L 46 36 L -46 36 Z" fill={color} stroke={INK} strokeWidth={6} strokeLinejoin="round" />
    <path d="M 0 -18 L 0 10" stroke={INK} strokeWidth={9} strokeLinecap="round" />
    <circle cy={24} r={5.5} fill={INK} />
  </g>
);
export const Clock: React.FC<{t: number; s?: number}> = ({t, s = 1}) => (
  <g transform={`scale(${s})`}>
    <circle r={50} fill="#fff" stroke={INK} strokeWidth={SW} />
    {[0, 1, 2, 3].map((i) => <path key={i} d="M 0 -40 L 0 -32" transform={`rotate(${i * 90})`} stroke={INK} strokeWidth={5} strokeLinecap="round" />)}
    <path d="M 0 0 L 0 -34" transform={`rotate(${t * 400})`} stroke={INK} strokeWidth={6} strokeLinecap="round" />
    <path d="M 0 0 L 0 -22" transform={`rotate(${t * 34})`} stroke={P.warning} strokeWidth={7} strokeLinecap="round" />
    <circle r={5} fill={INK} />
  </g>
);
export const Paper: React.FC<{checked?: number}> = ({checked = 0}) => (
  <g>
    <rect x={-70} y={-90} width={140} height={180} rx={6} fill="#F4F4F1" stroke={INK} strokeWidth={SW} />
    <path d="M -46 -54 L 46 -54" stroke={P.warning} strokeWidth={9} strokeLinecap="round" />
    {[-20, 6, 32, 58].map((y, i) => (
      <path key={y} d={`M -46 ${y} Q -20 ${y - 7} 0 ${y} T ${i === 3 ? 20 : 46} ${y}`} stroke={INK} strokeWidth={5} fill="none" strokeLinecap="round" />
    ))}
    {checked > 0 && <g transform={`translate(52 66) scale(${checked})`}><Check s={0.7} /></g>}
  </g>
);
export const HeartIcon: React.FC<{s?: number; beat?: number}> = ({s = 1, beat = 0}) => (
  <g transform={`scale(${s * (1 + 0.08 * beat)})`}>
    <path d="M 0 52 C -70 6 -78 -40 -44 -56 C -22 -66 -6 -52 0 -36 C 6 -52 22 -66 44 -56 C 78 -40 70 6 0 52 Z" fill={P.warning} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
    <path d="M -40 -30 Q -44 -44 -30 -48" stroke="#fff" strokeWidth={7} fill="none" strokeLinecap="round" opacity={0.8} />
  </g>
);
export const BrainIcon: React.FC<{s?: number}> = ({s = 1}) => (
  <g transform={`scale(${s})`}>
    <path d="M -58 10 C -72 -10 -60 -40 -36 -44 C -30 -62 -6 -66 6 -54 C 22 -66 50 -60 54 -38 C 74 -30 74 0 58 12 C 62 34 40 50 20 42 C 8 56 -18 56 -28 42 C -50 48 -66 30 -58 10 Z" fill="#F4B8C4" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
    <path d="M -30 -20 Q -10 -10 -24 8 M 8 -36 Q 0 -14 18 -6 M 30 12 Q 10 20 22 34" stroke={INK} strokeWidth={4.5} fill="none" strokeLinecap="round" />
  </g>
);
export const UpArrow: React.FC<{s?: number; color?: string}> = ({s = 1, color = P.warning}) => (
  <path transform={`scale(${s})`} d="M 0 -60 L 44 -6 L 18 -6 L 18 60 L -18 60 L -18 -6 L -44 -6 Z" fill={color} stroke={INK} strokeWidth={6} strokeLinejoin="round" />
);
export const Foot: React.FC<{s?: number}> = ({s = 1}) => (
  <g transform={`scale(${s})`}>
    <path d="M -30 -10 Q -32 22 -14 22 L 40 22 Q 50 8 36 -2 Q 16 -8 0 -16 Z" fill="#fff" stroke={INK} strokeWidth={5} strokeLinejoin="round" />
    <path d="M -24 16 L 40 16" stroke={P.patientShorts} strokeWidth={5} strokeLinecap="round" />
    <path d="M -46 -10 L -66 -10 M -50 6 L -74 6" stroke={INK} strokeWidth={5} strokeLinecap="round" />
  </g>
);

// ---------- narration captions (layer 1) ----------
// Mobile-first: Nunito Black 70 px, white fill + heavy ink outline, 1-2 balanced lines, one keyword lights up
// in its semantic colour when it is spoken. Zone 'low' sits above the Shorts description area and left of the
// action buttons; 'high' is used where the stage fills the lower frame (clinic board).
type Cue = {s: number; e: number; words: {w: string; hl: string | null; s: number}[]};
const CAP = {size: 70, lh: 84, cx: 505, maxChars: 21, low: 1352, high: 318};
const split = (ws: Cue['words']) => {
  const len = (a: Cue['words']) => a.reduce((n, w) => n + w.w.length, 0) + Math.max(0, a.length - 1);
  if (len(ws) <= CAP.maxChars) return [ws];
  let best = 1, bestV = 1e9;
  for (let i = 1; i < ws.length; i++) {
    const v = Math.max(len(ws.slice(0, i)), len(ws.slice(i)));
    if (v < bestV) { bestV = v; best = i; }
  }
  return [ws.slice(0, best), ws.slice(best)];
};
export const Captions: React.FC<{t: number; zoneAt: (t: number) => 'low' | 'high'}> = ({t, zoneAt}) => {
  const c = (CUES as Cue[]).find((q) => t >= q.s && t < q.e);
  if (!c) return null;
  const a = clamp((t - c.s) / 0.12);
  const lines = split(c.words);
  const y0 = (zoneAt(c.s) === 'low' ? CAP.low : CAP.high) - ((lines.length - 1) * CAP.lh) / 2 + CAP.size * 0.36;
  return (
    <g opacity={a} transform={`translate(0 ${(1 - a) * 12})`}>
      {lines.map((ln, i) => (
        <text key={i} x={CAP.cx} y={y0 + i * CAP.lh} textAnchor="middle" fontFamily={CAP_FONT} fontWeight={900} fontSize={CAP.size}
          fill="#fff" stroke={INK} strokeWidth={15} strokeLinejoin="round" paintOrder="stroke" style={{whiteSpace: 'pre'}}>
          {ln.map((w, j) => (
            <tspan key={j} fill={w.hl && t >= w.s - 0.04 ? (P as Record<string, string>)[w.hl] : '#fff'}>{w.w + (j < ln.length - 1 ? ' ' : '')}</tspan>
          ))}
        </text>
      ))}
    </g>
  );
};
// Soft paper veil behind the caption band so background art never competes with the words.
export const CaptionVeil: React.FC<{zone: 'low' | 'high'}> = ({zone}) => {
  const y = zone === 'low' ? CAP.low : CAP.high;
  return (
    <g>
      <defs>
        <linearGradient id={`veil${zone}`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor="#fff" stopOpacity={0} /><stop offset="0.28" stopColor="#fff" stopOpacity={0.72} />
          <stop offset="0.72" stopColor="#fff" stopOpacity={0.72} /><stop offset="1" stopColor="#fff" stopOpacity={0} />
        </linearGradient>
      </defs>
      <rect x={0} y={y - 175} width={1080} height={350} fill={`url(#veil${zone})`} />
    </g>
  );
};
