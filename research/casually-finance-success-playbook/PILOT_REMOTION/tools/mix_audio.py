"""Schedule measured voice stems and synthesize original, restrained sound design."""
import json,math,subprocess,time,wave
from pathlib import Path
import numpy as np
start=time.perf_counter(); sr=48000; seconds=42; n=sr*seconds
voice=json.loads(Path('evidence/voice-generation.json').read_text())
bounds=[0,130,304,462,638,822,948,1104,1260]; timeline=[]
for i,item in enumerate(voice['lines']):
 at=(bounds[i]+8)/30; end=at+item['duration']; assert end<=bounds[i+1]/30
 timeline.append({**item,'from':bounds[i],'endFrame':bounds[i+1],'voiceStart':at,'voiceEnd':end})
Path('src/timeline.json').write_text(json.dumps(timeline,indent=2))
t=np.arange(n)/sr
bed=np.zeros(n)
# Authored sparse four-note motif and held fifths, without third-party samples.
for i,root in enumerate([146.832,130.813,164.814,130.813,146.832,130.813,164.814]):
 a=i*6; local=t-a; env=np.clip(local/.8,0,1)*np.clip((6-local)/1.1,0,1); env[(local<0)|(local>=6)]=0
 for freq in [root,root*1.5,root*2]:bed+=.012*np.sin(2*np.pi*freq*local)*env
for at,freq in [(2.0,587.33),(10.65,659.25),(16.3,523.25),(23.3,587.33),(32.1,523.25),(38.5,659.25)]:
 local=t-at; env=np.exp(-np.maximum(local,0)*6)*(local>=0)*(local<.8); bed+=.013*np.sin(2*np.pi*freq*local)*env
sfx=np.zeros(n)
for at in [.9,2.2,5.65,11.6,17.1,22.4,27.9,29.1,30.4,33.15,37.8]:
 dt=t-at; env=(dt>=0)*(dt<.2)*np.exp(-np.maximum(dt,0)*22)
 sfx+=.055*np.sin(2*np.pi*(650*dt-1100*dt*dt))*env
fade=np.clip(t/.6,0,1)*np.clip((seconds-t)/1.0,0,1)
# Bed is additionally ducked around every narration interval.
duck=np.ones(n)
for item in timeline:
 a=item['voiceStart']; b=item['voiceEnd']; env=np.clip((t-(a-.12))/.12,0,1)*np.clip(((b+.2)-t)/.2,0,1)
 duck=np.minimum(duck,1-.52*env)
def save(file,data):
 with wave.open(file,'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(data,-1,1)*32767).astype('<i2').tobytes())
save('public/audio/music.wav',bed*fade*duck);save('public/audio/sfx.wav',sfx*fade)
args=['ffmpeg','-y','-v','error']
for i in range(8):args+=['-i',f'public/audio/voice-{i}.wav']
filters=[]
for i,item in enumerate(timeline):
 delay=round(item['voiceStart']*1000);filters.append(f'[{i}:a]aresample=48000,highpass=f=80,adelay={delay}:all=1[v{i}]')
filters+=[''.join(f'[v{i}]' for i in range(8))+'amix=inputs=8:normalize=0,loudnorm=I=-16:TP=-2:LRA=7,apad,atrim=duration=42[voice]']
subprocess.run(args+['-filter_complex',';'.join(filters),'-map','[voice]','-c:a','pcm_s16le','public/audio/narration.wav'],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i','public/audio/narration.wav','-i','public/audio/music.wav','-i','public/audio/sfx.wav','-filter_complex','[0:a][1:a][2:a]amix=inputs=3:normalize=0,alimiter=limit=0.891:level=false,apad,atrim=duration=42[a]','-map','[a]','-ar','48000','-ac','2','-c:a','pcm_s16le','public/audio/mix.wav'],check=True)
# Exact spoken text retained as sentence-level subtitles; cue splits are proportional, not ASR word alignment.
srt=[];j=0
for item in timeline:
 words=item['text'].split();chunks=[words[i:i+8] for i in range(0,len(words),8)];at=item['voiceStart']
 for chunk in chunks:
  j+=1;end=at+item['duration']*len(chunk)/len(words)
  def stamp(s):
   ms=round(s*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
  srt.append(f'{j}\n{stamp(at)} --> {stamp(end)}\n'+ ' '.join(chunk)+'\n');at=end
Path('render/pilot.srt').write_text('\n'.join(srt))
Path('evidence/audio-schedule.json').write_text(json.dumps({'seconds':seconds,'voice_seconds':sum(i['duration'] for i in timeline),'scheduled_lines':8,'sentence_sync':'measured clip starts; no ASR word-alignment certification','music':'original synthesized fifths/motif, ducked','sfx':'original synthesized chirps','mix_seconds':time.perf_counter()-start,'timeline':timeline},indent=2))
print('PASS 8 measured voice clips fit within 42 seconds; original bed/SFX and full subtitles saved')
