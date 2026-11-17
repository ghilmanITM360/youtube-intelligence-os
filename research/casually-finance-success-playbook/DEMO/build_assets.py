"""Generate original Mira SVG variants and one shared environment; no competitor art."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT/'assets'
INK='#243247'; FACE='#EDB76A'; JACKET='#157A78'; HAIR='#56384D'

def character(pose, expression):
    arms={
      'stand':('M112 250 Q90 300 96 349','M248 250 Q270 300 264 349'),
      'point':('M112 250 Q90 300 96 349','M248 250 L288 230 L332 216'),
      'explain':('M112 250 L77 289 L37 267','M248 250 L283 289 L323 267')}
    face={
      'neutral':'<path d="M150 166 Q180 177 209 166"/><path d="M136 122 L158 120 M202 120 L224 122"/>',
      'concerned':'<path d="M150 177 Q180 160 209 177"/><path d="M136 119 L158 127 M202 127 L224 119"/>',
      'curious':'<path d="M161 169 Q181 182 202 168"/><path d="M136 119 L158 121 M202 113 L224 109"/>'}
    a,b=arms[pose]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 540" role="img" aria-label="Mira {pose} {expression}">
<g stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
<path d="M128 353 L123 486 L165 486 L180 374 L195 486 L237 486 L232 353" fill="{INK}"/>
<path d="M120 483 L165 483 L169 513 L105 513 Q100 497 120 483 M195 483 L237 483 L254 513 L191 513Z" fill="{HAIR}"/>
<path d="M110 248 Q113 222 145 217 L215 217 Q247 222 250 248 L235 366 L125 366Z" fill="{JACKET}"/>
<path d="M154 217 L180 264 L206 217" fill="#FFF9EC"/>
<path d="{a}" fill="none" stroke="{JACKET}" stroke-width="29"/>
<path d="{b}" fill="none" stroke="{JACKET}" stroke-width="29"/>
<circle cx="{96 if pose!='explain' else 37}" cy="{349 if pose!='explain' else 267}" r="14" fill="{FACE}"/>
<circle cx="{264 if pose=='stand' else 332 if pose=='point' else 323}" cy="{349 if pose=='stand' else 216 if pose=='point' else 267}" r="14" fill="{FACE}"/>
<rect x="112" y="60" width="136" height="143" rx="45" fill="{FACE}"/>
<path d="M112 108 Q94 45 148 34 Q225 10 256 69 L249 114 Q225 92 218 61 Q185 93 112 108" fill="{HAIR}"/>
<path d="M151 143 L151 145 M209 143 L209 145" stroke-width="10"/>
<path d="M180 146 L175 155 L184 155" fill="none" stroke-width="4"/>
<g fill="none" stroke-width="5">{face[expression]}</g>
</g></svg>'''

def main():
    ASSETS.mkdir(exist_ok=True)
    variants=[]
    for pose in ['stand','point','explain']:
      for expression in ['neutral','concerned','curious']:
        name=f'mira_{pose}_{expression}.svg';(ASSETS/name).write_text(character(pose,expression));variants.append(name)
    (ASSETS/'environment.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="#FFF9EC"/><rect y="874" width="1920" height="206" fill="#E9DBC4"/><path d="M0 874H1920" stroke="#C7B89F" stroke-width="5"/><g fill="none" stroke="#C7B89F" stroke-width="8"><rect x="105" y="245" width="365" height="282" rx="20"/></g><g fill="#E0D5C4"><rect x="125" y="265" width="325" height="242" rx="12"/></g><path d="M85 773H640V809H85Z" fill="#7358A6"/><path d="M127 809V1000M594 809V1000" stroke="#56384D" stroke-width="24"/><path d="M480 773V663L515 608" fill="none" stroke="#243247" stroke-width="10"/><path d="M478 640L510 583L566 620Z" fill="#D55B47"/></svg>''')
    (ROOT/'asset-manifest.json').write_text(json.dumps({'original_character':'Mira','authored_rigs':1,'derived_pose_expression_variants':9,'poses':['stand','point','explain'],'expressions':['neutral','concerned','curious'],'environment_kits':1,'files':variants+['environment.svg'],'not_nine_unique_illustrations':True},indent=2)+'\n')
    grid='<svg xmlns="http://www.w3.org/2000/svg" width="900" height="900" viewBox="0 0 900 900"><rect width="900" height="900" fill="#FFF9EC"/>'
    for i,n in enumerate(variants):
      grid+=f'<image href="assets/{n}" x="{(i%3)*300+55}" y="{(i//3)*300}" width="190" height="270"/><text x="{(i%3)*300+30}" y="{(i//3)*300+290}" font-family="sans-serif" font-size="16">{n[5:-4].replace("_"," / ")}</text>'
    (ROOT/'character-grid.svg').write_text(grid+'</svg>')
    print('1 original rig, 9 derived states, 1 environment generated')

if __name__=='__main__': main()
