# RESUME HERE: Finance Short 01 keyframe animation

_Last updated: 2026-10-13, milestone C (first grouped scenes)._

## Where things are

| Item | Value |
|---|---|
| Branch | `production/finance-short-01-keyframe` (base `main`) |
| Draft PR | https://github.com/ghilmanITM360/youtube-intelligence-os/pull/29 (draft; do not merge) |
| Last verified pushed commit before this file | `5935cd6` (milestone B). This file ships in the milestone C commit. Verify with `git ls-remote origin refs/heads/production/finance-short-01-keyframe` |
| Audio | **Blocked.** The only MP3 (`experiment/PHASE_2_ASSETS/audio_analysis/source_audio/TTSOL-en-AU-WilliamMultilingual-20261013-154730.mp3`, SHA256 `f4a9e22d…7b33`) says "April" for APR at 38.63–39.03 s. No corrected MP3 has been found yet. All timings are PROVISIONAL; previews are muted and watermarked |
| Final export | **Not allowed** until a corrected MP3 passes the pronunciation gate (`timeline.gate.final_sync_allowed` in the bundle) |

## Shots (21)

| Status | Shots |
|---|---|
| Animated and QA'd (stills and contact sheets) | S01A, S01B, S02A, S02B, S03 |
| Remaining (they render as labelled static hero frames) | S04A, S04B, S04C, S05A, S05B, S06A, S06B, S07A, S07B, S08, S09A, S09B, S10A, S10B, S11, S12 |

The per-shot choreography plan (word-anchored) is in `experiment/PHASE_2_ASSETS/CLAUDE_HANDOFF.md` §5. The shot code is in `animation/src/shots/`. Keyframes reference narration words with `word(shot, norm)`, so they follow a re-alignment automatically.

## Known defects and deviations

- **S03:** the fingertip now lands on the IF lever face at (712, 742) instead of the hero frame's plate edge at (610, 1010). This is deliberate, so the press is physical, and it's documented in `S03.tsx`.
- **Captions:** they're moved above the action in S01A, S01B and S02A (`CAPTION_Y` in `Video.tsx`), and long chunks auto-shrink to fit one line (min 40 px).
- **12 scene instances** (label pills, qualifier text, the C14 clock) are generator variants of registered assets with different text or size. They're listed in `bundle.report`.
- **Text font:** Avenir Next is a macOS system font and can't be committed. On non-Mac machines the fallback font changes text widths, so re-check labels there.
- No human art-direction or motion review has happened yet. remy-2 hair still needs owner sign-off.

## Last successful QA

- `npm test` passes: rig parity on 22 poses, eyes and IK; leg IK; rigidity; walk with no foot slide (< 1e-11), knee 20–53°, hip −34…8°; timeline coverage; captions fit; asset resolution; the gate blocks final sync.
- `npx tsc --noEmit` is clean.
- Visual contact sheets for S01–S03 at `animation/out/qa/` (local, not committed).

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

Animate S04A–S04C (C05 ledger): title pop, balance card slide, month strip stagger, receipt rows growing under the NOT CHARGED YET clip, point_across, and the "not yet charged" pill. Then S05–S06.

## Not yet pushed

Nothing, once the milestone C commit is pushed. `animation/out/` (QA renders) is intentionally local.
