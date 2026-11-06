"""Executes the real validate.yml guard step against throwaway repos; no YAML dependency in the declared env."""
import subprocess
from pathlib import Path

import pytest

WORKFLOW = (Path(__file__).resolve().parents[1] / ".github/workflows/validate.yml").read_text(encoding="utf-8")
APPROVED = ["data/catalog/youtube_inventory.db", "data/catalog/youtube_channel_registry.db",
            "data/knowledge/reference_knowledge.db"]


def step_script(name):
    lines = WORKFLOW.splitlines()
    start = lines.index(f"      - name: {name}") + 2
    assert lines[start - 1].strip() == "run: |"
    body = []
    for line in lines[start:]:
        if line.strip() and not line.startswith("          "):
            break
        body.append(line[10:])
    return "\n".join(body)


def guard(tmp_path, tracked):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    for rel in tracked:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("x")
    subprocess.run(["git", "add", "-f", "."], cwd=tmp_path, check=True)
    script = step_script("Reject unapproved databases and generated junk")
    return subprocess.run(["bash", "-e", "-c", script], cwd=tmp_path, capture_output=True, text=True)


def test_approved_databases_pass(tmp_path):
    result = guard(tmp_path, APPROVED)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("junk", [
    "data/knowledge/other.db",
    "elsewhere/reference_knowledge.db",
    "data/knowledge/reference_knowledge.db-wal",
    "data/knowledge/reference_knowledge.db-shm",
    "data/catalog/youtube_inventory.db-wal",
    "data/catalog/youtube_inventory.db-shm",
    "outputs/generated.json",
    "scripts/cache.pyc",
])
def test_unapproved_files_fail(tmp_path, junk):
    assert guard(tmp_path, [*APPROVED, junk]).returncode != 0


def test_hosted_ci_runs_finance_reference_gates():
    script = step_script("Finance and reference framework gates")
    assert "reference_comparison.py check-all" in script
    assert "validate_audit_966.py" in script
    assert "reference-framework/test_reference_comparison.py" in script


def test_finance_gates_see_the_committed_registry():
    """validate_audit_966 pins the committed registry DB by SHA-256, so it must run before CI rebuilds that DB."""
    assert WORKFLOW.index("name: Finance and reference framework gates") < WORKFLOW.index("name: Build channel registry")


def test_visual_forensics_crosswalk_keeps_counts_separate():
    import collections
    import csv
    import sqlite3

    root = Path(__file__).resolve().parents[1]
    rows = list(csv.DictReader((root / "data/manifests/VISUAL_FORENSICS_REGISTRY_CROSSWALK.csv").open(encoding="utf-8")))
    assert len({r["video_id"] for r in rows}) == len(rows), "a video ID must not appear twice"
    registry = sqlite3.connect(f"file:{root}/data/catalog/youtube_channel_registry.db?mode=ro", uri=True)
    known = {v: c for v, c in registry.execute("SELECT youtube_video_id, canonical_channel_id FROM videos")}
    for row in rows:
        assert (row["video_id"] in known) == (row["in_registry"] == "true"), row["video_id"]
        assert known.get(row["video_id"], row["youtube_channel_id"]) == row["youtube_channel_id"], row["video_id"]
        assert len(row["source_commit"]) == 40
    xkcd = collections.Counter(r["in_registry"] for r in rows if r["youtube_channel_id"] == "UC6IxnFzHofFJ5X2PycSMsww")
    assert (xkcd["true"], xkcd["false"]) == (83, 8)
