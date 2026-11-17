# Visual Forensics Standard — install report (2026-10-23, Machine B)

## Outcome

**`VALIDATED_EXTERNAL_CANDIDATE — NOT_PUBLISHED`**

The integration is complete and validated. It is held outside Git at `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-10-23/VISUAL_FORENSICS_STANDARD_INSTALL/`. The repository was not modified, and **project integration is not claimed yet.**

**What blocks publication:**
- The only checked-out branch is the canonical Finance branch `research/finance-economics-intelligence`.
- Its published head `c5c3d60e` (local = origin, ahead/behind 0/0) is the Friday release. That release sets the state to `MACHINE_B_RELEASED_AWAITING_MACHINE_A_ACCEPTANCE`.
- Machine A acceptance has not been published.
- So any Machine B commit or push to that branch now would be a write inside the writer-ownership handoff.
- The owner also forbade new branches and worktrees, so no safe alternative branch exists.

## Starting and final state

| | Value |
|---|---|
| Host / user | Machine B, `ghilmanislam360` |
| Repo | `/Users/ghilmanislam360/Documents/youtube-intelligence-os`; one worktree |
| Branch / HEAD (start = final) | `research/finance-economics-intelligence` @ `c5c3d60ebb23f111721c6526146b569fe0f5d826` = origin |
| Working tree (start = final) | clean (0 porcelain entries) |
| Finance JSONL `VIDEO_AUDIT_966.jsonl` | `6ba11e4f…0576aa0` = handoff value |
| Finance workbook `FINANCE_1612_COMBINED_INTELLIGENCE.xlsx` | `b40bcaee…38a0` = handoff value |
| Usage at start | five-hour 20 %, weekly 4 %, context 16 %; disk 28 GiB free (97 % used) |

## What was read

- **Kit:** `YIOS_Visual_Forensics_Intelligence_Kit_v1.0.zip` (SHA-256 `a89de050280c9bcce94b5baf922bf6c716065f5f2c0a8afc5e4b274384895cff`, 95,862 B), extracted in a scratch folder. 32/32 files match `PACKAGE_FILE_MANIFEST.json`, and the kit's own `validate_kit.py` passes. Read in full:
  - the master install prompt, install README and integration insert;
  - `SKILL.md`, references 01–14 and all 7 templates.
- **Source prompts:** section structure checked for all four. Prompt 02's rules 7–8 (frame reconstruction format, 20-second multi-clip continuity) were read in full.
- **YIOS project:**
  - `AGENTS.md`. There is no `CLAUDE.md` and no `.claude/` directory. `.codex/skills/graphify` exists with no name collision.
  - `research/README.md`;
  - `docs/FORENSIC_STAGING_AND_PROMOTION.md`;
  - Finance `FINANCE_WRITER_OWNERSHIP.md` and `FINANCE_WEEKEND_HANDOFF_2026-10-23.md`.
- **Visual run:** `MULTI_CHANNEL_VISUAL_FORENSICS/` reports 03, 04, 06 (pilot 4), 07, 08, 09 and 10, plus `tools/build_manifest.py`.
- **Historical CF pipeline:** known from 04 (`origin/research/casually-finance-editing-forensics@090f84b3`), read via Git objects in the earlier run.

## Preserved original prompts (byte-identical)

| File | Bytes | SHA-256 |
|---|---|---|
| `source-prompts/01_UNIVERSAL_VIDEO_VISUAL_DNA_ORIGINAL.txt` | 27,886 | `d6c1ed63302b57ba29855cc708d2dea6b10e9b4b1f6b7dd1ed021aff307cd40d` |
| `source-prompts/02_VIDEO_FORENSIC_ATTENTION_ORIGINAL.txt` | 13,615 | `96db418e28d410653cfced0498963c7b27a29f1f61b567cd5051057ad21a310d` |
| `source-prompts/03_ULTRA_PRECISION_VISUAL_SCRIPT_ORIGINAL.txt` | 44,738 | `fea21e6c86f6165452f2a047d611af6b69b3e209564136d37cfdd28ed5d9e9ad` |
| `source-prompts/04_MASTER_VIDEO_FORENSIC_V4_ORIGINAL.txt` | 33,898 | `7a09f4e77f7c91d9276de9a78433f099e1203b0807e2ea91f372a84ea97cc841` |

- Prompt 01 has no final newline. It is kept exactly as supplied.
- Each prompt is stored once, under `research/visual-forensics/`. There are no duplicates inside the skill.
- The chat-typed "WORLD-CLASS VISUAL FORENSIC ANALYSIS" prompt is **not** available as exact project text. Only its mapped requirements exist, in reference 14. It is not claimed as a byte-verified file.

## Installed layout (candidate → repository paths)

- **`.claude/skills/visual-ct-scan/`:**
  - `SKILL.md` (augmented: see next section);
  - `references/01…14_*.md` (verbatim);
  - `templates/` (7 files, verbatim).
- **`research/visual-forensics/`:**
  - `README.md`;
  - `SOURCE_PROMPT_MANIFEST.json` (verbatim) and `source-prompts/` (4, verbatim);
  - `SKILL_INVOCATION_EXAMPLES.md`;
  - `validate_install.py`;
  - `INSTALLED_FILES.sha256` (30 files);
  - this report.
- **`AGENTS.md`:** one additive "Visual forensics" section, applied by `INSTRUCTION_AND_INDEX.patch`. Claude Code and Codex both load `AGENTS.md` here, so no new `CLAUDE.md` is needed.
- **`research/README.md`:** one additive index bullet, in the same patch.
- **Size and safety:** 252 KB total, no binaries or media. None of the paths is gitignored.

**`SKILL.md` changes vs kit:** additions only. The kit body is unchanged. The kit hash was `b7baff3e…1fd9`; the installed hash is `81515ba6…f878`.
1. The description gains the owner's trigger phrases. The frontmatter stays valid (`name`, `description`, 591 characters).
2. **Request routing** table:
   - "visual forensic(s)" → `DEEP` (asks only if the source is unknown);
   - "deep/deeper visual analysis" → `DEEP`;
   - "CT scan" / "frame by frame" → `CT_SCAN`;
   - "recreate/reconstruct/motion reconstruction" → adds `RECONSTRUCTION`;
   - "channel visual DNA" → adds `CHANNEL_DNA`;
   - plus prompt 04's section/screenshot modes, prompt 02's 20-second clip continuity, and an adaptive long-form CT scan.
3. **YIOS bridge:**
   - the ledger is the status authority;
   - existing tools are reused;
   - 1 fps maps to `STRUCTURAL` only;
   - `DEEP`/`CT_SCAN` require the 04 C-2 state detector plus frame-accurate authoring (04 C-3, the CF `QA.json` contract);
   - no repo writes while another writer owns the branch.

## How the standard extends the existing 1 fps method without over-certifying

The existing run has:
- a full decode;
- a per-frame scene score;
- 1 fps sheets covering every second;
- dense windows where views were ambiguous.

Under this standard that earns `full_temporal_overview` = PASS only. Each video stays `VISUAL_ANALYSIS_PARTIAL` until three things are true:
1. Every changed-state interval is bracketed at native PTS or frame precision.
2. Every candidate is confirmed or rejected.
3. Unseen gaps are declared.

ASR stays `ASR_ONLY_NOT_AUDIO_VERIFIED`. `FULL_AV_SIGNOFF_COMPLETE` needs human listening. Historical counts are context only, and no status was changed:
- 448 unique / 454 MP4s;
- 4 partial pilots;
- 38 CF Shorts;
- 12 What If `HISTORICAL_UNVERIFIED`.

## Conservative resolutions where prompts conflict with evidence rules

Reference 14 applies, plus these specifics:
- **Retention:** prompt 02 asks for a "retention spike timestamp" and a "full-video retention curve". These become a non-numeric risk/opportunity map unless owner-supplied retention data exists.
- **Lens and style:** prompt 02 asks for a "lens estimate" (~35 mm) and style names (e.g. "Pixar-like"). These are reported as an apparent framing class and a style analogy, not a measured focal length or proven influence.
- **AI "lenses":** prompt 03's seven model-named lenses (ChatGPT … Claude) are treated as brainstorming perspectives, not independent validation (reference 10).
- **Frame-by-frame scope:** "Every frame / every 100 ms" means exact PTS for real events plus a compressed hold log, not prose per frame (reference 14 §2).

## Verification results

1. **Kit integrity:** `validate_kit.py` PASS. 32/32 package hashes match.
2. **Candidate:** `validate_install.py` PASS on an assembled tree (HEAD's `AGENTS.md` + `research/README.md` + patch + candidate). It checks:
   - prompts byte-identical;
   - 30 installed-file hashes;
   - frontmatter;
   - references 01–14;
   - `SKILL.md` links resolve;
   - templates parse;
   - 6 modes and 6 owner trigger phrases routable;
   - `AGENTS.md` and index links present.
3. **Negative test:** one appended byte in a prompt plus a deleted reference 07 → FAIL with 4 specific errors (expected).
4. **Patch:** `git apply --check --whitespace=error-all` on the live repo → OK (a read-only check). Trailing whitespace: none in added files.
5. **Secret scan:** no credentials. The only matches are prose such as "no secret credentials" and "typography tokens".
6. **Smoke test** (`../SMOKE_TEST_uPQcyookL0Y/` in the external folder): a `/visual-ct-scan` CT_SCAN dry run on pilot `uPQcyookL0Y`, using archived evidence only.
   - The source was re-hashed: it equals ledger 03 and manifest 08. 28/28 derived hashes and 9/9 deliverable hashes match.
   - Gates:
     - `source_identity` PASS;
     - `full_temporal_overview` PASS;
     - `candidate_shots_verified`, motion, creative and script mapping PARTIAL;
     - `meaningful_state_timing`, `production_blueprint`, listening and AV sign-off BLOCKED.
   - Status stays `VISUAL_ANALYSIS_PARTIAL` / `AUDIO_REVIEW_PENDING`, with no metrics invented.
7. **Preservation:**
   - repo HEAD, tree and Finance JSONL/workbook are unchanged;
   - no source MP4 or ZIP was touched (one MP4 was read for hashing);
   - the visual run folder was not modified;
   - the kit ZIP is left in place.

## Applying it later (only in a safe, owner-authorized window)

Apply only after Machine A publishes acceptance and later releases back with `MACHINE_B_SOLE_WRITER_ACCEPTED` published, or after the owner authorizes another target. Recheck the live head and active writers first.

```bash
O=/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-10-23/VISUAL_FORENSICS_STANDARD_INSTALL
cd /Users/ghilmanislam360/Documents/youtube-intelligence-os
cp -Rn "$O/repo-candidate/.claude" "$O/repo-candidate/research" .
git apply -p1 "$O/INSTRUCTION_AND_INDEX.patch"
python3 -I research/visual-forensics/validate_install.py .
git add .claude/skills/visual-ct-scan research/visual-forensics AGENTS.md research/README.md
```

Then commit as a single docs-only commit and push normally.

## Remaining gaps

- **Not published:** the skill is not live in the project until the patch is applied, which is blocked as described above.
- **No real-session trigger test:** there is no live Claude Code test of automatic skill discovery, because the skill is not installed anywhere Claude Code scans. Routing was verified statically against the description and table.
- **WORLD-CLASS chat prompt:** not archived verbatim.
- **No video analysed:** no new video was analysed and no status was changed, by design.
