# YIOS automation and ownership

Observed through 2026-11-06T03:38Z. A lock receipt shows who claimed it, nothing more. The audit acquired, released and recovered no locks and changed no scheduler.

## Live locks at 03:38:52Z

| Channel | Lock | Label | Run | Acquired | Last heartbeat in receipt |
|---|---|---|---|---|---|
| Casually Finance — Video006 | `.vf_writer_lock` | `codex-Video006-followup-20261106` | `01a1ad01…`, pid 51841 | 03:18:50Z | 03:25:37Z |
| Primitive Education | `.pe_writer_lock` | `session-85559743-nonaudio-closure` | none, pid 86660 | 2026-11-05T22:07:36Z | 03:31:43Z |
| xkcd What If | `.xkcd_writer_lock` | `xkcd-whatif-nonaudio-followup` | `ea35c26f`, pid 87688 | 03:27:41Z | 03:27:41Z |
| Barely Evolved | `.be_writer_lock` | released 03:31:37Z by session 15f69c1b | | | |

## Schedulers and recurring work

| Item | Channel | Config | Enabled state | Last evidence | Real unattended research? |
|---|---|---|---|---|---|
| `com.yios.primitive-education-continue` (launchd) | Primitive Education | every 1800 s, `scripts/pe_continue.sh` | loaded, not running, runs 25, last exit 0 | `scheduler.log` 03:15:16Z SKIP lock held | **No, none proved** |
| `yios-visual-forensics-machine-a` (Claude scheduled task) | Casually Finance | `~/.claude/scheduled-tasks/.../SKILL.md` | schedule state not visible here | lock events `scheduled-*` at 21:13Z, 00:27Z, 01:53Z, 03:11Z; pushes W1 to W4 | **Yes by receipts:** W1-W4 pushed during these lock windows; handoff names runs 2547cbe6 and 88d103b4; W3 and W4 lock labels name 5c8c86e3 and b69509dd |
| `cf-longform-pilot-after-weekly-reset` (Claude scheduled task) | Casually Finance | one-time | Oct 21 file; not confirmed active | none seen | UNKNOWN |
| Codex 2-hour follow-up | Casually Finance | same-chat follow-up per handoff | no file in `~/.codex/automations` | run `01a1ad01` active now | Interactive/Codex; persistence UNKNOWN |
| `yios-verified-backup-continuation` (Codex) | Backup | path named in older notes | **not present** at `~/.codex/automations/` | none | No |
| xkcd What If, Barely Evolved | | no launchd job or scheduled task found | sessions only | lock events | Session-driven |

## Primitive Education: 17-run classification kept

File: `out/PRIMITIVE_EDUCATION_SCHEDULER_RUNS.csv`. Row-level, 20 runs.

| Class, first 17 | Count |
|---|---|
| Actual completed research cycle | **0** |
| BUSY exit, one a full worker costing $0.311 | 3 (runs 1, 3, 12) |
| Logged usage WAIT | 1 (run 13) |
| **Inferred WAIT / unverified outcome** (no log line) | **10** (runs 4-11, 16, 17) |
| Source-access failure, exit 0 | 2 (runs 14, 15) |
| Supervised test, not an unattended cycle | 1 (run 2) |

Runs 18-20: 1 inferred WAIT, 2 BUSY. launchd reports 25 now. Only two later log lines exist: 18:48:35Z WAIT at five-hour 1, and 03:15:16Z SKIP lock held. Runs 21-25 were not classified row by row, because launchd timestamps were not re-collected for them.

## Downloads blocker

- Last scheduled-context probe: 2026-11-05T12:54:40Z, all 4 held-out sources BLOCKED. Run 14 at 04:38Z hung in `open()`.
- Worker note in `NON_AUDIO_GATE_MATRIX.md`: tccd log at 12:27:42Z shows `AUTHREQ_PROMPTING` for `kTCCServiceSystemPolicyDownloadsFolder`, responsible process the claude binary launched by launchd. This audit did not replay that log. My own search of one other 10-minute window found no match, so the two are not in conflict. The link from prompt to hang stays INFERRED.
- Workaround by session 85559743: 15 SHA-256 verified copies in `primitive-education/source_media`, with `source_path.txt` repointed. No OS permission changed.
- **Not proved fixed.** No scheduled run has read those copies. Since 03:31Z `HOLD_NO_EXECUTABLE_WORK` makes the scheduler skip model calls, so no test will happen until someone deletes it. Interactive held-out completion is not a scheduler fix.

## Ownership issues to settle

1. **Conflicting writer rules for `research/casually-finance-editing-forensics`.** `~/.claude/CLAUDE.md` says sole writer is Claude session 873b9a27 and Machine B is sole Finance writer. Machine B's `HANDBACK_REQUIREMENTS.md` records an owner correction: ownership belongs to an active task, with no permanent sole writer. Lock events show Codex and scheduled Claude writing this branch today. Current practice follows the handback; CLAUDE.md looks stale. Owner should confirm.
2. **Finance:** last recorded writer `OWNER_DIRECTED_TAKEOVER_ghilmanislam360`, Nov 2. Whether Machine B is writing now: UNKNOWN. `yios-finance-machine-a` is clean at `9c6f42fb`, 15 commits behind PR #36.
3. **Lock owner vs code:** these locks prove claim, not work. Missing heartbeat is not release.
