# Three senior-health visual packages

**QA_BLOCKED — three draft illustration packages built, clinical and listening review still required.** No final video rendered. Branch: production/senior-health-casually-finance-three-videos. [Issue #33](https://github.com/ghilmanITM360/youtube-intelligence-os/issues/33). [Draft PR #34](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/34).

| Package | Duration | Scenes | First file |
|---|---:|---:|---|
| HIIT | 30.557460s | 8 | [Handoff](01_HIIT_AFTER_60/CLAUDE_HANDOFF.md) |
| Running | 31.927438s | 8 | [Handoff](02_RUNNING_AFTER_60/CLAUDE_HANDOFF.md) |
| Swimming | 17.866667s | 6 | [Handoff](03_SWIMMING_AFTER_60/CLAUDE_HANDOFF.md) |

Each package is independent: source provenance, unchanged copied AAC + decoded PCM (local transfer), two machine ASR runs, word alignment, draft SRT, narration analysis, clinical claims, complete storyboard, editable full SVGs and components, transparent PNG exports, start/mid/end states, contact sheets, explicit keyframe plan and validation. Reused designs/copies are not counted as independent artwork.

Start with PRODUCTION_STATUS.json and per-package qa/VALIDATION.json for exact counts. Global AUDIO_TRANSFER_MANIFEST.json gives paths/hashes for audio omitted from Git. Delivery ZIPs contain the audio; competitor screenshots and original MP4s stay local and outside them. Rights to supplied audio remain unverified.

## Clinical findings that block publication
HIIT: critical ASR disagreement at roughly 21.9s and broad avoidance advice. Running: universal three-runs limit, joint-risk generalization and VO₂ terminology. Swimming: contradictory joints sentence and unsupported best-exercise ranking. Ratings are opinion. See per-video MEDICAL_CLAIMS.csv and MEDICAL_SOURCES.json; checked CDC/AHA/YouTube sources support contextual review, not medical approval of this narration.

## Production design
Read CASUALLY_FINANCE_VISUAL_SPEC.md and SHARED_CHARACTER_STYLE_GUIDE.md. Research is pinned to Git refs without merging #21/#28. No YIOS engines, canonical evidence, existing production branches, or stashes were changed. No graph built. All artwork is authored SVG, no copied screenshots or third-party characters.

## Reproduction
From repository root: python3 productions/senior-health-casually-finance-3/tools/build.py; node productions/senior-health-casually-finance-3/tools/render.cjs; python3 productions/senior-health-casually-finance-3/tools/contact_sheets.py; python3 productions/senior-health-casually-finance-3/tools/validate.py. Run commands sequentially. Python needs Pillow; rendering uses bundled Sharp at the recorded absolute runtime path. ASR requires locally cached Whisper models. prepare.py does not alter inputs. On another machine, supply the exact source files or use the included audio and skip prepare/transcribe; renderer package path may need configuration.

Do not rerun validation in a clone without restoring local original media: source-integrity checks intentionally fail when originals are absent. Use stored hashes to distinguish portable asset integrity from local provenance re-verification.
