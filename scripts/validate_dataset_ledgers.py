#!/usr/bin/env python3
"""Checksum-ledger provenance validation for the DS-000021..DS-000025 funded
extraction batches (docs/audits/REPOSITORY_AUDIT_2026-09-14.md defect log).

Each dataset's data/manifests/DS-0000NN_FILES.csv row records a
repository_relative_path plus size_bytes/sha256 captured at packaging time.
Two kinds of row exist:

  RAW artifact evidence (immutable) — never edited after ingestion; the
  ledger hash must still match the current bytes on disk.

  Mutable code/document snapshots (a packaging script, a test file, a docs
  page) that legitimately keep changing after the dataset was packaged. Their
  ledger hash is a point-in-time snapshot, not a live invariant — it must
  instead match the Git blob at the commit recorded in KNOWN_HISTORICAL_SNAPSHOTS
  below (the commit was located by walking `git log` for the path and hashing
  each historical blob until one reconciled; see docs/audits/
  REPOSITORY_AUDIT_2026-09-14.md and the 2026-09-15 provenance fix for the
  verification basis).

Usage: python3 scripts/validate_dataset_ledgers.py [DS-000021 ...]
"""
import csv
import hashlib
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFESTS_DIR = REPO_ROOT / "data" / "manifests"

DEFAULT_DATASETS = [
    "DS-000020", "DS-000021", "DS-000022", "DS-000023", "DS-000024",
    "DS-000025", "DS-000027", "DS-000028", "DS-000030",
]

# (dataset_id, artifact_id) -> git commit whose blob content reconciles with
# the ledger's recorded sha256/size_bytes for that mutable snapshot. Located
# by walking `git log --all -- <path>` newest-first and hashing each blob;
# do not add an entry here without doing the same and recording the commit
# that actually matched.
KNOWN_HISTORICAL_SNAPSHOTS = {
    ("DS-000021", "DS-000021-F034"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000021", "DS-000021-F035"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000021", "DS-000021-F037"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000021", "DS-000021-F038"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000022", "DS-000022-F032"): "b138af0e8e216f897e0bb9a96021a153b5967a72",
    ("DS-000022", "DS-000022-F033"): "b138af0e8e216f897e0bb9a96021a153b5967a72",
    ("DS-000022", "DS-000022-F034"): "a6223dca62007cd8f6c23d8ec16bf0b158abec34",
    ("DS-000023", "DS-000023-F022"): "4fbdd57fd1975709a843ad9234ad27a080bbdb47",
    ("DS-000023", "DS-000023-F023"): "4fbdd57fd1975709a843ad9234ad27a080bbdb47",
    ("DS-000023", "DS-000023-F025"): "4fbdd57fd1975709a843ad9234ad27a080bbdb47",
    ("DS-000024", "DS-000024-F020"): "4fbdd57fd1975709a843ad9234ad27a080bbdb47",
    ("DS-000024", "DS-000024-F021"): "4fbdd57fd1975709a843ad9234ad27a080bbdb47",
    ("DS-000024", "DS-000024-F023"): "57491326ec76c7763c9da7b0affcc473a962b7e7",
    ("DS-000021", "DS-000021-F039"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000022", "DS-000022-F035"): "b138af0e8e216f897e0bb9a96021a153b5967a72",
    ("DS-000023", "DS-000023-F026"): "b138af0e8e216f897e0bb9a96021a153b5967a72",
    ("DS-000023", "DS-000023-F027"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000024", "DS-000024-F024"): "b138af0e8e216f897e0bb9a96021a153b5967a72",
    ("DS-000024", "DS-000024-F025"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000025", "DS-000025-F023"): "b138af0e8e216f897e0bb9a96021a153b5967a72",
    ("DS-000025", "DS-000025-F024"): "78ad5d728380873d67422d71e67f613ff28c37cf",
    ("DS-000025", "DS-000025-F022"): "57491326ec76c7763c9da7b0affcc473a962b7e7",
    ("DS-000027", "DS-000027-F018"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000027", "DS-000027-F017"): "57491326ec76c7763c9da7b0affcc473a962b7e7",
    ("DS-000027", "DS-000027-F019"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000027", "DS-000027-F027"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000027", "DS-000027-F028"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000027", "DS-000027-F030"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000027", "DS-000027-F031"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000027", "DS-000027-F029"): "25110136c61ac0cc8bb124a1cacd3aa5fae8a840",
    ("DS-000028", "DS-000028-F018"): "57491326ec76c7763c9da7b0affcc473a962b7e7",
    ("DS-000028", "DS-000028-F019"): "59cf21851b5f6e57975ab51944b7572a3edf7471",
    ("DS-000030", "DS-000030-F017"): "57491326ec76c7763c9da7b0affcc473a962b7e7",
    ("DS-000030", "DS-000030-F018"): "c740f89212dd7a1c59c273fce07e2613f24a68c4",
    # .gitattributes is shared mutable repo configuration; the ledgers captured
    # the 627-byte blob introduced at 59cf2185 (2026-09-22). Later commits
    # (71bb5946, c5c3d60e, b28f0484) legitimately extended it.
    ("DS-000028", "DS-000028-F020"): "59cf21851b5f6e57975ab51944b7572a3edf7471",
    ("DS-000030", "DS-000030-F019"): "59cf21851b5f6e57975ab51944b7572a3edf7471",
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_git_blob(commit, relpath, root=REPO_ROOT):
    """None if the path did not exist in that commit."""
    proc = subprocess.run(
        ["git", "show", "{}:{}".format(commit, relpath)],
        capture_output=True, cwd=root,
    )
    if proc.returncode != 0:
        return None
    return hashlib.sha256(proc.stdout).hexdigest()


def has_duplicate_segment(relpath):
    """Rejects a repeated single segment (a/a/b) or a repeated two-segment
    pair anywhere in the path (apify/<RUN_ID>/.../apify/<RUN_ID>) — the exact
    shape of the DS-000023 defect."""
    segments = relpath.split("/")
    for i in range(len(segments) - 1):
        if segments[i] == segments[i + 1]:
            return True
    for i in range(len(segments) - 1):
        pair = segments[i:i + 2]
        for j in range(i + 2, len(segments) - 1):
            if segments[j:j + 2] == pair:
                return True
    return False


def resolves_within_repo(relpath, root=REPO_ROOT):
    if Path(relpath).is_absolute():
        return False
    if ".." in Path(relpath).parts:
        return False
    try:
        (root / relpath).resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def validate_row(dataset_id, row, root=REPO_ROOT):
    """Returns a list of issue strings for one ledger row; empty means clean."""
    issues = []
    relpath = row["repository_relative_path"]

    if not resolves_within_repo(relpath, root):
        issues.append("PATH_ESCAPES_REPO")
        return issues  # unsafe to stat/open further
    if has_duplicate_segment(relpath):
        issues.append("DUPLICATE_PATH_SEGMENT")

    declared_sha = row["sha256"]
    declared_size = int(row["size_bytes"]) if row.get("size_bytes") else None
    pin = KNOWN_HISTORICAL_SNAPSHOTS.get((dataset_id, row["artifact_id"]))

    if pin:
        blob_sha = sha256_git_blob(pin, relpath, root)
        if blob_sha is None:
            issues.append("HISTORICAL_COMMIT_MISSING_PATH({})".format(pin))
        elif blob_sha != declared_sha:
            issues.append("HISTORICAL_BLOB_SHA_MISMATCH")
        return issues

    full = root / relpath
    if not full.exists():
        issues.append("FILE_MISSING")
        return issues
    if declared_size is not None and full.stat().st_size != declared_size:
        issues.append("SIZE_MISMATCH")
    if declared_sha and sha256_file(full) != declared_sha:
        issues.append("SHA_MISMATCH")
    return issues


def load_ledger_rows(dataset_id, root=REPO_ROOT):
    fp = root / "data" / "manifests" / "{}_FILES.csv".format(dataset_id)
    with open(fp, newline="") as f:
        return list(csv.DictReader(f))


def validate_dataset(dataset_id, root=REPO_ROOT):
    """Returns {artifact_id: [issues]} for every row with at least one issue."""
    problems = {}
    for row in load_ledger_rows(dataset_id, root):
        issues = validate_row(dataset_id, row, root)
        if issues:
            problems[row["artifact_id"]] = issues
    return problems


def main(argv):
    datasets = argv[1:] or DEFAULT_DATASETS
    total_issues = 0
    for dataset_id in datasets:
        problems = validate_dataset(dataset_id)
        total_issues += len(problems)
        if problems:
            print("{}: {} row(s) with issues".format(dataset_id, len(problems)))
            for artifact_id, issues in problems.items():
                print("  {}: {}".format(artifact_id, issues))
        else:
            print("{}: clean".format(dataset_id))
    return 1 if total_issues else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
