from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((R/'INPUT_MANIFEST.json').read_text());transfer=[]
for P in sorted(R.glob('0*')):
 for n in ['CASUALLY_FINANCE_VISUAL_SPEC.md','SHARED_CHARACTER_STYLE_GUIDE.md','MEDICAL_SOURCES.json','RESEARCH_REGISTER.json']:shutil.copyfile(R/n,P/n)
 source=next(m for m in manifest if m.get('package')==P.name)
 (P/'SOURCE_PROVENANCE.json').write_text(json.dumps(source,indent=2))
 files=[]
 for p in sorted((P/'source_audio').glob('*')):
  if p.suffix in ('.wav','.m4a'):
   row={'path_in_package':str(p.relative_to(P)),'absolute_local_path':str(p.resolve()),'sha256':sha(p),'bytes':p.stat().st_size,'git_included':False,'delivery_zip_included':True,'role':'Unchanged copied AAC' if p.suffix=='.m4a' else 'Decoded 24-bit PCM of original mixed audio'};files.append(row);transfer.append(dict(row,package=P.name))
 (P/'source_audio/AUDIO_TRANSFER_MANIFEST.json').write_text(json.dumps(files,indent=2))
 (P/'CHARACTER_BIBLE.md').write_text('# Character bible\n\nSee the included SHARED_CHARACTER_STYLE_GUIDE.md for identity/pose/contour rules. The actual delivered poses and layers are enumerated in assets/ASSET_REGISTER.json, not every theoretical combination. Each full SVG and matching PNG is local to this package. Parts preserve full-canvas registration; pivots are metadata, not automatic inverse-kinematics rigs. Sam is the running/HIIT participant; Nora is a fictional explainer; June is the swimming participant. No new pose is implicitly supplied.\n')
 (P/'CLAUDE_HANDOFF.md').write_text(f'''# {P.name} — Claude animation handoff

**Status: draft artwork built; QA_BLOCKED for publication.** Read qa/PUBLICATION_GATE.md and script/UNCERTAINTIES.json first. No final video has been generated.

1. Verify assets/FILE_HASHES.json and source_audio/AUDIO_TRANSFER_MANIFEST.json. Git excludes WAV/M4A; the local delivery ZIP includes both. If audio is absent, transfer the exact manifest file, do not synthesize narration. SOURCE_PROVENANCE.json identifies the original video. No competitor references are needed to assemble this package.
2. Review script/TRANSCRIPT_SMALL_EN.txt against original_audio.m4a continuously, especially the flagged clinical intervals. ASR.json and ASR_SMALL_EN.json are independent model runs of the SAME source, not independent evidence. WORDS_SMALL_EN.csv controls draft timing. DRAFT_ASR.srt is not publication-ready caption text. Clinical review must settle MEDICAL_CLAIMS.csv before any publishing decision.
3. Read storyboard/STORYBOARD.csv; use animation_plan/KEYFRAME_PLAN.json (1080×1920, 30fps, absolute frame indices, out exclusive). Audio remains at t=0, speed 1, pitch unchanged. Container duration and audio/video stream tails differ by milliseconds; do not shorten the supplied voice.
4. Import each full editable SVG or transparent PNG at its plan x/y/scale. assets/ASSET_REGISTER.json lists dimensions, pivots and separate component files. Parts stack in ascending z, on the SAME full asset canvas; do not crop/recenter individual pieces. Character pose swapping is supported; arbitrary bending requires additional rig work.
5. Keyframes are proposed reproducible methods, not reconstructed competitor project data. Hold prior values; easeOutCubic interpolates x/y/scale/opacity over the following segment. Draw objects in z order; hard-cut at scene boundaries. component_visibility overrides child visibility for staged work/recovery builds. fixed_text_layers sit above objects. White background. The scene SVGs include a small review footer and context label; keep these in review exports. Remove review footer only after signoffs, not by treating it as final viewer copy.
6. Compare start/mid/end scene_states and qa contact sheets. Stage one new explanatory object at a time. Do not fabricate diagnostic heart rhythms, risk percentages, efficacy scores, or dose prescriptions. Display ratings as speaker opinion. Proposed overlay copy is explicitly separate from ASR; it does not silently repair the unchanged audio.
7. Music/SFX: none supplied as isolated stems, none added. Background music presence is not listening-certified. Do not use destructive vocal separation or infer a clean voice stem. Any later music choice requires a licensed source and must remain below intelligible speech.

## Assembly limits
No video render, lip-sync, walk-cycle, physiological simulation, inverse-kinematics rig or human art-direction signoff is delivered. Poses/expressions and entrances are usable static building blocks. This is an original interpretation of the referenced visual grammar, not a claim of illustration parity. qa/VALIDATION.json verifies files/timing/source integrity, not clinical accuracy.

## Next concrete action
Listen end-to-end while reviewing UNCERTAINTIES.json, obtain clinical decisions for flagged claims, then retime entrance cues to the approved transcript and assemble a review animation. Preserve original audio and all provenance if a new narration version is approved.
''')
 (P/'RESUME_HERE.md').write_text(f'# Resume {P.name}\n\nStart with CLAUDE_HANDOFF.md. Artwork, storyboard, keyframes and source audio exist. Structural QA is recorded in qa/VALIDATION.json. Publication is blocked on human listening and clinical wording review; do not regenerate already delivered artwork simply because a transcript needs correction. Source files remain untouched.\n')
 (P/'qa/VISUAL_REVIEW.md').write_text('''# Static visual review — 2026-10-15

Author review, not independent human art direction. Inspected three hero moments and all end-state contact sheets at portrait/mobile scale. Supporting 12 reference sheets were viewed as a contact sheet; the supplied reference and inherited research establish visual grammar, not a pixel-match target.

- Typography: handwritten-style titles with readable short labels. Increased rating attribution from 23px to two 36px lines. Tiny source/review footer is production metadata, not substantive medical advice.
- Layout: simple white stage with separate character/explanatory prop, no generic dashboard cards. Running S01 rating originally overlapped tree; moved to x=650,y=550 and re-rendered. Full-scene output fits 1080×1920.
- Colour: authored teal/ochre/coral tokens; colours support labels and do not represent clinical measurement. Deliberately not claimed as measured competitor hex values.
- Illustration: original clothed figures; character proportions/faces remain consistent. Bent limbs join shoulders/hips; hands attached; swimming has two arms/two legs. Heart/joint/lungs are symbolic explanations, not anatomical training drawings. No copied character or reference raster is embedded.
- Copy: overlays are editorial proposals; uncertain clinical sentences remain in raw ASR and claims register. Score labels say speaker opinion. Clinical concerns remain an explicit publication blocker.

Remaining limits: no continuous motion review, no listened cue certification; swimming pose is a static stylized stroke, not coaching on technique. Scene state images are keyframe checkpoints, not final animation. Exact Casually Finance parity is not certified. Fuller character acting would require additional authored poses rather than repeated motion presets.

Result: static draft visually inspected; publication QA_BLOCKED. Structural checks have separate machine-verifiable results.
''')
(R/'AUDIO_TRANSFER_MANIFEST.json').write_text(json.dumps(transfer,indent=2))
(R/'MASTER_CLAUDE_HANDOFF.md').write_text('''# Three senior-health visual packages

**QA_BLOCKED — three draft illustration packages built, clinical and listening review still required.** No final video rendered. Branch: production/senior-health-casually-finance-three-videos. Issue #33.

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
''')
(R/'RESUME_HERE.md').write_text('''# Resume here

All three draft packages are built. Read MASTER_CLAUDE_HANDOFF.md and PRODUCTION_STATUS.json. Do not start over or expand YIOS scope. No final video was requested or produced.

Remaining external review: listen to original audio for all ASR uncertainty, resolve clinical claims with a qualified reviewer, then Claude may assemble an animation review using the existing assets and keyframes. The current status is QA_BLOCKED, not ready for publication. ZIP downloads and exact Git state are listed in delivery/final response; source audio is local-only in Git but included in delivery archives.

Source/reference originals were read-only. Canonical database untouched; unrelated finance-short-02-visual-calibration/ and research/ untracked files and stash preserved. Production branch starts from origin/main; research PRs were read by pinned ref without merging.
''')
print('Independent handoffs and transfer manifests written')
