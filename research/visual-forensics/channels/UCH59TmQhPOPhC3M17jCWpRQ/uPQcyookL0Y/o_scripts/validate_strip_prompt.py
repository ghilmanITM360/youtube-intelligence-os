import csv,sys,hashlib,json
from pathlib import Path
rv,batches,i0,i1=sys.argv[1],sys.argv[2].split(','),int(sys.argv[3]),int(sys.argv[4]);d=Path(f'agents/{rv}');R=lambda f:list(csv.DictReader(open(f)))
strips={r['strip_png'] for b in batches for r in R(f'tables/o_motion_peaks_{b}.csv')};reads=R(d/'evidence_reads.csv');paths={r['path'] for r in reads};err=[]
err+=['NOT_READ '+s for s in sorted(strips-paths)]
err+=['HASH '+r['path'] for r in reads if not Path(r['path']).exists() or hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()!=r['sha256']]
mo=R(d/'motion_events.csv');err+=['MOTION_MISSING '+s for s in sorted(strips-{r['strip_path'] for r in mo})]
S=[r['state_v4'] for r in R('tables/states_v6_draft.csv')][i0:i1];pr=R(d/'state_prompts.csv')
if [r['state'] for r in pr]!=S:err.append('PROMPT_COVERAGE')
for r in pr:
    for q in filter(None,(x.strip() for x in r['observed_basis_paths'].split(';'))):
        if not Path(q.split(' ')[0]).exists():err.append(f'BASIS_MISSING {r["state"]} {q}')
out={'reviewer':rv,'reads':len(reads),'strips':len(strips),'motion_rows':len(mo),'prompt_rows':len(pr),'errors':err};Path(f'tables/o_validation_{rv}.json').write_text(json.dumps(out,indent=1));print(out)
