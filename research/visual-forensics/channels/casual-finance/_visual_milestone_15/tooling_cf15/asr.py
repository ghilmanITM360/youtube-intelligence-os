import sys, json, whisper
wav, out = sys.argv[1], sys.argv[2]
m = whisper.load_model('small.en')
r = m.transcribe(wav, word_timestamps=True, fp16=False, language='en')
json.dump(r, open(out, 'w'))
print(len(r['segments']), 'segments;', sum(len(s.get('words', [])) for s in r['segments']), 'words')
