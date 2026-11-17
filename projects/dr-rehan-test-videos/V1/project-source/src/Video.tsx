import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Audio, continueRender, delayRender, staticFile, useCurrentFrame} from 'remotion';
import {FPS, W, H} from './lib';
import {Defs} from './ui';
import {SCENES} from './scenes';

// Audio is 60.581 s; 1818 frames = 60.600 s so the final syllable is never cut.
export const DURATION = 1818;

export const Video: React.FC = () => {
  const f = useCurrentFrame();
  const t = f / FPS;
  const [handle] = useState(() => delayRender('Kalam font'));
  useEffect(() => {
    document.fonts.load('700 72px Kalam').then(() => continueRender(handle));
  }, [handle]);
  let i = SCENES.length - 1;
  while (i > 0 && t < SCENES[i][0]) i--;
  const Scene = SCENES[i][1];
  return (
    <AbsoluteFill style={{background: '#fff'}}>
      <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H}>
        <Defs frame={f} />
        <Scene t={t} f={f} />
      </svg>
      <Audio src={staticFile('narration.mp3')} />
    </AbsoluteFill>
  );
};
