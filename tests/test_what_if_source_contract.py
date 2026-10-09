"""Offline contract checks; no external corpus or network required."""
import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_what_if_source_contract import ContractError, validate


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SourceContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        brain = self.root / "production_intelligence_brain"
        videos = self.root / "videos"
        brain.mkdir()
        videos.mkdir()
        index, mapping, entries = [], [], []
        for n in range(1, 15):
            sid = f"SRC{n:02}"
            filename = f"{sid}.mp4"
            media = videos / filename
            media.write_bytes(sid.encode())
            index.append({"SOURCE_VIDEO_ID": sid, "FILENAME": filename,
                          "FILE_SIZE_BYTES": str(media.stat().st_size),
                          "SHA256": digest(media)})
            mapping.append({"SOURCE_VIDEO_ID": sid, "SOURCE_FILENAME": filename,
                            "VIDEO_SLUG": f"slug_{sid}"})
            verified = n <= 10
            candidate = f"VIDEO{n:06}" if verified else None
            entries.append({"source_video_id": sid, "filename": filename,
                            "forensic_slug": f"slug_{sid}",
                            "relative_media_path": f"videos/{filename}",
                            "size_bytes": media.stat().st_size, "sha256": digest(media),
                            "candidate_youtube_video_id": candidate,
                            "canonical_youtube_video_id": candidate,
                            "mapping_status": "VERIFIED" if verified else "UNRESOLVED",
                            "mapping_evidence": ["catalog"] if verified else []})
        for name, rows in [("SOURCE_VIDEO_INDEX.csv", index),
                           ("SOURCE_TO_FORENSIC_MAP.csv", mapping)]:
            with (brain / name).open("w", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
        artifacts = {name: digest(brain / name) for name in
                     ["SOURCE_VIDEO_INDEX.csv", "SOURCE_TO_FORENSIC_MAP.csv"]}
        release = {"release_version": "1.0.0", "files": [
            {"relative_path": name, "sha256": sha} for name, sha in artifacts.items()]}
        (brain / "RELEASE_MANIFEST.json").write_text(json.dumps(release))
        self.contract = {"source_release": "1.0.0",
                         "brain_relative_path": "production_intelligence_brain",
                         "release_manifest_sha256": digest(brain / "RELEASE_MANIFEST.json"),
                         "source_artifact_sha256": artifacts, "sources": entries}
        self.contract_path = self.root / "contract.json"
        self.save()

    def save(self):
        self.contract_path.write_text(json.dumps(self.contract))

    def test_complete_contract_and_unresolved_are_not_promoted(self):
        result = validate(self.contract_path, self.root)
        self.assertEqual(result["sources"], 14)
        self.assertEqual(result["verified"], 10)
        self.assertEqual(result["unresolved"], 4)
        self.assertIsNone(self.contract["sources"][-1]["canonical_youtube_video_id"])

    def test_hash_mismatch_fails(self):
        (self.root / "videos/SRC01.mp4").write_bytes(b"changed")
        with self.assertRaisesRegex(ContractError, "media hash or size mismatch"):
            validate(self.contract_path, self.root)

    def test_missing_file_fails(self):
        (self.root / "videos/SRC01.mp4").unlink()
        with self.assertRaisesRegex(ContractError, "missing media"):
            validate(self.contract_path, self.root)

    def test_duplicate_source_id_fails(self):
        self.contract["sources"][1]["source_video_id"] = "SRC01"
        self.save()
        with self.assertRaisesRegex(ContractError, "duplicate source_video_id"):
            validate(self.contract_path, self.root)

    def test_duplicate_canonical_assignment_fails(self):
        self.contract["sources"][1]["canonical_youtube_video_id"] = "VIDEO000001"
        self.contract["sources"][1]["candidate_youtube_video_id"] = "VIDEO000001"
        self.save()
        with self.assertRaisesRegex(ContractError, "duplicate canonical assignment"):
            validate(self.contract_path, self.root)

    def test_unresolved_cannot_have_canonical_id(self):
        self.contract["sources"][-1]["canonical_youtube_video_id"] = "VIDEO999999"
        self.save()
        with self.assertRaisesRegex(ContractError, "unverified source"):
            validate(self.contract_path, self.root)


if __name__ == "__main__":
    unittest.main()
