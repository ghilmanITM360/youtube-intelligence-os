# Git auxiliary-ref investigation — 27 October 2026

**Historical classification: documented auxiliary-ref exception. Actor: ACTOR_UNKNOWN. Current exact-ref acceptance: BLOCKED. No observed canonical project-integrity loss in the checked scope.**

This is a read-only reconciliation of `/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z`. Its original `VALIDATION.json` remains **107 PASS / 1 FAIL / 108**, status INCOMPLETE_BLOCKED. No prior report, ref or receipt was changed.

## A. Canonical project-state integrity

Historical before/after and fresh checkout agree on HEAD `badec432bbf5610748123b3f0e0bcb9cdb25fa10`, branch `codex/what-if-archive-main-integration`, complete saved porcelain status, stash and worktree list. Existing untracked evidence remains present in the same status listing; a dirty source tree was preserved, not cleaned. Stash OID remains `5b6c3042679400b16aa1024b79058b71dade0ab9`. Only one registered YIOS worktree is shown: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`. All non-auxiliary local refs agree. A fresh bounded `git ls-remote --heads --tags origin` returns the same **40** publication entries as the historical receipt; this is not a fetch or proof of Machine B's unpushed work.

Current staged diff, unstaged tracked diff and tracked research diff are empty. Current raw index bytes, entries and flags were captured for end-of-review comparison. The original audit did not save a raw index digest, so byte-for-byte historical index preservation is not claimed. Historical porcelain status supports semantic staged/unstaged preservation.

The six selected Casually Finance documents all match their original canonical SHA-256 receipts, totalling **77,142 bytes**. Their Git blob bytes in the captured tree also match all six current and historical hashes. This establishes the relevant canonical research content within that bounded scope. It does not certify every ignored/untracked research artifact or Machine B data.

## B. Exact auxiliary event and fresh ref delta

Original failed check: `Git unchanged: refs`. The original exact delta is only this addition:

`refs/codex/turn-diffs/captures/1793071154306/f4029e0b-cceb-4bf2-8c8b-c56efc1ceeb1/base`

Recorded OID: `93dca940f88913968abf5ba9db1135c4a3027f69`.

The timestamp-like name component decodes to **2026-10-27T03:19:14.306000+00:00**; it is a naming observation, not a trusted creation timestamp or actor ID.

**Fresh result differs from the prompt's expected existence:** `git show-ref --verify` exits 128; the exact ref is absent. The loose ref file and its reflog file are absent, and `git reflog exists` exits 1. `git cat-file -t 93dca940f88913968abf5ba9db1135c4a3027f69` succeeds with type **tree**. HEAD's tree is `990c8a15a052a9b7021b7568fa3095d34a55911b`; the captured tree is not falsely treated as HEAD.

Since the prior final receipt, the saved comparison shows **one auxiliary checkpoint added and two auxiliary refs removed**, no retargeting. Exact full names and OIDs are in `GIT_REF_DELTA_EVIDENCE.json`. Every changed name is under `refs/codex/turn-diffs`; every changed entry concerns the same tree OID. No canonical branch, tag, stash or remote-tracking ref moved.

Other capture names share the structure `refs/codex/turn-diffs/captures/<milliseconds>/<UUID>/base` and resolve to trees. Checkpoint names share the same namespace family and tree type. The target already existed under older refs before the original addition. Five current refs still retain it:

- `refs/codex/turn-diffs/captures/1793026351693/ddf8a2c6-7f86-4faf-bacf-41c512bb9e4d/base`
- `refs/codex/turn-diffs/captures/1793058998914/421c6ec8-77e3-47e2-b470-bc83c26e1c49/base`
- `refs/codex/turn-diffs/checkpoints/881b4075302216c35a00ab882840b5e1/e15b0798c9c4f13b993ba0ba3ef29622/1793071514935/eb894917-7086-4de2-9282-89a7a95555a8`
- `refs/codex/turn-diffs/checkpoints/d4dc27cff36ceff0692c2856248094d1/78e351a272b375143aa2235076124f61/1793046683036/90b15567-a199-446a-b286-34ea97d8e38d`
- `refs/codex/turn-diffs/checkpoints/fe5858f7dacdb8b8882c040f4db6783d/be9b76541766524365cd4ebb69663030/1792961824514/821ae66a-de7d-479f-9319-7add9c9fe8fb`

Tree-to-HEAD metadata comparison reports **282 extra capture entries**, and no modifications to HEAD entries in that comparison. The reverse diff's `D` markers mean entries are present in the capture tree but absent from HEAD; they are not a deletion operation and do not establish source loss. The six research documents are among the captured entries.

## C. Attribution and bounded log review

**ACTOR_UNKNOWN** applies to both original creation and later auxiliary churn. No reflog identity or contemporaneous create/delete command was found for the exact ref. The prior authorized readiness rollout contains observations and report-writing commands mentioning this ref; those are not independent creation evidence. Seven local desktop log files for 27 October (about 5.2 MB) contain no exact event token or matching turn-diff logging. Absence of a log entry is not evidence that no tool acted.

The naming/structure and tree targets are consistent with the owner's stated Codex bookkeeping explanation. Public explanations and generic OpenAI documentation cannot identify the actor of this exact local event. A bounded official-documentation check did not establish this namespace's precise implementation. No creator attribution is inferred from generic tool behaviour. Official reference inspected: [OpenAI troubleshooting documentation](https://learn.chatgpt.com/docs/reference/troubleshooting). This reference is not used as evidence of attribution.

No tool was restarted, no ref recreated, and no Git mutation, checkout, reset, prune, garbage collection, fetch or cleanup was run. Git reads used `GIT_OPTIONAL_LOCKS=0` and `GIT_NO_LAZY_FETCH=1`.

## D. Recovery implications and acceptance

The original addition created another name retaining an already retained immutable tree. Its isolated historical impact is a documented auxiliary-ref exception. The later missing names do not remove the target tree's current reachability because five other refs retain it. No source loss or publication-history change was observed from this delta. This conclusion does not prove complete tree/blob closure, all-history LFS coverage or clean-machine recovery.

`ACCEPTANCE_CRITERIA.md` was written before the narrow checks ran. The resulting **13-check** narrow assessment is **12 PASS / 1 FAIL / BLOCKED** because the exact named ref does not currently exist. This is a distinct present-state failure, not a rewrite of the original 107/108 result. There is no silent waiver. A future owner decision may accept the documented historical exception and current auxiliary churn for planning; neither decision authorizes ref deletion/recreation or transfer.

All **84/84** prior sealed entries and **286/286** V7 historical control receipts match. V7 accepted verified bytes remain **6,332,524,432** (physical **6,332,929,262**, including the approved 404,830-byte duplicate). V8 uploads remain zero in this reconciliation; the backup automation remains PAUSED. Disk is below the 5 GB reserve and current authorized Drive quota could not be reauthenticated, so execution is separately blocked even if the owner accepts the documented exception.

Exact commands, captured outputs, source identities and log-review boundaries are under `evidence/`; consult the JSON addendum and handoff. No complete disaster-recovery certification is issued.

## Final verification receipt

Five-hour usage **11%**, weekly **57%**; paid balance0, two reset credits remain untouched. Mac free **4,088,963,072 bytes** (4.089 GB), reserve shortfall **911,036,928 bytes**; Drive current owner quota remains UNVERIFIED. All16 current-session preservation comparisons pass, including every YIOS ref, raw index SHA-256, index entries/flags, checkout state, eight source identities and PAUSED automation TOML. Deliverable arithmetic/schema checks **11/11 PASS**. These checks do not replace the separate narrow12/13 BLOCKED or historical107/108 result. Exact final HEAD/status are preserved in `evidence/GIT_CURRENT_AFTER.json` (282 pre-existing untracked status lines, no tracked edits). No source/cloud/Git mutations or recovery transfers performed.
