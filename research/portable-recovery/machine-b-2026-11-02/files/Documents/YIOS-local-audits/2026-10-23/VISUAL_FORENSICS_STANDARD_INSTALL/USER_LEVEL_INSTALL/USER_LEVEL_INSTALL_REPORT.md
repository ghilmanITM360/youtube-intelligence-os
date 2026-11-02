# Visual CT Scan — Machine B user-level install (2026-10-23)

**Verdict: `MACHINE_B_USER_VISUAL_CT_SCAN_SKILL_INSTALLED_AND_VALIDATED`**

- Installed at `/Users/ghilmanislam360/.claude/skills/visual-ct-scan/` (no prior skill of that name; nothing overwritten).
- 22 files: `SKILL.md`, references 01–14, 7 templates. Hashes in `USER_INSTALLED_FILES.sha256`.
- 21/22 byte-identical to the validated package (`repo-candidate/research/visual-forensics/INSTALLED_FILES.sha256`).
- `SKILL.md` differs on line 62 only: it adds the absolute external path to the source prompts, because the repo-relative path does not exist until publication. User-level hash `2801e0d9…3bea`; validated repo hash `81515ba6…f878` (unchanged, used for the repo install).
- Source prompts 4/4 match `SOURCE_PROMPT_MANIFEST.json`; they stay in `repo-candidate/research/visual-forensics/source-prompts/`.
- All markdown links resolve; 3 absolute paths in `SKILL.md` exist; templates parse.

## Fresh-session tests (`claude -p`, sonnet, scratch cwd outside the repo, tools limited to Skill/Read/Glob/Grep)

Transcripts in `discovery-tests/`. Every session's init listed `visual-ct-scan` in both skills and slash commands.

| Test | Prompt | Skill loaded | Mode chosen |
|---|---|---|---|
| manual | `/visual-ct-scan CT scan …` | slash expansion | CT_SCAN |
| t1 | Visual forensics | auto (Skill tool) | DEEP |
| t2 | deeper visual analysis | auto | DEEP |
| t3 | CT scan | auto | CT_SCAN |
| t4 | Frame-by-frame analysis | auto | CT_SCAN |
| t5 | Motion reconstruction | auto | CT_SCAN + RECONSTRUCTION |
| t6 | Channel visual DNA | auto | CHANNEL_DNA (gap reported) |
| c1 | CT scan + motion reconstruction + channel visual DNA | auto | CT_SCAN + RECONSTRUCTION + CHANNEL_DNA |

All 8 separated source evidence / measured events / inferred psychology / reconstruction recommendations. No file was opened beyond the skill itself; no video analysed.

Repo HEAD `c5c3d60e` = origin = remote, 0 porcelain entries; Finance JSONL/workbook hashes unchanged.
