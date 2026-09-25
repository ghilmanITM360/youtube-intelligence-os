#!/usr/bin/env python3
"""Read-only evidence check for the 23 pre-ledger legacy datasets (DS-000001
through DS-000019, DS-000029, DS-000031, DS-000032, DS-000033) — those
registered in the datasets table but predating the CSV-ledger format used by
validate_dataset_ledgers.py. Two older manifest formats exist:

  TABLE format (most datasets): a markdown table with a Relative Path,
  SHA-256 (sometimes truncated to a short prefix for readability) and
  Copied YES/NO column.

  BULLET format (DS-000001, DS-000017/018/019/029/031/032/033): a
  "### `filename`" heading per file followed by "- Canonical path:",
  "- Size:", "- SHA-256:" bullet lines, always with the full 64-char hash.

This script never writes anything. It locates each manifest-declared file on
disk by its recorded relative path (falling back to a same-directory-tree
filename search only if that exact path is absent, to tolerate the table
format's paths being relative to the original source root rather than the
repo) and compares its hash against the declared value. Rows the manifest
itself marks Copied=NO are expected to be absent from data/raw/ (disclosed
policy for large frame sequences) and are reported separately, not as
failures.

Usage: python3 scripts/validate_legacy_dataset_manifests.py [DS-000001 ...]
"""
import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFESTS_DIR = REPO_ROOT / "data" / "manifests"
RAW_DIR = REPO_ROOT / "data" / "raw"
REPO_MARKER = "youtube-intelligence-os/"

DEFAULT_DATASETS = [
    "DS-000001", "DS-000002", "DS-000003", "DS-000004", "DS-000005",
    "DS-000006", "DS-000007", "DS-000008", "DS-000009", "DS-000010",
    "DS-000011", "DS-000012", "DS-000013", "DS-000014", "DS-000015",
    "DS-000016", "DS-000017", "DS-000018", "DS-000019", "DS-000029",
    "DS-000031", "DS-000032", "DS-000033",
]

TABLE_ROW_RE = re.compile(
    r"^\|\s*`(?P<path>[^`]+)`\s*\|[^|]*\|\s*`(?P<hash>[a-f0-9]{6,64})(?P<trunc>…)?`\s*\|\s*(?P<copied>YES|NO)?\s*\|?"
)
# DS-000019's variant column order: | Role | Bytes | SHA-256 | Original path | Canonical path |
TABLE_ROW_RE_CANONICAL_LAST = re.compile(
    r"^\|[^|]*\|[^|]*\|\s*`(?P<hash>[a-f0-9]{64})`\s*\|[^|]*\|\s*`(?P<path>[^`]+)`\s*\|"
)
BULLET_BLOCK_RE = re.compile(
    r"- Canonical path: `(?P<path>[^`]+)`\n"
    r"(?:- [^\n]*\n){0,3}?"
    r"- SHA-256: `(?P<hash>[a-f0-9]{64})`"
)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def to_repo_relative(canonical_path):
    if canonical_path.startswith("data/"):
        return canonical_path
    idx = canonical_path.find(REPO_MARKER)
    if idx == -1:
        return None
    return canonical_path[idx + len(REPO_MARKER):]


def parse_manifest_rows(dataset_id):
    """Yields (relative_path, declared_hash, is_truncated, copied) per file row.
    copied is True/False from the table's Copied column, or None (bullet
    format / no such column — file is expected present)."""
    fp = MANIFESTS_DIR / "{}.md".format(dataset_id)
    if not fp.exists():
        return
    text = fp.read_text(encoding="utf-8")

    found_table = False
    for line in text.splitlines():
        m = TABLE_ROW_RE.match(line.strip())
        if not m:
            continue
        found_table = True
        copied = {"YES": True, "NO": False, None: None}[m.group("copied")]
        yield m.group("path"), m.group("hash"), bool(m.group("trunc")), copied

    if found_table:
        return

    for line in text.splitlines():
        m = TABLE_ROW_RE_CANONICAL_LAST.match(line.strip())
        if not m:
            continue
        found_table = True
        relpath = to_repo_relative(m.group("path"))
        if relpath is None:
            continue
        yield relpath, m.group("hash"), False, None

    if found_table:
        return

    for m in BULLET_BLOCK_RE.finditer(text):
        relpath = to_repo_relative(m.group("path"))
        if relpath is None:
            continue
        yield relpath, m.group("hash"), False, None


def find_dataset_dir(dataset_id):
    matches = [p for p in RAW_DIR.glob("*/{}".format(dataset_id)) if p.is_dir()]
    return matches[0] if matches else None


def locate_file(dataset_dir, relpath, root):
    """Table-format rows record a path relative to the dataset's own
    directory; bullet-format rows are already repo-relative. Try both exact
    joins before falling back to a same-dataset filename search (only used
    when it resolves to exactly one file, to avoid same-named files in
    different subdirectories silently picking the wrong one)."""
    if dataset_dir is not None:
        candidate = dataset_dir / relpath
        if candidate.exists():
            return candidate
    candidate = root / relpath
    if candidate.exists():
        return candidate
    if dataset_dir is None:
        return None
    matches = list(dataset_dir.rglob(Path(relpath).name))
    return matches[0] if len(matches) == 1 else None


def validate_dataset(dataset_id, root=REPO_ROOT):
    """Returns a list of (filename, status) for every parsed manifest row."""
    results = []
    dataset_dir = find_dataset_dir(dataset_id)
    for relpath, declared_hash, truncated, copied in parse_manifest_rows(dataset_id):
        filename = Path(relpath).name
        found = locate_file(dataset_dir, relpath, root)
        if found is None:
            if copied is False:
                results.append((filename, "NOT_COPIED_BY_POLICY"))
            else:
                results.append((filename, "MISSING_ON_DISK"))
            continue
        actual_hash = sha256_file(found)
        if truncated:
            ok = actual_hash.startswith(declared_hash)
        else:
            ok = actual_hash == declared_hash
        results.append((filename, "OK" if ok else "HASH_MISMATCH"))
    return results


def main(argv):
    datasets = argv[1:] or DEFAULT_DATASETS
    total_bad = 0
    for dataset_id in datasets:
        rows = validate_dataset(dataset_id)
        policy = [r for r in rows if r[1] == "NOT_COPIED_BY_POLICY"]
        bad = [r for r in rows if r[1] not in ("OK", "NOT_COPIED_BY_POLICY")]
        total_bad += len(bad)
        if not rows:
            print("{}: no parseable manifest rows found".format(dataset_id))
        elif bad:
            print("{}: {}/{} row(s) failed ({} not-copied-by-policy)".format(
                dataset_id, len(bad), len(rows), len(policy)))
            for filename, status in bad:
                print("  {}: {}".format(filename, status))
        else:
            print("{}: clean ({} files verified, {} not-copied-by-policy)".format(
                dataset_id, len(rows) - len(policy), len(policy)))
    return 1 if total_bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
