from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent.parent
REPORT = PROJECT / "outputs" / "Weird_and_worrying_questions_forensic_blueprint.md"


class ReportContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = REPORT.read_text() if REPORT.exists() else ""
        with (ROOT / "state_manifest.tsv").open() as handle:
            cls.states = list(csv.DictReader(handle, delimiter="\t"))
        with (ROOT / "motion_manifest.tsv").open() as handle:
            cls.events = list(csv.DictReader(handle, delimiter="\t"))

    def test_every_manifest_state_has_one_ordered_28_section_card(self):
        """Catches an omitted/duplicate card or any missing numbered reconstruction section."""
        starts = list(re.finditer(r"^## (V\d{2}) — ", self.text, re.MULTILINE))
        self.assertEqual([match.group(1) for match in starts], [row["visual"] for row in self.states])
        for index, match in enumerate(starts):
            end = starts[index + 1].start() if index + 1 < len(starts) else len(self.text)
            card = self.text[match.start() : end]
            headings = [int(value) for value in re.findall(r"^### (\d+)\. ", card, re.MULTILINE)]
            self.assertEqual(headings, list(range(1, 29)), match.group(1))

    def test_every_event_is_rendered_once_with_valid_state_links(self):
        """Catches missing animation cards, duplicate IDs, or a transition wired to the wrong state."""
        rendered_ids = re.findall(r"^#### ANIMATION (A\d{2})$", self.text, re.MULTILINE)
        expected_ids = [row["animation"] for row in self.events]
        self.assertEqual(rendered_ids, expected_ids)
        state_ids = {row["visual"] for row in self.states}
        for event in self.events:
            self.assertIn(event["source"].split("/")[0], state_ids)
            self.assertIn(event["target"].split("/")[0], state_ids)

    def test_animation_prompt_counts_are_exact_and_under_ceiling(self):
        """Catches stale printed counts, omitted status, or a prompt over the 500-character limit."""
        blocks = re.split(r"^#### ANIMATION ", self.text, flags=re.MULTILINE)[1:]
        self.assertEqual(len(blocks), len(self.events))
        for block in blocks:
            animation = block[:3]
            prompt_match = re.search(r'\*\*AI PROMPT:\*\* “(.+?)”  \n\*\*CHARACTER COUNT:\*\* (\d+) / 500  \n\*\*STATUS:\*\* (PASS|FAIL)', block)
            self.assertIsNotNone(prompt_match, animation)
            prompt, printed, status = prompt_match.groups()
            self.assertEqual(int(printed), len(prompt), animation)
            self.assertLessEqual(len(prompt), 500, animation)
            self.assertEqual(status, "PASS", animation)

    def test_each_card_has_standalone_prompt_text_decision_and_source_image(self):
        """Catches incomplete image packages that would force a recreator to guess."""
        self.assertEqual(self.text.count("**STANDALONE IMAGE PROMPT:**"), len(self.states))
        self.assertEqual(self.text.count("**BAKE TEXT:** NO"), len(self.states))
        self.assertEqual(self.text.count("**SOURCE REFERENCE:** [Open full-resolution frame]"), len(self.states))

    def test_keyframe_links_resolve_to_720_by_1280_images(self):
        """Catches a broken source-evidence link, corrupt frame, or wrong orientation."""
        from PIL import Image

        keyframes = sorted((PROJECT / "outputs" / "weird_worrying_forensics" / "keyframes").glob("V*.jpg"))
        self.assertEqual(len(keyframes), len(self.states))
        for path in keyframes:
            with Image.open(path) as image:
                self.assertEqual(image.size, (720, 1280), path.name)
            relative = f"weird_worrying_forensics/keyframes/{path.name}"
            self.assertIn(relative, self.text)

    def test_master_sections_and_completeness_totals_exist(self):
        """Catches delivery of cards without the required script/edit/audio/synthesis systems."""
        required = [
            "# Engine A — Script Intelligence",
            "# Engine B — Visual Intelligence",
            "# Engine C — Reconstruction and Motion Intelligence",
            "# Editing Decision List",
            "# Audio Intelligence",
            "# Thumbnail and Shorts Extraction",
            "# Engine D — Master Production Synthesis",
            "# Zero-to-Final Rebuild Order",
            "# Completeness Audit",
            "# Final Quality Gate",
        ]
        for heading in required:
            self.assertIn(heading, self.text)
        self.assertIn("VISUAL CARDS: 34/34", self.text)
        self.assertIn("TOTAL MOTION EVENTS: 39", self.text)
        self.assertIn("AI PROMPTS ≤500: 39/39", self.text)

    def test_no_unresolved_markers_remain(self):
        """Catches unfinished data leaking into the user-facing blueprint."""
        for marker in ("TO" + "DO", "T" + "BD", "PLACE" + "HOLDER", "FILL" + " ME"):
            self.assertNotIn(marker, self.text.upper())


if __name__ == "__main__":
    unittest.main()
