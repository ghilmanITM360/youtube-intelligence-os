import json,pathlib,subprocess,concurrent.futures
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21'); repo='ghilmanITM360/youtube-intelligence-os'
def api(p):
 x=subprocess.run(['gh','api',p],capture_output=True,text=True)
 return json.loads(x.stdout) if x.returncode==0 else {'error':x.stderr}
def one(pr):
 sha=pr['headRefOid'];checks=api(f'repos/{repo}/commits/{sha}/check-runs?per_page=100');runs=api(f'repos/{repo}/actions/runs?head_sha={sha}&per_page=100')
 out=dict(pr=pr,checks=checks,runs=runs)
 out['jobs']=[dict(run_id=r['id'],response=api(f'repos/{repo}/actions/runs/{r["id"]}/jobs?per_page=100')) for r in runs.get('workflow_runs',[])]
 (A/f'pr-{pr["number"]}-checks.json').write_text(json.dumps(out,indent=2))
 jobs=[j for r in out['jobs'] for j in r['response'].get('jobs',[])];steps=sum(len(j.get('steps',[])) for j in jobs)
 summary=dict(number=pr['number'],sha=sha,checks=[dict(name=c['name'],status=c['status'],conclusion=c['conclusion'],output=c.get('output')) for c in checks.get('check_runs',[])],runs=len(runs.get('workflow_runs',[])),jobs=len(jobs),steps=steps,executed_steps=sum(s.get('started_at') is not None for j in jobs for s in j.get('steps',[])))
 return summary
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(one,json.loads((A/'prs.json').read_text())))
(A/'ci-summary.json').write_text(json.dumps(rows,indent=2))
for r in rows:print(r['number'],r['sha'],[(c['name'],c['conclusion'])for c in r['checks']],r['runs'],r['jobs'],r['executed_steps'])
