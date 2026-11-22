# Render-facing claim gate engineering handoff

Status CLOSED for the document-proof build. This file records the original acceptance specification. See [operational closure](OPERATIONAL_ENGINEERING_CLOSURE.md) for actual test results and scope.

## Enforcement contract

Construct the resolved render input in memory, then validate that same object before asset preparation, frame generation or FFmpeg. Walk every rendered scene, overlay, title, label, crop, mark and voice cue that can express a factual payload. Require an approved claim ID and source binding for factual items, and an explicit illustrative role plus visible persistent qualification for fictional values. Unknown payload kind fails closed. Allow explicit non-factual assets such as an unlabelled generic prop. A structured source/excerpt ID binds capture hash, appendix/page, bounding region and publisher with the approved claim. An annotation's claim must match the document excerpt it marks. Reject inconsistent aliases, mismatched render values, units, date windows, denominators or versions where those are encoded. Require actual print or spoken qualifiers on the planned interval and verify printed cues stay legible throughout; spoken cues require an independently verified final narration artifact before publication. A check against a planned narration file alone certifies only the plan.

Freeze or hash the approved resolved payload and render from it. Avoid resolving mutable copy, asset paths or claim data again after validation. Every failure names scene, field path, claim ID and rejection reason. Sidecar verification can keep checking storyboard completeness; an extra or omitted render-facing record still requires an independent binding. For image-only claims, verify immutable asset hashes and require a signed-off reviewer record for image content, crop and context. Structural checks cannot verify whether a source statement is true or whether a quote is fair.

## Real-entry regression cases

Use the normal proof command with fixtures and temporary output paths, suppress expensive output after preflight where a positive path needs a test seam. Assert invalid cases exit nonzero, identify the actual failing field, and leave no frame/output artifacts.

| Case | Expected behavior |
|---|---|
| Rejected rendered annotation absent from storyboard | Reject the actual annotation claim |
| Unknown actual annotation ID | Reject before any render output |
| Approved claim wired to a different capture or marked excerpt | Reject source or locator mismatch |
| Required qualifier appears in sidecar but disappears from actual display or linked voice | Reject missing qualifier on actual cue |
| Hypothetical number appears in an unlabelled factual overlay | Reject role and qualifier mismatch |
| Render duration/denominator/period differs from verified normalized fields | Reject the conflicting render fields |
| Actual quote changes accepted excerpt text or highlights a different excerpt | Reject exact excerpt/binding mismatch and require independent contextual review |
| One approved claim is reused to certify two incompatible sides of a comparison | Reject field or operand mismatch. Require human review of compatibility and implications. |
| Valid full proof fixture | Contract passes and the resolved payload reaching the renderer is byte-equivalent to the accepted object |
| Legacy claim-free scene | Continues to render when declared non-factual, with arbitrary factual display strings excluded from that declaration |

Keep the historic proof binary and Rent outputs as evidence. Bounded frame verification of the resolved path is sufficient for this patch. Full-cost production follows only after owner authorization and independent final file QA.
