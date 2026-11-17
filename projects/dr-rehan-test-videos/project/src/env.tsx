import React from 'react';
import {INK, P, SW, W, H, rnd, clamp} from './lib';

// Camera over a world layer: centre (x,y) and zoom z.
export const Cam: React.FC<{x: number; y: number; z: number; children: React.ReactNode; boil?: boolean}> = ({x, y, z, children, boil = true}) => (
  <g filter={boil ? 'url(#boil)' : undefined}>
    <g transform={`translate(${W / 2} ${H / 2}) scale(${z}) translate(${-x} ${-y})`}>{children}</g>
  </g>
);

// ---------- 1. PARK (walking world). Ground line y = 0, walking direction +x ----------
export const BENCH_X = 1560;
const TREES = [-420, 260, 1000, 1880, 2620, 3350, 4150, 4900];
const LAMPS = [640, 2250, 3800];

const Tree: React.FC<{x: number; i: number}> = ({x, i}) => {
  const h = 250 + rnd(i) * 90, r = 105 + rnd(i + 9) * 30;
  return (
    <g transform={`translate(${x} -70)`}>
      <path d={`M -16 0 L -12 ${-h} L 12 ${-h} L 16 0 Z`} fill="#A9744A" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      <g stroke={INK} strokeWidth={SW * 2}>
        <circle cx={-r * 0.55} cy={-h - 10} r={r * 0.75} /><circle cx={r * 0.55} cy={-h - 20} r={r * 0.7} /><circle cx={0} cy={-h - r * 0.75} r={r * 0.85} />
      </g>
      <g fill={P.tree}>
        <circle cx={-r * 0.55} cy={-h - 10} r={r * 0.75} /><circle cx={r * 0.55} cy={-h - 20} r={r * 0.7} /><circle cx={0} cy={-h - r * 0.75} r={r * 0.85} />
      </g>
      <path d={`M ${-r * 0.4} ${-h - r * 0.9} q 20 -24 46 -18`} stroke="#A6DB95" strokeWidth={10} fill="none" strokeLinecap="round" />
    </g>
  );
};
const Lamp: React.FC<{x: number}> = ({x}) => (
  <g transform={`translate(${x} -60)`}>
    <path d="M 0 0 L 0 -470" stroke={INK} strokeWidth={22} strokeLinecap="round" />
    <path d="M 0 0 L 0 -470" stroke="#5B6372" strokeWidth={10} strokeLinecap="round" />
    <path d="M -34 -470 L 34 -470 L 22 -520 L -22 -520 Z" fill="#FFE38A" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
    <path d="M -40 -520 L 40 -520 L 0 -548 Z" fill="#5B6372" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
  </g>
);
export const Bench: React.FC<{x: number}> = ({x}) => (
  <g transform={`translate(${x} -6)`} stroke={INK} strokeWidth={SW} strokeLinejoin="round" strokeLinecap="round">
    {/* far frame (oblique) */}
    <path d="M -40 -40 L -40 -170 M 70 -40 L 70 -150" stroke="#6B4A2E" strokeWidth={14} />
    <path d="M -96 -200 L -96 -350 L -70 -350 L -70 -200 Z" fill="#B97C46" transform="translate(54 -36)" />
    {/* backrest slats */}
    <path d="M -104 -250 L 66 -286 L 66 -246 L -104 -210 Z" fill="#C98A50" />
    <path d="M -104 -318 L 66 -354 L 66 -314 L -104 -278 Z" fill="#C98A50" />
    {/* seat */}
    <path d="M -104 -168 L 120 -168 L 150 -196 L -74 -196 Z" fill="#D99A5E" />
    <path d="M -104 -168 L 120 -168 L 120 -150 L -104 -150 Z" fill="#B97C46" />
    {/* near legs + back post */}
    <path d="M -96 -150 L -96 0 M 112 -150 L 112 0" stroke={INK} strokeWidth={20} />
    <path d="M -96 -150 L -96 0 M 112 -150 L 112 0" stroke="#6B4A2E" strokeWidth={8} />
    <path d="M -104 -150 L -104 -360" stroke={INK} strokeWidth={22} />
    <path d="M -104 -150 L -104 -360" stroke="#8A5C36" strokeWidth={10} />
  </g>
);

export const Park: React.FC<{camX: number; dusk?: number}> = ({camX, dusk = 0}) => (
  <g>
    <rect x={-3000} y={-4000} width={12000} height={8000} fill="#FFFFFF" />
    {dusk > 0 && <rect x={-3000} y={-4000} width={12000} height={8000} fill="#D8DEF0" opacity={dusk} />}
    {/* clouds (parallax 0.35) */}
    {[[-200, -1420], [700, -1480], [1500, -1400], [2500, -1460], [3400, -1410], [4300, -1470]].map(([cx, cy], i) => (
      <g key={i} transform={`translate(${cx + camX * 0.65} ${cy})`}>
        <path d="M -110 30 Q -120 -20 -60 -24 Q -40 -76 20 -56 Q 70 -84 100 -30 Q 150 -20 130 30 Z" fill="#fff" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      </g>
    ))}
    {/* back grass + hedge line */}
    <path d="M -3000 -150 Q -2500 -190 -2000 -150 T -1000 -150 T 0 -150 T 1000 -150 T 2000 -150 T 3000 -150 T 4000 -150 T 5000 -150 T 6000 -150 T 7000 -150 L 7000 -40 L -3000 -40 Z" fill={P.grass} stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
    {TREES.map((x, i) => <Tree key={x} x={x} i={i} />)}
    {LAMPS.map((x) => <Lamp key={x} x={x} />)}
    {/* sidewalk */}
    <rect x={-3000} y={-46} width={10000} height={110} fill={P.sidewalk} />
    {Array.from({length: 40}, (_, i) => -3000 + i * 260).map((x) => (
      <path key={x} d={`M ${x} -46 L ${x - 30} 64`} stroke="#D2D2CC" strokeWidth={5} />
    ))}
    <path d="M -3000 -46 L 7000 -46" stroke={INK} strokeWidth={SW} />
    <path d="M -3000 64 L 7000 64" stroke={INK} strokeWidth={SW} />
    {/* front grass */}
    <rect x={-3000} y={64} width={10000} height={3000} fill="#E6F4DA" />
    {Array.from({length: 46}, (_, i) => -2800 + i * 210 + rnd(i) * 80).map((x, i) => (
      <path key={i} d={`M ${x} ${170 + rnd(i + 3) * 300} l 8 -26 l 8 22 l 8 -18 l 6 22`} stroke="#7FB36A" strokeWidth={5} fill="none" strokeLinecap="round" strokeLinejoin="round" />
    ))}
    <Bench x={BENCH_X} />
  </g>
);

// ---------- 2. CLINIC (consultation/explainer). Floor y = 0 ----------
export const BOARD = {x: -540, y: -1120, w: 800, h: 600};
export const Clinic: React.FC<{children?: React.ReactNode}> = ({children}) => (
  <g>
    <rect x={-3000} y={-4000} width={6000} height={4000} fill="#FBFAF6" />
    <rect x={-3000} y={0} width={6000} height={3000} fill="#EEF1F2" />
    <path d="M -3000 0 L 3000 0" stroke={INK} strokeWidth={SW} />
    {/* wall rail */}
    <path d="M -3000 -330 L 3000 -330" stroke="#D9DCD6" strokeWidth={10} />
    {/* window, right */}
    <g transform="translate(560 -1060)">
      <rect x={0} y={0} width={300} height={360} rx={8} fill="#DDEFFB" stroke={INK} strokeWidth={SW} />
      <path d="M 150 0 L 150 360 M 0 180 L 300 180" stroke={INK} strokeWidth={5} />
      <path d="M 40 300 Q 90 240 140 300" stroke="#A9D7F5" strokeWidth={10} fill="none" />
    </g>
    {/* plant, left */}
    <g transform="translate(-640 0)">
      <path d="M -60 0 L -74 -150 L 74 -150 L 60 0 Z" fill="#D9774A" stroke={INK} strokeWidth={SW} strokeLinejoin="round" />
      {[-40, -10, 22, 50].map((a, i) => (
        <path key={i} d={`M 0 -150 Q ${a * 2} -300 ${a * 3.2} ${-380 + i * 30}`} stroke={INK} strokeWidth={SW * 2.6} fill="none" strokeLinecap="round" />
      ))}
      {[-40, -10, 22, 50].map((a, i) => (
        <path key={'g' + i} d={`M 0 -150 Q ${a * 2} -300 ${a * 3.2} ${-380 + i * 30}`} stroke={P.tree} strokeWidth={SW * 1.4} fill="none" strokeLinecap="round" />
      ))}
    </g>
    {/* whiteboard */}
    <g transform={`translate(${BOARD.x} ${BOARD.y})`}>
      <rect x={-14} y={-14} width={BOARD.w + 28} height={BOARD.h + 28} rx={14} fill="#C9CED6" stroke={INK} strokeWidth={SW} />
      <rect x={0} y={0} width={BOARD.w} height={BOARD.h} rx={6} fill={P.board} stroke={INK} strokeWidth={4} />
      <path d={`M 40 ${BOARD.h + 14} L 40 ${BOARD.h + 30} L ${BOARD.w - 40} ${BOARD.h + 30} L ${BOARD.w - 40} ${BOARD.h + 14}`} stroke={INK} strokeWidth={5} fill="#C9CED6" />
      {children}
    </g>
  </g>
);

export const Dusk: React.FC<{v: number}> = ({v}) =>
  v > 0 ? <rect x={0} y={0} width={W} height={H} fill={P.duskTint} opacity={clamp(v) * 0.16} style={{mixBlendMode: 'multiply'}} /> : null;
