"""Phase 7c: Shorts. Campaign ASR is used where it exists; local whisper.cpp small.en (segments) for Shorts with media and no campaign ASR.
Writes phase7c_asr/<id>.json (whisper) and phase7c_inventory.csv."""
import csv, glob, subprocess
from pathlib import Path
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent / 'phase7c_asr'; OUT.mkdir(exist_ok=True)
LIB = '/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
M = Path.home() / '.cache/hyperframes/whisper/models/ggml-small.en.bin'
inv = []
for r in csv.DictReader(open(C / 'campaign/campaign_matrix.csv')):
    if r['format'] != 'SHORT': continue
    v = r['video_id']; g = glob.glob(LIB + f'*[[]{v}[]].mp4'); camp = (C / f'videos/{v}/asr/asr_small_en.json').exists()
    inv.append(dict(video_id=v, media=bool(g), campaign_asr=camp, asr_source='campaign' if camp else ('whisper_small_en' if g else 'none')))
with open(OUT.parent / '07c_SHORTS_INVENTORY.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=list(inv[0])); w.writeheader(); w.writerows(inv)
print('shorts', len(inv), 'media', sum(i['media'] for i in inv), 'campaign asr', sum(i['campaign_asr'] for i in inv), 'need whisper', sum(i['asr_source'] == 'whisper_small_en' for i in inv), flush=True)
for i in inv:
    if i['asr_source'] != 'whisper_small_en' or (OUT / f"{i['video_id']}.json").exists(): continue
    v = i['video_id']; wav = OUT / f'{v}.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', glob.glob(LIB + f'*[[]{v}[]].mp4')[0], '-ar', '16000', '-ac', '1', str(wav)], check=True)
    subprocess.run(['whisper-cli', '-m', str(M), '-f', str(wav), '-oj', '-of', str(OUT / v), '-np'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wav.unlink(); print('done', v, flush=True)
print('ALL DONE', flush=True)
