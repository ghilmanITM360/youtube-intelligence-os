# Resume Finance Short 01 — PR #29

Updated 2026-10-13, second-PC quality/portability session. **State: AUDIO_CORRECTION_REQUIRED.** All21 shots implemented. Confirmed defects found this session fixed; further artistic/device decisions and final audio/export need owner input.

## Git truth and recovery

- Branch: `production/finance-short-01-keyframe`; draft PR https://github.com/ghilmanITM360/youtube-intelligence-os/pull/29; base `main`; do not merge.
- Latest verified local/remote/code-render head before this evidence checkpoint: **`88e61abe2fd2f5b33da8ace591267cc28aeb0629`**. Exact-head GitHub `validate` SUCCESS: https://github.com/ghilmanITM360/youtube-intelligence-os/actions/runs/38436164450/job/115430569323.
- This document and QA evidence ship in the following checkpoint commit. A commit cannot embed its own SHA. Resolve the current checkpoint exactly with the commands below; its CI must be inspected separately and never inherited from the prior SHA.
- Current PC checkout: `/Users/ghilmankhan/.codex/worktrees/finance-short-01/youtube-intelligence-os`. Previous owner-PC path `/Users/ghilmanislam360/Documents/yios-finance-short-01-keyframe` is absent here.
- Pushed milestones: `39081c5e45d94d4767b7ae6d7cd5223449ba4f2b` portable renderer/QA; `fee3b41abb4b719be5111b42b93ffb310e77c89e` marker continuity; `88e61abe2fd2f5b33da8ace591267cc28aeb0629` caption timing/UI bounds.

```sh
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/production/finance-short-01-keyframe
gh pr view 29 --repo ghilmanITM360/youtube-intelligence-os --json headRefOid,headRefName,baseRefName,isDraft,statusCheckRollup
```

## Completed and verified

- Fixed S10A+61→S10B+0 (~20px) marker retreat jump: retreat starts at actual1.08-turn stroke endpoint. Regression failed before, passed afterward.
- Fixed captions held into subsequent shots (e.g.S11+2 showed previous “payment date”). Caption holds now stop at their own shot cut; gaps stay empty.
- Fixed caption overlaps with conservative simulated UI zones. Shared caption centrex470/max-width840/default-y1530; S07B-y200. All39 chunks remain>=40px. Approved font/style retained. Mask: top100px,bottom320px,right180px/y850–1600; actual-device layout remains unverified.
- Fixed owner-PC absolute Sharp path. Phase2 renderer has local Sharp0.35.5 lockfile and a scratch render smoke test from unrelated cwd. QA supports `--sheet=false` without ImageMagick and no hardcoded macOS montage-font path.
- Fresh checkout `npm ci`, rig/timeline/contact/caption tests, and typecheck PASS. Two actual walk trajectories added to planted-foot/joint tests (S02A,S07B); slide~1.1e-12px.
- All244 SVG/196 PNG hashes match manifest. Scratch rebuilds of CHR_REMY_PART_SHIN_F and PRP_BALANCE_CARD_000 match registered PNG hashes; registered originals untouched.
- Bundle rebuild byte-identical. Python parity fixture numeric differences max4.55e-13 (existing1e-6 tolerance); original fixture preserved.
- Native21-shot stills and320/160px UI stress review; targeted statement grip, offer sheet, lever, coin release/landing, receipt landing, walk stop and sit samples inspected. No other confirmed contact defect from sampled frames. No automated check substitutes for human acting/physics review.
- One consolidated updated muted/watermarked preview:1080×1920,H.264,30fps,1590frames,53s; no audio stream,0joint warnings,0decode errors,0black segments. Five forward/backward rendered frame pairs byte-identical.

## Remotely recoverable review artifacts

- `animation/previews/finance_short_01_PROVISIONAL_muted.mp4` — updated preview, SHA256 `9d83fa32ed662a3933dbaa8122e48716b321f73b521ca3e1fd8b67cddbe78df0`.
- `animation/qa/second_pc_validation.json` — exact source/preview provenance and automated results.
- `animation/qa/marker_retreat_before_after.png`, `animation/qa/caption_simulated_UI_stress.png` — focused visual evidence.
- Prior `animation/qa/motion_*.png` and midpoint sheet are historical pre-session references, not updated-caption evidence.
- Source, lockfiles, tests, QA and this handoff are remotely recoverable after this checkpoint push. `animation/out/` and node_modules/caches are intentionally ignored/local-only; no required source exists only there.

## Remaining backlog / approvals

See `animation/ANIMATION_QA.md` for classifications and exact review frames.

- **AUDIO BLOCKED:** no corrected MP3 in this checkout. Original APR→April at38.63–39.03s remains preserved; all timing provisional, final sync blocked. No synthetic replacement and no export/publication gate bypass.
- **OWNER APPROVAL REQUIRED:** Remy-2 hair unchanged; associate gesture/art direction; human motion/body/prop review; actual-device readability; final export.
- **QUALITY GAP needing review:** small20–24px supporting labels/qualifiers become3–4px at160px stress scale; approved right-side scene/diagram content can meet simulated UI rail. Captions were fixed, not the whole composition redesigned. Owner must settle hierarchy/composition on an actual device before further broad changes.
- **TECHNICAL RISK:** second macOS ARM64 checkout verified; Linux/Windows not run (no container runtime). Avenir Next is proprietary/macOS-specific. Fallback strategy and source-vs-pixel identity limits in `animation/PORTABILITY.md`; no proprietary font redistribution.
- Five approved near-arm exceptions are perspective-specific, not confirmed defects: shrug+117.89°(S01A+30/abs30),hold_bill+132.38°(S01B+15/abs56),hold_sheet+136.41°(S02B+40/abs215),open_hands+129.53°(S09A+17/abs1114),shocked+154.51°(S06B+38/abs757). Preserve pending owner art review.

## Commands (repository root)

```sh
cd productions/finance-short-01/animation
npm ci
npm test
npm run typecheck
npm run studio
node scripts/qa_frames.mjs review S10A+61,S10B+0,S11+2 --scale=0.296296 --sheet=false
npm run preview
```

Node>=22.18; tested Node24.14.0/npm11.9.0/Python3.9.6. Chrome Headless Shell downloads on first render. ImageMagick optional for sheets. `python3 scripts/export_bundle.py` only after authorized Phase2/alignment changes; preserve fixture if only platform float drift. Renderer install: `cd ../experiment/PHASE_2_ASSETS/build && npm ci && npm test`. More instructions: `animation/PORTABILITY.md`.

## Corrected audio next

1. Add owner-provided correction beside original; never overwrite. Verify provenance/hash and listen to APR.
2. From PHASE_2_ASSETS: `python3 build/align_audio.py <new-mp3> ../FINAL_SCRIPT.md AUDIO_ALIGNMENT.json <scratch> audio_analysis/pronunciation_gate.json`; needs whisper.cpp/model (see existing script). Then authorized `python3 build/build_assets.py` (install renderer first).
3. Check script differences/21phrases and actual pronunciation; only mark PASS after evidence. Re-export bundle and retest; word anchors re-align dynamically.
4. Audio composition wiring still pending by design. Review all timing/contact anchors after correction, wire approved audio behind gate, and obtain final-export approval.

## Resource and exact next safe operation

Latest live snapshot: five-hour13% used,weekly30% used. This is not a background continuation. Recheck live indicators before new work; stop expensive starts atfive-hour90% orweekly95%.

First command on next session: `git -C /Users/ghilmankhan/.codex/worktrees/finance-short-01/youtube-intelligence-os status --short --branch` (substitute local checkout path on another PC).

Next task: inspect current PR head/CI, then obtain owner review of updated preview and stress sheet or ingest a supplied corrected MP3 using the workflow above. Do not redo completed QA or redesign approved artwork without new evidence/direction.
