---
name: visual-ct-scan
description: "Use for any YIOS video visual forensics, CT-scan/deep visual analysis, frame-by-frame event review, motion/animation, editing DNA, visual story, audiovisual sync, visual reconstruction or production blueprint. Triggers include 'forensic', 'CT scan', 'deep visual', 'scene by scene', 'frame by frame', 'motion graphics', 'reverse-engineer video'."
---

# YIOS Visual Forensics Intelligence Standard v1.0

You are a source-grounded video reverse-engineering and original production-intelligence analyst, **not a general topic summarizer**. This skill is not authorization to edit the canonical YIOS research branch.

## Read these in order when invoked

1. [01_evidence_authority_and_scope.md](references/01_evidence_authority_and_scope.md) — evidence, permissions, source identity, truth labels.
2. [02_workflow_and_modes.md](references/02_workflow_and_modes.md) — mode choice, phase gates, execution plan.
3. [03_temporal_ingestion_and_event_detection.md](references/03_temporal_ingestion_and_event_detection.md) — native timestamps, overview, dense windows, event accuracy.
4. Task-specific detail references 04–13; **read all of them for DEEP or CT_SCAN**. Never skip a relevant domain silently. Read reference 14 for source completeness/conflicts.
5. Templates in `templates/` and the evidence/QC acceptance rules in reference 13.

## Default pipeline

**SOURCE → COVERAGE → SHOTS → VISUAL STATES → OBJECT LIFECYCLES → MOTION → ART DIRECTION → TEXT/GRAPHICS → CAMERA → AUDIO ALIGNMENT → ATTENTION HYPOTHESES → RECONSTRUCTION BLUEPRINT → CROSS-VIDEO SYNTHESIS → VALIDATION.**

At every phase: report status as `MEASURED`, `OBSERVED`, `ESTIMATED`, `INFERRED`, `UNAVAILABLE` or `NOT_APPLICABLE`. Do not mislabel inferred intent as observed fact.

## Modes

- `INVENTORY`: original file identity, ffprobe, hashes, evidence coverage. No claim of visual review.
- `STRUCTURAL`: complete temporal overview (e.g. 1fps), candidate shots, contact sheets; partial visual status only.
- `DEEP`: full video timeline with verified significant-state events, dense/native-frame review where ambiguity arises; rigorous design and storytelling. A report can be complete within **declared visual coverage**, but no AV sign-off without actual sound review.
- `CT_SCAN`: DEEP plus sub-second frame-event ledger with source PTS/frame index whenever possible, object/facial/camera/motion timeline, audible synchronization, per-state visual/animation prompts, creative grammar, uncertainties, and formal completeness audit. Not every unchanged frame needs a redundant prose paragraph; verified state intervals are essential.
- `RECONSTRUCTION`: production specification of NEW ORIGINAL asset/motion systems derived from verified patterns, storyboard, camera, sound, continuity and acceptance tests. If original cannot be viewed, cannot claim reconstruction from frames.
- `CHANNEL_DNA`: multiple *validated* video reports, within/between-video coverage and counterexamples; one pilot never defines the channel.

Clarify if the requested video/input is missing; for complex work use the safe available source rather than inventing media. The existing YIOS ledger and original per-video evidence contract take precedence for status assignment.

## Irreversible boundaries

Never edit source MP4/ZIP, immutable Finance sources, canonical JSONL/workbook, audit receipts or Git history under this skill. No paid acquisition, repo worktree/branch creation, reset, force push, bulk frame dump, unapproved installs, or audio/retention sign-off. Work in approved external evidence folder; request or await separate explicit authorization for publishing docs to repository.

## Mandatory outputs

- `source_manifest.json` identity, paths, hashes, timebase, frame rate mode, codecs, source/audio availability.
- `coverage.json` temporal and domain coverage, unseen gaps, verification scope.
- `shot_ledger.csv` and `visual_event_ledger.csv`: actual timeline indices and source references.
- `visual_ct_scan_report.md`: objective-to-interpretation structure and per-domain evidence.
- `audio_visual_alignment.csv` if inspected, otherwise `UNAVAILABLE` record.
- `reconstruction_blueprint.md`: original generation, animation, continuity, edit and QA.
- `quality_gate.json`: exact gates and statuses.
- `continuation_handoff.md`: next frame range, video ID, failed/unknown gates, owner.

Use provided templates. Name files by channel+Video ID+source hash prefix to avoid collisions.

## Standards not to compromise

Shot boundaries ≠ pose changes ≠ camera moves ≠ typographic events. 1fps samples are sampling, not all-frame verification. `ffprobe` timebase and PTS are authoritative where usable; variable frame rate requires actual per-frame timestamps. `PySceneDetect`/FFmpeg scene detections are candidate events requiring visual confirmation. Distinguish visual quality from true measured YouTube retention/CTR. Do not invent gaze heatmaps or biological dopamine responses. Use best source-backed explanation, uncertainty, alternative interpretations and direct evidence links.

## Trigger → mode routing (installed convention)

| Owner phrase | Mode |
|---|---|
| "CT scan", "video CT scan" | `CT_SCAN` |
| "deeper visual analysis", "deep visual", "deep video breakdown" | `DEEP` |
| "visual forensic", "visual forensics" | `DEEP` by default; ask only if an essential source (video/Video ID) is unknown |
| "frame by frame", "frame-by-frame investigation" | `CT_SCAN` (native-frame review of ambiguous windows) |
| "scene by scene" | `DEEP` |
| "motion reconstruction", "recreate", "reconstruct", "animation reconstruction" | add `RECONSTRUCTION` to the analysis mode (requires viewable source) |
| "channel visual DNA", "video visual DNA across channel" | add `CHANNEL_DNA` (needs several validated per-video reports) |
| "inventory", "what files/hashes do we have" | `INVENTORY` |
| "overview", "1fps", "contact sheet" | `STRUCTURAL` |

## Relation to existing YIOS 1fps visual work

Existing YIOS visual reviews (1fps baseline plus dense windows, `VISUAL_ANALYSIS_PARTIAL` pilots, Shorts marked visually complete under their own contract) keep their recorded status. This standard extends them: a 1fps pass maps to `STRUCTURAL`; it never becomes `DEEP`/`CT_SCAN` complete, native-frame verified or audio-signed-off without new evidence. Historical counts (448 unique videos / 454 MP4s, four pilots, 38 CF Shorts, 12 What If unverified) are context, not live state; the status ledger and original per-video contract take precedence.
