# YIOS-local-audits index (2026-11-14)

Index only. The files themselves stay in `~/YIOS-local-audits` (Machine A, durable local storage) and are not copied into the repo.

- `MANIFEST.csv.gz`: one row per file (101,971 files, 18,144,766,274 bytes): `relative_path` (relative to `~/YIOS-local-audits`), `bytes`, `mtime_epoch`, `sha256`. Symlinks skipped; 0 unreadable files.
- `SUMMARY.csv`: files and bytes per top-level entry.

Observed facts: hashes were computed on 2026-11-14 from the folder as it was then; the folder was not modified.
Comparison finding (same date): almost none of these files exist, by SHA-256, in this repo or its two sibling worktrees (`yios-audit-fixes`, `yios-finance-machine-a`), so the folder is the only copy of this evidence on Machine A.

Limits: Machine B contents were not checked. Frames/media are not in git by policy. Not committed.
