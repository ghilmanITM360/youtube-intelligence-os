import pathlib,subprocess,json,csv,io,hashlib,collections,zipfile,xml.etree.ElementTree as E
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21');ref='d41a5774f1381a21022b70f02d206303195be3a7';base='research/finance-economics-intelligence/'
def blob(p):return subprocess.check_output(['git','show',ref+':'+base+p])
u=list(csv.DictReader(io.StringIO(blob('reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv').decode())))
a=[json.loads(l)for l in blob('VIDEO_AUDIT_966.jsonl').splitlines()]
print('UNIVERSE KEYS',u[0].keys());print('STATUSES',collections.Counter(json.dumps(x['statuses'],sort_keys=True)for x in a).most_common(3))
print('UNIVERSE COUNTS',{k:dict(collections.Counter(x.get(k,'')for x in u))for k in ['population_layer','audit_status']})
ids=[x['video_id']for x in u];assert len(ids)==len(set(ids))==1612
m=list(csv.DictReader(io.StringIO(blob('VIDEO_MASTER.csv').decode())));assert len({x['Video_ID']for x in m})==966
# Existing workbook read only: all rows and saved cached values; no rebuild/recalculation.
w=blob('FINANCE_1612_COMBINED_INTELLIGENCE.xlsx');z=zipfile.ZipFile(io.BytesIO(w));ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ss=[''.join(t.itertext())for t in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)] if 'xl/sharedStrings.xml'in z.namelist()else []
def cells(f):
 d={}
 for c in E.fromstring(z.read(f)).findall('.//m:sheetData/m:row/m:c',ns):
  v=c.findtext('m:v','',ns)
  if c.get('t')=='s':v=ss[int(v)]
  elif c.get('t')=='inlineStr':v=''.join(c.find('m:is',ns).itertext())
  d[c.get('r')]=v
 return d
vs=cells('xl/worksheets/sheet2.xml');details=cells('xl/worksheets/sheet4.xml');dash=cells('xl/worksheets/sheet1.xml')
print('HEADERS',[(k,v)for k,v in vs.items()if k.endswith('4')and len(k)<5]);print('DETAILHEAD',[(k,v)for k,v in details.items()if k.endswith('4')and len(k)<5])
vids=[vs.get('A'+str(i),'')for i in range(5,1617)]; assert set(vids)==set(ids)and len(vids)==1612
errors=[]
for n in z.namelist():
 if n.startswith('xl/worksheets/')and n.endswith('.xml'):
  errors.extend((n,c.attrib)for c in E.fromstring(z.read(n)).findall('.//m:c',ns)if c.get('t')=='e')
result=dict(population=len(u),unique_ids=len(set(ids)),layers=dict(collections.Counter(x['population_layer']for x in u)),audit_status=dict(collections.Counter(x['audit_status']for x in u)),workbook_ids_match_universe=True,workbook_cached_dashboard={k:dash.get(k)for k in ['B5','B6','B7','B9']},workbook_formula_error_cells=errors,workbook_sha256=hashlib.sha256(w).hexdigest(),original_status_combinations=dict(collections.Counter(json.dumps(x['statuses'],sort_keys=True)for x in a)))
(A/'finance-independent-verification.json').write_text(json.dumps(result,indent=2));print(result)
# Rehash all original/local durable video pairs against established manifest.
manifest=json.loads(pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Media-Library/MACHINE_A_MEDIA_MANIFEST.json').read_text());checks=[]
for row in manifest:
 for k in ['path','durable_path']:
  p=pathlib.Path(row[k]);h=hashlib.sha256(p.read_bytes()).hexdigest();checks.append(dict(path=str(p),bytes=p.stat().st_size,sha256=h,match=h==row['sha256']))
assert all(x['match']for x in checks)
(A/'media-verification.json').write_text(json.dumps(dict(files=checks,manifest_entries=len(manifest),unique_hashes=len({x['sha256']for x in manifest}),unique_video_ids=len({x['video_id']for x in manifest}),bytes_one_copy=sum(x['bytes']for x in manifest)),indent=2));print('MEDIA',len(manifest),len(checks))
# Preserve unique ignored evidence in place; copied only useful ignored artifacts, not caches.
d=json.loads((A/'worktree-0-files.json').read_text());import shutil
for row in d['ignored']:
 if 'sha256'not in row or pathlib.Path(row['path']).name=='.DS_Store':continue
 p=pathlib.Path(row['path']);dst=A/'preserved-ignored'/p.relative_to(pathlib.Path.cwd());dst.parent.mkdir(parents=True,exist_ok=True)
 if not dst.exists():shutil.copy2(p,dst)
 assert hashlib.sha256(dst.read_bytes()).hexdigest()==row['sha256']
print('IGNORED_BACKUPS',sum(1 for p in (A/'preserved-ignored').rglob('*')if p.is_file()))
