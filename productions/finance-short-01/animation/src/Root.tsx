import React from "react";
import { Composition } from "remotion";
import { TL } from "./lib/bundle";
import { ShotPreview, Video } from "./Video";

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="FinanceShort01" component={Video} durationInFrames={TL.frames_total} fps={TL.fps} width={1080} height={1920} />
    {TL.shots.map((s) => (
      <Composition key={s.id} id={`Shot-${s.id}`} component={ShotPreview} defaultProps={{ shot: s.id }}
        durationInFrames={s.to - s.from} fps={TL.fps} width={1080} height={1920} />
    ))}
  </>
);
