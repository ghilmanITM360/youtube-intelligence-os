# Continuation handoff — visual-ct-scan install candidate (Machine A, 2026-10-24)

State: HOLD. Candidate preserved exactly as validated; repo untouched (HEAD 7e70f061aae849e9929b531c4bc855b23edda179, status fingerprint 4bd29880…, origin Finance branch c5c3d60ebb23…). No commit/push/branch/worktree.
Integrity: `cd <candidate> && shasum -a 256 -c SHA256SUMS` (40 files, all OK at 2026-10-24); zip a89de050…5cff.

## Blockers
1. Finance weekend handoff + sole-writer return not complete (Machine B owns Finance branch; origin ahead of local).
2. No owner authorization yet to publish.
3. Machine B's validated version is not visible in any local or remote ref → comparison below is incomplete.

## Dependencies
python3 (stdlib only), git, patch. No installs, no network, no media.

## Future installation (after owner authorization)
1. Confirm sole writer + clean tracked tree on the authorized checkout/branch; `git fetch` + fast-forward first.
2. FIRST reconcile with Machine B's version (below). If B already published `.claude/skills/visual-ct-scan`/`CLAUDE.md`, do NOT run install.sh; diff and merge instead.
3. `shasum -a 256 -c SHA256SUMS` then `python3 -I validate_candidate.py repo-overlay`
4. `./install.sh /Users/ghilmankhan/workprojects/youtube-intelligence-os` (refuses on tracked changes or existing targets)
5. `python3 -I validate_candidate.py <repo>`; `python3 -I routing_demo.py <repo>`
6. Stage ONLY `.claude/skills/visual-ct-scan`, `CLAUDE.md`, `docs/research/README.md`; check `git diff --cached --stat`, secret scan; normal commit + push; verify origin SHA.

## Machine A vs Machine B reconciliation checklist (B side not inspected)
| Item | Machine A candidate | Check on B |
|---|---|---|
| CLAUDE.md | Does not exist in repo at 7e70f061/origin c5c3d60e; candidate creates one: pointer to AGENTS.md + kit insert + mode routing | Does B have a CLAUDE.md? If so keep ONE; merge text, don't duplicate |
| AGENTS.md | Unmodified (only rules 1–16, no visual-forensics line) | Did B add a visual-forensics rule/pointer? Avoid duplicating it in CLAUDE.md |
| Research index | One line added to docs/research/README.md; research/ has no index file | Where did B link it (research/, docs/)? Use one location |
| Skill routing | SKILL.md appended routing table (CT scan→CT_SCAN; deep/forensic→DEEP; frame-by-frame→CT_SCAN; reconstruct adds RECONSTRUCTION; channel DNA adds CHANNEL_DNA) + 1fps→STRUCTURAL note; skill name `visual-ct-scan` | Same name/path? Same mapping? Differences in "frame-by-frame" or "scene by scene" mapping |
| Source prompts | inside skill `source-prompts/` + manifest | B location; keep one copy, hashes per manifest |
| Historical docs 01/03/04/06/09 | Absent from all local Git objects | Must come from B |
