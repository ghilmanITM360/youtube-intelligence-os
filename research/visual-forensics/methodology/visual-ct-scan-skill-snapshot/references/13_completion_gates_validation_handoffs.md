# 13 — Evidence contract, data schemas, validation and continuation

## Source identity gate

- Channel ID and exact Video ID verified against registry/manifests.
- Source MP4 stable SHA256, bytes, duration, stream metadata.
- Duplicate copies detected, external source unchanged.
- Local context: repository branch/HEAD recorded; media need not exist in Git.

## Temporal gate

- Entire video from beginning to end covered by documented strategy.
- Candidate shots manually verified; no stepped zoom falsely counted as a cut.
- Every **meaningful** visual state captured with boundaries at original PTS/frame precision when warranted; initial 1fps overview alone fails this gate.
- Identified dense/native-frame verification around fleeting captions, gestures, transitions, visual trickery; explicit unseen gaps and resolution floor.
- Shot cuts, internal state events, camera movement, graphic state, facial and object motion have separate taxonomy.

## Creative and reconstruction gate

- Applicable art/illustration/color/type/cinematography, motion, design/story, emotional/attention hypotheses recorded with source timestamps and labels.
- Actual object continuity, on-screen text and counterexamples checked.
- Image-generation and image-to-video reconstruction prompts for each important **distinct state**, preserving continuity, camera/motion/static anchors, labels, original asset identity.
- Practical editor/production timeline blueprint and QA; original, non-infringing recommendations.
- Scorecards and improvement options explicitly evidence-based and optional.

## Audio gate

- Human/qualified listener actually listened to the source sound from beginning to end before `FULL_AV_SIGNOFF_COMPLETE`.
- ASR without hearing is clearly `ASR_UNCERTIFIED`; listening gate stays pending.
- Timestamp alignment method and confidence recorded; do not fabricate audio beats or wording.

## Reporting exact status

Use the established YIOS ledger status semantics and receipts, never let this generic kit overwrite existing canonical progress. Mark `STRUCTURAL_ANALYSIS_COMPLETE` for sampled structure; `VISUAL_ANALYSIS_PARTIAL` for evidence gaps; `VISUAL_ANALYSIS_COMPLETE` only under real existing per-video contract, with no unintended implication of sound. `FULL_AV_SIGNOFF_COMPLETE` only with verified audio+video. Mark prior unverified claims `HISTORICAL_UNVERIFIED` rather than completed.

## Validation artifacts

`source_manifest.json`: `video_id`, `channel`, `source_path`, `source_sha256`, bytes, media stream/PTS, extraction versions, Git SHA, reader.
`coverage.json`: precise modes/time ranges/verified native frames, intervals and blind spots, audio/visual status, limitations.
`shot_ledger.csv`: shot id, start/end PTS, frame index, transition class, verification.
`visual_event_ledger.csv`: object/state id, event class, start/end PTS, before/after, evidence refs, confidence.
`audio_visual_alignment.csv`: exact phrase, audio source/method, timestamps if measured, corresponding visual and lag, note ASR status.
`reconstruction_blueprint.md`: asset/illustration prompts, motion, editable scene graph, continuity rules and acceptance.
`quality_gate.json`: gate-by-gate `PASS/PARTIAL/BLOCKED/NOT_APPLICABLE`, evidence locators, reviewer.
`continuation_handoff.md`: Video ID, source sha, next frame/interval, exact pending work, existing tools, git ownership, machine.

## Resource gate and no-data-loss policy

At five-hour usage ≥90% used or weekly ≥95% used or serious context warning, stop new expensive runs, finish current safe atomic work, preserve source hashes and validated external output, do not force-complete any partial video. Use current actual indicators, never guess. With low disk avoid bulk duplicate frames or source copies. No destructive Git commands. For ZIP ZIP containing the source prompts, don't silently overwrite repository `CLAUDE.md`, `AGENTS.md` or original YIOS receipts.

## Acceptance tests

1. Verify markdown reference links and nonempty modules/templates.
2. Verify all four attached source prompts are copied BYTE-IDENTICALLY with SHA256.
3. Confirm trigger text in SKILL.md and entry link under project root if authorized.
4. Validate sample per-video deliverables schema and report status.
5. Test invocation on existing 4-pilot partial status using only previously archived evidence, not by silently rerunning analysis.
6. Confirm no canonical JSONL/Excel/source media mutations or branch stomping.
7. If and only if explicitly authorized and ownership safe, stage specific skill/docs and normal-push. Otherwise external patch/handoff, not a false success.
