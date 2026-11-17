# Machine A targeted cleanup — 2026-10-29 PKT

## Completed

Four `_work` spectrogram staging PNGs were removed after current SHA-256 comparison with their retained `02_VIDEO_FORENSICS/<video>/evidence/` equivalents. All four retained files also match the pinned PR #21 blob identities in `storage/YIOS-targeted-ssd-cleanup-20261029T0010PKT/CF_PR21_VERSION_CROSSWALK.csv`. No open handles or direct script references to those spectrogram paths were found. Exact path and hash for each deletion are appended to `OPERATIONS.jsonl` under `DELETE_EXACT_DUPLICATE_CF_WORK_SPECTRO`.

Immediate free bytes: 17,922,134,016 before; 17,925,103,616 after; observed delta 2,969,600 bytes (0.00297 GB). Deleted file allocation totaled 4,059,136 bytes (0.00406 GB). APFS/background activity explains why these differ; no larger net gain is claimed. No folder was moved or deleted. Earlier 2,528-file cleanup was not repeated.

## Protected and blocked

- `YIOS-local-audits/tooling/visual-ct-scan-venv` (372,924 KiB occupied): isolated Python 3.12.14 plus 12-package recreation/import test passed in preceding operation, but Video 002 `v1_scripts/negative_tests.py` hardcodes its interpreter and Video 003 checkpoint handoff names the same path. Protected writer has not released it. No deletion.
- `Downloads/CasuallyFinance-Forensic-Research/_work` (remaining frames, review sheets, visual_auto/whisper data): four exact duplicates removed; other content has no demonstrated exact retained replacement or independent byte-recreation proof. No broad deletion.
- `YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd/selected-evidence-packages-20261026/04063-editing-41-part02.tar.gz`: Batch 35 remote restoration/member exception unresolved. Keep.
- `workprojects/yio-cf-editing-forensics-local-evidence`: 38 Shorts source evidence, protected.
- `workprojects/video data of what if`: authoritative original assets, protected.
- `YIOS-local-audits/2026-10-21/local-only-commits.bundle`: historical Git recovery, protected.

## Repository and Finance

Canonical checkout remained at commit `f4dc5d14d6ad03c1edd92e48fac779e7a8555fc5`, branch `codex/casually-finance-knowledge-navigation`, with three pre-existing untracked paths and one stash untouched. Live GitHub navigation branch matches local HEAD. PR #21 is open at `043b85bf58f84fb6a1c8981d54e3b233faa6a928`; PR #36 is open draft at `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff`; PR #44 is open draft at `f345abdef43d54ebde98251cfa4fafb6403c52be`. No repository files changed or pushed in this cleanup: existing Casually Finance entry point, storyboard example and `docs/TWO_MAC_WORKFLOW.md` already cover the proposed navigation and handoff without duplication.

Live PR #36 `VIDEO_AUDIT_966.jsonl` was streamed from GitHub blob `7332e2dff987a9a295e9f0bc4d40c1aaab9d037e` (9,908,193 bytes; SHA-256 `d5542a51cddc1c309c1a5ad1e9b798ffc35f49a6f8302f73d83edadde9249458`). It contains 966 rows, including 455 rows with all six review statuses `COMPLETE_LIMITED_EVIDENCE`; `W-j0_v9cXuQ` remains `LEGACY_OR_PENDING`. The historical 1,612 total therefore retains 1,157 pending under this exact acceptance definition. Machine B remains sole Finance writer; no ledger files were changed. Hosted CI status was not tested in this pass.

## Next executable action

Protected writer must release the CT environment's exact path and approve a path-compatible bootstrap. Then rerun the pinned lock and Video 002 negative test in isolation; only after that delete the venv and measure actual free bytes. Continue other exact duplicate checks meanwhile, without touching active evidence.

## Cold-start retrieval check

An independent read-only test followed repository `README.md` to the Casually Finance `START_HERE.md`, pinned PR #21 DNA, per-video `0ll9rEtoRrs` beats/reconstruction and QA. It generated an original four-scene rate-comparison storyboard with narration, original asset prompts, sequential motion, evidence and limitations. Navigation worked. It did not produce a rendered video; original media portability and two absent Shorts remain unresolved.

## Targeted continuation — Batch 35 restore, no source deletion

Live safety: five-hour usage 21%, weekly 17%, credits balance 0 with reset credits unused; disk reserve above 5 GB. This pass deleted **0 source files** and moved **0 folders**. Initial `df` free estimate was 17,930,792,960 bytes; final filesystem free was 17,983,664,128 bytes. The 52,871,168-byte difference includes background/APFS activity and a temporary 9,633,731-byte restore created then removed, so **0 GB attributable SSD gain** is claimed.

CT environment remains blocked: Video 002 `negative_tests.py` hardcodes its interpreter path and writes `tables/negative_tests.json` to source; Video 003 handoff and agent brief reference the same environment. No protected-writer release was available. Prior isolated Python 3.12.14 / 12-package smoke test remains the only recreation result; no negative test was run in this pass.

Batch 35 object `1efw8RrwgFuAaYZfSU-GblnguyVJDLFuu` was independently downloaded. Its 9,633,731 bytes matched SHA-256 `e6ae283040952261508ee1002d0180ad17b54de453034ef1728026fdeafa144a`. Member streaming found 300 common members, one original-only `timeline02_readonly_snapshot.json` (SHA-256 `dde9cc0a6d7ca1f1d27341042621121df1cff3a191f2dc55352d045858f278c4`) and a different embedded recovery manifest. The original-only member is also exact in authoritative What If workprojects and historically mapped to Drive object `17kNzrpgyylWgpo3BV8839ZQNs19vx_2F`, but the original wrapper itself has no byte-identical independent restore. Keep the wrapper. Temporary remote restore was removed.

Existing `_work` hash inventory showed only four remaining 1,599-byte duplicate blank frames among 1,257 files; these are named frame evidence with no deletion/recovery proof. No meaningful eligible cache found. PR #21 remains open at `043b85bf58f84fb6a1c8981d54e3b233faa6a928`; PR #36 remains open draft at `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff`. Machine B continuation is in `MACHINE_B_FINANCE_CONTINUATION_2026-10-29.md`. No repo commit or push.
