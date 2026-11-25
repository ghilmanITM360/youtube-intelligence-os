from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt
p=Path('/private/tmp/unreasonably-exact-script-rewrite-v3')
files=sorted((p/'revised_scripts_v3').glob('SCRIPT_*.md'))
assert len(files)==10
rows=[]
def count(t): return len(re.findall(r"\b[\w]+(?:['’][\w]+)*\b",t))
d=Document(); d.sections[0].header_distance=Inches(.5)
d.styles['Normal'].font.name='Arial'; d.styles['Normal'].font.size=Pt(11)
for i,f in enumerate(files):
 s=f.read_text(); title=re.search(r'^title: (.+)$',s,re.M).group(1); body=s.split('## Voiceover\n',1)[1].split('\n## Sources',1)[0].strip(); n=count(body); slot=int(f.name[7:9]); fmt='Long' if slot in [1,4,6,8] else 'Short'; seconds=n/150*60
 duration='78.2 seconds measured' if slot==2 else f'{int(seconds//60)}:{int(round(seconds%60)):02d} estimated at 150 wpm, before pauses'
 rows.append((slot,title,fmt,n,duration,f.name))
 if i: d.add_page_break()
 d.add_heading(f'{slot:02d}  {title}',0)
 d.add_paragraph(f'{fmt}  |  {n} words  |  {duration}')
 if slot==1: d.add_paragraph('Editorial alternative — owner review required.')
 for para in body.split('\n\n'): d.add_paragraph(para)
d.save(p/'UNREASONABLY_EXACT_10_VOICEOVER_SCRIPTS_V3.docx')
(p/'SCRIPT_INDEX.md').write_text('# Script index\n\nCounting method: regex `\\b[\\w]+(?:[\'’][\\w]+)*\\b` on narration only; contractions count as one token and numeric groups count as one. Estimates use 150 words/minute without pauses. Slot 02 is measured.\n\n| Slot | Title | Format | Words | Duration | File |\n|---|---|---|---:|---|---|\n'+''.join(f'| {s:02} | {t} | {fmt} | {n} | {dur} | [{f}](revised_scripts_v3/{f}) |\n' for s,t,fmt,n,dur,f in rows))
print('\n'.join(str(x) for x in rows))
