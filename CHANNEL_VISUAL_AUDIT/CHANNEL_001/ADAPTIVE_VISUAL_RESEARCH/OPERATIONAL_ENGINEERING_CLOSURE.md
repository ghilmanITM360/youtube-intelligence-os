# Final engineering closure

**Long-form visual research and scoped production engineering are closed.** Research was accepted at `824229da3abbfadf36a1d68de44c352b552ace4e`. Engineering acceptance covers the actual silent document-proof entry point and its approved operation set. Publication requires episode-specific approval.

## Implemented

- `productions/doc-animation-proof-01/build_proof.py` reads the separate storyboard, claim register, resolved plan and document spec. It validates them before building any beats, opening FFmpeg or creating a render-output directory. The renderer receives the already-validated argument values and a private copy of the exact approved capture bytes.
- `CLOSURE2/tools/claim_gate.py` adds the actual-payload validator. Stable digests bind exact render fields to reviewer-approved claim and source revisions. Every actual claim reference is checked, including document annotations. The gate checks passage against the referenced source and exact locator, binds document geometry and clip context, binds the printed compounding qualification, and requires hypothetical labels from scene entry. Comparison text and geometry are validated together. The older standalone storyboard CLI keeps its existing meaning.
- `render_plan.json` moves existing scene delivery out of independent Python text/geometry construction. `claims.json` records the independent review bindings. The three hypothetical labels now start at the scene cut and remain through their scenes. The two existing test files that used machine-specific absolute paths now locate their test assets relative to the repository. A new test file exercises the real entry point.
- The four production entry files now point to the [render contract](../../../productions/doc-animation-proof-01/RENDER_CONTRACT.md), which records dependencies, commands and the review process. The original independent delta report remains historical.

## Regression record

Executed `python3 -m unittest discover -s CHANNEL_VISUAL_AUDIT/CHANNEL_001/CLOSURE2/tests -q` in the worktree environment. **60 passed**, including 43 existing tests and 17 real-entry cases. The legacy backend reported an unclosed read-handle warning while importing the rig anchors. The warning did not change the test results.

| Acceptance case | Actual result |
|---|---|
| Rejected C4 omitted from storyboard, unknown annotation ID or unverified rendered C4 | Refused on the actual annotation path |
| Replaced capture even with its new hash entered in the document spec | Refused against the separately approved source |
| Alternate mark location or changed quotation | Refused against exact geometry/passages |
| Missing qualification from actual context or planned speech, despite original storyboard | Refused |
| Unlabelled hypothetical, wrong unit, period or denominator | Refused on actual fields |
| Changed comparison bar or substitution of one already-approved displayed operand for the other | Refused |
| Claim-free opening with newly injected assertion | Refused |
| Unmodified `--check` and actual bounded render | Authorized. Eight decoded 1920 × 1080 stills cover all six beats, including the legacy claim-free opening |
| Exact backend delivery | Through the entry point, the test compared canonical bytes for all backend operations with the validated plan and checked the unchanged spec. It replaced the original source after preflight and verified the document backend still received the approved capture bytes |

All 15 negative cases ran in rendering mode, exited nonzero before producing an output directory and identified the affected field. The bounded still times were 2, 8.6, 21, 30.5, 35, 45.8, 51 and 58 seconds. The original 60-second file and the V1 Rent R9b output were checked before and after. Their SHA-256s stayed `98ff35eaae3460258235654ea04782065023bc63ad24f6dcba87b7c6a7af7f04` and `5a2529d4b176c05890122a709bb88466c0a8196ad01ded703d3f15c4b71c3ce0`. Work stayed on `visual-audit/casual-finance` under the owner's scoped engineering authorization. The active V1 write-claim file and existing unrelated working-tree changes were excluded.

## Remaining episode checks

This is structural validation of a separately reviewed release input. Independently verify source meaning, claim accuracy, arithmetic, comparability, context and rights. A reviewer must compare any new crop to the original evidence. Check mark placement, table headers and qualifiers, audience-scale readability and timing against final speech. Bind actual audio if it carries factual claims, perform a human listen and review the final decoded export before approval. The current proof adapter handles a single document capture and its supported operation set. Other render entry points, new document formats and final voice assets need their own binding and regression checks. Shorts and sound design remain outside the research closure.
