import os
"""Scan decoded final output; measures do not certify human-perceived quality."""
import hashlib,json,subprocess,time
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFont
start=time.perf_counter();video=Path('render/fixed-mortgage-pilot.mp4')
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]));v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio')
assert (v['width'],v['height'],v['r_frame_rate'])==(1920,1080,'30/1');assert int(v['nb_frames'])==1260;assert abs(float(probe['format']['duration'])-42)<.05
subprocess.run(['ffmpeg','-v','error','-i',str(video),'-f','null','-'],check=True)
raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(video),'-vf','scale=192:108','-f','rawvideo','-pix_fmt','rgb24','-an','-']);frames=np.frombuffer(raw,dtype=np.uint8).reshape(-1,108,192,3)
means=frames.mean(axis=(1,2,3));delta=np.abs(np.diff(frames.astype(np.int16),axis=0)).mean(axis=(1,2,3));identical=[]
for i,d in enumerate(delta):
 if d==0:identical.append(i+1)
black=np.flatnonzero(means<5).tolist();assert not black
# Measure motion in illustration area, excluding the progress bar/captions.
region=frames[:,14:83,58:159,:];motion=np.abs(np.diff(region.astype(np.int16),axis=0)).mean(axis=(1,2,3))
logs=json.loads(Path('evidence/browser-log.json').read_text());errors=[l for l in logs if l['type']=='error'];text=[json.loads(l['text'][8:]) for l in logs if l['text'].startswith('TEXT_QA ')];clipped=[l for l in text if l['clipped']];assert not errors;assert not clipped
assert len(set(i['frame'] for i in text))==1260
loud=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
stats=json.JSONDecoder().raw_decode(loud[loud.rfind('{'):])[0];Path('evidence/final-audio-loudness.json').write_text(json.dumps(stats,indent=2))
timeline=json.loads(Path('src/timeline.json').read_text());assert len(timeline)==8
for i in timeline:assert i['voiceEnd']<=i['endFrame']/30
voice=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i','public/audio/narration.wav','-f','f32le','-ac','1','-ar','48000','-']),dtype='<f4')
coverage=[]
for i in timeline:
 x=voice[round(i['voiceStart']*48000):round(i['voiceEnd']*48000)];rms=float(np.sqrt(np.mean(x*x)));assert rms>.005
 coverage.append({'id':i['id'],'rms':rms,'start':i['voiceStart'],'end':i['voiceEnd']})
font=ImageFont.truetype(os.environ.get('PILOT_FONT','/System/Library/Fonts/Supplemental/Arial.ttf'),24)
samples=[0,45,210,385,571,747,920,1038,1218];sheet=Image.new('RGB',(1920,1170),'#FAF3E6');draw=ImageDraw.Draw(sheet)
for j,f in enumerate(samples):
 path=Path('qa_frames')/f'final-{f}.png';subprocess.run(['ffmpeg','-y','-v','error','-ss',str(f/30),'-i',str(video),'-frames:v','1',str(path)],check=True)
 im=Image.open(path).convert('RGB');im.thumbnail((640,360));x=j%3*640;y=j//3*390;sheet.paste(im,(x,y+30));draw.text((x+8,y+2),f'Original / {f/30:.2f}s',font=font,fill='#19353F')
sheet.save('evidence/pilot-contact-sheet.jpg',quality=93)
# Small-preview sheet retains both 320px and 160px views at real size.
small=Image.new('RGB',(1020,3*300),'#FAF3E6');d=ImageDraw.Draw(small)
for row,f in enumerate([45,571,1038]):
 im=Image.open(f'qa_frames/final-{f}.png');a320=im.resize((320,180),Image.Resampling.LANCZOS);a160=im.resize((160,90),Image.Resampling.LANCZOS);small.paste(a320,(20,row*300+45));small.paste(a160,(410,row*300+45));d.text((20,row*300+10),f'{f/30:.2f}s / 320px',font=font,fill='#19353F');d.text((410,row*300+10),'160px',font=font,fill='#19353F')
small.save('evidence/mobile-preview.png')
result={'video_sha256':hashlib.sha256(video.read_bytes()).hexdigest(),'bytes':video.stat().st_size,'format':{'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'frames':int(v['nb_frames']),'duration':probe['format']['duration'],'audio_duration':a['duration'],'audio_sample_rate':a['sample_rate']},'full_decode':'PASS','black_frame_indices':black,'identical_consecutive_frame_indices':identical,'illustration_region_motion_mean':float(motion.mean()),'illustration_region_motion_percentiles':np.percentile(motion,[0,10,50,90,100]).tolist(),'text_bounds_frames_checked':len(set(i['frame'] for i in text)),'clipped_text':clipped,'browser_errors':errors,'narration_coverage':coverage,'audio_measurements':stats,'qa_wall_seconds':time.perf_counter()-start,'human_full_listening':'PENDING','human_art_direction':'PENDING','agent_review':'rendered stills and bounded temporal frame sampling; not an independent human reviewer','limits':'No-black/no-identical-frame scans are technical proxies. Camera motion can prevent identical frames during intentional information holds; no frozen-placeholders conclusion also requires source inspection. Sentence starts are measured; word sync is not independently transcribed.'}
Path('evidence/render-qa.json').write_text(json.dumps(result,indent=2));print('PASS 1080p/30fps/1260 frames; full decode; no black frames; 1260 text-bound checks; 8 audible scheduled clips');print('identical frames:',len(identical),'integrated LUFS:',stats['input_i'],'true peak dBTP:',stats['input_tp'])
