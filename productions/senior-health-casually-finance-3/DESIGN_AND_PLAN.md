# Senior-health illustration production plan

Goal: three independent, original Casually Finance-informed asset and keyframe packages for Claude, using the entire unchanged supplied narration. No final video.

Spec: owner-supplied production brief; adopted by the owner on 2026-10-15 with delegated design decisions and no further questions.

Design: 1080×1920 portrait, 30 fps; warm black imperfect contours, sparse white stages, original clothed older adults and a silver-haired female explainer. Selective teal/ochre/coral, expressions and acting, progressive diagrams. Exact reference techniques are evidence; character design, palette, pivots and easing are original proposals. Editable SVG groups and transparent PNGs, source-timed scene states and explicit keyframe tracks.

Architecture: files only, isolated production branch from origin/main. Existing research read from pinned Git refs without merging. All changes limited to this production directory. Local-only references/audio excluded from Git with hashed transfer paths. Single agent.

## Execution
- [x] Inspect Git, quota, inputs and existing research; hash ZIP and all supplied videos; safe manifest and lossless audio extraction.
- [x] Machine transcribe each full audio with word timing; inspect source frames and uncertainty; record exact clinical claims and limitations.
- [x] Synthesize referenced visual rules and original style guide; produce full narration-led storyboard before artwork.
- [x] For each video: create three hero scenes; inspect character, explanation and hook at mobile scale; build required remaining layers and states; write keyframe plans.
- [x] Validate every referenced asset, timing coverage, SVG/PNG, IDs, source integrity and counts. Record visual QA honestly.
- [x] Commit each package; draft issue/PR; verify remote SHA and exact-head checks; produce independent Claude handoffs.

## Review focus
Beginning/end speech truncation; ordinal scores presented as medical evidence; unsupported clinical absolutes; intact character joints and independently addressable layers; transfer manifest actually matching local audio and source files.

## Decisions
User instruction to proceed overrides skill approval pauses. This is artifact production, not a new software subsystem. No canonical ingestion/database writes; use hash-first reference manifest principles only. No subagents. Medical accuracy can block publication while the unchanged-narration visual package remains available for review. Human listening cannot be claimed from ASR alone.

## Review ledger
- Four supplied sources hashed and unchanged; two ASR passes kept distinct from human verification.
- Twenty clinical claim records written; critical uncertainties prevent publication readiness.
- All 22 draft scenes and three checkpoints per scene exist; no final animation.
- Static hero/all-scene review found rating/tree overlap, corrected and inspected after re-render. Rating attribution enlarged.
- Sequential interval child reveals added to keyframe plan; scene labels exported independently.
- Focused validator passes source hashes, decoded PCM equality, frame/word coverage, assets/parts, transparency, XML and canvas bounds. Full unrelated repository suite was not run for artifact-only additions.
- Self-review only: explicit single-agent production brief overrides reviewer delegation. No independent art/clinical/listening signoff claimed.
- Ruling: keep packages available as review drafts with QA_BLOCKED rather than silently rewriting uncertain speech. Cost: final publication needs human decisions.
