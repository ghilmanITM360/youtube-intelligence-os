# xkcd What If? — per-video visual closure: final continuation prompt (2026-11-09)

Paste everything below the line into a fresh Claude Code session (project: youtube-intelligence-os).

---

You are continuing the LOCAL-ONLY visual forensics campaign for xkcd's What If? (channel UC6IxnFzHofFJ5X2PycSMsww, CH-000004). Reply to the owner in short Hinglish with sources as markdown links; write all files in English.

## 0. Ground rules (do not break)
- Visual-only. Audio and AV are BLOCKED (ASR-only = `ASR_UNCERTIFIED`). You may write `VISUAL_ANALYSIS_COMPLETE` (visual-only, no claim about sound) or `VISUAL_ANALYSIS_PARTIAL`. NEVER write `CT_SCAN_COMPLETE` or `FULL_AV_SIGNOFF_COMPLETE`.
- Local only. Do not commit, push, publish, install anything, spend credits, run background jobs or poll. One video at a time, at most one targeted reviewer.
- Never modify source MP4s or existing ledgers except through the existing closure tooling. Never create worktrees or branches. Do not run Graphify.
- Casual Economics is excluded. This task is xkcd only.

## 1. Method: use the installed skill AND the frozen contract
1. Load the `visual-ct-scan` skill (`~/.claude/skills/visual-ct-scan/`), DEEP mode. Read references 01-03, 13 and 14 first.
2. Apply the skill's 10 gates from `templates/COVERAGE_AND_QUALITY_GATES_TEMPLATE.json`: `source_identity`, `full_temporal_overview`, `candidate_shots_verified`, `meaningful_state_timing`, `motion_design_review`, `creative_design_review`, `visual_script_mapping`, `production_blueprint`, `audio_human_listening`, `final_av_signoff`. The last two stay BLOCKED for every video.
3. Also apply the frozen closure contract: `~/YIOS-local-audits/xkcd-whatif/asset_library/_channel/ct_closure/VISUAL_CLOSURE_CONTRACT_v1.md` (verify its sha256 file first) and its tooling in `~/YIOS-local-audits/tooling/asset_library/xkcd/` (`closure_v1.py`, `stack_strips.py`, `blueprint_v2.py`, `closure_gate_v1.py`, `closure_ledger.py`). Follow the per-video loop in `ct_closure/CT_CLOSURE_HANDOFF_v1.md`.
4. The skill has no per-video validator, so the contract's gate script (`closure_gate_v1.py`) is the real check. A video is COMPLETE only if that script passes it.
5. Mandatory per-video outputs (skill): source_manifest.json, coverage.json, shot_ledger.csv, visual_event_ledger.csv, visual_ct_scan_report.md, audio_visual_alignment.csv (or an UNAVAILABLE record), reconstruction_blueprint.md, quality_gate.json, continuation_handoff.md. Reuse what already exists in `videos/<id>/` and the closure_v1 folder; do not duplicate.
6. VIEWED-FRAME RECORD (required): in each video's closure record list the exact frame IDs / PTS you actually opened as images (strips, hold sheets, native crops). A frame not listed there counts as not viewed. 1 fps samples are sampling, not native-frame verification. Detector candidates need visual confirmation. ffprobe PTS is authoritative.
7. Label every claim MEASURED / OBSERVED / ESTIMATED / INFERRED / UNAVAILABLE / NOT_APPLICABLE.

## 2. Resource gates (check `get_usage` before each video; it is authoritative)
- Start new work only at five-hour usage <= ~50%.
- 85% five-hour = checkpoint: finish the current video, write the handoff, then decide.
- 90% five-hour (or 95% weekly) = no new work; finish only the current atomic step.
- 95% = seal (checksums + handoff), release the lock, stop.
- Check order: five-hour, weekly, context, credits. Never spend or reset credits.

## 3. Lock method
- `VF_LOCK_DIR=~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock` and `~/YIOS-local-audits/vf_lock.sh`.
- `acquire` needs a LABEL (for example `deepvf-ct2`). `heartbeat` and `release` must be run with `VF_LOCK_DIR=...` in the SAME command, otherwise NOT_OWNER.
- Check `status` first. Current state at 2026-11-09: FREE. If someone else holds it, do not take over; stop and report.
- Release it at the end of the run and say so.

## 4. Task order
**Step A — count first (before any analysis).** From the library manifest (`asset_library/library_manifest.csv`, 44 videos), the census and the ledger, list: how many are long vs Short; how many have local source media (27 videos reportedly have none); any source-hash mismatches; which are already COMPLETE (ledger `ct_closure/CLOSURE_LEDGER_v1.csv`: 20 Shorts, 0 longs). Reconcile the conflicting notes ("24 in library" vs "24 long + 20 Shorts") by counting, and report the real numbers and which videos are eligible (source present, hash OK).

**Step B — close long videos, one at a time, cheapest-gaps-first** (suggested start: `qu8nx1qUwEU`, then `s3oLIDaElaE`, `JqFSGkFPipM`, `p2M8Y0z9Rl0`). Target: reach the owner's goal of 20 closed longs only as far as the usage gates allow. A video that cannot pass stays PARTIAL with the failing gate named. Do not relax the contract to reach a number. After each video: update `quality_gate_visual_v1.json`, rebuild the ledger (`closure_ledger.py`), update the handoff.

**Step C — only with leftover budget, in this order:**
1. v9 missing-feature test: the `MAP_FILL` and merged multi-move scroll rules (rules v3) are UNTESTED because held-out v9 had no feature-present cases. Find fresh unused videos that contain those features, test, and report counts honestly (COVERAGE_GAP if none exist).
2. Proof attempt 3 / prompt pack: re-run machine checks only. P8/P9 stay PENDING_HUMAN; do not mark them passed.
3. `alkJ7xScBiw` (2026 journey long): acquisition is an owner-blocked item (no `yt-dlp`, installs out of scope). Do not install anything. Keep it as an acquisition blocker in the report.

## 5. Evidence hygiene
- Work only in `~/YIOS-local-audits/xkcd-whatif/`. Keep media in place; verify SHA-256 on anything copied.
- At the end: refresh `SHA256SUMS_ct_closure_v1.txt`, update `CT_CLOSURE_HANDOFF_v1.md` (next video, failing gates, owner decisions), and the campaign memory file.
- Do not touch the repo HEAD (f4dc5d14) or untracked research folders.

## 6. Final report (short)
One message: usage at start and end; real counts from Step A; videos closed this run (id, status, failing gates); what stays PARTIAL and why; lock released yes/no; files changed; what needs an owner decision. State plainly that audio is still blocked and that nothing here is a CT_SCAN or AV sign-off.
