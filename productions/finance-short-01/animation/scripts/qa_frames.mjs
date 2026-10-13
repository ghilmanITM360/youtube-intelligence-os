// Focused QA: render chosen frames of the timeline (one bundle, one browser) and tile them into a
// labelled contact sheet with ImageMagick. Usage:
//   node scripts/qa_frames.mjs <name> <frame>[,<frame>...] [--scale=0.35] [--cols=6]
// Frames are absolute timeline frames; "S05A+12" means 12 frames after the start of shot S05A.
import { bundle } from "@remotion/bundler";
import { openBrowser, renderStill, selectComposition } from "@remotion/renderer";
import { execFileSync } from "node:child_process";
import { mkdirSync, readFileSync } from "node:fs";
import path from "node:path";

const [name, list, ...rest] = process.argv.slice(2);
const opt = Object.fromEntries(rest.map((a) => a.replace(/^--/, "").split("=")));
const scale = Number(opt.scale ?? 0.35), cols = Number(opt.cols ?? 6);
const tl = JSON.parse(readFileSync(new URL("../src/data/bundle.json", import.meta.url), "utf8")).timeline;
const frames = list.split(",").map((x) => {
  const m = x.match(/^(S\d+[A-C]?)\+(\d+)$/);
  return m ? tl.shots.find((s) => s.id === m[1]).from + Number(m[2]) : Number(x);
});
const out = path.resolve("out/qa", name);
mkdirSync(out, { recursive: true });
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.ts") });
const browser = await openBrowser("chrome");
const composition = await selectComposition({ serveUrl, id: "FinanceShort01", puppeteerInstance: browser });
const files = [];
for (const frame of frames) {
  const file = path.join(out, `f${String(frame).padStart(4, "0")}.png`);
  await renderStill({ composition, serveUrl, frame, output: file, scale, puppeteerInstance: browser, overwrite: true });
  if (opt.crop) execFileSync("magick", [file, "-crop", opt.crop, "+repage", file]); // crop in output pixels
  const s = tl.shots.findLast((x) => x.from <= frame);
  files.push(["-label", `${frame} ${s.id}+${frame - s.from}`, file]);
}
await browser.close({ silent: true });
execFileSync("magick", ["montage", ...files.flat(), "-tile", `${cols}x`, "-geometry", "+6+6", "-font", opt.font ?? "/System/Library/Fonts/Helvetica.ttc", "-pointsize", "18",
  "-background", "#E9E4DA", path.join(out, "sheet.png")]);
console.log(path.join(out, "sheet.png"));
