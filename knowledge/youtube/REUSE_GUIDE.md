# Reuse guide

For finance, health, history or another niche, start at [preflight](RESEARCH_PREFLIGHT.md). Choose the topic documents in the [master index](MASTER_INDEX.md), then locate original sources in the CSV catalogs. Save only missing evidence or new analysis; reference the existing corpus.

Use `SOURCE_CATALOG.csv` for physical SHA256 identity and exact paths. `Duplicate_Of` points to another catalog row with identical bytes. Different hashes do not imply semantic independence. `BRANCH_SOURCE_INDEX.csv` uses immutable commits and Git blobs; branch names are discovery hints only. Access a Git source with `git show <Commit>:<Path>` without switching or merging another research branch. LFS pointer blobs require the corresponding LFS object; pointers do not certify media availability.

For another computer: Git-tracked paths require the repository and any relevant LFS objects; local-only absolute paths need a verified backup/copy. Drive sources require account access. Neither a filename nor an old manifest proves that the bytes exist on Laptop A/B.

Resume from [HANDOFF.md](HANDOFF.md). Revalidate only selected inputs that changed; do not rerun full corpus discovery by default. Keep this branch and draft PR for the next phase.
