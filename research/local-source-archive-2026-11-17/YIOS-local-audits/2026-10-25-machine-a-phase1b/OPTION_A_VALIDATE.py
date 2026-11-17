import pathlib,subprocess as s,json,hashlib,csv,io,re,collections,ast
D=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-25-machine-a-phase1b');P=D/'OPTION_A_EXECUTION_RECEIPT.json';x=json.loads(P.read_text());R=json.loads((D/'ANCESTRY_INTEGRATION_VERIFICATION.json').read_text());base=R['main']
def g(*a):return s.check_output(['git',*a]).decode().strip()
def blob(ref,p):return s.check_output(['git','show',ref+':'+p])
def sha(b):return hashlib.sha256(b).hexdigest()
files=[];formats=collections.Counter();csv_defects=[]
for row in R['archive_files']:
 p=row['path'];b=pathlib.Path(p).read_bytes();src=blob(R['head'],p);committed=blob('HEAD',p)
 assert b==src==committed and len(b)==row['bytes'] and sha(b)==row['sha256'],p
 if p.endswith('.json'):json.loads(b);formats['json']+=1
 if p.endswith('.py'):ast.parse(b);formats['python_ast']+=1
 if p.endswith('.csv'):
  rows=list(csv.reader(io.StringIO(b.decode('utf-8-sig'))));bad=[i+1 for i,v in enumerate(rows) if len(v)!=len(rows[0])];formats['csv_parsed']+=1
  if bad:csv_defects.append({'path':p,'rows':bad})
 files.append(row)
assert len(files)==397 and sum(v['bytes'] for v in files)==8221384
expected={v['path'] for v in files}|{'docs/YIOS_MASTER_PLAN.md','docs/AI_SESSION_CONTEXT.md','README.md'}
diff=g('diff','--name-status',base).splitlines();assert len(diff)==400 and {z.split('\t')[-1] for z in diff}==expected
assert collections.Counter(z.split('\t')[0] for z in diff)=={'A':399,'M':1}
commits=g('rev-list',base+'..HEAD').splitlines();finance={z.split()[0] for z in R['finance']['commits']};assert not finance.intersection(commits)
assert g('merge-base',base,'HEAD')==base
for row in x['mapping']:assert g('rev-parse',row['new']+'^')==row['parent']
assert sha(pathlib.Path('README.md').read_bytes())==R['readme_simulation']['result_sha256']
links=[]
for name in ['docs/YIOS_MASTER_PLAN.md','docs/AI_SESSION_CONTEXT.md']:
 for url in re.findall(r'\]\(([^)]+)\)',pathlib.Path(name).read_text()):
  if not re.match(r'https?://',url):
   path=(pathlib.Path(name).parent/url.split('#')[0]).resolve();assert path.exists(),(name,url);links.append({'doc':name,'url':url,'exists':True})
brain=pathlib.Path('research/visual-forensics/channels/CH-000004/what-if-source-package/production_intelligence_brain');rel=json.loads((brain/'RELEASE_MANIFEST.json').read_text());manifest_checks=[]
for row in rel['files']:
 path=brain/row['relative_path']
 if path.is_file():
  b=path.read_bytes();assert sha(b)==row['sha256'] and len(b)==row['size_bytes'],str(path);manifest_checks.append(str(path))
assert len([p for p in manifest_checks if '/01_master_data/MASTER_' in p])==8
contract=json.loads(pathlib.Path('data/manifests/what-if-forensic-source-v1.json').read_text());assert len(contract['sources'])==14
for path,digest in contract['source_artifact_sha256'].items():assert sha((brain/path).read_bytes())==digest
assert collections.Counter(v['mapping_status'] for v in contract['sources'])=={'VERIFIED':12,'UNRESOLVED':2}
assert not g('diff',base,'--','scripts','data','schemas','tests')
assert not g('diff',base,'--','research/finance-economics-intelligence')
for f,stat in x['untracked_ignored_stat'].items():
 a=pathlib.Path(f).lstat();assert [a.st_size,a.st_mtime_ns,a.st_ino]==stat,f
assert g('stash','list','--format=%H %gd %s')==x['stash']
# Whitespace warnings are immutable archive baseline. Strip only path-prefix differences (none expected).
a=s.run(['git','diff','--check',R['finance_sha'],R['head'],'--',*[v['path'] for v in files]],capture_output=True,text=True)
b=s.run(['git','diff','--check',base,'HEAD','--',*[v['path'] for v in files]],capture_output=True,text=True)
assert a.stdout==b.stdout and a.returncode==b.returncode
(D/'OPTION_A_HISTORICAL_WHITESPACE.txt').write_text(b.stdout)
x['local_validation']={'archive_files':files,'archive_count':397,'archive_bytes':8221384,'path_count':400,'status_counts':{'A':399,'M':1},'paths':diff,'finance_commits_inherited':0,'commits':commits,'formats':dict(formats),'csv_defects':csv_defects,'relative_doc_links':links,'release_manifest_present_entries_verified':len(manifest_checks),'master_tables_verified':8,'source_contract':{'sources':14,'VERIFIED':12,'UNRESOLVED':2,'artifacts_hash_equal':True},'runtime_data_schemas_tests_unchanged':True,'readme_main_plus_navigation':True,'untracked_ignored_stat_unchanged':True,'stash_unchanged':True,'historical_whitespace_equal_source':True,'historical_whitespace_warning_lines':len(b.stdout.splitlines()),'regressions':'35 passed in 1.00s','external_media_execution':'BLOCKED / NOT_RUN: external media/runtime restoration outside scope'}
P.write_text(json.dumps(x,indent=2));print('PASS',397,8221384,'400 paths; zero Finance ancestors; formats',dict(formats),'CSV defect files',len(csv_defects),'links',len(links),'release entries',len(manifest_checks))
