from pathlib import Path
from PIL import Image, ImageDraw
import csv, hashlib, math

root = Path(__file__).resolve().parents[2]
outdir = root / 'assets/vec'
outdir.mkdir(exist_ok=True)
ink, red, gray = '#0C0C0C', '#D7263D', '#C4C4C4'

class Art:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.im = Image.new('RGBA', (w, h)); self.d = ImageDraw.Draw(self.im); self.svg = []
    def line(self, pts, color=ink, width=7):
        self.d.line(pts, fill=color, width=width, joint='curve')
        for x,y in (pts[0],pts[-1]): self.d.ellipse((x-width/2,y-width/2,x+width/2,y+width/2), fill=color)
        self.svg.append(f'<polyline points="{" ".join(f"{x:.2f},{y:.2f}" for x,y in pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')
    def ellipse(self, box, fill=None, outline=None, width=1):
        self.d.ellipse(box,fill=fill,outline=outline,width=width);x,y,x2,y2=box
        self.svg.append(f'<ellipse cx="{(x+x2)/2}" cy="{(y+y2)/2}" rx="{(x2-x)/2}" ry="{(y2-y)/2}" fill="{fill or "none"}" stroke="{outline or "none"}" stroke-width="{width}"/>')
    def polygon(self, pts, fill):
        self.d.polygon(pts,fill=fill);self.svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{fill}"/>')
    def save(self, id, note):
        png=outdir/(id+'.png'); svg=outdir/(id+'.svg')
        if png.exists() or svg.exists(): raise FileExistsError(id)
        self.im.save(png);svg.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'+''.join(self.svg)+'</svg>\n')
        sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
        with (root/'assets/MANIFEST.csv').open('a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([id,str(png.relative_to(root)),sha(png),self.w,self.h,'RGBA','code',1,'PENDING_QA',note+'; SVG: '+str(svg.relative_to(root)),'','',''])
            writer.writerow([id+'-SVG',str(svg.relative_to(root)),sha(svg),self.w,self.h,'SVG','code',1,'PENDING_QA',note,'','',''])

def arrow(a,x,y,dx,dy,c=red):
    a.line([(x,y),(x+dx,y+dy)],c); ang=math.atan2(dy,dx); tip=(x+dx,y+dy)
    for z in (-.65,.65):a.line([tip,(tip[0]-14*math.cos(ang+z),tip[1]-14*math.sin(ang+z))],c)

# Mug mask is a stage-size approximation based on the current generated mug and needs overlay review.
a=Art(500,320);a.polygon([(131,69),(299,69),(289,248),(281,257),(149,257),(142,250)],'#FFFFFF');a.save('MSK-01','Approximate inset; verify against selected MUG-01')
a=Art(20,20);a.ellipse((4,4,16,16),ink);a.save('DOT-01','Position relative to ruler zero in compositor')
a=Art(220,160);pts=[(110+96*math.cos(t)*(1+.014*math.sin(9*t)),80+66*math.sin(t)*(1+.014*math.sin(9*t))) for t in [2*math.pi*i/150 for i in range(151)]];a.line(pts,red);a.save('RDC-01','Ellipse parameterized by compositor placement and scale')
a=Art(60,510);a.line([(48,8),(18,8),(18,502),(48,502)],red);a.save('BRK-01','Bracket; align endpoints to measured thermometer ticks')
a=Art(240,110);a.line([(8,85),(58,82),(112,69),(164,39),(225,20)],ink);a.line([(225,20),(207,20)],ink);a.line([(225,20),(216,36)],ink);a.save('ARR-01','Curved leader; placement and length set in compositor')
a=Art(45,600);a.line([(37,10),(10,10),(10,590),(37,590)],ink);a.save('NIA-05','Height bracket for stage y=120..700')
a=Art(90,90);arrow(a,14,62,25,-20);arrow(a,44,64,12,-30);a.save('HEAT-01','Two outward heat marks')
a=Art(60,145);pts=[(30+14*math.sin(6*math.pi*i/120),130-i) for i in range(121)];a.line(pts,red);a.line([(18,23),(30,10),(42,23)],red);a.save('HLS-01','Heat-out wave')
a=Art(240,145)
for x in (24,72,120,168,216):a.line([(x+10*math.sin(6*math.pi*i/120),130-i) for i in range(121)],red)
a.line([(108,23),(120,10),(132,23)],red);a.save('HLS-02','Five fanned heat waves')
a=Art(55,55);arrow(a,8,42,28,-20);a.save('HLS-03','Small heat input arrow')
a=Art(240,25);a.line([(5,12),(235,12)],red);a.save('STR-01','Strike length to be aligned with editable BOIL text')
a=Art(80,80);a.line([(7,7),(73,73)],red);a.line([(73,7),(7,73)],red);a.save('XOUT-01','Cross over flame')
a=Art(1080,810);a.line([(360,4),(360,806)],ink);a.line([(720,4),(720,806)],ink);a.save('EXP-01','Transparent dividers over white panel')
a=Art(45,110);a.line([(22,10),(22,100)],ink);a.line([(9,23),(22,10),(35,23)],ink);a.line([(9,87),(22,100),(35,87)],ink);a.save('EXP-02','Double-headed dip arrow')
a=Art(1080,810);a.line([(140,100),(140,700),(1000,700)],ink)
for color,off in [(ink,0),('#848484',2),(gray,6)]:
 pts=[(140+i*4, 170+int(480*(1-math.exp(-i/92)))+int(off*i/215)) for i in range(216)];a.line(pts,color)
a.save('CHT-01','Illustrative exponential curves; labels separate')
a=Art(48,48);a.polygon([(7,7),(41,7),(41,41),(7,41)],'white');a.line([(7,7),(41,7),(41,41),(7,41),(7,7)],ink)
for x,y in [(15,16),(31,20),(22,31)]:a.ellipse((x-2,y-2,x+2,y+2),ink)
a.save('SUG-01','34 px flat cube')
a=Art(44,55);a.polygon([(9,8),(29,8),(30,14),(27,18),(31,23),(27,28),(9,28)],'white');a.line([(9,8),(29,8),(30,14),(27,18),(31,23),(27,28),(9,28),(9,8)],ink)
for x,y in [(14,41),(25,44),(32,37)]:a.ellipse((x-2,y-2,x+2,y+2),ink)
a.save('SUG-02','Reduced broken cube')
a=Art(60,50)
for x,y,r in [(10,12,3),(25,8,2),(42,18,3),(20,31,2),(46,36,3)]:a.ellipse((x-r,y-r,x+r,y+r),ink)
a.save('SUG-03','Five sugar grains')
a=Art(120,60);a.line([(8,38),(20,28),(34,25),(50,31)],gray);a.line([(58,35),(72,25),(88,23),(108,30)],gray);a.save('SUG-04','Two faint swirl marks')
print('19 VEC assets written; QA pending')
