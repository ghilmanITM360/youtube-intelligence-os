import React from "react";
import { B, TL } from "../lib/bundle";
import { resolve } from "../rig/rig";
import { SceneWorld, type Override } from "../components/Svg";

/** Approved hero composition, unanimated. Used for shots whose animation is not built yet. */
export const StaticHero: React.FC<{ shot: string }> = ({ shot }) => {
  const s = TL.shots.find((x) => x.id === shot)!;
  const sc = B.scenes[s.scene];
  const ov: Record<string, Override> = {};
  for (const i of sc.world) if (i.char) ov[i.id] = { pose: resolve(B.joints, i.char.pose) };
  return (
    <SceneWorld id={s.scene} ov={ov}>
      <text x={540} y={1880} textAnchor="middle" fontFamily={B.font} fontSize={24} fontWeight={700} fill="#E8BC62">
        {shot} • static hero frame (not yet animated)
      </text>
    </SceneWorld>
  );
};
