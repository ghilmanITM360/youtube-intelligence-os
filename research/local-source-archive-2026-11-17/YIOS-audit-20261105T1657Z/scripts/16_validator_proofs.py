# Isolated proofs against a scratch copy; only scratch/proof is mutated. Canonical repo untouched.
import sys,os,json,sqlite3,glob,re,collections,pathlib,copy,csv
P=sys.argv[1];RF=P+'/research/finance-economics-intelligence/reference-framework';sys.path.insert(0,RF)
import reference_comparison as rc, content_plan_check as cp
res={}
comps=sorted(glob.glob(RF+'/comparisons/*.json'));print('comparison files',[os.path.basename(c) for c in comps])
print('baseline check_coverage',rc.check_coverage()[:3])
# A: corrupted comparison passes coverage gate; direct validate fails
target=RF+'/comparisons/NICK_281_REFERENCE_COMPARISON.json';orig=open(target).read()
d=json.loads(orig);d2=copy.deepcopy(d);d2['comparisons']=[];d2['rule_index_version']='BROKEN';d2['assessment_mode']='PROSPECTIVE_AUDIT'
open(target,'w').write(json.dumps(d2))
res['A_coverage_after_corrupting_NICK_281']=rc.check_coverage();res['A_direct_validate_on_same_file']=rc.validate(target)
open(target,'w').write('{}');res['A2_coverage_with_empty_object']=rc.check_coverage()
open(target,'w').write(orig)
# B: fabricated TITLE witness
d3=copy.deepcopy(d);n=0
for c in d3['comparisons']:
  if (c.get('witness') or {}).get('kind') in('TITLE','THUMBNAIL_OBSERVATION'):
    c['witness']['text']='FABRICATED TEXT THAT IS NOT THE TITLE';n+=1
open('/tmp/x','w') if False else None
fp=P+'/fab.json';json.dump(d3,open(fp,'w'));res['B_fabricated_title_or_thumb_witnesses_changed']=n;res['B_validate_errors']=rc.validate(fp)
# C: meaningless plan
db=P+'/data/knowledge/reference_knowledge.db';con=sqlite3.connect(f'file:{db}?mode=ro',uri=True)
sid=con.execute('select section_id from ref_section limit 1').fetchone()[0];rid=con.execute("select rule_id from ref_rule where framework_version='v1' and rule_class!='NOT_APPLICABLE' limit 1").fetchone()[0]
plan={'plan_id':'x','framework_version':'v1','retrieved':[sid],'applications':[{'stage':s,'rule_id':rid,'implementation':'x'} for s in cp.STAGES]}
res['C_plan_one_char_impl_same_rule_all_stages']=cp.check(db,plan)
plan2=copy.deepcopy(plan)
for a in plan2['applications']: a.pop('implementation');a['exception']='.'
res['C2_plan_exception_dot_all_stages']=cp.check(db,plan2)
# D: real witnesses vs actual titles
reg=sqlite3.connect(f'file:{P}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
cols=[r[1] for r in reg.execute('pragma table_info(videos)')];print('videos cols',cols[:12])
titlecol='title' if 'title' in cols else [c for c in cols if 'title' in c][0]; idc='youtube_video_id' if 'youtube_video_id' in cols else [c for c in cols if 'video_id' in c][0]
files=comps+sorted(glob.glob(P+'/research/finance-economics-intelligence/reanalysis/**/*.json',recursive=True))
st=collections.Counter();bad=[];nf=0
def norm(s):return re.sub(r'\s+',' ',s or '').strip().lower()
for f in files:
  try:j=json.load(open(f))
  except Exception:continue
  if not isinstance(j,dict) or 'comparisons' not in j:continue
  nf+=1;row=reg.execute(f'select {titlecol} from videos where {idc}=?',(j.get('video_id'),)).fetchone();t=norm(row[0]) if row else None
  for c in j['comparisons']:
    w=c.get('witness') or {};k=w.get('kind') or 'NONE';st[k]+=1
    if k=='TITLE':
      if t is None: st['TITLE_no_registry_title']+=1
      elif norm(w.get('text')) in t: st['TITLE_substring_of_actual']+=1
      else: st['TITLE_NOT_in_actual']+=1;bad.append((os.path.basename(f),j.get('video_id'),w.get('text'),row[0]))
res['D_files_with_comparisons']=nf;res['D_witness_kinds']=dict(st);res['D_title_mismatch_sample']=bad[:12]
print(json.dumps(res,indent=1,default=str)[:6000])
json.dump(res,open(sys.argv[2],'w'),indent=1,default=str)
