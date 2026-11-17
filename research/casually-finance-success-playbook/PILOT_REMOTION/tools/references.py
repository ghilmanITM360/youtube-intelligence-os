import os
"""Bounded, read-only reference clips and frames for internal craft criticism."""
import csv,hashlib,json,subprocess
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
repo=Path.cwd().parents[2];e=Path('evidence');e.mkdir(exist_ok=True);cache=Path('reference_clips');cache.mkdir(exist_ok=True)
root=repo/'data/extracted/forensic-analysis/casually-finance/2026-10-12'
alias=list(csv.DictReader((root/'00_MANIFEST/REPOSITORY_SOURCE_ALIASES.csv').open()))
sequences=[('roe3SgezmmU',0,3.4,'chart reveal'),('5umJ63d3rzQ',5.067,3.4,'bespoke character acting'),('rSa2aziEsAI',38.6,3.4,'banknote transfer')]
records=[]
font=ImageFont.truetype(os.environ.get('PILOT_FONT','/System/Library/Fonts/Supplemental/Arial.ttf'),22)
sheet=Image.new('RGB',(1920,3*312),'#FAF3E6');draw=ImageDraw.Draw(sheet)
for row,(vid,start,length,focus) in enumerate(sequences):
 source=next(a for a in alias if a['video_id']==vid);local=Path('/Users/ghilmanislam360/Downloads/CasuallyFinance')/Path(source['repository_source_path']).name
 digest=hashlib.sha256(local.read_bytes()).hexdigest();assert digest==source['sha256']
 subprocess.run(['ffmpeg','-y','-v','error','-ss',str(start),'-i',str(local),'-t',str(length),'-an','-vf','scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2:color=0xFAF3E6,fps=30','-c:v','libx264','-crf','21',str(cache/f'{vid}.mp4')],check=True)
 times=[start+.1,start+1.05,start+2.1,start+3.2]
 for col,t in enumerate(times):
  path=cache/f'{vid}-{col}.png';subprocess.run(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(local),'-frames:v','1',str(path)],check=True)
  im=Image.open(path);im.thumbnail((470,265));sheet.paste(im,(col*480,row*312+37));draw.text((col*480+6,row*312+5),f'{vid} / {t:.2f}s / {focus}',font=font,fill='#19353F')
 records.append({'video_id':vid,'url':f'https://www.youtube.com/watch?v={vid}&t={int(start)}','local_read_only':str(local),'sha256':digest,'start':start,'duration':length,'focus':focus,'rights':'Competitor copyright retained. Brief low-resolution excerpts for internal comparison/criticism; excluded from original pilot. Do not publish reference assets.'})
sheet.save(e/'reference-contact-sheet.jpg',quality=92)
(e/'reference-sequences.json').write_text(json.dumps(records,indent=2))
print('PASS 3 source hashes; 10.2 seconds total reference excerpts; 12 sampled frames')
