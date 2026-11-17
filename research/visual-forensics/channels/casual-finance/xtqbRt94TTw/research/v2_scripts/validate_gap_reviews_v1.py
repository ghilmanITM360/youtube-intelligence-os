import pathlib,json,csv,sys,hashlib
R=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
def validate(path,batch):
 expected=json.loads((R/f'agents/gap_review_{batch:02}/items.json').read_text());o=json.loads(path.read_text());assert [x['id'] for x in o['items']]==[x['id'] for x in expected],'ID coverage/order'
 for x,e in zip(o['items'],expected):
  assert int(x['start'])==int(e['start']) and int(x['end'])==int(e['end']),'range changed'
  cursor=int(e['start'])
  for s in x['segments']:
   assert int(s['start'])==cursor and int(s['end'])>=cursor,(x['id'],'gap/overlap',s)
   assert s['owner'] in ('PREVIOUS','FOLLOWING','NEW','UNRESOLVED'),s
   assert s['boundary_precision'] in ('EXACT_NATIVE','SAMPLED_BRACKET','UNVERIFIED'),s
   assert s['description'].strip() and s['evidence_frames'],s
   cursor=int(s['end'])+1
  assert cursor==int(e['end'])+1,(x['id'],'incomplete')
 required={q for e in expected for q in e['sheets']};success={x['path'] for x in o['evidence_reads'] if x.get('successful')}
 assert required<=success,('unread sheets',required-success)
 for r in o['evidence_reads']:
  p=pathlib.Path(r['path']);p=p if p.is_absolute() else R/p
  assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],r['path']
  assert r['witness'].strip() and r['scale'] in ('SCALED_480x270','NATIVE_1920x1080'),r
 return o
if __name__=='__main__':
 for n in map(int,sys.argv[1:]):
  p=R/f'agents/gap_review_{n:02}/OUT_gap_review_{n:02}.json';d=validate(p,n);print(n,'PASS',len(d['items']),'gaps',sum(len(x['segments']) for x in d['items']),'segments',len(d['evidence_reads']),'reads')
