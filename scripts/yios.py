#!/usr/bin/env python3
"""YIOS task checkpoints and cooperative two-Mac coordination. Run python -m scripts.yios."""
from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import uuid

from scripts.yios_coordination import Coordination, CoordinationError, Git, utc
from scripts.yios_workspace import FINANCE, FINANCE_BRANCH, COMPLETE, DIMS, check_safety, finance_counts, sha256, validate_checkpoint, verify_media


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)


class Workflow:
    def __init__(self, repo, machine=None, namespace='yios/claims'):
        self.git = Git(Path(repo))
        root = Path(self.git.run('rev-parse', '--show-toplevel'))
        self.git.repo = root
        if machine is None:
            try:
                machine = self.git.run('config','--get','yios.machine')
            except CoordinationError:
                machine = socket.gethostname()
        self.coordination = Coordination(self.git, machine=machine, namespace=namespace)
        self.local = Path(self.git.run('rev-parse','--path-format=absolute','--git-path','yios'))

    def session(self):
        p = self.local/'session.json'
        if not p.exists():
            raise CoordinationError('No task session in this worktree; use yios start')
        return json.loads(p.read_text())

    def safety(self):
        p = self.local/'safety.json'
        if not p.exists():
            raise CoordinationError('Fresh usage required: yios safety --five-hour N --weekly N --context AVAILABLE_UNMETERED --paid-credits 0')
        return check_safety(json.loads(p.read_text()), self.git.repo)

    def snapshot(self, branch=FINANCE_BRANCH):
        ref = 'refs/heads/' + branch
        sha = self.git.head(ref)
        if not sha:
            raise CoordinationError('Canonical remote branch missing')
        self.git.fetch(ref, sha)
        return sha

    def local_database(self):
        p=self.git.repo/'data/catalog/youtube_channel_registry.db'
        if p.exists():
            with p.open('rb') as f:
                pointer=f.read(100).startswith(b'version https://git-lfs.github.com/spec/v1')
            if pointer:
                # checkout reads the shared local LFS cache only; never fetch/pull.
                self.git.run('lfs','checkout','--','data/catalog/youtube_channel_registry.db')

    def counts(self, sha):
        rows = [json.loads(x) for x in self.git.run('show',f'{sha}:{FINANCE}/VIDEO_AUDIT_966.jsonl').splitlines()]
        universe = list(csv.DictReader(io.StringIO(self.git.run('show',f'{sha}:{FINANCE}/reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv'))))
        return rows, finance_counts(rows, universe)

    def status(self):
        sha = self.snapshot()
        _, counts = self.counts(sha)
        session_path = self.local/'session.json'
        session = json.loads(session_path.read_text()) if session_path.exists() else None
        local_head = self.git.run('rev-parse','HEAD')
        checkpoint = None
        if session:
            remote = self.git.head('refs/heads/' + session['branch'])
            task_git=Git(Path(session.get('worktree',str(self.git.repo))))
            task_head=task_git.run('rev-parse','HEAD')
            checkpoint = {'task':session['task'],'local_head':task_head,'remote_head':remote,
                          'publication':'SYNCED' if task_head == remote and not task_git.run('status','--porcelain') else 'UNSYNCED',
                          'continuation':session.get('continuation')}
        return {'machine':self.coordination.machine,'hostname':socket.gethostname(),
                'branch':self.git.run('rev-parse','--abbrev-ref','HEAD'),'local_head':local_head,
                'finance_remote_head':sha,'finance':counts,'claims':self.coordination.claims(),
                'local_checkpoint':checkpoint,'unpublished_paths':self.git.run('status','--porcelain').splitlines(),
                'worktrees':self.git.run('worktree','list','--porcelain'),
                'protected_snapshot_2026_10_30':{'finance':'LEGACY_MACHINE_B_SOLE_WRITER; MIGRATION_NOT_CERTIFIED',
                             'visual-forensics/5umJ63d3rzQ':'PROTECTED_PARTIAL_CHECKPOINT_6; release/recovery not verified'},
                'visual_snapshot_2026_10_30':{'o3FQcd91MIs':'VISUAL_ONLY_COMPLETE; FULL_AV_BLOCKED',
                                    'Uumnx2Fo6cE':'VISUAL_ONLY_COMPLETE; FULL_AV_BLOCKED',
                                    '5umJ63d3rzQ':'PARTIAL_PROTECTED; reviewer state requires owner checkpoint'},
                'media_recovery':'External frame/audio/source manifests exist; private restore NOT_TESTED. Run yios media manifest.json on destination Mac.'}

    def start(self, stream, video, destination, media_file=None, resume=False):
        self.safety()
        task = stream + '/' + video
        self.coordination.ref(task)
        self.coordination.legacy_gate(task)
        if self.coordination.namespace != 'yios/claims':
            raise CoordinationError('Test namespace is protocol-only; not production research authorization')
        canonical = self.snapshot()
        rows, _ = self.counts(canonical)
        row = next((r for r in rows if r['Video_ID'] == video),None)
        if stream == 'finance' and (not row or all(s in COMPLETE for s in row['statuses'].values())):
            raise CoordinationError('Already accepted or expansion lacks the canonical audit contract')
        if stream == 'visual-forensics' and video in {'o3FQcd91MIs','Uumnx2Fo6cE'}:
            raise CoordinationError('Existing accepted visual scope: use a separately reviewed continuation contract')
        media = json.loads(Path(media_file).read_text()) if media_file else []
        verify_media(media, required=stream == 'visual-forensics', video_id=video)
        old_sha, old = self.coordination.read(task)
        if resume:
            session = self.session()
            if session['task'] != task or old_sha != session['claim_sha'] or old['token'] != session['token']:
                raise CoordinationError('Cannot resume without matching local session and exact remote claim')
            return {'status':'RESUME_EXISTING_SESSION','worktree':str(self.git.repo),'session':session}
        if destination.exists():
            raise CoordinationError('Worktree destination already exists; preserve it')
        prior = old.get('checkpoint') if old else None
        base = prior or canonical
        if prior:
            self.git.fetch('refs/heads/' + old['task_branch'], prior)
        channel = row['Channel_ID'] if row else None
        if stream == 'visual-forensics':
            channels = {r.get('channel_id') for r in media}
            if len(channels) != 1 or None in channels:
                raise CoordinationError('Visual media must declare one canonical channel_id')
            channel = next(iter(channels))
        claim, state = self.coordination.acquire(task, old_sha, channel_id=channel)
        branch = f'yios/tasks/{task}/{state["token"][:12]}'
        session = {'task':task,'token':state['token'],'claim_sha':claim,'branch':branch,
                   'source_base':canonical,'previous_checkpoint':prior,'machine':self.coordination.machine,
                   'worktree':str(destination.resolve()),'publication':'UNSYNCED'}
        write_json(self.local/'session.json',session)
        self.git.run('worktree','add','-b',branch,str(destination.resolve()),base)
        child = Workflow(destination, self.coordination.machine)
        child.local_database()
        write_json(child.local/'session.json',session)
        shutil.copyfile(self.local/'safety.json', child.local/'safety.json')
        cp_path = destination/'research/tasks'/task/'CHECKPOINT.json'
        if prior:
            cp = json.loads(cp_path.read_text())
            for artifact in cp['artifacts']:
                p = destination/artifact['path']
                if not p.is_file() or p.stat().st_size != artifact['bytes'] or sha256(p) != artifact['sha256']:
                    raise CoordinationError('Published checkpoint artifact did not restore; claim retained for recovery')
            cp['source_base'] = canonical
            if media:
                cp['media'] = media
        else:
            fingerprints = json.loads(self.git.run('show',f'{canonical}:{FINANCE}/audit-baseline/MANIFEST.json'))['source_hashes']
            cp = {'task':task,'video_id':video,'channel_id':channel,'status':'IN_PROGRESS',
                  'source_base':canonical,'completed_stages':[],'remaining_stages':['Read existing evidence and define bounded review'],
                  'continuation':'Load existing evidence before new work; retain qualifications.',
                  'source_fingerprints':fingerprints,'artifacts':[],'media':media,'integration_files':[]}
        write_json(cp_path,cp)
        return {'status':'CLAIMED','worktree':str(destination),'branch':branch,'claim_sha':claim,
                'checkpoint_spec':str(cp_path),'resume':prior,'source_base':canonical}

    def save(self, files):
        self.safety()
        session = self.session()
        task = session['task']
        claim, state = self.coordination.read(task)
        if claim != session['claim_sha'] or state.get('token') != session['token'] or state['status'] != 'ACTIVE' or state.get('machine') != self.coordination.machine or state.get('owner') != self.coordination.owner:
            raise CoordinationError('Writer claim no longer matches this session')
        if self.git.run('rev-parse','--abbrev-ref','HEAD') != session['branch']:
            raise CoordinationError('Wrong task branch')
        if self.git.run('diff','--cached','--name-only'):
            raise CoordinationError('Index is not empty; inspect and preserve pre-existing staged work')
        relative = 'research/tasks/' + task + '/CHECKPOINT.json'
        cp = json.loads((self.git.repo/relative).read_text())
        if cp.get('task') != task or cp.get('video_id') != task.split('/')[1] or cp.get('channel_id') != state.get('channel_id'):
            raise CoordinationError('Checkpoint identity differs from exclusively claimed video/channel')
        old_files = [r['path'] for r in cp.get('artifacts',[])]
        intended = list(dict.fromkeys(old_files + files))
        cp = validate_checkpoint(self.git.repo,cp,intended)
        if cp['source_base'] != session['source_base']:
            raise CoordinationError('Checkpoint source_base differs from session')
        allowed = set(intended) | {relative}
        changed = set(self.git.run('diff','--name-only','HEAD').splitlines())
        if changed - allowed:
            raise CoordinationError('Unrelated tracked edits present; checkpoint publication refused')
        cp.update(saved_utc=utc(),previous_published_commit=session.get('published_commit'),
                  reviewer={'owner':self.coordination.owner,'machine':self.coordination.machine})
        write_json(self.git.repo/relative,cp)
        self.git.run('add','--',*sorted(allowed))
        self.git.run('diff','--cached','--check')
        if self.git.run('diff','--cached','--name-only'):
            self.git.run('commit','-m',f'research: checkpoint {task} {cp["status"]}')
        sha = self.git.run('rev-parse','HEAD')
        try:
            remote = self.git.head('refs/heads/' + session['branch'])
            if remote and remote != sha:
                self.git.run('merge-base','--is-ancestor',remote,sha)
            self.git.publish(sha,'refs/heads/' + session['branch'],remote)
            claim, _ = self.coordination.transition(task,claim,session['token'],'ACTIVE',checkpoint=sha,
                task_branch=session['branch'],continuation=cp['continuation'],acceptance=cp['status'],source_base=cp['source_base'])
        except (CoordinationError,OSError) as exc:
            session.update(publication='UNSYNCED',local_commit=sha,error=str(exc))
            write_json(self.local/'session.json',session)
            raise CoordinationError('UNSYNCED: local commit preserved '+sha+'; '+str(exc)) from exc
        session.update(claim_sha=claim,published_commit=sha,publication='REMOTELY_VERIFIED',continuation=cp['continuation'])
        write_json(self.local/'session.json',session)
        return {'publication':'REMOTELY_VERIFIED','checkpoint_commit':sha,'claim_sha':claim,
                'portable_research':'HASH_MANIFEST_PUBLISHED','source_media':'LOCAL_HASH_VERIFIED; other-Mac restore NOT_TESTED' if cp['media'] else 'NO_ORIGINAL_MEDIA_CLAIM',
                'acceptance':'NOT_CANONICALLY_ACCEPTED'}

    def recover(self):
        """Repair only a lost acknowledgement for this exact writer/checkpoint."""
        session=self.session()
        sha,state=self.coordination.read(session['task'])
        head=self.git.run('rev-parse','HEAD')
        if not state or any(state.get(k)!=v for k,v in {'token':session['token'],'owner':self.coordination.owner,'machine':self.coordination.machine,'task_branch':session['branch'],'checkpoint':head}.items()):
            raise CoordinationError('Recovery cannot reconcile exact writer/checkpoint; retain local work')
        if self.git.head('refs/heads/'+session['branch'])!=head or self.git.run('status','--porcelain'):
            raise CoordinationError('Recovery needs a clean, exactly published checkpoint')
        cp=json.loads((self.git.repo/'research/tasks'/session['task']/'CHECKPOINT.json').read_text())
        for artifact in cp['artifacts']:
            if sha256(self.git.repo/artifact['path'])!=artifact['sha256']:
                raise CoordinationError('Recovery artifact mismatch')
        session.update(claim_sha=sha,published_commit=head,continuation=cp['continuation'],
                       publication='RELEASED' if state['status']=='RELEASED' else 'REMOTELY_VERIFIED')
        write_json(self.local/'session.json',session)
        return {'status':'EXACT_STATE_RECOVERED','publication':session['publication'],'claim_sha':sha,'checkpoint':head}

    def switch_to(self, machine):
        self.safety()
        session = self.session()
        if self.git.run('status','--porcelain'):
            raise CoordinationError('Save the complete atomic unit first; local files remain untouched')
        sha = self.git.run('rev-parse','HEAD')
        if session.get('published_commit') != sha or self.git.head('refs/heads/' + session['branch']) != sha:
            raise CoordinationError('UNSYNCED: publish and verify exact checkpoint before release')
        claim,state = self.coordination.read(session['task'])
        if claim != session['claim_sha'] or state.get('checkpoint') != sha:
            raise CoordinationError('Stale handoff state')
        released,_ = self.coordination.transition(session['task'],claim,session['token'],'RELEASED',
                                                   transfer_to=machine,continuation=session['continuation'])
        session.update(claim_sha=released,publication='RELEASED',transfer_to=machine)
        write_json(self.local/'session.json',session)
        return {'status':'RELEASED_REMOTELY_VERIFIED','task':session['task'],'checkpoint':sha,
                'target_machine':machine,'release_sha':released,'receiving_command':f'yios start {session["task"].replace("/"," ")} --worktree NEW_PATH'}


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path.cwd())
    p.add_argument('--machine',help='machine-a / machine-b (or git config yios.machine)')
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('status')
    sub.add_parser('recover')
    setup=sub.add_parser('setup'); setup.add_argument('identity',choices=['machine-a','machine-b'])
    safety=sub.add_parser('safety'); safety.add_argument('--five-hour',type=float,required=True); safety.add_argument('--weekly',type=float,required=True)
    safety.add_argument('--context',choices=['AVAILABLE','AVAILABLE_UNMETERED','EXHAUSTED'],required=True)
    safety.add_argument('--paid-credits',type=float,required=True)
    start=sub.add_parser('start'); start.add_argument('stream',choices=['finance','visual-forensics']); start.add_argument('video')
    start.add_argument('--worktree',type=Path,required=True); start.add_argument('--media-manifest'); start.add_argument('--resume',action='store_true')
    save=sub.add_parser('save'); save.add_argument('--files',nargs='*',default=[])
    switch=sub.add_parser('switch-to'); switch.add_argument('machine',choices=['machine-a','machine-b'])
    release=sub.add_parser('release'); release.add_argument('--to',choices=['machine-a','machine-b'])
    media=sub.add_parser('media'); media.add_argument('manifest',type=Path); media.add_argument('--required',action='store_true')
    integrate=sub.add_parser('integrate'); integrate.add_argument('stream',choices=['finance','visual-forensics'])
    integrate.add_argument('--task',action='append',required=True); integrate.add_argument('--expected-head',required=True)
    integrate.add_argument('--worktree',type=Path,required=True); integrate.add_argument('--node',default='node')
    recovery=sub.add_parser('integrate-recover'); recovery.add_argument('operation')
    recovery.add_argument('--preserve-and-release',action='store_true')
    return p


def integrate(w, args):
    """Publish one validated canonical transaction; keep failed worktrees/claims."""
    from scripts.yios_integration import FINANCE as FINANCE_PATH, IntegrationError, prepare_finance, prepare_visual
    w.safety()
    stream = args.stream
    coordinator = 'integration/' + stream
    w.coordination.legacy_gate(coordinator)
    branch = FINANCE_BRANCH if stream == 'finance' else 'research/casually-finance-editing-forensics'
    canonical = w.snapshot(branch)
    if canonical != args.expected_head:
        raise CoordinationError('Stale canonical head; no import or publication performed')
    if len(args.task) != len(set(args.task)) or any(not t.startswith(stream+'/') for t in args.task):
        raise CoordinationError('Integration requires unique same-stream task identities')
    if args.worktree.exists():
        raise CoordinationError('Integration worktree already exists; preserve failed/unpublished state')
    packets = []
    for task in args.task:
        sha, state = w.coordination.read(task)
        if not state or state['status'] != 'RELEASED' or state.get('acceptance') != 'READY_FOR_INTEGRATION' or not state.get('checkpoint'):
            raise CoordinationError('Research must publish and explicitly release READY_FOR_INTEGRATION: '+task)
        w.git.fetch('refs/heads/'+state['task_branch'],state['checkpoint'])
        prefix = 'research/tasks/'+task+'/'
        cp = json.loads(w.git.run('show',state['checkpoint']+':'+prefix+'CHECKPOINT.json'))
        if cp.get('task') != task or cp.get('status') != 'READY_FOR_INTEGRATION' or cp.get('remaining_stages'):
            raise CoordinationError('Checkpoint/remote readiness does not reconcile')
        w.git.run('merge-base','--is-ancestor',cp['source_base'],canonical)
        if stream == 'finance':
            rows,_ = w.counts(canonical)
            prior_rows,_ = w.counts(cp['source_base'])
            video=task.split('/')[1]
            current=next((r for r in rows if r['Video_ID']==video),None)
            prior=next((r for r in prior_rows if r['Video_ID']==video),None)
            fingerprints=json.loads(w.git.run('show',f'{canonical}:{FINANCE}/audit-baseline/MANIFEST.json'))['source_hashes']
            if current is None or current != prior or all(v in COMPLETE for v in current['statuses'].values()) or cp['source_fingerprints'] != fingerprints:
                raise CoordinationError('Target already changed/accepted or source version mismatch: '+task)
        artifact_map={a['path']:a for a in cp['artifacts']}
        files={}
        for mapping in cp.get('integration_files',[]):
            source,destination=mapping['source'],mapping['destination']
            if source not in artifact_map or not source.startswith(prefix) or '..' in Path(source).parts:
                raise CoordinationError('Unmanifested integration artifact')
            # Binary-safe extraction, never a shell interpolation.
            result=subprocess.run(['git','-C',str(w.git.repo),'show',state['checkpoint']+':'+source],capture_output=True,
                                  env={**__import__('os').environ,'GIT_NO_LAZY_FETCH':'1'},timeout=30)
            data=result.stdout
            import hashlib
            a=artifact_map[source]
            if result.returncode or len(data)!=a['bytes'] or hashlib.sha256(data).hexdigest()!=a['sha256']:
                raise CoordinationError('Published artifact hash mismatch')
            if destination in files:
                raise CoordinationError('Duplicate integration destination')
            files[destination]=data
        if not files:
            raise CoordinationError('No explicit integration_files mapping')
        packets.append((task,sha,state,cp,files))
    old, _ = w.coordination.read(coordinator)
    claim, coord = w.coordination.acquire(coordinator,old,stage='canonical-publication')
    operation=uuid.uuid4().hex
    integration_branch='yios/integration/'+stream+'/'+operation
    recovery={'coordinator':coordinator,'claim_sha':claim,'token':coord['token'],'canonical_base':canonical,
              'branch':integration_branch,'canonical_branch':branch,'worktree':str(args.worktree.resolve()),'status':'IN_PROGRESS',
              'tasks':[{'task':t,'claim':sh,'checkpoint':s['checkpoint']} for t,sh,s,_,_ in packets]}
    write_json(w.local/('integration-'+operation+'.json'),recovery)
    # A failed integration intentionally retains its exclusive claim and isolated
    # worktree. Never release or delete unpublished artifacts in a finally block.
    w.git.run('worktree','add','-b',integration_branch,str(args.worktree.resolve()),canonical)
    stage=Git(args.worktree)
    Workflow(args.worktree,w.coordination.machine).local_database()
    baseline=Path(tempfile.mkdtemp(prefix='yios-integration-baseline-'))
    imported=[]
    if stream=='finance':
        shutil.copytree(args.worktree/FINANCE_PATH,baseline/'finance')
    try:
        for task,sha,state,cp,files in packets:
            if stream=='finance':
                for name,data in files.items():
                    p=Path(name)
                    prefix=Path(FINANCE)/'audit-batches'
                    if p.parent != prefix or p.suffix.lower() not in {'.json','.jpg','.png','.jpeg','.webp'} or len(data)>5*1024**2:
                        raise CoordinationError('Finance import outside bounded audit-batches artifacts')
                    dest=args.worktree/p
                    if dest.exists() or dest.is_symlink():
                        raise CoordinationError('Existing packet collision; do not overwrite: '+name)
                    dest.write_bytes(data); imported.append(name)
            else:
                imported += prepare_visual(args.worktree,files,task.split('/')[1],cp['channel_id'])
        if stream=='finance':
            receipt=prepare_finance(args.worktree,baseline/'finance',{t.split('/')[1] for t in args.task},node=args.node)
            outputs=receipt['canonical_outputs']
        else:
            # Each video must provide a reviewed scoped acceptance record. The
            # adapter only adds new records and cannot certify human listening.
            for task,_,_,cp,_ in packets:
                record=args.worktree/'research/visual-forensics/channels'/cp['channel_id']/task.split('/')[1]/'ACCEPTANCE.json'
                accepted=json.loads(record.read_text())
                if accepted.get('video_id')!=task.split('/')[1] or accepted.get('scope')!='VISUAL_ONLY' or not accepted.get('limitations') or not accepted.get('reviewers'):
                    raise CoordinationError('Reviewed VISUAL_ONLY acceptance with explicit limitations required')
            receipt={'validation':'PASS_BOUNDED_NEW_VISUAL_RECORDS','native_av_certification':'NOT_CLAIMED'}
            outputs=[]
        receipt.update(operation=operation,canonical_base=canonical,tasks=[{'task':t,'checkpoint':s['checkpoint'],'claim':sh} for t,sh,s,_,_ in packets],
                       ownership='EXCLUSIVE_COORDINATOR',created_utc=utc())
        receipt_path='research/coordination/integrations/'+operation+'.json'
        write_json(args.worktree/receipt_path,receipt)
        allowed=set(imported+outputs+[receipt_path])
        changed=set(stage.run('diff','--name-only','HEAD').splitlines())
        untracked=set(stage.run('ls-files','--others','--exclude-standard').splitlines())
        if (changed|untracked)-allowed:
            raise CoordinationError('Unexpected integration changes: '+str(sorted((changed|untracked)-allowed)))
        stage.run('add','--',*sorted(allowed))
        stage.run('diff','--cached','--check')
        if w.git.head('refs/heads/'+branch)!=canonical or w.coordination.read(coordinator)[0]!=claim:
            raise CoordinationError('Canonical/coordinator moved before commit')
        for task,sha,_,_,_ in packets:
            if w.coordination.read(task)[0]!=sha:
                raise CoordinationError('Task state changed before integration')
        stage.run('commit','-m','research: integrate '+', '.join(args.task))
        head=stage.run('rev-parse','HEAD')
        recovery.update(local_commit=head,status='UNSYNCED'); write_json(w.local/('integration-'+operation+'.json'),recovery)
        stage.publish(head,'refs/heads/'+branch,canonical)
        if stream=='finance':
            pr=subprocess.run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/pulls/36'],capture_output=True,text=True,timeout=30)
            data=json.loads(pr.stdout) if pr.returncode==0 else {}
            if data.get('head',{}).get('sha')!=head or data.get('state')!='open' or data.get('merged') or not data.get('draft'):
                raise CoordinationError('Canonical pushed; PR36 verification incomplete. Retain coordinator for reconciliation.')
        for task,sha,_,_,_ in packets:
            w.coordination.reconcile(task,sha,claim,coord['token'],head)
        release,_=w.coordination.transition(coordinator,claim,coord['token'],'RELEASED',checkpoint=head,task_branch=branch,acceptance='ACCEPTED',continuation='Recompute live ledger; select next released ready packet')
        recovery.update(status='REMOTELY_VERIFIED',published_commit=head,release_sha=release)
        write_json(w.local/('integration-'+operation+'.json'),recovery)
        return {**recovery,'validation':receipt,'finance':w.counts(head)[1] if stream=='finance' else None}
    except (CoordinationError,IntegrationError,OSError,KeyError,ValueError) as exc:
        recovery.update(status='BLOCKED_PRESERVED',error=str(exc),baseline=str(baseline))
        write_json(w.local/('integration-'+operation+'.json'),recovery)
        raise CoordinationError('Integration blocked; claim/worktree/baseline retained: '+str(exc)) from exc


def recover_integration(w, args):
    """Explicit recovery, never an inferred release from elapsed time or idleness."""
    w.safety()
    if not __import__('re').fullmatch('[a-f0-9]{32}',args.operation):
        raise CoordinationError('Invalid integration operation ID')
    record=w.local/('integration-'+args.operation+'.json')
    r=json.loads(record.read_text())
    claim,state=w.coordination.read(r['coordinator'])
    if not state or state['token']!=r['token'] or state['machine']!=w.coordination.machine or state['owner']!=w.coordination.owner:
        raise CoordinationError('Recovery requires the exact retained coordinator identity')
    live=w.git.head('refs/heads/'+r['canonical_branch'])
    published=r.get('local_commit') and live==r['local_commit']
    if state['status']=='RELEASED' and published and state.get('checkpoint')==live:
        r.update(status='REMOTELY_VERIFIED',published_commit=live,release_sha=claim)
        write_json(record,r); return r
    if claim!=r['claim_sha'] or state['status']!='ACTIVE':
        raise CoordinationError('Coordinator state changed; exact recovery refused')
    if published:
        if r['canonical_branch']==FINANCE_BRANCH:
            pr=subprocess.run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/pulls/36'],capture_output=True,text=True,timeout=30)
            data=json.loads(pr.stdout) if pr.returncode==0 else {}
            if data.get('head',{}).get('sha')!=live or data.get('state')!='open' or data.get('merged') or not data.get('draft'):
                raise CoordinationError('Published canonical commit still lacks exact OPEN/DRAFT PR36 verification')
        for task in r['tasks']:
            ts,record_state=w.coordination.read(task['task'])
            if record_state.get('acceptance')=='ACCEPTED' and record_state.get('canonical_commit')==live:
                continue
            w.coordination.reconcile(task['task'],task['claim'],claim,r['token'],live)
        released,_=w.coordination.transition(r['coordinator'],claim,r['token'],'RELEASED',checkpoint=live,
                       task_branch=r['canonical_branch'],acceptance='ACCEPTED',continuation='Canonical integration reconciled')
        r.update(status='REMOTELY_VERIFIED',published_commit=live,release_sha=released)
    elif live==r['canonical_base'] and args.preserve_and_release:
        # Packet branches are already remotely verified. All failed generated
        # outputs remain at the recorded path; nothing is reset or deleted.
        if not Path(r['worktree']).is_dir():
            raise CoordinationError('Preserved worktree unavailable; inspect manually before release')
        if w.git.head('refs/heads/'+r['canonical_branch'])!=live:
            raise CoordinationError('Canonical changed during recovery')
        released,_=w.coordination.transition(r['coordinator'],claim,r['token'],'RELEASED',checkpoint=None,
                     acceptance='BLOCKED_PRESERVED',continuation='Failed outputs retained at '+r['worktree']+'; retry fresh isolated integration')
        r.update(status='RELEASED_WITH_LOCAL_FAILURE_PRESERVED',release_sha=released,
                 warning='Uncommitted/generated outputs are LOCAL_ONLY; verified input packets remain published')
    else:
        raise CoordinationError('Canonical differs or release not requested; retain claim/worktree for review')
    write_json(record,r)
    return r


def main(argv=None):
    args=parser().parse_args(argv)
    try:
        w=Workflow(args.repo,args.machine)
        if args.command=='setup':
            w.git.run('config','--local','yios.machine',args.identity)
            result={'machine':args.identity,'hostname':socket.gethostname(),'production_readiness':'NOT_CERTIFIED'}
        elif args.command=='safety':
            record={'checked_utc':utc(),'five_hour':args.five_hour,'weekly':args.weekly,'context_reserve':args.context,'paid_credits':args.paid_credits,'source':'OPERATOR_CURRENT_METER_READING'}
            result=check_safety(record,w.git.repo); write_json(w.local/'safety.json',record)
        elif args.command=='status': result=w.status()
        elif args.command=='media': result=verify_media(json.loads(args.manifest.read_text()),args.required)
        elif args.command=='start': result=w.start(args.stream,args.video,args.worktree,args.media_manifest,args.resume)
        elif args.command=='save': result=w.save(args.files)
        elif args.command=='recover': result=w.recover()
        elif args.command in {'switch-to','release'}: result=w.switch_to(args.machine if args.command=='switch-to' else args.to)
        elif args.command=='integrate': result=integrate(w,args)
        elif args.command=='integrate-recover': result=recover_integration(w,args)
        print(json.dumps(result,indent=2,ensure_ascii=False))
        return 0
    except (CoordinationError,ValueError,OSError,KeyError) as exc:
        print(json.dumps({'status':'BLOCKED','reason':str(exc),'preservation':'No reset, cleanup or automatic ownership takeover performed'}),file=sys.stderr)
        return 2


if __name__=='__main__':
    sys.exit(main())
