"""Phase 9 (machine signals only, NOT listening): EBU R128 loudness + silence ratio for every library MP4.
ffmpeg ebur128 + silencedetect (-50 dB, >=0.35 s). Read-only on media. Run: python3 -I phase9_audio_levels.py"""
import csv, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
LIB = Path('/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel')
OUT = Path(__file__).resolve().parent.parent
def one(p):
    vid = re.search(r'\[([^\]]+)\]\.mp4$', p.name).group(1)
    r = subprocess.run(['ffmpeg', '-nostats', '-i', str(p), '-vn', '-af', 'ebur128=peak=true,silencedetect=n=-50dB:d=0.35', '-f', 'null', '-'], capture_output=True, text=True)
    e = r.stderr
    def g(pat):
        m = re.findall(pat, e); return float(m[-1]) if m else ''
    sil = [float(x) for x in re.findall(r'silence_duration: ([\d.]+)', e)]
    dur = re.findall(r'Duration: (\d+):(\d+):([\d.]+)', e); d = int(dur[0][0]) * 3600 + int(dur[0][1]) * 60 + float(dur[0][2]) if dur else ''
    return dict(video_id=vid, duration_s=round(d, 2) if d != '' else '', integrated_lufs=g(r'I:\s+(-?[\d.]+) LUFS'), lra_lu=g(r'LRA:\s+([\d.]+) LU'),
                true_peak_dbtp=g(r'Peak:\s+(-?[\d.]+) dBFS'), silence_events=len(sil), silence_total_s=round(sum(sil), 2), silence_ratio=round(sum(sil) / d, 4) if d else '')
files = sorted(LIB.glob('*.mp4'))
with ThreadPoolExecutor(4) as ex: rows = list(ex.map(one, files))
with open(OUT / '09_AUDIO_LEVELS_88.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('done', len(rows))
