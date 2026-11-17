import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Audio, Easing, continueRender, delayRender, staticFile, useCurrentFrame} from 'remotion';
import {FPS, W, H, INK, clamp, lerp, smooth} from './lib';
import {Defs, Captions, CaptionVeil} from './ui';
import {SCENES, TRANSITIONS, Transition, captionZone} from './scenes';

// Audio is 60.581 s; 1818 frames = 60.600 s so the final syllable is never cut.
export const DURATION = 1818;

const sceneAt = (t: number) => {
  let i = SCENES.length - 1;
  while (i > 0 && t < SCENES[i][0]) i--;
  return SCENES[i][1];
};

// Narrative match transitions: both shots are live during the window, tied to the same story point.
const About: React.FC<{c: [number, number]; s: number; o?: number; children: React.ReactNode}> = ({c, s, o = 1, children}) => (
  <g opacity={o} transform={`translate(${c[0]} ${c[1]}) scale(${s}) translate(${-c[0]} ${-c[1]})`}>{children}</g>
);
const Trans: React.FC<{tr: Transition; t: number; f: number}> = ({tr, t, f}) => {
  const Out = sceneAt(tr.at - 0.001), In = sceneAt(tr.at);
  const u = clamp((t - (tr.at - tr.a)) / (tr.a + tr.c));
  const e = smooth(u);
  const outS = <Out t={t} f={f} />, inS = <In t={t} f={f} />;
  if (tr.type === 'zoom') {
    return (
      <g>
        <About c={tr.from} s={1 + 1.8 * Easing.in(Easing.cubic)(u)} o={1 - clamp(u / 0.62)}>{outS}</About>
        <About c={tr.to ?? tr.from} s={lerp(1.4, 1, Easing.out(Easing.cubic)(clamp((u - 0.3) / 0.7)))} o={clamp((u - 0.3) / 0.45)}>{inS}</About>
      </g>
    );
  }
  if (tr.type === 'iris') {
    const r = lerp(0, 2300, Easing.in(Easing.quad)(u));
    return (
      <g>
        {outS}
        <clipPath id={`iris${tr.at}`}><circle cx={tr.from[0]} cy={tr.from[1]} r={Math.max(1, r)} /></clipPath>
        <g clipPath={`url(#iris${tr.at})`}>{inS}</g>
        <circle cx={tr.from[0]} cy={tr.from[1]} r={r} fill="none" stroke={INK} strokeWidth={16} opacity={1 - clamp((u - 0.75) / 0.25)} />
      </g>
    );
  }
  if (tr.type === 'slide') {
    const d = tr.dir ?? -1;
    return (
      <g>
        <g transform={`translate(${d * W * e} 0)`}>{outS}</g>
        <g transform={`translate(${-d * W * (1 - e)} 0)`}>{inS}</g>
      </g>
    );
  }
  // pullout: the anatomy shrinks back into the body it came from while the wider view fades up
  return (
    <g>
      {inS}
      <About c={tr.from} s={lerp(1, 0.22, Easing.in(Easing.cubic)(u))} o={1 - clamp((u - 0.35) / 0.4)}>{outS}</About>
    </g>
  );
};

export const Video: React.FC = () => {
  const f = useCurrentFrame();
  const t = f / FPS;
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    Promise.all([document.fonts.load('700 72px Kalam'), document.fonts.load('900 70px Nunito')]).then(() => continueRender(handle));
  }, [handle]);
  const tr = TRANSITIONS.find((q) => t >= q.at - q.a && t < q.at + q.c);
  const Scene = sceneAt(t);
  return (
    <AbsoluteFill style={{background: '#fff'}}>
      <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H}>
        <Defs frame={f} />
        {tr ? <Trans tr={tr} t={t} f={f} /> : <Scene t={t} f={f} />}
        <CaptionVeil zone={captionZone(t)} />
        <Captions t={t} zoneAt={captionZone} />
      </svg>
      <Audio src={staticFile('narration.mp3')} />
    </AbsoluteFill>
  );
};
