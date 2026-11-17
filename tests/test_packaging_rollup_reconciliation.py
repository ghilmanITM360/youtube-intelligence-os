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
    from reconcile_packaging_progress import dashboard_payload
    totals = dashboard_payload(RESEARCH)['totals']
    assert len(thumbnails) == totals['thumbnails']
    assert len(packages) == totals['packages']
    assert sum(not row['batch_id'].startswith('CHANNEL-002-') for row in packages.values()) == 518
    for file in RESEARCH.glob('channels/*/package-audits.json'):
        for row in json.loads(file.read_text()):
            assert packages[row['Package_ID']] == row
            assert row['Thumbnail_ID'] in thumbnails


def test_package_input_loader_excludes_unverified_drafts():
    from build_package_inputs import thumb_rows
    rows = thumb_rows()
    from reconcile_packaging_progress import dashboard_payload
    assert len(rows) == dashboard_payload(RESEARCH)['totals']['thumbnails']
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
    assert sum(r['Thumbnail_Audit_Status'].startswith('AUDITED') for r in master) == summary['thumbnails']['verified']
    assert sum(r['Packaging_Audit_Status'].startswith('AUDITED') for r in master) == len(packages) == summary['packages']['audited']
    assert len(qa_video_ids(RESEARCH)) == summary['packages']['qa_sampled']
    assert len(list(csv.DictReader((RESEARCH / 'rollup-reconciliation.csv').open()))) == sum(len(json.loads(file.read_text())) for file in RESEARCH.glob('channels/*/package-audits.json'))
    for path, digest in summary['source_SHA256'].items():
        assert hashlib.sha256((RESEARCH.parents[2] / path).read_bytes()).hexdigest() == digest, path


def test_dashboard_derives_current_exact_id_totals():
    import reconcile_packaging_progress as progress
    data = progress.dashboard_payload(RESEARCH)
    from packaging_audit_records import verified_records
    thumbnails, packages = verified_records(RESEARCH)
    assert data['totals']['titles'] == 2303
    assert data['totals']['thumbnails'] == len(thumbnails)
    assert data['totals']['packages'] == len(packages)
    assert data['totals']['channels_complete'] == 1
    assert data['current_channel']['completed_videos'] + data['current_channel']['remaining_videos'] == 39


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
    from packaging_audit_records import verified_records
    legacy_ids = {row['Video_ID'] for row in verified_records(tmp_path)[1].values() if row['batch_id'].startswith('PK-')}
    selected = next(row['Video_ID'] for row in before['master'] if row['Video_ID'] in legacy_ids and row['Channel_ID'] == before['current_channel']['Channel_ID'] and row['Packaging_Audit_Status'] == 'AUDITED' and row['Video_ID'] in before['qa_ids'])
    def clear_review(value):
        if isinstance(value, dict):
            if value.get('Video_ID') == selected or value.get('Package_ID') == 'PKG-' + selected:
                if 'result' in value:
                    value['result'] = 'QA_PENDING'
                if 'verdict' in value:
                    value['verdict'] = 'QA_PENDING'
            for item in value.values():
                clear_review(item)
        elif isinstance(value, list):
            for item in value:
                clear_review(item)
    for file in list(tmp_path.glob('package-qa-review-*.json')) + list(tmp_path.glob('channels/*/qa.json')):
        value = json.loads(file.read_text())
        clear_review(value)
        file.write_text(json.dumps(value))
    before = progress.dashboard_payload(tmp_path)
    review = dict(Video_ID=selected, result='PASS', Package_ID='PKG-' + selected)
    (tmp_path / 'package-qa-review-new.json').write_text(json.dumps([review, review]))
    (tmp_path / 'audit-batch-B002-unapproved.json').write_text('[{"Thumbnail_ID":"THB-draft"}]')
    after = progress.dashboard_payload(tmp_path)
    assert after['totals']['qa'] == before['totals']['qa'] + 1
    assert after['totals']['thumbnails'] == before['totals']['thumbnails']
    assert after['totals']['packages'] == before['totals']['packages']
    assert after['current_channel']['completed_videos'] == before['current_channel']['completed_videos'] + 1
    assert after['current_channel']['remaining_videos'] == before['current_channel']['remaining_videos'] - 1
    assert after['current_channel']['next_Video_ID'] != selected
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
    from reconcile_packaging_progress import dashboard_payload
    assert result['totals'] == dashboard_payload(RESEARCH)['totals']
    assert result['native_features'] == 'PASS'


def test_native_preserver_authors_preformatted_empty_cells(tmp_path):
    import zipfile
    from preserve_workbook_features import preserve
    namespace = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
    for name, cell in [('baseline', '<x:c r="A1" s="89"/>'), ('authored', '<c r="A1" t="str"><v>QA &amp; evidence</v></c>')]:
        with zipfile.ZipFile(tmp_path / name, 'w') as archive:
            archive.writestr('xl/worksheets/sheet1.xml', f'<x:worksheet xmlns:x="{namespace}" xmlns="{namespace}"><x:sheetData><x:row r="1">{cell}</x:row></x:sheetData></x:worksheet>')
            archive.writestr('native-feature', b'unchanged')
    preserve(tmp_path / 'authored', tmp_path / 'baseline')
    with zipfile.ZipFile(tmp_path / 'authored') as archive:
        xml = archive.read('xl/worksheets/sheet1.xml')
        assert b'>QA &amp; evidence<' in xml
        import xml.etree.ElementTree as ET
        ET.fromstring(xml)
        assert b's="89"' in xml
        assert archive.read('native-feature') == b'unchanged'


def test_existing_draft_precedes_new_visual_work(tmp_path):
    import shutil
    import reconcile_packaging_progress as progress
    for file in RESEARCH.glob('*'):
        if file.suffix in {'.csv', '.json'}:
            shutil.copy(file, tmp_path / file.name)
    shutil.copytree(RESEARCH / 'channels', tmp_path / 'channels')
    before = progress.dashboard_payload(tmp_path)
    channel = before['current_channel']['Channel_ID']
    candidates = [row for row in before['master'] if row['Channel_ID'] == channel and row['Packaging_Audit_Status'] != 'AUDITED']
    chosen = max(candidates, key=lambda row: row['Video_ID'])
    records = tmp_path / 'channels' / channel / 'packaging-progress.csv'
    rows = progress.read_csv(records)
    for row in rows:
        row['Thumbnail_Status'] = 'THUMBNAIL_DRAFT' if row['Video_ID'] == chosen['Video_ID'] else 'NOT_STARTED'
        row['Package_Status'] = 'NOT_STARTED'
    progress.write_csv(records, rows)
    pending = [dict(Video_ID=row['Video_ID'], result='PASS') for row in before['master'] if row['Channel_ID'] == channel and row['Packaging_Audit_Status'] == 'AUDITED']
    (tmp_path / 'package-qa-review-test.json').write_text(json.dumps(pending))
    assert progress.dashboard_payload(tmp_path)['current_channel']['next_Video_ID'] == chosen['Video_ID']


def test_promoted_successors_are_not_counted_as_unresolved_drafts():
    import reconcile_packaging_progress as progress
    from packaging_audit_records import verified_records
    data = progress.dashboard_payload(RESEARCH)
    verified, unused = verified_records(RESEARCH)
    unresolved = {row['Thumbnail_ID'] for file in RESEARCH.glob('audit-batch-B002-*.json') for row in json.loads(file.read_text()) if row['Thumbnail_ID'] not in verified}
    assert data['totals']['drafts'] == len(unresolved)
    assert data['totals']['drafts'] == data['totals']['drafts_valid'] + data['totals']['drafts_invalid']
    assert sum(int(row['Existing_Thumbnail_Drafts']) for row in data['queue']) == data['totals']['drafts_valid']
