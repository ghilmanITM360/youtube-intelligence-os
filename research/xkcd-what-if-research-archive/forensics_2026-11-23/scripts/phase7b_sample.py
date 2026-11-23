"""Phase 7b: same selection rule as phase7_sample.py, on the 20 long videos with no campaign ledger/ASR.
ASR = local whisper.cpp small.en segments (phase7b_asr/*.json). Rule: ASR segments matching QTY; the 2 hits closest to
1/3 and 2/3 of runtime (runtime = last segment end); still frame at segment midpoint; 640 px wide."""
import csv, glob, json, re, subprocess
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent
LIB = '/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
QTY = re.compile(r'\d|\b(times|meters?|metres?|miles?|feet|foot|kilomet\w+|percent|tons?|kilograms?|pounds?|degrees|billion|million|thousand|hundred|bigger|larger|smaller|heavier|faster|size of|as big|as wide)\b', re.I)
rows = []
for jf in sorted((OUT / 'phase7b_asr').glob('*.json')):
    vid = jf.stem; seg = [dict(start=s['offsets']['from'] / 1000, end=s['offsets']['to'] / 1000, text=s['text'].strip()) for s in json.load(open(jf))['transcription']]
    dur = seg[-1]['end']; hits = [s for s in seg if QTY.search(s['text'])]; picks = []
    for frac in (1/3, 2/3):
        c = [s for s in hits if s not in picks]
        if c: picks.append(min(c, key=lambda s: abs((s['start'] + s['end']) / 2 - frac * dur)))
    f = glob.glob(LIB + f'*[[]{vid}[]].mp4')[0]
    for i, s in enumerate(picks):
        tm = round((s['start'] + s['end']) / 2, 2); fn = f'phase7b_frames/{vid}_{i}.jpg'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(tm), '-i', f, '-frames:v', '1', '-vf', 'scale=640:-1', str(OUT / fn)], check=True)
        rows.append(dict(frame=fn, video_id=vid, t=tm, spoken=s['text']))
with open(OUT / '07b_SAMPLE_FRAMES.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
n = len(rows)
for k in range((n + 5) // 6):
    ch = rows[k*6:(k+1)*6]; m = len(ch); cmd = ['ffmpeg', '-v', 'error', '-y']
    for c in ch: cmd += ['-i', str(OUT / c['frame'])]
    lay = '|'.join(f'{(i%2)*640}_{(i//2)*360}' for i in range(m))
    fl = ''.join(f'[{i}:v]scale=640:360[v{i}];' for i in range(m)) + ''.join(f'[v{i}]' for i in range(m)) + (f'xstack=inputs={m}:layout={lay}' if m > 1 else 'copy')
    subprocess.run(cmd + ['-filter_complex', fl, str(OUT / f'phase7b_frames/sheet{k+1}.jpg')], check=True)
print(n, 'frames,', len(set(r['video_id'] for r in rows)), 'videos,', (n + 5) // 6, 'sheets')
