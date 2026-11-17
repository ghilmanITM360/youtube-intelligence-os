"""Focused offline regressions; fixtures never write real research outputs."""
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import wave
from pathlib import Path

PIPELINE = Path(__file__).resolve().parent

class VideoHelpersTest(unittest.TestCase):
    def test_two_video_ids_and_single_offset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scratch = root / "scratch"
            manifest = root / "docs/research/finance/casual-economics"
            manifest.mkdir(parents=True)
            captions = root / "data/extracted/channel-data/DS-000036/captions"
            captions.mkdir(parents=True)
            files = []
            for vid, offset, count in [("kbPauzdHhcI", .016667, 2), ("N9GUfsfiM4M", .041708, 3)]:
                work = scratch / vid
                (work / "sheets").mkdir(parents=True)
                states = [{"state_id": f"S001.{i}", "shot_id": "S001", "start": i*.2, "end": (i+1)*.2, "dur": .2, "rep_t": i*.2+.1} for i in range(count)]
                (work / "visual_auto.json").write_text(json.dumps({"video_id": vid, "fps": 24, "frames": 24, "states": states, "shots": [{"shot_id": "S001", "start": 0, "end": count*.2, "transition_in": "START", "transition_ep": ""}], "episodes": [{"ep_id": "E0001", "t0": .1, "t1": .2, "cls": "CHANGE", "peak_frac": .2, "bbox_area": .3}]}))
                (work / "DECODE_VALIDATION.json").write_text(json.dumps({"video_id": vid, "native_pts_frames": 24, "first_pts": offset, "last_pts": .95, "timestamp_offset_applied_to_candidate_tables": False}))
                (work / "sheets/sheet_001.jpg").write_bytes(b"fixture image locator")
                text = "".join(f"{vid} frame {i}|PERSON_presenter|OBSERVED representative frame\n" for i in range(count))
                subprocess.run([sys.executable, str(PIPELINE / "save_review.py"), vid, "1", str(scratch)], input=text, text=True, check=True, capture_output=True)
                ann = json.loads((work / "visual_review.json").read_text())
                self.assertEqual(len(ann), count)
                self.assertTrue(all(vid in a["description"] for a in ann.values()))
                with wave.open(str(work / "audio22k.wav"), "wb") as wav:
                    wav.setparams((1, 2, 22050, 0, "NONE", "not compressed"))
                    wav.writeframes(b"\0\0"*22050)
                srt = b"1\n00:00:0,080 --> 00:00:0,800\nA source caption.\n"
                (captions / (vid+".srt")).write_bytes(srt)
                files.append({"video_id": vid, "sha256": "a"*64, "duration_sec": 1, "channel_id": "channel", "source_locator": "fixture.mp4"})
            (manifest / "LOCAL_SOURCE_MANIFEST.json").write_text(json.dumps({"files": files}))
            for row, offset in zip(files, [.016667, .041708]):
                vid = row["video_id"]
                output = root / "output"
                cmd = [sys.executable, str(PIPELINE / "build_economics_video.py"), vid, str(root), str(scratch), str(output)]
                subprocess.run(cmd, check=True, capture_output=True)
                d = output / "02_VIDEO_FORENSICS" / vid
                with (d / "STATES.csv").open() as f:
                    states = list(csv.DictReader(f))
                self.assertTrue(all(s["video_id"] == vid for s in states))
                self.assertAlmostEqual(float(states[0]["start_sec"]), offset)
                self.assertEqual(float(states[0]["representative_source_seek_sec"]), .1)
                before = hashlib.sha256((d / "STATES.csv").read_bytes()).hexdigest()
                subprocess.run(cmd, check=True, capture_output=True)
                self.assertEqual(before, hashlib.sha256((d / "STATES.csv").read_bytes()).hexdigest())
                ptsfile = scratch / vid / "DECODE_VALIDATION.json"
                pts = json.loads(ptsfile.read_text())
                pts["timestamp_offset_applied_to_candidate_tables"] = True
                ptsfile.write_text(json.dumps(pts))
                self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)

if __name__ == "__main__":
    unittest.main()
