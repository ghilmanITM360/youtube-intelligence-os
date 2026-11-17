# HANDOFF PROMPT: xkcd's What If? visual forensics, clone-readiness pass (for a second Claude account)

Written 2026-11-08 by the Casual Finance session. Paste everything below the line into the other account.

---

You are taking over one scoped job for the owner: run the same visual-forensics research on the channel **xkcd's What If?** that was just run on Casual Finance (CF). Read this whole prompt before any action. The owner reads Hinglish: reply to the owner in short Hinglish, cite sources as markdown links, and write every file in English.

## 0. Goal in one paragraph
The owner wants an AI-built channel that is visually close to xkcd's What If?, but with ORIGINAL characters, logo and name in the same style. To get there, the channel's visuals must be (a) honestly measured, (b) actually looked at as images, (c) written up as model sheets and a style bible, (d) turned into motion-timing facts and (e) turned into structured, per-asset prompt packs. Animation will later be built from layered assets and authored keyframes (HumanCraft guide), never from text-to-video or image-to-video. You do (a) to (e) and stop. You do NOT generate assets, install a renderer, or work on audio.

## 1. Preflight (read-only, do all of it first)
1. **Same Mac check.** Every path below is on the owner's Mac under `~/YIOS-local-audits/`. If `~/YIOS-local-audits/xkcd-whatif/asset_library/` does not exist on your machine, STOP and tell the owner. Do not recreate it from the internet.
2. **Usage.** Check live five-hour usage, then weekly, then context. New work only at five-hour <= ~50%. 85% = checkpoint, 90% = start nothing new, 95% = seal and stop. Weekly 95% same. Never spend or reset credits. If the meter is unreadable, treat it as UNKNOWN and do small units only. Do not trust a hook message that says a limit is used up without checking the real meter.
3. **Claim.** One exclusive writer for this task: `VF_LOCK_DIR=~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock ~/YIOS-local-audits/vf_lock.sh` (read its header for acquire/release/status; token-owned, lease-based, recovery needs proof). If BUSY, do nothing and report. Never take over because of inactivity. Release explicitly at the end. Check usage BEFORE acquiring.
4. **Repo rules.** Repo `/Users/ghilmankhan/workprojects/youtube-intelligence-os`, `AGENTS.md` and `~/.claude/CLAUDE.md` govern. No worktrees, clones or temp checkouts without owner approval. No reset --hard, no force push, no destructive clean, no merge or PR close. Preserve stashes and all untracked or ignored evidence. Your work lives in the external folder, so the repo should stay untouched.
5. **Read, in this order** (all local):
   - `~/YIOS-local-audits/VISUAL_FORENSICS_OPERATIONS.md`
   - `~/YIOS-local-audits/CASUAL_FINANCE_CLONE_READINESS_PLAN_20261108.md` (the 6-step plan; you are doing the xkcd version of steps 3 and 4 plus the motion windows)
   - `~/YIOS-local-audits/xkcd-whatif/campaign/CONTINUATION_HANDOFF.md` (bottom first), `CAMPAIGN_GOAL_v1.md`, `CHANNEL_PRODUCTION_MANUAL_v0.7.md`, `HELDOUT_EVALUATION_v6.md`, `AUDIO_LISTENING_CAPABILITY.json`
   - `~/YIOS-local-audits/xkcd-whatif/asset_library/README_FOR_NEXT_AI.md` and `library_manifest.csv`
   - The CF worked example, to copy the METHOD (not the content): `~/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/asset_library/_channel/` -> `CATEGORY_AUDIT.md`, `HUMANCRAFT_ALIGNMENT.md`, `model_sheets/MODEL_SHEETS_CASUAL_FINANCE.md`
   - The kit: `~/Downloads/YIOS_Visual_Forensics_Intelligence_Kit_v1.0.zip` (unzip into its own NEW empty folder, never into the repo). Its installed copy is `~/.claude/skills/visual-ct-scan/` (SKILL.md, references 01-14, templates). Read references 01, 02, 04, 05, 09, 11, 12, 13 in full; skim the rest. Invoke the `visual-ct-scan` skill.
   - The guide: `~/Downloads/HumanCraft_Video_Studio_V2_Complete_Guide.pdf` (35 pages; read all of it, a few pages at a time).
6. **Verify, do not trust.** Memory and handoff notes are point-in-time. Re-check on disk: library video count, total state frames, that 3 random `states_index.csv` rows match their image SHA-256, and the `pts_check` column. Record what you verified in `STATE_SNAPSHOT.md`.

## 2. Facts to start from (as recorded 2026-11-06 / 2026-11-08; re-verify)
- Channel UC6IxnFzHofFJ5X2PycSMsww = CH-000004. Census: 45 long + 46 Shorts; media exists for 44 videos in the library; 27 videos in the repo's index have no local source media. Per-video status is `VISUAL_ANALYSIS_PARTIAL`. Audio is `BLOCKED_CAPABILITY` (ASR only, never listened). No video is `CT_SCAN_COMPLETE` and no video is audio-signed-off.
- The campaign (32 selected videos, held-out sets 1-5, manual v0.7, checkpoint R `3c6145cc`) used its own `scripts/xk_*.py` pipeline. It is NOT the CF 42-check validator. The campaign sits on `HOLD_NO_EXECUTABLE_WORK`: that hold covered the old campaign scope. This clone-readiness pass is NEW scope the owner has now explicitly requested, so the hold does not block it. Phase 7 knowledge links are already done (sidecar on the research branch) and are out of scope here.
- Frame library (local only): `~/YIOS-local-audits/xkcd-whatif/asset_library/` = 44 videos, 5,458 state frames, 2,755 near-duplicate clusters (9 span more than one video). One representative frame per ledger state. Every image in `_channel/unique_frames/` can be opened and viewed.
- 38 of 40 Shorts are narration excerpts of long videos (campaign note). Treat Shorts and their parent long videos as overlapping evidence, not independent samples (AGENTS rule 9). Count and say so.
- 10 videos shared with the repo's existing forensic index carry different media hashes there, so they are different files. Do not merge those two evidence sets.

## 3. Phases (one at a time; seal a handoff file after each)
Work folder: `~/YIOS-local-audits/xkcd-whatif/asset_library/_channel/` (new files only; never edit existing ledgers, reports, manuals or SHA lists). Copy the CF tools to `~/YIOS-local-audits/tooling/asset_library/xkcd/` and adapt the copies. Do not edit the CF originals (`make_sheet.py`, `categorize.py`, `model_sheet_data.py`); they hold CF-specific rules (peach head colour, CF keywords).

**P1. Coverage honesty audit** -> `XKCD_COVERAGE_AUDIT.md`
Per video: long or Short, resolution, duration, state count, ledger status, known gaps, whether a parent long video exists. Compare against kit reference 13 completion gates. Say plainly which gates xkcd meets and which it does not. Do NOT upgrade any status.

**P2. Viewing pass + category audit** -> `CATEGORY_AUDIT.md`, `review_sheets/`
- Tag all 2,755 clusters by rule (keywords from the xkcd ledger text plus pixel features), labelled INFERRED. Categories: characters, environments, props, graphics_ui (diagrams, charts, maps, inset images, screenshots), typography, transitions (ledger-measured only, since a single frame cannot show a transition), uncategorised.
- OPEN the images. Use random 24-tile contact sheets per category (CF tool design: tile number + short id, `.members.csv` sidecar). Target at least 10 sheets total, and cover each of the 44 videos at least once. Record the exact viewed count and percent. Tags are only for finding candidates; anything that enters a model sheet or prompt must have been opened as an image first.
- Write a purity verdict per sheet (what fraction truly fits the tag, which keywords over-match). One reader means say so. If you use a reviewer subagent, use one at a time and audit its transcript for real image reads (`xk_validate_review.py` exists).

**P3. Model sheets v0.1** -> `model_sheets/MODEL_SHEETS_XKCD_WHATIF.md` plus CSVs and contact sheets
Every field is labelled MEASURED, OBSERVED, ESTIMATED, INFERRED or UNAVAILABLE. Cover:
- Two format families: 16:9 long-form and 9:16 Shorts, with measured resolutions.
- Character model sheet: the base stick figure (head shape, fill, outline weight, limb style, proportions, hair/hat/clothes modifiers, held props, expression set, pose set). Views seen only; a missing turnaround is UNAVAILABLE, not invented. Measure head-to-figure ratio and stroke width from pixels (adapt the CF script; do not reuse the peach-colour detector).
- Environment sheet: canvas colour(s), recurring set pieces (whiteboard, question box, globes, diagram plates), any scenes or insets, depth or layering, camera behaviour.
- Graphics/typography sheet: the question card, labels, hand-lettered text, diagrams, charts, real-world inserts. Font = nearest match, flagged INFERRED. Owner already said a near font is fine.
- Palette from sampled pixels (hex + share), with the sampling method stated.
- Rhythm per video from state ledgers (median, p10, p90 gap, states/min). The owner wants BOTH rhythm types cloned (busy and calm); report both and which video types fall in each, plus how the narration or script drives it where ASR text allows (labelled INFERRED, audio unverified).
- Entering-class mix (cut, pop-in, pose, text swap, draw-on, zoom, slide) from the ledgers.
- One-page style bible (8-10 rules) with counterexamples listed.

**P4. Motion windows** -> `motion_windows/`
The CF library holds one frame per state, so true motion curves are unmeasured. For each important entering class pick 2-3 short windows (10-30 frames) from the existing, SHA-verified source MP4s and measure duration, overshoot, easing and hold. One window at a time, bounded extractions only, no bulk frame dumps, JPEG evidence, free disk > 3 GiB. Label results MEASURED or ESTIMATED. ffmpeg 9 notes: use `-/filter:v file` (not -filter_script), chunk long select expressions by 40, some sources have first-frame PTS 1/30. Python for numpy/PIL: `~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3 -I`. Whisper exists only under `/usr/bin/python3 -E`.

**P5. HumanCraft alignment** -> `HUMANCRAFT_ALIGNMENT.md`
Map the PDF onto xkcd: layered rig and prop plan, text layers, candidate motion mapping per entering class (all INFERRED until tested), the tiny 5-12 s proof requirement, the 10-dimension scorecard, SEEN vs INFERRED reference breakdown. Check the local renderer facts again (Node 24, ffmpeg 9 with overlay and zoompan but NO drawtext; HyperFrames CLI and Remotion NOT verified or installed). Do not install anything; installs need owner approval. Record that narration or audio is the timing authority and is BLOCKED here.

**P6. Prompt pack (text only)** -> `PROMPT_PACK/`
One file per asset or per asset family, plus an index CSV. Per asset: `asset_id`, name, category, target storage path (`.../asset_library/_clone_assets/<category>/<asset_id>/`), purpose, reference frame ids (images you opened), locked descriptors, required modifiers and expression/pose list, framing, a ChatGPT image-generation prompt, "transparent PNG, no checkerboard, no scenery, one subject, consistent outline" wording with a pure-green key-colour fallback, negative prompts, and an acceptance check (side by side against the model sheet; halo and edge QA). Rules: character sheet and anchor reference first; one pose strip per request; at most about 9 objects per request; every later prompt repeats the same descriptors and attaches the same reference. **Originality:** same STYLE SYSTEM, different original characters (for example an animal or fictional mascot), new logo, changed name and branding. Do not copy the source channel's logo, title lockup, name or any recurring named characters; those are structure references only. A real person's likeness is a rights risk; avoid it. Image generation needs owner approval: you only write the prompts.

## 4. Hard stops (do not do these)
- No audio work, no listening claims, no AV sign-off. Contract stays visual-only. Never write `CT_SCAN_COMPLETE`, `FULL_AV_SIGNOFF` or "indistinguishable".
- No asset generation, no renderer install, no test render, no blind test (those come later and need owner go-ahead).
- No publishing. Images and video NEVER go to GitHub. Text indexes (CSV, hashes, markdown) may be published only on explicit owner go-ahead, to branch `research/xkcd-whatif-visual-forensics`, by normal push with allowlist, readback and the existing `scripts/xk_publish.py` guards. Never modify raw sources, canonical JSONL or workbooks, audit receipts, SHA lists, or Git history.
- One video or one task at a time; at most one targeted reviewer; no long background jobs, no polling loops, no new scheduled tasks. Keep media in durable storage, never in temp; copies get SHA-256 verified; originals untouched.
- Take timestamps from `date -u` or file mtimes, never hand-typed.
- Do not touch the Casual Finance, Primitive Education or Barely Evolved workspaces or locks.

## 5. Reporting and handoff
- After each phase write `<phase>_HANDOFF.md`: what was done, exact counts, files, SHA-256 of every new deliverable (`SHA256SUMS`), what is NOT done, the next exact operation. Keep the facts / observations / inferences / hypotheses separate.
- Tell the owner (short Hinglish): usage at start and end, what is done, what is blocked, one decision needed (if any). No essays.
- At the end release the lock, confirm FREE, and list unfinished items. If you stop early because of usage, seal the current atomic operation first.
- Worst-case rule: if anything here conflicts with `AGENTS.md`, the repo's evidence files, or what you see on disk, the repo and disk win. Report the conflict instead of guessing.
