#!/usr/bin/env python3
"""QA for the rendered Short. Needs Pillow + numpy (already used by the asset pipeline).

  states <ref_dir> <hold_dir>   authored state SVG vs player frame at each state's last frame (camera off)
  sheet <mp4> <png>             FINAL_CONTACT_SHEET: one tile per state at its last frame
  video <mp4> [--narration]     decode check, stream facts, blank/frozen frame scan, audio peaks, narration sync
                                (compares against audio_mix when built; --narration for a narration-only file)
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
TL = json.loads((ROOT / 'animation/KEYFRAME_TIMELINE.json').read_text())


def states(ref_dir, hold_dir):
    holds = sorted(Path(hold_dir).glob('f*.png'))
    out = []
    for st, hp in zip(TL['states'], holds):
        a = np.asarray(Image.open(Path(ref_dir) / f"{st['id']}.png").convert('RGB'), dtype=np.int16)
        b = np.asarray(Image.open(hp).convert('RGB'), dtype=np.int16)
        d = np.abs(a - b).max(axis=2) > 48
        ys, xs = np.nonzero(d)
        box = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())] if len(xs) else None
        out.append(dict(state=st['id'], frame=hp.stem, diff_pct=round(100 * d.mean(), 3), diff_box=box))
    return out


def video(mp4):
    probe = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', mp4], capture_output=True, text=True).stdout)
    dec = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-f', 'null', '-'], capture_output=True, text=True).stderr.strip()
    v = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    w, h = 270, 480  # scan at quarter size: enough to see blank, frozen or flicker frames
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-vf', f'scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.int16)
    ink = (fr < 200).mean(axis=(1, 2))  # share of non-white pixels
    blank = [i for i, x in enumerate(ink) if x < 0.002]
    black = [i for i, x in enumerate(fr.mean(axis=(1, 2))) if x < 16]
    change = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
    still, run, longest = 0, 0, (0, 0)
    for i, c in enumerate(change):
        run = run + 1 if c < 0.01 else 0
        if run > longest[0]:
            longest = (run, i + 1 - run)
    # flicker: a frame that differs from both neighbours while the neighbours match each other
    flicker = [i for i in range(1, len(fr) - 1) if np.abs(fr[i - 1] - fr[i + 1]).mean() < 0.05 and change[i - 1] > 0.5]
    ast = subprocess.run(['ffmpeg', '-v', 'info', '-nostats', '-i', mp4, '-map', '0:a', '-af', 'astats=measure_perchannel=0,ebur128=peak=true', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    peak = [l.split(':')[-1].strip() for l in ast.splitlines() if 'Peak level dB' in l]
    tp = [l.split(':')[-1].strip() for l in ast.splitlines() if l.strip().startswith('Peak:')]
    a = next(s for s in probe['streams'] if s['codec_type'] == 'audio')
    # audio fidelity: decoded AAC vs the soundtrack it was encoded from (both 48 kHz mono float), zero-lag SNR
    mix = TL.get('audio_mix') if TL.get('audio_mix') and (ROOT / 'animation' / TL['audio_mix']).exists() and '--narration' not in sys.argv else None
    wav = ROOT / 'animation' / (mix or TL['audio'])
    pcm = lambda src: np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', str(src), '-map', '0:a', '-ac', '1', '-ar', '48000', '-f', 'f32le', '-'],
                                                   capture_output=True).stdout, np.float32).astype(np.float64)
    x, y = pcm(wav), pcm(mp4)
    n = min(len(x), len(y))
    snr = 10 * np.log10((x[:n] ** 2).sum() / max(1e-12, ((x[:n] - y[:n]) ** 2).sum()))
    # narration preserved: best-fit gain and lag of the original WAV inside the delivered audio
    nv = pcm(ROOT / 'animation' / TL['audio']); m = len(nv)
    lags = range(-240, 241, 8)  # +-5 ms
    corr = [float(np.dot(nv[2400:m - 2400], y[2400 + L:m - 2400 + L])) for L in lags]
    lag = list(lags)[int(np.argmax(corr))]
    g = float(np.dot(nv, y[:m]) / np.dot(nv, nv))
    rest = y[:m] - g * nv
    narration = dict(lag_samples=lag, fitted_gain_db=round(20 * np.log10(g), 2),
                     narration_to_rest_db=round(float(10 * np.log10((g * nv) @ (g * nv) / (rest @ rest))), 1), mp4_samples_48k=len(y), expected_samples_48k=round(TL['frames'] / TL['fps'] * 48000))
    # sync: the encoded file's hard cuts must land on the timeline's cut frames
    cuts = [round(st['start'] * TL['fps']) for st in TL['states'] if st['cut'] and st['start'] > 0]
    # change[i] is frame i -> i+1, so a cut on frame c peaks at change[c-1]; report the peak's offset in +-4 frames
    cut_hits = {c: int(np.argmax(change[c - 5:c + 3])) - 4 for c in cuts}
    return dict(file=mp4, bytes=int(probe['format']['size']), duration=float(probe['format']['duration']),
                video=dict(codec=v['codec_name'], profile=v.get('profile'), pix_fmt=v['pix_fmt'], width=v['width'], height=v['height'], fps=v['r_frame_rate'],
                           frames=int(v.get('nb_frames', len(fr))), duration=float(v['duration']), color=[v.get('color_space'), v.get('color_primaries'), v.get('color_transfer')]),
                audio=dict(codec=a['codec_name'], sample_rate=a['sample_rate'], channels=a['channels'], duration=float(a['duration']),
                           sample_peak_dbfs=peak[-1] if peak else None, true_peak_dbtp=tp[-1] if tp else None),
                decode_errors=dec or 'none', decoded_frames=len(fr), blank_frames=blank, black_frames=black,
                longest_identical_run=dict(frames=longest[0], start_frame=longest[1], start_sec=round(longest[1] / TL['fps'], 2)),
                flicker_frames=flicker,
                audio_vs_source=dict(source=str(wav.relative_to(ROOT)), source_samples_48k=len(x), mp4_samples_48k=len(y), snr_db=round(float(snr), 1)), narration_in_audio=narration,
                cut_sync_frame_error=cut_hits)


def sheet(mp4, out):
    """One tile per storyboard state, taken from the encoded video at that state's last frame."""
    from PIL import ImageDraw, ImageFont
    w, h, lab, cols = 270, 480, 30, 6
    font = ImageFont.load_default(size=17)
    st = TL['states']
    img = Image.new('RGB', (cols * w, -(-len(st) // cols) * (h + lab)), 'white')
    d = ImageDraw.Draw(img)
    for i, s in enumerate(st):
        f = round(s['end'] * TL['fps']) - 1
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-vf', f'select=eq(n\\,{f}),scale={w}:{h}', '-vframes', '1', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True).stdout
        x, y = (i % cols) * w, (i // cols) * (h + lab)
        img.paste(Image.frombytes('RGB', (w, h), raw), (x, y + lab))
        d.text((x + 6, y + 6), f"{s['id']}  {s['start']:.2f}-{s['end']:.2f}s{'  CUT' if s['cut'] else ''}", fill='#222', font=font)
        d.rectangle([x, y + lab, x + w - 1, y + lab + h - 1], outline='#bbb')
    img.save(out, optimize=True)
    return dict(sheet=out, tiles=len(st))


if __name__ == '__main__':
    cmd = sys.argv[1]
    r = states(*sys.argv[2:4]) if cmd == 'states' else sheet(*sys.argv[2:4]) if cmd == 'sheet' else video(sys.argv[2])
    print(json.dumps(r, indent=1))
