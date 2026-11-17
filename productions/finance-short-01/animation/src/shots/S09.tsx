// Beat 9. S09A "A true zero-percent introductory APR is different."  (APR anchor is PROVISIONAL:
// the supplied MP3 says "April" here; the word anchor re-times automatically after re-alignment.)
// S09B "Leaving a balance doesn't trigger interest for that zero-percent period."
import React from "react";
import { useCurrentFrame } from "remotion";
import { Raw, SceneWorld, type Override } from "../components/Svg";
import { E, fade, poseTrack, prog, track } from "../lib/anim";
import { C, assetMarkup, charTf, pose, shot, word } from "../lib/bundle";
import { without } from "../lib/markup";

const K = (k: string) => `diagram_compare__compare_${k}`;
const REMY_TF = charTf(540, 1960, 0.55);
const X_PATH = '<path d="M700 900 L860 1020 M860 900 L700 1020" fill="none" stroke="#147D83" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>';
const row2Right = without(assetMarkup("DIAGRAM_COMPARE_L_COMPARE_ROW2_RIGHT"), X_PATH);

/** Rise-and-fade reveal for a full-frame diagram layer. */
const rise = (f: number, f0: number, dur = 10): Override => {
  const u = prog(f, f0, f0 + dur, E.out);
  return { opacity: u, pre: `translate(0 ${(40 * (1 - u)).toFixed(2)})` };
};

function Compare({ t }: { t: number }) {
  const A = shot("S09A").from, w = (id: string, n: string) => word(id, n) + shot(id).from - A;
  const b0 = shot("S09B").from - A;
  const tru = w("S09A", "true"), apr = w("S09A", "apr"), is = w("S09A", "is"), diff = w("S09A", "different");
  const leaving = w("S09B", "leaving"), trigger = w("S09B", "trigger"), interest = w("S09B", "interest"), that = w("S09B", "that");
  // the X strikes through the rewind arrow: two strokes drawn in turn (stroke-dash)
  const x1 = prog(t, interest, interest + 6), x2 = prog(t, interest + 5, interest + 11);
  const glow = prog(t, leaving, leaving + 8) * (1 - 0.6 * prog(t, b0 + 40, b0 + 60));
  const ov: Record<string, Override> = {
    [K("panel_left")]: rise(t, 2),
    [K("row1_labels")]: rise(t, apr - 2, 8),
    [K("row1_left")]: rise(t, is, 8),
    [K("row1_right")]: rise(t, diff, 8),
    [K("row2_labels")]: rise(t, b0 + 2, 8),
    [K("row2_left")]: rise(t, leaving + 2, 8),
    [K("row2_right")]: {
      node: <g opacity={fade(t, trigger, 8)}>
        <Raw m={row2Right} />
        <path d="M700 900 L860 1020" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - x1} fill="none" stroke={C.teal} strokeWidth={14} strokeLinecap="round" opacity={x1 > 0 ? 1 : 0} />
        <path d="M860 900 L700 1020" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - x2} fill="none" stroke={C.teal} strokeWidth={14} strokeLinecap="round" opacity={x2 > 0 ? 1 : 0} />
      </g>,
    },
    // F8 qualifier: appears with "for that 0% period" and stays until the cut
    [K("after_note")]: rise(t, that - 4, 8),
    // right column highlight while S09B talks about it
    [K("panel_right")]: { ...rise(t, tru), after: <rect x={553} y={323} width={484} height={914} rx={30} fill="none" stroke={C.teal_lt} strokeWidth={8} opacity={glow} /> },
  };
  const remy = poseTrack(t, [
    { f: tru - 6, pose: pose("remy", "stand_neutral", { expr: { preset: "neutral", gaze: [2, -6] } }) },
    { f: tru + 6, pose: pose("remy", "open_hands", { expr: { preset: "content", gaze: [2, -6] } }), switchAt: 0.5 },
    { f: leaving - 2, pose: pose("remy", "open_hands", { expr: { preset: "content", gaze: [5, -6] } }) },
    { f: leaving + 8, pose: pose("remy", "point_up", { expr: { preset: "determined", gaze: [5, -6] } }), switchAt: 0.5 },
  ]);
  ov.remy = { pose: remy, tf: REMY_TF };
  return <SceneWorld id="SCN_C11_COMPARE" ov={ov} />;
}

export const S09A: React.FC = () => <Compare t={useCurrentFrame()} />;
export const S09B: React.FC = () => <Compare t={useCurrentFrame() + shot("S09B").from - shot("S09A").from} />;
