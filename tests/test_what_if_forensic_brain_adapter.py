import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from source_adapters.what_if_forensic_brain import ContractError, TABLE_IDS, load_brain


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class AdapterTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.brain = self.root / "production_intelligence_brain"
        self.brain.mkdir()
        (self.root / "videos").mkdir()
        self.entries, source_rows, map_rows = [], [], []
        for number in range(1, 15):
            source_id = f"SRC{number:02}"
            filename = f"{source_id}.mp4"
            media = self.root / "videos" / filename
            media.write_bytes(source_id.encode())
            source_rows.append({"SOURCE_VIDEO_ID": source_id, "FILENAME": filename,
                                "FILE_SIZE_BYTES": str(media.stat().st_size),
                                "SHA256": digest(media)})
            map_rows.append({"SOURCE_VIDEO_ID": source_id, "SOURCE_FILENAME": filename,
                             "VIDEO_SLUG": f"slug_{source_id}"})
            self.entries.append({"source_video_id": source_id, "filename": filename,
                                 "forensic_slug": f"slug_{source_id}",
                                 "relative_media_path": f"videos/{filename}",
                                 "size_bytes": media.stat().st_size, "sha256": digest(media),
                                 "candidate_youtube_video_id": None,
                                 "canonical_youtube_video_id": None,
                                 "mapping_status": "UNRESOLVED", "mapping_evidence": []})
        for name, rows in [("SOURCE_VIDEO_INDEX.csv", source_rows),
                           ("SOURCE_TO_FORENSIC_MAP.csv", map_rows)]:
            with (self.brain / name).open("w", newline="") as stream:
                writer = csv.DictWriter(stream, rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
        (self.brain / "01_master_data").mkdir()
        self.release_files = []
        for table, local_id in TABLE_IDS.items():
            path = self.brain / "01_master_data" / f"{table}.csv"
            with path.open("w", newline="") as stream:
                writer = csv.DictWriter(stream, ["VIDEO_SLUG", local_id, "START_SEC"])
                writer.writeheader()
                writer.writerow({"VIDEO_SLUG": "slug_SRC01", local_id: "ROW1", "START_SEC": "0"})
            self.release_files.append({"relative_path": f"01_master_data/{table}.csv",
                                       "size_bytes": path.stat().st_size,
                                       "sha256": digest(path), "canonical": True})
        artifacts = {}
        for name in ["SOURCE_VIDEO_INDEX.csv", "SOURCE_TO_FORENSIC_MAP.csv"]:
            path = self.brain / name
            artifacts[name] = digest(path)
            self.release_files.append({"relative_path": name,
                                       "size_bytes": path.stat().st_size,
                                       "sha256": digest(path), "canonical": True})
        self.release = {"release_version": "1.0.0", "files": self.release_files}
        self.contract = {"source_release": "1.0.0",
                         "brain_relative_path": "production_intelligence_brain",
                         "source_artifact_sha256": artifacts, "sources": self.entries}
        self.contract_path = self.root / "contract.json"
        self.save()

    def save(self):
        release_path = self.brain / "RELEASE_MANIFEST.json"
        release_path.write_text(json.dumps(self.release))
        self.contract["release_manifest_sha256"] = digest(release_path)
        self.contract_path.write_text(json.dumps(self.contract))

    def test_reads_only_canonical_tables(self):
        legacy = self.brain / "legacy"
        legacy.mkdir()
        (legacy / "MASTER_WORDS.csv").write_text("bad,duplicate\n")
        before = digest(self.brain / "01_master_data" / "MASTER_WORDS.csv")
        result = load_brain(self.root, self.contract_path)
        self.assertEqual(set(result["tables"]), set(TABLE_IDS))
        self.assertTrue(all(len(rows) == 1 for rows in result["tables"].values()))
        self.assertEqual(before, digest(self.brain / "01_master_data" / "MASTER_WORDS.csv"))

    def test_changed_canonical_table_rejected(self):
        path = self.brain / "01_master_data" / "MASTER_WORDS.csv"
        path.write_text(path.read_text() + "untracked,row,0\n")
        with self.assertRaisesRegex(ContractError, "release table missing or changed"):
            load_brain(self.root, self.contract_path)

    def test_unknown_slug_rejected_even_when_release_hash_matches(self):
        path = self.brain / "01_master_data" / "MASTER_WORDS.csv"
        path.write_text(path.read_text().replace("slug_SRC01", "unknown_slug"))
        entry = next(x for x in self.release_files if x["relative_path"] == "01_master_data/MASTER_WORDS.csv")
        entry["sha256"], entry["size_bytes"] = digest(path), path.stat().st_size
        self.save()
        with self.assertRaisesRegex(ContractError, "unknown slug"):
            load_brain(self.root, self.contract_path)

    def test_missing_canonical_flag_rejected(self):
        entry = next(x for x in self.release_files if x["relative_path"] == "01_master_data/MASTER_WORDS.csv")
        entry["canonical"] = False
        self.save()
        with self.assertRaisesRegex(ContractError, "missing canonical release table"):
            load_brain(self.root, self.contract_path)


if __name__ == "__main__":
    unittest.main()
