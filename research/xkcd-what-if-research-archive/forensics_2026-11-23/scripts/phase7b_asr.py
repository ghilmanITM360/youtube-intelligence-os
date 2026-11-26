"""Phase 7b: local whisper.cpp (small.en) segment timestamps for the 20 long videos that have media but no campaign ASR.
Read-only on media. ASR is a machine transcript (not listening), uncertified."""
import csv, glob, subprocess, os
from pathlib import Path
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent / 'phase7b_asr'
LIB = '/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
M = Path.home() / '.cache/hyperframes/whisper/models/ggml-small.en.bin'
t = {r['video_id'] for r in csv.DictReader(open(OUT.parent / '06_ALIGNED_TIMING_TABLE.csv'))}
V = sorted(r['video_id'] for r in csv.DictReader(open(C / 'campaign/campaign_matrix.csv')) if r['format'] == 'LONG_FORM' and r['video_id'] not in t)
for v in V:
    g = glob.glob(LIB + f'*[[]{v}[]].mp4')
    if not g or (OUT / f'{v}.json').exists(): continue
    wav = OUT / f'{v}.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', g[0], '-ar', '16000', '-ac', '1', str(wav)], check=True)
    subprocess.run(['whisper-cli', '-m', str(M), '-f', str(wav), '-oj', '-of', str(OUT / v), '-np'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wav.unlink(); print('done', v, flush=True)
