# Phase 1 validation

Validation date: 2026-10-15. The final command outputs and exact commit/CI state are recorded in the draft PR handoff.

- Local preservation: the read-only catalog checker rehashes all 2,732 indexed local files against their discovery hashes, including raw documents, archives and both databases. It does not claim a full hash census of excluded media/frame dumps.
- Historical preservation: 606 physical source paths shared with the original inventory database were compared with its registered SHA256 values; zero mismatches.
- Git recovery: 2,819 distinct Git blobs underlying 3,073 indexed branch path/versions resolve. Six are explicitly identified LFS pointers, not verified historical database payloads.
- Exact duplicates: references resolve to equal-hash root records. Original/canonical raw sources are preferred as duplicate-group anchors. Semantic families are separately documented.
- Hook semantic duplicate: both PDFs yielded 77,308 characters with pypdf; full pdftotext output comparison additionally verifies equality. No originals were rewritten.
- Link checks: local Markdown links are checked by `validate_knowledge.py`. Official URLs were fetched on the check date; cloud discovery-only sources are explicitly unreviewed.
- Counts: canonical registry and finance video/transcript totals were queried read-only. Placeholder transcripts are excluded. Research overlays are not added to canonical counts.
- Scope: only `knowledge/youtube/`, `research/finance-economics-intelligence/` and `docs/research/README.md` are intended for staging. No canonical data, media, agent instructions or existing PR content is changed.
- Secrets: repository `scripts/scan_tracked_secrets.py` scans staged/tracked text for its configured credential patterns. This is a bounded pattern scan, not a guarantee against every possible secret representation.
- Whitespace: `git diff --cached --check` must pass before committing.

This documentation/index change does not alter the production engine. Local full-suite execution is unnecessary for its scope; GitHub's repository validation workflow is reported separately, without claiming a pass before it completes.
