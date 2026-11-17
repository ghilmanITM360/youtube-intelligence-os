import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame } from "remotion";
import { B, C, TL } from "./lib/bundle";
import { CaptionPlate } from "./components/Svg";
import { activeCaption, CAPTION_METRICS, CAPTION_Y } from "./lib/captions";
import { prog } from "./lib/anim";
import { SHOTS } from "./shots";
import { StaticHero } from "./shots/StaticHero";

/** Screen-fixed captions from CAPTIONS.json (provisional timings). */
const Captions: React.FC = () => {
  const f = useCurrentFrame();
  const active = activeCaption(f, TL.captions, TL.shots);
  if (!active) return null;
  const {caption: c, end} = active;
  const o = prog(f, c.from - 2, c.from + 2) * (1 - prog(f, end - 3, end));
  return (
    <AbsoluteFill>
      <svg viewBox="0 0 1080 1920" width={1080} height={1920}><CaptionPlate text={c.text} opacity={o} cy={CAPTION_Y[c.shot] ?? CAPTION_METRICS.defaultY} /></svg>
    </AbsoluteFill>
  );
};

/** Shown while the pronunciation gate has not passed: timings are provisional, not a master. */
const Watermark: React.FC = () =>
  TL.gate.final_sync_allowed ? null : (
    <AbsoluteFill>
      <svg viewBox="0 0 1080 1920" width={1080} height={1920}>
        <rect x={24} y={24} width={640} height={44} rx={12} fill={C.navy_dk} fillOpacity={0.72} />
        <text x={44} y={53} fontFamily={B.font} fontSize={20} fontWeight={700} fill={C.gold}>
          PROVISIONAL TIMING • APR AUDIO FIX PENDING • NOT FINAL
        </text>
      </svg>
    </AbsoluteFill>
  );

export const Video: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <AbsoluteFill style={{ backgroundColor: C.navy_bg }}>
    {TL.shots.map((s) => {
      const Shot = SHOTS[s.id];
      return (
        <Sequence key={s.id} from={s.from} durationInFrames={s.to - s.from} name={`${s.id} ${s.narration}`}>
          {Shot ? <Shot /> : <StaticHero shot={s.id} />}
        </Sequence>
      );
    })}
    {captions && <Captions />}
    <Watermark />
  </AbsoluteFill>
);

/** One shot in isolation (for focused previews): the full timeline shifted to the shot start. */
export const ShotPreview: React.FC<{ shot: string }> = ({ shot }) => {
  const s = TL.shots.find((x) => x.id === shot)!;
  return <Sequence from={-s.from}><Video /></Sequence>;
};
