"""Single source of truth for "what belongs in a v1.0.0 release".

Shared by validate_brain.py (strict enumeration + RELEASE_MANIFEST checks) and
build_release_manifest.py (RELEASE_MANIFEST.json generation), so the two can
never silently drift apart on what counts as canonical.
"""
import glob
import hashlib
import os

CANONICAL_DIR_PATTERNS = [
    ('01_master_data', '*.csv', 'master_data'),
    ('02_production_dna', '*.md', 'dna'),
    ('02_production_dna', '*.json', 'dna'),
    ('03_reconstruction_system', '*.md', 'reconstruction'),
    ('03_reconstruction_system', '*.json', 'reconstruction'),
    ('04_patterns', '*.csv', 'pattern'),
    ('05_blueprints', '*.md', 'blueprint'),
    ('validator', '*.py', 'validator'),
    ('validator', '*.md', 'validator'),
    ('validator/schemas', '*.json', 'schema'),
    ('testing', '*.md', 'testing_protocol'),
    ('testing', '*.json', 'testing_protocol'),
]

CANONICAL_ROOT_FILES = [
    ('SOURCE_VIDEO_INDEX.csv', 'source_index'),
    ('SOURCE_TO_FORENSIC_MAP.csv', 'source_index'),
    ('BRAIN_MANIFEST.json', 'manifest'),
    ('CANONICAL_PATHS.md', 'manifest'),
    ('BRAIN_SUMMARY.md', 'report'),
    ('VALIDATION_REPORT.md', 'report'),
    ('CONTINUATION_HANDOFF.md', 'report'),
    ('PACKAGE_AUDIT.md', 'report'),
    ('RELEASE_NOTES.md', 'report'),
]

# RELEASE_MANIFEST.json never lists itself -- avoids a recursive hash dependency.
EXCLUDED = {'RELEASE_MANIFEST.json'}


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def list_canonical_files(brain_root):
    """Returns (relative_path, category, size_bytes, sha256) for every canonical release file."""
    entries = []
    for rel_dir, pattern, category in CANONICAL_DIR_PATTERNS:
        abs_dir = os.path.join(brain_root, rel_dir)
        if not os.path.isdir(abs_dir):
            continue
        for path in sorted(glob.glob(os.path.join(abs_dir, pattern))):
            rel_path = os.path.relpath(path, brain_root).replace(os.sep, '/')
            if os.path.basename(rel_path) in EXCLUDED:
                continue
            entries.append((rel_path, category, os.path.getsize(path), sha256_of(path)))
    for fname, category in CANONICAL_ROOT_FILES:
        if fname in EXCLUDED:
            continue
        path = os.path.join(brain_root, fname)
        if os.path.exists(path):
            entries.append((fname, category, os.path.getsize(path), sha256_of(path)))
    return entries


def dir_listing_matches_patterns(brain_root, rel_dir):
    """Returns (unexpected_basenames) for files in rel_dir not matched by any of its patterns."""
    abs_dir = os.path.join(brain_root, rel_dir)
    if not os.path.isdir(abs_dir):
        return []
    patterns = [p for d, p, _ in CANONICAL_DIR_PATTERNS if d == rel_dir]
    matched = set()
    for pattern in patterns:
        for path in glob.glob(os.path.join(abs_dir, pattern)):
            matched.add(os.path.basename(path))
    actual = {n for n in os.listdir(abs_dir) if not n.startswith('.') and
              os.path.isfile(os.path.join(abs_dir, n))}
    return sorted(actual - matched)
