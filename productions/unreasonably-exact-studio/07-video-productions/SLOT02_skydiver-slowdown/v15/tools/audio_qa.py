"""Narration intelligibility metrics (supporting evidence only; not a substitute for listening).
For every 0.4 s window inside Hamza's phrases: voice stem level minus summed background level,
broadband and in the speech band (300 Hz - 4 kHz). Also stem/master loudness and true peak.
  .venv/bin/python tools/audio_qa.py <stems_dir> <master.wav> [label]  -> prints + appends qa/audio_qa.json
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
SR = 48000
def rd(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(p), '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(float)
def bandpass(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR); return np.fft.irfft(X * ((f >= lo) & (f <= hi)), len(x))
def ebu(p):
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(p), '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    tail = out[out.rfind('Summary'):]
    g = lambda k: float(re.search(k + r':\s*(-?[\d.inf]+)', tail).group(1))
    return dict(I=g('I'), LRA=g('LRA'), TP=g('Peak'))
def main(stems, master, label):
    stems = Path(stems); v = rd(stems / 'VOICEOVER.wav')
    bg_files = [p for p in stems.glob('*.wav') if p.stem not in ('VOICEOVER', 'LIBRARY_REVIEW')]
    b = sum(rd(p) for p in bg_files); n = min(len(v), len(b)); v, b = v[:n], b[:n]
    vb, bb = bandpass(v, 300, 4000), bandpass(b, 300, 4000)
    narr = json.loads((ROOT / 'audio/narration_v14.json').read_text())
    W = int(.4 * SR); bro, spb = [], []
    for q in narr['cues']:
        for s in range(int(q['speech_start'] * SR), int(q['speech_end'] * SR) - W, W // 2):
            rv = np.sqrt(np.mean(v[s:s + W] ** 2))
            if rv < .01: continue          # voiced windows only (> -40 dBFS); in-phrase breaths are not words
            bro.append((s / SR, 20 * np.log10(rv / (np.sqrt(np.mean(b[s:s + W] ** 2)) + 1e-9))))
            spb.append((s / SR, 20 * np.log10(np.sqrt(np.mean(vb[s:s + W] ** 2)) / (np.sqrt(np.mean(bb[s:s + W] ** 2)) + 1e-9))))
    def summ(a):
        x = np.array([y for _, y in a]); worst = sorted(a, key=lambda r: r[1])[:3]
        return dict(windows=len(x), median=round(float(np.median(x)), 1), p10=round(float(np.percentile(x, 10)), 1), min=round(float(x.min()), 1),
                    worst=[(round(t, 2), round(y, 1)) for t, y in worst])
    res = dict(label=label, background_stems=sorted(p.stem for p in bg_files), broadband=summ(bro), speech_band=summ(spb),
               voice_stem=ebu(stems / 'VOICEOVER.wav'), background_sum_I=None, master=ebu(master))
    tmp = ROOT / 'qa/_bg.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f64le', '-ac', '1', '-ar', str(SR), '-i', '-', str(tmp)], input=b.tobytes(), check=True)
    res['background_sum_I'] = ebu(tmp)['I']; tmp.unlink()
    res['voice_minus_background_LU'] = round(res['voice_stem']['I'] - res['background_sum_I'], 1)
    print(json.dumps(res, indent=1))
    log = ROOT / 'qa/audio_qa.json'; allr = json.loads(log.read_text()) if log.exists() else []
    allr = [r for r in allr if r['label'] != label] + [res]; log.write_text(json.dumps(allr, indent=1))
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'run')
