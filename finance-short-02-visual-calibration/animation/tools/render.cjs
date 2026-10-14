#!/usr/bin/env node
// Frame-accurate renderer: serves the project locally, drives headless Chrome over CDP, seeks
// player.html to each frame time and pipes PNG screenshots into ffmpeg with the original WAV.
// No npm dependencies (Node >= 22 for global WebSocket).
//
//   node animation/tools/render.cjs --out animation/Finance_Short_02_FINAL.mp4
//   node animation/tools/render.cjs --out animation/Finance_Short_02_PREVIEW.mp4 --scale 0.5
//   node animation/tools/render.cjs --png-dir /tmp/frames --times 0,3.2,10 [--nocam]
//   node animation/tools/render.cjs --out clip.mp4 --from 0 --to 8 --scale 0.5
const http = require('node:http'), fs = require('node:fs'), path = require('node:path'), os = require('node:os');
const { spawn } = require('node:child_process');

const ROOT = path.resolve(__dirname, '../..');
const args = Object.fromEntries(process.argv.slice(2).reduce((a, x, i, all) => (x.startsWith('--') && a.push([x.slice(2), all[i + 1]?.startsWith('--') || all[i + 1] === undefined ? true : all[i + 1]]), a), []));
const CHROME = args.chrome || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const TL = JSON.parse(fs.readFileSync(path.join(ROOT, 'animation/KEYFRAME_TIMELINE.json')));
const fps = TL.fps, scale = Number(args.scale || 1);

const TYPES = { '.html': 'text/html', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.wav': 'audio/wav', '.js': 'text/javascript' };
const server = http.createServer((req, res) => {
  const p = path.normalize(path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname)));
  if (!p.startsWith(ROOT + path.sep) || !fs.existsSync(p) || !fs.statSync(p).isFile()) return res.writeHead(404).end();
  res.writeHead(200, { 'content-type': TYPES[path.extname(p)] || 'application/octet-stream' });
  fs.createReadStream(p).pipe(res);
});

function cdp(wsUrl) {
  const ws = new WebSocket(wsUrl);
  let id = 0;
  const pending = new Map();
  ws.onmessage = m => {
    const d = JSON.parse(m.data);
    if (d.id && pending.has(d.id)) { const { ok, ko } = pending.get(d.id); pending.delete(d.id); d.error ? ko(new Error(JSON.stringify(d.error))) : ok(d.result); }
  };
  const send = (method, params = {}, sessionId) => new Promise((ok, ko) => { const i = ++id; pending.set(i, { ok, ko }); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
  return new Promise(r => (ws.onopen = () => r({ send, close: () => ws.close() })));
}

async function main() {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'fs02-chrome-'));
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio', '--no-first-run', '--no-default-browser-check',
    '--disable-extensions', '--disable-background-networking', '--disable-component-update', '--disable-sync', '--force-color-profile=srgb', '--num-raster-threads=1', '--disable-partial-raster',
    '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank'], { stdio: ['ignore', 'ignore', 'pipe'] });
  const wsUrl = await new Promise((ok, ko) => {
    let buf = '';
    chrome.stderr.on('data', d => { buf += d; const m = buf.match(/DevTools listening on (ws:\/\/\S+)/); if (m) ok(m[1]); });
    setTimeout(() => ko(new Error('Chrome did not start: ' + buf.slice(-500))), 20000);
  });
  const b = await cdp(wsUrl);
  const { targetId } = await b.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.send('Target.attachToTarget', { targetId, flatten: true });
  const send = (m, p) => b.send(m, p, sessionId);
  await send('Emulation.setDeviceMetricsOverride', { width: TL.width, height: TL.height, deviceScaleFactor: scale, mobile: false });
  await send('Page.enable');
  await send('Page.navigate', { url: `http://127.0.0.1:${port}/animation/player.html?render=1${args.nocam ? '&nocam=1' : ''}` });
  for (let i = 0; ; i++) {
    const r = await send('Runtime.evaluate', { expression: 'window.__ready === true', returnByValue: true });
    if (r.result.value) break;
    if (i > 600) throw new Error('player never became ready');
    await new Promise(r => setTimeout(r, 50));
  }
  const shot = async t => {
    await send('Runtime.evaluate', { expression: `__render(${t})`, awaitPromise: true });
    const { data } = await send('Page.captureScreenshot', { format: 'png', fromSurface: true, captureBeyondViewport: false });
    return Buffer.from(data, 'base64');
  };

  if (args['state-svgs']) {  // authored reference: each SCENE_ASSET_MAP state SVG rendered by the same browser
    fs.mkdirSync(args['state-svgs'], { recursive: true });
    for (const st of TL.states) {
      await send('Page.navigate', { url: `http://127.0.0.1:${port}/assets/scene_compositions/${st.id}.svg` });
      for (let i = 0; i < 200; i++) {
        const r = await send('Runtime.evaluate', { expression: 'document.readyState', returnByValue: true });
        if (r.result.value === 'complete') break;
        await new Promise(r => setTimeout(r, 25));
      }
      await new Promise(r => setTimeout(r, 150));
      const { data } = await send('Page.captureScreenshot', { format: 'png', fromSurface: true });
      fs.writeFileSync(path.join(args['state-svgs'], st.id + '.png'), Buffer.from(data, 'base64'));
    }
  } else if (args.times) {  // spot frames for QA
    fs.mkdirSync(args['png-dir'], { recursive: true });
    for (const t of String(args.times).split(',').map(Number)) {
      const f = Math.round(t * fps);
      fs.writeFileSync(path.join(args['png-dir'], `f${String(f).padStart(5, '0')}.png`), await shot(f / fps));
    }
  } else {
    const f0 = Math.round(Number(args.from || 0) * fps);
    const f1 = args.to ? Math.round(Number(args.to) * fps) : TL.frames;
    const wav = path.join(ROOT, 'animation', TL.audio);
    const ff = spawn('ffmpeg', ['-y', '-hide_banner', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-',
      '-ss', String(f0 / fps), '-t', String((f1 - f0) / fps), '-i', wav, '-map', '0:v', '-map', '1:a',
      '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv', '-c:v', 'libx264', '-preset', 'slow', '-crf', String(args.crf || 16),
      '-tune', 'animation', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
      '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-af', args.gain ? `volume=${args.gain}dB` : 'anull',
      '-movflags', '+faststart', '-t', String((f1 - f0) / fps), path.resolve(args.out)], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((ok, ko) => ff.on('close', c => (c ? ko(new Error('ffmpeg exit ' + c)) : ok())));
    const t0 = Date.now();
    for (let f = f0; f < f1; f++) {
      const png = await shot(f / fps);
      if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 150 === 0) process.stderr.write(`frame ${f}/${f1} ${((Date.now() - t0) / 1000).toFixed(0)}s\n`);
    }
    ff.stdin.end();
    await done;
  }
  b.close(); server.close();
  const exited = new Promise(r => chrome.once('exit', r));
  chrome.kill();
  await exited;
  try { fs.rmSync(profile, { recursive: true, force: true, maxRetries: 5 }); } catch { /* temp profile; OS cleans it */ }
}
main().catch(e => { console.error(e); process.exit(1); });
