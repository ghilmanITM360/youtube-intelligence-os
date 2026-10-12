import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {Character, PATIENT, DOCTOR, walk, SIT, STAND, FRONT, pose, calfPoint} from './rig';
import {Defs, Label} from './ui';

export const RigTest: React.FC = () => {
  const f = useCurrentFrame();
  const t = f / 30;
  const grab = pose(STAND, {lean: 30, thighF: 14, kneeF: 20, head: 12, reachF: calfPoint(PATIENT, pose(STAND, {thighF: 14, kneeF: 20})), reachFW: 1, handF: 'fist'});
  return (
    <AbsoluteFill style={{background: '#fff'}}>
      <svg viewBox="0 0 1080 1920" width={1080} height={1920}>
        <Defs frame={f} />
        <Character look={PATIENT} x={200} y={700} s={0.55} pose={walk(0.1)} face="neutral" t={t} />
        <Character look={PATIENT} x={460} y={700} s={0.55} pose={walk(0.35, {limp: 1})} face="pain" t={t} pain={1} />
        <Character look={PATIENT} x={740} y={700} s={0.55} pose={grab} face="discomfort" t={t} pain={0.7} />
        <Character look={PATIENT} x={200} y={1200} s={0.55} pose={SIT} face="relief" t={t} relief={1} />
        <Character look={PATIENT} x={470} y={1200} s={0.55} pose={STAND} face="concern" t={t} />
        <Character look={PATIENT} x={760} y={1200} s={0.55} pose={FRONT} side={false} face="understanding" t={t} />
        <Character look={DOCTOR} x={250} y={1800} s={0.55} side={false} pose={pose(FRONT, {armF: 150, elbowF: 20, handF: 'open'})} face="talk" talk={0.6} t={t} />
        <Character look={DOCTOR} x={560} y={1800} s={0.55} side={false} pose={pose(FRONT, {armF: 80, elbowF: 0, handF: 'point'})} face="doctorConcern" talk={0.0} t={t} />
        <Character look={DOCTOR} x={860} y={1800} s={0.55} pose={walk(0.2)} face="happy" t={t} />
        <Label t={t} at={0} x={540} y={140} size={80}>RIG TEST</Label>
      </svg>
    </AbsoluteFill>
  );
};
