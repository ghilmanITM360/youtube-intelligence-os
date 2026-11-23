from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import subprocess
P=Path('.')
poses=['down','shrug','point']; faces=['neutral','smile','worried','surprised','smirk']
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',24)
def render(p,e):
 b=Image.open(P/f'rig_body_{p}.png');h=Image.open(P/f'rig_head_{e}.png');c=Image.new('RGBA',(1500,1900));c.alpha_composite(b,(0 if p=='point' else 100,600));c.alpha_composite(h,(400,19));return c
sheet=Image.new('RGB',(1920,1080),'#fdfdfb');d=ImageDraw.Draw(sheet)
for y,p in enumerate(poses):
 for x,e in enumerate(faces):
  im=render(p,e);im.thumbnail((260,300),Image.Resampling.LANCZOS);xx=x*380+55;yy=y*350+25;sheet.paste(im,(xx,yy),im);d.text((xx,yy+305),p+' / '+e,fill='#333333',font=font)
sheet.save(P/'all_combinations.jpg',quality=94)
# Each row cycles expressions while the pose stays fixed; rows then switch pose with shared expression.
proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','all_combinations_preview.mp4'],stdin=subprocess.PIPE)
for p in poses:
 for e in faces:
  im=render(p,e);im.thumbnail((650,780),Image.Resampling.LANCZOS);plate=Image.new('RGB',(1920,1080),'#fdfdfb');plate.paste(im,(640,155),im);ImageDraw.Draw(plate).text((55,45),p.upper()+' / '+e.upper(),font=font,fill='#555555');data=plate.tobytes()
  for i in range(30):proc.stdin.write(data)
proc.stdin.close();assert proc.wait()==0
