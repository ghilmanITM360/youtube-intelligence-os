"""Read-only reconciliation of the saved Office deliverables."""
from pathlib import Path
import csv,json,sys,hashlib,zipfile
from datetime import datetime,timezone
from docx import Document
from openpyxl import load_workbook
root=Path(sys.argv[1]);out=root/'OFFICE';path=out/'Casually_Finance_Analysis.xlsx'
rows=list(csv.DictReader((root/'VIDEO_PERFORMANCE.csv').open()));w=load_workbook(path,data_only=True);f=load_workbook(path,data_only=False);s=w['Video performance'];assert len(rows)==206 and len(w.sheetnames)==10
for i,r in enumerate(rows,5):
 assert s.cell(i,1).value==r['Video_ID'];assert s.cell(i,3).value==r['Title'];assert s.cell(i,5).value==int(r['Public_Views']);assert s.cell(i,29).value==r['Tier'];assert f['Video performance'].cell(i,2).hyperlink.target==r['URL']
 expected=datetime.fromisoformat(r['Publish_Date']).astimezone(timezone.utc).replace(tzinfo=None)
 assert abs((s.cell(i,4).value-expected).total_seconds())<.01
 assert abs(s.cell(i,11).value-float(r['Views_Per_Day']))<.06
 if r['Tier']!='INSUFFICIENT_DATA':assert abs(s.cell(i,28).value-float(r['Performance_Ratio']))<.001
 for j in [5,8,10,11]:assert isinstance(s.cell(i,j).value,(int,float))
for row in w['Summary'].iter_rows(min_row=6,max_row=12,min_col=1,max_col=3):
 tier,lf,short=[c.value for c in row];assert lf==sum(r['Format']=='LONG_FORM' and r['Tier']==tier for r in rows);assert short==sum(r['Format']=='SHORT' and r['Tier']==tier for r in rows)
errors=[]
for sheet in w:
 for row in sheet:
  errors.extend(f'{sheet.title}!{c.coordinate}:{c.value}' for c in row if c.data_type=='e' or isinstance(c.value,str) and 'not implemented' in c.value)
assert not errors,errors
for coord in ['D6','D16','D26']:assert w['Scorecards'][coord].value=='INCOMPLETE'
links=sum(c.hyperlink is not None for sh in f for row in sh for c in row);assert links==272
doc=Document(out/'Casually_Finance_Analysis.docx');headers=[p.text for p in doc.paragraphs if p.style.name=='Heading 1'];assert len(headers)==10,headers
full='\n'.join(p.text for p in doc.paragraphs)+'\n'+'\n'.join(c.text for t in doc.tables for row in t.rows for c in row.cells)
assert '7,503.2' in full and 'Shots/min' in full and 'States/min' in full
assert 'Credit wave typical' in full and 'something-off-2026 top performer' in full
assert 'asserted mismatch between interest paid' in full
with zipfile.ZipFile(out/'Casually_Finance_Analysis.docx') as z:doc_links=z.read('word/_rels/document.xml.rels').count(b'/hyperlink')
result={'status':'PASS','video_records':206,'worksheets':w.sheetnames,'native_excel_hyperlinks':links,'word_hyperlinks':doc_links,'typed_dates_numbers':True,'csv_tier_metadata_reconciliation':True,'cached_formula_error_count':0,'scorecard_input_change_test':'PASS in Artifact Tool; blank and zero evidence tested','word_sections':headers,'native_application_check':'LibreOffice DOCX rendered; Excel validated with Artifact Tool and saved-file read-only checks, not a live Microsoft Excel session','sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.glob('*') if p.suffix in ['.docx','.xlsx']}}
(out/'OFFICE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
