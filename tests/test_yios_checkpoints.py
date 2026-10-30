import hashlib
import json
from pathlib import Path

import pytest

from scripts.yios_coordination import CoordinationError
from scripts.yios_workspace import check_safety, validate_checkpoint, verify_media


def test_usage_or_disk_gate_blocks_without_spending(tmp_path):
    from scripts.yios_coordination import utc
    safe = dict(checked_utc=utc(), five_hour=43, weekly=23, context_reserve='AVAILABLE_UNMETERED', paid_credits=0)
    assert check_safety(safe, tmp_path, free_bytes=6 * 1024**3)['credits_action'] == 'NEVER_REDEEM_OR_PURCHASE'
    for key, value in [('five_hour', 90), ('weekly', 95), ('context_reserve', 'EXHAUSTED'), ('five_hour', None), ('checked_utc', '2020-01-01T00:00:00+00:00')]:
        with pytest.raises(CoordinationError):
            check_safety({**safe, key:value}, tmp_path, free_bytes=6 * 1024**3)
    with pytest.raises(CoordinationError):
        check_safety(safe, tmp_path, free_bytes=4 * 1024**3)


def test_media_restore_requires_actual_bytes_not_lfs_pointer(tmp_path):
    p = tmp_path / 'source.mp4'
    data = b'video-fixture'
    record = {'video_id':'TEST0000001', 'role':'original-video', 'path':str(p), 'bytes':len(data),
              'sha256':hashlib.sha256(data).hexdigest(), 'storage':'owner-private:fixture',
              'rights':'PRIVATE_REFERENCE_ONLY', 'recovery_status':'NOT_TESTED',
              'restore_procedure':'copy privately then verify this manifest'}
    with pytest.raises(CoordinationError, match='media'):
        verify_media([record], required=True)
    p.write_bytes(b'version https://git-lfs.github.com/spec/v1\noid sha256:' + b'a'*64)
    with pytest.raises(CoordinationError, match='media'):
        verify_media([record], required=True)
    p.write_bytes(data)
    assert verify_media([record], required=True)[0]['local_verification'] == 'HASH_VERIFIED_LOCAL_ONLY'
    assert record['recovery_status'] == 'NOT_TESTED'
    with pytest.raises(CoordinationError,match='identity'):
        verify_media([record],required=True,video_id='OTHER000001')
    with pytest.raises(CoordinationError,match='role'):
        verify_media([{**record,'role':'audio'}],required=True)


def test_partial_checkpoint_exact_artifacts_and_no_acceptance_upgrade(tmp_path):
    folder = tmp_path / 'research/tasks/finance/TEST0000001'
    folder.mkdir(parents=True)
    evidence = folder / 'notes.md'
    evidence.write_text('Observation with locator; interpretation explicitly limited.\n')
    cp = {'task':'finance/TEST0000001', 'video_id':'TEST0000001', 'channel_id':'fixture-channel',
          'status':'PARTIAL', 'completed_stages':['transcript'], 'remaining_stages':['claim-review'],
          'continuation':'Review claims; do not repeat transcript read.', 'artifacts':[], 'media':[],
          'source_fingerprints':{'fixture':'a'*64}}
    result = validate_checkpoint(tmp_path, cp, [str(evidence.relative_to(tmp_path))])
    assert result['status'] == 'PARTIAL'
    assert result['artifacts'][0]['sha256'] == hashlib.sha256(evidence.read_bytes()).hexdigest()
    with pytest.raises(CoordinationError):
        validate_checkpoint(tmp_path, {**cp, 'status':'ACCEPTED'}, [str(evidence.relative_to(tmp_path))])
    with pytest.raises(CoordinationError):
        validate_checkpoint(tmp_path, {**cp, 'continuation':''}, [str(evidence.relative_to(tmp_path))])


def test_checkpoint_rejects_canonical_edits_symlinks_and_huge_assets(tmp_path):
    prefix = 'research/tasks/finance/TEST0000001/'
    folder = tmp_path / prefix
    folder.mkdir(parents=True)
    outside = tmp_path / 'VIDEO_AUDIT_966.jsonl'
    outside.write_text('{}')
    (folder/'escape.json').symlink_to(outside)
    cp = {'task':'finance/TEST0000001','video_id':'TEST0000001','channel_id':'x','status':'IN_PROGRESS',
          'completed_stages':[],'remaining_stages':['all'],'continuation':'Read source','source_fingerprints':{'x':'a'*64},'media':[]}
    for name in ('VIDEO_AUDIT_966.jsonl', prefix+'escape.json', '../bad'):
        with pytest.raises(CoordinationError):
            validate_checkpoint(tmp_path, cp, [name])


def test_ready_packet_must_have_six_reviews_and_no_remaining_stages(tmp_path):
    folder=tmp_path/'research/tasks/finance/TEST0000001'
    folder.mkdir(parents=True)
    p=folder/'packet.json'
    p.write_text(json.dumps({'batch_id':'TEST','reviews':[{'Video_ID':'TEST0000001'}]}))
    cp={'task':'finance/TEST0000001','video_id':'TEST0000001','channel_id':'x','status':'READY_FOR_INTEGRATION',
        'completed_stages':['transcript'],'remaining_stages':[],'continuation':'Submit for integration',
        'source_fingerprints':{'x':'a'*64},'media':[]}
    with pytest.raises(CoordinationError, match='six|dimension'):
        validate_checkpoint(tmp_path, cp, [str(p.relative_to(tmp_path))])
