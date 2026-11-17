"""Static SVG artwork authoring only. No animation, timeline, rig, or video code."""
from pathlib import Path
import base64, html

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'editable_sources' / 'original'
BLACK, RED, GREEN, CREAM = '#171512', '#b93839', '#55904f', '#f5efdc'
FONT = 'Chalkboard, Comic Sans MS, sans-serif'

def text(x, y, value, size=50, color=BLACK, anchor='start'):
    # Live lettering, small deliberate pen-like orientation differences. Font is not embedded.
    rotations = ' '.join(str([-1.7, .9, -.4, 1.3, -.8, .3][i % 6]) for i in range(len(value)))
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" text-anchor="{anchor}" rotate="{rotations}">{html.escape(value)}</text>'

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
    face = path('M78 63 C89 38 106 27 130 31 Q153 28 172 40 C190 46 210 68 215 91 Q221 113 211 131 C201 153 187 161 164 167 Q143 174 122 165 C101 158 79 148 74 123 Q66 94 78 63 Z', '#e8b780', width=3.9)
    hair = path('M79 84 Q66 74 70 61 Q72 44 86 35 L92 30 Q99 23 107 21 C125 11 146 15 158 19 L166 18 Q185 22 192 38 Q209 42 216 60 L215 68 L219 86 C203 63 195 49 183 41 Q158 61 135 69 L126 76 Q99 82 78 96 Z', '#433126', width=4.2)
    bun = path('M211 91 C239 82 255 105 244 124 C237 139 217 133 211 120 Z', '#433126', width=4)
    eyes = '<g id="eyes"><ellipse cx="120" cy="108" rx="3.7" ry="4.6" fill="#171512"/><ellipse cx="174" cy="106" rx="3.7" ry="4.6" fill="#171512"/></g>'
    brows = path('M109 94 Q119 88 130 92 M163 91 Q173 85 184 90', width=3)
    mouth = path('M128 137 Q144 143 157 135', width=3.4)
    if expression == 'explaining':
        mouth = path('M128 133 Q145 149 160 131 Q145 137 128 133 Z', '#fff', width=3)
    if expression == 'surprised':
        eyes = group(path('M109 100 Q119 94 126 101 Q132 112 121 120 Q109 121 109 100 Z M165 97 Q175 92 183 100 Q188 111 179 118 Q166 123 165 97 Z', '#fff', width=2.4) + '<ellipse cx="122" cy="108" rx="3.2" ry="4.6" fill="#171512"/><ellipse cx="179" cy="105" rx="3.1" ry="4.2" fill="#171512"/>', ident='eyes')
        brows = path('M106 87 Q116 76 128 82 M164 79 Q175 71 186 77', width=2.7)
        mouth = path('M140 132 Q127 128 130 146 Q132 154 142 151 Q154 146 148 135 Q144 132 140 132 Z', '#171512', width=2.6)
    if expression == 'concerned':
        brows = path('M107 97 Q121 97 128 84 M164 86 Q175 96 184 95', width=2.9)
        mouth = path('M127 145 Q141 132 154 139 L160 144', width=3.1)
    prop = ''
    if pose == 'holding':
        # Paper behind near thumb: grip remains visible; no floating bill.
        prop = group(path('M204 157 Q231 151 267 153 L265 190 L262 225 Q229 225 201 229 Z', CREAM, width=2.8) + path('M218 177 Q232 180 250 174 M217 190 Q225 186 235 190 L249 188 M216 210 L249 205', width=2.2), ident='held-paper')
        prop += group(path('M207 202 Q196 193 198 188 Q200 181 207 185 L214 190 M207 202 Q201 204 201 196', '#e8b780', width=2.8), ident='gripping-thumb')
    return legs + torso + arms + group(bun+face+hair+eyes+brows+mouth, ident='face-'+expression) + prop

def fed(label='FED'):
    # Original pediment, capitals, arched door and skewed stair edges; no copied BoJ dome/seal.
    body = path('M29 94 Q140 90 262 95 L264 207 Q143 211 31 207 Z', '#faf8ee', width=3.8)
    body += path('M15 89 Q80 55 148 23 Q210 51 277 87 L15 89 Z', CREAM, width=4.4)
    body += path('M39 87 Q146 81 254 85 M35 100 Q156 104 257 99', width=2.1)
    for x in [50,82,206,237]:
        body += path(f'M{x} 111 L{x+12} 110 L{x+10} 192 L{x+1} 194 Z', CREAM, width=2.4)
        body += path(f'M{x-4} 108 L{x+16} 108 M{x-3} 197 L{x+15} 197', width=2.8)
    body += path('M117 206 L119 161 Q141 134 163 160 L167 206 Z', '#d4c6a7', width=3.1)
    body += path('M143 154 Q140 180 143 207 M128 172 L135 171 M152 172 L159 173', width=1.9)
    body += path('M23 209 L271 208 L270 220 L23 222 Z M13 222 L280 220 L282 235 L11 236 Z', CREAM, width=3.1)
    return body + text(147, 73, label, 28, anchor='middle')

def bank():
    body = path('M18 45 Q117 37 215 41 L219 198 L15 200 Z', '#faf8ee', width=3.7)
    body += path('M9 23 L227 18 L227 54 Q117 50 10 57 Z', CREAM, width=3.1)
    body += path('M93 199 L94 148 Q115 134 139 145 L144 199 Z', '#d4c6a7', width=2.7)
    body += path('M117 144 Q120 175 116 199 M15 203 L220 201 L225 214 L9 216 Z', CREAM, width=2.5)
    body += path('M41 77 L80 74 L78 119 L39 121 Z M160 76 L196 79 L193 122 L158 119 Z', '#fff', width=2.7)
    body += path('M59 77 L61 119 M40 98 L79 95 M176 78 L178 119 M158 98 L194 100 M27 133 L72 132 M163 135 L207 137', width=1.7)
    return body + text(119, 46, 'BANK', 25, anchor='middle')

def bill():
    return path('M28 13 Q107 7 164 10 L185 33 Q182 112 180 215 Q107 213 20 218 Q23 111 28 13 Z', CREAM, width=3.2) + path('M164 10 L163 33 L185 33', width=2.3) + text(101, 66, 'BILL', 34, RED, 'middle') + path('M45 95 Q55 100 66 93 Q78 101 88 94 Q107 100 150 92 M44 120 Q52 115 60 121 L71 118 Q77 125 89 116 L107 120 L148 116 M43 148 Q76 150 126 142 M45 174 Q72 168 99 174 L148 171 M42 199 Q91 194 149 197', width=2.2)

def note():
    return path('M7 14 Q45 19 81 12 Q114 5 156 8 L157 78 Q117 72 82 79 Q40 87 10 83 Z', '#93b886', width=3.2) + path('M22 27 Q89 20 141 23 L140 66 Q83 71 23 67 Z', 'none', width=1.7) + path('M53 49 Q54 25 82 26 Q111 29 110 51 Q107 73 79 71 Q51 66 53 49 Z', '#a8c497', width=1.7) + text(82, 62, '$', 38, '#171512', 'middle') + path('M29 36 L42 33 M120 55 L134 52', width=1.5)

def arrow(color=BLACK):
    return path('M6 21 Q49 17 88 23 L116 22 M99 9 L118 22 L100 35', stroke=color, width=4.8)

def highlight():
    return path('M8 12 Q116 5 263 12 L263 42 Q138 34 8 42 Z', '#f4de58', stroke='none', width=0)

def mismatch():
    return text(0,65,'Expenses',57,RED)+text(280,65,'>',67)+text(345,65,'income',57)+path('M18 93 Q236 102 550 93',width=3.4)

def source_image(name, x, y, w, h, ident):
    raw = ROOT/'ARTICLE_EVIDENCE'/'crops'/name
    data = 'data:image/png;base64,' + base64.b64encode(raw.read_bytes()).decode()
    return f'<image id="{ident}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" xlink:href="{data}"/>'

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
h1 += group(host('surprised','holding'),120,948,1.27,'host-surprised-grip')
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
h2 += text(487,1250,'An expense for the Fed.',53,RED,'middle')
h2 += text(80,1345,'Reserve-interest rate / IORB',34)
h2 += source_image('B_IORB_focus.png',570,1295,330,90,'iorb-actual-source-number')
h2 += group(path('M5 10 Q139 2 342 9 L340 70 Q176 76 4 70 Z',stroke=RED,width=2.8),564,1310,ident='iorb-separate-highlight')
h2 += text(80,1453,'Fed implementation note · 16 Sep 2026',31)
(ART/'HERO_02.svg').write_text(svg(h2,1080,1920,True))

h3 = text(80,195,'Losses build up.',78)
h3 += group(host('concerned','standing'),66,303,.83,'host-concerned')
h3 += group(mismatch(),338,402,.98,'expense-income-condition')
h3 += group(path('M480 547 Q475 597 480 662 M463 641 L480 664 L500 642',width=3.8),ident='condition-to-deferred-arrow')
h3 += text(480,747,'Deferred asset',64,anchor='middle') + text(480,861,'≈$234B',102,RED,'middle')
h3 += text(480,943,'7 October 2026 · cumulative',39,anchor='middle')
# Two genuine table-cell crops are openly separated for legibility, not a manufactured table.
h3 += text(80,1050,'H.4.1 / actual table row',37)
h3 += source_image('C_DEFERRED_label_SHARP.png',85,1082,700,112,'source-row-label')
h3 += source_image('C_DEFERRED_value_SHARP.png',216,1195,520,212,'source-row-total')
h3 += group(path('M10 18 Q190 9 535 15 L533 164 Q304 170 8 166 Z',stroke=RED,width=3.2),185,1235,ident='source-number-highlight')
h3 += text(80,1450,'Millions of dollars · Fed release 8 Oct 2026',31)
(ART/'HERO_03.svg').write_text(svg(h3,1080,1920,True))
print('Authored 4 host variants, 4 props, 2 annotations, 1 diagram; 4 static review compositions.')

# Static editor addresses. IDs are geometry/text layers, not a rig or animation engine.
import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
for file in ART.glob('*.svg'):
    tree = ET.parse(file)
    seen, counts = set(), {}
    for element in tree.getroot().iter():
        tag = element.tag.split('}')[-1]
        counts[tag] = counts.get(tag, 0) + 1
        ident = element.get('id', f'{tag}-{counts[tag]:02d}')
        if ident in seen:
            ident = f'{ident}-{counts[tag]:02d}'
        element.set('id', ident)
        seen.add(ident)
    tree.write(file, encoding='unicode')
