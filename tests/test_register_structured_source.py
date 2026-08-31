"""Tests for scripts/register_structured_source.py and migration 002.
Stdlib unittest only. All filesystem/DB work happens under
tempfile.TemporaryDirectory(); nothing here touches the real repository.
"""
import importlib.util
import io
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "schemas" / "inventory"
SCRIPTS_DIR = REPO_ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import inventory_catalog  # noqa: E402
import register_structured_source as rss  # noqa: E402


class Args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


# ---------------------------------------------------------------------------
# Minimal fixture XLSX/ZIP builders (no openpyxl; matches the raw structure
# scripts/source_adapters/youtube_master_data.py actually reads).
# ---------------------------------------------------------------------------

def _col_letter(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def _xlsx_bytes(sheets):
    """sheets: dict[sheet_name] -> list of rows (list of cell values, None for blank)."""
    shared, shared_index = [], {}

    def sidx(s):
        if s not in shared_index:
            shared_index[s] = len(shared)
            shared.append(s)
        return shared_index[s]

    sheet_files = {}
    for i, (name, rows) in enumerate(sheets.items(), start=1):
        row_xml = []
        for r_idx, row in enumerate(rows, start=1):
            cells = []
            for c_idx, value in enumerate(row, start=1):
                if value is None:
                    continue
                ref = "{}{}".format(_col_letter(c_idx), r_idx)
                if isinstance(value, (int, float)):
                    cells.append('<c r="{}"><v>{}</v></c>'.format(ref, value))
                else:
                    cells.append('<c r="{}" t="s"><v>{}</v></c>'.format(ref, sidx(str(value))))
            row_xml.append('<row r="{}">{}</row>'.format(r_idx, "".join(cells)))
        sheet_files["sheet{}.xml".format(i)] = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
            "<sheetData>{}</sheetData></worksheet>"
        ).format("".join(row_xml))

    sheets_xml = "".join(
        '<sheet name="{}" sheetId="{}" r:id="rId{}"/>'.format(xml_escape(name), i, i)
        for i, name in enumerate(sheets.keys(), start=1)
    )
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        "<sheets>{}</sheets></workbook>"
    ).format(sheets_xml)

    rels_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{}</Relationships>'
    ).format("".join(
        '<Relationship Id="rId{0}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{0}.xml"/>'.format(i)
        for i in range(1, len(sheets) + 1)
    ))

    shared_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{0}" uniqueCount="{0}">{1}</sst>'
    ).format(len(shared), "".join("<si><t>{}</t></si>".format(xml_escape(s)) for s in shared))

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("xl/workbook.xml", workbook_xml)
        zf.writestr("xl/_rels/workbook.xml.rels", rels_xml)
        zf.writestr("xl/sharedStrings.xml", shared_xml)
        for fname, content in sheet_files.items():
            zf.writestr("xl/worksheets/{}".format(fname), content)
    return buf.getvalue()


def _transcript_member_text(*, channel, title, video_id, url, published, duration, views, likes,
                             comments, caption_type, language, word_count, description="A description.",
                             transcript_body="Transcript body text."):
    sep = "=" * 78
    header = "\n".join([
        "Channel      : {}".format(channel), "Title        : {}".format(title),
        "Video ID     : {}".format(video_id), "URL          : {}".format(url),
        "Published    : {}".format(published), "Duration     : {}".format(duration),
        "Views        : {}".format(views), "Likes        : {}".format(likes),
        "Comments     : {}".format(comments), "Caption type : {}".format(caption_type),
        "Language     : {}".format(language), "Word count   : {}".format(word_count),
    ])
    return "\n".join([
        header, sep, "DESCRIPTION", sep, description, "", "CONTENT", "00:00 Start", "",
        sep, "TRANSCRIPT", sep, transcript_body,
    ])


def _make_video_row(idx, channel, video_id, title, sec, views, likes, comments,
                     views_per_day, engagement, desc_chars, transcript_words,
                     published="2026-01-01 00:00:00"):
    # Columns: A=#,B=Channel,C=Video ID,D=Title,E=Video URL,F=Published (UTC),
    # G=Sec,H=Views,I=Likes,J=Comments,K=Views/Day,L=Engagement,M=Desc Chars,N=Transcript Words
    return [
        idx, channel, video_id, title, "https://www.youtube.com/watch?v={}".format(video_id),
        published, sec, views, likes, comments, views_per_day, engagement, desc_chars, transcript_words,
    ]


def _make_workbook(channels, videos):
    """channels: list of (name, youtube_channel_id, handle, url, subs, total_videos).
    videos: list of dicts as produced by _make_video_row-style positional args (already rows)."""
    overview_rows = [
        ["Source: Test | Scraped 01 Jan 2026 | fixture"],
        ["Field"] + [c[0] for c in channels],
        ["Channel Name"] + [c[0] for c in channels],
        ["Handle"] + [c[2] for c in channels],
        ["Channel ID"] + [c[1] for c in channels],
        ["Channel URL"] + [c[3] for c in channels],
        ["Subscribers"] + [c[4] for c in channels],
        ["Total Videos (YouTube)"] + [c[5] for c in channels],
    ]
    all_videos_rows = [
        ["#", "Channel", "Video ID", "Title", "Video URL", "Published (UTC)", "Sec", "Views",
         "Likes", "Comments", "Views/Day", "Engagement", "Desc Chars", "Transcript Words"],
    ] + videos
    return _xlsx_bytes({"Channel Overview": overview_rows, "All Videos": all_videos_rows})


class RegisterStructuredSourceTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.tmp.name)
        self.db_path = self.tmp_path / "catalog" / "test.db"

        self._orig_raw_root = inventory_catalog.RAW_DATA_ROOT
        self._orig_manifests_dir = inventory_catalog.MANIFESTS_DIR
        inventory_catalog.RAW_DATA_ROOT = self.tmp_path / "data" / "raw"
        inventory_catalog.MANIFESTS_DIR = self.tmp_path / "data" / "manifests"

    def tearDown(self):
        inventory_catalog.RAW_DATA_ROOT = self._orig_raw_root
        inventory_catalog.MANIFESTS_DIR = self._orig_manifests_dir
        self.tmp.cleanup()

    def init_catalog(self):
        inventory_catalog.cmd_init(Args(db_path=str(self.db_path)))

    def ingest_fixture(self, dataset_id="DS-000001", channels=None, videos=None,
                        extra_zip_members=None, unavailable_video_ids=None):
        """Builds a fixture workbook+transcript zip, ingests via Phase 1A, returns source dir."""
        channels = channels or [("Channel A", "UCAAA", "@a", "https://yt/a", 100, 2)]
        videos = videos if videos is not None else [
            _make_video_row(1, "Channel A", "vid00000001", "Video One", 100, 10, 1, 0, 1.0, 0.1, 50, 500),
            _make_video_row(2, "Channel A", "vid00000002", "Video Two", 200, 20, 2, 0, 2.0, 0.2, 60, 600),
        ]
        unavailable_video_ids = unavailable_video_ids or set()
        workbook_bytes = _make_workbook(channels, videos)

        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w") as zf:
            zf.writestr("INDEX.txt", "fixture index")
            for row in videos:
                video_id, title = row[2], row[3]
                is_unavailable = video_id in unavailable_video_ids
                zf.writestr(
                    "ChannelA/{}.txt".format(video_id),
                    _transcript_member_text(
                        channel=row[1], title=title, video_id=video_id,
                        url="https://www.youtube.com/watch?v={}".format(video_id),
                        published="2026-01-01T00:00:00.000Z", duration="00:01:40",
                        views=row[7], likes=row[8], comments=row[9],
                        caption_type="NONE AVAILABLE" if is_unavailable else "auto_generated",
                        language="-" if is_unavailable else "en", word_count=row[13],
                        transcript_body=("(No captions available for this video on YouTube.)"
                                          if is_unavailable else "Transcript body text."),
                    ),
                )
            for name, text in (extra_zip_members or {}).items():
                zf.writestr(name, text)

        source_dir = self.tmp_path / "source"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "YouTube_Master_Data.xlsx").write_bytes(workbook_bytes)
        (source_dir / "Transcripts_Test.zip").write_bytes(zip_buf.getvalue())

        inventory_catalog.cmd_ingest(Args(
            db_path=str(self.db_path), source=str(source_dir), dataset_id=dataset_id,
            name="Fixture Dataset", semantic_class="B", discovered_as=None,
        ))
        return source_dir

    # -- Test 1: Migration 1 -> 2 -----------------------------------------

    def test_migration_1_to_2_applies_cleanly(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        try:
            versions = {r[0] for r in conn.execute("SELECT schema_version FROM schema_meta;").fetchall()}
            # Every shipped migration file must apply, and every applied
            # version must correspond to a real shipped file — checked
            # against schemas/inventory/ itself so this test never needs
            # updating by hand when a later phase adds another migration.
            expected_versions = {
                int(p.stem.split("_", 1)[0]) for p in inventory_catalog.SCHEMA_DIR.glob("*.sql")
            }
            self.assertEqual(versions, expected_versions)
            self.assertIn(1, versions)
            self.assertIn(2, versions)
            tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()}
            expected = {"channels", "channel_snapshots", "videos", "video_snapshots", "transcripts", "field_provenance"}
            self.assertTrue(expected.issubset(tables))
            self.assertEqual(conn.execute("PRAGMA integrity_check;").fetchone()[0], "ok")
        finally:
            conn.close()

    # -- Test 2: Phase 1A data survives migration --------------------------

    def test_phase1a_data_survives_migration_explicit(self):
        self.init_catalog()
        self.ingest_fixture(dataset_id="DS-000001")
        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM datasets WHERE dataset_id='DS-000001';").fetchone()[0], 1
            )
            self.assertGreater(
                conn.execute("SELECT COUNT(*) FROM source_files WHERE dataset_id='DS-000001';").fetchone()[0], 0
            )
        finally:
            conn.close()

    # -- Test 3: Channel uniqueness ----------------------------------------

    def test_channel_youtube_id_uniqueness(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            conn.execute("""INSERT INTO datasets (dataset_id, dataset_name, semantic_class, description,
                source_type, ingestion_mode, status, discovered_as, date_received, created_at, updated_at, notes)
                VALUES ('DS-X','X','B',NULL,'EXTERNAL_FOLDER','CONTROLLED_COPY','INGESTED',NULL,'t','t','t',NULL);""")
            conn.execute("""INSERT INTO channels (channel_id, youtube_channel_id, handle, display_name, channel_url,
                created_from_dataset_id, created_at, updated_at, notes)
                VALUES ('CH-000001','UCdupe','@a','A',NULL,'DS-X','t','t',NULL);""")
            conn.commit()
            with self.assertRaises(sqlite3.IntegrityError):
                conn.execute("""INSERT INTO channels (channel_id, youtube_channel_id, handle, display_name, channel_url,
                    created_from_dataset_id, created_at, updated_at, notes)
                    VALUES ('CH-000002','UCdupe','@b','B',NULL,'DS-X','t','t',NULL);""")
        finally:
            conn.close()

    # -- Test 4: Video uniqueness -------------------------------------------

    def test_register_rejects_duplicate_workbook_video_id_without_duplicate_entity(self):
        self.init_catalog()
        videos = [
            _make_video_row(1, "Channel A", "sameid00001", "First", 100, 10, 1, 0, 1.0, 0.1, 50, 500),
            _make_video_row(2, "Channel A", "sameid00001", "Duplicate Row", 100, 10, 1, 0, 1.0, 0.1, 50, 500),
        ]
        self.ingest_fixture(videos=videos)
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM videos WHERE youtube_video_id='sameid00001';").fetchone()[0], 1
            )
        finally:
            conn.close()

    # -- Test 5: Snapshot append model --------------------------------------

    def test_video_snapshot_append_model_allows_multiple_observed_dates(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            self._insert_minimal_video(conn)
            conn.execute("""INSERT INTO video_snapshots (video_snapshot_id, video_id, dataset_id, registration_run_id,
                observed_at, published_at, title, duration_seconds, views, likes, comments, views_per_day,
                engagement_rate, description_char_count, transcript_word_count, created_at, notes)
                VALUES ('VS-000001','VID-000001','DS-X','RUN-000001','2026-01-01',NULL,'T',10,1,0,0,0,0,0,0,'t',NULL);""")
            conn.execute("""INSERT INTO video_snapshots (video_snapshot_id, video_id, dataset_id, registration_run_id,
                observed_at, published_at, title, duration_seconds, views, likes, comments, views_per_day,
                engagement_rate, description_char_count, transcript_word_count, created_at, notes)
                VALUES ('VS-000002','VID-000001','DS-X','RUN-000001','2026-02-01',NULL,'T',10,2,0,0,0,0,0,0,'t',NULL);""")
            conn.commit()
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM video_snapshots WHERE video_id='VID-000001';").fetchone()[0], 2
            )
        finally:
            conn.close()

    # -- Test 6: Duplicate same-dataset snapshot rejected -------------------

    def test_duplicate_snapshot_same_observed_at_rejected(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            self._insert_minimal_video(conn)
            conn.execute("""INSERT INTO video_snapshots (video_snapshot_id, video_id, dataset_id, registration_run_id,
                observed_at, published_at, title, duration_seconds, views, likes, comments, views_per_day,
                engagement_rate, description_char_count, transcript_word_count, created_at, notes)
                VALUES ('VS-000001','VID-000001','DS-X','RUN-000001','2026-01-01',NULL,'T',10,1,0,0,0,0,0,0,'t',NULL);""")
            conn.commit()
            with self.assertRaises(sqlite3.IntegrityError):
                conn.execute("""INSERT INTO video_snapshots (video_snapshot_id, video_id, dataset_id, registration_run_id,
                    observed_at, published_at, title, duration_seconds, views, likes, comments, views_per_day,
                    engagement_rate, description_char_count, transcript_word_count, created_at, notes)
                    VALUES ('VS-000002','VID-000001','DS-X','RUN-000001','2026-01-01',NULL,'T',10,2,0,0,0,0,0,0,'t',NULL);""")
        finally:
            conn.close()

    def _insert_minimal_video(self, conn):
        conn.execute("""INSERT INTO datasets (dataset_id, dataset_name, semantic_class, description,
            source_type, ingestion_mode, status, discovered_as, date_received, created_at, updated_at, notes)
            VALUES ('DS-X','X','B',NULL,'EXTERNAL_FOLDER','CONTROLLED_COPY','INGESTED',NULL,'t','t','t',NULL);""")
        conn.execute("""INSERT INTO ingestion_runs (run_id, dataset_id, started_at, completed_at, status,
            source_file_count, archive_member_count, total_size_bytes, errors_count, verification_status,
            tool_version, run_type, notes) VALUES ('RUN-000001','DS-X','t','t','COMPLETED',0,0,0,0,'VERIFIED','t','STRUCTURED_REGISTRATION',NULL);""")
        conn.execute("""INSERT INTO channels (channel_id, youtube_channel_id, handle, display_name, channel_url,
            created_from_dataset_id, created_at, updated_at, notes)
            VALUES ('CH-000001','UCabc','@a','A',NULL,'DS-X','t','t',NULL);""")
        conn.execute("""INSERT INTO videos (video_id, youtube_video_id, channel_id, canonical_url,
            created_from_dataset_id, created_at, updated_at, notes)
            VALUES ('VID-000001','abc123xyz00','CH-000001',NULL,'DS-X','t','t',NULL);""")

    # -- Test 7: Transcript availability (both states) ----------------------

    def test_transcript_availability_states(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            self._insert_minimal_video(conn)
            conn.execute("""INSERT INTO source_files (file_id, dataset_id, ingestion_run_id, parent_file_id,
                storage_kind, file_role, original_filename, original_path, relative_path, canonical_path,
                archive_member_path, extension, mime_type, size_bytes, sha256, semantic_class, evidence_layer,
                is_copied, is_archive_member, processing_status, verification_status, created_at, notes)
                VALUES ('FILE-000001','DS-X','RUN-000001',NULL,'ARCHIVE_MEMBER','TRANSCRIPT','a.txt','/x','a.txt',
                NULL,'a.txt','.txt',NULL,10,'h','B','RAW_SOURCE',0,1,'CATALOGED','HASHED','t',NULL);""")
            conn.execute("""INSERT INTO transcripts (transcript_id, video_id, dataset_id, registration_run_id,
                archive_member_file_id, availability_status, caption_type, language, word_count,
                transcript_sha256, description_present, created_at, notes)
                VALUES ('TR-000001','VID-000001','DS-X','RUN-000001','FILE-000001','AVAILABLE','auto_generated','en',100,'h',1,'t',NULL);""")
            conn.commit()
            self.assertEqual(conn.execute("SELECT availability_status FROM transcripts;").fetchone()[0], "AVAILABLE")
            with self.assertRaises(sqlite3.IntegrityError):
                conn.execute("""INSERT INTO transcripts (transcript_id, video_id, dataset_id, registration_run_id,
                    archive_member_file_id, availability_status, caption_type, language, word_count,
                    transcript_sha256, description_present, created_at, notes)
                    VALUES ('TR-000002','VID-000001','DS-X','RUN-000001','FILE-000001','SOMETHING_ELSE','x','x',0,'h',0,'t',NULL);""")
        finally:
            conn.close()

    # -- Test 8: Missing-caption placeholder registers UNAVAILABLE ----------

    def test_register_creates_unavailable_transcript_for_missing_caption(self):
        self.init_catalog()
        videos = [
            _make_video_row(1, "Channel A", "haswithcap1", "Has Captions", 100, 10, 1, 0, 1.0, 0.1, 50, 500),
            _make_video_row(2, "Channel A", "nocaptionid", "No Captions", 100, 10, 1, 0, 1.0, 0.1, 50, 0),
        ]
        self.ingest_fixture(videos=videos, unavailable_video_ids={"nocaptionid"})
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        conn = sqlite3.connect(str(self.db_path))
        try:
            row = conn.execute(
                """SELECT t.availability_status FROM transcripts t JOIN videos v ON v.video_id = t.video_id
                   WHERE v.youtube_video_id = 'nocaptionid';"""
            ).fetchone()
            self.assertEqual(row[0], "UNAVAILABLE")
            available_row = conn.execute(
                """SELECT t.availability_status FROM transcripts t JOIN videos v ON v.video_id = t.video_id
                   WHERE v.youtube_video_id = 'haswithcap1';"""
            ).fetchone()
            self.assertEqual(available_row[0], "AVAILABLE")
        finally:
            conn.close()

    # -- Test 9: Provenance target CHECK -------------------------------------

    def test_field_provenance_exactly_one_target_check(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            conn.execute("""INSERT INTO datasets (dataset_id, dataset_name, semantic_class, description,
                source_type, ingestion_mode, status, discovered_as, date_received, created_at, updated_at, notes)
                VALUES ('DS-X','X','B',NULL,'EXTERNAL_FOLDER','CONTROLLED_COPY','INGESTED',NULL,'t','t','t',NULL);""")
            conn.execute("""INSERT INTO ingestion_runs (run_id, dataset_id, started_at, completed_at, status,
                source_file_count, archive_member_count, total_size_bytes, errors_count, verification_status,
                tool_version, run_type, notes) VALUES ('RUN-000001','DS-X','t','t','COMPLETED',0,0,0,0,'VERIFIED','t','STRUCTURED_REGISTRATION',NULL);""")
            conn.execute("""INSERT INTO channels (channel_id, youtube_channel_id, handle, display_name, channel_url,
                created_from_dataset_id, created_at, updated_at, notes)
                VALUES ('CH-000001','UCabc','@a','A',NULL,'DS-X','t','t',NULL);""")
            conn.commit()
            # zero targets
            with self.assertRaises(sqlite3.IntegrityError):
                conn.execute("""INSERT INTO field_provenance (provenance_id, dataset_id, registration_run_id,
                    source_file_id, channel_id, channel_snapshot_id, video_id, video_snapshot_id, transcript_id,
                    field_name, source_locator, value_origin, evidence_layer, extraction_method, observed_at,
                    created_at, notes) VALUES ('PR-1','DS-X','RUN-000001',NULL,NULL,NULL,NULL,NULL,NULL,'x','loc',
                    'SOURCE_EXTRACTED','EXTRACTED_FACT','m',NULL,'t',NULL);""")
            # two targets
            with self.assertRaises(sqlite3.IntegrityError):
                conn.execute("""INSERT INTO field_provenance (provenance_id, dataset_id, registration_run_id,
                    source_file_id, channel_id, channel_snapshot_id, video_id, video_snapshot_id, transcript_id,
                    field_name, source_locator, value_origin, evidence_layer, extraction_method, observed_at,
                    created_at, notes) VALUES ('PR-2','DS-X','RUN-000001',NULL,'CH-000001',NULL,'VID-000001',NULL,NULL,
                    'x','loc','SOURCE_EXTRACTED','EXTRACTED_FACT','m',NULL,'t',NULL);""")
            # exactly one target succeeds
            conn.execute("""INSERT INTO field_provenance (provenance_id, dataset_id, registration_run_id,
                source_file_id, channel_id, channel_snapshot_id, video_id, video_snapshot_id, transcript_id,
                field_name, source_locator, value_origin, evidence_layer, extraction_method, observed_at,
                created_at, notes) VALUES ('PR-3','DS-X','RUN-000001',NULL,'CH-000001',NULL,NULL,NULL,NULL,
                'x','loc','SOURCE_EXTRACTED','EXTRACTED_FACT','m',NULL,'t',NULL);""")
            conn.commit()
        finally:
            conn.close()

    # -- Test 10: Registration idempotency -----------------------------------

    def test_register_idempotent_on_rerun(self):
        self.init_catalog()
        self.ingest_fixture()
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos;").fetchone()[0], 2)
            self.assertEqual(
                conn.execute(
                    "SELECT COUNT(*) FROM ingestion_runs WHERE run_type='STRUCTURED_REGISTRATION' AND status='COMPLETED';"
                ).fetchone()[0],
                1,
            )
        finally:
            conn.close()

    def test_backfill_legacy_workbook_provenance_changes_only_source_file_id(self):
        self.init_catalog()
        self.ingest_fixture()
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))

        def snapshot_without_source_file_id(conn):
            snapshot = {}
            tables = [r[0] for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;"
            )]
            for table in tables:
                columns = [r[1] for r in conn.execute("PRAGMA table_info({});".format(table))]
                if table == "field_provenance":
                    columns.remove("source_file_id")
                snapshot[table] = conn.execute(
                    "SELECT {} FROM {};".format(", ".join(columns), table)
                ).fetchall()
            return snapshot

        conn = sqlite3.connect(str(self.db_path))
        workbook_file_id = conn.execute(
            """SELECT file_id FROM source_files
               WHERE dataset_id='DS-000001' AND storage_kind='PHYSICAL_FILE'
                 AND file_role='STRUCTURED_METADATA' AND original_filename='YouTube_Master_Data.xlsx';"""
        ).fetchone()[0]
        before_without_link = snapshot_without_source_file_id(conn)
        before_links = dict(conn.execute(
            "SELECT provenance_id, source_file_id FROM field_provenance ORDER BY provenance_id;"
        ))
        workbook_provenance_ids = {
            r[0] for r in conn.execute(
                """SELECT provenance_id FROM field_provenance
                   WHERE dataset_id='DS-000001' AND source_file_id IS NULL
                     AND source_locator LIKE 'YouTube_Master_Data.xlsx#%';"""
            )
        }
        conn.close()
        self.assertTrue(workbook_provenance_ids)

        args = Args(db_path=str(self.db_path), dataset_id="DS-000001")
        rss.cmd_backfill_workbook_provenance(args)

        conn = sqlite3.connect(str(self.db_path))
        after_without_link = snapshot_without_source_file_id(conn)
        after_links = dict(conn.execute(
            "SELECT provenance_id, source_file_id FROM field_provenance ORDER BY provenance_id;"
        ))
        conn.close()
        self.assertEqual(after_without_link, before_without_link)
        self.assertEqual(
            after_links,
            {provenance_id: (workbook_file_id if provenance_id in workbook_provenance_ids else source_file_id)
             for provenance_id, source_file_id in before_links.items()},
        )

        rss.cmd_backfill_workbook_provenance(args)
        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(
                dict(conn.execute(
                    "SELECT provenance_id, source_file_id FROM field_provenance ORDER BY provenance_id;"
                )),
                after_links,
            )
        finally:
            conn.close()

    # -- Test 11: Changed-source rejection -----------------------------------

    def test_register_rejects_changed_canonical_source(self):
        self.init_catalog()
        self.ingest_fixture()
        conn = sqlite3.connect(str(self.db_path))
        canonical_xlsx = conn.execute(
            "SELECT canonical_path FROM source_files WHERE dataset_id='DS-000001' AND file_role='STRUCTURED_METADATA';"
        ).fetchone()[0]
        conn.close()
        Path(canonical_xlsx).write_bytes(b"tampered-bytes-not-a-real-xlsx")

        with self.assertRaises(SystemExit) as ctx:
            rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        self.assertNotEqual(ctx.exception.code, 0)

        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos;").fetchone()[0], 0)
            self.assertEqual(
                conn.execute(
                    "SELECT COUNT(*) FROM ingestion_runs WHERE run_type='STRUCTURED_REGISTRATION' AND status='COMPLETED';"
                ).fetchone()[0],
                0,
            )
        finally:
            conn.close()

    # -- Test 12: Atomic rollback on critical parse failure -------------------

    def test_register_rolls_back_fully_on_malformed_data(self):
        self.init_catalog()
        videos = [
            _make_video_row(1, "Channel A", "goodvideoid", "Good", 100, 10, 1, 0, 1.0, 0.1, 50, 500),
            _make_video_row(2, "Channel A", "badvideoid1", "Bad", "NOT_A_NUMBER", 10, 1, 0, 1.0, 0.1, 50, 500),
        ]
        self.ingest_fixture(videos=videos)
        with self.assertRaises(SystemExit):
            rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM channels;").fetchone()[0], 0)
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos;").fetchone()[0], 0)
            self.assertEqual(
                conn.execute(
                    "SELECT COUNT(*) FROM ingestion_runs WHERE run_type='STRUCTURED_REGISTRATION' AND status='FAILED';"
                ).fetchone()[0],
                1,
            )
        finally:
            conn.close()

    # -- Extra: full successful register end-to-end --------------------------

    def test_register_end_to_end_counts_and_provenance_coverage(self):
        self.init_catalog()
        self.ingest_fixture()
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        conn = sqlite3.connect(str(self.db_path))
        try:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM channels;").fetchone()[0], 1)
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM videos;").fetchone()[0], 2)
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM video_snapshots;").fetchone()[0], 2)
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM transcripts;").fetchone()[0], 2)
            expected_provenance = (
                1 * len(rss.CHANNEL_FIELDS) + 1 * len(rss.CHANNEL_SNAPSHOT_FIELDS)
                + 2 * len(rss.VIDEO_FIELDS) + 2 * len(rss.VIDEO_SNAPSHOT_FIELDS)
                + 2 * len(rss.TRANSCRIPT_HEADER_FIELDS)
            )
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM field_provenance;").fetchone()[0], expected_provenance)
            self.assertEqual(conn.execute("PRAGMA integrity_check;").fetchone()[0], "ok")
            self.assertEqual(len(conn.execute("PRAGMA foreign_key_check;").fetchall()), 0)
            status = conn.execute("SELECT status FROM datasets WHERE dataset_id='DS-000001';").fetchone()[0]
            self.assertEqual(status, "STRUCTURED_REGISTERED")
        finally:
            conn.close()

        manifest_path = inventory_catalog.MANIFESTS_DIR / "DS-000001.md"
        self.assertTrue(manifest_path.exists())
        text = manifest_path.read_text()
        self.assertIn("## Phase 1B Structured Registration", text)
        self.assertIn("## Dataset Identity", text)  # Phase 1A section preserved

    def test_verify_reports_verified_after_successful_register(self):
        self.init_catalog()
        self.ingest_fixture()
        rss.cmd_register(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        try:
            rss.cmd_verify(Args(db_path=str(self.db_path), dataset_id="DS-000001"))
        except SystemExit as exc:
            self.fail("cmd_verify unexpectedly exited with code {}".format(exc.code))


if __name__ == "__main__":
    unittest.main()
