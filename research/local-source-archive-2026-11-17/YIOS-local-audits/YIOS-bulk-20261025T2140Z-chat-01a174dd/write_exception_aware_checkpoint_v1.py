"""Append-only operational receipts; legacy selected totals and physical bytes stay distinct."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, shutil
R=Path(__file__).parent
def read(p): return json.loads(Path(p).read_text())
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    with Path(p).open('x') as f: json.dump(v,f,indent=2)
    Path(p).chmod(0o400)
def accounting():
    state=read_json_output(['python3',str(R/'continue_backup.py'),'state','{}'])
    assert state['uploaded_bytes_including_controls']==state['verified_bytes_including_controls']
    extra=0
    for p in R.glob('batch-*/EXCEPTION_APPROVAL.json'):
        x=read(p); assert x['status']=='OWNER_APPROVED_LIMITED_UNATTRIBUTED_VERIFIED_DUPLICATE'
        extra+=x['extra_physical_bytes']
    done={x['source'] for x in read(R/'recovery-20261026-machine-b-handoff/SOURCE_TO_DRIVE_INVENTORY.json')['files']}
    for p in R.glob('batch-*/RECEIPT.json'):
        if int(p.parent.name.split('-')[1])>=10: done.update(x['source_absolute'] for x in read(p)['files'])
    plan=max(R.glob('ORDERED_PLAN_V*.json'),key=lambda p:int(p.stem.rsplit('_V',1)[1]))
    pending=[x for x in read(plan)['files'] if x['source_absolute'] not in done]
    return dict(state,physical_remote_verified_bytes_including_duplicate=state['verified_bytes_including_controls']+extra,
        extra_physical_bytes=extra,extra_unique_source_coverage=0,remaining_genuinely_unuploaded_objects=len(pending),
        remaining_genuinely_unuploaded_payload_bytes=sum(x['bytes'] for x in pending),next_sequence=pending[0]['sequence'] if pending else None,
        plan=str(plan),plan_sha256=digest(plan),next_ordered_sources=pending[:3])
def read_json_output(cmd): return json.loads(subprocess.check_output(cmd,text=True))
mode=sys.argv[1]; a=json.loads(sys.argv[2]); now=datetime.datetime.now(datetime.timezone.utc)
if mode=='handoff':
    n=a['batch']; b=R/f'batch-{n:04d}'; receipt=read(b/'RECEIPT.json'); assert receipt['status']=='VERIFIED'
    ac=accounting(); assert ac['physical_remote_verified_bytes_including_duplicate']<12000000000
    stamp=now.strftime('%Y%m%dT%H%M%SZ'); d=R/('checkpoint-'+stamp); d.mkdir(mode=0o700)
    ex=read(R/'batch-0031/EXCEPTION_APPROVAL.json')
    report={'batch_receipt':receipt,'recovery_mapping':read(b/'RECOVERY_MAPPING.json'),'accounting_before_this_control':ac,
        'batch31_exception_approval':ex,'batch31_receipt_sha256':digest(R/'batch-0031/RECEIPT.json'),
        'attribution':'Owner account actor established; exact client/session/duplication mechanism UNRESOLVED. Both copies preserved unchanged; zero extra source coverage.',
        'scope':'File-level cloud recovery; no independent-machine disaster recovery claim. All historical BLOCKED receipts preserved.'}
    p=d/f'YIOS_BATCH_{n:04d}_VERIFIED_EXCEPTION_AWARE_{stamp}.md'
    text='# YIOS verified recovery checkpoint\n\nBatch31 CLOSED_WITH_APPROVED_EXCEPTION_UNATTRIBUTED_DUPLICATE. Only the specific duplicate exception is accepted; all future gates remain mandatory.\n\nPhysical verified bytes before this document: '+str(ac['physical_remote_verified_bytes_including_duplicate'])+'. Selected and prior confirmed/verified transfer bytes including controls: '+str(ac['verified_bytes_including_controls'])+'. Difference404830 is redundant physical storage, zero additional unique coverage. This document is counted separately after independent full retrieval.\n\n```json\n'+json.dumps(report,indent=2)+'\n```\n'
    with p.open('x') as f:f.write(text)
    p.chmod(0o400)
    print(json.dumps(dict(checkpoint_dir=str(d),handoff_path=str(p),handoff_bytes=p.stat().st_size,handoff_sha256=digest(p))))
elif mode=='checkpoint':
    d=Path(a['control']['checkpoint_dir']); assert d.parent==R
    prev=max(R.glob('checkpoint-*/CONTINUATION.json')); v=read(prev); ac=accounting(); gate=a['gate']
    assert ac['physical_remote_verified_bytes_including_duplicate']<=12000000000 and gate['conservative_free_bytes']>=2000000000
    v.update(ac);v.update(utc=now.isoformat(),status='VERIFIED_WITH_SPECIFIC_BATCH31_APPROVED_EXCEPTION',
        latest_verified_batch=a['batch'],last_fully_verified_atomic_batch=a['batch'],unfinished_batch=None,
        confirmed_uploaded_bytes_including_controls=ac['uploaded_bytes_including_controls'],
        verified_selected_and_prior_bytes_including_controls=ac['verified_bytes_including_controls'],
        latest_compact_receipt=a['control'],gate=gate,mac_free_bytes=shutil.disk_usage(R).free,
        next_action='Fresh normal gates then next ordered source. Always add404830 to legacy helper selected/confirmed totals for physical accounting. Do not reupload4014-4016. Stop any unexplained object. Specific duplicate remains permanently unattributed.',
        previous_immutable_checkpoint=str(prev.parent),transfers_resumed=True,automation=a.get('automation',{'status':'PAUSED_DURING_EXCLUSIVE_OPERATOR_TURN'}))
    save(d/'CONTINUATION.json',v)
    with (d/'SHA256SUMS').open('x') as f:
        for p in sorted(d.iterdir()):
            if p.is_file() and p.name!='SHA256SUMS': f.write(digest(p)+'  '+p.name+'\n')
    (d/'SHA256SUMS').chmod(0o400)
    for l in (d/'SHA256SUMS').read_text().splitlines():
        h,n=l.split('  ',1);assert digest(d/n)==h
    print(json.dumps({k:v[k] for k in ['latest_verified_batch','confirmed_uploaded_bytes_including_controls','physical_remote_verified_bytes_including_duplicate','remaining_genuinely_unuploaded_objects','remaining_genuinely_unuploaded_payload_bytes','next_sequence']}))
