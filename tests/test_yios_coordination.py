"""Two independent Git clients; no fake production audits or network required."""
import concurrent.futures
import json
import subprocess
import threading
from pathlib import Path

import pytest

from scripts.yios_coordination import Coordination, CoordinationError, Git


def git(path, *args):
    return subprocess.check_output(['git', '-C', str(path), *args], stderr=subprocess.STDOUT, text=True).strip()


@pytest.fixture
def clients(tmp_path):
    remote = tmp_path / 'remote.git'
    subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
    result = []
    for name in ('machine-a', 'machine-b'):
        p = tmp_path / name
        subprocess.run(['git', 'init', str(p)], check=True, capture_output=True)
        git(p, 'config', 'user.name', name)
        git(p, 'config', 'user.email', name + '@example.invalid')
        git(p, 'remote', 'add', 'origin', str(remote))
        result.append(Coordination(Git(p), namespace='yios-test/claims', machine=name, owner=name))
    return result


def test_simultaneous_clients_exactly_one_writer_and_independent_video(clients):
    a, b = clients
    gate = threading.Barrier(2)
    def claim(c):
        gate.wait()
        try:
            return c.acquire('finance/TEST0000001', expected=None)
        except CoordinationError:
            return None
    with concurrent.futures.ThreadPoolExecutor(2) as pool:
        results = list(pool.map(claim, [a, b]))
    assert sum(x is not None for x in results) == 1
    winner = next(x for x in results if x is not None)
    assert a.read('finance/TEST0000001')[0] == winner[0]
    assert b.acquire('finance/TEST0000002', expected=None)[1]['machine'] == 'machine-b'


def test_release_reacquire_no_aba_and_wrong_owner_fails(clients):
    a, b = clients
    task = 'visual-forensics/TEST0000001'
    sha, state = a.acquire(task, expected=None)
    with pytest.raises(CoordinationError):
        b.transition(task, sha, state['token'], 'RELEASED', checkpoint=None)
    released, _ = a.transition(task, sha, state['token'], 'RELEASED', checkpoint=None, transfer_to='machine-b')
    with pytest.raises(CoordinationError):
        a.acquire(task, expected=released)
    second, new = b.acquire(task, expected=released)
    assert new['token'] != state['token']
    assert git(b.git.repo, 'rev-parse', second + '^') == released
    with pytest.raises(CoordinationError):
        a.transition(task, sha, state['token'], 'RELEASED')
    with pytest.raises(CoordinationError):
        a.acquire(task, expected=None)


def test_concurrent_transitions_from_same_parent_reject_stale_update(clients):
    a, b = clients
    task = 'finance/TEST0000001'
    sha, state = a.acquire(task, expected=None)
    new, _ = a.transition(task, sha, state['token'], 'ACTIVE', checkpoint='a' * 40)
    with pytest.raises(CoordinationError):
        a.transition(task, sha, state['token'], 'RELEASED')
    assert b.read(task)[0] == new


def test_network_failure_is_not_an_unclaimed_slot(clients):
    a, _ = clients
    git(a.git.repo, 'remote', 'set-url', 'origin', '/definitely/missing/yios.git')
    with pytest.raises(CoordinationError):
        a.read('finance/TEST0000001')


def test_released_ready_submission_cannot_race_canonical_publication(clients):
    a,b=clients
    task='finance/TEST0000001'
    sha,state=a.acquire(task,None)
    released,_=a.transition(task,sha,state['token'],'RELEASED',checkpoint='a'*40,acceptance='READY_FOR_INTEGRATION')
    with pytest.raises(CoordinationError,match='frozen'):
        b.acquire(task,released)


def test_production_legacy_gates_fail_closed_before_remote_claim(clients):
    a, _ = clients
    production = Coordination(a.git, machine='machine-b', owner='machine-b')
    for task in ('finance/XP-26tqGFXc', 'integration/finance', 'visual-forensics/5umJ63d3rzQ'):
        with pytest.raises(CoordinationError, match='legacy|protected'):
            production.acquire(task, expected=None)
    assert not git(a.git.repo, 'ls-remote', '--heads', 'origin', 'refs/heads/yios/claims/*')


def test_ref_namespace_and_identity_reject_path_and_command_injection(clients):
    a, _ = clients
    for task in ('finance/../x', '-x', 'finance/TEST0000001/extra', 'finance/TEST 000001'):
        with pytest.raises(CoordinationError):
            a.acquire(task, expected=None)


def test_claim_commit_has_only_state_and_no_research_tree(clients):
    a, _ = clients
    sha, state = a.acquire('finance/TEST0000001', expected=None)
    assert git(a.git.repo, 'ls-tree', '--name-only', sha) == 'state.json'
    assert json.loads(git(a.git.repo, 'show', sha + ':state.json')) == state


def setup_checkpoint(client):
    from scripts.yios import Workflow, write_json
    from scripts.yios_coordination import utc
    client.git.run('commit','--allow-empty','-m','isolated checkpoint fixture')
    task='finance/TEST0000001'
    claim,state=client.acquire(task,None,channel_id='fixture-channel')
    branch='yios-test/checkpoints/TEST0000001'
    client.git.run('switch','-c',branch)
    w=Workflow(client.git.repo,client.machine,namespace=client.namespace)
    w.coordination=client
    write_json(w.local/'safety.json',dict(checked_utc=utc(),five_hour=10,weekly=10,context_reserve='AVAILABLE_UNMETERED',paid_credits=0))
    base=client.git.run('rev-parse','HEAD')
    write_json(w.local/'session.json',{'task':task,'claim_sha':claim,'token':state['token'],'branch':branch,'source_base':base})
    p=client.git.repo/'research/tasks'/task
    write_json(p/'CHECKPOINT.json',{'task':task,'video_id':'TEST0000001','channel_id':'fixture-channel',
       'status':'PARTIAL','source_base':base,'completed_stages':['evidence'], 'remaining_stages':['review'],
       'continuation':'Continue fixture review','source_fingerprints':{'fixture':'a'*64},'media':[],'artifacts':[]})
    (p/'notes.md').write_text('NON-PRODUCTION PARTIAL CHECKPOINT\n')
    return w,p


def test_partial_checkpoint_pushed_then_loaded_by_independent_context(clients):
    from scripts.yios_workspace import sha256
    a,b=clients
    w,p=setup_checkpoint(a)
    saved=w.save([str((p/'notes.md').relative_to(w.git.repo))])
    assert saved['publication']=='REMOTELY_VERIFIED'
    release=w.switch_to('machine-b')
    sha,state=b.read('finance/TEST0000001')
    assert state['status']=='RELEASED' and sha==release['release_sha']
    b.git.fetch('refs/heads/'+state['task_branch'],state['checkpoint'])
    b.git.run('switch','-c','loaded-checkpoint',state['checkpoint'])
    cp=json.loads((b.git.repo/'research/tasks/finance/TEST0000001/CHECKPOINT.json').read_text())
    assert cp['status']=='PARTIAL' and cp['continuation']=='Continue fixture review'
    for artifact in cp['artifacts']:
        assert sha256(b.git.repo/artifact['path'])==artifact['sha256']
    assert b.acquire('finance/TEST0000001',sha)[1]['machine']=='machine-b'


def test_failed_push_keeps_local_commit_checkpoint_and_claim(clients):
    a,_=clients
    w,p=setup_checkpoint(a)
    remote=Path(git(a.git.repo,'remote','get-url','origin'))
    hook=remote/'hooks/pre-receive'
    hook.write_text('#!/bin/sh\nwhile read old new ref; do\n case "$ref" in refs/heads/yios-test/checkpoints/*) exit 1;; esac\ndone\nexit 0\n')
    hook.chmod(0o755)
    with pytest.raises(CoordinationError,match='UNSYNCED'):
        w.save([str((p/'notes.md').relative_to(w.git.repo))])
    session=w.session()
    assert session['publication']=='UNSYNCED'
    assert git(a.git.repo,'rev-parse','HEAD')==session['local_commit']
    assert json.loads(git(a.git.repo,'show','HEAD:research/tasks/finance/TEST0000001/CHECKPOINT.json'))['status']=='PARTIAL'
    assert a.read('finance/TEST0000001')[1]['status']=='ACTIVE'
    assert not git(a.git.repo,'status','--porcelain')


def test_lost_ack_recovery_is_bound_to_exact_writer_checkpoint(clients):
    from scripts.yios import write_json
    a,_=clients
    w,p=setup_checkpoint(a)
    original=w.session()
    w.save([str((p/'notes.md').relative_to(w.git.repo))])
    saved=w.session()
    write_json(w.local/'session.json',{**original,'publication':'UNSYNCED'})
    assert w.recover()['publication']=='REMOTELY_VERIFIED'
    assert w.session()['claim_sha']==saved['claim_sha']
    write_json(w.local/'session.json',{**saved,'token':'wrong-writer'})
    with pytest.raises(CoordinationError):
        w.recover()


def test_checkpoint_claim_identity_cannot_be_changed(clients):
    from scripts.yios import write_json
    a,_=clients
    w,p=setup_checkpoint(a)
    cp=json.loads((p/'CHECKPOINT.json').read_text())
    write_json(p/'CHECKPOINT.json',{**cp,'channel_id':'other-channel'})
    with pytest.raises(CoordinationError,match='identity'):
        w.save([str((p/'notes.md').relative_to(w.git.repo))])
