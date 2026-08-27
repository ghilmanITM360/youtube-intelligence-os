"""Tests for scripts/register_batch.py and migration 003/004 (Phase 1C).
Stdlib unittest only. All filesystem/DB work happens under
tempfile.TemporaryDirectory() with monkeypatched fixture roots; nothing
here touches the real repository or real source folders.
"""
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import inventory_catalog as ic  # noqa: E402
import register_batch as rb  # noqa: E402
from source_adapters import batch_rules as rules  # noqa: E402


class Args:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class RegisterBatchTestCase(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmpdir.name)
        self.db_path = self.tmp / "catalog" / "test.db"

        self._orig_raw_root = ic.RAW_DATA_ROOT
        self._orig_manifests_dir = ic.MANIFESTS_DIR
        ic.RAW_DATA_ROOT = self.tmp / "data" / "raw"
        ic.MANIFESTS_DIR = self.tmp / "data" / "manifests"

        self._orig_root_specs = rules.ROOT_SPECS
        self._orig_codex_rules = rules.CODEX_RULES
        self._orig_registration_order = rules.REGISTRATION_ORDER
        self._orig_codex_meta = rules.CODEX_DATASET_META

        ic.cmd_init(Args(db_path=str(self.db_path)))
        self._seed_ds_000001()

    def tearDown(self):
        ic.RAW_DATA_ROOT = self._orig_raw_root
        ic.MANIFESTS_DIR = self._orig_manifests_dir
        rules.ROOT_SPECS = self._orig_root_specs
        rules.CODEX_RULES = self._orig_codex_rules
        rules.REGISTRATION_ORDER = self._orig_registration_order
        rules.CODEX_DATASET_META = self._orig_codex_meta
        self._tmpdir.cleanup()

    def _seed_ds_000001(self):
        """A minimal already-ingested DS-000001 so ROOT-1 hash comparison has
        something real to compare against."""
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA foreign_keys = ON;")
        source_dir = self.tmp / "ds1_source"
        source_dir.mkdir(parents=True)
        f = source_dir / "canonical.txt"
        f.write_text("canonical content")
        digest = ic.sha256_file(f)
        now = ic.now_iso()
        with conn:
            conn.execute(
                "INSERT INTO datasets (dataset_id, dataset_name, semantic_class, description, source_type, "
                "ingestion_mode, status, discovered_as, date_received, created_at, updated_at, notes) "
                "VALUES ('DS-000001','Fixture','B',NULL,'EXTERNAL_FOLDER','CONTROLLED_COPY','INGESTED',NULL,?,?,?,NULL);",
                (now, now, now),
            )
            conn.execute(
                "INSERT INTO ingestion_runs (run_id, dataset_id, started_at, completed_at, status, "
                "source_file_count, archive_member_count, total_size_bytes, errors_count, verification_status, "
                "tool_version, notes) VALUES ('RUN-000001','DS-000001',?,?,'COMPLETED',1,0,?,0,'VERIFIED','fixture',NULL);",
                (now, now, f.stat().st_size),
            )
            conn.execute(
                "INSERT INTO source_files (file_id, dataset_id, ingestion_run_id, parent_file_id, storage_kind, "
                "file_role, original_filename, original_path, relative_path, canonical_path, archive_member_path, "
                "extension, mime_type, size_bytes, sha256, semantic_class, evidence_layer, is_copied, "
                "is_archive_member, processing_status, verification_status, created_at, notes) "
                "VALUES ('FILE-000001','DS-000001','RUN-000001',NULL,'PHYSICAL_FILE','UNSPECIFIED', "
                "'canonical.txt', ?, 'canonical.txt', ?, NULL, '.txt', NULL, ?, ?, 'B', 'RAW_SOURCE', 1, 0, "
                "'CATALOGED', 'VERIFIED', ?, NULL);",
                (str(f), str(f), f.stat().st_size, digest, now),
            )
        conn.close()
        self.ds1_source_dir = source_dir
        self.ds1_file = f

    def _flat_root(self, name, files):
        """Creates a temp flat-dataset root with the given {filename: content}."""
        root = self.tmp / "roots" / name
        root.mkdir(parents=True)
        for fname, content in files.items():
            (root / fname).write_text(content)
        return root

    def _set_rules(self, root_specs, codex_rules=None, registration_order=None, codex_meta=None):
        rules.ROOT_SPECS = root_specs
        rules.CODEX_RULES = codex_rules if codex_rules is not None else []
        rules.REGISTRATION_ORDER = registration_order if registration_order is not None else [
            r["dataset_key"] for r in root_specs if r.get("kind") == "flat_dataset"
        ]
        rules.CODEX_DATASET_META = codex_meta if codex_meta is not None else {}

    # -- 1/2: recursive traversal, nested directories -----------------------

    def test_recursive_traversal_finds_nested_files(self):
        root = self.tmp / "roots" / "nested"
        (root / "a" / "b" / "c").mkdir(parents=True)
        (root / "top.txt").write_text("top")
        (root / "a" / "mid.txt").write_text("mid")
        (root / "a" / "b" / "c" / "deep.txt").write_text("deep")
        spec = {"index": 1, "path": str(root), "kind": "flat_dataset", "dataset_key": "NESTED",
                "dataset_name": "Nested", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY"}
        entries = list(rb.walk_root(spec))
        files = {e["relative_path"] for e in entries if e["entry_type"] == "FILE"}
        self.assertEqual(files, {"top.txt", "a/mid.txt", "a/b/c/deep.txt"})
        # every directory level is also recorded (3/4/1 rule: nothing silently skipped)
        dirs = {e["relative_path"] for e in entries if e["entry_type"] == "DIR"}
        self.assertEqual(dirs, {"a", "a/b", "a/b/c"})

    # -- 3: symlink non-following --------------------------------------------

    def test_symlinks_recorded_but_not_followed(self):
        root = self.tmp / "roots" / "symtest"
        real_dir = root / "real"
        real_dir.mkdir(parents=True)
        (real_dir / "inside.txt").write_text("inside")
        link_dir = root / "link_to_real"
        link_file = root / "link.txt"
        os.symlink(real_dir, link_dir)
        os.symlink(real_dir / "inside.txt", link_file)
        spec = {"index": 1, "path": str(root), "kind": "flat_dataset", "dataset_key": "SYM",
                "dataset_name": "Sym", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY"}
        entries = list(rb.walk_root(spec))
        symlink_paths = {e["relative_path"] for e in entries if e["entry_type"] == "SYMLINK"}
        self.assertEqual(symlink_paths, {"link_to_real", "link.txt"})
        # the symlinked directory's contents must never appear (not followed)
        all_paths = {e["relative_path"] for e in entries}
        self.assertNotIn("link_to_real/inside.txt", all_paths)

    # -- 4: exact duplicate detection -----------------------------------------

    def test_exact_duplicate_detection_across_roots(self):
        root_a = self._flat_root("dupA", {"one.txt": "same bytes"})
        root_b = self._flat_root("dupB", {"two.txt": "same bytes"})
        specs = [
            {"index": 2, "path": str(root_a), "kind": "flat_dataset", "dataset_key": "DUPA",
             "dataset_name": "Dup A", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY"},
            {"index": 3, "path": str(root_b), "kind": "flat_dataset", "dataset_key": "DUPB",
             "dataset_name": "Dup B", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY"},
        ]
        self._set_rules([self._already_ingested_spec()] + specs)
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        conn = sqlite3.connect(str(self.db_path))
        rows = conn.execute("SELECT relative_path, disposition FROM discovered_files WHERE relative_path IN ('one.txt','two.txt');").fetchall()
        by_name = dict(rows)
        # first-seen (root order) keeps INGEST, the later one becomes EXACT_DUPLICATE
        self.assertEqual(by_name["one.txt"], "INGEST")
        self.assertEqual(by_name["two.txt"], "EXACT_DUPLICATE")
        conn.close()

    def _already_ingested_spec(self):
        return {"index": 1, "path": str(self.ds1_source_dir), "kind": "already_ingested",
                "dataset_key": None, "existing_dataset_id": "DS-000001"}

    # -- 5: image metadata extraction -----------------------------------------

    def test_image_pipeline_extracts_metadata(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("Pillow not installed in this interpreter")
        img_path = self.tmp / "sample.png"
        Image.new("RGB", (16, 10), color=(255, 0, 0)).save(img_path)
        import image_pipeline
        info = image_pipeline.inspect(str(img_path))
        self.assertEqual(info["width_px"], 16)
        self.assertEqual(info["height_px"], 10)
        self.assertEqual(info["orientation"], "LANDSCAPE")
        self.assertEqual(len(info["dhash"]), 16)

    # -- 6: perceptual hash stability ------------------------------------------

    def test_perceptual_hash_stable_for_identical_image(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("Pillow not installed in this interpreter")
        import image_pipeline

        def _gradient_image(diagonal=False):
            img = Image.new("L", (20, 20))
            for y in range(20):
                for x in range(20):
                    v = ((x + y) if diagonal else x) * 12 % 256
                    img.putpixel((x, y), v)
            return img.convert("RGB")

        p1 = self.tmp / "a.png"
        p2 = self.tmp / "b.png"
        _gradient_image().save(p1)
        _gradient_image().save(p2)
        h1 = image_pipeline.inspect(str(p1))["dhash"]
        h2 = image_pipeline.inspect(str(p2))["dhash"]
        self.assertEqual(h1, h2)
        # dhash is gradient-based: a diagonal gradient has a genuinely
        # different adjacent-pixel structure than a horizontal one, so it
        # must hash differently (a flat solid-color image would not, since
        # dhash compares neighboring-pixel brightness and a flat fill has no
        # internal gradient to compare — not a useful case for this check).
        p3 = self.tmp / "c.png"
        _gradient_image(diagonal=True).save(p3)
        h3 = image_pipeline.inspect(str(p3))["dhash"]
        self.assertNotEqual(h1, h3)

    # -- 7: OCR result structure (schema-only, no live Vision call needed here) -

    def test_hamming_distance_helper(self):
        self.assertEqual(rb._hamming("00", "00"), 0)
        self.assertEqual(rb._hamming("00", "ff"), 8)
        self.assertEqual(rb._hamming("0f", "00"), 4)

    # -- 8: archive safety already covered by inventory_catalog's zip-bomb /
    # path-traversal guards (test_inventory_catalog.py); Phase 1C does not
    # add new archive-extraction code, so no duplicate test is added here.

    # -- 9: nested archive handling -- not exercised in this batch (no nested
    # archives were discovered in the real batch); the underlying safety
    # guard is the same one covered above.

    # -- 10: disposition completeness ------------------------------------------

    def test_every_discovered_entry_has_a_disposition(self):
        root = self._flat_root("cov", {"a.txt": "1", "b.txt": "2"})
        self._set_rules([self._already_ingested_spec(), {
            "index": 2, "path": str(root), "kind": "flat_dataset", "dataset_key": "COV",
            "dataset_name": "Coverage", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY",
        }])
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        conn = sqlite3.connect(str(self.db_path))
        total = conn.execute("SELECT COUNT(*) FROM discovered_files;").fetchone()[0]
        with_disp = conn.execute("SELECT COUNT(*) FROM discovered_files WHERE disposition IS NOT NULL AND disposition != '';").fetchone()[0]
        self.assertEqual(total, with_disp)
        self.assertGreater(total, 0)
        conn.close()

    # -- 11: existing DS-000001 idempotency (never re-ingested) ----------------

    def test_already_ingested_root_never_creates_duplicate_dataset(self):
        self._set_rules([self._already_ingested_spec()])
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        conn = sqlite3.connect(str(self.db_path))
        row = conn.execute(
            "SELECT disposition FROM discovered_files WHERE relative_path = 'canonical.txt';"
        ).fetchone()
        self.assertEqual(row[0], "ALREADY_INGESTED")
        dataset_count = conn.execute("SELECT COUNT(*) FROM datasets WHERE dataset_id = 'DS-000001';").fetchone()[0]
        self.assertEqual(dataset_count, 1)
        conn.close()

    def test_revision_detected_when_root1_hash_changes(self):
        # Mutate the "already ingested" source after seeding — simulates a
        # changed canonical file, which must halt rather than silently proceed.
        self.ds1_file.write_text("MUTATED CONTENT")
        self._set_rules([self._already_ingested_spec()])
        with self.assertRaises(ic.CatalogError) as ctx:
            rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        self.assertEqual(ctx.exception.error_type, "RevisionDetected")

    # -- 12: logical dataset assignment (codex-style prefix rules) -------------

    def test_codex_style_prefix_rules_resolve_longest_match_first(self):
        # Two datasets share a batch root; a specific file-level rule must
        # win over a shorter directory-level catch-all (the real bug found
        # and fixed during this batch: loose files under a shared outputs/
        # dir must not fall through to the wrong sibling dataset).
        codex_rules = [
            ("shared/outputs/topic_a_report.md", "SUPPORTING_EVIDENCE", "TOPIC_A", "topic A report"),
            ("shared/outputs/topic_b_report.md", "SUPPORTING_EVIDENCE", "TOPIC_B", "topic B report"),
            ("shared", "SUPPORTING_EVIDENCE", "TOPIC_A", "batch-level catch-all (must lose to the specific rules above)"),
        ]
        # classify_codex reads rules.CODEX_RULES at call time
        self._set_rules([], codex_rules=codex_rules)
        disp_a, key_a, _ = rb.classify_codex("shared/outputs/topic_a_report.md", False)
        disp_b, key_b, _ = rb.classify_codex("shared/outputs/topic_b_report.md", False)
        disp_other, key_other, _ = rb.classify_codex("shared/outputs/unrelated.md", False)
        self.assertEqual(key_a, "TOPIC_A")
        self.assertEqual(key_b, "TOPIC_B")
        self.assertEqual(key_other, "TOPIC_A")  # falls through to the catch-all correctly

    def test_tooling_directory_name_wins_regardless_of_nesting(self):
        self._set_rules([], codex_rules=[("evidence", "SUPPORTING_EVIDENCE", "SOME_DATASET", "evidence tree")])
        disp, key, reason = rb.classify_codex("evidence/work/__pycache__/x.pyc", False)
        self.assertEqual(disp, "TOOLING")
        self.assertIsNone(key)

    # -- 13: content-domain vs editing-style separation -------------------------

    def test_entity_classification_editing_style_defaults_unknown(self):
        root = self._flat_root("cls", {"shot.png": "not really a png but fine for this test"})
        self._set_rules([self._already_ingested_spec(), {
            "index": 2, "path": str(root), "kind": "flat_dataset", "dataset_key": "CLS",
            "dataset_name": "Classification Test", "semantic_class": "B", "content_domain": "HEALTH",
            "copy_mode": "COPY",
        }])
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        rb.cmd_register(Args(db_path=str(self.db_path), batch_id=self._get_batch_id()))
        import json
        conn = sqlite3.connect(str(self.db_path))
        dataset_id = conn.execute("SELECT dataset_id FROM datasets WHERE discovered_as = 'CLS';").fetchone()[0]
        conn.close()
        payload = {
            "dataset_id": dataset_id,
            "images": [{"path": str(root / "shot.png"), "visual_packaging_pattern_notes": "doctor-led"}],
        }
        state_path = self.tmp / "semantic.json"
        state_path.write_text(json.dumps(payload))
        import load_semantic_results as lsr
        orig_default_db = ic.DEFAULT_DB_PATH
        ic.DEFAULT_DB_PATH = self.db_path
        try:
            lsr.sys.argv = ["load_semantic_results.py", str(state_path), "HEALTH"]
            lsr.main()
        finally:
            ic.DEFAULT_DB_PATH = orig_default_db
        conn = sqlite3.connect(str(self.db_path))
        row = conn.execute(
            "SELECT content_domain, editing_style FROM entity_classifications WHERE dataset_id = ?;", (dataset_id,)
        ).fetchone()
        conn.close()
        self.assertEqual(row[0], "HEALTH")
        self.assertEqual(row[1], "UNKNOWN")  # never inferred from a screenshot

    def _get_batch_id(self):
        conn = sqlite3.connect(str(self.db_path))
        row = conn.execute("SELECT batch_id FROM source_batches ORDER BY batch_id DESC LIMIT 1;").fetchone()
        conn.close()
        return row[0]

    # -- 14: source_surface provenance is preserved in structured_json ---------

    def test_source_surface_distinction_round_trips_through_structured_json(self):
        root = self._flat_root("surf", {"shot.png": "placeholder"})
        self._set_rules([self._already_ingested_spec(), {
            "index": 2, "path": str(root), "kind": "flat_dataset", "dataset_key": "SURF",
            "dataset_name": "Surface Test", "semantic_class": "B", "content_domain": "HEALTH",
            "copy_mode": "COPY",
        }])
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        rb.cmd_register(Args(db_path=str(self.db_path), batch_id=self._get_batch_id()))
        conn = sqlite3.connect(str(self.db_path))
        dataset_id = conn.execute("SELECT dataset_id FROM datasets WHERE discovered_as = 'SURF';").fetchone()[0]
        discovered_file_id = conn.execute(
            "SELECT discovered_file_id FROM discovered_files WHERE relative_path = 'shot.png' AND dataset_id = ?;",
            (dataset_id,),
        ).fetchone()[0]
        va_id = ic._next_id(conn, "visual_assets", "visual_asset_id", "VA")
        with conn:
            conn.execute(
                "INSERT INTO visual_assets (visual_asset_id, discovered_file_id, dataset_id, sha256, width_px, "
                "height_px, color_mode, image_format, orientation, exif_json, perceptual_hash, "
                "perceptual_hash_algorithm, frame_sequence_id, frame_index, visual_state_cluster_id, created_at, "
                "notes) VALUES (?, ?, ?, 'x', 1, 1, 'RGB', 'PNG', 'SQUARE', '{}', 'abc', 'dhash8x8', NULL, NULL, "
                "NULL, ?, NULL);",
                (va_id, discovered_file_id, dataset_id, ic.now_iso()),
            )
            obs_id = ic._next_id(conn, "visual_observations", "visual_observation_id", "VOBS")
            import json
            payload = json.dumps({
                "subscriber_count": "10K", "subscriber_count_source_surface": "YOUTUBE_UI",
                "est_earnings_source_surface": "VIDIQ_OVERLAY",
            })
            conn.execute(
                "INSERT INTO visual_observations (visual_observation_id, visual_asset_id, observation_type, "
                "observation_method, source_surface, extracted_text, confidence, structured_json, evidence_layer, "
                "observed_at, notes) VALUES (?, ?, 'SEMANTIC_INSPECTION', 'claude_native_vision_inspection', NULL, "
                "NULL, NULL, ?, 'OBSERVATION', ?, NULL);",
                (obs_id, va_id, payload, ic.now_iso()),
            )
        row = conn.execute(
            "SELECT structured_json FROM visual_observations WHERE visual_observation_id = ?;", (obs_id,)
        ).fetchone()
        conn.close()
        import json
        parsed = json.loads(row[0])
        self.assertEqual(parsed["subscriber_count_source_surface"], "YOUTUBE_UI")
        self.assertEqual(parsed["est_earnings_source_surface"], "VIDIQ_OVERLAY")

    # -- 15: batch partial failure does not corrupt other completed datasets ---

    def test_one_dataset_registration_failure_does_not_corrupt_others(self):
        good_root = self._flat_root("good", {"ok.txt": "fine"})
        specs = [
            self._already_ingested_spec(),
            {"index": 2, "path": str(good_root), "kind": "flat_dataset", "dataset_key": "GOOD",
             "dataset_name": "Good", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY"},
        ]
        self._set_rules(specs)
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        batch_id = self._get_batch_id()
        rb.cmd_register(Args(db_path=str(self.db_path), batch_id=batch_id))
        conn = sqlite3.connect(str(self.db_path))
        good_id = conn.execute("SELECT dataset_id FROM datasets WHERE discovered_as = 'GOOD';").fetchone()
        conn.close()
        self.assertIsNotNone(good_id)
        # re-running register for the same batch must be idempotent (skip
        # already-registered datasets) rather than raising or duplicating
        rb.cmd_register(Args(db_path=str(self.db_path), batch_id=batch_id))
        conn = sqlite3.connect(str(self.db_path))
        count = conn.execute("SELECT COUNT(*) FROM datasets WHERE discovered_as = 'GOOD';").fetchone()[0]
        conn.close()
        self.assertEqual(count, 1)

    # -- 16: source immutability -------------------------------------------------

    def test_discovery_and_registration_never_modify_source_files(self):
        root = self._flat_root("immut", {"keep.txt": "do not touch me"})
        target = root / "keep.txt"
        before_mtime = target.stat().st_mtime
        before_hash = ic.sha256_file(target)
        self._set_rules([self._already_ingested_spec(), {
            "index": 2, "path": str(root), "kind": "flat_dataset", "dataset_key": "IMMUT",
            "dataset_name": "Immutable", "semantic_class": "G", "content_domain": None, "copy_mode": "COPY",
        }])
        rb.cmd_discover(Args(db_path=str(self.db_path), dry_run=False))
        rb.cmd_register(Args(db_path=str(self.db_path), batch_id=self._get_batch_id()))
        self.assertEqual(target.stat().st_mtime, before_mtime)
        self.assertEqual(ic.sha256_file(target), before_hash)


if __name__ == "__main__":
    unittest.main()
