from pathlib import Path
import csv,json,re,sys
from datetime import datetime
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

root=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
files=['EXECUTIVE_FINDINGS.md','TITLE_THUMBNAIL_PLAYBOOK.md','TOPIC_TREND_ANALYSIS.md','SCRIPT_STORYTELLING_ANALYSIS.md','VISUAL_MOTION_PRODUCTION_DNA.md','ASSET_FACTORY_AND_CODEX_FEASIBILITY.md','ORIGINAL_CHANNEL_PRODUCTION_SOP.md','IMPROVEMENT_OPPORTUNITIES.md','EVIDENCE_AND_LIMITATIONS.md']
repo='https://github.com/ghilmanITM360/youtube-intelligence-os/blob/research/casually-finance-success-playbook/'
def clean(s): return re.sub(r'\*\*|`','',s).strip()
def visible(s):return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1',clean(s))
def linkurl(s):
 if s.startswith('http'):return s
 return repo+str((Path('research/casually-finance-success-playbook')/s)).replace('research/casually-finance-success-playbook/../../','')
def inline(p,s):
 pattern=r'\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|`([^`]+)`'
 pos=0
 for m in re.finditer(pattern,s):
  p.add_run(s[pos:m.start()]);pos=m.end()
  if m.group(1):
   h=OxmlElement('w:hyperlink'); h.set(qn('r:id'),p.part.relate_to(linkurl(m.group(2)),RT.HYPERLINK,is_external=True))
   r=OxmlElement('w:r');pr=OxmlElement('w:rPr');col=OxmlElement('w:color');col.set(qn('w:val'),'245A81');pr.append(col);r.append(pr);t=OxmlElement('w:t');t.text=m.group(1);r.append(t);h.append(r);p._p.append(h)
  else:
   r=p.add_run(m.group(3) or m.group(4));r.bold=bool(m.group(3))
   if m.group(4):r.font.name='Consolas';r.font.size=Pt(9)
 p.add_run(s[pos:])
def tables(text):
 lines=text.splitlines();result=[];head='';i=0
 while i<len(lines):
  if lines[i].startswith('#'):head=re.sub(r'^#+\s*','',lines[i])
  if lines[i].startswith('|') and i+1<len(lines) and re.match(r'^\|[\s:|\-]+$',lines[i+1]):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    if not re.match(r'^\|[\s:|\-]+$',lines[i]):rows.append([clean(x) for x in lines[i].strip('|').split('|')])
    i+=1
   result.append({'heading':head,'rows':rows});continue
  i+=1
 return result
doc=Document(); sec=doc.sections[0];sec.top_margin=Inches(.7);sec.bottom_margin=Inches(.65);sec.left_margin=sec.right_margin=Inches(.7)
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3']:
 st=doc.styles[name];st.font.name='Calibri';st.font.color.rgb=RGBColor(0,0,0)
 for border in st.element.findall('.//'+qn('w:pBdr')):border.getparent().remove(border)
doc.styles['Normal'].font.size=Pt(10);doc.styles['Normal'].paragraph_format.space_after=Pt(5)
doc.styles['Normal'].paragraph_format.line_spacing=1.06
doc.styles['Title'].font.size=Pt(25)
for n,size in [('Heading 1',18),('Heading 2',13),('Heading 3',11)]:doc.styles[n].font.size=Pt(size)
doc.core_properties.title='Casually Finance Success and Production Analysis';doc.core_properties.author='YouTube Intelligence OS'
doc.add_paragraph('Casually Finance Success and Production Analysis','Title')
doc.add_paragraph('Research and original channel production playbook','Subtitle')
doc.add_paragraph('Prepared 13 October 2026. Public performance snapshot 11 October 2026.')
doc.add_paragraph('Build original videos around a concrete financial anomaly, one understandable mechanism and a truthful payoff. This report examines 206 distinct public uploads and reuses existing source-backed research from 16 available videos. It explains observable differences in reach, packaging, storytelling and visual production, then provides a practical original production system.')
doc.add_paragraph('Public views show relative reach. They cannot establish which title, thumbnail, hook or animation caused success. CTR, retention, impressions and traffic sources are unavailable. Facts, measured associations, interpretations, hypotheses and recommendations remain distinguishable throughout.')
doc.add_heading('How to use the analysis',1)
doc.add_paragraph('Read the executive findings first. Use the companion Excel workbook to sort all 206 uploads, examine performance peers and sensitivity, compare title and topic patterns, and complete your own editorial scorecards. The remaining chapters provide evidence-linked storyboards, visual methods, asset specifications, production gates and test plans.')
for i,f in enumerate(files,1):doc.add_paragraph(f'{i}. '+re.sub(r'^#\s*','',(root/f).read_text().splitlines()[0]))
doc.add_paragraph('Video links open the exact upload. Repository evidence links open the research branch on GitHub. Source files are frozen at the documented research base; titles and transcript interpretations are not independently certified by this report.')
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
footer.add_run('Casually Finance analysis  |  ')
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
alltables={}
for fi,f in enumerate(files):
 text=(root/f).read_text();alltables[f]=tables(text)
 if f=='EXECUTIVE_FINDINGS.md':text=text.split('## Demonstration result')[0]
 lines=text.splitlines();i=0;code=False
 while i<len(lines):
  line=lines[i];i+=1
  if line.startswith('```'):code=not code;continue
  if not line.strip():continue
  if line.startswith('!['):
   if Path('/private/tmp/cf-performance-chart.png').exists():doc.add_picture('/private/tmp/cf-performance-chart.png',width=Inches(6.8))
   continue
  if code:
   p=doc.add_paragraph();p.paragraph_format.space_after=Pt(1);p.paragraph_format.keep_with_next=True
   r=p.add_run(line);r.font.name='Consolas';r.font.size=Pt(8.5);continue
  if line.startswith('#'):
   lev=min(len(line)-len(line.lstrip('#')),3);original=re.sub(r'^#+\s*','',line);title=re.sub(r'[^\w\s]',' ',visible(original));title=' '.join(title.split());heading=doc.add_heading(title,lev)
   if lev==1 and fi==0:heading.paragraph_format.page_break_before=True
   if '](' in original:inline(doc.add_paragraph(),original)
   continue
  if line.startswith('|') and i<len(lines) and re.match(r'^\|[\s:|\-]+$',lines[i]):
   rows=[[x.strip() for x in line.strip('|').split('|')]];i+=1
   while i<len(lines) and lines[i].startswith('|'):
    rows.append([x.strip() for x in lines[i].strip('|').split('|')]);i+=1
   n=len(rows[0])
   if n==6:
    rows=[['Video and title','Saved views','Age days','Relative tier and confidence']]+[[r[0]+'\n'+r[1],r[2],r[3],r[4]+'\n'+r[5]] for r in rows[1:]];n=4
   elif n==7 and rows[0][0]=='Feature':
    rows=[['Title feature','Long form','Aged Shorts']]+[[r[0],'n '+r[1]+'\nMedian ratio '+r[2]+'\nWithout feature '+r[3],'n '+r[4]+'\nMedian ratio '+r[5]+'\nWithout feature '+r[6]] for r in rows[1:]];n=3
   elif n==7:
    original=rows;rows=[['Metric',original[1][0],original[2][0]]]+[[original[0][j],original[1][j],original[2][j]] for j in range(1,7)];n=3
   table=doc.add_table(rows=0,cols=n);table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
   # Allocate widths to actual text density while keeping short columns compact.
   weights=[max(12,min(65,sum(len(visible(r[j])) for r in rows[:])/len(rows))) for j in range(n)]
   if rows[0][0]=='Title feature':weights=[27,42,42]
   widths=[6.85*w/sum(weights) for w in weights]
   for j,w in enumerate(widths):table.columns[j].width=Inches(w)
   pr=table._tbl.tblPr;borders=OxmlElement('w:tblBorders')
   for edge in ['top','left','bottom','right','insideH','insideV']:
    el=OxmlElement('w:'+edge);el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
   pr.append(borders)
   for ri,row in enumerate(rows):
    cells=table.add_row().cells
    for j,val in enumerate(row):
     cells[j].width=Inches(widths[j]);cells[j].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
     tcpr=cells[j]._tc.get_or_add_tcPr();marg=OxmlElement('w:tcMar')
     for ed in ['top','bottom','left','right']:
      e=OxmlElement('w:'+ed);e.set(qn('w:w'),'90');e.set(qn('w:type'),'dxa');marg.append(e)
     tcpr.append(marg);sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'E6EDF2' if ri==0 else ('F6F8FA' if ri%2==0 else 'FFFFFF'));tcpr.append(sh)
     p=cells[j].paragraphs[0];p.paragraph_format.space_after=Pt(2);p.paragraph_format.line_spacing=1
     inline(p,val)
     for r in p.runs:r.font.size=Pt(9);r.bold=ri==0 or r.bold
    if ri==0:
     repeat=OxmlElement('w:tblHeader');table.rows[ri]._tr.get_or_add_trPr().append(repeat)
    cant=OxmlElement('w:cantSplit');table.rows[ri]._tr.get_or_add_trPr().append(cant)
   doc.add_paragraph().paragraph_format.space_after=Pt(2);continue
  style='Normal'
  if line.startswith('- '):style='List Bullet';line=line[2:]
  elif re.match(r'^\d+\. ',line):style='Normal'
  inline(doc.add_paragraph(style=style),line)
doc.save(out/'Casually_Finance_Analysis.docx')
records=list(csv.DictReader((root/'VIDEO_PERFORMANCE.csv').open()))
data={'videos':records,'tables':alltables,'summary':json.loads((root/'ANALYTICS_SUMMARY.json').read_text()),'source_hashes':json.loads((root/'SOURCE_HASHES.json').read_text())}
Path('/private/tmp/cf-office-data.json').write_text(json.dumps(data))
print(json.dumps({'docx':str(out/'Casually_Finance_Analysis.docx'),'videos':len(records),'chapters':len(files)}))
