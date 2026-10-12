import React from 'react';
import {Composition} from 'remotion';
import '@fontsource/kalam/700.css';
import '@fontsource/nunito/900.css';
import {Video, DURATION} from './Video';
import {RigTest} from './RigTest';
import {FPS, W, H} from './lib';

export const Root: React.FC = () => (
  <>
    <Composition id="CalfPain" component={Video} durationInFrames={DURATION} fps={FPS} width={W} height={H} />
    <Composition id="RigTest" component={RigTest} durationInFrames={60} fps={FPS} width={W} height={H} />
  </>
);
