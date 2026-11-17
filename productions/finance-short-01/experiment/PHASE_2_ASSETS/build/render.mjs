// Rasterize SVG files to PNG with the same Sharp/librsvg runtime used in Phase 1.
// Usage: node build/render.mjs jobs.json   (jobs: [{svg, png, width?}])
import fs from 'node:fs';
import sharp from 'sharp';

const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
for (const job of jobs) {
  let img = sharp(fs.readFileSync(job.svg), {density: job.density || 72});
  if (job.width) img = img.resize({width: job.width});
  await img.png({compressionLevel: 9}).toFile(job.png);
}
console.log(`rendered ${jobs.length} PNG(s)`);
