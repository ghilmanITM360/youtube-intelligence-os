import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

test('renderer works from an unrelated cwd with local locked dependencies', () => {
  const dir = mkdtempSync(path.join(tmpdir(), 'finance-render-'));
  try {
    const svg = path.join(dir, 'test.svg'), png = path.join(dir, 'test.png');
    writeFileSync(svg, '<svg xmlns="http://www.w3.org/2000/svg" width="8" height="8"><rect width="8" height="8" fill="red"/></svg>');
    const jobs = path.join(dir, 'jobs.json');
    writeFileSync(jobs, JSON.stringify([{svg, png, width:16}]));
    execFileSync(process.execPath, [new URL('./render.mjs', import.meta.url).pathname, jobs], {cwd:dir});
    const bytes = readFileSync(png);
    assert.equal(bytes.subarray(1,4).toString(), 'PNG');
    assert.equal(bytes.readUInt32BE(16), 16);
    assert.equal(bytes.readUInt32BE(20), 16);
    execFileSync(process.execPath, [new URL('./render.mjs', import.meta.url).pathname, jobs], {cwd:dir});
    assert.deepEqual(readFileSync(png), bytes);
  } finally { rmSync(dir, {recursive:true, force:true}); }
});
