# Casually Finance current status and media guide

Read the [startup prompt](CASUAL_FINANCE_NEW_AI_START_PROMPT.md), [knowledge index](CASUAL_FINANCE_VISUAL_INTELLIGENCE_INDEX.md), [playbook](CASUAL_FINANCE_SCRIPT_TO_VIDEO_PLAYBOOK.md) and [master Visual DNA](CASUAL_FINANCE_MASTER_VISUAL_DNA.md) in that order. Their paths are relative to the checkout on `visual-audit/casual-finance`.

| Area | Authority |
|---|---|
| Original landscape finance videos | [Research sufficiency at 824229da](ADAPTIVE_VISUAL_RESEARCH/FINAL_RESEARCH_SUFFICIENCY_DECISION.md), [frozen rules](ADAPTIVE_VISUAL_RESEARCH/FINAL_RULE_FREEZE.md), [holdouts](ADAPTIVE_VISUAL_RESEARCH/HOLDOUT_VALIDATION_REPORT.md) |
| Actual render preflight | [Scoped acceptance at 52dcefd3](ADAPTIVE_VISUAL_RESEARCH/OPERATIONAL_ENGINEERING_CLOSURE.md), [render contract](../../productions/doc-animation-proof-01/RENDER_CONTRACT.md), [document schema](../../productions/new-original-video-v1-rent-01/tools/doc_scene_schema.md) |
| Original assets | [Asset prompts](PRODUCTION_SYSTEM/ASSET_PROMPTS_BATCH1_FOR_CODEX.md), [V1 rig handoff](../../productions/new-original-video-v1-rent-01/CODEX_HANDOFF_V2_LONGFORM_RIG.md), [photo composite recipes](ADAPTIVE_VISUAL_RESEARCH/B03_PHOTOGRAPHIC_MOTION_AND_VIDEO006.md) |
| Narration, export and publication | [Rent candidate checklist](../../productions/new-original-video-v1-rent-01/R9_PUBLICATION_CHECKLIST.md), [R9b addendum](../../productions/new-original-video-v1-rent-01/R9B_ADDENDUM.md) |

Long-form research is closed. The 53/100 score pertains to historical Shorts reconstruction. Shorts and sound design remain outside closure. The historical 4.8-second estimate measures label proximity and is retired as a timing rule. Use the [document event observations](CLOSURE2/EVIDENCE_FORENSICS_2026-11-22.md) and align annotation to the relevant reviewed narration clause. Earlier missing-renderer and pending-payload verdicts predate the scoped engineering fix. Candidate artwork failures are historical QA examples. For new assets use the current playbook and test the actual rig. Episode source verification, rights, phone legibility, final speech, audio and publication authorization remain separate gates.

## External inputs

Use [the local media registry](../../docs/LOCAL_MEDIA_AVAILABILITY.md), an authorized durable media root and SHA-256 verification. First-run planning uses the documents and structured evidence without reference media.

| Material | Find or reproduce |
|---|---|
| 216 physical reference MP4s | [Corpus classification](ADAPTIVE_VISUAL_RESEARCH/FULL_CORPUS_VISUAL_CLASSIFICATION.csv) records filenames, public IDs where known, formats and hashes. Copy from the authorized media owner and verify the exact hash. Unmatched copies or public transcodes may have different frame indices. |
| Deep scans and adaptive frames | [Legacy integration receipts](ADAPTIVE_VISUAL_RESEARCH/LEGACY_RESEARCH_INTEGRATION_REGISTER.csv) locate historical inputs. [Frame checksum register](ADAPTIVE_VISUAL_RESEARCH/CONTINUATION_MEDIA.sha256) and [batch ledger](ADAPTIVE_VISUAL_RESEARCH/ADAPTIVE_RESEARCH_BATCH_LEDGER.csv) locate adaptive measurements. Use the identified source, timestamp and frame index to reproduce a selected frame. |
| R9b production candidate | Owner-held `productions/new-original-video-v1-rent-01/out_full/V1_RENT_FULL_R9b_assembled.mp4`, SHA-256 `5a2529d4b176c05890122a709bb88466c0a8196ad01ded703d3f15c4b71c3ce0`. See [other preserved outputs](PRESERVED_OUTSIDE_GIT.md). |
| Original silent proof | `productions/doc-animation-proof-01/out/DOC_PROOF_60s.mp4`, SHA-256 `98ff35eaae3460258235654ea04782065023bc63ad24f6dcba87b7c6a7af7f04`. The local historical branch already contains this artifact. See the [publication manifest](GITHUB_PUBLICATION_MANIFEST.md) for the clean-history delivery and [folder map](COMPLETE_FOLDER_AND_FILE_MAP.md) for file dispositions. Generate bounded review stills from the approved capture and plan using the render contract. A new capture requires renewed source and crop review and new approval digests. |

First obtain the reviewed capture from the authorized evidence owner. Place it at `productions/doc-animation-proof-01/evidence/originals/cfpb_compound_interest_full.png` and verify SHA-256 `f841bfb44691dba445e4e4d95c204813eee83ac9a3e3f9d190306a53e3a0e282`. A fresh capture from the official source linked in the document spec requires renewed review and new approval digests. Keep the capture outside commits.

From the repository root, in a Python environment with Pillow and NumPy, run:

```sh
python3 productions/doc-animation-proof-01/build_proof.py --check
python3 -m unittest discover -s CHANNEL_VISUAL_AUDIT/CHANNEL_001/CLOSURE2/tests -q
```

The scoped build authorizes one reviewed document capture and a fixed operation set. FFmpeg is required for MP4 export. New operations, multiple document captures, additional renderer entry points and final speech need their own review bindings and regression tests. The validator enforces reviewed input identity. Reviewers establish factual truth and source suitability.
