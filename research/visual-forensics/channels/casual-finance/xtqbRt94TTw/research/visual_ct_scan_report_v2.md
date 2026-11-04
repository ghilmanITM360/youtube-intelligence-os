# Video006 visual forensics — integrated research, partial certification

Video: xtqbRt94TTw, “To Save the Economy... We’re About to Break It”, Casual Finance. Source SHA-256: `030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66`. The supplied ID/hash pair is the identity authority. Original MP4 remains unchanged in `/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/`. Evidence workspace: `/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan/`.

Status: **VISUAL_ANALYSIS_PARTIAL / AUDIO_NOT_VERIFIED / NOT_CT_COMPLETE**. Latest layer: checkpoint O / integrated_v4. All146 targeted items are adjudicated;165/199 ASR-qualified visual relations are reviewed,34pending. No actual listening or CT certification.

## Coverage and precision

MEASURED: 19,862 decoded video frames, 1920×1080, 24 fps, time base 1/12288, first PTS 0.0416667 s. Every saved per-frame PTS agrees with `(frame+1)/24` within the six-decimal recording tolerance; a fresh independent ffprobe decode counted the same 19,862 frames. Final frame PTS is 827.583333 s and its exclusive display end is 827.625 s. The audio stream starts at 0 and lasts 827.670522 s. Stream duration and absolute last display time are distinct.

All ten immutable first-pass reviewers have 766 candidate rows, 447 draft state rows and 339 dispute rows in aggregate. Independent ID/order/field/enum checks pass, including a tampered-verdict rejection. Actual historical image-return logs match all 1,552 required row paths. This establishes tool delivery, not universal native viewing or undivided attention. Stable images are 960×540; dispute thumbnails are 480×270; candidate sheets combine scaled fullframes with native bounding-box crops.

Independent gap review covered all 123 missing intervals/3,116 frames. Its 375 image returns comprise 180 scaled sheets and 195 native source-frame derivatives, individually matched by returned-image byte hash and multiplicity. The final targeted review adds 17 native source frames, 20 scaled state pairs, six mixed candidate sheets and six original-render checkpoints. Native source endpoints 0 and 19,861 were also actually viewed by the coordinator. Extraction files never count as viewed unless a successful image return exists.

The initial gap review used every fourth gap frame plus scene-cut neighbors and before/after context. That approximately 167 ms sample spacing is not a global 100 ms or all-frame visual review. Fifty-four initial gap segments have native boundary checks; 120 initially retain sampled precision. Subsequent targeted inspection adjudicated nine remaining owner-uncertain frames and corrected one additional edge frame. `integrated_v4/frame_partition_v4.csv` accounts for each frame exactly once with no missing/overlapping/unresolved owner. **Numerical continuity is not semantic or motion-onset certification.**

## Editing and significant recovered states

OBSERVED, independently checked at native adjacent frames where stated:

| Source frames | Visible event | Consequence for reconstruction |
|---|---|---|
| 226–300 | Four figures around a gray table; first speech bubble begins 262, replacement begins 279 | A missing composition, followed by internal text states; cannot extend the prior calendar state through it |
| 301 | Fed page and pointer narrator replace the table | The draft next state began one frame too late |
| 8412 / 8430 / 8492 / 8543 | Doors/meme; snap-open/logo reveal within retained layout; red title/shocked host; chart | Separate composition cuts from the internal door-state swap; no interpolated opening curve proved |
| 14340–14373; 14374 | “Way 1” running-character insertion, then DEBT visual | Recover the omitted insertion; the later visual starts at the last former gap frame |
| 18086 / 18563 / 18644 | Skyscraper addition / pointer presenter addition / third bag addition | Significant graphic states within larger compositions; native bbox pairs support onsets, not hard-cut claims |
| 19282; 19301 | First thin article-card sliver; later different card | Preserve entrance state and replacement; do not attach the whole transition to the eventual card |
| 19651; 19712 | Wide map/debt composition; end card | The gap contains a new shot and the first end-card frame |

The shard-3 discrepancy has a concrete explanation: S0065 requests a merge into S0064 while carrying its own prompt for speech/text/expression changes. Thirty merge flags therefore need not equal 29 duplicate prompts. Independent review supports one dominant layout with meaningful internal events. Conversely S0424 has a duplicated prompt but a distinct scene from its adjacent predecessor; prompt equality is not a visual merge rule.

MEASURED: all 339 disputed scene-detect frames lie inside their claimed source candidates. First-pass verdicts are 314 motion and 25 state changes. These are **not** 339 missing shot cuts. The provisional dispute-cut list is not the entire shot inventory. Whole-video shot counts, cuts/minute, median shot durations and novelty rates remain uncertified. Source candidate windows are measured detection windows, not automatically exact visual onsets.

## Art direction, illustration and information design

OBSERVED in the first-pass state evidence: a hand-drawn/whiteboard-like figure-and-prop system on a light field alternates with full-screen and composited documents, tables, web pages, logos, diagrams and inserted clips. The table insertion, map/rate-disc scenes, presenter/document combinations and late statistics table provide concrete examples. Media origin is appearance-based: the compressed output cannot establish the software, asset supplier, rig or AI model.

The figures use simplified silhouettes and facial/gesture replacements. Source positions and scale estimates are retained per state in `production_v1/per_state_production_spec_DRAFT_v1.csv`; they are estimates from source images, not calibrated geometry. The native first frame has a measured RGB(253,253,253) blank field; this is one frame measurement, not a universal palette token. Other color/type/line-width estimates in reviewer notes remain estimates.

OBSERVED: annotations and selections make specific source-table regions salient; S0393–S0396 preserve the statistics-table/red-mark/building progression, while S0406 preserves chart/presenter/number progression. Text transcriptions distinguish readable from unreadable content. Exact font identities, native layer separation, precise easing, lens parameters and original project settings are UNAVAILABLE. Financial numbers shown or transcribed remain source claims; this research does not independently validate their real-world truth.

INFERRED: retaining a diagram/document while adding one prop or mark may preserve orientation and focus explanation. A competing possibility is clutter or reading overload. This interpretation is not measured gaze, retention, CTR, emotion or creator intent. No artist/studio influence or numerical audience-performance claim is established.

## Motion, facial grammar and camera

The useful distinction is between composition replacement, additive graphics, expression/pose changes, apparent camera/viewer transformations and motion inside a retained layout. G065 demonstrates why a detector spike or pose swap is not automatically another shot. The native boundary evidence supports the visible snap at 8430, not an unseen smooth door-opening path. The original evidence sheets and motion descriptions retain start/end states; exact curves and object trajectories are not globally measured.

The three late graphic splits retain additive events even when composition groups merge. Red “41” starts at 18586 in native bbox evidence; completion of its draw and the chart's green trace remains sampled/unverified. At G088 the robot antenna is already visible at 13074: ownership is corrected, but true entrance onset is **at or before** that frame and has not been established. Use `integrated_v4/visual_event_ledger_v4.csv`, which separates content-window evidence from onset claims.

Facial/gesture observations exist per state and candidate; a complete normalized object lifecycle, blink/gaze trajectory and facial timing ledger has not been certified. Apparent document zoom/scroll is visible but underlying editor/camera implementation is non-identifiable. These domains stay PARTIAL rather than receiving invented mechanical detail.

## Narration, sound and visual relation

The locally installed cached Whisper-base model processed the decoded source audio into 199 tentative sentence segments (segment-union 820.52 s, envelope 0–820.76 s). `production_v1/asr_visual_overlap_v1.csv` records numerical intersections with visual intervals. It is neither semantic alignment nor word timing. The final 820.76–827.670522 interval is untranscribed, not certified silent.

**Actual listening: 0 seconds.** No qualified source-audio perception/listener receipt is available in the current harness. ASR cannot establish vocal stress, music, SFX, auditory pauses, intelligibility or audiovisual synchronization. Full AV sign-off remains blocked until actual qualified beginning-to-end hearing is recorded. No automatic sound or retention pass is awarded.

## Original production and reconstruction check

The 447-state draft index retains source observations and first-pass reconstruction proposals with provenance; it is not a production-approved prompt package. Duplicate proposals, source-like identities, missing motion/static-anchor detail and pending composition rulings require QA. A new production should use visibly different original assets, type, palette and script rather than reproducing the competitor's distinctive characters or branded copy.

A bounded timing transfer was actually rendered: 75 frames at 24 fps (3.125 s), new navy/coral geometric characters, cream field, fixed table/figures, no bubble at relative 0–35, “PLAN A” at 36–52, “PLAN B” at 53–74. Version 1's square-head/spec mismatch was recorded; version 2 corrects rounded heads. Automated decoded-frame, schedule and anchor checks pass. Six actual checkpoint images were independently reviewed; a separate stream probe confirms 75 frames/24 fps. The test is intentionally silent and local-only. It validates this original timing unit, not full-video cold-start reconstruction or source-audio synchronization.

## Remaining gates

All146 targeted items are now adjudicated:142 composition merges applied, three kept distinct and one same-layout recurrence kept noncontiguous; three within-composition graphic-state splits are retained. Two rejected/noncontiguous original merge flags are not silently forced. The resulting329 composition intervals are not a certified shot count. Raw reviewers and v1–v3 remain immutable.

ASR-qualified sampled relations cover165/199 segments:57DATA,52LITERAL,16METAPHOR,11HUMOR,2CONTRAST,5POTENTIAL_MISMATCH,22UNDETERMINED.34 exact pending IDs remain, startingASR156. New image-return audits confirm146+152 displays and four prior-image reuses; no listening. Potential source/ASR disagreements concern2.5%vs2.4%,10–14%,Earlier-stage wording, annual/monthly basis and sales/cash-flow denominator. They are questions for actual hearing/context, not automatic financial corrections. Out-of-interval representatives do not establish mismatch.

The full-field audit found missing motion objects for confirmedSUB101,SUB103,SUB104,SUB151; nullSUB107 is a no-change case. Original outputs are unchanged; the structured motion index exposes these gaps instead of inventing paths/easing. Three description-length exceptions are recorded separately. Native1:1 regions at1436/1437/1438/1441 show no confidently identifiable discrete feature forSUB032; actual pixel variation is measured, but semantic feature and codec cause remain unproven. Keep its uncertainty.

Further execution stops at the weekly reserve: reviewer new reads stopped at92%weekly, preserving validation/publication/lock-release headroom below95%. Exact next work is pending34ASR IDs, then source-aligned checks forundetermined relations and flagged numeric wording, four missing motion objects, SUB032 if further discriminating evidence is feasible, remaining native onset/object/facial/production QA, and actual qualified full-source listening. Current harness lacks qualified audio perception. No CT_SCAN_COMPLETE or full AV sign-off.

Raw media, derivative frames, audio and rendered videos are durable **LOCAL_ONLY** dependencies. Published hashes/manifests are not remote evidence availability. See `session_20261103/EXTERNAL_EVIDENCE_MANIFEST_checkpoint_N.json` and the external-media checksum inventory.
