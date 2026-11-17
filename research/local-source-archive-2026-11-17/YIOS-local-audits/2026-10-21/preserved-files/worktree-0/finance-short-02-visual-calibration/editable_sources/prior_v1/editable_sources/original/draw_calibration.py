"""Static SVG artwork authoring only. No animation, timeline, rig, or video code."""
from pathlib import Path
import base64, html

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'editable_sources' / 'original'
BLACK, RED, GREEN, CREAM = '#171512', '#b93839', '#55904f', '#f5efdc'
FONT = 'Chalkboard, Comic Sans MS, sans-serif'

def text(x, y, value, size=50, color=BLACK, anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{html.escape(value)}</text>'

def path(d, fill='none', stroke=BLACK, width=5):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>'

def svg(body, w, h, white=False):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + ('<rect width="100%" height="100%" fill="#fff"/>' if white else '') + body + '</svg>'

def group(body, x=0, y=0, scale=1, ident='layer'):
    return f'<g id="{ident}" transform="translate({x} {y}) scale({scale})">{body}</g>'

def host(expression='neutral', pose='standing'):
    # Original flat pen redraw of our own generated woman concept, never a competitor trace.
    legs = path('M139 269 Q141 309 135 337 M135 337 L114 372 L101 377 M136 337 Q155 354 167 376 L181 376', width=3.8)
    torso = path('M145 170 Q139 223 139 269 M132 177 L140 187 L147 175', width=3.8)
    arms = path('M141 207 Q120 211 103 229 L134 245 M142 208 Q167 216 180 230 L147 246', width=3.8)
    if pose == 'pointing':
        arms = path('M141 208 L111 227 L132 243 M142 208 Q176 212 196 194 L234 171 M234 171 L250 162 M236 172 L250 172 M237 173 L245 177', width=3.8)
    if pose == 'holding':
        arms = path('M141 207 L109 229 L132 244 M142 207 L180 234 L207 200', width=3.8)
    face = path('M78 63 C92 32 138 24 172 40 C207 55 224 92 211 131 C200 159 162 179 122 165 C82 154 65 119 78 63 Z', '#e8b780', width=4.2)
    hair = path('M79 84 C57 67 76 35 107 21 C138 6 178 20 192 38 C212 45 222 62 219 86 C208 68 195 47 183 41 Q139 72 78 96 Z', '#433126', width=4.6)
    bun = path('M211 91 C239 82 255 105 244 124 C237 139 217 133 211 120 Z', '#433126', width=4)
    eyes = '<g id="eyes"><ellipse cx="120" cy="108" rx="3.7" ry="4.6" fill="#171512"/><ellipse cx="174" cy="106" rx="3.7" ry="4.6" fill="#171512"/></g>'
    brows = path('M109 94 Q119 88 130 92 M163 91 Q173 85 184 90', width=3)
    mouth = path('M128 137 Q144 143 157 135', width=3.4)
    if expression == 'explaining':
        mouth = path('M128 133 Q145 149 160 131 Q145 137 128 133 Z', '#fff', width=3)
    if expression == 'surprised':
        brows = path('M108 86 Q117 78 129 83 M164 82 Q175 73 185 79', width=3)
        mouth = path('M138 131 C126 127 127 150 137 152 C149 154 151 128 138 131 Z', '#171512', width=3)
    if expression == 'concerned':
        brows = path('M107 97 Q120 97 128 87 M164 87 Q172 96 184 94', width=3)
        mouth = path('M128 143 Q143 129 159 141', width=3.2)
    prop = ''
    if pose == 'holding':
        # Paper behind near thumb: grip remains visible; no floating bill.
        prop = group(path('M204 157 L267 153 L262 225 L201 229 Z', CREAM, width=3) + path('M218 177 L250 174 M217 190 L249 188', width=2.5), ident='held-paper')
        prop += group(path('M207 202 Q196 193 198 188 Q200 181 207 185 L214 190 M207 202 Q201 204 201 196', '#e8b780', width=2.8), ident='gripping-thumb')
    return legs + torso + arms + group(bun+face+hair+eyes+brows+mouth, ident='face-'+expression) + prop

def fed(label='FED'):
    return path('M15 89 L148 23 L277 87 L15 89 Z', CREAM) + path('M29 95 L262 95 L260 210 L30 211 Z', '#faf8ee') + path('M13 211 L280 211 L280 228 L12 229 Z', CREAM) + path('M60 110 L62 198 M91 111 L92 197 M204 111 L204 198 M234 112 L233 197', width=7) + path('M125 144 L170 144 L171 208 L124 209 Z', '#d4c6a7', width=4) + text(147, 81, label, 29, anchor='middle')

def bank():
    return path('M18 37 L215 32 L219 205 L15 207 Z', '#faf8ee') + path('M9 22 L227 18 L227 50 L10 53 Z', CREAM) + path('M101 138 L140 138 L141 206 L101 205 Z', '#d4c6a7', width=4) + path('M42 77 L78 76 L78 108 L42 109 Z M158 75 L193 77 L192 110 L156 109 Z', '#fff', width=3.5) + text(119, 46, 'BANK', 25, anchor='middle')

def bill():
    return path('M28 13 L185 8 L180 215 L20 218 Z', CREAM, width=4.5) + text(101, 58, 'BILL', 34, RED, 'middle') + path('M48 86 Q82 92 149 83 M45 107 Q85 102 151 106 M45 130 L128 127 M45 160 L151 157 M44 191 L151 191', width=3.1)

def note():
    return path('M7 14 L156 8 L157 78 L10 83 Z', '#93b886', width=4) + path('M22 27 L141 23 L140 66 L23 67 Z', 'none', width=2.1) + text(82, 62, '$', 43, '#f5eac7', 'middle')

def arrow(color=BLACK):
    return path('M6 21 Q49 17 88 23 L116 22 M99 9 L118 22 L100 35', stroke=color, width=4.8)

def highlight():
    return path('M8 12 Q116 5 263 12 L263 42 Q138 34 8 42 Z', '#f4de58', stroke='none', width=0)

def mismatch():
    return text(0,65,'Expenses',57,RED)+text(280,65,'>',67)+text(345,65,'income',57)+path('M18 93 Q236 102 550 93',width=3.4)

assets = {'PROP_FED':(fed(),300,250), 'PROP_BANK':(bank(),245,225), 'PROP_BILL':(bill(),210,230), 'PROP_NOTE':(note(),175,95), 'ANN_ARROW':(arrow(),125,45), 'ANN_HIGHLIGHT':(highlight(),275,55), 'DGM_EXPENSE_INCOME':(mismatch(),590,120)}
for name,(body,w,h) in assets.items():
    (ART/(name+'.svg')).write_text(svg(body,w,h))
for name,expr,pose in [('HOST_NEUTRAL','neutral','standing'),('HOST_POINT','explaining','pointing'),('HOST_BILL','surprised','holding'),('HOST_CONCERNED','concerned','standing')]:
    (ART/(name+'.svg')).write_text(svg(host(expr,pose),290,400))

# One original host shown across four expression/pose variants.
sheet = text(80,95,'Original host / pose & expression test',44)
for x,y,expr,pose,label in [(120,150,'neutral','standing','Neutral · standing'),(710,150,'explaining','pointing','Explaining · pointing'),(120,900,'surprised','holding','Surprised · paper grip'),(710,900,'concerned','standing','Concerned · standing')]:
    sheet += group(host(expr,pose),x,y,1.55,expr+'-variant') + text(x, y+655,label,32)
(ART/'CHARACTER_SHEET.svg').write_text(svg(sheet,1350,1650,True))

# Hero compositions are later states of persistent scenes, not proposed slides.
h1 = text(80,205,'Rates up.',90) + text(80,324,'Bill up, too.',90,RED)
h1 += group(fed(),105,440,2.05,'fed-building')
h1 += group(path('M18 201 L20 66 L3 84 L22 28 L53 82 L35 66 L35 201 Z',GREEN,width=4),785,475,1.2,'rate-arrow') + text(684,793,'Interest rate',38)
h1 += group(host('surprised','holding'),135,960,1.18,'host-surprised-grip')
h1 += group(bill(),625,1038,1.33,'fed-interest-bill') + group(arrow(RED),565,972,1.15,'bill-emphasis-arrow')
h1 += text(565,1405,'Fed interest bill',41,RED)
(ART/'HERO_01.svg').write_text(svg(h1,1080,1920,True))

h2 = text(80,195,'Reserves at the Fed.',70)
h2 += group(bank(),82,380,1.23,'commercial-bank') + group(fed(),593,385,1.1,'fed-building')
h2 += text(189,711,'Banks',48,anchor='middle') + text(750,711,'Fed',48,anchor='middle')
h2 += text(485,829,'≈$3T in reserves',57,anchor='middle')
# Dashed balances relationship is not a truck of cash or a timed reserve transfer.
h2 += '<g id="reserve-balance-relationship" fill="none" stroke="#171512" stroke-width="4" stroke-dasharray="10 9"><path d="M285 864 Q485 895 696 865"/><path d="M682 853 L701 864 L681 879"/></g>'
h2 += text(489,1022,'Interest paid to banks',49,GREEN,'middle')
h2 += group(path('M744 1090 Q507 1151 266 1090 M290 1074 L263 1090 L291 1106',stroke=GREEN,width=6),ident='interest-payment-flow')
h2 += group(note(),423,1080,0.8,'interest-note')
h2 += text(487,1300,'Higher rate = higher expense',49,RED,'middle') + text(487,1412,'for the Fed.',50,RED,'middle')
(ART/'HERO_02.svg').write_text(svg(h2,1080,1920,True))

h3 = text(80,195,'Losses build up.',78)
h3 += group(mismatch(),88,355,1.37,'expense-income-condition')
h3 += path('M480 520 Q483 576 480 632 M462 609 L480 632 L499 609',width=5)
h3 += text(480,720,'Deferred asset',61,anchor='middle') + text(480,844,'≈$234B',102,RED,'middle')
h3 += text(480,928,'7 October 2026 · cumulative',42,anchor='middle')
# Genuine source pixels, unchanged, plus a separate yellow annotation.
row = ROOT/'editable_sources'/'references'/'H41_20261008_row_final.png'
data='data:image/png;base64,'+base64.b64encode(row.read_bytes()).decode()
h3 += text(80,1081,'H.4.1 · real source excerpt',40)
h3 += f'<image id="government-excerpt-original-pixels" x="80" y="1130" width="840" height="96" xlink:href="{data}"/>'
h3 += '<g id="source-number-highlight" opacity="0.30">'+group(highlight(),786,1193,0.50,'separate-highlight')+'</g>'
h3 += text(80,1320,'Original units: millions of dollars',35) + text(80,1385,'Federal Reserve · release 8 Oct 2026',35)
h3 += text(80,1450,'federalreserve.gov/releases/h41/20261008/',30)
(ART/'HERO_03.svg').write_text(svg(h3,1080,1920,True))
print('Authored 4 host variants, 4 props, 2 annotations, 1 diagram; 4 static review compositions.')
