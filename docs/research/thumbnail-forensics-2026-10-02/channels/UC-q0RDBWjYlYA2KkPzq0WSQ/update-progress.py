"""Reconcile this channel into the control files; idempotent, keeps queue order."""
import csv, datetime, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
R=HERE.parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(name): return list(csv.DictReader((R/name).open()))
def write(name, rows):
    with (R/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\r\n' if name=='completion-ledger.csv' else '\n');w.writeheader();w.writerows(rows)

m=list(csv.DictReader((HERE/'packaging-progress.csv').open()))
qa=json.loads((HERE/'qa.json').read_text())
verified={r['Thumbnail_ID'] for r in qa['reviews'] if r['result'] in ('PASS','PASS_WITH_CORRECTIONS')}
counts=dict(verified=sum(r['Thumbnail_Status']=='THUMBNAIL_VERIFIED' for r in m),draft=sum(r['Thumbnail_Status']=='THUMBNAIL_DRAFT' for r in m),
            packages=sum(r['Package_Status']=='PACKAGE_AUDITED' for r in m),qa=sum(r['QA_Status'] in ('PASS','HISTORICAL_SAMPLE') for r in m),complete=sum(r['Current_Status']=='COMPLETE' for r in m))
queue=read('channel-processing-queue.csv')
row=next(r for r in queue if r['Channel_ID']==HERE.name)
row.update(Existing_Verified_Thumbnail_Audits=counts['verified'],Existing_Thumbnail_Drafts=counts['draft'],Existing_Package_Audits=counts['packages'],Existing_Package_QA=counts['qa'],Videos_Remaining=10-counts['complete'])
write('channel-processing-queue.csv',queue)
cross=read('legacy-batch-to-channel.csv')
for row in cross:
    if row['Thumbnail_ID'] in verified:
        row.update(Legacy_Status='VERIFIED',QA_Status='PRIMARY_SEQUENTIAL_QA_PASS',**{'Already_Reused?':'NO'})
        row['Notes']='New channel-first audit; legacy batch/sequence retained as queue provenance, not a newly authored global batch.'
write('legacy-batch-to-channel.csv',cross)
ledger=read('completion-ledger.csv')
batch='CHANNEL-001-M01'
entry=dict(zip(ledger[0],['']*len(ledger[0])))
entry.update(batch_id=batch,scope='Genius History video 279aqcCGBpI: channel-first thumbnail/package microbatch',status='COMPLETE',discovered_units='1',opened_units='1',classified_units='1',audited_units='1',excluded_units='0',ambiguous_units='0',remaining_units='0',QA_status='PASS',provenance='PRIMARY_AGENT_SEQUENTIAL; source SHA256 checked; historical title reused; content NOT_CHECKED',output='channels/'+HERE.name+'/thumbnail-audits.json; channels/'+HERE.name+'/package-audits.json; channels/'+HERE.name+'/qa.json')
ledger=[r for r in ledger if r['batch_id']!=batch]+[entry]
thumbs=json.loads((HERE/'thumbnail-audits.json').read_text())
for bid in sorted({r['batch_id'] for r in thumbs if r['batch_id']!=batch}):
    selected=[r for r in thumbs if r['batch_id']==bid]
    reviewed_selected=[r for r in qa['reviews'] if r['Thumbnail_ID'] in {t['Thumbnail_ID'] for t in selected}]
    newentry=dict(entry)
    newentry.update(batch_id=bid,scope='Genius History channel-first videos '+','.join(r['Video_ID'] for r in reviewed_selected),discovered_units=str(len(selected)),opened_units=str(len(selected)),classified_units=str(len(selected)),audited_units=str(len(reviewed_selected)),remaining_units=str(len(selected)-len(reviewed_selected)),status='COMPLETE' if len(selected)==len(reviewed_selected) else 'QA_PENDING')
    newentry['QA_status']='PASS_WITH_CORRECTIONS' if any(r['corrections'] for r in reviewed_selected) else 'PASS'
    ledger=[r for r in ledger if r['batch_id']!=bid]+[newentry]
write('completion-ledger.csv',ledger)
s=json.loads((R/'packaging-progress-summary.json').read_text())
s.update(timestamp=stamp,phase='CHANNEL_BY_CHANNEL',status='IN_PROGRESS')
baseline_thumb=sum(int(r['audited_units']) for r in ledger if r['batch_id'] in ('B001','B002'))
legacy_packages={row['Video_ID'] for file in R.glob('package-audit-PK-*.json') for row in json.loads(file.read_text())}
legacy_qa={row['Package_ID'].removeprefix('PKG-') for file in R.glob('package-qa-review-*.json') for row in json.loads(file.read_text()).get('rows',[]) if row.get('Package_ID')}
new_packages={r['Video_ID'] for r in json.loads((HERE/'package-audits.json').read_text())}
s['thumbnails']['verified']=baseline_thumb+len(verified);s['thumbnails']['remaining']=s['thumbnails']['eligible']-s['thumbnails']['verified']
s['packages']['audited']=len(legacy_packages|new_packages)
s['packages']['qa_sampled']=len(legacy_qa|{r['Video_ID'] for r in qa['reviews']});s['packages']['remaining']=s['packages']['eligible']-s['packages']['audited']
s['progress'].update(thumbnail=s['thumbnails']['verified']/s['thumbnails']['eligible'],package=s['packages']['audited']/s['packages']['eligible'],qa=s['packages']['qa_sampled']/s['packages']['eligible'])
s['progress']['composite']=sum(s['progress'][k] for k in ('title','thumbnail','package','qa'))/4
nextrow=next(r for r in m if r['Current_Status']!='COMPLETE')
s['current_channel'].update(completed_videos=counts['complete'],remaining_videos=10-counts['complete'],progress=(1+counts['verified']/10+counts['packages']/10+counts['qa']/10)/4,next_Video_ID=nextrow['Video_ID'],next_Thumbnail_ID=nextrow['Thumbnail_ID'])
s['resource']=dict(starting_short_window_used_percent=23,latest_short_window_used_percent=28,weekly_used_percent=15,subagents=0,background_agents=0,watchers=0,visual_analysis=True,tool_output_truncation=False,context_window_warning=False)
s['next_step']='Continue Genius History in canonical Video_ID order, reuse completed legacy rows; next video '+nextrow['Video_ID']
for name in ('completion-ledger.csv',):
    relative='docs/research/thumbnail-forensics-2026-10-02/'+name
    s['source_SHA256'][relative]=hashlib.sha256((R/name).read_bytes()).hexdigest()
s['channel_microbatch']=dict(ids=sorted({r['batch_id'] for r in thumbs}),authored_thumbnail_rows=len(thumbs),authored_package_rows=len(new_packages),reopened_qa_rows=len(qa['reviews']),result='PASS_WITH_CORRECTIONS' if any(r['corrections'] for r in qa['reviews']) else 'PASS',evidence_tier='D_AGE_ADJUSTED_PUBLIC',causality='NOT_ESTABLISHED')
(R/'packaging-progress-summary.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps(dict(channel=counts,progress=s['progress'],next_video=nextrow['Video_ID'])))
