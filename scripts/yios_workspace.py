"""Portable checkpoint validation; no source copying or remote writes."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import shutil

from scripts.yios_coordination import CoordinationError

FINANCE = 'research/finance-economics-intelligence'
FINANCE_BRANCH = 'research/finance-economics-intelligence'
DIMS = ('TITLE', 'THUMBNAIL', 'SCRIPT', 'TOPIC', 'PERFORMANCE', 'VIRALITY')
COMPLETE = {'COMPLETE_EVIDENCE_BACKED', 'COMPLETE_LIMITED_EVIDENCE'}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def check_safety(record: dict, path: Path, free_bytes: int | None = None) -> dict:
    try:
        age = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(record['checked_utc'])).total_seconds()
        if not 0 <= age <= 1200:
            raise ValueError('usage reading older than 20 minutes')
        for key, limit in [('five_hour', 90), ('weekly', 95)]:
            value = record[key]
            if not isinstance(value, (float, int)) or not 0 <= value < limit:
                raise ValueError(key + ' missing or stop threshold reached')
        if record['context_reserve'] not in {'AVAILABLE', 'AVAILABLE_UNMETERED'}:
            raise ValueError('context/execution reserve unavailable')
        if not isinstance(record['paid_credits'], (float, int)) or record['paid_credits'] < 0:
            raise ValueError('credit reading unavailable')
    except (KeyError, TypeError, ValueError) as exc:
        raise CoordinationError('Safety gate: ' + str(exc)) from exc
    free = shutil.disk_usage(path).free if free_bytes is None else free_bytes
    if free < 5 * 1024**3:
        raise CoordinationError('Safety gate: less than 5 GiB free')
    return {**record, 'free_bytes':free, 'credits_action':'NEVER_REDEEM_OR_PURCHASE'}


def verify_media(records: list[dict], required: bool = False, video_id: str | None = None,
                 channel_id: str | None = None) -> list[dict]:
    if required and not records:
        raise CoordinationError('Required original media manifest is missing')
    if required and not any(r.get('role') == 'original-video' for r in records):
        raise CoordinationError('Required original-video media role missing')
    result = []
    for r in records:
        required_keys = {'video_id','role','path','bytes','sha256','storage','rights','recovery_status','restore_procedure'}
        if required_keys - r.keys() or not re.fullmatch('[a-f0-9]{64}', r.get('sha256','')):
            raise CoordinationError('Incomplete media provenance/recovery record')
        if (video_id and r['video_id'] != video_id) or (channel_id and r.get('channel_id') != channel_id):
            raise CoordinationError('Media video/channel identity mismatch')
        p = Path(r['path']).expanduser()
        valid = p.is_file() and p.stat().st_size == r['bytes'] and sha256(p) == r['sha256']
        if valid:
            with p.open('rb') as f:
                valid = not f.read(128).startswith(b'version https://git-lfs.github.com/spec/v1')
        if required and not valid:
            raise CoordinationError('Required media missing, hash mismatch or LFS pointer: ' + str(p))
        result.append({**r, 'local_verification':'HASH_VERIFIED_LOCAL_ONLY' if valid else 'MISSING_OR_UNVERIFIED'})
    return result


def validate_checkpoint(repo: Path, checkpoint: dict, files: list[str]) -> dict:
    task = checkpoint.get('task','')
    if not re.fullmatch(r'(finance|visual-forensics)/[A-Za-z0-9_-]{11}', task):
        raise CoordinationError('Invalid checkpoint task')
    if checkpoint.get('video_id') != task.split('/')[1] or not checkpoint.get('channel_id'):
        raise CoordinationError('Checkpoint video/channel identity missing')
    if checkpoint.get('status') not in {'PARTIAL','IN_PROGRESS','READY_FOR_INTEGRATION'}:
        raise CoordinationError('Only canonical integration can mark research ACCEPTED')
    if not checkpoint.get('continuation') or not isinstance(checkpoint.get('remaining_stages'),list) or not isinstance(checkpoint.get('completed_stages'),list):
        raise CoordinationError('Exact continuation and stage lists required')
    fingerprints = checkpoint.get('source_fingerprints')
    if not isinstance(fingerprints,dict) or not fingerprints or any(not re.fullmatch('[a-f0-9]{64}', v) for v in fingerprints.values()):
        raise CoordinationError('Source SHA-256 fingerprints required')
    root = repo.resolve()
    prefix = 'research/tasks/' + task + '/'
    artifacts = []
    packets = []
    if not files or len(files) != len(set(files)):
        raise CoordinationError('Explicit unique checkpoint artifact list required')
    for name in files:
        p = root / name
        if not name.startswith(prefix) or '..' in Path(name).parts or p.is_symlink() or not p.resolve().is_relative_to(root / prefix) or not p.is_file():
            raise CoordinationError('Checkpoint files must stay within their own task folder: ' + name)
        if p.suffix.lower() not in {'.json','.jsonl','.csv','.tsv','.md','.txt','.yaml','.yml','.png','.jpg','.jpeg','.webp'} or p.stat().st_size > 5 * 1024**2:
            raise CoordinationError('Unsupported/large checkpoint asset; use private media manifest: ' + name)
        if p.suffix == '.json':
            value = json.loads(p.read_text())
            if isinstance(value,dict) and 'reviews' in value:
                packets.append(value)
        artifacts.append({'path':name,'bytes':p.stat().st_size,'sha256':sha256(p)})
    ready = checkpoint['status'] == 'READY_FOR_INTEGRATION'
    if ready and checkpoint['remaining_stages']:
        raise CoordinationError('READY research still has remaining stages')
    if ready and task.startswith('finance/'):
        reviews = [r for p in packets for r in p['reviews']]
        if len(reviews) != 1 or reviews[0].get('Video_ID') != checkpoint['video_id']:
            raise CoordinationError('Exactly one own-video Finance packet required')
        statuses = reviews[0].get('statuses',{})
        if set(statuses) != {d+'_REVIEW' for d in DIMS} or not all(v in COMPLETE for v in statuses.values()):
            raise CoordinationError('All six Finance dimensions required for integration submission')
        for section in ('title','thumbnail','script','topic','virality'):
            if not reviews[0].get(section):
                raise CoordinationError('Missing research dimension: ' + section)
    media = verify_media(checkpoint.get('media',[]), required=task.startswith('visual-forensics/'),
                         video_id=checkpoint['video_id'], channel_id=checkpoint['channel_id'] if task.startswith('visual-forensics/') else None)
    return {**checkpoint,'artifacts':artifacts,'media':media,'acceptance':'NOT_CANONICALLY_ACCEPTED'}


def finance_counts(rows: list[dict], universe: list[dict]) -> dict:
    if len(rows) != len({r['Video_ID'] for r in rows}) or len(universe) != len({r['video_id'] for r in universe}):
        raise CoordinationError('Duplicate canonical identities')
    complete = {r['Video_ID'] for r in rows if set(r['statuses']) == {d+'_REVIEW' for d in DIMS} and all(v in COMPLETE for v in r['statuses'].values())}
    original = {r['Video_ID'] for r in rows}
    if not original <= {r['video_id'] for r in universe}:
        raise CoordinationError('Canonical universe/ledger identity drift')
    # The current expansion source contract has no accepted audit ledger yet.
    # Fail closed rather than inventing expansion completion from metadata.
    if any(r.get('audit_status') == 'DEEP_AUDIT_COMPLETE' and r['video_id'] not in original for r in universe):
        raise CoordinationError('Expansion acceptance needs its registered canonical audit contract')
    pending = next((r for r in rows if r['Video_ID'] not in complete and r.get('script',{}).get('review_scope') == 'NOT_REVIEWED'),None)
    return {'total':len(universe),'complete':len(complete),'remaining':len(universe)-len(complete),
            'original_pending':len(original-complete),'expansion_pending':len(universe)-len(original),
            'next':None if pending is None else {'video_id':pending['Video_ID'],'channel_id':pending['Channel_ID'],'title':pending['identity']['Title']}}
