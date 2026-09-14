"""Tests for scripts/inventory_catalog.py. Stdlib unittest only.

All filesystem work happens under tempfile.TemporaryDirectory(); nothing
here reads or writes the real repository's data/raw or data/manifests.
"""
import hashlib
import importlib.util
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "inventory_catalog.py"

spec = importlib.util.spec_from_file_location("inventory_catalog", SCRIPT_PATH)
inventory_catalog = importlib.util.module_from_spec(spec)
sys.modules["inventory_catalog"] = inventory_catalog
spec.loader.exec_module(inventory_catalog)


class Args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class InventoryCatalogTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.tmp.name)
        self.db_path = self.tmp_path / "catalog" / "test.db"

        # Redirect raw-copy and manifest output away from the real repo.
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

    def make_source_dir(self, files):
        """files: dict of filename -> bytes."""
        source_dir = self.tmp_path / "source"
        source_dir.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (source_dir / name).write_bytes(content)
        return source_dir

    def make_zip_bytes(self, members):
        """members: dict of archive-path -> bytes."""
        import io

        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            for name, content in members.items():
                zf.writestr(name, content)
        return buf.getvalue()

    # -- Test 1: Schema initialization ----------------------------------

    def test_schema_initialization_creates_expected_tables(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        try:
            tables = {
                row[0]
                for row in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table';"
                ).fetchall()
            }
        finally:
            conn.close()
        expected = {
            "schema_meta", "datasets", "ingestion_runs", "source_locations",
            "source_files", "file_relationships", "ingestion_errors",
        }
        self.assertTrue(expected.issubset(tables))

    # -- Test 2: Foreign keys --------------------------------------------

    def test_foreign_keys_reject_invalid_reference(self):
        self.init_catalog()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        try:
            with self.assertRaises(sqlite3.IntegrityError):
                conn.execute(
                    """INSERT INTO ingestion_runs
                       (run_id, dataset_id, started_at, status, tool_version)
                       VALUES ('RUN-999999', 'DS-DOES-NOT-EXIST', '2026-01-01T00:00:00.000Z',
                               'STARTED', 'test');"""
                )
                conn.commit()
        finally:
            conn.close()

    # -- Test 3: SHA-256 correctness -------------------------------------

    def test_sha256_matches_known_value(self):
        f = self.tmp_path / "known.txt"
        content = b"hello world"
        f.write_bytes(content)
        expected = hashlib.sha256(content).hexdigest()
        self.assertEqual(inventory_catalog.sha256_file(f), expected)
        self.assertEqual(inventory_catalog.sha256_bytes(content), expected)

    # -- Test 4: Safe ingestion (source untouched) -----------------------

    def test_safe_ingestion_does_not_modify_source(self):
        self.init_catalog()
        source_dir = self.make_source_dir({"data.xlsx": b"fake-xlsx-bytes"})
        before = {
            p.name: (p.stat().st_size, inventory_catalog.sha256_file(p))
            for p in source_dir.iterdir()
        }

        inventory_catalog.cmd_ingest(Args(
            db_path=str(self.db_path), source=str(source_dir), dataset_id="DS-000001",
            name="Test Dataset", semantic_class="B", discovered_as=None,
        ))

        after = {
            p.name: (p.stat().st_size, inventory_catalog.sha256_file(p))
            for p in source_dir.iterdir()
        }
        self.assertEqual(before, after)

        canonical = inventory_catalog.RAW_DATA_ROOT / "competitors" / "DS-000001" / "data.xlsx"
        self.assertTrue(canonical.exists())
        self.assertEqual(inventory_catalog.sha256_file(canonical), before["data.xlsx"][1])

    # -- Test 5: ZIP member inventory ------------------------------------

    def test_zip_member_inventory_without_permanent_extraction(self):
        zip_path = self.tmp_path / "archive.zip"
        member_content = b"INDEX file content"
        zip_path.write_bytes(self.make_zip_bytes({
            "INDEX.txt": member_content,
            "sub/one.txt": b"transcript body",
        }))

        members = inventory_catalog._inspect_zip_members(zip_path)

        self.assertEqual(len(members), 2)
        names = {m["archive_member_path"] for m in members}
        self.assertEqual(names, {"INDEX.txt", "sub/one.txt"})
        index_member = next(m for m in members if m["archive_member_path"] == "INDEX.txt")
        self.assertEqual(index_member["sha256"], hashlib.sha256(member_content).hexdigest())
        self.assertEqual(index_member["file_role"], "ARCHIVE_INDEX")
        # No extraction directory was created next to the archive.
        self.assertFalse((self.tmp_path / "sub").exists())

    # -- Test 6: Idempotency ----------------------------------------------

    def test_idempotent_reingest_creates_no_duplicate_dataset(self):
        self.init_catalog()
        source_dir = self.make_source_dir({"data.xlsx": b"fixed-content"})

        for _ in range(2):
            inventory_catalog.cmd_ingest(Args(
                db_path=str(self.db_path), source=str(source_dir), dataset_id="DS-000001",
                name="Test Dataset", semantic_class="B", discovered_as=None,
            ))

        conn = sqlite3.connect(str(self.db_path))
        try:
            dataset_count = conn.execute(
                "SELECT COUNT(*) FROM datasets WHERE dataset_id = 'DS-000001';"
            ).fetchone()[0]
            file_count = conn.execute(
                "SELECT COUNT(*) FROM source_files WHERE dataset_id = 'DS-000001';"
            ).fetchone()[0]
        finally:
            conn.close()
        self.assertEqual(dataset_count, 1)
        self.assertEqual(file_count, 1)

    # -- Test 7: Conflict handling -----------------------------------------

    def test_conflicting_content_under_same_dataset_id_fails_safely(self):
        self.init_catalog()
        source_dir = self.make_source_dir({"data.xlsx": b"version-one"})
        inventory_catalog.cmd_ingest(Args(
            db_path=str(self.db_path), source=str(source_dir), dataset_id="DS-000001",
            name="Test Dataset", semantic_class="B", discovered_as=None,
        ))

        # Same Dataset ID, different content.
        source_dir2 = self.make_source_dir2({"data.xlsx": b"version-two-different"})
        with self.assertRaises(SystemExit) as ctx:
            inventory_catalog.cmd_ingest(Args(
                db_path=str(self.db_path), source=str(source_dir2), dataset_id="DS-000001",
                name="Test Dataset", semantic_class="B", discovered_as=None,
            ))
        self.assertNotEqual(ctx.exception.code, 0)

        conn = sqlite3.connect(str(self.db_path))
        try:
            recorded_hash = conn.execute(
                "SELECT sha256 FROM source_files WHERE dataset_id='DS-000001' AND original_filename='data.xlsx';"
            ).fetchone()[0]
            failed_runs = conn.execute(
                "SELECT COUNT(*) FROM ingestion_runs WHERE dataset_id='DS-000001' AND status='FAILED';"
            ).fetchone()[0]
        finally:
            conn.close()
        self.assertEqual(recorded_hash, hashlib.sha256(b"version-one").hexdigest())
        self.assertEqual(failed_runs, 1)

    def make_source_dir2(self, files):
        source_dir = self.tmp_path / "source2"
        source_dir.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (source_dir / name).write_bytes(content)
        return source_dir

    # -- Test 8: Manifest/database consistency -----------------------------

    def test_manifest_file_count_matches_database(self):
        self.init_catalog()
        zip_bytes = self.make_zip_bytes({
            "INDEX.txt": b"Total files: 1",
            "channel/001_vid_title.txt": b"Caption type : auto_generated\ntranscript text here",
        })
        source_dir = self.make_source_dir({
            "data.xlsx": b"fake-xlsx-bytes",
            "transcripts.zip": zip_bytes,
        })

        inventory_catalog.cmd_ingest(Args(
            db_path=str(self.db_path), source=str(source_dir), dataset_id="DS-000001",
            name="Test Dataset", semantic_class="B", discovered_as=None,
        ))

        conn = sqlite3.connect(str(self.db_path))
        try:
            db_count = conn.execute(
                "SELECT COUNT(*) FROM source_files WHERE dataset_id = 'DS-000001';"
            ).fetchone()[0]
        finally:
            conn.close()

        manifest_path = inventory_catalog.MANIFESTS_DIR / "DS-000001.md"
        self.assertTrue(manifest_path.exists())
        manifest_text = manifest_path.read_text()
        self.assertIn("File record count: {}".format(db_count), manifest_text)

    def test_verify_allows_uncopied_reference_with_null_canonical_path(self):
        self.init_catalog()
        source_dir = self.make_source_dir({"reference.txt": b"historical reference"})
        inventory_catalog.cmd_ingest(Args(
            db_path=str(self.db_path), source=str(source_dir), dataset_id="DS-000001",
            name="Reference Dataset", semantic_class="C", discovered_as=None,
        ))
        conn = sqlite3.connect(str(self.db_path))
        with conn:
            conn.execute(
                "UPDATE source_files SET canonical_path=NULL,is_copied=0 "
                "WHERE dataset_id='DS-000001' AND original_filename='reference.txt'"
            )
        conn.close()
        inventory_catalog.cmd_verify(Args(db_path=str(self.db_path), dataset_id="DS-000001"))

    def test_verify_rejects_copied_file_with_null_canonical_path(self):
        self.init_catalog()
        source_dir = self.make_source_dir({"required.txt": b"required copy"})
        inventory_catalog.cmd_ingest(Args(
            db_path=str(self.db_path), source=str(source_dir), dataset_id="DS-000001",
            name="Required Dataset", semantic_class="C", discovered_as=None,
        ))
        conn = sqlite3.connect(str(self.db_path))
        with conn:
            conn.execute(
                "UPDATE source_files SET canonical_path=NULL "
                "WHERE dataset_id='DS-000001' AND original_filename='required.txt'"
            )
        conn.close()
        with self.assertRaises(SystemExit):
            inventory_catalog.cmd_verify(Args(db_path=str(self.db_path), dataset_id="DS-000001"))


if __name__ == "__main__":
    unittest.main()
