# Publication coordination record — Codex ten-script drafts (2026-11-24)

This is a dated record, not a `yios` claim ref and not a release of anyone else's claim.

## Owner authorization (from the owner's chat message, 2026-11-24)
- Normal commit and push of the prepared What If research and script files to `research/what-if-channel-strategy-2026-11-18` is authorized.
- The Machine B Claude session is designated exclusive coordinator for this one publication, until push and verification finish, "if valid under repository rules and no existing writer claim conflicts".
- The designation does not release any other writer's claim.

## What was verified by this session (Machine B)
| Check | Result |
|---|---|
| Rules read | `AGENTS.md` (Writer coordination), `docs/YIOS_TWO_MAC_WORKFLOW.md`, `research/coordination/CHANNELS.md` |
| Remote branch tip before this commit | `3f262afde512e3b8ff292c78329eb05b73e289c1` (equals local HEAD) |
| Remote claim/integration refs | `git ls-remote origin` shows no `refs/heads/yios/claims/*` and no `.../integration/*`. Only two `yios-test/.../finance/TEST000000{1,2}` fixture refs exist. None concern What If |
| What If handoffs or release records in repo | None found under `research/coordination/` or `docs/` |
| `yios` CLI What If support | Confirmed unsupported: `scripts/yios.py` accepts `finance` and `visual-forensics` only for `start` and `integrate`. The `yios` launcher is also not on PATH. So no valid CLI claim could be created, and none was faked |
| Other branches | `research/xkcd-what-if-research-archive` (`f22c8212`) is not an ancestor of the target; it has 2 commits not on the target. It was left untouched |
| Machine A | Not accessible from this session. "No remote claim found" is a fact about origin only. Machine A's unpushed local state is **not verified** |

## Why the owner designation is applied the way it is
The two-Mac workflow rules cover the Finance and visual-forensics streams. For the What If stream no claim protocol exists, so there is no outstanding claim to bypass and none to release. The owner's designation is recorded here as the authority for this single publication. A normal fast-forward push is the technical guard: if another writer had pushed to the branch in the meantime, Git would reject the push and nothing would be overwritten.

## Scope of this publication
- Added: `productions/unreasonably-exact-codex-drafts-2026-11-24/` (81 files: ten Codex script packages, index, claim ledger, source inventory, coherence, final review, Day 1 three-way comparison, model reproduction code and output).
- Added: `research/what-if-channel-strategy/WHAT_IF_RESEARCH_AND_SCRIPTS_INDEX.md` and this record.
- Not changed: approved Day 1 V3 (`productions/unreasonably-exact-01-free-fall/`), Day 2 draft, Claude V1/V2 package, calendar, Finance files.
- Not added: the untracked xkcd workbook, images, audio, video, raw third-party books, Playbook PDF, caches.
