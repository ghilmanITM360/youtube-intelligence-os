// Timeline / sync checks on the generated bundle. Run: node scripts/test_timeline.ts
import { captionLayout } from "../src/lib/captions.ts";
import { readFileSync } from "node:fs";

const B = JSON.parse(readFileSync(new URL("../src/data/bundle.json", import.meta.url), "utf8"));
const T = B.timeline;
let fails = 0;
const check = (ok: boolean, msg: string) => { if (!ok) { fails++; console.error("FAIL", msg); } };

check(T.shots.length === 21 && T.phrases.length === 21, `21 shots / 21 phrases (got ${T.shots.length}/${T.phrases.length})`);
check(T.shots[0].from === 0 && T.shots.at(-1).to === T.frames_total, "shots cover the whole timeline");
T.shots.forEach((s: any, i: number) => {
  if (i) check(s.from === T.shots[i - 1].to, `${s.id} starts where ${T.shots[i - 1].id} ends`);
  check(s.to > s.from, `${s.id} has frames`);
  const p = T.phrases[s.phrase];
  check(p.from >= s.from && p.to <= s.to, `${s.id}: its phrase ${p.from}-${p.to} sits inside the shot ${s.from}-${s.to}`);
  check(B.scenes[s.scene] !== undefined, `${s.id}: scene ${s.scene} exists`);
});
for (const w of T.words) {
  const p = T.phrases[w.phrase];
  check(w.from >= p.from && w.to <= p.to && w.to >= w.from, `word ${w.i} "${w.text}" inside its phrase`);
}
const lastWord = T.words.at(-1);
check(lastWord.to <= T.frames_total, "narration not truncated by the timeline");
const audioFrames = Math.round(T.audio.duration_s * T.fps);
check(T.frames_total >= audioFrames && T.frames_total - audioFrames <= 12, `timeline ${T.frames_total} f covers audio ${audioFrames} f plus a short end hold`);
for (const c of T.captions) {
  const s = T.shots.find((x: any) => x.id === c.shot);
  check(c.from >= s.from && c.to <= s.to, `caption "${c.text}" inside ${c.shot}`);
  const size = captionLayout(c.text, 0).size; // shared CaptionPlate geometry
  check(size >= 40, `caption "${c.text}" fits one line at >= 40 px (got ${size.toFixed(1)})`);
}
// every scene instance resolves to a registered asset (or carries its own generator markup)
for (const [id, sc] of Object.entries(B.scenes) as [string, any][]) for (const i of [...sc.world, ...sc.ui]) {
  check(i.char || (i.m ? B.markup[i.m] : B.assets[i.asset]), `${id}:${i.id} asset ${i.asset} resolves`);
}
check(!T.gate.final_sync_allowed || T.gate.result.startsWith("PASS"), "final sync only when the pronunciation gate passed");
console.log(fails ? `timeline tests: ${fails} FAILED` : `timeline tests: PASS (${T.shots.length} shots, ${T.words.length} words, ${T.captions.length} captions; gate ${T.gate.result}, final sync ${T.gate.final_sync_allowed ? "ALLOWED" : "BLOCKED"})`);
process.exit(fails ? 1 : 0);
