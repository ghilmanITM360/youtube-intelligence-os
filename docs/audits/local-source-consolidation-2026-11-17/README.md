# Local source folder consolidation audit (2026-11-17)

Per-file SHA-256 manifest of 11 local source folders (~27 GB, 145,544 entries) taken before any cleanup.
Manifest: `manifest_classified.tsv.gz` (SHA-256 `c512f22d557d3c6181316161fa1fd330fad404aa8f395831b9d74626e7f88e52`). Builder: `hash_sources.py` (symlinks recorded, never followed).

Columns: source, absolute path, type, size, sha256 (or symlink target), git blob sha1, classification.

Classes: A = git blob id present in a remote ref (byte readback NOT yet done); C = content not in any ref, NOT durably preserved;
D = venv/site-packages/pycache/.DS_Store (reproducible); E = symlink (target recorded only).

Totals: A 14,860 files / 1.8 GB; C 80,357 / 25.0 GB; D 50,154 / 2.1 GB; E 173.

Status: nothing deleted. Class C has no verified durable remote copy. Recover by locating the original absolute path and comparing sha256.
