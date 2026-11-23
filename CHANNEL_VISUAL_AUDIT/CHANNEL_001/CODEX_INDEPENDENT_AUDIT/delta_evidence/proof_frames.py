"""Decode delivered proof frames, measure whiteness and make timestamped sheets."""
from pathlib import Path
import csv
import subprocess
from PIL import Image, ImageDraw

out = Path(__file__).resolve().parent
root = out.parents[3]
video = root / 'productions/doc-animation-proof-01/out/DOC_PROOF_60s.mp4'
sets = {
 'document': [155, 156, 251, 252, 253, 263, 312, 362, 495, 516, 537, 563, 564, 573, 574, 576, 615, 616, 622, 630, 639, 747, 811, 831, 855, 878, 879, 880, 915, 930, 974, 975, 978, 984, 1040],
 'diagram': [1150, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1370, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1515, 1595, 1596, 1709],
}
full = {362, 537, 564, 615, 639, 831, 855, 879, 915, 1185, 1386, 1515}
p = subprocess.Popen(['ffmpeg','-v','error','-xerror','-i',str(video),'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
size = (1920,1080)
thumbnails = {}
with (out/'proof_frame_whiteness.csv').open('w') as dest:
    w = csv.writer(dest)
    w.writerow(['frame','seconds','pixels_all_channels_ge_245','pixels_not_white'])
    for i in range(1800):
        raw = p.stdout.read(size[0]*size[1]*3)
        frame = Image.frombytes('RGB',size,raw)
        if i in sets['document'] or i in sets['diagram']:
            thumbnails[i] = frame.resize((640,360), Image.Resampling.LANCZOS)
        if i in full:
            frame.save(out/f'proof_f{i:04d}.png')
        if any(lo <= i <= hi for lo,hi in ((150,166),(968,996),(1178,1202),(1378,1403),(1590,1609))):
            from PIL import ImageChops
            a,b,c = frame.split()
            h = ImageChops.darker(ImageChops.darker(a,b),c).histogram()
            w.writerow([i, f'{i/30:.3f}',sum(h[245:]),sum(h[:255])])
assert p.wait() == 0
for title, ids in sets.items():
    for start in range(0,len(ids),12):
        chunk=ids[start:start+12]
        sheet=Image.new('RGB',(1280,384*((len(chunk)+1)//2)), '#ddd')
        draw=ImageDraw.Draw(sheet)
        for j,i in enumerate(chunk):
            x, y = (j%2)*640, (j//2)*384
            sheet.paste(thumbnails[i],(x,y+24))
            draw.text((x+6,y+4),f'f{i}  {i/30:.3f} s',fill='black')
        sheet.save(out/f'{title}_{start//12+1}.jpg',quality=90)
