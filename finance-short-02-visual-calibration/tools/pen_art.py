"""Original static pen drawings. No timeline, frame evaluator, rig or motion engine."""
from pathlib import Path
import html,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
NS='http://www.w3.org/2000/svg'
INK='#211b18';RED='#ba4340';GREEN='#598b50';CREAM='#f6efd9';SKIN='#e8b780';HAIR='#433126'
def p(d,fill='none',stroke=INK,sw=4):
 return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def g(body,x=0,y=0,s=1,ident=None):
 return f'<g'+(f' id="{ident}"' if ident else '')+f' transform="translate({x} {y}) scale({s})">{body}</g>'
# Original single-line display alphabet. Unequal widths, curved bowls and leaning stems
# are drawn deliberately; no random jitter, font dependency or proprietary font outline.
GLYPHS={
'A':('M1 22 L7 1 Q8 0 9 2 L16 22 M4 14 Q9 12 13 14',17),
'B':('M2 22 L2 1 Q15 0 14 6 Q14 11 3 11 Q18 10 16 17 Q15 23 2 22',18),
'C':('M17 3 Q8 -1 3 5 Q-1 13 4 19 Q9 24 17 20',18),
'D':('M2 1 L2 22 Q18 23 18 12 Q19 0 2 1',20),
'E':('M16 1 L2 2 L2 22 L17 21 M2 11 L14 10',18),
'F':('M17 1 L2 2 L2 22 M2 11 L14 10',18),
'G':('M17 3 Q8 -1 3 5 Q-1 14 5 20 Q11 24 18 19 L18 12 L11 12',20),
'H':('M2 1 L1 22 M17 0 L16 22 M2 11 Q9 10 17 11',19),
'I':('M2 2 L12 1 M7 2 L7 21 M1 22 L13 21',14),
'J':('M3 1 L15 1 M12 1 L11 17 Q10 25 2 20',16),
'K':('M2 1 L2 22 M17 1 L3 12 L18 22',20),
'L':('M2 1 L1 22 L17 21',18),
'M':('M1 22 L3 1 L11 14 L20 1 L22 22',24),
'N':('M2 22 L3 1 L18 22 L19 0',21),
'O':('M10 1 Q0 0 1 12 Q1 23 11 22 Q21 22 20 11 Q19 0 10 1 Z',22),
'P':('M2 22 L2 1 Q17 -1 17 7 Q17 14 2 12',19),
'Q':('M10 1 Q0 0 1 12 Q1 23 11 22 Q21 22 20 11 Q19 0 10 1 Z M12 15 L23 25',24),
'R':('M2 22 L2 1 Q17 -1 17 7 Q17 14 2 12 M9 12 L19 22',21),
'S':('M17 3 Q6 -2 3 5 Q1 10 10 12 Q20 14 17 19 Q11 26 1 20',19),
'T':('M0 2 Q10 0 21 1 M11 2 L10 22',22),
'U':('M2 1 L2 15 Q2 24 10 22 Q18 22 18 15 L19 0',21),
'V':('M1 1 L10 22 L20 0',22),
'W':('M1 0 L6 22 L14 8 L21 22 L27 0',29),
'X':('M1 1 L19 22 M19 0 L1 22',21),
'Y':('M1 1 L10 12 L20 0 M10 12 L10 22',22),
'Z':('M1 2 L19 1 L1 22 L20 21',22),
'0':('M9 1 Q1 0 1 12 Q1 23 10 22 Q19 21 18 11 Q18 0 9 1 Z M5 18 L14 5',20),
'1':('M2 6 L9 1 L8 22 M2 22 L15 21',17),
'2':('M1 5 Q7 -2 14 3 Q20 9 9 15 L1 22 L19 21',21),
'3':('M2 2 Q17 -2 16 6 Q15 11 8 11 Q20 10 18 18 Q16 25 1 21',20),
'4':('M13 22 L14 0 L1 15 L20 14',22),
'5':('M18 1 L3 2 L2 11 Q19 7 18 17 Q16 26 1 21',20),
'6':('M17 2 Q4 -2 1 13 Q0 25 12 22 Q21 18 16 12 Q9 7 2 13',20),
'7':('M1 2 L19 1 L8 22',21),
'8':('M9 1 Q1 0 2 6 Q3 12 10 11 Q18 10 17 5 Q16 0 9 1 Z M9 11 Q-1 12 2 19 Q5 24 12 22 Q22 19 16 13 L9 11',20),
'9':('M17 11 Q8 17 2 9 Q-1 1 10 1 Q19 0 18 11 Q17 24 3 22',20),
'$':('M17 3 Q6 -2 3 5 Q1 10 10 12 Q20 14 17 19 Q11 26 1 20 M10 -3 L9 26',20),
'+':('M2 11 L20 10 M11 2 L10 20',22),
'-':('M2 11 L19 10',21),
'=':('M1 7 L20 7 M2 15 L19 14',22),
'>':('M2 2 L20 11 L1 21',22),
'<':('M20 2 L1 11 L20 21',22),
'×':('M2 3 L19 20 M19 3 L2 20',22),
'≈':('M1 8 Q6 3 11 7 Q16 11 21 6 M1 17 Q6 12 11 16 Q16 20 21 15',23),
'%':('M1 22 L20 0 M5 1 Q0 1 1 7 Q2 12 6 9 Q10 7 8 3 Q7 0 5 1 Z M15 13 Q10 14 12 20 Q14 25 18 21 Q23 17 18 14 Z',24),
'.':('M3 21 L4 21',7),',':('M4 21 L2 26',7),':':('M3 6 L4 6 M3 18 L4 18',8),
'/':('M1 24 L16 0',18),"'":('M3 0 L2 5',6),'(':('M9 0 Q0 11 8 24',11),')':('M1 0 Q10 11 2 24',11),'?':('M1 5 Q8 -2 14 4 Q18 9 9 13 L8 16 M8 22 L9 22',18),
'!':('M5 0 L4 15 M4 22 L5 22',9),
}
def lettering(value,size=50,color=INK):
 value=value.upper().replace('−','-').replace('–','-').replace('·','.')
 s=size/27;cursor=0;parts=[]
 for char in value:
  if char==' ':cursor+=10*s;continue
  if char not in GLYPHS:raise ValueError('Unsupported original lettering: '+char)
  d,w=GLYPHS[char];parts.append(g(p(d,stroke=color,sw=2.1),cursor,0,s));cursor+=(w+4)*s
 return ''.join(parts),max(0,cursor-4*s)
def txt(x,y,value,size=50,color=INK,anchor='start'):
 body,width=lettering(value,size,color);offset={'start':0,'middle':-width/2,'end':-width}[anchor]
 return f'<g data-text="{html.escape(value)}" data-lettering="original-paths" transform="translate({x+offset:.3f} {y-size*.81:.3f})">{body}</g>'
def svg(body,w,h,ident='art'):
 return f'<svg xmlns="{NS}" xmlns:xlink="http://www.w3.org/1999/xlink" id="{ident}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
def outline_v2(body):
 root=ET.fromstring(svg(body,1000,1000));ET.register_namespace('',NS)
 for par in list(root.iter()):
  for el in list(par):
   if el.tag==f'{{{NS}}}text':
    new=ET.fromstring(svg(txt(float(el.get('x')),float(el.get('y')),el.text or '',float(el.get('font-size',40)),el.get('fill',INK),el.get('text-anchor','start')),1000,1000))[0]
    par.insert(list(par).index(el),new);par.remove(el)
 return ''.join(ET.tostring(x,encoding='unicode') for x in root)
# Load only V2 function definitions; do not execute its factory or overwrite V2.
source=ROOT/'editable_sources/original/draw_calibration.py'
base={'__file__':str(source)}
exec(compile(source.read_text().split('\nassets = ')[0],str(source),'exec'),base)
def v2(name):return outline_v2(base[name]())
def face(expr):
 eyes=p('M110 106 Q117 101 124 106 M165 104 Q173 99 180 104',sw=3)
 pupils='<circle cx="120" cy="110" r="3.7" fill="'+INK+'"/><circle cx="174" cy="108" r="3.7" fill="'+INK+'"/>'
 brows=p('M108 93 Q119 86 130 91 M161 90 Q173 83 185 90',sw=2.9)
 mouth=p('M127 135 Q143 148 159 134',sw=3)
 if expr=='EXPLAIN':mouth=p('M126 132 Q143 148 160 131 Q150 154 134 145 Z','#fff',sw=2.8)
 if expr=='WOW':
  eyes=p('M109 101 Q112 94 121 96 Q133 99 128 114 Q124 124 112 118 Z M164 98 Q168 91 177 94 Q188 96 184 111 Q180 121 169 117 Z','#fff',sw=2.6)
  pupils='<ellipse cx="124" cy="107" rx="3.2" ry="4.3" fill="'+INK+'"/><ellipse cx="180" cy="105" rx="3.2" ry="4.3" fill="'+INK+'"/>'
  brows=p('M106 86 Q116 74 129 81 M162 79 Q175 68 187 77',sw=2.8);mouth=p('M135 131 Q149 124 153 139 Q155 153 140 152 Q128 146 135 131 Z',INK,sw=2.5)
 if expr=='WORRIED':
  eyes='';brows=p('M107 98 Q118 96 130 85 M161 86 Q173 98 185 96',sw=2.8);mouth=p('M125 144 Q140 131 155 139 L160 144',sw=3)
 if expr=='THINK':
  eyes='';pupils='<circle cx="121" cy="108" r="3.5" fill="'+INK+'"/><circle cx="176" cy="103" r="3.5" fill="'+INK+'"/>'
  brows=p('M107 93 L131 91 M162 83 Q175 78 186 86',sw=2.8);mouth=p('M133 139 L151 137',sw=3)
 if expr=='RESOLVE':
  eyes='';brows=p('M107 93 L130 97 M161 95 L185 88',sw=2.8);mouth=p('M125 135 Q144 145 159 134',sw=3)
 return eyes+pupils+brows+mouth
POSE_ARMS={
'OPEN':p('M141 208 Q115 217 98 209 L71 195 M72 195 L61 192 M73 195 L63 199 M142 208 Q166 218 187 207 L218 192 M217 192 L230 186 M220 191 L233 195',sw=3.8),
'UP':p('M140 208 Q119 218 111 233 L132 243 M142 208 Q177 206 190 177 L242 140 M242 140 L245 123 M242 140 L255 130 M242 140 L257 141',sw=3.8),
'THINK':p('M140 208 Q111 228 133 245 M143 208 Q163 192 166 173 L149 149 M149 149 Q142 145 139 147 M149 149 L145 154',sw=3.8),
'LEFT':p('M140 208 Q108 208 84 188 L52 171 M52 171 L35 164 M52 171 L36 174 M142 208 L174 230 L146 243',sw=3.8),
'SHIELD':p('M141 208 L108 230 L133 243 M142 208 Q165 218 189 216 L219 207',sw=3.8),
'REPAIR':p('M141 208 L109 227 L129 241 M142 208 Q167 213 185 233 L213 253 M213 253 L226 263',sw=3.8),
}
def host(pose='STAND',expr='NEUTRAL',upper=False):
 old={'STAND':'standing','POINT':'pointing','BILL':'holding'}.get(pose,'standing');body=base['host']('neutral',old)
 root=ET.fromstring(svg(body,290,400));fc=next(n for n in root if n.tag.endswith('g') and n.get('id','').startswith('face-'))
 for node in list(fc)[3:]:fc.remove(node)
 for n in ET.fromstring(svg(face(expr),290,400)):fc.append(n)
 if pose in POSE_ARMS:
  root.remove(root[2]);root.insert(2,ET.fromstring(svg(POSE_ARMS[pose],290,400))[0])
 if upper:root.remove(root[0])
 return ''.join(ET.tostring(n,encoding='unicode') for n in root)
def arrow(color=INK):return p('M8 22 Q57 16 112 24 M91 8 L114 24 L91 39',stroke=color,sw=5)
def up(color=GREEN):return p('M22 182 Q28 102 26 48 L8 69 L27 17 L53 64 L36 47 Q38 112 34 182 Z',color,sw=3.3)
def moneybag():
 return p('M81 34 L65 8 L84 14 L106 5 L114 34 Q144 52 157 119 Q169 182 90 183 Q13 180 26 126 Q35 59 81 34 Z','#a8c391',sw=4.2)+p('M76 36 Q98 42 120 34 M43 155 Q58 167 73 161',sw=2.8)+txt(92,130,'$',70,anchor='middle')
def stack():
 b=''
 for x,y in [(30,37),(12,67),(26,96)]:b+=g(v2('note'),x,y,.95)
 return b+p('M114 36 L139 37 L138 174 L116 177 Z',CREAM,sw=2.8)
def bond():
 return p('M26 12 Q102 8 191 15 L185 245 Q115 237 19 244 Z',CREAM,sw=4)+p('M40 31 L172 31 L164 212 L36 216 Z',sw=1.8)+txt(103,74,'BOND',32,anchor='middle')+p('M49 105 Q100 110 153 102 M49 126 L154 123 M49 151 L150 148',sw=2)+p('M75 178 L90 171 L102 178 L114 171 L123 187 L110 202 L96 194 L84 200 Z','#d4c6a7',sw=2.6)+p('M94 199 L91 223 M108 198 L117 223',sw=2)
def coupon():return p('M16 17 L156 10 L159 102 L13 110 Z',CREAM,sw=3.8)+p('M39 14 L38 104',sw=2.4)+txt(102,62,'COUPON',22,anchor='middle')+p('M61 81 L139 76',sw=2)
def ledger():
 return p('M20 25 Q81 5 152 24 Q219 7 282 28 L283 211 Q216 190 150 209 Q83 193 17 214 Z',CREAM,sw=4.3)+p('M151 25 Q146 119 151 209 M30 39 Q87 21 139 39 M168 40 Q221 24 271 42',sw=2.5)+p('M40 73 L127 66 M42 101 L124 96 M39 130 L128 125 M41 159 L126 154 M172 72 L259 69 M173 100 L260 96 M172 128 L257 125 M172 157 L260 152',sw=1.8)
def treasury():
 return p('M24 75 L151 15 L286 72 L24 75 Z',CREAM,sw=4.2)+p('M41 79 L268 78 L269 197 L40 198 Z','#faf8ee',sw=3.5)+p('M66 92 L80 91 L80 188 L67 190 M229 91 L243 92 L244 189 L228 188 M105 100 L202 98 L201 184 L107 186 Z',CREAM,sw=2.7)+p('M22 201 L286 199 L287 219 L19 222 Z M11 224 L296 220 L299 234 L10 238 Z',CREAM,sw=3.2)+txt(154,64,'TREASURY',24,anchor='middle')+p('M156 120 L153 185',sw=2.2)
def deferredpile():
 b=''
 for x,y in [(46,10),(24,34),(7,58)]:b+=g(p('M10 9 L161 5 L170 120 L7 126 Z',CREAM,sw=3)+p('M28 27 L140 23 M28 45 L138 42 M27 67 L115 64',sw=1.8),x,y)
 return b+txt(114,119,'LOSSES',26,RED,'middle')
def clock():
 return p('M88 12 C35 8 9 38 15 84 Q18 141 79 144 Q145 144 151 86 Q157 25 88 12 Z',CREAM,sw=4)+p('M83 78 L83 38 M83 78 L117 96 M83 22 L83 29 M139 79 L130 79 M84 132 L84 123 M26 78 L33 78',sw=3)+p('M21 135 L8 147 M140 135 L153 147',sw=3)
def pause():return p('M15 10 L40 9 L40 111 L14 112 Z',RED,sw=3)+p('M65 10 L89 9 L91 111 L65 112 Z',RED,sw=3)
def shield():return p('M22 13 Q86 33 149 10 L152 70 Q140 133 87 166 Q29 136 18 77 Z',GREEN,sw=4)+p('M49 83 L75 111 L121 57',stroke='#fff',sw=7)
def price():return p('M12 20 L125 13 L164 65 L119 117 L9 111 Z',CREAM,sw=4)+p('M133 59 Q138 53 143 59 Q145 66 138 68 Q131 67 133 59 Z','#fff',sw=2.7)+txt(72,79,'$',55,RED,'middle')+g(up(RED),173,14,.65)
def wrench():return p('M32 41 Q14 11 37 1 L36 23 L52 29 L68 16 L65 0 Q94 10 77 38 L132 100 L117 115 L62 49 Z','#d4c6a7',sw=3.3)+p('M116 102 Q122 96 128 103 Q130 109 124 111 Z','#fff',sw=2)
def bankrep():
 return p('M101 151 L99 237 L81 309 L67 315 M99 237 L125 310 L143 312 M99 181 L71 203 L91 215 M99 181 L127 205 L151 190',sw=3.8)+p('M55 49 Q66 12 107 18 Q149 16 167 56 Q181 102 157 131 Q116 166 76 139 Q42 116 55 49 Z','#dcb188',sw=4)+p('M53 63 Q38 39 64 21 Q84 5 125 13 Q151 17 166 49 L158 67 L150 37 Q116 47 81 36 L58 72 Z','#6f6b60',sw=4)+p('M75 77 L108 76 L108 102 L74 103 Z M123 76 L153 78 L155 100 L124 101 Z M109 86 L123 86',sw=2.4)+p('M96 127 Q114 141 136 124',sw=3)+p('M98 154 L110 156 L103 174 L96 157 Z',GREEN,sw=2.4)
def desk():return p('M18 19 L257 9 L289 42 L15 52 Z',CREAM,sw=4)+p('M26 51 L24 159 L45 159 L46 49 M265 45 L265 157 L283 157 L283 47',CREAM,sw=3.6)+p('M44 49 L265 46',sw=2)
def stepbridge():return p('M15 127 L15 95 L60 96 L60 66 L112 69 L112 40 L166 42 L167 13 L221 14 M14 135 L228 135',sw=4.2)
