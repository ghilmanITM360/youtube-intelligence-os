import hashlib
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
EXPORT_DIR = ROOT / "exports/2026-09-27-master-knowledge-and-senior-health-export"
SCRIPT = EXPORT_DIR / "scripts/build_supplemental_archive.py"

pytestmark = pytest.mark.skipif(not SCRIPT.exists(), reason="local export folder not present")


def _module():
    spec = importlib.util.spec_from_file_location("supp_archive", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _tree(path):
    return sorted(str(p.relative_to(path)) for p in path.rglob("*"))


def test_builder_leaves_no_loose_files_and_is_reproducible(tmp_path):
    m = _module()
    before = _tree(EXPORT_DIR)
    a, b = tmp_path / "a.zip", tmp_path / "b.zip"
    m.build(a)
    m.build(b)
    assert _tree(EXPORT_DIR) == before
    assert hashlib.sha256(a.read_bytes()).digest() == hashlib.sha256(b.read_bytes()).digest()


def test_builder_refuses_to_overwrite(tmp_path):
    m = _module()
    existing = tmp_path / "keep.zip"
    existing.write_bytes(b"user data")
    with pytest.raises(FileExistsError):
        m.build(existing)
    assert existing.read_bytes() == b"user data"
