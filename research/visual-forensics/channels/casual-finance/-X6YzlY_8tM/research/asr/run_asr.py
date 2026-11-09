import whisper,json,sys
m=whisper.load_model('base');r=m.transcribe('asr/audio16k.wav',language='en',fp16=False,condition_on_previous_text=False)
json.dump({'engine':'openai-whisper base (machine ASR, unverified by listening)','segments':[{'start':s['start'],'end':s['end'],'text':s['text'].strip()} for s in r['segments']]},open('asr/asr_whisper_base.json','w'),indent=1)
print(len(r['segments']))
