import os
"""Rendered moving comparison. Reference pixels never enter the original pilot."""
import json,subprocess
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
refs=json.loads(Path('evidence/reference-sequences.json').read_text());starts=[16.5,4.333333,21.266667];cache=Path('reference_clips');font=os.environ.get('PILOT_FONT','/System/Library/Fonts/Supplemental/Arial.ttf');parts=[]
for i,(ref,start) in enumerate(zip(refs,starts)):
 out=cache/f'comparison-{i}.mp4';parts.append(out)
 label=cache/f'labels-{i}.png';header=Image.new('RGBA',(1280,430),(0,0,0,0));hd=ImageDraw.Draw(header);hf=ImageFont.truetype(font,27)
 hd.text((16,12),f"REFERENCE {ref['video_id']}",font=hf,fill='#19353F');hd.text((656,12),f'ORIGINAL / {start:.2f}s',font=hf,fill='#19353F');header.save(label)
 filters="[0:v]setpts=PTS-STARTPTS,pad=640:430:0:60:color=0xFAF3E6[l];[1:v]scale=640:360,setpts=PTS-STARTPTS,pad=640:430:0:60:color=0xFAF3E6[r];[l][r]hstack=inputs=2[base];[base][2:v]overlay=0:0[v]"
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(cache/f"{ref['video_id']}.mp4"),'-ss',str(start),'-i','render/fixed-mortgage-pilot.mp4','-i',str(label),'-filter_complex',filters,'-map','[v]','-an','-t','3.4','-r','30','-c:v','libx264','-crf','20',str(out)],check=True)
Path('reference_clips/concat.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i','reference_clips/concat.txt','-c','copy','evidence/motion-comparison.mp4'],check=True)
sheet=Image.new('RGB',(1280,3*470),'#FAF3E6');d=ImageDraw.Draw(sheet);f=ImageFont.truetype(font,22)
strip=Image.new('RGB',(1920,3*265),'#FAF3E6');sd=ImageDraw.Draw(strip)
for i,(ref,start) in enumerate(zip(refs,starts)):
 for j,offset in enumerate([0,.1,.3,.6,1.4,3.2]):
  im=cache/f'pilot-{i}-{j}.png';subprocess.run(['ffmpeg','-y','-v','error','-ss',str(start+offset),'-i','render/fixed-mortgage-pilot.mp4','-frames:v','1',str(im)],check=True)
  img=Image.open(im);img.thumbnail((320,180));strip.paste(img,(j*320,i*265+52));sd.text((j*320+5,i*265+8),f'Pilot {start+offset:.2f}s',font=f,fill='#19353F')
 clip=cache/f'pair-{i}.png';subprocess.run(['ffmpeg','-y','-v','error','-ss','1.05','-i',str(parts[i]),'-frames:v','1',str(clip)],check=True)
 img=Image.open(clip);img.thumbnail((1280,430));sheet.paste(img,(0,i*470));d.text((14,i*470+440),f"{ref['focus']} | reference {ref['start']:.3f}s–{ref['start']+ref['duration']:.3f}s | pilot {start:.3f}s–{start+3.4:.3f}s",font=f,fill='#19353F')
sheet.save('evidence/quality-comparison.jpg',quality=93);strip.save('evidence/temporal-motion-strip.jpg',quality=93)
Path('evidence/comparison-edit.json').write_text(json.dumps({'reference_audio':'muted; this comparison judges visual craft','reference_duration_total':10.2,'comparison_duration':10.2,'aspect':'reference aspect preserved, Short pillarboxed; no format-normalized superiority claim','pairs':[{'reference':r,'pilot_start':s,'duration':3.4}for r,s in zip(refs,starts)]},indent=2))
print('Rendered 10.2-second moving comparison, paired contact sheet and 18-frame temporal pilot strip')
