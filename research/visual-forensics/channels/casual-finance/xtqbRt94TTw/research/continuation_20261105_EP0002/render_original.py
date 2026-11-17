"""Bounded cold-input renderer: only the frozen original spec, no source imagery."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, subprocess, hashlib
P=Path(__file__).parent
S=json.loads((P/'RECONSTRUCTION_CRITERIA_FROZEN.json').read_text())
assert S['frame_count']==28 and S['timeline']['badge_first_rim']==39
R=P/'original_render_attempt01';R.mkdir(exist_ok=False)
(R/'encoded_inputs').mkdir();(R/'decoded').mkdir()
top={39:665,40:650,41:633,42:616,43:600,44:584,45:569,46:554,47:540,48:526,49:513,50:500,51:486,52:472,53:455,54:440,55:428,56:418,57:409,58:403,59:400}
palette={'background':'#fbf4eb','ink':'#1e375a','accent':'#e66e64','light':'#54bdb0'}
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',38)
for i,n in enumerate(range(37,65)):
    im=Image.new('RGB',(1920,1080),palette['background']);d=ImageDraw.Draw(im)
    if n>=39:
        y=top[min(n,59)]
        d.rounded_rectangle((855,y,1065,y+210),radius=24,fill=palette['ink'])
        d.rounded_rectangle((867,y+12,1053,y+198),radius=16,fill=palette['accent'])
        if n>=45:d.line((910,y+110,1005,y+110),fill=palette['background'],width=10)
    d.rectangle((680,670,1240,1080),fill=palette['ink'])
    d.text((755,760),'POLICY CONSOLE',font=font,fill=palette['background'])
    for x in [865,1005]: d.ellipse((x,900,x+44,944),fill=palette['light'])
    for bounds,label in [((100,200,620,340),'NOTE A'),((1100,80,1700,220),'NOTE B')]+([((1250,320,1820,500),'NOTE C')] if n>=49 else []):
        d.rounded_rectangle(bounds,radius=12,fill=palette['ink']);d.text((bounds[0]+30,bounds[1]+40),label,font=font,fill=palette['background'])
    im.save(R/'encoded_inputs'/f'f{i:03}.png')
cmd=['ffmpeg','-v','error','-framerate','24','-i',str(R/'encoded_inputs/f%03d.png'),'-c:v','ffv1','-pix_fmt','bgr0',str(R/'original_timing_master.mkv')]
subprocess.run(cmd,check=True)
subprocess.run(['ffmpeg','-v','error','-i',str(R/'original_timing_master.mkv'),'-fps_mode','passthrough','-start_number','37',str(R/'decoded/f%05d.png')],check=True)
subprocess.run(['ffmpeg','-v','error','-i',str(R/'original_timing_master.mkv'),'-c:v','libx264','-crf','18','-pix_fmt','yuv420p',str(R/'original_timing_preview.mp4')],check=True)
(R/'render_receipt.json').write_text(json.dumps({'criteria_sha256':hashlib.sha256((P/'RECONSTRUCTION_CRITERIA_FROZEN.json').read_bytes()).hexdigest(),'input':'Only frozen original spec and explicitly original geometry; no source imagery read','source_index_to_render_index':'render index=source index-37; starts PTS0 independently of source timebase','implementation_choices':'Rounded-square geometry and discrete lookup positions are original test choices, not recovered source keyframes/curve','master_sha256':hashlib.sha256((R/'original_timing_master.mkv').read_bytes()).hexdigest(),'command':cmd,'actual_listening_seconds':0},indent=2))
print(R)
