"""Phase 7 sample: deterministic selection of quantity/scale moments from ASR, frame extraction, contact sheets.
Rule: 24 long videos sorted by id, take every 2nd (12). In each, ASR segments matching QTY regex; take the 2 hits
closest to 1/3 and 2/3 of the runtime. Frame at segment midpoint. Read-only on media."""
import csv, json, re, subprocess, glob
from pathlib import Path
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent
LIB = '/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
QTY = re.compile(r'\d|\b(times|meters?|metres?|miles?|feet|foot|kilomet\w+|percent|tons?|kilograms?|pounds?|degrees|billion|million|thousand|hundred|bigger|larger|smaller|heavier|faster|size of|as big|as wide)\b', re.I)
t = list(csv.DictReader(open(OUT / '06_ALIGNED_TIMING_TABLE.csv')))
L = sorted(r['video_id'] for r in t if r['format'] == 'LONG_FORM')[::2]
rows = []
for vid in L:
    a = json.load(open(C / 'videos' / vid / 'asr/asr_small_en.json')); dur = a['duration_s']
    hits = [s for s in a['segments'] if QTY.search(s['text'])]
    picks = []
    for frac in (1/3, 2/3):
        c = [s for s in hits if s not in picks]
        if c: picks.append(min(c, key=lambda s: abs((s['start'] + s['end']) / 2 - frac * dur)))
    f = glob.glob(LIB + f'*[[]{vid}[]].mp4')[0]
    for i, s in enumerate(picks):
        tm = round((s['start'] + s['end']) / 2, 2); fn = f'phase7_frames/{vid}_{i}.jpg'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(tm), '-i', f, '-frames:v', '1', '-vf', 'scale=640:-1', str(OUT / fn)], check=True)
        rows.append(dict(frame=fn, video_id=vid, t=tm, spoken=s['text'].strip()))
w = csv.DictWriter(open(OUT / '07_SAMPLE_FRAMES.csv', 'w', newline=''), fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
print(len(rows), 'frames from', len(L), 'videos')
