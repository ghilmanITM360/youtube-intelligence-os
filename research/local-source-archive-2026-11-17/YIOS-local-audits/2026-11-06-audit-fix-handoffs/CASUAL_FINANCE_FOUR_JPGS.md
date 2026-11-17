# Casual Finance Video006: four JPGs still in the tree

Owner: the current Video006 writer. At 2026-11-06T15:30Z the `.vf_writer_lock` receipt names `codex-Video006-native-20261106`, run `01a1ad01-ac14-7990-9f0b-d9f2189b47ce`, pid 51841. Do not edit these files or take over this claim. No fix was made from this audit.

Branch `research/casually-finance-editing-forensics`, tip `f8665fee2465f015978fbd9cda6bfdc43409feb5`. Base path `research/visual-forensics/channels/casual-finance/xtqbRt94TTw/research/continuation_20261105_EP0002/`.

| Path under base | Bytes | SHA-256 | Introduced by |
|---|---:|---|---|
| `ep0015_native_batch/strip_336_338.jpg` | 59,861 | `15988b953842fef9595cf698fae424fc837af19c58273b0e7a4bf1863df635d5` | `a69a8a75` |
| `sub007_008_native_batch/strip_307-336_roi.jpg` | 192,754 | `27c47fce7f1878909e3c0e93622e43e20a0d48e87757c759239d1ec42c836497` | `9a1ab687` |
| `sub009_native_batch/overview_f377_half.jpg` | 61,720 | `a7abd88b07243a7d0acb10029d4c45ce916e6419637871b39eb965c554c452ce` | `5e497970` |
| `sub009_native_batch/strip_338-398_roi.jpg` | 327,874 | `4ac814872aecc6330eb575af7c48bd201374436a4dde2c3942c72082e8d7f7c8` | `5e497970` |

The guard already exists and must not be duplicated: `publication_preflight.py`, `publish_followup.py`, `MEDIA_DEFECT.json`, and `NEXT_AUTHORIZED_PUBLICATION.md` in `continuation_20261106_followup/`. It blocks new media. It tolerates these four as documented defects, so its pass does not mean the tree is clean.

## Steps for the claim holder
1. Keep a verified copy outside Git and record its SHA-256 and locator in the text manifest.
2. Remove the four files in a normal commit through `publish_followup.py`, then update `MEDIA_DEFECT.json` as that workflow requires.
3. Do not rewrite history or force push. The bytes stay in older commits, so report this as removed from the tree, not removed from Git.
