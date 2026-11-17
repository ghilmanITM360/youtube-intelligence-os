"""Cooperative remote writer exclusion using durable, single-parent Git histories.

No ref deletion, force update, timeout takeover, shared index or canonical writes.
Every state mutation has exactly the inspected remote state as its only parent.
This restriction, rather than arbitrary fast-forward pushes, makes races conflict.
"""
from __future__ import annotations

import datetime as dt
import getpass
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import uuid


class CoordinationError(RuntimeError):
    pass


class Git:
    def __init__(self, repo: Path, remote: str = 'origin'):
        self.repo = Path(repo).resolve()
        if not re.fullmatch(r'[A-Za-z0-9_-]+', remote):
            raise CoordinationError('Invalid remote name')
        self.remote = remote

    def run(self, *args: str, data: str | None = None) -> str:
        env = {**os.environ, 'GIT_NO_LAZY_FETCH': '1', 'GIT_TERMINAL_PROMPT': '0',
               'GIT_LFS_SKIP_SMUDGE': '1'}
        try:
            result = subprocess.run(['git', '-C', str(self.repo), *map(str, args)], input=data,
                                    capture_output=True, text=True, env=env, timeout=60)
        except subprocess.TimeoutExpired as exc:
            raise CoordinationError(f'git {args[0]} timed out; verify remote state before retry') from exc
        if result.returncode:
            raise CoordinationError(f'git {args[0]} failed: {result.stderr.strip()}')
        return result.stdout.strip()

    def head(self, ref: str) -> str | None:
        self.run('check-ref-format', ref)
        lines = self.run('ls-remote', '--refs', self.remote, ref).splitlines()
        if not lines:
            return None
        exact = [line.split() for line in lines if line.split()[1] == ref]
        if len(exact) != 1 or not re.fullmatch(r'[a-f0-9]{40}', exact[0][0]):
            raise CoordinationError('Ambiguous remote reference')
        return exact[0][0]

    def fetch(self, ref: str, sha: str) -> None:
        self.run('fetch', '--no-tags', '--no-write-fetch-head', self.remote, ref)
        self.run('cat-file', '-e', sha + '^{commit}')
        if self.head(ref) != sha:
            raise CoordinationError('Remote changed during fetch; retry from fresh state')

    def publish(self, sha: str, ref: str, expected: str | None) -> None:
        if self.head(ref) != expected:
            raise CoordinationError('Stale remote head; unpublished commit preserved: ' + sha)
        self.run('push', '--porcelain', self.remote, f'{sha}:{ref}')
        if self.head(ref) != sha:
            raise CoordinationError('UNSYNCED: exact remote publication unverified; local commit ' + sha)


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


class Coordination:
    def __init__(self, git: Git, namespace: str = 'yios/claims', machine: str | None = None,
                 owner: str | None = None):
        self.git = git
        if not re.fullmatch(r'(?:yios/claims|yios-test/[A-Za-z0-9_/-]+)', namespace):
            raise CoordinationError('Only production or explicit yios-test namespaces are allowed')
        git.run('check-ref-format', 'refs/heads/' + namespace + '/probe')
        self.namespace = namespace
        self.machine = machine or socket.gethostname()
        self.owner = owner or getpass.getuser()

    def ref(self, task: str) -> str:
        if not re.fullmatch(r'(?:finance|visual-forensics)/[A-Za-z0-9_-]{11}|integration/(?:finance|visual-forensics)', task):
            raise CoordinationError('Invalid task identity (stream/canonical YouTube ID)')
        return f'refs/heads/{self.namespace}/{task}'

    def read(self, task: str) -> tuple[str | None, dict | None]:
        ref = self.ref(task)
        sha = self.git.head(ref)
        if sha is None:
            return None, None
        self.git.fetch(ref, sha)
        state = json.loads(self.git.run('show', sha + ':state.json'))
        if state.get('version') != 1 or state.get('task') != task or state.get('status') not in {'ACTIVE', 'RELEASED'}:
            raise CoordinationError('Malformed remote ownership state; manual review required')
        return sha, state

    def legacy_gate(self, task: str) -> None:
        if self.namespace != 'yios/claims':
            return
        if task.startswith('finance/') or task == 'integration/finance':
            self._release_gate('finance', 'research/finance-economics-intelligence')
        if task in {'visual-forensics/5umJ63d3rzQ', 'integration/visual-forensics'}:
            self._release_gate('visual-forensics', 'research/casually-finance-editing-forensics')

    def _release_gate(self, stream: str, branch: str) -> None:
        """Only a published explicit release + both real-Mac attestations unlocks legacy scope."""
        message = f'{stream} legacy/protected ownership: published release and real two-Mac acceptance not certified'
        ref = 'refs/heads/' + branch
        sha = self.git.head(ref)
        if sha is None:
            raise CoordinationError(message)
        self.git.fetch(ref, sha)
        try:
            release = json.loads(self.git.run('show', f'{sha}:research/coordination/releases/{stream}.json'))
            if release['state'] != 'EXPLICITLY_RELEASED_TO_YIOS_COORDINATION' or release['scope'] != stream or not release['released_by'] or not release['continuation']:
                raise ValueError('release identity/scope missing')
            self.git.run('merge-base','--is-ancestor',release['checkpoint_commit'],sha)
            self.git.run('merge-base','--is-ancestor',release['implementation_commit'],sha)
            self.git.run('cat-file','-e',release['implementation_commit']+':scripts/yios.py')
            self.git.run('cat-file','-e',release['implementation_commit']+':scripts/yios_integration.py')
            hosts = set()
            for machine in ('machine-a','machine-b'):
                entry = release['machine_acceptance'][machine]
                cert_ref = 'refs/heads/' + entry['branch']
                cert_head = self.git.head(cert_ref)
                if not cert_head:
                    raise ValueError('acceptance branch missing')
                self.git.fetch(cert_ref,cert_head)
                self.git.run('merge-base','--is-ancestor',entry['commit'],cert_head)
                cert = json.loads(self.git.run('show',f'{entry["commit"]}:{entry["path"]}'))
                if cert['machine'] != machine or cert['status'] != 'REAL_MAC_ACCEPTANCE_PASS' or cert['simulated'] is not False:
                    raise ValueError('actual-Mac acceptance required')
                if not cert.get('protocol_tests_pass') or not cert.get('checkpoint_restore_pass') or not cert.get('media_gate_pass'):
                    raise ValueError('acceptance gates incomplete')
                hosts.add(cert['hardware_id_sha256'])
            if len(hosts) != 2:
                raise ValueError('two distinct actual hosts required')
        except (KeyError,ValueError,CoordinationError) as exc:
            raise CoordinationError(message + '; ' + str(exc)) from exc

    def _write(self, task: str, expected: str | None, state: dict) -> tuple[str, dict]:
        ref = self.ref(task)
        if self.git.head(ref) != expected:
            raise CoordinationError('Stale claim state; no ownership change')
        state = {**state, 'version': 1, 'task': task, 'previous': expected, 'updated_utc': utc(),
                 'transition_id': uuid.uuid4().hex}
        blob = self.git.run('hash-object', '-w', '--stdin', data=json.dumps(state, sort_keys=True) + '\n')
        tree = self.git.run('mktree', data=f'100644 blob {blob}\tstate.json\n')
        parents = ['-p', expected] if expected else []
        sha = self.git.run('commit-tree', tree, *parents, data=f'YIOS {task} {state["status"]}\n')
        # Keep attempts recoverable even if the network response is lost.
        self.git.run('update-ref', 'refs/yios/attempts/' + state['transition_id'], sha)
        self.git.publish(sha, ref, expected)
        return sha, state

    def acquire(self, task: str, expected: str | None, channel_id: str | None = None,
                stage: str = 'whole-video') -> tuple[str, dict]:
        self.ref(task)
        self.legacy_gate(task)
        sha, old = self.read(task)
        if sha != expected:
            raise CoordinationError('Stale claim state; retry after inspecting current writer')
        if old and old['status'] != 'RELEASED':
            raise CoordinationError('Task already has an active writer; no idle/timeout takeover')
        if old and old.get('acceptance') == 'ACCEPTED':
            raise CoordinationError('Task already canonically accepted; no duplicate audit')
        if old and old.get('acceptance') == 'READY_FOR_INTEGRATION':
            raise CoordinationError('Submitted packet is frozen for integration; withdrawal needs a reviewed explicit protocol')
        if old and old.get('transfer_to') not in (None, self.machine):
            raise CoordinationError('Explicit handoff is reserved for another machine')
        state = {**(old or {}), 'status': 'ACTIVE', 'owner': self.owner, 'machine': self.machine,
                 'hostname': socket.gethostname(), 'token': uuid.uuid4().hex, 'channel_id': channel_id,
                 'stage': stage, 'transfer_to': None, 'acceptance': 'IN_PROGRESS',
                 'action': 'ACQUIRE'}
        return self._write(task, expected, state)

    def transition(self, task: str, expected: str, token: str, status: str, **updates) -> tuple[str, dict]:
        sha, state = self.read(task)
        if sha != expected or not state or state['status'] != 'ACTIVE':
            raise CoordinationError('Stale or released writer state; no transition authorized')
        if state.get('token') != token or state.get('machine') != self.machine or state.get('owner') != self.owner:
            raise CoordinationError('Writer identity/token mismatch; cannot release another writer')
        if status not in {'ACTIVE', 'RELEASED'}:
            raise CoordinationError('Invalid ownership transition')
        allowed = {'checkpoint', 'task_branch', 'continuation', 'acceptance', 'transfer_to', 'source_base'}
        if set(updates) - allowed:
            raise CoordinationError('Invalid ownership fields')
        if updates.get('acceptance') == 'ACCEPTED' and not task.startswith('integration/'):
            raise CoordinationError('Only verified canonical reconciliation can accept a research task')
        return self._write(task, expected, {**state, **updates, 'status': status, 'action': 'RELEASE' if status == 'RELEASED' else 'CHECKPOINT'})

    def reconcile(self, task: str, expected: str, coordinator_sha: str, coordinator_token: str,
                  canonical_commit: str) -> tuple[str,dict]:
        stream = task.split('/')[0]
        coord_sha, coord = self.read('integration/' + stream)
        sha, state = self.read(task)
        if coord_sha != coordinator_sha or not coord or coord['status'] != 'ACTIVE' or coord['token'] != coordinator_token or coord['machine'] != self.machine or coord['owner'] != self.owner:
            raise CoordinationError('Canonical reconciliation requires current exclusive coordinator')
        if sha != expected or not state or state['status'] != 'RELEASED' or state.get('acceptance') != 'READY_FOR_INTEGRATION':
            raise CoordinationError('Task changed or was not released READY_FOR_INTEGRATION')
        return self._write(task,sha,{**state,'acceptance':'ACCEPTED','canonical_commit':canonical_commit,'action':'INTEGRATED'})

    def claims(self) -> list[dict]:
        lines = self.git.run('ls-remote', '--heads', self.git.remote, f'refs/heads/{self.namespace}/*')
        result = []
        for line in lines.splitlines():
            sha, ref = line.split()
            task = ref.split(self.namespace + '/', 1)[1]
            got, state = self.read(task)
            if got != sha:
                raise CoordinationError('Claims changed while listing; rerun status')
            result.append({'remote_sha': sha, **state})
        return result
