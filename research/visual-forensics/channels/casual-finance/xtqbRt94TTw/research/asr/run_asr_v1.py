import sys,pathlib,json,hashlib,subprocess,datetime
sys.path.append('/Users/ghilmankhan/Library/Python/3.9/lib/python/site-packages')
import whisper,torch
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=json.loads((R/'source_manifest.json').read_text());A=R/'asr';output=A/'asr_whisper_base_v1.json';assert not output.exists()
model=pathlib.Path('/Users/ghilmankhan/.cache/whisper/base.pt');assert model.is_file();torch.set_num_threads(2)
wav=A/'audio16k_v1.wav'
if not wav.exists():subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-n','-i',S['source_path'],'-vn','-ac','1','-ar','16000',str(wav)],check=True)
m=whisper.load_model(str(model),device='cpu');r=m.transcribe(str(wav),language='en',fp16=False,condition_on_previous_text=False)
data={'engine':'installed openai-whisper base; cached weights only; CPU threads2','truth_label':'ASR_UNCERTIFIED_NOT_LISTENING','source_sha256':S['sha256'],'source_audio':'AAC 44100Hz decoded to mono16k WAV; timestamps relative to decoded audio start','model_sha256':hashlib.sha256(model.read_bytes()).hexdigest(),'audio_wav_sha256':hashlib.sha256(wav.read_bytes()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'segments':[{'id':s['id'],'start':s['start'],'end':s['end'],'text':s['text'].strip(),'avg_logprob':s['avg_logprob'],'no_speech_prob':s['no_speech_prob']} for s in r['segments']],'actual_listening_seconds':0,'limitations':['Machine sentence timestamps, not word-aligned; wording and financial numbers unverified.','No claim of audible music/SFX, intonation, emphasis or synchronization sign-off.']}
output.write_text(json.dumps(data,indent=2));print('ASR segments',len(data['segments']),flush=True)
