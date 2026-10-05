import csv,io,json,subprocess,zipfile,xml.etree.ElementTree as E
from pathlib import Path
r=Path(__file__).resolve().parent.parents[1]
root=r.parents[2]
n={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def parse(z):
 ss=[''.join(t.itertext()) for t in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',n)]
 out={}
 for k in range(1,12):
  doc=E.fromstring(z.read(f'xl/worksheets/sheet{k}.xml'))
  cells={}
  for c in doc.findall('.//m:sheetData/m:row/m:c',n):
   v=c.findtext('m:v',default='',namespaces=n)
   if c.get('t')=='s':v=ss[int(v)]
   f=c.findtext('m:f',default='',namespaces=n)
   cells[c.get('r')]=(f,v)
  out[k]=(doc,cells)
 return out
before=parse(zipfile.ZipFile(io.BytesIO(subprocess.check_output(['git','show','HEAD:docs/research/thumbnail-forensics-2026-10-02/PACKAGING-PROGRESS.xlsx'],cwd=root))))
after=parse(zipfile.ZipFile(r/'PACKAGING-PROGRESS.xlsx'))
s=json.loads((r/'packaging-progress-summary.json').read_text())
assert len(after)==11
assert after[1][1]['H11'][1]==str(s['thumbnails']['verified'])
assert after[1][1]['B15'][1]==str(s['packages']['audited'])
assert after[1][1]['E15'][1]==str(s['packages']['qa_sampled'])
assert abs(float(after[1][1]['G25'][1])-s['progress']['composite'])<1e-10
for sheet,col,count in [(2,'B',75),(3,'D',2303)]:
 ids=[after[sheet][1][f'{col}{i}'][1] for i in range(2,count+2)]
 assert len(ids)==len(set(ids))==count
 assert after[sheet][0].find('m:sheetViews/m:sheetView/m:pane',n) is not None
 assert after[sheet][0].find('m:tableParts',n) is not None
assert any(x.get('type')=='dataBar' for x in after[1][0].findall('.//m:cfRule',n))
assert any(x.get('type')=='dataBar' for x in after[2][0].findall('.//m:cfRule',n))
assert after[4][1]['B15'][1]==s['current_channel']['next_Video_ID']
for k in [5,6,7,8,11]:
 assert before[k][1]==after[k][1],f'Unrelated sheet {k} modified'
for k in range(1,12):
 for cell,(formula,value) in after[k][1].items():
  assert value not in ('#REF!','#DIV/0!','#VALUE!','#NAME?','#NUM!','#SPILL!','#CALC!'),(k,cell,value)
print(json.dumps(dict(sheets=11,channel_rows=75,video_rows=2303,unique_IDs='PASS',data_bars='PASS',tables_filters_and_freeze_panes='PASS',summary_reconciliation='PASS',unrelated_sheets_preserved='PASS',formula_error_scan='PASS')))
