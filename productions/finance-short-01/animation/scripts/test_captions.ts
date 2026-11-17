import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { activeCaption, captionLayout, CAPTION_METRICS, CAPTION_Y } from "../src/lib/captions.ts";
const timeline = JSON.parse(readFileSync(new URL("../src/data/bundle.json", import.meta.url), "utf8")).timeline;
for (const shot of timeline.shots) {
  for (const frame of [shot.from, shot.from + 1, shot.to - 1]) {
    const active = activeCaption(frame, timeline.captions, timeline.shots);
    if (active) {
      assert.equal(active.caption.shot, shot.id, `frame ${frame}: caption cannot carry from another shot`);
      assert.ok(active.end <= shot.to, `frame ${frame}: caption hold must end at shot cut`);
    }
  }
}
const shots = [{id:"a",from:0,to:20},{id:"b",from:20,to:40}];
const captions = [{shot:"a",text:"a",from:2,to:10},{shot:"b",text:"b",from:30,to:35}];
assert.equal(activeCaption(25,captions,shots),null,"gap before next caption must stay empty");
assert.equal(activeCaption(40,captions,shots),null,"no caption after timeline ends");
console.log("caption tests: PASS (shot cuts, holds, gaps, end boundary)");

for (const c of timeline.captions) {
  const l = captionLayout(c.text, CAPTION_Y[c.shot] ?? CAPTION_METRICS.defaultY);
  assert.ok(l.size >= 40, `${c.shot}: readable caption size`);
  assert.ok(l.x >= 40 && l.x + l.width <= 890, `${c.shot}: caption outside simulated right UI rail with 10px margin`);
  assert.ok(l.y >= 100 && l.y + l.height <= 1590, `${c.shot}: caption outside simulated top/bottom UI bands with margin`);
}
