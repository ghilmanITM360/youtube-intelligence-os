import subprocess,json,pathlib,csv,io,collections,hashlib,zipfile,xml.etree.ElementTree as E
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21');ref='d41a5774f1381a21022b70f02d206303195be3a7';base='research/finance-economics-intelligence/'
def blob(p):return subprocess.check_output(['git','show',ref+':'+base+p])
a=[json.loads(l)for l in blob('VIDEO_AUDIT_966.jsonl').splitlines()];m=list(csv.DictReader(io.StringIO(blob('VIDEO_MASTER.csv').decode())))
print('AUDIT KEYS',a[0].keys());print('MASTER',len(m),m[0].keys());print('STATUS SAMPLE',[(k,str(v)[:250])for k,v in a[-1].items() if not isinstance(v,dict)])
exp=[]
for p in ['expansion-12-channel-2026-10-20/FINANCE_EXPANSION_MASTER.csv','expansion-monkey-explains-1999-2026-10-21/FINANCE_EXPANSION_MASTER.csv']:
 rows=list(csv.DictReader(io.StringIO(blob(p).decode())));exp+=rows;print(p,len(rows),rows[0].keys())
validation=json.loads(blob('VALIDATION_966.json'));print('VALIDATION', {k:v for k,v in validation.items()if k not in ['batches','coverage']})
# Inspect XLSX ZIP directly without modifying or recalculating the existing workbook.
w=blob('FINANCE_1612_COMBINED_INTELLIGENCE.xlsx');z=zipfile.ZipFile(io.BytesIO(w));ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ss=[]
if 'xl/sharedStrings.xml'in z.namelist():
 ss=[''.join(x.itertext())for x in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]
sheets=[]
for s in E.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',ns):sheets.append(dict(s.attrib))
print('SHEETS',sheets)
for f in ['xl/worksheets/sheet1.xml','xl/worksheets/sheet2.xml','xl/worksheets/sheet3.xml']:
 if f not in z.namelist():continue
 root=E.fromstring(z.read(f));out=[]
 for row in root.findall('m:sheetData/m:row',ns)[:18]:
  vals=[]
  for c in row.findall('m:c',ns):
   v=c.findtext('m:v','',ns)
   if c.get('t')=='s':v=ss[int(v)]
   elif c.get('t')=='inlineStr':v=''.join(c.find('m:is',ns).itertext())
   vals.append((c.get('r'),v[:160]))
  out.append(vals)
 print(f,root.find('m:dimension',ns).attrib if root.find('m:dimension',ns)is not None else '',out[:12])
summary={'ref':ref,'original_master_rows':len(m),'audit_rows':len(a),'expansion_rows':len(exp),'validation':validation,'workbook_sha256':hashlib.sha256(w).hexdigest(),'workbook_bytes':len(w),'sheets':sheets,'audit_jsonl_sha256':hashlib.sha256(blob('VIDEO_AUDIT_966.jsonl')).hexdigest()}
(A/'finance-verification.json').write_text(json.dumps(summary,indent=2))
