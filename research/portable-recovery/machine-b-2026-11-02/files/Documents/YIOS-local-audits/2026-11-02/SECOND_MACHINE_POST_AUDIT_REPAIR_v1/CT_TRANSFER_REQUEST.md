# CT recovery / transfer request (nothing resumed, no reviewers launched, no measurement rerun)

Checked: all 46+ fetched branch tips (fetched 2026-11-02). Newest published visual-forensics handoffs: Video 004 `0ll9rEtoRrs` (checkpoint P), Video 005 `-X6YzlY_8tM` (checkpoint J, `research/casually-finance-editing-forensics` @ `f067ad22`), `5umJ63d3rzQ` (checkpoint 11). **No handoff, manifest or workspace for a newer Video 006 / "Checkpoint B" exists in Git**; `xtqbRt94TTw` appears only as older forensics CSVs on `codex/casually-finance-forensic-research` (PR21-era package, source sha reported `030a85ad…`, not verified here and NOT a substitute). No accessible transfer location is configured; none was probed.

## Request to Machine A (ordered, smallest sufficient set)
1. UNKNOWN workspace root path + the latest `CONTINUATION_HANDOFF.md`/BRIEF for Video 006 (path UNKNOWN, size UNKNOWN, sha UNKNOWN) and its source manifest.
2. Checkpoint manifests (`EVIDENCE_SHA256SUMS_checkpoint_B` and any later) for Video 006 — sizes UNKNOWN.
3. Shard map + original shard 1 and 3 reviewer outputs (`OUT_shard_1.json`, `OUT_shard_3.json`) and validators — paths/hashes UNKNOWN until measured at source.
4. Only the source imagery those shard outputs reference.
5. Writer-lock record (`~/YIOS-local-audits/vf_lock.sh`) state.
Do not send all 5,092 v1 entries. Reviewer conclusions must not be reconstructed from summary text.

## Video 005 (`-X6YzlY_8tM`) — hash-pinned dependency set already enumerated
`CT_VIDEO005_CHECKPOINT_MANIFEST_ENTRIES.csv`: 161 entries (A–J) parsed from the published `EVIDENCE_SHA256SUMS_*` files, bytes UNKNOWN. `CT_TRANSFER_REQUEST_video005_-X6YzlY_8tM.csv`: the 30 v1 requirement rows (SOURCE_MP4 already hash-verified present, sha `adff6676…`, 21,270,077 B at `~/Documents/YIOS-Media-Library/CasuallyFinance/`). Transfer by hash; preserve any collision.
