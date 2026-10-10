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
