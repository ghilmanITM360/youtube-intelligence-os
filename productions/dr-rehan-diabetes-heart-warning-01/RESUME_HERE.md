# Resume here

## Phase 2 animation (2026-10-15)
Muted provisional preview built: `animation/Dr_Rehan_Heart_Warning_PREVIEW_MUTED.mp4` (45.5 s, 1080×1920@30). Editable: `animation/animate.py` (cues) → `animation/KEYFRAME_TIMELINE.json` → render. Rebuild: `python3 animation/animate.py timeline && python3 animation/animate.py render`. Timing from owner MP3 (sha256 in `animation/AUDIO_ALIGNMENT.json`; file not committed — place it locally). MP3 has no final 'That is why… when…' sentence. Still needed: confirm ACS/angina/subsets/sudden wording, doctor credit/likeness, clinician review, then mux audio + optional licensed music → FINAL. See `animation/ANIMATION_QA.md`.

Status: ASSET_PACKAGE_READY_FOR_OWNER_REVIEW; SCRIPT_APPROVAL_REQUIRED before final animation/publication. Eight scene groups / eighteen static visual states (seventeen narrative states plus one non-public ending placeholder). See DELIVERY_COUNTS.json; 17 original illustration designs, not 167 independently drawn assets.

Branch: production/dr-rehan-diabetes-heart-warning-assets
Issue: https://github.com/ghilmanITM360/youtube-intelligence-os/issues/31
Draft PR: https://github.com/ghilmanITM360/youtube-intelligence-os/pull/32
Clean base: 08e719264e31ecd82de24f8eeb8f065c08359fe5
Starting checkout / pinned research: fce81670bd2d6f29db6ef515732238fa3c5f09e3

All scene batches were committed and pushed sequentially. Last scene-batch checkpoint before final handoff: 0c13e0615bee09d62c80817f9a9f0da3ce3df37f. Final handoff commit is the Git HEAD containing this file; use `git rev-parse HEAD` rather than embedding a self-referential commit hash. No merge, worktree creation, research refresh, source modification, audio synthesis or video render was performed.

Open REVIEW_OVERVIEW.png, reviews/S01.png through S08.png, and FULL_ASSET_CONTACT_SHEET.png. Read SCRIPT_ISSUES.md and MEDICAL_CLAIMS_QA.md before animation. All 18 states have mobile visual review; native review sampled the contact-sensitive diabetes scene, doctor pointing source and heart diagram. No claim of human art approval, clinician sign-off or full AV QA.

Next owner actions: supply MP3 and full ending; confirm quoted wording and display credit; approve generic presenter or supply authorized likeness direction; approve visual direction and medical labels with clinician. Clinical anatomy is simplified and must be reviewed. Do not invent missing words or treat this package as an endorsement.

Claude can assemble from KEYFRAME_HANDOFF.json, SCENE_ASSET_MAP.csv, PART_REGISTER.csv and existing SVG/PNG files once inputs are approved. No need to regenerate assets. Detailed instructions: CLAUDE_ANIMATION_HANDOFF.md.

Unrelated state preserved: existing finance-short-02-visual-calibration/ and research/casually-finance-script-intelligence/ untracked files; pre-existing stash; PR #25 and #30. On main-based production checkout, Git may display the remaining research files under `?? research/`; do not remove them.

## Phase 3 — V2 visual redesign (2026-10-15)
V2 lives in `animation_v2/` (start with `V2_REPORT.md`). It is a white-canvas redesign with 37 new original assets, 9 scenes and audio-timed keyframes. The preview `Dr_Rehan_Heart_Warning_V2_PREVIEW.mp4` (45.5 s, with voice, original music and SFX) is NOT for publication. V1 in `animation/` is kept unchanged for comparison. Open approvals: the four uncertain ASR phrases, the presenter credit, clinician review, the ~42 s trim, and the music rights decision.
