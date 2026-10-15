from pathlib import Path
import whisper,json,csv,torch,argparse
R=Path(__file__).resolve().parents[1]
torch.set_num_threads(4)
parser=argparse.ArgumentParser();parser.add_argument('--model',choices=['base','small.en'],default='base');args=parser.parse_args()
suffix='_SMALL_EN' if args.model=='small.en' else ''
m=whisper.load_model(args.model)
for p in sorted(R.glob('0*/source_audio/narration_mix.wav')):
 out=p.parents[1]/'script'; dest=out/f'ASR{suffix}.json'
 if dest.exists():continue
 r=m.transcribe(str(p),language='en',word_timestamps=True,fp16=False,verbose=False,condition_on_previous_text=False)
 r['verification']='ASR_MACHINE_ALIGNED_NOT_HUMAN_VERIFIED';r['model']='openai-whisper '+args.model
 dest.write_text(json.dumps(r,indent=2)); (out/f'TRANSCRIPT{suffix}.txt').write_text('\n'.join(f"[{s['start']:.2f}–{s['end']:.2f}] {s['text'].strip()}" for s in r['segments']))
 with (out/f'WORDS{suffix}.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=['start','end','word','probability'],lineterminator='\n');w.writeheader()
  for s in r['segments']:w.writerows(s['words'])
 print(p.parents[1].name,r['text'],flush=True)
