"""Research rollups must include verified channel overlays without accepting drafts."""
import importlib.util
import json
import sys
from pathlib import Path

RESEARCH = Path(__file__).resolve().parents[1] / 'docs/research/thumbnail-forensics-2026-10-02'
sys.path.insert(0, str(RESEARCH))


def builder():
    spec = importlib.util.spec_from_file_location('packaging_master_test', RESEARCH / 'build_master_packages.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_master_loader_includes_all_verified_channel_overlays():
    module = builder()
    thumbnails, packages = module.audited(), module.package_audits()
    assert len(thumbnails) == 518
    assert len(packages) == 518
    for file in RESEARCH.glob('channels/*/package-audits.json'):
        for row in json.loads(file.read_text()):
            assert packages[row['Package_ID']] == row
            assert row['Thumbnail_ID'] in thumbnails


def test_package_input_loader_excludes_unverified_drafts():
    from build_package_inputs import thumb_rows
    rows = thumb_rows()
    assert len(rows) == 518
    assert all(batch != 'B002-27' for batch, row in rows.values())


def test_unreviewed_overlay_cannot_enter_rollups(tmp_path):
    import pytest
    from packaging_audit_records import verified_records
    (tmp_path / 'package-batch-plan.json').write_text('{"verified_thumbnail_batches": []}')
    (tmp_path / 'individual-audit-batch-001.json').write_text('[]')
    channel = tmp_path / 'channels' / 'channel'
    channel.mkdir(parents=True)
    (channel / 'thumbnail-audits.json').write_text('[{"Thumbnail_ID":"THB-missing","qa_status":"PRIMARY_SEQUENTIAL_QA_PASS"}]')
    (channel / 'qa.json').write_text('{"reviews": []}')
    with pytest.raises(ValueError, match='explicit QA'):
        verified_records(tmp_path)


def test_current_rollups_reconcile_and_source_hashes_match():
    import csv
    import hashlib
    from reconcile_packaging_progress import qa_video_ids
    master = list(csv.DictReader((RESEARCH / 'master-packages.csv').open()))
    packages = json.loads((RESEARCH / 'package-forensics.json').read_text())['rows']
    summary = json.loads((RESEARCH / 'packaging-progress-summary.json').read_text())
    assert sum(r['Thumbnail_Audit_Status'].startswith('AUDITED') for r in master) == 518
    assert sum(r['Packaging_Audit_Status'].startswith('AUDITED') for r in master) == len(packages) == 518
    assert len(qa_video_ids(RESEARCH)) == summary['packages']['qa_sampled'] == 121
    assert len(list(csv.DictReader((RESEARCH / 'rollup-reconciliation.csv').open()))) == 8
    for path, digest in summary['source_SHA256'].items():
        assert hashlib.sha256((RESEARCH.parents[2] / path).read_bytes()).hexdigest() == digest, path


def test_dashboard_derives_current_exact_id_totals():
    import reconcile_packaging_progress as progress
    data = progress.dashboard_payload(RESEARCH)
    assert data['totals'] == dict(titles=2303, thumbnails=518, packages=518, qa=121, channels_complete=1)
    assert data['current_channel']['completed_videos'] == 5
    assert data['current_channel']['remaining_videos'] == 34


def test_dashboard_updates_qa_without_double_counting_or_drafts(tmp_path):
    import shutil
    import reconcile_packaging_progress as progress
    # Use real authoritative records; add a valid review twice, plus an unapproved draft.
    for name in ['package-batch-plan.json', 'individual-audit-batch-001.json', 'master-packages.csv', 'title-analyst-audit.csv', 'channel-processing-queue.csv']:
        shutil.copy(RESEARCH / name, tmp_path / name)
    for pattern in ['audit-batch-B002-*.json', 'package-audit-PK-*.json', 'package-qa-review-*.json']:
        for file in RESEARCH.glob(pattern):
            shutil.copy(file, tmp_path / file.name)
    shutil.copytree(RESEARCH / 'channels', tmp_path / 'channels')
    before = progress.dashboard_payload(tmp_path)
    review = dict(Video_ID='EvuEMhh7SSk', result='PASS', Package_ID='PKG-EvuEMhh7SSk')
    (tmp_path / 'package-qa-review-new.json').write_text(json.dumps([review, review]))
    (tmp_path / 'audit-batch-B002-unapproved.json').write_text('[{"Thumbnail_ID":"THB-draft"}]')
    after = progress.dashboard_payload(tmp_path)
    assert after['totals']['qa'] == before['totals']['qa'] + 1
    assert after['totals']['thumbnails'] == before['totals']['thumbnails']
    assert after['totals']['packages'] == before['totals']['packages']
    assert after['current_channel']['completed_videos'] == 6
    assert after['current_channel']['remaining_videos'] == 33
    assert after['current_channel']['next_Video_ID'] != 'EvuEMhh7SSk'
    # Overlay and duplicated title identities remain part of the exact-ID union.
    with (tmp_path / 'title-analyst-audit.csv').open('a') as file:
        file.write((tmp_path / 'title-analyst-audit.csv').read_text().splitlines()[1] + '\n')
    assert progress.dashboard_payload(tmp_path)['totals']['titles'] == 2303
    assert after['totals']['channels_complete'] == 1
    assert all(row['Thumbnail_ID'] != 'THB-draft' for row in after['master'] if row['Thumbnail_Audit_Status'].startswith('AUDITED'))


def test_channel_completion_uses_full_coverage_not_stale_status(tmp_path):
    import shutil
    import reconcile_packaging_progress as progress
    for file in RESEARCH.glob('*'):
        if file.suffix in {'.csv', '.json'}:
            shutil.copy(file, tmp_path / file.name)
    shutil.copytree(RESEARCH / 'channels', tmp_path / 'channels')
    queue = progress.read_csv(tmp_path / 'channel-processing-queue.csv')
    next(row for row in queue if row['Channel_Name'] == 'Hypothetically')['Channel_Status'] = 'COMPLETE'
    progress.write_csv(tmp_path / 'channel-processing-queue.csv', queue)
    data = progress.dashboard_payload(tmp_path)
    assert data['totals']['channels_complete'] == 1
    assert data['current_channel']['name'] == 'Hypothetically'


def test_workbook_and_json_match_derived_summary():
    from validate_progress_workbook import validate
    result = validate(RESEARCH)
    assert result['totals']['thumbnails'] == 518
    assert result['native_features'] == 'PASS'
