# CASUAL FINANCE: NEW-AI START PROMPT (paste into a fresh session)

You are continuing the Casual Finance (CH001) visual-production work. You have no memory of earlier sessions; everything you need is in files.

Work from the root of an owner-approved checkout of `visual-audit/casual-finance`. Verify the branch and working state before editing. Follow repository writer coordination and get explicit authorization for commits, pushes and workspace changes. The [current status and media guide](CURRENT_STATUS_AND_MEDIA.md) identifies the accepted checkpoints, first-run commands and external inputs.

Read `CLAUDE.md` and `AGENTS.md` for repository and writer coordination rules. Then read the [knowledge index](CASUAL_FINANCE_VISUAL_INTELLIGENCE_INDEX.md), the [script-to-video playbook](CASUAL_FINANCE_SCRIPT_TO_VIDEO_PLAYBOOK.md) and the [master Visual DNA](CASUAL_FINANCE_MASTER_VISUAL_DNA.md). Use the [operational closure record](ADAPTIVE_VISUAL_RESEARCH/OPERATIONAL_ENGINEERING_CLOSURE.md) for the status of the scoped production path.

To make a new original video from a script:
- Ask for: the script, narration audio (or note none), format (long-form or Shorts), owner's evidence preferences.
- Follow the 19 steps in the playbook. Write the ten-question reasoning for each narration beat, use the scene-spec template, capture real evidence (screenshots, data files) with URL/date/sha256, and build highlight/ring/arrow layers.
- Reuse the existing renderer and asset pipeline (`productions/new-original-video-v1-rent-01/tools/`, `CHANNEL_VISUAL_AUDIT/CHANNEL_001/PRODUCTION_SYSTEM/`). The document-scene renderer now exists (`doc_scene.py`); extend it only if a real scene needs more (PDF pages, scrolling tables are untested).
- Codex makes character/prop artwork from prompts; you do research, storyboard, procedural graphics, rig integration, rendering, QA. Have a separate reviewer check the final file.
- BEFORE storyboard scenes are produced, build `claims.json` and `scenes.json` and pass `CHANNEL_VISUAL_AUDIT/CHANNEL_001/CLOSURE2/tools/claim_gate.py check` (exit 0). UNVERIFIED/MISLEADING/REJECTED claims block their scenes; keep qualifications; label hypotheticals; recompute arithmetic. The gate does not prove truth; read each cited source yourself.
- Before rendering, run `python3 productions/doc-animation-proof-01/build_proof.py --check` for the reference proof. Follow its [render contract](../../productions/doc-animation-proof-01/RENDER_CONTRACT.md) when wiring an episode entry point. Keep the claim register, resolved plan and reviewed source spec aligned. Use a new output directory for bounded checks.
- For real articles, charts or tables use `productions/new-original-video-v1-rent-01/tools/doc_scene.py` (see `doc_scene_schema.md`, example `productions/doc-animation-proof-01/`): original capture with SHA, document-local marks, onset frames set from the verified narration clause. There is NO default highlight delay (the old 4.8 s rule is retracted); sites such as BLS refuse automated capture, so ask the owner for a manual capture or redraw with attribution.
- Never fabricate sources, quotes or figures; never claim publication approval; human listening to any audio edit seam and the owner's final review are required before release.
- Do not copy the reference channel's artwork, characters, screenshots or third-party clips; use the method.
- After the production, append lessons to `CHANNEL_VISUAL_AUDIT/CHANNEL_001/PRODUCTION_LESSONS.md`.

Status of V1 Rent (do not rebuild): candidate files `productions/new-original-video-v1-rent-01/out_full/V1_RENT_FULL_R9_assembled.mp4` and `..._R9b_assembled.mp4`; open items (owner audio seam listening, wording choice, Zillow methodology page, publication approval) are in [the publication checklist](../../productions/new-original-video-v1-rent-01/R9_PUBLICATION_CHECKLIST.md) and [the R9b addendum](../../productions/new-original-video-v1-rent-01/R9B_ADDENDUM.md).

Resource rule: check five-hour and weekly usage and context before expensive work; near 90% five-hour or 95% weekly, stop after the current safe step and write a handoff with checksums.

## Adaptive visual research

Read the [master visual DNA](CASUAL_FINANCE_MASTER_VISUAL_DNA.md) and the [adaptive checkpoint](ADAPTIVE_VISUAL_RESEARCH/CONTINUATION_CHECKPOINT.md) for tested variations, scope and unresolved gates.

### First task in a fresh account

1. Read this file, the [index](CASUAL_FINANCE_VISUAL_INTELLIGENCE_INDEX.md), the [playbook](CASUAL_FINANCE_SCRIPT_TO_VIDEO_PLAYBOOK.md) and the [master visual DNA](CASUAL_FINANCE_MASTER_VISUAL_DNA.md) in that order. Use the index to open only the underlying modules needed for the script.
2. Ask what the viewer must understand at each beat. Return a clause-level claim register, sourced excerpt and rights manifest, storyboard with editable layers and animation timing, and an independent QA plan. Resolve unsupported factual lines before committing to visual emphasis. Reserve original assets and clearly labeled models for explanatory beats. Use the [three transfer cases](ADAPTIVE_VISUAL_RESEARCH/TRANSFER_STORYBOARDS_AND_REVIEW.md) as format examples.
3. Check the [scope and open gates](ADAPTIVE_VISUAL_RESEARCH/FINAL_RESEARCH_SUFFICIENCY_DECISION.md). Bind source and mark events to final narration, and independently compare actual render inputs with the claim register. Run the actual renderer preflight as well as the storyboard checks. The proof gate verifies the exact approved inputs. Keep research readiness, render approval and publication approval distinct.
