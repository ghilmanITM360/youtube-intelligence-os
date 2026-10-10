"""Explicit pending transcript registration; no canonical repository writes."""
import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import inventory_catalog as ic
import register_supplied_channel as rsc
import register_structured_source as rss
from test_register_structured_source import Args, _xlsx_bytes, _transcript_member_text


@pytest.fixture
def packet(tmp_path):
    db = tmp_path / 'catalog.db'
    ic.cmd_init(Args(db_path=str(db)))
    workbook = tmp_path / 'Master.xlsx'
    directory = tmp_path / 'transcripts'
    directory.mkdir()
    workbook.write_bytes(_xlsx_bytes({
        'Channel Overview': [
            ['Source: Test | Scraped 10 Sep 2026 | 2 videos'],
            ['Field', 'Value'], ['Channel Name', 'Channel X'], ['Handle', '@channelx'],
            ['Channel ID', 'UCCHANNELX'], ['Channel URL', 'https://www.youtube.com/channel/UCCHANNELX'],
            ['Subscribers', 100], ['Total Videos (YouTube)', 2],
        ],
        'All Videos': [
            ['#', 'Video ID', 'Title', 'Video URL', 'Published (UTC)', 'Date', 'Sec', 'Views', 'Likes', 'Comments', 'Views/Day', 'Engagement', 'Desc Chars', 'Transcript Words', 'Transcript File', 'Thumbnail URL'],
            [1, 'video000001', 'Title A', 'https://www.youtube.com/watch?v=video000001', '2026-09-09 00:00:00', 46274, 600, 10, 1, 1, 10, .2, 12, 3, 'one.txt', 'https://i.ytimg.com/a.jpg'],
            [2, 'video000002', 'Title B', 'https://www.youtube.com/watch?v=video000002', '2026-09-09 00:00:00', 46274, 600, 10, 1, 1, 10, .2, 12, None, None, 'https://i.ytimg.com/b.jpg'],
        ],
        'Descriptions': [
            ['#', 'Video ID', 'Title', 'Link Count', 'Description Links (URLs)', 'Full Description'],
            [1, 'video000001', 'Title A', 0, '', 'Description A'],
            [2, 'video000002', 'Title B', 0, '', 'Description B'],
        ],
    }))
    (directory / 'one.txt').write_text(_transcript_member_text(
        channel='Channel X', title='Title A', video_id='video000001',
        url='https://www.youtube.com/watch?v=video000001', published='2026-09-09T00:00:00.000Z',
        duration='00:10:00', views=10, likes=1, comments=1,
        caption_type='auto_generated', language='en', word_count=3,
        transcript_body='Transcript body text.',
    ))
    return workbook, directory, db, tmp_path / 'raw', tmp_path / 'manifests'


def test_default_still_requires_complete_transcript_pack(packet):
    with pytest.raises(ic.CatalogError, match='reconcile exactly'):
        rsc.register(*packet)


def test_pending_identity_has_no_fake_transcript_and_verifies(packet, monkeypatch):
    monkeypatch.setattr(ic, "MANIFESTS_DIR", packet[4])
    result = rsc.register(*packet, transcript_pending_ids=['video000002'])
    assert result['transcript_pending_ids'] == ['video000002']
    with sqlite3.connect(packet[2]) as conn:
        assert conn.execute('SELECT COUNT(*) FROM videos').fetchone()[0] == 2
        assert conn.execute('SELECT COUNT(*) FROM transcripts').fetchone()[0] == 1
        assert conn.execute("SELECT transcript_word_count FROM video_snapshots s JOIN videos v USING(video_id) WHERE v.youtube_video_id='video000002'").fetchone()[0] is None
        gap = conn.execute("SELECT message FROM ingestion_errors WHERE error_type='TranscriptPending'").fetchone()[0]
        assert 'video000002' in gap
        assert conn.execute('PRAGMA foreign_key_check').fetchall() == []
    manifest = Path(result['manifest']).read_text()
    assert 'Transcript pending: 1' in manifest
    assert 'video000002' in manifest
    rss.cmd_verify(Args(db_path=str(packet[2]), dataset_id=result['dataset_id']))
    with pytest.raises(ic.CatalogError, match='overlap'):
        rsc.register(*packet, transcript_pending_ids=['video000002'])


@pytest.mark.parametrize('pending', [['unknown0001'], ['video000001', 'video000002'], ['video000002', 'video000002']])
def test_pending_declaration_must_match_only_missing_ids(packet, pending):
    with pytest.raises(ic.CatalogError):
        rsc.register(*packet, transcript_pending_ids=pending)
    with sqlite3.connect(packet[2]) as conn:
        assert conn.execute('SELECT COUNT(*) FROM videos').fetchone()[0] == 0


def test_empty_transcript_cannot_be_relabelled_pending(packet):
    text = (packet[1] / 'one.txt').read_text().replace('Transcript body text.', '')
    (packet[1] / 'empty.txt').write_text(text)
    with pytest.raises(ic.CatalogError, match='empty'):
        rsc.register(*packet, transcript_pending_ids=['video000002'])


def test_missing_transcripts_remain_visible_in_coverage(packet):
    import report_channel_coverage as coverage
    rsc.register(*packet, transcript_pending_ids=['video000002'])
    with sqlite3.connect(packet[2]) as conn:
        conn.row_factory = sqlite3.Row
        row = coverage._tier_a_registered_channels(conn)[0]
    assert row['transcripts_available'] == 1
    assert row['transcripts_pending'] == 1


def test_verifier_rejects_missing_pending_declaration(packet, monkeypatch):
    monkeypatch.setattr(ic, "MANIFESTS_DIR", packet[4])
    result = rsc.register(*packet, transcript_pending_ids=['video000002'])
    with sqlite3.connect(packet[2]) as conn:
        conn.execute("DELETE FROM ingestion_errors WHERE error_type='TranscriptPending'")
    with pytest.raises(SystemExit):
        rss.cmd_verify(Args(db_path=str(packet[2]), dataset_id=result['dataset_id']))


def test_existing_channel_pending_registration_preserves_history(packet, monkeypatch):
    import io
    import zipfile

    monkeypatch.setattr(ic, 'MANIFESTS_DIR', packet[4])
    first = rsc.register(*packet, transcript_pending_ids=['video000002'])
    with sqlite3.connect(packet[2]) as conn:
        before = conn.execute('SELECT * FROM video_snapshots ORDER BY video_snapshot_id').fetchall()
    output = io.BytesIO()
    with zipfile.ZipFile(packet[0]) as source, zipfile.ZipFile(output, 'w') as target:
        for member in source.namelist():
            data = source.read(member)
            if member == 'xl/sharedStrings.xml':
                data = data.replace(b'video000001', b'video000003').replace(b'video000002', b'video000004').replace(b'one.txt', b'')
            if member == 'xl/worksheets/sheet2.xml':
                data = data.replace(b'<c r="N2"><v>3</v></c>', b'')
            target.writestr(member, data)
    packet[0].write_bytes(output.getvalue())
    (packet[1] / 'one.txt').unlink()
    second = rsc.register(*packet, transcript_pending_ids=['video000003', 'video000004'])
    assert second['channel_id'] == first['channel_id']
    assert second['transcript_count'] == 0
    with sqlite3.connect(packet[2]) as conn:
        assert conn.execute('SELECT COUNT(*) FROM channels').fetchone()[0] == 1
        assert conn.execute('SELECT COUNT(*) FROM videos').fetchone()[0] == 4
        assert conn.execute('SELECT * FROM video_snapshots ORDER BY video_snapshot_id LIMIT 2').fetchall() == before
    rss.cmd_verify(Args(db_path=str(packet[2]), dataset_id=second['dataset_id']))


def test_sparse_identity_packet_does_not_invent_public_observations(packet, monkeypatch):
    import io
    import zipfile
    import xml.etree.ElementTree as element_tree

    monkeypatch.setattr(ic, 'MANIFESTS_DIR', packet[4])
    output = io.BytesIO()
    namespace = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(packet[0]) as source, zipfile.ZipFile(output, 'w') as target:
        for member in source.namelist():
            data = source.read(member)
            if member == 'xl/worksheets/sheet1.xml':
                tree = element_tree.fromstring(data)
                for row in tree.findall('m:sheetData/m:row', namespace):
                    for cell in list(row):
                        if cell.get('r') in {'B7', 'B8'}:
                            row.remove(cell)
                data = element_tree.tostring(tree)
            if member == 'xl/worksheets/sheet2.xml':
                tree = element_tree.fromstring(data)
                for row in tree.findall('m:sheetData/m:row', namespace)[1:]:
                    for cell in list(row):
                        if cell.get('r', '').rstrip('0123456789') in {'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'}:
                            row.remove(cell)
                data = element_tree.tostring(tree)
            target.writestr(member, data)
    packet[0].write_bytes(output.getvalue())
    (packet[1] / 'one.txt').unlink()
    result = rsc.register(*packet, transcript_pending_ids=['video000001', 'video000002'])
    with sqlite3.connect(packet[2]) as conn:
        assert conn.execute('SELECT COUNT(*) FROM transcripts').fetchone()[0] == 0
        assert conn.execute('SELECT video_type FROM video_snapshots').fetchall() == [(None,), (None,)]
        assert conn.execute('SELECT views,likes,comments,duration_seconds,transcript_word_count FROM video_snapshots').fetchall() == [(None, None, None, None, None)] * 2
    rss.cmd_verify(Args(db_path=str(packet[2]), dataset_id=result['dataset_id']))


@pytest.mark.parametrize('field', ['title', 'views'])
def test_v2_verifier_rejects_missing_observed_field_provenance(packet, monkeypatch, field):
    monkeypatch.setattr(ic, 'MANIFESTS_DIR', packet[4])
    result = rsc.register(*packet, transcript_pending_ids=['video000002'])
    with sqlite3.connect(packet[2]) as conn:
        conn.execute('DELETE FROM field_provenance WHERE video_snapshot_id IS NOT NULL AND field_name=?', (field,))
    with pytest.raises(SystemExit):
        rss.cmd_verify(Args(db_path=str(packet[2]), dataset_id=result['dataset_id']))
