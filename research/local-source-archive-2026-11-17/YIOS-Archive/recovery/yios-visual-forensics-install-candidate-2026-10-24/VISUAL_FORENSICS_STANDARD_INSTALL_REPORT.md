# Visual Forensics Standard — Install Report (candidate, NOT installed in repo)

Date 2026-10-24 · Host Ghilmans-Laptop.local (Machine A) · Repo /Users/ghilmankhan/workprojects/youtube-intelligence-os
Start/final repo HEAD: `7e70f061aae849e9929b531c4bc855b23edda179`, branch `research/finance-economics-intelligence` (unchanged; zero repo writes).
Origin tip of same branch (after dry-run fetch): `c5c3d60e` ("preserve Nick Invests channel intelligence and weekend handoff") — Machine B is actively writing this branch.
Kit zip SHA-256: `a89de050280c9bcce94b5baf922bf6c716065f5f2c0a8afc5e4b274384895cff`

## Status: VALIDATED EXTERNAL CANDIDATE. Not committed, not pushed, not live in the repo.
Reason: current branch is the shared Finance branch (Machine B sole Finance writer per policy), local tree has 282 untracked files from other tasks (`finance-short-02-visual-calibration/`, `productions/`, `research/casually-finance-script-intelligence/`), local is behind origin, and no owner authorization to publish on this branch. `research/casually-finance-editing-forensics` (090f84b3) is owned by another Claude session and was not touched. No worktrees/branches created.

## Read
Repo AGENTS.md, global CLAUDE.md policy, `docs/research/README.md`, branch list/log, CH-000004 editing pilot (from Git object), entire kit (master prompt, README, SKILL, manifests, insert, validator). No root `CLAUDE.md` existed; `.claude/` exists but is empty.

## Candidate tree (`repo-overlay/`)
- `.claude/skills/visual-ct-scan/SKILL.md` (+ appended routing table and 1fps-relation section)
- `references/01..14` (14), `templates/` (7), `source-prompts/` (4 originals, byte-identical), `SOURCE_PROMPT_MANIFEST.json`, `INVOCATION_EXAMPLES.md`
- `CLAUDE.md` (new; pointer to AGENTS.md + kit insert + mode routing)
- `docs/research/README.md` (one added index line; patch in `docs-research-README.patch`)
Four prompt SHA-256: 01 d6c1ed63…cd40d · 02 96db418e…a310d · 03 fea21e6c…d9ad · 04 7a09f4e7…cc841 (full values in manifest; verified).

## Verification
- Kit `validate_kit.py`: PASS. `validate_candidate.py`: PASS (4 hashes, frontmatter, 14 refs, 7 templates, JSON/CSV parse, dead links, CLAUDE.md/index pointers).
- `routing_demo.py`: visual forensics→DEEP, CT scan→CT_SCAN, deeper visual analysis→DEEP, motion reconstruction→+RECONSTRUCTION, frame-by-frame→CT_SCAN, channel visual DNA→+CHANNEL_DNA; description contains all trigger phrases. This is a static check of the installed text, not a live Claude Code discovery test (skill is not in `.claude/skills` yet).
- Pilot dry-run (read-only, no decoding): CH-000004 `editing-visual-intelligence-pilot-2026-09-11.json` status `WORKING_WITH_FORENSIC_EVIDENCE` is kept as is. Under the new gates it has no native-PTS event ledger, no audio alignment, no full-state coverage → it is at most `STRUCTURAL`; it is NOT DEEP/CT_SCAN complete and no AV sign-off.
- Repo unchanged: HEAD same, `git status` fingerprint identical before/after; no MP4/ZIP/JSONL/workbook touched.

## Gaps
1. Not installed/published (blocked as above). Install later: `./install.sh /path/to/clean/authorized/checkout`, then stage only the 3 paths.
2. Historical Machine-B docs (`01_EXISTING_VISUAL_WORK_DISCOVERY.md`, `04_…METHOD_RECONSTRUCTION.md`, `03_…COVERAGE.csv`, `06_…PILOT…REPORT.md`, `09_CONTINUATION_HANDOFF.md`) are in no local branch/Git object; the 448/454/4/38/12 figures are unverified context from the kit only.
3. WORLD-CLASS chat prompt exists only as the mapping in reference 14, not as a byte-exact file.
4. Live skill discovery untested until installed. Origin Finance branch is ahead; re-fetch before installing.
