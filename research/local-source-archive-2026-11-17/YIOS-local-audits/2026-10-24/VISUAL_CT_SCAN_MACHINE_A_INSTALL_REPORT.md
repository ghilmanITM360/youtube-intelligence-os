# Visual CT Scan — Machine A install report (2026-10-24)

Verdict: **MACHINE_A_VISUAL_CT_SCAN_PARTIALLY_INSTALLED** (skill + Python pipeline fully working; Tesseract OCR deliberately not installed — see Blockers)

## Environment
Host Ghilmans-Laptop.local, user ghilmankhan, Claude Code 2.1.305, system Python 3.9.6, venv Python 3.12.14 (Homebrew). Usage before work: 5h 12%, weekly 8%. Disk free before 12 GiB, after 12Gi (venv 364 MB).

## Skill
- Path: /Users/ghilmankhan/.claude/skills/visual-ct-scan/ (new; target did not exist before)
- Source: yios-visual-forensics-install-candidate-2026-10-24/repo-overlay/.claude/skills/visual-ct-scan
- 28 files: SKILL.md, SOURCE_PROMPT_MANIFEST.json, INVOCATION_EXAMPLES.md, 14 references, 7 templates, 4 source prompts.
- Source checks before copy: candidate SHA256SUMS all OK; CONTINUATION_HANDOFF.sha256 OK; validate_candidate.py on overlay PASS; kit validate_kit.py PASS (4 prompts hash-verified, 14 refs, 7 templates).
- Copy is byte-identical to source (diff -r clean). Intentional path changes: NONE. All source-prompt/reference links are relative inside the skill folder, so they are valid for a personal install; 0 broken links; 4 prompts re-verified against manifest SHA-256.
- Installed checksums: /Users/ghilmankhan/YIOS-local-audits/2026-10-24/visual-ct-scan-installed.SHA256SUMS (0 failures).
- validate_candidate.py against the installed folder reports only "CLAUDE.md pointer" and "index link" — repo-only checks (project CLAUDE.md / docs index), intentionally not installed.
- Original candidate and Downloads kit untouched.

## Tooling (isolated venv, repo .venv untouched)
Venv: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-venv ; lock: /Users/ghilmankhan/YIOS-local-audits/tooling/visual-ct-scan-requirements.lock
Pinned: opencv-python-headless 5.0.0.93, scenedetect 0.7.2, numpy 2.5.4, scipy 1.18.1, pandas 3.1.0, pillow 13.0.0, click 8.5.0, tqdm 4.70.1, platformdirs, python-dateutil, six, tzdata.
Note: PySceneDetect 0.7.2 has no opencv-headless extra, so opencv-python (GUI) was pulled first, uninstalled, and replaced with the headless wheel; only one OpenCV variant is installed. pip check prints a metadata-only complaint (scenedetect declares opencv-python); import and CLI work.
System: ffmpeg/ffprobe 9.0.1; openai-whisper 20240930 with cached base.pt and small.en.pt (no downloads).

## Tool verification (all run)
ffmpeg/ffprobe OK; cv2 5.0.0, numpy, PIL, scipy, pandas, scenedetect imports OK; scenedetect CLI list-scenes OK.
Synthetic test (external folder tooling/_synthetic_test): 2 s red + 2 s blue 30 fps clip. PySceneDetect found the hard cut at 2.0 s ([0-2],[2-4]); OpenCV read all 120 frames and imread of an extracted PNG returned the expected red pixel. Scene detection is a cut detector only, not a motion/animation detector. No real video decoded.

## Discovery / routing
- Fresh headless session (claude -p, haiku) lists visual-ct-scan among available skills: discovery PASS.
- Manual invocation: skill loads by name; one test could not read SKILL.md without a permission grant (sandbox permission, not a skill fault).
- Automatic activation: prompt "CT scan with motion reconstruction of a channel video's visual style" (no skill named) loaded visual-ct-scan and selected CT_SCAN + RECONSTRUCTION: PASS.
- Routing table in SKILL.md inspected: visual forensics→DEEP, deeper visual→DEEP, CT scan→CT_SCAN, frame-by-frame→CT_SCAN, motion reconstruction→+RECONSTRUCTION, recreate→+RECONSTRUCTION, channel visual DNA→+CHANNEL_DNA; combinations add modes. Only 2 small model calls were used; the other routes were not live-tested.
- Slash command /visual-ct-scan: skill is listed in this session's skill list; typed-slash UI not exercised.

## Visual-forensics knowledge gates (from installed files)
References 01–14 cover evidence authority, temporal ingestion, art direction, motion/animation/camera, editing/script, audio-visual sync, attention hypotheses, reconstruction blueprints, channel DNA, scorecards and completion gates. Reference 03/13 and SKILL.md state a 1 FPS pass maps to STRUCTURAL and never to CT_SCAN_COMPLETE; reference 07 requires real human listening for FULL_AV_SIGNOFF; no eye-tracking or retention claims without evidence.

## Repository protection
HEAD 4cc60c36e4121735aeb135d6fff3b1fc927d1c15 (unchanged, equals pre-install 4cc60c36…). Status: ?? finance-short-02-visual-calibration/ ?? productions/ ?? research/casually-finance-script-intelligence/  (the same 3 pre-existing untracked paths; 0 tracked changes). Stash count        1 (unchanged). No commit, push, branch, worktree, clone; no files written into the repo.

## Blockers / limitations
1. Tesseract OCR NOT installed. brew install --dry-run shows it would also upgrade 13 shared libraries (libpng, freetype, glib, cairo, pcre2, xz, little-cms2, etc.), which I judged outside "no unrelated upgrades" on a 98%-full disk. Install when authorized: brew install tesseract. Until then on-screen text is read from native frames by Claude vision.
2. The Casually Finance forensic scripts exist only in Git (090f84b3); no external copy yet.
3. Whisper ASR remains uncertified; local human listening is impossible for the agent.
4. Disk is ~12 GiB free: cap frame extraction per video.
5. o3FQcd91MIs identity is title+duration only (HIGH_CONFIDENCE_NEEDS_REVIEW); owner confirmation still pending.

---
## Addendum 2026-10-24 (owner decisions applied)
- Tesseract: `OPTIONAL_DEFERRED` per owner; no Homebrew changes made.
- PySceneDetect metadata warning **resolved**: `scenedetect` replaced by `scenedetect-headless 0.7.2` in the isolated venv; `pip check` = "No broken requirements found"; synthetic hard-cut test re-passed (cut at 00:00:02.000, 120 frames read). Lock regenerated; previous lock kept as `visual-ct-scan-requirements.lock.pre-headless-swap`.
- Skill, 14 references, 7 templates, 4 source prompts: unchanged.
- First pilot (`o3FQcd91MIs`) evidence: `/Users/ghilmankhan/YIOS-local-audits/2026-10-24-o3FQcd91MIs-deep-ct-scan/`.
