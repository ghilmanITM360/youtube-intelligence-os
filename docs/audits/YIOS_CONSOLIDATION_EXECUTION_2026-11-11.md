# YIOS Consolidation Execution — 2026-11-11

Written for: the owner and later Claude/Codex sessions. Source audit: `YIOS_SELECTED_FOLDERS_RECONCILIATION_2026-11-11.md`.

## Result in numbers
- **922 local-only files integrated, 4,226,627,186 bytes (4.23 GB), every SHA-256 verified source vs destination, 0 mismatches.**
  - 795 raw files (4.222 GB) cloned (APFS `cp -c`, zero extra disk) into the canonical checkout, git-ignored: 439+1 source MP4s + 355 preserved worktree evidence files (distinct hashes of the 321 unique + internal duplicates).
  - 127 files (4.3 MB) committed: Creator audit (102) and Algorithm audit (25), labelled HISTORICAL_CONTEXT.
- Already in repo or on GitHub (no copy needed): 23,305 exact+published files, 4,049 git-history files, 66+17 LFS objects (see audit report).
- Senior Health (15 ch, 308 videos, 307 transcripts) extracted + manifests, and the Dr Rehan Omar supplement manifests, committed. Rehan raw stays local and separate from competitors; DS-000032 untouched; nothing registered, no DS-ID allocated.

## Where things now are
| Asset | Location |
|---|---|
| Source MP4s | `data/raw/forensic-analysis/media-library-2026-11-11/<channel>/` (ignored; also `~/Documents/YIOS-Media-Library`) |
| Preserved What If / Casual Finance / thumbnail / Finance Short evidence | `data/raw/forensic-analysis/preserved-worktree-evidence-2026-10-21/` |
| Transcripts (Senior Health) | `data/extracted/channel-data/senior-health-16-acquisition/` |
| Creator / Algorithm audits | `docs/audits/external/` |
| Finance/Economics corpus | registry DB (LFS) + branch `research/finance-economics-intelligence` |
| Search entry | `data/manifests/YIOS_MASTER_RESEARCH_INDEX.csv`; per-file: `YIOS_RETAINED_ASSET_PROVENANCE.csv` |

## Git protection
- `stash@{0}` preserved, never popped/dropped: refs `refs/preservation/stash0-2026-11-11`, `refs/preservation/stash0-untracked-2026-11-11` and local branches `preservation/stash0-tracked-delta-2026-11-11`, `preservation/stash0-untracked-LOCAL-ONLY-2026-11-11`.
- The untracked half (1,729 files, ~757 MB) was **not pushed**: it contains two zips over GitHub's 100 MB limit. Secret scan of names and content: no tokens (hits were file names like `apify_api_*.json`). Needs an off-device export.
- The 4 ahead commits (docs from PR #48 + merge 2b6ccea5) contained no secrets and were pushed fast-forward (no force) to `research/finance-economics-intelligence`; remote head verified `2b6ccea5`.

## Verification
- LFS: registry DB payload was fetched from the GitHub LFS server into an empty temp store and hashed `39e7a28b…` = expected. **Verified for that one object only**; the other LFS objects were not fetched.
- Not done: semantic-overlap / DIFFERENT_REVISION content comparison (Creator, Algorithm vs DS-000011/018); marked UNKNOWN_OR_UNVERIFIED, hence not counted as independent evidence.
- Not committed: unrelated pre-existing changes in the active worktree (8 modified scripts/tests, `docs/project-audit/`, `docs/prompts/`) — not mine, left untouched.

## Cleanup
- **Bytes deleted: 0.** Nothing was removed or moved.
- `YIOS_CLEANUP_CANDIDATES.csv`: 440 MP4 rows `BLOCKED_BACKUP` (no off-device copy; a same-Mac clone is not a backup) + cache/.DS_Store rows `PROPOSED_NOT_EXECUTED` (inside hashed audit packages).
- Disk is at 99% (~9 GB free) — the real risk. 12.6 GB unique content in `~/YIOS-local-audits` was not copied for that reason.

## Still unprotected (sole local copy)
~13.35 GB: MP4s, preservation/recovery payloads, stash untracked half, preserved evidence. 

## Owner decisions
1. Off-device destination (external drive / cloud) for the above, then hash-verify there.
2. Approve Trash of cache rows; only after backup, decide on MP4 / duplicate originals.
3. Register Rehan supplement and Creator/Algorithm audits (DS-IDs) and run overlap check?
4. Merge the PR; DoctorLaura ($~1.58) and timestamped SRT runs.
