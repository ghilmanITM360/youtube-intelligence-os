# Provisional local ASR (faster-whisper, CPU int8). Output is machine text, NOT audio listening.
import sys,json,csv,time,wave,numpy as np,faster_whisper,ctranslate2
wav,out,model=sys.argv[1],sys.argv[2],sys.argv[3]
w_=wave.open(wav);assert w_.getframerate()==16000 and w_.getnchannels()==1;aud=np.frombuffer(w_.readframes(w_.getnframes()),np.int16).astype(np.float32)/32768.0 # decode via numpy; pyav 19 incompatible with faster-whisper 1.2.1
t=time.time();m=faster_whisper.WhisperModel(model,device="cpu",compute_type="int8",cpu_threads=4)
segs,info=m.transcribe(aud,language="en",beam_size=5,word_timestamps=True,vad_filter=False)
rows=[];words=[]
for s in segs:
    rows.append({"start":round(s.start,2),"end":round(s.end,2),"text":s.text.strip(),"avg_logprob":round(s.avg_logprob,3),"no_speech_prob":round(s.no_speech_prob,3)})
    for w in (s.words or []): words.append({"w":w.word,"start":round(w.start,2),"end":round(w.end,2),"p":round(w.probability,3)})
json.dump({"tool":"faster-whisper "+faster_whisper.__version__,"ctranslate2":ctranslate2.__version__,"model":model,"language":info.language,"language_prob":round(info.language_probability,3),"duration_s":round(info.duration,2),"runtime_s":round(time.time()-t,1),"label":"PROVISIONAL_ASR_NOT_LISTENING","segments":rows,"words":words},open(out+".json","w"),indent=1)
csv.DictWriter(f:=open(out+"_segments.csv","w",newline=""),fieldnames=list(rows[0])).writeheader() if False else None
w=csv.DictWriter(open(out+"_segments.csv","w",newline=""),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows),"segments",len(words),"words",round(time.time()-t,1),"s")
