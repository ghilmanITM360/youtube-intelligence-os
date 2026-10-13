# RESUME HERE: Finance Short 01 keyframe animation

_Last updated: 2026-10-13, milestone D complete (all 21 shots animated) + QA checkpoint. Stopped at the 5-hour usage checkpoint (85 %)._

## Where things are

| Item | Value |
|---|---|
| Branch | `production/finance-short-01-keyframe` (base `main`) |
| Draft PR | https://github.com/ghilmanITM360/youtube-intelligence-os/pull/29 (draft; do not merge) |
| Last verified pushed commit before this file | `ff205a5` (S09–S12). This file ships in the QA checkpoint commit right after it. Verify with `git ls-remote origin refs/heads/production/finance-short-01-keyframe` |
| Audio | **Blocked.** The only MP3 (`experiment/PHASE_2_ASSETS/audio_analysis/source_audio/TTSOL-en-AU-WilliamMultilingual-20261013-154730.mp3`, SHA256 `f4a9e22d…7b33`) says "April" for APR at 38.63–39.03 s. No corrected MP3 has been found yet. All timings are PROVISIONAL; previews are muted and watermarked |
| Final export | **Not allowed** until a corrected MP3 passes the pronunciation gate (`timeline.gate.final_sync_allowed` in the bundle) |

## Shots (21)

| Status | Shots |
|---|---|
| Animated and QA'd: stills, contact sheets, motion strips and a full muted preview | **All 21:** S01A, S01B, S02A, S02B, S03, S04A, S04B, S04C, S05A, S05B, S06A, S06B, S07A, S07B, S08, S09A, S09B, S10A, S10B, S11, S12 |
| Remaining | No animation is missing. Still to do: audio sync once the corrected MP3 arrives, human review, and the final render once the owner approves |

The per-shot choreography plan (word-anchored) is in `experiment/PHASE_2_ASSETS/CLAUDE_HANDOFF.md` §5. The shot code is in `animation/src/shots/`. Keyframes reference narration words with `word(shot, norm)`, so they follow a re-alignment automatically.

## Known defects and deviations

- Full QA record: `animation/ANIMATION_QA.md`. It covers checks, deliberate deviations from the hero frames (S03 contact, S10 live circle, S11 sit-down, IK walk) and open items.
- **Captions:** default y is 1550; S01A/B, S02A, S07B and S09 have per-shot overrides (`CAPTION_Y` in `Video.tsx`). Long chunks auto-shrink to fit one line (min 40 px). Check these on a phone.
- **12 scene instances** (label pills, qualifier text, the C14 clock) are generator variants of registered assets with different text or size. They're listed in `bundle.report`.
- **Text font:** Avenir Next is a macOS system font and can't be committed. On non-Mac machines the fallback font changes text widths, so re-check labels there.
- No human art-direction or motion review has happened yet. remy-2 hair still needs owner sign-off.

## Last successful QA

- `npm test` passes and `npx tsc --noEmit` is clean.
- The full render gives 0 joint-envelope violations across 1590 frames, 0 black segments and 0 decode errors.
- Seek-order stills are byte-identical.
- Committed evidence:
  - `animation/qa/contact_sheet_shot_midpoints.png` and the `motion_*.png` strips
  - `animation/previews/finance_short_01_PROVISIONAL_muted.mp4` (muted and watermarked, SHA256 `ba5a5ee3…e2ed`, 5.4 MB)

## Rebuild and preview

```bash
cd productions/finance-short-01/animation
npm ci                                   # Node >= 22.18 (tests use native TS type stripping); tested on Node 25.2.1
npm test                                 # rig + timeline checks
npx tsc --noEmit
npm run studio                           # Remotion Studio; compositions FinanceShort01 and Shot-<ID>
node scripts/qa_frames.mjs <name> S04A+0,S04A+20 --scale=0.35   # contact sheet in out/qa/<name>/ (needs ImageMagick)
npm run preview                          # full muted PROVISIONAL render to out/ (not committed)
python3 scripts/export_bundle.py         # only after PHASE_2_ASSETS changes (deterministic)
```

## Dependencies

- **Committed:** asset package (`experiment/`, SHA256-verified import, see `IMPORT_MANIFEST.sha256`), `animation/src/data/bundle.json`, and `package-lock.json`.
- **Local only:**
  - Node ≥ 22.18 and npm.
  - Remotion downloads Chrome Headless Shell on the first render.
  - ImageMagick, for QA sheets only.
  - Python 3, only for `export_bundle.py` and the PHASE_2 build.
  - whisper.cpp with `ggml-small.en.bin`, only for re-alignment (`align_audio.py`; default path `~/.cache/hyperframes/whisper/models/`).
  - Avenir Next (macOS).
- **Phase 2 PNG rebuild:** `experiment/PHASE_2_ASSETS/build/render.mjs` imports Sharp from a local Codex runtime path. Remotion doesn't need it; only the Phase 2 PNG rebuild does.

## When the corrected MP3 arrives

1. Copy it next to the original in `experiment/PHASE_2_ASSETS/audio_analysis/source_audio/`. Never overwrite the original.
2. Re-run the alignment, then the build:
   - `python3 build/align_audio.py <mp3> ../FINAL_SCRIPT.md AUDIO_ALIGNMENT.json <scratch> audio_analysis/pronunciation_gate.json` (run from `PHASE_2_ASSETS`)
   - then `python3 build/build_assets.py`
3. Check that `script_comparison.differences` is empty and that there are 21 phrases. Listen to APR, then set the gate result to PASS.
4. Run `python3 scripts/export_bundle.py && npm test` in `animation/`. Review each shot's word anchors and freeze the timeline.
5. Add the audio to the composition (not yet wired), then render the final once the owner approves.

## Next exact operation

1. Get the owner's review of `previews/finance_short_01_PROVISIONAL_muted.mp4` and `qa/` (acting, pacing, caption positions, remy-2 hair).
2. When the corrected MP3 arrives:
   - Follow "When the corrected MP3 arrives" above.
   - Wire `<Audio>` from a copy of the new MP3 under `animation/public/`, gated on `TL.gate.final_sync_allowed`.
   - Re-check each shot's word anchors and its S09A "apr" anchor.
   - Re-render, run the QA, and get owner approval before the final H.264/AAC export.

## Not yet pushed

Nothing, once the milestone C commit is pushed. `animation/out/` (QA renders) is intentionally local.

## 2026-10-13 second-PC milestone: portability

- Current checkout: `/Users/ghilmankhan/.codex/worktrees/finance-short-01/youtube-intelligence-os`, branch `production/finance-short-01-keyframe`; old owner-PC path does not exist here.
- Verified starting local/remote/PR head: `a9543746622e5dc8ad715551b184f06887b8e2fb`; exact-head GitHub validate SUCCESS. This section ships in the next milestone; resolve its SHA with `git log -1` and remote with `git ls-remote` (a commit cannot contain its own SHA).
- Fixed confirmed second-PC PNG renderer failure: local locked Sharp 0.35.5 instead of hardcoded owner-PC cache. Added real scratch render test (unrelated cwd, dimensions, deterministic output).
- QA frame extraction now supports `--sheet=false` without ImageMagick; default montage font no longer uses a macOS filesystem path.
- Fresh `npm ci`, rig/timeline tests, typecheck, bundle rebuild, and four 320px stills PASS. 244 SVG / 196 PNG hashes match. Renderer `npm ci` and smoke test PASS. `PORTABILITY.md` contains exact commands and font strategy.
- Bundle bytes match; fixture float drift max 4.55e-13, within 1e-6 tolerance; original committed fixture preserved.
- New previews are local-only ignored `animation/out/qa/portability/`; existing committed preview remains remotely recoverable. No visual shot artwork changed in this milestone.
- Corrected MP3 absent; original remains intact, final export blocked. Hair and human art/motion/mobile approval remain pending.
- Usage at milestone: five-hour 3%, weekly 29% (live snapshot; recheck).
- Next safe operation: inspect fresh mobile stills, then sample sensitive contact transitions and classify any confirmed defect. All 21 implemented shots remain in scope; no claim of human approval.

## Marker contact milestone

- Prior milestone pushed and remote verified: `39081c5e45d94d4767b7ae6d7cd5223449ba4f2b`.
- CONFIRMED DEFECT fixed: S10A absolute frame 1375 → S10B frame 1376 marker retreat jumped from the 1.08-turn endpoint to the zero-angle start (~20px). Retreat now begins at the actual completed stroke endpoint; approved circle geometry and timing remain unchanged.
- Added production-path contact tests: approach, endpoint hold, continuous retreat, home return, backward seeking. Test failed on old path and passed after fix. Rig/timeline tests and typecheck PASS; before/after frames 1374–1377 and 1381 inspected. Evidence in ignored local `animation/out/qa/marker_comparison.png`; final source fix is remotely recoverable after push.
- Usage: five-hour 6%, weekly 29%. Audio and owner approvals unchanged.
- Next safe operation: inspect sampled grip, coin, lever, receipt, walk and seated contacts, then finish mobile obstruction review.

## Caption milestone

- Previous local/remote head `fee3b41abb4b719be5111b42b93ffb310e77c89e`; exact-head CI SUCCESS.
- Fixed confirmed caption carry across cuts (e.g. old “payment date” persisted at S11+2). Holds are now bounded by their source shot and caption gaps stay empty.
- Fixed caption overlap with the explicitly simulated UI mask: top y0–100, bottom y1600–1920, right x900–1080/y850–1600. These are conservative test zones, not a claim about every YouTube app/device layout.
- Shared metrics: centre x470, maximum plate width840, default y1530, S07B y200; font >=40px for every current chunk. Existing font/style and one-line captions retained.
- New caption regression tests failed with old timing/geometry and pass after fixes; checks cover all 21 shot boundaries, hold ends, gaps, all current caption safe bounds and minimum size. Rig/timeline/contact tests and typecheck PASS.
- Native 21-shot stills plus 320px/160px simulations reviewed; 11 targeted updated caption samples inspected. Local-only ignored paths: `animation/out/qa/all_shots_native/`, `mobile_320/`, `mobile_160/`, `caption_mobile/`, `contacts/`.
- Prop/contact samples reviewed at S01B+12/13/15, S02A+49/50/51, S03+20/21/25, S05A+13/14/26, S06B+30/31/32, S07B+69/70, S11+2/11/19. No additional confirmed contact defect from those samples; this does not certify every intervening frame or replace motion review.
- Remaining mobile risk: small source qualifiers/diagram supporting labels at stress scale and right-side scene content under simulated rail. Recomposition of approved diagrams requires deliberate owner review; no claim that captions make all scene content phone-safe.
- Usage snapshot five-hour8%, weekly30%; corrected MP3 still absent. Next safe operation: one consolidated updated muted full preview, decode and joint-warning checks; then owner review checkpoint.
