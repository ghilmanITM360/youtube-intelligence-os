# Narrow auxiliary-ref review criteria — defined before execution

This review does not replace VALIDATION.json (107 PASS / 1 FAIL). It tests only whether the exact historical addition is isolated from canonical project state.

1. The sealed original delta must contain only the named capture ref, with no removals or retargeting.
2. The exact ref must resolve to 93dca940f88913968abf5ba9db1135c4a3027f69, type tree; older refs must already retain that OID.
3. Historical HEAD, branch, status, stashes, worktrees and every non-auxiliary ref must agree before/after.
4. Fresh checkout HEAD, branch, tracked staged/unstaged state, stashes, worktrees and publication refs must be reconciled; index byte integrity can only be compared within this review because no historical raw index hash was recorded.
5. Protected canonical research must match existing hashes within a bounded, explicitly stated manifest scope; no claim of a new whole-ecosystem census.
6. No observed protected-state drift may be attributed away as tool bookkeeping. Unknown actor remains ACTOR_UNKNOWN unless a contemporaneous creation record proves it.
7. Original evidence/checksums and automation PAUSED state must remain unchanged.

If 1–7 establish isolation: DOCUMENTED_AUXILIARY_REF_EXCEPTION, narrow acceptance PASS_WITH_DECLARED_LIMITATIONS. If unexplained protected-source drift or impact remains: BLOCKED. This is an impact review, not attribution, historical pass conversion, upload permission or disaster-recovery certification. The exact byte-hash index history and whole ignored/untracked content universe remain unproven if no historical evidence exists.

Resource gate is separate: disk <5 GB or unverified current Drive reserve blocks execution even if narrow ref acceptance passes. No downloads, uploads, Git writes, cleanup, ownership changes, automation edits, or source modifications are permitted. Only small new external evidence/report files are written.
