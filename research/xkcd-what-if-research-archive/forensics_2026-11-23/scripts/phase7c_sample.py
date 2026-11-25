"""Phase 7c sample: ONE frame per Short with media. Rule: ASR segments matching the Phase 7 quantity regex; the hit nearest 1/2 of the runtime;
still frame at segment midpoint; fit into 360x640 cells (letterboxed if not portrait). Shorts with no quantity hit are listed, not sampled.
ASR = campaign faster-whisper where it exists, else local whisper.cpp small.en."""
import csv, glob, json, re, subprocess
from pathlib import Path
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent
LIB = '/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
QTY = re.compile(r'\d|\b(times|meters?|metres?|miles?|feet|foot|kilomet\w+|percent|tons?|kilograms?|pounds?|degrees|billion|million|thousand|hundred|bigger|larger|smaller|heavier|faster|size of|as big|as wide)\b', re.I)
(OUT / 'phase7c_frames').mkdir(exist_ok=True)
rows, none = [], []
for i in csv.DictReader(open(OUT / '07c_SHORTS_INVENTORY.csv')):
    if i['media'] != 'True': continue
    v = i['video_id']
    if i['asr_source'] == 'campaign': seg = [dict(start=s['start'], end=s['end'], text=s['text'].strip()) for s in json.load(open(C / f'videos/{v}/asr/asr_small_en.json'))['segments']]
    else: seg = [dict(start=s['offsets']['from']/1000, end=s['offsets']['to']/1000, text=s['text'].strip()) for s in json.load(open(OUT / f'phase7c_asr/{v}.json'))['transcription']]
    dur = seg[-1]['end']; hits = [s for s in seg if QTY.search(s['text'])]
    if not hits: none.append(v); continue
    s = min(hits, key=lambda s: abs((s['start'] + s['end']) / 2 - dur / 2)); tm = round((s['start'] + s['end']) / 2, 2); fn = f'phase7c_frames/{v}.jpg'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(tm), '-i', glob.glob(LIB + f'*[[]{v}[]].mp4')[0], '-frames:v', '1', '-vf', 'scale=360:640:force_original_aspect_ratio=decrease,pad=360:640:(ow-iw)/2:(oh-ih)/2:color=gray', str(OUT / fn)], check=True)
    rows.append(dict(frame=fn, video_id=v, t=tm, asr_source=i['asr_source'], spoken=s['text']))
with open(OUT / '07c_SAMPLE_FRAMES.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
n = len(rows)
for k in range((n + 5) // 6):
    ch = rows[k*6:(k+1)*6]; m = len(ch); cmd = ['ffmpeg', '-v', 'error', '-y']
    for c in ch: cmd += ['-i', str(OUT / c['frame'])]
    lay = '|'.join(f'{(i%3)*360}_{(i//3)*640}' for i in range(m))
    fl = ''.join(f'[{i}:v]null[v{i}];' for i in range(m)) + ''.join(f'[v{i}]' for i in range(m)) + (f'xstack=inputs={m}:layout={lay}' if m > 1 else 'copy')
    subprocess.run(cmd + ['-filter_complex', fl, str(OUT / f'phase7c_frames/sheet{k+1}.jpg')], check=True)
print(n, 'frames;', len(none), 'Shorts without a quantity hit:', none)
