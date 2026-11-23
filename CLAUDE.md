# Project standing instructions (YIOS)
Repository rules live in `AGENTS.md` (read it first; it governs). The visual-audit rules below are merged in, not a replacement.

## Persistent YouTube Visual Audit rules
Full rulebook: `docs/YOUTUBE_VISUAL_INTELLIGENCE_MASTER_RULEBOOK.md` (v2.0 with addendum pointer, copied 2026-11-20) + mandatory addendum `docs/YOUTUBE_CHANNEL_SAMPLING_AND_PARALLEL_BRANCH_RULES.md` (R27-R29). Read it at task start; reread the relevant section on every phase change, before each scene batch, before reconstruction tests and before verdicts.
1. Analyze only channels with real, decodable, local `.mp4` reference videos (MP3/transcript/screenshot-only = excluded).
2. Inspect and verify existing analysis first; reuse what is verified, repair gaps. A file existing is not proof.
3. No superficial analysis: every material shot needs frame/time-accurate, measured descriptions (geometry, colors, layers, characters, camera, motion, transitions, rebuild recipe).
4. Do real work, not plans.
5. Ledger: `CHANNEL_VISUAL_AUDIT/AUDIT_PROGRESS.md`. Read on start/resume and before each batch; update after each verified unit, before compaction and at session end.
6. When blocked: read the error, research, test a fix, log it. Never claim a browser/tool that was not used.
7. Audio is a timing reference only; no unsupported audio claims.
8. Validate by rendering: same-video reconstruction (original assets only, no source footage) plus original-scene tests.
9. Sampling (R27): inventory ALL MP4s cheaply (T0), deep-analyze only information-rich ones: start 4-6, expand to 12-18 only if needed, ceiling 24-30 (not a target); add in batches of 3-5, measure information gain, keep >=2 holdouts, defer the rest (`VIDEO_SELECTION_REGISTER.csv`, `DEFERRED_VIDEO_QUEUE.md`). Never mark uninspected videos as analyzed.
9b. Branches (R28): one channel per branch/worktree, GO is per channel, parallel channels allowed, never mix channel evidence. Here: reuse existing worktrees only; no new worktree/branch creation, commit or push without owner approval (global policy overrides).
9c. Before each session/batch/verdict: read CLAUDE.md, rulebook sections, addendum, channel ledger, check git branch/worktree, deep-analysed count, saturation + reconstruction status.
10. No GO without executed renders and QA, a score of 85+ and no critical blockers. Do not start the next channel before a real GO.
11. Never delete or overwrite sources; recreations using third-party footage/audio stay internal.
Repo policy still applies: no commits, pushes, new worktrees or PR merges without explicit authorization.
