import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame } from "remotion";
import { B, C, TL } from "./lib/bundle";
import { CaptionPlate } from "./components/Svg";
import { prog } from "./lib/anim";
import { SHOTS } from "./shots";
import { StaticHero } from "./shots/StaticHero";

// Caption plate centre. Default y 1550 keeps the plate (≈1500–1600) above the Shorts UI band
// (bottom 320 px) and below Remy's face in the stage set-ups; shots with a big Remy override it.
const CAPTION_Y: Record<string, number> = { S01A: 720, S01B: 720, S02A: 560, S07B: 100 };
const CAPTION_DEFAULT_Y = 1550;

/** Screen-fixed captions from CAPTIONS.json (provisional timings). */
const Captions: React.FC = () => {
  const f = useCurrentFrame();
  const i = TL.captions.findIndex((c, k) => f >= c.from && f < (TL.captions[k + 1]?.from ?? c.to + 12));
  if (i < 0) return null;
  const c = TL.captions[i];
  const end = Math.min(c.to + 12, TL.captions[i + 1]?.from ?? Infinity);
  const o = prog(f, c.from - 2, c.from + 2) * (1 - prog(f, end - 3, end));
  return (
    <AbsoluteFill>
      <svg viewBox="0 0 1080 1920" width={1080} height={1920}><CaptionPlate text={c.text} opacity={o} cy={CAPTION_Y[c.shot] ?? CAPTION_DEFAULT_Y} /></svg>
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
